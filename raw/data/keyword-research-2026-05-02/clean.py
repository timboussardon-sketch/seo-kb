#!/usr/bin/env python3
"""Filtre le bruit (k-pop, plantes, marques homonymes) et garde les mots-clés exploitables."""
import csv
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent
SRC = ROOT / "all-keywords.csv"

# Patterns de bruit à exclure
NOISE = [
    r"\bpark seo\b", r"\bseo joon\b", r"\bseo taiji\b", r"\bseo eun\b",
    r"\bseo kang\b", r"\bseo i yeon\b", r"\bseo in guk\b", r"\bseo yea?\b",
    r"\bia?nseo\b", r"\bseoul\b", r"\bbusan\b", r"\bincheon\b", r"\bdaejeon\b",
    r"\bpyongyang\b", r"\bkorean?\b", r"\bk[- ]?pop\b",
    r"\baeonium\b", r"\baeon flux\b", r"\baeonium ", r"^aeon ",
    r"\baesio\b", r"\baeon stock\b", r"\baeo stock\b",
    r"\bpromoseo\b", r"\bfatrank\b", r"\bkhazana\b", r"\bmichelin guide\b",
    r"\bnyc vs\b", r"\blondon vs\b", r"\btokyo vs\b",
    r"\baeon credit\b", r"\baeon mall\b",
    r"\bbrewing love\b", r"\bvillain the hero\b",
    r"\bseo business convers", r"\bconverse track\b",
    r"\bia[- ]?seo\b" if False else r"\bianseo\b",  # tir à l'arc
    r"\bagence wam\b", r"\bpica pau\b",
    r"\bclaude monet\b", r"\bclaude lemarchand\b",
    r"\bgeo guess\b", r"\bgeoguessr\b",
]

NOISE_RE = re.compile("|".join(NOISE), re.IGNORECASE)

# Patterns "branded competitor / very long tail spam"
BRAND_NOISE = re.compile(
    r"\b(odd angles media|fatrank|promoseo|rankstar|effective marketer|"
    r"keyword cupid|seo khazana|park seo|ianseo|seo taiji|seo eun)\b",
    re.IGNORECASE,
)

# Catégories rangées + intentions
CAT_LABEL = {
    "aeo_geo": "AEO / GEO / AI Search",
    "seo_ia_claude": "SEO + IA / Claude / Agents",
    "pseo_programmatique": "pSEO / Programmatique",
    "audit_quickwin": "Audit / Quick win / GSC",
    "methode_maillage": "Méthode / Maillage / Topical",
    "strategie_b2b": "Stratégie B2B / SaaS / Lead-gen",
    "contenu_redaction": "Contenu / Rédaction",
    "reddit_social": "Reddit / Social",
    "local_lyon": "Local Lyon",
    "vertical_avocat": "Vertical Avocat",
    "vertical_serrurier": "Vertical Serrurier",
    "vertical_immo": "Vertical Immobilier",
    "vertical_hotel": "Vertical Hôtellerie",
    "autre": "Autre / Misc",
}

INTENT_CAT = {
    "aeo_geo": "Know",
    "seo_ia_claude": "Know-décisionnel",
    "pseo_programmatique": "Know",
    "audit_quickwin": "Do",
    "methode_maillage": "Know",
    "strategie_b2b": "Do",
    "contenu_redaction": "Know",
    "reddit_social": "Know",
    "local_lyon": "Do",
    "vertical_avocat": "Do",
    "vertical_serrurier": "Do",
    "vertical_immo": "Do",
    "vertical_hotel": "Do",
    "autre": "?",
}

by_cat = defaultdict(list)
removed = 0
kept = 0

with SRC.open() as f:
    reader = csv.DictReader(f)
    for row in reader:
        kw = row["keyword"]
        cnt = int(row["count"])
        cat = row["category"]
        if NOISE_RE.search(kw) or BRAND_NOISE.search(kw):
            removed += 1
            continue
        # Skip très long tail nichées (10+ mots = souvent du spam)
        if len(kw.split()) > 9:
            removed += 1
            continue
        # Skip doublons trop proches du root (cas "audit seo", "audit seo en")
        if kw.endswith(" en") or kw.endswith(" la") or kw.endswith(" le") or kw.endswith(" un"):
            removed += 1
            continue
        by_cat[cat].append((kw, cnt))
        kept += 1

print(f"Kept: {kept} / Removed (noise): {removed}")

# Sort
for c in by_cat:
    by_cat[c].sort(key=lambda x: (-x[1], x[0]))

# Output : md propre + csv propre
out_md = ROOT / "keywords-cleaned.md"
out_csv = ROOT / "keywords-cleaned.csv"

with out_csv.open("w") as f:
    f.write("keyword,count,category,intent\n")
    for cat, items in by_cat.items():
        for kw, cnt in items:
            kw_safe = kw.replace('"', '""')
            f.write(f'"{kw_safe}",{cnt},{cat},{INTENT_CAT.get(cat, "?")}\n')

with out_md.open("w") as f:
    f.write("# Mots-clés Organikk — Google Suggest FR (filtré) — 2026-05-02\n\n")
    f.write(f"Source : scraping Google Suggest (FR) sur 40 racines × 39 expansions = 1680 requêtes.\n")
    f.write(f"Bruit retiré : k-pop, plante aeonium, mutuelle aesio, marques compétiteurs.\n\n")
    f.write(f"**Filtré** : {kept} mots-clés conservés sur 2587 ({removed} exclus).\n")
    f.write(f"**count** = nombre de fois où la suggestion est apparue parmi les 1680 requêtes (récurrence Google FR ≠ volume Semrush).\n\n")
    f.write("⚠️ Validation finale : croiser avec GSC organikk.co (positions/impressions) ou Semrush/Ahrefs (volume/difficulté).\n\n")
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
        intent = INTENT_CAT.get(cat, "?")
        f.write(f"## {CAT_LABEL[cat]} — {len(items)} mots-clés (intention dominante : {intent})\n\n")
        f.write("| # | Mot-clé | count |\n|---|---|---|\n")
        for i, (kw, cnt) in enumerate(items[:25], 1):
            f.write(f"| {i} | {kw} | {cnt} |\n")
        if len(items) > 25:
            f.write(f"\n*+ {len(items) - 25} autres dans `keywords-cleaned.csv`*\n")
        f.write("\n")

print(f"Wrote {out_md}")
print(f"Wrote {out_csv}")
