---
type: source
source_type: paper
title: CORE — Controlling Output Rankings in Generative Engines (Jin et al. 2025)
aliases: [core-paper, core-ranking, jin-2025, arxiv-2602.03608]
tags: [paper, core, ranking-manipulation, black-box, productbench, llm-search]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: high
status: stable
---

# CORE — Controlling Output Rankings in Generative Engines (Jin et al. 2025)

**Auteurs** : Haibo Jin, Ruoxi Chen, Peiyan Zhang, Yifeng Luo, Huimin Zeng, Man Luo, Haohan Wang (UIUC / HKUST / Intel Labs)
**Publication** : preprint arxiv, 3 février 2025
**arxiv** : 2602.03608
**Fichier raw PDF** : `raw/etudes-seo/arxiv-2602.03608v1.pdf`
**Fichier raw synthèse** : `raw/etudes-seo/etude-core-ranking-2025.md`

---

## Thèse

Le **contenu textuel seul** peut faire passer un item du dernier rang au Top-1 dans un LLM-based search. Le ranking de sortie des LLM suit largement l'ordre de retrieval initial (baseline PSR = 0 %), mais cette tendance est **renversable** via 3 stratégies d'optimisation textuelle.

## Méthodes testées

### 1. Shadow-Model (accès embeddings)
- Clone LLM synthétisant avec un shadow Llama-3.1-8B
- Optimise le texte cible par gradient descent dans l'espace embedding
- Résultat : **String-based** = chaîne de tokens optimisée, **non lisible** (perplexité ~1500, détection immédiate)

### 2. Query-Based black-box pur — 2 stratégies
- **Reasoning-based** : ajoute une logique Chain-of-Thought qui guide le LLM vers l'item cible. Perplexité ~72, détectable ~62 %
- **Review-based** : ajoute un narratif d'achat crédible *"After buying this item, I compared it to alternatives and found..."*. Perplexité ~32, détectable **18 %** seulement

## Résultats — ProductBench (15 catégories × 200 produits × top-10 Amazon)

| Stratégie | Top-5 PSR | Top-3 PSR | **Top-1 PSR** |
|---|---|---|---|
| Baseline (sans CORE) | 0 % | 0 % | 0 % |
| String-based | ~58 % | ~46 % | ~34 % |
| Reasoning-based | 91.4 % | 86.6 % | **80.3 %** |
| **Review-based** | **~93 %** | **~88 %** | **~82 %** |

→ Le dernier item passe en Top-1 dans **80 %+ des cas** avec Reasoning ou Review.

## Findings critiques

1. **Le ranking LLM suit le retrieval à ~100 %** en baseline — l'ordre initial domine sans manipulation textuelle
2. **Review > Reasoning > String pour la naturalité** — Review est quasi indétectable et la plus efficace
3. **Robuste cross-model** — testé sur GPT-4o, Gemini-2.5, Claude-4, Grok-3. Review transfère le mieux
4. **La position d'insertion compte** — item en position 1 domine le Top-1 (>70 %). En position 3, l'efficacité chute
5. **Les filtres de défense (perplexité, patterns, longueur) sont insuffisants** — Review passe à travers tous les filtres testés

## Implications SEO

- Les **descriptions produit style "review authentique"** sont un levier de ranking GE massif — ni backlinks ni domain authority n'interviennent
- **Le contenu on-page est le nouveau champ de bataille** — pas l'off-page
- **Menace ET opportunité** : concurrents peuvent manipuler ; marques légitimes aussi
- Pour un e-commerce : générer des reviews structurées authentiques = avantage GEO direct
- Pour un SaaS : narratif d'usage client > liste de features

## Limites éthiques

- La frontière entre **optimisation légitime** et **manipulation** est floue
- Le paper documente une vulnérabilité ; son application en production pour manipuler les résultats reviews est éthiquement problématique
- Pour Tim : la méthode Review est intéressante **si** appliquée sur ses propres contenus avec données réelles, pas injectée dans des reviews tiers

## Limites méthodologiques

- ProductBench = domaine e-commerce, pas généralisable automatiquement à tous les secteurs
- Testé sur top-10 Amazon uniquement — distribution de contenu spécifique
- Évaluation 2025 — robustesse cross-model peut bouger avec nouvelles générations

## Pages liées

**Concepts** : [[concepts/answer-first-pattern]] · [[concepts/data-proprietaire]] · [[concepts/product-led-seo]] · [[concepts/agentic-search]]

**Entities** : [[entities/product-bench]]

**Sources liées** : [[sources/2026-04-13-geo-aggarwal-2024]] · [[sources/2026-04-13-sageo-arena-2025]] · [[sources/2026-04-13-raid-gseo-2025]] · [[sources/2026-04-13-searchllm-2026]]
