#!/usr/bin/env bash
# Scrape Google Suggest (FR) avec expansion alphabétique
# Usage: ./scrape-suggest.sh
set -u

OUT_DIR="$(dirname "$0")/raw"
mkdir -p "$OUT_DIR"

# Thématiques racines extraites de la doctrine + blog Organikk
ROOTS=(
  # Méta-SEO 2026 / AEO
  "aeo"
  "answer engine optimization"
  "ai overviews"
  "passage ranking"
  "topical authority"
  "geo seo"
  "search generative experience"

  # SEO + IA / Claude / agents
  "seo claude"
  "audit seo claude"
  "agent seo ia"
  "agent seo"
  "seo ia"
  "chatgpt seo"
  "claude seo"

  # Doctrine programmatique / production
  "pseo"
  "seo programmatique"
  "programmatic seo"
  "contenu ia seo"
  "rédaction seo ia"

  # Lead-gen B2B / commercial
  "consultant seo b2b"
  "seo b2b"
  "seo saas"
  "seo lead generation"
  "stratégie seo"
  "audit seo"

  # Local Lyon (cas-clients)
  "seo lyon"
  "consultant seo lyon"
  "agence seo lyon"
  "seo serrurier"
  "seo agence immobilière"
  "seo avocat"
  "seo hôtel"

  # Micro-intentions / méthode
  "maillage interne seo"
  "cocon sémantique"
  "cannibalisation seo"
  "quick win seo"
  "search console audit"
  "intention de recherche seo"

  # Concepts émergents
  "reddit seo"
  "reddit geo"
  "information gain seo"
  "product led seo"
)

# Expansion alphabétique : récupère "racine a", "racine b"... pour la longue traîne
ALPHA=(a b c d e f g h i j k l m n o p q r s t u v w x y z)

# Modifiers question/intention
MODIFIERS=("comment" "pourquoi" "quel" "quelle" "définition" "exemple" "prix" "outil" "gratuit" "guide" "tutoriel" "vs" "pour")

fetch() {
  local q="$1"
  local slug
  slug=$(echo "$q" | tr ' /' '_-' | tr -cd '[:alnum:]_-')
  local out="$OUT_DIR/${slug}.json"
  curl -sf --max-time 8 \
    "http://suggestqueries.google.com/complete/search?client=firefox&q=$(printf %s "$q" | sed 's/ /+/g')&hl=fr&gl=fr" \
    > "$out" 2>/dev/null && echo "OK $q" || echo "FAIL $q"
}

export -f fetch
export OUT_DIR

# Génère toutes les requêtes
{
  for r in "${ROOTS[@]}"; do
    echo "$r"
    for a in "${ALPHA[@]}"; do
      echo "$r $a"
    done
    for m in "${MODIFIERS[@]}"; do
      echo "$m $r"
    done
  done
} | sort -u > "$OUT_DIR/queries.txt"

total=$(wc -l < "$OUT_DIR/queries.txt")
echo "Total queries: $total"

# Parallèle 8 workers, polite delay
cat "$OUT_DIR/queries.txt" | xargs -P 8 -I {} bash -c 'fetch "$@"' _ {} > "$OUT_DIR/log.txt" 2>&1

echo "Done. Logs: $OUT_DIR/log.txt"
echo "OK count:    $(grep -c '^OK ' "$OUT_DIR/log.txt")"
echo "FAIL count:  $(grep -c '^FAIL ' "$OUT_DIR/log.txt")"
