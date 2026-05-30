#!/bin/bash
# Rapport automatique des emails lifecycle Fusionn → vault Obsidian.
# Récupère les stats par séquence (taux d'ouverture / clic) depuis Supabase et
# écrit un rapport markdown daté dans seo-kb/fusionn/rapports-emails/.
# La clé service_role est récupérée à la volée via la CLI Supabase (jamais en dur).
# Planifié par launchd (co.fusionn.email-report). Lançable à la main aussi.
set -euo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

REF="fwhfnzbtlddzfxbsejyf"
URL="https://${REF}.supabase.co"
OUTDIR="$HOME/Code/seo-kb/fusionn/rapports-emails"
DATE="$(date +%F)"
OUT="$OUTDIR/${DATE}-rapport-emails.md"
mkdir -p "$OUTDIR"

# Clé service_role via la CLI (authentifiée localement)
SRK=""
for i in 1 2 3 4 5; do
  SRK=$(supabase projects api-keys --project-ref "$REF" 2>/dev/null | grep -i "service_role" | grep -oE "eyJ[A-Za-z0-9._-]+") || true
  [ -n "$SRK" ] && break; sleep 2
done
[ -z "$SRK" ] && { echo "Clé service_role introuvable" >&2; exit 1; }

STATS=$(curl -s "$URL/rest/v1/email_stats_by_sequence?select=*" -H "apikey: $SRK" -H "Authorization: Bearer $SRK")

# Noms lisibles + ordre du parcours
LABELS='{
  "activation_no_search":"Activation (inscrit, 0 analyse)",
  "nudge_after_1_search":"Après 1 analyse",
  "nudge_after_2_searches":"Après 2 analyses",
  "reengage_inactive":"Réengagement (inactif 14j)",
  "premium_click_no_purchase":"Premium (clic sans achat)",
  "premium_onboarding":"Onboarding premium"
}'
ORDER='["activation_no_search","nudge_after_1_search","nudge_after_2_searches","reengage_inactive","premium_click_no_purchase","premium_onboarding"]'

ROWS=$(echo "$STATS" | jq -r --argjson lab "$LABELS" --argjson ord "$ORDER" '
  (map({(.sequence_key): .}) | add // {}) as $bykey
  | $ord[] as $k
  | ($bykey[$k]) as $r
  | ($r.sent // 0) as $s | ($r.opened // 0) as $o | ($r.clicked // 0) as $c
  | "| \($lab[$k]) | \($s) | \($o) | " +
    (if $s>0 then (($o*1000/$s|floor)/10|tostring)+" %" else "—" end) + " | \($c) | " +
    (if $s>0 then (($c*1000/$s|floor)/10|tostring)+" %" else "—" end) + " |"')

TOTAL_SENT=$(echo "$STATS" | jq '[.[].sent] | add // 0')
TOTAL_OPEN=$(echo "$STATS" | jq '[.[].opened] | add // 0')
NOTE=""
if [ "${TOTAL_OPEN:-0}" = "0" ] && [ "${TOTAL_SENT:-0}" != "0" ]; then
  NOTE=$'\n> ⚠️ Aucune ouverture enregistrée. Si le suivi vient d'\''être activé c'\''est normal, sinon vérifier que le suivi des ouvertures est activé sur le domaine Resend et que le webhook reçoit bien les événements.'
fi

cat > "$OUT" <<EOF
---
type: rapport
sujet: emails-lifecycle-fusionn
date: ${DATE}
---

# Rapport emails lifecycle Fusionn — ${DATE}

Total envoyés : **${TOTAL_SENT}** · ouvertures enregistrées : **${TOTAL_OPEN}**

| Séquence | Envoyés | Ouverts | Taux d'ouverture | Clics | Taux de clic |
|---|---|---|---|---|---|
${ROWS}
${NOTE}

> Note : le taux d'ouverture est indicatif (Apple Mail et Gmail faussent la mesure). Le taux de clic est le signal fiable.

*Généré automatiquement depuis Supabase (\`email_stats_by_sequence\`).*
EOF

echo "Rapport écrit : $OUT"
