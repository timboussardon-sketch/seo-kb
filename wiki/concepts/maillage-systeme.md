---
type: concept
title: Maillage-système (architecture éditoriale 3 axes)
aliases: [maillage-systeme, maillage-3-axes, maillage-architecture]
tags: [doctrine-tim, maillage-interne, hub-satellite, ancres, cocon, skill]
created: 2026-05-01
updated: 2026-05-01
sources: 2
confidence: high
status: stable
---

# Maillage-système

**Skill propriétaire Tim** complémentaire de `maillage-interne-gsc`. Raisonne sur la **structure éditoriale et le contenu**, sans dépendre de la GSC. Utilisable dès la phase de cadrage d'un nouveau site, avant qu'aucune donnée comportementale ne soit disponible.

Cas d'application chiffré : **0 → 62 liens internes** sur le blog Organikk (14 articles, 4 piliers) [[sources/2026-04-30-newsletter-maillage-interne]].

## Trois axes simultanés

| Axe | Lecture par | Critère de validation |
|---|---|---|
| **Topique** | Google (sémantique classique) | La cible parle-t-elle du même sujet ? |
| **Vectoriel** | LLM (embeddings) | L'ancre s'aligne-t-elle mathématiquement avec le passage cible ? |
| **Cognitif** | Humain | Le lecteur a-t-il envie de cliquer ? |

Une ancre qui rate l'un des trois = lien gaspillé. Le maillage est un **système, pas une passe**.

## Architecture en piliers (3 à 5 max)

- Regrouper articles par **cohérence sémantique**, pas par catégorie technique
- Chaque pilier : **1 hub** (article le plus stratégique, vocabulaire central) + N satellites
- Cluster < 3 articles → reste sous-cluster d'un pilier existant
- Le hub n'est pas figé : si un satellite devient plus complet, on bascule

## Règles de gouvernance (par nouvelle publication)

- ≥ 3 liens entrants depuis 3 articles existants
- ≥ 3 liens sortants vers articles existants
- ≥ 1 lien sortant vers page **Do** (orientation funnel Know → Do)
- ≥ 1 lien sortant vers un autre pilier (cross-pillar pollination)
- Aucune ancre exact match dupliquée vers la même cible
- Tous les liens **in-body**, aucun en bloc "Voir aussi"

## Distinction avec `maillage-interne-gsc`

- `maillage-systeme` (ce skill) = **structure éditoriale d'abord** (sans GSC)
- `maillage-interne-gsc` = **donnée comportementale ensuite** (avec GSC ≥ 6 mois)
- Les deux se chaînent : architecture, puis injection donnée GSC pour priorisation

## Connexion KB

- Implémente le framework Know-Simple/Know/Do du skill `seo-cluster-aeo` ([[concepts/aeo]]) appliqué à du maillage
- Réf [[concepts/5-types-ancres]] pour la sélection ancre par lien (exact / partial / sémantique / naming / contextuelle)
- Cohérent avec [[concepts/data-proprietaire]] : un hub n'est pas un titre de catégorie, c'est l'article le plus stratégique du pilier qui définit le vocabulaire

## Pages liées

[[sources/2026-04-30-newsletter-maillage-interne]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[concepts/5-types-ancres]] · [[concepts/aeo]] · [[concepts/data-proprietaire]] · [[concepts/programmatique-pseo]] · [[entities/organikk-co]]
