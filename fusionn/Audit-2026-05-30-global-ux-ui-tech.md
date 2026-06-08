# Audit global Fusionn — UX / UI / technique (2026-05-30)

> Produit audité : [[entities/fusionn-io]].

Audit complet post-pivot "site-first" (URL → crawl 20 pages → mot-clé + contexte → prompts onglets → dashboard + agent GSC). 3 axes en parallèle (UX, UI, technique). Synthèse priorisée.

> **Statut au 2026-05-30 (commit `00a6be7`) : la quasi-totalité des P0 et des P1 prioritaires sont corrigés et déployés.**
> Fait : S1 (auth JWT), S2 (RLS documents), R1 + R4 (fiabilité crawl), UX1 + UX2 (quota avant crawl + crédits), UX4/UX6 (onboarding keyword-first retiré), UI1 + design system (tokens, verts/glass, marque, focus-visible, aria), perf (loadSearchHistory + resultsLoader), UX10 (copy temps). Détail dans `Historique.md`.
> Reste P2 (non traité, hors scope) : responsive mobile du workspace, unification IA navigation, écrans d'erreur crawl enrichis, autres `generate-*` (userId body, write-only faible risque), CORS `*`.

Constat transverse : **le pivot site-first est partiel**. L'entrée URL (`SiteAuditPanel`) est posée par-dessus tout le système keyword-first qui coexiste (onboarding mot-clé, `HeroInput`, `?keyword=`, chat conversationnel). Beaucoup des frictions viennent de ces deux modèles mentaux contradictoires dans le même écran. Le cœur "workspace" (tokens CSS, classes `.workspace-*`/`.agent-chat-*`) est sain ; la dette se concentre sur les écrans récents et la sécurité des Edge Functions.

---

## P0 — Bloquants (à traiter en premier)

### Sécurité

**S1 — `userId` lu depuis le body, pas le JWT (IDOR + bypass quota crédits).**
`supabase/functions/generate-semantic-keywords/index.ts:172`, `generate-business-score/index.ts:619`. Ces fonctions ouvrent un client **service_role** et n'appellent jamais `auth.getUser` : le `userId` vient de `req.json()` et sert aux écritures + au décrément de crédits (`.eq('id', userId)`). Avec la seule anon key (publique), on peut écrire de l'historique au nom d'un autre user et décrémenter ses crédits. À comparer à `check-rate-limit` qui, lui, dérive le userId du token. Fix : dériver le userId du token dans toutes les functions service_role, ignorer le champ body, et vérifier `verify_jwt` (aucun `config.toml` ne le surcharge dans le repo).

**S2 — Policy RLS `documents` ouverte à `anon`.**
`migrations/20260123032458_*.sql` : `"Anyone can manage documents by session_id" FOR ALL TO anon USING (session_id IS NOT NULL)` — le prédicat ne compare rien, donc tout anon peut lire/écrire/supprimer toute ligne `documents`. Les migrations suivantes ajoutent des policies user-scopées mais ne droppent pas celle-ci. Fix : `DROP POLICY`.

### Robustesse

**R1 — `start-site-crawl` fetch les 20 pages dans la requête HTTP synchrone → crawl qui peut rester bloqué à l'infini.**
`start-site-crawl/index.ts:149-186` (+ découverte sitemap `61-82` : jusqu'à 50 sitemaps × 8s). Si le budget temps de l'Edge Function est dépassé, la fonction est tuée, `site_crawls.status` reste `crawling`, et le polling front (`useSiteCrawl`, 2s) **boucle sans fin** (aucun statut terminal écrit). `crawl-batch` existe pour ça mais est débranché. Fix : déléguer le fetch en async (`EdgeRuntime.waitUntil` / `crawl-batch`) + **toujours** écrire un statut terminal (deadline globale + finally).

### UX / activation

**UX1 — Le quota gratuit n'est vérifié qu'APRÈS le crawl complet.**
`SiteAuditPanel.tsx:287` (`startCrawl` sans rate-limit) ; le check ne tombe que dans `performSearch` une fois l'audit fini. Un free user à 0 crédit subit ~60s d'audit + l'écran "ce qu'il faut retenir", puis se prend le mur. Le crawl backend est consommé pour rien. Fix : `checkRateLimit` dans `submit` avant tout crawl, modal abo immédiat si `!allowed`.

**UX2 — `SiteAuditPanel` n'affiche jamais les crédits restants.**
L'entrée principale est aveugle sur le quota (l'ancien `HeroInput` affichait `X/3`). Fix : passer + afficher `remainingSearches`.

### UI

**UI1 — `SiteAuditPanel.tsx` entièrement en `slate-*` (palette froide étrangère au DS).**
36 occurrences `slate-*` + shimmer `#94a3b8/#0f172a` (déjà flaggé par Tim). C'est le **premier écran** post-saisie d'URL, et il jure visuellement avec le reste de `/compte` (gris chaud `--ws-text-strong #212121`). Fix : migrer `slate-*` → tokens `--ws-*`, shimmer en gris chaud. (Note : c'est l'écran que j'ai construit cette session, dette assumée.)

---

## P1 — Importants

**UX4 + UX6 — Deux entrées contradictoires : URL vs mot-clé.** Le hero demande une URL, mais l'`OnboardingOverlay` qui se superpose demande un **mot-clé** (et peut surgir par-dessus un audit en cours car son garde-fou ne couvre pas `?siteUrl=` / `localStorage`). `Compte.tsx:689-705` vs `OnboardingOverlay.tsx:27-62`. Fix : trancher site-first ; onboarding + exemples en URL ; ajouter `siteUrl`/`fusionn_pending_site_audit` à la condition de suppression de l'overlay.

**UI design system — Verts `#244831` + glassmorphism résiduels hors DS.** `OnboardingOverlay.tsx` (dégradé vert, bouton vert), `SeoConversationalChat.tsx:342,387,507`, `SubscriptionChoiceModal.tsx` (glass + vert green-700/100). Contre la doctrine gris/blanc/`#FF371C`. Fix : tokens + brand.

**UI — Marque fragmentée.** `const BRAND='#FF371C'` redéclaré localement (×475 hex dans le repo), et **5 valeurs différentes** de hover orange (`#E22E14`, `#E5301A`, `#E62E13`, `#E63312`, `#E62F17`). Fix : `var(--ws-brand)` + un seul `--ws-brand-hover` + tokens sévérité.

**Perf P-1 — `loadAllResults` = 18 `select('*')` en parallèle par ouverture de dashboard.** `resultsLoader.ts` (dédup en mémoire). Fix : colonnes ciblées + dédup SQL.

**Perf P-2 — `loadSearchHistory` : 5 requêtes `.in()` sur ~500 ids juste pour des booléens.** `Compte.tsx:91-102`. (Le `select('*')` lourd a déjà été corrigé cette session ; restent les 5 IN.) Fix : réutiliser `results_summary` déjà stocké, ou un count SQL agrégé.

**Perf P-4 — Chunk `Compte` = 1.7 Mo eager.** Tout le workspace dans un seul chunk. Fix : `React.lazy` sur les onglets lourds (graphes `@xyflow`, éditeur tiptap), lazy `pdf`/`mammoth`.

**R3 — Watchdog 75s jamais nettoyé + race sur recherche obsolète.** `useSearchPipeline.ts:433`. Fix : `clearTimeout` après le race + garde `searchId`.

**R4 — Chaînage crawl front best-effort sans retry.** `useSiteCrawl.ts:71-103` : le ref est posé **avant** le fetch → une invocation ratée n'est jamais relancée, polling infini. Fix : poser le ref après succès + timeout d'arrêt de polling.

**UX9 — Architecture d'info éclatée.** Mode-bar à 2 entrées (Stratégie/Agent) mais 5 `ViewMode` (planAction/llm/writer cachés) + 11 sous-onglets `ResultsNav`. Navigation mi-cachée mi-dense. Fix : unifier.

**UX10 — Promesse temps incohérente.** "Quelques secondes" (Landing/Connexion), "30 secondes" (Onboarding), réalité crawl ~60s (`SiteAuditPanel` PHASES = 60s). Fix : aligner le copy sur ~1 min.

**Accessibilité (UI P1-1/P1-2/P1-3) — focus clavier quasi inexistant** (4 règles `:focus` dans tout l'index.css), **boutons icon-only sans `aria-label`** (AgentChatView, SiteAuditPanel), **contraste `--ws-text-faint #9CA3AF` sous WCAG AA** sur du texte porteur d'info. Fix : `:focus-visible` global brand, `aria-label`, réserver `faint` au décoratif.

**UI P1-5 — Layout Agent non responsive** (sidebar 258px fixe, aucune media query `agent-chat-*`). + UX15 : workspace 3 colonnes `100dvh overflow:hidden`, `Navbar` lit `innerWidth` figé au render. Produit desktop-only. Fix : drawer/empilement sous breakpoint.

---

## P2 — Confort / dette

- **UX3 + UX8 — Écran d'erreur de crawl pauvre** (pas de cause ni recours) et **dashboard incomplet silencieux** quand `forceDone` (45s) débloque sans signaler les onglets ratés. Marquer les onglets indisponibles + messages d'erreur typés + fallback "analyse par mot-clé".
- **UX7 — Écran "ce qu'il faut retenir" peut être vide** si `opportunities_status='error'` ou `primary_keyword` null après ~60s. Garantir un contenu minimal.
- **UX11 — `FirstSearchTour` tutoie** alors que tout vouvoie. **UX12 — le tour pointe des onglets pas encore générés** (vecteurs `false` par défaut). **UX14 — état vide agent = cul-de-sac** ("lancez une analyse de mot-clé" sans lien, wording keyword).
- **UX13 — GSC verrouillée sans recours pour le multi-clients** (Projets) : `handleGscPropertyChange` existe mais débranché. (Voir nuance ci-dessous.)
- **UX17 — Trop de "Bientôt" visibles** (Reddit vendu sur la Landing mais grisé, onglet Agents "Bientôt"). Masquer plutôt que griser.
- **UX18 — Remise abo incohérente** (-31% modal vs -30% landing).
- **Perf P-3 — Re-fetch complet à chaque clic d'historique** (pas de cache). **P-5 — `pdf`/`mammoth` à charger en dynamic import.**
- **Sécurité S4 — CORS `*`** : **décision 2026-05-30, gardé en `*` (choix assumé)**. L'auth Supabase est par Bearer token (pas cookie), donc pas de CSRF possible ; restreindre casserait le dev local + les previews Netlify pour un gain marginal. La vraie barrière est l'auth JWT (S1, corrigé). **S3 — update `documents` sans `.eq('user_id')`** ceinture-bretelles.
- **Robustesse R2 — `crawl-batch` = code mort** (débranché) avec réservation `pending→fetching` non atomique. **R5 — `ai-chat` boucle outils sans timeout Gemini.** **R6 — sitemap sans budget temps global.**
- **Qualité — `any` dans loaders (`resultsLoader`), erreurs avalées sans log, `gscPropDomain` dupliqué ×3, Reddit débranché à flaguer (`REDDIT_ENABLED`).**

---

## Top priorités absolues (les 8)

1. **S1 — authentifier `userId` par le JWT** dans les functions service_role (IDOR + bypass crédits exploitable avec l'anon key publique). Le plus grave.
2. **R1 — fiabiliser `start-site-crawl`** : fetch async + statut terminal garanti, sinon le polling boucle à l'infini quand le crawl dépasse son budget temps.
3. **UX1 + UX2 — vérifier le quota AVANT le crawl** et **afficher les crédits** dans `SiteAuditPanel` (le bug d'activation le plus coûteux : 60s d'audit pour rien).
4. **S2 — dropper la policy RLS `documents` ouverte à anon.**
5. **UX4/UX6 — trancher site-first vs keyword-first** : l'onboarding mot-clé contredit et peut écraser l'audit URL.
6. **UI1 + design system — migrer `SiteAuditPanel` vers les tokens** et tuer les verts `#244831` / glassmorphism + unifier la marque (`--ws-brand` + un seul hover).
7. **R3/R4 — nettoyer watchdog + chaînage crawl** (timers non nettoyés, refs posés avant succès, polling infini).
8. **Perf — `loadAllResults`/`loadSearchHistory` colonnes ciblées + code-split `Compte` 1.7 Mo.**

---

## Note sur le GSC verrouillé (UX13)

Le verrouillage GSC sur le site analysé a été posé cette session **à la demande de Tim** (priorité absolue au site analysé, suppression du sélecteur multi-domaines). L'audit le relève comme une limite pour le multi-clients (Projets), mais c'est un choix produit assumé, pas un bug. À réévaluer seulement si le cas multi-propriétés devient fréquent.

---

*Audit généré par 3 sous-agents (UX, UI, technique) sur l'état `main` de `/Users/timothee/Code/newFusionn`, 2026-05-30. Détail complet des findings disponible dans les sorties d'agents de la session.*
