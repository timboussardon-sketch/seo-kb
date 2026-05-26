"""Helpers partagés entre les scripts d'indexation du vault."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterator

import yaml

VAULT_ROOT = Path(__file__).resolve().parents[2]
INDEX_DIR = VAULT_ROOT / ".claude" / "index"
VECTOR_STORE = VAULT_ROOT / ".claude" / "vector-store"

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H2_RE = re.compile(r"^##\s+", re.MULTILINE)

SKIP_DIRS = {
    ".git", ".obsidian", ".obsidian.broken", ".claude", ".venv",
    "node_modules", "mockups", "raw/revue-de-presse",
}


def iter_markdown(root: Path = VAULT_ROOT) -> Iterator[Path]:
    """Yield all .md files under root, skipping known noise directories."""
    for path in root.rglob("*.md"):
        rel = path.relative_to(root).as_posix()
        if any(rel == d or rel.startswith(d + "/") for d in SKIP_DIRS):
            continue
        yield path


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Empty dict if no frontmatter."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        data = {}
    body = text[m.end():]
    return data if isinstance(data, dict) else {}, body


def slug_from_path(path: Path) -> str:
    """wiki/concepts/aeo.md -> aeo"""
    return path.stem


def extract_wikilinks(body: str) -> list[str]:
    """Return slugs of [[wikilinks]] found in body."""
    out = []
    seen = set()
    for m in WIKILINK_RE.finditer(body):
        target = m.group(1).strip()
        slug = target.split("/")[-1]
        if slug not in seen:
            seen.add(slug)
            out.append(slug)
    return out


def read_markdown(path: Path) -> tuple[dict, str]:
    """Read file, return (frontmatter, body)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    return parse_frontmatter(text)
