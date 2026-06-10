---
type: query
title: Golfiller, analyse GSC 90 jours (2026-03-12 au 2026-06-10)
aliases: [golfiller-gsc-90j]
tags: [golfiller, gsc, pseo, product-led, do-vs-know, client]
created: 2026-06-10
updated: 2026-06-10
sources: 1
confidence: high
status: stable
---

# Golfiller, analyse GSC 90 jours

> **En résumé.** Data API Search Console, propriété `https://golfiller.fr/`, du 2026-03-12 au 2026-06-10. Le site fait 5 480 clics / 113 965 impressions sur son top 1000 de requêtes, dont ~29 % de branded. Les pages « Do » dominent tout le non-branded, exactement comme le prédisait [[golfiller-strat]]. Le signal le plus exploitable : une seule page « tarifs des parcours » capte 1 346 requêtes distinctes avec 388 parcours nommés. C'est la preuve par la data que les modèles de pages à variable (parcours, modèle de balle, profil de joueur) sont le prochain levier. Suite : [[modeles-pseo-2026-06-10-golfiller]].

Source : pull API searchAnalytics via la connexion GSC Fusionn (fonction edge `admin-gsc-export`), dimensions query, page et page×query, 90 jours.

## Vue d'ensemble

| Indicateur | Valeur |
|---|---|
| Clics (top 1000 requêtes) | 5 480 |
| Impressions | 113 965 |
| Clics branded (« golfiller » + variantes) | ~1 580 (29 %) |
| « balle de golf » | pos 5,9 · 12 791 imp · 415 clics |
| Requêtes occasion / reconditionné | 510 clics · 7 874 imp · pos 2,8 à 4,6 |

Le branded est en CTR 22 à 84 % selon la variante orthographique (golfiller, golf filler, golfiler, golffiller) : la notoriété directe est réelle.

## Top pages non-branded : le « Do » écrase tout

| Page | Clics | Imp | Pos |
|---|---|---|---|
| /blogs/infos/tableau-comparatif-de-compression-de-balles | 1 310 | 11 427 | 7,3 |
| /blogs/infos/calcul-index-golf | 652 | 22 261 | 7,9 |
| /blogs/infos/quelle-balle-de-golf-pour-quel-joueur | 464 | 8 483 | 6,1 |
| /blogs/infos/vitesse-de-swing-au-golf-tableaux-par-profil... | 377 | 3 723 | 4,8 |
| /blogs/infos/le-tarif-de-chaque-parcours-de-golf-en-france | 160 | 9 535 | 5,6 |
| /pages/guide-de-gradation | 146 | 716 | 5,9 |
| /blogs/infos/connaitre-le-slope-de-votre-golf | 128 | 4 266 | 6,6 |
| /blogs/infos/calculateur-score-differentiel-et-index-golf-whs | 104 | 3 337 | 9,4 |

Aucune page « Know » pure dans le top. Confirmation terrain de [[know-simple-know-do]] : consulter une valeur, calculer, comparer.

## Le signal pSEO : la long tail des pages uniques

- **Tarifs des parcours** : 1 346 requêtes distinctes sur une seule URL, dont **388 parcours nommés** (tarif golf national, golf de prunevelle, tarif golf dunkerque, golf de la gruyère, golf de valescure...). Les requêtes nommées pèsent ~980 impressions sur les 3 337 de la page et la page sort en position 2 à 14 dessus **sans jamais les cibler**. Chaque parcours justifie sa page.
- **Slope** : 36 requêtes sur tout le site (877 imp), dont des requêtes par parcours (« slope golf national », « slope golf etretat ») et « classement slope golf france » (60 imp, pos 5). Même mécanique : la donnée slope + SSS par parcours nommé.
- **Modèles de balles** : 119 requêtes branded-produit (titleist pro v1, srixon ad333, callaway supersoft, tp5...), 12 976 impressions, fiches produit en position 4 à 8. La couche « avis » (« balle inesis tour 900 avis », « titleist tour soft avis ») sort en pos 3 à 11 sans page avis dédiée.
- **Profils de joueurs** : « meilleur balle de golf pour senior » (214 imp, pos 9,8), « meilleures balles de golf pour joueur moyen » (133 imp, pos 4), « quelle balle de golf pour debutant ». La page générique « quelle balle pour quel joueur » plafonne en pos 9-11 sur ces variantes.
- **Prix** : « prix balle de golf » (1 406 imp, pos 9,7), « combien coûte une balle de golf » (313 imp, pos 5,5). Intention d'achat directe, aucune page dédiée.

## Points de vigilance

1. **Cannibalisation index** : `/calcul-index-golf` (pos 7,9) et `/calculateur-score-differentiel-et-index-golf-whs` (pos 9,4) se partagent la famille « calcul index golf » (46 requêtes, 8 588 imp). À trancher : un seul calculateur canonique, l'autre en satellite maillé, cf. [[concepts/cannibalisation]].
2. **« balles de golf » au pluriel** : pos 15,9 (7 166 imp) contre 5,9 au singulier. La home capte le singulier, personne ne capte proprement le pluriel.
3. **CTR de la home** : 4 030 clics pour 67 078 impressions (6 %) en pos 6,3. Une part vient des requêtes parcours/tarif où la home sort à la place d'une page dédiée inexistante.

Pages liées : [[entities/golfiller]] · [[golfiller-strat]] · [[modeles-pseo-2026-06-10-golfiller]] · [[concepts/product-led-seo]]
