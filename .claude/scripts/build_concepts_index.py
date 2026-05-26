"""Construit concepts.json — index inversé des concepts et entités du vault.

Pour chaque fichier de wiki/concepts/ et wiki/entities/, on stocke :
- métadonnées (type, title, aliases, tags, status, confidence)
- outlinks : [[wikilinks]] sortants du fichier
- backrefs : chemins de tous les fichiers du vault qui linkent vers ce concept

Output : .claude/index/concepts.json
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

from _common import (
    INDEX_DIR,
    VAULT_ROOT,
    extract_wikilinks,
    iter_markdown,
    read_markdown,
    slug_from_path,
)

INDEXED_DIRS = ["wiki/concepts", "wiki/entities"]


def collect_indexed_nodes() -> dict[str, dict]:
    """Index concepts + entities — la 'colonne vertébrale' du graphe."""
    nodes: dict[str, dict] = {}
    for sub in INDEXED_DIRS:
        for path in (VAULT_ROOT / sub).glob("*.md"):
            fm, body = read_markdown(path)
            slug = slug_from_path(path)
            nodes[slug] = {
                "type": fm.get("type", "unknown"),
                "title": fm.get("title", slug),
                "aliases": fm.get("aliases", []) or [],
                "tags": fm.get("tags", []) or [],
                "status": fm.get("status"),
                "confidence": fm.get("confidence"),
                "file": path.relative_to(VAULT_ROOT).as_posix(),
                "outlinks": extract_wikilinks(body),
                "backrefs": [],
            }
    return nodes


def add_backrefs(nodes: dict[str, dict]) -> None:
    """Scan le vault entier, peuple node.backrefs."""
    alias_to_slug: dict[str, str] = {}
    for slug, node in nodes.items():
        alias_to_slug[slug] = slug
        for alias in node["aliases"]:
            alias_to_slug.setdefault(alias, slug)

    backrefs: dict[str, set[str]] = defaultdict(set)
    for path in iter_markdown():
        _, body = read_markdown(path)
        links = extract_wikilinks(body)
        if not links:
            continue
        src = path.relative_to(VAULT_ROOT).as_posix()
        for link in links:
            target_slug = alias_to_slug.get(link)
            if target_slug and target_slug != slug_from_path(path):
                backrefs[target_slug].add(src)

    for slug, refs in backrefs.items():
        nodes[slug]["backrefs"] = sorted(refs)


def main() -> int:
    nodes = collect_indexed_nodes()
    add_backrefs(nodes)

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    output = INDEX_DIR / "concepts.json"
    output.write_text(
        json.dumps(nodes, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    n_concepts = sum(1 for n in nodes.values() if n["type"] == "concept")
    n_entities = sum(1 for n in nodes.values() if n["type"] == "entity")
    n_with_backrefs = sum(1 for n in nodes.values() if n["backrefs"])
    print(f"concepts.json built: {len(nodes)} nodes "
          f"({n_concepts} concepts, {n_entities} entities), "
          f"{n_with_backrefs} avec backrefs")
    print(f"  -> {output.relative_to(VAULT_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
