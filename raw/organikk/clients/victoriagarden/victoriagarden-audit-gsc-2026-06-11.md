---
type: audit
title: "Victoria Garden : audit GSC complet, évolution positions et trafic (3 mois vs N-1)"
aliases: [victoriagarden-audit-gsc]
tags: [seo, gsc, client, victoriagarden, audit, quick-win]
created: 2026-06-11
updated: 2026-06-11
sources: 2
confidence: high
status: stable
---

# Victoria Garden : évolution des positions et du trafic

Données : exports GSC du 2026-06-11, périodes comparées « 3 derniers mois » vs « même période l'année dernière ». 137 pages, 1 645 requêtes. Bruts immuables dans `raw/data/exports-gsc/victoriagarden-2026-06-11/`.

## En résumé

Le global a l'air excellent : clics +47 % (2 808 → 4 130), position pondérée 18,8 → 10,0. Mais en séparant marque / hors-marque et commercial / éditorial, trois mouvements opposés.

1. **La marque recule, c'est l'alerte n°1.** -41 % de clics marque. « victoria garden bordeaux » passe de la position 1,8 à 4,8, « victoria garden pau » de 1,8 à 6,1. Le site n'est plus premier sur son propre nom : quelqu'un intercepte de la réservation directe (schéma classique des OTA dans l'hôtellerie, relevé SERP manuel à faire pour confirmer).
2. **Le hors-marque explose (×4,3) mais c'est du Know.** 70 nouvelles pages, et les locomotives sont éditoriales : `/evenements-bordeaux-2026/` fait 1 181 clics à elle seule. Pendant ce temps, le trafic des pages commerciales baisse de 13 %. Le trafic monte, les réservations potentielles non, tant que ces pages ne maillent pas vers la résa.
3. **La page money s'est vidée.** `/destination/appart-hotel-bordeaux-centre/` gagne 15 places (25,3 → 9,8) et perd quand même 555 clics : ses impressions se sont effondrées de 121 000 à 33 000. À élucider en priorité avec l'export requêtes de cette page.

Côté opportunités : ~+1 500 clics/trimestre sans créer de page, détaillés dans [[victoriagarden-quick-wins-2026-06-11]] (boulangeries de Pau +438, Bordeaux centre +273, monuments +205, fiches actions title/méta/FAQ et densification atomique incluses). Première action à valider : le relevé SERP marque, pour savoir qui est passé devant et sur quel format.

## 1. Les chiffres globaux

| Indicateur | N-1 | 3 derniers mois | Évolution |
|---|---|---|---|
| Clics | 2 808 | 4 130 | +47 % |
| Impressions | 373 726 | 242 686 | -35 % |
| Position pondérée (impressions) | 18,8 | 10,0 | +8,8 places |
| Requêtes en positions 4-10 | 117 | 410 | ×3,5 |
| Requêtes en positions 21+ | 787 | 305 | -61 % |
| Pages nouvelles / disparues | | 70 / 4 | |
| Requêtes nouvelles / perdues | | 162 / 19 | |

La lecture rapide serait « tout va bien ». Elle est fausse : la hausse des clics et la chute des impressions viennent de mouvements différents, qu'il faut séparer marque / hors-marque et commercial / éditorial pour comprendre.

## 2. Alerte n°1 : la marque recule

161 requêtes contiennent « victoria ». Sur ce périmètre : 1 509 → 896 clics (-41 %), position pondérée 13,2 → 8,8 mais avec un effondrement sur les requêtes qui comptent :

| Requête | Clics N-1 → maintenant | Position N-1 → maintenant |
|---|---|---|
| victoria garden bordeaux | 408 → 260 | 1,8 → 4,8 |
| victoria garden bordeaux centre | 237 → 153 | 2,7 → 7,3 |
| victoria garden pau | 144 → 79 | 1,8 → 6,1 |
| hotel victoria garden bordeaux | 66 → 31 | 1,9 → 8,3 |
| appart hotel victoria bordeaux | 30 → 7 | 1,9 → 16,8 |

Le site ne se positionne plus premier sur son propre nom. Quelqu'un capte cette demande à sa place : à vérifier en SERP réelle, mais le schéma classique sur l'hôtellerie, ce sont les OTA (Booking, Expedia) et les agrégateurs qui prennent le dessus quand la page de marque faiblit. C'est de la réservation directe (sans commission) qui part ailleurs : la priorité business numéro un de cet audit, avant tout le reste.

## 3. Le hors-marque explose, tiré par l'événementiel

1 484 requêtes hors marque : 239 → 1 040 clics (×4,3), position pondérée 33,9 → 11,1. La stratégie de nouvelles pages fonctionne : 70 pages nouvelles, 162 requêtes nouvelles. Les locomotives :

| Page | Clics N-1 → maintenant | Position |
|---|---|---|
| /evenements-bordeaux-2026/ | 0 → 1 181 | 6,5 |
| /appart-hotel-au-mois/ | 0 → 321 | 8,6 |
| /evenements-pau-2026/ | 0 → 254 | 6,9 |
| /restaurant-etoile-bordeaux/ | 4 → 159 | 34,0 → 10,6 |
| /les-meilleures-boulangeries-de-pau/ | 8 → 78 | 31,4 → 9,2 |

À noter : `/appart-hotel-au-mois/` (321 clics, page commerciale) et `/appart-hotel-place-de-la-victoire-bordeaux/` montrent que le modèle marche aussi sur du décisionnel, pas seulement sur de l'info.

## 4. Alerte n°2 : le mix de trafic s'est inversé

En classant les pages par type (heuristique sur les URLs) :

| Type de pages | Clics N-1 | Clics maintenant |
|---|---|---|
| Éditorial / événements | 499 | 2 079 |
| Commercial (destinations, appartements, mois) | 2 113 | 1 833 |

Le trafic total monte de 47 %, mais le trafic commercial baisse de 13 %. La croissance est du Know (festival bordeaux 2026, fête du vin, boulangeries), pas du Do. Ce trafic a de la valeur seulement s'il est travaillé : maillage systématique des pages événements vers les pages de réservation de la même ville, bloc de disponibilités, capture d'e-mail (la doctrine [[concepts/know-simple-know-do]] s'applique telle quelle).

Le cas qui résume tout : `/destination/appart-hotel-bordeaux-centre/` passe de la position 25,3 à 9,8 (excellente progression) et perd pourtant 555 clics, parce que ses impressions tombent de 121 462 à 32 893. La requête « appart hotel bordeaux » elle-même perd la moitié de ses impressions (10 546 → 5 606). La page rankait l'an dernier, loin mais sur un univers de requêtes très large ; cet univers s'est contracté. À creuser en priorité dans GSC (liste des requêtes de cette page N-1 vs maintenant) pour départager : perte de couverture sur des requêtes larges, baisse de demande, ou AI Overviews qui absorbe les variantes informationnelles.

## 5. Les quick wins (potentiel chiffré : ~+1 500 clics/3 mois)

Détail complet, tableau et fiches actions dans [[victoriagarden-quick-wins-2026-06-11]]. Les cinq plus gros :

| Page | Position | Impressions/3 mois | CTR réel vs attendu | Potentiel |
|---|---|---|---|---|
| /les-meilleures-boulangeries-de-pau/ | 9,2 | 17 163 | 0,5 % vs ~3 % | +438 clics |
| /destination/appart-hotel-bordeaux-centre/ | 9,8 | 32 893 | 2,2 % vs ~3 % | +273 clics |
| /monuments-bordeaux/ | 7,7 | 9 348 | 0,8 % vs ~3 % | +205 clics |
| /appart-hotel-place-de-la-victoire-bordeaux/ | 9,6 | 7 480 | 0,5 % vs ~3 % | +186 clics |
| /restaurant-etoile-bordeaux/ | 10,6 | 23 279 | 0,7 % vs ~1 % | +121 clics |

## 6. Pertes sèches à reprendre

Trois pages produits ont décroché : `/apartment/studio-double-appart-hotel-pau/` (42 → 2 clics, position 9,3 → 16,0), `/apartment/suite-executive-appart-hotel-bordeaux/` (13 → 2, position 11,8 → 32,5, impressions divisées par 28) et `/apartment/studio-lits-jumeaux-appart-hotel-bordeaux/` (8 → 1). Les fiches appartement perdent du terrain pendant que l'éditorial monte : vérifier qu'elles sont encore maillées depuis les nouvelles pages et qu'elles n'ont pas été appauvries à la refonte.

## 7. Plan d'action priorisé

1. **Marque (cette semaine).** Relevé SERP manuel sur « victoria garden bordeaux / pau / bordeaux centre » : qui est passé devant, et sur quel format (OTA, fiche Google Business, agrégateur). Renforcer les pages de marque (title, schéma Organization/Hotel, avis) et l'entité.
2. **Money page Bordeaux centre.** Export GSC des requêtes de la page N-1 vs maintenant pour expliquer les -88 000 impressions, puis recouvrir les requêtes perdues (sections, FAQ).
3. **Quick wins.** Dérouler les fiches de [[victoriagarden-quick-wins-2026-06-11]], en commençant par les deux pages à plus de 17 000 impressions.
4. **Convertir l'événementiel.** Maillage systématique événements → page de réservation de la ville + bloc de capture sur les 5 pages locomotives. Sans ça, les 2 079 clics éditoriaux restent du trafic, pas des réservations.
5. **Fiches appartement.** Re-maillage et réenrichissement des 3 fiches en perte.
6. **Mesure.** Fiche preuve à J+30 et J+90 sur chaque action (boucle sortie → apprentissage).

Sources : [[sources/2026-06-11-victoriagarden-gsc-export]] · données brutes `raw/data/exports-gsc/victoriagarden-2026-06-11/` · méthode quick wins [[concepts/intention-recherche]]
