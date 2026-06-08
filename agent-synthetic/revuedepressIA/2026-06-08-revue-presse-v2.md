# Algorithme — édition du 8 juin 2026 (v2)

## Résumé en 5 points

- Étude Averi publiée le 8 juin 2026 sur 12 mois de Search Console d'un SaaS B2B : 97,7 % des pages mesurées avec au moins 1 000 impressions tombent sous 1 % de CTR, sur un dataset de 12 638 816 impressions et 30 254 clics.
- Les deux pages les plus dégradées du panel sont une page comparative « AirOps alternatives » (0,02 % de CTR) et une page de témoignages clients (0,03 %) : des pages product-marketing typiques, pas des outils interactifs au sens strict.
- L'étude n'invalide pas le filtre 80 % du test de substitution LLM, mais elle précise son périmètre opérationnel : la défense joue sur les pages-fonctionnalité, pas sur les pages-contenu autour du produit.
- L'audience d'appel du 9e Circuit dans Amazon vs Perplexity est confirmée au 11 juin 2026 à Seattle, avec amici déjà déposés par News/Media Alliance, Digital Content Next et ACLU sur la qualification CFAA d'un agent autorisé par l'utilisateur.
- Semrush a lancé le 3 juin 2026 un connecteur MCP dans Perplexity Computer, donnant accès à son inventaire (28,4 milliards de mots-clés, 261 millions de requêtes LLM tracées) depuis l'interface du moteur génératif.

---

## Info du jour — Une étude Averi sur 12 mois de GSC documente la cannibalisation par AI Overviews et pose une question précise à la doctrine Product-Led SEO

**Pilier : Product-Led SEO (mesure de la défensibilité des pages-produit face aux AI Overviews).**

L'éditeur Averi a publié le 8 juin 2026 une étude basée sur 12 mois de Google Search Console de son propre site, du 23 mai 2025 au 22 mai 2026. Source primaire : [Averi, AI Overview cannibalisation, 8 juin 2026](https://www.averi.ai/breakdowns/12-months-of-gsc-data-how-ai-overviews-killed-ctr). L'étude est mono-source primaire et porte sur un seul SaaS B2B ; les chiffres précis qui suivent sont à lire comme une mesure interne, pas comme une valeur de marché.

Le panel : 711 pages avec au moins 1 000 impressions, 12 638 816 impressions cumulées, 30 254 clics, soit 0,24 % de CTR moyen portfolio. Sur ces 711 pages, 695 (97,7 %) terminent l'année avec un CTR inférieur à 1 %. Les impressions ont progressé de 18 984 % en glissement annuel, les clics de 606 % : la visibilité gonfle, la conversion d'impression en clic s'effondre. Deux points d'inflexion documentés : le 7 septembre 2025 (passage sous 1 % de CTR), puis le 17 octobre 2025 (passage sous 0,5 %). À partir de mars 2026, le CTR se stabilise autour de 0,18 %, soit une réduction de plus de 80 % par rapport aux normes pré-AI Overviews.

Le motif macro est corroboré par des sources externes : Seer Interactive a documenté en avril 2026 une chute du CTR moyen pondéré sur 53 marques et 5,47 millions de requêtes, avec un creux à 1,3 % en décembre 2025 puis un rebond à 2,4 % en février 2026, sur les SERP avec AI Overviews. Source : [Search Engine Land, étude Seer recovery AI Overviews](https://searchengineland.com/google-ai-overviews-ctr-recovery-study-475566). Ahrefs a aussi documenté en 2026 une chute du CTR de 58 % sur les pages les mieux classées en présence d'AI Overviews. Source : [Ahrefs sur les citations AI Overviews](https://ahrefs.com/blog/ai-overview-citations-top-10/). Le sens général tient, l'amplitude varie selon le panel et l'instrumentation.

Ce qui rend l'étude Averi intéressante pour la doctrine [[concepts/product-led-seo]] tient à deux pages identifiées nominativement dans le rapport. La page la plus dégradée est intitulée « AirOps alternatives » : 77 967 impressions sur 12 mois, 17 clics, 0,02 % de CTR, position moyenne 4,7. La deuxième est la page de témoignages clients (« /customers ») : 17 582 impressions, 5 clics, 0,03 % de CTR, position moyenne 2,9. Ce sont deux pages product-marketing standard d'un SaaS B2B : une page comparative orientée capture d'intention concurrentielle, une page de référence sociale. Elles ne sont pas des pages-outil au sens strict du [[concepts/product-led-seo]] tel que défini dans la doctrine, qui exige que la page elle-même embarque le composant fonctionnel — calculateur, simulateur, configurateur, générateur, comparateur côte à côte avec données temps réel.

La distinction est opérationnelle, pas terminologique. Une page « AirOps alternatives » est un comparatif éditorial. Un LLM générant un AI Overview peut produire 80 % ou plus de cette page : il connaît AirOps, il connaît les concurrents, il peut générer la liste comparative directement dans la réponse. Le [[concepts/test-substitution-llm]] dirait : ne pas créer cette page. Une page calculateur, à l'inverse, embarque un composant interactif que l'AI Overview ne peut pas exécuter dans la SERP. Le test de substitution est tenu, par construction.

L'étude Averi ne mesure pas un échantillon de pages-fonctionnalité au sens strict. Le rapport ne précise pas si la totalité du panel inclut des outils interactifs ou seulement des pages-contenu autour du produit. Les deux pages nommées sont du second type. Tirer du rapport la conclusion « le Product-Led SEO ne marche plus » serait un raccourci que la donnée ne porte pas.

Lien doctrine, en termes nets. Le filtre 80 % de [[concepts/test-substitution-llm]] tient, et reçoit même un appui empirique négatif : les pages substituables par un LLM sont précisément celles qui s'effondrent au CTR dans l'étude. Le [[concepts/product-led-seo]] au sens strict (la page EST l'outil) n'est ni invalidé ni confirmé par cette étude, faute de mesure dédiée. Une fiche de doctrine plus précise pourrait isoler trois catégories distinctes : (1) page-outil interactive, (2) page comparative éditoriale, (3) page de référence sociale. Les deux dernières sont vulnérables à l'AI Overview, la première est défendable jusqu'à preuve du contraire. Proposition à formaliser en revue hebdo.

La réserve méthodologique principale, en plus du caractère mono-source : Averi est éditeur d'un outil de citation IA et propose ses propres remédiations payantes. Le rapport oriente vers son produit. Sa partie chiffrée GSC est néanmoins reproductible avec n'importe quelle propriété GSC ; le motif macro est corroboré indépendamment chez Seer et Ahrefs ; l'angle Product-Led SEO en revanche est ma lecture, pas celle d'Averi.

---

## Brèves

### Audience d'appel 9e Circuit Amazon vs Perplexity le 11 juin à Seattle, avec amici déjà déposés

**Pilier : Recherche agentique (qualification juridique d'un agent IA autorisé par l'utilisateur).**

L'audience d'appel dans Amazon.com Services LLC v. Perplexity AI, Inc. est fixée au 11 juin 2026 à Seattle devant la Cour d'appel des États-Unis pour le 9e Circuit. Sources : [Search Engine Journal, dossier CFAA Amazon-Perplexity](https://www.searchenginejournal.com/amazon-vs-perplexity-the-cfaa-case-that-decides-whether-ai-agents-can-visit-your-website/575499/), [Justia, docket 26-1444](https://dockets.justia.com/docket/circuit-courts/ca9/26-1444).

L'enjeu : le navigateur Comet de Perplexity se connecte au compte Amazon d'un utilisateur sur instruction explicite de ce dernier et finalise des achats. Amazon a obtenu le 10 mars 2026 du tribunal de district du Nord de la Californie une injonction préliminaire bloquant Comet sur ses pages authentifiées, au titre du Computer Fraud and Abuse Act. Perplexity a fait appel ; le 9e Circuit a suspendu l'injonction pendant l'examen et a déposé son mémoire en appel le 8 mai 2026 en qualifiant la lecture CFAA d'Amazon de « fundamental misfit » pour un agent visitant un site sur autorisation explicite de l'utilisateur.

Plusieurs amici curiae ont été déposés. Le 29 avril 2026, la News/Media Alliance et Digital Content Next ont soutenu Amazon. Source : [News/Media Alliance, amicus 29 avril 2026](https://www.newsmediaalliance.org/news-media-alliance-files-amicus-brief-in-amazon-v-perplexity/). Digital Content Next représente des éditeurs cumulant 259 millions de visiteurs uniques aux États-Unis (Associated Press, BBC Studios, Bloomberg, Conde Nast, Dow Jones, Financial Times, NBCUniversal, News Corp, The New York Times, NPR, Vox Media, Washington Post). L'ACLU et plusieurs organisations de défense des libertés ont déposé en sens inverse, en soutien de Perplexity, sur le terrain du Premier Amendement. Source : [ACLU, Amazon v. Perplexity](https://www.aclu.org/cases/amazon-v-perplexity).

Le 11 juin n'est pas une décision au fond mais une plaidoirie. Aucune issue à attendre ce jour-là, hors prises de parole publiques des juges. À surveiller. La résolution de la prédiction P-2026-06-01-v2-2 reste reportée à fin septembre 2026 dans tous les scénarios autres qu'une cassation rapide.

Lien doctrine : la fiche [[concepts/agentic-search]] note comme limite empirique que « l'agentic search au sens strict (agent qui agit) reste mal couvert ». L'affaire en cours est précisément le test juridique de cette limite : un agent qui agit sur autorisation utilisateur, contre un site qui refuse cette autorisation par procédé technique.

### Semrush branche un connecteur MCP dans Perplexity Computer le 3 juin 2026

**Pilier : Recherche agentique (intégration d'un éditeur de données SEO classique dans un moteur génératif).**

Semrush a annoncé le 3 juin 2026 la mise à disposition d'un connecteur Model Context Protocol pour les utilisateurs de Perplexity Computer. Source primaire : [Semrush newsroom, lancement MCP Perplexity](https://www.semrush.com/news/460693-semrush-launches-mcp-connector-in-perplexity-integrating-search-intelligence-within-the-ai-search-engine/). L'intégration donne à Perplexity Computer un accès direct, dans le flux conversationnel, à l'inventaire de Semrush : 28,4 milliards de mots-clés, 43 trillions de backlinks documentés, 261 millions de requêtes LLM tracées, 808 millions de profils de domaines.

Les cas d'usage cités : recherche de mots-clés, analyse concurrentielle, audits SEO, suivi de classements, analytique de domaine, données de backlinks. Le connecteur est disponible pour tout utilisateur Perplexity Computer, sous réserve de disponibilité régionale. Aucune restriction par plan Semrush n'est précisée dans le communiqué.

Le fait stricto sensu : un éditeur de données SEO traditionnel branche sa couche d'inventaire dans un moteur conversationnel via MCP, sans application intermédiaire. Pour le praticien, cela documente la migration de l'usage SEO depuis l'interface dédiée (semrush.com) vers l'interface conversationnelle (perplexity.com). L'accès au backend par programmation reste une activité distincte. Aucun chiffre d'usage n'est publié à ce stade.

Lien doctrine : [[concepts/agentic-search]] décrit l'agent comme entité qui agit sur la recherche, non comme simple répondeur. Le connecteur Semrush MCP fournit à Perplexity une fonction d'accès à des données structurées sur demande, ce qui ressemble à un outil au sens function-calling. La fiche peut être complétée par une note sur l'usage MCP comme couche d'intégration verticale pour des éditeurs de données.

### Eli Schwartz argumente le 4 juin pour un profil product manager dans les rôles AEO

**Pilier : Actualité SEO (recrutement et organisation des équipes search en 2026).**

Eli Schwartz, auteur de Product-Led SEO et conseil en croissance organique, a publié le 4 juin 2026 sur sa newsletter The Future of SEO un essai sur le profil à recruter pour les rôles AEO. Source : [Eli Schwartz, Who should you hire for AEO?, 4 juin 2026](https://www.productledseo.com/p/who-should-you-hire-for-aeo). La thèse : les entreprises recrutent mal en cherchant des exécutants administratifs là où elles ont besoin de profils proches du product management.

Le profil défendu combine cinq caractéristiques : (1) compréhension de l'intention utilisateur derrière la requête, (2) modèle mental du fonctionnement des algorithmes Google et des LLM, (3) capacité à manipuler les données internes (Search Console, analytics, CRM), (4) influence politique sans autorité formelle, (5) usage de l'IA comme multiplicateur sans abdication du jugement. Schwartz cite trois cas chiffrés : BigRentz avec +186 % de trafic et 1 950 conversions sur 12 mois, Self Financial avec +50 000 visites mensuelles et 685 nouveaux clients, Secure Data avec 1 968 appels téléphoniques générés. Sources des cas dans le post, non recoupables indépendamment hors du site Schwartz.

L'argument n'est pas un fait neuf de marché, c'est une prise de position datée d'un praticien sur la structuration des équipes search. La citation directe : « This person looks more like a product manager than anything else ». À mettre en regard du débat plus large sur l'AEO comme prolongement du SEO ou comme discipline distincte ; Schwartz défend une continuité opérationnelle (mêmes leviers internes, même profil de praticien) et une discontinuité de mesure (le clic n'est plus la métrique, la citation l'est).

Lien doctrine : la position de Schwartz est compatible avec [[concepts/product-led-seo]] tel que défini dans le wiki, dans la mesure où elle exige un profil qui décide de produire ou non une page en fonction d'un test de défensibilité (proche du [[concepts/test-substitution-llm]]). C'est un appui externe au filtre 80 %, sans le formaliser.

---

## Notes éditoriales

Cette édition v2 du 8 juin se distingue franchement de la v1 du même jour. V1 = pilier Actualité SEO (CNN-Perplexity et bilan core update mai). V2 = pilier Product-Led SEO en info du jour (étude Averi), brèves Recherche agentique (Amazon-Perplexity audience 11 juin, Semrush MCP) et Actualité SEO (Eli Schwartz Hiring AEO). Aucun chevauchement avec said_index v1.

Sources nouvelles ce run : aucune source vraiment neuve à ajouter au registre explore. Averi est déjà en explore (trust 0.62, plusieurs hits utiles, candidate au passage exploit en revue hebdo si l'étude du 8 juin est confirmée par d'autres mesures indépendantes). Eli Schwartz / productledseo.com est ajouté en explore (trust 0.8, source de référence sur le pilier Product-Led SEO, auteur du livre éponyme, 15 000+ abonnés Substack), avec recoupement insuffisant ce run pour passer en exploit (un seul article cité).

Doctrine touchée et propositions : (1) [[concepts/product-led-seo]] mérite une distinction explicite entre pages-fonctionnalité (interactives, défendables) et pages-contenu autour du produit (comparatifs, témoignages, vulnérables) ; (2) [[concepts/test-substitution-llm]] reçoit un appui empirique indirect, à formaliser comme observation et non comme preuve ; (3) [[concepts/agentic-search]] peut être complétée par une note sur l'intégration MCP comme couche verticale d'éditeurs de données dans les moteurs génératifs.

Prédictions ouvertes confortées par ce run : P-2026-06-06-v3-2 (au moins un site Product-Led documente publiquement une perte de trafic mesurée sur une page substituable) reçoit ici une mesure concrète sur deux pages nominalement identifiées d'un SaaS B2B, à reclasser en `resolved-partial` à l'agent 9. P-2026-06-01-v2-2 (appel Amazon-Perplexity non tranché au fond avant 2026-09-30) reste ouverte, à reconsidérer après la plaidoirie du 11 juin.

Une prédiction nouvelle à ajouter : P-2026-06-08-v2-1, sur l'éligibilité empirique du test de substitution LLM, à formuler en agent 9.

Une piste écartée et loggée : l'article Kevin Indig du 1er juin 2026 « AIOs turn search into reading sessions » (846 000 sessions, repris par Search Engine Land le 3 juin) recoupe une étude déjà traitée en édition v1 du 8 juin sur le même dataset SEJ 846K. Pas de fait neuf, pas de brève. À garder en veille pour une éventuelle suite avec mesure d'engagement ou de conversion.

Rien n'a été envoyé.
