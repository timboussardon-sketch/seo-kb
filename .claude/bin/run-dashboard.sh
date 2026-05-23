#!/bin/zsh
# Daily dashboard generator — invoked by launchd com.timboussardon.dashboard
# Generates wiki/dashboard.md with KPIs across the vault
set -uo pipefail

export PATH="/usr/local/bin:/usr/bin:/bin"
export HOME="/Users/timothee"

VAULT="/Users/timothee/Code/seo-kb"
LOG_DIR="$VAULT/.claude/logs"
LOG_FILE="$LOG_DIR/dashboard-$(date +%Y-%m-%d).log"
OUT="$VAULT/wiki/dashboard.md"

mkdir -p "$LOG_DIR"
cd "$VAULT"

{
  echo "=== dashboard run started at $(date -Iseconds) ==="

  TODAY=$(date +%Y-%m-%d)
  NOW=$(date "+%Y-%m-%d %H:%M")

  # === Helper functions ===
  count_files() {
    local dir="$1"
    [ -d "$dir" ] && find "$dir" -type f -name "*.md" 2>/dev/null | wc -l | tr -d ' ' || echo 0
  }
  count_words() {
    local dir="$1"
    if [ -d "$dir" ]; then
      find "$dir" -type f -name "*.md" -print0 2>/dev/null | xargs -0 cat 2>/dev/null | wc -w | tr -d ' '
    else
      echo 0
    fi
  }
  last_modif() {
    local dir="$1"
    if [ -d "$dir" ]; then
      find "$dir" -type f -name "*.md" -exec stat -f "%m %N" {} \; 2>/dev/null \
        | sort -rn | head -1 | awk '{print $1}' \
        | xargs -I{} date -r {} "+%Y-%m-%d" 2>/dev/null
    fi
  }
  days_since() {
    local d="$1"
    [ -z "$d" ] && echo "?" && return
    local then_ts=$(date -j -f "%Y-%m-%d" "$d" "+%s" 2>/dev/null)
    local now_ts=$(date "+%s")
    [ -n "$then_ts" ] && echo $(( (now_ts - then_ts) / 86400 )) || echo "?"
  }

  # === Volume ===
  RAW_FILES=$(count_files "raw")
  WIKI_FILES=$(count_files "wiki")
  TOTAL_FILES=$((RAW_FILES + WIKI_FILES))

  WIKILINKS=$(grep -rho '\[\[[^]]*\]\]' raw wiki 2>/dev/null | wc -l | tr -d ' ')
  AVG_LINKS=$(awk -v t=$WIKILINKS -v f=$TOTAL_FILES 'BEGIN { if (f>0) printf "%.1f", t/f; else print "0" }')

  # === Sub-folder table data ===
  build_folder_row() {
    local label="$1" dir="$2"
    local n=$(count_files "$dir")
    local w=$(count_words "$dir")
    local m=$(last_modif "$dir")
    [ -z "$m" ] && m="—"
    local wk=$(awk -v w=$w 'BEGIN { if (w>=1000) printf "%.1fk", w/1000; else print w }')
    echo "| $label | $n | $wk | $m |"
  }

  # === Production ===
  COMMITS_7D=$(git log --since="7 days ago" --oneline 2>/dev/null | wc -l | tr -d ' ')
  COMMITS_30D=$(git log --since="30 days ago" --oneline 2>/dev/null | wc -l | tr -d ' ')

  FILES_NEW_7D=$(git log --since="7 days ago" --diff-filter=A --name-only --pretty=format: 2>/dev/null \
    | grep -E '\.md$' | sort -u | wc -l | tr -d ' ')
  FILES_MOD_7D=$(git log --since="7 days ago" --diff-filter=M --name-only --pretty=format: 2>/dev/null \
    | grep -E '\.md$' | sort -u | wc -l | tr -d ' ')
  FILES_NEW_30D=$(git log --since="30 days ago" --diff-filter=A --name-only --pretty=format: 2>/dev/null \
    | grep -E '\.md$' | sort -u | wc -l | tr -d ' ')
  FILES_MOD_30D=$(git log --since="30 days ago" --diff-filter=M --name-only --pretty=format: 2>/dev/null \
    | grep -E '\.md$' | sort -u | wc -l | tr -d ' ')

  # === Métier — flux ===
  RDP_TOTAL=$(count_files "raw/revue-de-presse")
  RDP_LAST_FILE=$(ls -1t raw/revue-de-presse/*.md 2>/dev/null | head -1)
  RDP_LAST=$([ -n "$RDP_LAST_FILE" ] && basename "$RDP_LAST_FILE" .md || echo "")
  RDP_LAST_DATE=$([ -n "$RDP_LAST_FILE" ] && date -r "$RDP_LAST_FILE" "+%Y-%m-%d" || echo "")
  RDP_LAST_GAP=$(days_since "$RDP_LAST_DATE")
  RDP_30D=$(find raw/revue-de-presse -name "*.md" -newermt "30 days ago" 2>/dev/null | wc -l | tr -d ' ')

  NL_TOTAL=$(count_files "raw/newsletter")
  NL_LAST=$(ls -1t raw/newsletter/*.md 2>/dev/null | head -1 | xargs -I{} basename {} .md 2>/dev/null)
  NL_LAST_FILE=$(ls -1t raw/newsletter/*.md 2>/dev/null | head -1)
  NL_LAST_DATE=$([ -n "$NL_LAST_FILE" ] && date -r "$NL_LAST_FILE" "+%Y-%m-%d" || echo "")
  NL_LAST_GAP=$(days_since "$NL_LAST_DATE")

  ART_TOTAL=$(count_files "raw/articles")
  ART_LAST3=$(ls -1t raw/articles/*.md 2>/dev/null | head -3 | xargs -I{} basename {} .md 2>/dev/null)

  BRIEFS_RAW=$(count_files "raw/briefs")
  BRIEFS_WIKI=$(count_files "wiki/briefs")

  CONCEPTS=$(count_files "wiki/concepts")
  ENTITIES=$(count_files "wiki/entities")
  SOURCES=$(count_files "wiki/sources")
  SYNTHESES=$(count_files "wiki/syntheses")

  NOTES_RAW=$(count_files "raw/notes")

  # === Ratio raw → wiki ===
  RATIO=$(awk -v r=$RAW_FILES -v w=$WIKI_FILES 'BEGIN { if (r>0) printf "%.2f", w/r; else print "—" }')

  # === Wikilinks normalisés (basename uniquement, tous caractères acceptés) ===
  TMP_LINKS=$(mktemp)
  grep -rho '\[\[[^]]*\]\]' raw wiki 2>/dev/null \
    | sed -E 's/\[\[([^|#\]]+).*/\1/' \
    | grep -v ',' \
    | grep -vE '^[0-9]+$' \
    | awk -F'/' '{ print $NF }' \
    | sed -E 's/\]+$//' \
    | sort -u > "$TMP_LINKS"

  # === Top 10 hubs (basename normalisé) ===
  TOP_HUBS=$(grep -rho '\[\[[^]]*\]\]' raw wiki 2>/dev/null \
    | sed -E 's/\[\[([^|#\]]+).*/\1/' \
    | grep -v ',' \
    | grep -vE '^[0-9]+$' \
    | awk -F'/' '{ print $NF }' \
    | sed -E 's/\]+$//' \
    | sort | uniq -c | sort -rn | head -10 \
    | awk '{ count=$1; $1=""; sub(/^ */, ""); printf "- `[[%s]]` — **%d** backlinks\n", $0, count }')

  # === Orphelins (fichiers .md sans backlink) ===
  ORPHANS_COUNT=0
  ORPHAN_LIST=""
  while IFS= read -r f; do
    base=$(basename "$f" .md)
    if ! grep -qFx "$base" "$TMP_LINKS"; then
      ORPHANS_COUNT=$((ORPHANS_COUNT + 1))
      [ $ORPHANS_COUNT -le 10 ] && ORPHAN_LIST+="- \`$f\`\n"
    fi
  done < <(find raw wiki -type f -name "*.md" ! -name "dashboard.md" ! -name "index.md" ! -name "log.md" 2>/dev/null)
  rm -f "$TMP_LINKS"

  # === Heatmap commits 30 derniers jours ===
  HEATMAP=""
  for i in $(seq 29 -1 0); do
    DAY=$(date -v-${i}d "+%Y-%m-%d")
    N=$(git log --since="$DAY 00:00" --until="$DAY 23:59" --oneline 2>/dev/null | wc -l | tr -d ' ')
    case $N in
      0) HEATMAP+="·" ;;
      1|2) HEATMAP+="▁" ;;
      3|4) HEATMAP+="▃" ;;
      5|6|7) HEATMAP+="▅" ;;
      *) HEATMAP+="█" ;;
    esac
  done

  # === Streak (jours consécutifs avec commit, en partant d'aujourd'hui) ===
  STREAK=0
  for i in $(seq 0 60); do
    DAY=$(date -v-${i}d "+%Y-%m-%d")
    N=$(git log --since="$DAY 00:00" --until="$DAY 23:59" --oneline 2>/dev/null | wc -l | tr -d ' ')
    if [ "$N" -gt 0 ]; then
      STREAK=$((STREAK + 1))
    else
      break
    fi
  done

  # === Dossiers inactifs > 14j ===
  STALE_LIST=""
  for d in raw/articles raw/notes raw/briefs raw/journal raw/newsletter raw/revue-de-presse \
           wiki/concepts wiki/entities wiki/sources wiki/syntheses wiki/briefs wiki/audit; do
    [ ! -d "$d" ] && continue
    LM=$(last_modif "$d")
    [ -z "$LM" ] && STALE_LIST+="- \`$d\` — vide ou jamais modifié\n" && continue
    GAP=$(days_since "$LM")
    if [ "$GAP" != "?" ] && [ "$GAP" -gt 14 ]; then
      STALE_LIST+="- \`$d\` — dernière modif il y a **${GAP}j** ($LM)\n"
    fi
  done

  # === État des LaunchAgents ===
  LA_STATUS=""
  for label in revue-presse recap-jour refresh-snapshots dashboard; do
    JOB="com.timboussardon.${label}"
    if launchctl list "$JOB" >/dev/null 2>&1; then
      EXIT=$(launchctl list "$JOB" | grep LastExitStatus | grep -oE '[0-9]+' | head -1)
      [ -z "$EXIT" ] && EXIT="—"
      LAST_LOG=$(ls -t "$LOG_DIR/${label}-"*.log 2>/dev/null | head -1)
      LAST_DATE=$([ -n "$LAST_LOG" ] && date -r "$LAST_LOG" "+%Y-%m-%d %H:%M" || echo "jamais")
      EMOJI="✓"
      [ "$EXIT" != "0" ] && [ "$EXIT" != "—" ] && EMOJI="✗"
      LA_STATUS+="| ${label} | ${LAST_DATE} | ${EXIT} | ${EMOJI} |\n"
    else
      LA_STATUS+="| ${label} | non chargé | — | ⚠️ |\n"
    fi
  done

  # === Couverture revue-presse 30j ===
  RDP_COVERAGE=$(awk -v n=$RDP_30D 'BEGIN { printf "%.0f", n*100/30 }')

  # === Mots totaux ===
  TOTAL_WORDS=$(find raw wiki -type f -name "*.md" -print0 2>/dev/null | xargs -0 cat 2>/dev/null | wc -w | tr -d ' ')
  TOTAL_WORDS_K=$(awk -v w=$TOTAL_WORDS 'BEGIN { printf "%.0fk", w/1000 }')

  # === Génération du markdown ===
  cat > "$OUT" <<MARKDOWN
# 📊 Dashboard SEO KB

*Généré automatiquement le ${NOW} — actualisé chaque jour à 09:30*

## 🗂️ Volume du vault

- **${TOTAL_FILES} fichiers** markdown (${RAW_FILES} dans \`raw/\`, ${WIKI_FILES} dans \`wiki/\`)
- **${TOTAL_WORDS_K} mots** au total
- **${WIKILINKS} wikilinks** (moyenne ${AVG_LINKS} / fichier)
- **Ratio raw→wiki** : ${RATIO} *(< 1 = matière brute pas encore synthétisée)*

### Détail par dossier

| Dossier | Fichiers | Mots | Dernière modif |
|---------|---------:|-----:|:--------------:|
$(build_folder_row "raw/articles" "raw/articles")
$(build_folder_row "raw/notes" "raw/notes")
$(build_folder_row "raw/revue-de-presse" "raw/revue-de-presse")
$(build_folder_row "raw/newsletter" "raw/newsletter")
$(build_folder_row "raw/journal" "raw/journal")
$(build_folder_row "raw/briefs" "raw/briefs")
$(build_folder_row "raw/etudes-seo" "raw/etudes-seo")
$(build_folder_row "raw/papers" "raw/papers")
$(build_folder_row "raw/cas-clients" "raw/cas-clients")
$(build_folder_row "wiki/concepts" "wiki/concepts")
$(build_folder_row "wiki/entities" "wiki/entities")
$(build_folder_row "wiki/sources" "wiki/sources")
$(build_folder_row "wiki/syntheses" "wiki/syntheses")
$(build_folder_row "wiki/briefs" "wiki/briefs")
$(build_folder_row "wiki/queries" "wiki/queries")
$(build_folder_row "wiki/posts-linkedin" "wiki/posts-linkedin")
$(build_folder_row "wiki/revues-presse" "wiki/revues-presse")
$(build_folder_row "wiki/audit" "wiki/audit")

## 📈 Production

### 7 derniers jours
- **${COMMITS_7D}** commits
- **${FILES_NEW_7D}** fichiers créés
- **${FILES_MOD_7D}** fichiers modifiés

### 30 derniers jours
- **${COMMITS_30D}** commits
- **${FILES_NEW_30D}** fichiers créés
- **${FILES_MOD_30D}** fichiers modifiés

## 📰 Flux métier

### Revue de presse "Algorithme"
- **${RDP_TOTAL}** éditions publiées (${RDP_30D} sur les 30 derniers jours)
- Dernière édition : \`${RDP_LAST:-aucune}\` (il y a ${RDP_LAST_GAP}j)
- **Couverture 30j** : ${RDP_30D}/30 (${RDP_COVERAGE}%)

### Newsletter
- **${NL_TOTAL}** newsletters
- Dernière : \`${NL_LAST:-aucune}\` (il y a ${NL_LAST_GAP}j)

### Articles longs
- **${ART_TOTAL}** articles
- 3 derniers :
$(echo "$ART_LAST3" | awk '{ printf "  - `%s`\n", $0 }')

### Briefs & analyses
- **${BRIEFS_RAW}** briefs raw + **${BRIEFS_WIKI}** briefs wiki

### Wiki structuré
- **${CONCEPTS}** concepts · **${ENTITIES}** entités · **${SOURCES}** sources · **${SYNTHESES}** synthèses

### Notes brutes (input flow)
- **${NOTES_RAW}** notes raw

## 🕸️ Graphe & maillage

### Top 10 hubs (les plus cités)

${TOP_HUBS:-aucun wikilink détecté}

### Orphelins (sans backlink) : **${ORPHANS_COUNT}**

$(echo -e "$ORPHAN_LIST" | head -20)
$([ $ORPHANS_COUNT -gt 10 ] && echo "*(${ORPHANS_COUNT} au total — voir \`wiki/audit\` pour la liste complète)*")

## 🔥 Activité git

\`\`\`
30j: ${HEATMAP}
       (· = 0, ▁ = 1-2, ▃ = 3-4, ▅ = 5-7, █ = 8+)
\`\`\`

**Streak actuel** : ${STREAK} jour(s) consécutif(s) avec commit

### Dossiers inactifs > 14j

$(echo -e "${STALE_LIST:-*Aucun — tout est actif*}")

## 🤖 Automatisations (LaunchAgents)

| Job | Dernier run | Exit | État |
|-----|-------------|-----:|:----:|
$(echo -e "$LA_STATUS")

---

*Source : \`/Users/timothee/Code/seo-kb/wiki/dashboard.md\` · Régénéré par \`com.timboussardon.dashboard\` (LaunchAgent quotidien 09:30)*
MARKDOWN

  echo ""
  echo "Dashboard généré : $OUT ($(wc -l < "$OUT") lignes)"
  echo ""
  echo "--- auto-commit wiki/dashboard.md ---"
  git add wiki/dashboard.md 2>/dev/null || true
  if git diff --cached --quiet; then
    echo "Pas de changement, rien à commit."
  else
    git -c user.email="noreply@anthropic.com" -c user.name="dashboard-cron" \
      commit -m "Dashboard ${TODAY} (auto)"
    if git push origin main; then
      echo "Pushed."
    else
      echo "WARN: git push failed."
    fi
  fi
  echo "=== dashboard run ended at $(date -Iseconds) ==="
} >> "$LOG_FILE" 2>&1
