---
type: entity
title: "Qadence SEO Agent (Edge Function Supabase)"
aliases: [qadence-seo-agent, qadence-agent, qadence]
tags: [agent, supabase, edge-function, deno, dispatcher, gsc, opendecoder, claude-tool-use]
created: 2026-04-30
updated: 2026-04-30
sources: 1
confidence: high
status: stable
---

# Qadence SEO Agent

**Sous-catégorie taxonomique** : Architectures IA / Agents (extension §4.1 — agent en production, distinct des architectures de recherche pure type Titans/MIRAS).

Edge Function Supabase (Deno + `@supabase/supabase-js`) qui orchestre un agent SEO connecté GSC. **Snapshot 2026-04-30 : 2643 LoC**, dispatcher complet (system prompt français ~600 lignes + logique d'exécution ~2000 lignes).

## Repo source

`qadence` (Cursor workspace, fichier source : `supabase/functions/seo-agent/index.ts`)

## 9 tools exposés

`fetch_gsc_data` · `fetch_ga4_data` · `load_skill` · `fetch_serp` · `fetch_page_content` · `fetch_page_meta` · `fetch_pagespeed` · `score_content` (OpenDecoder v2) · `parse_keyword_planner` · `update_project_memory`.

## Patterns architecturaux notables

- **Skill loader sémantique** via embedding Gemini → matche message utilisateur ↔ skills disponibles
- **Mémoire projet persistante** (table Supabase indexée par `(user_id, domain)`) — pattern wiki persistant côté DB
- **Scoring obligatoire** via `scoreContent` qui appelle l'engine OpenDecoder v2 après tout livrable contenu
- **Skills en markdown** chargés dynamiquement (pattern [[concepts/cli-tools-optional]])

## Garde-fous notables (system prompt)

- INTERDIT d'écrire pseudo-code dans la réponse texte → toujours appeler les FUNCTION CALLS
- Anti-contamination : contexte projet ≠ choix du skill (seul le message utilisateur décide)
- Réponses courtes après clarification → confirmation, pas reposition
- GSC connectée → ne JAMAIS demander secteur/ville quand la question porte sur les performances

## Pertinence pour la KB

- Première implémentation **agent en production** documentée dans la KB Tim
- Opérationnalise [[concepts/agentic-search]] côté infrastructure (vs MAGEO/AgenticGEO côté optimisation contenu)
- Tool `score_content` rend [[sources/2026-04-15-opendecoder-seo-scoring-system]] exécutable dans une boucle d'agent
- Référence pour la conception d'un futur agent Organikk

## Pages liées

[[sources/2026-04-30-qadence-seo-agent-snapshot]] · [[sources/2026-04-15-opendecoder-seo-scoring-system]] · [[concepts/agentic-search]] · [[concepts/data-proprietaire]] · [[concepts/persistent-wiki-vs-rag]] · [[concepts/memory-llm-vs-wiki-persistant]] · [[concepts/cli-tools-optional]] · [[entities/organikk-co]]
