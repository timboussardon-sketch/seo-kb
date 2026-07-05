---
type: source
source_type: article
title: La méthode Claude pour travailler ta sémantique SEO
aliases: [algorithme-methode-claude-semantique]
tags: [algorithme, tim, semantique, claude, geo]
created: 2026-05-27
updated: 2026-07-05
sources: 1
confidence: high
status: stable
---

# La méthode Claude pour travailler ta sémantique SEO

**Auteur** : Timothée Boussardon (algorithme.substack.com)
**Type** : newsletter / article
**URL** : https://algorithme.substack.com/p/la-methode-claude-pour-travailler
**Date publication** : 2026-05-27

## Contexte
Tim publie son skill d'audit sémantique complet (prompt copiable dans l'article) : un pipeline en 13 phases qui remplace le SEO par mots-clés par une cartographie d'entités sémantiques pondérées, alignée sur le fonctionnement des LLM et de l'AI Overview. La méthode couvre création et audit de page, avec scoring déterministe (Content Gap Score, Surprise Score) et garde-fous anti-hallucination.

## Chiffres / faits clés
- Pipeline en 13 phases (0 à 13), du filtre stratégique (test de substitution LLM) à la boucle de feedback KB.
- Phase 2 : 30 à 50 entités sémantiques, tableau 7 colonnes, poids 0 à 1.
- Pondération : poids > 0,8 = entité pivot ; 0,5-0,8 = support ; < 0,5 = périphérique.
- Densité cible (pour 2 000 mots) : pivots 0,5-1 % ; support 0,2-0,5 % ; périphérique < 0,2 %.
- Information Gain (Aggarwal KDD'24, arXiv:2311.09735) : ajout de citation +41 % PAWC ; ajout de statistiques +34 % ; citer ses sources +29 % ; ton autoritaire seul +13 %.
- SAGEO Arena 2025 (Kim et al., arXiv:2602.12187) : optimisation du corps seul -4,54 Hit Rate ; couche structurelle (title/meta/headings/schema) seule +22 % ; structurel + statistiques +35 %.
- Surprise Score sémantique (0-100) : 0-30 médiocrité statistique (refonte) ; 30-60 acceptable mais réplicable ; 60-85 Information Gain validé (publiable) ; 85-100 inversion experte maximale.
- Content Gap Score : couverture standard < 70 % = base sémantique absente ; ≥ 70 % + Surprise < 30 % = indexable mais peu mémorisable par l'IA ; ≥ 70 % + Surprise ≥ 30 % = cible optimale.
- Freshness Guard : données de plus de 36 mois omises sauf paper fondateur.
- Confidence Score à 3 niveaux (high/medium/low) ; low remplacé par le placeholder `[À SOURCER]`.
- Priorités de correction en mode audit : P0 bloquant (structurel / Triade SERP), P1 important (pain points, divergence, preuves, Surprise < 60), P2 nice-to-have (FAQ, multimodal).
- Action Engine Flag (phase 1) : une requête Do exige un outil interactif (calculateur, simulateur) pour atteindre Fully Meets ; le texte seul échoue.

## Citations marquantes
> "un concept, un outil, une méthode, une personne, un algorithme que ta page doit nommer" (attribution : Tim, définition d'une entité, 2026-05-27)

> "L'agence précédente m'envoyait des rapports de 40 pages" (attribution : Tim, exemple de verbatim haute surprise, 2026-05-27)

## Angle SEO à retenir
- Le classement d'une page se joue d'abord sur la couche structurelle : SAGEO montre que le corps seul dégrade le Hit Rate, alors que title/meta/headings/schema apportent +22 %.
- Le Surprise Score opérationnalise l'inversion d'expertise : viser 60-85 (Information Gain validé), pas la simple couverture sémantique qui reste réplicable et oubliable par l'IA.
- Le skill assume ses limites mathématiques (cosinus simulé, non calibré API) et code l'anti-hallucination dans le process via `[À SOURCER]` et le Freshness Guard 36 mois.

## Limites
- Scrape propre et complet, article non paywallé, prompt du skill inclus.
- Les similarités cosinus de la phase 2 sont explicitement simulées (projection du corpus Claude), non calibrées par une API d'embeddings : à traiter comme indicatives.
- Références académiques (Aggarwal KDD'24, SAGEO Arena 2025) citées avec identifiants arXiv ; l'identifiant SAGEO (2602.12187) est à vérifier avant citation publique.

## Pages liées
**Concepts** : [[concepts/ingenierie-semantique-inversee]] · [[concepts/entites-vectorielles]] · [[concepts/surprise-metric]] · [[concepts/information-gain]] · [[concepts/structural-information-geo]] · [[concepts/test-substitution-llm]] · [[concepts/confidence-score]] · [[concepts/triade-serp]]
**Entity** : [[entities/sageo-arena-benchmark]]
