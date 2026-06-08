#!/usr/bin/env python3
"""add.py — ajoute un souvenir à syntheticmemory (append-only, traçable git).

Généralement appelé par Claude après un feedback/décision/préférence durable de Tim.
Valide les champs requis, génère l'id, écrit une ligne. Ne réécrit jamais l'historique.

Usage :
  ./add.py --type preference --subject wording --statement "..." \
           [--evidence "..."] [--confidence 0.9] [--tags a,b] [--supersedes SM-...]
"""
import json, os, sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, "store.jsonl")
TYPES = {"preference", "fact", "decision", "principle", "skill_feedback", "mistake"}


def parse_args():
    a = sys.argv[1:]
    d, i = {}, 0
    while i < len(a):
        if a[i].startswith("--"):
            key = a[i][2:]
            val = a[i + 1] if i + 1 < len(a) else ""
            d[key] = val
            i += 2
        else:
            i += 1
    return d


def next_id(today):
    n = 0
    if os.path.exists(STORE):
        with open(STORE, encoding="utf-8") as f:
            for line in f:
                if f'"SM-{today}-' in line:
                    n += 1
    return f"SM-{today}-{n + 1:03d}"


def main():
    d = parse_args()
    for req in ("type", "subject", "statement"):
        if not d.get(req):
            print(f"manque --{req}")
            sys.exit(1)
    if d["type"] not in TYPES:
        print(f"type invalide « {d['type']} ». Attendu : {sorted(TYPES)}")
        sys.exit(1)
    today = date.today().isoformat()
    rec = {
        "id": next_id(today),
        "added": today,
        "type": d["type"],
        "subject": d["subject"],
        "statement": d["statement"],
        "evidence": d.get("evidence", ""),
        "confidence": float(d.get("confidence", 0.8)),
        "tags": [t.strip() for t in d.get("tags", "").split(",") if t.strip()],
        "supersedes": d.get("supersedes") or None,
    }
    with open(STORE, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"ajouté {rec['id']} ({rec['type']}/{rec['subject']}) : {rec['statement'][:70]}...")


if __name__ == "__main__":
    main()
