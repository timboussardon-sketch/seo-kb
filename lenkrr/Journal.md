# lenkrr : Journal de développement

## En résumé (au 2026-06-02)

**lenkrr** est le nouveau produit né du pivot de Qadence : un SaaS qui analyse le maillage interne d'un site puis applique les liens lui-même, en exécutant la doctrine des skills `maillage-interne-gsc` et `maillage-systeme`. La doctrine qu'il met en code, c'est le [[concepts/maillage-systeme]] ; vue d'ensemble dans [[moc/moc-maillage]].

État : **Phases 0, 1, 2 et 3 terminées et committées**. Le repo tourne en local sur http://localhost:3000, en accès direct. Chaîne complète : connecter un site (WordPress ou Git) → analyser (architecture en piliers + hubs, intentions, audit orphelines/dead-ends) → plan de liens priorisé (score d'urgence + 3 ancres + passage, ancres affinées par Gemini via l'edge function `lenkrr-anchors` déployée sur le projet Qadence). Prochaine étape : Phase 4 (write-back gated : appliquer les liens en révision WordPress / Pull Request Git). C'est la phase outward-facing à valider explicitement avec Tim avant de coder l'application réelle.

Repo : `/Users/timothee/Code/lenkrr`. Plan détaillé : `~/.claude/plans/staged-whistling-engelbart.md`.

---

## Décisions produit (cadrées avec Tim)

- SaaS multi-tenant, deux audiences : no-tech (web app guidée) et tech (serveur MCP, plus tard).
- Connecteurs multi dès le départ : WordPress (REST API) + repo Git (Next.js / MDX), derrière une interface commune `SiteConnector`.
- Stack : Next.js 15 + React 19, Supabase (Auth + Postgres + Edge Functions Deno), Gemini.
- Lecture du site : API du CMS + [[entities/gsc]] par-dessus (comportemental).
- Profondeur : application auto des liens, mais derrière une porte d'approbation groupée (sur Git, la PR fait office de porte).
- Onboarding WordPress : plugin maison + application password (les deux).
- Comptes multi-tenant en v1, facturation Stripe après validation.
- MCP plus tard, mais socle API-first donc MCP-ready.
- Design validé : minimaliste, ultra accessible. Tokens gris/blanc portés de Qadence.

## Infra

- Supabase : réutilise le projet de Qadence (ref `ytgbnqqmcnhmscbvhoin`, alias `api.qadence.io`).
- Conséquence : les edge functions lenkrr seront préfixées `lenkrr-*` pour ne PAS écraser celles de Qadence (`google-auth`, `google-oauth-callback`, `get-gsc-sites`).
- `.env.local` câblé sur l'URL et l'anon key du projet (gitignored, non committé).
- Pour pousser les migrations sur la base partagée : lier le repo (`supabase link`, demande le mot de passe DB). Pas encore fait.
- Pour l'OAuth GSC en local : il faudra ajouter le callback de lenkrr aux redirect URIs du client OAuth Google de Qadence (manip console Google). Pas encore fait.

## Phasage et suivi

### Phase 0 : Scaffold + Auth multi-tenant. FAIT (committé)
- Next.js 15 / React 19, App Router, design system porté.
- Auth multi-tenant Supabase via `@supabase/ssr` : `middleware.ts`, `/login`, dashboard shell.
- Migration `supabase/migrations/20260602000001_init.sql` : schéma maillage (`sites`, `pages`, `pillars`, `links_existing`, `link_proposals`, `runs`) + `google_connections` / `gsc_cache`, RLS par `user_id`.
- Edge functions GSC portées (`google-auth`, `google-oauth-callback`, `get-gsc-sites`) + helpers `_shared` (`gsc.ts`, `gemini.ts`, `env.ts`). Nettoyage : URLs via env, plus de fallback user_id, scope GSC en lecture seule.
- Accès direct activé : le gate d'auth est désactivé dans `middleware.ts` (réactivable en décommentant le bloc).
- Build vert, pages 200 en local.

### Phase 1 : Connecteurs en lecture (WordPress + Git). FAIT (committé)
- Logique placée dans `lib/connectors/` (TS pur, fetch-based, portable vers edge functions ensuite), exposée via Route Handler Next.js pour être testable en local sans déploiement.
- Interface `SiteConnector` + format pivot (`PageRef`, `PageContent`) dans `lib/connectors/types.ts`.
- `WordPressConnector` (application password) : `verify`, `listPages` (posts + pages), `getPageContent`. Structurellement prêt, test live en attente de vrais identifiants WP.
- `GitConnector` (API GitHub) : `verify`, `listPages` (`.md` / `.mdx` / `.tsx` filtrés par dossier), `getPageContent`. Vérifié en local sur reactjs/react.dev (24 pages MDX listées).
- Route Handler `POST /api/connect/test` : vérifie + renvoie un aperçu, lecture seule, ne persiste rien.
- UI `/connect` : sélecteur WordPress / Git, formulaires, aperçu des pages détectées. Cartes du dashboard reliées.
- RESTE pour la Phase 1 : connexion GSC dans l'UI (bouton OAuth) + persistance du site en base. Tous deux dépendent du lien Supabase (migration poussée + fonction `lenkrr-google-auth` déployée + redirect URI Google). Reportés au branchement infra.

### Phase 2 : Moteur d'analyse (ingest + analyze 1 à 4). FAIT (committé)
- `lib/analysis/` (module pur, exécutable en local) : `urls.ts` (normalisation), `links.ts` (extraction de liens HTML + Markdown/MDX/JSX, comptage de mots), `classify.ts` (intentions par signaux de titre / URL + piliers heuristiques par segment d'URL ou clustering de tokens), `engine.ts` (orchestration : lecture des contenus en concurrence limitée, graphe inbound / outbound, désignation des hubs, BFS profondeur de clic, détection orphelines / dead-ends / hubs sous-maillés).
- Résolution des liens : URL normalisée exacte + fallback par slug (rattrape le préfixe de route des sites Git).
- Route `POST /api/analyze` + composant `AnalysisPanel` (blocs 1 « Architecture détectée » et 2 « Audit du graphe » de la doctrine). Bouton « Analyser le maillage » dans `/connect`.
- Vérifié en local sur react.dev/learn : 52 pages, 87 liens internes, 3 piliers, hubs et audit cohérents.
- LIMITES connues (à améliorer) : intentions et piliers heuristiques (affinage par Gemini prévu) ; profondeur de clic limitée au sous-ensemble analysé ; analyse plafonnée à 100 pages ; reconstruction d'URL Git imparfaite (atténuée par le fallback slug). Persistance en base toujours en attente du lien Supabase.

### Phase 3 : Propositions de liens + UI revue. FAIT (committé)
- `lib/analysis/propose.ts` : liens manquants selon les priorités de la doctrine (fix orphelines, Know→Do, satellite→hub, cross-pillar), score d'urgence (poids intention + gain authority), priorité haute/moyenne/faible, dédup vs liens existants. Vérifié sur graphe synthétique.
- Edge function `supabase/functions/lenkrr-anchors` (déployée sur le projet Qadence, namespacée) : 3 ancres + passage par lien via Gemini (`gemini-3.5-flash`), selon les 5 critères d'ancre. Vérifiée en direct, sortie conforme (exact/partial/sémantique + passage naturel).
- `/api/analyze` fusionne les ancres Gemini dans les propositions, repli heuristique si indispo.
- `AnalysisPanel` : bloc 3 « Plan de liens à créer » (priorité, score, source→cible, nature, 3 ancres, passage, justification).
- NOTE modèles Gemini : la clé du projet ne connaît pas `gemini-3.1-flash` (nom Qadence) ; on utilise `gemini-3.5-flash`. Branche debug `{"list":true}` dans la fonction pour relister.
- NOTE rate limit : l'analyse Git non authentifiée tape la limite GitHub (60/h) ; le champ Token de l'UI lève à 5000/h.
- RESTE transverse (toujours en attente du lien Supabase) : persistance en base (sites/pages/proposals), connexion GSC dans l'UI, connecteur WordPress testé en live.

### Phase 4 : Write-back gated. FAIT côté Git (committé) — WordPress à venir
- Edge function `lenkrr-insert-link` (déployée) : Gemini choisit le paragraphe hôte EXISTANT et le réécrit a minima pour intégrer le lien ; renvoie l'original verbatim + la version modifiée + l'ancre choisie ; `skip` si hors-sujet. Vérifiée en direct : bon paragraphe, ancre exacte, insertion markdown propre, diff 1 paragraphe.
- `GitConnector.applyEdit` : branche `lenkrr/<slug>` + commit du fichier patché + ouverture de PR (jamais de merge auto). Exige un token GitHub en écriture.
- `/api/apply` : lecture source → insert-link → **remplacement EXACT** (refuse d'écrire si le paragraphe d'origine n'est pas retrouvé tel quel, sécurité anti-réécriture) → PR.
- `AnalysisPanel` : bouton « Appliquer (PR) » par proposition (sites Git), lien vers la PR ouverte.
- **Connecteur `nextdata` construit** (pour Organikk) : `lib/connectors/github.ts` (client GitHub partagé), `nextdata-parse.ts` (parseur du Record d'articles, brace-matching respectant les strings), `NextDataConnector` (une entrée = une page ; applyEdit réécrit le champ `content` avec échappement du quote TS + PR). Parseur vérifié sur le vrai `articles.ts` : 19 articles, 36 liens internes, **671/671 paragraphes verbatim**. Onglet UI « Next.js (data) » ajouté.
- **Coordonnées Organikk** : repo `timboussardon-sketch/organikk-next`, branche `main`, fichier `src/data/articles.ts`, préfixe route `blog`, site `https://organikk.co`. Repo **privé** (404 sans token).
- **TEST RÉEL ORGANIKK VALIDÉ (2026-06-03)** : sur le site de [[entities/organikk-co]], token classique fourni → analyse `organikk-next` (19 articles, 35 liens internes, 3 orphelines, 2 piliers, 25 propositions toutes enrichies Gemini) → PR #4 ouverte avec lien markdown relatif correct `[ancre](/blog/audit-seo-claude)`, 1 paragraphe modifié, TS valide (quotes équilibrées), branche dédiée, jamais de merge auto. À relire/merger par Tim.
- **2 bugs trouvés et corrigés par le test réel** : (1) `ECONNRESET` réseau sur les gros PUT GitHub → `fetchRetry` (retry transitoire) dans le client GitHub ; (2) Gemini insérait parfois le TEXTE de l'ancre sans la syntaxe markdown `[..](..)` → garde-fou dans `/api/apply` qui refuse la PR si le lien n'est pas réellement présent, + insertion en chemin relatif + prompt durci.
- **Persistance réparée (2026-06-03)** : le `saved:False` avait 2 causes empilées — (1) `sites.type` rejetait `nextdata` (contrainte `check` élargie via migration `20260603000001`) ; (2) l'insert du run tombait sur `fetch failed`/ECONNRESET, le client Supabase ne réessayait pas → `admin` client configuré avec un `fetch` à retry. Analyse Organikk désormais persistée en entier (site + run + 20 pages avec intent/inbound/statut + 26 propositions). Reste : write-back WordPress (révision) pas encore implémenté.

### Persistance : LIVE (2026-06-03)
- `supabase link` fait par Tim, `supabase db push` appliqué : les 6 tables lenkrr existent. Analyse react.dev/learn persistée (52 pages + propositions, site + run créés). Persistance best-effort confirmée de bout en bout.

### Phase 5 : WordPress write-back + onboarding guidé. FAIT (committé) — plugin reporté
- **Write-back WordPress** : `WordPressConnector.applyEdit` lit `content.raw` (context=edit, pour ne pas casser Gutenberg), remplacement exact, met à jour le post (WordPress enregistre une révision = réversible), renvoie l'URL d'édition. `getPageContent` passe aussi en `content.raw`. Validation du lien dans `/api/apply` étendue au HTML `href=` (pas que markdown). UI : application autorisée pour WP, libellés « Appliquer (révision) » / « Post mis à jour ». Helper `lib/net.ts` (fetchRetry).
- **Onboarding guidé** (décision Tim : pas de plugin PHP) : guide repliable dans l'onglet WordPress, 5 étapes pour créer un application password + lien profond profil WP + bouton « Générer via WordPress » (`authorize-application.php` natif). Design minimaliste vérifié en capture.
- **NON testé en live** (pas de WP de test fourni) : à valider comme Git/Organikk dès qu'un WordPress + application password est dispo. Plugin PHP reporté à ce moment-là.

### Phase 6 : Suivi d'impact + ouverture MCP / Stripe. EN COURS
- **Serveur MCP : FAIT (committé)** — `mcp/` (package isolé, `@modelcontextprotocol/sdk`, stdio) expose 2 outils mappant l'API lenkrr (API-first) : `lenkrr_analyze_internal_linking` (lecture seule) et `lenkrr_apply_link` (PR Git / révision WP, gated). `LENKRR_API_URL` configurable. README (config Claude Code/Desktop/Cursor) + `test-client.mjs`. Vérifié end-to-end : client MCP → analyse Organikk (20 pages, 37 liens, 26 propositions).
- **Suivi d'impact : edge function FAITE (committée, déployée)** — `lenkrr-impact` compare position/CTR/clics/impressions d'une page sur 2 fenêtres GSC (avant/après pose du lien) via `fetchGSC`. NON testable en live : tous les tokens de `google_connections` sont révoqués (401 partout, ré-autorisations Qadence successives). Débloquer = ajouter le redirect URI `https://ytgbnqqmcnhmscbvhoin.supabase.co/functions/v1/lenkrr-google-oauth-callback` aux URI autorisés du client OAuth Google (console Google Cloud, même client que Qadence), puis re-connexion GSC fraîche. Ensuite : wiring du bouton « Connecter GSC » + affichage impact dans l'UI.
- **Stripe** : bloqué sur décisions pricing + déploiement.

## Consolidation transverse (2026-06-03) — EN COURS, partiellement bloquée

- Fonctions GSC renommées et **déployées** sur le projet Qadence : `lenkrr-google-auth`, `lenkrr-google-oauth-callback`, `lenkrr-get-gsc-sites` (+ `lenkrr-anchors`). Aucun impact sur Qadence (noms distincts).
- Migration rendue **strictement additive + idempotente** : ne recrée pas `google_connections` / `gsc_cache`, ne touche pas à leur RLS. FK vers `auth.users` retirées (tolère le mode « compte unique »). Unique `sites(user_id, base_url)`, colonnes titres sur `link_proposals`.
- **Décision identité : « compte unique moi »** (pas de login à l'écran). `user_id` fixe = `49d9b314-fae2-4e9a-8bbd-f2d71c051a56` (un des comptes de Tim, posé dans `.env.local` via `LENKRR_USER_ID`). Persistance serveur via clé **service-role** (bypass RLS) dans `lib/supabase/admin.ts` + `lib/db/persist.ts`, câblée best-effort dans `/api/analyze`.
- **BLOCAGE** : pousser la migration (`supabase db push`) exige le **lien au projet** = mot de passe DB (non récupérable via CLI ; la Management API a refusé le token CLI). Tant que la migration n'est pas poussée, la persistance est un no-op silencieux (le flux stateless marche).
- **Action attendue de Tim** : `! cd /Users/timothee/Code/lenkrr && supabase link --project-ref ytgbnqqmcnhmscbvhoin` → ensuite `supabase db push` + persistance live.
- **Manips Tim restantes (non bloquantes)** : ajouter `https://ytgbnqqmcnhmscbvhoin.supabase.co/functions/v1/lenkrr-google-oauth-callback` aux redirect URIs du client OAuth Google (console Google) pour la GSC ; fournir un site WordPress + application password pour tester ce connecteur en live.

## Connexion simplifiée + moteur fidèle aux skills (2026-06-03)

- **Connexion repensée (Tim : « tu demandes trop d'infos »)** : « Se connecter avec GitHub » (OAuth, routes `/api/github/*`, token stocké en `github_connections`, injecté dans analyze/apply) + auto-détection du repo (type git/nextdata, dossier, branche, URL). Onglet « Next.js » supprimé. **Prouvé en réel** : Tim connecte GitHub → choisit organikk-next → auto-détection → analyse, zéro champ. GitHub OAuth App créée par Tim (creds dans `.env.local`). WordPress URL-seule (flux natif) : à faire.
- **Moteur de propositions réécrit fidèle aux 2 skills** (Tim : « pixel perfect respecter les 2 skills ») : Hub→Satellite (priorité #1 « activer le cocon »), fix dead-ends (≥2 sortants, était absent), conservation garantie (orphelines/hub≥5/dead-ends), Know-décisionnel=0.8, jamais de lien vers la home, densité 2-5/1000 mots, 1 seul exact match par cible + diversification propagée à l'application, money page (Do) = ~10 entrants tolérés. Fin de la cannibalisation d'ancre constatée sur Organikk (money page 8 liens / 1 exact).
- **Couverture complète FAITE** : analyse via **crawl du sitemap** (`lib/analysis/crawl.ts`, type `crawl` dans `/api/analyze`, cœur `buildReport` partagé). Vérifié sur organikk.co : **134 pages** (vs 20), 534 liens internes, 5 piliers. Le flux GitHub crawle tout le site dès que l'URL publique est renseignée.
- **Write-back multi-sources FAIT** : détection fiable par scan des routes `src/app/<prefix>/[slug]/page.tsx` (mapping préfixe→fichier lu depuis les imports). `NextDataConnector` multi-sources résout une URL crawlée vers le bon fichier de données et édite le bon paragraphe. **Prouvé** : PR sur `/strategies/` édite bien `strategies.ts`. Marche pour les 5 fichiers au format Record+paragraphes (articles/newsletter/strategies/news/pages).
- **LIMITE wiki** : `wiki.ts` = tableau de concepts avec maillage par arrays `related[]`/`articles[]` (pas de paragraphes markdown). Write-back wiki = adaptateur dédié (ajout de slug dans un array), non couvert. Analyse OK (crawl), écriture non.

## Suivi d'impact GSC (2026-06-03)
- `lenkrr-impact` (edge function) déployée, mesure avant/après. Callback OAuth GSC corrigée (`--no-verify-jwt` + diagnostic d'erreur). Le token frais n'a pas été stocké malgré le « ça fonctionne » de Tim (échange de token échoue, cause exacte non encore identifiée — la callback remonte maintenant l'erreur Google précise). Test impact toujours bloqué tant qu'un token GSC frais n'est pas stocké sous `LENKRR_USER_ID`.

## Parcours d'entrée + landing DA (2026-06-04)
- Commit `4d3dcb4` : parcours d'entrée complet + landing en direction artistique + formalisation du design system (`docs/design-system.md`). Connecteur WordPress repensé (`components/WordPressConnect.tsx`, `lib/wordpress-auth.ts`, `lib/wordpress-provision.ts`), embeddings de pages (`lib/analysis/semantic.ts`, edge function `lenkrr-embeddings`, migrations `wordpress_connections` + `page_embeddings`).

## Consolidation : merge sur master (2026-06-06)
- **Branche `feat/wordpress-et-maillage-agentique` (5 commits) mergée sur `master` et poussée** (`c744c63`). Build de prod vert : 25 routes dont 17 API, middleware 89.8 kB.
- Les callbacks OAuth (`app/api/github/*`, `app/api/wordpress/*`) utilisent `${origin}` dynamique : ils s'adaptent au domaine de prod automatiquement, pas de hardcode localhost.
- 6 env vars requises pour tourner : `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `LENKRR_USER_ID`, `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET`.
- **Déploiement public : NON fait, décision de Tim « nulle part pour l'instant »** (pas de domaine lenkrr réservé). Quand on déploiera, il faudra : choisir l'hébergeur (Netlify pour rester homogène avec Fusionn/Organikk), câbler les 6 env vars, et ajouter le callback de prod `<domaine>/api/github/callback` au client OAuth GitHub (un OAuth App classique n'autorise qu'une seule callback URL → soit on bascule l'URL, soit on crée une 2e OAuth App pour la prod).

## Diagnostic flux GSC refait de bout en bout (2026-06-06) — DÉBLOQUÉ
Refait tout le flux OAuth + impact étape par étape pour localiser le blocage supposé. Conclusion : **plus rien ne bloque, le journal du 03/06 était périmé.**
1. **lenkrr-google-auth** : génère l'URL de consentement correcte. `redirect_uri = https://ytgbnqqmcnhmscbvhoin.supabase.co/functions/v1/lenkrr-google-oauth-callback`, client_id `309434449968-...`, scopes webmasters.readonly + userinfo.
2. **Test redirect_uri** : faux code envoyé au callback → Google répond `invalid_grant: Malformed auth code`, **PAS** `redirect_uri_mismatch`. Donc l'URI **est** bien inscrite dans le client OAuth Google. La manip console qu'on croyait manquante était déjà faite. L'hypothèse « callback local » était fausse : le redirect Google passe par l'URL publique Supabase, jamais par localhost (localhost = seulement `frontendUrl()`, le renvoi navigateur en toute fin, inoffensif).
3. **Stockage** : 28 lignes dans `google_connections` pour `LENKRR_USER_ID`, refresh_token présent partout, email tim.boussardon@gmail.com. La persistance marche.
4. **Refresh de token** : `lenkrr-get-gsc-sites` renvoie la liste fraîche de toutes les propriétés → le refresh fonctionne, **les tokens ne sont PAS révoqués** (contrairement au « 401 partout » du 03/06 ; Tim a dû ré-autoriser depuis).
5. **lenkrr-impact** : `ok:true` avec vraies données. golfiller.fr (pivot 06/05, ±21j) : avant 1286 clics / pos 6,3 → après 1232 clics / pos 5,6. Chaîne complète validée.
- **Note** : mesurer l'impact d'un lien posé il y a 3 jours est prématuré (GSC a 2-3j de latence + il faut une fenêtre « après » qui se remplit). Sur une page sans trafic, `found:false` est normal.
- **RESTE pour rendre l'impact utilisable dans le produit** (pas un blocage technique) : câbler le bouton « Connecter GSC » dans l'UI + afficher l'impact par proposition appliquée.

## Règle de travail

Avancer phase par phase sans rien casser : le build doit rester vert, les écrans rendre en 200, et ne jamais écraser les fonctions de Qadence sur le projet Supabase partagé.

## Historique des analyses + sites mémorisés + plein écran analyse (2026-06-06)

Trois demandes de Tim, traitées ensemble (working tree, par-dessus le refactor `components/result/` en cours qui compile). **Aucune migration** : on réutilise `sites.config` (jsonb) et `runs.output_data` (jsonb) existants.

- **Persistance enrichie** (`lib/db/persist.ts`) : `runs.output_data` stocke désormais le **report complet** (et non plus seulement `report.stats`), donc une analyse se recharge sans relancer le crawl. `sites.config` mémorise la connexion **sans secrets** (`{analyzeCfg, applyCfg}`, tokens/app passwords retirés — réinjectés serveur à chaque run/apply). Le type de site stocké vient de `applyCfg` (toujours git/nextdata/wordpress), jamais `'crawl'` : **bug corrigé** au passage — un crawl posait `type:'crawl'` qui violait la contrainte `sites_type_check`, donc les analyses crawl ne se persistaient probablement pas avant.
- **Transport applyCfg** : l'UI joint la cible de write-back via la clé `__apply` dans le body de `/api/analyze` (rétro-compatible MCP qui poste un cfg nu). Câblé dans `AnalysisContext.runAnalysis`.
- **Lecture** (`lib/db/history.ts`, client service-role + `LENKRR_USER_ID`) : `listRuns()`, `getRun(id)` (garde-fou : un vieux run sans report complet → null), `listSites()` (filtre les sites sans `analyzeCfg`), `getSite(id)`.
- **Onglet Historique** : `/app/analyses` liste les runs (date, site, pages/propositions) → `/app/analyses/[runId]` recharge le report dans `ResultWorkspace`. L'onglet « Analyses » existait déjà en placeholder.
- **Mes sites mémorisés** : `/app` liste les sites connectés (sinon Dashboard de connexion) avec « Analyser ce site » (→ `/connect?site=<id>`) + « Connecter un autre site ». Nouvelle route `GET /api/sites/[id]`.
- **Plein écran analyse** (`ConnectClient`) : dès que l'analyse tourne ou qu'un report est présent, tout le bloc de connexion (titre, sélecteur WP/GitHub, formulaire « Connecté · 1 site ») disparaît au profit du workspace ; lien « ← Analyser un autre site » pour revenir. Auto-lancement depuis `?site=<id>` (fetch config + `runAnalysis`, URL nettoyée pour éviter la relance au refresh).
- **Validé end-to-end en local** (port 3000) : `tsc` + `next build` verts ; crawl réel organikk.co (100 pages, 99 propositions) → persisté (site `nextdata` + run avec report complet + config sans secrets) → `/app/analyses/[runId]` recharge le workspace sans relancer, le run apparaît dans la liste, `/api/sites/[id]` renvoie bien `{analyzeCfg, applyCfg}` sans token.
- **Limite connue** : les runs antérieurs au 2026-06-06 ne stockaient que les stats → ils apparaissent dans la liste mais affichent « Analyse introuvable » au clic (pas de report complet à recharger). Seules les analyses lancées depuis ce changement sont rechargeables.
- **Écran Impact refait (page-centric)** : remplacé les catégories + compteurs + score abstrait (Impact/Confiance/P1/P2) par un compte rendu en **pages nommées** (`buildPagePlan`), groupées en « stratégiques à renforcer » / « orphelines à récupérer » / « culs-de-sac à corriger », chacune avec objectif métier + sources réelles (Depuis/Vers) + nombre de liens. Répond aux 3 questions du SEO (qu'est-ce qui ne va pas / quelles pages / quoi faire) en voir→comprendre→agir. Carte cliquable → Plan d'action. Icônes fonctionnelles plutôt que les émojis du brief, pour rester dans le design system gris/blanc.
- **Codemod icônes** : tout le repo a migré de `lucide-react` vers `@phosphor-icons/react/ssr` pendant la session (mes fichiers alignés dessus).
- **Commité sur `master`** : `bda3587` (build + tsc verts). Le commit regroupe la feature historique/sites/plein écran + l'Impact page-centric + le refactor `components/result/` qui était en cours + le codemod phosphor (tout intriqué, validé par Tim « ok »).

## Espace de travail à onglets + audit sémantique (2026-06-06)

Virage produit : passer d'un rapport en 3 étapes à un **espace de travail permanent à onglets**, chaque onglet = une responsabilité. Modèle cible : **IA explique → IA détecte → IA propose → Humain valide**.

- **Workspace à onglets** (`SiteWorkspace.tsx`, remplace `ResultWorkspace`) : sidebar verticale gauche (Dashboard / Audit / Opportunités / Pages / Architecture / Déploiement), état des décisions partagé entre onglets (onglets côté client). Réutilisé après analyse ET depuis l'Historique. Historique reste dans la nav globale.
- **Dashboard graphique** (`DashboardView.tsx`) : graphiques SVG maison, zéro dépendance (jauge de score avant/après, donut santé des pages, barres intentions, histogramme liens entrants, barres clusters, avant/après du plan).
- **Plan d'action** itéré 3× (« illisible ») : stepper → maître-détail → tableaux → **cartes par page** (conclusion d'abord : page + statut + +N liens + « pourquoi » + Valider ; tableau de liens replié derrière « Voir les recommandations détaillées »).
- **Transparence des signaux** (`explainProposal` dans `lib/maillage.ts`) : chaque lien expose la règle du skill (Hub→Satellite, Know→Do…), le cosinus, l'intention cible (+poids), l'autorité source, le score. Le cosinus n'est QU'UN signal ; on montre tout le calcul de `propose.ts`.
- **Audit sémantique** : embeddings calculés à CHAQUE analyse (avant : repli seulement). `engine.ts` exporte un bloc `semantic` (cohésion/cluster, pages mal classées, quasi-doublons cosinus>0,9, clusters sans hub) + une `explanation`. Onglet Audit = incohérences ; Architecture = explication + cohésion.
- **Explication rédigée par l'IA** : edge function `lenkrr-explain` (Gemini `gemini-3.5-flash`, déployée sur le projet Qadence), ancrée sur les faits calculés (zéro chiffre inventé), appelée dans `/api/analyze` avec **repli auto** sur `computeExplanation` si le LLM échoue.

### RÈGLE GÉNÉRALE du crawl (correctif)
- **Bug (trouvé par Tim)** : page wiki « Fully Meets » marquée orpheline alors qu'elle a du maillage (« Concepts voisins », « Aller plus loin »). Cause : `crawl.ts` ne gardait que le **premier `<main>`/`<article>`** (regex non-greedy) → 3 liens sur 61, maillage hors `<main>` perdu, fausses orphelines en masse.
- **Règle posée** (`stripChrome` dans `lib/analysis/crawl.ts`) : on NE restreint plus au `<main>`. On retire le chrome (`script/style/head/header/nav/footer`) et on garde tout le reste. L'audit compte **tous les liens internes éditoriaux** (y compris « Concepts voisins » / « Aller plus loin » / « Voir aussi ») ; les liens de nav répétés survivants sont écartés par le filtre template (>50 % des pages). Vaut pour **tout site crawlé**.
- **Validé** : « Fully Meets » repasse en `ok` (4 entrants / 7 sortants), orphelines 21 → 14, 532 liens internes capturés. Run `435fe8de`.

### À COMMITTER
- Tout ce bloc est **non commité** (build + tsc verts). La feature historique/sites du début de session est déjà dans `bda3587`. Edge `lenkrr-explain` déjà déployée.
- Seules les analyses lancées après ce travail ont le bloc `semantic` + `explanation` (vieux runs antérieurs).

## Boucle d'apprentissage (« brain ») — Sprint 1 / fondation (2026-06-08)

Virage : passer lenkrr d'open-loop (analyse→proposition→application→mesure ponctuelle) à une **boucle fermée** façon content-brain. Décisions cadrées avec Tim : apprentissage en **ledger + priors relus par lui** (le moteur `propose.ts` reste figé, les priors redescendent comme contexte de re-ranking), **pilote golfiller.fr seul**.

Modèle : analyse → proposition → application → **prédiction datée** (chaque lien posé = un pari, resolve_by J+30/J+90) → résolution GSC en **diff-in-diff** (delta cible moins delta d'un panel de pages témoins, pour soustraire saisonnalité/updates) → apprentissage (ledger + table de priors par bucket) → le prochain briefing lit les priors. On n'apprend que sur des **agrégats** de buckets, jamais sur un pari isolé (bruit GSC).

### Fait ce sprint (build + tsc verts, NON commité, migration NON poussée)
- **Migration `20260608000001_link_bets.sql`** (additive, idempotente, RLS owner + bypass service-role) :
  - `link_bets` : un pari par lien posé. Self-contained pour la résolution (`gsc_site`, `target_url`, `applied_at` = pivot). Dimensions de bucket en **texte souple** (pas de check strict, pour ne pas rejeter un import comme l'avait fait la contrainte `nextdata`) : `rule` (= nature du lien), `target_intent`, `anchor_kind`, `source_authority`. Prédiction `expected` (jsonb). `resolve_by_30/90`, `status` (pending/resolved_30/resolved_90/unmeasurable/expired), `verdict_30/90` (hit/partial/miss/no_data), `measured` (jsonb diff-in-diff). Index de file de résolution `(status, resolve_by_30)`.
  - `linking_priors` : agrégat `unique(site_id, bucket_key)`, `bucket_key = rule|target_intent|anchor_kind|source_authority`. `n_bets/n_hits/n_miss`, `win_rate`, `avg_position_delta` (négatif = la cible monte), `avg_clicks_delta`.
- **`lib/db/bets.ts`** : `logBet()` best-effort (service-role, `LENKRR_USER_ID`), calcule `resolve_by_30/90`, + helper `bucketKey()`.
- **`/api/apply` câblé** : `ApplyBody.bet?` optionnel (gscSite, sourceUrl, rule, targetIntent, sourceAuthority, expected, siteId/runId/proposalId). Log du pari après application réussie ; `gsc_site` fourni par l'UI sinon **dérivé** de l'URL publique (`sc-domain:<host>`). `anchor_kind`/`anchor_text` repris de l'ancre réellement choisie par Gemini.
- **`/api/bets/backfill`** : importe une liste de liens DÉJÀ posés à la main → paris datés. Amorce la boucle sur golfiller sans attendre que lenkrr pose les liens lui-même.

### RESTE (prochain sprint)
- **Pousser la migration** sur la base Qadence partagée (`supabase db push`) — outward-facing, à valider avec Tim avant.
- **Résolution** : edge function `lenkrr-resolve-bets` (réutilise `lenkrr-impact` + panel témoin → diff-in-diff → verdict → maj priors → ledger).
- **Réveil** : routine distante quotidienne qui tape `lenkrr-resolve-bets` (file des paris échus).
- **Ledger** : `seo-kb/lenkrr/ledgers/<date>.md` (verdicts + buckets gagnants/perdants + questions).
- **Retour** : lecture de `linking_priors` dans le flux d'analyse, passée à la couche de décision Claude.
- **Question ouverte** : comment les liens arrivent-ils sur golfiller (write-back lenkrr vs pose manuelle) → décide hook `/api/apply` vs amorçage par `/api/bets/backfill`. La fondation supporte les deux.

## Refonte Audit + Dashboard + KPI sémantiques + extractions backend (2026-06-08)

Même session. Build + tsc + `next build` verts, dev sur :3001. **NON commité.**

### Audit — pills anti-scroll (`components/result/AuditView.tsx`)
Trois `ProblemCard` empilées (orphelines, culs-de-sac, hubs + sémantiques) scrollaient à l'infini sur un gros site. Remplacé par un contrôle segmenté (pills, une catégorie à la fois, avec compteur) + pages rendues en **chips** qui s'enroulent dans un conteneur à hauteur bornée (`maxHeight 420, overflow-y auto`). Les tables sémantiques (mal classées, doublons) passent aussi en scroll borné.

### Dashboard — refonte « panneau d'instrumentation » (`components/result/DashboardView.tsx`)
Demande Tim : ultra-détaillé point par point + rendu ultra-moderne sans pattern IA. DA respectée (monochrome, Inter + JetBrains Mono, hairlines). Modules numérotés en mono (01→08), grille 12 colonnes asymétrique (`.dash-grid` ajouté à globals.css), chiffres tabulaires mono, révélation décalée. Diagnostic = score global + ses 3 composantes réelles (connectivité/fluidité/densité, mêmes formules que `maillageScore`). Modules : santé structurelle (donut + stack + %), couverture crawl, liens entrants, **profondeur de clic** (nouveau), intentions × conversion (inbound moyen Do vs site), clusters avec **cohésion sémantique par pilier**, cohérence sémantique, projection du plan (par nature + priorité + avant/après).

### KPI sémantiques (module « Signaux sémantiques & autorité »)
Tous **dérivés du rapport, zéro chiffre inventé** : Similarité cosinus (moy. `relatedness` des liens), Distance sémantique (1−cos), Cohérence des ancres (diversification ≤1 exacte/cible + % affinées IA), **Link Gap Score** (% pages en déficit = orphelines+culs-de-sac+hubs sous-maillés), **Topical Authority Flow** (autorité des hubs ÷ page moyenne, ×N).

### Extractions backend ajoutées (pour rendre réels les 2 KPI manquants)
Refusé de fabriquer → construit la vraie donnée :
- **Typage de page** (`classifyPageType` dans `classify.ts`, type `PageType`) : home/product/category/transactional/editorial/other, heuristique URL+titre déterministe. Champ `pageType` ajouté à `AnalyzedPage` (engine.ts ET AnalysisPanel.tsx). Alimente « Répartition du maillage vers » (transactionnelles/informationnelles/catégories/produits, par type de la cible des liens proposés). Limite assumée : un produit sans signal d'URL retombe en `other` (précision parfaite = lecture du type côté CMS/Woo).
- **Extraction d'entités** (`lib/analysis/entities.ts`, `buildEntityCoverage`) : déterministe, sans LLM. Séquences en Titre majuscule, filtre mots-vides + **récurrence ≥2 pages** (tue le bruit de début de phrase). Couverture = part du vocabulaire d'entités du cluster couverte par page (moy.). `EntityReport {distinctCount, coverage, top[]}` attaché à `semantic.entities`. Alimente le KPI « Couverture d'entités » + chips « entités dominantes ». Testé OK sur input type golfiller (sort Titleist Pro V1, Callaway, Bridgestone).

### RESTE
- Commit de toute la session (bets + audit + dashboard + extractions).
- Précision du typage produit/catégorie : brancher le type CMS quand le connecteur WordPress/Woo est en place (aujourd'hui heuristique URL).
- Entités : suffisant en heuristique pour le KPI ; passage LLM/NER dédié seulement si Tim veut une précision d'entités fine.
