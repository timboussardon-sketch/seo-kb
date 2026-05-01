---
type: concept
title: Passage Ranking
aliases: [passage-ranking, passage-indexing]
tags: [google, ranking, nlp, seo-technique]
created: 2026-04-12
updated: 2026-04-13
sources: 3
confidence: high
status: stable
---

# Passage Ranking

Capacité de Google à **ranker un passage spécifique** d'une page plutôt que la page entière. Pertinent pour les Featured Snippets, AI Overviews, et les réponses directes.

## Ce que cette KB sait déjà

- Le [[concepts/workflow-redaction-8-etapes]] intègre un **"passage ancré"** (150-200 mots, dans les 300 premiers mots) conçu pour être extrait en Featured Snippet + un **bloc authorship** (~50 mots) pour Position 0 / AI Overview [[sources/2026-03-31-tim-workflow-redaction]]
- Cité dans les skills brief-contenu et entites-vectorielles [[sources/2026-04-12-tim-skills-seo-proprietary]]
- Connexion avec [[concepts/grounding-score]] : le passage ancré est la **brique opérationnelle** du grounding — c'est le texte que les moteurs extraient

## Fondement architectural — MIRAS

[[sources/2026-04-13-miras-architecture]] (Multi-Resolution Adaptive Summarization, extension Titans) fournit la mécanique : un même contenu encodé à plusieurs granularités (document → section → passage → phrase), chaque niveau matché indépendamment contre l'intention. Justifie structurellement le découpage Hn comme objet d'optimisation à part entière, pas un habillage. Cf. [[entities/miras]].

## Limites

- Transfert MIRAS → passage-ranking en production Google = par analogie, pas par évidence directe
- Pas encore de doc Google officielle dédiée ingérée

## Pages liées

[[sources/2026-04-13-miras-architecture]] · [[sources/2026-04-13-sageo-arena-2025]] (placement réponse dans premiers paragraphes améliore reranking) · [[sources/2026-04-13-searchllm-2026]] (Answer Firstness 97.66 vs 95.05) · [[entities/miras]] · [[concepts/answer-first-pattern]] · [[concepts/grounding-score]] · [[concepts/structural-information-geo]] · [[concepts/workflow-redaction-8-etapes]] · [[sources/2026-04-12-tim-skills-seo-proprietary]]
