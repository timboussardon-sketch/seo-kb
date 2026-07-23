---
type: query
title: "Victoria Garden — les mots-clés business non traités"
aliases: [vg-business-non-traites, decisionnels-victoriagarden]
tags: [victoriagarden, mots-cles, decisionnels, business, pseo, cannibalisation]
created: 2026-07-23
updated: 2026-07-23
sources: 4
confidence: medium
status: draft
---

# MOTS-CLÉS DÉCISIONNELS — Victoria Garden : ce qui n'est pas encore traité

## En résumé

Le site couvre 72 pages indexables. J'ai croisé leurs title et H1 avec les 1 645 requêtes de l'export GSC et avec 375 relevés Google Suggest faits aujourd'hui. Il reste **17 clusters business sans page dédiée**, dont 6 qui pèsent déjà des impressions réelles sans qu'aucune page ne les vise.

Le plus gros trou est aussi le plus simple : **la kitchenette**. C'est ce qui distingue l'offre d'un hôtel classique, le mot est présent dans le corps de 27 pages, et **aucun title ni H1 ne le porte**. « hôtels avec kitchenette bordeaux » sort à 125 impressions en position 12,1 pour zéro clic.

Le deuxième est le **logement temporaire** : 792 impressions en position 8,2 sur trois mois, six formulations confirmées par Suggest avec la ville, et zéro page. Il avait été repéré le 17 juillet hors commande, il ressort ici en tête de la data.

Le troisième n'est pas un mot-clé mais un gabarit : **l'hébergement par établissement de santé**. La page hospitalisation existe mais reste générique, alors que Suggest nomme le CHU Pellegrin, l'hôpital Haut-Lévêque, la clinique Tivoli, Bordeaux Nord, Saint-Augustin et Bel-Air. Un gabarit, huit établissements.

Trois pages en double ont aussi été trouvées au passage, toutes indexables avec canonical sur elles-mêmes.

## Méthode et sourcing

- Inventaire des pages : sitemaps Yoast du 2026-07-23, 140 URL, 72 pages FR indexables hors mentions légales et fiches appartement. Title, H1 et corps de page récupérés sur chacune.
- Export GSC victoriagarden.com du 2026-06-11, 1 645 requêtes, trois derniers mois. 166 requêtes de nom, 1 479 hors nom, dont **1 075 requêtes business** pour 48 978 impressions et 336 clics (les 404 requêtes restantes sont éditoriales : restaurants, boulangeries, événements).
- Google Suggest (`hl=fr`, `gl=fr`), relevé du 2026-07-23 : 375 seeds testés, dont expansion alphabet sur `appart hotel bordeaux`, `appart hotel pau`, `hotel au mois bordeaux` et `location courte durée bordeaux`.
- Aucun volume affiché. Les chiffres des tableaux viennent tous de l'export GSC, jamais d'une estimation.

**Définition retenue de « traité »** : une page dont le title ou le H1 vise le cluster. Un mot présent dans le corps d'une page ne compte pas, sinon la kitchenette serait couverte 27 fois.

**Colonne `Suggest`** : ✓ = formulation remontée telle quelle par Google Suggest. ✗ = construite par expansion, non confirmée.

## Le score de conversion

Proximité à l'offre × intention d'achat × faisabilité de ranker, chaque axe sur 5, produit ramené sur 10.

La faisabilité tient compte d'un fait structurant : **Victoria Garden a une seule adresse à Bordeaux** (cours de la Somme, Place de la Victoire) et une seule à Pau. Tout mot-clé de quartier où la résidence n'est pas implantée est écarté, quelle que soit sa demande.

## Les 17 clusters non traités

### Rang 1 — Score 10/10

| Cluster | Suggest | Étage | GSC (imp · clics · pos) | Page cible | Format | CTA |
|---|---|---|---|---|---|---|
| **hôtel avec kitchenette bordeaux** | ✓ | Do — Local | 140 · 0 · 12,1 | Nouvelle page satellite du hub | Tableau des équipements de cuisine par typologie, avec ce qui est fourni et ce qui ne l'est pas | Réserver en direct |
| **logement temporaire bordeaux / pau** | ✓ | Do — Local | 792 · 13 · 8,2 | Nouvelle page, deux villes | Page motif : durée, résiliation, facturation, ce qu'on fournit | Devis séjour long |

Sur la kitchenette, Suggest confirme aussi « hotel avec cuisine bordeaux ». Les deux formulations tiennent sur une seule page.

Sur le temporaire, Suggest confirme six formulations **avec la ville** : logement, hébergement, location, résidence, studio et appartement temporaires à Bordeaux. C'est le seul cluster de cette note qui obtient la ville dans Suggest sur autant de variantes.

### Rang 2 — Score 8/10

| Cluster | Suggest | Étage | GSC (imp · clics · pos) | Page cible | Format | CTA |
|---|---|---|---|---|---|---|
| **hébergement par établissement de santé** | ✓ | Do — Local | 28 · 0 · 27,0 | Gabarit × 8 établissements, satellites de la page hospitalisation | Distance réelle, ligne de tram, horaires de visite, tarif accompagnant | Réserver |
| **hôtel proche Zénith / Palais Beaumont / Stade du Hameau (Pau)** | ✓ | Do — Local | 0 | 3 pages, gabarit de la page Arkea Arena | Distance à pied, accès soir de spectacle, parking | Réserver |
| **location courte durée bordeaux / pau** | ✓ | Do — Local | 513 · 4 · 18,9 | Nouvelle page, deux villes | Comparatif durée par durée face à la location entre particuliers | Réserver |
| **capacités manquantes à Pau (3, 4, 6 personnes)** | ✗ | Do — Local | non isolable | 3 pages, gabarit déjà en production à Bordeaux | Identique aux pages Bordeaux | Réserver |
| **mois manquants à Bordeaux (mars, avril, mai, octobre)** | ✗ | Do — Local | non isolable | 4 pages, gabarit déjà en production | Identique aux 9 pages mois existantes | Réserver |

Sur la santé, la page `/appart-hotel-hospitalisation/` existe et cite Pellegrin dans son corps, mais son H1 reste générique. Suggest confirme « hôtel proche chu pellegrin bordeaux », « logement proche chu pellegrin bordeaux », « hotel proche hopital haut leveque pessac », « hotel proche clinique tivoli bordeaux », « hotel proche clinique bordeaux nord », « hotel proche clinique saint augustin bordeaux », « hotel proche clinique bel air bordeaux » et « hotel proche clinique du sport bordeaux ». Huit établissements nommés, un seul gabarit.

Sur Pau, la page Arkea Arena fait 2 753 impressions à Bordeaux. Les trois équipements de Pau ont chacun leur formulation confirmée dans Suggest, et aucune page.

Sur la courte durée, une réserve : la première suggestion est « location courte durée bordeaux réglementation », donc une partie de l'intention est juridique et non commerciale. La page doit ouvrir sur l'offre, pas sur la réglementation.

Les capacités et les mois sont les deux seuls clusters où le gabarit tourne déjà. Sept pages, un coût de production quasi nul.

### Rang 3 — Score 6/10

| Cluster | Suggest | Étage | GSC (imp · clics · pos) | Page cible | Format | CTA |
|---|---|---|---|---|---|---|
| **hôtel proche gare Saint-Jean bordeaux** | ✓ | Do — Local | 149 · 2 · 10,6 | Nouvelle page | Temps de trajet réel, ligne de tram, arrivée tardive | Réserver |
| **hébergement parc des expositions / palais des congrès** | ✓ | Do — Local | 0 | Nouvelle page, ou refonte de l'article existant | Accès, horaires de salon, facture entreprise | Devis |
| **annulation gratuite / réservation en direct** | ✓ | Do — Comparatif | 0 | Bloc sur le hub + page dédiée | Comparaison des conditions en direct et via les plateformes | Réserver en direct |
| **séminaire et salle de réunion à Pau** | ✓ | Do — Local | 0 | Bloqué : intrant client | À définir | Devis |

La gare Saint-Jean est le seul mot-clé de quartier défendable en dehors de la Victoire, et il demande de l'honnêteté : le routage OSRM donne 21 minutes à pied pour 1,6 km, pas les 5 minutes annoncées ailleurs sur le site. La page se tient sur le tram C, pas sur la marche.

Le parc des expositions a déjà un article sur le site, mais c'est un contenu touristique, pas une page d'hébergement. Suggest confirme « hotel proche parc des expositions bordeaux » et « logement parc des expositions bordeaux ».

L'annulation gratuite est le seul cluster de la liste qui répond directement à l'alerte n°1 de l'audit du 11 juin, la perte de 41 % des clics sur les requêtes de nom au profit des plateformes. Suggest confirme « appart hotel bordeaux annulation gratuite ».

Le séminaire à Pau reste bloqué par la même question qu'au 17 juillet : la mention « Séminaires : Bordeaux seulement » sur `/entreprises-et-groupes/` n'a pas été tranchée.

### Rang 4 — Score 5/10 et moins

| Cluster | Suggest | Étage | GSC (imp · clics · pos) | Décision |
|---|---|---|---|---|
| **chambre à louer pau** | ✓ | Do — Local | 387 · 2 · 8,8 | Bloc sur la page Pau au mois, pas de page |
| **résidence hôtelière bordeaux / pau** | ✓ | Do — Local | 174 · 0 · 14,4 | Variante lexicale à intégrer au hub |
| **hôtel proche Matmut Atlantique / Cité du Vin** | ✓ | Do — Local | 0 | À garder en réserve |
| **hôtel autonome / sans réception bordeaux** | ~ | Do — Local | 51 · 0 · 10,0 | Bloc services, pas de page |
| **hôtel avec balcon / terrasse bordeaux** | ✗ | Do — Local | 62 · 0 · 20,1 | Bloc sur la fiche studio terrasse |
| **note de frais, TVA et facture entreprise** | ✓ | Know commercial | 0 | Bloc B2B, fort potentiel de citation IA |

Sur « chambre à louer pau », attention au même type de piège que sur « comité entreprise bordeaux ». Les 387 impressions sont réelles et la position 8,8 est bonne, mais Suggest complète vers « studio à louer pau le bon coin » et « logement à louer pau », donc vers de la location entre particuliers et de la colocation. Une partie de ce trafic ne réservera jamais une nuitée. Le bloc se justifie, la page non.

Sur la note de frais, Suggest confirme « tva hotel note de frais », « récupération tva note de frais hotel » et « facture hotel note de frais ». C'est national, sans ville, et c'est du contenu que les moteurs de réponse citent volontiers. Ça ne convertit pas seul, ça arme la page entreprises.

## Trois pages en double trouvées au passage

Ce n'est pas de la recherche de mots-clés, mais ça conditionne tout ce qui précède : chaque page ajoutée sur un site qui se cannibalise aggrave la dispersion.

| Doublon | Statut | Ce qu'il faut faire |
|---|---|---|
| `/entreprises-et-groupes-copie/` vs `/entreprises-et-groupes/` | Les deux dans le sitemap, canonical sur elles-mêmes, aucune balise robots | 301 de la copie vers l'originale |
| `/votre-sejour-en-apparthotel-a-bordeaux-en-novembre/` vs `/chambre-dhotel-a-bordeaux-en-novembre/` | Deux pages pour le même mois, les deux indexables | 301 vers la plus forte des deux |
| `/reservez-votre-prochain-hotel-pour-votre-seminaire/` vs `/hotel-salle-de-reunion-bordeaux/` | Déjà diagnostiqué le 17 juillet | Fusion en un hub, 301 de l'autre |

La règle d'élagage tient dans les trois cas : redirection 301 vers la page la plus proche, jamais de 410.

## Ce qui n'est pas dans la liste, et pourquoi

**Les quartiers de Bordeaux où la résidence n'est pas.** Suggest est très fertile sur « appart hotel bordeaux lac », « bruges », « mérignac », « pessac », « chartrons », « belvédère », « bassins à flot », et la GSC montre 109 impressions sur « appart hotel floirac ». Toutes ces SERP sont tenues par des chaînes qui ont réellement une adresse sur place. Écrire une page « appart hôtel Bordeaux Lac » depuis la Place de la Victoire serait une promesse fausse, et la requête ne serait pas satisfaite. Seule la gare Saint-Jean passe, parce que le tram C la relie directement.

**Le logement étudiant, stagiaire et alternant.** Suggest confirme « logement stagiaire bordeaux », « logement alternant bordeaux », « residence alternant bordeaux » et « logement alternant pau ». Mais les complétions partent toutes vers le CROUS, les résidences étudiantes et des budgets de 250 à 300 euros par mois. L'offre ne rentre pas dans cette fourchette. La GSC confirme : 6 impressions sur trois mois, en position 54,5.

**L'hébergement de chantier et d'ouvriers.** Le cadrage du 10 juillet le listait comme motif de séjour. Suggest renvoie **zéro suggestion** sur « hébergement chantier bordeaux » et « hébergement chantier pau ». Le motif existe commercialement, il ne se cherche pas sur Google. Pas de page.

**Les salons, congrès, concerts et tournages.** Zéro suggestion sur « hebergement salon professionnel bordeaux », « hebergement congres bordeaux », « hotel pour concert bordeaux » et « hebergement tournage bordeaux ». Même verdict que pour les autocaristes et les ministères au 17 juillet : segments de relation commerciale, pas de recherche.

## Un désalignement à signaler, qui n'est pas un mot-clé manquant

« appart hotel pau » fait **1 986 impressions en position 6,8** sur trois mois. La page qui répond est `/destination/visiter-pau/`, dont le slug et le H1 disent « visiter Pau » et non « appart'hôtel à Pau ». Le title est correct, le reste ne l'est pas.

Bordeaux a son hub sur `/destination/appart-hotel-bordeaux-centre/`. Pau n'a pas d'équivalent. C'est le plus gros écart entre la demande réelle et la structure du site, et il se corrige sans écrire une page de plus.

Dans le même registre, « hotel pau pas cher » fait 1 323 impressions en position 12,3 pour **zéro clic**, alors que `/appart-hotel-pas-cher-a-pau/` existe. La page est là, elle ne remonte pas.

## Top 5 à attaquer en premier

1. **La kitchenette.** Score 10, aucune page, et c'est l'argument qui distingue l'offre d'un hôtel. Le mot est déjà écrit partout dans les corps de page, il ne manque qu'un H1.
2. **Le logement temporaire, deux villes.** Score 10, 792 impressions déjà acquises en position 8,2, six formulations confirmées avec la ville. C'est le plus gros volume réel de la liste.
3. **Les 7 pages de gabarit.** Trois capacités à Pau, quatre mois à Bordeaux. Le modèle tourne déjà, le coût de production est marginal, et ça complète deux séries incomplètes.
4. **Le gabarit établissements de santé.** Huit pages depuis un gabarit, sur un motif où l'offre est objectivement meilleure qu'un hôtel classique.
5. **Les trois doublons en 301.** À faire avant les quatre points précédents, pas après.

## Liens

[[recherche-2026-07-17-victoriagarden-b2b-sport-cse]] · [[motif-seminaire-diagnostic-2026-07-17]] · [[5-modeles-corpus-victoriagarden]] · [[stack-corpus-victoriagarden]] · [[victoriagarden-audit-gsc-2026-06-11]] · [[victoriagarden-quick-wins-2026-06-11]] · [[entities/victoria-garden]] · [[concepts/mots-cles-decisionnels]] · [[concepts/know-simple-know-do]] · [[concepts/cannibalisation]]

## Sources

- victoriagarden.com, sitemaps Yoast (`post`, `page`, `destination`, `apartment`), relevés le 2026-07-23 : 140 URL, 72 pages FR analysées (title, H1, corps).
- Google Search Console, export victoriagarden.com du 2026-06-11, dimensions Requêtes (1 645 lignes) et Pages (136 lignes), trois derniers mois comparés à N-1.
- Google Suggest (`suggestqueries.google.com`, `hl=fr`, `gl=fr`), relevé du 2026-07-23 : 375 seeds, dont expansion alphabet sur 4 seeds fertiles.
- Vérification des balises canonical et robots sur les 4 pages en doublon, le 2026-07-23.
