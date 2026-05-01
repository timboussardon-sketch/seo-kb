---
type: entity
title: Muvera
aliases: [muvera, multi-vector-retrieval]
tags: [algorithme-google, recherche-semantique, ranking, multi-vecteur]
created: 2026-04-12
updated: 2026-04-12
sources: 1
confidence: medium
status: evolving
---

# Muvera

**Sous-catégorie taxonomique** : Algorithmes Google (§4.1 AGENTS.md v2.2).

Algorithme de Google combinant **recherche vectorielle et structurelle** pour une pertinence sémantique améliorée. Représente un document non pas par un seul vecteur (comme [[entities/dpr|DPR]]) mais par **plusieurs vecteurs** capturant différentes facettes du contenu.

## Ce que cette KB sait

- Muvera encode un document en **multiple vecteurs** (un par section/passage significatif)
- Permet un matching plus fin : une requête peut correspondre à un vecteur spécifique du document sans que l'ensemble soit pertinent
- Combine la structure du document (hiérarchie Hn, position des passages) avec le contenu sémantique
- Évolution du paradigme single-vector (DPR) vers le multi-vector retrieval

## Pertinence SEO/GEO

- Renforce massivement l'importance de la **structure Hn** : chaque H2/H3 génère potentiellement un vecteur distinct dans Muvera
- Justifie la doctrine de Tim sur le [[concepts/passage-ranking]] : "H2 = vecteur sémantique"
- Le [[concepts/grounding-score]] avec Muvera n'est plus un score unique mais un **ensemble de scores** par passage → chaque passage doit être optimisé individuellement
- Connexion avec les [[concepts/skill-entites-vectorielles|entités vectorielles]] de Fusionn : mapper les relations sémantiques aide Muvera à associer le bon vecteur à la bonne requête
- Le brief de contenu (skill-brief-contenu) prend encore plus d'importance : chaque H2 doit cibler un vecteur sémantique distinct et intentionnel

## Pages liées

[[entities/dpr]] · [[entities/bert]] · [[concepts/passage-ranking]] · [[concepts/grounding-score]] · [[concepts/ingenierie-semantique-inversee]] · [[entities/fusionn-io]]
