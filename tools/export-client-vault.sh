#!/bin/bash
# Transfert vault client — tout sauf stratégie client
# Usage : bash tools/export-client-vault.sh [bootcamp|retainer]
# Doc complète : wiki/queries/transfert-vault-client.md

set -e

SRC="$HOME/Documents/seo-kb"
DST="$HOME/seo-kb-client-export"
MODE="${1:-bootcamp}"

if [[ "$MODE" != "bootcamp" && "$MODE" != "retainer" ]]; then
  echo "❌ Mode invalide. Usage : bash tools/export-client-vault.sh [bootcamp|retainer]"
  exit 1
fi

rm -rf "$DST"
mkdir -p "$DST"

# 1. Structure de base
cp "$SRC/AGENTS.md" "$DST/"
cp "$SRC/README.md" "$DST/" 2>/dev/null || true
mkdir -p "$DST/wiki/"{sources,entities,concepts,syntheses,queries,briefs,clusters,quick-wins,cannibalisation,maillage,posts-linkedin,revues-presse}
mkdir -p "$DST/raw/"{articles,papers,etudes-seo,notes,data,assets}

# 2. Concepts — exclure les 3 concepts bootcamp (tabou-visibilite transféré par défaut, doctrine vente générique)
EXCLUDE_CONCEPTS=(
  "avatar-freelance-sans-systeme"
  "cercle-vicieux-temps-structure"
  "peur-train-ia"
)
for f in "$SRC/wiki/concepts/"*.md; do
  name=$(basename "$f" .md)
  skip=false
  for ex in "${EXCLUDE_CONCEPTS[@]}"; do [[ "$name" == "$ex" ]] && skip=true; done
  $skip || cp "$f" "$DST/wiki/concepts/"
done

# 3. Entities — exclure prospects + clients Tim + produits Tim
EXCLUDE_ENTITIES=(
  "arnaud" "marrusia-cecile" "jamel" "dev-web-anon" "juliette"
  "christophe" "franck" "julien" "audopass" "jumpto"
  "victoria-garden" "bootcamp-seo-ia"
)
# Mode retainer : exclure aussi organikk-co + fusionn-io (commerciaux Tim)
if [[ "$MODE" == "retainer" ]]; then
  EXCLUDE_ENTITIES+=("organikk-co" "fusionn-io")
fi

for f in "$SRC/wiki/entities/"*.md; do
  name=$(basename "$f" .md)
  skip=false
  for ex in "${EXCLUDE_ENTITIES[@]}"; do [[ "$name" == "$ex" ]] && skip=true; done
  $skip || cp "$f" "$DST/wiki/entities/"
done

# 4. Sources — exclure prospects + client-note + stratégie commerciale
EXCLUDE_SOURCES=(
  "2026-04-13-analyse-calls-prospects-bootcamp"
  "2026-04-13-call-01-arnaud" "2026-04-13-call-04-jamel"
  "2026-04-13-call-05-dev-web" "2026-04-13-call-06-juliette"
  "2026-04-13-call-07-christophe" "2026-04-13-call-08-franck"
  "2026-04-13-call-09-julien"
  "2026-04-13-cas-clients-resultats"
  "2026-04-13-offre-bootcamp-seo-ia"
  "2026-04-13-victoria-garden-pseo"
)
# Mode retainer : exclure aussi skills proprietary + prompts pSEO + scrapes organikk
if [[ "$MODE" == "retainer" ]]; then
  EXCLUDE_SOURCES+=(
    "2026-04-12-tim-skills-seo-proprietary"
    "2026-04-13-prompt-pseo-produit-service"
    "2026-04-13-prompt-pseo-non-produit"
    "2026-04-12-organikk-blog-scrape"
    "2026-04-12-organikk-glossaire-scrape"
  )
fi

for f in "$SRC/wiki/sources/"*.md; do
  name=$(basename "$f" .md)
  skip=false
  for ex in "${EXCLUDE_SOURCES[@]}"; do [[ "$name" == "$ex" ]] && skip=true; done
  $skip || cp "$f" "$DST/wiki/sources/"
done

# 5. Syntheses — seule doctrine-seo-post-sge
cp "$SRC/wiki/syntheses/doctrine-seo-post-sge.md" "$DST/wiki/syntheses/" 2>/dev/null || true

# 6. Queries — transférer wiki-pattern-vs-grounding-score uniquement (la query transfert reste chez Tim)
cp "$SRC/wiki/queries/2026-04-12-wiki-pattern-vs-grounding-score.md" "$DST/wiki/queries/" 2>/dev/null || true

# 7. Raw articles / papers / etudes-seo — tout (sources publiques)
cp "$SRC/raw/articles/"*.md "$DST/raw/articles/" 2>/dev/null || true
cp "$SRC/raw/papers/"*.md "$DST/raw/papers/" 2>/dev/null || true
cp "$SRC/raw/papers/"*.pdf "$DST/raw/papers/" 2>/dev/null || true
cp "$SRC/raw/etudes-seo/"* "$DST/raw/etudes-seo/" 2>/dev/null || true

# 8. Raw notes — exclure perso Tim + stratégie commerciale
EXCLUDE_NOTES=(
  "tim-about-me" "tim-my-rules" "tim-my-voice"
  "tim-readme-bot-instructions"
  "offre-bootcamp-seo-ia"
  "analyse-calls-prospects-bootcamp"
  "cas-clients-resultats"
)
# Mode retainer : exclure aussi les 10 skills + les 2 prompts pSEO + tim-workflow + tim-prompt
if [[ "$MODE" == "retainer" ]]; then
  for skill in skill-brief-contenu skill-cannibalisation skill-cluster-aeo \
               skill-entites-vectorielles skill-maillage-interne skill-peurs-objections \
               skill-product-led-seo skill-programmatique-pseo skill-quick-win \
               skill-workflow-article prompt-pseo-produit-service prompt-pseo-non-produit \
               tim-workflow-redaction tim-prompt-systeme; do
    EXCLUDE_NOTES+=("$skill")
  done
fi

for f in "$SRC/raw/notes/"*.md; do
  name=$(basename "$f" .md)
  skip=false
  for ex in "${EXCLUDE_NOTES[@]}"; do [[ "$name" == "$ex" ]] && skip=true; done
  $skip || cp "$f" "$DST/raw/notes/"
done

# 9. Régénérer index.md et log.md vides
cat > "$DST/wiki/index.md" <<'INDEX'
# Index du wiki SEO/IA/GEO

> Index à régénérer au fil de l'ingestion de vos propres sources.
> Structure attendue : voir AGENTS.md §8.

## Sources (N)
## Entities (N)
## Concepts (N)
## Syntheses (N)
## Queries (N)
INDEX

cat > "$DST/wiki/log.md" <<LOG
# Log

> Journal chronologique append-only. Parseable via \`grep "^## \\[" wiki/log.md\`.

## [$(date +%Y-%m-%d)] bootstrap | Vault reçu de Timothée Boussardon (mode: $MODE)
- doctrine SEO/GEO + papers de référence + méthode Karpathy/Obsidian
- à personnaliser avec vos propres sources clients et cas terrain
LOG

# 10. .gitkeep pour dossiers vides
for dir in "$DST/wiki/"{briefs,clusters,quick-wins,cannibalisation,maillage,posts-linkedin,revues-presse} "$DST/raw/"{data,assets}; do
  touch "$dir/.gitkeep"
done

# 11. Rapport
echo ""
echo "✅ Vault exporté : $DST"
echo "   Mode : $MODE"
echo ""
echo "📊 Contenu :"
echo "   - concepts : $(ls "$DST/wiki/concepts/" | wc -l | tr -d ' ')"
echo "   - entities : $(ls "$DST/wiki/entities/" | wc -l | tr -d ' ')"
echo "   - sources  : $(ls "$DST/wiki/sources/" | wc -l | tr -d ' ')"
echo "   - syntheses: $(ls "$DST/wiki/syntheses/" | wc -l | tr -d ' ')"
echo "   - raw notes: $(ls "$DST/raw/notes/" | wc -l | tr -d ' ')"
echo ""
echo "⚠️  À vérifier manuellement avant envoi :"
echo "   1. ls $DST/wiki/sources/ | grep -E 'call-|cas-clients|bootcamp|victoria'  → doit être vide"
echo "   2. ls $DST/wiki/entities/ | grep -E 'arnaud|jamel|christophe|victoria|bootcamp'  → doit être vide"
echo "   3. ls $DST/raw/ | grep -E 'cas-clients|transcripts'  → doit être vide"
echo ""
echo "📦 Zip : zip -r seo-kb-starter-$MODE.zip seo-kb-client-export/"
