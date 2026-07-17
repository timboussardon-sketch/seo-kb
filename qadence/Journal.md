# Journal qadence

Repo : `~/Code/qadence` (GitHub privé `timboussardon-sketch/qadence`). Supabase partagé `ytgbnqqmcnhmscbvhoin` (« Radarr »). Front `src/` (Vite/React) sur Netlify (qadence.io). Vault RAG sur Supabase Fusionn `fwhfnzbtlddzfxbsejyf`.

## État actuel — point de départ (2026-06-13)

Ce qui est **live en prod** et sert de base à la prochaine session :
- **Agent** : edge `seo-agent` sous Claude (Messages API, streaming SSE). Outils : `search_kb` (vault Obsidian via `kb-search` → `kb_chunks`), `gsc_query` (GSC réelle, résolveur tolérant à la fragmentation des sessions), `load_skill` (doctrine table `skills`), `update_memory`. Voix `ton_de_voix_tim`.
- **Doctrine** : table `skills` = `~/.claude/skills/seo-*` verbatim, synchro par `qadence/sync-skills.py` (audit : 26 slugs identiques 100 %).
- **Front** (Vite/React, design Google-mono) : chat + `SkillLauncher` (« + Skills » top bar), `AccountPage` plein écran (Profil/Abonnement/Connexions/Stats), GSC multi-comptes (`gsc-properties`), espace compte + déconnexion.
- **Déploiement** : backend via `supabase functions deploy … --project-ref ytgbnqqmcnhmscbvhoin` (live direct) ; front via `npm run build` + `netlify deploy --prod --site=0584c0db-0d72-48bd-b7f5-24a231b54959`.

**Prochaines étapes** (non faites) : relier le site Netlify ↔ repo GitHub (auto-deploy) ; agents autonomes (watcher/quickwin/cannibal/cocon) sous Claude pas branchés ; borne GSC gros comptes (edge 150s) ; 9 skills `proprietary` encore en stubs (audit_gsc, faq_*, structure_hn…).

Snapshot code figé : `raw/agents/qadence-seo-agent/snapshot-2026-06-13-claude/`. Connaissance vault : [[entities/qadence-seo-agent]].

---

## Refonte « qadence = mon système SEO sous Claude » (2026-06-13)

Virage majeur : qadence ne tournait plus côté IA (modèles `gemini-3.1-flash/pro` → **404 model not found**, clé Gemini de qadence HS). Décision de Tim : reconstruire la couche agents **sous Claude** et faire que qadence réponde **avec sa doctrine, ses skills, ses boucles et son vault Obsidian** — « comme si le user était branché sur mon Obsidian ».

### Mise sous git + bundle complet
- Le vrai repo `timboussardon-sketch/qadence` existait déjà (front `src/` Vite canonique, pas le `bot/` Next). Cloné sur `~/Code/qadence`, complété avec les **edge functions déployées récupérées de la prod** (le repo + le « transfer bundle » étaient tous deux partiels). Commits multiples, poussés.

### Audits (docs/AUDIT-agents.md, AUDIT-skills.md)
- **Agents** : 2 architectures — déployée vivante (seo-agent conversationnel, seo-squad) vs refonte « Hermes » jamais déployée (agent-runner + cron-watcher/quickwin/cannibal/cocon, table `agents` inexistante = code mort). Couche cron (botbeat/digests/rank-tracker) éteinte.
- **Skills** : la **table `skills` (Supabase) = source de vérité runtime**. Fichiers locaux périmés / mi-stubs.

### Découverte Gemini (importante)
- `gemini-3.1-*` (utilisé partout, dont seo-agent live) renvoie **404**. MAIS `gemini-embedding-001` et `gemini-2.5-flash` **fonctionnent**. → Claude retenu (décision Tim), et le seo-agent Gemini aurait pu être ressuscité en changeant juste le nom de modèle (filet de secours noté).

### Vault RAG branché (« mon Obsidian en direct »)
- Pipeline existant réutilisé : `export_supabase.py` → `kb-ingest` → table **`kb_chunks` (pgvector)** sur le Supabase Fusionn (embeddings `gemini-embedding-001`, vivants).
- Nouvelle edge **`kb-search`** (déployée sur Fusionn) : retrieval pur → renvoie les chunks bruts {path,title,content} du vault. Testée : « mots-clés décisionnels » → vrais extraits du vault.
- Secrets qadence `KB_SEARCH_URL`/`KB_SEARCH_KEY` (accès cross-projet).

### seo-agent reconstruit sous Claude — EN PROD (bascule faite)
- Socle `claude.ts` : boucle Claude Messages API tool-use + **variante streaming** (parse le flux Anthropic → émet le SSE).
- `seo-agent` (le slug que le front appelle) **redéployé en version Claude** : streaming SSE au contrat front exact (`thinking|text|memory_updated|done`) → **zéro changement front**. Outils : `search_kb` (vault), `gsc_query` (GSC réelle), `load_skill` (table skills = doctrine), `update_memory`. Voix `ton_de_voix_tim` en système.
- Ancien Gemini conservé : `seo-agent-gemini-legacy/` (rollback = redeploy).
- Vérifié live (golfiller) : data GSC réelle (3 943 clics…) + doctrine (« conversion > trafic ») + voix, en streaming. Le run sur gros compte peut timeouter (plafond edge ~150s) — à borner.

### Endpoints front cassés réparés
- `set-gsc-site` (était déployé sous `set-gsc-site-`, slug cassé → 404) redéployé au bon slug.
- `fetch-page-proxy` (jamais déployé, appelé par le front pour l'auto-détection de secteur) **reconstruit** : fetch page + meta + classification secteur **via Claude** (la clé Gemini de qadence échouant). Testé : fgformation → « Formation professionnelle ».

### Skills = 100 % ma doctrine
- **24 skills** portés depuis `~/.claude/skills/seo-*` (contenu = source verbatim) + **`ton_de_voix_tim`** (12 Ko) en système.
- **12 skills** sans équivalent /seo- (audit_gsc, analyse_gsc_complete, cohortes_gsc, gsc_traffic_mapping, faq_query, faq_strategique, strategie_seo, content_gaps, intention_recherche, query_requete, structure_hn, structure_hn_editoriale) **alignés** par un prompt « ancré doctrine » : principes non négociables + tâche dans le cadrage de Tim + instruction d'interroger `search_kb` (le vault) avant de répondre. Zéro invention.
- 6 hooks internes (agent_critique, auto_memory, escalade_pro, never_assume_zero, skill_before_responding, use_memory_first) laissés (runtime, pas doctrine).
- Backup avant port : `supabase/skills-backup/`.

### Refonte design « Google mono » + règles Fusionn (front src/)
- Polices **Roboto + Roboto Mono** (fini Inter/JetBrains). Palette **monochrome Google** (fond #F8F9FA, cartes blanches, gris #202124/#5F6368, bordures #DADCE0, **accent bleu unique #1A73E8**, fini le teal). Sidebar repassée en clair (style Gmail/Drive). Échelle/grille/radius des règles Fusionn (radius 8, pills 40). Tokens dans `src/index.css`, cascade sur les composants. Sweep des couleurs en dur (teal, overlays blancs).

## Reste à faire (optionnel / décision)
- **Agents autonomes** (watcher/quickwin/cannibal/cocon) sous Claude + tables `agents`/`agent_runs` + pg_cron + **décision coût** (pilote vs 143 users). Pas branchés dans le front actuel.
- **Squad** (Indigo/Ambre/Jade/Carmin) sous Claude (déjà couvert par le conversationnel via load_skill).
- Finitions : outils fetch_serp/score_content au conversationnel ; sync auto `~/.claude/skills`→table `skills` ; borne GSC gros comptes ; polish design composant par composant ; retirer code mort (score-engine/agent-runner jamais déployés).

## 2026-06-13 — Espace compte (stats + déconnexion)
- Nouveau composant `src/components/AccountPanel.jsx` : modale "Mon compte" ouverte depuis un bouton en bas de la Sidebar.
- Identité : email Google (table `google_connections`), pastille statut connecté.
- Stats réelles : projets suivis + conversations (localStorage), sites GSC connectés, recommandations (`optimizations`), faits mémorisés (`project_memory`), rapports (`botbeat_reports`) — comptés via PostgREST `count=exact`.
- Liste des sites Search Console connectés.
- Déconnexion : `supabase.auth.signOut()` + purge des clés `radarr_*` + reload.
- Design Google-mono (Roboto/Roboto Mono, gris Google, accent #1A73E8, chiffres en mono).
- Commit + push main + déployé prod sur qadence.io (site inquisitive-pegasus).

## 2026-06-13 (suite) — Connexion GSC : fix fragmentation + système multi-comptes/multi-sites
**Problème** : l'agent répondait « Google Search Console non connectée » alors que fgformation.fr était bien connecté. Cause : `seo-agent/gsc.ts` cherchait le token strictement par le `user_id` de la session courante. Les sessions anonymes fragmentent les connexions Google sur plusieurs user_id (Tim en avait 5+, ses 23-30 propriétés éparpillées).
**Diagnostic prouvé** : avec le token le plus frais de tim.boussardon@gmail.com → fgformation.fr 28j = 663 clics / 51 609 impressions / CTR 1,28 % / pos 12,7.
**Fixes livrés (tous en prod)** :
- `seo-agent/gsc.ts` : résolveur robuste (user_id+site → user_id → site → domaine). Validé live avec user_id orphelin → sort les vrais chiffres. Propagé seo-agent ET seo-agent-claude.
- Edge `gsc-properties` : liste les propriétés groupées par compte Google (résout par email à travers les user_id, refresh token, fusionne Google+DB). Test : 30 propriétés pour tim.
- Edge `stripe-portal` : portail de facturation (STRIPE_SECRET_KEY déjà posé).
- Front `AccountPage.jsx` plein écran (remplace l'ancienne mini-modale AccountPanel, supprimée) : onglets Profil / Abonnement / Connexions / Statistiques. Connexions = liste des comptes Google + « Connecter un autre compte » (google-auth add_account) + sélecteur de propriété par projet (optgroup par compte, gère multi-sites/multi-comptes). Déconnexion.
- `ConnectGoogle.jsx` : passe `user_id` à google-auth (réduit la fragmentation future).
- App.jsx : state `view` chat|account ; bouton « Mon compte » sidebar.
Commit + push main + déploiement prod qadence.io. Design Google-mono.
**Reste** : connecter le site Netlify au repo GitHub pour l'auto-deploy (étape dashboard).

## 2026-06-13 (suite) — Lanceur de skills dans la barre du haut
- Composant `SkillLauncher.jsx` : bouton « + Skills » dans la top bar de Chat.
- Liste les skills actifs `skill_type in (seo, proprietary)` = 36 skills doctrine (exclut les 6 hooks `behavior` et la `voice ton_de_voix_tim`, qui sont des règles d'exécution).
- Lecture anon de la table `skills` (RLS le permet). Labels nettoyés (retire « Seo », GSC/GEO/pSEO/RRF en capitales), groupés « Skills SEO » / « Méthodes propriétaires », recherche live.
- Clic = envoie au chat `Lance le skill « X » (load_skill, slug: name) puis applique sa méthode pas à pas sur <domain>` → l'agent charge le skill et l'exécute.
- Commit + push + déploiement prod qadence.io.

## 2026-06-13 (suite) — Audit doctrine agent ↔ Obsidian + synchro permanente
**Audit** : confronté la table `skills` (base doctrinale de l'agent qadence) à la source `~/.claude/skills`.
- ✅ 20 skills SEO + `ton_de_voix_tim` = IDENTIQUES à 100 % (verbatim) aux SKILL.md.
- ✅ 4 alias propriétaires (maillage_interne, objections_clients, score_geo, score_semantique) = byte-identiques à leur doctrine SEO.
- ⚠️ 11 entrées `proprietary` étaient des stubs génériques ~700 car. (rappel de principes + search_kb, pas la méthode complète) ; 3 exposées dans load_skill.
**Correctifs** :
- Nouveau `qadence/sync-skills.py` : synchro idempotente table `skills` ← SKILL.md (26 slugs mappés, alias inclus), `--dry-run` dispo. Créds dans `~/.config/seo-kb/qadence-skills.env` (hors repo, chmod 600). À relancer après modif d'un SKILL.md / `./kb rebuild`.
- Upgradé les 2 stubs exposés : `content_gaps` ← seo-cluster-aeo (724→2344), `strategie_seo` ← seo-roadmap-pseo (707→16180). Vérifié en base.
- Stubs restants (audit_gsc, analyse_gsc_complete, cohortes_gsc, faq_*, intention_recherche, query_requete, structure_hn*) laissés tels quels : pas de skill source 1:1, grounded par search_kb + gsc_query.

## 2026-06-16 — Réparation des crons (rapports auto 7h / 8h30 / hebdo)
**Constat** : les 14 fonctions cron étaient déployées mais les 3 features (7h positions, 8h30 corrections, hebdo montées/chutes) **n'avaient aucun schedule pg_cron** (seuls les 4 jobs Hermes du 15/06 existaient). `daily-digest` avait tourné jusqu'au 1er juin puis stoppé ; `rank_history` et `weekly_push_reports` à 0.
**Causes trouvées** :
- Aucun schedule pour rank-tracker / daily-digest / weekly-push (migration `setup_crons` jamais appliquée + URL `rank-tracker-cron` en 404).
- Boucles sur les **1299 connexions OAuth orphelines** → timeout (56 projets GSC mais ~16 propriétés/user actif).
- `rank-tracker` : `onConflict` sur `date` au lieu de `recorded_date` → upsert planté.
- Modèles Gemini hardcodés **invalides** (`gemini-3.1-flash` / `gemini-3.1-pro` → 400) dans daily-digest ET weekly-push.
- `daily-digest` filtrait sur des clés mémoire disparues (`insights`, `known_pages`).
- `weekly-push` (worker) **ignorait le body** et rebouclait sur tous les users à chaque appel du wrapper.
**Correctifs** (commit `c4b5fc9` + déploiements) :
- Vue `active_gsc_targets` : pilote unique = sites avec `project_memory` < 30j résolus vers une connexion GSC = **~22 cibles réelles** (choix de Tim : « comptes actifs récemment »).
- 3 fonctions branchées sur la vue ; traitement par **lots concurrents** (digest 6, weekly 4) ; modèles → `gemini-flash-latest` / `gemini-pro-latest` ; fix onConflict ; fallback RAS ; weekly-push respecte désormais `user_id`/`gsc_site` du body.
- 3 schedules pg_cron créés : `qadence_rank_tracker` (0 7 * * *), `qadence_daily_digest` (30 8 * * *), `qadence_weekly_push` (0 8 * * 1), URLs corrigées.
**Vérifié live** : rank-tracker → 910 lignes `rank_history` (21 sites) ; daily-digest → run complet 24s, écrit (RAS au 1er jour, normal : pas encore d'historique J-7). weekly-push **vérifié** : après parallélisation des 3 pages (timeout edge réglé) + purge des colonnes inexistantes (current_period/previous_period/generated_at) qui faisaient échouer l'insert en silence → 1re ligne écrite dans `weekly_push_reports` (HTTP 200, 3 pages). Les 3 features tournent. (commits `c4b5fc9`, `772d78f`, `c41d47b` sur `fix/audit-sprint0-security`)
**Note infra** : `net.http_post` (pg_cron) timeout à 5s → log un timeout mais la fonction continue server-side (fire-and-forget OK). Accès DB de debug via token CLI keychain « Supabase CLI » + API Management `database/query`.

## 2026-06-23 — Clé Gemini, limite freemium 7→3, audit & économie de tokens

**Clé API Gemini** : testée avant pose (gemini-flash-latest/pro-latest/embedding-001 → 200), posée en secret `GEMINI_API_KEY` (projet qadence). `GEMINI_API_KEY_2` (secours) inchangée ; Fusionn intacte.

**Limite gratuite 7 → 3** : `UPDATE plan_limits` free/beta=3 en prod (lu par `consume_quota`, effet immédiat). Front : `FREE_LIMIT` (Chat) + `PLAN_LIMITS` (AccountPage) = 3, migration alignée. Wording cards tarif « 3 actions au total » / « ≈20 min » + quotaTitle (FR+EN). Build + déploiement Netlify. Commit `54daa95`.

**Audit token + 3 fixes (commit `cca3126`)** : l'historique n'était pas caché (system+outils oui, messages non) → transcript (dumps RAG `get_document` 40k, skills) retraité plein tarif chaque tour. Opus 4.7 = 4.8 (même prix) → le levier est le contexte, pas le modèle.
- #1 cache historique : `cache_control` sur le dernier bloc de `messages` (claude.ts) → ~0,1×.
- #2 trim (`get_document` 40k→12k, cap tool results 60k→24k) + context editing beta `clear_tool_uses_20250919` (header `context-management-2025-06-27`), kill-switch `SEO_AGENT_CTX_EDIT`. Validé sur appel Anthropic réel via sonde jetable → HTTP 200 ; activé (`=1`), `seo-agent` redéployé, sonde supprimée.
- #3 effort par tier : Sonnet 'low' / Opus 'high' (index.ts), posé seulement sur opus/sonnet.

## 2026-07-03 — Conscience temporelle, proactivité, DA « Métriques », boucle de résultat

**DA « Métriques » sur tous les onglets Suivi & Analyse** (commits `e43da36`, `1741621`, `9fc366a`, `295d70f`) : 5 propositions maquettées en dev (`/design-onglets`), Tim a retenu « Métriques » (alignée sur Performances). Cartes métriques colorées langage GSC (`MetricCards`/`GSC`/`StatusChip` dans dashKit), deltas verts/rouges (fini le bleu accent), tableaux à en-tête gris arrondi (coins 14 px, `border-collapse: separate` car collapse ignore border-radius), barres de données en dégradés de bleu (jamais d'ocre), flèches de tendance `TrendArrow` à la place des mini-traits (Rapport + Suivi), listes d'URLs une ligne par URL.

**Conscience temporelle de l'agent** (commit `e6da2f0`, 7 chantiers d'un audit validé par Tim) :
- Prompt : état SEO (snapshots), journal 10 événements (`project_events`), recos + résultats mesurés, décisions dures (`decision:*`), déjà expliqué (`explained:*`), signaux crons.
- Nouveaux outils : `record_decision`, `track_reco`, `open_view` ; `suggest_agent` élargi aux 7 personas ; continuité de profondeur sur l'historique (un follow-up court reste en tour profond).
- « Prochaine meilleure action » obligatoire en fin d'analyse : bloc ```nba rendu en carte (impact /5, minutes, ≈ clics/mois, confiance %, pourquoi), chiffres dérivés des outils uniquement, puis `track_reco`.
- Boucle de résultat : table `agent_recos` (migration `20260703120000`) + edge `cron-reco-outcome` (cron pg 7h15 UTC, job 32) qui re-mesure la GSC à J+14/J+30, écrit les deltas, notifie, trace un `project_events`.
- `distill-session` extrait décisions/concepts/événements en fin de session.
- Front : ouverture proactive du chat (daily-briefing assemblé, zéro LLM, 1×/jour/projet), `NextActionCard`, bouton open_view, Thinking à étapes sur l'onglet To do (`24d7309`).
- Évals de régression : `evals/run-evals.mjs` + `prompts.json` (10 prompts dorés), à lancer avant tout deploy du prompt.

**Optimisation cache** (commit `76314d7`) : voix (12 003 car.) + règle fondamentale (~6 500 car.) déplacées dans la tête cacheable du prompt (~4 600 tokens qui passaient plein tarif à chaque session/invalidation → tarif cache 10 %). Rappel court en fin de queue pour garder le poids de fin de prompt.

**Déploiements** : migration via API Management (HTTP 201), `seo-agent` v261, `distill-session` v34, `cron-reco-outcome` v1, front Netlify ×3. Vérifs : cron actif en cron.job, fonctions répondent, `agent_recos` existe. Le système démarre à vide : les blocs temporels se remplissent avec l'usage, premiers outcomes à J+14.

## 2026-07-17 — Agents autonomes : les findings n'atteignaient jamais la base (2 bugs) — DÉPLOYÉ

Parti d'une question de Tim : « où s'affichent les résultats une fois les crons terminés ? ». Réponse : **nulle part**. Les agents tournaient, trouvaient, et jetaient tout. Découvert en vérifiant la prod, pas le code.

**Le constat en base** : `optimizations` = 1 053 lignes, **toutes avec `agent_id` NULL**, la plus récente du 26/05 et venant d'un autre écrivain. Aucun finding d'agent n'y était jamais arrivé. En face : Watcher 436 runs `success` / 1 310 findings comptés, 649 notifications « X points trouvés — À regarder dans tes optimisations » pointant vers un panneau vide.

**Bug 1** — `optimizations.domain` est `NOT NULL` sans défaut, et `persistFinding` (`agent-runner/index.ts`) ne l'envoyait jamais. Chaque insert cassait sur `23502 null value in column "domain"`. Prouvé en rejouant l'insert exact en prod avec rollback garanti.

**Bug 2** — `optimizations.type` porte un `CHECK` sur 8 valeurs (`title, meta, contenu, cwv, maillage, structure_hn, quick_win, other`), alors que le prompt laissait le LLM inventer les siennes (`traffic_drop`…). Masqué par le bug 1, apparu au premier run réparé. Fix : normalisation sur `other` + type d'origine conservé dans `evidence.type_agent` (on ne perd pas la trouvaille) + prompt qui énumère les valeurs acceptées.

**La cause racine des deux : l'erreur était avalée.** Un `console.error`, un run marqué `success`, et `findings_count` qui comptait la sortie du LLM au lieu de ce qui était gardé. Corrigé : perte totale (trouvé > 0, enregistré = 0) → run en `error` ; perte partielle → `success` mais casse écrite dans `agent_runs.error` ; `findings_count` et la notification comptent l'**enregistré**. Leçon générale : ne jamais notifier sur une écriture non vérifiée.

**Vérif prod** (qadence.io, run réel) : 3 trouvés → 3 enregistrés → 0 erreur. Cinq lignes `agent_id='watcher'` en base, les premières de l'histoire de la table. Les résultats s'affichent dans le panneau Recommandations, le plan d'action et la cloche.

**Déploiements** : `agent-runner` (×2, le premier run échouait encore parce que le deploy n'était pas passé — toujours vérifier la sortie `Deployed Functions`). Commit `9f794be0`, push OK (183 commits de retard rattrapés).

**Restes ouverts** (non traités) : les 1 053 lignes `agent_id` NULL viennent d'un autre écrivain arrêté le 26/05, à investiguer ; `cocon` fait 7 runs `success` pour **0 finding** ; `cannibal` est à 9 erreurs sur 51 runs (18 %, vs 3/439 pour watcher) ; un run watcher bloqué en `running` depuis le 23/06 ; 5 findings en doublon sur qadence.io issus de mes runs de test.

**Journal à corriger** : la ligne « retirer code mort (score-engine/agent-runner jamais déployés) » plus haut est fausse — `agent-runner` est déployé et tourne en prod depuis mars.
