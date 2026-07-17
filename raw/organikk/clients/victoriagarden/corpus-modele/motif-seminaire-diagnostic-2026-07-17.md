---
type: pseo-strategy
client: victoriagarden
created: 2026-07-17
title: "Victoria Garden — motif séminaire : diagnostic et intrants réels"
statut: cadrage interne, à valider avec le client
doctrine: feedback-corpus-avant-pages
methode: agrégation GSC par motif (export 2026-06-11) + scraping des 4 pages existantes le 2026-07-17
related:
  - "[[5-modeles-corpus-victoriagarden]]"
  - "[[stack-corpus-victoriagarden]]"
  - "[[victoriagarden-faits-verifies-2026-07-10]]"
  - "[[victoriagarden-audit-gsc-2026-06-11]]"
tags: [victoriagarden, pseo, motif, seminaire, cannibalisation, corpus]
---

# Motif séminaire : diagnostic et intrants réels

## En résumé

Le séminaire est le plus gros motif non traité de Victoria Garden : 9 454 impressions sur trois mois pour 42 clics, soit 0,44 % de CTR. Ce n'est pas un manque de page, c'est l'inverse. Quatre URL se partagent le cluster, dont deux qui décrivent les mêmes salons aux mêmes tarifs dans les mêmes termes.

Le chantier n'est donc pas d'écrire une page de plus. C'est de résoudre une cannibalisation à 4 URL, exactement comme celle à 8 URL traitée sur « appart hotel bordeaux » le 2026-07-01.

Contrairement à ce que supposait le cadrage du 10 juillet, il n'y a presque aucun intrant bloquant. Les tarifs, les capacités et les équipements des deux salles sont publiés sur le site. La liste des intrants réellement manquants tient en cinq lignes, et aucun ne bloque le démarrage.

## Correction du fichier de faits du 10 juillet

[[victoriagarden-faits-verifies-2026-07-10]] indique « Salle de réunion : existe, tarif non publié » et range « tarif de la salle de réunion » parmi ce qui « ne s'obtient que par le client ». C'est faux.

Le tarif est publié sur `/hotel-salle-de-reunion-bordeaux/` et sur `/reservez-votre-prochain-hotel-pour-votre-seminaire/`, dans le corps de page et dans la meta description. Les deux lignes concernées du fichier de faits sont à corriger.

## La data GSC

Source : export Search Console du 2026-06-11, trois derniers mois.

### Par page

| Page | Impressions | Clics | CTR | Position |
|---|---|---|---|---|
| `/reservez-votre-prochain-hotel-pour-votre-seminaire/` | 5 606 | 15 | 0,27 % | 23,4 |
| `/trouver-une-salle-de-formation-a-bordeaux/` | 1 845 | 12 | 0,65 % | 7,0 |
| `/hotel-salle-de-reunion-bordeaux/` | 1 558 | 11 | 0,71 % | 24,2 |
| `/entreprises-et-groupes/` | 445 | 4 | 0,90 % | 11,0 |
| **Total** | **9 454** | **42** | **0,44 %** | — |

### Par requête

L'agrégation des 1 648 requêtes de l'export sur le motif (séminaire, salle de réunion, salle de formation, entreprise, team building, congrès) donne 77 requêtes et 6 975 impressions. L'écart avec le total par page vient des requêtes anonymisées par Google, absentes de la dimension requête. Le total par page fait foi.

Trois sous-intentions se distinguent nettement.

**Le séminaire hôtelier**, la plus grosse en volume, la plus mal placée. « hotel seminaire bordeaux » fait 619 impressions en position 11,7, « hôtel pour séminaire » 307 impressions en position 21,5, « seminaire bordeaux » 258 impressions en position 29,9. L'essentiel du cluster est entre la position 20 et la position 45, donc invisible.

**La salle de formation**, la plus petite en volume et de loin la mieux placée. « location salle de formation bordeaux » fait 538 impressions en position 5,4, « salle de formation bordeaux » 265 impressions en position 6,9, « salle de formation » 239 impressions en position 5,3, « louer salle de formation bordeaux » 38 impressions en position 3,8. Environ 1 420 impressions se tiennent autour de la position 5.

**La salle de réunion**, intermédiaire. « salle de réunion bordeaux » fait 156 impressions en position 31,8, « hotel salle de reunion bordeaux » 109 impressions en position 10,8.

## Ce que le diagnostic révèle

### La cannibalisation

`/reservez-votre-prochain-hotel-pour-votre-seminaire/` et `/hotel-salle-de-reunion-bordeaux/` publient le même contenu : les deux salons, les mêmes surfaces, les mêmes capacités, les mêmes tarifs, les mêmes équipements inclus, les mêmes suppléments. Deux URL, un seul corpus. Elles se disputent les mêmes requêtes et sortent toutes les deux autour de la position 24.

`/entreprises-et-groupes/` est un hub commercial qui couvre cinq segments (déplacement pro, comités d'entreprise, séminaires, autocaristes, équipes sportives) sur deux villes, et qui renvoie vers un e-mail commercial. Il capte 445 impressions en position 11 sans être une page séminaire.

### La page qui ranke le mieux travaille contre l'offre

`/trouver-une-salle-de-formation-a-bordeaux/` est la seule page du cluster en première page, en position 7,0 sur 1 845 impressions. C'est cohérent avec la doctrine corpus : c'est la seule des quatre qui est un relevé comparatif plutôt qu'une plaquette. La densité paie.

Mais son contenu pose un problème business direct. Elle compare Victoria Garden à l'Espace Callipolis et à Kobo, affiche Callipolis à 15 € TTC la demi-journée contre 100 € pour le salon Pauillac, et conclut en toutes lettres « le moins cher : Espace Callipolis ». La meilleure page du cluster oriente le lecteur vers une autre adresse, et elle le fait sur la sous-intention où Victoria Garden est déjà en position 5.

C'est ce qui explique un CTR de 0,65 % en position 7. La page ranke, elle ne vend pas.

Deux réserves avant d'y toucher. Les tarifs des autres lieux ne sont pas datés sur la page et n'ont pas été revérifiés à leur source : ils peuvent être périmés. Et la comparaison porte sur des objets différents, une salle de coworking de 50 m² sans équipement dédié contre un salon équipé avec vidéoprojecteur et écran. Le comparatif est à reconstruire à périmètre égal, pas à supprimer.

## Les faits publiés, vérifiés le 2026-07-17

Source : scraping de `/hotel-salle-de-reunion-bordeaux/` et `/reservez-votre-prochain-hotel-pour-votre-seminaire/`.

| Salon | Surface | Conférence | Disposition en U | Demi-journée | Journée |
|---|---|---|---|---|---|
| Pauillac | 35 m² | 20 personnes | 15 personnes | 100 € TTC | 180 € TTC |
| Margaux | 50 m² | 25 personnes | 20 personnes | 120 € TTC | 200 € TTC |

Inclus dans chaque réservation : vidéoprojecteur, écran de projection, paperboard, wifi. La page formation ajoute la climatisation et le mobilier modulable.

Suppléments : café d'accueil à 5 € par personne (café, thé, viennoiseries), pause matin ou après-midi à 3 € par personne (café, thé, jus de fruits).

Accès publié : tram B, arrêts Saint-Nicolas et Victoire à 30 mètres. Depuis Euratlantique, 15 à 20 minutes en transport en commun. Depuis Mériadeck, environ 10 minutes.

Réserve : la page séminaire annonce « à 5 minutes à pied de la Place de la Victoire » et « à proximité immédiate de la gare Saint-Jean ». Le routage OSRM du 10 juillet donne 21 minutes à pied pour la gare Saint-Jean, à 1,6 km. Le même biais de sous-estimation que dans la base activités se retrouve donc dans les pages déjà en ligne.

## Les intrants réellement manquants

Aucun ne bloque le démarrage du chantier. Ils conditionnent la profondeur des pages, pas leur existence.

1. **Le séminaire à Pau.** `/entreprises-et-groupes/` porte la mention « Séminaires : Bordeaux seulement », alors que les autres segments couvrent les deux villes. À confirmer : Pau n'a pas de salle, ou la salle existe et n'est pas commercialisée. La réponse décide si le modèle se décline sur deux villes ou une seule. La GSC montre par ailleurs une demande de Pau sur d'autres motifs (« hotel famille béarn », 32 impressions).

2. **La capacité d'hébergement d'un groupe.** Cent appartements sont annoncés, mais rien ne dit combien de collaborateurs peuvent être logés simultanément sur un séminaire, ni s'il existe un seuil de blocage. C'est la première question que pose un organisateur.

3. **Le forfait séminaire.** `/entreprises-et-groupes/` annonce « deux types de services, à la carte et au forfait » et « des tarifs toujours adaptés à vos besoins », sans un chiffre. Un forfait par personne incluant nuit, petit-déjeuner, salle et pauses est la brique qui manque pour répondre à « séminaire avec hébergement » (47 impressions) et « logement et salle pour séminaire » (46 impressions).

4. **La location à l'heure.** « salle de réunion à l'heure bordeaux » sort à 10 impressions. Les tarifs publiés démarrent à la demi-journée. À confirmer avant d'écrire quoi que ce soit sur ce format.

5. **La data PMS sur le segment affaires.** Part des séjours affaires, saisonnalité des séminaires, durée moyenne. C'est le seul intrant réellement inaccessible sans le client, et il reste le même que pour tous les autres motifs.

## Ce que je recommande

Le corpus séminaire existe déjà et il est complet. Il est simplement éclaté sur quatre URL, dont deux jumelles, et sa meilleure page recommande un autre lieu.

L'ordre logique, calqué sur ce qui a été fait pour « appart hotel bordeaux » le 2026-07-01 :

1. Trancher la cannibalisation entre la page séminaire et la page salle de réunion. Elles portent un seul corpus, elles doivent devenir une seule page hub, l'autre partant en 301 vers elle. La règle d'élagage tient : redirection vers la page la plus proche, jamais de 410.
2. Reconstruire le comparatif des salles de formation à périmètre égal, avec des tarifs datés et sourcés, et le mailler vers le hub. C'est la page qui ranke, c'est celle qui a le plus à gagner et le moins à risquer.
3. Baliser le hub. Un séminaire est une offre chiffrée avec des capacités et des tarifs publics, donc Product, Offer et FAQPage sont applicables immédiatement, sans attendre le moindre intrant client.
4. Corriger les distances annoncées sur les pages en ligne, qui reprennent le biais de la base activités.

Le modèle « Appart'hôtel pour [motif] à [ville] » ne s'applique pas tel quel ici. Le séminaire n'est pas un motif de séjour individuel, c'est une offre à part avec son propre point de conversion, le service commercial. Il mérite son hub, pas une page motif de plus.

## Liens

[[5-modeles-corpus-victoriagarden]] · [[stack-corpus-victoriagarden]] · [[victoriagarden-faits-verifies-2026-07-10]] · [[victoriagarden-audit-gsc-2026-06-11]] · [[victoriagarden-journal-appart-hotel-bordeaux-2026-07-01]]

## Sources

- Google Search Console, export victoriagarden.com du 2026-06-11, dimensions Requêtes (1 648 lignes) et Pages, trois derniers mois comparés à N-1.
- victoriagarden.com, pages `/reservez-votre-prochain-hotel-pour-votre-seminaire/`, `/trouver-une-salle-de-formation-a-bordeaux/`, `/hotel-salle-de-reunion-bordeaux/` et `/entreprises-et-groupes/`, scrapées le 2026-07-17.
- Routage piéton OSRM du 2026-07-10, repris de [[victoriagarden-faits-verifies-2026-07-10]].
