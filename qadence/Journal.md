# Journal qadence

Repo : `~/Code/qadence` (GitHub privé `timboussardon-sketch/qadence`). Supabase partagé `ytgbnqqmcnhmscbvhoin` (« Radarr »). Front `src/` (Vite/React) sur Netlify (qadence.io). Vault RAG sur Supabase Fusionn `fwhfnzbtlddzfxbsejyf`.

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
