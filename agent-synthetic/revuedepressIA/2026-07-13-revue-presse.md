# Algorithme, édition du 13 juillet 2026 · La mesure de la visibilité dans les moteurs de réponse IA se déplace des vendeurs SEO vers les outils opérateurs côté marque

*Draft SyntheticBrain, non publié.*

## À retenir

- Theory House, agence de branding retail qui compte PepsiCo, McCormick et Diageo comme clients, a lancé Kasper via son incubateur TheoryNXT en juin 2026 : un outil qui interroge ChatGPT, Gemini et Perplexity et calcule un « Brand Inclusion Rate » pour les marques CPG.
- Loftie, marque de wellness, mesure depuis fin 2025 la part de clients qui déclarent avoir entendu parler d'elle via un moteur IA en post-purchase survey : 1,5 pct à Q4 2025, 3 pct à mai 2026. Matthew Hassett, son fondateur, a également construit un agent interne, Mariah, qui interroge mensuellement les principaux moteurs.
- Cette couche de mesure côté opérateur (marque qui achète ou construit son outil) est distincte de la couche vendeur SEO (Ahrefs Brand Radar, Semrush AI Visibility Toolkit, Profound, Previsible, CiteLens) déjà documentée dans les éditions précédentes.
- Brève 1 · Duane Forrester (Search Engine Journal, 9 juillet) documente le mécanisme de retrieval collapse via un papier de la conférence Web 2026 : quand deux tiers d'un corpus est synthétique, plus de 80 pct des passages effectivement récupérés dans les réponses le sont aussi.
- Brève 2 · Jason Tabeling (Search Engine Land, 10 juillet) publie une lecture opérationnelle du Universal Commerce Protocol : l'attribut `native_commerce` de Google Merchant Center devient éligibilité de base pour qu'un produit apparaisse dans une transaction agentique.
- Brève 3 · Modern Retail confirme que Shopify a ajouté un tableau de bord dédié à la traçabilité des ventes provenant de canaux d'achat IA, côté marchand. Le suivi par canal générique quitte le blog vendor pour devenir un composant natif de la plateforme e-commerce.

---

## Info du jour · Business SEO / GEO. Les marques CPG bâtissent leur propre couche de mesure de visibilité dans les moteurs de réponse IA, distincte des outils vendus par les acteurs SEO

Modern Retail a publié le 30 juin 2026 une enquête d'Anna Hensel intitulée [Brands Briefing: Measurement is the next frontier in GEO for brands](https://www.modernretail.co/technology/brands-briefing-measurement-is-the-next-frontier-in-geo-for-brands/), qui documente une transition peu commentée jusqu'ici : la mesure de la visibilité dans les moteurs de réponse IA ne se joue plus seulement chez les fournisseurs d'outils SEO, elle devient un chantier interne côté marque.

**Kasper by Theory House, via TheoryNXT.** Jim Cusson, président de l'agence de branding retail Theory House (clients cités : PepsiCo, McCormick, Diageo, Proximo Spirits), a lancé Kasper via son incubateur TheoryNXT. La page produit primaire [getkasper.ai](https://getkasper.ai) décrit Kasper comme un « agentic commerce audit tool that measures how visible your brand is when AI systems make product recommendations ». La métrique centrale, dénommée Brand Inclusion Rate™, se calcule en interrogeant trois moteurs, ChatGPT, Gemini et Perplexity, avec 100 questions à forte intention par moteur soit 300 réponses par cycle. Modern Retail cite un chiffre supérieur pour l'offre étendue, jusqu'à 1 000 requêtes par mois selon la catégorie couverte. Le processus documenté sur le site tient en cinq étapes : description de la marque, mesure du taux d'inclusion, calcul de la part invisible dans la catégorie, score de commerce agentique, feuille de route d'optimisation. La page ajoute « Amazon Rufus, and whatever comes next » comme extension future des moteurs interrogés.

**Loftie et l'agent Mariah.** La marque de wellness Loftie, connue pour un réveil connecté, a ajouté une question dans son post-purchase survey pour saisir la part d'acheteurs qui déclarent avoir entendu parler de la marque en premier lieu via un moteur IA (ChatGPT, Gemini). Anna Hensel cite deux mesures issues de Loftie : environ 1,5 pct à la fin de 2025, environ 3 pct six mois plus tard. Matthew Hassett, fondateur de Loftie et opérateur d'une plateforme distincte pour le commerce direct-to-consumer nommée Deliberate, a également construit un agent interne baptisé Mariah, qui pose mensuellement la même série de questions aux principaux moteurs pour mesurer combien de fois Loftie est mentionné. Verbatim Hassett dans l'article : « If you don't prepare for it, you are missing out ».

**Autres pièces de la même couche opérateur.** L'article cite un tableau de bord Shopify ajouté côté marchand pour tracer les ventes provenant de canaux d'achat IA, ainsi que deux startups qui vendent des outils de share of voice IA, Evertune et Profound. Ce dernier point relève de la couche vendeur, mais le tableau de bord Shopify appartient à la couche opérateur puisqu'il devient un composant natif d'une plateforme e-commerce que la marque utilise directement.

**Lecture SEO/GEO.** Cette édition inscrit la mesure GEO dans deux couches complémentaires, jusqu'ici confondues dans les analyses.
- La couche **vendeur analyste** (déjà documentée) rassemble Ahrefs Brand Radar sur 260M prompts, Semrush AI Visibility Toolkit sur 126M prompts, Profound côté zero-click session, Previsible sur 6,77M sessions GA4 (édition du 7 juillet v2), CiteLens sur 500 prompts (édition du 3 juillet v2). Ces outils produisent une mesure horizontale pluri-clients, souvent commercialisée sous forme de rapport ou d'abonnement.
- La couche **opérateur / marque** (celle documentée ici) rassemble Kasper via TheoryNXT, l'agent Mariah construit par Hassett pour Loftie, et le tableau de bord Shopify natif. Elle produit une mesure verticale mono-client, alignée sur la stratégie de la marque et connectée à sa propre séquence commerciale (post-purchase survey, catalogue, funnel).

Ces deux couches ne mesurent pas exactement la même chose et ne servent pas les mêmes décisions.
- La couche vendeur mesure un share of voice comparatif dans un univers de prompts standardisés. Elle sert la comparaison concurrentielle et l'audit sectoriel.
- La couche opérateur mesure l'apparition dans les prompts commerciaux du client précis, croisée avec l'auto-déclaration acheteur, et sert la décision d'allocation de budget en interne (média, contenu, catalogue, structure).

**Doctrine touchée.** Le concept [[metriques-visibilite-geo]] gagne une dimension supplémentaire : la mesure côté opérateur (Brand Inclusion Rate mono-marque + attribution acheteur en post-purchase) s'ajoute aux dimensions déjà documentées côté agrégat (impressions Google GSC AI Overviews Search Console, position dans réponse générative, referral tracable GA4 dans Previsible, share of voice pluri-clients dans les outils vendor). Le concept [[data-proprietaire]] se renforce : Kasper monétise une méthodologie vendue à la marque, mais Loftie via Mariah génère sa propre donnée sans intermédiaire, ce qui pose la question de l'internalisation vs externalisation de la mesure GEO. Le concept [[concepts/tabou-visibilite]] tient : les acteurs cités ici parlent d'« inclusion », de « recommandation », d'« attribution », pas de « visibilité » ; ce vocabulaire précis fait le travail.

**Limites documentaires à énoncer.**
- **Source vendeur pour Kasper.** La page getkasper.ai est un site marketing et l'article Modern Retail cite Jim Cusson, fondateur de la solution. Aucune évaluation méthodologique tierce indépendante n'est publiée à ce jour. La description de la méthodologie (100 questions à forte intention par moteur, 3 moteurs) et le volume mensuel évoqué (jusqu'à 1 000 requêtes) ne sont pas assortis d'une définition publique du critère d'apparition (mention textuelle, mention dans la liste comparée, position dans la réponse).
- **Loftie 1,5 pct puis 3 pct sur 6 mois.** Chiffres auto-déclarés par la marque, sans publication du protocole du post-purchase survey (échantillon, taux de réponse, formulation exacte de la question). L'auto-déclaration acheteur souffre du biais mémoire et du biais social ; la mesure est indicative, pas fiable comme baseline.
- **Agent Mariah non documenté publiquement.** L'agent est cité par le fondateur mais aucune méthodologie, aucun code, aucune donnée agrégée n'est rendu public. La mesure interne est utile en régime de décision, pas comme benchmark reproductible.
- **Le pilier Business SEO a été info du jour deux fois sur les trois éditions précédentes.** Le sujet est ici cadré comme GEO/Business SEO parce que l'angle central est la couche de mesure de visibilité dans les moteurs de réponse IA, distincte des angles récents (SSI Kevin Indig 12 juillet v1, motion NYT vs OpenAI 11 juillet v2).

**Implication opérationnelle pour un consultant SEO/GEO.**
- Sur un audit client dans le CPG ou le commerce direct-to-consumer, séparez la question « quel est mon share of voice dans les prompts sectoriels standardisés » (couche vendeur, à mesurer avec un outil comme Ahrefs Brand Radar ou Semrush AI Visibility Toolkit) de la question « combien d'acheteurs déclarent m'avoir découvert via un moteur IA » (couche opérateur, à mesurer avec un post-purchase survey ou un agent maison).
- Kasper facture la méthode. Si le client dispose déjà d'une équipe technique, un agent maison type Mariah avec 3 moteurs et 100 requêtes par cycle est reproductible à faible coût et livre la mesure alignée sur le catalogue précis du client, sans partager la donnée à un tiers.
- Le chiffre Loftie de 1,5 pct à 3 pct sur 6 mois est un point de référence utile, uniquement en direct-to-consumer wellness. Ne l'extrapolez pas à d'autres verticales sans mesure propre.

**Prédictions vérifiables datées.**
- **P-2026-07-13-1** (échéance 31 décembre 2026) : d'ici la fin 2026, une deuxième agence de branding CPG ou retail publie un outil de mesure de visibilité IA équivalent à Kasper (méthodologie propre, moteurs listés, métrique nommée). Résolution positive : billet blog ou page produit d'une agence nommée. Résolution négative : silence sur ce créneau spécifique.
- **P-2026-07-13-2** (échéance 31 mars 2027) : d'ici fin mars 2027, au moins une plateforme e-commerce parmi BigCommerce, Salesforce Commerce Cloud, Adobe Commerce ou WooCommerce ajoute un tableau de bord natif de traçabilité des ventes provenant de canaux d'achat IA, comparable à celui de Shopify. Résolution positive : page produit ou release note nommée. Résolution négative : aucune annonce.
- **P-2026-07-13-3** (échéance 30 septembre 2026) : d'ici fin septembre 2026, Kasper publie ou Modern Retail documente un premier score Brand Inclusion Rate mesuré chez un client CPG nommé. Résolution positive : chiffre publié attribué à une marque. Résolution négative : aucune donnée publique.

---

## Brèves

### Brève 1 · Actualité SEO / GEO doctrinal. Le mécanisme de retrieval collapse documenté empiriquement quand le corpus se remplit de contenus synthétiques

Duane Forrester, ancien senior product manager chez Bing et Microsoft, a publié le 9 juillet 2026 sur Search Engine Journal [The Web Is Eating Itself And Your Metrics Look Fine](https://www.searchenginejournal.com/the-web-is-eating-itself-and-your-metrics-look-fine/581497/), une synthèse doctrinale qui articule quatre études empiriques.

**Chiffres cités.**
- **Graphite** : plus de la moitié des articles anglophones nouvellement publiés sur le web sont déjà générés par IA (chiffre repris par Forrester sans URL primaire dans son article, à recouper).
- **Jordi Ribas, Microsoft** : les agents IA pourraient générer « a thousand times more queries than all human search combined » d'ici quelques années (verbatim cité par Forrester, source primaire Ribas non liée dans l'article).
- **Papier ACM Web Conference 2026** (arXiv [2602.16136](https://arxiv.org/abs/2602.16136), Hongyeon Yu, NAVER Corp) : quand deux tiers du corpus disponible devient synthétique, plus de 80 pct des passages effectivement récupérés dans les réponses sont synthétiques, alors même que la précision moyenne des réponses ne varie quasiment pas (68 à 70 pct). Titre exact du papier : « Retrieval Collapses When AI Pollutes the Web ». Présenté à la conférence à Dubaï du 13 au 17 avril 2026.
- **Étude SIGIR** citée par Forrester (source primaire non liée dans l'article) : les systèmes de retrieval présentent un biais de préférence mesurable pour le texte machine-généré, sans justification de pertinence.

**Lecture.** Le mécanisme est double. D'abord un biais de source qui promeut le contenu machine sans amélioration de pertinence. Ensuite une contamination du réservoir de sources dans lequel les moteurs de réponse puisent : le contenu synthétique atteint un seuil au-delà duquel les réponses générées cannibalisent leur propre alimentation. La précision de surface reste stable, ce qui masque la dégradation en amont et rend l'alerte difficile pour les équipes qui suivent seulement leur volume de citations et leur CTR AIO.

**Recoupement.** Le papier a été relayé le 25 juin 2026 par [Axios](https://www.axios.com/2026/06/25/ai-search-collapse-geo-seo) et par [Unite.ai](https://www.unite.ai/ai-pollution-in-search-results-risks-retrieval-collapse/), qui documente la mécanique en deux étapes (dominance du contenu IA puis infiltration adversariale). Le papier est disponible en preprint sur arXiv et publié dans les proceedings de l'ACM Web Conference 2026.

**Limite.** Le papier NAVER modélise le phénomène avec un protocole contrôlé qui ajoute du contenu machine-généré à un pool réel de résultats de recherche par tours successifs. Le seuil des deux tiers n'a pas été observé en conditions naturelles sur un corpus web complet. La mesure Graphite de « plus de la moitié » d'articles anglophones IA-générés est publiée par Graphite en 2024 sur un échantillon Common Crawl et souffre de biais de détection (les classifieurs de contenu IA ont un taux d'erreur documenté sur les articles hybrides humain-IA).

**Doctrine.** Le concept [[structural-information-geo]] gagne une dimension antagoniste : la structure ne suffit pas si le pool d'entrée est massivement synthétique. Le concept [[data-proprietaire]] est renforcé : produire de la data originale et signée devient un signal de rareté dans un pool contaminé. Le concept [[concepts/anti-ai-writing]] gagne un motif empirique complémentaire : au-delà du style, l'origine machine du texte pénalise le retrieval lui-même quand le seuil de contamination est atteint.

**Prédiction vérifiable datée.**
- **P-2026-07-13-4** (échéance 30 juin 2027) : d'ici fin juin 2027, une deuxième équipe de recherche publie une reproduction du protocole retrieval collapse sur un corpus distinct de NAVER, avec un seuil de contamination mesuré (pouvant confirmer ou infirmer les deux tiers de Yu et al.). Résolution positive : papier arXiv ou proceedings identifiés. Résolution négative : silence sur la reproduction.

### Brève 2 · Recherche agentique. Une lecture opérationnelle du Universal Commerce Protocol place l'éligibilité aux transactions agentiques dans le Merchant Center

Jason Tabeling (Further) a publié le 10 juillet 2026 sur Search Engine Land l'analyse [Google's Universal Commerce Protocol: The SEO implications](https://searchengineland.com/google-universal-commerce-protocol-seo-implications-481923), qui documente ce que le UCP change concrètement dans le workflow SEO d'un e-commerce.

**Faits déjà connus rappelés dans l'article.** Le UCP est un standard open source co-développé par Google avec Shopify, Walmart, Target, Wayfair et Etsy, présenté à Google I/O 2026. Il permet aux agents IA de découvrir, évaluer, comparer et effectuer des achats directement dans les interfaces conversationnelles Google (AI Mode, Gemini, YouTube, Gmail). Le marchand garde son statut de Merchant of Record.

**Nouveauté opérationnelle documentée dans l'article.** Google Merchant Center a introduit de nouveaux attributs sémantiques et une capacité `native_commerce` qui rend un produit éligible aux transactions via UCP. Tabeling recommande trois étapes techniques : activer l'attribut `native_commerce` dans Google Merchant Center pour chaque produit éligible, synchroniser les données structurées `Product`, `Offer`, `Review` avec le flux catalogue, préparer les données de compatibilité et d'inventaire temps réel.

**Lecture.** L'article n'apporte pas de fait nouveau côté produit (le UCP a été couvert dans plusieurs éditions précédentes, notamment 30 mai v3 pour l'annonce initiale et 12 juin v2 pour l'articulation avec la famille ACP), mais il opérationnalise le champ précis dans Merchant Center. La conséquence pour un consultant SEO e-commerce est directe : la question SEO « comment mon produit se classe dans une SERP shopping » reste valide mais s'accompagne d'une question distincte, « mon produit est-il déclaré éligible à une transaction agentique ». Les deux ne demandent pas la même infrastructure de catalogue.

**Verbatim.** Tabeling écrit : « The future of search isn't just about getting found. It's about getting bought. »

**Limite.** L'article est une lecture d'analyste (Further est une agence SEO) et non un fait produit inédit. Le champ `native_commerce` a été annoncé au moment du lancement UCP à Google I/O 2026 mais aucune mesure publique d'adoption par les catalogues Merchant Center n'est disponible. La performance transactionnelle mesurée pour un produit éligible vs non-éligible n'est pas publiée par Google.

**Doctrine.** Le concept [[agentic-search]] gagne un critère d'éligibilité opérationnel dans un outil déjà existant (Merchant Center), au lieu d'une infrastructure séparée. Cette continuité avec l'outillage SEO existant est notable et distingue UCP côté Google de l'infrastructure ACP côté OpenAI, qui a bâti une famille de protocoles séparés.

### Brève 3 · Business SEO. Shopify ajoute un tableau de bord natif pour tracer les ventes provenant des canaux d'achat IA côté marchand

L'enquête Modern Retail du 30 juin 2026 cite un tableau de bord ajouté par Shopify pour permettre aux marchands de suivre les ventes provenant des canaux d'achat IA. Anna Hensel écrit : « Shopify has added a dashboard for merchants to track sales from AI shopping channels ».

**Contexte.** Le fait s'inscrit dans une séquence documentée dans les éditions précédentes : Shopify a été partenaire du lancement UCP côté Google I/O 2026 (30 mai), partenaire de ChatGPT Instant Checkout côté OpenAI ACP (Etsy et Shopify cités dans la brève B2 du 12 juillet v1), et acteur cité comme référence du commerce agentique dans les analyses SEO.

**Ce que ce tableau de bord change.** Le suivi par canal générique quitte l'outil vendeur pour devenir un composant natif de la plateforme e-commerce que la marque utilise déjà quotidiennement. Le marchand n'a pas besoin d'exporter ses données vers un outil tiers pour distinguer une vente provenant d'un panier ChatGPT ou Gemini d'une vente provenant d'une visite Google organique classique. C'est un mouvement de la couche vendeur (rapport) vers la couche opérateur (tableau de bord intégré à la stack existante).

**Limite.** L'article de Modern Retail cite le tableau de bord sans lier de source primaire Shopify (blog, changelog, page produit). Aucune capture ni verbatim Shopify direct n'apparaît dans l'article. Le champ précis mesuré (canal d'origine, panier via UCP, panier via ACP, panier via Perplexity Shopping) et la fenêtre d'attribution ne sont pas décrits.

**Recoupement.** Shopify a publié en 2025 une extension pour tracer les ventes provenant des chatbots IA (référence secondaire du même mouvement), mais le tableau de bord natif décrit par Modern Retail semble être un ajout distinct plus récent. Sans lien primaire Shopify, la mesure exacte de ce qui est nouveau reste imprécise.

**Doctrine.** Ce point renforce l'analyse de l'info du jour : les plateformes e-commerce internalisent la mesure des ventes IA, ce qui aligne la donnée disponible chez le marchand avec les métriques Kasper (Brand Inclusion Rate) et Mariah (mentions agrégées). Un consultant SEO/GEO qui audite un client Shopify peut désormais croiser trois mesures : le taux d'inclusion dans les moteurs (Kasper ou équivalent maison), la traçabilité de la vente réelle (dashboard Shopify natif), et l'attribution auto-déclarée acheteur (post-purchase survey). La convergence de ces trois mesures donne un ROI mesurable là où les outils vendeurs analystes seuls ne descendaient pas jusqu'à la vente.

**Prédiction vérifiable datée.**
- **P-2026-07-13-5** (échéance 30 juin 2027) : d'ici fin juin 2027, une étude publique agrégée (Adobe Analytics, Salesforce, ou un vendor e-commerce nommé) publie une distribution des ventes par canal d'origine IA sur un échantillon d'au moins 100 marchands Shopify utilisant le tableau de bord natif. Résolution positive : rapport nommé avec méthodologie publique. Résolution négative : silence prolongé sur les données agrégées.

---

*Édition Algorithme du 13 juillet 2026. Draft SyntheticBrain, non publié.*
