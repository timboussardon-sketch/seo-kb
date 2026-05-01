---
type: etude
source_type: paper
title: "SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization"
aliases: ["SAGEO Arena", "SAGEO", "Kim et al. 2025", "stage-aware SAGEO"]
tags: ["sageo", "geo", "benchmark", "retrieval", "reranking", "generation", "structural-information", "schema-markup"]
created: "2026-04-13"
updated: "2026-04-13"
sources: ["arXiv:2602.12187"]
confidence: haute
status: actif
auteurs: ["Sunghwan Kim", "Wooseok Jeong", "Serin Kim", "Sangam Lee", "Dongha Lee"]
institution: "Yonsei University / Konkuk University"
publication: "Preprint, février 2025"
date_publication: "2025-02-12"
arxiv: "2602.12187"
---

# SAGEO Arena — Benchmark réaliste pour le GEO

## Pourquoi cette étude est critique

Premier benchmark qui évalue le GEO **à chaque étape du pipeline** (retrieval → reranking → generation) au lieu de ne mesurer que la génération finale. Corpus de 170K documents web avec informations structurelles complètes (title, meta, headings, schema, body text).

## Problème posé

Les benchmarks existants (GEO-bench, AutoGEO, C-SEO Bench) ont 2 failles majeures : (1) ils ne testent que la génération, pas le retrieval ni le reranking, et (2) ils ignorent les informations structurelles (schema markup, headings, meta descriptions) que les vrais moteurs exploitent.

## Architecture SAGEO Arena

Pipeline complet : **Retriever** (BM25, top-100) → **Reranker** (cross-encoder, top-10) → **Generator** (LLM avec citations). Chaque étape est mesurée indépendamment avec Hit Rate et ΔRank.

## Findings majeurs

### 1. Le body text seul DÉGRADE la visibilité

Optimiser uniquement le body text dégrade le retrieval dans TOUTES les stratégies testées. Moyenne : -4.54 Hit Rate, -16% ΔRank au retrieval. Raison : les rewrites remplacent les termes communs par des synonymes rares, réduisant le chevauchement lexical avec les requêtes BM25.

**AutoGEO (le pire)** : -22.35 Hit Rate, -36% au retrieval — les rewrites longues diluent la densité de mots-clés.

### 2. L'information structurelle est le levier principal

Optimiser les éléments structurels (title, meta, headings, schema) donne les meilleurs résultats :
- Retrieval : **+22% Hit Rate, +2.72 ΔRank** en moyenne
- La stratégie "Statistics" sur structural info : **+35% Hit Rate** au retrieval
- Les titles enrichis avec entités/chiffres alignent mieux le document avec les requêtes

### 3. Le reranking est le bottleneck persistant

Toutes les stratégies dégradent le reranking. Les documents top-10 sont très proches en relevance → un micro-changement peut faire passer un doc de rank 10 à rank 11 et l'exclure du generator. 5.8% des documents cibles passent de rank 10 à 11 après optimisation.

### 4. Le placement de la réponse compte énormément

Case study clé : placer la réponse directe dans les premiers paragraphes améliore le reranking. La repousser plus loin le dégrade — même si le contenu est identique.

### 5. Stage-Aware SAGEO (leur méthode)

Optimisation différenciée par étape :
- **Retrieval** : enrichir les champs structurels avec entités clés, chiffres, nombres
- **Generation** : rendre les claims proéminentes et auto-suffisantes, placer la réponse au début
- **Cross-stages** : maintenir la cohérence topique entre paragraphes
- Résultat : **+28% retrieval, +4.86 ΔRank** et **+1.01 ΔRank en generation**

### 6. Le modèle backbone change tout

- LLaMA-3.3-70B domine au retrieval (42.2% win rate) grâce à ses textes courts et denses en mots-clés
- GPT-5-mini domine au reranking (63.1%) et en generation (73.2%) grâce à la cohérence de ses réponses
- Le BM25 favorise les textes courts → les modèles qui génèrent des textes longs perdent au retrieval

## Guidelines pratiques extraites

- Enrichir les champs structurels avec les entités et chiffres clés du body text
- Placer les claims principales au début du document
- Chaque statement doit être auto-suffisant et porter des preuves spécifiques
- S'adapter au domaine : les domaines "Shopping" dégradent avec toutes les optimisations
- Ne PAS diluer le contenu avec des expansions longues

## Concepts liés

[[grounding-score]] · [[agentic-search]] · [[entites-vectorielles]] · [[maillage-interne]] · [[fully-meets]] · [[surprise-gap]]

## Études liées

[[etude-geo-aggarwal-2024]] · [[etude-core-ranking-2025]] · [[etude-raid-gseo-2025]] · [[etude-searchllm-2026]]

## Skills mobilisés

[[skill-entites-vectorielles]] · [[skill-brief-contenu]] · [[skill-cluster-aeo]]
