---
type: concept
title: Reciprocal Rank Fusion (RRF)
aliases: [rrf, reciprocal-rank-fusion]
tags: [ranking, algo, seo-technique, freshness]
created: 2026-04-12
updated: 2026-05-16
sources: 1
confidence: medium
status: stable
---

# Reciprocal Rank Fusion (RRF)

Méthode de fusion de rankings issus de plusieurs systèmes de retrieval. Listé en §4.2 d'`AGENTS.md` comme concept attendu.

## Ce que cette KB sait déjà

- [[sources/2026-04-11-seo-ia-tim]] : Tim propose que le score RRF doit inclure un coefficient de **"Fraîcheur Sémantique"** — un contenu ancien, même pertinent, voit ses poids s'effondrer (Weight Decay) face à un contenu nouveau à fort gradient de surprise
- Connexion directe avec [[concepts/weight-decay]] : le biais de récence observé par [[entities/metehan]] serait une conséquence architecturale impactant les scores RRF
- Le skill cluster-aeo cite le RRF : un cluster couvrant toutes les sous-intentions améliore le score global [[sources/2026-04-12-tim-skills-seo-proprietary]]
- Le skill programmatique-pseo l'utilise aussi pour la priorisation

## TODO

Stub étendu. `confidence: medium` car mentionné dans 2 sources, mais aucune source ne décrit le mécanisme RRF en détail (formule, paramètres, papers). À enrichir avec le paper original RRF ou une doc Google.

## Pages liées

[[sources/2026-04-11-seo-ia-tim]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[concepts/weight-decay]] · [[entities/metehan]]
