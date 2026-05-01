---
type: concept
title: 4W Deep Reflection (Who / What / Why / How — méthode RAID)
aliases: [4w-deep-reflection, raid-method, multi-role-reflection]
tags: [geo, methode, intent-modeling, multi-role, brief-contenu]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: high
status: stable
---

# 4W Deep Reflection

**Méthode proposée par [[sources/2026-04-13-raid-gseo-2025]]** pour raffiner l'inférence d'intention latente côté créateur de contenu, dans un contexte black-box (requêtes utilisateur invisibles).

## Les 4 perspectives

### Who — qui va chercher ?

Lister les **rôles utilisateurs** probables qui poseraient une requête sur le sujet : techniciens, lecteurs, décideurs, experts, novices, acheteurs, détracteurs, etc.

Distribution empirique (RAID, 8 030 instances) :
- 38 % Knowledge Producers and Researchers
- 31 % Civic Everyday Actors
- 22 % Economic Activity Participants
- 6 % Health and Care Stakeholders
- 3 % Cultural and Creative Professionals

Biais du modèle : privilégie les perspectives généralistes et publiques. Pour un contenu B2B niché, compenser manuellement.

### What — quels besoins informationnels ?

Pour chaque rôle identifié, formuler **ce qu'il cherche** précisément. Même sujet, besoins distincts :
- Technicien → spécifications, dépannage, compatibilité
- Décideur → coûts, ROI, alternatives comparées
- Novice → définition, exemples, étapes simples

### Why — quels écarts avec l'intent initial ?

Identifier les **mismatches** entre l'intent que le LLM a inféré automatiquement et les besoins réels des rôles listés. Le gap révèle ce que le contenu actuel **manque**.

### How — comment généraliser l'intent ?

Reconstruire l'intent **élargi** via prompt-based reasoning, pour couvrir l'union des besoins des rôles sans perdre la spécificité.

## Pipeline RAID complet

1. Content Summarization (résumé sémantique contraint)
2. Intent Inference initial (LLM génère représentation brute)
3. **4W Deep Reflection** (cette méthode)
4. Step Planning (décomposition en étapes actionnables)
5. Content Rewriting (réécriture tracée)

## Performance empirique

- Sans 4W : score **−3.18** (négatif)
- Avec 4W + Step Planning : **+4.72** (Subjective Impression)
- Gain attribuable au module 4W seul : ablation confirme l'importance critique

RAID G-SEO surpasse les 9 baselines GEO précédentes (dont Cite Sources, Statistics Addition, etc.) — cf. [[sources/2026-04-13-geo-aggarwal-2024]].

## Application pratique (brief contenu)

Avant d'écrire un article, lister :

1. **Who (5 min)** — 4-6 rôles distincts qui cherchent ce sujet
2. **What (10 min)** — 2-3 besoins par rôle → 8-18 micro-intentions au total
3. **Why (5 min)** — scanner le draft : quelles micro-intentions sont ignorées ?
4. **How (10 min)** — restructurer le plan pour couvrir l'union sans diluer

Total 30 min de pré-rédaction qui remplace la "persona research" classique par un process plus rapide et plus systématique.

## Articulation avec doctrine Tim

- Complémente le skill `seo-brief-contenu` (étape "personas" existante mais moins structurée)
- Nourrit [[concepts/surprise-gap]] : les rôles sous-représentés par le consensus = source de gap naturel
- Cohérent avec [[concepts/ingenierie-semantique-inversee]] — reverse-engineering depuis les rôles plutôt que depuis les mots-clés
- Alimente la FAQ d'un article : une question par rôle majeur

## Limites

- Méthode encore nouvelle (preprint AAAI 2026 non reviewed)
- Distribution des rôles biaisée généralistes — à ajuster pour niches B2B
- Pas de test cross-secteur large — évaluation sur corpus spécifique
- Le plafond effective rate à 70 % (aucune méthode GEO n'y arrive) s'applique aussi à RAID

## Pages liées

[[sources/2026-04-13-raid-gseo-2025]] · [[concepts/surprise-gap]] · [[concepts/information-gain]] · [[concepts/ingenierie-semantique-inversee]] · [[concepts/workflow-redaction-8-etapes]] · [[concepts/avatar-freelance-sans-systeme]]
