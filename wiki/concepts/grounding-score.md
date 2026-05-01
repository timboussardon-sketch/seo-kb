---
type: concept
title: Grounding Score
aliases: [grounding-score, score-ancrage]
tags: [seo-ia, geo, aeo, vecteurs, ranking]
created: 2026-04-11
updated: 2026-04-13
sources: 6
confidence: high
status: stable
---

# Grounding Score

Concept central du skill `seo-entites-vectorielles`. Référencé en §4.2 d'`AGENTS.md` comme concept attendu dans cette KB.

## Définition canonique (AGENTS.md §4.2)

> **Grounding Score** : similarité cosinus entre le vecteur d'intention d'une requête et le vecteur d'une page

Mesure de **proximité vectorielle** — plus une page est "grounded" par rapport à l'intention, plus elle est susceptible d'être servie par un moteur à composante vectorielle (SGE, ChatGPT Search, Perplexity).

## Évolution via la Surprise Metric (source Tim)

[[sources/2026-04-11-seo-ia-tim]] propose une évolution :

- **Grounding classique** = proximité vectorielle (pertinence seule)
- **Grounding Titans** = proximité **+ divergence informationnelle** ([[concepts/surprise-metric]])

Dans un modèle [[entities/titans]], une page n'est pas sélectionnée uniquement parce que son vecteur est proche de l'intention. Elle doit aussi générer un **gradient de surprise suffisant** pour être mémorisée. Une page parfaitement pertinente mais redondante avec la Persistent Memory a un gradient ≈ 0 → ignorée.

**Hypothèse** : le Grounding Score optimal pour le GEO n'est pas une proximité maximale, c'est **proximité + divergence**. Ni trop loin (hors-sujet) ni trop proche (redondant). Sweet spot entre les deux.

## Connexion avec le pattern wiki persistant

L'hypothèse posée sur [[sources/2026-04-11-karpathy-llm-wiki]] (section *Implications SEO*, angle 4) trouve ici son mécanisme :

Un wiki persistant compound **à la fois** le vecteur de grounding (en ajoutant des claims et des cross-refs) **et** le gradient d'information (en intégrant des updates datés et des contradictions flaguées → surprise informationnelle). Les deux axes bougent ensemble. Le wiki produit des pages **grounded et surprenantes** par construction.

## Implications skill `seo-entites-vectorielles`

1. **Grounding pur** insuffisant — "trop proche, trop prévisible", oublié.
2. **Surprise pure** insuffisante — "hors-sujet", mal routée.
3. **Les deux** — vecteur proche + faits nouveaux à chaque section — configuration cible.

Cf. [[concepts/surprise-gap]] : apporter l'info **manquante** (pas inexistante) qui rend la page grounded et surprenante simultanément.

## Affinement multi-résolution (MIRAS)

[[sources/2026-04-13-miras-architecture]] propose un encodage multi-granularité (document → section → passage → phrase). Le grounding peut se calculer sur le segment le plus pertinent vs moyenne diluée du document → une page avec un seul H2 fortement vectorisé peut remonter même si le reste est moyen. Connecte directement à [[concepts/passage-ranking]].

## Limites

- **Aucune définition officielle de Google**. "Grounding Score" est un terme de doctrine SEO (dont `AGENTS.md` §4.2), pas un concept publié par Google avec ce nom exact.
- **Lien avec Titans/MIRAS spéculatif**. Rien ne prouve que SGE calcule effectivement une similarité cosinus intégrant une composante de surprise.
- `confidence: medium` — concept fondé sur 2 sources (Karpathy + Tim) qui convergent structurellement, mais aucun benchmark empirique.

## Pages liées

[[sources/2026-04-13-titans-architecture-google-deepmind]] · [[sources/2026-04-13-miras-architecture]] · [[sources/2026-04-13-sageo-arena-2025]] (retrieval-stage grounding via structural info) · [[sources/2026-04-13-searchllm-2026]] (grounding = gate non-négociable en prod) · [[sources/2026-04-11-seo-ia-tim]] · [[sources/2026-04-11-karpathy-llm-wiki]] · [[concepts/surprise-metric]] · [[concepts/surprise-gap]] · [[concepts/passage-ranking]] · [[concepts/ingenierie-semantique-inversee]] · [[concepts/structural-information-geo]] · [[concepts/answer-first-pattern]] · [[concepts/metriques-visibilite-geo]] · [[entities/titans]] · [[entities/miras]]
