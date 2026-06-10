---
client: Golfiller
site: golfiller.fr
secteur: E-commerce balles de golf occasion / reconditionnées (Shopify)
type: Fiche projet (suivi accompagnement SEO)
statut: en cours
ouvert: 2026-06-10
---

# Golfiller

> **En résumé.** [[entities/golfiller|Golfiller]] (golfiller.fr) vend des balles de golf d'occasion et reconditionnées. Cas SEO phare de Tim : top 1-6 sur « balle de golf » devant les sites d'autorité du secteur, sans un seul lien acheté. La GSC (90 jours, 2026-03-12 au 2026-06-10) confirme que les pages winners sont toutes des pages « Do » (tableau de compression, calcul d'index, tarifs des parcours, slope). Le chantier en cours : répliquer ces patterns en [[concepts/pseo-data-driven-models|modèles de pages pSEO]], en partant des requêtes réelles de la GSC, jamais des mots-clés génériques. Analyse complète : [[2026-06-10-golfiller-gsc-90j]]. Modèles de pages scorés : [[modeles-pseo-2026-06-10-golfiller]].

---

## 1. Le client

- **Activité** : vente en ligne de balles de golf d'occasion, reconditionnées et de lots (Shopify, collections par modèle et par lot).
- **Modèle de conversion** : achat direct sur la boutique. Pas de devis, pas de call : le SEO doit amener l'acheteur sur une fiche produit ou une collection.
- **Positionnement** : la verticale « balles d'occasion » plutôt que l'affrontement frontal sur le matériel de golf généraliste. Autorité thématique de niche défendable.
- **Stratégie source** : [[golfiller-strat]] (doctrine croisée), log de travail dans [[golfiller-conversations]].

## 2. État SEO (GSC 90 jours, data réelle)

- 5 480 clics et 113 965 impressions sur le top 1000 des requêtes. Environ 29 % des clics sont branded (« golfiller » et variantes, CTR 22 à 84 %).
- **« balle de golf »** : position 5,9, 12 791 impressions, 415 clics. La requête tête est tenue.
- **Requêtes occasion / reconditionné** (le cœur business) : 510 clics, 7 874 impressions, positions 2,8 à 4,6. Marge de progression vers le top 3 stable.
- **Les winners sont des « Do »** : tableau de compression (1 310 clics), calcul d'index (652 clics, 22 261 impressions), quelle balle pour quel joueur (464 clics), vitesse de swing (377 clics, position 4,8), tarifs des parcours (160 clics, 9 535 impressions), slope (128 clics).
- **Signal pSEO majeur** : la page unique « tarif de chaque parcours de golf en France » ranke sur 1 346 requêtes distinctes, dont 388 parcours nommés (« tarif golf national », « golf de prunevelle », « tarif golf dunkerque »...). Une seule page absorbe toute une grappe : chaque parcours mérite sa page.
- **Point de vigilance** : `/blogs/infos/calcul-index-golf` et `/blogs/infos/calculateur-score-differentiel-et-index-golf-whs` rankent tous les deux sur la famille « calcul index golf ». Cannibalisation à surveiller, cf. [[2026-06-10-golfiller-gsc-90j]].

## 3. Chantier en cours

1. **Modèles de pages réplicables** identifiés et scorés depuis la GSC : [[modeles-pseo-2026-06-10-golfiller]]. Patterns à variable : parcours nommé (tarif + slope + SSS), avis par modèle de balle, meilleure balle par profil, comparateur modèle vs modèle, prix.
2. **Phase 2 pSEO parcours** (prévu dans [[golfiller-strat]]) : passer de la page unique à une URL par parcours, base de ~40 parcours à étendre vers ~100.
3. **5 outils « Do »** déjà priorisés dans la stratégie source (calculette index, quiz balle, carte de score, tableau distances, comparateur).

## 4. Accès data

- GSC branchée via les `google_connections` Fusionn (propriété `https://golfiller.fr/`). Export à la demande par la fonction edge `admin-gsc-export` (projet Supabase fusionn).
