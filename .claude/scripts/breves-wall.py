#!/usr/bin/env python3
"""Publie les brèves IA sur le wall d'actualités d'organikk.co.

Pipeline : parse les éditions de agent-synthetic/revuedepressIA/breves-IA/,
condense chaque brève en UNE ligne (via `claude -p`, couvert par l'abonnement),
et upsert dans la table Supabase `breves_wall` (projet Fusionn). La page
/actualites d'organikk lit cette table côté navigateur : aucune build Netlify.

Lancé par launchd (com.tim.breves-wall) après l'auto-pull de midi, ou à la main :
    python3 .claude/scripts/breves-wall.py [--backfill N]
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
MAX_LINE = 120

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

def parse_edition(path: Path):
    """Retourne [(position, titre, url, source)] pour une édition."""
    text = path.read_text(encoding='utf-8')
    out = []
    for m in re.finditer(r'\*\*(\d+)\.\s+(.+?)\*\*(.*?)(?=\n---|\Z)', text, re.S):
        pos = int(m.group(1))
        title = re.sub(r'\s+', ' ', m.group(2)).strip()
        src = re.search(r'\*Sources\s*:\s*\[([^\]]+)\]\((https?://[^)]+)\)', m.group(3))
        if not src:
            continue
        out.append((pos, title, src.group(2), src.group(1)))
    return out

def condense(titles: list[str]) -> list[str]:
    """Une ligne ultra courte par titre, via claude -p. Fallback : troncature."""
    numbered = '\n'.join(f'{i+1}. {t}' for i, t in enumerate(titles))
    prompt = (
        "Condense chacune de ces brèves search/IA en UNE ligne de "
        f"{MAX_LINE} caractères maximum, factuelle, en français, qui garde l'acteur, "
        "le fait et le chiffre clé s'il y en a un. Aucun chiffre inventé, aucun tiret cadratin. "
        "Réponds UNIQUEMENT avec un tableau JSON de chaînes, dans le même ordre, sans rien d'autre.\n\n"
        + numbered
    )
    try:
        out = subprocess.run(['claude', '-p', prompt], capture_output=True, text=True, timeout=300).stdout.strip()
        out = re.sub(r'^```(json)?|```$', '', out, flags=re.M).strip()
        lines = json.loads(out)
        if isinstance(lines, list) and len(lines) == len(titles):
            return [str(l)[:MAX_LINE + 20] for l in lines]
    except Exception as e:
        print(f'  condensation claude -p en échec ({e}), fallback troncature', file=sys.stderr)
    return [t[:MAX_LINE].rsplit(' ', 1)[0] + '…' if len(t) > MAX_LINE else t for t in titles]

def main():
    backfill = int(sys.argv[sys.argv.index('--backfill') + 1]) if '--backfill' in sys.argv else 1
    key = service_key()
    done = {r['edition'] for r in rest('GET', '/breves_wall?select=edition', key)}
    editions = sorted(p for p in BREVES_DIR.glob('*-breves*.md'))[-backfill:]
    total = 0
    for path in editions:
        edition = path.stem
        if edition in done:
            continue
        date = re.match(r'(\d{4}-\d{2}-\d{2})', edition).group(1)
        items = parse_edition(path)
        if not items:
            print(f'{edition} : aucune brève parsée, on saute')
            continue
        lines = condense([t for _, t, _, _ in items])
        rows = [
            {'edition': edition, 'edition_date': date, 'position': pos, 'line': line, 'url': url, 'source': source}
            for (pos, _, url, source), line in zip(items, lines)
        ]
        rest('POST', '/breves_wall?on_conflict=edition,position', key, rows)
        print(f'{edition} : {len(rows)} lignes publiées')
        total += len(rows)
    print(f'OK · {total} lignes ajoutées au wall')

if __name__ == '__main__':
    main()
