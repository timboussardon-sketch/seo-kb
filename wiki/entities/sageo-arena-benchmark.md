---
type: entity
title: SAGEO Arena (benchmark pipeline complet — Kim et al. 2025)
aliases: [sageo-arena-benchmark, sageo-arena]
tags: [benchmark, geo, retrieval, reranking, generation, structural]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: high
status: stable
---

# SAGEO Arena (benchmark)

**Sous-catégorie taxonomique** : Ressources / Benchmarks (§4.1).

Premier benchmark qui évalue le GEO **à chaque étape du pipeline** (retrieval → reranking → generation). Publié avec [[sources/2026-04-13-sageo-arena-2025]].

## Composition

- **170 000 documents web** (corpus réaliste vs benchmarks synthétiques précédents)
- Informations **structurelles complètes** par document : title, meta description, headings, schema markup, body text
- Requêtes alignées sur les 3 étapes du pipeline GE

## Architecture évaluée

- **Retriever** : BM25, top-100
- **Reranker** : cross-encoder, top-10
- **Generator** : LLM avec citations inline

Chaque étape = métriques Hit Rate + ΔRank indépendantes.

## Différence vs GEO-Bench

| Axe | [[entities/geo-bench]] | SAGEO Arena |
|---|---|---|
| Volume | 10 000 requêtes | 170 000 documents |
| Étapes évaluées | Génération finale seulement | Retrieval + Reranking + Generation |
| Structural info | Body text principalement | Title + meta + schema + body |
| Usage | Benchmark méthodes GEO | Benchmark pipeline GE complet |

Les deux sont complémentaires, pas substituts.

## Limites

- Corpus anglophone
- "Shopping" domain dégrade avec toutes les optimisations — pas universellement applicable
- Cross-encoder reranker spécifique — ne reflète pas forcément les rerankers de production des GE commerciaux
- Publié 2025, stack backbone LLM évolue

## Pages liées

[[sources/2026-04-13-sageo-arena-2025]] · [[concepts/structural-information-geo]] · [[concepts/metriques-visibilite-geo]]
