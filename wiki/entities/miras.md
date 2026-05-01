---
type: entity
title: MIRAS (architecture)
aliases: [miras-architecture, multi-resolution-adaptive-summarization]
tags: [architecture-ia, google, passage-ranking, grounding-score, multi-resolution]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: medium
status: stable
---

# MIRAS (architecture)

**Sous-catégorie taxonomique** : Architectures IA (§4.1 AGENTS.md v2.2).

Architecture étendant [[entities/titans]] pour le traitement de contenu à **résolutions multiples**. Décrite dans [[sources/2026-04-13-miras-architecture]]. Auteurs : équipes recherche IA (Google / affiliés) — non précisé dans le raw.

## Mécanisme

Encode un même contenu long à plusieurs granularités (document → section → passage → phrase). Chaque niveau est matché indépendamment contre une intention de requête → retrieval plus fin que le matching page entière.

## Pertinence SEO (hypothèse, non validée publiquement)

- Fondement architectural du [[concepts/passage-ranking]] : chaque H2 = vecteur sémantique distinct
- Affine [[concepts/grounding-score]] : matching cosine sur le segment le plus pertinent vs moyenne diluée du document
- Justifie structurellement la doctrine briefs Tim ([[concepts/ingenierie-semantique-inversee]]) — chaque H2 doit porter un vecteur distinct, au moins un H2 doit créer un [[concepts/surprise-gap]]

## Limites

- Lien paper original non disponible
- Aucun benchmark numérique dans la source
- Transfert vers passage-ranking en production Google = par analogie, pas par évidence directe
- `confidence: medium`

## Pages liées

[[sources/2026-04-13-miras-architecture]] · [[entities/titans]] · [[entities/google-deepmind]] · [[concepts/passage-ranking]] · [[concepts/grounding-score]] · [[concepts/ingenierie-semantique-inversee]]
