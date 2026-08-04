# Algorithme — édition du 4 août 2026

*Pilier info du jour : Actualité SEO*
*Pilier brèves : Actualité SEO*

**Résumé**

- Microsoft publie le 3 août la troisième mise à jour en 25 jours de la brique AI Citations de Clarity, avec cette fois la séparation des requêtes marque et hors marque, sur un produit qui reste gratuit face à des outils GEO facturés jusqu'à plusieurs centaines de dollars par mois.
- La séquence complète est datée : Topic Insights le 9 juillet, Query Topics en bêta le 22 juillet, Branded Query Segmentation en disponibilité générale le 3 août. Cadence rapide sur un seul module.
- Microsoft retire les API SOAP/POX de Bing Webmaster Tools au 31 août 2026, avec migration vers la version JSON/HTTP à fonctionnalités et clé identiques.
- Google Trends passe de 125 termes en 5 groupes de 25 à 400 termes en 8 groupes de 50, un plafond multiplié par 3,2 pour la comparaison de mots-clés.
- Google teste dans Search une demande de connexion au compte pour continuer à voir les résultats au-delà des premières pages, en remplacement du captcha, observée dans Chrome en navigation privée.

---

## Info du jour — Actualité SEO : Microsoft Clarity accélère sur la mesure d'AI search et la maintient gratuite

Microsoft a publié le 3 août 2026 la troisième mise à jour en 25 jours du module AI Citations de sa plateforme d'analyse Clarity. La nouveauté du 3 août sépare les requêtes qui contiennent une marque des requêtes génériques, à la fois dans la carte des requêtes et dans la mesure de Share of Authority ([Search Engine Land, 3 août 2026, Barry Schwartz](https://searchengineland.com/microsoft-clarity-adds-branded-and-non-branded-ai-queries-484185), [PPC Land, 3 août 2026, Luis Rijo](https://ppc.land/microsoft-clarity-splits-ai-citations-by-brand-in-3rd-release-in-25-days/)). Le module lui-même reste gratuit pour tous les comptes Clarity.

La chronologie tient sur trois dates publiques, toutes documentées par le blog produit et repris par la presse spécialisée. Le 9 juillet 2026, Microsoft rend disponible Topic Insights, signé Ihab Rizk sur le blog Clarity, un outil qui compare la présence d'un domaine dans les réponses génératives sur des sujets définis par l'utilisateur ([annonce Microsoft, 9 juillet 2026](https://clarity.microsoft.com/blog/topic-insights-announcement/), [PPC Land, 11 juillet 2026](https://ppc.land/microsoft-clarity-gives-away-ai-visibility-tool-rivals-charge-for/)). Le 22 juillet 2026, Query Topics entre en bêta, avec une fonction qui regroupe automatiquement les requêtes de citation en thèmes chiffrés, avec un compteur de citations et un pourcentage de Share of Authority par thème ([PPC Land, 22 juillet 2026](https://ppc.land/microsoft-clarity-beta-cuts-ai-citation-query-sorting-into-ranked-topics/)). Le 3 août 2026 arrive la segmentation par requête de marque, en disponibilité générale. Trois libérations distinctes sur un même chantier, avec deux passages en disponibilité générale et une bêta, en un peu plus de trois semaines.

Le tableau de démonstration publié par Microsoft, repris par PPC Land le 3 août, illustre la mécanique sur un cas d'équipement de ski.

| Requête | Type | Citations | Share of Authority |
| --- | --- | --- | --- |
| best all-mountain skis | non-marque | 2 500 | 20,3 % |
| alpine beginner ski boots | marque | 1 900 | 24,2 % |
| alpine ski insulated snow pants | marque | 1 600 | 22,3 % |
| top snowboard brands | non-marque | 1 100 | 18,6 % |
| waterproof ski jackets | non-marque | 986 | 15,9 % |

Sur cet exemple, les requêtes marquées comme brandées atteignent 24,2 % et 22,3 % de Share of Authority, contre 20,3 %, 18,6 % et 15,9 % pour les non-marquées. La séparation permet de lire deux régimes distincts sur la même page de rapport, sans faire tourner un export ni maintenir un tag externe. C'est ce que PPC Land nomme la question laissée ouverte par les deux releases précédentes : les citations mesurées répondent-elles à une demande de marque déjà installée, ou signalent-elles une découverte nouvelle par un utilisateur qui ne connaissait pas le domaine.

Le contexte concurrentiel de Clarity a été formulé par Microsoft dans l'annonce Topic Insights, reprise le 11 juillet par PPC Land. La plupart des produits de mesure GEO du marché, dont plusieurs cités par la presse spécialisée depuis un an (Profound, Otterly.AI, Scrunch AI, Peec AI, plus Adobe, Amplitude, Semrush et Ahrefs sur leurs modules dédiés), positionnent l'analyse de citations et la comparaison concurrentielle comme des fonctions payantes. Clarity conserve ces trois modules dans le socle gratuit. La cadence de trois releases en 25 jours et la gratuité du socle constituent le fait franchement neuf : la mesure GEO côté citations passe d'un marché de niche à un outil livré par défaut avec la plateforme d'analyse comportementale que Microsoft distribue depuis 2020.

Deux qualifications restent nécessaires. Premièrement, la brique bêta du 22 juillet n'a pas encore de date de disponibilité générale annoncée. Deuxièmement, Clarity mesure les requêtes qui déclenchent une citation vers des sources tierces dans les réponses génératives ; elle ne mesure pas directement le trafic de renvoi, ni la conversion en aval, ni l'attribution sur un CRM. Les caveats posés par les études empiriques récentes tiennent : le trafic de renvoi depuis les réponses génératives reste faible en volume ([Orbit Media, 22 juillet 2026, 0,5 % du trafic sur 97 sites B2B](https://www.orbitmedia.com/blog/conversion-rates-ai-search/)), l'essentiel du poids de citation vient de sources tierces ([Aleyda Solis, 2 août 2026, 84 à 93 % sur SaaS](https://www.optimixed.com/ai-search-is-a-3rd-party-citation-problem-with-an-on-page-corroboration-base-the-data-across-saas-ecommerce-and-finance-international-seo-consultant-author-speaker-aleyda-solis/)), et la conversion utile passe par le rattachement de la citation à un money-query set ([Kevin Lee, Search Engine Land, 3 août 2026](https://searchengineland.com/geo-hit-revenue-targets-484144)).

L'implication opérationnelle pour un consultant qui audite un module de mesure GEO est double. Un, la question de savoir si l'on paie pour une mesure de citations doit maintenant se poser en distinguant deux cas d'usage : la mesure de présence à l'échelle du domaine (couverte par Clarity dans le socle gratuit à condition d'installer le tag), et la mesure de portefeuille sur des requêtes de recommandation reliées à un CRM (couverte par des outils spécialisés dont la logique de money-query set formulée par Kevin Lee est un cadre récent). Ces deux cas d'usage ne se recouvrent pas, et Clarity ne remplace pas les deuxièmes. Deux, la séparation branded/non-branded introduite le 3 août rend enfin lisible sur une même vue une distinction qui compte pour arbitrer un budget : la mention dans une réponse générative qui reprend une marque déjà cherchée renseigne sur la solidité d'un nom acquis, la mention sur une requête non brandée renseigne sur la capacité du contenu à être choisi en dehors de la reconnaissance de marque. La confusion des deux fabrique des tableaux de bord dont la lecture surestime la découverte.

Cette séquence de trois releases s'insère dans un mouvement de commodification côté mesure GEO, sans encore rien changer aux mécanismes qui font qu'un contenu est cité. La citation reste construite en amont, sur l'écosystème de sources tierces et la corroboration on-page, dimensions déjà formalisées dans le vault ([[concepts/metriques-visibilite-geo]], [[concepts/tabou-visibilite]]). Nous ajoutons une prédiction datée : un des produits payants de mesure GEO nommés dans la presse spécialisée (Profound, Otterly.AI, Scrunch AI, Peec AI) publiera avant le 31 décembre 2026 une baisse de prix ou l'ajout d'un palier gratuit pour la mesure de citations, en réaction à la trajectoire de Clarity.

---

## Brèves

### Actualité SEO — Bing Webmaster Tools retire ses API SOAP/POX le 31 août 2026

Microsoft retirera les API SOAP/POX de Bing Webmaster Tools le 31 août 2026, avec une migration recommandée vers la version JSON/HTTP (REST), synthèse publiée par Barry Schwartz le 3 août ([Search Engine Roundtable, 3 août 2026, Barry Schwartz, repris sur optimixed](https://www.optimixed.com/bing-webmaster-tools-soap-pox-apis-retires-august-31-2026/), [recap 3 août 2026](https://www.optimixed.com/daily-search-forum-recap-august-3-2026/)). Après cette date, les requêtes envoyées sur les anciens endpoints ne seront plus servies. Le fait annexe utile : la migration ne demande pas de re-génération de clé API, ne change pas les fonctionnalités disponibles, et conserve les quotas et permissions. La consigne s'adresse aux comptes qui utilisent encore la version historique de l'API, sans impact pour ceux qui interagissent uniquement via l'interface web ou déjà via REST. Un consultant SEO qui maintient un connecteur maison ou un plugin tiers appuyé sur SOAP/POX doit vérifier l'état du connecteur d'ici la fin du mois, sans quoi l'export automatisé s'arrêtera silencieusement au 1er septembre. Sujet mécanique, pas d'inflexion doctrinale.

### Actualité SEO — Google Trends passe de 125 à 400 termes comparables par requête

Google a élargi la limite de comparaison de termes dans Google Trends de 125 termes en 5 groupes de 25 à 400 termes en 8 groupes de 50, mesure documentée le 3 août par Barry Schwartz ([Search Engine Roundtable, 3 août 2026, repris sur optimixed](https://www.optimixed.com/google-trends-lets-you-compare-more-search-terms/)). Le plafond total est multiplié par 3,2, le nombre de groupes par 1,6, et la taille d'un groupe individuel par 2. La mise à jour concerne l'explorateur, l'interface classique n'a pas été mise à jour à la date de l'annonce. Utilité pour un consultant qui construit un dossier d'intentions par grappe : il devient possible de tenir un cluster de 50 requêtes reliées à un même produit dans une seule vue, sans découper artificiellement en plusieurs export. Rappel du contexte : Google Trends reste une mesure d'intérêt relatif, pas de volume absolu, et les termes à trop faible fréquence n'apparaissent pas dans l'échantillon. La bascule dépend d'un déploiement progressif côté interface utilisateur.

### Actualité SEO — Google teste une demande de connexion pour continuer à voir les résultats de Search

Google Search a été observé le 3 août en train de demander à un utilisateur de se connecter à son compte pour continuer à voir les résultats au-delà des premières pages, en remplacement du captcha classique ([Search Engine Roundtable, 3 août 2026, repris sur optimixed](https://www.optimixed.com/google-search-testing-sign-in-to-verify-searches-are-human/)). Le test a été observé par Kamlesh Shukla dans Chrome en navigation privée, après plusieurs pages consultées. L'article précise que le test n'a pas été reproduit largement, ce qui suggère un déploiement limité ou conditionné à des paramètres précis. Aucun communiqué officiel de Google n'accompagne l'observation. Ce que ce test change potentiellement : le mécanisme historique de vérification anti-bot passait par un captcha jouable sans compte, la bascule vers une demande de connexion transfère la vérification sur l'identifiant Google. Deux angles à surveiller sur les prochaines semaines. Un, l'effet sur les outils SEO qui interrogent Search sans authentification (scraping, trackers de position) ; s'il se généralise au-delà des 3 à 5 premières pages, il ajoute une friction pour les échantillons à profondeur élevée. Deux, l'effet sur la mesure de trafic organique déconnecté, qui devient marginal dans le total mais reste un signal utile pour les vérifications ponctuelles hors compte. Test isolé à ce stade, pas encore un fait à intégrer dans une méthodologie ; à re-tester quand une confirmation Google sort ou quand une reproduction large est publiée.

---

*Draft SyntheticBrain. Rien n'a été envoyé.*
