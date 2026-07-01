---
type: audit
title: "Victoria Garden : analyse de marché sémantique et cannibalisation sur « appart hotel bordeaux »"
aliases: [victoriagarden-analyse-appart-hotel-bordeaux]
tags: [seo, gsc, client, victoriagarden, cannibalisation, entites-vectorielles, geo, appart-hotel]
created: 2026-07-01
updated: 2026-07-01
sources: 2
confidence: high
status: stable
---

# Victoria Garden : « appart hotel bordeaux », pourquoi on plafonne

Élucidation de la question laissée ouverte dans [[victoriagarden-audit-gsc-2026-06-11]] (« la page money s'est vidée, à creuser en priorité avec l'export requêtes de cette page »). Data : export GSC via `admin-gsc-export` (Fusionn), propriété `https://www.victoriagarden.com/`, fenêtre 2026-04-02 → 2026-07-01 (90 j). Skill sémantique : `seo-entites-vectorielles`. SERP concurrentielle relevée sur données publiques (index US, positions FR à confirmer en relevé manuel).

## En résumé

Sur « appart hotel bordeaux » (3 348 impressions/90 j, position moyenne 8,8, CTR 0,7 %), le problème n'est pas le contenu : c'est l'architecture. Deux causes distinctes se cumulent.

1. **Chute d'impressions** (déjà flaggée le 11/06) : la requête est passée de 10 546 (N-1) à 5 606 (juin) à 3 348 (maintenant). Contraction de couverture / demande / absorption AI Overview. C'est le problème de volume.
2. **Cannibalisation** (apport de cette analyse) : 8 URL de victoriagarden.com se présentent sur la même requête. Google ne tranche pas, aucune ne passe le top 8. C'est le problème de conversion des impressions restantes.
3. **Pack local** : Victoria est 3e dans le pack local sur cette requête (relevé manuel Tim, 11/06). Le pack rabote le CTR organique en position 8.

La page porteuse réelle est `/destination/appart-hotel-bordeaux-centre/` (et non la version EN `/destination/bordeaux/`). Actif à protéger et à ériger en pilier unique : `/appart-hotel-au-mois/`, qui domine proprement le cluster « au mois / longue durée / logement temporaire » (5 549 impressions, positions 1,9 à 7), non cannibalisé, à forte valeur business.

## 1. La data GSC (90 jours)

| Requête | Impressions | Clics | Position |
|---|---|---|---|
| appart hotel bordeaux | 3 348 | 23 | 8,8 |
| appart hotel bordeaux centre | 825 | 4 | 7,6 |
| appartement hotel bordeaux | 514 | 2 | 11,0 |
| appart hôtel bordeaux (accent) | 512 | 4 | 11,1 |
| Cluster générique (69 requêtes) | 9 654 | 137 | ~20 |
| Cluster « au mois / longue durée » (76 req.) | 5 549 | 138 | mixte, dont 1,9-7 |
| Branded (victoria garden bordeaux) | 2 801 | 266 | 4,0 |

Le branded tient. Le générique plafonne : beaucoup d'impressions, peu de clics.

## 2. Cannibalisation prouvée

URL de Victoria qui se présentent en même temps sur « appart hotel bordeaux » :

| URL | Impressions | Position | Rôle attendu |
|---|---|---|---|
| /destination/appart-hotel-bordeaux-centre/ | 3 275 | 8,86 | Pilier réel |
| / (accueil) | 44 | 2,89 | Parasite le head term |
| /appart-hotel-au-mois/ | 21 | 10,95 | Doit rester sur « au mois » |
| /appart-hotel-place-de-la-victoire-bordeaux/ | 2 | 1,5 | Doublon quartier |
| /trouvez-votre-appart-hotel-a-bordeaux-avec-parking/ | 5 | 6,4 | Satellite « parking » |
| /apparthotel-pour-4-personnes-a-bordeaux/ | 1 | 5 | Satellite « famille » |
| /en/ et /es/ | 19-30 | 8-10 | Versions langue mal isolées |

Le cluster « au mois » est propre à l'inverse : /appart-hotel-au-mois/ capte quasi seule (« au mois bordeaux » pos 1,9 ; « longue durée » pos 4,2 ; « logement temporaire bordeaux » pos 6,98 sur 397 impressions).

## 3. Analyse vectorielle des entités attendues

Requête : « appart hotel bordeaux ». Intention : locale, transactionnelle, forte composante comparative.

| Entités Techniques (>80% top 10) | Preuves Quantitatives | Vecteurs Multimodaux | Divergence (Haute Surprise) |
|---|---|---|---|
| appart'hôtel, résidence de tourisme, studio, kitchenette | Prix plancher (72€/nuit) | Photos par typologie | Comparatif appart'hôtel vs Airbnb vs hôtel (page /airbnb-ou-appart-hotel... déjà existante) |
| courte / longue durée, au mois, séjour temporaire | Nb d'appartements (100), capacité | Carte quartiers + POI | Grille « quel quartier selon le motif de séjour » |
| quartiers : Centre, Victoire, Nansouty, Chartrons, Saint-Michel, Mériadeck | Distances gare Saint-Jean / aéroport / centre | Tableau typologies + tarifs | Data first-party (durée moyenne de séjour, % affaires) [À SOURCER interne] |
| POI : Cité du Vin, Place de la Bourse, Grand Théâtre, Saint-Émilion, Arcachon | Note + volume d'avis chiffrés | Bloc avis note agrégée | Angle séjour d'affaires (Mériadeck, salle de réunion, TVA) |
| services : parking, petit-déj, ménage, wifi, animaux, bébé | Tarifs services (petit-déj 12€, parking 15€) | FAQ balisée (FAQPage) | Angle famille : studios communicants |

Gap de la page pilier :
- Technique : pas de données structurées détectées (Product/Offer sur le prix, AggregateRating/Review sur les avis, FAQPage sur les 5 questions déjà présentes).
- Intention : peu de couverture multi-quartiers, pas de comparatif intégré, alors que la SERP récompense le choix (chaînes multi-résidences Adagio/Appart'City/All Suites + agrégateurs Booking/Cozycozy).
- Maillage : les satellites (au mois, parking, famille, place de la Victoire, comparatif Airbnb) ne remontent pas vers un pilier, ils se concurrencent.

## 4. Recommandation (page hub/comparative, validée par Tim le 01/07)

La page pilier existe déjà : `/destination/appart-hotel-bordeaux-centre/`. Le travail est de la désigner pilier unique et de nettoyer autour.

1. Résoudre la cannibalisation d'abord. Un seul pilier sur « appart hotel bordeaux ». Satellites gardés chacun sur leur longue traîne (au mois, parking, 4 personnes, place de la Victoire) et maillés vers le pilier. Sortir l'accueil et les versions langue de la course sur le head term (hreflang + maillage).
2. Transformer le pilier en hub comparatif. H2 par quartier avec distances réelles, H2 comparatif (appart'hôtel / hôtel / location, en réutilisant la page Airbnb), bloc « selon votre séjour » qui route vers au mois et famille.
3. Baliser le technique. Product/Offer + AggregateRating + FAQPage sur des éléments déjà présents. Quick win sous 2 semaines.
4. Capitaliser sur le cluster « au mois ». Différenciation la plus forte et la moins concurrencée. Le hub l'alimente, ne lui prend pas ses requêtes.
5. Ne pas oublier le pack local (GBP) : sur cette requête, une part des clics passe par la fiche Google Business, pas par l'organique. Avis + photos + lien de réservation directe sur la fiche sont au même rang que la page web.

## Suites

- Construire l'architecture hub + satellites via `seo-cluster-aeo` (cluster) et formaliser le plan de résolution via `seo-cannibalisation`.
- Relevé SERP manuel FR pour confirmer positions et présence AI Overview sur le head term.
- À rapprocher de l'alerte marque de [[victoriagarden-audit-gsc-2026-06-11]] et des gains sans création de page de [[victoriagarden-quick-wins-2026-06-11]].
