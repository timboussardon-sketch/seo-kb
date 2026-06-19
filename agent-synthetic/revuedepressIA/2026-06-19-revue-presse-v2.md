# Algorithme — édition du 19 juin 2026 (v2)

*Pilier info du jour : Actualité SEO.*

## Résumé en 4 points

- La CMA britannique a publié le 17 juin 2026 deux nouvelles obligations contraignantes contre Google : classement organique objectif et non discriminatoire (AI Overviews compris) avec préavis sur les changements significatifs, et portabilité des données de recherche vers des tiers autorisés. Délais : 6 mois pour la première, 3 mois pour la seconde.
- USA Today publie cinq fiches pré-écrites par jour pour la Coupe du monde 2026, assemblées à l'aide d'une IA qui pioche dans les archives, afin de publier avant la génération des AI Overviews. Le jour d'ouverture du tournoi (11 juin), USA Today Sports a totalisé 2 millions de pages vues.
- Une analyse SISTRIX de 3,8 millions de réponses ChatGPT en allemand mesure un déplacement de 47 % des citations en 48 heures lors du passage à GPT-5.5 (22-23 mai 2026), au profit des éditeurs allemands (FAZ +124 %, Welt +99 %) et au détriment des agrégateurs internationaux (Tripadvisor −53 %, Expedia et Rome2rio −60 %).
- Google a lancé le 18 juin la bêta de « Ask Ad Manager », un assistant Gemini intégré à Google Ad Manager pour les éditeurs, avec API REST et serveur MCP annoncés plus tard en 2026. Yahoo est cité comme premier partenaire intégrateur.

---

## Info du jour — La CMA britannique impose à Google six mois pour un classement organique objectif (AI Overviews compris) et trois mois pour la portabilité des données de recherche

La Competition and Markets Authority du Royaume-Uni a publié le 17 juin 2026 deux nouvelles obligations contraignantes (« conduct requirements ») contre Google Search au titre du régime britannique de marchés numériques ([communiqué officiel CMA / GOV.UK](https://www.gov.uk/government/news/further-cma-action-to-secure-a-fairer-deal-for-businesses-and-improve-google-search-services-in-uk), [Search Engine Land](https://searchengineland.com/uk-cma-orders-google-to-explain-how-search-results-are-ranked-480520), [Search Engine Journal](https://www.searchenginejournal.com/google-must-give-notice-before-significant-ranking-changes/579696/)).

Première obligation, fair ranking. Google doit classer les résultats organiques sur des critères « objectifs et non discriminatoires », mettre en place un préavis sur les changements significatifs de classement, et ouvrir un processus formel par lequel les entreprises britanniques peuvent contester une décision de classement. Le périmètre couvre les résultats organiques **y compris les AI Overviews**, et exclut explicitement les résultats sponsorisés. Délai d'implémentation : 6 mois ([SE Roundtable Schwartz](https://www.seroundtable.com/cma-google-search-results-ranked-data-portability-41525.html), [Telecompaper](https://www.telecompaper.com/news/cma-imposes-new-fair-ranking-data-portability-requirements-on-google-search--1574536)).

Deuxième obligation, data portability. Les utilisateurs de Google Search au Royaume-Uni doivent pouvoir transférer leurs données de recherche vers des tiers autorisés (plateformes de récompenses, comparateurs, fournisseurs d'offres personnalisées). Délai d'implémentation : 3 mois.

Will Hayter, Executive Director Digital Markets de la CMA, cité dans le communiqué officiel : « Search is a vital gateway for businesses in the UK to reach customers, and clearer, predictable and more transparent ranking systems could give them greater scope to expand and invest. »

Réponse Google reprise par Search Engine Journal : les systèmes de classement de Google « are fair, transparent and show the most relevant, highest quality results ». Aucune réponse plus détaillée n'a été publiée par Google le jour de l'annonce.

Lecture. Trois éléments à tenir séparés.

Premier, le préavis sur les changements significatifs de classement est l'élément le plus directement opérationnel pour le SEO. La CMA ne précise pas dans son ordonnance ce qui constitue un changement « significatif », ni la durée minimale du préavis ; cette précision arrivera dans la mise en œuvre. Si elle est tenue, c'est la première fois qu'un régulateur national impose à Google un mécanisme de notification ex-ante sur les core updates pour les entreprises d'un marché donné. La portée géographique reste UK seulement, mais la concurrence DMA européenne et CMA britannique sur le même périmètre rend probable une extension par alignement réglementaire.

Deuxième, le périmètre AI Overviews compris est explicite. L'ordonnance distingue les résultats organiques (avec AI Overviews) des résultats sponsorisés, et applique la même obligation d'objectivité aux deux. Côté SEO, cela signifie que la décision algorithmique de citer un site dans un AI Overview doit reposer sur des critères « objectifs et non discriminatoires », opposables, et que les entreprises britanniques pourront contester l'absence de citation par la voie d'un processus formel à créer. Côté Google, l'exposition d'un raisonnement d'AI Overview à un mécanisme de contestation pose une difficulté technique nouvelle, puisqu'un AI Overview n'est pas une page de résultats stable mais une réponse générative recomposée par requête.

Troisième, la portabilité des données de recherche déplace la dépendance utilisateur vers la plateforme. Aujourd'hui, l'historique de recherche d'un utilisateur Google n'est exploitable que dans l'écosystème Google. Avec la nouvelle obligation, un utilisateur britannique pourra l'exporter vers un agrégateur, un comparateur ou une plateforme de récompenses. Trois mois pour implémenter, c'est court. Si Google joue la lettre minimale, l'export prendra la forme d'un fichier brut peu exploitable ; si la CMA exige une portabilité utilisable, on entre dans une logique de marché secondaire sur la donnée de recherche.

Doctrine. Pas de lien wiki direct sur l'obligation de fair ranking côté régulation, ce qui est attendu pour un fait procédural. La fiche [[concepts/agentic-search]] est touchée indirectement par le périmètre AI Overviews : un AI Overview est une réponse générative, un mécanisme de contestation suppose une trace explicable des sources sélectionnées, et la fiche [[concepts/metriques-visibilite-geo]] gagne ici une dimension régulatoire (la décision de citer ou non devient potentiellement contestable, ce qui change l'enjeu de la métrique de citation). À surveiller pour mise à jour des deux fiches après publication de la mise en œuvre côté Google.

Limites. Premier, l'ordonnance est britannique. Le périmètre couvre Google Search au Royaume-Uni. Pas d'extension automatique au DMA européen ni aux États-Unis, même si l'alignement est probable. Deuxième, Google a six mois pour le fair ranking et trois mois pour la portabilité, donc rien d'effectif avant le 17 septembre 2026 pour la portabilité et le 17 décembre 2026 pour le classement. Troisième, aucune sanction financière n'est attachée à l'ordonnance dans le texte public consulté ; la CMA dispose en théorie d'un pouvoir de sanction au titre du Digital Markets, Competition and Consumers Act 2024, mais l'amende n'est pas chiffrée à ce stade. Quatrième, Google peut contester l'ordonnance devant le Competition Appeal Tribunal britannique, ce qui peut décaler la mise en œuvre.

Prédiction. La CMA publiera avant le 31 mars 2027 une définition opérationnelle de « changement significatif de classement », précisant un seuil de variation de visibilité agrégée (par exemple : variation supérieure à X % sur Y % des requêtes mesurées) qui déclenche l'obligation de préavis aux entreprises britanniques.

---

## Brèves

### B1 — USA Today publie cinq fiches pré-écrites par jour pour la Coupe du monde 2026, afin de devancer la génération des AI Overviews (Actualité SEO)

USA Today utilise un système de fiches pré-écrites automatisées (« automated shell files ») assemblées par une IA qui pioche dans les archives du groupe (sous-titres, photos, liens) pour les événements de l'actualité chaude. Les éditeurs valident, les journalistes ajoutent l'information du moment, et la publication intervient en quelques minutes. La stratégie cible explicitement la fenêtre courte avant la génération d'un AI Overview par Google sur la requête correspondante ([Digiday, Sara Guaglione, 18 juin 2026](https://digiday.com/media/how-usa-today-co-is-trying-to-beat-ai-overviews-on-world-cup-news/), [Search Engine Land, Danny Goodwin, 18 juin 2026](https://searchengineland.com/usa-today-google-ai-overviews-world-cup-480603), [Nieman Lab](https://www.niemanlab.org/reading/how-usa-today-co-is-trying-to-beat-ai-overviews-on-world-cup-news/)).

Chiffres documentés par le groupe USA Today : cinq fiches préparées par jour pendant la Coupe du monde 2026, 2 millions de pages vues sur USA Today Sports le 11 juin (jour d'ouverture), 116 millions de pages vues sur l'ensemble du réseau pendant la couverture des Jeux d'hiver 2026 (1er janvier au 28 février), 91 millions sur le site flagship soit 82 % de plus que la couverture des Jeux d'hiver 2022, 40 millions de visiteurs uniques mensuels sur la verticale sport, 200+ publications locales dans le réseau, 16 reporters déployés dans les villes hôtes.

Alicia DelGallo, directrice éditoriale Sports de USA Today, citée par Digiday : « We're trying not to be as reliant on SEO strategy. Pre-writes are huge… We do brainstorm sessions on anticipatory content, and try to pre-write as much as we can, and then time it for as soon as something happens. »

Élément de contexte cité par Barry Adams (Polemic Digital) dans la couverture Search Engine Land : un AI Overview apparaît sur une requête d'actualité environ quatre heures après l'événement. La fenêtre opérationnelle d'un éditeur d'actualité pour précéder l'AI Overview tient donc en quelques heures, pas en quelques jours.

Lecture. Trois implications opérationnelles.

Premier, le déplacement de l'objet à optimiser est explicite. La directrice éditoriale formule en clair la sortie de la logique SEO classique (« trying not to be as reliant on SEO strategy »). Ce n'est pas une déclaration de rupture, c'est la reconnaissance d'un nouvel objet à viser : la fenêtre temporelle de quatre heures avant la génération de l'AI Overview, période pendant laquelle la requête « match score X-Y » est encore une requête de recherche classique répondue par une page web indexée et non par une réponse générative. La fiche [[concepts/answer-first-pattern]] (réponse directe dans les 2-3 premières phrases) est mobilisée par ce dispositif, mais avec une dimension temporelle ajoutée : la réponse directe doit aussi être la plus précoce dans l'index.

Deuxième, la production assistée par IA pour publier avant l'IA. Le groupe USA Today utilise une IA pour pré-positionner des structures éditoriales que des journalistes humains complètent au moment de l'événement. C'est une réponse à la compression d'information par AI Overviews via la pré-compression d'information par fiches d'archives. La signature humaine au moment de l'événement reste critique pour la qualité, mais l'industrialisation du pré-positionnement passe par l'IA. À noter : 2 millions de pages vues en une journée sur un événement préparé montre que la mécanique fonctionne sur du trafic mesurable, pas sur une hypothèse.

Troisième, la métrique business est explicite et publique. USA Today documente 116 millions de pages vues sur les Jeux d'hiver 2026 et 91 millions sur le flagship, avec 82 % de progression par rapport à 2022. C'est un cas de réussite documentée de stratégie publisher anti-AI Overviews, à comparer aux pertes documentées sur d'autres verticales éditoriales (overfishing.org, All About Berlin couvertes le 14 juin 2026).

Limites. Premier, la mécanique ne fonctionne que sur des événements anticipables (Coupe du monde, Olympics, élections, sorties produit programmées). Elle ne couvre pas l'actualité totalement imprévue. Deuxième, l'optimisation pour la fenêtre pré-AIO suppose que cette fenêtre reste de l'ordre de quelques heures ; si Google ramène la génération à quelques minutes, la mécanique s'effondre. Troisième, USA Today publie des chiffres agrégés (page views, visitors), pas la décomposition entre trafic Search, trafic Discover, trafic réseaux sociaux, ce qui rend l'attribution exacte au dispositif anti-AIO impossible. Quatrième, la stratégie est applicable à un éditeur d'actualité avec archives profondes ; elle n'est pas transposable telle quelle à une marque sans capital éditorial.

### B2 — SISTRIX mesure un déplacement de 47 % des citations ChatGPT en 48 heures lors du passage à GPT-5.5 sur les requêtes allemandes (GEO)

Johannes Beus, fondateur de SISTRIX, a publié le 2 juin 2026 une analyse mesurant l'effet du passage de GPT-5 mini à GPT-5.5 (22-23 mai 2026) sur les citations de ChatGPT en réponse aux requêtes en allemand. Méthodologie : 38 échantillons quotidiens de 100 000 réponses ChatGPT, soit 3,8 millions de réponses analysées, comparaison des quatre jours qui précèdent et des quatre jours qui suivent le changement de modèle ([SISTRIX, blog Beus](https://www.sistrix.com/blog/chatgpt-core-update/), [Search Engine Journal, Matt G. Southern, 2 juin 2026](https://www.searchenginejournal.com/chatgpt-citations-changed-after-gpt-5-5-sistrix-data-shows/577694/), [PPC Land](https://ppc.land/sistrix-may-2026-mcp-for-all-core-update-patterns-and-chatgpt-shifts/)).

Chiffre principal : 47 % des citations vont à des domaines différents après le changement de modèle. Avant l'événement, la variation quotidienne typique des citations était de 1 à 2 %. Au moment du passage, elle est passée à 47 % en 48 heures.

Gagnants documentés en allemand. Reddit : +7 007 citations pour 10 000 réponses (+59 %). Éditeurs allemands : Welt.de +99 %, FAZ.net +124 %, Bild.de +83 %. Plateformes spécialisées : Mapbox et OpenStreetMap +83 % chacune, JustWatch +624 %, DAZN +383 %, Sky.de +157 %, Kicker.de +357 %. Perdants documentés. Agrégateurs internationaux : Indeed −47 %, Tripadvisor −53 %, Expedia et Rome2rio −60 %. Plateformes globales : YouTube −18 %, Wikipedia −14 %, Google.com −22 %.

Interprétation de SISTRIX reprise dans Search Engine Journal : GPT-5.5 cite plus fréquemment des sources originellement allemandes sur les requêtes allemandes. Les médias et marques de service allemands gagnent, les agrégateurs internationaux perdent. Mécaniquement, le modèle paraît avoir resserré son ancrage de langue (langue de la requête vers langue de la source) là où GPT-5 mini agrégeait plus largement.

Lecture. Trois points.

Premier, l'instabilité temporelle des citations IA est confirmée à grande échelle. Une mesure SparkToro publiée en 2025 et reprise par Profound (40 à 60 % de variation mensuelle) suggérait l'ordre de grandeur ; le travail de Beus le mesure sur 3,8 millions de réponses et le rattache à un événement identifiable (changement de modèle). La fiche [[concepts/metriques-visibilite-geo]] gagne une dimension d'attribution causale : le déplacement de citations n'est plus seulement aléatoire, il peut être daté et rapporté à une mise à jour de modèle. C'est une avancée méthodologique.

Deuxième, l'effet de localisation est documenté en allemand mais probablement non spécifique. Si la même mécanique opère en français, en italien, en espagnol, l'enjeu pour les marques internationales est de mesurer leur exposition au déplacement de modèle par langue, pas globalement. Pour une marque dont la stratégie de présence ChatGPT reposait sur une page anglophone classée en autorité de domaine, le passage à GPT-5.5 a pu faire effondrer la part de citation sur les marchés locaux non anglophones, sans alerte préalable.

Troisième, l'agrégateur perd, le primaire local gagne. Le motif (Indeed −47 %, Tripadvisor −53 %, Expedia et Rome2rio −60 % côté agrégateurs ; Welt, FAZ, Bild côté éditeurs allemands) recoupe la lecture de Aleyda Solis sur le core update Google de mai 2026 (« intent-destination reset » couvert le 14 juin 2026), où les destinations canoniques locales gagnaient au détriment des agrégateurs. Deux systèmes très différents (Google ranking + ChatGPT citation) convergent ce semestre sur la même direction : la source primaire la plus proche du marché de la requête est valorisée par rapport à la couche d'agrégation. C'est un motif structurel, pas un accident.

Limites. Premier, la mesure est en allemand. Pas de mesure équivalente publiée à ce jour en français, en anglais britannique ou en espagnol. Deuxième, la mesure isole un changement de modèle (mai 2026), pas un effet long terme : sur 30 ou 60 jours, la distribution peut se restabiliser ou continuer à dériver. Troisième, SISTRIX est un éditeur outil (vendeur), à traiter avec la réserve méthodologique habituelle même si la méthode est explicite et le dataset large.

### B3 — Google lance Ask Ad Manager, assistant Gemini intégré à Google Ad Manager, en bêta pour les éditeurs (Actualité SEO)

Google a annoncé le 18 juin 2026 le lancement en bêta de « Ask Ad Manager », un assistant conversationnel intégré à Google Ad Manager, propulsé par Gemini, destiné aux éditeurs qui monétisent leur inventaire publicitaire via la régie de Google ([annonce officielle Google, Peentoo Patel, Senior Product Management Director](https://blog.google/products/admanager/ask-ad-manager/), [Search Engine Land](https://searchengineland.com/google-launches-ai-agent-for-ad-manager-480613), [Adweek](https://www.adweek.com/media/google-ai-agent-ads-analytics-advisor/)).

Trois capacités décrites par Google. Diagnostiquer en temps réel un problème de monétisation (line item bloqué, erreur de targeting) sans quitter l'interface. Générer des rapports personnalisés et des métriques sur demande à partir d'une question en langage naturel. Faciliter la navigation dans la plateforme par liens contextuels et filtres pré-chargés.

Partenaire d'intégration cité par Google : Yahoo. « Yahoo is already integrating Ad Manager into custom agents to streamline their ad operations, from forecasting and line item creation to reporting and campaign optimization. » Annoncés pour plus tard en 2026 : une API REST et un serveur MCP pour intégrer Ad Manager dans des workflows agents externes.

Lecture. Trois implications.

Premier, c'est une extension du pattern Ask Advisor (lancé en avril 2026 sur Ads, Analytics et Merchant Center) au stack publisher. Côté éditeur, l'interaction avec Google Ad Manager passe progressivement de l'interface graphique au prompt conversationnel. C'est cohérent avec les annonces antérieures Gemini × Business Profile (12 juin 2026) et Ask Advisor (avril 2026) : Google industrialise la couche conversationnelle sur toutes les interfaces business.

Deuxième, le serveur MCP annoncé en fin d'année est l'élément structurant pour 2027. Une fois le serveur MCP disponible, n'importe quel agent externe (Claude, ChatGPT, agent maison) peut interroger Ad Manager via le protocole standard. Combiné aux annonces Tableau MCP de Salesforce (15 juin 2026) et au cadre Open Knowledge Format de Google Cloud (12 juin 2026), c'est un troisième pivot enterprise vers une couche d'intégration MCP unifiée côté business analytics et adtech.

Troisième, l'interlocuteur reste la régie. La nouveauté est conversationnelle, pas structurelle : Ask Ad Manager ne modifie pas la mécanique d'enchère, le profil utilisateur, ni la politique éditoriale de Google. Pour un éditeur, l'enjeu est l'efficacité opérationnelle (moins de temps en reporting et debugging), pas une nouvelle source de revenu.

Limites. Premier, la bêta démarre en juin 2026 sans périmètre géographique précisé dans la communication officielle. Pas d'information sur les marchés à la sortie de bêta. Deuxième, l'intégration via API REST et MCP est annoncée « plus tard en 2026 », sans date précise ; jusqu'à la disponibilité du MCP, l'usage reste enfermé dans l'interface Google. Troisième, aucun éditeur indépendant n'est cité comme intégrateur en dehors de Yahoo, dont la dépendance commerciale à Google sur la stack publicitaire est un cas particulier. La preuve d'adoption en dehors de partenaires intégrés reste à venir.

---

## Méthode et incertitudes

Édition produite en mode cloud, sans accès local au binaire `./kb` ni à `youtube-claude-seo`. Recoupement réalisé sur sources web uniquement.

Info du jour CMA : 5 sources indépendantes ont confirmé les éléments factuels (GOV.UK primaire, Search Engine Land Schwartz, Search Engine Journal Southern, Search Engine Roundtable Schwartz, Telecompaper). Citation Will Hayter confirmée sur deux sources (GOV.UK + reprises). Aucune sanction financière chiffrée à ce stade. Pilier varié vs édition matinale (Recherche agentique → Actualité SEO).

B1 USA Today : 3 sources indépendantes (Digiday scoop primaire par Sara Guaglione, Search Engine Land reprise Goodwin, Nieman Lab reprise). Quotes Alicia DelGallo verbatim confirmées sur Digiday + Search Engine Land. Chiffres 116M / 91M / 2M page views attribués à USA Today Co. (vendeur, à lire comme tel).

B2 SISTRIX GPT-5.5 : 3 sources (SISTRIX primaire Beus, Search Engine Journal Southern, PPC Land Rijo). Méthodologie explicite (3,8M réponses, 38 échantillons quotidiens, 4 jours avant/après). La publication date du 2 juin 2026 (15 jours), couverte ici car la mesure n'avait pas été traitée dans `said_index`. SISTRIX est éditeur outil, à traiter comme tel.

B3 Ask Ad Manager : 3 sources (Google blog primaire, Search Engine Land, Adweek). Partenaire d'intégration unique nommé (Yahoo) à cette date.

Anti-pattern IA. Run propre sur le plan de la voix. Zéro métaphore vérifiée (pas de bataille, vague, rails, moteur figuré, fusée, ouvrir la voie, passer à la caisse, écosystème imagé). Tentations identifiées et écartées : « la régulation prend le contrôle » (rejeté pour info du jour, personnification), « USA Today contre Google » (rejeté pour B1, militarisme implicite), « Google industrialise sa couche conversationnelle » (gardé car descriptif littéral de la stratégie produit). « Couche » employé trois fois (vocabulaire informatique standard, à surveiller la fréquence). Aucune personnification de Google, CMA, USA Today, SISTRIX, ChatGPT, Yahoo. Aucun tiret cadratim hors structurels markdown ---. Vouvoiement maintenu. Citations Hayter, DelGallo, Google et Yahoo signalées comme verbatim.

Prochaines fenêtres à surveiller. (1) Réponse écrite formelle de Google à la CMA dans les jours qui viennent (recours, contestation, calendrier de mise en œuvre). (2) Première réaction d'autres autorités européennes (CNIL, BAFin, AGCOM) ou de la Commission européenne (DMA). (3) Mesure indépendante du déplacement de citations ChatGPT en français ou en espagnol équivalente à SISTRIX en allemand. (4) Réplique éditeur du dispositif USA Today shell files par un autre groupe (Reuters, AP, Le Monde, Le Figaro).
