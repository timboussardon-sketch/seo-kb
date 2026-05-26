"""Embed du vault dans ChromaDB.

Chunking : par section H2 du markdown (avec entête de l'article comme contexte H1).
Embedding : sentence-transformers paraphrase-multilingual-mpnet-base-v2 (local, FR-friendly).
Storage : ChromaDB persistant à .claude/vector-store/.

Métadonnées indexées : path, slug, type, source_type, tags (joints en string), status,
confidence, created, section_title. Permet le filtrage déterministe avant la recherche.

--full : rebuild from scratch.
Par défaut : incremental (skip si mtime inchangé depuis dernier index).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

from _common import (
    VAULT_ROOT,
    VECTOR_STORE,
    INDEX_DIR,
    iter_markdown,
    read_markdown,
    slug_from_path,
)

MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"
COLLECTION_NAME = "seo_kb"
MTIME_INDEX = INDEX_DIR / "embed_mtime.json"

MIN_CHUNK_CHARS = 200
MAX_CHUNK_CHARS = 4000


def looks_binary(text: str) -> bool:
    """Détecte les chunks contenant du base64/binaire encodé inline.

    Heuristique : un chunk avec >30% de mots longs (>40 chars) sans espace
    intérieur OU un ratio de whitespace très bas (<5%) est suspect.
    """
    if not text:
        return False
    words = text.split()
    if not words:
        return True
    long_dense = sum(1 for w in words if len(w) > 40)
    if long_dense / len(words) > 0.3:
        return True
    whitespace_ratio = sum(1 for c in text if c.isspace()) / max(len(text), 1)
    if whitespace_ratio < 0.05 and len(text) > 400:
        return True
    return False


def chunk_markdown(body: str, title: str) -> list[tuple[str, str]]:
    """Split par H2. Préfixe chaque chunk par '# {title}\n## {section}'.
    Return list of (section_title, chunk_text).
    """
    lines = body.split("\n")
    chunks: list[tuple[str, str]] = []
    current_section = "intro"
    current_lines: list[str] = []

    def flush():
        text = "\n".join(current_lines).strip()
        if len(text) < MIN_CHUNK_CHARS:
            return
        if looks_binary(text):
            return
        full = f"# {title}\n## {current_section}\n\n{text}"
        if len(full) > MAX_CHUNK_CHARS:
            for i in range(0, len(full), MAX_CHUNK_CHARS - 200):
                piece = full[i:i + MAX_CHUNK_CHARS]
                if not looks_binary(piece):
                    chunks.append((current_section, piece))
        else:
            chunks.append((current_section, full))

    for line in lines:
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            flush()
            current_section = m.group(1).strip()
            current_lines = []
        else:
            current_lines.append(line)
    flush()

    if not chunks and body.strip():
        full = f"# {title}\n\n{body.strip()}"[:MAX_CHUNK_CHARS]
        chunks.append(("intro", full))
    return chunks


def stringify(value) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return ", ".join(str(v) for v in value)
    return str(value)


def file_signature(path: Path) -> str:
    stat = path.stat()
    return f"{stat.st_mtime_ns}:{stat.st_size}"


def load_mtime_index() -> dict[str, str]:
    if MTIME_INDEX.exists():
        return json.loads(MTIME_INDEX.read_text())
    return {}


def save_mtime_index(idx: dict[str, str]) -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    MTIME_INDEX.write_text(json.dumps(idx, indent=2, sort_keys=True))


def main() -> int:
    ap = argparse.ArgumentParser(description="Build vector index du vault")
    ap.add_argument("--full", action="store_true",
                    help="Rebuild from scratch (drop la collection)")
    args = ap.parse_args()

    print(f"Loading model {MODEL_NAME}...")
    from sentence_transformers import SentenceTransformer
    import chromadb

    model = SentenceTransformer(MODEL_NAME)

    VECTOR_STORE.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(VECTOR_STORE))

    if args.full:
        try:
            client.delete_collection(COLLECTION_NAME)
            print(f"  dropped collection {COLLECTION_NAME}")
        except Exception:
            pass

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    mtime_index = {} if args.full else load_mtime_index()
    new_mtime: dict[str, str] = dict(mtime_index)

    to_index: list[Path] = []
    for path in iter_markdown():
        rel = path.relative_to(VAULT_ROOT).as_posix()
        sig = file_signature(path)
        if mtime_index.get(rel) == sig:
            continue
        to_index.append(path)
        new_mtime[rel] = sig

    if not to_index:
        print("Rien à réindexer (tout est à jour).")
        return 0

    print(f"Indexing {len(to_index)} fichier(s)...")

    all_ids, all_texts, all_metadatas = [], [], []
    skipped_to_delete: list[str] = []

    for path in to_index:
        rel = path.relative_to(VAULT_ROOT).as_posix()
        fm, body = read_markdown(path)
        title = fm.get("title") or slug_from_path(path)
        chunks = chunk_markdown(body, str(title))
        if not chunks:
            continue

        skipped_to_delete.append(rel)

        for i, (section, text) in enumerate(chunks):
            chunk_id = hashlib.sha1(f"{rel}::{i}".encode()).hexdigest()
            all_ids.append(chunk_id)
            all_texts.append(text)
            all_metadatas.append({
                "path": rel,
                "slug": slug_from_path(path),
                "section": section,
                "chunk_index": i,
                "type": stringify(fm.get("type")),
                "source_type": stringify(fm.get("source_type")),
                "tags": stringify(fm.get("tags")),
                "status": stringify(fm.get("status")),
                "confidence": stringify(fm.get("confidence")),
                "created": stringify(fm.get("created")),
                "title": str(title),
            })

    if not args.full and skipped_to_delete:
        try:
            collection.delete(where={"path": {"$in": skipped_to_delete}})
        except Exception as e:
            print(f"  warn: delete partielle: {e}")

    print(f"Encoding {len(all_texts)} chunks...")
    batch_size = 64
    for i in range(0, len(all_texts), batch_size):
        batch_texts = all_texts[i:i + batch_size]
        batch_ids = all_ids[i:i + batch_size]
        batch_metas = all_metadatas[i:i + batch_size]
        embeddings = model.encode(
            batch_texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False,
        ).tolist()
        collection.upsert(
            ids=batch_ids,
            embeddings=embeddings,
            documents=batch_texts,
            metadatas=batch_metas,
        )
        print(f"  upserted {min(i + batch_size, len(all_texts))}/{len(all_texts)}")

    save_mtime_index(new_mtime)
    total = collection.count()
    print(f"\nDone. Collection {COLLECTION_NAME}: {total} chunks indexés.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
