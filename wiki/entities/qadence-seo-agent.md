---
type: entity
title: "Qadence (qadence.io)"
aliases: [qadence, qadence-io, qadence-seo-agent, qadence-agent, watcher, scorer, botbeat, veilleur]
tags: [agent, produit-tim, supabase, edge-function, deno, vite, react, netlify, claude, claude-api, vault-rag, gemini-legacy, gsc, opendecoder, dispatcher, organikk]
created: 2026-04-30
updated: 2026-07-03
sources: 3
confidence: high
status: stable
---

# Qadence

**Sous-catégorie taxonomique** : Offres / Produits Tim (§4.1) ∩ Architectures IA / Agents (§4.1 — agent en production).

Plateforme SEO agentique de Tim. Frontend `qadence.io` + API `api.qadence.io`. Pitch : *"Votre partenaire SEO connecté à votre GSC, pas un chatbot qui invente."* Cible : praticien SEO sénior, contexte cumulatif entre conversations.

Distinct de [[entities/organikk-co]] (laboratoire public + acquisition) : Qadence = produit SaaS agentique, sortie commerciale de la doctrine 4 piliers ([[concepts/methode-organikk-4-piliers]]).

## Conscience temporelle + proactivité (2026-07-03) : l'agent tient ses dossiers

Chantier structurant livré en prod le 2026-07-03 (commits `e6da2f0`, `76314d7`). Le principe : l'agent ne vit plus dans le présent, chaque réponse est située dans l'histoire du projet. Incarnation produit de [[concepts/memory-llm-vs-wiki-persistant]] : la mémoire n'est plus un sac de faits, c'est une timeline + des décisions + des résultats mesurés.

**Le prompt reçoit, dans l'ordre** : contexte client → décisions SEO actées (contraintes dures) → état SEO actuel (clics/impressions 28 j vs 28 j précédents, depuis `gsc_daily_snapshots`, zéro appel GSC ajouté) → journal du projet (10 derniers événements datés, table `project_events`) → recommandations déjà émises avec leurs résultats mesurés (`agent_recos`) → concepts déjà expliqués (jamais réexpliqués) → signaux des crons → mémoire ponctuelle → question.

**Boucle de résultat** (le différenciateur) : toute analyse se termine par une « prochaine meilleure action » chiffrée (bloc `nba` rendu en carte : action, impact /5, minutes, ≈ clics/mois, confiance %, pourquoi ; chaque chiffre dérive des outils consultés, champ non étayable = omis). L'outil `track_reco` l'enregistre avec ses métriques de départ ; le cron `cron-reco-outcome` (7h15 UTC) re-mesure position et clics dans la GSC à J+14 et J+30, écrit le delta réel, notifie, et le résultat revient dans le prompt des sessions suivantes. Même logique que la boucle sortie→apprentissage du vault ([[preuves/index]]), appliquée au produit.

**Mémoire à 3 régimes** dans `project_memory` : faits ponctuels (update_memory), décisions SEO durables (`decision:*`, outil `record_decision` : refus d'une tactique, CMS, URLs intouchables, périmètre de mots-clés ; contraintes dures respectées à 6 mois), concepts expliqués (`explained:*`). La distillation de fin de session (`distill-session`) extrait automatiquement les trois + les événements notables.

**Proactivité** : l'agent ouvre la conversation sur un projet (point du jour assemblé depuis `daily-briefing`, zéro appel LLM, 1×/jour/projet, chips d'action cliquables) ; `suggest_agent` couvre les 7 personas (jade, indigo, onyx, ambre, carmin, azur, veille) ; `open_view` propose un bouton vers l'onglet pertinent ; continuité de profondeur (un follow-up court au milieu d'un audit reste sur le tour profond).

**Économie de tokens** : voix + règle fondamentale (~4 600 tokens statiques) déplacées dans la tête cacheable du prompt (servies à 10 % du tarif), rappel court en fin de queue. Blocs temporels plafonnés (~1 800 tokens max). Évals de régression : `evals/run-evals.mjs` (10 prompts dorés, règles déterministes : wording, structure Observation/Action/Impact, nba présent sur les analyses), à lancer avant tout déploiement d'une modification du prompt.

## DA « Métriques » des onglets Suivi & Analyse (2026-07-03)

Refonte visuelle validée par Tim (proposition 2 sur 5, maquettes dev `/design-onglets`) : tous les onglets (Alertes, Indexation, Sitemaps, Suivi de positions, Cartographie, Rythme hebdo + les dashboards partagés) parlent le langage de l'onglet Performances. Règles durables :
- Cartes métriques en dégradé, une couleur par métrique (langage GSC : bleu clics, violet impressions, teal CTR, orange position, rouge chutes, vert hausses) : `MetricCards` + `GSC` dans `src/lib/dashKit.jsx`.
- Deltas verts (gains) / rouges (pertes), plus jamais le bleu accent. Chips de statut colorées (`StatusChip`).
- Barres de DONNÉES en dégradés de bleu (`#3450C0` → `#D6DEF6`), jamais d'ocre : l'ambre reste réservé au sémantique (statut, quota, sévérité).
- Le SENS d'une évolution = flèche verte haut / rouge bas (`TrendArrow`, vizKit), jamais un mini-trait. Listes d'URLs = une ligne par URL avec delta, jamais un paragraphe à virgules.
- Tableaux : en-tête gris neutre arrondi (le bandeau bleu reste réservé aux tableaux du chat), coins 14 px, `border-collapse: separate` (collapse ignore border-radius).

## Refonte majeure — agent sous Claude (2026-06-13)

Bascule complète de la couche IA **Gemini → Claude** (les modèles `gemini-3.1-*` renvoyaient 404 ; décision de Tim : reconstruire sous Claude et faire que l'agent réponde *avec sa doctrine, ses skills et son vault Obsidian*). Le snapshot Gemini plus bas est conservé pour historique mais **périmé**. Détail session par session : journal de dev `qadence/Journal.md`.

**Architecture runtime actuelle**
- **Front** : SPA **Vite + React** (`src/`, repo `~/Code/qadence`, GitHub `timboussardon-sketch/qadence`) sur Netlify (`qadence.io`). Fini Next.js.
- **Agent conversationnel** : edge function `seo-agent` réécrite sous **Claude Messages API** (boucle tool-use + streaming SSE, contrat front inchangé). Outils : `search_kb` (vault), `gsc_query` (GSC réelle), `load_skill` (doctrine), `update_memory`. Ancien Gemini gardé en `seo-agent-gemini-legacy` (rollback).
- **Vault Obsidian branché en direct** : `search_kb` interroge la table `kb_chunks` (pgvector, embeddings `gemini-embedding-001`) du Supabase Fusionn via l'edge `kb-search`. L'agent répond donc avec le second cerveau de Tim, pas du SEO générique — opérationnalise [[concepts/persistent-wiki-vs-rag]].
- **Doctrine = table `skills`** alimentée verbatim depuis `~/.claude/skills/seo-*` (script `qadence/sync-skills.py`). Audit de correspondance fait le 2026-06-13 : 26 slugs = doctrine identique à 100 %. Voix `ton_de_voix_tim` en système.

**Nouvelles capacités (front)**
- **Espace compte** plein écran (`AccountPage`) : Profil · Abonnement (portail Stripe via edge `stripe-portal`) · Connexions · Statistiques.
- **GSC multi-comptes / multi-sites** : edge `gsc-properties` (propriétés groupées par compte Google), sélecteur de propriété par projet, bouton « connecter un autre compte ». Résolveur GSC tolérant à la fragmentation des sessions anonymes (token résolu par site/domaine, plus seulement par `user_id`).
- **Lanceur de skills** dans la barre du haut (`SkillLauncher`) : liste les 36 skills doctrine, clic = `load_skill` + exécution.
- Design **« Google mono »** : Roboto / Roboto Mono, palette monochrome Google, accent bleu unique `#1A73E8`, échelle/grille/radius des règles Fusionn.

Supabase : projet `ytgbnqqmcnhmscbvhoin` (« Radarr »), partagé avec [[project_lenkrr|leenq]] + Fusionn.

## Architecture (snapshot v112, 2026-05-08 — PÉRIMÉ, ère Gemini)

> ⚠️ Tout le bloc qui suit (Architecture, agents cron, Tools, Skills, Tables, Patterns, Garde-fous, TODOs) décrit l'**architecture Gemini d'avril-mai 2026, conservée pour historique**. Pour l'état réel, voir « Refonte sous Claude (2026-06-13) » plus haut. Snapshot code à jour : `raw/agents/qadence-seo-agent/snapshot-2026-06-13-claude/`.


| Couche | Stack |
|---|---|
| Frontend | Next.js 15 App Router · React 19 · Netlify (`qadence.io`) |
| Backend | Supabase Edge Functions · Deno/TS (`api.qadence.io`) |
| AI | Gemini 2.5 Pro (raisonnement) + 2.0 Flash (rapidité) |
| DB | Supabase PostgreSQL |
| Auth | Google OAuth 2.0 (scope webmasters + userinfo) |
| Scheduler | pg_cron Supabase (anciennement cron-job.org externe) |

Repo local : `/Users/timothee/Downloads/qadence/` (transfer package v112). Manifest source-of-truth : `qadence.yaml`.

## 6 agents cron-driven (`agents/registry.ts`)

| Agent | Schedule | Skill | Edge function |
|---|---|---|---|
| `watcher` | 8h/j | `audit_gsc` | `cron-watcher` (alias Botbeat / Veilleur) |
| `quickwin` | Lundi 7h | `quick_win` | `cron-quickwin` |
| `cannibal` | Lundi 8h | `cannibalisation` | `cron-cannibal` |
| `brief` | Trigger | `brief_contenu` | `agent-runner` (récursif depuis Watcher) |
| `scorer` | Trigger | `content_scoring` | `agent-runner` — OpenDecoder 4-score (Pertinence + Qualité + Potentiel + AEO), 16 LLM queries |
| `cocon` | 1er du mois | `maillage_interne` | `cron-cocon` |

## Tools (deux niveaux)

**6 tools natifs (registry `tools/registry.ts`)** : `gsc` · `page_meta` · `serp` · `llm_citation` (GEO multi-LLM) · `sitemap` · `embeddings` (Gemini text-embedding-004 + cosine).

**10 function calls exposés à Gemini par `seo-agent` edge function** (snapshot 2026-04-30, ~2643 LoC) : `fetch_gsc_data` · `fetch_ga4_data` · `load_skill` · `fetch_serp` · `fetch_page_content` · `fetch_page_meta` · `fetch_pagespeed` · `score_content` (OpenDecoder v2) · `parse_keyword_planner` · `update_project_memory`.

## Skills (sync MD ↔ DB)

Présents en MD `skills/` (et miroir Claude Code `/seo-*`) : `maillage-interne-gsc` · `seo-quick-win` · `seo-cannibalisation` · `seo-brief-contenu` · `seo-cluster-aeo` · `seo-entites-vectorielles` · `seo-peurs-objections` · `seo-product-led` · `seo-programmatique-pseo` · `seo-workflow-article` · `content-pipeline` · `linkedin-post-tim` · `revue-presse-iteration`.

DB-only (table `skills` Supabase, à puller) : `audit_gsc` · `score_geo` · `content_gaps` · `intention_recherche` · `query_requete` · `faq_query` · `structure_hn` · `agent_critique` · `mots_cles_decisionnels` · `gsc_rules` · `memory_rules` · `strategie_seo`.

Format alternatif testé : `skills-hermes-format/` (sous-dossier + `SKILL.md` frontmatter, à la Hermes).

## Tables Supabase clés

`google_connections` (OAuth + plan + messages_used) · `projects` · `project_memory` (mémoire agent par projet, key/value — pattern wiki persistant côté DB) · `optimizations` · `rank_history` · `botbeat_reports` · `weekly_push_reports` · `rate_limits` · `tools` · `skills` · `gsc_cache`.

## Patterns architecturaux notables

- **Skill loader sémantique** via embedding Gemini → matche message utilisateur ↔ skills disponibles
- **Mémoire projet persistante** indexée par `(user_id, domain)` — incarne [[concepts/persistent-wiki-vs-rag]] et [[concepts/memory-llm-vs-wiki-persistant]] côté DB
- **Scoring obligatoire** via `score_content` qui appelle l'engine OpenDecoder v2 après tout livrable contenu ([[sources/2026-04-15-opendecoder-seo-scoring-system]])
- **Skills en markdown** chargés dynamiquement (pattern [[concepts/cli-tools-optional]])
- **Manifest YAML source-of-truth** (`qadence.yaml`) — agents/tools/cron/paths centralisés, pattern Hermes-inspired

## Garde-fous notables (system prompt agent)

- INTERDIT d'écrire pseudo-code dans la réponse texte → toujours appeler les FUNCTION CALLS
- Anti-contamination : contexte projet ≠ choix du skill (seul le message utilisateur décide)
- Réponses courtes après clarification → confirmation, pas reposition
- GSC connectée → ne JAMAIS demander secteur/ville quand la question porte sur les performances

## TODOs connus

- Sprint 0 : remplacer la SPA minifiée par un repo Vite+React clean
- Sprint 2 : "Stratège" (cron lundi, `weekly_plan` 3 actions)
- Récupérer 11 edge functions + 11 skills DB-only depuis Supabase
- Re-soumettre Google Ads API Basic Access

## Pertinence pour la KB

- Première implémentation **agent en production** documentée dans la KB Tim
- Opérationnalise [[concepts/agentic-search]] côté infrastructure (vs MAGEO/AgenticGEO côté optimisation contenu)
- Tool `score_content` rend [[sources/2026-04-15-opendecoder-seo-scoring-system]] exécutable dans une boucle d'agent
- Concrétise les 4 piliers ([[concepts/methode-organikk-4-piliers]]) en produit : Watcher = Surprise/Grounding monitoring, Quickwin/Cannibal = Grounding, Cocon = pSEO, Scorer/llm_citation tool = AEO

## Pages liées

[[sources/2026-04-30-qadence-seo-agent-snapshot]] · [[sources/2026-04-15-opendecoder-seo-scoring-system]] · [[concepts/agentic-search]] · [[concepts/data-proprietaire]] · [[concepts/persistent-wiki-vs-rag]] · [[concepts/memory-llm-vs-wiki-persistant]] · [[concepts/cli-tools-optional]] · [[concepts/methode-organikk-4-piliers]] · [[entities/organikk-co]]
