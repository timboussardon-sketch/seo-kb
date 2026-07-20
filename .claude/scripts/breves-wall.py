#!/usr/bin/env python3
"""Publie les brèves IA sur le wall d'actualités d'organikk.co.

Pipeline : parse les éditions de agent-synthetic/revuedepressIA/breves-IA/ et
upsert dans la table Supabase `breves_wall` (projet Fusionn). Les brèves passent
VERBATIM : le titre et le corps sont exactement ceux de l'édition Obsidian,
aucune réécriture (règle de Tim, 2026-06-12). La page /actualites d'organikk
lit cette table côté navigateur : aucune build Netlify.

Lancé par launchd (com.tim.breves-wall) après l'auto-pull de midi, ou à la main :
    python3 .claude/scripts/breves-wall.py [--backfill N] [--force]
    (--force : republie aussi les éditions déjà présentes, p.ex. après un
     changement de format)
"""
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
BREVES_DIR = VAULT / 'agent-synthetic' / 'revuedepressIA' / 'breves-IA'
SUPABASE_URL = 'https://fwhfnzbtlddzfxbsejyf.supabase.co'
PROJECT_REF = 'fwhfnzbtlddzfxbsejyf'

def service_key() -> str:
    import time
    for attempt in range(4):
        out = subprocess.run(
            ['supabase', 'projects', 'api-keys', '--project-ref', PROJECT_REF, '-o', 'json'],
            capture_output=True, text=True, timeout=60,
        ).stdout
        try:
            for k in json.loads(out):
                if k.get('description') and 'service' in k['description']:
                    return k['api_key']
        except json.JSONDecodeError:
            pass
        time.sleep(3 * (attempt + 1))
    raise SystemExit('clé service_role introuvable (CLI supabase muette après 4 essais)')

def rest(method: str, path: str, key: str, body=None):
    req = urllib.request.Request(
        f'{SUPABASE_URL}/rest/v1{path}',
        method=method,
        headers={
            'apikey': key, 'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json', 'Prefer': 'resolution=merge-duplicates',
        },
        data=json.dumps(body).encode() if body is not None else None,
    )
    import time
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read().decode()
                return json.loads(raw) if raw else None
        except Exception:
            if attempt == 3:
                raise
            time.sleep(3 * (attempt + 1))

PASTILLE = '🟢🟡🟠🔵'

def strip_badges(text: str) -> str:
    """Retire les badges de fiabilité, garde les identifiants techniques.

    Les backticks portent soit un badge (`🟢 Confirmé`), soit un identifiant
    technique (`Google-GeminiNotebook`, `robots.txt`). Tout supprimer amputait
    les brèves de leurs noms propres. Seul un span à pastille est un badge."""
    text = re.sub(rf'`[^`]*[{PASTILLE}][^`]*`\s*(?:—|-)?\s*', '', text)
    return re.sub(r'`([^`]*)`', r'\1', text)

def clean_body(raw: str) -> str:
    """Texte de la brève en clair : sans la ligne Sources, sans badge, sans markdown."""
    # « Sources : » (édition longue) ou « Source : » (bloc stat du jour, singulier)
    body = re.split(r'\*Sources?\s*:', raw)[0]
    body = strip_badges(body)
    body = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', body)
    body = body.replace('**', '').replace('*', '')
    return re.sub(r'\s+', ' ', body).strip()

def source_of(chunk: str):
    """(url, nom) de la source d'une brève. Priorité à la ligne Sources ; à
    défaut le premier lien du chunk (format 3 blocs : `🟢` — *[SEJ](url)*)."""
    m = re.search(r'\*Sources?\s*:\s*\[([^\]]+)\]\((https?://[^)]+)\)', chunk)
    if not m:
        m2 = re.search(r'\[([^\]]+)\]\((https?://[^)]+)\)', chunk)
        if not m2:
            return None
        return m2.group(2), re.sub(r'\s+', ' ', m2.group(1)).strip()
    return m.group(2), re.sub(r'\s+', ' ', m.group(1)).strip()

def parse_legacy(text: str):
    """Format historique (jusqu'au 2026-06-29) : titre en `**N. Titre**`."""
    out = []
    for m in re.finditer(r'\*\*(\d+)\.\s+(.+?)\*\*(.*?)(?=\n---|\Z)', text, re.S):
        src = source_of(m.group(3))
        if not src:
            continue
        title = re.sub(r'\s+', ' ', m.group(2)).strip()
        out.append((int(m.group(1)), title, clean_body(m.group(3)), src[0], src[1]))
    return out

def parse_headings(text: str):
    """Variante ancienne : titre en `### N. Titre` (ex. 2026-06-03)."""
    out = []
    for m in re.finditer(r'^###\s+(\d+)\.\s+(.+?)$(.*?)(?=^###\s|^##\s|\Z)', text, re.S | re.M):
        src = source_of(m.group(3))
        if not src:
            continue
        title = re.sub(r'\s+', ' ', m.group(2)).strip()
        out.append((int(m.group(1)), title, clean_body(m.group(3)), src[0], src[1]))
    return out

def parse_3blocs(text: str):
    """Format 3 blocs (décision Tim, 2026-07-14) : `## 01 · L'info du jour`,
    `## 02 · La stat du jour`, `## 03 · Les autres infos en bref`.

    Positions : 1 = info du jour, 2 = stat du jour, 3+ = les brèves numérotées.
    Le titre en gras ouvre la phrase dans le bloc 03, donc le body garde le
    titre : l'amputer produirait un texte qui commence au milieu d'une phrase."""
    out = []
    blocs = {}
    for m in re.finditer(r'^##\s*0?(\d+)\s*·\s*(.+?)$(.*?)(?=^##\s|\Z)', text, re.S | re.M):
        blocs[int(m.group(1))] = m.group(3)
    if not blocs:
        return []

    if 1 in blocs:
        chunk = blocs[1]
        t = re.search(r'\*\*(.+?)\*\*', chunk, re.S)
        src = source_of(chunk)
        if t and src:
            title = re.sub(r'\s+', ' ', t.group(1)).strip()
            body = clean_body(re.split(r'\*\*.+?\*\*', chunk, maxsplit=1, flags=re.S)[-1])
            out.append((1, title, body, src[0], src[1]))

    if 2 in blocs:
        chunk = blocs[2]
        src = source_of(chunk)
        body = clean_body(chunk)
        if src and body:
            # pas de titre dédié dans ce bloc : la première phrase fait le titre
            title = re.split(r'(?<=[.!?])\s+', body)[0].strip()
            out.append((2, title, body, src[0], src[1]))

    if 3 in blocs:
        items = re.finditer(
            r'^(\d+)\.\s+\*\*(.+?)\*\*(.*?)(?=^\d+\.\s+\*\*|\Z)',
            blocs[3], re.S | re.M,
        )
        for m in items:
            src = source_of(m.group(3))
            if not src:
                continue
            title = re.sub(r'\s+', ' ', m.group(2)).strip()
            body = clean_body(f'**{m.group(2)}**{m.group(3)}')
            out.append((int(m.group(1)) + 2, title, body, src[0], src[1]))
    return out

def parse_edition(path: Path):
    """Retourne [(position, titre, body, url, source)] pour une édition.

    Trois formats coexistent dans breves-IA/ : on tente le 3 blocs, puis le
    legacy, puis les titres en `###`. Réparer l'un en cassant l'autre
    republierait un historique vide."""
    text = path.read_text(encoding='utf-8')
    return parse_3blocs(text) or parse_legacy(text) or parse_headings(text)

def canonical_by_date():
    """Un seul fichier par jour : le plus complet (plus de brèves), puis le plus
    récent. La table a DEUX contraintes uniques — (edition, position) ET
    (edition_date, position) — donc deux fichiers du même jour aux mêmes
    positions (ex. -breves / -v2 / -v3) se télescopent en 409. On ne publie
    donc qu'une édition canonique par date."""
    best = {}
    for path in BREVES_DIR.glob('*-breves*.md'):
        m = re.match(r'(\d{4}-\d{2}-\d{2})', path.stem)
        if not m:
            continue
        date = m.group(1)
        n = len(parse_edition(path))
        score = (n, path.stat().st_mtime)
        if date not in best or score > best[date][0]:
            best[date] = (score, path)
    return {d: p for d, (s, p) in best.items()}

def dry_run(backfill: int):
    """Contrôle du parsing sans réseau ni clé : ce qui SERAIT publié."""
    canon = canonical_by_date()
    for date in sorted(canon)[-backfill:]:
        path = canon[date]
        items = parse_edition(path)
        flag = '' if items else '   ← AUCUNE BRÈVE PARSÉE'
        print(f'\n{date}  ({path.name})  {len(items)} brèves{flag}')
        for pos, title, body, url, source in items:
            print(f'  {pos}. {title[:90]}')
            print(f'     {source} · {url[:80]}')
            print(f'     {body[:120]}…')

def main():
    backfill = int(sys.argv[sys.argv.index('--backfill') + 1]) if '--backfill' in sys.argv else 1
    force = '--force' in sys.argv
    if '--dry-run' in sys.argv:
        dry_run(backfill)
        return
    key = service_key()
    # « déjà publié » se juge par DATE, pas par nom de fichier : si le fichier
    # canonique d'un jour change (v2 -> v3), republier sous un nouveau stem
    # violerait la contrainte (edition_date, position). On verrouille par date.
    done = {r['edition_date'] for r in rest('GET', '/breves_wall?select=edition_date', key)}
    canon = canonical_by_date()
    dates = sorted(canon)[-backfill:]
    total = 0
    for date in dates:
        if date in done and not force:
            continue
        path = canon[date]
        edition = path.stem
        items = parse_edition(path)
        if not items:
            print(f'{edition} : aucune brève parsée, on saute')
            continue
        rows = [
            {'edition': edition, 'edition_date': date, 'position': pos, 'line': title, 'body': body, 'url': url, 'source': source}
            for (pos, title, body, url, source) in items
        ]
        # arbitre (edition_date, position) : un re-run --force met à jour le jour
        # en place même si le fichier canonique a changé de nom.
        rest('POST', '/breves_wall?on_conflict=edition_date,position', key, rows)
        print(f'{edition} : {len(rows)} lignes publiées ({date})')
        total += len(rows)
    print(f'OK · {total} lignes ajoutées au wall')

if __name__ == '__main__':
    main()
