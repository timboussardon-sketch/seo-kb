#!/usr/bin/env python3
"""Archive les brouillons versionnés (-v2, -v3...) de agent-synthetic/revuedepressIA :
seule la version la plus haute de chaque édition reste visible et indexée."""
import pathlib, re, collections, subprocess, sys
ROOT = pathlib.Path('/Users/timothee/Code/seo-kb')
base = ROOT / 'agent-synthetic/revuedepressIA'
groups = collections.defaultdict(list)
for f in list(base.glob('*.md')) + list((base / 'breves-IA').glob('*.md')):
    m = re.match(r'^(.*?)(?:-v(\d+))?$', f.stem)
    groups[(f.parent, m.group(1))].append((int(m.group(2) or 1), f))
moved = 0
for (parent, stem), versions in groups.items():
    if len(versions) > 1:
        versions.sort()
        arch = parent / '_archive'
        arch.mkdir(exist_ok=True)
        for _, f in versions[:-1]:
            f.rename(arch / f.name); moved += 1
print(f"{moved} brouillons archivés")
if moved:
    subprocess.run(['git', '-C', str(ROOT), 'add', 'agent-synthetic/'], check=True)
    subprocess.run(['git', '-C', str(ROOT), 'commit', '-m', 'Purge auto des brouillons versionnés (hebdo)'], check=True)
    subprocess.run(['git', '-C', str(ROOT), 'pull', '--rebase', '--autostash', 'origin', 'main'])
    subprocess.run(['git', '-C', str(ROOT), 'push', 'origin', 'main'])
