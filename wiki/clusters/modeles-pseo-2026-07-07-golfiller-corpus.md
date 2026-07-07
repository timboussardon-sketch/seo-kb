---
type: cluster
title: "Modèles pSEO Golfiller par corpus (scorés)"
aliases: [modeles-corpus-golfiller, meilleurs-modeles-golfiller]
tags: [golfiller, pseo, product-led, corpus, modeles-pseo, know-simple-know-do, surprise-gap]
created: 2026-07-07
updated: 2026-07-07
sources: 2
confidence: medium
status: draft
---

# Modèles pSEO Golfiller par corpus (scorés)

Sélection des meilleurs modèles de pages (template + variable) qui constituent les corpus du [[corpus-golfiller|Corpus Golfiller]]. Money Page = la collection de balles filtrable (point de conversion : ajout panier). Chaque modèle est rattaché à sa base et scoré `Proximité × Intention × Faisabilité` (chaque facteur 1-5, produit ramené sur 10).

Ancrage data : GSC réelle (tableau compression 5 652 clics pos 7,17 ; calcul index 1 816 clics pos 11,77 ; page « quelle balle » 1 330 clics pos 8,45) et requêtes réelles relevées le 2026-07-07 (grading occasion AAAA/AAA/AA, mapping vitesse de swing → compression).

## Tableau scoré

| # | Modèle (template × variable) | Corpus / base | Intention | P×I×F | Score /10 | Format | Maillage → Money Page |
|---|---|---|---|---|---|---|---|
| 1 | Comparateur `[balle X]` vs `[balle Y]` | 2 · specs balles | Choisir entre deux balles avant d'acheter | 5×5×4 | 8 | Comparateur dynamique, `/comparer/x-vs-y` | « acheter la Pro V1 d'occasion » |
| 2 | Meilleure balle pour `[profil]` (débutant, swing lent, petit budget, senior, femme, contrôle, distance) | 2 · specs + mapping profil→compression | Trouver la balle adaptée à soi | 5×5×4 | 8 | Guide + reco produit filtrée | « voir les balles pour ce profil » |
| 3 | Balles d'occasion qualité `[grade]` (AAAA / AAA / AA) | 2 · champ état/grade | Choisir le niveau de reconditionnement | 5×5×3 | 6 | Facette de collection | facette directe de la collection |
| 4 | Fiche `[modèle]` d'occasion (specs, compression, prix) | 2 · specs balles | Acheter un modèle précis reconditionné | 5×5×3 | 6 | Fiche modèle + CTA | « ajouter au panier » |
| 5 | Quelle balle joue `[pro]` + sa vitesse de swing | 3 · balles des pros | Jouer la même balle qu'un pro | 4×3×4 | 4 | Fiche joueur, angle Haute Surprise | « la même balle en occasion » |
| 6 | Distances réelles par club, index `[tranche]` | 5 · data clients (différé) | Se situer et choisir sa balle | 3×3×3 | 2 | Tableau par profil | « balles pour cet index » |
| 7 | Slope + SSS du `[parcours]` | 1 · base parcours | Consulter une valeur pour son calcul d'index | 2×2×5 | 2 | Page parcours + calculateur | faible : autorité et trafic, pas conversion |
| 8 | Quel flex de shaft pour `[vitesse]` | 4 · constantes physiques | Choisir son matériel selon sa vitesse | 2×3×4 | 2 | Page + mini-outil | hors cœur balles |
| 9 | Conversion `[X en Y]` (yards/mètres, mph/km-h) | 4 · constantes physiques | Convertir une mesure | 2×2×4 | 1 | Convertisseur | trafic pur |

## Lecture

Le corpus 2 (specs des balles) rafle les quatre premières places. C'est cohérent avec la GSC : la page qui performe déjà (tableau de compression) sort de cette base. Construire proprement la base modèles paie donc quatre modèles d'un coup, dont les deux seuls à 8.

Les modèles 1 et 2 sont des vecteurs « Do » ([[know-simple-know-do]]) : un comparateur et une reco filtrée, deux formats qu'un AI Overview n'exécute pas à la place de l'utilisateur. Ils sont constructibles tout de suite, sans attendre de volume client, car le mapping profil → compression est public et stable.

Les modèles 7 à 9 captent du trafic mais convertissent mal sur la vente de balles : leur proximité à l'offre est faible. Ils tiennent le rôle d'autorité et de maillage, pas de conversion. Le corpus 1 (parcours) reste utile pour le calculateur d'index et l'autorité locale, mais ce n'est pas là que la vente se joue.

Le modèle 6 (corpus 5) est le seul actif non copiable ([[surprise-gap]]) mais reste différé : il attend la data client. Voir son modèle détaillé : [[modele-corpus-5-golfiller]].

## Top 3 à construire en premier

1. **Comparateur `[X]` vs `[Y]`** (corpus 2). La base specs existe en partie (tableau compression). Le rendre dynamique ouvre des centaines d'URLs `/comparer/` sur des requêtes de pré-achat, chacune maillant vers la fiche produit.
2. **Meilleure balle pour `[profil]`** (corpus 2). Même base, variable = profil. Réponse answer-first + collection filtrée. Golfiller ranke déjà « quelle balle » en position 8 : on capitalise sur un signal prouvé.
3. **Fiche `[modèle]` d'occasion** (corpus 2). Le pont entre le corpus et la vente : chaque comparateur et chaque guide y renvoient, et la page porte le CTA d'achat.

Règle de production maintenue : un modèle ne se lance que si sa base est remplie. Le corpus 2 se remplit à la main (specs publiques par modèle), donc les trois premiers modèles n'ont aucune dépendance bloquante.

Liens : [[corpus-golfiller]], [[modele-corpus-5-golfiller]], [[golfiller-strat-source]], [[pseo-data-driven-models]]
