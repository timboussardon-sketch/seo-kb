---
type: entity
title: GEO-Bench (benchmark Aggarwal 2024)
aliases: [geo-bench, geo-benchmark-10k]
tags: [benchmark, geo, dataset, aggarwal, kdd-2024]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: high
status: stable
---

# GEO-Bench

**Sous-catégorie taxonomique** : Ressources / Benchmarks (nouvelle sous-catégorie §4.1).

Premier benchmark publiquement disponible pour évaluer les méthodes d'optimisation pour moteurs génératifs. Publié avec [[sources/2026-04-13-geo-aggarwal-2024]].

## Composition

- **10 000 requêtes** total
- **25 domaines** (Arts, Health, Games, Law, Business, Science, etc.)
- **9 types de requêtes**, **7 catégorisations** différentes
- **Distribution** : 80 % informationnelles, 10 % transactionnelles/navigationnelles, 10 % synthétiques
- **Splits** : 8 000 train / 1 000 validation / 1 000 test

**7 datasets sources** : MS Macro, ORCAS-1, Natural Questions, AllSouls, LIMA, Davinci-Debate (Perplexity), GPT-4 Generated Queries.

## Accès

- URL : https://generative-engines.com/GEO/
- Paper : [[sources/2026-04-13-geo-aggarwal-2024]]
- Licence ACM, paper sous Creative Commons Attribution International 4.0

## Limites

- Évaluation 2024 — GE évoluent
- Top 5 sources seulement par requête (hors top 5 non évalué)
- LLM-as-judge pour métriques subjectives (variance admise)
- Anglais principalement
- Single-turn (pas multi-turn conversationnel)

## Pages liées

[[sources/2026-04-13-geo-aggarwal-2024]] · [[concepts/metriques-visibilite-geo]]
