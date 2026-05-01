---
type: entity
title: RankBrain (Google)
aliases: [rankbrain, rank-brain]
tags: [algorithme-google, machine-learning, ranking, interpretation-requetes]
created: 2026-04-12
updated: 2026-04-12
sources: 0
confidence: high
status: stable
---

# RankBrain (Google)

**Sous-catégorie taxonomique** : Algorithmes Google (§4.1 AGENTS.md v2.2).

Premier signal de ranking basé sur le machine learning, déployé par Google en 2015. Troisième signal le plus important dans le ranking au moment de son lancement.

## Ce que cette KB sait

- Gère les requêtes jamais vues auparavant (~15% des requêtes quotidiennes sont nouvelles)
- Interprète l'**intention** derrière la requête au-delà de la correspondance exacte des mots-clés
- Transforme les requêtes en vecteurs mathématiques pour trouver des correspondances sémantiques
- Fonctionne en tandem avec [[entities/bert]] et [[entities/neural-matching]]
- Toujours actif dans le core ranking Google en 2026

## Pertinence SEO/GEO

- A initié le passage du SEO "mots-clés exacts" vers le SEO "intention de recherche"
- Pertinent pour la doctrine de la KB : les requêtes longues (4 → 24 mots, cf. calls prospects) sont mieux comprises grâce à RankBrain
- Le [[concepts/grounding-score]] est une évolution du même principe : matching vectoriel query ↔ contenu
- Renforce l'approche de Tim : trouver des mots-clés business par intention, pas par volume

## Pages liées

[[entities/bert]] · [[entities/neural-matching]] · [[concepts/grounding-score]] · [[concepts/ingenierie-semantique-inversee]]
