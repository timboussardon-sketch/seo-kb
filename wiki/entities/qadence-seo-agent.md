---
type: entity
title: "Qadence (qadence.io)"
aliases: [qadence, qadence-io, qadence-seo-agent, qadence-agent, watcher, scorer, botbeat, veilleur]
tags: [agent, produit-tim, supabase, edge-function, deno, nextjs, netlify, gemini, gsc, opendecoder, dispatcher, organikk]
created: 2026-04-30
updated: 2026-05-08
sources: 2
confidence: high
status: stable
---

# Qadence

**Sous-catégorie taxonomique** : Offres / Produits Tim (§4.1) ∩ Architectures IA / Agents (§4.1 — agent en production).

Plateforme SEO agentique de Tim. Frontend `qadence.io` + API `api.qadence.io`. Pitch : *"Votre partenaire SEO connecté à votre GSC, pas un chatbot qui invente."* Cible : praticien SEO sénior, contexte cumulatif entre conversations.

Distinct de [[entities/organikk-co]] (laboratoire public + acquisition) : Qadence = produit SaaS agentique, sortie commerciale de la doctrine 4 piliers ([[concepts/methode-organikk-4-piliers]]).

## Architecture (snapshot v112, 2026-05-08)

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
