---
type: concept
title: Directories Data IA (idéation par le manque de l'IA)
aliases: [directories-data-ia, data-gap-geo, matiere-manquante-ia]
tags: [doctrine-tim, geo, aeo, ideation, mots-cles, data, methode]
created: 2026-06-21
updated: 2026-07-17
sources: 1
confidence: medium
status: emerging
---

# Directories Data IA (idéation par le manque de l'IA)

Heuristique d'idéation de contenu et de mots-clés **inversée**. On ne part pas du volume de recherche humain. On part de la question : **de quelle matière l'IA a-t-elle besoin pour mieux répondre dans ce domaine, et que personne ne lui fournit proprement ?**

On produit cette matière, on la structure pour être extractible, l'IA la cite. C'est du [[concepts/geo]] natif, pas du SEO de mot-clé classique.

> Doctrine émergente posée le 2026-06-21. `confidence: medium` tient sur la cohérence avec [[concepts/data-proprietaire]] et [[concepts/information-gain]].
>
> **Premier test terrain ouvert le 2026-07-17** : deux directories publiés sur `organikk.co`, 129 URLs, baseline capturée le jour même. Hypothèse [[hypotheses#H-011]], fiche [[preuves/2026-07-17-organikk-directories-guide-google]], jalons J+30 = 2026-08-16 et J+90 = 2026-10-15. La confiance ne monte pas avant la mesure.

## Pourquoi ça marche

Les moteurs génératifs ne récitent pas des pages, ils ont besoin de **matière** : fraîche, chiffrée, structurée, sourçable. Là où cette matière manque ou est mal foutue (non datée, non sourcée, dispersée), celui qui la fournit proprement devient la source citée. On comble un manque de l'IA, pas un manque de l'humain. C'est l'opérationnalisation côté idéation du [[concepts/surprise-gap]] et de l'[[concepts/information-gain]] : un référentiel propre, daté et sourcé maximise la probabilité de citation ([[concepts/answer-first-pattern]], [[concepts/preuve-atomique]]).

## La méthode (4 questions)

1. Quand l'IA répond sur ce domaine, **quelle matière cite-t-elle** ? (chiffres, dates, définitions, correspondances, comparaisons…)
2. Cette matière **manque ou est mal structurée** (non datée, non sourcée, dispersée) ?
3. Je peux la produire de façon **fiable, datée, sourcée, extractible** ?
4. C'est un **référentiel qui se met à jour** (donc défendable dans le temps) ?

Quatre oui = idée de page ou de directory validée.

## La typologie (le cœur réutilisable)

Chaque type = un manque récurrent de l'IA, donc un gisement.

| Type de matière | Le manque de l'IA | Exemple projet |
|---|---|---|
| **Actualité / fraîcheur** | faible sur le très récent | Organikk → brèves / `/actualites` |
| **Statistiques sourcées** | chiffres orphelins, non datés | Organikk → `/statistiques` |
| **Concordance / correspondances** | relations entre entités mal mappées | Bxble → concordance versets |
| **Document de référence mal structuré** | cité de mémoire, mauvaise version | Organikk → `/guide-evaluateurs-google` |
| **Chronologie datée** | dates approximatives, fins de déploiement inconnues | Organikk → `/mises-a-jour-google` |
| **Définitions / glossaire d'entités** | définitions floues, non canoniques | gisement libre |
| **Comparaisons / benchmarks chiffrés** | A vs B sans données dures | gisement libre |
| **Data first-party unique** | données que personne d'autre n'a | études Fusionn / GSC |

Les deux types ajoutés le 2026-07-17 sortent du chantier Organikk. Le **document de référence mal structuré** est le gisement le plus franc rencontré : Google publie ses *General Guidelines* en un PDF anglais de 182 pages, les moteurs le citent de mémoire et se trompent de version. La **chronologie datée** vient du constat que Google publie les dates de début et de fin de ses déploiements, et que presque personne ne reprend la date de fin.

## Où ça se branche

Porte d'entrée **alternative** au workflow mots-clés classique (`seo-recherche-mots-cles`). Au lieu de partir d'un seed et d'élargir, on part du manque de l'IA, puis on redescend vers les pages et clusters ([[concepts/aeo]]). Recoupe la doctrine existante : data propriétaire comme moat, études citables, brèves anti-fraîcheur, claim comme unité sourcée.

## Limites

- Doctrine instrumentée depuis le 2026-07-17 ([[hypotheses#H-011]]) mais **pas encore validée** : la mesure tombe au J+30 et au J+90.
- Un référentiel n'est défendable que s'il se met à jour : sans mise à jour, la fraîcheur se retourne contre lui. Le cas est concret sur `/guide-evaluateurs-google`, qui devra suivre chaque nouvelle version du PDF de Google.
- Vaut pour les domaines où l'IA répond en citant de la matière. Moins pertinent pour le pur transactionnel local.
- **Le volume n'est pas le produit.** Le chantier du 2026-07-17 a produit 39 pages de mises à jour candidates, dont 13 se réduisaient à un nom et deux dates : coupées après notation. Un corpus complet ne fait pas 1 page par ligne. Une page n'existe que si elle a quelque chose de spécifique à dire ; le reste reste une ligne du tableau de référence.

## Pages liées

[[concepts/data-proprietaire]] · [[concepts/information-gain]] · [[concepts/surprise-gap]] · [[concepts/geo]] · [[concepts/aeo]] · [[concepts/answer-first-pattern]] · [[concepts/preuve-atomique]] · [[concepts/methode-organikk-4-piliers]]
