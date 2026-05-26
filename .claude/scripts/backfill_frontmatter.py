"""Audit et backfill du frontmatter pour raw/.

- Audit : liste les fichiers de raw/ sans frontmatter ou avec un schéma incomplet.
- Backfill (--apply) : génère un frontmatter inféré (type, source_type, created, title)
  et l'ajoute en tête du fichier. Affiche un diff par défaut (dry-run).

Inférence :
- type=source (raw/ = sources par définition)
- source_type via le sous-dossier (papers→paper, transcripts→transcript, articles→article,
  notes→doctrine, data→gsc-export, etudes-seo→paper, bootcamp4→transcript)
- created depuis le préfixe YYYY-MM-DD du filename si présent, sinon mtime du fichier
- title depuis le premier H1, sinon dérivé du slug
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

from _common import VAULT_ROOT, parse_frontmatter

RAW_DIR = VAULT_ROOT / "raw"

DATE_PREFIX_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)

SOURCE_TYPE_BY_SUBDIR = {
    "papers": "paper",
    "etudes-seo": "paper",
    "transcripts": "transcript",
    "bootcamp4": "transcript",
    "articles": "article",
    "revue-de-presse": "article",
    "auteurs": "article",
    "notes": "doctrine",
    "journal": "doctrine",
    "ia-employe": "doctrine",
    "acquisition": "doctrine",
    "todo": "doctrine",
    "scoring": "doctrine",
    "data": "gsc-export",
    "cas-clients": "client-note",
    "fusionn": "client-note",
    "agents": "doctrine",
}


def infer_source_type(path: Path) -> str:
    rel = path.relative_to(RAW_DIR).parts
    if not rel:
        return "doctrine"
    top = rel[0]
    return SOURCE_TYPE_BY_SUBDIR.get(top, "doctrine")


def infer_created(path: Path) -> str:
    m = DATE_PREFIX_RE.match(path.stem)
    if m:
        return m.group(1)
    mtime = path.stat().st_mtime
    return date.fromtimestamp(mtime).isoformat()


def infer_title(body: str, path: Path) -> str:
    m = H1_RE.search(body)
    if m:
        return m.group(1).strip()
    return path.stem.replace("-", " ").replace("_", " ")


def build_frontmatter(path: Path, body: str) -> str:
    title = infer_title(body, path).replace('"', '\\"')
    return (
        "---\n"
        "type: source\n"
        f"source_type: {infer_source_type(path)}\n"
        f'title: "{title}"\n'
        "aliases: []\n"
        "tags: []\n"
        f"created: {infer_created(path)}\n"
        f"updated: {infer_created(path)}\n"
        "sources: 0\n"
        "confidence: medium\n"
        "status: draft\n"
        "---\n\n"
    )


def find_missing(verbose: bool = False) -> list[Path]:
    missing = []
    for path in RAW_DIR.rglob("*.md"):
        if ".git" in path.parts or "revue-de-presse" in path.relative_to(RAW_DIR).parts[:1]:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, _ = parse_frontmatter(text)
        if not fm:
            missing.append(path)
            if verbose:
                print(f"  [MISSING] {path.relative_to(VAULT_ROOT)}")
    return missing


def show_diff(path: Path, new_fm: str) -> None:
    rel = path.relative_to(VAULT_ROOT)
    print(f"\n=== {rel} ===")
    for line in new_fm.rstrip("\n").splitlines():
        print(f"+ {line}")


def apply_backfill(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(text)
    if fm:
        return
    new_fm = build_frontmatter(path, text)
    path.write_text(new_fm + text.lstrip(), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Audit / backfill du frontmatter raw/")
    ap.add_argument("--apply", action="store_true",
                    help="Écrire les frontmatters (sinon dry-run avec diff)")
    ap.add_argument("--audit", action="store_true",
                    help="Lister les fichiers manquants et sortir")
    args = ap.parse_args()

    missing = find_missing(verbose=args.audit)
    print(f"\n{len(missing)} fichier(s) raw/ sans frontmatter")

    if args.audit or not missing:
        return 0

    if not args.apply:
        print("\n--- DRY-RUN ---\n")
        for path in missing:
            text = path.read_text(encoding="utf-8", errors="replace")
            new_fm = build_frontmatter(path, text)
            show_diff(path, new_fm)
        print(f"\n[dry-run] Re-lance avec --apply pour écrire.")
        return 0

    for path in missing:
        apply_backfill(path)
        print(f"  [WRITTEN] {path.relative_to(VAULT_ROOT)}")
    print(f"\n{len(missing)} fichier(s) backfillé(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
