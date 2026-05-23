# Historique — Fusionn

Journal du travail sur Fusionn (repo `~/Code/newFusionn`). Entrée la plus récente en haut.

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
