---
type: concept
title: "Détection du slop coordonné (Content Integrity)"
aliases: ["slop coordonné", "content integrity", "adversarial slop"]
tags: [ia, pseo, quality-raters, geo]
created: 2026-07-15
updated: 2026-07-15
sources: 1
confidence: medium
status: draft
---

# Détection du slop coordonné (Content Integrity)

Approche documentée par Google côté modération vidéo ([[sources/2026-07-15-google-slop-detection-s-cts]]) : le système ne vise pas l'usage de l'IA mais la **production coordonnée et massive de contenu synthétique de faible valeur** (« slop »). La décision se prend au niveau du **cluster de comptes**, pas de la page isolée.

## La signature détectée
- narratifs templatés et répétitifs (embeddings de texte + salient terms quasi identiques d'un contenu à l'autre)
- cadence de publication non-humaine (upload pace, time-to-first-upload)
- similarité sémantique forte entre les contenus d'un même groupe de comptes

## Le garde-fou
Google applique un « precision-over-recall mandate » : il distingue « Creative AI Use » de « Adversarial Slop », et le « Cluster requirement » protège le créateur isolé qui utilise l'IA. L'IA n'est pas le motif de sanction ; la mécanique de masse l'est.

## Transfert SEO (analyse, pas preuve)
Un pSEO paresseux présente exactement cette signature : pages quasi identiques, publiées à cadence de robot, sans donnée propre. La défense est la même que dans la doctrine : donnée réelle par page, variation réelle, cadence de publication plausible, différenciation via [[concepts/surprise-gap]]. Voir aussi les 7 règles anti-thin de [[concepts/programmatique-pseo]] et les modèles de [[concepts/pseo-data-driven-models]].

Le raisonnement au niveau cluster renforce l'idée d'une réputation d'entité/domaine, adossée à la [[concepts/data-proprietaire]] plutôt qu'à la page prise isolément.

## Liens
- [[entities/youtube]]
- [[concepts/data-proprietaire]]
