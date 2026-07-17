---
type: audit
client: victoriagarden
created: 2026-07-10
title: "Victoria Garden : faits vérifiés pour les pages motif (scraping site + routage + sources publiques)"
statut: stable
sources: 5
confidence: high
tags: [victoriagarden, faits, sourcing, distances, tarifs]
---

# Faits vérifiés pour les pages motif

## En résumé

Le scraping du site a rempli 11 des 14 placeholders des trois pages motif. Deux découvertes changent le contenu produit.

**Les distances de la base activités ne tiennent pas.** Sur les 48 lieux annoncés « à pied » dans `base-activites-bordeaux.xlsx`, 43 ont pu être routés. Les 43 sont sous-estimés, écart médian **+12 minutes**, maximum +20. Aucun n'est cohérent. Le Marché des Capucins, annoncé à 5 minutes, est à 11 minutes de marche pour 800 m. La rue Sainte-Catherine, annoncée à 8 minutes, est à 21 minutes pour 1,6 km. Ces chiffres sont déjà publiés dans le hub, le brief et les pages activités.

**Le « tarif dégressif à partir de 30 nuits » n'existe pas.** Le site annonce une remise de 20 % dès 4 nuits, et une remise de 10 % pour toute réservation faite 30 jours à l'avance. La confusion entre « 30 nuits » et « 30 jours à l'avance » vient du brief du hub. Aucun tarif mensuel n'est publié.

---

## 1. Faits établis, scrapés sur victoriagarden.com le 2026-07-10

### Typologies et tarifs

Source : `/destination/appart-hotel-bordeaux-centre/`, tableau publié.

| Typologie | Capacité | Description | À partir de |
|---|---|---|---|
| Studio Lits Jumeaux | 2 personnes | Deux lits séparés | 72 €/nuit |
| Studio Double | 2 personnes | Un lit double | 72 €/nuit |
| Studio Supérieur | 2 personnes | Plus spacieux, lit double | 82 €/nuit |
| Studio Supérieur Terrasse | 2 personnes | Terrasse privée | 82 €/nuit |
| Studio Triple | 3 personnes | Idéal petit groupe | 102 €/nuit |
| Suite | 4 personnes | Espace et confort prolongé | 122 €/nuit |
| Studios Communicants | 4 personnes | Deux studios reliés | 150 €/nuit |

Superficies : 20 à 36 m².

### Remises

- **20 % dès quatre nuits**, soit 57,60 €/nuit sur le studio de base.
- **10 % pour toute réservation effectuée trente jours à l'avance.**

Il n'existe **aucun tarif mensuel publié**, ni aucune dégressivité liée à un seuil de 30 nuits. La page `/appart-hotel-au-mois/` dit seulement « sur des séjours de longue durée, c'est plus économique car vous payez au mois et non pas à la nuitée », sans chiffre.

### Services et suppléments

| Service | Tarif | Source |
|---|---|---|
| Parking sécurisé | 15 € par nuit | Hub + schema `amenityFeature` |
| Petit-déjeuner continental | 12 € par adulte, 6 € par enfant jusqu'à 12 ans | Hub |
| **Animaux** | **12 € par nuit** | Hub |
| Ménage à la demande | 25 €, pour les séjours de 7 nuits et plus | Hub |
| Panier de bienvenue | 25 € pour 2 personnes | Hub |
| Matériel bébé | Sur demande : lit parapluie, chaise haute. Code promo Gambin | Hub |
| Salle de réunion | **Tarifs publiés.** Salon Pauillac (35 m²) : 100 € TTC la demi-journée, 180 € la journée. Salon Margaux (50 m²) : 120 € TTC la demi-journée, 200 € la journée | `/hotel-salle-de-reunion-bordeaux/` et `/reservez-votre-prochain-hotel-pour-votre-seminaire/`, vérifié le 2026-07-17 |

### Facturation entreprise

Question publiée en FAQ sur le hub : « Les factures de Victoria Garden permettent-elles la récupération de TVA pour une note de frais ? » Réponse : **Oui**.

### Identité et coordonnées

Source : JSON-LD `Hotel` de `/appart-hotel-au-mois/`.

- 127 cours de la Somme, 33800 Bordeaux
- Téléphone : +33 5 56 33 48 48
- Coordonnées : 44,825785 / -0,572715
- `petsAllowed: true`, `priceRange: "€€"`

---

## 2. Distances : le problème

Méthode : routage piéton OSRM (`routing.openstreetmap.de/routed-foot`), origine = coordonnées GPS de la résidence extraites du JSON-LD du site. Comparaison avec la colonne `Distance VG (min)` de la base activités, restreinte aux lignes dont la colonne `Transport` vaut exactement « marche ».

| Lieu | Base | Distance réelle | Temps à pied réel | Écart |
|---|---|---|---|---|
| Marché des Capucins | 5 min | 0,8 km | 11 min | +6 |
| Rue Sainte-Catherine | 8 min | 1,6 km | 21 min | +13 |
| Quartier Saint-Michel | 10 min | 1,3 km | 17 min | +7 |
| Cinéma Utopia | 10 min | 1,8 km | 24 min | +14 |
| Librairie Mollat | 12 min | 1,8 km | 24 min | +12 |
| Baillardran | 12 min | 1,9 km | 26 min | +14 |
| Porte Cailhau | 12 min | 1,9 km | 25 min | +13 |
| Palais Gallien | 18 min | 2,9 km | 38 min | +20 |

**43 lieux sur 43 routés sont sous-estimés. Écart médian +12 min. Zéro cohérent.**

Le biais est systématique, ce qui exclut l'erreur de saisie ponctuelle. Deux hypothèses restent ouvertes : la colonne a été estimée à vue, ou elle mesure autre chose que le temps de marche réel (vol d'oiseau converti à une vitesse irréaliste, ou temps en vélo).

Les lignes dont `Transport` vaut « tram A », « tram B » ou « tram C » ne sont **pas** concernées par ce test : un trajet en tram est légitimement plus rapide que la marche. Elles restent à vérifier séparément contre les horaires TBM.

### Distances longue portée, routées

| Destination | À pied | En voiture |
|---|---|---|
| CHU Pellegrin | 3,2 km, 42 min | routage en échec, à refaire |
| Hôpital Saint-André | 1,4 km, 19 min | 1,9 km, 5 min |
| Hôpital Haut-Lévêque (Pessac) | 9,1 km, 121 min | 10,1 km, 15 min |
| Gare Bordeaux Saint-Jean | 1,6 km, 21 min | 2,2 km, 4 min |
| Aéroport Bordeaux-Mérignac | — | 18,0 km, 27 min |

---

## 3. Accès au CHU Pellegrin

L'arrêt **Hôpital Pellegrin** est desservi par les lignes de tram **A et F**, ainsi que par les bus 8, 20, 55, 73 et 80. La station est un terminus partiel de la ligne A. Source : CHU de Bordeaux, Wikipédia (ligne A), Moovit.

**Non vérifié** : le temps de trajet en tram depuis la résidence, et le nombre de correspondances. La résidence n'est pas sur la ligne A. Ne pas écrire « à X minutes en tram » avant d'avoir simulé le trajet sur infotbm.com aux heures de visite.

---

## 4. Chiens dans les parcs

Arrêtés municipaux du conseil de Bordeaux du 15 juillet 2008, appliqués depuis le 15 septembre 2008. Une signalétique est affichée à l'entrée de chaque parc.

| Parc | Chiens non classés | Vérifié |
|---|---|---|
| Jardin Public | Autorisés, tenus en laisse. Catégorie 2 autorisée tenue en laisse et muselée | Oui |
| Parc Bordelais | Autorisés, tenus en laisse | Oui |
| Parc Rivière | — | **Non** |
| Parc Nelson Mandela | — | **Non** |
| Quais de la Garonne | — | **Non** |

Règle générale : les chiens de première catégorie (chiens d'attaque) sont interdits dans tous les parcs et jardins. Les chiens de deuxième catégorie sont interdits dans les petits parcs et squares, même tenus en laisse et muselés. Certains squares sont totalement interdits aux animaux domestiques.

La page bordeaux.fr du règlement n'a pas pu être lue directement (404 sur `/p32229`, redirection vers l'accueil sur l'URL longue). Les deux lignes vérifiées viennent d'une reprise du règlement. **À confirmer sur le PDF de l'arrêté avant publication.**

---

## 5. Ce qui reste introuvable

- **Horaires de réception et procédure d'arrivée tardive.** Absents du site. Seule mention de « 24h/24 » : les vélos en libre-service, pas la réception.
- **Politique de prolongation et d'annulation** pour un séjour d'accompagnement hospitalier.
- **Conditions animaux au-delà du tarif** : poids maximum, nombre, espaces interdits. Le site donne le prix (12 €/nuit) et rien d'autre.
- ~~**Tarif de la salle de réunion.**~~ **Corrigé le 2026-07-17 : ce point était faux.** Les tarifs, surfaces, capacités et équipements des deux salons sont publiés sur le site. Voir [[motif-seminaire-diagnostic-2026-07-17]].
- **Data PMS** : durée moyenne de séjour, motif, part affaires.

Ces quatre points ne s'obtiennent que par le client.

---

## 6. Ce que la page « au mois » révèle sur les motifs

La page `/appart-hotel-au-mois/` nomme elle-même ses profils clients : déménagement en cours, projets professionnels de quelques semaines ou mois, **stage de fin d'études ou échange universitaire d'un mois ou plus**, voyageurs longue durée et nomades numériques, arrivée dans une nouvelle ville.

Le motif « étudiant », que j'avais écarté sur la foi de ses 6 impressions GSC, est donc déjà revendiqué par le site. L'absence d'impressions traduit une page qui ne cible pas la requête, pas une absence de demande. Cela confirme la réserve posée dans le document use cases : ce motif se tranche par un relevé SERP, pas par l'export.

---

## Sources

- victoriagarden.com, pages `/destination/appart-hotel-bordeaux-centre/` et `/appart-hotel-au-mois/`, scrapées le 2026-07-10.
- JSON-LD `Hotel` et `LodgingBusiness` du site (coordonnées GPS, tarifs services).
- Routage piéton et automobile : OSRM public, `routing.openstreetmap.de`, données OpenStreetMap.
- Géocodage : Nominatim, OpenStreetMap.
- CHU de Bordeaux, page d'accès au groupe hospitalier Pellegrin.
- Ville de Bordeaux, règlement des espaces verts, arrêtés du 15 juillet 2008.
