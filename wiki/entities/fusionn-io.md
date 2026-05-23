---
type: entity
title: Fusionn.io
aliases: [fusionn, fusionn-io, fusionn-ai]
tags: [outil, seo, geo, saas, doctrine-tim]
created: 2026-04-12
updated: 2026-05-20
sources: 7
confidence: high
status: stable
---

# Fusionn.io

**Sous-catégorie taxonomique** : Outils SEO (§4.1 AGENTS.md).

Plateforme SaaS d'analyse sémantique SEO/GEO créée par Tim. Recherche de mots-clés pour ChatGPT, Gemini, YouTube.

## Ce que cette KB sait

- **URL** : https://fusionn.io
- **Repo** : https://github.com/timboussardon-sketch/fusionn.git (privé, créé 2026-05-07, branche `main`, ~775 Ko, TypeScript)
- Mentionné dans les 6 newsletters Algorithme comme CTA récurrent
- Le bot intégré (Fusionn AI) utilise les concepts de Tim : [[concepts/surprise-gap]], [[concepts/grounding-score]], cosine similarity, micro-intentions, Demand Score, Score GEO [[sources/2026-03-31-tim-prompt-systeme-fusionn]]
- C'est la **version commercialisée** du framework [[concepts/ingenierie-semantique-inversee]]
- Données accessibles côté produit : Semantic Keywords, Demand Scores, Google Ads metrics, FAQ/objections, structure Hn, plan d'action 360°, analyse sémantique multi-variables

## Stack technique (snapshot repo 2026-05-20)

- **Front** : Vite + React + TypeScript + Tailwind + Tiptap 3 (extensions Highlight / Placeholder / TaskList / TaskItem / TextAlign / Underline) + @dnd-kit/core
- **Backend** : Supabase (RLS activé, 169 migrations dans `supabase/migrations/`)
- **Paiement** : Stripe (3 checkout sessions + admin-link-stripe)
- **Lint** : ESLint
- **Build** : `npm run build` (Vite) avec prebuild `generate-blog-urls.js`, postbuild `react-snap` puis `inject-seo-tags.js`
- **Sitemap** : `generate-sitemap.js`
- **Hébergement** : Netlify, Node 20, redirect SPA `/* → /index.html`, cache 1 an immutable sur `/assets/*`, 7 j sur SVG
- **Bootstrap** : trace `.bolt/` à la racine (init via Bolt.new probable)

## Architecture client

### Pages publiques

Landing, APropos, Contact, Conditions, Confidentialite, Glossaire, Blog, BlogPost.

### Pages outils

AnalyseTexte, SemanticScore, Discuter.

### Pages compte / admin

Compte, ResetPassword, Admin, BlogAdmin.

### Composants notables

- **Analyse / Score** : BusinessScoreView, GeoScoreCard, GeoAnalysisHistory, AnalyseChatPanel, HighlightedText, AnalysisLimitCounter
- **Brief / Rédaction** : BriefView, BriefRedactionView
- **Chat IA** : ChatMessage, ContextualChatModal, AddContextModal, ContextManager
- **Recherche / Mots-clés** : DraggableSearchItem, ClusteredTableView, FilterStatusBanner
- **Blog** : BlogCard, BlogCategoryBadge, BlogHeroImage, BlogShareButtons, ArticleCTABanner
- **UI / Glass** : GlassFeatureCard, FloatingActionBar, FloatingNoteButton, ConsultantsSection, FAQSection, Footer
- **Auth / Upload** : AuthModal, FileUploadZone, FileUploader, ErrorBoundary

### Lib

authorityScore, explorationInsights, markdownParser, seoMarkdownParser, hnToHtml, csvGenerator, keywordActions, resultsLoader, searchUtils, projectsHelper, animations, mindmapUtils, webVitals, logger, supabase, hooks.

## Backend Supabase — Edge Functions

~30+ fonctions edge (Deno) dans `supabase/functions/` :

- **Analyses IA** : `analyze-geo-sentinel`, `analyze-semantic-score`, `analyze-hn-score`, `analyze-seo-chat`, `ai-chat`
- **Générations IA** : `generate-action-plan`, `generate-brief`, `generate-brief-redaction`, `generate-business-score`, `generate-faq`, `generate-hn-structure`, `generate-micro-intentions`, `generate-models`, `generate-objections`, `generate-pseo-strategy`, `generate-semantic-analysis`, `generate-semantic-keywords`, `generate-sitemap`
- **Data externe** : `fetch-google-ads-metrics`, `fetch-volume-trends`
- **Limites / Rate-limit** : `check-geo-analysis-limit`, `check-hn-score-limit`, `check-semantic-score-limit`, `check-rate-limit`
- **Paiement** : `create-checkout-session`, `create-annual-checkout-session`, `create-promo-checkout-session`, `admin-link-stripe`
- **Admin** : `admin-stats-v2`

## Base de données Supabase

Tables identifiées via `SECURITY_CONFIG.md` :

`user_notes` (4 RLS) · `chat_threads`, `chat_messages` · `chat_usage_daily` · `brief_basket_items` · `keyword_trends_data` (RLS avec jointure) · `daily_analytics` · `subscriptions` (Stripe).

Migration `fix_rls_performance_and_security_issues` appliquée : 19 politiques RLS optimisées (`(select auth.uid())`), 56 index inutilisés supprimés, fonction `update_keyword_trends_updated_at()` avec `search_path` immutable.

Configs Supabase manuelles encore à appliquer (cf. `SECURITY_CONFIG.md`) :

- Auth DB Connection Strategy à passer en Percentage (5-10 %) au lieu de Fixed (10 connexions)
- Activer Leaked Password Protection (HaveIBeenPwned) sur le provider Email

## SEO et pré-rendu

URLs listées dans `package.json` (`reactSnap.include`) et pré-rendues par react-snap (crawl actif, waitFor 2 000 ms, minimalQueuedTime 5 000 ms, skipThirdPartyRequests, asyncScriptTags) :

- `/`, `/a-propos`, `/contact`, `/glossaire`, `/conditions`, `/confidentialite`
- `/blog` (index), `/score-semantique` (page outil)
- Articles : `pourquoi-88-pourcent-sites-seo-napparaissent-pas-dans-ia`, `prompts-seo-strategies-workflows`, `fin-contenu-genere-humain-opportunite-seo`, `ma-reflexion-du-moment-sur-le-seo-ia`, `quadrillage-semantique-strategie-seo-face-ia`, `google-punit-il-le-contenu-ia`, `trouver-mots-cles-pertinents`

## Points à clarifier (côté Tim)

- Cible : grand public, clients Organikk, ou les deux ?
- Lien avec Organikk : produit indépendant ou outil livré pendant le bootcamp ?
- Statut commercial : déjà payant via Stripe en prod, ou en pre-launch ?
- Choix de la stack Bolt-bootstrapped : MVP rapide, ou base long terme à durcir ?

## Pages liées

[[sources/2026-03-31-tim-prompt-systeme-fusionn]] · [[sources/2026-04-13-offre-bootcamp-seo-ia]] · [[sources/2026-04-13-cas-clients-resultats]] (Julien reprend positions après refonte via Fusionn) · [[sources/2026-04-13-call-03-cecile-suite]] (Cécile utilise Fusion pour mots-clés ; Tim positionne Claude Code en complémentaire) · [[entities/bootcamp-seo-ia]] · [[concepts/ingenierie-semantique-inversee]] · [[concepts/grounding-score]] · [[concepts/surprise-gap]] · [[concepts/cli-tools-optional]]
