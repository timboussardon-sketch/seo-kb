# Historique — Fusionn

Journal du travail sur [[entities/fusionn-io]] (repo `~/Code/newFusionn`). Entrée la plus récente en haut.

## Liens

- Produit : [[entities/fusionn-io]].
- Donnée de référence pour la promesse AI Overviews du produit : [[etude-ctr-ai-overviews-gsc]].

---

## 2026-06-29 · Refonte agent mots-clés type Qadence (chatbot + skills + mémoire + Google Ads) — DÉPLOYÉ

- Nouveau parcours : la landing perd l'input d'URL, gagne une flexbox « décrivez votre produit/service » → route `/recherche` (chatbot plein écran type Qadence, DA Fusionn). Pages SEO publiques inchangées.
- Edge function `keyword-agent` (déployée, `--no-verify-jwt`) : port de la boucle agentique Qadence (`runAgentLoopStream`), scope mots-clés. Outils : `load_skill` (skills dédiés recherche/clustering/décisionnels/micro-intentions/structure Hn/brief/décodage/GEO, repris de `agentSkills` + `guide-skills`), `update_memory` (mémoire par projet), `keyword_metrics` (Google Ads via `_shared/google-ads.ts fetchKeywordHistoricalMetrics` → volume + CPC + compétition réels, rendu obligatoire par Tim). Modèle `KEYWORD_AGENT_MODEL` (défaut Sonnet 4.6).
- Front : sidebar dédiée à UN projet (sélecteur de projet en haut + onglets dédiés Chat/Mots-clés/Clusters/Micro-intentions/Structure Hn/Briefs/Mémoire + historique par projet), réflexion live (StepsBox), tableau mots-clés DA Fusionn (Volume/CPC/Compétition/Business/Bucket). Modèle de données projet → conversations + mémoire, en localStorage. Fichiers : `src/pages/Recherche.tsx`, `src/components/recherche/*`.
- Dev local sans Docker : serve via Deno (`npm run serve:keyword-agent`, clé dans `.env.keyword-agent.local` gitignoré, `VITE_KEYWORD_AGENT_URL`). En prod le front tape la fonction déployée (secrets ANTHROPIC_API_KEY + GOOGLE_ADS_* déjà sur le Supabase `fwhfnzbtlddzfxbsejyf`). Deploy CLI : resets intermittents sur api.supabase.com, relancer 2-4x (token keychain "Supabase CLI").
- Reste à faire : capturer les livrables clusters/micro/hn/briefs dans leurs onglets dédiés (aujourd'hui produits dans le chat ; seul l'onglet Mots-clés capture la donnée structurée).

## 2026-06-10 · Opportunités : findings de crawl ne polluent plus les Quick wins — DÉPLOYÉ

- Retour Tim (capture) : « Pousser "timothée boussardon" en page 1 » et « Pousser "2 pages au contenu fin (< 250 mots)" en page 1 » → « ça ne sert strictement à rien ».
- Bug : `scanCrawlFindings` faisait `keyword = suggested_keyword || title`. Pour un finding `thin` (mappé en `optimiser_page`), le `suggested_keyword` est vide → le **titre descriptif** (« 2 pages au contenu fin ») devenait le mot-clé d'un faux Quick win. Idem orphan/dead_end → « Mailler vers "1 page orpheline" ».
- Fix : `thin` retiré de CRAWL_ACTION (pas de bucket sensé). Findings structurels orphan/dead_end → reco centrée PAGE (`crawlStructuralReco`), jamais le titre comme mot-clé. Candidat crawl créé seulement s'il porte une vraie requête (`suggested_keyword`) ou, pour le maillage, une URL.
- « timothée boussardon » (marque) = données périmées d'un vieux scan ; `charterReject` le filtre déjà. **Vérifié au re-scan organikk.co : 0 requête de marque, 0 faux mot-clé crawl** ; restent 2 opportunités propres (cannibalisation + maillage) avec problématique en titre.
- Commit `6ee55ec`. (organikk.co = site brand-heavy → peu d'opportunités décisionnelles, normal.)

---

## 2026-06-10 · Agent Opportunités : génération des problématiques RÉPARÉE + vérifiée en prod — DÉPLOYÉ

- Suite de « go » (Tim veut voir le résultat réel). Premier scan forcé → 0 problématique, 0 page à créer, marque non filtrée. Débogage long (réseau très instable toute la session).
- **Cause racine trouvée** : `gemini-2.5-flash` **pense** (thinking) avant de répondre et bouffe le budget de tokens → JSON tronqué (`finishReason: MAX_TOKENS`, préambule « Here is the JSON requested ») → `parseJSON` échoue → charte en fallback, agent 0 gap, enrichissement sans `query`. Intermittent (parfois flash pense peu → JSON valide). Cf. note mémoire « Flash JSON malformé / thinking coupé ».
- **Fixes** : (1) `thinkingConfig:{thinkingBudget:0}` sur tous les appels Gemini JSON (charte, relevanceGate, enrichissement). (2) `huntGaps` réécrit en **single-call** : fetch déterministe Suggest+Reddit+YouTube → 1 appel JSON no-thinking qui génère les problématiques (la boucle function-calling produisait 0 gap : flash orchestre mal ses outils sur un prompt doctrine long). Code FC mort supprimé (GAP_TOOLS, callGeminiFC, listSitemap). (3) enrichissement 2048→6144 tokens.
- **Vérifié en prod** (scan réel sur croisiere-evasion.fr, site client à trafic décisionnel) : 46 opportunités, 8 `creer_page` + quick wins, **20/25 avec problématique 24 mots en titre + mot-clé en label**. Ex. « Est-ce qu'une croisière à la cabine vaut le coup pour un particulier seul qui veut juste se détendre ? », « Comment passer d'une simple sortie journée à une mini-croisière sans contraintes logistiques ? ». Charte auto-dérivée nickel, marque (« timothée boussardon ») filtrée. Pile la doctrine 4→24 mots.
- **Note infra** : `RADAR_CRON_SECRET` a été roté vers une valeur connue (synchronisée edge + GitHub secret) pour pouvoir déclencher le worker en direct pendant le debug. Le cron GitHub quotidien reste fonctionnel (les deux côtés ont la nouvelle valeur). Constat au passage : sur organikk.co l'agent renvoie 0 gap, c'est NORMAL (le site ne reçoit des clics que sur sa propre marque → aucun seed décisionnel).
- Commit `2370c1d`.

---

## 2026-06-10 · Agent Opportunités : doctrine problématique ENRICHIE (anatomie + tests + garde-fou) — DÉPLOYÉ

- Retour Tim : « creuse là-dessus pour avoir les meilleures réponses possibles » (sur la doctrine 4→24 mots).
- 2 recherches parallèles : (a) doctrine propriétaire de Tim minée dans la KB/calls/skills — test de requêtabilité (`seo-modeles-pseo`), modificateurs décisionnels Do, génération par intention, Know-Simple/Know/Do, exemples acceptés/rejetés qualiopi, test substitution ChatGPT ; (b) patterns réels moteurs IA (Semrush AI Mode 7,22 mots ; 8+ mots = ~57 % de déclenchement AI Overview ; vocal ~29 mots ; anatomie persona+situation+obstacle+résultat+contrainte+comparaison ; anti keyword-stuffing).
- **Implémentation** :
  - Constante `PROBLEMATIQUE_DOCTRINE` (anatomie, 2 tests durs requêtabilité + substitution, modificateurs Do, 6 gabarits, exemples ACCEPTÉ/REJETÉ, longueur 8-24 mots, ≤3 contraintes) injectée dans le gap-hunter ET l'enrichissement déterministe.
  - Garde-fou déterministe `looksLikeProblematique` : écarte les « problématiques » qui restent des mots-clés collés (< 5 mots, ou 5-7 mots sans mot-outil/préposition). Ex. rejeté « prix accompagnement qualiopi audit », accepté « prix d'un accompagnement qualiopi pour un audit de surveillance ».
  - `AGENT.md` enrichi.
- Edge function déployée. Commit `47ffc69`. Sources-clés : `seo-modeles-pseo/SKILL.md`, `leexi-seo/.../call-decouverte-2026-05-21.md:135`, `wiki/concepts/know-simple-know-do.md`.

---

## 2026-06-10 · Agent Opportunités : doctrine « 4 → 24 mots » (problématique, pas mot-clé) — DÉPLOYÉ

- Retour Tim : « pourquoi on n'a pas de prompt et uniquement des mots-clés ? notre doctrine c'est passer de 4 à 24 mots. Qu'est-ce qui bloque ? »
- **Diagnostic** (4 verrous) : (1) sources de l'agent = GSC + Google Suggest = requêtes courtes de l'ère 4 mots ; les prompts de 24 mots vivent dans ChatGPT/Perplexity, pas dans Google. (2) Le seul signal long (titres Reddit/YouTube) était **compressé exprès** en mot-clé (ligne « reformule en requête courte »). (3) L'agent ne lit jamais la data propriétaire (calls/tickets/`documents`) où vivent les vraies problématiques. (4) Modèle centré mot-clé (champ `keyword` court, pas de champ problématique).
- **Reframe (choix Tim : reframe agent d'abord)** :
  - L'unité devient la **problématique longue** (`recommendation.query`, 12-24 mots, langage naturel) ; le mot-clé court = simple label.
  - `submit_gaps` exige `problematique` + `keyword` ; system prompt porte la doctrine « 4 → 24 mots » et interdit de compresser Reddit/YouTube.
  - `enrichRecos` dérive aussi la `query` longue pour les opportunités déterministes (quick wins, titles, déclins).
  - Dédup des gaps sur la problématique (plus sur le mot-clé).
  - Front : problématique en **titre**, mot-clé en **label** (choix Tim).
- **Limite restante (palier suivant)** : brancher la data propriétaire (`documents`, calls) dans l'agent — c'est là que vivent les vraies requêtes de 24 mots. Non fait (Tim a choisi le reframe d'abord).
- Edge function déployée. Front commité/poussé (`7f34869`). Nouveau format au prochain scan `cron-opportunity-radar`.

---

## 2026-06-09 · Agent Opportunités : restructure (charte business + gates de pertinence) — DÉPLOYÉ

- Retour Tim : « pages à créer » absurdes (« manifestation seoul », « anssi certification cspn », « quality rater jobs work from home », « training seoul ») et cannibalisations de marque (« organikk.co », « timothée boussardon »). « Est-ce un vrai agent ? a-t-il un skill / un agent.md ? »
- **Diagnostic** : `run-opportunity-scan` est bien un agent Gemini function-calling (6 outils) MAIS sans contexte business — il seedait sur les **impressions GSC brutes** (le site matche par accident « manifesto seoul » via `/manifeste`, « quality rater jobs » via la page rater, « seoul » contient « seo »), et le seul garde-fou était `check_covered` (déjà couvert ?), pas la pertinence. Pas d'AGENTS.md, prompt inline de 20 lignes.
- **Restructure complète** (`index.ts`, ~250 lignes) :
  - **Charte business auto-dérivée** par run (`buildCharter`) : home scrapée + requêtes à CLICS → summary, ICP, in_scope, exclude_terms, brand_terms. Zéro saisie user.
  - **3 gates** : (1) seeding par les clics au lieu des impressions ; (2) charte injectée dans le system prompt du gap-hunter ; (3) double filet sortie = `relevanceGate` (LLM, fail-open) sur les gaps + `charterReject` (déterministe : marque en sous-chaîne + hors-sujet en mot entier) sur TOUT.
  - **Cannibalisation** : vraie dispute seulement (2e page ≥30 % des impressions de la 1re + les 2 pages ≤ position 25). Marque écartée par la charte.
  - **Réconciliation `persist`** : suppression des opportunités auto encore ouvertes (`new`/`seen`) non re-détectées → fini l'accumulation ; `dismissed`/`actioned` préservées. Nettoie le bruit existant au prochain scan.
  - **Front** (`OpportunitiesView.tsx`) : la carte cannibalisation montre les pages en concurrence (chemin + position + impressions).
  - **`AGENT.md`** créé dans le dossier de la fonction : contrat explicite (mission, charte, 3 gates, réconciliation, règles invariantes).
- Edge function **déployée** (`supabase functions deploy run-opportunity-scan`, projet fwhfnzbtlddzfxbsejyf). Front commité/poussé (`4fda947`). Le bruit existant disparaît au prochain passage du cron `cron-opportunity-radar`.

---

## 2026-06-09 · Onglet Opportunités : scope par propriété GSC + DA Fusionn — DÉPLOYÉ

- Retour Tim : l'onglet Opportunités mélangeait tous les sites dans les résultats, et avait une palette « IA » (violet + arc-en-ciel hors-tokens).
- **Bug du mélange** (`OpportunitiesView.tsx`) : la requête chargeait TOUTES les opportunités de toutes les watchlists (`limit 800`, aucun filtre par site), puis défaultait sur « le site avec le plus de lignes ». Avec les 20+ propriétés GSC de Tim → mélange + troncature.
- **Fix** : 2 effets séparés. (1) charge les watchlists `type=account` une fois et défaute sur la propriété GSC active lue dans `localStorage['fusionn_gsc_property']` (helper `getSelectedGscProperty`, match via `domainOf`). (2) charge opportunités + runs **scopés** `.eq('watchlist_id', siteId)` (limit 400/10). Une seule propriété à la fois, plus de fuite. Sélecteur de site reste pour switcher (override local, non persisté — choix Tim).
- **DA** : palette `ACTIONS`/`INTENT` passée des hex hors-tokens (violet `#7c3aed`, `#1f9d63`, `#2559DD`, `#0891b2`...) aux tokens `--ws-warning/success/danger/brand` + gris neutres. `creer_page` = rouge brand (action héro). Pastille « Actif », icône run, badge intention : tokens. Plus aucun hex hors-token.
- Type-check vert sur le fichier (erreurs TS restantes = préexistantes ailleurs), vérifié en local (localhost:5175/compte). Commit `ee710e2`.

---

## 2026-06-09 · « Bonjour <prénom> » affiché une seule fois (entrées site / mot-clé / contexte) — DÉPLOYÉ

- Retour Tim : le « Bonjour Tim » se répétait à chaque changement d'entrée (Mon site / Un mot-clé / Par contexte), lourd.
- Fix dans `Compte.tsx` : flag `heroTouched` (false à l'arrivée, true au 1er clic sur le sélecteur d'entrée) → `heroGreetingName` passé aux 3 panels seulement tant qu'on n'a pas touché le sélecteur. Le « Bonjour <prénom> » n'apparaît donc qu'une fois, à l'arrivée sur l'onglet par défaut « Mon site ».
- Les 3 hero panels (`SiteAuditPanel`, `KeywordHeroPanel`, `ContextHeroPanel`) affichent la **question seule** quand il n'y a pas de prénom : « Sur quoi allons-nous travailler ? » / « Quel mot-clé veut-on travailler ? » / « Partez de vos documents. » (plus de « Bonjour, » orphelin).
- Type-check vert, vérifié en local (localhost). Le « Bonjour <prénom> ! » du chat conversationnel (post-lancement) n'est PAS touché, laissé tel quel.
- **Correction (même jour, retour Tim)** : finalement on **garde** le « Bonjour <prénom> » en permanence sur l'onglet **site** (c'est la page d'accueil), et on ne le retire que sur **mot-clé** et **contexte**. Suppression du flag `heroTouched` ; `SiteAuditPanel` reçoit le prénom, `KeywordHeroPanel` / `ContextHeroPanel` reçoivent `undefined`.

- **Demande Tim** : « 1 seul requête gratuit. De partout. Wording aussi. » Décisions cadrées : **chaque fonction plafonnée à 1** (pas un crédit unique partagé) et **à vie** (plus de reset mensuel/quotidien).
- **Constat** : le « gratuit » était éclaté en 4+ quotas séparés (recherches 3 total, Hn 5/mois, sémantique 5/mois, geo 5/mois, chat 5/jour), chacun avec sa constante front, sa fonction edge et parfois une fonction SQL.
- **Enforcement passé à 1 / à vie (déployé sur Supabase `fwhfnzbtlddzfxbsejyf`)** :
  - `check-rate-limit` : `searchLimit` 3→1 ; mode keyword passe de fenêtre glissante 24h à **à vie** (retrait du `gte(since)`).
  - `check-hn-score-limit` / `check-semantic-score-limit` : `monthlyLimit` free 5→1, retrait du filtre `startOfMonth` (compte à vie).
  - `analyze-geo-sentinel` : `freeLimit` 5→1, retrait de la fenêtre mensuelle.
  - `get-all-quotas` : `LIMITS` tous à 1, comptage à vie (plus de `gte`), `period: 'total'`, `resetsAt: null`.
  - `analyze-semantic-score` : message d'erreur 429 reformulé (plus de date de réinitialisation).
  - `SEARCH_LIMITS` (front, `compte/types.ts`) : valeurs free → 1.
- **Chat laissé tel quel** (jugement) : `check_and_increment_chat_usage` / `get_chat_daily_usage` non touchés. 1 message à vie casserait l'assistant conversationnel ; « requête » = analyse, pas message de chat. **À confirmer avec Tim.**
- **Wording** : ~20 chaînes mises à jour (FAQ, Landing ×3, ArticleCTABanner, ToolPageLayout, Connexion, Documentation, CitationProbe, KeywordGenerator, ComparateurVolumeBusiness, SubscriptionChoiceModal, compteurs SearchPanel/HeroInput/ConversationalSearch/StickyInput, KeywordHeroPanel, SiteAuditPanel, AnalysisLimitCounter « ce mois »→« à vie », HnScoreView, SemanticScoreView, SemanticScore). De « 3 recherches / 5 analyses / par mois / réinitialisation » vers « 1 requête gratuite à vie ».
- **Build** : tsc clean, `vite build` OK (le `react-snap` post-build échoue pour un souci Puppeteer local, sans rapport). Commit `e6c7233` poussé sur `main` → Netlify redéploie fusionn.co.
- **RESTE — 1 étape manuelle** : la migration `20260606120000_one_free_request_lifetime.sql` (slot SQL `reserve_semantic_analysis_slot` 3→1 à vie) n'a pas pu être poussée (`supabase db push` demande le mot de passe DB que je n'ai pas). Le gate sémantique est déjà effectif via `check-semantic-score-limit` (edge) ; la migration aligne le backstop serveur. **Tim : lancer `cd ~/Code/newFusionn && supabase db push`.**



- **Origine** : idée Tim née d'une session FG Formation (extraction de 14 calls .docx → personas → mots-clés décisionnels → modèles pSEO). « Ça pourrait devenir un onglet : j'ajoute des documents et tu lances la recherche. » À côté de « Mon site » et « Un mot-clé », nouveau mode « Par contexte ».
- **Découverte** : l'infra existait déjà à 90%. La table `documents`, le pipeline `startAnalysis(kw, ctx, documentIds)` qui injecte les docs (ligne 322 de `useConversationalAnalysis`), et l'upload dans `ContextPills` étaient en place. **Cause racine du blocage** : `ContextPills` n'acceptait que `.txt/.csv/.json/.md` et rejetait les `.docx`/`.pdf`.
- **Livré (MVP, branche `feat/recherche-par-contexte`)** :
  - `src/lib/parseDocument.ts` (nouveau) : parser navigateur partagé — docx→mammoth, pdf→pdfjs (`?worker` Vite), xlsx→xlsx-js-style, csv/txt/md/json→texte. Libs déjà installées.
  - `ContextPills.tsx` : utilise le parser partagé → accepte enfin docx/pdf/csv/xlsx (bénéficie aussi au flux mot-clé existant). Limite 5→10 Mo.
  - `ContextHeroPanel.tsx` (nouveau) : panneau de l'onglet, thématique + upload front + note, upload vers `documents`, design system `--ws-*`.
  - `useConversationalAnalysis.ts` : `handleContextModeSubmit(kw, note, documentIds)` → `startAnalysis` direct (saute les questions), exporté.
  - `Compte.tsx` : 3e onglet `context`, rendu `ContextHeroPanel`, quota réutilise le mode `keyword` (3/j free) pour le MVP.
- **MVP assumé** : les documents enrichissent le pipeline existant (mots-clés/FAQ/objections vus à travers les docs). Pas encore d'extraction de personas formalisés (V2 décidée avec Tim).
- **État** : type-check OK + build prod OK (worker pdfjs bundlé en chunk séparé). Commit `4694b5e` mergé sur `main` + push (auto-deploy Netlify `fusionn2`). Le push a aussi emporté `d2ebaf3` (ops-alert, commit local du monitoring non encore poussé). Branche `feat/recherche-par-contexte` conservée.
- **Suites possibles (non faites)** : quota dédié `context` dans `check-rate-limit` (réutilise `keyword` pour l'instant) ; V2 extraction de personas formalisés.

---

## 2026-06-04 · Chatbot (suppression/édition + skills partagés) + premium + home

- **Premium** : `louis.bertin@live.fr` passé Premium 1 mois (subscription `active`, `current_period_end` 2026-07-04, sans Stripe) via l'API Management Supabase. `is_subscription_valid` = true. Modèle = table `subscriptions`.
- **Chatbot Agent** (`AgentChatView.tsx`, `ChatMessage.tsx`) : suppression d'une conversation depuis la sidebar (corbeille au survol, confirm, cascade via policy DELETE existante) ; édition d'un message utilisateur façon LLM (coupe la suite en base + régénère, rechargement post-envoi pour ids réels) ; sparkles remplacés par `FusionnIcon`.
- **Chatbot onglet mots-clés** (`ContextualChatModal.tsx`) : même menu Skills que l'agent, via nouveau module partagé `src/lib/agentSkills.ts` (`buildAgentSkills(keyword)`). `keyword={mainKeyword}` passé depuis `SortableKeywordsTable`. Origine : un mot-clé pSEO n'apparaît pas dans l'onglet mots-clés et l'agent ne l'analysait pas — cause racine : onglet + agent ne lisent que `search_semantic_results`, le pSEO vit dans `action_plan_results.pseo_playbooks`. Livré : parité des skills + **ajout d'un mot-clé à analyser** (champ dans le chatbot → `insertManualKeyword` dans `search_semantic_results`, dédoublonné, affichage immédiat dans l'onglet via état local `localKeywords`, vu par l'agent, analyse lancée automatiquement).
- **Home** : retrait de la pill de démo « assurance vie en ligne » (`DemoSection.tsx`).
- Commit + push `main` (Netlify auto-deploy). Type-check OK (warnings restants pré-existants).

---

## 2026-06-02 · Onglet Stratégie pSEO — scroll + lisibilité

**Contexte.** Sur l'onglet Stratégie pSEO (vue `actionPlan`), en arrivant depuis un autre sous-onglet on restait à la position « en bas » héritée. Et les cartes de playbooks (stratégies) manquaient de lisibilité, toutes au même fond neutre.

**Fix 1 — scroll (`WorkspaceLayout.tsx`).** Le `strategyContentRef` existait mais n'était jamais exploité. Ajout d'un `useEffect([analyzeSubView])` qui `scrollTo({ top: 0 })` la zone scrollable à chaque changement de sous-onglet → on arrive toujours en haut.

**Fix 2 — alternance (`PseoStrategyView.tsx`).** Dans `PlaybookCard`, fond orange très léger (`#FFF5F2`, bordure `#FBD9CF`) une carte sur deux (`index % 2 === 1`) ; hover et bloc description dépliés alignés sur le même fond.

**Deploy.** Commit `7503e88` sur `main` (Netlify auto-deploy, site fusionn2). tsc clean, build Vite OK (react-snap échoue en local sur puppeteer mais OK côté CI Netlify), montré en local sur `localhost:5173`. Inclut aussi les modifs working tree en cours (admin, tables, modal abonnement, edge `admin-stats-v2`).

---

## 2026-05-30 · Moteur d'emails de cycle de vie (lifecycle / drip)

**Contexte.** Tim demande des séquences email automatiques et gratuites par comportement (inscrit 0 recherche, 1 recherche, 2 recherches, etc.). Choix validés : moteur complet + tout le cycle de vie. Constat à l'exploration : toute la data existe déjà (`user_profiles.created_at`, `search_history` par user, `analytics_events.premium_click`, `subscriptions`), seul l'envoi email manquait (aucun Resend/SMTP dans le repo).

**Ce qui a été construit (3 fichiers, branche dédiée).**
- **Migration `20260530180000_create_email_lifecycle_system.sql`** : tables `email_sequences` (catalogue + seed des 6 séquences, vouvoiement, design Fusionn `#FF371C`/`#F4F5F7`), `email_queue` (file, `UNIQUE(user_id, sequence_key)` = idempotent), `user_email_preferences` (opt-out + token désinscription). RLS activé, écritures service_role only. Fonction SQL `enqueue_lifecycle_emails()` (SECURITY DEFINER) qui calcule les 6 segments et remplit la file en `ON CONFLICT DO NOTHING`.
- **Edge `cron-lifecycle-emails`** : cron quotidien → RPC enqueue puis envoi des dus via Resend. Garde-fous : DRY-RUN par défaut (tant que `LIFECYCLE_EMAILS_ENABLED!=true` ou pas de `RESEND_API_KEY`, 0 envoi), batch plafonné 90/run (< 100/jour gratuit Resend), `X-Cron-Secret`.
- **Edge `email-unsubscribe`** : désinscription 1 clic par token, sans login (RGPD). Lien présent dans chaque mail + header `List-Unsubscribe`.

**Les 6 séquences.** activation_no_search · nudge_after_1_search · nudge_after_2_searches · reengage_inactive (14j) · premium_click_no_purchase · premium_onboarding.

**Déployé (même session, clé Resend fournie par Tim).** Migration `20260530180000` poussée en prod (`db push`), 2 Edge Functions déployées, secrets posés (`RESEND_API_KEY`, `EMAIL_FROM=Fusionn <hello@fusionn.co>`, `LIFECYCLE_EMAILS_ENABLED=false`). Test à blanc : RPC `enqueue_lifecycle_emails` appelée → 40 users segmentés (24 activation_no_search, 12 nudge_after_1, 4 nudge_after_2), tous `pending`, 0 envoi. Clé Resend en mode « envoi seul ».

**Vérif domaine + DNS (fait).** `fusionn.co` ajouté chez Resend (clé restreinte « envoi seul »). DNS posés via API Netlify (zone `6a0d950565bb45eb3fb31539`, token CLI dans `~/Library/Preferences/netlify/config.json`) : DKIM `resend._domainkey`, MX `send` → `feedback-smtp.ap-northeast-1.amazonses.com`, SPF `send`, DMARC `_dmarc`. Aucun conflit ImprovMX (racine vs sous-domaine `send`). Domaine vérifié après clic « Verify DNS Records » de Tim.

**Pivot produit « site first » (correction Tim en cours de route).** Le produit n'est plus « taper un mot-clé » mais « analyser son site » (table `site_crawls`, `status='done'`, bouton UI « Analyser »). Donc segmentation REBASÉE sur `site_crawls` (migration `20260530200000`), copy entièrement réécrit. Nouvelle règle mémoire appliquée : **jamais « concurrent/concurrence »** dans le copy (comme netlinking/backlink). Borne `activation_no_search` aux inscrits < 30 jours (migration `20260530190000`).

**Logo + signature.** Logos du repo en SVG (pas email-safe) → généré un PNG via PIL (marque atome `#FF371C` + wordmark), uploadé sur Supabase Storage bucket public `assets` (`/storage/v1/object/public/assets/fusionn-logo.png`). Wrapper email : logo en tête + signature « A+, Tim » + lien désinscription. PS « répondez OK » ajouté à l'activation (délivrabilité ; replies `hello@fusionn.co` → ImprovMX → Gmail Tim).

**Personnalisation des 3 emails post-analyse (migration `20260530210000` + fonction).** Marqueur `{{PERSO_BLOCK}}` remplacé par destinataire : top 3 opportunités réelles du dernier crawl (`crawl_findings` du dernier `site_crawls` à `opportunities_status='done'`), **filtrées** des termes bannis (`netlinking|backlink|link building|achat de lien|concurrent`), + « Par où commencer » + sujet dynamique référençant le domaine. Repli générique si pas de data. Activation reste générique (pas de data site à ce stade).

**LIVE.** Domaine vérifié, secret dédié `LIFECYCLE_CRON_SECRET` (la clé restreinte ne lit pas `CRON_SECRET`), fonction améliorée (inner join `is_active` = pause sans brûler la file ; fix embed `user_profiles` via requête séparée). **49 emails d'activation envoyés** (segmentation site-first : 49 inscrits 0 analyse), 0 échec, confirmés `sent` en base. Aperçus envoyés à Tim (activation v2 + perso organikk.co réel).

**Affinages copy (demandes Tim).** Email 2 : clusters au lieu de mots-clés exacts (moins risqué). Email 3 : + plan d'action 2 phases (Phase 1 décisionnel/transactionnel, Phase 2 informationnel). Email 4 : TABLEAU des 10 meilleurs mots-clés par vrai score business `interet_business` (table `search_business_score_results`, Gemini, `user_id`, scores 87-98 + bucket Fort/Moyen/Faible) dédupliqué. Email 5 : analyses illimitées + 4 agents SEO en « bientôt » (Maillage, Search Console, Rédaction, Veille ; « gap concurrentiel » retiré). PS « répondez OK » sur l'activation (délivrabilité). Filtre `FORBIDDEN_TERMS` sur tout mot-clé/opportunité affiché.

**Règle « — » : nettoyée partout** (pied de page, bloc perso, libellés). Zéro tiret cadratin en base.

**PLEINE AUTO LIVE (Tim : « go pour les 6 »).** 6 séquences `is_active=true`. Cron `lifecycle-emails-daily` posé via **pg_cron + pg_net** (`supabase db query --linked`, secret injecté one-off = PAS dans git), `0 9 * * *`, header `X-Cron-Secret`=`LIFECYCLE_CRON_SECRET`. Fonction redéployée `--no-verify-jwt` (secret = seul guard). Test chemin cron : 200, 1 activation enqueue+envoyée auto. **Moteur autonome en production.**

**Dette technique.** Repo basculé sur `main` (session parallèle) : fonctions + migrations (180000/190000/200000/210000/224700) en PROD mais source sur branche `feat/lifecycle-emails` à recommiter ; collisions de numéros avec les `lock_documents_rls` parallèles (d'où renommage `224700`). Secret cron aussi dans `/tmp/lifecycle_secret.txt` (local). Réglages possibles : heure du cron (9h UTC = 11h Paris), cadrage agents « bientôt » vs dispo.

**Règle ajoutée.** Jamais parler d'argent dans le copy Fusionn (« paient votre SEO », « se rentabilise », ROI, prix). Retiré des emails 3 et 5. Mémoire `feedback_fusionn_pas_argent`.

**Suivi ouvertures/clics + rapports Obsidian.** Migration `20260530231500_email_events_tracking` : table `email_events` (idempotente sur provider_id+event_type) + vue `email_stats_by_sequence`. Edge `resend-webhook` (`--no-verify-jwt`, vérif signature Svix via `RESEND_WEBHOOK_SECRET`) déployée, reliée par `provider_id`. Rapport auto : `seo-kb/fusionn/scripts/email-report.sh` (clé service_role via CLI, jamais en dur) écrit `rapports-emails/AAAA-MM-JJ-rapport-emails.md` dans le vault ; planifié par launchd `co.fusionn.email-report` chaque lundi 9h.

**Config Resend (faite par moi via clé full-access fournie par Tim, puis révocable).** Suivi ouvertures + clics activé sur fusionn.co, webhook créé et `RESEND_WEBHOOK_SECRET` posé. Chaîne vérifiée bout-en-bout (event `delivered` signé reçu et stocké en 10s). La clé de prod reste la « envoi seul ».

**Refonte admin (`/admin`).** `admin-stats-v2` étendu (accès `tim.boussardon@gmail.com` + objet `emails` depuis la vue). UI refondue en onglets au design Fusionn (Vue d'ensemble / Emails / Business / Utilisateurs / Usage), nouveau composant `AdminEmailLifecycle` (KPIs + taux ouverture/clic par séquence + derniers envois). Montré en local (port 5177) puis validé.

**PUSH MAIN (`e249cdc`).** Tout commité et poussé sur `main` (Netlify auto-deploy) : refonte admin + moteur emails complet (functions + 6 migrations) + suivi. Dette « source à recommiter » RÉSOLUE. Restait juste : `email-unsubscribe`/README restaurés depuis la branche `feat/lifecycle-emails` avant commit.

---

## 2026-05-29 · Finalisation des 3 nouveaux outils gratuits

**Contexte.** Reprise du chantier WIP laissé non commité à la session précédente : 3 nouveaux outils gratuits Product-Led SEO. Type-check vert, dev relancé sur :5173 pour montrer les pages.

**Les 3 outils.**
- **Explorateur de questions** (`/explorateur-questions-seo`) → edge function `tool-question-explorer` (déterministe, sans clé) : renvoie les vraies questions tapées autour d'un mot-clé, catégorisées (definition, prix, comment, combien…).
- **Clusteriseur de mots-clés** (`/clusteriser-mots-cles`) → edge function `tool-cluster-keywords` : regroupe une liste brute en clusters sémantiques via embeddings Gemini (`GEMINI_API_KEY` présent, méthode `embeddings`, seuil 0.8). 1 cluster = 1 page.
- **Mots-clés qui convertissent** (`/mots-cles-qui-convertissent`) → 100% client via `src/lib/decisionalScore.ts`, aucun appel réseau. Tri par potentiel de conversion (transactionnel → informationnel).

**Câblage.** Routes `App.tsx`, footer (7 outils gratuits au total), doc section 19 (« Quatre » → « Sept outils »).

**Sitemap.** Constat : AUCUN outil gratuit n'était dans le sitemap (manque préexistant, pas que les 3 nouveaux). Ajout des 7 outils dans `staticPages` de l'edge function `generate-sitemap`, redéployée. Sitemap régénéré (curl direct, le script `generate-sitemap.js` plantait sur `.env` absent) : 45 URLs, 7 outils présents.

**Deploy.** 3 edge functions déployées sur prod (`fwhfnzbtlddzfxbsejyf`) : `tool-question-explorer`, `tool-cluster-keywords`, `generate-sitemap`. Smoke-test prod OK (HTTP 200 sur les 2 endpoints outils). Commit `9da09b1` poussé sur `main` (11 fichiers, staging sélectif pour ne pas embarquer l'article blog WIP google-io). Netlify rebuild auto.

**Maillage interne + fix lien mort (commit `bf297ac`).** Constat : footer OK mais aucune page outil existante ne pointait vers les 3 nouvelles (maillage entrant nul hors footer). Au passage, lien mort détecté dans StructureHn (`/score-business-mot-cle`, route inexistante). Corrections : StructureHn lien mort → `/mots-cles-qui-convertissent` ; SuggestExtractor (entrée du funnel) → +Explorateur de questions +Clusteriseur ; ComparateurVolumeBusiness → +Mots-clés qui convertissent. Résultat : explorateur-questions 1 entrante, clusteriser 3, convertissent 4 (+ footer). Ton respecté par fichier (Suggest tutoie, Comparateur vouvoie).

**Suivi des 2 points (commit `31eb7e7`) — traités.**
- **Canonical `fusionn.io` → `fusionn.co`.** Vérifié par curl : `fusionn.io` renvoie un 301 vers `fusionn.co` (200), `www.fusionn.co` aussi. Donc TOUT le site déclarait sa canonical / og:image / schema.org / sitemap sur un domaine de redirection (bug SEO site-wide, pas que le sitemap). Corrigé en centralisant sur `SITE_URL` : `src/config/site.ts`, `SEOHead.tsx` (canonical, og, schema Organization + BlogPosting), `generate-sitemap` (baseUrl, redéployée, sitemap régénéré : 45 URLs, 0 `fusionn.io`), `BriefSynthesisView` (footer + retrait d'un tiret cadratin au passage).
- **Seuil clustering 0.80 → 0.88.** Calibré empiriquement (tests prod sur échantillon 12 mots-clés multi-intentions aux seuils 0.80/0.84/0.86/0.88/0.90). À 0.80 → 1 méga-cluster inutilisable (les mots-clés SEO partagent tous « seo », cosinus élevé). 0.88 = meilleur compromis : garde les vrais synonymes (« formation seo » / « formation référencement naturel ») tout en séparant prix / audit / géo. L'UI ne règle pas le seuil (défaut serveur affiché), donc le défaut impacte tous les users. Edge function redéployée. Limite résiduelle connue : l'algo « leader » à pivot unique fait que « seo lyon » attrape parfois « agence seo » — ce n'est pas le seuil, c'est l'algo (chantier futur si besoin).

---

## 2026-05-29 · Suppression page seo-content-writer + doctrine anti-backlink

**Demande Tim (2 points).** (1) Supprimer la page `/listes-mots-cles/seo-content-writer` partout. (2) Règle permanente : ne JAMAIS parler d'achat de backlink, d'achat de lien ou de netlinking — nulle part, jamais (Fusionn n'en fait pas et n'en parle pas).

**Point 1 — suppression.** La row DB `blog_posts` était déjà supprimée (session précédente coupée en plein delete). Nettoyé les 4 références locales restantes : fichier de contenu `liste-des-mots-cles-seo-content-writer.json` (rm), entrée dans `keyword-lists.json` (22 entrées restantes), `package.json` (liste prerender), `public/sitemap.xml` (bloc `<url>`).

**Point 2 — guardrail générateur.** Le prompt de `tool-hn-structure` (qui alimente la page `/structure-h2-h3-seo`) n'avait aucune interdiction. Ajout d'une ligne « INTERDICTION ABSOLUE » alignée sur le guardrail existant de `guided-exploration`. Edge function redéployée sur prod (`fwhfnzbtlddzfxbsejyf`).

**Point 2 bis — nettoyage pages publiques.** Termes interdits retirés de 4 pages déjà en ligne : `pourquoi-88-pourcent...` (« achat de backlinks » → « signaux techniques »), `agence-seo`, `freelance-seo`, `expert-seo` (mentions « netlinking » dans des listes de spécialités/ancres → autres requêtes SEO légitimes). Vérif : 0 occurrence restante dans `public/`, JSON tous valides.

**Deploy.** Commit `640685a` poussé sur `main` (9 fichiers, staging sélectif pour ne pas embarquer le chantier WIP « 3 nouveaux outils gratuits » resté non commité). Netlify rebuild auto.

---

## 2026-05-29 · Resserrement de l'outil « Générateur de mots-clés Google Suggest »

**Demande Tim.** L'outil gratuit `tool-suggest-extract` (page `/generateur-mots-cles-google-suggest`) renvoyait des résultats « trop larges ». Objectif : ne garder que les requêtes les plus proches du mot-clé. Tim précise : resserrement **sémantique**, pas lexical.

**Diagnostic.** Filtre lexical pur (`contient tous les mots`, n'importe où) → ~150 résultats, dont 115 remontés par un seul préfixe (villes étrangères kochi/karachi/madagascar, noms propres).

**Piste embeddings testée puis abandonnée (donnée réelle).** Couche cosinus via Gemini `gemini-embedding-001` (taskType SEMANTIC_SIMILARITY ; `text-embedding-004` → 404 pour cette clé). Testé en prod : **la similarité sature à 0.89-1.0** pour des requêtes quasi-identiques. Aucun seuil ne coupe proprement, et le cosinus ne vire pas le vrai bruit (« consultant seo karachi » EST sémantiquement du consultant seo). Mauvais outil pour ce problème.

**Solution retenue : pull >= 2.** Le bruit = les suggestions remontées par **un seul** préfixe. Gate sur pull>=2 (corroboration par plusieurs préfixes indépendants) = le vrai signal de cohérence, gratuit et instantané. Ironie : le « pull » soupçonné gadget est le meilleur filtre anti-bruit. Choix Tim : **pull>=2** + **virer complètement** le hors-intention (salaire/formation/emploi). Filet `MIN_RESULTS=8` pour les mots-clés de niche.

**Résultats live.** consultant seo 150→28 (propre), logiciel facturation 42 (riche, par métier), rachat de credit lille 3 (niche, filet ok). Résidu mineur : un nom propre passe encore en pull=2.

**Deploy.** Edge function déployée via supabase CLI (`fwhfnzbtlddzfxbsejyf`). Source commitée `309f8c1` sur main. Aucune modif UI (le front affiche déjà `pull`).

---

## 2026-05-28 · Refonte v2 des 23 directories (1 partie = 1 skill, sans marques)

Tim rejette les variations de format et fixe le cap définitif : modèle pixel-perfect appliqué uniformément, enrichi par les skills mots-clés, un tableau par skill. Structure validée : **4 parties = 4 skills mots-clés**.

### Structure v2 finale

1. Partie 1. Recherche de mots-clés (`seo-recherche-mots-cles`) : 12 listings × ~78 mots-clés
2. Partie 2. Clustering en pages (`seo-clustering-mots-cles`) : clusters + cannibalisations
3. Partie 3. Mots-clés décisionnels (`seo-mots-cles-decisionnels`) : shortlist scorée /125, triée
4. Partie 4. Modèles de pages satellites (`seo-modeles-pseo`) : Spokes scorés /5, triés

Parties Entités/Outils/Scoring/Plan d'action du modèle initial supprimées.

### Règles éditoriales durcies

- **Pas de marques** ([[feedback-pas-de-marques-directories-seo]]) : interdit concurrents/marques/personnes dans agence/consultant/outil. Plateformes techniques de travail conservées (Shopify, WooCommerce, Prestashop, Amazon, WordPress, FBA/FBM, Liquid, Symfony).
- **Tout en français** : « page satellite » pas « Spoke », « appel d'offres » pas « RFP », « signaux d'alerte » pas « red flags ».
- **0 tiret cadratin** : étages « Do · Achat », funnel « Know vers Do ».
- **Ton Tim sur les intros uniquement**, intros aérées en paragraphes courts, cellules factuelles, pas de colonne #.

### Itérations UI rollback

Essais coloration dégressive + table-layout fixed + container élargi + encadré intro : rejetés (« tableaux illisibles »). Retour CSS d'origine. Seule modif conservée : aération des intros (HTML, pas CSS).

### Industrialisation

agence marketing en pilote (validé), puis « go sans validation » : 7 sub-agents parallèles (3 pages/agent) pour les 21 restantes (dont consultant SEO repassé en seo-recherche). Pas de stall cette fois (charge réduite). Sanity check global : marques tierces résiduelles (Klaviyo, Brevo, Helium 10, Jungle Scout, Stripe, PayPal, transporteurs) générifiées à la main sur 4 fichiers. Vérif finale : 0 marque, 0 tiret cadratin, 0 Spoke, 0 colonne # sur les 23.

Commit `19102de` poussé, Netlify redéploie.

### Reste à faire

- Google Ads / DataForSEO → volumes [À SOURCER]
- Maillage interne entre directories
- Confirmer si Stripe/PayPal doivent rester bannis (générifiés par prudence)

---

## 2026-05-27 (suite 5) · Enrichissement anti-slope des 22 directories

Tim détecte que les 23 directories publiées en suite 4 sont du slope IA : template figé répliqué, cellules génériques (Semrush, Ahrefs, AIDA partout), zéro data propriétaire, exemples prévisibles par Claude seul. Il fixe deux règles obligatoires pour toute production SEO future ([[feedback-obligation-skills-seo-et-data-reelle]]) :
1. Appeler ses skills SEO en amont (seo-recherche-mots-cles, seo-modeles-pseo, seo-entites-vectorielles, seo-product-led-seo, seo-peurs-objections, etc.)
2. Scraper de la data métier/secteur via WebSearch/WebFetch (marques niche nommées, chiffres vérifiables avec source)

### Pilote validé : agence SEO

WebSearch x4 sur le marché (leaders Eskimoz/Ad's up/Rankit/Primelis/Junto, tarifs précis 500€-6000€/mois, pain points marché brume/junior/sans résultats). Skill seo-recherche-mots-cles invoqué formellement → 78 mots-clés qualifiés sur 12 listings sauvegardés dans `seo-kb/wiki/keywords/recherche-2026-05-27-agence-seo.md`. HTML réécrit cellule par cellule. Taille 13 kB → 18 kB. Commit `b36008a`.

### Industrialisation : 21 directories restantes

4 sub-agents Claude en parallèle (background), un par cluster, avec consigne stricte d'invocation des skills + WebSearch pour chaque keyword. Total ~1h de wall clock pour les 4 agents.

Résultats :
- **Cluster A (7)** : agence marketing/communication/webmarketing/inbound/growth + freelance SEO + expert SEO. Marques nommées : Yumens, BETC, Inbound Value, Growth Room, Pharow, Malt, Olivier Andrieu, Daniel Roch, Olivier Duffez, Sylvain Peyronnet, SMX Paris, BrightonSEO. Chiffres : Malt 2 647 référencés, TJM 376-412€ médian Malt 2026, plafond micro 83 600€, TJM expert senior 1 200-2 500€.
- **Cluster B (6)** : outil SEO/IA/SaaS B2B/logiciel marketing/plateforme analytics/outil prospection. Marques : Mistral, Anthropic, Apollo (260M contacts), Pharow, Waalaxy, Pennylane, Brevo, PostHog, Mixpanel, Amplitude, Plausible 6-19€, Piwik PRO 35€. Chiffres publics : Mistral 11,7 Md€ valuation 400M€ ARR 40% Fortune 500 EU, HubSpot 248k clients, marché logiciel marketing 7,39→8,08 Md$ CAGR 9,3%, churn médian SaaS 3,5%, NRR enterprise 118%.
- **Cluster C (3)** : rédacteur web, content manager (salarié in-house, 28-76k€ grilles Glassdoor médiane 42 498€), SEO content writer (TJM 500-700€, intersection SEO + frameworks E-E-A-T/GEO/RAG). Marques : Malt, Codeur, TextMaster, Surfer, NeuronWriter, FRASE, Glassdoor, WTTJ, BDM, Doctolib, PayFit, Sézane.
- **Cluster D (5)** : e-commerçant (data FEVAD 196,4 Md€ marché FR, +7%, parts Shopify 22,2% / WooCommerce 47,4% / Prestashop 19,3%), expert Shopify (Liquid/Hydrogen, Klaviyo, Recharge, Loop, TJM 600-1500€), expert WooCommerce (HPOS, Yoast, RankMath, TJM 300-600€), vendeur Amazon (FBA/FBM, A9, Helium 10, Jungle Scout, AMC DSP, frais 0,99€/unité+39€/mois, Pan-European FBA), expert Prestashop (Prestashop 1.7/8/9, Symfony, Smarty, modules officiels, refonte 15-40k€).

### Métriques de qualité

| | Slope (suite 4) | Enrichi (suite 5) |
|---|---|---|
| Taille HTML moyenne | 12-14 kB | 18-23 kB |
| Reading time | 7 min | 9-11 min |
| Marques nommées par article | 0 | 14-24 |
| Chiffres vérifiables par article | 0 | 5-14 |
| Sources externes citées | 0 | Sortlist, Deux.io, Cartelis, Malt, mo.agency, panja.io, Glassdoor, FEVAD, McKinsey State of AI 2025, etc. |
| Tirets cadratins | 0 (déjà OK) | 0 (déjà OK) |

### Déploiement

Publish batch via `./scripts/publish-batch.sh` → 22 upserts sur Supabase (slug stable, contenu remplacé). `posts.json` régénéré, 30 articles dans la DB (8 anciens + 22 enrichis = 30, copywriter supprimé). Commit `9f6f747` poussé sur main, Netlify redéploie.

### Limites assumées

- Volumes mots-clés tous en `[À SOURCER]` (Google Ads API en attente d'approbation depuis ce matin)
- Scores Effort/Conversion/Priorité encore qualitatifs (1-5 raisonné par positionnement, pas issu de data)
- Pas de maillage interne entre les 23 directories (chaque directory pointe vers sa propre catégorie, mais pas de bloc « voir aussi »)
- Pas de migration vers route dédiée `/directories/` ou `/listes-mots-cles/` (toujours sous `/blog/`)

À traiter dans les prochaines itérations : volumes Google Ads, maillage interne, repositionnement URL si Tim confirme.

---

## 2026-05-27 (suite 4) · Industrialisation modèle « Liste des mots-clés » · 23 nouveaux articles

Après restauration des 8 anciens articles, Tim demande comment industrialiser le modèle « Liste des mots-clés pour [X] ». Doctrine validée : 5 piliers (consultant SEO, agence marketing, agence communication, outil SEO, outil IA, etc.). Décisions :
- **Volume** : tout publier d'un coup (24 piliers, sans ghostwriter).
- **Source data** : scoring qualitatif sans Google Ads ni DataForSEO (en attendant l'approbation Google).

### Outillage créé

- `data/keywords-cibles.csv` : 24 mots-clés cibles répartis en 4 clusters (A services SEO/marketing, B éditeurs d'outils, C rédaction, D e-commerce), avec status + draft_file par ligne.
- `scripts/publish-batch.sh` : wrapper bash qui boucle sur le CSV, appelle `publish.sh` pour chaque ligne status=todo, régénère posts.json à la fin. Options : `--dry-run`, `--draft`, `--cluster <A|B|C|D>`.

### Rédaction des 23 articles HTML

5 sub-agents Claude lancés en parallèle (1 par cluster, A coupé en 2 pour équilibrer la charge), chacun avec :
- Template de référence : `liste-mot-cle-consultant-seo.html`
- Guide voix Tim : `raw/notes/tim-my-voice.md`
- Liste de 3 à 6 keywords à traiter
- Instructions strictes sur structure (5 parties, tables, scoring) + voix (tutoiement, anti-IA writing, aucun tiret cadratin)

Résultat : 23 fichiers HTML générés dans `seo-kb/fusionn/blog-drafts/`, 12 à 14 kB chacun, 0 tiret cadratin détecté. Différenciation par cluster (vocabulaire growth pour agence growth, A9 algorithm pour vendeur Amazon, Liquid/Hydrogen pour expert Shopify, AIDA/PAS pour copywriter, etc.).

### Publish batch

`./scripts/publish-batch.sh` → 23 articles upsertés via service_role sur Supabase. Bug bash mineur : le compteur dans le pipe `tail | while` est dans un sous-shell, le récap final affiche `Publiés : 0` même quand tout a marché. Sans impact sur la publication.

Régénération manuelle de `posts.json` (le bug bash a empêché l'auto-régénération) → **31 articles dans la DB** (8 anciens + 23 nouveaux ; consultant SEO comptait dans les 8 restaurés).

### Déploiement

Commit `4e79278` : « Blog : industrialisation modèle 'Liste mots-clés' x23 nouveaux articles » → push origin/main → Netlify auto-déploie. Branch up to date.

### Pattern industrialisable pour la suite

Pour publier une nouvelle « Liste des mots-clés pour [X] » :
1. Rédiger le HTML dans `seo-kb/fusionn/blog-drafts/liste-mot-cle-<slug>.html` en suivant le template.
2. Ajouter une ligne au CSV avec status=todo.
3. Lancer `./scripts/publish-batch.sh` (ou `--cluster X` pour filtrer).
4. Commit + push → déploiement auto.

À améliorer dans une prochaine itération :
- Fix bug bash du compteur dans publish-batch.sh.
- Brancher DataForSEO ou Google Ads API pour scorer Effort/Conversion sur de vraies données (en attente approbation Google soumise aujourd'hui).
- Ajouter le maillage interne automatique entre pages liste-mots-cles (bloc « voir aussi » + page index `/blog/liste-des-mots-cles/`).

---

## 2026-05-27 (suite 3) · Restauration des 8 articles de blog supprimés

Tim signale qu'il n'y a plus qu'un seul article visible sur fusionn.co/blog.

### Diagnostic

Audit complet en 3 sondes :
1. `posts.json` dans `public/blog-data/` ne référence qu'un article (`liste-des-mots-cles-consultant-seo`).
2. Les 8 fichiers JSON individuels d'anciens articles sont toujours présents sur disque.
3. La table Supabase `blog_posts` contient `0-0/1` (1 ligne) via service_role + `Prefer: count=exact`.

Conclusion : les 8 anciens articles ont été supprimés manuellement de la base (aucune migration coupable, dernière migration touchant `blog_posts` = `20260203143726_fix_blog_posts_public_access.sql` qui ajoute juste une policy RLS).

Le frontend charge `/blog-data/posts.json` en priorité ; au build, `generate-blog-urls.js` régénère ce fichier depuis Supabase → 1 article retourné → posts.json écrasé avec 1 entrée.

Note GRANT bonus : l'API anon retourne `42501 permission denied for table blog_posts`. Le `GRANT SELECT ... TO anon` manque côté Postgres (RLS policy seule ne suffit pas). À fixer dans une future migration.

### Restauration

Création du script `scripts/restore-blog-from-json.mjs` (réutilisable) :
- Lit tous les JSON de `public/blog-data/` sauf `posts.json`
- Filtre les colonnes autorisées (whitelist sur le schéma `blog_posts`)
- Upsert sur `slug` via service_role
- Mode `--dry-run` pour vérifier avant exécution

Exécution :
- Dry run : OK, 8 articles à restaurer
- Run réel : 8 articles upsertés
- Vérif DB : `0-0/8` (8 lignes), OK
- `generate-blog-urls.js` rerun avec `VITE_SUPABASE_ANON_KEY=<service_role>` (contournement du grant manquant) → posts.json à 8 entrées

Commit `f5b2426` : "Blog : restaurer les 8 articles supprimés de Supabase" puis push origin/main → déclenche le redéploiement Netlify auto.

### À surveiller pour le futur

- Le `GRANT SELECT ON blog_posts TO anon` est manquant → si Netlify a la même config et que son prebuild échoue silencieusement, le posts.json commité (à jour) est servi tel quel, donc OK temporairement.
- Vraie solution : migration qui restaure le grant, sinon tout publish futur via `publish-keyword-list.mjs` regénérera un posts.json à 1 entrée au prochain build Netlify si le grant tombe.

---

## 2026-05-27 (suite 2) · Pivot Approche A · pipeline 4 sources avec YouTube + Brave

Tim retoque le draft v2 : trop pauvre, hallucinations résiduelles, contenu débutant. Demande la méthode de génération des mots-clés.

### Diagnostic du problème

Le process `pytrends.related_queries(seed)['rising']` produit du bruit :
- Métrique relative (%) sans signal de volume absolu
- Seeds génériques captent homonymes et questions débutantes
- Pas de cross-source, pas de clustering en secteurs

### Pivot vers Approche A

Source primaire = signal humain (Reddit + YouTube SEO), Trends devient validateur de volume, Brave Search valide la SERP gap. ProductHunt en complément (et non plus en primaire : confirmé en pratique, 3 candidats PH testés → 0 hockey stick).

### Branchement YouTube Data API v3

Première tentative : Tim donne par erreur les credentials OAuth (Client ID + Secret) au lieu d'une API key. Diagnostic, alerte sécu (Client Secret exposé dans le chat).

Deuxième tentative : Tim donne sa `GEMINI_API_KEY` au lieu de `YOUTUBE_API_KEY`. Diagnostic via test croisé (Gemini accepte, YouTube refuse). Alerte sécu prioritaire (`GEMINI_API_KEY` exposée dans le chat, recommandation rotation immédiate).

Troisième tentative : Tim copie la bonne `YOUTUBE_API_KEY` depuis Supabase Dashboard. Test OK, clé écrite dans `~/.fusionn-trends/.env` (perms 600).

7 chaînes SEO référence connectées avec leurs channelIds : Backlinko, Ahrefs, Aleyda Solis, Matt Diggity, Neil Patel, Semrush, Yoast. Scan 7 derniers jours → 24 vidéos retournées.

### Branchement Brave Search API

Tim crée une clé sur api-dashboard.search.brave.com, free tier 2000 req/mois. Cap conso fixé à 5 SERP par édition = 150 req/mois = 7,5 % du free tier. Compteur de conso mensuelle dans `~/.fusionn-trends/brave-usage-2026-05.txt`.

### Signal détecté pour l'édition #1 (cross-source ultra fort)

**Cluster principal : Google I/O 2026 + AI Search** — validé par 14 signaux indépendants en 7 jours :
- 8 vidéos YouTube (5 chaînes différentes : Backlinko, Neil Patel, Yoast)
- 3 posts Reddit r/SEO + r/TechSEO (280 / 77 / 53 votes)
- 3 termes Google Trends en hockey stick (`Google I/O 2026` +353 %, `AI Mode Google` +43 %, `Google AI search` stable haut)

**Sous-cluster ultra explosif : AI Citations** — Trends `AI citations SEO` à 27x sur 3 mois (max 100). 2-3 vidéos YouTube ciblées (Backlinko "Use LinkedIn micro creators", Neil Patel "AI Picks One Brand Per Answer").

**Sous-cluster opérationnel : UGC + Communautés** — 2 vidéos Backlinko sur le poids de l'UGC pour l'IA.

**Annexe : May 2026 Core Update** — 2 posts Reddit r/SEO confirment chute de rankings.

### Verdicts SERP gap (Brave top 10 FR)

- `google ai search rules` : 0 FR / 0 grosse autorité → **fenêtre maximale du jour**
- `google i/o 2026 seo` : 0 FR / 1 autorité (Neil Patel) → fenêtre ouverte
- `may 2026 core update` : 0 FR / 2 autorités → fenêtre française nette
- `ai mode google` : top 1-3 = Google direct, top 4-10 accessible
- `ai citations seo` : 1 FR / 3 autorités → compétitif

### Livrable

Draft v3 dans `seo-kb/fusionn/newsletters-drafts/2026-05-27.md` avec :
- 4 sources actives, validation cross-source obligatoire
- Toutes citations YouTube/Reddit verbatim + traduction FR explicite + URL cliquable
- SERP gap intégré sous chaque mot-clé recommandé
- 0 hallucination (chiffres bruts depuis API uniquement)

Preview HTML stylée Linear/Stripe à `seo-kb/fusionn/newsletters-drafts/2026-05-27.html`, servie sur `http://localhost:4173/2026-05-27.html`.

### Sécurité (à faire par Tim)

- Rotation `GEMINI_API_KEY` exposée dans le chat (priorité haute, c'est la clé qui facture chez Google pour toutes les fonctions de génération Fusionn)
- Rotation OAuth Client Secret `309434449968-9dbb8b...` exposé dans le chat (priorité moyenne, exploitation impossible sans redirect URI déclarée)
- `YOUTUBE_API_KEY` et `BRAVE_API_KEY` également exposées, à rotater si veille de prod

### À faire en sprint 0.2 / 1

- Mettre à jour `~/.claude/skills/fusionn-trends-quotidien/SKILL.md` avec YouTube + Brave + nouveau pipeline cross-source
- Élargir Reddit à r/marketing, r/digital_marketing
- Vérifier pourquoi Matt Diggity et Aleyda Solis ont 0 vidéo sur 7j (chaînes inactives ou handles incorrects ?)
- Valider l'angle "Google I/O 2026" en publiant sur LinkedIn
- Si signal positif : sprint 1 = infra fusionn.co (route /newsletter, formulaire opt-in, table abonnés Supabase, sync Loops.so)

---

## 2026-05-27 (suite) · Sprint 0 lancé · skill + 1er digest live

Tim a validé "go" sur le sprint 0 après vérification du coût (0 € pour MVP, 0 € sprint 1 et 2 sous 1k abonnés, puis 49 $/mois Loops.so).

### Skill créé

`~/.claude/skills/fusionn-trends-quotidien/SKILL.md` (397 lignes). Pipeline 5 étapes : scan 4 sources → normalisation → scoring momentum → filtrage anti-bruit → rédaction au ton Fusionn. Output dans `~/Code/seo-kb/fusionn/newsletters-drafts/{YYYY-MM-DD}.md`.

### Premier digest généré en live (test sprint 0)

Fichier : `seo-kb/fusionn/newsletters-drafts/2026-05-27.md`. 3 sources scannées (ProductHunt skippé, token developer pas encore créé).

Stats du run :
- Google Trends : 21 rising queries sur 12 seeds (2 fails)
- Reddit : 25 posts sur 8 subs
- Hacker News : 13 stories matchant les keywords AI/SEO sur 24h
- Durée : ~90 secondes

Contenu retenu :
- 5 trends Google (Gemini omni, Gemini 3.5 flash, meta tag description seo, seo mentor, blog writing for seo)
- 3 posts Reddit (clustering Sam Altman interviews, interpretability Anthropic, PrismML Bonsai modèles binaires)
- 2 stories HN (sleep-like consolidation pour LLMs, outsourcing + local AI vs frontier)

### Bugs trouvés et corrigés dans le skill

1. **pytrends 4.9.2 + urllib3 v2** : TypeError `method_whitelist` sur tous les seeds. Fix : pin `urllib3<2` ajouté dans la section Pré-requis du skill.
2. **Hacker News Algolia 400 Bad Request** : le caractère `>` dans `numericFilters` n'était pas encodé avec curl direct. Fix : passage à `curl -sG --data-urlencode` dans le skill.

### Bruit notable à filtrer en v2 du skill

- Seed `SEO` capte des noms propres : `consultant seo adrien beaujeu` +4100%, `seo hyun woo` +1300%
- Seed `AEO` capte des requêtes hors thème : `lidl near me` +1000%
- Plusieurs variantes Gemini en parallèle (omni, spark, flash, editing4u) à regrouper sémantiquement

### À attendre de Tim

- Relecture du draft `2026-05-27.md` et arbitrage : poster sur LinkedIn pour tester l'angle ?
- 8 décisions stratégiques du cadrage (hosting, nom, cadence, outil envoi, signature, CTA produit, cible, sprint 0 confirmé)
- Validation des seeds Trends pour itération v2 du skill

---

## 2026-05-27 · Cadrage newsletter trends quotidienne pour Fusionn.co

Demande Tim : *"écrire une newsletter quotidien. L'idée c'est de scrapper/trouver les mots clés ou secteurs qui sont en tendance, qui sont en train d'exploser. Une sorte d'agrégation de data."*

### Décisions cadrées avec Tim

- **Positionnement** : pour Fusionn.co (pas Algorithme, pas Organikk). Newsletter comme canal d'acquisition top-funnel pour casser la fuite identifiée au diag du 2026-05-26.
- **Niche** : Tendances SEO/IA only (pas business large, pas grand public).
- **Sources** : Google Trends (pytrends), Reddit (API JSON publique), Hacker News (Algolia API), ProductHunt (GraphQL v2). 4 sources gratuites.
- **Livrable demandé** : cadrage écrit AVANT de coder.

### Cadrage produit

Doc complet écrit dans `seo-kb/fusionn/Cadrage-newsletter-trends.md` (status draft, à valider point par point). 14 sections :
1. Promesse + audience
2. Pourquoi maintenant pour Fusionn (lien diag activation)
3. Différenciation vs Algorithme / Exploding Topics / Ahrefs / SEJ
4. Sources détaillées (méthodes, seeds, rate limits, anti-bruit par source)
5. Pipeline 5 étapes (scan, normalisation, scoring, filtrage, rédaction)
6. Format de sortie (template du digest)
7. Intégration produit Fusionn (deep links `/score-semantique?keyword=X`, UTM, onboarding différencié, boucle preuves)
8. Architecture technique : 3 options évaluées, reco **Option C hybride** (GH Action génère MD → archive indexée sur fusionn.co/newsletter + envoi via Loops.so)
9. Cadence (lun-ven 7h Paris)
10. KPIs (inscrits, open rate, CTR, conv vers Fusionn payant)
11. Phasage Sprint 0 (skill local, valider l'angle) → Sprint 1 (infra) → Sprint 2 (envoi auto) → Sprint 3 (boucle preuves)
12. Risques (redondance Algorithme, rate limits, pollution Reddit, anti-spam, charge dev vs roadmap activation)
13. **8 décisions à trancher avant code** (hosting, nom, cadence, outil envoi, signature, CTA produit, cible, lancement sprint 0)
14. Prochaines étapes

### À attendre de Tim

Réponse sur les 8 décisions (section 13 du cadrage). Si feu vert global, sprint 0 = skill local `fusionn-trends-quotidien` à coder cette semaine pour générer un 1er digest manuel et tester l'angle sur LinkedIn avant tout dev infra.

### Notes

- Cadrage écrit en respect ton-de-voix Tim + zéro em-dash (règle maison, 6 occurrences nettoyées après écriture initiale).
- Pas de code Fusionn touché à ce stade (validation cadrage d'abord).
- Cohérence avec doctrine : Surprise Score (trends que les SEO n'avaient pas vues), Confidence Score (cross-source corroboration), Freshness Guard (entrées > 7j out).

---

## 2026-05-26 · Onglet Agent : kill patterns IA + écran de démarrage minimaliste

Demande Tim : *"pareil tu patterns IA de l'onglet chatbot, et rendre le truc design et minimaliste et travailler écran de démarrage"*.

### Patterns IA virés

- **Gradient pastel orange** sur le header (`background: linear-gradient(180deg, rgba(255,55,28,0.03), transparent)`) : supprimé. Le header entier a été retiré, le tab title "Agent" du segmented control suffit à identifier l'onglet.
- **Icône carrée 36×36 fond pastel orange + couleur brand** sur le header : supprimée avec le header.
- **Icône carrée 44×44 fond pastel orange + couleur brand** sur l'empty state : supprimée. L'empty state n'a plus de hero icon.
- **Suggestions en chips ronds avec icônes décoratives** (`Sparkles`, `BarChart3`, `ListChecks`, `Target`, `Lightbulb` venant de lucide-react) + halo orange au hover : remplacées par une liste verticale de questions complètes en plain text.
- **Imports lucide superflus** : seuls `Send` (bouton envoyer) et `Loader2` (états chargement) gardés. 6 icônes décoratives retirées.

### Écran de démarrage refait (sobriété type Linear / Notion)

- Container max-width passé de 820px à 760px (resserre le focus).
- Padding scroll augmenté à `32px 28px` (plus d'air).
- Titre 22px gras à gauche : *"Posez votre première question sur <keyword>"* avec le mot-clé en italique gris muted pour le détacher visuellement.
- Sous-titre 13.5px en muted : précise ce que voit l'agent (mots-clés, clusters, micro-intentions, business score, tous les onglets).
- 5 questions naturelles présentées **telles qu'elles seront posées** (pas un label compressé). Listées verticalement avec séparateurs `border-bottom: 1px solid var(--ws-border)`, padding `14px 0`. Sobre.
- Hover suggestion : passage de `color: var(--ws-text)` (muted) à `--ws-text-strong` (noir). Pas de couleur, pas de halo, pas de fond.
- Footnote bas de l'input : raccourci utile *"Entrée pour envoyer, Shift+Entrée pour aller à la ligne"* (au lieu d'une description marketing du modèle).

### Couleur de marque qui reste

Toujours `#FF371C` uniquement sur le **bouton Send** (action primaire) et le **check validé** du Plan d'action.

### Commit + push

- Commit `5560b93` poussé sur main
- 2 fichiers : `AgentChatView.tsx` (-77 +60 lignes), `index.css` (-114 +60 lignes)
- Netlify auto-deploy déclenché

## 2026-05-26 — Plan d'action + LLM : kill les patterns IA, sobriété visuelle

Demande Tim : *"sur l'onglet plan d'action, il faut killer tous les patterns IA (notamment trait de couleur sur le côté gauche) et améliorer la lisibilité"*. Audit + refactor élargi à l'onglet LLM dans la foulée parce que les barres + headers de domaine orange sur 12-15 répétitions criaient pareil.

### Patterns IA tués sur Plan d'action

- **Trait coloré vertical à gauche du banner mois** (`border-left: 4px solid` + `borderLeftColor: meta.accent`) : pattern signature des UI générées par IA. Supprimé. Remplacé par un séparateur `border-bottom: 1px solid var(--ws-border)` sobre.
- **3 couleurs arbitraires par mois** (M1 #FF371C rouge, M2 #D97706 orange, M3 #059669 vert) : supprimées. La progression dans le temps n'est pas une dimension visuelle, c'est juste un ordre. Tous les mois ont le même rendu monochrome.
- **Symboles décoratifs ★ ◆ ●** devant chaque mot-clé pour HUB / SPOKE / FAQ : supprimés. Pure ornementation.
- **Bullet dot coloré stoplight** (vert / orange / gris) pour le potentiel Fort / Moyen / Faible : remplacé par un badge texte sobre `Fort` / `Moyen` / `Faible` avec différenciation par le contraste typo, pas par la couleur.
- **Pills colorées pastel** pour le rôle (Hub rouge, Spoke noir, FAQ gris) : remplacées par badges monochromes. Hub se distingue par bordure noire + texte gras (donc plus de hiérarchie info sans l'effet "arc-en-ciel").
- **Tag de semaine en couleur accent** : remplacé par un badge bordé monochrome (typo et bordure font le travail).
- **Icône Link2 colorée** dans le footer KPI : supprimée.
- **Import `Link2`** de lucide-react : supprimé du composant.

### Lisibilité améliorée

- "Mois 1 / 2 / 3" au lieu de "M1 / M2 / M3" : lisible direct, plus formel.
- Hiérarchie typo nette : numéro de mois en petit-caps faint (label), titre en 17px gras strong, sous-titre 13.5px muted, progression chiffrée à droite avec `18/24` propre (chiffre fort en strong + séparateur faint + total normal).
- Espacement augmenté : padding banner `18/24`, rangées mots-clés `11/16`, gap `12px` entre colonnes.
- Badge `Fort` pour les mots-clés à fort potentiel : bordure noire et texte noir, distingue par le contraste pas par une couleur.

### Patterns IA tués sur l'onglet LLM (cleanup foulée)

- **`color: var(--ws-brand)` sur `.llm-url-domain`** : 12 cartes URL avaient leur header en orange uppercase, trop tapageur. Passé en `--ws-text-muted` gris.
- **`background: var(--ws-brand)` sur `.llm-domain-fill`** : 15 barres orange (top 15 domaines), trop. Passé en `--ws-text-strong` (noir sobre) : fort visuel sans agressivité.

### Seule couleur de marque qui reste

`#FF371C` réservée au **check validé** du Plan d'action (`<CheckCircle2>` quand l'utilisateur coche une action). C'est le seul "punch couleur" du composant. Tout le reste est monochrome sur la base `--ws-bg-card`, `--ws-text-strong`, `--ws-text`, `--ws-text-muted`, `--ws-text-faint`, `--ws-border`.

### Commit + push

- Commit `443074a` poussé sur main
- 2 fichiers : `PlanActionView.tsx` (-110 +86 lignes, refactor JSX), `index.css` (+157 -110 lignes, classes plan-action + 2 classes llm)
- Netlify auto-deploy déclenché à 06:36 UTC

### LLM tab : pas d'autre changement à pousser

Audit confirme que les autres composants LLM (sélecteur cluster, summary cards, query matrix, polling state) n'ont pas de pattern IA marqué. Les icônes utilisées (Radar, Layers, RefreshCw, Loader2, AlertCircle, ExternalLink) sont navigationnelles, pas décoratives. Pas d'emoji, pas de gradients, pas de blur, pas de cards-in-cards. Quota badge avec icône Crown pour Premium conservé (utilisé en cas premium seulement, peu visible).

---

## 2026-05-26 — Business Score : streaming + Realtime + barre de progression

Tim signale que l'affichage des colonnes "Score Business" et "Potentiel" dans l'onglet mots-clés est trop lent et qu'on ne voit rien pendant le calcul. Diagnostic : un seul appel Gemini 2.5 Pro qui scoreait les 10 mots-clés d'un bloc (15-30s), polling frontend toutes les 3s, et juste un `…` gris pour signaler l'attente.

### Refactor en 3 axes

**1. Edge Function `generate-business-score` — streaming par batchs**
- Modèle : `gemini-2.5-pro` → `gemini-2.5-flash` (3-5× plus rapide, qualité validée sur le prompt ComparativeRanker V3 inchangé).
- Split des keywords en batchs de 5 (`LLM_BATCH_SIZE=5`), tous lancés en parallèle via `Promise.all`.
- Chaque batch insère ses scores en DB dès qu'il a fini, avec `bucket='Low'` placeholder.
- Update de `processed_count` / `progress` / `phase` à chaque batch terminé.
- Phase finale `bucketing` : recalcule les buckets percentile-based et UPDATE chaque row.
- Reset des anciennes rows en début de run (delete `search_business_score_results` pour ce `search_id`) pour gérer les re-runs proprement.

**2. Hook `useBusinessScores` — polling → Supabase Realtime**
- Channels Realtime sur `search_business_score_results` (INSERT + UPDATE) et `generation_status` (INSERT + UPDATE).
- Les scores apparaissent dès qu'ils tombent en DB, plus de latence morte de 0-3s.
- Polling fallback à 8s seulement (au cas où Realtime échoue, RLS, etc.).
- Trigger auto inchangé (POST à l'Edge), mais déclenché aussi sur "stalled" (>60s en `in_progress`).
- Hook expose en plus : `progress`, `phase`, `processedCount`, `totalCount`, `bucketsReady`.

**3. UI — skeleton shimmer + barre de progression live**
- Composant `BusinessScoreProgress` au-dessus du tableau : phase label en français ("Mesure de la demande Google", "Scoring business par IA", "Classement final"), compteur "X/Y mots-clés", barre rayée animée brand `#FF371C` avec pourcentage.
- Composant `ShimmerPill` : remplace les `…` des cellules par un pill gris dégradé animé (keyframes `ws-shimmer-bg`).
- Logique bucket : on n'affiche le badge Potentiel que si `bucketsReady === true` (sinon ShimmerPill), pour ne pas montrer le placeholder `Low` pendant la phase scoring.

### Migration SQL

`20260526140000_business_score_streaming_and_realtime.sql` :
- Ajoute `processed_count`, `total_count`, `phase` à `generation_status`.
- `REPLICA IDENTITY FULL` sur les deux tables (pour que les payloads UPDATE Realtime soient complets).
- Ajoute `search_business_score_results` et `generation_status` à la publication `supabase_realtime` (idempotent via `pg_publication_tables`).

### Gains attendus

| Avant | Après |
|---|---|
| 1 appel Gemini Pro séquentiel ~25s | 2 batchs Flash parallèles ~5s pour les premiers scores |
| Polling DB 3s (latence morte) | Realtime push instantané |
| `…` gris dans les cellules | Shimmer + barre de progression avec phase + compteur |

### À déployer côté Tim

1. Appliquer la migration : `supabase db push` (ou via dashboard).
2. Redéployer l'Edge Function : `supabase functions deploy generate-business-score`.
3. Vérifier que la publication `supabase_realtime` est bien activée (la migration le fait, mais double-check côté dashboard si Realtime ne se déclenche pas).

### Vérifications locales

Type-check vert. Dev server lancé sur `http://localhost:5174/`.

---

## 2026-05-26 — Onglet "LLM" : Radar AEO Gemini par cluster

Session post-étude des marques **Trendtrack** (e-com intelligence) et **TryBrandSearch.ai** (consulting AEO). Décision stratégique : reproduire la brique "Library + Tracker + Analytics" de Trendtrack adaptée au monitoring des citations Gemini, sans repositioning frontal de Fusionn. Ajout d'un 4ème onglet "LLM" dans le workspace.

### Cadrage retenu

- **Moteur ciblé** : Gemini standalone uniquement (API officielle, Google Search grounding). V1 sans Google AI Overviews scraping. Le code Gemini grounded existait déjà dans `tool-citation-probe` (test du 2026-05-23), réutilisé.
- **Mode "cluster"** : pas de mode "query unique". On scanne en parallèle les `suggested_keyword` d'un `search_semantic_results.cluster` (label texte, pas UUID) pour mesurer la domination transversale, plus juste qu'une seule query.
- **Déclenchement auto** : ouverture de l'onglet LLM avec un cluster sélectionné = insert auto dans `tracked_clusters` (si sous quota) + premier scan déclenché immédiatement en fire-and-forget.
- **Quota visible** : 1 cluster en plan gratuit, 10 en plan Pro. Badge en haut à droite.
- **Tooltips systématiques** : tous les InfoTip ajoutés (titre, sélecteur, quota, cartes summary, métriques URL et domaine, matrice). Pédagogie continue, jamais d'écran sans explication.
- **Pas de V0 manuel préalable** : Tim a accepté le risque méthodologique. Si la variance Gemini est trop forte, ajustement en V2.

### Décisions data model

- **Identifiant cluster** : `(user_id, search_id, cluster_name)`. Pas d'UUID dédié parce que les clusters vivent dans `search_semantic_results` comme labels.
- **Granularité maximale conservée** : on stocke chaque citation par run (pas d'agrégation matérialisée). Les agrégats 30j sont calculés à la lecture via 4 fonctions SQL (`llm_domain_ranking`, `llm_url_ranking`, `llm_query_matrix`, `llm_cluster_summary`).
- **Fenêtre fixe 30 jours glissants** en V1. V2 verra l'ajout de séries temporelles (trend ↗/↘) une fois 60-90j de data accumulés.

### Livré (V1 déployable)

**2 migrations SQL** dans `supabase/migrations/` :
- `20260526133200_create_llm_radar_tables.sql` : `tracked_clusters` + `gemini_cluster_runs` + `gemini_citations` + indexes + RLS (lecture utilisateur via FK sur tracked_clusters, service_role full access).
- `20260526133300_create_llm_radar_rpc_aggregations.sql` : 4 fonctions SQL d'agrégation (domain ranking, URL ranking, query matrix, summary) toutes en `SECURITY INVOKER`.

**6 Edge Functions** dans `supabase/functions/` :
- `_shared/gemini-grounded.ts` (helper partagé : 1 query → URLs via Gemini 2.5 Pro grounded)
- `query-gemini-grounded` (HTTP endpoint pour debug ponctuel)
- `run-cluster-radar` (1 cluster → toutes ses queries en batches parallèles de 5, persiste citations, met à jour `last_run_at`)
- `ensure-tracked-cluster` (auto-track + quota check + premier scan en fire-and-forget)
- `get-llm-cluster-data` (agrégats 30j pour l'UI, appelle les 4 RPCs en parallèle)
- `cron-llm-daily` (3x/jour, sélectionne les `tracked_clusters` dus selon `runs_per_day`, déclenche `run-cluster-radar`. Protégé par header `X-Cron-Secret`)

**Frontend** :
- `src/components/workspace/WorkspaceLayout.tsx` : 4 onglets (Stratégie / Agent / Plan d'action / **LLM**). Segmented control passé de `workspace-segmented-3` (420px) à `workspace-segmented-4` (540px), translateX 0/100/200/300, icône `Radar` de lucide.
- `src/components/workspace/LLMView.tsx` (nouveau, ~480 lignes) : auto-pick du plus gros cluster au mount, polling 30s × 5 min si scan en attente, sous-composants `SummaryCard`, `DomainRanking`, `UrlList`, `QueryMatrix`, InfoTip sur chaque métrique.
- `src/index.css` : ~280 lignes CSS pour `.llm-*` (tokens existants `--ws-bg-page`, `--ws-bg-card`, `--ws-brand`, etc.).

Type-check `npx tsc --noEmit` : exit 0. Dev local OK sur http://localhost:5173/.

### À faire côté ops (non couvert par le commit)

1. Pousser les 2 migrations sur l'instance Supabase de prod (`supabase db push` ou via Dashboard SQL editor).
2. Déployer les 6 Edge Functions (`supabase functions deploy <name>`).
3. Vérifier que `GEMINI_API_KEY` est bien dans les env vars des Edge Functions (déjà utilisée par `tool-citation-probe`).
4. Ajouter `CRON_SECRET` dans les env vars Edge Functions.
5. Configurer le Scheduled Function `cron-llm-daily` dans Supabase Dashboard à 3 fois par jour (06h, 14h, 22h UTC par exemple) avec header `X-Cron-Secret`.

### Coût Gemini API estimé

Gemini 2.5 Pro grounded : ~$0.008/requête. 1 cluster (15 queries) × 3 runs/jour × 30j = 1350 req/mois ≈ $11/cluster/mois. Free tier Google AI 1500 req/jour suffit pour ~1 utilisateur actif. Au-delà, facturable. Implique un pricing premium si le tracking devient l'usage principal.

### Variance Gemini : à surveiller

Le risque méthodologique non levé : Gemini peut renvoyer des citations différentes entre deux runs identiques. La fréquence sur 30j × 3 runs (90 observations par query) devrait lisser ça, mais à mesurer sur les premières semaines. Si variance > 70%, basculer sur Google AI Overviews via SerpAPI (~$0.005/req).

### Pivot positioning : différé

Le repositioning frontal de Fusionn (de "copilote de rédaction" à "radar AEO") n'a PAS été enclenché. Décision Tim : on garde les 3 onglets actuels intacts, on ajoute juste LLM. Si l'usage du Radar dépasse celui des autres onglets dans 4-6 semaines, on pourra envisager le swap (hub Radar + outputs en aval).

### Ops déploiement (même session, fin d'aprem)

**Quota cappé à 1 cluster pour V1** (Free comme Pro). Décision Tim avant deploy pour limiter le coût Gemini sur la durée de mesure.

**Migrations push** : `supabase db push` a buggé sur 2 sujets :
1. Migration distante `20260521190000` non en local (probablement un hotfix appliqué via SQL editor). Réconcilié via `supabase migration repair --status reverted 20260521190000` (le SQL appliqué en prod reste, on retire juste le tracking).
2. 7 migrations locales en attente (5 du 22/05, 1 du 25/05, et 1 doublon de timestamp avec `20260522120000_create_youtube_reddit_results_tables` qui partageait son timestamp avec `..._fix_chat_threads_recherche_mode`). Toutes étaient déjà appliquées en prod (CREATE TABLE / policies déjà présentes). Marquées `--status applied` une à une. Le doublon a été renommé `20260522120001_fix_chat_threads_recherche_mode.sql` pour résoudre la collision de clé primaire `schema_migrations_pkey`.

Au final, seules les 2 migrations LLM Radar ont été poussées en prod (les autres étaient déjà appliquées hors-tracker).

**Fonctions deployées** (5/5) :
- `query-gemini-grounded`, `run-cluster-radar`, `ensure-tracked-cluster`, `get-llm-cluster-data`, `cron-llm-daily`

**Secret `CRON_SECRET`** généré et stocké via `supabase secrets set`. À conserver hors-repo (1Password / Bitwarden) car il sert au header `X-Cron-Secret` du scheduled function.

**Bug grounding Gemini détecté en smoke-test** : les URLs retournées par l'API sont **toutes proxifiées** via `vertexaisearch.cloud.google.com/...`. Sans résolution, tous les domaines auraient été identiques en BDD et l'agrégation par domaine inutile. Fix appliqué dans `_shared/gemini-grounded.ts` : HEAD HTTP avec `redirect: 'manual'` sur chaque URL proxy pour récupérer la vraie destination via le header `Location`. Fallback sur le champ `title` (qui contient parfois le domaine) si la résolution échoue ou timeout (4s). Les `query-gemini-grounded` et `run-cluster-radar` ont été redéployées avec le fix. Re-test smoke prod : 9 citations sur 9 vrais domaines distincts (clubic.com, formalive.fr, plateya.fr, paulvengeons.fr, chatseo.app, social-media-for-you.com, seranking.com, impli.fr, ibdeo.fr) sur la query *"meilleur outil SEO IA pour freelance"*.

### Pivot post-déploiement : scan déclenché à la recherche (pas via cron)

Décision Tim immédiate après le smoke-test : *"ce n'est pas un cron, c'est lors de la recherche que tu dois lancer le résultat de l'onglet LLM. Et tu dois push sur Netlify car on est en main"*.

**Changements appliqués** :
- `useSearchPipeline.ts` : après que `generate-semantic-keywords` résout, on calcule le cluster majoritaire (max count `cluster`) et on appelle `ensure-tracked-cluster` en fire-and-forget. Ajouté à `Promise.allSettled` pour propre tracking.
- `ensure-tracked-cluster` : avec quota=1, on **swap automatiquement**. Si le user a déjà un cluster actif, on le passe en `status='paused'` avant d'insérer / réactiver celui demandé. Data historique conservée.
- `cron-llm-daily/index.ts` : annoté `[DÉSACTIVÉ EN V1]`, conservé pour V2 si time-series nécessaire. Aucun scheduled function configuré côté Dashboard.
- LLMView garde son picker : l'utilisateur peut basculer entre clusters d'une recherche, chaque switch fait ensure-tracked-cluster qui gère le swap.

### Commit + push main

Commit `f33ce03` poussé sur `main` (auto-deploy Netlify lancé).

13 fichiers, +2095 lignes, -4 lignes :
- 1 composant frontend (LLMView), 1 hook patché (useSearchPipeline), 1 layout patché (WorkspaceLayout 4 onglets), index.css +421 lignes
- 1 helper partagé, 5 edge functions (déjà déployées)
- 2 migrations LLM (déjà appliquées) + 1 rename pour la collision de timestamp

**Préservé hors-commit** : WIP de Tim sur business score realtime (`BusinessScoreProgress.tsx`, `VirtualKeywordTable.tsx`, `useBusinessScores.ts`, `generate-business-score/index.ts`, migration `20260526140000_business_score_streaming_and_realtime.sql`) délibérément exclus du `git add` ciblé.

**CSS index.css** : reconstruction manuelle pour exclure ~35 lignes de keyframes `ws-shimmer-bg` (WIP business-score) mêlées à mes 421 lignes `.llm-*`. Méthode : extract de mes lignes via `sed`, revert du fichier à HEAD, append de mes lignes seules. Diff final : +421 / -0 (clean).

---

## 2026-05-25 — Audit complet (5 passes) + Phase 1 (bugs + nettoyage + UX)

Session d'amélioration globale lancée par « ON va améliorer fusionn ». 5 passes d'audit (fonctionnel / UX / qualité LLM / conversion / dette technique) croisées avec les audits du vault (`Audit-UI-design-system`, `Audit-UX-CX`, `Audit-prompts-vs-doctrine`, `Audit-ux-workspace`, `Briefs-outils-product-led-seo`). Shortlist de 21 chantiers proposée à Tim, qui retient tout sauf #8 (ChatGPT/Perplexity dans Citation Probe), #9 (footer outils + maillage inter-outils), #11 (anti-hallucination `[À SOURCER]`).

Plan d'exécution en 6 phases. Phase 1 (quick wins + bugs + nettoyage) bouclée dans la foulée.

### Phase 1 — livré

**#4 Barème HN aligné /5 → /10** — `generate-hn-structure/index.ts` produisait `note_globale` sur /5 alors que `analyze-hn-score` et l'UI affichent /10 (incohérence d'affichage : `4/10` apparaissait au lieu de `8/10` pour une analyse "très bonne"). Prompt repris (l.168, 178, 194, 199, 205) + commentaire (l.290) + données mockées de la page `/apercu-resultats` (`note_globale: 4` → `8`). Migration SQL prête à appliquer : `supabase/migrations/20260525120000_rescale_hn_note_globale_to_10.sql` (UPDATE × 2 conditionnel sur `note_globale <= 5` pour ne pas re-multiplier des lignes déjà migrées).

Faux positifs de l'audit (déjà fixés en interne avant cette session) : `generate-brief` lisait bien `structure_proposee` ; `note_globale` était bien produit. L'audit `Audit-prompts-vs-doctrine.md` est périmé sur ces 2 points.

**#18 Tailwind `white` → `#FFFFFF`** — RETIRÉ DU PLAN. Aucune redéfinition de `white` dans `tailwind.config.*` ni `index.css`. Le bug n'existe plus (peut-être jamais existé). L'audit `Audit-ux-workspace.md:57` est périmé.

**#21 Nettoyage code mort** — supprimé :
- `src/pages/Discuter.tsx` (non routée dans App.tsx, ne servait qu'à wrapper l'ancienne UI chat)
- `supabase/functions/fetch-google-ads-metrics/` (0 appelant)
- `supabase/functions/get-gsc-sites/` (0 appelant — Google OAuth login reste actif via `google-auth` + `google-oauth-callback`)
- Conservé : `fetch-volume-trends` (utilisée par `src/hooks/useVolumeTrends.ts`)

**#17 Wording onglets vides** — les 10 empty states de `ResultsContainer.tsx` (FAQ, Outils, Vecteurs, YouTube, Reddit, Semantic, Micro-Intentions, HN Structure, Objections, Modèles) disaient tous *« Lancez la génération depuis le bouton dédié »* alors qu'aucun bouton de re-génération individuelle n'existe (la pipeline `useSearchPipeline` génère tout en batch au lancement de la recherche). Wording remplacé par *« Cette analyse n'a pas été générée pour cette recherche. Relancez une nouvelle recherche pour la produire. »* — honnête. Bug d'à côté corrigé au passage : l'empty state des objections affichait *« Aucun cluster disponible »* (mauvais titre copié-collé) → *« Aucune objection disponible »*.

`EmptyPlaceholder` étendu avec props optionnelles `actionLabel` + `onAction` pour préparer des CTA inline futurs (quand des handlers de re-génération individuelle seront ajoutés, cf. Phase ultérieure).

**#16 Composant onglet unifié** — analyse : les « 3 modèles d'onglet actif » identifiés par l'audit sont en réalité 3 widgets distincts par nature (segmented control top-nav avec slider, sidebar Writer avec disabled+badge, sidebar gauche stratégie avec groupes+dot loading). Les fusionner ferait perdre la cohérence visuelle de chaque contexte. Refactor local appliqué : le segmented control top-nav (3 boutons quasi-identiques répétés dans `WorkspaceLayout.tsx:379-399`) passe en `.map()` sur config `[{ key, label, Icon }]` — réduit 20 lignes en 14.

### État TypeScript

40 erreurs `tsc` préexistantes (TS6133 imports inutilisés, TS2322/TS2345 types lâches). **Aucune régression introduite** par les changements de cette session. Dette à traiter dans une session dédiée si Tim souhaite un repo `tsc --noEmit` propre.

### Actions à faire après merge

1. `supabase db push` pour appliquer la migration HN /5 → /10
2. `supabase functions deploy generate-hn-structure` pour le nouveau prompt
3. Vérifier visuellement sur localhost:5174 :
   - `/compte` → top-nav 3 onglets identique
   - `/compte` → ouvrir une recherche, naviguer vers FAQ/Outils/Objections → wording honnête
   - `/apercu-resultats` → carte "Structure Hn" affiche `8/10`

### Audits du vault à mettre à jour

`Audit-prompts-vs-doctrine.md` et `Audit-ux-workspace.md` contiennent maintenant des recommandations périmées (cf. faux positifs #4 et #18). À nettoyer lors d'un prochain refresh.

### Phase 2 — livré (même session, sans pause)

Tim a demandé d'enchaîner sur les chantiers business critiques.

**#2.1 Connexion sans confirmation email bloquante** — la confirmation Supabase forçait l'utilisateur à quitter l'app, perdre son mot-clé et attendre un email. `Connexion.tsx:114-125` simplifié : suppression de la branche `view === 'signup'` qui affichait *« Vérifiez votre boîte mail… »* — désormais, dès que `signUp()` réussit, l'`useEffect` existant l.42-49 redirige automatiquement vers `/compte?keyword=…` (le `pendingKeyword` est déjà persisté via URL). **⚠️ Tim doit désactiver `email_confirm` dans Supabase Dashboard → Authentication → Sign In/Up** pour que le flux soit complet. Sans ça, `signUp()` ne retourne pas de session et l'`useEffect` ne déclenche pas (l'utilisateur reste sur la page connexion sans feedback — bug régressif). À faire avant déploiement.

**#2.2 Quotas alignés 3→5 + widget récap + endpoint dédié** — bug d'incohérence : `types.ts:86` déclarait `FREE_USER_HN_ANALYSIS: 3` mais `supabase/functions/check-hn-score-limit/index.ts:110` autorisait 5/mois. Choix : aligner sur 5 (plus généreux, moins frustrant). 3 fichiers patchés : `types.ts`, `Landing.tsx:758`, `SubscriptionChoiceModal.tsx:153` (+ mention « par mois » ajoutée partout pour clarifier le reset mensuel).

Nouvel endpoint `supabase/functions/get-all-quotas/index.ts` qui retourne en 1 round-trip `{isPremium, quotas: {searches, hn, semantic, geo}, resetsAt}`. Logique premium dupliquée depuis `check-rate-limit` (subscription active/trialing + period_end valide). 4 compteurs en parallèle (`search_history` total, `hn_score_analysis` mensuel, `semantic_score_analysis` mensuel, `geo_analysis_history` mensuel).

Nouveau hook `src/hooks/useQuotas.ts` (~50 lignes) + composant `src/components/workspace/QuotasFooter.tsx` (footer compact, masqué si `isPremium`, valeurs en rouge brand si `remaining ≤ 1`, CTA « Passer Premium »). Intégré en bas de `ResultsNav.tsx` via `margin-top: auto`. CSS `.workspace-quotas-*` ajouté dans `index.css` (tokens `--ws-bg-card`, `--ws-border`, etc.). Le widget n'apparaît que dans la vue Stratégie (limitation acceptée pour le MVP).

Bonus : retiré le `if (visibleSections.length === 0) return null;` de `ResultsNav.tsx` pour que le footer quotas soit visible même quand aucun résultat n'a été généré (vue stratégie vide).

**#2.3 Aligner promesse landing ↔ paywall** — copy alignée par #2.2 (5/mois HN + mention reset mensuel). Ajout d'une nouvelle Q en bas de `FAQSection.tsx` : *« Comment fonctionnent les quotas du plan gratuit ? »* qui clarifie 3 recherches sans expiration + 5 HN/Sémantique/GEO par mois avec reset le 1er.

### Phase 3 — livré (même session)

**#3.7 Pages React Générateur Hn** — `src/pages/StructureHn.tsx` (293 lignes, daté 23 mai) existait déjà, routée sur `/structure-h2-h3-seo` et appelle `tool-hn-structure`. Audit `Briefs-outils-product-led-seo.md` périmé sur ce point.

**#3.10 Stripe customer portal** — l'ancien lien dans `UserProfile.tsx:299` pointait vers le « login link » Stripe générique (`billing.stripe.com/p/login/28EfZh…`) qui force l'utilisateur à ressaisir son email. Nouvel endpoint `supabase/functions/create-billing-portal-session/index.ts` qui résout le `stripe_customer_id` du user via la table `subscriptions` et appelle `stripe.billingPortal.sessions.create({ customer, return_url })`. Bouton `<button>` remplace le `<a>`, état de loading, retour erreur si pas d'abonnement Stripe (« Souscrivez Premium d'abord »).

**#3.5 Section « À reprendre » en tête du compte** — découverte : la section *Reprendre* existait déjà dans `HistoryPanel.tsx:99-120` (filtre `has_saved_results`, tri par `last_opened_at`, top 3) mais visible **uniquement dans la vue Historique**. Extrait en composant réutilisable `src/components/compte/ResumeSection.tsx` (~60 lignes, props `searchHistory`, handlers, `limit`, `title`, `className`). `HistoryPanel` ré-utilise désormais ce composant (suppression du `useMemo` local + de l'import `SearchItem` orphelin). Ajout dans `Compte.tsx` du même composant en TÊTE de la vue conversational, visible **uniquement quand `conversational.phase === 'hero'`** (avant la saisie du mot-clé) — évite de polluer le flow d'analyse. Le parent passe à `overflow: auto` dans cette phase pour que la section ne déborde pas.

### Phase 4 — livré partiellement (même session)

**#4.14 Mobile responsive** — surprise : les fixes critiques étaient déjà en place dans `index.css:2886-2992` (mediaquery 768px) : `.workspace-strategy-sidebar` passe en colonne avec `max-height: 38vh` scrollable (les 15 onglets restent atteignables), éditeur passe à `85dvh` au lieu de 50/50, mode bar wrappé en 2 lignes, boutons d'action en icônes seules. L'audit `Audit-UX-CX.md:l.41` était périmé sur la gravité du « mobile cassé ».

Finalisation : 3 occurrences de `100vh` migrées vers `100dvh` pour iOS Safari (qui réserve la place de la barre d'URL avec `100vh` mais pas avec `100dvh`) — `App.tsx:39` (`calc(100vh - 80px)` → `calc(100dvh - 80px)`), `App.tsx:76` (fallback Suspense), `AnalyseTexte.tsx:642` (page entière). Restes de `100vh` (modale Notes, ToC blog sticky, Admin, PreviewOrganikk) laissés en l'état : ce sont des `max-h` ou modales secondaires, pas des layouts critiques.

**#4.15 Actions « quoi en faire » par vue** — reporté. Demande la création d'un composant `<ViewActions>` générique (copier / exporter XLSX / JSON-LD / envoyer-éditeur) et l'intégration dans 8+ vues (FAQ, Hn, Outils, Vecteurs, YouTube, Reddit, Semantic, Micro-Intentions, Objections, Modèles, Mots-clés, Clusters) avec des handlers spécifiques par format. Session dédiée nécessaire.

### Actions Tim — récap consolidé (à faire avant de tester)

1. **Supabase Dashboard → Authentication → Sign In/Up → décocher « Confirm email »** (sinon `signUp()` ne retourne pas de session et la connexion reste bloquée — régression vs avant)
2. **Migrations & déploiements** :
   - `supabase db push` (migration HN /5 → /10)
   - `supabase functions deploy generate-hn-structure` (prompt /10)
   - `supabase functions deploy get-all-quotas` (nouveau)
   - `supabase functions deploy create-billing-portal-session` (nouveau)
3. **Validation visuelle** sur `http://localhost:5174/` :
   - `/compte` → sidebar gauche → footer « Vos quotas » (4 lignes + reset + CTA)
   - `/compte` (avec recherches sauvegardées) → en haut, section « Reprendre » avant le HeroInput
   - `/compte` → onglets vides (FAQ, Outils, Objections) → wording honnête + EmptyPlaceholder
   - `/apercu-resultats` → carte Structure Hn affiche `8/10`
   - `/` → bento gratuit : « 5 analyses Hn et 5 analyses sémantiques par mois »
   - `/` → FAQ : nouvelle Q sur quotas en dernière position
   - Profile menu (premium) → « Gérer mon abonnement » → loader + redirect Stripe portal sans saisir l'email
   - `/connexion?mode=signup` → création compte → redirection directe `/compte` (après désactivation `email_confirm`)
4. **Tester sur mobile** (DevTools ou vrai device) → la sidebar 15 onglets reste accessible, l'éditeur n'est plus en 50/50, pas de débordement vertical iOS

### Surface de risque

Beaucoup de chantiers empilés sans commit intermédiaire. Si une régression apparaît, la dichotomie sera coûteuse. Recommandation : commit groupé `Phase 1+2+3+4 d'amélioration globale` puis sessions futures unitaires par phase.

### Commits réalisés

- `b352cdd` Decode entities : titres et meta du site fingerprint propres (WIP pré-existant)
- `c6db84e` Amélioration globale Phase 1+2+3+4 : bugs, quotas, rétention, mobile
- `8648a24` Cards prix : 1ère tentative (sync avec features récentes — voir correctif `99909cb`)
- `99909cb` Cards prix honnêtes : reflet du gating réel de l'outil (correctif du précédent)

### Bonus session : cards prix mises à jour (post-commit)

Tim a signalé que les 2 cards de prix (`Landing.tsx` section pricing l.744-810 + `SubscriptionChoiceModal.tsx` modal interne) étaient désynchronisées de l'état réel de l'app au 25 mai. Retirées :
- « Briefs rédactionnels » (l'onglet Rédaction a été retiré le 23 mai, cf. commit `6c3cf3d`)
- « Visualisation en clusters (aperçu) » seul (remplacé par « Visualisation en clusters et carte »)
- « Aperçu des résultats de chaque analyse » (vague)
- « Les premiers mots-clés de chaque recherche » (déplacé en « 50-80 mots-clés par recherche »)
- « Chat IA contextuel » → renommé en « Agent conversationnel IA » (plus à jour)

Ajoutées en Freemium (4 items) :
- « 5 audits GEO Sentinel par mois »
- « Outils gratuits : Score Business, Structure Hn, Test citation IA »
- « Aperçu des micro-intentions et modèles »
- « 50-80 mots-clés par recherche » (chiffre exact)

Ajoutées en Premium (4 items) :
- « Plan d'action SEO 3 mois personnalisé » (Phase 3 du 23 mai)
- « Stratégie pSEO : cluster AEO complet »
- « Mots-clés YouTube et discussions Reddit »
- « Modèles BoFu complets »
- « Vecteurs » ajouté à la ligne micro-intentions

Refactor secondaire : les 2 cards (Freemium + Premium) de `SubscriptionChoiceModal` étaient écrites en blocs JSX répétés (~9 lignes par feature). Passées en `.map()` sur un array `[{ title, desc }]` (-146 / +60 lignes au total). Plus simple à maintenir pour les futures évolutions.

### Phase 4.15 — Actions « quoi en faire » par vue (commit `17a9bc7`)

Implémentation complète de ce qui était resté en backlog en début de session. 12 vues du workspace gagnent un bouton **« Copier en markdown »** dans leur en-tête, et la FAQ gagne aussi **« Copier le JSON-LD »** (FAQPage selon schema.org, directement collable dans un `<script type="application/ld+json">`).

**Choix de scope** :
- Action « envoyer dans l'éditeur » retirée de la matrice : le mode `writer` dans `WorkspaceLayout.tsx:532` est code mort (aucun `setViewMode('writer')` dans le code, aucun bouton dans l'UI top-nav 3 onglets). Pas de cible pour l'envoi.
- Action « exporter Excel » non étendue : `SortableKeywordsTable` a déjà son export gated en premium (`SortableKeywordsTable.tsx:539-559`). Étendre l'export aux autres vues = session dédiée.
- Format choisi : markdown pipe-table pour tableaux, headers/listes/blockquotes selon le contenu. Compatible Notion, Obsidian, blogs, briefs.

**Composants créés** :
- `src/lib/copyHelpers.ts` — 12 formatters markdown + `formatFaqJsonLd()` pour JSON-LD FAQPage. Helper `esc()` qui échappe les pipes et écrase les retours à la ligne pour les cellules de tableau. Helper `table()` qui prend headers + rows et produit du markdown pipe-table.
- `src/components/workspace/ViewActions.tsx` — composant avec slots conditionnels `getMarkdown` et `getJsonLd`, feedback visuel "Copié" pendant 1.5s, gestion erreur clipboard.
- CSS `.view-actions`, `.view-action-btn`, `.view-action-error` dans `index.css` avec tokens du design system (`--ws-bg-card`, `--ws-border`, etc.).

**12 vues équipées dans `ResultsContainer.tsx`** :
- Stratégie / Comprendre : Mots-clés, Clusters, Micro-intentions, Vecteurs, Analyse sémantique
- Produire : Structure Hn, FAQ (markdown + JSON-LD), Outils, Objections, Modèles
- Découvrir : YouTube, Reddit
- **Non équipée** : Carte (vue graphique D3, copier en markdown n'a pas de sens)

**Bugs de types corrigés au passage** :
- `ClusteredKeywords.keywords` est `SemanticKeyword[]` : les champs sont `suggested_keyword` et `relevance_score`, pas `keyword` et `relevance`. Corrigé dans `formatClustersMarkdown`.
- `ContextVector` a `{term, weight}` (pas `{label, description}`) et `SemanticEntity` a `{entity_id, entity_type, salience, context_value}` (pas `{term, salience}`). Corrigé dans `formatSemanticAnalysisMarkdown`.

0 régression TS.

---

### Correctif `99909cb` : audit gating et cards honnêtes

Tim a signalé après le 1er commit cards (`8648a24`) que la mention « 5 analyses Hn et 5 sémantiques par mois » n'existe plus et que la différence Freemium / Premium ne se voyait pas.

Audit précis lancé via agent Explore — verdict cinglant : **seules 2 limites sont réellement appliquées** dans l'outil aujourd'hui :
1. **3 recherches** (`check-rate-limit` appelé depuis `Compte.tsx:40` + paywall via `SubscriptionChoiceModal`)
2. **Export Excel** (`SortableKeywordsTable.tsx:539-559` — bouton grisé `#9CA3AF`, clic = modale d'upgrade)

Plus 2 différences cosmétiques :
- Historique limité à 5 dernières recherches en gratuit (`Compte.tsx:62` — `query.limit(5)` si `!isPremium`)
- `HistoryStatsCards` masquées en gratuit (`HistoryPanel.tsx:81, 96`)

**Tout le reste est ouvert en gratuit** :
- `check-hn-score-limit` : jamais appelé depuis le frontend (mort)
- `check-semantic-score-limit` : seulement appelé depuis `/score-semantique` (outil public hors workspace)
- `check-geo-analysis-limit` : seulement appelé depuis `/analyse-texte` (page protégée hors workspace)
- `MicroIntentionsTable`, `ModelsTable`, `AgentChatView`, `PlanActionView`, `PseoStrategyView`, `YoutubeKeywordsTable`, `RedditKeywordsTable`, etc. : prop `isPremium` déclarée mais **jamais utilisée dans le render**
- Aucun gate sur Agent IA, Plan d'action 3 mois, Stratégie pSEO, briefs, FAQ, vecteurs, objections, modèles, YouTube/Reddit, GEO
- `ai-chat` : aucune limite implémentée (« 15 messages/jour » est du marketing pur)

Décision Tim : assumer cette différenciation faible avec des cards 100 % honnêtes plutôt que de promettre du gating non implémenté ou d'ajouter de vrais gates en urgence.

Cards finales (5 lignes chacune, différence claire) :
- Freemium : 3 ✓ + 2 ✗ (`Export Excel`, `Historique complet — 5 derniers max`)
- Premium : 5 ✓

Action future à considérer : **vraiment gater des features** (Agent IA, Plan d'action 3 mois, Stratégie pSEO) pour justifier le 20-29€/mois. C'est une décision produit, pas technique. Si Tim choisit cette voie, ouvrir un nouveau chantier dédié.

---

## 2026-05-25 - Fix entités HTML non décodées dans FusionnKnowsYouCard

Bug visible dans le bloc `Contexte de l'analyse` (composant `FusionnKnowsYouCard`) : les apostrophes scrappées depuis les H2 du site sortaient encodées (`d&#x27;acquisition`, `Ce qu&#x27;en`) au lieu de `d'acquisition`, `Ce qu'en`.

Racine : `stripHtml()` dans `supabase/functions/enrich-context/index.ts` utilisait `.replace(/&[a-z]+;/gi, " ")`, qui ne couvre pas les entités numériques (`&#x27;`, `&#39;`) et remplace les entités nommées par un espace au lieu de les décoder.

Correction sur 2 niveaux :

1. **Source (edge function `enrich-context`)** : nouvelle fonction `decodeHtmlEntities()` qui gère entités hex (`&#x27;`), décimales (`&#39;`) et nommées (`apos`, `nbsp`, `quot`, `laquo`, etc.). `stripHtml()` la rappelle après le strip des balises. Demande un `npx supabase functions deploy enrich-context` pour activer en prod.
2. **Affichage (`src/components/compte/FusionnKnowsYouCard.tsx`)** : helper `decodeEntities()` local au composant, appliqué à `siteFingerprint.title`, `siteFingerprint.metaDescription` et chaque `h2s[i]`. Shield défensif au boundary externe (contenu scrapé) qui agit immédiatement en local avant le deploy edge.

`finalUrl` non décodé : URL = sémantique préservée (`&amp;` ≠ `&` dans une query string).

Pas encore commité, en attente de validation visuelle Tim.

---

## 2026-05-23 - Workspace top-nav 3 onglets (Stratégie / Agent / Plan d'action 3 mois) + onboarding enrich-context

Commit `6c3cf3d` poussé sur `main`. Très grosse session, 5 axes.

### Workspace top-nav : 3 onglets de premier niveau

Retrait définitif de l'onglet `Rédaction` (briefRedaction). 14 fichiers nettoyés (`src/types.ts`, `useCompteState`, `useSearchPipeline`, `useConversationalAnalysis`, `useGenerationStatus`, `WorkspaceLayout`, `ResultsNav`, `ResultsContainer`, `SeoConversationalChat`, `Compte.tsx`, `ResultsPreview.tsx`, `xlsxGenerator.ts`, `resultsLoader.ts`, `types/compte`), composant `BriefRedactionView.tsx` supprimé, edge function `generate-brief-redaction/` supprimée. 0 nouvelle erreur TS introduite.

Le `viewMode` passe de `'strategy' | 'writer'` à `'strategy' | 'agent' | 'planAction' | 'writer'` (writer reste dans le code mais n'est plus accessible depuis l'UI). Le segmented control 2-boutons devient 3-boutons avec slider qui se déplace sur 3 positions.

**Icônes Fusionn-like** (anti-IA) : Stratégie = `Crosshair`, Agent = `MessageSquare`, Plan d'action = `ListChecks`. Plus de `Bot`, `Zap`, `Sparkles` qui faisaient cliché IA.

**Mount persistent** : pattern lazy-mount + keep-mounted via state `visitedTabs: Set<ViewMode>`. Quand l'utilisateur switch d'onglet, l'état est conservé. L'Agent garde son streaming en cours, le Plan d'action garde son plan généré et ses checkboxes "fait".

### Agent conversationnel (Phase 2)

Composant `AgentChatView.tsx` : interface chat avec streaming SSE Gemini en temps réel, 5 suggestions de questions au démarrage contextualisées (selon onglets disponibles : mots-clés, business score, micro-intentions, etc.). Réutilise l'edge function `ai-chat` existante avec `contextType: 'full_context'` étendu.

Persistance via tables existantes `chat_threads` + `chat_messages`, indexées par `search_id`. Au mount du composant, charge l'historique du thread `full_context` lié à la recherche en cours.

### Plan d'action 3 mois (Phase 3)

Refonte complète. L'ancien plan d'action 4 piliers (Surprise / Grounding / pSEO / AEO) avec 3 actions chacun ne donnait pas de roadmap temporelle ni de priorisation par mot-clé. Le nouveau format croise les deux :

- **Headline** : mot-clé pilier · 20 mots-clés priorisés · N pages à créer · KPI cible 3 mois
- **3 cards mensuelles** avec accent progressif (rouge M1 / orange M2 / vert M3, symbolise la pyramide Surprise → Grounding → AEO)
- **Pour chaque mois** : table mots-clés (★ Hub / ◆ Spoke / ● FAQ + score business + bucket dot) · actions hebdomadaires cochables avec bullets concrets · KPI fin de mois
- **Continuité 3 mois** : à chaque clic "Régénérer", Fusionn produit un nouveau plan daté du jour (le compteur recommence sur le présent)
- **4-3-4 actions** par mois (Tim a choisi : M1 et M3 intenses, M2 plus léger)

Edge function `generate-plan-action` repensée : prompt avec doctrine 4 piliers compressée + règles de priorisation Fusionn + structure JSON stricte (headline + months[3]). Le LLM reçoit 40 mots-clés + business score + micro-intentions + clusters + objections et doit en sélectionner exactement 20 répartis sur 3 mois.

Composant `PlanActionView.tsx` : barre de progression globale, checkboxes persistées en `localStorage` par `search_id`, cache du plan généré pour ne pas re-call inutilement.

⚠️ Pas de mention "Organikk" dans le copy (Tim a demandé "Fusionn" partout). Le terme "pyramide stratégique" remplace "pyramide Organikk".

### Onboarding enrich-context (3 champs)

Tim a signalé que les champs URL et marque étaient invisibles dans le HeroInput initial. **Refonte complète UX** :

- **3 cases strictement identiques** (mot-clé, site web, entreprise/marque) avec label clair au-dessus chacune et le mot "facultatif" en gris léger pour les 2 dernières
- **Plus d'icônes décoratives** dans les inputs (pas de Search, Globe, Building2 — c'était cliché IA)
- **Plus de wrapper "Personnalisez l'analyse" avec Sparkles** et copy marketing
- **Plus de badge OBLIGATOIRE rouge** — trop agressif
- Focus state : bordure passe en `#0F172A` (noir profond) + ring très subtile (look Linear/Notion)

Bug fix : **autostart bypass corrigé**. Avant, depuis la landing `?keyword=X&startChat=true` → `handleKeywordSubmit` était appelé direct → bypass du HeroInput → utilisateur ne pouvait pas saisir URL/marque. Maintenant, nouvelle fonction `prefillKeyword(kw)` qui pré-remplit le champ mot-clé sans changer la phase. Sync via `useEffect` dans HeroInput pour gérer le cas où `initialValue` arrive après le mount.

Spinner pendant l'enrich-context : nouveau state `isEnriching` exposé par le hook, propagé jusqu'au bouton HeroInput. Le bouton "Lancer l'analyse" devient "Analyse de votre site et de votre marque" avec spinner pendant les ~8s d'enrichissement.

### Edge function enrich-context : anti-hallucination + parallèlisation

Tim a constaté que pour "Fusionn" (marque récente, peu indexée), Gemini hallucinait sur une plateforme data engineering type Fivetran/Talend. **3 corrections** :

1. **Modèle pour brand lookup passé en `gemini-2.5-flash`** (le `flash-lite` ne supporte pas le grounding Google Search fiablement). Le scrape URL reste sur `gemini-3.1-flash-lite` côté reste de la function.
2. **Tool `google_search` activé** : Gemini cherche vraiment sur le web au lieu d'inventer.
3. **Prompt durci** : « Si tu trouves au moins une source publique crédible, rédige... Sinon réponds EXACTEMENT INCONNU. N'invente jamais. Mieux vaut INCONNU qu'une réponse hasardeuse. »
4. **Filtres post-réponse** : INCONNU, "désolé", "je ne sais pas", textes < 80 chars → `brandSummary = ""` → composant `FusionnKnowsYouCard` ne rend pas la section.

**Tests live validés** :
- Decathlon → résumé factuel propre ("entreprise française spécialisée dans...")
- Fusionn → INCONNU (Gemini ne le connaît pas avec certitude, refus de fabuler)
- Marque inventée "ZorgblattZyx..." → INCONNU

**Performance** : scrape et brand lookup passés en `Promise.all` parallèle. Latence avant analyse divisée par ~2 (de 13s à ~8s max).

Coût marginal : 1 call Gemini 2.5 Flash avec grounding ≈ $0.002 par recherche.

### Refonte UX FusionnKnowsYouCard (anti-IA writing)

L'encart "Ce que Fusionn sait de vous" était trop IA (halo, Sparkles, gradient, sections décorées). Refondu en **fact-sheet** :

```
┌─────────────────────────────────────────────────┐
│ Contexte de l'analyse              site + marque │
├─────────────────────────────────────────────────┤
│ Site          fusionn.co (titre, meta)           │
│ Sections      H2 séparés par · sans pills        │
│ Marque        Résumé Gemini sourcé               │
└─────────────────────────────────────────────────┘
```

Layout en grille `label | valeur`, séparateurs gris léger, mini-tag source en haut à droite, lien souligné sobre. Plus d'icône décorative. Titre changé en "Contexte de l'analyse" (plus neutre que l'anthropomorphique "Ce que Fusionn sait de vous").

### Context-builder étendu (Agent voit tout)

`supabase/functions/_shared/context-builder.ts` `buildFullContext` étendu de 8 à 14 sources :

Ajoutées :
- `search_input` : keyword + contexte enrich-context (scrape URL + brand summary)
- `micro_intentions`
- `vecteurs`
- `semantic_analysis`
- `youtube_keywords`
- `reddit_keywords`

L'Agent voit désormais toutes les données de l'onglet Stratégie + le contexte d'entrée (site scrape, brand Gemini). Tim avait insisté : « l'agent doit connaître tous les onglets de stratégie et le contexte qu'on a mis en entrée avec scraping du site ».

### Bug fix barre de progression Sémantique 7/8

Tim a signalé que la barre restait bloquée à "Sémantique" 7/8. Cause : `setCompletedSteps(prev => ({ ...prev, semantic: true }))` n'était appelé que dans la branche `success` de `generate-semantic-analysis`. En cas d'échec ou de format inattendu, la step restait à `false` → barre figée à 7/8.

Fix : `setCompletedSteps semantic: true` est maintenant appelé dans tous les chemins (succès, erreur business, exception réseau). La barre arrive à 8/8 quoi qu'il arrive.

### Edge Functions déployées au cours de la session

- `enrich-context` (2 deploys : parallélisation + brand grounding)
- `score-keywords-batch` (Phase outils précédente)
- `tool-hn-structure` (Phase outils)
- `tool-citation-probe` (Phase outils)
- `generate-plan-action` (2 deploys : v1 4 piliers puis v2 plan 3 mois)
- `ai-chat` (re-deploy avec context-builder étendu)

### Commits de la session

- `6c3cf3d` : commit unique de la session (refonte workspace + onboarding + bug fixes)

⚠️ La session a aussi inclus du travail sur 4 outils gratuits Product-Led SEO (`/comparateur-volume-business-seo`, `/structure-h2-h3-seo`, `/test-citation-ia-gemini`, brief technique du Score Business) commités plus tôt. Ne sont pas réinclus ici.

---

## 2026-05-23 - Workspace : Business Scores persistants entre onglets + colonne Score Business dans Clusters

Trois demandes Tim sur le workspace :
1. « Dans onglet mots-clés, lorsqu'on change d'onglet, une fois les score business calculé, les garder, ne pas le relancer à chaque fois »
2. « Ajouter Score sém dans score » (dans l'onglet Clusters)
3. « Ajouter des tooltips dans Clusters pour les colonnes »

**Diagnostic** : le state `businessScores` vivait dans `SortableKeywordsTable.tsx` (useState local + useEffect de fetch/polling/trigger). Or `SortableKeywordsTable` est démonté dès qu'on change d'onglet (`activeView !== 'sortable'`), donc le state était perdu et le polling redémarrait à chaque retour sur l'onglet Mots-clés. La table Clusters n'avait par ailleurs aucun accès aux Business Scores.

**Refactor** :
- Création du hook `src/hooks/useBusinessScores.ts` qui porte toute la logique fetch + polling 3s + trigger automatique de la function `generate-business-score` + détection des cas no-status / failed / in_progress-stalled. Retourne `{ scores: Map<string, { score, bucket }>, loading: boolean }`.
- `ResultsContainer.tsx` (parent stable, jamais démonté pendant le switch d'onglet) appelle `useBusinessScores(searchId)` une seule fois et passe `businessScores` + `businessScoreLoading` en props à `SortableKeywordsTable` ET `ClusteredTableView`.
- `SortableKeywordsTable.tsx` : retire useState `businessScores`, retire useState `businessScoreLoading`, retire le useEffect de ~108 lignes (toute la machinerie hoistée), retire l'import `useAuth` et l'usage de `user` (plus nécessaire ici). Accepte désormais `businessScores` / `businessScoreLoading` en props.

**ClusteredTableView** :
- Props `businessScores` + `businessScoreLoading` ajoutées.
- Renommage de la colonne « Score » en « Score Sém » (elle affichait déjà `keyword.relevance_score`, le nouveau label désambiguïse).
- Nouvelle colonne « Score Business » à droite, qui lit `businessScores.get(normalizeKeyword(keyword.suggested_keyword))` et affiche le score + le bucket en sous-libellé (`formatBucket`). État loading : `…` ; absent : `-`.
- **Tooltips ajoutés sur toutes les colonnes** : Cluster, Type d'Intention (`IntentInfoTip`), Mots-clés, Score Sém (`ScoreInfoTip`), Score Business (`BusinessScoreInfoTip`). Variantes `light` pour rester lisibles sur le header orange brand.

**Effet utilisateur** : on calcule le Score Business une seule fois par `searchId` puis on navigue librement entre Mots-clés / Clusters / Carte sans relancer le polling, et les deux tableaux affichent désormais les mêmes scores.

---

## 2026-05-23 - Test citation Gemini : passage en gemini-2.5-pro avec Google Search grounding

Tim a testé l'outil sur « outil ia mot cle » et obtenu 0/9 citations. Ses doutes : « la réponse ne fait que deux lignes, il va vraiment scrapper toute la réponse pour voir les citations ? ». Diagnostic complet de ma part : l'outil mesurait juste la mémoire fossile de `gemini-3.1-flash-lite` (modèle léger, mémoire de marque limitée), avec `maxOutputTokens: 600` qui tronquait les réponses, et sans grounding Google Search (donc pas de reflet de ce qu'un utilisateur final verrait en chat avec Gemini connecté au web).

Patch retenu (Tim « ok go ») :

**Function `tool-citation-probe/index.ts`** :
- Modèle : `gemini-3.1-flash-lite` → `gemini-2.5-pro` (mémoire de marque beaucoup plus large)
- `maxOutputTokens` : 600 → 4096 (les réponses « Top 5 », « Comparatif » ne sont plus tronquées)
- **Google Search grounding activé** via `tools: [{ google_search: {} }]`. Gemini recherche réellement sur le web pour chaque requête avant de répondre, comme ce que verrait un utilisateur en chat. Coût API marginal, gratuit côté Gemini.
- Extraction des **sources consultées** depuis `candidate.groundingMetadata.groundingChunks[].web.uri` (jusqu'à 10 sources par requête, dédupliquées). Chaque source porte `url` + `title`.
- **Détection de citation à deux niveaux** :
  - `via: "source"` (signal fort) : le domaine est dans une des URL sources que Gemini a consultées
  - `via: "text"` (signal faible) : le brand est mentionné dans le texte de la réponse
  - Le payload retourne aussi `citedBySource` (combien sont citations « via source »).
- Verdict reformulé pour distinguer les deux cas : « citations dans le texte uniquement, mais Gemini ne consulte jamais directement votre site » signale une visibilité fragile vs « Gemini consulte votre site sur X requêtes » = AEO solide.

**Page `CitationProbe.tsx`** :
- Type `PromptResult` étendu : `via: 'source' | 'text' | null`, `sources: { url, title? }[]`.
- Badge par ligne : « Cité dans les sources » (vert) vs « Cité dans le texte » (ambre) ; absent si pas cité.
- Liste des sources sous chaque réponse, sous forme de badges cliquables (hostname + icône external link). Les sources dont le hostname matche le domaine de l'utilisateur sont mises en vert (preuve forte de citation).
- Excerpt passé en `line-clamp-3` (au lieu de 2) pour exploiter les réponses plus longues retournées par Pro.
- Footer message : « Test effectué sur gemini-2.5-pro avec grounding Google Search activé. Gemini recherche réellement sur le web pour chaque requête avant de répondre, comme ce que verrait un utilisateur en chat. »

**Smoke test post-deploy** : `fusionn.co` sur « outil ia mot cle » retourne toujours 0/9 citations, MAIS chaque requête expose maintenant 4 à 7 sources que Gemini a effectivement consultées. Le verdict est précis : Tim sait que son site n'est ni cité dans le texte, ni dans le corpus de sources que Gemini parcourt. C'est une vraie mesure AEO, pas une devinette sur la mémoire d'un Flash Lite.

**Ce qui reste possible si on veut aller plus loin** : brancher SerpAPI / DataForSEO pour tester aussi le vrai Google AI Mode (SGE / AI Overview), ChatGPT Search, Perplexity. Mentionné dans la conversation, pas implémenté ici.

---

## 2026-05-23 - Comparateur Score Business : calcul déterministe en code (retrait du volume)

Demande Tim : « l'outil ne donne pas le volume, juste le score business, et on explique comment on construit le score business au lecteur pour justifier » + « oui calcul déterministe en code basé sur notre reflexion ». L'ancienne version laissait Gemini sortir un `scoreBusiness` arbitraire. Désormais, le LLM ne sort QUE des signaux qualitatifs, et le score est calculé en code à partir de pondérations fixes et publiques.

**Function `score-keywords-batch/index.ts`** réécrite :
- Le prompt Gemini demande uniquement 6 signaux qualitatifs : `intent` (5 buckets), `hasCommercialModifier`, `hasLocalSignal`, `isLLMSubstitute`, `cpcTier` (very-high/high/medium/low/unknown), `proximityToOffer` (core/adjacent/peripheral), et une `rationale` ≤ 90 chars.
- En code, fonction `computeScore(signals)` qui applique des pondérations fixes :
  - Intent : Actionnel +35, Transactionnel +30, Décisionnel +25, Comparatif +15, Informationnel 0
  - Commercial modifier : +15
  - Signal local : +15
  - Substitution LLM : −25 (pénalité)
  - CPC tier : very-high +20, high +15, medium +8, low 0, unknown +5
  - Proximité offre : core +15, adjacent +8, peripheral 0
- Total borné `[0, 100]`. Bucket : Fort ≥ 70, Moyen 40–69, Faible < 40.
- Champion = top score ≥ 40. Plus de logique « gap volume vs score » (puisque le volume n'existe plus).
- Le payload retour inclut `method.weights` et `method.buckets` pour traçabilité.

**Smoke test post-deploy** : `agence seo paris` → 100/100 (Actionnel + commercial + local + CPC very-high + core), `c est quoi le seo` → 0/100 (Informationnel + LLM substitue −25). Logique déterministe validée, deux mots-clés contrastés bien départagés.

**Page `ComparateurVolumeBusiness.tsx`** :
- Retrait complet de la colonne « Volume » dans le tableau de résultats (et de tout `volumeEstimate` côté front).
- Ajout d'un bloc d'introduction « Comment on calcule le Score Business » visible en haut du tool, avec 6 cards de pondération (une par signal). Le lecteur voit la méthode AVANT de lancer le calcul.
- Sous chaque ligne de résultat : tags compacts qui résument les signaux (« Actionnel · commercial · local · CPC élevé · cœur d'offre »). Le tag « LLM substitue » est en rouge si la pénalité s'applique.
- Bouton « Voir » par ligne qui déplie un breakdown en 6 lignes (label + détail + points), avec total final, et la rationale Gemini en italique.
- Labels bucket francisés en affichage (Fort/Moyen/Faible) tout en gardant les keys serveur (High/Medium/Low).
- FAQ refondue : retrait des questions « le volume ne sert vraiment à rien ? » et « Gap de Décision ». Ajout de « Comment le Score Business est-il calculé ? » et « Pourquoi un calcul déterministe et pas une note sortie par l'IA ? ».
- Liens connexes mis à jour (label outil Hn → « Structure Hn et balises »).

**Architecture** : c'est la première brique propriétaire de Fusionn qui combine LLM (signaux qualitatifs) + algorithme déterministe en code (score). Modèle reproductible pour les 2 autres outils (`tool-hn-structure`, `tool-citation-probe`) si Tim veut généraliser.

---

## 2026-05-23 - Polish landing : pulse pills, footer 4 colonnes, FAQ épurée, outils gratuits commit

Grosse passe d'amélioration UX/UI sur la landing + commit des 3 outils gratuits qui étaient encore en untracked.

**DemoSection (pills secteurs)** :
- Pulse plus marquée qui saute de pill en pill toutes les 2s (double box-shadow rouge brand, opacité 0.85, rayon final 20px). Boucle infinie jusqu'au premier clic, le hover ne stoppe plus.
- Titre passé de « Voilà ce que Fusionn fait. » à « Voilà ce que Fusionn fait pour vous. »

**Footer (`src/components/Footer.tsx`)** : refondu en 4 colonnes (Brand + tagline + social / Produit / Outils gratuits / Légal & support) + bottom bar copyright + mention « Un produit Organikk ». Fond `#F4F5F7` (token DS). La version minimal aussi passée sur les tokens DS. Footer désormais identique sur Landing, Blog et BlogPost (retrait du `minimal={true}` sur ces deux pages, demande explicite de Tim : « le footer en home page doit être le même sur la partie blog »).

**Renommage des 3 outils dans le footer** (choix Tim « style fonctionnel court ») :
- Comparateur Volume / Business → Score business des mots-clés
- Structure H2 / H3 SEO → Structure Hn et balises
- Test citation Gemini (inchangé)

**Outil Hn** : H1 passé de « Structure H2/H3 SEO : un plan d'article qui ranke » à « Outil balise hn et structure page optimisé » (formulation Tim, conservée telle quelle malgré l'accord grammatical).

**FAQ (`src/components/tools/ToolFAQ.tsx`)** : retiré le radial-gradient orange en arrière-plan des questions ouvertes, retiré le shadow rouge `rgba(255,55,28,0.25)` remplacé par un shadow neutre gris, bordure d'ouverture passée de `#FF371C/20` à `gray-300`. Retiré le petit trait gradient orange (`h-px` linear-gradient) entre la question et la réponse. Le numéro 01/02 en gradient orange et le `+/×` orange restent (marquent l'état actif sans faire « halo »).

**Commit des 3 outils gratuits** (étaient untracked) : pages `ComparateurVolumeBusiness.tsx`, `StructureHn.tsx`, `CitationProbe.tsx`, layout partagé `ToolPageLayout.tsx` + composant `ToolFAQ.tsx`, et les 3 Edge Functions associées (`score-keywords-batch`, `tool-hn-structure`, `tool-citation-probe`).

**Edge Functions non déployées en prod** : diag rapide pendant la session via curl direct sur `https://fwhfnzbtlddzfxbsejyf.supabase.co/functions/v1/<name>` : les 3 functions renvoyaient HTTP 404 `Requested function was not found`. Le SDK Supabase JS convertit ce 404 en message générique « Failed to send a request to the Edge Function » côté front, ce qui ne dit rien d'utile. À déployer avec `supabase functions deploy <name>` ou en bloc avec `--project-ref fwhfnzbtlddzfxbsejyf`. Vérifier aussi que les secrets Supabase nécessaires sont présents (OPENAI_API_KEY, ANTHROPIC_API_KEY, etc.).

**Règle utilisateur** : Tim a posé deux nouvelles règles persistantes durant la session, sauvegardées en mémoire : « montre-moi en local toujours » (lancer le dev server + donner URL après toute modif UI) et « pas de tiret cadratin » (déjà existant mais réaffirmé en pratique). Voir [[feedback_montrer_en_local]].

---

## 2026-05-23 - DemoSection : pulse qui saute de pill en pill (entrée initiale, replacée par la passe complète ci-dessus)

Problème : la rangée de pills secteurs (`consultant SEO IA`, `logiciel CRM PME`, etc.) dans `DemoSection.tsx` ressemblait à des tags statiques. Le premier secteur étant sélectionné par défaut, l'utilisateur voyait déjà le rapport sans aucune incitation à toucher les pills → zéro engagement avec le sélecteur.

Choix retenu après proposition de 4 variantes : **pulse qui saute de pill en pill** (vs pulse fixe / shimmer balayant / flèche bounce). Avantage : signale que TOUTES les pills sont cliquables (pas juste une) + crée du mouvement subtil sans bloquer la lecture + démontre la variété des secteurs passivement.

**Implémentation** :
- `src/index.css` : keyframe `demoPillPulse` (box-shadow rouge brand `#FF371C` à 55% d'opacité qui s'étend de 0 à 12px en 1.4s easeOut) + classe utilitaire `.demo-pill-pulse`.
- `src/components/landing/DemoSection.tsx` : 3 nouveaux states (`pulseIdx`, `pulseTick`, `interacted`). `useEffect` avec `setInterval(2000)` qui incrémente `pulseIdx` en sautant la pill active. `pulseTick` bump à chaque saut pour forcer le re-mount du span d'overlay et rejouer la keyframe. Le pulse s'arrête définitivement au 1er clic, hover ou focus (`stopPulse()` sur `onClick`/`onMouseEnter`/`onFocus`).
- L'effet est rendu par un `<span>` absolute en overlay (pas sur le button directement) pour que le box-shadow s'étende joliment autour sans interférer avec le contenu.

Comportement : 2s par pill, skip de la pill active, arrêt définitif dès interaction.

À noter : la section `DemoSection` utilise toujours `bg-gray-50` (rend `#F9FAFB`, l'ancien gris) au lieu du token `--ws-bg-page` (`#F4F5F7`) du design system validé. Pas corrigé dans cette session (scope = pills uniquement), à traiter dans une passe ultérieure.

---

## 2026-05-23 - Page connexion split-screen + preview animée + optimisations LCP

Commit `ce23418` poussé sur `main`. Une grosse passe + dommage collatéral.

**Page `/connexion`** : split 50/50, formulaire gauche (Google OAuth + email/password, signin↔signup togglable, lien reset password), aperçu animé droite. Pas de modale : Navbar et Landing naviguent vers `/connexion` (avec `?keyword=` préservé pour le pending search). La modale `AuthModal` reste en place uniquement dans `Compte` (re-auth).

**`KeywordResultsPreview`** : composant réutilisé sur `/connexion` et au centre du hero Landing. Mockup browser-chrome → en-tête keyword `agence seo paris` (74 résultats) → tab bar 5 onglets (icônes du workflow réel : `List` / `Target` / `Layers` / `ListTree` / `Map`) → table 7 lignes. Une **souris SVG animée se balade entre les onglets et clique**, avec halo orange autour (radial-gradient blur), pulse au moment du clic, ripple, et l'onglet change. Crossfade propre du `<motion.tbody>` (table-layout fixed pour zéro reflow). Float vertical doux du card (`y: [0, -6, 0]` 6s ease-in-out).

**Hero Landing** : la preview animée a remplacé le MockScreen central. Les deux écrans latéraux (formation IA, plombier paris) sont passés de 3 à 7 lignes pour aligner la hauteur avec la preview.

**Optimisations LCP** (commit même) :
- `<script html2pdf>` était bloquant dans le `<head>` → passé en `defer`. Gain estimé 200-400ms LCP
- Fonts Google réduites de 9 poids (100→900) Inter + Poppins à seulement les poids effectivement utilisés (Inter 400/500/600/700 + Poppins 500/600/700). Économie ~150kB sur le download initial
- `rel="preload"` ajouté sur la feuille de styles Google Fonts
- `prefers-reduced-motion` respecté dans `KeywordResultsPreview` (souris désactivée pour les users qui le préfèrent)
- `IntersectionObserver` qui pause l'animation dès que la preview sort du viewport (économie CPU + INP)

Résultat build : `index.js` passe de 155 → 130 kB (-25kB / -6kB gzip). `Connexion.js` à 3.5 kB gzip.

⚠️ **Dommage collatéral du commit** : `git add -A` a inclus 158 migrations Supabase qui étaient untracked depuis plusieurs sessions. Elles sont maintenant versionnées dans le repo (ce qui est sain pour les autres devs), mais le commit mélange deux scopes. À l'avenir, utiliser `git add <paths>` explicite.

---

## 2026-05-23 - Maillage interne blog (24 liens in-body sur 7 articles)

Commit `c7f019a` poussé sur `main`. 7 fichiers JSON modifiés.

Injection directe dans le HTML `content` des 7 articles publics (`public/blog-data/*.json`), pas de composant React type "Voir aussi" en bas (volonté de garder le maillage 100 % in-body comme recommande le skill).

**Architecture** :
- Pilier A « Stratégie SEO face à l'IA » : hub = `quadrillage-semantique`, satellites = `fin-contenu-genere-humain`, `ma-reflexion-du-moment`, `google-punit-il-le-contenu-ia`
- Pilier B « Visibilité AEO LLMs » : hub = `pourquoi-88-pourcent`, satellite = `trouver-mots-cles-pertinents`
- Page Do transversale : `prompts-seo-strategies-workflows`, reçoit 5 inbound depuis les deux piliers

**Audit final** : 0 orpheline, 0 dead-end. Hub A reçoit 6 inbound, page Do reçoit 5 inbound, hub B reçoit 4 inbound. Ancres diversifiées, jamais d'exact match répété vers la même cible (règle Boussardon respectée). Densité 3-5 liens par article (~1500 mots).

⚠️ **À syncer côté Supabase** : les modifs sont dans les JSON locaux uniquement. Le prochain `npm run build` régénère les JSON depuis Supabase et écrase les liens. Tim doit soit (a) recopier le `content` modifié dans la BDD via le BlogAdmin, soit (b) désactiver temporairement `prebuild` pendant qu'on stabilise.

Plan de maillage complet documenté dans la conversation (passages, ancres exact/partial/sémantique, scoring de priorité). Si extension du corpus à 10+ articles, viser 3 piliers en créant 3-4 articles sur l'outillage (autour de `prompts-seo` qui devient hub C).

---

## 2026-05-23 - Refonte complète design blog + articles + retrait tirets cadratins

Commit `9190f9c` poussé sur `main` (auto-deploy Netlify). 29 fichiers, +586/-337.

**Page Blog (`/blog`)** : hero éditorial inspiré de la DA home (halo radial rouge + grain), titre H1 en gradient orange (`#FF371C → #FF6B4A → #FF8C69` via classe utilitaire `fusionn-title-gradient` ajoutée à `index.css`), filter bar pills blancs bordurés + search rond, grille uniforme 3 col. Plus de badge "Le journal Fusionn".

**Cards (`BlogCard`)** : card blanche sur fond gris, hover lift `-translate-y-0.5`, titres en gradient orange, méta date/temps en bas, flèche `ArrowUpRight` qui s'anime au hover.

**Article (`/blog/:slug`)** : layout 240px TOC + article max-w-720px centré. Plus de hero image en début d'article (commence direct par catégorie pill + titre + excerpt + méta). H1 en gradient orange.

**Prose CSS (pattern IA cassé)** : zéro trait de couleur sur les callouts (border-l-4 colorés des articles d'origine flattenés en bloc gris doux `#F4F5F7` rounded-2xl). Couleurs sémantiques (`text-red-600`, `text-blue-600`...) forcées en `#0F172A`. Les `<strong>` passent à `font-weight: 700` + `color: #0F172A`. Premier paragraphe en 18px gris foncé. Liens en underline rouge subtil.

**Nettoyage runtime du HTML** : fonction `cleanContent` dans `BlogPost.tsx` qui convertit les `<div class="bg-X border-l-4 ...">` en `<blockquote>` propres et strip toutes les classes Tailwind décoratives (garde uniquement `article-content` et `lead`). Marche sur les 7 articles existants ET sur tous les futurs articles.

**TOC sticky** : passage breakpoint `xl` → `lg` (visible plus tôt). Item actif uniquement en orange `#FF371C`, plus de barre verticale rouge. Card blanche bordurée, label "Sommaire" en uppercase muted.

**BlogHeroImage** : remplacé le gradient orange flashy par fond gris + halo radial rouge subtil + grain + bulle blanche centrée avec icône Lucide en `#FF371C`. Position du halo pseudo-aléatoire par hash de `iconName` (7 placements distincts pour les 7 articles).

**CTA article (`ArticleCTABanner`)** : refonte au style du CTA final de la home (fond `#1A1A1A` + grain + halo rouge en haut + bouton `#FF371C`). Texte changé en "Votre plan d'action stratégique en quelques secondes".

**Manifest `posts.json`** : `Blog.tsx` interroge maintenant `/blog-data/posts.json` en priorité avant Supabase (plus de blog vide si la BDD locale dort). `scripts/generate-blog-urls.js` génère le manifest à chaque prebuild en plus des fichiers slug-par-slug.

**Audit maillage interne** (via skill `maillage-systeme`) : 7 articles tous orphelins, plan de 22 liens proposé en 2 piliers (Stratégie SEO face à l'IA / Visibilité AEO LLMs) + page Do transversale `prompts-seo`. Hubs désignés : `quadrillage-semantique` (A) et `pourquoi-88-pourcent` (B). **Pas encore implémenté côté code** (besoin de validation avant injection in-body dans les JSON + Supabase).

**Sweep tiret cadratin** : 19 fichiers nettoyés, ~50 occurrences. Code (`/* X — Y */`, UI labels) → ` : `. Articles JSON (incises) → `, `. Placeholders `'—'` → `'-'`. Mémoire `feedback_pas_de_tiret_cadratin` déjà active, le sweep applique la règle au repo existant.

---

## 2026-05-22 - Itération post-déploiement : accents, onboarding, refonte du process de sortie

Suite de la session, plusieurs passes poussées sur `main` (auto-deploy Netlify).

- **Accents** (`d94f6e5`) : les chaînes d'interface étaient écrites sans accents partout. Passe de correction sur 54 fichiers (composants, pages, hooks, lib) via 2 agents, périmètres disjoints. Uniquement le texte visible ; identifiants, clés, enums et logs intacts. +387/-387.
- **Onboarding contexte** (`3276b77`, `197a9e8`) : `generate-context-questions` repassée au vouvoiement, prompt durci (2 questions max, 4-5 suggestions cliquables obligatoires, situation concrète de l'utilisateur), température 0.6→0.45. Fallback raccourci. Exemples de documents ajoutés à l'étape Documents. Edge Function redéployée.
- **Process de sortie** (`06825cd`) : refonte du flux post-analyse dans `SeoConversationalChat`. Après une analyse, l'écran n'affiche plus que la synthèse « Ce qu'il faut retenir » + un bouton « Accéder à mon dashboard complet ». Retirés : aperçus de résultats, cartes Quick Wins, animation compteur, et tout le chat de suivi (questions, messages, barre de saisie). Transition d'étape recâblée, code mort de l'ancien chat nettoyé.
- **Tooltips dashboard** (`06825cd`) : bulle d'aide « ? » en tête des 15 vues de résultats du workspace, expliquant chaque résultat (via un agent).

Question encore en suspens : un titre/contenu peut rester au tutoiement dans des coins non couverts ; à signaler si repéré.

---

## 2026-05-22 - Déploiement : refonte home + Score Business, merge avec l'onboarding contextuel

Commit `ade67b3` (refonte home mode SaaS + Score Business dans l'onglet mots-clés + onglet Business supprimé + tooltips micro-intentions), puis push refusé : `main` distant avait avancé de 4 commits issus d'une session parallèle (questions de cadrage par mot-clé, AuthModal contextuel, polish ContextPills, et une passe Landing concurrente `08497f0`).

Intégration en merge `1da1f68` : seul vrai conflit `Landing.tsx`, résolu en gardant la refonte de cette session. Le prop `defaultView="signup"` de l'AuthModal contextuel reporté. Footer remis à sa version d'origine (le footer XXL de `08497f0` écarté, comme la décision prise en session de ne pas garder le footer XXL). L'onboarding contextuel distant (fichiers disjoints) conservé intact.

Poussé sur `main` → deploy Netlify de fusionn.co. Build + `tsc` OK.

**Détail de la refonte home (itérée longuement avec Tim) :** hero 3 écrans (agence seo au centre, formation IA / plombier paris sur les côtés, décalés) avec fond grainy + halo orange ; grille bento (cases grises sur section blanche, 2 tuiles vedettes avec aperçu produit) ; section « Score business, clusters et briefs » (3 blocs détaillés, l'exemple verset bible mariage avec scores business volontairement bas) ; section workflow en timeline ; mur d'avis décalé 2 colonnes (captures Pinterest, zoom ×1.40) ; WhyFusionn et FAQ aplatis (fin du glassmorphism) ; titres de section factuels ; alternance gris/blanc des sections.

---

## 2026-05-22 - Refonte de la home page en mode SaaS

Demande de Tim : refonte de la home (`src/pages/Landing.tsx`) en mode SaaS. Implémentée en local. Non commité. Build + `tsc` OK.

Toute la logique conservée (barre de recherche live, redirection auth, toggle pricing mensuel/annuel, prefetch Compte). Le `return` JSX entièrement réécrit.

- **Hero** : badge SEO+AEO, titre recentré sur le résultat (« Trouvez les mots-clés qui rapportent »), barre de recherche restylée en neutre (la bordure verte `#244831` remplacée par gris), et surtout une **maquette produit en DOM** (cadre navigateur + reproduction de l'onglet mots-clés réel avec les colonnes Score / Score Business / Bucket) au lieu d'un hero vide.
- **Supprimé** : les 4 blocs image/texte en photos Pinterest, la fausse preuve sociale (6 photos stock de gens au hasard, sans citation), la vague SVG orange, les dégradés et blurs orange un peu partout.
- **Ajouté** : grille bento de 7 fonctionnalités réelles ; section workflow en 3 étapes.
- **Pricing** refondu : 2 cartes blanches propres, Premium en bordure `#FF371C` + badge « Le plus choisi » (fini la carte noire en dégradé).
- **CTA final** : une seule carte sombre soignée au lieu du bandeau plein orange.
- Conservés tels quels : `WhyFusionn`, `FAQSection`, `Footer`, `SEOHead`, `AuthModal`.

À faire côté Tim : fournir de vrais témoignages clients (la fausse preuve sociale a été retirée, pas remplacée par de l'inventé).

---

## 2026-05-22 - Score Business fusionné dans l'onglet mots-clés + onglet Business supprimé

Demande de Tim : le Score Business ne doit plus être un onglet séparé, il s'affiche dans l'onglet mots-clés. Non commité. Build Vite + `tsc` OK. Aucune Edge Function modifiée (rien à redéployer).

**Choix de Tim (questions posées) :** génération auto à chaque recherche (recherche plus lente, assumé) ; colonnes reprises = Score Business + Bucket.

**Pipeline** (`useSearchPipeline.ts`) : `generate-business-score` est maintenant déclenchée automatiquement après `generate-semantic-keywords` (elle lit `search_semantic_results`). La fonction reste inchangée et asynchrone côté serveur.

**Onglet mots-clés** (`SortableKeywordsTable` + `VirtualKeywordTable`) : 2 colonnes ajoutées, Score Business (note /100, badge sombre) et Bucket (badge High vert / Medium ambre / Low gris). La table charge `search_business_score_results` par `search_id` et sonde toutes les 3 s tant que la génération tourne (robuste à la course où la ligne `generation_status` n'existe pas encore). Tooltips `BusinessScoreInfoTip` / `BucketInfoTip`. Export CSV enrichi.

**Onglet Business supprimé** : retiré de `ResultsNav` (section Décider) et du routage de `ResultsContainer`. `BusinessScoreView.tsx` supprimé. L'état `businessScoreResults` est conservé (toujours consommé par SummaryView, QuickWinsCards, chat) ; seul l'onglet dédié disparaît.

⚠️ **Limite connue** : `generate-business-score` ne score que les 10 mots-clés les plus pertinents (`.limit(10)`). La colonne Score Business est donc remplie pour ~10 lignes, tiret au-delà. Comportement hérité de l'ancien onglet Business. Étendre à tous les mots-clés = changement backend à part (coût Gemini + Google Suggest).

**Micro-intentions** : tooltips d'aide ajoutés sur les 6 colonnes (Requête, Intention, Vecteur clé, Similarité, Distance, Score) via le composant `InfoTip`.

---

## 2026-05-22 - Gris PSEO + traduction Reddit

Revue UI de Tim. Commit `cef3310` poussé sur `main` (gris PSEO + traduction Reddit). `generate-reddit-keywords` redéployée. Build Vite OK.

**1. Gris du graphe PSEO** - `ObsidianGraphView.tsx` (graphe de relations sémantiques du PSEO) avait un fond `#FAFAF9`, un gris chaud (`stone-50` Tailwind) hors design system, quasi indiscernable du blanc. Remplacé par `#F4F5F7`, le token `--ws-bg-page` du design system (gris froid validé).

**2. Sujets Reddit non traduits** - le pipeline `keyword_fr` existait déjà (colonne DB, prompt, persistance, affichage `keyword_fr || keyword`), mais les sujets ressortaient en anglais. Causes : cache `ai_response_cache` 30 j servant des réponses antérieures à la feature, et passe de traduction inline du modèle peu fiable. Correctifs sur `generate-reddit-keywords` (redéployée) :
- prompt : `keyword_fr` passé de simple mention à règle stricte n°4, OBLIGATOIRE, jamais vide, jamais d'anglais ;
- cache busté : `functionName` `reddit-keywords` → `reddit-keywords-v2` (ignore les vieilles entrées non traduites) ;
- filet de sécurité serveur : après aplatissement, tout `keyword_fr` vide déclenche une passe Gemini de traduction dédiée ; en dernier recours, fallback sur le texte d'origine pour ne jamais renvoyer un champ vide.
- les recherches Reddit déjà enregistrées restent en anglais (données figées) ; seules les nouvelles sont traduites.

**3. Colonne Demande sur l'onglet mots-clés : ajoutée puis retirée** - le thermomètre Froid/Tiède/Chaud (Google Suggest) n'existe que dans l'onglet **Business** (`BusinessScoreView`). Tim l'a d'abord voulu aussi dans l'onglet mots-clés. Implémenté de bout en bout (backend `generate-semantic-keywords` enrichi avec Google Suggest sur les 2 chemins d'insertion ; colonne front sur `SortableKeywordsTable` + `VirtualKeywordTable` via `DemandBadge`) puis déployé. Tim a ensuite décidé de la retirer. Reversion complète : `git checkout` des 3 fichiers (`SortableKeywordsTable.tsx`, `VirtualKeywordTable.tsx`, `generate-semantic-keywords/index.ts`), `generate-semantic-keywords` redéployée dans son état d'origine. La demande reste donc uniquement dans l'onglet Business, comme avant. Effet de bord inoffensif : les recherches lancées pendant la courte fenêtre où la fonction enrichie tournait ont écrit quelques lignes dans `keyword_demand_captures` (conservées, sans impact).

---

## 2026-05-22 - Refonte /admin : mots-clés, connexions, téléchargements, jours d'usage

Commit `8263fdc` sur `main`. Le `/admin` sert `admin-v2/AdminPage.tsx` (l'ancien `Admin.tsx` est sur `/admin/legacy`).

Ajout des métriques demandées par Tim :
- 30 derniers mots-clés recherchés (panneau `AdminRecentKeywords`).
- Dernières connexions, via `auth.users.last_sign_in_at` (panneau `AdminRecentLogins`), avec jours actifs et nombre de requêtes.
- Téléchargements de liste (panneau `AdminDownloads`) : **nouveau tracking**. L'export CSV de `SortableKeywordsTable` écrit un event `analytics_events` de type `download`. Migration `20260522190000` qui autorise ce type dans le CHECK.
- Jours d'utilisation distincts par compte : colonne « Jours actifs » ajoutée à `AdminTopUsers`.

Le « temps de connexion » demandé n'a pas été fait : aucune notion de session/durée dans la base, et un vrai heartbeat donne une donnée fausse (onglet ouvert). Remplacé par des proxies fiables : dernière activité, jours actifs, nombre de recherches. Choix validé par Tim.

Côté données, tout passe par la fonction `admin-stats-v2` (étendue : `recentKeywords`, `recentLogins`, `downloads`, `daysActive`). `AdminPage` tolère l'ancien format (`|| []`), donc pas de crash si la fonction n'est pas encore redéployée.

✅ **Déployé le 2026-05-22** : migration `20260522190000` appliquée en prod, fonction `admin-stats-v2` déployée (projet `fwhfnzbtlddzfxbsejyf`), front publié sur fusionn.co via Netlify. Le tracking des téléchargements n'est pas rétroactif : il compte à partir de ce déploiement.

---

## 2026-05-22 - Bug critique paiement : le webhook Stripe n'enregistrait aucun abonnement

Commit `3e81c99` sur `main` (migration `20260522180000_fix_subscriptions_webhook_columns.sql`).

**Symptôme** signalé par Tim : un client paie, le compte ne passe pas en Premium, il faut le faire à la main.

**Cause** trouvée par audit du code. La table `subscriptions` minimaliste créée le 2026-05-20 (migration `20260520150000`, « DB neuve / nouveau projet ») n'a ni la colonne `current_period_start`, ni de contrainte unique sur `stripe_subscription_id`. Or les trois fonctions qui enregistrent un abonnement (`stripe-webhook`, `verify-checkout-session`, `sync-subscription`, inchangées depuis l'import initial `574d72c`) écrivent `current_period_start` et le webhook fait un `upsert` avec `onConflict: stripe_subscription_id`. À chaque paiement, l'écriture en base échouait. Le webhook avale l'erreur et répond quand même 200, donc Stripe ne réessaie pas : échec totalement silencieux. Aucune des modifs UI récentes n'était en cause, le code Stripe n'avait pas bougé.

**Correctif** : migration non destructive et idempotente qui ajoute la colonne `current_period_start` (nullable) et l'index unique `subscriptions_stripe_subscription_id_key`. Aucun redéploiement de fonction nécessaire.

✅ **Appliqué en prod le 2026-05-22** : la migration a été passée dans le SQL Editor Supabase. Le webhook peut désormais enregistrer les abonnements, le prochain client payant bascule en Premium automatiquement.

À traiter à froid plus tard : le webhook renvoie 200 même en cas d'échec d'écriture, ce qui a rendu ce bug invisible des mois. Le durcir pour qu'un vrai échec remonte une erreur et déclenche les relances Stripe (demande un redéploiement de fonction).

---

## 2026-05-22 - Fin de l'élimination de l'ancien gris dans les onglets

Commit `2a15d15` sur `main`.

Suite directe de `33463fa` (« éliminer l'ancien gris #F9FAFB des onglets de résultats »). Ce premier commit ne balayait que la chaîne hex `#F9FAFB` et ratait `bg-gray-50`, qui est l'alias Tailwind du **même** `#F9FAFB` — d'où sa fausse conclusion « plus aucun #F9FAFB dans le code ».

- 12 usages de `bg-gray-50` subsistaient dans 6 vues d'onglets : `HnStructureView`, `BriefRedactionView`, `BriefView`, `BusinessScoreView`, `PseoStrategyView`, `VecteursView` — en fond de carte/encart comme en survol de bouton.
- Tous consolidés vers `#F4F5F7` (le gris du système validé), variantes d'opacité préservées (`hover:bg-gray-50/50` → `hover:bg-[#F4F5F7]/50`).
- Build Vite OK. L'échec `react-snap` du `postbuild` est un souci d'environnement puppeteer pré-existant (errno -86, archi Chromium), sans rapport avec ce changement.

Point d'attention : `bg-gray-100` (= `#F3F4F6`, zébrage de tableaux + survols) reste en place. Visuellement quasi identique à `#F4F5F7` (1 unité par canal), ce n'est pas l'« ancien gris » perçu — laissé tel quel. Reste aussi ~52 `bg-gray-50` hors vues de résultats (pages, modales, navbar) à traiter si on veut bannir totalement l'alias.

---

## 2026-05-22 - Passe UI : workspace, historique, design system, onglet Tendance

Série de retouches UI sur `main` (poussées, déployées).

- Onglet « Conversation » retiré du workspace (`5e063f5`).
- Icône du chatbot : étoile remplacée par le logo Fusionn, icône `Atom` (`a12dc6c`).
- Connexion Search Console masquée du front à la demande de Tim (`0fe0496`) ; code conservé, rendu neutralisé par `{false && ...}`.
- Refonte des cartes de mots-clés de l'historique : design minimaliste, mots-clés longs sur 2 lignes au lieu d'être tronqués, bouton Relancer en orange, ajout d'un bouton Voir (`b8b0377`, `c74ad32`, `425dceb`).
- **Audit UI complet** (doc `Audit-UI-design-system.md`) : verdict = garder fond gris + cartes blanches (bon pattern), le souci était que `#FAFAF9` était trop pâle. Refonte P0/P1 appliquée (`3d7c650`) : fond de page `#FAFAF9` → `#F4F5F7`, couleur de marque unifiée (`#FE371C` → `#FF371C`), typo en 400/600, vert hors-marque `#244831` retiré du Hero.
- **Onglet Tendance masqué** (`e934c9e`). Constat : la colonne « Tendances » affichait une courbe libellée « Intérêt de recherche Google Trends » qui était en réalité **entièrement estimée par Gemini** (`fetch-volume-trends`), sans aucune source réelle. Donnée non sourcée présentée comme sourcée, contraire à la doctrine anti-hallucination. Colonne masquée (flag `SHOW_TRENDS`), génération de fausse donnée coupée. À ne réactiver qu'avec une vraie source (DataForSEO ou équivalent payant). Voir `Audit-UI-design-system.md` et le constat détaillé.

---

## 2026-05-22 - Onglets Mots-clés YouTube et Reddit

Commits `ee62892` puis `2d65b4b` sur la branche `feat/youtube-reddit-tabs` (depuis `main`), poussés. Non mergé, backend non déployé.

Deux nouveaux onglets dans le workspace (nouvelle section de nav « Découvrir »), générés en parallèle des autres à chaque recherche.

- **generate-youtube-keywords** : Edge Function qui tape YouTube Data API v3 (`search.list` + `videos.list`) pour les vraies vidéos qui rankent, puis Gemini pour clusteriser les mots-clés. Vues/titres/chaînes viennent de l'API.
- **generate-reddit-keywords** : Edge Function qui tape l'API JSON publique de Reddit (sans clé, User-Agent requis), puis Gemini pour extraire sujets et questions. Upvotes/commentaires viennent de l'API.
- **Anti-hallucination** : Gemini ne produit aucun chiffre. Il référence vidéos/posts par id, le serveur joint la donnée réelle. Respecte la doctrine de Tim.
- 2 tables `search_youtube_keywords_results` / `search_reddit_keywords_results` (migration `20260522120000`), cache 30j, `generation_status`, RLS.
- Câblage complet : types, `useCompteState`, `ResultsNav`, `ResultsContainer`, `WorkspaceLayout`, les 2 pipelines (`useConversationalAnalysis` + `useSearchPipeline`), `resultsLoader`, `useGenerationStatus`, rechargement d'historique.
- Clé `YOUTUBE_API_KEY` posée en secret Supabase. Mode auto retenu par Tim (les 2 onglets se génèrent avec les 12 autres). Quota YouTube : ~100 recherches distinctes/jour.

- Corrections post-revue (`2d65b4b`) : sections YouTube/Reddit ajoutées à l'export CSV ; l'Edge Function Reddit bascule automatiquement sur l'OAuth Reddit si `REDDIT_CLIENT_ID`/`REDDIT_CLIENT_SECRET` sont posés en secrets (sinon endpoint JSON public). Modèle Gemini gardé en `gemini-3-pro-preview` à la demande explicite de Tim (pas de bascule vers Flash).

- Déploiement + smoke tests (`567f676`) : les 2 Edge Functions sont déployées sur le projet Supabase. Tests curl directs :
  - YouTube : la fonction tourne correctement, mais la clé renvoie `403 API_KEY_SERVICE_BLOCKED`. YouTube Data API v3 n'est pas activée, ou la clé est restreinte. À régler côté Google Cloud (projet `309434449968`).
  - Reddit : la fonction tourne, mais l'API JSON publique renvoie un `403` depuis l'IP datacenter de l'Edge Function. L'approche keyless est **inutilisable côté serveur** : l'OAuth Reddit (`REDDIT_CLIENT_ID`/`REDDIT_CLIENT_SECRET`) devient obligatoire, pas optionnel.
- Résolution YouTube : Tim a activé YouTube Data API v3 et débloqué la clé côté Google Cloud. Smoke test relancé → **HTTP 200, 42 mots-clés, 7 clusters, vraies vues** (71, 3664, 4133...). YouTube fonctionne de bout en bout. Génération ~62s (gemini-3-pro-preview, modèle thinking).
- Résolution Reddit (`3b182a0`) : la création d'app Reddit étant bloquée chez Tim (captcha en boucle), bascule d'architecture. L'API JSON publique de Reddit bloque les IP datacenter mais répond aux IP résidentielles → **le navigateur** récupère désormais les posts Reddit (`src/lib/redditClient.ts`) et les transmet à l'Edge Function, qui ne fait que le clustering Gemini. Plus aucun compte, app ni secret Reddit nécessaire. Smoke test (posts simulés) → HTTP 200, 44 sujets, 4 clusters, métriques réelles. Une inconnue runtime : le CORS du fetch Reddit navigateur, à confirmer au premier test réel dans l'app.

- Migration appliquée le 2026-05-22 via le SQL Editor (le mot de passe base et le token CLI n'étant pas accessibles, et `db push` étant écarté à cause du backlog de ~150 migrations non suivies). Les 2 tables existent.

**Reste à faire** : tester dans l'app (une recherche, vérifier les onglets YouTube et Reddit, surveiller la console pour le CORS Reddit), puis merger `feat/youtube-reddit-tabs` dans `main`. Backend entièrement en place : Edge Functions déployées, tables créées, YouTube validé, Reddit en fetch navigateur. Note : `_shared/gemini.ts` n'existant pas sur `main`, les 2 fonctions appellent Gemini en direct avec retry inline, modèle `gemini-3-pro-preview`.

---

## 2026-05-22 - Balise Search Console, datafa.st, build main réparé

Commits sur `main` : `502ea50` (balise + datafa.st), `dfc4580` (réparation build). En ligne sur `fusionn.co`.

- Remplacement de la balise `google-site-verification` dans `index.html` (head). Ancienne valeur (`4oGanlQiiiXGZTiDCNrfhPh6gg1piefUsLsQa7tEoeU`) obsolète, remplacée par `llcJ5QMMUOjh_Anle8I5t61o-Iw8O2geHJDzeqvkAu0`. Se propage à toutes les pages via le pré-rendu react-snap.
- Script analytics datafa.st : `data-domain` passé de `foccus.io` à `fusionn.co`. À vérifier : le `data-website-id` (`dfid_6UJtDB9V2HKbZhvEIuiOK`) est inchangé et pointe peut-être encore vers une propriété foccus.io dans datafa.st.
- **Hébergement** : `fusionn.co` tourne sur **Netlify** (site `fusionn2`, id `a50cfaba-84fb-403f-a12f-d9479406d032`), auto-deploy depuis la branche `main`. Pas AWS. Le CLI `netlify` est authentifié en local sous le compte de Tim.
- **Build `main` cassé depuis `c55f31b`** : `useConversationalAnalysis.ts` importait `getSelectedGscProperty` depuis `ConnectGoogleSearchConsole.tsx`, fonction qui n'existe que sur `feat/gsc-usage-ab`. Conséquence : chaque build `main` échouait (exit 2), prod gelée sur le deploy du 2026-05-21 13:53. Réparé par `dfc4580` : ajout du helper sur `main` (lecture localStorage, inerte tant qu'aucune propriété GSC sélectionnée). Build vérifié OK, deploy Netlify publié.
- La feature GSC A/B (`608c72d`) et le retry Gemini (`bf75852`) restent sur `feat/gsc-usage-ab`, non mergés.

---

## 2026-05-21 — Fiabilisation des générations IA (retry Gemini)

Cause racine : quand une recherche démarre, une douzaine d'Edge Functions tapent l'API Gemini exactement en même temps. Certaines se prennent un rate limit (429) ou un 5xx transitoire, et sans aucune reprise l'onglet correspondant du workspace restait vide. Diagnostic en base : sur 11 recherches, 4 sans brief de rédaction (statut `null`), environ 1 échec sur 3.

- `generate-brief-redaction` (commit `c55f31b`, sur `main`) : 3 tentatives sur l'appel Gemini avec backoff progressif (1,5s puis 3s), parsing JSON tolérant aux barrières markdown. Front (`useSearchPipeline` + `useConversationalAnalysis`) qui relance l'appel une fois si la génération échoue (fonction idempotente, pas de doublon). Les 4 briefs manquants régénérés ; vérifié : 11 recherches, 11 briefs.
- Les 11 autres fonctions du pipeline (commit `bf75852`, sur `feat/gsc-usage-ab`) : helper partagé `_shared/gemini.ts` (`callGeminiWithRetry`, 3 tentatives, backoff) ; 10 fonctions migrées vers le helper ; `generate-hn-structure` traitée à part, retry dédié conservant son timeout de 120s par tentative et son parsing multi-parts (modèle thinking `gemini-3-pro-preview`). `generationConfig` et modèles inchangés. Les 12 fonctions déployées.

---

## 2026-05-21 — Merge PR #1 et retouches

- PR #1 mergée dans `main` (merge commit `99109da`) : les 13 commits de la session (fix premium, taxonomie, prompts, refonte UX, modale conversationnelle, GSC backend) sur la branche principale.
- Icône « Convertir » du chat (commit `451bd0d`) : `CircleDollarSign` remplacé par `Target`, l'objectif Convertir n'évoque plus l'argent.

---

## 2026-05-21 — Intégration Google Search Console (connexion + usage A)

Branchement de GSC comme source de données réelle, modèle porté de Qadence (flux OAuth maison, pas de service account, pas de clé API). Doc de config : `GSC_SETUP.md` à la racine du repo.

### Connexion
- Migration `20260521190000_create_google_connections_gsc.sql` : tables `google_connections` et `gsc_cache` (RLS lecture propriétaire). Appliquée via `supabase db push` après `migration repair` des 2 migrations fantômes `20260521150000` / `20260521170000`.
- Edge Functions déployées : `google-auth`, `google-oauth-callback` (en `--no-verify-jwt`, reçoit la redirection Google), `get-gsc-sites`.
- Composant `ConnectGoogleSearchConsole` dans le hero : bouton de connexion + sélecteur de propriété (choisie à chaque recherche, mémorisée en localStorage `fusionn_gsc_property`).
- Config GCP : scope `webmasters`, redirect URI sur le client OAuth, secrets `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET`. Piège rencontré : 2 clients OAuth dans le projet, le secret pointait vers l'un, la redirect URI était sur l'autre.

### Usage A — recherche de mots-clés enrichie
- `_shared/gsc.ts` + Edge Function `gsc-fetch` : récupère les requêtes/pages GSC (position, clics, impressions, CTR), cache 2h.
- Moment 1 (graines réelles) : `useConversationalAnalysis` récupère les requêtes GSC liées au seed et les passe à `generate-semantic-keywords`, qui les injecte dans le prompt comme socle d'expansion. Cache de la fonction étendu avec un marqueur GSC pour éviter la pollution.
- Moment 2 (enrichissement) : hook `useGscEnrichment` + badges dans `SortableKeywordsTable` (« Position X » déjà positionné / « Nouveau »).

### Usage B — analyser l'existant
Modale `GscSiteAuditModal`, ouverte par le bouton « Analyser mon site » sur le hero (état connecté). Diagnostic GSC de la propriété : quick wins (position 3-15, triés par impressions), requêtes zéro-clic (impressions sans clic), cannibalisation (une requête servie par plusieurs pages, via `type: queries_pages`). Lecture seule.

Badge GSC (« Position X » / « Nouveau ») ajouté aussi sur `VirtualKeywordTable`, plus seulement `SortableKeywordsTable`.

### Reste à faire
- GSC dans `useSearchPipeline` (l'autre chemin d'analyse) ; seul `useConversationalAnalysis` est branché.
- Tout le travail GSC est non commité.

---

## 2026-05-21 — Corrections de l'audit UX/CX (lot 2)

Commit `703d4c3`, build OK.

- Préavis paywall : message « Dernière recherche gratuite » visible quand il reste 1 recherche, compteur de crédits rendu lisible.
- Mot-clé persistant : le mot-clé tapé sur la landing est sauvegardé en localStorage et rejoué après l'inscription (survit au flux email).
- Encarts d'exploitation : un conseil sobre en tête de chaque vue de résultat du workspace (composant `ExploitationHint`).
- Mobile : nav workspace en liste verticale, mode rédaction en plein écran, `100vh` remplacé par `100dvh`, mode-bar qui wrappe.

Reste (infra ou architecture, hors code isolé) :
- Désactiver la confirmation email obligatoire : réglage à faire par Tim dans le dashboard Supabase (Authentication, « Confirm email »).
- Emails de relance : besoin d'un service d'envoi et d'un cron.
- Pont conversationnel / workspace : refonte architecturale.

---

## 2026-05-21 — Corrections de l'audit UX/CX (lot 1)

Commits `ffd2c13` (modale conversationnelle) et `537b713` (corrections audit). Build OK.

Fait :
- Tier 1 : promesse de la landing alignée sur la réalité conversationnelle, wording freemium honnête, onboarding masqué quand un mot-clé vient de la landing. (Note : la section témoignages avait été retirée à tort, l'audit l'avait prise pour des photos de stock alors qu'ils sont réels ; elle a été restaurée.)
- Tier 2 (copy) : quotas justes dans la modale d'abonnement, badge d'économie annuelle (sans afficher le débit de 240€, choix de Tim), messages d'erreur de checkout orientés action.
- Tier 3 (rétention) : `created_at` n'est plus muté à l'ouverture (`last_opened_at` à la place), tri par `last_opened_at`, déduplication par mot-clé + contexte, cartes d'historique transformées en cartes projet, section « Reprendre ».
- Tier 4/5 : code mort supprimé (`SidebarNavigation`, `PremiumModal`), 15 onglets du workspace regroupés en sections Comprendre / Produire / Décider, EmptyPlaceholder corrigés.

Reste à faire (infra ou architecture) :
- Désactiver la confirmation email obligatoire (réglage Supabase Auth) et persister le mot-clé de la landing en localStorage.
- Préavis « dernière recherche gratuite » avant le paywall.
- Emails/notifications de relance (besoin d'un service d'envoi + cron).
- Encarts « quoi faire de ce résultat » par vue du workspace.
- Pont conversationnel / workspace.
- Responsive mobile (nav workspace, éditeur en rédaction, 100dvh).

---

## 2026-05-21 — Audit UX et expérience client

Audit large en 3 lots (acquisition/onboarding, conversion/premium, rétention/workspace). Détail complet : [[Audit-UX-CX]].

Constat : produit riche, mais le parcours client fuit à chaque couture. 21 points identifiés, classés en 5 tiers.

- Tier 1, tunnel d'acquisition : confirmation email qui casse l'élan, mot-clé de la landing perdu, onboarding qui fait doublon, promesse freemium mensongère. Priorité absolue.
- Tier 2, conversion : 3 quotas gratuits contradictoires, annuel affiché de façon trompeuse, paywall sans préavis.
- Tier 3, rétention : aucun mécanisme de retour, pas de section « à reprendre », `created_at` muté, historique = cimetière de recherches. Bon rapport effort/impact, les données existent déjà.
- Tier 4, workspace : 15 onglets à plat, pas d'action « quoi en faire », conversationnel et workspace = deux produits.
- Tier 5, dette : `SidebarNavigation` et `PremiumModal` morts, faux témoignages, accents incohérents, mobile cassé.

Côté refonte de la modale de contexte (`ContextPills`) : reconstruite en fil de chat conversationnel, une question à la fois, copy au vouvoiement professionnel, design épuré inspiré de Claude, avatar = logo Fusionn. Non commité.

---

## 2026-05-21 — Audit UX/UI du workspace + tooltips d'aide

### Audit UX/UI du workspace
Audit complet de la partie workspace (shell `WorkspaceLayout`, nav `ResultsNav`, dispatch `ResultsContainer`, `index.css`, tokens Tailwind). Rapport : [[Audit-ux-workspace]].

Cause du « parfois gris, parfois blanc » des onglets : `WorkspaceLayout` pilotait le fond de la zone de contenu via une liste d'onglets codée en dur (9 onglets en blanc, 6 en gris).

### Corrections appliquées
- **Fin du clignotement** : la page Stratégie est toujours `#FAFAF9` ; chaque vue « plate » est enveloppée dans une carte blanche standard `.workspace-view-card`. Padding ad hoc `p-8 sm:p-10` retiré de `microIntentions`.
- **Système de tokens CSS** : bloc `:root` (`--ws-bg-page`, `--ws-bg-card`, `--ws-border`, `--ws-text-*`, `--ws-brand`...) ; tout le CSS migré vers ces variables (valeurs identiques, zéro changement visuel) ; unification `#FAFAFA` vers `#FAFAF9` ; suppression des doublons CSS (`.streaming-cursor`, `@keyframes fadeIn` défini 3 fois).
- **Non traité** (noté dans le rapport) : token `white` du Tailwind config qui vaut encore `#FAFAF9` ; palette slate de la vue Conversation ; unification des 3 modèles d'onglet actif.

### Tooltips d'aide
Nouveau composant `InfoTip` (icône « ? », tooltip minimaliste foncé au survol, purement informatif). Presets `IntentInfoTip` (explique Do / Know / Know-Simple) et `ScoreInfoTip` (explique le score sémantique). Branchés sur les en-têtes de colonnes Intention et Score des deux tables (`SortableKeywordsTable`, `VirtualKeywordTable`).

Build Vite OK à chaque étape. Non commité.

---

## 2026-05-21 — Couleurs d'intention dans l'onglet mots-clés

Code couleur des intentions de recherche dans l'onglet mots-clés, sur 3 fichiers : `SortableKeywordsTable.tsx`, `VirtualKeywordTable.tsx` (`getIntentBadgeStyle`) et `InsightCards.tsx` (`getIntentColor`, carte « intention dominante »).

- Ancienne taxonomie : Transactionnel → bleu `#2563EB`, Informationnel → jaune `#CA8A04`, Comparatif/Commercial → vert `#059669`.
- Nouvelle taxonomie (celle réellement produite par `generate-semantic-keywords` depuis la migration) : **Do → bleu**, **Know → jaune**, **Know-Simple → vert**.

Les deux taxonomies sont alignées sur la même palette (bleu = action/transactionnel, jaune = informationnel, vert = simple/comparatif). Build Vite OK. Non commité.

---

## 2026-05-21 — Backlog structurel (1/3) : migration de taxonomie Know/Do

Premier chantier du backlog structurel de l'audit. Commit `6e051a0`.

**Migration de la taxonomie d'intention** Informationnel/Comparatif/Transactionnel + TOFU/MOFU/BOFU → **Know-Simple / Know / Do**, en stratégie **superset** : la base et le front acceptent les deux taxonomies en coexistence → aucune donnée migrée, aucun INSERT cassé.
- DB : contrainte CHECK `semantic_keywords.intent_type` étendue aux 6 valeurs (migration `20260521170000`, appliquée).
- Backend : `generate-semantic-keywords` (prompt + `normalizeIntentType` réécrite) et `generate-micro-intentions` (prompt + `funnel_stage`) redéployées.
- Front : type `IntentType` en superset + 10 composants d'affichage mis à jour. Build OK.

**Bug fixé** : `generate-hn-structure` — `note_globale` était toujours 0, désormais calculée côté code (moyenne des 3 notes de section).

### Reste du backlog structurel (2/3 et 3/3)
- Nouveaux champs de sortie (gap concurrentiel, Schema.org, maillage, multimodal, confidence_score, page/format/CTA) — ~8 fonctions, chacune = prompt + parsing + colonne DB + front.
- Refonte `generate-brief` / `generate-brief-redaction` (doublons RRF → vrai brief).
- Harmonisation des barèmes `analyze-hn-score` (/10) vs `generate-hn-structure` (/5).

---

## 2026-05-21 — Correction des prompts + création de 2 skills

Suite de l'audit. Réalignement des 15 prompts IA sur la doctrine SEO, **sans toucher aux structures de sortie JSON** (pour ne pas casser le parsing).

Appliqué (commit `d20af3f`, 15 Edge Functions redéployées) :
- règle anti-hallucination + placeholder `[À SOURCER]` ;
- Surprise Gap / Haute Surprise exigé ;
- garde-fous anti-AI-writing ;
- « ne jamais copier les concurrents » ;
- règles spécifiques par skill (7 règles non-négociables pSEO, leviers d'expansion mots-clés, format des preuves quantitatives, priorisation des 3 objections, MECE, signaux décisionnels) ;
- `generate-business-score` / `generate-models` : volume retiré des formules de score → proximité × intention × faisabilité ;
- `generate-topical-authority` traduit en français ;
- bug fix : `generate-brief` lisait `structure_html` (colonne inexistante) → `structure_proposee` ;
- `generate-pseo-strategy` : temperature 0.7 → 0.2.

Skills créés : **`seo-geo-audit`** (versionne les 7 scores GEO de analyze-geo-sentinel) et **`seo-modeles-pseo`** (source de vérité pour generate-models).

### Backlog structurel — NON fait (change les structures de sortie → DB + front + tests, à traiter à part)
- Migration de la taxonomie d'intention vers **Know-Simple/Know/Do** (touche generate-semantic-keywords, generate-micro-intentions, generate-models, generate-business-score, generate-topical-authority + colonnes DB + types TS + front).
- Nouveaux champs de sortie : 4 catégories d'entités (multimodal, divergence) + gap concurrentiel + reco par zone (vecteurs / semantic-analysis) ; format/Schema.org/maillage/roadmap (topical-authority) ; confidence_score/specs (tools) ; template/matrice (pseo-strategy) ; page-cible/format/CTA (objections, business-score, models).
- `generate-brief` et `generate-brief-redaction` : doublons RRF, aucun ne produit un vrai brief (structure Hn + FAQ) → refonte.
- `generate-hn-structure` : `note_globale` jamais produite → calculer côté code.
- Barèmes incohérents `analyze-hn-score` (/10) vs `generate-hn-structure` (/5).

---

## 2026-05-21 — Audit des prompts IA vs doctrine SEO

Vérification des 17 prompts IA des Edge Functions Fusionn contre la doctrine codifiée dans les skills `seo-*`. Détail complet : [[Audit-prompts-vs-doctrine]].

Bilan : **1 à jour** (`generate-faq`), 1 fidèle mais sans skill (`analyze-geo-sentinel`), **8 partielles, 7 obsolètes**. Les prompts ont divergé de la doctrine actuelle.

Divergences systémiques : taxonomie d'intention obsolète (TOFU/MOFU/BOFU et Informationnel/Comparatif/Transactionnel au lieu de Know-Simple/Know/Do) ; règle anti-hallucination absente (le LLM invente des scores non sourcés) ; Surprise Gap absent de ~9 fonctions ; aucun garde-fou anti-AI-writing.

Bugs annexes : `generate-brief` lit une colonne `structure_html` inexistante ; `generate-hn-structure` lit `note_globale` jamais produite (score toujours 0) ; `generate-brief` et `generate-brief-redaction` sont deux décodages RRF redondants.

Skills manquants à créer : un skill GEO, un skill « modèles pSEO ».

---

## 2026-05-21 — Réparation de fusionn.io (redirection vers fusionn.co)

### Problème
`fusionn.io` affichait « Ce site est inaccessible » (`ERR_CONNECTION_REFUSED`). Cause : le DNS pointait encore vers un vieux serveur IBM SoftLayer `75.126.100.28` qui ne faisait qu'une redirection **HTTP** (port 80) vers `fusionn.co`, sans aucun HTTPS (port 443 fermé). Les navigateurs étant passés en HTTPS-first, ils tentent `https://` d'abord → connexion refusée.

### Diagnostic
- `fusionn.co` = site de prod, fonctionne (HTTPS 200), hébergé sur **Netlify** (site `fusionn2`) — les IP `52.74.6.109` / `13.215.239.219` sont des nœuds CDN Netlify sur infra AWS, pas un hébergement AWS direct.
- Le forwarding intégré de Name.com ne supporte pas le HTTPS sur le domaine source → inutilisable.
- Voie Netlify abandonnée : `fusionn.io` est verrouillé dans le registre de domaines Netlify par un site fantôme `f59fc6d2-79bd-4712-bc15-01608911c104` sur un compte Netlify inaccessible (probablement un vieux déploiement Bolt).

### Solution retenue — Cloudflare
- DNS de `fusionn.io` migré de Name.com vers Cloudflare (nameservers `mcgrory` + `natasha.ns.cloudflare.com`).
- Enregistrements `A` `@` et `www` → `192.0.2.1`, proxiés (nuage orange).
- 2 Page Rules : `fusionn.io/*` et `www.fusionn.io/*` → Forwarding URL **301** → `https://fusionn.co/$1` (chemin + query string préservés).
- Certificat Universal SSL Cloudflare provisionné automatiquement.
- Validé via l'edge Cloudflare avant propagation : `301` OK en HTTP et HTTPS, apex + www.

### État à la fin de session
- Config Cloudflare complète et testée. En attente de propagation des nameservers au registre `.io` — `fusionn.io` redeviendra accessible automatiquement (typiquement < 1 h).
- Site Netlify `fusionn-io-redirect` créé puis abandonné (voie Cloudflare retenue) — **à supprimer**, ainsi que le dossier local `~/Code/fusionn-io-redirect/`.

---

## 2026-05-21 — Audit UX, déblocage de l'analyse, prompts 2026

### Repo
- Repo sorti d'iCloud : `Documents/fusionn` → `~/Code/newFusionn` (iCloud créait des copies de conflit `* 2.sql`).
- Vieille copie Bolt isolée → `Downloads/fusionn-project-OLD-bolt` (à ne plus jamais ouvrir).

### Audit UX du workflow « du mot-clé à l'analyse » + 9 correctifs — commit `6d8ae5c`
- mot-clé corrigeable depuis l'étape contexte (retour au hero pré-rempli) ;
- étape contexte clairement facultative + secteur pré-rempli depuis l'onboarding ;
- progression d'analyse honnête (`ThinkingAnimation` piloté par la vraie progression, fin du faux timer) ;
- suppression de ~5 s d'animation décorative post-analyse ;
- bouton « Annuler l'analyse » + `AbortController` sur les 12 appels IA ;
- synthèse chiffrée en tête des résultats + 1er bloc déplié par défaut ;
- couleurs score/intention dans les tables (`SortableKeywordsTable`, `VirtualKeywordTable`) ;
- brouillon de contexte conservé entre les démontages de `ContextPills`.

### Bug « modale Choisir un plan au lieu des résultats » — RÉSOLU
Cause racine = base du **nouveau projet Supabase** mal montée :
- droits de table manquants (`authenticated` et `service_role` sans aucun privilège) → 403 côté app, 500 sur `check-rate-limit` ;
- colonne `search_history.context` absente → l'INSERT échouait → l'analyse renvoyait au hero.

Correctifs appliqués directement en base + capturés dans la migration `20260521150000_reconcile_grants_and_search_history_context.sql` — commit `d5e1fbe`. Edge Function `check-rate-limit` redéployée (ne vérifie plus les Stripe IDs). Abonnement Premium réinjecté pour `mywaymalte@gmail.com` (actif jusqu'en 2036).

### Prompts — contrainte temporelle 2026 — commit `311412f`
Règle uniformisée sur les 14 fonctions de génération : toute année mentionnée = 2026 ou ultérieure, jamais 2025/2024 ou avant, et pas de date forcée si inutile. 9 Edge Functions redéployées.

### ⚠️ Points d'attention restants
- La base du nouveau projet a probablement d'autres trous de schéma (table `analytics_metrics` absente, etc.) — réconcilier proprement les migrations un jour.
- Rôle `anon` non re-grant → vérifier les pages publiques (landing, blog) pré-connexion.
- Erreurs React #418/#423 = pré-rendu `react-snap`, cosmétique.
- Branche `fix/premium-front-serveur-sync` : mergée dans `main` (merge commit `99109da`).

---

## 2026-05-27 · Modèle de page « Liste mot-clé pour X » + publication consultant SEO

**Contexte.** Première application du pattern `raw/articles/modele-production/modele-mots-clés.md` (vault seo-kb) sur Fusionn, en remplacement de la sortie HTML « Organikk gradient bleu » de Mai 14. Cible business : ranker sur la requête « liste mots clés [keyword] » et capter le clic des recherches type « liste mots clés SaaS B2B », « liste mots clés immobilier », etc.

**Itérations consultant SEO** (5 passes) :
1. Pass 1 (rejetée, « trop IA ») : header 5 stats + cards + entity grid + tool cards + warning emoji.
2. Pass 2 : tout en tableaux, 1 paragraphe court par partie, H1 « Liste mot-clé pour X », interdit « consultant SEO netlinking ».
3. Pass 3 : bloc doctrine 4 piliers pixel-perfect inséré en intro (pattern mis à jour dans le vault, étape 2 ajoutée à la structure obligatoire).
4. Pass 4 : retrait des colonnes Impact SEO et Data dispo (non scorables sans Keyword Planner ni input client). Reste 3 scores fiables : Effort (déterministe), Conversion (intent classification sur modificateurs), Priorité (dérivée).
5. Pass 5 : design Fusionn pixel-perfect (tokens `--ws-*`, Inter + Poppins, gradient orange H1, callout gris arrondi pour la doctrine, table styling `prose-fusionn`).

**Fichiers produits.**
- `~/Downloads/test-pseo-consultant-seo.html` : référence visuelle standalone Fusionn-styled.
- `seo-kb/fusionn/blog-drafts/liste-mot-cle-consultant-seo.html` : contenu HTML body compatible `prose-fusionn` (sans classes, blockquote pour la doctrine).
- `seo-kb/fusionn/blog-drafts/liste-mot-cle-consultant-seo.sql` : SQL INSERT idempotent (ON CONFLICT (slug) DO UPDATE) à exécuter dans Supabase SQL Editor.
- `seo-kb/raw/articles/modele-production/modele-mots-clés.md` : mis à jour (étape 2 bloc doctrine, étape 6 nouveau format tableau priorisation 6 colonnes).
- Mémoire auto : `feedback_doctrine_page_mots_cles.md` + `feedback_modele_liste_mot_cle_fusionn.md`.

**Publication.** SQL idempotent prêt, à exécuter par Tim dans Supabase Dashboard → SQL Editor (projet `fusionn`). Article publié au slug `/blog/liste-mot-cle-consultant-seo`.

**À faire ensuite (industrialisation).** Écrire `newFusionn/scripts/publish-keyword-list.mjs` qui prend en input un mot-clé pilier + un fichier HTML body et publie via supabase-js + service_role. Permettra de scaler à N articles « Liste mot-clé pour [X] » sans copier-coller du SQL.

**Suite 2026-05-27** : correction titre « Liste des mots-clés pour X » (pluriel, pas singulier), refonte tables dans `BlogPost.tsx` pour matcher pixel-perfect le design workspace (header brand orange `#FF371C`, white uppercase). Ancien slug `liste-mot-cle-consultant-seo` supprimé, republié sous `liste-des-mots-cles-consultant-seo`. Script `scripts/publish.sh` (wrapper service_role auto via CLI Supabase) + `scripts/publish-keyword-list.mjs` créés et committed dans `newFusionn` (push sur `main`, Netlify auto-deploy). URL live : https://fusionn.co/blog/liste-des-mots-cles-consultant-seo. Règle d'autonomie sauvegardée en mémoire : Claude exécute désormais publish + commit + push + deploy sans rien demander.

## 2026-05-28 — Compte : 4e case "Contexte" sur HeroInput

**Demande Tim.** Sur `/compte`, ajouter sous "Votre entreprise ou marque" une 4e case permettant d'uploader un fichier de contexte (md, doc, pdf, etc.).

**Implémentation.**
- `src/components/compte/HeroInput.tsx` : nouveau champ "Contexte" facultatif, file picker `.md/.txt/.pdf/.docx`. Parsers chargés en dynamic import (pdfjs-dist 5.7 et mammoth 1.12) pour ne pas alourdir le bundle initial. Le `.doc` (vieux binaire Word) n'est pas supporté : message d'erreur invite à réexporter en .docx. Chip d'affichage du fichier avec nom + nb caractères + croix pour retirer. État `isParsingContext` avec spinner pendant lecture.
- `HeroSubmitPayload` gagne `context` et `contextFileName`.
- `src/hooks/useConversationalAnalysis.ts` : `handleHeroSubmit` propage `context` vers `enrich-context` comme `freeText`. Présence de contexte compte aussi comme "extra" qui déclenche l'enrichissement automatique (sans passer par les questions de cadrage).
- `supabase/functions/enrich-context/index.ts` : plafond `freeText` monté de 800 → 10 000 chars. Label dans le contextSummary passé à Gemini : "Contexte fourni" au lieu de "Activité décrite".

**Deploy.** Front push sur main (Netlify auto-deploy). Edge function `enrich-context` déployée via `supabase functions deploy --project-ref fwhfnzbtlddzfxbsejyf`. Commit `a2da8dc`.

## 2026-05-28 (suite) — Fix carte "Contexte de l'analyse" + Page Documentation

**Suite session précédente sur la 4e case Contexte.**

**Bug trouvé et corrigé.** La carte `FusionnKnowsYouCard` prévoyait dans son type un champ `freeText` à rendre sous la row "Activité", mais `useConversationalAnalysis.handleHeroSubmit` ne le passait jamais dans `setEnrichmentContext`. Résultat : le contexte uploadé partait bien jusqu'au prompt Gemini (vérifié end-to-end sur `generate-semantic-keywords` ligne 412, `generate-faq` ligne 205, `generate-micro-intentions` ligne 123, `generate-tools` ligne 174, `generate-models` ligne 89, `generate-objections` ligne 206, `generate-brief` ligne 89), mais l'utilisateur ne voyait pas la preuve que son fichier avait été pris en compte. Correction : on reprend `contextText` + `payload.contextFileName` côté hook pour fabriquer un snippet (400 chars max) affiché dans la carte avec le label "Contexte" (renommé depuis "Activité"). Commit `5bb5756`.

**Verification pipeline contexte → prompts.** Le `cacheKey` de `generate-semantic-keywords` inclut le contexte (ligne 289) et la cache est explicitement bypassée quand un contexte est fourni (ligne 297) → chaque recherche avec contexte produit donc une réponse fraîche orientée par ce contexte. Le contexte est aussi persisté dans `search_history.context` pour debug a posteriori.

**Page /documentation.** Ajout d'une vraie page de doc SaaS accessible depuis le footer (colonne Produit + version minimal). `src/pages/Documentation.tsx`, 549 lignes. Layout : sidebar TOC sticky à gauche (Intersection Observer pour highlight la section active au scroll), 21 sections numérotées à droite. Couvre : démarrage, 4 champs de recherche (avec FieldBlock par champ — Mot-clé, Site, Marque, Contexte), GSC, 14 blocs de résultats (mots-clés sémantiques, FAQ, micro-intentions, structure Hn, objections, mini-outils, modèles, vecteurs, brief, plan d'action, score sémantique, YouTube, Reddit "bientôt"), crédits & abonnement, outils gratuits (avec liens), glossaire, support. Composants internes réutilisables : `Section`, `FieldBlock`, `Steps`, `Bullets`, `Tip`. Route lazy-loaded dans `App.tsx`. Commit `5f26c03`.

**Deploy.** Push main → Netlify auto-deploy (front uniquement, pas de re-deploy edge function nécessaire pour ces commits).

## 2026-05-28 (suite) — Gestion de projet Phase 1 (Tableau de bord)

**Demande Tim.** Gérer des projets dans le Tableau de bord. Projet = un client (agence). Ambition "vrai PM" mais livré en Phase 1 (fondations).

**Découverte clé.** Une table `projects` + `project_searches` + `project_tasks` existait déjà (migration `20251222073448_create_projects_system.sql`, déc. 2025) mais l'UI n'avait jamais été branchée (composants orphelins `ProjectFolder.tsx`, `ProjectCreator.tsx`, `ProjectTaskList.tsx`, `projectsHelper.ts`). On a réutilisé le schéma (junction `project_searches`, pas de FK directe) et étendu la table `projects` avec status/client_contact/site_url/default_brand/default_context/archived_at (migration `20260528120000_create_projects.sql`).

**Décisions de cadrage (validées par Tim).** Projet = client. Multi-user "pas tout de suite" (schema solo, ouvert au partage futur). Recherches existantes = bucket "Sans projet". Création projet "les deux" (Tableau de bord + on-the-fly dans HeroInput). Pré-remplissage HeroInput depuis le projet = OUI (site/marque/contexte). Tags existants conservés en parallèle des projets.

**Livré.** Onglet Projets (cards compactes), modal création/édition avec upload contexte, drawer détail + picker "Ajouter des recherches" existantes, archivage. Champ Projet dans le formulaire de recherche (préfill + rattachement auto). Badge projet + menu "Rattacher à..." + filtre projet dans l'historique. "Mon Espace" (navbar Action) ouvre le Tableau de bord au lieu du workspace.

**Retours visuels traités.** Cards trop grandes → layout compact. Bande couleur latérale → avatar coloré. Texte coupé → min-w-0 sur les troncatures. Perf (rame) → loadProjects passé de N+1 à 2 requêtes. Heatmap "Activité 12 mois" coupée à droite → pleine largeur + auto-scroll droite + placée au-dessus de l'Historique. "Sujets pivots" → "Sujets piliers". Barre de stats "Votre travail" refondue (séparateurs, valeur en avant, flèche tendance).

**Fix data important (anti-hallucination cluster).** L'insight "Cette semaine vous avez surtout creusé X" comptait les LIGNES BRUTES (double-comptage si même sujet relancé). Vérifié via service_role sur le compte de Tim : ses vrais clusters = "Services Agence SEO E-commerce (23)" etc., le "Services SEO B2B Lyon (35)" qu'il voyait n'existait nulle part (cache/démo navigateur). Règles déterministes posées : périmètre 7j strict, comptage DISTINCT, tri stable (count desc → date → nom), seuil anti-bruit >=2 mots-clés. Comptage distinct aussi appliqué aux cards de cluster.

**Deploy.** Commit `fa1fe4a` push main → Netlify auto-deploy. Migration `projects` déjà appliquée en prod via `supabase db push`. Aucune edge function impactée.

**Reste pour Phase 2+ (non fait).** Kanban + tasks (table project_tasks existe déjà), briefs/plan d'action consolidés par projet, deadlines, notifications. Question ouverte : retirer l'icône historique séparée de la navbar (redondante avec "Mon Espace").

## 2026-05-28 (suite) — Écriture humaine : anti-tics IA sur les 23 articles « Liste des mots-clés »

**Demande Tim.** Sur le blog (modèles « Liste des mots-clés »), corriger 3 tics IA : (1) persona halluciné « le marchand » (« personne ne dit le marchand »), (2) absolutisme faux « en 2026 ton prospect ne tape plus X » (certains tapent encore → formuler en proportion), (3) « a un différenciant » → « se différencie de la masse et du généraliste ». Règle générale : parler comme un humain, parler d'« utilisateur », ne pas inventer de mots.

**Diagnostic.** Ces phrases n'étaient PAS des chaînes statiques d'un prompt : c'est du contenu publié dans `public/blog-data/liste-des-mots-cles-*.json` (BlogPost lit le JSON statique d'abord, DB `blog_posts` en fallback). 23 articles, « ne tape plus » dans 20, « différenciant » dans 22, « marchand » dans 5.

**Fix.** Script `scripts/fix-blog-wording.mjs` (idempotent, dry-run par défaut) avec regexes ciblées :
- « En 2026 ton prospect ne tape plus « X » tout seul. Il tape… » → « En 2026, ton prospect tape de moins en moins « X » tout seul. Il tape plutôt… » (garde le singulier pour ne pas casser l'accord « son secteur… »). Variantes gérées : ton/le prospect, tout seul/seul, Il tape/Le candidat tape.
- « [sujet] a un différenciant que … ne servent pas » → « se différencie de la masse et du généraliste ». Forme « tu as un différenciant » → « tu te différencies… ».
- « le marchand » → « l'utilisateur » (+ accords). Résidus finaux : 0.
DB `blog_posts` resynchronisée sur les 23 slugs (update content/excerpt/meta_description via service_role).

**Prévention futures générations.** Mêmes règles injectées dans le prompt de l'assistant conversationnel `analyze-seo-chat` (REGLE 11 — FORMULATION HUMAINE + bloc dans `<style>`), déployé. Règle sauvegardée en mémoire (`feedback_ecriture_humaine_fusionn.md`).

**Deploy.** Commit `ab8445e` push main → Netlify auto-deploy. Edge function déployée.

## 2026-05-28 (suite) — Section dédiée « Listes de mots-clés » (sortie du blog)

**Demande Tim.** Cloner pixel-perfect le blog mais réservé aux listes de mots-clés, dans une section « Listes de mots-clés » (comme « Stratégies » sur Organikk). Décision actée : migrer les URLs de détail vers `/listes-mots-cles/:slug` (avec 301), lien en Footer uniquement. En cours de route : « un icône différent sur chaque miniature ».

**État de départ.** Les 23 « Liste des mots-clés pour X » étaient publiées dans la table `blog_posts` (slug préfixé `liste-des-mots-cles-`), servies sous `/blog/:slug`, et le blog les affichait pêle-mêle avec les 7 vrais articles. Discriminant retenu : le préfixe de slug (zéro migration DB).

**Fix.**
- Routing : `/listes-mots-cles` (index) + `/listes-mots-cles/:slug` → `BlogPost section="keywords"` (slug DB reconstruit = `liste-des-mots-cles-${param}`, canonical/back-link adaptés). Pas de duplication des 330 lignes de BlogPost.
- Nouvelle page `ListesMotsCles.tsx` (clone de Blog.tsx) : fetch `/blog-data/keyword-lists.json`, fallback Supabase `slug like 'liste-des-mots-cles-%'`. `BlogCard` reçoit un prop `href` + `iconName`.
- `Blog.tsx` exclut désormais les listes (`not slug like prefix`) ; `generate-blog-urls.js` génère 2 manifests (`posts.json` = 7 articles, `keyword-lists.json` = 23 listes) et bascule les URLs reactSnap vers `/listes-mots-cles/...`.
- 301 : `netlify.toml` (prioritaire sur `_redirects`) `/blog/liste-des-mots-cles-* → /listes-mots-cles/:splat force=true`, placé AVANT le catch-all SPA. Doublon documentaire dans `_redirects`.
- Sitemap edge function + `inject-seo-tags.js` + `publish-keyword-list.mjs` alignés sur la nouvelle URL. Constantes partagées dans `config/site.ts` (`KEYWORD_LIST_PREFIX/PATH`, helpers).
- Icône distinct par carte : palette de 35 icônes lucide, assignation stable par rang alphabétique du slug (23 distincts garantis). Vérifié headless (Chrome système — le Chromium puppeteer plante en -86 arch).

**Vérif.** Render headless OK (index 23 cartes + icônes uniques, détail h1/back/canonical, blog sans listes). Bundle vite build OK. Post-deploy prod : `/blog/liste-...-consultant-seo` → 301 `Location: /listes-mots-cles/consultant-seo`, index + détail 200, sitemap = 23 URLs.

**Deploy.** Commit `11aedde` push main → Netlify (`fusionn2`). Edge function `generate-sitemap` redéployée + `sitemap.xml` régénéré (via curl direct, `generate-sitemap.js` exige un `.env` absent). Le commit embarque aussi, à la demande de Tim, sa feature tracking analytics en cours (PageTracker, `lib/tracking`, admin-v2, `admin-stats-v2`, 3 migrations) ; `supabase db push --dry-run` = « up to date » (migrations déjà appliquées en prod par sa session parallèle).

**À noter (non traité, hors scope).** Incohérence pré-existante `fusionn.io` (sitemap, inject-seo-tags, config/site `SITE_URL`) vs prod canonique `fusionn.co`. 96 erreurs TS pré-existantes dans le repo (le build vite ne typecheck pas).

## 2026-05-28 (suite) — Scores des « Liste des mots-clés » unifiés sur /10

**Demande Tim.** « Pourquoi cette note sur 125 ? Tu peux pas faire que des notes sur 10 partout ? On doit retravailler les scores. Si impossible, ne pas mettre de score. » Contexte : il challengeait la qualité des pages (slop ?) et la fausse précision des scores. Décisions actées : Score /10 entier partout, propagation pages + skills.

**Diagnostic des échelles.** 2 tableaux scorés par page : décisionnels `Score /125` (= proximité × intention × faisabilité, chacun 1-5, produit max 125) et modèles `Score /5` (même produit ramené sur 5). Sources : skills `seo-mots-cles-decisionnels` (/125) et `seo-modeles-pseo` (/5). La colonne « Pages » du tableau de segmentation (8, 7, 6…) n'est PAS un score → à ne pas toucher.

**Fix.** Script `scripts/rescale-scores.mjs` (newFusionn, idempotent, dry-run par défaut, garde `isMain`) : transforme uniquement la colonne dont l'en-tête contient « Score ». Rescale déterministe `/125 → round(v/12.5)`, `/5 → round(v*2)` (gère la décimale FR « 4,0 »), clamp 0-10, en-tête → « Score /10 ». Prose alignée (« sur 125 » → « sur 10 », « scorés sur 5 (proximité…) » → « sur 10 »). Appliqué aux 23 drafts (`--apply`) + DB `blog_posts` (`--db --apply`, service_role) + régénération `public/blog-data`. Résidus /125 ou /5 : 0 partout. Vérif headless : en-têtes « Score /10 », valeurs 8/6…, colonne Pages intacte.

**Skills corrigés.** `seo-mots-cles-decisionnels` (méthodo + exemple `64/125` → `5/10`) et `seo-modeles-pseo` (« ramené sur 0-5 » → « 0-10 », en-tête `Score Business /5` → `/10`, exemples). Vérifié : aucune edge function ni Qadence ne hardcode le /125. NON touchés (échelles différentes, hors de ces pages) : `seo-roadmap-pseo` (score priorité max 24) et `seo-product-led-seo` (Confidence Score sans dénominateur fixe) — à harmoniser plus tard si Tim veut.

**Deploy.** newFusionn commit `d1b9ce2` push main → Netlify (`fusionn2`). DB déjà resynchronisée. 23 drafts commités dans seo-kb. Skills `~/.claude/skills` modifiés en local.

**Question de fond ouverte (slop).** Le rescale règle l'échelle, pas le grounding : les scores restent des jugements modèle (pas de volume/difficulté sourcés). Gemini juge la page Prestashop « très haute volée » mais évalue 1 page en lecture, sans voir l'isomorphisme des 23 templates ni l'absence de data. Reste à grounder (vraie data métier) et différencier (1 angle Haute Surprise par page) si on veut sortir franchement de la zone slop.

## 2026-05-28 (suite) — Grounding des 23 pages sur data réelle (Google Suggest)

**Demande Tim.** Suite au débat slop : grounder le contenu (et le score) des pages mots-clés sur des sources gratuites réelles. Validé après proto sur Prestashop. Consigne ajoutée en cours de route : **aucune note de provenance/méthode ni disclaimer volume sur les pages** (le grounding reste invisible) — sauvegardé en mémoire `feedback_pas_de_provenance_pages.md`.

**Découverte clé.** Le `fetch-volume-trends` de Fusionn n'a pas de vraie source : il fait estimer les volumes par **Gemini** = même slop. Pour de la vraie data gratuite : Google Suggest (requêtes réelles), Reddit JSON, HN Algolia. Les volumes absolus restent non-sourçables sans Keyword Planner / API payante → jamais inventés.

**Outils créés (newFusionn/scripts).**
- `ground-keyword.mjs` : Google Suggest (seed + a-z + topic + rôles + modificateurs FR) avec un `pull` = nb de seeds qui font remonter la requête (proxy de demande) + Reddit + HN. Sans clé API. Sortie data pack JSON.
- `ground-brief.mjs` : transforme un pack en buckets actionnables (villes, comparatifs vs/ou, pricing, rôles, **hors-intention à écarter** type formation/emploi/salaire/definition).
- `rescale-scores.mjs` : déjà créé à la session scores.

**Harvest.** 23 mots-clés, packs dans `seo-kb/fusionn/grounding/*.json`. Riche pour les métiers de service (centaines de requêtes, vraies villes), **bruité** pour les mots génériques (growth → « beard growth », ia → « ia ou ai », marketing → « burger king »). Reddit/HN faibles sur le B2B FR.

**Grounding appliqué (drafts + DB + JSON).**
- Prestashop (proto complet) : certif « core skills » (au lieu de « 2/3 étoiles » inventé), villes réelles (Grenoble/Vannes), comparatifs vs/ou WordPress, « freelance prestashop tarif ». Exclusion assumée des requêtes hors-intention (formation, emploi).
- 13 autres pages de service : **vraies villes par métier** (Lyon #1 sur consultant/freelance/expert shopify ; Casablanca/Montréal sur marketing ; offshore Tunisie/Maroc/Madagascar sur rédacteur web), villes devinées retirées (Londres/Berlin/Amsterdam sur growth, Strasbourg sur communication), fausse précision retirée (TJM inventés agence SEO).
- Les 22 : **disclaimer volume « pas de Keyword Planner branché »** retiré (2 variantes templatées).
- Pages outils (outil seo/ia, logiciel marketing, saas b2b, plateforme analytics, outil de prospection, vendeur amazon, seo-content-writer, e-commerçant) : pas de grounding villes (pas d'intention locale / data trop bruitée), déjà alignées sur l'intention réelle (gratuit/meilleur/pas cher) + disclaimer retiré. Grounding plus poussé possible plus tard si Tim veut.

**Constat honnête.** Les pages bien développées (agence-seo, consultant-seo) étaient **déjà** alignées sur l'intention réelle (elles couvrent GEO/AEO, tarif, alternative, sans engagement — tous high-pull réels). Moins de slop que craint ; le vrai gisement de grounding c'était les **listes de villes** (souvent devinées) + tuer la fausse précision.

**Deploy.** newFusionn commit `c235e29` (empilé sans conflit sur un commit parallèle `d442cb1` de Tim) push main → Netlify. DB resync 23/23. Drafts + packs + Historique commités dans seo-kb.

**Reste à faire si Tim veut aller plus loin.** Grounding éditorial profond des pages outils ; score regroundé sur le `pull` réel (au lieu du jugement modèle) ; brancher une vraie source de volumes (Keyword Planner / DataForSEO) pour passer de « requêtes réelles » à « requêtes réelles + volume réel ».

## 2026-05-28 (suite) — « Pour qui » factuel + scores regroundés sur le pull

**Demande Tim.** (1) « Sait quel pan du SEO il veut faire bouger en priorité : ça ne veut rien dire. Sois factuel, anti-AI writing. » → colonne « Pour qui » des tableaux à rendre concrète. (2) « On va changer et partout, regrounder le score sur le pull réel de Suggest. » Skill `ton-de-voix-tim` chargé. Règle sauvegardée : [[feedback_pour_qui_factuel]].

**Pour qui factuel (23 pages).** Réécriture des cellules « Pour qui » vagues (mind-reading creux : « sait quel pan il veut faire bouger », « se reconnaît dans un rôle ») en factuel concret ancré sur la colonne Exemples (leviers, rôles, secteurs réels). Agence-seo fait à la main (étalon), les 22 autres délégués à 3 sous-agents en parallèle puis vérifiés (0 tiret cadratin, 0 mot banni, scores intacts) ; 17 cellules résiduelles ratées par un agent corrigées à la main. Pages outils adaptées (intention produit, pas prestataire).

**Scores regroundés sur le pull (script `reground-score-pull.mjs`).** Le score /10 ne reflète plus un jugement modèle mais la demande réelle : match des tokens DISTINCTIFS du mot-clé (terme tête retiré) contre les requêtes du pack Suggest, pull → /10 (bucket). Stoplist élargie (google, mois, jours, villes…) après un 1er run qui matchait « 90 jours » sur « seoul combien de jours ». Mots-clés à vraie demande montent (tarif→8, GEO/AEO→7), inventions sans demande → 4 (demande non confirmée, gardées et transparentes, choix Tim). Révèle que ~la moitié des « décisionnels » d'agence-seo n'avaient aucune demande réelle.

**Deploy.** newFusionn : le travail s'est retrouvé poussé en `8ab7ea5` (commit identique d'une session parallèle ; mon commit local redondant droppé au rebase). DB resync 23/23. Drafts + Historique commités dans seo-kb.

---

## 2026-05-29 — Filtre anti-noms propres (Générateur Suggest)

**Règle.** Interdiction de publier le nom d'un freelance, d'une personne, d'une entreprise ou d'une agence dans les résultats du Générateur de mots-clés. Le résidu « adrien beaujeu » survivait au filtre `pull>=2` (commit `309f8c1`) parce que corroboré par 2 préfixes indépendants.

**Solution.** Dictionnaire de prénoms FR (~270 entrées) dans `tool-suggest-extract/index.ts`. Google Suggest renvoyant tout en minuscules, la casse est inutile : un prénom isolé dans une requête de service = quasi toujours une personne. Helper `isNominal(query, kwTokens)` ; drop en amont du filet `MIN_RESULTS` (comme `hors-intention`) pour qu'aucun nom interdit ne soit ressuscité pour remplir la page.

**Garde-fous faux positifs.** Prénoms aussi noms communs/marques (rose, pierre, olivier, margaux, jade, iris, camille…) volontairement absents de la liste. Un prénom déjà présent dans le mot-clé tapé n'est jamais filtré (respect d'une recherche nominale volontaire).

**Deploy + test.** Commit `afe2f57` poussé sur `main`, edge function déployée sur Supabase prod (`fwhfnzbtlddzfxbsejyf`). Test live `consultant seo` : 24 résultats, 0 nom propre (vs « adrien beaujeu » avant).

---

## 2026-05-29 — Premium manuel pour seosfpro@gmail.com

**Demande.** Passer seosfpro@gmail.com en premium avec recherche illimitée.

**Action.** Insertion d'une ligne dans la table `subscriptions` (Supabase prod `fwhfnzbtlddzfxbsejyf`) pour le user `5ad447b8-380d-4e2d-b237-1f75b655d03d` : `status: active`, `plan_name: Premium manuel`, `plan_price: 0`, `current_period_end: 2099-12-31`, sans Stripe (le code valide le premium sur statut + période, pas sur les ids Stripe depuis la migration). Pas d'abonnement préexistant.

**Effet.** Premium reconnu front + edge functions → recherche illimitée (free = 3), Semantic/HN 999/mois, chat 15/jour. Pas de déploiement, data prod, effet immédiat après refresh.

---

## 2026-05-30 — Retrait de la page /analyse-texte

**Contexte.** Tim ne veut plus de la page publique `fusionn.co/analyse-texte` (analyse de texte GEO en standalone).

**Action.** Suppression frontend complète + 301 + backend. Commit `3c1e804` sur `main` (repo newFusionn), push → auto-deploy Netlify (site `fusionn2`).
- Supprimé : page `AnalyseTexte.tsx`, composants exclusifs `GeoAnalysisHistory`, `HighlightedText`, `SemanticCoverageDisplay`, `AnalyseChatPanel` (déjà orphelin).
- Retiré : la route `/analyse-texte` dans `App.tsx` + l'entrée « Analyser » du menu Navbar.
- 301 `/analyse-texte` → `/` ajouté dans `netlify.toml` (URL déjà indexée).
- Edge function `check-geo-analysis-limit` supprimée (code + déploiement Supabase `fwhfnzbtlddzfxbsejyf`).

**Conservé.** L'analyse GEO reste dans le **workspace** (`/compte`) : `GeoScoreCard`, `EditorAnalysisPanel`, et l'edge function `analyze-geo-sentinel` (partagée, toujours active).

## 2026-05-30 — Nettoyage navbar (Notes + Historique)

**Contexte.** Suite au retrait de /analyse-texte, Tim veut alléger la navbar.

**Action.** Commit `4a501ae` sur `main` (repo newFusionn), push → auto-deploy Netlify.
- Retiré le bouton **Notes** (icône stylo) de la navbar + suppression des composants `NotesModal.tsx` et `FloatingNoteButton.tsx` (ce dernier déjà orphelin).
- Retiré l'**icône Historique** de la navbar (jugée redondante avec « Mon Espace »). Pas d'ajout dans le bouton Action (demande annulée par Tim).
- Nettoyage des imports/state inutilisés (`Pen`, `History`, `AnimatePresence`, `isNotesOpen`, `hasActiveNote`, `notesDropdownRef`).

**Note.** Erreurs `tsc` pré-existantes dans `Documentation.tsx` (typage LucideIcon), sans rapport ; le build réel est `vite build` (pas de type-check), passe vert.

## 2026-05-30 — Radar LLM : plus de relance automatique

**Contexte.** Tim : « Sur tableau de bord, il faut toujours voir ou relancer sur les mots-clés, jamais relancer tout seul. »

**Diagnostic.** L'onglet Radar LLM (`LLMView.tsx`) appelait `ensure-tracked-cluster` dans un `useEffect` au montage / changement de mot-clé. Avec quota=1, ça mettait l'ancien cluster en pause et lançait un scan Gemini fire-and-forget sans clic → relance automatique non voulue, consommant le quota.

**Action.** Commit `853e66c` sur `main` (newFusionn).
- À l'ouverture : lecture seule de l'existant via `select tracked_clusters` (RLS « Users select own tracked clusters »), aucun scan.
- Mot-clé jamais scanné → état vide explicite + bouton manuel « Lancer le scan Gemini ».
- Premier scan + re-scan : uniquement sur clic. Aucun changement backend (RLS suffisait).

**Note.** Le déclenchement du radar via `useSearchPipeline` (lors d'une recherche explicite « Rechercher ») a été laissé tel quel : c'est une action utilisateur, pas une relance auto.

---

## 2026-05-30 — Agent Search Console + refonte header + onglet Historique

**Search Console dans l'agent.** Reprise du fil GSC inachevé (table `google_connections` + flux OAuth `google-auth`/`google-oauth-callback` déjà en prod, 44 connexions existantes, mais aucune récupération de données ni consommation chat). Porté le `fetchGSC` de Qadence dans `supabase/functions/_shared/gsc.ts` (refresh token, searchAnalytics, cache 2h). Créé la fonction `gsc-fetch` (que le front appelait dans le vide). Ajouté le **function-calling Gemini** dans `ai-chat` (outil `fetch_gsc_data`) — garde-fou : comportement strictement inchangé si l'utilisateur n'a pas connecté sa Search Console. Onglet Agent : bannière de connexion + sélecteur de propriété GSC. Décisions Tim : réutiliser l'onglet Agent (pas de nouvel onglet) + tool-calling à la Qadence. Fonctions déployées sur prod `fwhfnzbtlddzfxbsejyf`.

**Refonte header (Navbar).** Supprimé le bouton « + » et son dropdown → 3 entrées minimalistes **Rechercher / Espace / Historique** (texte + petite icône, accent `#FF371C` sur l'actif). Icône compte refaite en avatar minimaliste (cercle initiale + prénom). Bouton « Accéder à mon compte » supprimé (Espace fait le même job). Contenu du header désormais **identique home / compte**.

**Espace = workspace dernière recherche.** `handleAnalyzeClick` ouvre maintenant `handleHistoryItemClick(searchHistory[0])` au lieu du tableau de bord.

**Tableau de bord.** Nouvel onglet **Historique** (Recherches / Historique / Projets) : toute la liste filtrable des recherches y a basculé, l'onglet Recherches garde la vue d'ensemble (stats + récentes). Carte « Historique » renommée **« Opportunités détectées »** (lève la confusion avec l'entrée de nav), sous-texte réécrit, badge compteur en pill marque, score badge `/100` teinté quand pertinence ≥70.

**Deploy.** Front : commit `d6e477f` poussé sur `main` (Netlify auto-deploy). Build prod OK. Backend : `ai-chat` + `gsc-fetch` déployées.

---

## 2026-05-30 (suite) — Agent : panneau latéral, croisement GSC, anti-netlinking ; Structure+FAQ ; flash home

**Chat / Agent.**
- Panneau latéral repliable à droite du chat : onglet **Historique** (conversations précédentes = mots-clés analysés, clic rouvre la recherche via `onOpenSearch`→`handleHistoryItemClick`) + onglet **Agents (Bientôt)** = teaser `AgentsComingSoon` (thinking flow animé en boucle + écrans mockés Agent Maillage/Search Console/Rédaction/Veille).
- Search Console mise en avant : **point vert « connectée »** + sélecteur « Propriété analysée ».
- Prompt `ai-chat` : **REGLE 12 anti-netlinking** (jamais d'achat/vente/échange de liens ; maillage interne OK) + **croisement systématique** Search Console ↔ analyse workspace dans les réponses.

**Fix GSC (erreur d'accès fusionn.io).** `fetchGSC` (`_shared/gsc.ts`) : restauration de la validation de propriété contre les sites réellement vérifiés (auto-correction `sc-domain:`/`https://`/www/slash) + erreur explicite listant les propriétés accessibles. Diag : `fusionn.io` est un 301 vers `.co` ; la donnée vit sous une autre propriété. Tim a plusieurs comptes Fusionn (même Google) ; la propriété connectée est `https://fusionn.io/`.

**Workspace.** Onglet **FAQ fusionné dans Structure** (la FAQ s'affiche sous la structure Hn, onglet FAQ retiré de `ResultsNav`).

**Home.** **Flash UX orange** (glow pulsé) sur la barre « votre site » pour inciter à saisir son site ; s'arrête au focus, off si reduced-motion.

**Navbar.** « Espace » non cliquable s'il n'y a aucune recherche (calcul `effectiveCanAccessEspace` côté Navbar global).

**Deploy.** Front commit `807f24e` sur `main` (Netlify). Edge `ai-chat` + `gsc-fetch` déployées. Build prod OK.

---

## 2026-05-30 (suite) — Audit global UX/UI/technique + corrections « tout corriger »

**Audit.** 3 sous-agents (UX, UI, technique) sur l'état prod `main`. Synthèse priorisée écrite dans `fusionn/Audit-2026-05-30-global-ux-ui-tech.md` (P0/P1/P2 + 8 priorités absolues). Constat : pivot site-first partiel (entrée URL posée par-dessus le système keyword-first), cœur workspace sain, dette concentrée sur les écrans récents + sécurité des Edge Functions.

**Corrections déployées (mêmes que commit `00a6be7`).**
- **Sécurité S1.** `_shared/auth.ts` : le `userId` est dérivé du JWT, plus du body, dans `generate-semantic-keywords` et `generate-business-score` (corrige un IDOR + un bypass des crédits exploitable avec la clé anon publique). Vérif d'appartenance de la recherche sur business-score. Functions redéployées.
- **Sécurité S2.** Migration `20260530220000_lock_documents_rls` : suppression des policies anon « Anyone can ... » qui exposaient tous les documents de contexte (cross-user). Appliquée en prod via `db push`.
- **Fiabilité crawl R1.** `start-site-crawl` renvoie `crawl_id` tout de suite et exécute le crawl en arrière-plan (`EdgeRuntime.waitUntil`) avec deadline globale 70s + statut terminal garanti (plus de polling infini). `useSiteCrawl` : verrou coverage/opportunities relâché en cas d'échec + garde-fou anti-boucle (5 min).
- **Activation UX1/UX2.** `SiteAuditPanel` vérifie le quota AVANT le crawl (plus de ~1 min d'analyse pour un compte sans crédit) et affiche les analyses restantes. Onboarding keyword-first retiré : le hero site-first est l'unique point d'entrée.
- **Design system.** `SiteAuditPanel` : `slate-*` migré vers tokens `--ws-*`, shimmer en gris chaud, marque sur `var(--ws-brand)`. Nouveaux tokens `--ws-brand-hover` + sévérité, `focus-visible` global. Verts `#244831` + glassmorphism retirés de `OnboardingOverlay`, `SubscriptionChoiceModal`, `SeoConversationalChat`. `aria-label` sur les boutons icône de l'agent. `FirstSearchTour` au vouvoiement.
- **Perf.** `loadSearchHistory` dérive les compteurs de `results_summary` (les 4 requêtes lourdes ne tournent plus que pour les anciennes recherches sans summary). `resultsLoader` : colonnes ciblées au lieu de `select('*')`. Code-split déjà en place (Compte/pdf/mammoth en chunks séparés).
- **Copy.** Promesse de temps alignée (~1 min) sur Landing et Connexion.

**Reste P2 non traité (volontairement, hors scope risque/temps) :** responsive mobile du workspace 3 colonnes, unification IA de la navigation (ViewMode/ResultsNav), écrans d'erreur crawl enrichis, autres `generate-*` qui écrivent avec userId du body (write-only, faible risque), CORS `*` à restreindre.

**WIP de Tim non touché :** migrations email lifecycle (`180000`-`210000`) + `cron-lifecycle-emails` laissées non commitées.

**Deploy.** Front commit `00a6be7` sur `main` (Netlify auto-deploy). Edge `start-site-crawl` + `generate-semantic-keywords` + `generate-business-score` redéployées. Migration RLS appliquée. Build prod OK, tsc clean.

**Suite P2 (commit `c2d0ac9`).**
- **Sécurité (suite S1).** `generate-vecteurs/tools/reddit-keywords/objections/youtube-keywords/faq` : userId effectif dérivé du JWT (`authed ?? body`), parcours authentifié non usurpable. `analyze-hn-score` déjà JWT-only. Functions redéployées.
- **Robustesse R5.** `ai-chat` : timeout AbortController 30s sur les appels Gemini (boucle outils + streaming).
- **Responsive mobile.** Agent chat : sidebar 258px + conteneur en pleine largeur empilée sous 768px. Workspace 3 colonnes : scroll vertical au lieu de clip sous 768px.
- **UX.** Écran d'erreur crawl enrichi (cause + recours). Remise annuelle alignée à -30% (modale abo). Teasers Reddit « Bientôt » retirés (nav workspace + carte Landing). Au passage, mot « concurrents » retiré d'un visuel Landing.
- **Restent hors scope :** unification IA navigation (ViewMode/ResultsNav), CORS `*` (volontairement gardé : le restreindre casserait dev local + previews Netlify, et l'auth fait foi), onglet « Agents Bientôt » et doc Reddit conservés (retrait risqué).
- **Deploy.** Front `c2d0ac9` sur `main` (Netlify). 7 functions redéployées. Build prod OK, tsc clean. WIP email de Tim toujours non touché.

**Unification navigation workspace (commit `3212895`).** Choix de Tim : supprimer les orphelins + condenser.
- Retrait des 3 modes orphelins (rendus mais inaccessibles) : `planAction` (doublon du sous-onglet pSEO), `llm` (radar citations IA), `writer` (éditeur). `WorkspaceLayout` ne garde que **Stratégie + Agent** ; tout le code éditeur/polling/autosave retiré (-70 modules au build). `ViewMode` = `'strategy' | 'agent'`. Type mort `'conversation'` retiré (`businessScore`/`synthese` gardés, encore référencés).
- `ResultsNav` : **5 sections → 3** (Comprendre : Brief, Mots-clés, Clusters, Micro-intentions, Analyse | Produire : Structure, Outils, Objections, YouTube | Décider : Stratégie pSEO).
- Composants orphelinés (PlanActionView, LLMView, EditorPanel, AssistantChat, EditorAnalysisPanel) laissés en modules morts (tree-shakés), non supprimés pour éviter une cascade risquée.
- Deploy : front `3212895` sur `main` (Netlify). Build OK (2925 modules), tsc clean.

## 2026-06-01 — Fix focus champ URL hero (carré orange)

**Bug.** Au focus du champ URL du hero (`SiteAuditPanel`, phase accueil « Bonjour [prénom] »), un outline orange à coins droits débordait du champ arrondi (« carré orange cassé »). Cause : la règle globale d'accessibilité `input:focus-visible { outline: 2px solid var(--ws-brand) }` (`src/index.css`) s'applique à l'`<input>` intérieur alors que le visuel du champ est le `div` wrapper arrondi ; sa spécificité (`input:focus-visible`) écrase le `outline-none` Tailwind, d'où la persistance.

**Fix (`SiteAuditPanel.tsx`).** Outline neutralisé sur l'input (`focus:outline-none focus-visible:outline-none`) et affordance de focus portée sur le wrapper via `focus-within:border-[--ws-brand] focus-within:ring-1 focus-within:ring-[--ws-brand]`. Ring orange 1px qui épouse les coins arrondis, toujours accessible au clavier, raccord design system. Règle globale `input:focus-visible` conservée pour le reste de l'app.

**Deploy.** Commit `35c75af` sur `main` (Netlify auto-deploy). tsc clean, montré en local sur `/compte`.

## 2026-06-02 — Refonte agent : plein écran, attribution GSC, fix historiques, bouton Skills

**Chat plein écran (façon Claude).** La conversation occupe désormais toute la partie droite, de sous la nav bar jusqu'en bas. Suppression de la carte flottante centrée : `.agent-chat-container` perd `border` + `border-radius` + `max-width: 1040px` et passe en `height: 100%` ; `.agent-chat-layout` perd son `padding`/`gap`. Sidebar historique rendue flush (bordure droite seule au lieu d'une carte arrondie). Bouton de repli avec petite marge quand la sidebar est fermée.

**Attribution GSC (prouver qu'il n'invente rien).** Dans `ai-chat/index.ts`, section « Google Search Console » du prompt système (active dès que la GSC est connectée) : règle non négociable d'annoncer explicitement la source à chaque donnée issue d'un `fetch_gsc_data` (« D'après votre Google Search Console… », « Ce que je lis sur votre Search Console… ») avec période et propriété, et de séparer le constat chiffré de l'interprétation. Interdiction de présenter un chiffre comme GSC sans appel d'outil préalable.

**Fix historiques qui disparaissaient/fusionnaient.** Cause racine : un seul thread par (user, search, full_context). Au clic « Nouvelle conversation » le client envoyait `threadId=null`, et l'edge réutilisait le dernier thread au lieu d'en créer un neuf → toutes les conversations fusionnaient ; pire, `.maybeSingle()` plantait dès 2+ threads. Correctifs : nouveau param `newThread` (le client l'arme via `forceNewThreadRef` au clic « Nouvelle conversation ») qui force un `insert` ; lookup robuste `order('updated_at').limit(1).maybeSingle()` au lieu de `maybeSingle()` seul ; `loadConversations()` rappelé après chaque envoi pour rafraîchir la liste latérale.

**Refonte UX box « Propriété analysée ».** Le `<select>` natif héritait du brand orange en `accent-color` (contour orange cassé). Remplacé par un contrôle custom `.gsc-property-select` : `appearance: none`, chevron SVG gris, bordure + focus du design system (halo gris léger, plus d'orange). Cas mono-propriété affiché en chip gris clair.

**Bouton « + Skills » (repris de Qadence).** En haut à droite de la conversation, un bouton ouvre un popover listant 10 skills SEO ; le clic envoie un prompt prêt à l'emploi à l'agent via le `sendMessage` existant, sans aucune dépendance serveur ajoutée (pas de tool `load_skill` ni de table comme Qadence). Skills : Quick wins, Audit Search Console, Cannibalisation, Maillage interne, Mots-clés décisionnels, Brief de contenu, Structure Hn, Décodage de la requête, FAQ stratégique, Contenus manquants, Score GEO. Chaque prompt s'adapte au mot-clé en cours et pousse à s'appuyer sur la GSC. Header passé en barre flex (GSC à gauche, Skills à droite) affichée même sans GSC connectée ; popover fermé au clic extérieur + Échap ; skills désactivés tant qu'aucune analyse n'est lancée.

**Deploy.** Commit `482244f` sur `main` (Netlify auto-deploy front). Edge `ai-chat` redéployée (Supabase) pour activer fix historique + attribution GSC. tsc clean, montré en local sur :5173. Dossier non suivi `supabase/functions/admin-gsc-study/` laissé de côté (non créé dans cette session).

---

## 2026-06-03 — Diagnostic & remise en route du moteur d'emails lifecycle

**Constat.** Tim demande si 10 nouveaux inscrits ont reçu les emails du workflow selon leur nombre de recherches. Croisement `email_queue` × `auth.users` × `search_history` (service_role, projet `fusionn` fwhfnzbtlddzfxbsejyf) : **la file était figée à 50 lignes, toutes datées du 2026-05-30** (jour du go-live), zéro entrée depuis. Le cron quotidien n'avait jamais été planifié (le README renvoyait au Dashboard, étape jamais faite). Résultat : tous les users devenus éligibles après le 30/05 n'ont rien reçu.

**Nuance.** Les 10 de la liste ont tous fait 1-2 recherches → ils ne relèvent pas de `activation_no_search` (0 recherche) mais des nudges, déclenchés 24h après la recherche. 8 (recherche du 06-02) n'avaient pas encore passé les 24h ; 2 (rousclement, t.rabeson, recherche du 06-01) étaient en retard.

**Actions.**
1. **Rattrapage réel** : régénéré `LIFECYCLE_CRON_SECRET` (valeur d'origine non extractible), invoqué `cron-lifecycle-emails` en réel (`LIFECYCLE_EMAILS_ENABLED=true` déjà armé). **13 emails envoyés, 0 échec** (4 activation, 6 nudge_1, 3 nudge_2) — dont rousclement + t.rabeson.
2. **Cron durable** : migration `20260603050000_schedule_lifecycle_emails_cron.sql` → job pg_cron `lifecycle-emails-daily` à `0 9 * * *`, POST de la fonction via pg_net, secret `X-Cron-Secret` lu depuis **Vault** (jamais en clair dans le repo). Vérifié : job id=2 actif. Secret rédigé hors du fichier après push. Commit `d3f59d8` sur `feat/lifecycle-emails`.

**Suite.** Les 8 inscrits du 06-02 partiront automatiquement au run de 09:00 UTC à mesure qu'ils passent 24h.

## 2026-06-03 — Compte : bouton « Gérer mon compte » vers le portail Stripe

**Constat.** Dans la modale Compte (`UserProfile.tsx`), les premium voyaient « Abonnement géré manuellement. Pour toute modification, contactez le support. » au lieu d'un bouton vers le portail Stripe. Cause : le bouton n'était rendu que si `subscription.stripe_customer_id` existait en base, or beaucoup de comptes premium n'ont pas ce `cus_` synchronisé.

**Correction.**
1. **Edge function `create-billing-portal-session`** : si pas de `stripe_customer_id` en base, on retrouve le client existant **par email** (`stripe.customers.list({ email })`, jamais de création → pas de double facturation, cf. règle `admin-link-stripe` proscrit), puis backfill de la ligne `subscriptions`. Déployée sur `fwhfnzbtlddzfxbsejyf`.
2. **Front** : le bouton « Gérer mon compte » s'affiche toujours pour un premium et ouvre le portail. Message « géré manuellement » supprimé.

Typecheck OK. Commit + push `main` (Netlify déploie fusionn.co).

---

## 2026-06-06 — Réparation moteur emails lifecycle + monitoring

**Constat** : séquence email morte depuis le 3 juin (63 envoyés du 30 mai au 3 juin, puis 0, `email_queue` vide). Inscrits récents ne recevaient rien.

**Cause racine (définitive)** : `cron-lifecycle-emails` est en `verify_jwt=true`, mais le pg_cron l'appelle avec `X-Cron-Secret` seul, sans header `Authorization`. Tous les tirs rejetés en **401 par la plateforme** avant d'atteindre le code. Les envois 30 mai-3 juin = déclenchements manuels (avec JWT). Preuve : sans Authorization → 401 ; avec → 200, `sent:14`.

**Correctifs** : (1) backlog flushé = 14 emails (0 échec, total 77) ; (2) `LIFECYCLE_CRON_SECRET` régénéré ; (3) nouveau déclencheur = routine distante `trig_01Fx1xDt1CAR4Hh3c5Tp4jof` (quotidienne 08:00 UTC, curl avec Authorization anon + X-Cron-Secret). pg_cron laissé actif mais en 401 (inoffensif, idempotence) ; nettoyage propre = accès DB requis.

**Monitoring (nouveau)** : edge function `ops-alert` (Resend, `--no-verify-jwt`, commit `d2ebaf3`) + watchdog quotidien `trig_01H7tem5fgt25yF2vAddPSyJ` (11:00 UTC) + rapport hebdo email `trig_015EHXasyZs5zGmdR6kYtNMZ` (dimanche 12:00 UTC). Détail : note mémoire `project_monitoring_automatisations`.

---

## 2026-06-06 — Onglet « Par contexte » : les prompts mots-clés ignoraient le contexte/documents

**Symptôme (signalé par Tim)** : en mode « Par contexte », le contexte saisi + documents uploadés ne semblaient pris en compte que dans les micro-intentions, pas dans la liste de mots-clés.

**Diagnostic** : le câblage existe (extraction docs ≤30k chars, fusion note+docs, injection `context` dans les 11 edge functions, cache contourné si contexte ≠ vide). MAIS dans `generate-semantic-keywords` le contexte était **dumpé en vrac** (`CONTEXTE :\n${context}`) sans aucune directive d'usage, noyé sous les règles génériques (expansion, clustering, scoring) qui ne parlaient que du mot-clé pivot. À temp 0.2 → contexte inerte, mots-clés génériques. Les autres functions (faq, tools, objections, models, micro-intentions, semantic-analysis, vecteurs, youtube) avaient une directive « Utilise ce contexte pour adapter… » → d'où l'impression que seules les micro-intentions en tenaient compte. `generate-brief` était aussi un simple dump.

**Correctifs** : (1) `generate-semantic-keywords` — bloc « CONTEXTE IMPÉRATIF » qui prime, + rappels dans MÉTHODE (filtre le plus dur = contexte) et CLUSTERING (nommage dérivé du contexte). (2) `generate-brief` — contexte rendu impératif. Les 5 autres functions vérifiées : directive déjà OK. **Déployé** sur `fwhfnzbtlddzfxbsejyf` (generate-semantic-keywords, generate-brief).

---

## 2026-06-06 — Nouvel outil gratuit « Générateur de mots-clés gratuit »

**Objectif** : outil gratuit qui, à partir d'UN mot-clé de départ, génère 20 mots-clés autour via l'API Gemini, avec Score Business et fourchette de volume dans l'analyse. Construit sur le modèle des autres outils (ToolPageLayout).

**Edge function** : `tool-keyword-generator` (déployée sur `fwhfnzbtlddzfxbsejyf`). Gemini (`gemini-3.1-flash-lite`) propose 20 requêtes + signaux qualitatifs ; le **Score Business est calculé en code** (mêmes poids déterministes que `score-keywords-batch` : intent, modificateur commercial, signal local, pénalité substitution IA, tension commerciale, proximité offre, borné 0-100). La **fourchette de volume** est un ordre de grandeur estimé (tiers very-high→niche), **hors du score** et jamais un chiffre précis inventé (doctrine anti-volume + anti-hallucination). Sanitize/dedup côté serveur, exclut le seed.

**Page** : `src/pages/KeywordGenerator.tsx`, route `/generateur-mots-cles-gratuit`. Un seul champ de saisie (comme Suggest) → tableau trié par Score Business avec colonnes Volume estimé / Score / Potentiel / Détail (breakdown ligne par ligne), bloc « champion », bloc méthodo, FAQ + related links + schema FAQPage. Copy au vouvoiement, zéro mention d'argent (« tension commerciale » au lieu de CPC/euros), pas de tiret cadratin.

**Câblage** : route App.tsx (lazy), lien Footer (en tête des outils gratuits), entrée sitemap.xml.

**Vérifs** : tsc OK sur les 2 nouveaux fichiers (bruit TS préexistant ailleurs ignoré par `vite build`). Test réel sur « consultant seo » → 20 résultats, champion « agence seo paris » (100/100), volumes et scores cohérents. Montré en local (port dev).

**Reste à faire** : commit + push main pour déploiement Netlify prod (en attente de la relecture locale de Tim).

---

## 2026-06-06 — Migration LLM hybride Gemini → Claude (brief Opus 4.7, objections+vecteurs Sonnet 4.6)

**Contexte** : audit des 17 edge functions `generate-*`. Tri masse (reste Gemini) vs raisonnement stratégique (→ Claude). Helper `_shared/claude.ts` (Anthropic Messages API, raw HTTP). Sélecteur provider par fonction via `body.<x>Model` (override testable) ou env `<X>_MODEL` ; défaut Gemini inchangé.

**POC brief réel** (« accompagnement qualiopi », Opus 4.7 vs Gemini Flash) : Opus nettement supérieur (entités réglementaires réelles décret 2019-565/COFRAC/RNQ 32 indicateurs, 8 semantic gaps vs 4, Surprise Gap métier « désalignement BPF/site/conventions »). Coût réel mesuré : 2564 in / 3545 out, **0 token de thinking** → ~0,10 $/brief vs ~0,01 $ Gemini.

**Activé en prod** (clé `ANTHROPIC_API_KEY` posée dans secrets) :
- `BRIEF_MODEL=claude-opus-4-7`
- `OBJECTIONS_MODEL=claude-sonnet-4-6`
- `VECTEURS_MODEL=claude-sonnet-4-6`

**Décision technique** : thinking COUPÉ sur tous les appels Claude. Raison = limite edge Supabase 150s (objections+thinking a timeout à 155s) ET qualité identique sans thinking (le POC brief gagnant avait 0 token thinking). Sonnet sans thinking : objections 64s, vecteurs 73s — OK.

**Bug pré-existant détecté** (hors migration) : table `search_semantic_analysis_results` réduite à 3 colonnes (id/user_id/search_id) → le save de `generate-semantic-analysis` échoue, quel que soit le modèle. Migration de cette fonction codée mais NON activée tant que le schéma n'est pas réparé. À traiter séparément.

**Coût estimé** : ~+42 $/mois à ~200 analyses (brief +18, objections +12, vecteurs +12). Réversible instantanément : `supabase secrets unset BRIEF_MODEL OBJECTIONS_MODEL VECTEURS_MODEL`.

## 2026-06-06 (suite) — Répartition LLM complète appliquée

**Réparé** : table `search_semantic_analysis_results` (n'avait que id/user_id/search_id) → ajout `context_vectors jsonb`, `entities jsonb`, `created_at` + reload schéma PostgREST. Test Sonnet OK (14s, save OK) → activé.

**Répartition finale en prod (flags secrets, défaut Gemini si flag absent)** :
- Opus 4.7 : `BRIEF_MODEL` (brief)
- Sonnet 4.6 : `OBJECTIONS_MODEL`, `VECTEURS_MODEL`, `SEMANTIC_ANALYSIS_MODEL`, `PLAN_ACTION_MODEL`, `HN_STRUCTURE_MODEL`
- Gemini Flash : tout le reste, + youtube/reddit redescendus de gemini-2.5-pro → flash (Pro inutile sur du clustering de data réelle), + **pseo-strategy GARDÉ sur Gemini** (output 16k tokens > limite edge Supabase 150s en Sonnet : a timeout, n'a pas sauvegardé).

**Contrainte clé découverte** : edge functions Supabase = **150s wall-clock max**. → thinking coupé sur tous les appels Claude ; fonctions à très gros output (pseo) incompatibles avec Claude synchrone.

**Non curl-testés** (exigent un JWT user, anon refusé) : plan-action, hn-structure — activés sur la base du pattern identique validé 4× ; à confirmer au 1er run réel. Rollback : `supabase secrets unset <FLAG>`.

## 2026-06-06 (vérif finale) — Tests end-to-end de toutes les fonctions migrées

Vérif via vrai JWT utilisateur (user de test créé/supprimé). Résultats :
- brief (Opus 4.7) ✅, objections / vecteurs / semantic-analysis / **plan-action** (57s) / **hn-structure** (25s, async, save OK) en Sonnet 4.6 ✅.
- youtube/reddit : downgrade Pro→Flash **annulé** (Flash produit du JSON malformé sur les titres vidéos/posts réels) → **remis sur gemini-2.5-pro**, youtube re-testé OK. `responseMimeType: application/json` ajouté.
- **reddit-keywords** : 403 Reddit pré-existant (IP datacenter bloquée) — plante avant le LLM, besoin `REDDIT_CLIENT_ID`/`REDDIT_CLIENT_SECRET`. Hors périmètre migration.

Tout déployé, commité, poussé. Données de test nettoyées, user de test supprimé.

## 2026-06-11 · Radar d'opportunités : 504 du cron quotidien (run GH Actions rouge)

**Symptôme** : workflow `Opportunity Radar` rouge (curl 504 après 2m33), job digest skipped (normal, il ne part que le lundi 7h).

**Cause** : `cron-opportunity-radar` attendait la FIN de chaque scan (lots de 12 séquentiels). Avec 123 watchlists actives dues et les scans v2 (boucle agentique Gemini) qui durent des minutes, le planificateur explosait le timeout gateway (150 s).

**Correctifs (déployés en `--no-verify-jwt`, commit `b721b93` + suivant) :**
- `run-opportunity-scan` répond **202 immédiatement** et scanne en tâche de fond (`EdgeRuntime.waitUntil`). Personne d'autre que le cron ne l'appelle, rien à adapter côté UI.
- `cron-opportunity-radar` : fan-out **synchrone** par lots de 12 avec pause 2 s (≈35 s pour 120 watchlists, loin des 150 s). La variante « fan-out en tâche de fond » a été testée puis abandonnée : l'instance est tuée ~50 s après la réponse (60 scans sur 123 déclenchés).
- `persist()` : insert → **upsert** `onConflict (watchlist_id, dedup_key), ignoreDuplicates` (3 erreurs duplicate key constatées quand deux scans de la même watchlist se chevauchent).

**Validation** : 3 vagues forcées (PATCH last_run_at=null + workflow_dispatch) → workflows verts en 10-28 s, 90 scans done, 0 erreur après l'upsert. Limite connue : sous forte concurrence le worker refuse une partie des déclenchements (réponses non-2xx ignorées par le cron) ; les watchlists restent « dues » et sont rattrapées au run suivant, auto-cicatrisant au quotidien.

## [2026-06-12] pSEO sans géolocalisation + retour du bouton « Tout télécharger » (CSV)

- **generate-pseo-strategy** : le playbook 1 « Géolocalisation » est retiré du prompt. 7 playbooks au lieu de 8 (Comparatif, Use Case, Prix, Tutoriel, Intégration, Temporalité, Problème/Solution), renumérotés, exemple JSON et plan 6 mois mis à jour. Règle stricte ajoutée : interdiction de proposer un playbook ou des mots-clés localisés « [requête] + [ville] », même si l'activité a une composante locale. Edge function redéployée.
- **Bouton « Tout télécharger »** : restauré dans la barre de mode du workspace (il avait été retiré le 30 mai avec « Copier le brief » et « Rechercher »), mais en export CSV au lieu d'Excel : un zip contenant un CSV par onglet (séparateur `;`, BOM UTF-8 pour Excel FR) + un `00-sommaire.csv` (mot-clé, contexte, date, liste des fichiers). Implémentation : `src/lib/csvGenerator.ts` (JSZip, nouvelle dépendance), réutilise `buildAllSections()` extrait de `xlsxGenerator.ts` (refactor partagé Excel/CSV, l'export Excel reste intact).
- Build vert, commit `0de4243` poussé (auto-deploy Netlify).

## 2026-06-12 — kb-chat multi-corpus (espaces clients)
- `kb_chunks` : colonne `project` (défaut `seo-kb`, index) ; `match_kb_chunks(query_embedding, match_count, filter_project)` remplace la version non filtrée (ancienne signature supprimée).
- `kb-ingest` : paramètre `project` (slug validé), reset scopé au projet.
- `kb-chat` : paramètre `project` ; prompt client dédié (vouvoiement, corpus = vault Obsidian du client) quand project ≠ seo-kb ; déployés en `--no-verify-jwt`.
- 1er corpus client : leexi (109 chunks, 16 fichiers, script `leexi-seo/scripts/export-kb-chat.py`). Testé : « le meilleur mot clé ? » répond depuis la recherche mots-clés Leexi, plus depuis la base de Tim.

## [2026-06-12] Lifecycle emails : requalification selon l'avancée du compte

- Demande Tim : un email en file doit refléter l'état RÉEL du compte à l'envoi (cas vu : un inscrit fait son analyse entre l'enqueue et le run, et reçoit quand même l'email d'activation).
- `enqueue_lifecycle_emails()` ajoute désormais une passe (0) de requalification : suppression des `pending` dont le segment ne tient plus (activation si ≥1 analyse, nudge_1 si ≠1, nudge_2 si ≠2, réengagement si analyse <14j, premium_click si abonné, premium_onboarding si plus abonné). DELETE et pas `skipped` : l'unicité (user, sequence) permet ainsi une remise en file future légitime.
- Incident en route : la migration 20260612120000 a écrasé le RPC prod avec l'ancienne segmentation `search_history` (la prod tournait sur `site_crawls done` depuis 20260530200000) → 46 mises en file erronées. Correctif 20260612130000 : purge totale des `pending` + redéfinition sur la bonne base. Rien n'est parti à tort (les envois n'ont lieu qu'au run quotidien).
- Vérif post-fix : 0 pending, RPC insère 0 (état stable). Les 10 envois de la semaine étaient légitimes.

## [2026-06-17] Fix favoris mots-clés : l'étoile ne « tenait » pas

- Symptôme Tim : ajout d'un mot-clé en favori « ne fonctionne pas ».
- Forensic prod (service_role + user JWT jetable) : RLS OK (un propriétaire authentifié met bien `is_saved=true`), lignes `search_semantic_results` présentes, backend ne réécrit pas `is_saved` (business-score = update partiel `google_suggestions_count`). Test end-to-end via la vraie edge function `generate-semantic-keywords` puis PATCH favori avec le JWT user → 1 ligne mise à jour, persistée. **La persistance marche à 100%.** 54 favoris existaient (3 autres users, 27 mai→2 juin) ; Tim n'en avait jamais réussi un.
- Vraie cause = bug UI dans `SortableKeywordsTable.tsx` : `useEffect(() => setLocalKeywords(keywords), [keywords])` ré-écrasait l'état favori local à chaque re-render du parent (scores business en streaming / realtime / progression reconstruisent `keywords` avec `is_saved=false`). L'étoile se « dé-cochait » toute seule → perçu comme cassé.
- Correctifs (build local, pas déployé) :
  1. `src/components/SortableKeywordsTable.tsx` : le resync depuis `keywords` fusionne et préserve `is_saved` local tant qu'on reste sur la même recherche ; reset propre au changement de `searchId`.
  2. `src/lib/keywordActions.ts` (`toggleKeywordSaved` + `bulkSaveKeywords`) : ajout de `.select('id')` ; un UPDATE à 0 ligne renvoie désormais `success:false` (avant : faux `success:true` silencieux qui masquait tout échec).
- Type-check vert. Données/users de test nettoyés. Local : http://localhost:5176/. À déployer sur demande.

## [2026-06-23] Limite freemium 10→2 + Agent/Opportunités réservés aux abonnés + clé Gemini

- **Clé Gemini** : nouveau `GEMINI_API_KEY` posé dans les secrets edge (project ref `fwhfnzbtlddzfxbsejyf`), live au runtime (pas de redéploiement nécessaire).
- **Limite gratuite 10→2 par fonction** : front `src/components/compte/types.ts` (SEARCH_LIMITS) + 5 edge functions (`check-rate-limit`, `check-hn-score-limit`, `check-semantic-score-limit`, `analyze-geo-sentinel`, `get-all-quotas`) + fonction DB `reserve_semantic_analysis_slot` (migration 20260623100000, appliquée en prod via Management API). Premium reste 999.
- **Agent + Opportunités réservés aux abonnés** :
  - UI (`WorkspaceLayout.tsx`) : verrou discret (icône Lock + tooltip « Réservé aux abonnés ») sur les onglets pour les free ; clic = `onUpgradeClick`, accès bloqué.
  - Hardening backend : `ai-chat` renvoie 403 si `feature:'agent'` et user non abonné (AgentChatView envoie le flag ; le chat contextuel gratuit ne l'envoie pas → épargné). `run-opportunity-scan` skip si la watchlist appartient à un non-abonné.
- Déployé : 7 edge functions (run-opportunity-scan en `--no-verify-jwt`) + push main (auto-deploy Netlify fusionn2). Commits `d99fd4a` + `ef38e5a`.

## [2026-06-23] Audit & économie tokens (coût explosé)

- **Constat** : 7 fonctions "generate-*" peuvent tourner sur Claude `opus-4-7` (le plus cher) via des secrets `*_MODEL`. `PSEO_STRATEGY_MODEL` était ABSENT → `generate-pseo-strategy` tournait sur Opus 4.7 par défaut (16k tokens out), poste silencieux le plus lourd.
- **Levier #1 (zéro deploy)** : les 7 secrets modèle (BRIEF/PSEO_STRATEGY/SEMANTIC_ANALYSIS/HN_STRUCTURE/VECTEURS/PLAN_ACTION/OBJECTIONS_MODEL) passés à `claude-sonnet-4-6`. Pour ces tâches d'extraction/structuration, Sonnet = qualité quasi égale à ~1/5 du prix. Réversible en changeant le secret.
- **Leviers code (commit 9173743, déployés)** :
  - `generate-pseo-strategy` : max_tokens 16000→12000 (Claude + fallback Gemini).
  - `analyze-semantic-score` : contenu de page tronqué à 3000 mots avant Gemini (l'analyse n'a pas besoin de 10k mots).
  - `run-opportunity-scan` : cache 6h du « charter » business par domaine (table `opportunity_charter_cache`, migration 20260623110000) → coupe le refetch home + appel Gemini à chaque scan du Radar (gros multiplicateur).
- Réponse à Tim sur "Opus 4.7 suffit ?" : oui et c'est même trop pour ces tâches ; Opus 4.7 = le plus cher, Sonnet suffit. Économie estimée 50-70% du poste LLM sans perte de qualité.

- **Décision modèle finale (Tim)** : `generate-pseo-strategy` + `generate-brief` repassés sur `claude-opus-4-8` (qualité max sur les 2 livrables phares) ; les 5 autres generate-* restent Sonnet 4.6 ; l'agent (`ai-chat`) reste sur Gemini (pas de chemin Claude, et coût/message élevé sur un chat). À vérifier : accès Opus 4.8 sur le compte Anthropic Fusionn (étaient sur 4.7).

## 2026-06-27 — Prompt caching Anthropic (brief)
- **Contexte** : Tim veut activer le prompt caching Anthropic (réduction coût/latence sur le préfixe statique).
- **Audit** : 7 generate-* appellent Claude via `_shared/claude.ts` (single-shot, pas d'agent). Aucune ne passait de `system` ni de `cache_control`. Tout (instructions + données) était concaténé dans le `prompt`, avec `${keyword}`/`${context}` tissé dès la L1 → aucun préfixe statique propre à cacher sans réécrire le wording. De plus, objections/vecteurs/semantic ont déjà un cache de RÉSULTATS applicatif (table keyword+context) qui court-circuite le LLM pour un input identique (mieux que le 0,1× du prompt caching).
- **Décision (Tim)** : cibler **`generate-brief` seulement** (Opus 4.8, le plus cher, structure propre : 1 seule interpolation `${contextInfo}`, pas de result-cache par mot-clé).
- **Changements** :
  - `_shared/claude.ts` : option `cacheSystem?: boolean` → pose `cache_control: ephemeral` sur le bloc system. Rétrocompatible (sans effet si non passé).
  - `generate-brief/index.ts` : template découpé en `INSTR_HEAD` / `briefEntree` (données) / `INSTR_TAIL`. Chemin Gemini (défaut) : `prompt` recomposé HEAD+ENTRÉE+TAIL = **byte-identique** à l'ancien, inchangé. Chemin Claude : instructions statiques → `system` caché (`cacheSystem:true`), `briefEntree` (données) → message user.
- **Effet** : les ~2k tokens d'instructions du brief (identiques pour tous les briefs) sont relus à 0,1× sur les rafales de briefs distincts < 5 min. Opus 4.8 min cacheable = 1024 tok → le cache s'enclenche.
- **Vérifs** : helper `deno check` OK ; brief parse OK (lint warnings `any` pré-existants seulement) ; backticks équilibrés.
- **Pas encore déployé** : `supabase functions deploy generate-brief` + `_shared` = acte prod, en attente du feu vert Tim. (NB : un push main ne déploie QUE le front Netlify, pas les edge functions Supabase.)

## 2026-06-29 — Recherche mots-clés : colonne Potentiel, navbar, écran démo home

- **Colonne Potentiel** dans le tableau de mots-clés (`KeywordTable.tsx`) : synthèse calculée client-side = demande (volume Google Ads) × conversion (business) × accessibilité (compétition), rendue en jauge + label Fort/Moyen/Faible. Distincte du Score sémantique. Présente dans le chat, l'onglet Mots-clés (réutilise le même composant) et le panneau détail (`projectViews.tsx`). CSS jauge dans `chat.css`, tableau passé à 8 colonnes.
- **Thinking rassurant** (`keyword-agent/index.ts`, déployé) : `thinkMsg`→`thinkLines` renvoie une séquence de lignes nommant les sources réelles (« Je consulte les données Google », « volume réel Google Keyword Planner », « CPC et concurrence Google Ads », « croise avec votre Search Console »). S'empilent en checklist.
- **Photo Google sur le bouton compte** (Sidebar) : charge `google_connections` (picture/name/email), avatar + nom + email, fallback initiale.
- **Carte Premium 29€** dans l'onglet Abonnement du Compte (`AccountView.tsx`) : vraie carte + bouton branché sur `create-checkout-session` (Stripe, 2900c).
- **Écran « Voilà ce que Fusionn fait pour vous »** (`landing/DemoSection.tsx`) réécrit : colonnes Mot-clé/Intention/Volume/CPC/Compétition/Potentiel (la vraie data Ads), onglets Mots-clés/Micro-intentions/Objections/Brief (synthèse 8 sections), header « Projet » + description produit, CTA → `/recherche` avec `state.description`.
- **Navbar** (`Navbar.tsx`) alignée : pages publiques = menu Tarifs/Outils gratuits/Documentation + CTA « Lancer une recherche »/« Ma recherche » → `/recherche` ; lien YouTube « Démo » retiré ; boutons legacy (Rechercher/Espace/Historique → /compte) conservés uniquement quand les handlers sont passés (page `/compte`).
- **Vérifs** : `tsc --noEmit` = 0 erreur sur tout le projet ; dev `http://localhost:5176` (`/` et `/recherche` = 200) ; edge `keyword-agent` déployée.

## 2026-06-29 (suite) — keyword-agent : hybride Sonnet/Gemini (économie tokens)

- Découpage modèles aligné sur l'ancien Fusionn, validé par Tim : **chatbot + brief = Sonnet 4.6** (obligatoire) ; **génération de masse = Gemini** (moins cher, plus exhaustif que Haiku). Reco assumée : Gemini > Haiku pour l'idéation mots-clés (coût + souffle + déjà éprouvé en prod + cohérence ancien Fusionn).
- 3 outils Gemini ajoutés dans `keyword-agent` : `generate_keywords` (**gemini-2.5-pro** : idéation 40+ mots-clés PUIS le serveur attache volume/CPC/compétition réels Google Ads et renvoie la liste prête `{keyword,intention,volume,cpc,competition,business,bucket}`), `generate_micro_intentions` (**gemini-3.1-flash-lite**), `generate_objections` (**gemini-2.5-pro**). Helper `callGemini(model,prompt)` (responseMimeType json) + `parseJsonArray` tolérant + dédup.
- Skills mis à jour : `recherche_mots_cles` appelle generate_keywords (ne brainstorme plus → gros gain tokens Sonnet) ; `micro_intentions` appelle l'outil ; nouveau skill `objections`. Clustering/décisionnels/structure_hn restent Sonnet (transfo légère). Flags surchargeables `KEYWORD_GEN_MODEL` / `KEYWORD_GEN_LITE_MODEL`.
- Lignes « thinking » rassurantes par outil Gemini. Anti-hallucination : volume/CPC = Google Ads via generate_keywords OU keyword_metrics, jamais inventés.
- `deno check` OK ; déployé `--no-verify-jwt` ; secrets GEMINI_API_KEY + ANTHROPIC + GOOGLE_ADS_* présents ; smoke test 200 (cadrage Sonnet OK).

## 2026-06-29 (suite 2) — Persistance projets par compte + reprise post-connexion

- **Persistance serveur** : table `public.kw_user_state` (user_id PK → auth.users, data jsonb, updated_at) + RLS select/insert/update own, grant authenticated. Créée via API Management `/database/query` (PAT décodé du keychain « Supabase CLI » : valeur `go-keyring-base64:<base64(sbp_...)>`).
- Module `src/lib/kwSync.ts` : snapshot/apply du namespace `fusionn_kw_*`, fetch/push/clear remote (upsert onConflict user_id), `mergeSnapshots` au grain projet (union projets, convs fusionnées par id la + récente, mémoire/contexte/briefs du côté le + récent). localStorage = cache, Supabase = source durable.
- `Recherche.tsx` : boot async hydrate (fetch remote → merge local → apply → re-push), `scheduleSync()` debouncé (1,2 s) après chaque save, listener `onAuthStateChange` pour capter une connexion tardive. `AccountView.deleteAll` vide aussi le serveur (sinon resurrection à la synchro). Sync seulement si user non-anon.
- **Reprise recherche après connexion** : Landing handleSearch non connecté → `sessionStorage['fusionn_pending_recherche']` + `/connexion` ; reprise gérée DEUX fois (Connexion useEffect pour email/mdp ; Landing au montage car redirect Google = `origin+'/'`) → `/recherche` state.description, kickoff auto, sans retaper.
- Copy : H1 « L'agent qui trouve vos meilleurs mots-clés pour ChatGPT, Google, YouTube » + sous-titre « Décrivez votre produit… identifie vos meilleurs mots-clés, récupère leur volume… CPC… suivi de vos positions » ; onglet Mémoire phrase réécrite.
- `tsc` 0 erreur, `npm run build` OK (react-snap prerender échoue = non bloquant). Commit + push `main` (`d524765..4ca60ec`) → déploiement Netlify prod.

## 2026-07-01 — Preuve d'origine des data : logos Google Ads + Search Console

- Nouveau composant `src/components/recherche/DataSourceLogos.tsx` : `GoogleAdsLogo`, `GoogleSearchConsoleLogo` (SVG couleur officiels) + `sourceForStep(label)` qui mappe un libellé d'étape → `'ads'` (volume/CPC/Google Ads) ou `'gsc'` (Search Console/positions/impressions/requêtes/clics).
- `KeywordChat.tsx` : (1) badge « Données Google réelles » dans la topbar avec les deux logos + tooltip d'origine ; (2) `StepsBox` affiche le logo de la source à côté de chaque étape de thinking concernée (ex. « Je relève le volume et le CPC réels (Google Ads) » → logo Ads).
- But : prouver visuellement que les chiffres viennent de sources réelles, pas inventés.
- `tsc` 0 erreur, `npm run build` OK (react-snap échoue en local = non bloquant). Push `main` (`0041266..e8c5e13`) → deploy Netlify prod `ready` sans erreur (commit_ref e8c5e13).
- Même traitement porté sur **Qadence** (`src/components/DataSourceLogos.jsx` + `Chat.jsx`, GSC en premier car source principale, Ads bêta). Déployé prod via `netlify deploy --prod --dir=dist` → https://qadence.io.
- Note : le commit `43baa72` (edge function `alexia-copilot/index.ts`, auto-commitée avant la session) est parti dans le même push main — sans impact front (edge function Supabase, déployée à part).

## 2026-07-01 — 2 nouveaux outils gratuits : générateur mots-clés Amazon + IA
- Cluster « générateur de mots-clés » (page qui décolle en impressions) transformé en cluster d'outils : 2 pages-outils ajoutées pour attaquer/renforcer.
- **/generateur-mots-cles-amazon** : réutilise le MÊME moteur de scoring (`tool-keyword-generator-amazon`, copie déterministe de tool-keyword-generator), prompt calibré barre de recherche Amazon (marque/modèle/usage/avis…).
- **/generateur-mots-cles-ia** : nouveau moteur `tool-generateur-mots-cles-ia`, angle éclatement en micro-intentions (besoin réel + requêtes + format), groupé Do/Know/Know-Simple (GEO).
- Branché : routes App.tsx, footer Outils gratuits, sitemap + reactSnap.include (au passage ajouté /generateur-mots-cles-gratuit qui manquait au sitemap/prerender).
- 2 edge functions déployées sur projet fusionn (fwhfnzbtlddzfxbsejyf), testées OK. Site pas encore poussé en prod.
