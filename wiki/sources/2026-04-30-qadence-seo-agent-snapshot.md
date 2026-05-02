---
type: source
source_type: doctrine
title: "Qadence SEO Agent — snapshot Edge Function Supabase (2643 LoC)"
aliases: [qadence-seo-agent, qadence-snapshot]
tags: [agent, supabase, edge-function, deno, dispatcher, gsc, opendecoder, claude-tool-use]
created: 2026-04-30
updated: 2026-04-30
sources: 1
confidence: high
status: stable
---

# Qadence SEO Agent — snapshot Edge Function Supabase

**Type** : référence figée du dispatcher Qadence à un instant T (2026-04-30, **2643 LoC**). Edge Function Supabase (Deno + `@supabase/supabase-js`) qui orchestre un agent SEO connecté GSC.
**Repo source** : `qadence` (Cursor workspace)
**Fichier raw** : `raw/agents/qadence-seo-agent/README.md` + `raw/agents/qadence-seo-agent/index.ts`

## Architecture

L'agent contient à la fois la **doctrine** (system prompt en français, ~600 lignes) et la **logique d'exécution** (~2000 lignes). Reçoit un message utilisateur, charge le contexte projet (mémoire + GSC), choisit un tool, et répond avec des **données réelles** plutôt que des templates.

**Principe directeur du prompt** : *agir, pas annoncer*. Si la GSC est connectée et la question porte sur trafic/positions/CTR, l'agent fetch immédiatement plutôt que de dire "je vais analyser".

## 9 tools exposés

| Tool | Rôle |
|---|---|
| `fetch_gsc_data` | Pages, requêtes, positions, clics, impressions ([[concepts/data-proprietaire]]) |
| `fetch_ga4_data` | Trafic et conversions GA4 |
| `load_skill` | Déclenche un skill propriétaire (mots-clés décisionnels, content gaps, [[concepts/fully-meets|stratégie actionnelle]], etc.) |
| `fetch_serp` | SERP via Custom Search API (cohérent avec stack autorisé [[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]]) |
| `fetch_page_content` / `fetch_page_meta` | Scrape ciblé d'URL |
| `fetch_pagespeed` | PSI mobile/desktop |
| `score_content` | **Scoring [[sources/2026-04-15-opendecoder-seo-scoring-system|OpenDecoder v2]]** (obligatoire après tout livrable contenu) |
| `parse_keyword_planner` | Ingestion d'un export Google Keyword Planner |
| `update_project_memory` | Persiste une décision/contexte pour les futures sessions |

## Patterns architecturaux

- **Skill loader sémantique** : `loadRelevantTools` + `retrieveRelevantSkills` utilisent l'embedding **Gemini** pour matcher le message utilisateur aux skills disponibles dans la table `tools`
- **Mémoire projet** : `loadProjectContext` + `updateProjectMemory` lisent/écrivent dans une table Supabase indexée par `(user_id, domain)` — pattern proche d'un **wiki persistant côté DB** ([[concepts/memory-llm-vs-wiki-persistant]])
- **Scoring** : `scoreContent` appelle l'engine OpenDecoder v2 (référence systématique pour évaluer un livrable avant publication)
- **Skills en markdown** : skills stockés en table, format texte, chargés dynamiquement — pattern [[concepts/cli-tools-optional]] où l'agent reste piloté par fichiers texte plutôt que code dur

## Garde-fous notables (extraits du system prompt)

- **INTERDIT** d'écrire `print()` ou pseudo-code dans la réponse texte → l'agent doit appeler les FUNCTION CALLS, pas les annoncer
- **Règle anti-contamination** : le contexte projet (mémoire, nom, domaine) ne doit JAMAIS influencer le choix du skill — seul le message utilisateur décide
- **Réponses courtes** (`oui`, `clics`, `les deux`) après une question de clarification → interpréter comme confirmation et agir, pas reposer la question
- Si la GSC est connectée → ne JAMAIS demander le secteur/ville quand la question porte sur les performances (déductible des requêtes GSC)

## Déploiement

```bash
cd /Users/boussardontimothee/Downloads/Cursor/qadence
supabase functions deploy seo-agent
```

Au 2026-04-30, déploiement bloqué sur authentification (pas de creds locaux ni de `SUPABASE_ACCESS_TOKEN`). Login interactif requis : `npx supabase login` puis `npx supabase link --project-ref <REF>`.

## Pourquoi c'est dans le vault

- **Documenter l'architecture** des tools et la doctrine du system prompt pour réutilisation dans d'autres agents (Organikk, futurs clients)
- **Comparer les évolutions** du prompt avec les versions futures (le repo qadence évolue, ce snapshot reste fixe)
- **Extraire des patterns réutilisables** : anti-contamination, agir-pas-annoncer, mapping skill ↔ message via embedding sémantique

## Apports à la KB

- Première **entité agent** documentée comme source — pattern réutilisable pour de futurs agents Tim
- Implémentation concrète de [[concepts/agentic-search]] côté infrastructure (vs le côté optimisation contenu couvert par MAGEO/AgenticGEO)
- Le tool `score_content` opérationnalise [[sources/2026-04-15-opendecoder-seo-scoring-system]] dans un agent en production
- Cohérent avec [[concepts/persistent-wiki-vs-rag]] : Qadence n'est PAS un RAG stateless — il maintient une mémoire projet par `(user_id, domain)` qui s'accumule dans le temps
- Stack Edge Function Supabase : précédent technique pour un futur agent Organikk

## Limites

- Snapshot daté (2026-04-30) — le repo continue d'évoluer, ce wiki page sera désynchronisé
- Pas de métriques de performance terrain (combien de requêtes traitées, latence moyenne, taux de hallucination)
- Stack 100 % Supabase = lock-in. Pas de discussion documentée sur la portabilité vers Vercel ou Cloudflare Workers
- 2643 LoC dans un seul `index.ts` — pas de découpage modulaire à date

## Pages liées

[[concepts/agentic-search]] · [[concepts/data-proprietaire]] · [[concepts/persistent-wiki-vs-rag]] · [[concepts/memory-llm-vs-wiki-persistant]] · [[concepts/cli-tools-optional]] · [[concepts/fully-meets]] · [[sources/2026-04-15-opendecoder-seo-scoring-system]] · [[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[entities/organikk-co]]
