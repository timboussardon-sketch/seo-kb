---
title: Workflow audit SEO — version bootcamp 4 (resserrée)
derive-de: "Workflow V3 — Méthodologie Timothée Boussardon, avril 2026"
version: "Bootcamp 4, mai 2026"
principe: "100% données Google + structure éditoriale. Aucun outil payant tiers (Claude Pro 20€/mois + GSC + Chrome)."
phases: 7
related:
  - "[[sequencage-semaine-3]]"
  - "[[session-3-audit-prep]]"
---

# Faire un audit SEO avec Claude 

Version bootcamp 4 du workflow audit. Dérivée du V3, **resserrée sur l'audit technique + structurel** : on retire la partie stratégie de contenu (clusters AEO, analyse vectorielle, briefs de réécriture), on ajoute l'audit d'indexation et l'audit structurel Hn. Le maillage tourne sur **deux passes** : structurelle (`maillage-systeme`) puis data GSC (`maillage-interne-gsc`).

**Règles de scrapping de l'audit :**
- Analyse des URLs de votre site
- Les données viennent de la GSC + la recherche web Claude (qui montre qui est visible) + le crawl Chrome de vos pages
- Aucun outil payant tiers : Claude Pro (20€/mois) + données gratuites de Google

**Les 7 phases :**

| Phase | Skill | Source | Durée |
|-------|-------|--------|-------|
| 0 · Positionnement | aucun (prompt) | GSC + recherche web | 20-30 min |
| 1 · Indexation | `indexation-check` | sitemap + URLs (lecture web publique) | 15-25 min |
| 2 · Quick Wins | `seo-quick-win` | GSC + Chrome | 15-20 min |
| 3 · Audit structurel Hn | aucun (prompt + scrap) | sitemap complet + Chrome/curl + GSC | variable (scale sitemap) |
| 4 · Cannibalisations | `seo-cannibalisation` | GSC + Chrome | 15-20 min |
| 5 · Maillage interne | `maillage-systeme` + `maillage-interne-gsc` | Chrome (crawl liens) + GSC | 25-40 min |
| 6 · Synthèse + plan | aucun (synthèse Claude) | résultats Phases 0-5 | 20-30 min |

Une phase nourrit la suivante. Budget total : 3-4,5h, étalable (la Phase 3 dépend de la taille du sitemap).

---

## PHASE 0 — Audit de positionnement

**Skill** : aucun. Collecte de données.
**Source** : export GSC + recherche web Claude.
**Durée** : 20-30 min.

### Prompt exact

```
Voici mon export GSC [période].
Et voici mes 5-10 requêtes business principales : [liste]

1. Pour chaque requête business, analyse mes données GSC :
   - Ma position moyenne
   - Mes impressions et clics
   - Mon CTR (et l'écart avec le CTR attendu pour cette position)
   - L'URL qui ranke

2. Identifie les requêtes business où je n'apparais PAS dans la GSC
   → Ce sont mes gaps critiques

3. Via recherche web, pour chaque requête business (y compris mes gaps) :
   - Quels types de résultats dominent ? (guides, outils, pages services, annuaires)
   - Y a-t-il des AI Overviews actifs sur cette requête ?
   - Quels acteurs sont visibles en top 3 ? (juste noms et URLs, pas de scrapping)

4. Depuis la GSC, identifie les requêtes à fort volume où je ranke
   mais qui ne sont PAS dans ma liste de requêtes business
   → Ce sont mes opportunités cachées

Génère un tableau de synthèse :
| Requête | Position GSC | Impressions | CTR | CTR attendu | Gap CTR | Type SERP | Priorité |
```

### Output attendu

- Tableau de positionnement par requête (données GSC réelles)
- Gaps : requêtes business sans présence
- Opportunités cachées : requêtes GSC à fort volume non exploitées
- Types de SERP par requête (via recherche web)

### Ce que ça nourrit

→ Phase 1 (un gap est-il dû à une page non indexée ?) → Phase 2 (pages sous-performantes = quick wins) → Phase 3 (le Hn des pages business répond-il à l'intention ?) → Phase 6 (les gaps alimentent l'horizon "nouvelles pages").

---

## PHASE 1 — Audit d'indexation

**Skill** : `indexation-check`.
**Source** : sitemap.xml + liste d'URLs du site (un export `articles.ts` / `wiki.ts` / `urls.txt` fait aussi l'affaire). Lecture seule sur le web public. **Aucune GSC ni Chrome requis** — c'est la phase la plus accessible, à dérouler tôt.
**Durée** : 15-25 min.

### Étape 1A — Inventaire des URLs

Croiser deux listes :
- Les URLs du sitemap.xml
- Les URLs vues par Google dans la GSC (Phase 0)

Repérer les écarts : URL active en GSC mais absente du sitemap ; URL au sitemap que Google n'a jamais servie.

### Étape 1B — Lancer `indexation-check`

Sur chaque URL, le skill vérifie 9 points : statut HTTP, blocages techniques (robots.txt, X-Robots-Tag), directive noindex, sitemap (présence + `lastmod` + cohérence), maillage interne entrant, longueur de contenu, statut d'indexation Google estimé.

⚠️ Distinguer strictement **« non indexée »** et **« non testable »** (rate-limit Google). Aucune action de forçage, lecture seule.

### Output attendu

- Rapport d'indexation : anomalies **critiques en tête** (page business non indexée, noindex oublié, sitemap périmé), anomalies mineures, recommandations priorisées
- Liste claire : indexées / non indexées / non testables

### Ce que ça nourrit

→ Phase 2 (une page non indexée ne sera JAMAIS un quick win) → Phase 6 (le déblocage d'indexation va dans l'horizon Semaine 1-2).

---

## PHASE 2 — Quick Wins

**Skill** : `seo-quick-win`.
**Source** : export GSC + Chrome (mon site).
**Durée** : 15-20 min.

### Étape 2A — Identifier les opportunités via GSC

```
Voici mon export GSC [période]. Identifie les quick wins :

Critères :
- Pages en position 3-12
- Impressions élevées (top 20% de mes pages)
- CTR sous-performant (écart > 1.5% vs CTR attendu pour la position)

Pour chaque quick win, calcule :
- Delta CTR = CTR attendu - CTR réel
- Impact estimé = Impressions × Delta CTR = clics potentiels gagnés

Priorise par impact estimé (du plus élevé au plus bas).
```

### Étape 2B — Scrapper le contenu de mes pages via Chrome

Connecte-toi à Chrome, navigue sur chaque page quick win, extrait : title + meta actuels, structure Hn (H1-H4), 300 premiers mots, présence FAQ / données structurées, liens internes entrants/sortants visibles, présence de preuves atomiques [Sujet + Relation + Donnée], nombre de mots.

Depuis la GSC, pour chaque page : toutes les requêtes en impression, et les requêtes à fort potentiel non exploitées (impressions élevées, position 10+). Comparer title/meta actuels vs requêtes GSC.

Générer pour chaque page : Title actuel → Title recommandé, Meta actuelle → Meta recommandée, actions classées par impact (immédiat / 1 semaine / 1 mois).

### Étape 2C — Vérifier la présence locale

Si MCP Local Falcon connecté : scan visibilité locale (fiche GBP, score Local Pack). Sinon : vérifier manuellement si une fiche Google Business Profile existe. Pas de fiche GBP → création prioritaire (souvent le quick win #1).

### Output attendu

- Top 5-10 quick wins avec impact estimé en clics
- Diagnostic page par page (GSC + contenu réel)
- Recommandations title/meta basées sur les requêtes GSC réelles
- Statut présence locale

### Ce que ça nourrit

→ Phase 3 : les pages quick win sont déjà scrappées (Hn extrait en 2B), la Phase 3 étend le scan Hn à tout le sitemap. Une page quick win dont le seul vrai problème est le Hn = quick win structurel.

---

## PHASE 3 — Audit structurel (architecture Hn)

**Skill** : aucun (prompt + scrap).
**Source** : **le sitemap.xml complet** (toutes les URLs, pas un échantillon de 50 — le périmètre suit le site) + Chrome (Cowork) ou `curl`/`grep` (terminal) + export GSC.
**Durée** : variable selon la taille du sitemap.

### Périmètre

- Récupérer la liste **complète** des URLs depuis le sitemap.xml (déjà chargé en Phase 1). Le nombre de pages auditées suit le site : 50, 200, 800 — pas de cap arbitraire.
- **Terminal** : volume quasi illimité, c'est gratuit (~1-2 min / 10 URLs).
- **Cowork (Chrome)** : si le sitemap est gros, **prioriser** — auditer d'abord les pages avec impressions GSC + les pages quick win (Phase 2) + les pages en position 4-20, puis le reste si le budget tokens le permet. On ne tape pas 800 URLs à l'aveugle dans Chrome.

### Étape 3A — Extraire l'arborescence Hn

Pour chaque URL, extraire H1 → H6 dans l'ordre du document.
- Terminal : `curl -sL -A "Mozilla/5.0" {URL} | grep -oE '<h[1-6][^>]*>'` (puis lire le texte des balises)
- Cowork : Chrome lit les headings du DOM de la page

### Étape 3B — Audit de chaque page (8 contrôles)

1. **H1 unique et présent** — 0 H1 = critique ; >1 H1 = à corriger
2. **Hiérarchie sans saut de niveau** — un H1 → H3 sans H2 = arborescence cassée
3. **H1 vs intention** — le H1 répond-il à la requête principale GSC de la page, ou est-ce un H1 générique / le nom du site / un slogan ?
4. **H2 vs micro-intentions** — les H2 couvrent-ils les requêtes GSC où la page est en position 4-20 (signal « Google la trouve pertinente mais incomplète ») ?
5. **Hn génériques bannis** — « Introduction », « Conclusion », « Pour aller plus loin », « En résumé » = signal de contenu faible / IA
6. **Hn sur-optimisés** — le mot-clé exact répété dans chaque Hn = sur-optimisation
7. **Passage Ranking** — chaque H2 doit pouvoir se lire comme une réponse autonome (extractible en featured snippet, citable par un LLM)
8. **Pages sans structure** — aucun Hn ou « div soup » = invisible au Passage Ranking

### Étape 3C — Croisement

- Pages business (requêtes Phase 0) avec un Hn cassé ou hors-sujet → priorité haute
- Recouper avec la Phase 2 : une page quick win dont le seul problème est le Hn = quick win structurel (effort faible, impact rapide)

### Output attendu

- Tableau par URL : `| URL | H1 ok | hiérarchie ok | H1↔intention | H2↔requêtes GSC | Hn génériques | verdict |`
- Anomalies critiques en tête : page business sans H1, H1 hors-sujet, structure absente
- Recommandations Hn par page prioritaire — le H1/H2 cible précis, pas « revoir la structure »

### Ce que ça nourrit

→ Phase 4 (un Hn qui se chevauche entre 2 pages = signal de cannibalisation de contenu) → Phase 6 (les réécritures Hn vont dans l'horizon Mois 1).

---

## PHASE 4 — Détection des cannibalisations

**Skill** : `seo-cannibalisation`.
**Source** : export GSC + Chrome (vérification contenu).
**Durée** : 15-20 min.

### Pré-condition

Combien d'URLs distinctes dans l'export GSC ?
- **< 10 URLs** → skip cette phase, documenter un diagnostic de « sous-granularité » (pas assez de pages pour cannibaliser, c'est un constat en soi) et passer directement à la **Phase 5**.
- **≥ 10 URLs** → continuer.

### Détection via GSC

Pour chaque requête, vérifier si plusieurs URLs reçoivent des impressions :
- Type A : même requête exacte → plusieurs URLs
- Type B : requêtes très proches (même intention) → URLs différentes

Pour chaque conflit : position / impressions / clics / CTR de chaque URL ; l'une vole-t-elle les impressions de l'autre ; les positions fluctuent-elles (Google hésite).

Classifier : Type A (mot-clé exact, risque élevé) / Type B (même intention, risque moyen) / Type C (proximité sémantique, à surveiller) / Triade SERP (2+ URLs top 10, opportunité positive). Recommander l'action : 301, merge, différenciation d'angle, renforcement maillage, ou aucune action.

### Vérification du contenu via Chrome

Ouvrir les 2 URLs en conflit, scraper : même intention réelle ? H1/H2 se chevauchent-ils (croiser avec la Phase 3) ? même page pilier ? liens internes croisés ? Diagnostic root cause : **problème de contenu** (pages trop similaires) ou **de maillage** (Google ne comprend pas la hiérarchie).

### Output attendu

- Cannibalisations détectées via GSC + confirmées par lecture du contenu
- Diagnostic root cause : contenu vs maillage
- Action recommandée par conflit

---

## PHASE 5 — Audit du maillage interne (2 passes)

**Skills** : `maillage-systeme` (passe structurelle) + `maillage-interne-gsc` (passe data).
**Source** : Chrome (crawl des liens internes) + export GSC.
**Durée** : 25-40 min.

> Deux passes complémentaires. **La structurelle d'abord** (raisonne sur l'éditorial, ne dépend pas de la GSC, tourne toujours), **la data ensuite** (la hiérarchie réelle vue par Google). Doctrine : architecture d'abord, donnée GSC quand elle est là.

### Étape 5A — Cartographier les liens existants via Chrome

Connecte-toi à Chrome. Navigue sur chaque page du site, extrait pour chacune : URL, tous les liens internes (ancre texte + URL cible), position du lien (nav / body / footer / sidebar).

Génère la matrice : `| Page source | Lien vers | Ancre utilisée | Position dans la page |`
Identifie : pages orphelines (aucun lien entrant), pages sur-linkées (>20 entrants), pages stratégiques sous-linkées (<3 entrants), ancres non-optimisées (« cliquez ici », « en savoir plus »).

### Étape 5B — Passe structurelle (`maillage-systeme`)

À partir de la matrice 5A : architecture en piliers (chaque pilier ≥10 liens entrants ?), classification hub/satellite, pages orphelines & dead-end, diversification des ancres entrantes, croisement avec les cannibalisations (Phase 4 : pages en conflit pointant vers le même pilier = aggravant). **Ne dépend pas de la GSC** — produit déjà un livrable seul.

### Étape 5C — Passe data GSC (`maillage-interne-gsc`)

Sur l'export GSC : hiérarchie page mère / fille / petite-fille (méthode Boussardon), pages mères potentielles sous-maillées, pages stratégiques GSC (grosses impressions) sous-linkées, application des règles Know → Do. Croiser avec 5B : **une page forte en impressions GSC mais orpheline structurellement = priorité absolue**.

⚠️ Pas de GSC propre → ne lancer que 5A + 5B et documenter que la passe data est sautée. La passe structurelle suffit à sortir un plan d'action.

### Output attendu

- Matrice de maillage actuel du site
- Diagnostic structurel : piliers sous-maillés, orphelines, dead-end, ancres (passe `maillage-systeme`)
- Diagnostic data : hiérarchie mère/fille, pages fortes GSC sous-linkées (passe `maillage-interne-gsc`)
- Plan d'action priorisé avec ancres exactes, trié par impact (impressions GSC × déficit de maillage)

---

## PHASE 6 — Synthèse & plan d'action priorisé

**Skill** : aucun, synthèse assistée par Claude.
**Durée** : 20-30 min.

### Prompt exact

```
Voici les résultats de mon audit SEO :

PHASE 0 - Positionnement : [coller synthèse]
PHASE 1 - Indexation : [coller synthèse]
PHASE 2 - Quick Wins : [coller synthèse]
PHASE 3 - Structure Hn : [coller synthèse]
PHASE 4 - Cannibalisations : [coller synthèse]
PHASE 5 - Maillage interne : [coller synthèse]

Génère le plan d'action final en 3 horizons :

SEMAINE 1-2 (Quick Wins) :
Actions à impact immédiat, zéro création de contenu.
Déblocage des pages non indexées, réécritures title/meta,
corrections Hn rapides, liens internes à ajouter,
résolution cannibalisation, fiche GBP.

MOIS 1 (Fondations) :
Optimisation des pages existantes, réécriture des Hn hors-sujet,
restructuration du maillage en piliers,
résolution structurelle des cannibalisations.

MOIS 2-3 (Croissance) :
Création de nouvelles pages sur les gaps identifiés en Phase 0,
outils interactifs.

Pour chaque action :
| Action | Page | Type | Impact estimé | Effort | Dépendances bloquantes |

Génère aussi : la matrice de dépendances, les actions parallélisables,
un Gantt simplifié, les KPIs de suivi par horizon.
```

### Output attendu

Le rapport d'audit final, format client : synthèse exécutive en tête, anomalies critiques d'abord, plan d'action priorisé en 3 horizons. C'est CE livrable qui fait signer.

---

## Configuration minimale & checklist pré-audit

**Audit complet** : export GSC + Chrome + sitemap.
- GSC sert les Phases 0, 2, 3, 4, 5 (passe data)
- Chrome (extension Claude in Chrome) sert les Phases 2, 3, 5
- Le sitemap sert les Phases 1 et 3 (Phase 3 = sitemap **complet**, pas un échantillon)
- Phase 5 : la passe structurelle (`maillage-systeme`) ne dépend PAS de la GSC ; la passe data (`maillage-interne-gsc`) la requiert

**Checklist pré-audit :**
- [ ] Export GSC en CSV, 3-6 derniers mois, toutes requêtes + toutes pages
- [ ] Chrome ouvert avec l'extension Claude in Chrome connectée et testée
- [ ] URL du site + sitemap.xml accessible (liste complète des URLs)
- [ ] Liste de 5-10 requêtes business principales
- [ ] Connaissance du business model et des pages stratégiques
- [ ] Budget temps : 3-4,5h pour l'audit complet, étalable (la Phase 3 dépend du nombre d'URLs)

---

*Workflow audit — version bootcamp 4 (resserrée), dérivée du V3. Méthodologie Timothée Boussardon, mai 2026. Phases retirées vs V3 : clusters AEO, analyse vectorielle, briefs de contenu. Phases ajoutées : audit d'indexation (P1), audit structurel Hn (P3). Maillage : `maillage-systeme` (passe structurelle) + `maillage-interne-gsc` (passe data).*
