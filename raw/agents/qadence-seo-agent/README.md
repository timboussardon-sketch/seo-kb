---
type: agent-source
slug: qadence-seo-agent
title: "Qadence — agent SEO connecté GSC (Supabase Edge Function)"
source_local: "~/Code/qadence/supabase/functions/seo-agent/ (repo timboussardon-sketch/qadence)"
source_repo: "qadence (GitHub timboussardon-sketch/qadence)"
runtime: "Deno / Supabase Edge Function"
date_added: 2026-04-30
updated: 2026-06-13
language: typescript
loc: 560
---

# Qadence — agent SEO connecté GSC

> **MISE À JOUR 2026-06-13 — agent reconstruit SOUS CLAUDE.** L'agent ne tourne plus sous Gemini. Le snapshot actuel est dans [`snapshot-2026-06-13-claude/`](./snapshot-2026-06-13-claude/) (`index.ts` + `claude.ts` + `gsc.ts`, ~560 lignes). Le gros `index.ts` (2643 lignes, Gemini, avril) est **conservé pour historique mais périmé**. Tout le reste de cette fiche décrit l'ancienne architecture Gemini.
>
> **Architecture Claude (résumé)** : edge `seo-agent` = boucle Claude Messages API (tool-use + streaming SSE) dans `claude.ts` ; GSC dans `gsc.ts` (résolveur tolérant à la fragmentation des sessions). 4 outils : `search_kb` (vault Obsidian via edge `kb-search` → `kb_chunks` pgvector sur le Supabase Fusionn), `gsc_query` (GSC réelle), `load_skill` (doctrine = table `skills`, synchro depuis `~/.claude/skills` via `seo-kb/qadence/sync-skills.py`), `update_memory`. Voix `ton_de_voix_tim` en système. Front = Vite/React (`src/`), plus Next.js. Détail vivant : [[entities/qadence-seo-agent]] + `seo-kb/qadence/Journal.md`.

Edge Function Supabase (Deno + `@supabase/supabase-js`) qui orchestre un [[agentic-search|agent SEO]] augmentant le consultant. **[Section historique Gemini ci-dessous — périmée.]**

## Ce que fait l'agent

Le fichier contient à la fois la doctrine (system prompt en français, ~600 lignes) et la logique d'exécution (~2000 lignes). L'agent reçoit un message utilisateur, charge le contexte projet ([[ingest-workflow|ingestion de la mémoire]] + GSC), choisit un tool, et répond avec des données réelles plutôt que des templates.

Principe directeur du prompt : **agir, pas annoncer**. Si la GSC est connectée et la question porte sur trafic/positions/CTR, l'agent fetch immédiatement plutôt que de dire "je vais analyser".

## Tools exposés

| Tool | Rôle |
|---|---|
| `fetch_gsc_data` | Récupère pages, requêtes, positions, clics, impressions ([[data-proprietaire]]) |
| `fetch_ga4_data` | Trafic et conversions GA4 |
| `load_skill` | Déclenche un skill propriétaire (mots-clés décisionnels, content gaps, [[fully-meets|stratégie actionnelle]], etc.) |
| `fetch_serp` | SERP via Custom Search API |
| `fetch_page_content` / `fetch_page_meta` | Scrape ciblé d'URL |
| `fetch_pagespeed` | PSI mobile/desktop |
| `score_content` | Scoring OpenDecoder v2 (obligatoire après tout livrable contenu) |
| `parse_keyword_planner` | Ingestion d'un export Google Keyword Planner |
| `update_project_memory` | Persiste une décision/contexte pour les futures sessions |

## Architecture qu'on voit dans le code

- **Skill loader sémantique** : `loadRelevantTools` + `retrieveRelevantSkills` utilisent l'embedding Gemini pour matcher le message utilisateur aux skills disponibles dans la table `tools`.
- **Mémoire projet** : `loadProjectContext` + `updateProjectMemory` lisent/écrivent dans une table Supabase indexée par `(user_id, domain)`. Pattern proche d'un [[memory-llm-vs-wiki-persistant|wiki persistant]] côté DB.
- **Scoring** : `scoreContent` appelle l'engine OpenDecoder v2 (référence systématique pour évaluer un livrable avant publication).
- **Skills en markdown** : skills stockés en table, format texte, chargés dynamiquement — pattern [[cli-tools-optional|CLI-tools-optional]] où l'agent reste piloté par fichiers texte plutôt que code dur.

## Garde-fous notables (extraits du system prompt)

- INTERDIT d'écrire `print()` ou pseudo-code dans la réponse texte — l'agent doit appeler les FUNCTION CALLS, pas les annoncer.
- Règle **anti-contamination** : le contexte projet (mémoire, nom, domaine) ne doit JAMAIS influencer le choix du skill — seul le message utilisateur décide.
- Réponses courtes (`oui`, `clics`, `les deux`) après une question de clarification → interpréter comme confirmation et agir, pas reposer la question.
- Si la GSC est connectée, ne JAMAIS demander le secteur/ville quand la question porte sur les performances — c'est déductible des requêtes GSC.

## Déploiement

```bash
cd /Users/boussardontimothee/Downloads/Cursor/qadence
supabase functions deploy seo-agent
```

Au 2026-04-30 le déploiement bloque sur l'authentification (pas de creds locaux ni de `SUPABASE_ACCESS_TOKEN`). Login interactif requis : `npx supabase login` puis `npx supabase link --project-ref <REF>`.

## Pourquoi c'est dans le vault

Référence figée du dispatcher Qadence à un instant T (2026-04-30, 2643 LoC). Sert à :
- Documenter l'architecture des tools et la doctrine du system prompt pour réutilisation dans d'autres agents (organikk, futurs clients).
- Permettre de comparer les évolutions du prompt avec les versions futures (le repo qadence évolue, ce snapshot reste fixe).
- Extraire des patterns réutilisables (anti-contamination, agir-pas-annoncer, mapping skill ↔ message).

---

**Connecté avec :** [[agentic-search]] · [[data-proprietaire]] · [[ingest-workflow]] · [[fully-meets]] · [[memory-llm-vs-wiki-persistant]] · [[cli-tools-optional]]
