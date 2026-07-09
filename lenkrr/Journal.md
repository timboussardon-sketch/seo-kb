# leenq (ex-lenkrr) : Journal de développement

## Cadrage IA AUTO (2026-07-09)

Nouvelle direction produit cadrée avec Tim : leenq passe du module « maillage interne » à l'agent autonome de SEO technique. Spec écrite dans [[IA-AUTO]], rien de codé.

Idée centrale : les outils du marché s'arrêtent au constat, leenq va jusqu'à l'écriture dans la source, en PR, avec vérification **avant** la fusion. Le maillage devient une règle parmi d'autres dans le même moteur.

Quatre corrections apportées à la spec initiale de Tim : la vérification passe avant la fusion et non après (un rollback de canonical ou de 301 ne défait pas ce que Google a déjà vu) ; le droit d'agir vient d'une table de classes d'action alimentée par le journal des résultats, jamais de la confiance auto-déclarée du modèle ; on compte les correcteurs vérifiés, pas les règles (500 règles = le terrain de Screaming Frog, et 200 000 constats sur lesquels personne n'agit) ; le correcteur ne touche pas à ce qui n'est pas du SEO (WebP, lazy loading, suppression de scripts, ce dernier étant l'action qui détruit un client).

Module manquant identifié : la correspondance URL vers fichier source, absente de la spec initiale, et qui décide quels sites le produit accepte.

État du code : modules 0 (partiel), 1, 4 et 6 existent déjà (connecteurs, write-back gated, auth GSC, boucle d'impact `link_bets`). Manquent le moteur de règles généralisé, la table des classes d'action, et la vérification de préversion.

Pain point chiffré : Leexi, moins 43 % de SEO hors-marque en six mois, refonte sans 301, réparé à la main sur 178 URLs.

**Deuxième passe, même jour.** Décision Tim : zéro validation humaine, un dashboard de contrôle. Spec réécrite en conséquence. La validation humaine est du théâtre (un consultant qui reçoit 40 PR par nuit clique, il ne lit pas), elle est remplacée par quatre mécanismes : vérification de préversion, budget d'actions par nuit, déploiement progressif par classe, retour arrière automatique. Une action dangereuse n'est plus « soumise à approbation », elle est **hors de l'espace d'action** : l'agent ne sait pas l'exprimer. Trois modes d'adoption : ombre (30 nuits, il montre ce qu'il aurait fait, il remplit le journal), canari, autonome.

Veille faite sur les deux produits cités par Tim. **Okara** (~66 $/mois) audite chaque jour et livre « 2 high-impact recommendations daily with copy-ready snippets » : il n'écrit pas sur le site, le livrable est un extrait à coller. **Polsia** n'est pas un produit SEO, c'est une plateforme d'agents autonomes (identité persistante, mémoire, outils, boucle planifiée) ; RankPilot vit sur `rankpilot-7.polsia.app` et semble être une app tierce, à confirmer. Conclusion : personne n'écrit dans la source du client, la ligne de démarcation de leenq est intacte.

Deux emprunts. À Polsia le runtime (le signal déclenche, pas l'utilisateur ; « ton agent » pas « notre plateforme »). À Okara la **cadence bornée** : deux corrections par jour n'est pas une limitation, c'est le budget de rayon d'explosion déguisé en rythme produit. La contrainte de sécurité est l'argument commercial. « Trois corrections cette nuit, trois vérifiées, zéro régression depuis quatre mois » remplace le compteur qui s'emballe.

Non repris : le link building autonome annoncé par RankPilot (achat de liens automatisé, interdit par la doctrine), et le positionnement anti-retainer d'Okara.

**Décision Tim : l'acheteur est le consultant SEO**, pas le fondateur sans SEO (cible d'Okara et Polsia). Tarif par site. Le dashboard multi-sites est la surface. Le plan unique à 39 €/mois du squelette Stripe ne correspond plus au produit.

## Renommage + mise en prod (2026-06-11)

Grosse session « on fait tout » : les 5 restes du backlog traités d'un coup.

- **Rebrand lenkrr → leenq** (décision Tim, domaine cible leenq.co) : tout le user-facing renommé (UI, landing, PR, app passwords WP, user-agents, branches `leenq/*`), repo GitHub renommé `timboussardon-sketch/leenq` (redirections actives), dossier local `~/Code/leenq`. Les identifiants INTERNES restent lenkrr (edges `lenkrr-*`, tables, `LENKRR_USER_ID`) pour ne rien casser.
- **PROD = Railway** (décision Tim ; Netlify écarté : functions ~26 s vs `/api/analyze` 5 min ; Vercel refusé) : projet `leenq`, auto-deploy sur push `master`, **https://web-production-023b.up.railway.app**, 8 env vars posées. Piège machine : l'API Railway coupe les clients TLS du CLI et de Python, **seul curl passe** → tout pilotage en GraphQL v2 + curl (token dans `~/.config/leenq/railway.token`).
- **Gate d'auth prod** (`middleware.ts`) : `LEENQ_AUTH_GATE=1` sur Railway → tout sauf `/`, `/login`, `/auth`, `/abonnement`, webhook Stripe exige une session du propriétaire (id `LENKRR_USER_ID` ou email `LEENQ_OWNER_EMAIL`). API → 401, pages → redirect login. Vérifié en prod. Local inchangé (accès direct).
- **Bouton « Connecter GSC »** : Réglages → carte Search Console (`components/GscConnect.tsx`, `/api/gsc/connect|status`), le callback edge redirige désormais vers `/app/reglages` (redéployé). Statut lu en service-role (connecté, email, propriétés).
- **Écran Impact** (`/app/impact`, nav) : liste les paris `link_bets` (lien, ancre, règle, date, PR/révision), verdicts J+30/J+90 + deltas ajustés stockés, bouton « Mesurer » à la demande via `lenkrr-impact` (fenêtres 28 j avant/après). Pont depuis l'écran Publier.
- **Write-back wiki.ts** : nouveau chemin STRUCTUREL déterministe (sans LLM) pour les sources « array » : `parseWikiConcepts` (slices verbatim), `prepareStructuralEdit` (ajout du slug cible dans `related[]`/`articles[]`, idempotent), branche dédiée dans `applyEdit` (remplacement de code verbatim, garde-fou « seulement un array de maillage »). **Validé en réel : PR #9 sur organikk-next**, diff d'une ligne (grounding-score → fully-meets).
- **Write-back WordPress VALIDÉ EN LIVE** : WP local monté sans Docker (PHP Homebrew + plugin SQLite, `~/.cache/lenkrr-wp`, port 8787, `php -S`). Leçon : sans HTTPS, les application passwords exigent `WP_ENVIRONMENT_TYPE=local` (le 401 initial n'était pas un bug). Chaîne complète analyze (6 pages, 9 propositions) → prepare → apply : 2 liens `<a href>` insérés dans les bons paragraphes du hub + 2 révisions réversibles.
- **Stripe squelette « prêt à vendre »** (décisions Tim : plan unique **39 €/mois**, squelette d'abord, multi-tenant plus tard) : table `leenq_subscriptions` (migration poussée), `lib/billing.ts`, routes checkout / portail / webhook (signature vérifiée), page `/abonnement` hors nav. Tout dégrade proprement tant que `STRIPE_SECRET_KEY` / `STRIPE_PRICE_ID` / `STRIPE_WEBHOOK_SECRET` ne sont pas posés. `LEENQ_BILLING=1` réservé à l'après-multi-tenant.

### Manips Tim restantes (notées aussi en mémoire)
1. Acheter **leenq.co** (dashboard Netlify, ~15 $/an) → ensuite je câble DNS Netlify → Railway + domaine custom.
2. **OAuth App GitHub de prod** (l'actuelle pointe sur localhost) : callback `https://web-production-023b.up.railway.app/api/github/callback` (puis leenq.co), poser les nouveaux CLIENT_ID/SECRET sur Railway.
3. **Allowlist auth Supabase** (dashboard, la Management API refuse le token CLI) : ajouter l'URL prod aux redirect URLs pour le login Google en prod.
4. **Stripe** : créer une clé restreinte + me la passer (méthode fichier local) → je crée produit + price 39 € + webhook moi-même.

Commits : `c4fa5ec` (GSC+Impact), `f16bb7b` (wiki), `afdacc0` (rebrand), `fe1efba` (gate), `44c7648` (billing).

État final vérifié en prod (Railway, deploy SUCCESS) : landing et `/abonnement` en 200, `/app` redirige vers le login, API en 401 sans session. Dev local : http://localhost:3000.

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
- Précision du typage produit/catégorie : brancher le type CMS quand le connecteur WordPress/Woo est en place (aujourd'hui heuristique URL).
- Entités : suffisant en heuristique pour le KPI ; passage LLM/NER dédié seulement si Tim veut une précision d'entités fine.

## Boucle d'apprentissage — résolution + réveil (2026-06-08)

Session committée et **déployée** (autonomie publish/deploy/commit). 3 commits sur master : `fc7abbf` (bets+audit+dashboard+extractions), `fa1234d` (resolve-bets), `dfe1bff` (enrichissement réponse). Migration `link_bets` **poussée** sur le Supabase Qadence (tables live).

### `lenkrr-resolve-bets` (edge déployée, --no-verify-jwt)
Ferme la boucle. Prend les paris échus (pending→J+30, resolved_30→J+90), groupe les fetches GSC par (user|site|pivot|phase) pour économiser les appels, mesure la cible en **diff-in-diff** : `Δajusté = Δcible − médiane(Δ du site sur la même fenêtre)` (soustrait saison + updates Google). Verdict `hit/partial/miss/no_data` (hit si Δposition ajustée ≤ −0,3 ou Δclics ajustés ≥ 1). Écrit `measured` sur le pari, agrège `linking_priors` par bucket (compteurs + moyennes glissantes), **1× à J+30** pour ne pas double-compter (J+90 = confirmation, n'agrège pas). La réponse renvoie `resolvedDetails[]` + `priors[]` pour le ledger. Smoke-test dryRun + live OK (tables vides → « aucun pari »).

### Routine distante = le réveil (la « loop qui prompte l'agent »)
`trig_011xk7JdVv5ED38Rc5DWqSJG`, cron `0 0 * * *` (08h Manille), repo seo-kb, Sonnet 4.6. Chaque jour : appelle l'edge (anon key publique embarquée, aucun secret service-role côté routine), et si `resolved>0` écrit un ledger `lenkrr/ledgers/<date>.md` (résumé + verdicts + priors triés par win_rate + 1-3 questions au conditionnel) puis commit/push. Si rien à résoudre : n'écrit rien. Règle « zéro chiffre inventé » dans le prompt. Premier run 2026-06-09 00:02 UTC.

### Schéma de la boucle, état
- log pari (`/api/apply` + `/api/bets/backfill`) ✅
- résolution GSC diff-in-diff (`lenkrr-resolve-bets`) ✅
- apprentissage → `linking_priors` ✅
- ledger + questions (routine) ✅
- **RETOUR** : lecture des `linking_priors` dans le flux d'analyse → passée à la couche de décision Claude (`decide.ts`). **PAS encore câblé.** Dernière pièce. Touche au comportement de décision → à montrer à Tim avant.

### Bloquant data (inchangé)
La boucle est **idle tant qu'aucun pari n'existe**. Décision en attente : sur golfiller, maillage à la main → amorcer par `/api/bets/backfill` ; ou maillage par lenkrr → hook `/api/apply`. Sans ça, la routine tourne à vide tous les matins.

## Boucle d'apprentissage — le RETOUR câblé (2026-06-09)

Session committée (`5574fef` sur master) et edge **déployée**. Dernière pièce de la boucle fermée : les priors mesurés redescendent dans la décision.

### Ce qui a été fait
- **`lib/db/priors.ts`** (nouveau) : `loadPriors(siteId?)` lit `linking_priors` pour `LENKRR_USER_ID`. Garde-fou doctrine : un bucket n'est exposé que s'il a **≥ 2 paris résolus** (`n_hits + n_miss`, jamais un pari isolé = bruit GSC), tri par `win_rate` desc, plafonné à 24. Best-effort, `[]` si persistance off.
- **`engine.ts`** : `const priors = await loadPriors()` juste avant `decidePlan`, passé dans ses args. Pas de `siteId` à ce stade (le site n'est persité qu'**après** l'analyse, dans `persistAnalysis`), donc priors au niveau compte (pilote mono-site golfiller). `loadPriors` accepte déjà un `siteId` pour scoper plus tard.
- **`decide.ts`** : champ `priors?: LinkingPrior[]` ajouté aux args, transmis tel quel à l'edge (`body: JSON.stringify(args)`).
- **`lenkrr-plan` (edge)** : reçoit `priors`, et **n'injecte le bloc dans le prompt QUE si non vide**. Format compact par bucket (`règle | intention | ancre | autorité`, n_résolus, win_rate, delta_position_moyen, delta_clics_moyen) + une consigne : signal empirique qui module la priorisation, la doctrine reste première, zéro chiffre inventé, pas d'extrapolation d'un bucket absent.

### Sûreté
Prompt **byte-identique** tant que la boucle n'a rien appris (0 prior aujourd'hui) : le `system` caché ne bouge pas, et le bloc priors est conditionnel. Zéro régression de décision. L'effet n'apparaît qu'à **J+30**, quand les premiers paris se résolvent. tsc + `next build` verts, edge déployée, smoke test (payload sans priors → validation `400` attendue) OK.

### Schéma de la boucle — COMPLET
- log pari (`/api/apply` + `/api/bets/backfill`) ✅
- résolution GSC diff-in-diff (`lenkrr-resolve-bets`) ✅
- apprentissage → `linking_priors` ✅
- ledger + questions (routine) ✅
- **RETOUR** : priors → décision Claude (`decide.ts` → edge `lenkrr-plan`) ✅ **(ce sprint)**

La boucle est désormais fermée de bout en bout. Le seul reste, c'est l'amorçage : **tant qu'aucun pari n'est posé** (décision golfiller `/api/bets/backfill` vs hook `/api/apply`), `linking_priors` reste vide et le RETOUR ne fait rien. C'est le prochain blocage à lever pour que tout s'allume.

## Amorçage de la boucle → pivot fgformation + connexion WordPress robuste (2026-06-13)

Objectif de départ : amorcer la boucle d'apprentissage (la faire tourner sur de la vraie donnée). Le travail a dévié, à raison, vers la **fiabilité de la connexion WordPress**, prérequis réel.

### Correctif boucle : `gsc_site` du pari (commit `697c2c0`, poussé)
Bug qui aurait cassé l'amorçage **en silence** : `/api/apply-plan` enregistrait le pari avec un `sc-domain:<host>` fabriqué, alors que `lenkrr-resolve-bets` interroge l'API GSC avec `gsc_site` **verbatim**. Si la propriété connectée est en **URL-prefix** (`https://host/`, cas de fgformation et golfiller), l'appel échoue → pari `no_data` à vie → priors jamais alimentés. Nouveau `resolveGscSite()` (`lib/db/gsc.ts`) choisit la propriété réellement connectée pour l'hôte (URL-prefix puis sc-domain), repli sur le fabriqué en dernier recours. Câblé `/api/apply-plan` (WordPress) et `/api/apply` (Git).

### Pivot d'amorçage : golfiller → fgformation
- **golfiller écarté** : Shopify → leenq peut crawler mais pas écrire (write-back = Git/WordPress). Backfiller le maillage existant fausserait les priors (un lien déjà en place n'a pas de fenêtre avant/après). Et son sitemap est **cassé** (boucle de redirection `/sitemap.xml` ↔ `/sitemap_index.xml`, conflit AIOSEO/Yoast/RankMath) — vrai problème SEO client à part.
- **fgformation retenu** : WordPress → leenq écrit lui-même (révision) et logge le pari automatiquement via `/api/apply-plan`. Propriété GSC `https://fgformation.fr/` **déjà connectée** sous `LENKRR_USER_ID` → résolution J+30 OK. `link_bets` toujours vide.
- **Friction rencontrée** : login wp-admin masqué (wp-login.php 404, plugin de sécurité), one-click → 403. J'avais donné l'URL `/api/wordpress/login` brute qui court-circuite le pré-vol → mur.

### Connexion WordPress robuste (commit `e11f3ac`, poussé) — décision Tim : « robuste complet », retirer provisionViaLogin du primaire
Une entrée (URL) → leenq sonde → route vers la méthode qui marchera, jamais de mur ni de spinner infini.
- `lib/wordpress-capabilities.ts` : `probeWordpress(site)` → profil {isWordpress, appPasswords, loginAccessible, authTransportConfirmed, recommendedMethod ∈ oneclick|manual|blocked, blockers+remèdes}.
- **Calibrage important** : le discriminateur d'acheminement du header `Authorization` (Basic auth bidon) ne peut que **confirmer** que le transport marche (`invalid_username`/`incorrect_password` = header arrivé). Un **utilisateur inexistant** donne le même `rest_not_logged_in` qu'un header strippé (testé sur ma.tt, wptavern, techcrunch). Donc on ne **bloque jamais** sur ce signal. La détection **certaine** du stripping se fait à `verify()` avec de vrais identifiants → remède `.htaccess`.
- **NB fgformation** : sa réponse `rest_not_logged_in` au Basic bidon est **ambiguë**, pas une preuve de stripping. On saura seulement en tentant de vrais identifiants. La sonde le route en `manual` (login masqué), pas en `blocked`.
- `verify()` décodé (`lib/connectors/wordpress.ts`, type `VerifyResult` + `decodeAuthFailure`) : rest_not_logged_in→transport strippé, incorrect_password→mauvais secret, 403→pare-feu.
- `/api/wordpress/login` **pré-vole** (ne redirige vers authorize-application.php que si oneclick viable, sinon renvoie `/connect?method=manual|blocked&reason=`).
- `/api/wordpress/health` : santé d'une connexion stockée (app password révoqué).
- UI `WordPressConnect.tsx` réécrite : fetchs bornés (AbortController+timeout, plus de « Vérification… » infinie), routage auto, remèdes affichés, santé par site + reconnexion. `provisionViaLogin` retiré du primaire (route/lib conservées, non câblées).
- `lib/wordpress-remedies.ts` : remèdes partagés serveur/client (module pur, pas de Buffer côté bundle).
- Vérifié en local (:3000) : tsc + `next build` verts, sonde/routage testés sur fgformation (→manual), ma.tt (→oneclick), techcrunch (→oneclick). `/connect` rend en 200, health gère réseau/révoqué sans crash.

### RESTE pour l'amorçage (inchangé, débloqué par la connexion robuste)
1. **Connecter fgformation** : créer un app password (profil WP, login masqué → URL custom) → le manuel décodé. Si `verify()` renvoie `auth_transport_blocked`, appliquer le remède `.htaccess` AVANT d'aller plus loin.
2. Lancer l'analyse fgformation via le connecteur WP → plan de liens.
3. Appliquer une 1re cohorte (révision) → paris datés sur `https://fgformation.fr/`.
4. Vérifier `link_bets` peuplé → routine résout à J+30 → priors → ledger.

### Note repo
Pendant la session, des fichiers **non liés** étaient modifiés dans le working tree par un travail parallèle (onboarding, FreeAnalysis, HeroAnalyze, MaillageLoader, crawl.ts, engine.ts, middleware, globals.css…). Laissés **intacts** : mes deux commits ne contiennent que leurs fichiers respectifs.

## Échec révélateur sur fgformation : 2 défauts produit (2026-06-13)

Premier vrai test bout-en-bout d'application de liens sur un site client (fgformation, WordPress connecté). Résultat : ratage, mais deux bugs réels exposés et un contenu.

### Contexte connexion
- Compte propriétaire leenq (`LENKRR_USER_ID` `49d9b314…`) n'avait AUCUN moyen de login (ni email, ni mdp, ni provider). Provisionné un login email+mdp confirmé via admin API : `tim.boussardon+leenq@gmail.com` (l'email nu était déjà pris par un autre compte) → passe le gate (`user.id === LENKRR_USER_ID`).
- Signup public cassé : `mailer_autoconfirm:false` + SMTP intégré Supabase saturé (`over_email_send_rate_limit`). Email de confirmation jamais reçu. Contournement = Google OAuth, ou provisioning admin. Fix propre (autoconfirm / Resend SMTP) = config Auth partagée avec Fusionn, à décider.

### Défaut A — diversification d'ancres CASSÉE (critique)
9 liens posés vers le même hub, **tous avec la même ancre exact-match** « Numéro de déclaration d'activité : GUIDE 2026 » (1 ancre distincte / 9, toutes `exact`). Violation directe de la doctrine (1 exact match max par cible). **Cause localisée** : `lib/analysis/engine.ts` (~l.649-664), le générateur de propositions issu du plan LLM met `anchorExact = anchorPartial = titre cible`, `recommendedAnchorKind:'exact'` pour TOUS, sans diversification — il contourne la diversification qui existe pourtant dans `propose.ts` (l.245-250). **Fix non appliqué** : engine.ts a les modifs non commitées de l'autre agent (réécriture du moteur) → l'éditer clobberait son travail. À folder dans sa réécriture : compteur par cible (1er=exact, puis alterne partial/semantic) + anchorPartial réellement distinct (titre raccourci).

### Défaut B — incompatibilité page builder (CORRIGÉ, commit `af50ebc`)
fgformation est sous **Elementor** : il rend depuis `_elementor_data` et IGNORE `post_content`. leenq écrivait le lien dans post_content (API 200), mais rien ne sortait sur le site public — et affichait « posé » (lien fantôme). `_elementor_edit_mode` n'est pas exposé en REST, et les marqueurs « elementor » sont partout (thème entier Elementor) donc non discriminants. **Détection fiable retenue** (`applyEdit`, `renderedReflects`) : si le paragraphe d'origine est dans `content.raw` mais PAS dans `content.rendered`, post_content n'est pas affiché → page builder → on REFUSE l'édition avec message clair. Validé : page Elementor 25922 refusée, post classique 26527 accepté.

### Conséquences
- Aucun dégât SEO réel : les liens (et leurs ancres sur-optimisées) n'ont jamais été rendus (Elementor), Google ne les a jamais vus. Les 9 paris bidons ont été supprimés de `link_bets` (loop repropre).
- **fgformation est majoritairement Elementor → write-back leenq inutilisable sur ces pages.** Seuls les articles de blog en contenu classique (ex. post 26527) sont éditables. Support Elementor réel (écrire dans `_elementor_data`) = chantier à part.

### RESTE
- Fix A (diversification) : à appliquer dans engine.ts une fois la réécriture de l'autre agent commitée.
- Support page builder (Elementor) : décision produit — soit on écrit dans `_elementor_data` (gros), soit on assume « leenq n'édite que le contenu classique ».

## Corrections core du moteur de maillage — faites et vérifiées (2026-06-13)

Suite au ratage fgformation, Tim a dit « fait le » : j'ai appliqué les corrections P0 sur le moteur (sur la base WIP de l'autre agent, qu'il a autorisé à embarquer car couplé). Commit `8d06464`.

### Fait (engine.ts), vérifié sur fgformation (run connecteur, 215 pages)
- **Plafond** `MAX_ANALYZE` 100 → 600 : fini la troncature des sites 200+ pages.
- **dead_end** basé sur `hostInternalOut` (vrais liens internes, même vers pages hors lot), plus sur les seules arêtes du lot.
- **Diversification d'ancres** dans le générateur issu du plan : 1 exact/cible puis partiel (titre raccourci distinct)/sémantique en rotation.
- **Résultat avant→après** : analysées 100/215→**215/215**, arêtes **36→482**, page test `devenir-…-sans-diplome` `outbound:0`(fausse orpheline)→**`outbound:2 inbound:1 OK`**, ancres 9×exact→**20/18/12**.

### Reste (non bloquant)
- P1 libellé de page quand `<title>` dupliqué (crawl.ts) — laissé : fichier le plus en mouvement chez l'autre agent, cosmétique côté connecteur.
- P1 crawl des sites rendus côté client + état des embeddings.
- Sites > 600 pages : prévoir pagination/streaming.
- orphan/inbound ne voit que les sources éditoriales du lot (une page liée seulement depuis la nav reste « orpheline ») — limite doctrine assumée.

### Note couplage
Le commit `8d06464` embarque la réécriture moteur en cours de l'autre agent (analyzeCrawl light + crawl.ts/net.ts/analyze route), indissociable d'engine.ts au commit. Build type-check + run connecteur OK. Relevé complet et à jour dans `leenq/docs/core-fixes.md`.
