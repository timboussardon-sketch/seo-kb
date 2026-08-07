---
type: concept
title: CLI tools (optionnels, émergents)
aliases: [cli-tools, qmd-wiki]
tags: [pattern-kb, outil, cli, meta, optionnel]
created: 2026-04-11
updated: 2026-08-07
sources: 1
confidence: medium
status: stable
---

# CLI tools (optionnels, émergents)

Position de [[sources/2026-04-11-karpathy-llm-wiki]] sur le tooling : **optionnel par défaut, utile à mesure que la KB grossit**.

> **Mise à jour 2026-08-07** ([[revue-hebdo/2026-W32]] point 6, en miroir de [[concepts/persistent-wiki-vs-rag]]) : la prédiction ci-dessous s'est vérifiée. Le seuil ~100 sources est franchi (110 au 2026-08-07) et l'outil de recherche a émergé exactement au moment prédit — pas `qmd` cité par la source, mais un outil maison (`./kb`, ChromaDB + `paraphrase-multilingual-mpnet-base-v2`, commit 2026-05-26, AGENTS.md §7ter), conforme au principe DIY décrit plus bas (« vibe-code a naive search script as the need arises »). Le point qui reste vrai : le tooling ne s'est pas substitué à l'index markdown, il s'est ajouté par-dessus, filtré par le frontmatter avant la recherche cosinus. Pattern modulaire confirmé, pas contredit.

## Ce que dit la source

> "At some point you may want to build small tools that help the LLM operate on the wiki more efficiently"

Deux messages :

1. **Au début, tu n'as besoin de rien.** `index.md` seul tient jusqu'à ~100 sources. Pas d'embeddings, pas de RAG, pas de pipeline.
2. **Quand ça grossit**, un moteur de recherche sur les markdown devient l'outil le plus évident à ajouter.

## L'option concrète citée : qmd

`qmd` est mentionné comme *"a good option"* — moteur de recherche local pour fichiers markdown, hybride **BM25 + vectoriel + re-ranking LLM**, tout on-device. Double interface :

- **CLI** — l'agent peut shell out
- **MCP server** — l'agent peut l'utiliser comme outil natif

La source ne benchmarke pas `qmd` et ne le compare à aucune alternative. `confidence: medium` parce que la recommandation est verbale, pas chiffrée.

## L'alternative DIY

> "the LLM can help you vibe-code a naive search script as the need arises"

Principe : le besoin de tooling **émerge**. On ne pré-construit pas, on attend que le wiki soit assez gros pour que l'absence d'outil se fasse sentir, puis on code le minimum viable avec l'agent.

## Pourquoi c'est explicitement optionnel

Le pattern entier est présenté comme **modulaire** : *"pick what's useful, ignore what isn't"*. Si ta KB est petite, l'index suffit. Si tes sources sont text-only, pas besoin de download d'images. Si tu ne fais pas de slides, pas besoin de Marp. Le CLI tooling est dans le même bucket — ajoutable à la carte.

## Pages liées

[[sources/2026-04-11-karpathy-llm-wiki]] · [[concepts/persistent-wiki-vs-rag]] · [[entities/obsidian]]
