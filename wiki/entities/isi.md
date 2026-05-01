---
type: entity
title: ISI (Index Serve Infrastructure)
aliases: [isi, index-serve-infrastructure]
tags: [infrastructure-google, index, serving, ranking]
created: 2026-04-12
updated: 2026-04-12
sources: 1
confidence: medium
status: stable
---

# ISI (Index Serve Infrastructure)

**Sous-catégorie taxonomique** : Infrastructure Google (§4.1 AGENTS.md v2.2).

Infrastructure de Google déterminant **quels documents sont servis pour quelles requêtes**. Couche intermédiaire entre l'index (stockage des pages crawlées) et le ranking (classement des résultats).

## Ce que cette KB sait

- ISI décide quels documents de l'index sont **candidats** pour une requête donnée, avant même que le ranking ne s'applique
- C'est le mécanisme de **recall** : sur des milliards de pages indexées, ISI réduit le pool à quelques milliers de candidats
- Les pages non servies par ISI pour une requête donnée ne peuvent jamais ranker, quelle que soit leur qualité
- Le crawl budget, l'indexation, et les signaux de qualité macros (domaine, PageRank) influencent la sélection ISI

## Pertinence SEO/GEO

- ISI est la couche invisible qui explique pourquoi certaines pages "disparaissent" des résultats même sans pénalité directe
- Connexion avec la Phase 1 de la [[concepts/triade-serp]] (Document Ranking) : ISI est le pré-filtre avant le Document Ranking
- Les pages orphelines (sans maillage interne) risquent de ne pas être servies par ISI → cf. skill-maillage-interne
- Le crawl budget limité justifie la recommandation de Tim : "supprimer les pages sans valeur pour libérer du budget crawl"

## Pages liées

[[concepts/triade-serp]] · [[entities/bm25]] · [[entities/rankbrain]]
