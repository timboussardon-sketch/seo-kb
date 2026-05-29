#!/bin/zsh
# Export du starter kit bootcamp : copie une ALLOWLIST du vault seo-kb vers un dossier propre,
# filtre les entités nominatives, puis re-scanne pour mettre en quarantaine toute fuite de nom.
# Ne touche PAS le repo source. Ne push rien. Construit un dossier local relisible.
set -euo pipefail

SRC="/Users/timothee/Code/seo-kb"
DST="$HOME/Documents/seo-kit-starter"
QUAR="$DST/_QUARANTINE_REVIEW"

if [ -d "$DST" ]; then
  echo "ERREUR: $DST existe déjà. Supprime-le ou renomme-le avant de relancer."
  exit 1
fi

mkdir -p "$DST"
cd "$SRC"

echo "=== 1. Copie de l'ALLOWLIST ==="

# Fichiers racine
for f in AGENTS.md README.md MIGRATION.md kb; do
  [ -f "$f" ] && { mkdir -p "$DST/$(dirname "$f")"; cp "$f" "$DST/$f"; }
done

# Dossiers .claude partageables
for d in .claude/skills .claude/commands .claude/scripts .claude/bin .claude/launchd; do
  [ -d "$d" ] && { mkdir -p "$DST/$d"; cp -R "$d/." "$DST/$d/"; }
done
[ -f .claude/README.md ] && cp .claude/README.md "$DST/.claude/README.md"

# Doctrine wiki (hors entities, traité séparément)
for d in wiki/concepts wiki/syntheses wiki/decisions wiki/moc; do
  [ -d "$d" ] && { mkdir -p "$DST/$d"; cp -R "$d/." "$DST/$d/"; }
done
[ -f wiki/000-home.md ] && cp wiki/000-home.md "$DST/wiki/000-home.md"

# Doctrine raw/notes partageable
for d in raw/notes/drive-accompagnement raw/notes/contenu-seo raw/notes/archive; do
  [ -d "$d" ] && { mkdir -p "$DST/$d"; cp -R "$d/." "$DST/$d/"; }
done

# Skills templates revue de presse + doc cowork (depuis bootcamp4, fichiers génériques uniquement)
mkdir -p "$DST/raw/bootcamp4"
for f in raw/bootcamp4/SKILL-revue-presse-bootcamp.md raw/bootcamp4/SKILL-revue-presse-theme-seo.md raw/bootcamp4/SKILL-revue-presse-client-template.md raw/bootcamp4/bundle-todo.md raw/bootcamp4/IMPLEMENTATION-COWORK.md; do
  [ -f "$f" ] && cp "$f" "$DST/$f"
done

echo "=== 2. Filtre des entités (concepts/tech uniquement, exclut les personnes/clients) ==="

mkdir -p "$DST/wiki/entities"
KEEP_ENTITIES="bert bm25 chatgpt-search dpr geo-bench google-ai-mode google-deepmind gsc isi karpathy linkedin metehan miras mum muvera naver neural-matching notebooklm obsidian perplexity product-bench qadence-seo-agent quality-raters-guidelines rankbrain sageo-arena-benchmark seer-interactive semrush sge titans vannevar-bush youtube organikk-co"
for e in ${(z)KEEP_ENTITIES}; do
  [ -f "wiki/entities/$e.md" ] && cp "wiki/entities/$e.md" "$DST/wiki/entities/$e.md"
done

echo "=== 3. Filet anti-fuite : scan des noms dans le dossier exporté ==="

mkdir -p "$QUAR"
# Noms de participants / entreprises clientes (word boundaries pour limiter les faux positifs)
NAMES='marrusia|marussia|\bjamel\b|\bjuliette\b|\bchristophe\b|\bfranck\b|\bjulien\b|\bcaroline\b|stéphanie|angélique|christelle|jean-jacques|\blydia\b|grégory|\balexandre\b|\bcécile\b|\bcecile\b|\banthony\b|\barnaud\b|fg-formation|audopass|\bjumpto\b|victoria-garden|fusionn'

QUAR_COUNT=0
find "$DST" -name "*.md" -type f | while read -r f; do
  # ne pas scanner la quarantaine elle-même
  case "$f" in "$QUAR"/*) continue;; esac
  if grep -liE "$NAMES" "$f" >/dev/null 2>&1; then
    rel="${f#$DST/}"
    mkdir -p "$QUAR/$(dirname "$rel")"
    mv "$f" "$QUAR/$rel"
    echo "  QUARANTINE: $rel"
  fi
done

echo ""
echo "=== 4. Bilan ==="
SHIPPED=$(find "$DST" -name "*.md" -type f -not -path "$QUAR/*" | wc -l | tr -d ' ')
QUARANTINED=$(find "$QUAR" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
echo "  Fichiers .md shippés   : $SHIPPED"
echo "  Fichiers .md quarantaine : $QUARANTINED (à relire/anonymiser à la main, PAS dans le repo final)"
echo "  Dossier export : $DST"
echo "  Quarantaine    : $QUAR"
echo ""
echo "NOTE: relis _QUARANTINE_REVIEW/ . Supprime-le AVANT de pousser sur GitHub."
