---
type: entity
title: DPR (Dense Passage Retrieval)
aliases: [dpr, dense-passage-retrieval]
tags: [architecture-ia, recherche-semantique, embeddings, passage-ranking]
created: 2026-04-12
updated: 2026-04-12
sources: 1
confidence: high
status: stable
---

# DPR (Dense Passage Retrieval)

**Sous-catégorie taxonomique** : Architectures IA (§4.1 AGENTS.md v2.2).

Architecture de recherche neuronale développée par Facebook AI Research (2020). Encode requêtes et passages en **vecteurs denses** dans un même espace, puis mesure leur proximité par similarité cosinus.

## Ce que cette KB sait

- DPR utilise deux encodeurs BERT séparés : un pour la requête, un pour le passage
- Chaque texte est transformé en un vecteur dense (embedding) dans un espace à haute dimension
- La pertinence = **proximité cosinus** entre les deux vecteurs
- Surpasse BM25 sur les requêtes complexes/ambiguës où la correspondance lexicale échoue
- Utilisé comme base dans les systèmes RAG (Retrieval-Augmented Generation) modernes

## Pertinence SEO/GEO

- DPR est le mécanisme technique derrière le [[concepts/passage-ranking]] : Google évalue chaque passage (bloc H2) indépendamment, pas seulement la page entière
- Le [[concepts/grounding-score]] repose sur le même principe : cosine similarity entre le vecteur requête et le vecteur passage
- Justifie la doctrine de Tim sur les **H2 comme vecteurs sémantiques distincts** : chaque H2 est encodé séparément par un système type DPR
- L'architecture DPR explique pourquoi un article peut ranker sur une requête grâce à un seul passage pertinent, même si le reste de la page est hors-sujet

## Pages liées

[[entities/bm25]] · [[entities/bert]] · [[concepts/passage-ranking]] · [[concepts/grounding-score]] · [[concepts/ingenierie-semantique-inversee]]
