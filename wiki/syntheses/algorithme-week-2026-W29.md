---
type: synthese
title: Algorithme — Récap semaine 29 (2026-07-12 au 2026-07-17)
date: 2026-07-19
week: 2026-W29
tags: [synthese, algorithme, recap-hebdo, seo, ia, geo]
status: stable
updated: 2026-08-07
sources_count: 6
---

# Récap semaine 29 — La semaine où le clic est devenu une variable aléatoire

> Synthèse des 6 revues de presse Algorithme publiées entre le 2026-07-12 et le 2026-07-17. Pas d'édition les 18 et 19.

## Tendance dominante

Six éditions, un même fil : la mesure ne tient plus. Le 12, Chris Green montre que ChatGPT sous-traite ses recherches à quatre systèmes internes et que le recouvrement des URLs citées chute de 45 % quand le système change d'une exécution à l'autre. Le 14, Kevin Indig trouve que 91 % des citations IA n'existent que dans un seul moteur. Le 15, deux rapports donnent la part de ChatGPT dans le trafic IA à 92 % et à 62 %. Le 16 et le 17, Google ouvre ses rapports d'impressions IA dans la Search Console sans donner les clics. Chaque édition documente un instrument de mesure cassé, et le marché continue de vendre des dashboards de citation calculés sur un passage unique. C'est la vraie histoire de la semaine : le SEO a passé vingt ans à piloter une position stable et vérifiable, il doit maintenant piloter une probabilité que personne ne sait calculer proprement. La seule mesure qui survit à ce constat, c'est la répétition (même question, plusieurs fois, plusieurs jours) et la donnée de conversion sur ton propre serveur.

## Pilier dominant : SEO — 56 % du volume (15 items sur 27)

Sur les 6 infos du jour et les 21 brèves, 15 items relèvent du SEO au sens classique (Google, SERP, Search Console, données structurées, avis, régulation) et 12 des moteurs de réponse et des agents. Le ratio est trompeur : seulement 5 items sur 27 ne parlent pas d'IA du tout (la suppression d'avis Google du 13, la 7-Eleven update et le bug d'indexation du 14, la propriété Category du 16). Autrement dit, 81 % de l'actualité SEO de la semaine est de l'actualité IA déguisée en actualité Google. Le pilier CONTENU est à zéro sur six éditions, et ce n'est probablement pas un hasard : la production de contenu est passée du côté de la commodité, l'actualité se déplace vers ce qui décide de sa distribution.

## Ce qui fait consensus

- **Le llms.txt ne sert à rien** — confirmé sur trois éditions par trois sources indépendantes : Google Search Central et John Mueller (13/07), DigitalApplied sur l'adoption (15/07), Ahrefs sur les logs (17/07). Chiffres : 97 % des fichiers llms.txt n'ont reçu aucune requête sur 137 000 domaines, 96 % du trafic résiduel vient de crawlers d'audit SEO, les robots ChatGPT et Perplexity pèsent 1 %.
- **L'IA mange l'informationnel et laisse le transactionnel** — même mesure dans deux éditions : 53 % des requêtes informationnelles déclenchent une réponse IA contre 6 % des requêtes d'achat (Agarwal & Sen le 15/07, études AI Overviews 2026 le 16/07). C'est le chiffre le plus actionnable de la semaine.
- **Les clics perdus ne sont pas du déchet** — l'essai randomisé d'Agarwal & Sen casse l'argument de Google : -39,8 % de clics organiques avec AI Overview, mais taux de rebond sous 10 secondes identique dans les deux groupes (~18 %). Les visiteurs que l'IA prend se comportaient comme ceux qu'elle laisse.
- **Une citation IA n'est pas une position, elle ne se reproduit pas** — Green mesure 45 % de chute de recouvrement au changement de système et 11,6 % de questions qui changent de source principale (12/07) ; Indig trouve 91 % de citations mono-moteur sur 3 981 domaines et Semrush ne compte que 36 marques présentes tous les mois dans le top 100 des quatre plateformes (14/07).
- **Ce qui n'est pas en texte lisible par une machine n'existe pas** — YouTube récupéré puis ignoré faute de transcription exploitable (12/07) ; 18 % des essais citent une source tierce même quand le prix est publié, parce qu'il est enfermé dans un calculateur (14/07) ; les fiches produit doivent être structurées pour l'agent Comet de Perplexity (16/07).
- **La Search Console donne les impressions IA, pas les clics** — confirmé les 16 et 17/07. Données à partir du 18 mai 2026, aucun rattrapage rétroactif, aucune date annoncée pour les clics.

## Ce qui fait débat

- **La part réelle de ChatGPT dans le trafic IA** — Previsible l'établit à 92,4 % sur 6,77 M de sessions (17/07), un autre rapport la situe autour de 62 % avec Claude en deuxième (15/07). L'écart vient de la méthode d'attribution. Tim's take, formulé le 15/07 : « Personne ne sait encore compter proprement le trafic IA. Méfiez-vous des chiffres ronds présentés comme une vérité, y compris les miens. »
- **L'ampleur de la perte de clics** — -39,8 % en essai randomisé contrôlé (Agarwal & Sen) contre jusqu'à -58 % rapportés par les éditeurs depuis la bascule du 10 juillet (TechTimes, BigGo). Les deux chiffres ne mesurent pas la même chose : l'un isole l'effet AI Overview toutes choses égales par ailleurs, l'autre agrège un avant/après sans contrôle. À trancher : ne jamais citer les deux dans la même phrase.
- **Google contre la donnée académique** — Google répète depuis un an que l'AI Overview ne retire que des visites sans valeur. L'étude du 1er juillet dit le contraire, avec la seule méthode qui prouve un lien de cause à effet. Le désaccord est tranché : la donnée gagne.
- **Cloudflare contre Cloudflare** — pay-per-crawl en 2025, pay-per-citation depuis le 1er juillet 2026. L'acteur qui contrôle une grosse part des accès au web a changé de doctrine en un an. À suivre, parce que le blocage par défaut des robots à double usage sur les pages avec publicité tombe le 15 septembre et touche tous les comptes gratuits.

## Signaux faibles à surveiller

- **Un tribunal allemand a jugé Google responsable d'une réponse IA erronée** — une ligne dans les chiffres du 16/07, jamais développée. C'est pourtant l'explication mécanique du 53 % contre 6 % : si Google engage sa responsabilité sur la réponse générée, il a intérêt à ne pas répondre à la place du marchand sur les sujets où l'erreur coûte de l'argent. À creuser : la responsabilité juridique comme frontière durable entre ce que l'IA absorbe et ce qu'elle laisse passer.
- **Le régulateur britannique impose à Google des critères de classement objectifs et un préavis avant les changements importants** — six mois pour s'exécuter, trois mois pour la portabilité des données de recherche (17/07). Un préavis officiel avant une core update, ce serait une première en vingt ans. À creuser : ce que Google publiera vraiment, et si l'effet déborde hors du Royaume-Uni.
- **28,8 % du trafic ChatGPT atterrit sur le moteur de recherche interne du site** — info du jour du 17/07, jamais recroisée par une autre source de la semaine. Le modèle sait choisir le domaine et ne sait pas désigner la page. À creuser en priorité, voir l'angle 1 ci-dessous.
- **Ask YouTube ouvert à tous les utilisateurs américains connectés depuis le 6 juillet** — cité une seule fois (12/07). Un deuxième moteur de réponse grand public qui lit les transcriptions pour décider quel extrait ressortir, et qui va s'étendre à d'autres langues. Le triptyque YouTube/LinkedIn/Reddit prend une justification technique supplémentaire.

## Angles à creuser semaine prochaine

### Angle 1 : ton log de recherche interne vaut plus que ton export Semrush

**Pourquoi maintenant** : 28,8 % des visiteurs envoyés par ChatGPT arrivent sur ta page de résultats interne avec une requête déjà tapée dedans (Previsible, 6,77 M de sessions sur 166 sites). Chaque requête de ce log est une page qui manque, formulée par quelqu'un qui te cherchait, toi, et pas ton secteur. Personne d'autre ne l'a. Ça branche directement la doctrine data propriétaire sur une source gratuite, immédiate, et que le marché ignore encore parce qu'il regarde les outils de tracking de citations. Le contre-pied est net : pendant que tout le monde achète un dashboard GEO à 200 € par mois pour mesurer une citation non reproductible, la vraie donnée est dans GA4, filtre source = chatgpt.com, colonne page d'atterrissage.

**Format suggéré** : article long sur organikk.co (protocole d'extraction GA4 + lecture du log + transformation en pages), plus un post LinkedIn court sur le seul chiffre des 28,8 %.

### Angle 2 : la citation IA n'est pas une position, c'est un tirage au sort

**Pourquoi maintenant** : quatre chiffres de la semaine disent la même chose sous quatre angles. Quatre systèmes de recherche internes chez ChatGPT, invisibles et non documentés. 45 % de chute du recouvrement quand le système change entre deux exécutions. 11,6 % de questions qui changent carrément de source principale. 91 % des citations qui n'existent que dans un seul moteur. Le marché vend un score de citation calculé sur un passage unique, et la mécanique sous-jacente rend ce score non reproductible par construction. C'est une inversion expertise disponible tout de suite : la bonne question n'est pas « suis-je cité », c'est « à quelle fréquence sur dix essais ». Le protocole de re-test (cinq questions business, dix exécutions, trois jours) est un livrable vendable en l'état.

**Format suggéré** : post LinkedIn tranchant, plus une page permanente dans `wiki/concepts/` sur la non-reproductibilité de la citation IA, avec le protocole de mesure par répétition.

---

## Index des éditions de la semaine

- [[2026-07-12-revue-presse|2026-07-12]] — Les quatre systèmes de recherche cachés de ChatGPT
- [[2026-07-13-revue-presse|2026-07-13]] — Des avis Google effacés par erreur, sans recours
- [[2026-07-14-revue-presse|2026-07-14]] — Les agents IA et les pages prix illisibles
- [[2026-07-15-revue-presse|2026-07-15]] — Les clics pris par l'AI Overview n'étaient pas des mauvais clics
- [[2026-07-16-revue-presse|2026-07-16]] — Google bascule en réponse IA par défaut
- [[2026-07-17-revue-presse|2026-07-17]] — 28,8 % du trafic ChatGPT atterrit sur la recherche interne

Concepts mobilisés : [[concepts/data-proprietaire]] · [[concepts/know-simple-know-do]] · [[concepts/tabou-visibilite]] · [[concepts/anti-ai-writing]]

---

*Récap auto-généré à partir de `raw/revue-de-presse/`. Pour traiter les angles : ouvre `wiki/queries/` et crée un brief, ou `wiki/posts-linkedin/` pour un draft.*
