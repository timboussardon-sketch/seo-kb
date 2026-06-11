---
type: cluster
title: Golfiller, modèles de pages pSEO depuis la GSC
aliases: [modeles-pseo-golfiller]
tags: [golfiller, pseo, modeles-pseo, product-led, gsc, client]
created: 2026-06-10
updated: 2026-06-10
sources: 1
confidence: high
status: stable
---

# Modèles pSEO Golfiller

> **En résumé.** 7 modèles de pages réplicables, tous extraits des requêtes réelles de la GSC ([[2026-06-10-golfiller-gsc-90j]]), zéro mot-clé générique. Les trois à lancer en premier : la page « avis » par modèle de balle (score 8), la page prix « combien coûte une balle de golf » (score 8) et l'industrialisation « une URL par parcours » qui éclate la page tarifs et ses 388 parcours nommés. Chaque modèle maille vers la Money Page occasion.

**Money Page : collections balles de golf occasion / reconditionnées** (`/collections/...`). Point de conversion : achat direct. Les requêtes occasion font déjà 510 clics en pos 2,8 à 4,6 sur 90 jours.

Méthode : skill `seo-modeles-pseo`, Score Business = Proximité offre × Intention d'achat × Faisabilité (1 à 5 chacun), produit ramené sur 10. La faisabilité est lue dans la GSC (position actuelle sur la grappe), pas estimée.

## Tableau des modèles

| Catégorie | Modèle (requête type, réelle GSC) | Variable | Intention | P×I×F | Score /10 | Format de page | Ancre → Money Page |
|---|---|---|---|---|---|---|---|
| Reviews / Avis | « balle inesis tour 900 avis » | modèle de balle | Vérifier avant d'acheter ce modèle | 5×4×5 | 8 | Page avis par modèle : état réel des balles reconditionnées, compression mesurée, verdict + CTA fiche produit | « [modèle] d'occasion » |
| Pricing / Cost | « combien coûte une balle de golf », « prix balle de golf » | neuf vs reconditionné | Connaître le budget avant d'acheter | 5×5×4 | 8 | Page prix : grille par gamme et par état, écart neuf/occasion chiffré sur la data boutique | « balles reconditionnées » |
| Best option | « meilleur balle de golf pour senior », « ...pour joueur moyen » | profil de joueur | Choisir LA balle pour son profil | 5×4×4 | 6 | Page par profil (senior, débutant, joueur moyen, femme, distance) : reco + 3 modèles dispo en occasion | « voir ces balles d'occasion » |
| Comparatif | « inesis tour 900 vs pro v1 », « tp5 vs z star » | modèle A vs modèle B | Trancher entre deux modèles | 5×4×4 | 6 | URL /comparer/[a]-vs-[b], specs côte à côte depuis le tableau de compression existant | « les deux en occasion » |
| Outil / donnée | « balle de golf compression 80 », « [modèle] compression » | valeur ou modèle | Trouver une compression précise | 4×3×5 | 5 | Déclinaison du tableau winner : une ancre/page par tranche de compression, filtre pré-appliqué | « balles compression [X] » |
| Fiche parcours | « tarif golf [parcours] », « slope golf [parcours] » | parcours (388 détectés) | Préparer une partie : tarif, slope, SSS | 3×3×5 | 4 | Une URL par parcours : green fee, slope, SSS, par, longueur + bloc « les balles des joueurs d'ici » | « balles de golf d'occasion » |
| Donnée par club | « vitesse balle de golf fer 7 », « vitesse de swing driver » | club × profil | Consulter sa valeur de référence | 3×2×5 | 2 | Extension du tableau vitesse existant : une section/page par club, data agrégée clients | « balle adaptée à votre vitesse » |

Toutes les requêtes du tableau sont tapées telles quelles dans la GSC : le filtre de requêtabilité humaine est passé par construction.

## Top 3 à créer en premier

1. **Avis par modèle de balle.** Les fiches produit rankent déjà pos 3 à 8 sur « [modèle] avis » sans page dédiée. Faible effort (un gabarit, ~15 modèles au catalogue), conversion immédiate, et la donnée first-party (état des balles reçues, compression mesurée) crée le [[surprise-gap]] qu'aucun site générique ne peut copier.
2. **Page prix.** 1 700+ impressions sur la grappe prix/combien, pos 5 à 10, intention d'achat maximale, et c'est l'argument structurel de Golfiller (l'écart neuf/occasion). Une seule page à produire.
3. **Fiches parcours (industrialisation).** Score conversion plus faible mais c'est le moteur d'autorité thématique : 1 346 requêtes et 388 parcours nommés prouvés sur une seule page. C'est la Phase 2 déjà prévue dans [[golfiller-strat]] : démarrer sur les ~40 parcours dont la donnée slope/SSS existe, étendre vers 100. Le « classement slope golf france » (pos 5) sert de page mère de la grappe.

## Modèle additionnel — Balle par usage/besoin (2026-06-10, scrape blog + GSC non couvert)

Identifié en relisant le blog (qui couvre déjà parcours, compression, spin, vitesse, slope) puis en cherchant les familles de requêtes GSC NON couvertes. Source : [[queries/2026-06-10-golfiller-gsc-6mois]].

| Modèle | Requête réelle | Variable | Intention | P×I×F | Score | Gabarit | Ancre |
|---|---|---|---|---|---|---|---|
| Best-for / Usage | « meilleur balle de golf pour la distance » (265 imp, pos 14,5), « ...pour le contrôle », « balles de golf pour débutants » (167 imp, pos 12,8) | besoin technique (distance, contrôle/spin, toucher, durabilité, petit budget, vent) | Choisir LA balle pour SON besoin | 5×4×4 | 7 | Page par besoin : critère technique (compression/spin du tableau existant) + 3 modèles reco dispo en occasion + CTA fiche | « ces balles d'occasion » |

GSC : ~1 069 imp sur la grappe usage, toutes en position 9 à 15, aucune page dédiée. Demande Do non captée.

**Frontière anti-cannibalisation avec le modèle « Best option / profil » (déjà au tableau ci-dessus) :** le modèle profil segmente par JOUEUR (senior, débutant, femme, joueur moyen), le modèle usage segmente par BESOIN technique (distance, contrôle, vent, durabilité, budget). On ne crée pas deux pages sur la même intention : « débutant » reste sur la page profil, « pour la distance / le contrôle » va sur la page usage. Une page = un axe, maillage croisé entre les deux, cf. [[concepts/cannibalisation]].

## Maillage

Chaque Spoke pointe vers la Money Page occasion avec son ancre du tableau. La Money Page liste les Spokes avis et profils en cross-sell. Les fiches parcours maillent entre elles par région et remontent vers la page mère classement slope, selon [[concepts/maillage-interne]]. Prérequis avant production : trancher la cannibalisation calcul index relevée dans [[2026-06-10-golfiller-gsc-90j]].

Pages liées : [[entities/golfiller]] · [[golfiller-strat]] · [[concepts/product-led-seo]] · [[know-simple-know-do]]
