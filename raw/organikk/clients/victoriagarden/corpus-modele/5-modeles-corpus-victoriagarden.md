---
type: pseo-strategy
client: victoriagarden
created: 2026-07-10
title: Victoria Garden — les 5 modèles de pages (issus de la stack corpus)
statut: cadrage interne, à valider avec le client
doctrine: feedback-corpus-avant-pages
methode: convergence, candidats testés contre le double-usage exploitation
related:
  - "[[stack-corpus-victoriagarden]]"
  - "[[victoriagarden-brief-hub-appart-hotel-bordeaux-2026-07-01]]"
tags: [victoriagarden, pseo, corpus, modeles, doctrine]
---

# Victoria Garden : les 5 modèles de pages

## En résumé

Cinq modèles, chacun adossé à un corpus qui sert l'exploitation ET la page. Deux s'appuient sur de la data déjà en main (155 activités avec distances, normales Météo-France). Trois demandent un corpus curé une fois, dont un intrant bloquant côté client : la data PMS.

On les classe dans l'ordre de construction : le motif de séjour d'abord, parce que c'est le seul modèle qui touche la réservation directe, le point de fuite identifié par l'audit (les requêtes de nom perdent 41 % de clics, position 1,8 → 4,8 sur « victoria garden bordeaux »).

Deux candidats ont été écartés du top 5, ils sont en fin de note.

## Les 5 modèles

### 1. Appart'hôtel pour [motif de séjour] à [ville]

Corpus : lexique motif × durée × typologie × services non négociables. Curé une fois. Motifs : mutation professionnelle, chantier, mission longue, étudiant, hospitalisation d'un proche, week-end, famille, séjour d'affaires.

Double-usage : c'est le corpus que la réception et le service résa lisent pour qualifier une demande et devise un séjour au mois. L'améliorer améliore le script de qualification.

Template × variable : 1 gabarit × N motifs × 2 villes (Bordeaux, Pau). La page ouvre sur la situation vécue, pas sur l'établissement.
Point de conversion : intention décisionnelle haute, réservation directe. C'est le modèle qui protège et étend `/appart-hotel-au-mois/`, la page la plus forte du site (5 549 impressions, positions 1,9 à 7, non cannibalisée).
Grounding : structure prête, motifs à confirmer par la data PMS. Intrant bloquant côté client.

### 2. Que faire à [quartier ou POI] depuis la résidence

Corpus : les 155 activités avec distance réelle à pied et en tram depuis chaque résidence. Fini, curé, déjà en fichier.

Double-usage : c'est ce que la réception dit toute la journée. Alimente les posts Google Business et l'e-mail pré-séjour. Le pack local est un levier au même rang que la page web sur les deux requêtes principales, et ce corpus le nourrit.

Template × variable : 1 gabarit × N quartiers et POI. La page montre le tableau de distances réelles, pas de la prose touristique.
Point de conversion : intention Know, converti par maillage vers le hub et bloc de disponibilités. C'est le correctif du problème n°2 de l'audit : le trafic éditorial monte de 317 %, le trafic commercial baisse de 13 %.
Grounding : le plus solide des cinq. Six adresses restent à vérifier avant publication.

### 3. Quand venir à [ville] et météo en [mois]

Corpus : normales Météo-France 1991-2020 croisées avec l'affluence et la grille tarifaire. Fini, stable.

Double-usage : sert le yield et l'argumentaire de basse saison, celui qui fait vivre l'offre 30 nuits -10 % en janvier. Aucune chaîne ne publie un contenu daté et sourcé sur les mois creux, parce qu'aucune chaîne n'a intérêt à dire « venez en novembre ».

Template × variable : 1 gabarit × 12 mois × 2 villes, plus une page pilier « quand venir ».
Point de conversion : capte l'intention en amont de la réservation, redirige la demande vers les mois à remplir.
Grounding : data sourcée, prêt.

### 4. Appart'hôtel, hôtel ou location : lequel pour [motif]

Corpus : concordance des avis et objections, balayée depuis les avis Google et Booking et les questions récurrentes en résa.

Double-usage : la réponse aux avis, la formation de la réception, la levée d'objection en direct. Le corpus de la vente, exposé.

Template × variable : 1 gabarit comparatif × N motifs. La page `/airbnb-ou-appart-hotel-a-bordeaux-lequel-est-vraiment-le-moins-cher/` existe déjà : elle est le prototype de ce modèle, pas une page isolée.
Point de conversion : c'est le contenu le plus citable par les IA, et l'argument qui ramène la réservation directe face aux OTA.
Grounding : avis publics disponibles. Prêt dès que le balayage est fait.

### 5. Outils gratuits

Corpus : les preuves chiffrées rendues calculables. Simulateur du coût d'un mois à Bordeaux, comparateur appart'hôtel contre location courte durée sur une durée saisie, générateur d'itinéraire depuis la résidence.

Double-usage : c'est la grille tarifaire et la base activités exposées en public. Sert l'acquisition, pas un contenu à côté.

Template × variable : famille Product-Led, quelques pages à forte intention.
Point de conversion : capture d'e-mail et note « Fully Meets ». Un simulateur de coût au mois adresse frontalement la requête où Victoria domine déjà.
Grounding : dépend de faits tarifaires à jour. Intrant bloquant côté client.

## Ordre de construction

1. Modèle 1 d'abord, dès que la data PMS arrive. Il touche la réservation directe, le point de fuite.
2. Modèle 2 en parallèle, il est prêt et sans dépendance.
3. Modèle 4 en continu, depuis les avis publics.
4. Modèle 3 une fois, il est stable.
5. Modèle 5 quand les faits tarifaires sont validés.

Prérequis transverse, avant tout modèle : résoudre la cannibalisation (8 URL sur le head term) et baliser le hub (Product/Offer, AggregateRating, FAQPage). Sans ça, chaque page ajoutée aggrave la dispersion au lieu de la corriger.

## Ce qui n'est pas un modèle

L'agenda événementiel (`/evenements-bordeaux-2026/`, 1 181 clics) reste une locomotive de trafic, pas un corpus fondateur : il se périme chaque année et ne nourrit ni la réception ni la résa. On le garde, on le maille vers le hub et vers la page motif de la même ville, on ne le multiplie pas.

Les fiches appartement ne sont pas un modèle non plus, ce sont des pages produit. Trois d'entre elles ont décroché depuis la refonte. Elles se réparent par le maillage, pas par un chantier pSEO.

## Liens

[[stack-corpus-victoriagarden]] · [[victoriagarden-brief-hub-appart-hotel-bordeaux-2026-07-01]] · [[victoriagarden-audit-gsc-2026-06-11]]
