---
type: entity
title: BERT (Google)
aliases: [bert, bidirectional-encoder-representations-from-transformers]
tags: [algorithme-google, nlp, ranking, comprehension-requetes]
created: 2026-04-12
updated: 2026-04-12
sources: 0
confidence: high
status: stable
---

# BERT (Google)

**Sous-catégorie taxonomique** : Algorithmes Google (§4.1 AGENTS.md v2.2).

**Bidirectional Encoder Representations from Transformers**. Déployé par Google en octobre 2019. Première intégration majeure de deep learning dans la compréhension des requêtes de recherche.

## Ce que cette KB sait

- BERT permet à Google de comprendre le **contexte bidirectionnel** des mots dans une requête (avant ET après chaque mot)
- Impact principal : les prépositions et mots de liaison changent le sens ("vol Paris pour Londres" ≠ "vol Paris de Londres")
- Affecte ~10% des requêtes en anglais au lancement
- Toujours actif dans le ranking Google en 2026
- Fondation du [[concepts/passage-ranking]] : BERT permet d'évaluer des passages individuels, pas seulement des pages entières

## Pertinence SEO/GEO

- BERT a rendu le keyword stuffing obsolète : Google comprend l'intention, pas juste les mots-clés
- Renforce l'importance de la rédaction naturelle et contextuelle
- Précurseur de [[entities/mum]] (1000x plus puissant) et des architectures type [[entities/titans]]
- Le [[concepts/grounding-score]] (cosine similarity) hérite de la logique BERT : matching sémantique, pas lexical

## Pages liées

[[entities/mum]] · [[entities/rankbrain]] · [[concepts/passage-ranking]] · [[concepts/grounding-score]] · [[concepts/ingenierie-semantique-inversee]]
