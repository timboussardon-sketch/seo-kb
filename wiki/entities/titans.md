---
type: entity
title: Titans (architecture)
aliases: [titans-architecture, titans-mac]
tags: [architecture-ia, google-deepmind, neural-memory, surprise-metric]
created: 2026-04-11
updated: 2026-04-13
sources: 2
confidence: high
status: stable
---

# Titans (architecture)

**Sous-catégorie taxonomique** : Architectures IA (§4.1 AGENTS.md v2.2).

Architecture neurale de [[entities/google-deepmind]] qui introduit la **test-time memorization** — mémorisation active pendant l'inférence, sans réentraînement offline. Décrit en détail dans [[sources/2026-04-11-seo-ia-tim]].

## Structure 3 couches

1. **Core (Short-term)** — attention classique sur le focus actuel.
2. **Neural Memory (Long-term)** — réseau neural profond (MLP multi-couches) qui **apprend à mémoriser pendant l'inférence**. Stocke les infos à fort gradient de surprise (cf. [[concepts/surprise-metric]]). Contrairement aux RNN qui compressent dans un vecteur fixe, mémoire **de profondeur variable** = plus de puissance expressive.
3. **Persistent Memory** — connaissances **fixes** sur la tâche. Marques reconnues, entités fortes, faits invariants.

## Mécanismes clés

- **Surprise metric** (gradient) — mesure l'écart mémoire actuelle vs nouvelle input. Haut gradient → mémorisation forcée.
- **Momentum** — combine surprise momentanée + surprise passée pour capturer les séquences pertinentes.
- **Weight Decay (Forgetting gate)** — oubli adaptatif pour gérer la capacité finie. Cf. [[concepts/weight-decay]].

## Résultats benchmarks (du paper)

- **Contextes 2M+ tokens** (vs. ~8k-200k Transformer classique)
- **Outperforms GPT-4** sur BABILong (reasoning long-context) avec moins de paramètres
- Supérieur à Transformer++, Mamba-2, Gated DeltaNet sur C4, WikiText, HellaSwag, PIQA
- Généralise au-delà du texte (DNA, time-series)

## Pertinence SEO (hypothèse Tim, non validée)

Selon [[sources/2026-04-11-seo-ia-tim]], si les moteurs génératifs adoptent une architecture type Titans, la stratégie SEO/GEO passe de *maximiser la pertinence sémantique* à *maximiser le gradient de surprise*. **Aucune confirmation publique** que Google Search utilise Titans. Cf. [[concepts/surprise-gap]].

## Pages liées

[[sources/2026-04-13-titans-architecture-google-deepmind]] (paper, citation primaire) · [[sources/2026-04-11-seo-ia-tim]] · [[sources/2026-04-13-miras-architecture]] · [[entities/google-deepmind]] · [[entities/miras]] · [[concepts/surprise-metric]] · [[concepts/weight-decay]] · [[concepts/grounding-score]]
