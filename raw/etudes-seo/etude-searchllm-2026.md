---
type: etude
source_type: paper
title: "SearchLLM: Aligning Large Language Models with Searcher Preferences"
aliases: ["SearchLLM", "Wu et al. 2026", "RedNote AI Search", "Gated Aggregation"]
tags: ["searchllm", "rlhf", "grpo", "reward-model", "generative-search", "rednote", "alignment", "production", "xiaohongshu"]
created: "2026-04-13"
updated: "2026-04-13"
sources: ["arXiv:2603.10473"]
confidence: haute
status: actif
auteurs: ["Wei Wu", "Peilun Zhou", "Liyi Chen", "Qimeng Wang", "Chengqiang Lu", "Yan Gao", "Yi Wu", "Yao Hu", "Hui Xiong"]
institution: "Xiaohongshu Inc. / USTC / HKUST"
publication: "KDD '26, Jeju, Corée"
date_publication: "2026-08-09"
arxiv: "2603.10473"
---

# SearchLLM — Aligner les LLM avec les préférences des chercheurs

## Pourquoi cette étude est critique

Premier LLM dédié à la **recherche générative open-ended** déployé en production à grande échelle (RedNote/Xiaohongshu, des centaines de millions d'utilisateurs). Introduit un système de reward multi-dimensionnel avec garanties de sécurité non-négociables.

## Problème posé

La recherche générative open-ended sur les grandes plateformes de contenu pose 3 défis simultanés :
- **R1 — Robustesse** : requêtes ambiguës, evidence bruitée/conflictuelle/outdated
- **R2 — Fiabilité (bottom-line)** : factual grounding, sécurité, compliance format — non-négociable
- **R3 — Alignement utilisateur** : brevity vs coverage, novelty vs safety, richesse vs concision

Le conflit R2 vs R3 est le cœur du problème : optimiser pour l'engagement (R3) peut compromettre la factualité (R2).

## Architecture SearchLLM

### Pipeline de recherche générative
Query + Session History → **Intent Planning** → Evidence Selection (multi-source : internal notes, web search, real-time tools) → **Evidence-Grounded Generation** → Final Response

### Système de reward à 2 couches

**Layer I — Bottom-line Constraints (non-négociables)**
- Hallucination & Factual Grounding (vérification phrase par phrase + base de connaissances externes)
- Basic Answer Quality (logique, cohérence, détection de texte gibberish)
- Format Compliance (markdown, longueur)
- Agrégation : **Geometric Mean δ-smoothed (Soft-AND gate)** — si un seul score bottom-line → 0, le reward entier → 0

**Layer II — Behavioral Objectives (optimisables)**
- Robustness to Query & Evidence (intent alignment, gestion des conflits d'evidence)
- Richness & Diversity (claims diversifiées, perspectives multiples)
- Conciseness & Usability (answer-first, réduction redondance, signal-to-noise ratio)
- Évaluation : **LLM judges calibrés par humains** + Weighted Arithmetic Mean

**Reward final** : R(x,y) = B_δ(x,y) × U(x,y) — les behavioral objectives ne comptent QUE si les bottom-line constraints sont satisfaites.

### Gated Aggregation Strategy
Le reward est optimisé par GRPO (Group Relative Policy Optimization). La "gate" géométrique fait que le modèle **lock in** d'abord la sécurité/factualité, puis optimise l'utilité. Élimine le "seesaw effect" entre dimensions.

## Résultats

### Reward alignment (vs human experts)
| Métrique | GenRM | Rubric | **SearchLLM (Ours)** |
|---|---|---|---|
| Hallucination detection | 49-89% | 66-84% | **85-95%** |
| Holistic preference (AUC) | 70.90 | 72.13 | **86.48** |

### A/B test production (RedNote)
- **Valid Consumption Rate (VCR)** : +1.03% (statistiquement significatif, p<0.05)
- **Re-search Rate** : -2.81% (les utilisateurs relancent moins souvent)
- Safety et reliability maintenues

### Offline policy evaluation
GRPO-Gated surpasse tous les baselines sur TOUTES les dimensions simultanément :
- Robustness : 0.9959 (query), 0.7089 (evidence)
- Bottom-line : 0.9875 (basic), 0.9836 (hallucination), 0.9925 (format)
- Alignment : 0.9832 (richness), 0.9099 (usability)

## Findings critiques

### 1. Le seesaw effect est réel et dangereux
Sans Gated Aggregation, optimiser la richesse dégrade la conciseness (et inversement). GRPO-Linear souffre d'instabilité entre safety et utility. La gate géométrique résout ce problème en hiérarchisant les objectifs.

### 2. Human-in-the-loop calibration est nécessaire
Les LLM judges seuls sont bruiteux. Le protocole dual-track (Blind Group + Assisted Group) identifie les cas limites et aligne les évaluateurs avec les préférences humaines réelles.

### 3. Answer-first est un signal clé
La métrique "Answer Firstness" (placer la réponse au début) montre le gain le plus fort en usability : 97.66 pour SearchLLM vs 95.05 pour Rubric. Cohérent avec les findings de [[etude-sageo-arena-2025]].

### 4. Le DPO est insuffisant pour la search
DPO exploite les patterns faciles (longueur) sans respecter les hard constraints de sécurité. GRPO-Gated est strictement supérieur.

## Ce que ça change pour le SEO

- **La recherche générative est DÉJÀ en production à grande échelle** — ce n'est plus théorique
- **Le factual grounding est le gate principal** — un contenu non-sourcé sera pénalisé avant même d'être évalué sur sa qualité
- **Answer-first pattern** : si ton contenu ne donne pas la réponse dans les premières phrases, il sera moins bien classé
- **La diversité des claims est récompensée** — couvrir plusieurs facettes d'un sujet > répéter le même point
- **Le format Markdown est attendu** — les LLM de search sont entraînés sur du Markdown structuré

## Concepts liés

[[agentic-search]] · [[grounding-score]] · [[surprise-gap]] · [[fully-meets]] · [[entites-vectorielles]]

## Études liées

[[etude-geo-aggarwal-2024]] · [[etude-sageo-arena-2025]] · [[etude-core-ranking-2025]] · [[etude-raid-gseo-2025]]

## Skills mobilisés

[[skill-entites-vectorielles]] · [[skill-brief-contenu]] · [[skill-cluster-aeo]] · [[skill-workflow-article]]
