# Algorithme — édition du 20 juin 2026

*Pilier info du jour : Recherche agentique.*

## Résumé en 4 points

- Google publie le 17 juin 2026 la spécification Agentic Resource Discovery (ARD), un protocole ouvert v0.9 sous Apache 2.0 cosigné par onze acteurs (Cisco, Databricks, GitHub, GoDaddy, Google, Hugging Face, Microsoft, Nvidia, Salesforce, ServiceNow, Snowflake) qui permet à un agent IA de découvrir et de vérifier les capacités disponibles à l'exécution, via deux primitives : un fichier `ai-catalog.json` posé à un chemin connu du domaine d'un éditeur, et une API de registre qui indexe les catalogues et répond à une requête en langage naturel.
- Trois implémentations de référence sortent le même jour : GitHub Agent Finder, Hugging Face Discover Tool, Cisco AGNTCY Agent Directory. Le support natif côté Google Agent Registry est annoncé pour les mois à venir.
- À Search Central Live Milan le 18 juin 2026, Google indique que forcer un découpage en paragraphes pour faciliter l'IA n'apporte rien au classement, prépare un signal de qualité au niveau du site dans Search Console, et observe que les clics venant d'un AI Overview ont une durée de session plus élevée.
- Google met à jour le 18 juin 2026 sa documentation de migration de domaine : la demande Change of Address doit couvrir toutes les variantes (www, non-www, sous-domaines) même inutilisées, et l'outil est explicitement déconseillé dans quatre cas (HTTP vers HTTPS, changement de catégorie d'URL, bascule www / non-www seule, changement d'hébergeur ou de CDN sans changement d'URL).

---

## Info du jour — Google publie le 17 juin 2026 la spécification Agentic Resource Discovery (ARD), protocole ouvert cosigné par onze acteurs pour la découverte de capacités côté agents

Google a publié le 17 juin 2026 la spécification Agentic Resource Discovery (ARD), un protocole ouvert pour publier, découvrir et vérifier des capacités IA accessibles à un agent ([Google Developers Blog, Junjie Bu et Srinivas Krishnan](https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/), [Search Engine Journal, Matt G. Southern](https://www.searchenginejournal.com/google-microsoft-back-draft-ai-agent-discovery-spec/579894/), [site officiel agenticresourcediscovery.org](https://agenticresourcediscovery.org/), [Hugging Face Blog](https://huggingface.co/blog/agentic-resource-discovery-launch)).

Onze acteurs cosignent la spécification : Cisco, Databricks, GitHub, GoDaddy, Google, Hugging Face, Microsoft, Nvidia, Salesforce, ServiceNow, Snowflake. La spécification est en version draft v0.9, sous licence Apache 2.0. Elle s'appuie sur le modèle de données AI Catalog porté par l'AI Catalog Working Group de la Linux Foundation.

Deux primitives techniques. Premièrement, un fichier `ai-catalog.json` que l'organisation publie à un chemin connu sur son domaine (`/.well-known/ai-catalog.json`). Ce fichier liste les capacités exposées : agents, serveurs MCP, skills, plugins, APIs, workflows. La propriété du domaine sert d'identité, et une couche de métadonnées cryptographiques peut s'ajouter pour la vérification. Deuxièmement, une API de registre, qu'une organisation peut exploiter pour son propre périmètre, qui parcourt les catalogues, les indexe, et répond à une requête en langage naturel posée par un agent. Plusieurs registres peuvent coexister, avec leurs politiques propres de confiance, classement et accès, sans catalogue central. Le modèle est explicitement fédéré, et les registres peuvent se référencer entre eux.

ARD ne remplace pas le Model Context Protocol (MCP). MCP décrit comment un client se connecte à une capacité et l'invoque. ARD décrit comment l'agent trouve cette capacité au moment de l'exécution, sans pré-câblage. Les serveurs MCP figurent parmi les types de capacités qui peuvent être déclarés dans un catalogue ARD. La distinction est posée explicitement dans la spécification : ARD est un protocole de découverte, pas un runtime d'exécution.

Trois implémentations sortent le même 17 juin 2026. GitHub publie Agent Finder. Hugging Face publie Discover Tool, qui adapte la recherche sémantique de son Hub aux contraintes du format ARD (catalogue accessible sur `huggingface.co/.well-known/ai-catalog.json`, négociation de type média entre `application/ai-skill`, `application/mcp-server+json` et un format propre). Cisco intègre l'AGNTCY Agent Directory. Côté Google, le support natif de ARD dans Agent Registry est annoncé pour les mois suivants, sans date précise dans la publication.

Lecture. Trois implications opérationnelles.

Premièrement, le problème adressé est la couche au-dessus de MCP : la découverte. L'écosystème agentique a multiplié au premier semestre 2026 les points d'accès (Adyen Agentic pour le paiement le 16 juin 2026, Visa Agent Score et Agentic Directory au Visa Payments Forum du 10 juin 2026, L'Oréal × OpenAI le 17 juin 2026, WebMCP côté navigateur, Open Knowledge Format côté connaissance). Chaque acteur a sa propre forme d'entrée. ARD propose un format de catalogue unique qui permet à un agent de demander, à l'exécution, où trouver une capacité, sans qu'un développeur ait préalablement codé la connexion. Cela rapproche la situation d'une logique de référencement : exister sur l'index d'un registre devient l'équivalent agentique d'exister sur l'index d'un moteur de recherche.

Deuxièmement, l'identité du publieur passe par le domaine. La spécification utilise la propriété du domaine (le fait que `example.com/.well-known/ai-catalog.json` n'est servi que par l'entité qui contrôle `example.com`) comme base d'identité, avec possibilité d'ajouter des signatures cryptographiques en production. C'est la même mécanique que le `robots.txt`, le `sitemap.xml` ou la TLS, transposée à la couche capacité. Pour une marque, la question opérationnelle nouvelle est : qui publie mon `ai-catalog.json`, qui décide des capacités exposées, et qui en mesure la consommation. Aucun de ces trois rôles n'a aujourd'hui de propriétaire évident dans une organisation marketing classique.

Troisièmement, le modèle fédéré et concurrent des registres ouvre une zone de mesure inédite. Plusieurs registres pourront indexer les mêmes catalogues, avec des politiques différentes de classement et de confiance. Pour un agent client, le choix du registre devient une décision (équivalent du choix du moteur de recherche), et pour la marque, la visibilité dans tel ou tel registre devient une métrique distincte. La fiche [[concepts/metriques-visibilite-geo]] devra à terme couvrir non seulement la présence dans les réponses génératives mais aussi l'indexation dans les registres ARD, avec des outils de mesure encore inexistants au 20 juin 2026.

Doctrine. Lien direct avec [[concepts/agentic-search]] : ARD formalise la couche découverte que la fiche posait jusqu'ici uniquement côté demande (« être sélectionné par l'agent »). Lien indirect avec [[concepts/metriques-visibilite-geo]] (indexation dans un registre comme nouvelle dimension de mesure, à ajouter) et [[concepts/structural-information-geo]] (le `ai-catalog.json` est de l'information structurelle native par le domaine, dans la même logique que `robots.txt`, `sitemap.xml` ou les schémas JSON-LD).

Limites. Premièrement, version draft v0.9. Le format peut évoluer sur des points significatifs avant publication finale. Pas d'engagement de stabilité publié à ce stade. Deuxièmement, le support côté Google Agent Registry n'est pas effectif au 20 juin 2026. Hugging Face, GitHub et Cisco fournissent des implémentations utilisables ; Google annonce sans date. Tant qu'un acteur dominant n'opère pas un registre largement adopté, l'effet de réseau reste limité. Troisièmement, ARD ne dit rien des politiques de classement à l'intérieur d'un registre : les critères qui décideront quel agent ou quelle capacité sort en premier sur une requête en langage naturel restent à la main du registre. La transparence sur ces critères est l'enjeu suivant. Quatrièmement, aucune mesure publique d'adoption du format `ai-catalog.json` sur le web ouvert au 20 juin 2026. Les volumes sont à construire.

Prédiction. Au moins un acteur enterprise d'analytique ou de data warehousing (Snowflake étant le premier candidat puisque cosignataire) publiera avant le 31 décembre 2026 une mesure d'adoption de `ai-catalog.json` sur un échantillon de 10 000+ domaines, comparable à la mesure Ahrefs sur `llms.txt` du 15 juin 2026. Le taux d'adoption initial sera inférieur à 5 % des domaines mesurés.

---

## Brèves

### B1 — Google précise à Search Central Live Milan le 18 juin 2026 la position « chunking inutile pour l'IA », un signal qualité site dans Search Console, et observe un meilleur engagement post-AI Overview (Actualité SEO)

Google a tenu un Search Central Live à Milan le 18 juin 2026, couvert le jour même par Search Engine Roundtable et plusieurs reprises spécialisées ([Search Engine Roundtable, Barry Schwartz](https://www.seroundtable.com/google-search-central-live-milan-41533.html), [Digital Phablet](https://digitalphablet.com/digital-marketing/ai-insights-chunking-signals-paywalls-subscriptions/)).

Quatre points opérationnels documentés.

Sur le découpage de contenu (« chunking »), Google indique que forcer un format en chunks courts pour faciliter la consommation par l'IA n'apporte rien. La citation reprise par les comptes-rendus : « Forcer le découpage en paragraphes pour l'IA est inutile ; l'organisation du contenu doit suivre des critères de lisibilité humaine. » Côté moteur, les systèmes de Google traitent la nuance de plusieurs sujets dans une même page et savent montrer le passage pertinent à l'utilisateur. C'est cohérent avec la position de John Mueller du printemps 2026 sur le fichier `llms.txt` qualifié de « temporary crutch » pour les outils de codage.

Sur les réglages IA dans Search Console, Google confirme un déploiement progressif des fonctions de reporting IA et indique le travail en cours sur un signal de qualité agrégé au niveau du site qui peut tirer le classement vers le bas. La formulation rapportée : « Une URL n'est pas une île ; elle fait partie de votre site dans son ensemble, et la qualité site-wide peut peser sur le ranking. »

Sur les abonnements et paywalls, Google met en avant la combinaison Subscription Linking + Reader Revenue Manager pour structurer un contenu payant. Le compte-rendu cite un chiffre d'études internes : « +34 % d'engagement utilisateur » sur la découverte de contenu pour les abonnés existants, lorsque la structure paywall est correctement déclarée via Reader Revenue Manager. Le chiffre est attribué à Google sans publication méthodologique séparée à ce jour ; il est à traiter comme déclaratif vendeur, à recouper.

Sur les clics venant d'AI Overviews, Google indique que le trafic entrant par un lien interne d'un AI Overview a une durée de session plus élevée que le trafic moyen. Aucune valeur chiffrée n'est publiée. C'est la première formulation publique de Google qui assume un effet qualité positif de la sélection AIO sur l'engagement post-clic, là où l'attention publique s'était focalisée sur la baisse de CTR ([[concepts/metriques-visibilite-geo]] doit prendre en compte cette dimension d'engagement, distincte du CTR brut).

Lecture. L'événement n'apporte pas d'annonce produit majeure, mais consolide quatre positions de Google qui étaient jusqu'ici fragmentées : pas de format spécial IA en interne du contenu, signal site-wide qui pèse, dispositif paywall officiel, et engagement positif des clics AIO. Pour un éditeur, l'écart entre la perte de CTR documentée par Seer Interactive (24 avril 2026, 53 marques, +120 % d'écart CTR pour les pages citées vs non citées) et l'engagement post-clic plus élevé reformulé ici par Google se résout opérationnellement : la priorité reste la citation, pas l'optimisation de format pour le passage en chunks. La fiche [[concepts/structural-information-geo]] gagne une confirmation officielle qu'aucune mise en forme spécifique IA n'est attendue sur la page produit ou éditorial pour le moteur.

Limites. Premièrement, les comptes-rendus utilisés (Search Engine Roundtable, Digital Phablet) reposent sur la prise de notes d'assistants à l'événement. Aucune transcription officielle Google publiée au 20 juin 2026. Les formulations exactes peuvent diverger d'un compte-rendu à l'autre. Deuxièmement, le chiffre « +34 % d'engagement utilisateur » paywall est interne Google, non publié sous forme d'étude. À traiter en directionnel, pas en valeur de référence. Troisièmement, l'observation « durée de session plus élevée après clic AIO » n'a aucune valeur numérique attachée publique au 20 juin, et n'est attestée que par les comptes-rendus secondaires de l'événement.

### B2 — Google resserre le 18 juin 2026 la documentation de migration de domaine : toutes les variantes (www, non-www, sous-domaines) doivent être migrées, quatre cas où l'outil Change of Address est déconseillé (Actualité SEO)

Google a mis à jour le 18 juin 2026 sa documentation sur les migrations de domaine et l'usage de l'outil Change of Address de Search Console ([Search Engine Land, Barry Schwartz](https://searchengineland.com/for-site-moves-specify-all-domain-variants-with-googles-change-of-address-tool-480552), [Search Engine Journal, Roger Montti](https://www.searchenginejournal.com/google-tightens-requirements-for-domain-migrations/579781/)).

Texte de la consigne mise à jour, repris in extenso par Search Engine Journal : « For domain migrations: If you're moving your site from one domain to another, make sure to submit Change of Address requests for all subdomains and the www and non-www variants of the old domain name (for example, from en.example.com, www.example.com, and example.com to new-example.net). » Les variantes doivent être vérifiées dans Search Console avant la soumission, même celles qui ne sont pas activement utilisées.

Quatre cas où Google déconseille l'outil Change of Address, repris par Search Engine Journal :

- migration de HTTP vers HTTPS ;
- changement de structure d'URL de catégorie (par exemple `/blog/` vers `/articles/`) ;
- bascule de www vers non-www ou inversement seule (sans changement de domaine) ;
- changement d'hébergeur ou de CDN, lorsque les URL restent identiques.

Justification publiée par Google dans le changelog associé : « Domain migrations work best when all variants of a site are migrated properly. »

Lecture. Trois implications opérationnelles.

Premièrement, la mise à jour ne change pas l'algorithme. Elle renforce le contrat opérationnel : un site qui rate la migration d'une variante (un sous-domaine `en.example.com` que personne n'utilise mais qui reste indexé, par exemple) risque de perdre la passation de signaux sur cette variante. Pour un site en migration de domaine, la checklist devient stricte sur l'inventaire des sous-domaines verifiés en Search Console, pas seulement ceux marketés.

Deuxièmement, la liste des quatre cas déconseillés délimite explicitement l'usage de l'outil. Une migration HTTP vers HTTPS, par exemple, doit passer par les redirections 301 et la déclaration `https` en propriété, pas par Change of Address. C'est l'occasion pour Google de clarifier un usage que beaucoup d'agences avaient extrapolé à tort.

Troisièmement, sur la stratégie de migration globale, le resserrement met l'accent sur la complétude au moment de la passation. Pour un site avec plusieurs sous-domaines techniques (CDN, support, blog, environnements de staging exposés indexables), le travail préparatoire d'inventaire et de vérification dépasse maintenant la migration marketing du domaine principal.

Limites. Premièrement, la mise à jour de documentation ne s'accompagne d'aucune étude empirique sur l'effet quantifié des migrations « incomplètes » antérieures, et reste donc une consigne opérationnelle sans chiffres mesurés. Deuxièmement, la documentation ne précise pas le délai au-delà duquel une Change of Address devient inutile (par exemple : ancien domaine inactif depuis 18 mois) ; ce point reste à la main du praticien. Troisièmement, deux comptes-rendus indépendants sont disponibles (SEL Schwartz et SEJ Montti, tous deux 18 juin 2026), mais l'historique du changement côté Google (date exacte du commit documentation, version précédente) n'est pas publié sur le diff visible.

---

## Méthode et incertitudes

Édition produite en mode cloud, sans accès local au binaire `./kb` ni à `youtube-claude-seo`. Recoupement réalisé sur sources web uniquement. Deux brèves, structure assumée comme pour 2026-06-17-v2 : info du jour franchement structurelle (ARD multi-acteurs) + deux brèves Actualité SEO sur des annonces opérationnelles fraîches du 18 juin 2026. Pilier info du jour varié par rapport aux six dernières (Actualité 2026-06-19-v2 → Recherche agentique 2026-06-19 → GEO 2026-06-18-v2 → Actualité 2026-06-18 → Recherche agentique 2026-06-17-v2 → GEO 2026-06-17), et fait franchement neuf qui justifie le retour en Recherche agentique : 11 cosignataires industriels, distinct de MCP, trois implémentations le jour même.

Info du jour ARD : 4 sources indépendantes (Google Developers Blog primaire, agenticresourcediscovery.org spécification, Search Engine Journal Matt G. Southern, Hugging Face Blog). Liste des onze cosignataires confirmée par deux sources (SEJ + site officiel). Version draft v0.9 et licence Apache 2.0 confirmées par site officiel. Pas de chiffre d'adoption à publier à ce stade. Distinct de l'info du jour Adyen Agentic du 2026-06-19 (couche paiement, un PSP) et de l'info du jour L'Oréal × OpenAI du 2026-06-17-v2 (couche fabricant FMCG, un acteur).

B1 Search Central Live Milan : 2 sources (Search Engine Roundtable Schwartz primaire, Digital Phablet reprise). Chiffre « +34 % engagement paywall » est interne Google sans publication méthodologique, à traiter directionnel. Citations Google reprises de comptes-rendus, pas de transcription officielle au 20 juin 2026.

B2 Google domain migration : 2 sources indépendantes (Search Engine Land Schwartz 18 juin + Search Engine Journal Montti 18 juin). Texte de la consigne et liste des quatre cas déconseillés confirmés sur les deux sources. Date exacte du commit Google côté documentation non publiée.

Anti-pattern IA. Run propre sur le plan de la voix. Zéro métaphore vérifiée (pas de bataille, vague, rails, moteur figuré, ouvrir la voie, écosystème imagé, passer à la caisse). Tentations identifiées et écartées : « ARD pose les bases de la découverte agentique » (rejeté pour info du jour, métaphore implicite), « la couche au-dessus de MCP » (gardé : descriptif littéral de l'architecture, ARD opère effectivement à un niveau distinct de MCP), « formaliser la frontière » (rejeté B1, métaphore géographique), « contrat opérationnel » (gardé B2, vocabulaire opérationnel standard). Aucune personnification de Google, Microsoft, Hugging Face, GitHub, Cisco, Snowflake, OpenAI. Citations Google reprises de comptes-rendus signalées comme telles. Vouvoiement maintenu. Pas de tiret cadratim hors structurels markdown.

Prochaines fenêtres à surveiller. (1) Première mesure publique d'adoption du format `ai-catalog.json` sur un échantillon large (par analogie avec l'étude Ahrefs sur `llms.txt` du 15 juin 2026). (2) Date effective de support natif ARD dans Google Agent Registry. (3) Annonce d'un registre ARD opéré par un acteur tiers (par exemple une plateforme de discovery enterprise, ou un acteur ouvert). (4) Publication par Google d'une transcription officielle de Search Central Live Milan, ou d'une étude méthodologique sur le chiffre « +34 % engagement paywall » repris à l'événement. (5) Premières remontées de praticiens SEO sur les effets de la consigne Change of Address mise à jour sur des migrations en cours.
