---
type: concept
title: Cannibalisation SEO
aliases: [cannibalisation, keyword cannibalism, cannibalisation de mots-clés]
tags: [seo, cannibalisation, gsc, architecture]
created: 2026-06-12
updated: 2026-06-12
sources: 2
confidence: high
status: stable
---

# Cannibalisation SEO

Deux pages (ou plus) du même site qui se disputent la même requête ou la même intention de recherche. Google hésite entre les deux, les positions oscillent, et aucune ne consolide l'autorité que la requête mérite. Le diagnostic se fait sur la data GSC réelle, jamais à l'œil : c'est le périmètre du skill `seo-cannibalisation`, dont les audits vivent dans `wiki/cannibalisation/`.

## Les types de conflit

1. **Mot-clé exact** : deux URL rankent en alternance sur la même requête (le cas le plus net dans la GSC : la position moyenne saute quand l'URL servie change).
2. **Même intention** : deux pages différentes répondent au même besoin (ex. un article « top 8 outils gratuits » dans l'ancien hub ET dans le nouveau, cas réel Leexi après refonte, cf. [[analyse-gsc-approfondie-leexi]] côté repo client).
3. **Proximité sémantique** : deux pages proches qui se diluent mutuellement sans conflit frontal ; se voit au plafonnement des deux.
4. **Triade SERP** : faux positif. Google affiche volontairement plusieurs URL du même site sur une requête (marque, multi-intentions). Aucune action.

## Les remèdes, par ordre de violence

- **Aucune action** si Triade SERP ou si les deux pages servent des intentions réellement distinctes.
- **Maillage croisé + différenciation** : re-spécialiser chaque page sur sa micro-intention, ancres distinctes.
- **Fusion** : une page absorbe l'autre, qui redirige.
- **301** : l'URL la plus faible redirige vers la canonique ; obligatoire dans les cas de doublons post-refonte (ancienne et nouvelle URL coexistent).

## Les déclencheurs typiques

- **Refonte ou migration sans redirections** : les anciennes URL survivent à côté des nouvelles (cas Leexi 2026 : `/ai-meeting/` vs `/assistant-ia/`, −43 % hors-marque).
- **pSEO sans garde-fou** : deux modèles de pages proches (profil vs usage) génèrent des pages qui se recouvrent ; d'où le garde-fou anti-cannibalisation posé dans [[clusters/modeles-pseo-2026-06-10-golfiller]].
- **Production au fil de l'eau** : un blog qui retraite un sujet déjà couvert au lieu d'enrichir la page existante (anti-règle : 1 cluster = 1 page, cf. [[concepts/know-simple-know-do]]).

## Doctrine

On ne tranche jamais une cannibalisation sans croiser requête × page dans la GSC. Un export pages seul fait deviner ; un export croisé fait voir. Et la cannibalisation entre un article de blog et un post LinkedIn long se prévient en amont : un concept = un seul canal indexable par mot-clé (raison du choix blog OU LinkedIn dans la stratégie hebdo d'Organikk).

## Liens

[[concepts/know-simple-know-do]] · [[clusters/modeles-pseo-2026-06-10-golfiller]] · [[entities/gsc]] · [[entities/golfiller]]
