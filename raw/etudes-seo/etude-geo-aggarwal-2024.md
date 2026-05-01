---
type: etude
source_type: paper
title: "GEO: Generative Engine Optimization"
aliases: ["GEO", "GEO paper", "Aggarwal et al. 2024", "GEO-bench"]
tags: ["geo", "generative-engine", "aeo", "visibilite-ia", "benchmark", "perplexity", "citations", "statistiques"]
created: "2026-04-13"
updated: "2026-04-13"
sources: ["arXiv:2311.09735"]
confidence: haute
status: actif
auteurs: ["Pranjal Aggarwal", "Vishvak Murahari", "Tanmay Rajpurohit", "Ashwin Kalyan", "Karthik Narasimhan", "Ameet Deshpande"]
institution: "Princeton University / IIT Delhi"
publication: "KDD '24, Barcelone"
date_publication: "2024-08-25"
arxiv: "2311.09735"
---

# GEO: Generative Engine Optimization

## Papier fondateur du GEO

Première étude à formaliser le concept de **Generative Engine Optimization** — l'optimisation de contenu web pour augmenter la visibilité dans les réponses générées par les moteurs IA (BingChat, Perplexity, Google SGE).

## Problème posé

Les moteurs génératifs (Generative Engines) combinent retrieval + LLM pour synthétiser des réponses. Contrairement au SEO classique (ranking linéaire), la visibilité dans un GE dépend de si et comment le contenu est cité dans la réponse générée. Les créateurs de contenu n'ont aucun contrôle sur ce process black-box.

## Contributions clés

**1. Framework GEO** — Premier framework d'optimisation black-box pour moteurs génératifs. Le site source est modifié → réinjecté → on mesure si la visibilité dans la réponse augmente.

**2. GEO-bench** — Benchmark de 10 000 requêtes issues de 9 datasets (MS Macro, ORCAS, Natural Questions, AllSouls, LIMA, Davinci-Debate, Perplexity Discover, ELI-5, GPT-4 Generated). 25 domaines, 9 types de requêtes, 7 catégorisations.

**3. 9 méthodes GEO testées** :

| Méthode | Résultat |
|---|---|
| Keyword Stuffing | Quasi nul — ne fonctionne PAS sur les GE |
| Unique Words | Quasi nul |
| Cite Sources | +30-40% PAWC, +15-30% Subjective Impression |
| Statistics Addition | +30-40% PAWC, meilleur score moyen |
| Quotation Addition | +27.2 PAWC (meilleur score absolu) |
| Fluency Optimization | +15-30% visibilité |
| Easy-to-Understand | +15-30% visibilité |
| Authoritative | Bon sur débats/histoire |
| Technical Terms | Modéré |

## Findings critiques pour le SEO

- **Le Keyword Stuffing est MORT pour les GE** — zéro amélioration, voire dégradation
- **Cite Sources + Statistics Addition = meilleure combinaison** — Fluency + Stats donne +5.5% de plus que toute stratégie isolée
- **Les sites faiblement rankés bénéficient le PLUS du GEO** — Cite Sources donne +115% pour un site Rank 5, mais -30% pour le Rank 1. Les GE démocratisent la visibilité
- **Validé sur Perplexity.ai en production** — Statistics Addition donne 33.9 en Subjective Impression vs 24.7 baseline (+37%)
- **Domain-specific** : Statistics Addition domine en Law & Gov, Authoritative en History/Debate, Quotation en People & Society

## Métriques proposées

- **Position-Adjusted Word Count (PAWC)** — nombre de mots cités pondéré par la position de la citation (décroissance exponentielle)
- **Subjective Impression** — 7 sous-métriques : relevance, influence, uniqueness, diversity, follow-up, position, count

## Implication directe

Le SEO classique (backlinks, keyword density, domain authority) est **insuffisant** pour les GE. Il faut ajouter : citations sourcées, données chiffrées, quotes d'autorité, et améliorer la fluence. C'est un changement de paradigme.

## Concepts liés

[[agentic-search]] · [[grounding-score]] · [[surprise-gap]] · [[fully-meets]] · [[entites-vectorielles]]

## Études liées

[[etude-sageo-arena-2025]] · [[etude-core-ranking-2025]] · [[etude-raid-gseo-2025]] · [[etude-searchllm-2026]]

## Skills mobilisés

[[skill-entites-vectorielles]] · [[skill-cluster-aeo]] · [[skill-brief-contenu]]
