#!/usr/bin/env python3
"""
Grounding du lexique des modificateurs d'intention (corpus 1 Qadence).

Ne décide RIEN sur le sens d'un modificateur. Mesure seulement, sur de la
donnée déjà collectée :
  - la fréquence réelle d'apparition dans des requêtes Google Suggest FR
  - le nombre de verticales métier où le modificateur apparaît
  - la distribution d'intention observée (source : keywords-cleaned.csv,
    classé lors de la recherche du 2026-05-02)
  - des exemples de requêtes réellement remontées

Sources (lecture seule) :
  fusionn/grounding/*.json                      13 344 requêtes, 23 verticales
  raw/data/keyword-research-2026-05-02/keywords-cleaned.csv   2 424 mots-clés classés

Sortie : qadence/grounding/modificateurs.json
La curation (quel token est un modificateur d'intention, dans quelle famille)
se fait ensuite à la main contre la doctrine du vault. Ce script ne la fait pas.
"""

import json
import csv
import re
import glob
import os
import collections

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUGGEST = os.path.join(VAULT, "fusionn", "grounding", "*.json")
CLASSED = os.path.join(
    VAULT, "raw", "data", "keyword-research-2026-05-02", "keywords-cleaned.csv"
)
OUT_DIR = os.path.join(VAULT, "qadence", "grounding")
OUT = os.path.join(OUT_DIR, "modificateurs.json")

TOKEN_RE = re.compile(r"[a-zà-ÿ0-9']+")

# Mots vides FR/EN : jamais des modificateurs d'intention à eux seuls.
STOP = {
    "de", "du", "des", "le", "la", "les", "un", "une", "et", "ou", "a", "à",
    "au", "aux", "en", "dans", "sur", "par", "pour", "avec", "sans", "ce",
    "cette", "ces", "son", "sa", "ses", "il", "elle", "on", "je", "tu", "nous",
    "vous", "qui", "que", "quoi", "est", "sont", "the", "of", "in", "for",
    "and", "to", "is", "are", "on", "at", "with", "by", "d", "l", "s", "n",
}


def load_suggest():
    """Retourne [(verticale, requête)] depuis les 23 fichiers de grounding."""
    rows = []
    for path in sorted(glob.glob(SUGGEST)):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        vertical = data.get("keyword", os.path.basename(path))
        for item in data.get("real_queries", []):
            q = (item.get("query") or "").strip().lower()
            if q:
                rows.append((vertical, q))
    assert rows, f"aucune requête lue depuis {SUGGEST}"
    return rows


def load_intents():
    """Retourne [(mot-clé, intention)] depuis le CSV déjà classé."""
    rows = []
    with open(CLASSED, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            kw = (r.get("keyword") or "").strip().lower()
            intent = (r.get("intent") or "").strip()
            if kw and intent and intent != "?":
                rows.append((kw, intent))
    assert rows, f"aucune intention lue depuis {CLASSED}"
    return rows


def ngrams(query, root_tokens):
    """Unigrammes et bigrammes de la requête, hors racine métier et mots vides."""
    toks = TOKEN_RE.findall(query)
    out = []
    for t in toks:
        if len(t) > 1 and t not in root_tokens and t not in STOP:
            out.append(t)
    for a, b in zip(toks, toks[1:]):
        if a in root_tokens or b in root_tokens:
            continue
        if len(a) > 1 and len(b) > 1:
            out.append(f"{a} {b}")
    return out


def main():
    suggest = load_suggest()
    intents = load_intents()

    occurrences = collections.Counter()
    verticals = collections.defaultdict(set)
    examples = collections.defaultdict(list)

    for vertical, query in suggest:
        root = set(TOKEN_RE.findall(vertical.lower()))
        for gram in set(ngrams(query, root)):
            occurrences[gram] += 1
            verticals[gram].add(vertical)
            if len(examples[gram]) < 6:
                examples[gram].append(query)

    # Distribution d'intention observée. Appariement en LIMITES DE MOTS :
    # en sous-chaîne, « se » matcherait « seo », « conseil », « analyse »… et la
    # distribution ne voudrait plus rien dire.
    intent_dist = collections.defaultdict(collections.Counter)
    kw_tokens = [(set(TOKEN_RE.findall(kw)), TOKEN_RE.findall(kw), intent) for kw, intent in intents]
    for gram in occurrences:
        parts = gram.split(" ")
        counter = intent_dist[gram]
        for tokset, toklist, intent in kw_tokens:
            if len(parts) == 1:
                hit = parts[0] in tokset
            else:
                hit = any(
                    toklist[i : i + len(parts)] == parts
                    for i in range(len(toklist) - len(parts) + 1)
                )
            if hit:
                counter[intent] += 1

    modifiers = []
    for gram, count in occurrences.most_common():
        if count < 8:
            continue
        modifiers.append(
            {
                "token": gram,
                "occurrences": count,
                "verticales": len(verticals[gram]),
                "intention_mesuree": dict(intent_dist.get(gram, {})),
                "exemples": examples[gram],
            }
        )

    os.makedirs(OUT_DIR, exist_ok=True)
    payload = {
        "sources": {
            "google_suggest": {
                "chemin": "fusionn/grounding/*.json",
                "requetes": len(suggest),
                "verticales": len(set(v for v, _ in suggest)),
            },
            "mots_cles_classes": {
                "chemin": "raw/data/keyword-research-2026-05-02/keywords-cleaned.csv",
                "mots_cles": len(intents),
            },
        },
        "seuil_retenu": "8 occurrences minimum",
        "candidats": len(modifiers),
        "modificateurs": modifiers,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"requêtes lues        : {len(suggest)}")
    print(f"mots-clés classés    : {len(intents)}")
    print(f"candidats retenus    : {len(modifiers)}")
    print(f"écrit                : {OUT}")


if __name__ == "__main__":
    main()
