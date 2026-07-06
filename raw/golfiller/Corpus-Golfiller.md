---
type: source
source_type: doctrine
title: "Corpus Golfiller (doctrine de production)"
aliases: [corpus-golfiller]
tags: [golfiller, pseo, product-led, data-proprietaire, corpus, doctrine]
created: 2026-07-06
updated: 2026-07-06
sources: 1
confidence: medium
status: draft
---

# Corpus Golfiller

Note de doctrine, 6 juillet 2026. Même logique que le [[corpus-qadence|Corpus Qadence]], transposée d'un agent vers un e-commerce.

## La règle

Je ne crée pas de pages SEO. Je construis les bases de données dont un outil du site a besoin pour fonctionner, l'outil les lit au moment où l'utilisateur s'en sert, et j'expose ces bases en pages publiques.

Le SEO est le sous-produit du carburant du produit.

C'est la logique que Golfiller applique déjà sans l'avoir formulée. Le calculateur d'index avait besoin du slope et du SSS des parcours : j'ai construit la base parcours, elle est devenue les pages parcours. Le comparateur avait besoin des specs de chaque balle : j'ai construit la base modèles, elle est devenue le tableau de compression qui fait 5 652 clics. Le convertisseur avait besoin des constantes physiques du golf : elles sont devenues les pages conversion.

Une balle de golf d'occasion se vend sur la même mécanique que la concordance de bxble ou le grounding de Fusionn : la donnée nécessaire au produit devient la page.

## Pourquoi ça tient

Une page qui sort d'une base est dense par construction. Un rédacteur ou une IA qui « écrit une page balle de golf » produit du corpus moyen, donc de la commodité, donc rien qui rank sur une verticale déjà tenue par Décathlon et Amazon.

Le coût de la page est déjà payé : la base était nécessaire à l'outil.

La base est stable. Le slope d'un parcours ne bouge pas, la compression d'une Pro V1 non plus. Une page qui repose sur une donnée périssable meurt avec sa donnée.

Sans data propriétaire, on retombe dans le corpus moyen de l'IA. Je le répète depuis le début : la data propriétaire est la matière première, tout le reste est copiable. Sur cette verticale, la data, c'est la base parcours construite à la main et les distances réelles agrégées des clients.

## Ce que j'ai rejeté (et pourquoi)

- Articles « comment choisir sa balle de golf » en prose : intention Know, du corpus moyen, mangé par les AI Overviews. Aucune base dessous, aucune défense.
- Fiches conseil génériques (« les 10 erreurs du golfeur ») : aucune donnée, personne ne les cite, elles ne servent aucun outil.
- Actus produit et nouveautés balles : donnée périssable, la page meurt à la sortie du modèle suivant.
- Guides règles du golf : tout le monde en a un, l'utilisateur ne les cherche pas chez un vendeur de balles.

## Les 5 corpus retenus

| # | Corpus | Ce que l'outil / la page en fait | Pages publiques | Requêtes captées | Taille |
|---|---|---|---|---|---|
| 1 | Base parcours France (slope + SSS) | Le calculateur d'index lit le slope et le SSS pour sortir le différentiel | Calculateur pilier + 1 page par parcours | « slope [golf de X] », « SSS [parcours] », « calcul index golf » | ~100 parcours FR, corpus fini |
| 2 | Base modèles de balles (specs) | Le comparateur et le tableau lisent compression, spin, construction, catégorie par modèle | Tableau de compression + fiches modèle + pages /comparer/x-vs-y | « compression balle X », « pro v1 vs pro v1x », « meilleure balle [profil] » | quelques centaines de modèles, fini |
| 3 | Base balles des pros (+ vitesses de swing) | La page dit quelle balle joue quel pro et croise la vitesse de swing (angle Haute Surprise) | Page balles des pros + fiches joueur | « balle de [joueur] », « vitesse de swing pro » | top mondial + LPGA, fini |
| 4 | Constantes physiques du golf | Convertisseur et projections lisent les formules (yards/mètres, mph/km-h, vitesse→distance, choix de flex) | Convertisseur + page flex/vitesse de swing | « yards en mètres », « quelle vitesse pour quel flex », « distance selon vitesse » | corpus fini de formules |
| 5 | Distances réelles agrégées (data clients) | Le tableau de distances par profil et la reco balle par index sortent de l'observé | Tableau distances par profil + reco personnalisée | « distance moyenne fer 7 », « distance drive par handicap » | différé, dépend du volume clients |

Les corpus 1 à 4 sont finis, bornables, et sortent de bases construites à la main ou de constantes publiques, sans dépendre du volume de trafic.

Le corpus 5 est le seul actif que personne ne peut copier : les distances réelles par profil viennent de l'instrumentation client de Golfiller, pas d'une source publique. C'est lui qui porte la Haute Surprise, celle qui force une IA à citer le site. Anonymisation dès la réception et DPA, comme sur les dashboards clients. On pose le schéma d'agrégation maintenant, on publie quand le volume donne des chiffres solides.

## Le maillage vient tout seul

Une fiche parcours renvoie au calculateur d'index. Le tableau de compression pointe vers la fiche du modèle comparé. La page balles des pros classe ses joueurs par vitesse, donc par flex, donc vers le convertisseur. Cinq corpus, un seul graphe interne, le même effet que Versets vers Lexique sur bxble.

Chaque page se termine sur le même renvoi : la balle qui correspond à ce profil est dans la collection, filtrée.

## Règle absolue de production

Interdit de créer une page dont je n'ai pas la donnée. Chaque page part d'une base réelle : un slope relevé, une compression sourcée, une distance mesurée. La base est muette sur un cas : la page ne se fait pas, on note le trou et on construit la donnée d'abord.

C'est la règle qui a fait ranker Golfiller sur « balle de golf » devant les gros sans un seul lien acheté : sans base dessous, la page est générique, et une page générique sur cette verticale ne passe pas le filtre d'admission.

Conséquence sur les backlogs : la liste des pages d'un corpus se filtre d'abord par la couverture de la base. Le potentiel SEO d'une page passe après la disponibilité de sa donnée.

## Ordre de construction

1. Base modèles de balles. C'est le corpus déjà prouvé en GSC (tableau de compression à 5 652 clics). On la structure proprement, on branche le comparateur dynamique, on ouvre les pages /comparer/x-vs-y.
2. Base parcours France. Pilote déjà actif (~40 parcours). On étend vers ~100 et on ouvre une URL par parcours une fois la pilier validée.
3. Constantes physiques. Convertisseur et page flex déjà produits ; on consolide la base de formules pour qu'ils partagent la même source.
4. Base balles des pros. Page déjà produite ; on l'adosse à une vraie base joueur → balle → vitesse plutôt qu'à un contenu figé.
5. Schéma d'agrégation des distances clients posé tôt, publication plus tard, quand le volume tient.

Discipline de fond : un modèle scalable, une unicité réelle (plus de 70 % du contenu change entre deux pages, sur le fond), une data propriétaire injectée, une montée en charge pilotée par la Search Console. On ne déverse jamais des centaines de pages d'un coup.

Liens : [[golfiller-strat-source]], [[golfiller-conversations]], [[ranker-verticale-niche-sans-backlink]], [[pseo-data-driven-models]]
