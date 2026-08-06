---
type: revue-presse
title: "Algorithme — édition du 6 août 2026"
date: 2026-08-06
pilier_info_jour: business-seo
sources: 12
confidence: high
status: draft
---

# Algorithme — édition du 6 août 2026

## L'essentiel en 5 points

- Google a confirmé le 5 août un bug d'enforcement automatique qui a flaggué à tort des blogs hébergés sur Blogger comme malware le 4 août, en affichant un compte à rebours à 89 jours avant suppression permanente.
- Le thread officiel de support Blogger 457259506 recense au moins 298 propriétaires touchés, plusieurs blogs opérant depuis 12 à 18 ans sans signal correspondant dans Search Console ni Safe Browsing.
- Le message officiel de Google indique une mauvaise détection de « moins d'un jour » alors que les tableaux de bord affichent 89 jours ; deux sources primaires indépendantes (PPC Land, BleepingComputer) documentent des restaurations dès le 5 août sans procédure d'appel.
- Une étude Pieter Serraris publiée le 5 août sur Search Engine Land mesure sur 272 propriétés Bing un biais anglais dans le fetch AI : ChatGPT récupère 65 à 79 % de pages en anglais quand les autres langues existent, avec un index de représentation à 2,6.
- People Inc. (parent PEOPLE, Better Homes & Gardens) a déclaré le 5 août lors de son appel Q2 que la part de trafic Google Search est tombée à 21 % contre « près de deux tiers » historiquement.

## Info du jour — Business SEO : un bug d'enforcement Google verrouille des blogs Blogger de 12 à 18 ans avec un compte à rebours à 89 jours

Le 4 août 2026 dans la soirée, des propriétaires de blogs hébergés sur Blogger ont reçu un email de suppression citant la politique « Malware et contenu malveillant similaire » de Google, tandis que leur tableau de bord affichait un compte à rebours de 89 jours avant suppression permanente ([PPC Land](https://ppc.land/blogger-owners-face-89-day-deletion-clock-as-google-malware-flags-misfire/) ; [BleepingComputer](https://www.bleepingcomputer.com/news/google/google-blogger-locks-hundreds-of-blogs-in-malware-false-positive/)). Le 5 août à 19 h 58, Google a répondu à PPC Land : « We are aware of a bug that incorrectly flagged some Blogger-hosted sites as malware for less than a day. We are working on a fix. » ([PPC Land](https://ppc.land/blogger-owners-face-89-day-deletion-clock-as-google-malware-flags-misfire/)).

Le thread officiel du support Blogger 457259506 recense au moins 298 propriétaires ayant cliqué « I have the same question », plus de 100 réponses de publieurs touchés, et documente des blogs opérant depuis 12 à 18 ans sans signaux correspondants dans Search Console ni Safe Browsing ([Blogger Community](https://support.google.com/blogger/thread/457259506/august-4-2026-false-positives-for-malware-and-similar-malicious-content-policy?hl=en) ; [BleepingComputer](https://www.bleepingcomputer.com/news/google/google-blogger-locks-hundreds-of-blogs-in-malware-false-positive/)). Les Product Experts de Google, cités par BleepingComputer, ont confirmé qu'il ne s'agissait pas d'une opération concertée contre une catégorie éditoriale mais d'une erreur de classification à large échelle par les systèmes de scan automatique ([BleepingComputer](https://www.bleepingcomputer.com/news/google/google-blogger-locks-hundreds-of-blogs-in-malware-false-positive/)). Les restaurations ont commencé le 5 août sans appel formel, PPC Land documente des blogs restaurés puis re-supprimés durant la fenêtre d'incident ([PPC Land](https://ppc.land/blogger-owners-face-89-day-deletion-clock-as-google-malware-flags-misfire/)).

Trois points méritent d'être isolés du bruit médiatique. Le premier : la déclaration de Google et l'interface utilisateur se contredisent factuellement. Google parle d'un flag « de moins d'un jour », le tableau de bord affiche un compte à rebours de 89 jours avant destruction du contenu. La différence n'est pas cosmétique. Un propriétaire de blog qui n'a pas suivi l'actualité SEO du 5 août voit littéralement un compte à rebours de suppression sur ses 12 ans de contenu, sans confirmation de résolution côté produit. Le second : aucun des sites touchés n'avait de signal correspondant dans Search Console ni dans Safe Browsing, deux outils qu'un opérateur SEO utilise habituellement pour vérifier l'état de santé d'un site avant de faire confiance à un signalement automatique. La détection s'est donc faite en dehors de la procédure de vérification usuelle. Le troisième : la population touchée n'est pas anecdotique. BleepingComputer estime la plateforme Blogger à environ 200 000 sites totaux d'après des trackers tiers ; l'échantillon des 298 propriétaires actifs sur le thread officiel plus les « thousands » évoqués dans les mentions Reddit et X (non chiffrés) constitue une part non-négligeable de la base.

Pour un opérateur SEO qui a placé une part significative de son actif éditorial sur une plateforme d'hébergement propriétaire, le fait mesuré ici chiffre un risque qui restait jusqu'à présent hypothétique. Le compte à rebours à 89 jours est le fait franchement neuf. La doctrine [[concepts/arbitrage-plateforme-publication]] décrit le choix de plateforme comme un arbitrage vers là où Google envoie le clic (Substack, YouTube, LinkedIn, Reddit). Le cas Blogger inverse le raisonnement : quand on choisit une plateforme d'hébergement gratuite propriété du même moteur qui juge le contenu, le risque d'enforcement automatique s'ajoute au risque de position. Un consultant SEO qui audite un client dont l'actif principal est sur Blogger doit désormais compter un scénario documenté de perte totale sur 89 jours, sans corrélation avec les outils de vérification usuels. La question actionnable devient : quelle procédure de sauvegarde et de portage sur un domaine propriétaire mettre en place avant qu'un bug analogue ne redémarre. La question doctrinale ouverte : cette classe de risque plateforme mérite une fiche concept propre distincte de l'arbitrage vers-la-plateforme-visible-en-SERP, à discuter en revue hebdo.

Le fait est également une fenêtre inhabituelle sur la calibration des systèmes de scan automatique de Google. Les Product Experts, en confirmant que l'incident n'était pas ciblé, ont exposé que le taux de faux positifs des systèmes automatiques d'enforcement dépasse le seuil auquel un opérateur SEO peut se fier à Safe Browsing seul pour évaluer un site tiers. C'est un caveat méthodologique pour les workflows d'audit qui reposent sur Safe Browsing comme signal de propreté.

**Prédictions :**
- **P-2026-08-06-1** : un autre grand hébergeur de blogs (WordPress.com, Substack, Medium) publie ou voit documenté un incident enforcement automatique similaire avec compte à rebours de suppression avant le 31 décembre 2026 (confidence 0,40).
- **P-2026-08-06-2** : Google modifie l'interface Blogger pour ne plus afficher de compte à rebours de suppression tant qu'un flag n'est pas confirmé humainement, avant le 31 mars 2027 (confidence 0,35).

## Brèves

### GEO — ChatGPT récupère 65 à 79 % de pages en anglais quand les autres langues existent, mesure Serraris sur 272 sites Bing

Pieter Serraris (Strategy Director OMcollective) publie le 5 août 2026 sur Search Engine Land une analyse de logs serveurs et de données de citation AI sur 272 propriétés Bing multilingues et 26 propriétés pour l'analyse ChatGPT ([Search Engine Land](https://searchengineland.com/multilingual-websites-english-pages-ai-visibility-484251)). Le fait chiffré : ChatGPT récupère 65 à 79 % de pages en anglais quand les versions locales existent, avec un index de représentation à 2,6 (2,6 fois la part proportionnelle attendue). Copilot et Google AI Mode affichent une préférence anglaise nettement moindre à l'agrégat, respectivement 52 % et 28 % de gain pour les sites qui ajoutent un dossier `/en/`, contre 122 % pour ChatGPT. La fenêtre d'observation est de 30 jours pour la sous-analyse ChatGPT, non spécifiée pour la partie Bing.

Le fait se lit sur deux plans. Sur le plan doctrinal, il ajoute une dimension de mesure aux 3 métriques Aggarwal formalisées dans [[concepts/metriques-visibilite-geo]] (Imp_wc, Imp_pos, Subjective Impression) : la langue de fetch devient un attribut de citation distinct de la position et de la densité. Sur le plan opérationnel, la recommandation Serraris est prudente : n'ajouter du contenu anglais que s'il peut être maintenu sur le long terme, une page anglaise obsolète pesant négativement plus qu'une absence. La règle dure explore s'applique : Serraris est une source nouvelle (index 0,55 initial, cadrage OMcollective), le corroborant est [Weglot](https://www.weglot.com/blog/multilingual-seo-ai-visibility) qui rapporte un gain « +327 % » sur un panel plus large mais sans méthodologie ouverte. Deux sources qui pointent dans la même direction, une seule primaire, chiffre à traiter comme direction et non comme valeur de référence.

### Actualité SEO — Google Content API for Shopping se retire le 18 août 2026, HTTP 410 côté v2.1

Google a signalé la retraite définitive de la Content API for Shopping au 18 août 2026, remplacée par la Merchant API modulaire ([Productsup](https://www.productsup.com/blog/google-merchant-api-migration-what-changes-before-the-august-2026-deadline-and-how-to-prepare/) ; [ALM Corp](https://almcorp.com/blog/google-shopping-api-migration-deadline-2026/)). Le mécanisme est explicite : à partir du 19 août, les appels aux endpoints v2.1 de la Content API renverront un HTTP 410 Gone. Les intégrations manuelles (upload de fichier, feeds Google Sheets, fetch programmés) restent opérationnelles ; la retraite ne concerne que les intégrations API programmatiques.

Deux notes opérationnelles. La première : la deadline du 18 août est présentée comme sans extension prévue. Un consultant qui audite un client marchand doit vérifier la présence d'une intégration Content API v2.1 et, le cas échéant, la marge de sécurité disponible pour migrer avant J-12. La seconde : cette retraite s'articule avec le rebranding de Merchant Center Next en Merchant Center intervenu en juillet 2026 et l'ajout d'AI Performance Insights (déjà couvert dans l'édition du 2 août). L'ensemble constitue une refonte cohérente du stack Merchant côté API et côté interface, à documenter comme telle plutôt qu'en événements isolés.

### Business SEO — People Inc. déclare que Google Search est tombé à 21 % de son trafic contre « près de deux tiers » historiquement

Lors de son appel de résultats Q2 le 5 août 2026, Neil Vogel (CEO de People Inc., parent de People, Better Homes & Gardens et Investopedia) a déclaré que Google Search représente désormais 21 % du trafic du groupe, contre « près de deux tiers » historiquement ([Nieman Lab](https://www.niemanlab.org/2026/07/search-traffic-has-declined-so-much-that-some-publishers-are-considering-opting-out-of-google-entirely/) contexte). Vogel a également indiqué que bloquer entièrement les crawlers Google est « entirely on the table » sans avoir pris cette décision au moment de l'appel.

Le chiffre est un fait documenté qui n'était disponible qu'en agrégats sectoriels jusqu'à présent (Semrush : USA Today -50 %, Politico -23 %, CNN -25 %, Business Insider -85 % entre juin 2025 et juin 2026 selon l'agrégation Nieman Lab). Pour un consultant qui audite un client publisher, la baisse quantifiée d'un groupe de la taille de People Inc. donne une référence terrain de plus. La question ouverte : combien de publishers du top 100 US atteindront un seuil similaire (moins d'un quart du trafic issu de Google) avant que blocking devienne majoritaire dans le peer group. La prédiction P-2026-07-31-1 (résultats Reddit T3 2026 fin octobre) et P-2026-08-01-3 (métriques OpenAI Business Agent Campaign publiques) restent les principaux jalons associés.

---

Draft SyntheticBrain. Rien n'a été envoyé.
