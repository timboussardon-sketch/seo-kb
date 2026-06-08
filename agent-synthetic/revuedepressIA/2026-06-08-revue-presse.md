# Algorithme — édition du 8 juin 2026

## Résumé en 5 points

- CNN a déposé une plainte fédérale contre Perplexity le 28 mai 2026 au tribunal de district de New York Sud, sur trois chefs cumulés (copyright, marque, publicité mensongère) plutôt que sur le seul copyright.
- L'allégation centrale de publicité mensongère vise l'abonnement Comet Plus : Perplexity y aurait présenté CNN comme source incluse alors qu'aucun accord n'existait.
- Le core update Google de mai 2026 s'est achevé le 2 juin après 11 jours et 21 heures, l'analyse d'Aleyda Solis sur les données SISTRIX US et UK décrit un pattern de réalignement de la visibilité par type de destination plus que par autorité de domaine.
- Étude Ahrefs publiée en juin 2026 sur 3 millions de requêtes US des AI Overviews : YouTube 20,9 % de part de citations, Reddit 19,6 %, Facebook 11,6 %, Google.com 6 % ; à comparer aux 17,42 % de Google.com sur AI Mode mesurés par SE Ranking en mars 2026.
- Un drapeau du navigateur Chrome Canary, découvert le 5 juin 2026, redirigeait les requêtes de la barre d'adresse vers AI Mode ; Google a déclaré que c'était une erreur et qu'il ne prévoit pas de basculer le défaut.

---

## Info du jour — CNN poursuit Perplexity sur copyright et publicité mensongère, et vise précisément l'abonnement Comet Plus

**Pilier : Actualité SEO (conflit éditeurs vs moteurs IA).**

Le 28 mai 2026, CNN a déposé un complaint de 54 pages contre Perplexity AI devant le tribunal de district des États-Unis pour le district sud de New York (dossier 1:26-cv-04427). L'action est la première engagée par une chaîne de télévision américaine contre un moteur de recherche IA. Sources : [Variety](https://variety.com/2026/biz/news/cnn-sues-perplexity-alleging-copyright-infringement-1236760987/), [NPR](https://www.npr.org/2026/05/28/g-s1-124680/cnn-sues-ai-company-perplexity-alleging-it-violates-copyright-protections), [Al Jazeera](https://www.aljazeera.com/economy/2026/5/28/cnn-sues-perplexity-alleging-unlawful-distribution-of-copyrighted-content), [PPC Land](https://ppc.land/cnn-sues-perplexity-for-copying-17-000-works-in-landmark-ai-copyright-case/).

La plainte porte sur plus de 17 000 articles, photos et vidéos que Perplexity aurait copiés, redistribués et utilisés pour entraîner ou alimenter ses produits, sans licence ni autorisation. Les trois chefs cumulés sont la contrefaçon de droits d'auteur, l'atteinte à la marque CNN et la publicité mensongère. La combinaison des trois est ce qui distingue cette action des autres procédures déjà engagées contre Perplexity (New York Times, Dow Jones, Reddit) et de celle pendante au 9e Circuit avec Amazon.

Le chef de publicité mensongère vise précisément l'abonnement Comet Plus. Selon le complaint, lorsqu'un utilisateur interroge le chatbot Perplexity avec « What is Comet Plus? », il reçoit une réponse présentant CNN comme partenaire du bouquet premium d'actualités, comparé à Apple News Plus. CNN affirme qu'aucun accord de ce type n'a été signé : les négociations entamées en 2025 ont échoué, et CNN a ensuite bloqué le bot de Perplexity. Source primaire : extraits du complaint repris par [Variety](https://variety.com/2026/biz/news/cnn-sues-perplexity-alleging-copyright-infringement-1236760987/) et [PPC Land](https://ppc.land/cnn-sues-perplexity-for-copying-17-000-works-in-landmark-ai-copyright-case/).

La réponse publique de Perplexity, par la voix de son porte-parole Jesse Dwyer, tient en quatre mots : « You can't copyright facts ». Sources : [Variety](https://variety.com/2026/biz/news/cnn-sues-perplexity-alleging-copyright-infringement-1236760987/), [Yahoo Finance / TheWrap](https://www.thewrap.com/industry-news/public-policy-legal/cnn-sues-perplexity-ai-stealing-news-chatbot-copyright/). C'est la défense déjà déployée par Perplexity contre le New York Times et le Tribune Publishing Company. La nouveauté ici est que cette défense ne couvre pas le chef de publicité mensongère : un fait peut être libre, mais déclarer une source comme partenaire d'un abonnement payant alors qu'elle ne l'est pas relève d'une autre catégorie juridique.

Pour un éditeur, deux signaux concrets à retenir.

Premier signal : la plainte ne demande pas seulement des dommages-intérêts non chiffrés, elle demande une injonction. Une décision en ce sens pourrait imposer à Perplexity de purger ses index ou de bloquer la génération de réponses depuis des contenus CNN. Cela rendrait visible, pour la première fois, le coût opérationnel de la rétractation d'une source dans un moteur IA déployé. C'est un précédent à surveiller pour qui mesure la composition des sources des moteurs IA.

Deuxième signal : le chef de publicité mensongère ouvre une voie d'attaque distincte du seul copyright pour les éditeurs qui ont des programmes d'abonnement. Si un moteur IA cite ou présente une source comme incluse dans une offre payante sans accord, l'angle juridique se déplace du « peut-on copier des faits » vers « peut-on vendre l'apparence d'un partenariat ». Cette piste de droit de la consommation et de droit des marques échappe à la défense « facts are free » et n'a presque pas été testée à ce jour.

Lien doctrine. La fiche [[concepts/agentic-search]] note explicitement comme limite que « l'agentic search au sens strict (agent qui agit, pas juste génère une réponse) reste mal couvert empiriquement ». Le procès CNN remplit cette limite par un cas d'usage : un agent (le chatbot Perplexity) qui agit en présentant une offre commerciale (Comet Plus) avec une composition de sources incorrecte. La fiche [[concepts/data-proprietaire]] est l'autre lien direct : CNN avance que sa valeur éditoriale propre justifie le paiement, ce qui formalise l'argument du contenu original comme actif défendable face à la captation par moteur IA. Une fiche dédiée à la composition des sources contestées dans les moteurs IA n'existe pas encore dans la doctrine : à proposer en revue hebdo.

Le calendrier des procédures Perplexity se densifie. Le 11 juin, le 9e Circuit entend Amazon vs Perplexity sur le CFAA à Seattle. La plainte CNN se cumule à celles du New York Times, du Dow Jones et de Reddit. Aucune décision au fond, pour l'instant, dans aucun de ces dossiers. Le délai à 24 mois reste l'horizon attendu pour un précédent jurisprudentiel.

---

## Brèves

### Bilan du core update Google de mai 2026 : le pattern « intent-destination reset » se confirme sur deux séries de mesures

**Pilier : Actualité SEO.**

Le core update de mai 2026 s'est achevé le 2 juin après 11 jours et 21 heures, avec trois pics de volatilité distincts les 23-24 mai, le 30 mai et le 2 juin lui-même. Source : [DigitalApplied recovery playbook](https://www.digitalapplied.com/blog/google-may-2026-core-update-complete-recovery-playbook). Google a recommandé d'attendre une semaine après la fin de déploiement pour des données stables, soit le 9 juin.

Deux analyses indépendantes convergent dès maintenant. Aleyda Solis, publiée le 3 juin sur les données SISTRIX US et UK couvrant la fenêtre 26 mai - 2 juin, décrit un « intent-destination reset » : la visibilité se réaligne sur le type de source qui correspond le mieux à l'intention dominante et au marché de la requête, plus que sur l'autorité brute du domaine. Source : [aleydasolis.com](https://www.aleydasolis.com/en/ai-search/google-may-2026-core-update-analysis-intent-market-fit-and-source-type-drove-the-biggest-visibility-shifts/). Relais et confirmation par Matt G. Southern dans [Search Engine Journal](https://www.searchenginejournal.com/googles-may-core-update-favored-pages-that-match-intent/) le 4 juin 2026.

Les chiffres précis disponibles à ce jour, sur dataset SISTRIX : Amazon.co.uk gagne 21,3 % au Royaume-Uni, Amazon.com perd 54,6 % sur le même marché ; Reddit perd 23,8 % au Royaume-Uni et 13,7 % aux États-Unis ; StackExchange perd 31,8 % au Royaume-Uni et 18,3 % aux États-Unis. Côté gagnants par catégorie : Indeed +26 % au Royaume-Uni, Glassdoor +36,6 % aux États-Unis, Cambridge +40,9 % et Merriam-Webster +33,3 % au Royaume-Uni. Côté perdants : YouGlish -69,6 %, Forvo -68,1 %, HiNative -62,9 % au Royaume-Uni dans les dictionnaires et outils de prononciation.

Le motif consolidé : agrégateurs et marketplaces désalignés du marché local perdent, marques de référence et destinations transactionnelles directes gagnent, forums et Q&A reculent. Les outils tiers de volatilité confirment l'amplitude du mouvement : Semrush a relevé 78/100, SISTRIX 65/100, AccuRanker 72/100. Source : [seo-kreativ.de](https://www.seo-kreativ.de/en/blog/google-may-2026-core-update-started/) qui agrège les relevés.

La prédiction P-2026-06-06-v2-2 (consolidation du motif avec une 2e source de mesure de visibilité) est résolue partiellement par DigitalApplied qui s'appuie sur l'agrégateur cross-tool Wiredboard. La prédiction P-2026-06-01-1 (profil des perdants comme agrégateurs déficients en signaux structurés) reçoit un appui empirique : les perdants sont des agrégateurs hors-marché ou sans format de réponse adapté à l'intention. À confirmer après le 9 juin avec des données stables.

### Étude Ahrefs sur 3 millions de requêtes : YouTube et Reddit captent 40 % des citations dans AI Overviews

**Pilier : GEO (mesure agrégée de la composition des sources).**

Ahrefs a publié en juin 2026, via son outil Brand Radar, le palmarès des 50 sites les plus cités dans Google AI Overviews aux États-Unis, calculé sur plus de 3 millions de requêtes couvrant tous les sujets. Source : [Ahrefs](https://ahrefs.com/blog/most-cited-domains-ai-overviews/). Les chiffres principaux : YouTube 20,9 %, Reddit 19,6 %, Facebook 11,6 %, Google.com 6,0 %, Instagram 5,2 %, Wikipedia 4,8 %, Amazon 4,0 %, Quora 4,0 %, TikTok 3,6 %.

Trois plates-formes sociales captent plus de la moitié des citations totales. Les marques de référence et les marketplaces occupent une part résiduelle. Le 10e domaine cité (Walmart) ne pèse plus que 0,9 %. La distribution est très concentrée en tête, et la queue longue dilue le reste.

Le chiffre à mettre en regard d'une autre mesure : selon une étude SE Ranking publiée en mars 2026 sur 1,3 million de citations AI Mode et 68 313 mots-clés, Google.com pèse 17,42 % des sources citées par AI Mode et apparaît comme premier domaine. Source : [Search Engine Land](https://searchengineland.com/google-ai-mode-citing-google-more-study-471042). L'écart entre 6 % sur AI Overviews et 17,42 % sur AI Mode pour le même domaine Google.com tient à plusieurs facteurs non encore désentrelacés : différence de surface (AI Overviews est intégré aux SERP classiques, AI Mode est conversationnel), méthodologies de mesure distinctes (Brand Radar vs panel SE Ranking), et fenêtres temporelles différentes (juin 2026 vs mars 2026).

Lien doctrine. La fiche [[concepts/metriques-visibilite-geo]] décrit trois métriques au niveau d'une réponse individuelle (Imp_wc, Imp_pos, Subjective Impression) et ne couvre pas la mesure agrégée de la composition des sources entre moteurs. L'étude Ahrefs documente une 4e métrique de fait, la mention share, applicable à l'échelle d'un moteur entier. À intégrer comme proposition d'évolution de la fiche en revue hebdo.

Réserve méthodologique : Ahrefs ne publie pas la composition exacte des 3 millions de requêtes ni leur pondération par catégorie. Sur un panel orienté requêtes informationnelles, les sites UGC sont structurellement avantagés. Une étude SEJ sur 846 000 sessions montre que les utilisateurs lisent plus longtemps les AI Overviews que les SERP classiques, ce qui change la valeur d'une citation en termes d'exposition utile, pas seulement de présence. Source : [Search Engine Journal](https://www.searchenginejournal.com/google-search-sessions-show-how-users-pause-scroll-reconsider-before-clicking/575243/).

### Un drapeau Chrome Canary redirigeait les requêtes vers AI Mode par défaut, Google parle d'erreur

**Pilier : Actualité SEO (trajectoire produit Google sur la frontière Search / AI Mode).**

Le 5 juin 2026, Windows Report a découvert dans Chrome Canary un drapeau intitulé « Fulfill Searchbox Queries in AI Mode » qui redirigeait l'ensemble des requêtes saisies dans la barre d'adresse vers le mode conversationnel AI Mode, plutôt que vers la page de résultats classiques de Google. Sources : [9to5google](https://9to5google.com/2026/06/05/google-tests-sending-users-straight-to-ai-mode-instead-of-search-in-chrome/), [Engadget](https://www.engadget.com/2188080/chrome-canary-reportedly-sending-search-straight-to-ai/), [Android Authority](https://www.androidauthority.com/google-denies-ai-mode-chrome-3675152/).

Le drapeau était présent sur les versions Canary pour Mac, Windows, Linux et ChromeOS, et n'était pas activé par défaut. L'utilisateur devait passer par `chrome://flags` pour le mettre en marche.

Rajan Patel, VP Engineering Search chez Google, a publié sur X dans la journée du 5 juin : « This was an error. We're not planning to make AI Mode the default for Chrome searches ». Source primaire reprise par [9to5google](https://9to5google.com/2026/06/05/google-tests-sending-users-straight-to-ai-mode-instead-of-search-in-chrome/). Le commentaire de code laissé par le développeur précise : « This is just for exploration. There are no current plans to push this live ».

Le fait stricto sensu est mince : un drapeau expérimental rejeté publiquement. L'intérêt est ce qu'il révèle sur le pipeline produit. Un ingénieur a codé l'option, l'a poussée jusqu'au canal de tests publics, et la firme a dû la désamorcer en quelques heures. Cela documente l'existence d'un travail interne sur la bascule AI Mode comme défaut, indépendamment de la décision finale.

Pour la stratégie SEO : l'urgence reste mesurée. Le défaut Search classique tient pour les sessions Chrome standard. Les ratios de trafic mesurés sur AI Mode (1 milliard d'utilisateurs mensuels selon les annonces de Google I/O 2026, à recouper à un horizon plus long) ne sont pas un produit d'une bascule défaut, mais d'adoptions volontaires. Si une bascule défaut Chrome devait advenir un jour, le profil de trafic des sites changerait massivement et brutalement. À surveiller, sans surévaluer le signal isolé.

---

## Notes éditoriales

Trois sources nouvelles ajoutées au registre explore ce run : ppc.land confirme déjà sa qualité sur la couverture juridique IA ; aleydasolis.com (analyse SISTRIX core update) est ajoutée en explore et candidate au passage exploit ; thewrap est ajoutée en explore sur la couverture industrie médias. Sources connues mobilisées : SEJ, SE Land, 9to5google, Engadget, Variety, NPR, Al Jazeera, Ahrefs, DigitalApplied.

Une piste écartée et loggée : la révélation de l'étude SE Ranking sur Google self-citation AI Mode est datée du 6 mars 2026 et reste un cadre de référence, pas un fait neuf ; elle ne sert qu'à mettre en regard l'écart entre AI Mode et AI Overviews.

Doctrine touchée : [[concepts/agentic-search]] (limite empirique sur l'agent qui agit, comblée par le cas Comet Plus), [[concepts/data-proprietaire]] (argument économique de CNN), [[concepts/metriques-visibilite-geo]] (proposition d'évolution avec la mention share agrégée).

Prédictions ouvertes confortées par ce run : P-2026-06-01-1 (profil perdants core update), P-2026-06-06-v2-2 (consolidation bilan). À résoudre formellement après le 9 juin pour la première, dès qu'une 3e mesure indépendante hors SISTRIX/Wiredboard tombe pour la seconde.

Rien n'a été envoyé.
