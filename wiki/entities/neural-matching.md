---
type: entity
title: Neural Matching (Google)
aliases: [neural-matching, super-synonym]
tags: [algorithme-google, nlp, ranking, comprehension-semantique]
created: 2026-04-12
updated: 2026-04-12
sources: 0
confidence: high
status: stable
---

# Neural Matching (Google)

**Sous-catégorie taxonomique** : Algorithmes Google (§4.1 AGENTS.md v2.2).

Système de matching sémantique déployé par Google en 2018. Surnommé le système "super-synonyme". Comprend les concepts au-delà des mots-clés exacts.

## Ce que cette KB sait

- Mappe les **requêtes aux pages** en comprenant les concepts sous-jacents, pas juste les mots
- Permet à Google de faire correspondre une requête comme "pourquoi ma TV a des couleurs bizarres" avec une page sur "dépannage écran LCD" sans correspondance lexicale
- Fonctionne au niveau du **document entier** (contrairement au [[concepts/passage-ranking]] qui fonctionne au niveau du passage)
- Complémentaire à [[entities/rankbrain]] (requêtes) et [[entities/bert]] (compréhension contextuelle)
- Affecte ~30% des requêtes selon Google

## Pertinence SEO/GEO

- Fondation du concept d'[[concepts/ingenierie-semantique-inversee]] dans la KB : si Google comprend les concepts, il faut structurer le contenu par concepts (entités, relations) et pas par mots-clés
- Justifie l'approche vectorielle de Fusionn ([[entities/fusionn-io]]) : les entités connectées (Roi-Reine) sont des concepts que Neural Matching comprend
- Le [[concepts/grounding-score]] est l'évolution de ce principe : matching vectoriel multi-dimensionnel
- Renforce l'importance des [[concepts/skill-entites-vectorielles|entités vectorielles]] : mapper les relations sémantiques pour couvrir le champ conceptuel complet

## Pages liées

[[entities/rankbrain]] · [[entities/bert]] · [[entities/fusionn-io]] · [[concepts/grounding-score]] · [[concepts/ingenierie-semantique-inversee]] · [[concepts/passage-ranking]]
