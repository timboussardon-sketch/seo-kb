---
type: pseo-strategy
client: victoriagarden
created: 2026-07-10
title: Victoria Garden — la stack corpus (doctrine « corpus d'abord, pages ensuite »)
statut: cadrage interne, à valider avec le client
doctrine: feedback-corpus-avant-pages
related:
  - "[[victoriagarden-audit-gsc-2026-06-11]]"
  - "[[victoriagarden-analyse-semantique-appart-hotel-bordeaux-2026-07-01]]"
  - "[[victoriagarden-brief-hub-appart-hotel-bordeaux-2026-07-01]]"
  - "[[5-modeles-corpus-victoriagarden]]"
tags: [victoriagarden, pseo, corpus, doctrine, hotellerie]
---

# Victoria Garden : la stack corpus

## En résumé

On ne conçoit pas des pages SEO pour Victoria Garden. On part de la donnée dont l'exploitation a besoin (réception, réservation directe, fiche Google Business, yield saisonnier), on construit ces corpus, l'exploitation les utilise, et on les expose en pages. Le SEO est le sous-produit.

Chez Leexi, le produit qui lit le corpus est le logiciel. Ici, le produit qui lit le corpus est humain : la réception qui répond « que faire à pied depuis la résidence », le service résa qui devise un séjour au mois, la fiche Google Business qui capte le clic avant le lien organique. Un corpus qui n'aide personne à l'accueil ou à la vente n'est pas un corpus, c'est un chantier contenu.

Deux corpus existent déjà et personne d'autre ne les a : la base de 155 activités avec distances réelles depuis la résidence, et les normales Météo-France Bordeaux-Mérignac 1991-2020. Ce qui manque n'est pas la matière, c'est la donnée d'exploitation (PMS) : durée moyenne de séjour, motif de séjour, part affaires. C'est le seul intrant qu'on ne peut pas produire à leur place.

## Le test à passer avant tout modèle de page

Un modèle de page n'existe que si son corpus sert l'exploitation ET la page. On refuse tout corpus dont le grounding est cher ou périssable. C'est ce qui disqualifie l'agenda événementiel comme corpus fondateur, alors même que `/evenements-bordeaux-2026/` fait 1 181 clics : il se périme chaque année, il ne nourrit ni la réception ni la résa, et son trafic est du Know qui ne convertit pas tant qu'il n'est pas maillé.

## La stack corpus de Victoria Garden

| Couche | Équivalent Leexi | Type | Ce que le corpus fait pour l'exploitation | Page qui en sort |
|---|---|---|---|---|
| 1. Lexique motif de séjour × typologie × services | Types de réunion (couche 1) | Curé | Le corpus que la réception et le service résa lisent pour qualifier une demande. Chaque motif (mutation, chantier, mission, étudiant, hospitalisation d'un proche, week-end, famille, affaires) a sa durée, sa typologie adaptée, ses services non négociables (kitchenette, studios communicants, facture TVA, parking, animaux, matériel bébé). Améliorer ce corpus, c'est améliorer le script de qualification et le devis longue durée. | « Appart'hôtel pour [motif] à [ville] » : le pSEO décisionnel qui protège `/appart-hotel-au-mois/` |
| 2. Corpus lieux et distances | Connexions curées (couche 4) | Curé (fini) | Les 155 activités avec distance réelle à pied et en tram depuis chaque résidence. C'est ce que la réception dit toute la journée, ce qui alimente les posts Google Business et l'e-mail pré-séjour. Aucune chaîne ne l'a, parce qu'aucune chaîne n'est ancrée à une adresse. | Page activités, blocs distances du hub, longue traîne « appart hôtel [quartier] » |
| 3. Corpus climat, saisonnalité et affluence | (propre à VG) | Curé (fini, stable) | Normales Météo-France 1991-2020 croisées avec l'affluence et la grille tarifaire. Sert le yield et l'argumentaire de basse saison, celui qui fait vivre l'offre 30 nuits -10 % en janvier. | « Quand venir à [ville] » et « météo [ville] en [mois] » |
| 4. Concordance des avis et objections | Concordance des problématiques (couche 2) | Balayé | Extrait des avis Google, Booking et des questions récurrentes en résa : ce que le client demande avant de réserver, ce qui le fait annuler, ce qui le fait revenir. Sert la réponse aux avis, la formation de la réception, et la levée d'objection en direct. Le travail était de toute façon nécessaire. | FAQ balisée, comparatif appart'hôtel vs hôtel vs location, blocs preuve |
| 5. Corpus de preuves chiffrées | Preuves chiffrées client (couche 5) | Accumulé | Prix plancher par typologie, capacités, tarifs de services, note et volume d'avis, durée moyenne de séjour, part affaires. Ce sont les faits que la page doit afficher et que le balisage doit exposer (Product/Offer, AggregateRating, FAQPage, tous absents aujourd'hui). Sert directement la réservation directe face aux OTA. | Schema sur le hub, comparatifs chiffrés, pages tarifs |

Les couches se nourrissent. Une page motif (couche 1) cite une distance réelle (couche 2), recommande un mois de venue (couche 3), lève une objection tirée des avis (couche 4) et affiche un prix balisé (couche 5). Le maillage suit les liens réels entre corpus, il n'est pas une carte de clusters plaquée après coup. C'est ce qui répare, par construction, la cannibalisation à 8 URL sur « appart hotel bordeaux ».

## Deux types de corpus

Fini et curé une fois : les distances (couche 2) et le climat (couche 3). Ils existent déjà en fichier, ils bougent peu, ils servent l'exploitation dès demain.

Balayé depuis un corpus source : la concordance des avis (couche 4), calculée depuis les avis Google et Booking. Le coût marginal de la page est quasi nul.

## Ordre de construction

1. Couches 1 et 5 d'abord. Le motif de séjour est le seul corpus qui touche la réservation directe, et les preuves chiffrées sont ce qui manque au hub pour convertir ses impressions. Ce sont les deux angles à plus forte valeur, et ils portent l'alerte n°1 de l'audit : les requêtes de nom perdent 41 % de clics, la réservation directe part chez les OTA.
2. Couche 2 tout de suite après : elle est prête, le fichier existe, six adresses restent à vérifier.
3. Couche 3 au fil des saisons, elle est stable et se publie une fois.
4. Couche 4 en continu, vague par vague, depuis les avis déjà publiés.

## Ce que ça change concrètement

Le point de départ n'est plus « quelles pages créer autour d'appart hotel bordeaux ». C'est : de quoi la réception a besoin pour qualifier un séjour au mois, et de quoi la fiche Google Business a besoin pour reprendre la première place sur le nom. On construit ce corpus, l'exploitation l'utilise, on l'expose.

Le hub comparatif et le plan de maillage déjà produits restent la couche d'exposition. Ils ne sont plus le point de départ.

## Intrants bloquants côté client

- Data PMS : durée moyenne de séjour, motif de séjour, part affaires. Sans elle, la couche 1 sort avec des motifs supposés au lieu de motifs mesurés.
- Faits tarifaires à jour par typologie et par service, pour baliser Product/Offer sans inventer un prix.
- Les six adresses marquées « à vérifier » dans la base activités.

## Liens

[[5-modeles-corpus-victoriagarden]] · [[victoriagarden-audit-gsc-2026-06-11]] · [[victoriagarden-analyse-semantique-appart-hotel-bordeaux-2026-07-01]] · [[victoriagarden-brief-hub-appart-hotel-bordeaux-2026-07-01]]
