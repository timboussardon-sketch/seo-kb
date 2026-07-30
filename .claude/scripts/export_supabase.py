"""Export d'un sous-ensemble PUBLIC du vault vers Supabase pgvector (table kb_chunks).

Alimente le chatbot kb-chat des dashboards (bootcamp / accompagnement).
L'embedding se fait côté serveur (edge function kb-ingest, clé Gemini sur Supabase) :
ce script n'envoie que du texte.

CONFIDENTIALITÉ (règle dure) : on n'exporte JAMAIS raw/, ni les dossiers/fichiers
client ou internes. Filtre en trois couches :
  1. wiki/ uniquement.
  2. denylist de dossiers internes/client + registres système racine.
  3. par fichier : noms de clients/prospects, type de source client, frontmatter confidential.

Config attendue dans ~/.config/seo-kb/kb-export.env :
  SUPABASE_FN_URL=https://<ref>.supabase.co/functions/v1
  SUPABASE_ANON_KEY=...
  KB_ADMIN_SECRET=...

Usage : python3 .claude/scripts/export_supabase.py [--dry-run]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import VAULT_ROOT, iter_markdown, read_markdown, slug_from_path  # noqa: E402
from embed_vault import chunk_markdown, stringify  # noqa: E402

CONFIG = Path.home() / ".config" / "seo-kb" / "kb-export.env"
BATCH = 40

# Couche 2 : dossiers wiki/ jamais exportés (data client ou interne système).
DENY_DIRS = {
    "wiki/sources",       # transcripts de calls prospects, snapshots produit
    "wiki/audit",         # audits internes du vault
    "wiki/revue-hebdo",   # rituel interne
    "wiki/propositions",  # templates de propale avec exemples client
    "wiki/preuves",       # perf client mesurée
    "wiki/agents",        # config interne
    "wiki/moc",           # MOC = navigation du vault de Tim, wikilinks non portables hors Obsidian
    "wiki/decisions",     # ADR internes (schéma vault, LaunchAgents, infra perso)
    "wiki/ops",           # health-checks des automatisations perso de Tim
    "wiki/revues-presse", # éditions de la newsletter perso Algorithme
    "wiki/posts-linkedin",# drafts LinkedIn perso de Tim
    "wiki/queries",       # questions ad-hoc, souvent sur le business Organikk lui-même
    "wiki/methodes",      # fiches méthode des automatisations perso (SyntheticBrain, etc.)
}
# Registres système à la racine de wiki/.
DENY_ROOT = {
    "wiki/index.md", "wiki/log.md", "wiki/hypotheses.md",
    "wiki/contradictions.md", "wiki/ingest-backlog.md",
    "wiki/dashboard.md",  # stats auto-générées du vault perso de Tim
}
# Couche 3 : noms de CLIENTS / PROSPECTS (pas les produits de Tim).
CLIENT_RE = re.compile(
    r"\b(leexi|fg.?formation|golfiller|alexia)\b", re.IGNORECASE
)
CALL_RE = re.compile(r"call-\d+", re.IGNORECASE)
DENY_SOURCE_TYPES = {"client-note", "transcript", "gsc-export"}
# Types méta-vault : décrivent le SYSTÈME de Tim (navigation, décisions, méthode), pas la doctrine SEO.
DENY_TYPES = {"moc", "decision", "register", "methode"}
# Fiches de personnes (prospects, clients, participants) reconnues par leurs tags.
DENY_TAGS = {"prospect", "client", "personne"}
TITLE_PERSON_RE = re.compile(r"\((?:prospect|client|bo[iî]te)\b", re.IGNORECASE)
BODY_CLIENT_RE = re.compile(
    r"entreprise cliente|client[e]?/prospect|prospect r[ée]f[ée]renc|bo[iî]te de\b",
    re.IGNORECASE,
)


def _tagset(fm: dict) -> set[str]:
    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",")]
    return {str(t).strip().lower() for t in tags}


def load_config() -> dict[str, str]:
    if not CONFIG.exists():
        sys.exit(f"Config manquante : {CONFIG}")
    cfg = {}
    for line in CONFIG.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        cfg[k.strip()] = v.strip()
    for req in ("SUPABASE_FN_URL", "SUPABASE_ANON_KEY", "KB_ADMIN_SECRET"):
        if not cfg.get(req):
            sys.exit(f"Config : {req} manquant dans {CONFIG}")
    return cfg


def excluded(rel: str, fm: dict, body: str) -> str | None:
    """Retourne la raison d'exclusion, ou None si le fichier passe."""
    if not rel.startswith("wiki/"):
        return "hors wiki/"
    if rel in DENY_ROOT:
        return "registre système"
    for d in DENY_DIRS:
        if rel == d or rel.startswith(d + "/"):
            return f"dossier interne ({d})"
    if stringify(fm.get("type")) in DENY_TYPES:
        return f"type={fm.get('type')} (méta-vault, non portable)"
    if stringify(fm.get("source_type")) in DENY_SOURCE_TYPES:
        return f"source_type={fm.get('source_type')}"
    if str(fm.get("confidential")).lower() in ("true", "1", "yes", "oui"):
        return "frontmatter confidential"
    if _tagset(fm) & DENY_TAGS:
        return "fiche personne (tag prospect/client)"
    if TITLE_PERSON_RE.search(str(fm.get("title") or "")):
        return "fiche personne (titre)"
    if BODY_CLIENT_RE.search(body):
        return "entreprise client/prospect (texte)"
    if CALL_RE.search(rel):
        return "transcript de call"
    if CLIENT_RE.search(rel) or CLIENT_RE.search(body):
        return "mention client/prospect"
    return None


def collect() -> tuple[list[dict], list[tuple[str, str]]]:
    kept: list[dict] = []
    dropped: list[tuple[str, str]] = []
    for path in iter_markdown():
        rel = path.relative_to(VAULT_ROOT).as_posix()
        fm, body = read_markdown(path)
        reason = excluded(rel, fm, body)
        if reason:
            if rel.startswith("wiki/"):
                dropped.append((rel, reason))
            continue
        title = fm.get("title") or slug_from_path(path)
        for i, (section, text) in enumerate(chunk_markdown(body, str(title))):
            kept.append({
                "id": hashlib.sha1(f"{rel}::{i}".encode()).hexdigest(),
                "path": rel,
                "section": section,
                "title": str(title),
                "type": stringify(fm.get("type")),
                "tags": stringify(fm.get("tags")),
                "content": text,
            })
    return kept, dropped


def post_batch(cfg: dict, chunks: list[dict], reset: bool) -> dict:
    payload = {"secret": cfg["KB_ADMIN_SECRET"], "reset": reset, "chunks": chunks}
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(payload, f)
        tmp = f.name
    try:
        out = subprocess.run(
            ["curl", "-s", "--retry", "4", "--retry-all-errors", "--max-time", "200",
             "-X", "POST", f"{cfg['SUPABASE_FN_URL']}/kb-ingest",
             "-H", "Content-Type: application/json",
             "-H", f"apikey: {cfg['SUPABASE_ANON_KEY']}",
             "-H", f"Authorization: Bearer {cfg['SUPABASE_ANON_KEY']}",
             "--data", f"@{tmp}"],
            capture_output=True, text=True, timeout=300,
        )
    finally:
        os.unlink(tmp)
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return {"error": out.stdout[:300] or out.stderr[:300]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="liste sans envoyer")
    args = ap.parse_args()

    chunks, dropped = collect()
    files = sorted({c["path"] for c in chunks})
    print(f"Fichiers wiki/ exportés : {len(files)}  |  chunks : {len(chunks)}")
    print(f"Fichiers wiki/ exclus   : {len(dropped)}")
    if args.dry_run:
        print("\n-- exportés --")
        for f in files:
            print("  +", f)
        print("\n-- exclus (raison) --")
        for rel, reason in sorted(dropped):
            print(f"  - {rel}  [{reason}]")
        return 0

    cfg = load_config()
    total = 0
    for i in range(0, len(chunks), BATCH):
        batch = chunks[i:i + BATCH]
        res = post_batch(cfg, batch, reset=(i == 0))
        if "error" in res:
            sys.exit(f"Échec batch {i}: {res['error']}")
        total += res.get("inserted", 0)
        print(f"  upserted {total}/{len(chunks)}")
    print(f"\nOK. {total} chunks dans kb_chunks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
