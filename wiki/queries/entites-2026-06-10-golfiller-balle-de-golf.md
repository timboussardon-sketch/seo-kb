---
type: query
title: Golfiller, entités vectorielles pour la page « balle(s) de golf »
aliases: [entites-golfiller-balle-de-golf]
tags: [golfiller, entites-vectorielles, grounding-score, money-page, product-led, client]
created: 2026-06-10
updated: 2026-06-10
sources: 1
confidence: high
status: stable
---

# Entités vectorielles, page « balle(s) de golf » Golfiller

> **En résumé.** Cible : la page collection Money de Golfiller sur « balle de golf » (singulier, position 8,5 sur 26 574 impressions) et « balles de golf » (pluriel, en chute de 9,6 à 17,6 sur 13 562 impressions). Le diagnostic GSC montre que la page tient le singulier mais perd tout le champ commercial pluriel (prix, pas cher, meilleures, marques). La cause probable : une page collection pauvre en entités, qui ne couvre pas le champ sémantique réel des acheteurs (occasion, compression, prix neuf vs reconditionné, lot, profils, marques). Ce document liste les entités à intégrer, par zone, pour remonter le Grounding Score. Source data : [[queries/2026-06-10-golfiller-gsc-6mois]], [[sources/2026-06-10-golfiller-gsc-6mois]].

Requête cible : `balle de golf` / `balles de golf`. Page : collection Money (occasion / reconditionné). Intention : Do (achat), point de conversion = ajout panier / fiche produit.

## Champ sémantique réel (mesuré sur la GSC, pas inventé)

| Grappe d'entités | Requêtes (top export) | Impressions | Clics | Lecture |
|---|---|---|---|---|
| occasion | 30 | 10 707 | 542 | cœur de l'offre, déjà capté, à garder central |
| prix / combien | 36 | 8 182 | 79 | énorme gap : intention d'achat, CTR ras |
| compression | 56 | 2 690 | 420 | actif fort (le tableau), à relier à la collection |
| meilleures balles | 13 | 2 684 | 64 | gap : reco par usage absente |
| pas cher | 16 | 2 266 | 44 | gap : angle budget non traité |
| reconditionnées | 7 | 2 356 | 178 | synonyme de occasion, à inclure explicitement |
| lot / 100 balles / 50 balles | 9 | ~2 338 | 21 | gap : achat au volume, fort en occasion |
| profils (senior, débutant, distance) | 6 | 788 | 16 | gap : segmentation joueur |

## Tableau des entités à intégrer

### 1. Entités sémantiques obligatoires (le vecteur du sujet)
balle de golf, balles de golf (pluriel explicite dans le contenu), occasion, reconditionnée, état / grade (A, B), compression, spin, nombre de couches (2, 3, 4 pièces), enveloppe (uréthane, surlyn), marques nommées (Titleist Pro V1, Callaway, Srixon, TaylorMade TP5, Inesis), lot / pack, budget.

### 2. Preuves quantitatives (les chiffres à afficher, data first-party)
compression mesurée par modèle (réutiliser le tableau existant), écart de prix neuf vs reconditionné chiffré, nombre de balles contrôlées par grade, pourcentage d'économie moyen, prix par balle selon le lot. Règle : aucun chiffre inventé, tout vient de la boutique. Placeholder [À SOURCER depuis le catalogue] si la donnée n'est pas dispo.

### 3. Vecteurs multimodaux
tableau de compression intégré ou lié, photos de l'état réel des balles reconditionnées, filtres visibles (marque, compression, état, prix, lot), bloc comparateur, grille de prix par gamme.

### 4. Divergence / Haute Surprise (ce qu'aucun site générique n'a)
l'état réel mesuré des balles reconditionnées (grade + compression contrôlée chez Golfiller), l'angle « même balle, même perf, à -X% » prouvé par la donnée, le conseil par profil de joueur appuyé sur la data vitesse de swing. C'est le [[concepts/surprise-gap]] que seul un acteur qui manipule le stock peut produire.

## Gap actuel de la page

La page capte le singulier mais ne couvre pas : la grille de **prix** (8 182 imp, 79 clics), l'angle **pas cher / lot** (achat volume très présent en occasion), la **reco par profil**, les **sous-sections par marque**, et la **compression inline**. Le pluriel chute parce que la page est trop mince pour les requêtes commerciales larges. C'est un déficit d'entités, pas un problème technique.

## Implémentation par zone

- **H1** : inclure « balles de golf » au pluriel + « occasion / reconditionnées » (couvrir les deux nombres et le cœur d'offre).
- **Intro (90 mots)** : balle de golf, occasion vs neuf, économie chiffrée, compression, marques. Densité d'entités dès le premier paragraphe.
- **Corps, sections dédiées** : (a) prix et budget avec grille neuf vs reconditionné, (b) par marque (Titleist, Callaway, Srixon, TaylorMade, Inesis) en sous-blocs maillés vers les futures pages de marque, (c) par profil (senior, débutant, distance, femme), (d) compression expliquée + lien tableau, (e) lots / packs.
- **FAQ** : « combien coûte une balle de golf », « quelle différence neuf / reconditionné », « quelle compression choisir », « quelle balle pour débutant / senior ». Reprend mot pour mot les requêtes prix/profil non captées.
- **Maillage** : la page reçoit des liens des Spokes avis et profils, et pointe vers les fiches produit et le tableau de compression, cf. [[clusters/modeles-pseo-2026-06-10-golfiller]].

## Prochain pas

Transformer ces entités en plan Hn exécutable avec `seo-brief-contenu`, puis produire via `content-brain`. Les pages de marque (gap « inesis », « callaway ») se traitent en parallèle avec `seo-modeles-pseo`.

Pages liées : [[entities/golfiller]] · [[golfiller-strat]] · [[queries/2026-06-10-golfiller-gsc-6mois]] · [[clusters/modeles-pseo-2026-06-10-golfiller]] · [[concepts/product-led-seo]] · [[concepts/surprise-gap]]
