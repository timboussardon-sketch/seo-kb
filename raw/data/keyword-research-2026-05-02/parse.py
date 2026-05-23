#!/usr/bin/env python3
"""Parse Google Suggest JSON dumps → liste mots-clés dédoublonnée + classée."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent / "raw"
OUT = Path(__file__).parent

# Catégorisation par regex (ordre = priorité, premier match gagne)
CATEGORIES = [
    ("aeo_geo", r"\b(aeo|answer engine|ai overview|search generative|sge|geo|llm)"),
    ("seo_ia_claude", r"\b(claude|chatgpt|gpt|ia|ai\b|agent|gemini|perplexity)"),
    ("pseo_programmatique", r"\b(pseo|programmatique|programmatic|template)"),
    ("local_lyon", r"\b(lyon|villeurbanne|grenoble)"),
    ("vertical_avocat", r"\b(avocat|juridique|anadavi|oniam|cabinet)"),
    ("vertical_serrurier", r"\b(serrurier|serrurerie)"),
    ("vertical_immo", r"\b(immobili|agence immobil|immo)"),
    ("vertical_hotel", r"\b(hotel|hôtel|airbnb|appart)"),
    ("audit_quickwin", r"\b(audit|quick win|cannibalis|search console)"),
    ("methode_maillage", r"\b(maillage|cocon|topical|silo|micro.intention|passage rank|information gain|product.led)"),
    ("strategie_b2b", r"\b(b2b|saas|consultant|stratégie|lead gen)"),
    ("contenu_redaction", r"\b(rédaction|content|contenu|article|blog|newsletter)"),
    ("reddit_social", r"\b(reddit|linkedin|x\.com|twitter|tiktok)"),
]

def categorize(kw: str) -> str:
    for name, pat in CATEGORIES:
        if re.search(pat, kw, re.IGNORECASE):
            return name
    return "autre"

# Parse all JSON files
suggestions = Counter()  # kw -> count of times it appears across queries
sources = {}  # kw -> set of source queries that surfaced it

for fp in sorted(ROOT.glob("*.json")):
    try:
        data = json.loads(fp.read_text())
    except Exception:
        continue
    if not isinstance(data, list) or len(data) < 2:
        continue
    source_q = data[0]
    for sug in data[1]:
        sug_norm = sug.lower().strip()
        if not sug_norm or sug_norm == source_q.lower().strip():
            continue
        suggestions[sug_norm] += 1
        sources.setdefault(sug_norm, set()).add(source_q)

print(f"Total unique suggestions: {len(suggestions)}")
print(f"Total raw occurrences:    {sum(suggestions.values())}")

# Classify
by_cat: dict[str, list[tuple[str, int]]] = {}
for kw, cnt in suggestions.items():
    cat = categorize(kw)
    by_cat.setdefault(cat, []).append((kw, cnt))

# Sort each category by count desc
for cat in by_cat:
    by_cat[cat].sort(key=lambda x: (-x[1], x[0]))

# Write all keywords (CSV)
all_csv = OUT / "all-keywords.csv"
with all_csv.open("w") as f:
    f.write("keyword,count,category\n")
    for cat, items in sorted(by_cat.items()):
        for kw, cnt in items:
            kw_safe = kw.replace('"', '""')
            f.write(f'"{kw_safe}",{cnt},{cat}\n')
print(f"Wrote {all_csv}")

# Write categorized markdown report (top 30 per cat)
md = OUT / "keywords-classified.md"
with md.open("w") as f:
    f.write("# Mots-clés Organikk — Google Suggest FR (2026-05-02)\n\n")
    f.write(f"Source : scraping Google Suggest (FR/google.fr) sur 40 racines × 39 expansions = 1680 requêtes.\n\n")
    f.write(f"**Total unique** : {len(suggestions)} suggestions distinctes.\n")
    f.write(f"**count** = nombre de fois où la suggestion est apparue parmi les 1680 requêtes (= signal de récurrence Google, pas volume réel).\n\n")
    f.write("⚠️ Pas de volumes / positions / impressions ici. Pour la priorisation finale → croiser avec GSC organikk.co ou Semrush.\n\n")
    f.write("---\n\n")

    cat_order = [
        "aeo_geo", "seo_ia_claude", "pseo_programmatique",
        "audit_quickwin", "methode_maillage", "strategie_b2b",
        "contenu_redaction", "reddit_social",
        "local_lyon", "vertical_avocat", "vertical_serrurier",
        "vertical_immo", "vertical_hotel", "autre",
    ]
    for cat in cat_order:
        items = by_cat.get(cat, [])
        if not items:
            continue
        f.write(f"## {cat} ({len(items)} mots-clés)\n\n")
        f.write("| Rank | Mot-clé | count |\n|---|---|---|\n")
        for i, (kw, cnt) in enumerate(items[:30], 1):
            f.write(f"| {i} | {kw} | {cnt} |\n")
        if len(items) > 30:
            f.write(f"\n*+ {len(items) - 30} autres dans `all-keywords.csv`*\n")
        f.write("\n")

print(f"Wrote {md}")
