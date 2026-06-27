#!/usr/bin/env python3
"""Publie les éditions MediaSEO sur le wall d'actualités d'organikk.co.

Successeur de breves-wall.py, adapté au format et au dossier MediaSEO :
- dossier : agent-synthetic/MediaSEO/{date}-MediaSEO.md
- format  : sujets en `## Titre  `🟢 Confirmé``, corps, `*Sources : [..](..)*`
  (au lieu des anciennes brèves numérotées `**N. Titre**`).

Réutilise la même table Supabase `breves_wall` (colonnes edition / edition_date /
position / line / body / url / source) et la même logique « un fichier canonique
par date » que breves-wall.py. Pendant la transition, MediaSEO écrase le jour en
place (on_conflict=edition_date,position).

Lancé par launchd ou à la main :
    python3 .claude/scripts/mediaseo-wall.py [--backfill N] [--force]
"""
import json
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
MEDIA_DIR = VAULT / 'agent-synthetic' / 'MediaSEO'
SUPABASE_URL = 'https://fwhfnzbtlddzfxbsejyf.supabase.co'
PROJECT_REF = 'fwhfnzbtlddzfxbsejyf'


def service_key() -> str:
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
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read().decode()
                return json.loads(raw) if raw else None
        except Exception:
            if attempt == 3:
                raise
            time.sleep(3 * (attempt + 1))


def clean_body(raw: str) -> str:
    """Corps en clair : faits + Limites, sans la ligne Sources, sans markdown."""
    body = re.split(r'\n\*\*Sources?\.\*\*|\n\*Sources?\s*:', raw)[0]
    body = re.sub(r'`[^`]*`', '', body)                 # tags `🟢 Confirmé` éventuels
    body = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', body)  # liens markdown
    body = body.replace('**', '').replace('*', '')
    return re.sub(r'\s+', ' ', body).strip()


def strip_title(raw: str) -> str:
    """Titre sans le tag de fiabilité ni markdown."""
    t = re.sub(r'`[^`]*`\s*$', '', raw)          # `🟢 Confirmé` en fin de titre
    t = t.replace('**', '').replace('*', '')
    return re.sub(r'\s+', ' ', t).strip()


def parse_edition(path: Path):
    """Retourne [(position, titre, body, url, source)] pour une édition MediaSEO.

    Chaque sujet est une section `## ...` contenant une ligne `*Sources : [..](..)*`.
    Les blocs sans source (titre H1, fil du jour, note de fiabilité) sont ignorés.
    """
    text = path.read_text(encoding='utf-8')
    out = []
    pos = 0
    for m in re.finditer(r'(?m)^##\s+(.+?)\s*$\n(.*?)(?=\n##\s|\Z)', text, re.S):
        title = strip_title(m.group(1))
        if 'réseaux sociaux' in title.lower():  # section interne (propositions), pas pour le wall
            continue
        block = m.group(2)
        # ligne Sources / Source : « **Sources.** Nom — url » OU « *Sources : [nom](url) »
        srcline = (re.search(r'(?im)^\*\*Sources?\.\*\*\s*(.+)$', block)
                   or re.search(r'(?im)\*Sources?\s*:\s*(.+)$', block))
        if not srcline:
            continue
        line = srcline.group(1)
        url_m = re.search(r'https?://[^\s)]+', line)
        if not url_m:
            continue
        url = url_m.group(0)
        name_md = re.search(r'\[([^\]]+)\]', line)
        if name_md:
            source = name_md.group(1)
        else:
            source = re.split(r'\s+[—–-]\s+', line.strip())[0]
            source = re.sub(r'[*`]+', '', source).strip()
        pos += 1
        out.append((pos, title, clean_body(block), url, source))
    return out


def canonical_by_date():
    """Un seul fichier par jour : le plus complet (plus de sujets), puis le plus récent."""
    best = {}
    for path in MEDIA_DIR.glob('*-MediaSEO*.md'):
        m = re.match(r'(\d{4}-\d{2}-\d{2})', path.stem)
        if not m:
            continue
        date = m.group(1)
        score = (len(parse_edition(path)), path.stat().st_mtime)
        if date not in best or score > best[date][0]:
            best[date] = (score, path)
    return {d: p for d, (s, p) in best.items()}


def main():
    backfill = int(sys.argv[sys.argv.index('--backfill') + 1]) if '--backfill' in sys.argv else 1
    force = '--force' in sys.argv
    key = service_key()
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
            print(f'{edition} : aucun sujet parsé, on saute')
            continue
        rows = [
            {'edition': edition, 'edition_date': date, 'position': pos,
             'line': title, 'body': body, 'url': url, 'source': source}
            for (pos, title, body, url, source) in items
        ]
        rest('POST', '/breves_wall?on_conflict=edition_date,position', key, rows)
        print(f'{edition} : {len(rows)} sujets publiés ({date})')
        total += len(rows)
    print(f'OK · {total} lignes ajoutées au wall')


if __name__ == '__main__':
    main()
