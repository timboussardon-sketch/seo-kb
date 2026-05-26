---
type: source
source_type: paper
title: "Titans : Architecture à Mémoire Neurale — Google DeepMind"
aliases: []
tags: []
created: 2026-04-12
updated: 2026-04-12
sources: 0
confidence: medium
status: draft
---

# Titans : Architecture à Mémoire Neurale — Google DeepMind

## Référence
- Auteurs : Google DeepMind
- Date : 2024-2025
- Source : Publication recherche Google DeepMind
- Lien : non disponible (paper interne / preprint)

## Résumé
- Architecture en 3 couches : attention de base (core), mémoire neurale, mémoire persistante
- Introduit la **mémorisation au moment du test** (test-time memorization) : le modèle décide en temps réel ce qu'il retient
- Le mécanisme central est la **Surprise Metric** : l'information inattendue (haute surprise) est stockée en mémoire neurale, l'information attendue (basse surprise) est oubliée
- Le **Weight Decay** (décroissance adaptative) gère la capacité finie de la mémoire : les informations moins pertinentes sont progressivement effacées
- Implications directes pour le SEO : le contenu "consensus" (basse surprise) est oublié, le contenu avec data propriétaire unique (haute surprise) est mémorisé par les LLM

## Concepts clés extraits
- [[surprise-metric]] — gradient d'information, haute surprise = stockage mémoire
- [[weight-decay]] — oubli adaptatif, gestion capacité finie
- [[surprise-gap]] — application SEO : créer du contenu qui contredit le consensus pour forcer la mémorisation
- [[grounding-score]] — cosine similarity enrichie par la surprise metric
- [[information-gain]] — information nouvelle qui change la perception

## Pertinence pour la KB
Fondation théorique de toute la doctrine SEO post-SGE de Tim. Le concept de Surprise Gap (80% consensus + 20% data unique) découle directement de l'architecture Titans. Explique pourquoi le contenu générique IA ne ranke plus et pourquoi la data propriétaire est le nouveau moat.

## Citations dans la KB
- raw/notes/seo-ia-tim.md (analyse approfondie)
- wiki/entities/titans.md
- wiki/concepts/surprise-metric.md
- wiki/concepts/weight-decay.md
- wiki/syntheses/doctrine-seo-post-sge.md
