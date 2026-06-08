#!/usr/bin/env python3
"""recall.py — rappel déterministe sur syntheticmemory (ce que le système sait sur Tim et sa méthode).

Pas d'API, pas de vector store : scoring par recouvrement de termes sur statement+tags+subject+type.
Lecture seule. Sûr à relancer.

Usage : ./recall.py "wording marque"  [--type preference] [--n 5]
"""
import json, os, sys, re

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, "store.jsonl")


def load():
    rows, bad = [], 0
    if not os.path.exists(STORE):
        return rows, bad
    with open(STORE, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            try:
                rows.append(json.loads(s))
            except Exception:
                bad += 1
    return rows, bad


def terms(t):
    return set(re.findall(r"\w+", (t or "").lower()))


def score(rec, q):
    hay = " ".join([rec.get("statement", ""), " ".join(rec.get("tags", []) or []),
                    rec.get("subject", ""), rec.get("type", "")])
    inter = q & terms(hay)
    if not inter:
        return 0.0
    return len(inter) + 0.1 * float(rec.get("confidence", 0) or 0)


def main():
    args = sys.argv[1:]
    typ, n, query = None, 5, []
    i = 0
    while i < len(args):
        if args[i] == "--type" and i + 1 < len(args):
            typ = args[i + 1]; i += 2
        elif args[i] == "--n" and i + 1 < len(args):
            n = int(args[i + 1]); i += 2
        else:
            query.append(args[i]); i += 1
    if not query:
        print('usage: ./recall.py "<requête>" [--type T] [--n N]')
        return
    q = terms(" ".join(query))
    rows, bad = load()
    cand = [r for r in rows if (typ is None or r.get("type") == typ)]
    scored = sorted(((score(r, q), r) for r in cand), key=lambda x: x[0], reverse=True)
    hits = [(s, r) for s, r in scored if s > 0][:n]
    if not hits:
        print("(aucun souvenir pertinent)")
    for s, r in hits:
        print(f"[{r.get('id')}] {r.get('type')}/{r.get('subject')} · conf {r.get('confidence')} · score {round(s, 1)}")
        print(f"  {r.get('statement')}")
    if bad:
        print(f"(note: {bad} ligne(s) illisible(s) dans store.jsonl)")


if __name__ == "__main__":
    main()
