---
type: concept
title: Agentic Search (SEO agentique)
aliases: [agentic-search, seo-agentique, mle-star]
tags: [agentic, agents-ia, seo-ia, geo, titans]
created: 2026-04-12
updated: 2026-04-13
sources: 7
confidence: high
status: stable
---

# Agentic Search (SEO agentique)

Paradigme où des **agents IA autonomes** (MLE-STAR, Claude Computer Use, etc.) effectuent des recherches et des actions pour l'utilisateur. Le SEO devient "être sélectionné par l'agent pour accomplir une tâche", pas juste "être affiché dans une liste de liens".

## Ce que cette KB sait déjà

- [[sources/2026-04-11-seo-ia-tim]] décrit le concept MLE-STAR : pour qu'un agent **sélectionne** ton site, il doit pénétrer la Neural Memory ([[concepts/surprise-metric]]) ou la Persistent Memory (marque forte → indélogeable) de [[entities/titans]]
- Le skill Product-Led SEO recommande de prévoir une version "agent-friendly" avec API/embed [[sources/2026-04-12-tim-skills-seo-proprietary]]
- Le skill cluster-aeo utilise le framework Know-Simple / Know / **Do** — les pages "Do" sont les plus pertinentes pour l'Agentic Search (outils que l'agent peut utiliser)
- Tim dans ses newsletters : "se préparer au SEO agentique" — Avant: requête→liens→clic→site. Après: requête→réponse IA→(parfois) clic→site [[sources/2026-03-06-algorithme-etude-citation-ia]]

## Sources paper ingérées (2026-04-13)

### [[sources/2026-04-13-core-ranking-jin-2025]]
Démontre que le contenu textuel seul peut **renverser le ranking** dans un LLM-based search. Review-based narrative passe un item du dernier rang au **Top-1 dans 80 %+ des cas**. Implication agentic : un agent IA qui évalue des produits sera sensible aux narratifs authentiques, pas aux signaux off-page.

### [[sources/2026-04-13-raid-gseo-2025]]
Le framework 4W Deep Reflection (Who/What/Why/How) — cf. [[concepts/4w-deep-reflection]] — modélise les rôles utilisateurs côté créateur. Transposable à l'agentic : anticiper quel **type d'agent** viendra chercher (navigation, comparaison, achat, recherche approfondie).

### [[sources/2026-04-13-searchllm-2026]]
LLM de recherche générative **déployé en production** (RedNote/Xiaohongshu, cent. M utilisateurs). Reward à 2 couches avec gate géométrique : factualité = non-négociable avant tout autre critère. Confirme que les agents de recherche évaluent d'abord la fiabilité, puis l'utilité.

## Limites

- Aucune des 3 études ne parle explicitement d'agents autonomes type MLE-STAR / Claude Computer Use — la KB extrapole depuis leurs findings vers l'agentic
- L'agentic search au sens strict (agent qui **agit**, pas juste génère une réponse) reste mal couvert empiriquement
- Les benchmarks actuels sont single-turn, pas workflow agentique multi-étapes

## Pages liées

[[sources/2026-04-11-seo-ia-tim]] · [[sources/2026-04-13-core-ranking-jin-2025]] · [[sources/2026-04-13-raid-gseo-2025]] · [[sources/2026-04-13-searchllm-2026]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[sources/2026-04-15-scan-arxiv-15-avril]] (AgenticGEO 2603.20213, Role-Augmented G-SEO 2508.11158) · [[sources/2026-04-25-scan-arxiv-25-avril]] (MAGEO 2604.19516 — 3 agents avec mémoire) · [[sources/2026-04-15-algorithme-listicles-chatgpt-30pct-baisse]] (Addy Osmani formalise l'AEO côté Google Cloud) · [[concepts/surprise-metric]] · [[concepts/aeo]] · [[concepts/4w-deep-reflection]] · [[concepts/answer-first-pattern]] · [[concepts/data-proprietaire]] · [[concepts/grounding-score]] · [[entities/titans]]
