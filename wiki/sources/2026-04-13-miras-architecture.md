---
type: source
source_type: paper
title: MIRAS — Multi-Resolution Adaptive Summarization
aliases: [miras-paper, miras-architecture]
tags: [architecture-ia, passage-ranking, grounding-score, geo, aeo, briefs]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: medium
status: stable
---

# MIRAS — Multi-Resolution Adaptive Summarization

**Auteurs** : équipes de recherche IA (Google / affiliés) — non précisé dans le raw
**Type** : paper recherche (lien non disponible)
**Fichier raw** : `raw/papers/miras-architecture.md`
**Date** : 2024-2025

---

## Contexte

Extension des architectures type [[entities/titans]] pour le traitement de contenu à **résolutions multiples**. Permet aux LLM de résumer et prioriser le contenu à différents niveaux de granularité — fondement architectural du [[concepts/passage-ranking]] (chaque H2 = vecteur sémantique distinct).

## Méthode

Le raw ne détaille pas le protocole expérimental. Le mécanisme exposé : un même contenu long est encodé à plusieurs granularités (document → section → passage → phrase), chaque niveau pouvant être matché indépendamment contre une intention de requête.

## Chiffres clés

Aucun benchmark numérique dans le raw. La pertinence repose sur la mécanique architecturale, pas sur des % de gain mesurés.

## Résumé structuré

### Connexion passage-ranking

Chaque section (H2) est évaluée comme un vecteur sémantique distinct. Le matching ne se fait plus uniquement page entière ↔ requête, mais passage ↔ requête. Cf. [[concepts/passage-ranking]] (jusqu'ici stub).

### Connexion grounding-score

[[concepts/grounding-score]] gagne en finesse : le matching cosine peut s'opérer sur le segment le plus pertinent au lieu de la moyenne diluée du document. Une page qui n'a qu'un H2 pertinent peut quand même remonter — si ce H2 porte un vecteur sémantique fort.

### Implication doctrine briefs Tim

Justifie structurellement la doctrine de [[concepts/ingenierie-semantique-inversee]] et [[sources/2026-04-12-tim-skills-seo-proprietary]] (skill brief-contenu) : **chaque H2 doit porter un vecteur sémantique distinct, au moins un H2 doit créer un [[concepts/surprise-gap]]**. Ce n'est plus une pratique cosmétique — c'est aligné sur la mécanique de retrieval multi-résolution.

## Limites

- **Lien original non disponible** dans le raw
- **Pas de benchmark cité** — le transfert vers passage-ranking en production (Google) est par analogie, pas par évidence directe
- **`confidence: medium`** : mécanique paper crédible, application SEO inférée

## Implications SEO

- **Briefs** : la structure Hn devient un objet d'optimisation à part entière, pas un habillage typographique
- **Featured Snippets / AI Overviews** : un passage isolé bien cadré peut être extrait et cité même si la page entière n'est pas dominante sur la requête
- **Stratégie cluster** : les pages satellites d'un cluster AEO doivent porter chacune un vecteur distinct (sinon elles diluent le signal du pilier)

## Pages liées

**Entities** : [[entities/miras]] · [[entities/titans]] · [[entities/google-deepmind]]

**Concepts** : [[concepts/passage-ranking]] · [[concepts/grounding-score]] · [[concepts/ingenierie-semantique-inversee]]

**Sources** : [[sources/2026-04-13-titans-architecture-google-deepmind]] (architecture parente) · [[sources/2026-04-11-seo-ia-tim]] (analyse doctrinale)
