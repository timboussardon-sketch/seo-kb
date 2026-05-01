---
type: etude
source_type: paper
title: "CORE: Controlling Output Rankings in Generative Engines for LLM-based Search"
aliases: ["CORE", "CORE ranking", "Jin et al. 2025", "ProductBench"]
tags: ["core", "ranking", "generative-engine", "manipulation", "llm-search", "e-commerce", "shadow-model", "black-box"]
created: "2026-04-13"
updated: "2026-04-13"
sources: ["arXiv:2602.03608"]
confidence: haute
status: actif
auteurs: ["Haibo Jin", "Ruoxi Chen", "Peiyan Zhang", "Yifeng Luo", "Huimin Zeng", "Man Luo", "Haohan Wang"]
institution: "UIUC / HKUST / Intel Labs"
publication: "Preprint, février 2025"
date_publication: "2025-02-03"
arxiv: "2602.03608"
---

# CORE — Contrôler les rankings dans les moteurs génératifs

## Pourquoi cette étude est critique

Première étude qui démontre qu'on peut **contrôler le ranking de sortie** des LLM en search en modifiant uniquement le contenu textuel des items. Implication directe : le SEO pour les GE est un problème d'optimisation du contenu, pas de backlinks.

## Problème posé

Dans le LLM-based search (ChatGPT, Perplexity, etc.), le LLM synthétise les résultats de recherche en un ranking. Ce ranking suit largement l'ordre de retrieval initial. Mais le contenu textuel de chaque item peut influencer la position finale. CORE exploite cette faille.

## Méthode CORE

Deux approches pour promouvoir un item du dernier rang vers le Top-1 :

### 1. Shadow-Model (accès aux embeddings)
- Clone le comportement du LLM synthétisant avec un shadow model (Llama-3.1-8B)
- Optimise le texte de l'item cible par gradient descent dans l'espace embedding
- Reconstruction discrète du texte optimisé
- **Stratégie String-based** : chaîne de tokens optimisée, non lisible

### 2. Query-Based (black-box pur)
- Boucle itérative : Generator → Optimizer → re-query
- Deux stratégies naturelles :
  - **Reasoning-based** : ajoute une logique CoT qui guide le LLM vers l'item cible
  - **Review-based** : ajoute un narratif d'achat crédible style "After buying this item, I compared it to alternatives and found..."

## Résultats sur ProductBench

Benchmark : 15 catégories de produits × 200 produits chacune, top-10 Amazon.

| Stratégie | Top-5 PSR | Top-3 PSR | Top-1 PSR |
|---|---|---|---|
| Baseline (sans CORE) | 0% | 0% | 0% |
| String-based | ~58% | ~46% | ~34% |
| Reasoning-based | **91.4%** | **86.6%** | **80.3%** |
| Review-based | ~93% | ~88% | ~82% |

Le dernier item passe en Top-1 dans **80%+ des cas** avec Reasoning ou Review.

## Findings critiques

### 1. Le ranking LLM suit le retrieval à ~100%
Baseline PSR = 0% — le LLM reproduit quasi systématiquement l'ordre de retrieval. Le contenu textuel peut renverser cette tendance.

### 2. Review > Reasoning > String pour la naturalité
- String : perplexité ~1500 (détectable immédiatement)
- Reasoning : perplexité ~72 (modérément détectable, 62%)
- Review : perplexité ~32 (quasi indétectable, 18% seulement)

### 3. Robuste cross-model
Testé sur GPT-4o, Gemini-2.5, Claude-4, Grok-3. Les stratégies transfèrent entre modèles. Review est la plus robuste au transfert.

### 4. La position d'insertion compte
Review en position 1 → domine le Top-1 (>70%). Reasoning en position 1 → domine aussi. En position 3, les deux perdent en efficacité.

### 5. Implications sécurité
Les filtres de défense (perplexité, patterns, longueur) sont **insuffisants**. La stratégie Review passe à travers tous les filtres testés.

## Ce que ça change pour le SEO

- Le contenu textuel peut **renverser le ranking** dans les moteurs génératifs
- Les descriptions produit de style "review authentique" ou "raisonnement structuré" sont les plus efficaces
- C'est une **menace et une opportunité** : les concurrents peuvent manipuler les réponses IA, mais les marques légitimes aussi
- Le SEO classique (backlinks, domain authority) est insuffisant — le contenu on-page est le nouveau champ de bataille

## Concepts liés

[[agentic-search]] · [[grounding-score]] · [[fully-meets]] · [[surprise-gap]]

## Études liées

[[etude-geo-aggarwal-2024]] · [[etude-sageo-arena-2025]] · [[etude-raid-gseo-2025]] · [[etude-searchllm-2026]]

## Skills mobilisés

[[skill-entites-vectorielles]] · [[skill-product-led-seo]] · [[skill-peurs-objections]]
