---
title: "Jour 1 Semaine 4 — Audit Core Web Vitals (skill distribuable + pédagogie)"
bootcamp: 4
semaine: 4
jour: 1
type: skill-distribuable
usage: "Bundle Drive S4 J1. Skill HORS pack des 9, vraie nouvelle install. Audit Lighthouse local mobile sur 50 pages du sitemap, rapport priorisé sur les 5 pires URLs. Livré en pack tech avec [[skill-donnees-structurees]] sur le même jour."
related:
  - "[[skill-donnees-structurees]]"
  - "[[skill-maillage-systeme]]"
  - "[[session-3-audit-prep]]"
  - "[[observations-whatsapp-bootcamp]]"
---

# Jour 1 Semaine 4 — L'audit perf qui sort un plan de correction, pas un score

Salut à tous,

Deuxième livrable du J1 S4. Un skill d'audit Core Web Vitals qui crawle ton sitemap, passe Lighthouse mobile sur 50 pages en parallèle, et sort un rapport avec les 5 pires URLs à corriger en priorité, le LCP element identifié page par page, et le breakdown qui dit où le temps part. Pas un PDF PageSpeed copié-collé, un vrai diagnostic exploitable.

## Pourquoi c'est dans la semaine automatisations

Un audit qui te prend quatre heures à faire à la main page par page, c'est un audit que tu fais une fois et que tu ne refais jamais. Donc tu ne mesures rien, donc tu ne sais pas si tes corrections ont bougé l'aiguille chez ton client. Un audit qui tourne en huit minutes te permet de re-mesurer après chaque chantier. C'est ça qui transforme la perf SEO en cycle d'amélioration et pas en mission ponctuelle qu'on ressort en rapport tous les six mois.

Concrètement chez ton client : tu poses un baseline en début de mission, tu corriges les cinq pires, tu re-mesures la semaine d'après, tu prouves le gain en chiffres. PageSpeed Insights cliqué URL par URL, tu peux oublier, ça prend des jours et tu n'as pas l'historique.

## Les 3 règles, en clair

- Mobile uniquement. Google indexe en mobile-first. Auditer en desktop, c'est mesurer ce qui ne compte pas pour le ranking.
- Pas de score halluciné. Si une URL timeout ou crash, elle est marquée ERROR dans le rapport. Pas un 0, pas un placeholder. Un audit qui invente des chiffres est pire qu'un audit qu'on ne fait pas, parce qu'il oriente vers de mauvaises corrections.
- Pas de reco sans opportunity Lighthouse correspondante. Le skill ne sort jamais "tu devrais optimiser X" si Lighthouse n'a pas remonté X sur cette page. On reste collé au diagnostic réel, pas aux best practices génériques.

## Le piège à éviter

Lire le score perf global et s'arrêter là. Le score est une moyenne pondérée, il cache souvent un seul vrai problème, typiquement le LCP image découverte tardivement. Le skill te sort le LCP element par page avec son selector CSS, et le breakdown (TTFB, load delay, render delay) qui dit exactement où le temps part. C'est ça que tu vises pour intervenir. Le score, c'est juste l'étiquette qu'on montre au client.

Autre piège : extrapoler "tout le site" à partir de 50 URLs sur 2000. L'échantillon est honnête, le rapport le précise dans ses limites. À toi de le redire au client sans le maquiller.

## Pré-requis

Lighthouse en CLI sur ta machine (`npm install -g lighthouse`) et `jq` (`brew install jq`). Sans ça, le skill s'arrête et te demande d'installer, il n'installe rien tout seul derrière ton dos.

Si tu n'as pas Node, `brew install node` d'abord. Si tu n'as pas Homebrew, on le pose en MP, pas jeudi. Compte cinq minutes pour tout poser.

Site WordPress, Webflow, Squarespace, PHP custom, peu importe : le skill crawle le sitemap public, il ne touche jamais ton stack. Ce qu'il mesure, c'est ce que voit le navigateur d'un visiteur. Pas besoin d'accès serveur, pas besoin de plugin.

---

## Procédure d'install / vérification

Skill HORS pack des 9. Vraie nouvelle install, un seul fichier.

1. Dossier `~/.claude/skills/seo-core-web-vitals/`
2. `SKILL.md` = le bloc entre `=====` ci-dessous
3. Relance Claude, vérifie avec `/skills` (tu dois voir `seo-core-web-vitals` dans la liste)

Pas de sous-dossier `references/` ici, contrairement au skill données structurées. Juste le SKILL.md, un seul fichier.

Vérification rapide après install : tape `which lighthouse` dans ton terminal, ça doit répondre un chemin (genre `/usr/local/bin/lighthouse`). Si ça ne répond rien, `npm install -g lighthouse` (peut demander sudo selon ta config Node).

Déclenchement : il part dès que tu dis "audit Core Web Vitals", "audit CWV", "perf SEO", "LCP CLS TBT", "Lighthouse audit", "vitesse de chargement", "audit performance site", "PageSpeed score", ou tu l'appelles avec `/seo-core-web-vitals`.

Premier audit conseillé : ton propre site. Tu verras tout de suite la lecture du rapport, et tu repèreras les patterns que tu retrouveras chez les clients (typiquement images hero non préloadées, scripts tiers bloquants, CLS dû à des pubs ou des fonts).

Node, Lighthouse ou jq qui coincent ? MP aujourd'hui, pas jeudi.

=====

---
name: seo-core-web-vitals
description: |
  Audit Core Web Vitals (LCP, CLS, TBT) d'un site via Lighthouse local sur un échantillon d'URLs depuis sitemap.xml. Mobile-first. Produit un tableau de scores par URL + problèmes récurrents site-wide + plan de correction priorisé pour les 5 pires pages.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "audit Core Web Vitals", "audit CWV", "perf SEO", "LCP CLS TBT", "Lighthouse audit", "vitesse de chargement", "audit performance site", "pourquoi mon site est lent en SEO", "PageSpeed score", "audit perf mobile", "score Lighthouse", "audit Web Vitals".

  Skill du périmètre SEO technique. Complémentaire de `indexation-check`, `seo-donnees-structurees`, `seo-cannibalisation`, `maillage-systeme`.
---

# Skill — Audit Core Web Vitals (Lighthouse local)

## Quand déclencher

Diagnostic de performance SEO d'un site complet, ou avant intervention technique (refonte, optimisation perf, migration). Toujours mobile (Google = mobile-first indexing).

## Pré-requis (à vérifier en début de skill)

```bash
which lighthouse || echo "MANQUANT — installer : npm install -g lighthouse"
which jq || echo "MANQUANT — installer : brew install jq"
```

Si Lighthouse manque, proposer `npm install -g lighthouse` à l'utilisateur et stopper. Ne pas installer silencieusement.

Alternative sans install globale : remplacer `lighthouse` par `npx lighthouse` dans toutes les commandes (premier lancement plus lent).

## Input requis

| Source | Obligatoire | Défaut |
|--------|-------------|--------|
| URL du sitemap.xml (ex. `https://site.com/sitemap.xml`) | Oui | — |
| Échantillon | Non | 50 URLs |
| Mode `all` (audit toutes les URLs du sitemap) | Non | off |

## Pipeline (5 étapes)

### Étape 1 — Récupérer le sitemap

```bash
SITEMAP_URL="<url>"
curl -sL "$SITEMAP_URL" | grep -oE '<loc>[^<]+</loc>' | sed -E 's|</?loc>||g' > /tmp/cwv-urls.txt
wc -l /tmp/cwv-urls.txt
```

**IMPORTANT (compat BSD/macOS)** : utiliser `sed -E 's|</?loc>||g'` et **PAS** `sed 's|</\?loc>||g'` — le `\?` ne marche pas en sed BSD (macOS) et laisse les balises intactes silencieusement.

**Si le sitemap est un index** (contient `<sitemapindex>` au lieu de `<urlset>`), récupérer le premier sitemap enfant et l'utiliser :

```bash
FIRST_CHILD=$(curl -sL "$SITEMAP_URL" | grep -oE '<loc>[^<]+</loc>' | sed -E 's|</?loc>||g' | head -1)
curl -sL "$FIRST_CHILD" | grep -oE '<loc>[^<]+</loc>' | sed -E 's|</?loc>||g' > /tmp/cwv-urls.txt
```

### Étape 2 — Échantillonner

```bash
TOTAL=$(wc -l < /tmp/cwv-urls.txt | tr -d ' ')
if [ "$TOTAL" -gt 50 ] && [ "$MODE" != "all" ]; then
  head -50 /tmp/cwv-urls.txt > /tmp/cwv-sample.txt
else
  cp /tmp/cwv-urls.txt /tmp/cwv-sample.txt
fi
wc -l /tmp/cwv-sample.txt
```

Les 50 premières URLs du sitemap sont généralement les plus prioritaires (homepage, hubs, top articles). Si l'utilisateur demande `all`, auditer toutes les URLs.

### Étape 3 — Lancer Lighthouse mobile en parallèle (3 workers)

```bash
rm -rf /tmp/cwv-results /tmp/cwv-errors.log
mkdir -p /tmp/cwv-results
cat /tmp/cwv-sample.txt | xargs -I {} -P 3 sh -c '
  url="$1"
  hash=$(echo -n "$url" | md5)
  lighthouse "$url" \
    --output=json \
    --output-path="/tmp/cwv-results/${hash}.json" \
    --only-categories=performance \
    --form-factor=mobile \
    --screenEmulation.mobile=true \
    --chrome-flags="--headless=new --no-sandbox" \
    --quiet 2>/dev/null || echo "FAIL: $url" >> /tmp/cwv-errors.log
' _ {}
echo "Results: $(ls /tmp/cwv-results/ 2>/dev/null | wc -l | tr -d ' ')"
[ -f /tmp/cwv-errors.log ] && echo "Errors:" && cat /tmp/cwv-errors.log
```

**IMPORTANT (zsh-safe)** : utiliser `rm -rf /tmp/cwv-results && mkdir -p /tmp/cwv-results` et **PAS** `rm -f /tmp/cwv-results/*` — le glob vide fait gueuler zsh (`no matches found`) et l'exit code 1 peut interrompre la suite.

**`--headless=new`** (et pas `--headless` legacy) — plus stable depuis Chrome 109+, requis pour Lighthouse 13.

**Compter** : ~15-30 secondes par URL avec 3 workers parallèles. 50 URLs ≈ 5-10 min.

### Étape 4 — Parser les résultats

Pour chaque JSON dans `/tmp/cwv-results/`, extraire avec jq (chemin Lighthouse 13) :

```bash
for f in /tmp/cwv-results/*.json; do
  jq '{
    url: .finalDisplayedUrl,
    lcp_ms: (.audits."largest-contentful-paint".numericValue // 0),
    cls: (.audits."cumulative-layout-shift".numericValue // 0),
    tbt_ms: (.audits."total-blocking-time".numericValue // 0),
    score: ((.categories.performance.score // 0) * 100),
    lcp_element: [.audits."lcp-breakdown-insight".details.items[]? | select(.type == "node") | {selector, snippet, nodeLabel}] | .[0],
    lcp_breakdown: [.audits."lcp-breakdown-insight".details.items[]? | select(.type == "table") | .items[]? | {subpart, label, duration_ms: .duration}],
    opportunities: [.audits | to_entries[] | select(.value.details.type == "opportunity" and (.value.details.overallSavingsMs // 0) > 100) | {id: .key, title: .value.title, savings_ms: .value.details.overallSavingsMs}] | sort_by(-.savings_ms) | .[0:5]
  }' "$f"
done | jq -s '.' > /tmp/cwv-parsed.json
echo "Parsed: $(jq 'length' /tmp/cwv-parsed.json) URLs"
```

**Chemins clés Lighthouse 13** :
- URL finale : `.finalDisplayedUrl` (et **PAS** `.finalUrl` qui peut être null)
- LCP element : `.audits."lcp-breakdown-insight".details.items[] | select(.type == "node")` (et **PAS** `.audits."largest-contentful-paint-element"` qui est null depuis LH 13)
- LCP breakdown (TTFB / render delay / load delay) : `.audits."lcp-breakdown-insight".details.items[] | select(.type == "table") | .items[]` — utile pour diagnostiquer **où** se passe le temps LCP

**Seuils Google (à appliquer pour le verdict)** :

| Métrique | Good | Needs Improvement | Poor |
|----------|------|-------------------|------|
| LCP | < 2500 ms | 2500-4000 ms | > 4000 ms |
| CLS | < 0.1 | 0.1-0.25 | > 0.25 |
| TBT (proxy INP) | < 200 ms | 200-600 ms | > 600 ms |
| Score perf | ≥ 90 | 50-89 | < 50 |

### Étape 5 — Produire le rapport markdown

Voir section "Output obligatoire" ci-dessous.

### Étape 4bis — Détection automatique du pattern "redirect sitemap"

Si l'opportunity `redirects` apparaît sur **>50% des pages auditées** avec un gain moyen >300ms : c'est quasi-certainement un mismatch de trailing slash entre le sitemap et le serveur.

```bash
REDIRECT_COUNT=$(jq -r '.[] | .opportunities[] | select(.id == "redirects") | .id' /tmp/cwv-parsed.json | wc -l | tr -d ' ')
TOTAL=$(jq 'length' /tmp/cwv-parsed.json)
if [ "$REDIRECT_COUNT" -gt $((TOTAL / 2)) ]; then
  echo "⚠️ ALERTE : $REDIRECT_COUNT/$TOTAL pages ont une redirection. Vérifier le trailing slash du sitemap vs serveur."
fi
```

Ce pattern doit être mis EN TÊTE du rapport — c'est le quick win le plus rentable quand il est présent.

## Output obligatoire

```markdown
# Audit Core Web Vitals — [domaine] — [date]

**Échantillon** : X URLs auditées / Y URLs dans le sitemap. **Form factor** : mobile.
**Note importante** : INP non mesurable en local par Lighthouse (métrique field). TBT utilisé comme proxy.

## Scores par URL

| URL | LCP | CLS | TBT | Score | Verdict |
|-----|-----|-----|-----|-------|---------|
| / | 1.8s ✅ | 0.05 ✅ | 150ms ✅ | 92 | Good |
| /blog/article-x | 4.2s ❌ | 0.18 ⚠️ | 720ms ❌ | 38 | Poor |
| /categorie/y | — | — | — | — | ERROR (timeout) |

Légende : ✅ Good — ⚠️ Needs Improvement — ❌ Poor

## Synthèse

- **X/Y pages** sont en Poor (score < 50)
- **X/Y pages** ont un LCP > 4s (critique pour le ranking)
- **X/Y pages** ont un CLS > 0.25 (UX dégradée)
- Score perf médian : X / Score perf moyen : Y

## Problèmes récurrents site-wide

Opportunities Lighthouse qui apparaissent sur > 30% des pages auditées :

1. **Unused JavaScript** — X pages affectées — gain moyen estimé : Xs
   - Cause probable : [bundle non tree-shaké / scripts tiers (analytics, chat, ads)]
2. **Render-blocking resources** — X pages — gain moyen : Xs
3. **Image sizing / Properly size images** — X pages — gain moyen : Xs
4. **Largest Contentful Paint image** — X pages — gain moyen : Xs
5. **Reduce JavaScript execution time** — X pages — gain moyen : Xs

## Top 5 pages à corriger en priorité

(triées par score perf croissant)

### 1. /blog/article-x (score : 38)
- **LCP** : 4.2s ❌ — élément : `<img class="hero" src="...">` (selector : `main > article > img.hero`)
  - Breakdown : TTFB 800ms / load delay 1200ms / load duration 1500ms / render delay 700ms
  - → Le gros du temps part en **load delay** (image découverte tardivement)
- **CLS** : 0.18 ⚠️ — shifts probables : pub Adsense / images sans dimensions
- **TBT** : 720ms ❌ — JS bloquant : [scripts identifiés]

**Plan de correction** :
1. Préload de l'image hero LCP + `fetchpriority="high"`
2. Définir width/height explicites sur toutes les images du contenu
3. Defer les scripts non critiques (analytics, chat) — passer en `loading="lazy"` les iframes

**Lecture du LCP breakdown** :
- TTFB > 600ms → problème serveur / CDN / cache
- Load delay > 200ms → image LCP pas dans le HTML initial (lazy, dans CSS background, JS-injectée)
- Load duration > 500ms → image trop lourde ou pas servie en format moderne (avif/webp)
- Render delay > 300ms → blocage CSS/JS render-blocking ou hydratation lente

### 2. ...

(répéter pour les 5 plus mauvaises)

## Limites de l'audit

- INP non mesuré (Lighthouse lab → TBT comme proxy)
- Pas de variation par device réel (émulation Moto G Power)
- Pas de mesure sur connexion réelle (throttling 4G simulé)
- Pour les vraies données field : croiser avec PageSpeed Insights API ou CrUX
```

## Règles absolues

- **Mobile uniquement** — Google indexe en mobile-first. Pas de desktop par défaut.
- **INP non mesuré** — toujours préciser dans le rapport que TBT est utilisé comme proxy.
- **Pas de score halluciné** — si une URL échoue (timeout, 404, JS error), la marquer `ERROR` dans le tableau, pas `0` ou un placeholder.
- **Pas de reco sans opportunity Lighthouse correspondante** — ne pas inventer "il faudrait optimiser X" si Lighthouse ne l'a pas remonté pour cette page.
- **Pas d'installation silencieuse** — si Lighthouse manque, demander à l'utilisateur de l'installer.
- **Échantillon honnête** — si l'échantillon est de 50/2000 URLs, le dire clairement, ne pas extrapoler "tout le site" à partir de 2,5% du contenu.

## Edge cases

- **Sitemap index** (sitemapindex au lieu d'urlset) → récupérer le premier child + l'utiliser, signaler à l'utilisateur qu'il peut spécifier un sitemap enfant précis pour cibler.
- **Sitemap protégé** (auth, 403) → demander à l'utilisateur un export local des URLs.
- **Plus de 500 URLs avec mode `all`** → confirmer avec l'utilisateur (sera lent : 500 URLs × ~10s/3 workers ≈ 30 min).
- **Site en SPA ou auth-walled** → certaines pages peuvent timeout, c'est normal, les marquer ERROR.
- **Sitemap multi-langues** → garder tel quel, le rapport montrera les écarts par locale.

=====

## Note pour Tim (interne)

- **Positionnement J1 S4.** Livré avec [[skill-donnees-structurees]] comme pack tech du J1. Cohérence : les deux sont des skills HORS pack des 9, vraie nouvelle install, périmètre technique. Données-structurées = écrire le balisage qui se génère depuis le contenu. CWV = mesurer ce qui se passe avant/après une intervention tech. Pair logique pour ouvrir la semaine.
- **Hors thème automatisation strict.** Le skill est un AUDIT, pas une automatisation au sens "ce qui se génère depuis ta donnée". Mais il rend mesurable le bénéfice des automatisations qu'on pose dans la semaine. À cadrer en intro de session : "celui-là sert à prouver que les autres marchent". Alternative de framing : l'audit lui-même est automatisé (Lighthouse + parsing + rapport en une commande au lieu de quatre heures à la main), donc c'est cohérent avec le thème "ce qui peut tourner tout seul, doit tourner tout seul".
- **Risque audience identique à données structurées.** Skill technique (CLI, Node, jq). Les WordPress-only sans terminal vont décrocher. Section "Pré-requis" rabat ça : on cadre en MP. À marteler J1 que l'install se fait UNE fois et qu'après c'est juste une question d'invoquer le skill.
- **Source canonique.** Le skill vit dans `~/.claude/skills/seo-core-web-vitals/SKILL.md`. Single file (pas de sous-dossier `references/`). Si tu fais évoluer le skill, régénère ce bundle.
- **Compat macOS.** Le SKILL.md utilise `md5` (commande native macOS). Sur Linux ce serait `md5sum`. La quasi-totalité du bootcamp est sur Mac d'après les sessions précédentes (Romain, Anthony, etc.). Si un participant remonte `md5: command not found`, c'est qu'il est sur Linux, patcher en MP en remplaçant `md5` par `md5sum` dans la commande de l'étape 3.
- **Limites du skill à rappeler en session.** Pas d'INP (métrique field-only, Lighthouse lab utilise TBT comme proxy). Pas de variation device réel (émulation Moto G Power). Pas de connexion réelle (throttling 4G simulé). Pour les vraies données field : croiser avec PageSpeed Insights API ou CrUX. Potentiel skill futur si la demande monte.
- **Normalisation.** Doc sans em-dashes dans la partie pédagogique (règle maison). Le bloc SKILL.md est reproduit verbatim depuis `~/.claude/skills/seo-core-web-vitals/` et conserve ses em-dashes techniques.
