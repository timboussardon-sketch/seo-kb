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

def clean_body(raw: str) -> str:
    """Texte de la brève en clair : sans la ligne Sources, sans markdown."""
    body = re.split(r'\n\*Sources\s*:', raw)[0]
    body = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', body)
    body = body.replace('**', '').replace('*', '')
    return re.sub(r'\s+', ' ', body).strip()

def parse_edition(path: Path):
    """Retourne [(position, titre, body, url, source)] pour une édition."""
    text = path.read_text(encoding='utf-8')
    out = []
    for m in re.finditer(r'\*\*(\d+)\.\s+(.+?)\*\*(.*?)(?=\n---|\Z)', text, re.S):
        pos = int(m.group(1))
        title = re.sub(r'\s+', ' ', m.group(2)).strip()
        src = re.search(r'\*Sources\s*:\s*\[([^\]]+)\]\((https?://[^)]+)\)', m.group(3))
        if not src:
            continue
        out.append((pos, title, clean_body(m.group(3)), src.group(2), src.group(1)))
    return out

def main():
    backfill = int(sys.argv[sys.argv.index('--backfill') + 1]) if '--backfill' in sys.argv else 1
    force = '--force' in sys.argv
    key = service_key()
    done = {r['edition'] for r in rest('GET', '/breves_wall?select=edition', key)}
    editions = sorted(p for p in BREVES_DIR.glob('*-breves*.md'))[-backfill:]
    total = 0
    for path in editions:
        edition = path.stem
        if edition in done and not force:
            continue
        date = re.match(r'(\d{4}-\d{2}-\d{2})', edition).group(1)
        items = parse_edition(path)
        if not items:
            print(f'{edition} : aucune brève parsée, on saute')
            continue
        rows = [
            {'edition': edition, 'edition_date': date, 'position': pos, 'line': title, 'body': body, 'url': url, 'source': source}
            for (pos, title, body, url, source) in items
        ]
        rest('POST', '/breves_wall?on_conflict=edition,position', key, rows)
        print(f'{edition} : {len(rows)} lignes publiées')
        total += len(rows)
    print(f'OK · {total} lignes ajoutées au wall')

if __name__ == '__main__':
    main()
