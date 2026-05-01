---
type: concept
title: Weight Decay + biais de récence
aliases: [weight-decay, forgetting-gate, biais-recence]
tags: [titans, freshness, ranking, rrf, seo-ia]
created: 2026-04-11
updated: 2026-04-13
sources: 2
confidence: medium
status: stable
---

# Weight Decay + biais de récence

Mécanisme d'oubli de l'architecture [[entities/titans]] qui, selon [[sources/2026-04-11-seo-ia-tim]], **explique architecturalement** le biais de récence observé par [[entities/metehan]].

## Définition (du paper)

Pour gérer la capacité finie de la Neural Memory, Titans utilise un **forgetting gate** : un oubli adaptatif qui jette les informations plus nécessaires. Combiné avec le **momentum** (surprise momentanée + passée), ça donne une mémoire qui **favorise structurellement** les informations récentes et surprenantes.

## Le biais de récence observé (Metehan, non ingéré)

[[entities/metehan]] aurait observé que les **résultats top 10 Google sont systématiquement plus récents de 1 à 5 ans**, attribuant cela au paramètre interne `use_freshness_scoring_profile`. Claim **non vérifié indépendamment** — citation secondaire de Tim. `confidence: medium`.

## La thèse de Tim

Ce biais **n'est pas un réglage arbitraire** mais une **nécessité architecturale** :

> "Le modèle est conçu pour oublier les anciennes informations au profit des nouvelles données surprenantes"

Si cette thèse tient :
- Le biais de récence est **inévitable** avec les architectures actuelles, pas un choix éditorial.
- Mettre à jour les contenus n'est pas une "best practice" — c'est une **contrainte de survie** en Neural Memory.
- Le **RRF** doit inclure un coefficient de **Fraîcheur Sémantique** : contenu ancien → poids s'effondrent face à contenu nouveau à fort gradient.
- **Cohérence avec le pattern wiki persistant** : un wiki maintenu par LLM ([[concepts/persistent-wiki-vs-rag]]) produit par construction des updates datés → nourrit le critère de récence.

## Implications SEO concrètes

1. **Contenus statiques structurellement pénalisés** dans le long terme — Weight Decay grignote leurs poids.
2. **Refresh incrémental > rewrite complet**. Des micro-updates à fort gradient maintiennent le contenu "vivant" sans le reset.
3. **Hygiène data schema critique**. YAAD (variante MIRAS) gère les outliers mais pénalise l'incohérence. Prix, dates, stock : zéro tolérance.

## Limites

- **Transfert non validé** : rien ne prouve que Google Search utilise un weight decay similaire à Titans.
- **Dépendance Metehan non ingérée** : le chiffre "1-5 ans" repose sur une seule citation secondaire.
- **Pas de mesure de "gradient suffisant"** en pratique SEO. Reste qualitatif.

## Pages liées

[[sources/2026-04-13-titans-architecture-google-deepmind]] (paper primaire) · [[sources/2026-04-11-seo-ia-tim]] · [[entities/titans]] · [[entities/metehan]] · [[concepts/surprise-metric]] · [[concepts/surprise-gap]] · [[concepts/persistent-wiki-vs-rag]]
