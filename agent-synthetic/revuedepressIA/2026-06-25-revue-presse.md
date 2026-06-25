# Algorithme : édition du 25 juin 2026

## L'essentiel en 4 points

- Similarweb publie le 21 juin 2026 « The Downstream Impact of AI Visibility », première mesure par clickstream desktop US des suites d'une recommandation ChatGPT : 2,5 fois plus de visites du site recommandé en 7 jours, 55,9 pct du trafic downstream qui arrive via recherche brandée et non par clic direct depuis ChatGPT, et un engagement moyen de 12,0 pages vues / 11,8 minutes contre 6,5 pages / 5,6 minutes pour les visiteurs non influencés par l'IA.
- Cette mesure ouvre une 4e dimension dans la fiche de doctrine [[concepts/metriques-visibilite-geo]] : jusqu'ici l'apparition, la position dans la réponse et les sous-métriques LLM-as-judge mesuraient la visibilité dans la réponse IA elle-même. L'étude ajoute l'effet downstream sur le site, et indique qu'une recommandation IA prise sans visite consécutive n'épuise pas la mesure de visibilité.
- Pinterest a publié le 17 juin 2026 l'app expérimentale « Ask Pinterest » et le Pinterest MCP avec partenaires alpha PMG, Pacvue, Dentsu, Havas, Innovid by Mediaocean et Jump450 (Omnicom). C'est la 1re plateforme de découverte produit IA-native distincte de la boîte de recherche principale annoncée pendant la séquence Cannes Lions 2026.
- Cannes Lions 2026, Day 3 du 24 juin : restitution par Adweek d'une tribune partagée sur la LinkedIn Rooftop avec Jessica Jensen (CMO LinkedIn), Colin Fleming (CMO OpenAI), Shiv Singh (CEO Savvy Matters), Lorraine Twohill (CMO Google) et Carla Hassan (CMO JPMorgan Chase). C'est la première session publique connue où CMO Google et représentants OpenAI partagent la même tribune sur la découverte par les modèles. Le contenu effectif des prises de parole reste partiellement non restitué à l'heure d'écriture.

---

## Info du jour

**Pilier de l'édition : GEO (Generative Engine Optimization).**

### Similarweb met un chiffre sur ce qui se passe après une recommandation ChatGPT, et c'est plus que la citation

Similarweb a publié le 21 juin 2026 le rapport « The Downstream Impact of AI Visibility », rapport ensuite repris par [Search Engine Journal](https://www.searchenginejournal.com/ai-recommended-brands-saw-2-5x-more-site-visits-similarweb/580241/) le 23 juin et par [Search Engine Land](https://searchengineland.com/chatgpt-recommendations-brand-website-visits-study-480989) le 24 juin sous la plume de Danny Goodwin, ainsi que par [ppc.land](https://ppc.land/your-analytics-are-lying-similarweb-traces-ai-recommendations-to-real-traffic/). Source primaire : le [rapport Similarweb](https://www.similarweb.com/corp/reports/the-downstream-impact-of-ai-visibilty/).

C'est, à notre connaissance, la première mesure publique de l'effet downstream d'une recommandation par un moteur génératif, construite sur un panel clickstream desktop US opt-in, et non sur de la modélisation ou du déclaratif annonceur.

**Le protocole.** Similarweb a suivi des utilisateurs ayant reçu une recommandation de marque dans ChatGPT, sur juillet à décembre 2025, dans trois verticales : Finance, Voyage, Beauté. Chaque verticale a une paire concurrente directe : American Express vs Capital One (Finance), Skyscanner vs Kayak (Voyage), Sephora vs Ulta (Beauté). Les utilisateurs ayant visité la marque dans les 4 semaines précédentes ou ayant nommé la marque dans leur prompt ont été exclus, pour isoler l'effet de la recommandation. Un volet d'enquête déclarative a été ajouté en janvier 2026 pour qualifier les étapes du parcours.

**Les chiffres centraux.** Les marques recommandées par ChatGPT ont reçu 2,5 fois plus de visites du site dans les 7 jours suivant la recommandation, comparé à leur concurrent direct (ratio sur la fenêtre de mesure, et non sur les visites absolues du concurrent isolément). 55,9 pct de ce trafic downstream est arrivé via recherche brandée, c'est-à-dire que l'utilisateur a retapé le nom de la marque dans un moteur classique après l'avoir vu dans la réponse de ChatGPT, et non par clic direct depuis l'interface ChatGPT. Les visiteurs influencés par l'IA ont consulté 12,0 pages en moyenne et passé 11,8 minutes sur le site, contre 6,5 pages et 5,6 minutes pour les visiteurs non influencés.

**Les chiffres par secteur, sur le taux de visite consécutif à la recommandation.** En Finance, American Express a été visité par 7,2 pct des utilisateurs ayant reçu une recommandation IA, vs 3,1 pct pour Capital One. En Voyage, Skyscanner 9,5 pct vs Kayak 7,6 pct. En Beauté, Sephora 7,9 pct vs Ulta 3,3 pct. Toujours selon [Search Engine Land](https://searchengineland.com/chatgpt-recommendations-brand-website-visits-study-480989).

**L'angle parcours.** Similarweb a aussi mesuré, par étape du parcours d'achat déclaré, quel outil est jugé le plus utile par l'utilisateur. Au stade « découverte / premières idées », 35,0 pct des sondés citent un outil IA, contre 13,6 pct pour les moteurs de recherche classiques. Au stade « recherche / comparaison », 30,0 pct IA vs 20,0 pct moteurs classiques. Au stade « trouver où acheter / meilleur prix », l'écart se resserre : 24,3 pct IA vs 22,1 pct moteurs classiques. Soit une présence IA forte à l'amont du parcours, et un rééquilibrage relatif des moteurs classiques à l'aval.

**Ce que ça déplace côté doctrine.** La fiche [[concepts/metriques-visibilite-geo]] définit trois dimensions mesurables de la visibilité dans une réponse générative : l'apparition d'une source dans la réponse (`Imp_wc`), la position de la phrase qui cite (`Imp_pos`), et la sous-évaluation par LLM-as-judge sur 7 critères. Ces trois dimensions répondent à la question : « est-on cité, et comment ». Aucune ne mesure ce qui se passe après. L'étude Similarweb ajoute une 4e dimension : l'effet downstream sur le trafic et l'engagement. Cette dimension demande un panel clickstream pour être mesurée correctement, donc pas de réplication possible par un outil SEO standard depuis un export GSC. Implication pratique : pour un site donné, être cité dans une réponse IA n'épuise pas la question de la visibilité. La conversion d'une mention IA en visite, en recherche brandée et en lecture longue est une variable indépendante, qu'il faut suivre séparément. C'est une recommandation d'ajout de section à la fiche, à valider en revue hebdo.

**Ce que la mesure ne dit pas, et les biais à signaler.** Le panel est desktop US uniquement : mobile et hors États-Unis hors mesure. La fenêtre est de juillet à décembre 2025, donc antérieure à la rebascule de Google sur Gemini 3.5 Flash en AI Mode I/O 2026, qui peut avoir modifié la dynamique downstream sur les requêtes Google. Trois verticales seulement, donc pas de généralisation à l'industrie entière (par exemple, B2B SaaS, e-commerce non-luxe ou santé non couverts). Similarweb est commercialement intéressé par la mesure de la visibilité IA puisqu'il vend le 2026 GenAI Brand Visibility Index et un produit de tracking AI visibility ; le rapport n'a pas d'évaluation indépendante. Il faut traiter les chiffres comme une 1re mesure crédible, à reproduire par un cabinet neutre ou un autre panel (Chartbeat, Nielsen, Datos, Comscore) avant d'en faire un standard.

**Verdict.** L'étude est solide sur l'opérationnel : panel réel, exclusion des biais de proximité de marque, paire concurrente par verticale, sources primaires citées. Les ordres de grandeur (2,5x visites, 12 pages, 11,8 minutes) sont à retenir comme premier point de référence pour la dimension downstream de la visibilité IA. Le confidence reste medium à high tant qu'une 2e mesure indépendante hors panel Similarweb ne sort pas.

**Prédiction associée.** Si la dimension downstream se stabilise au niveau de cette mesure, alors la conversation « être cité dans une réponse IA » va devenir secondaire devant « être visité après avoir été cité ». Concrètement, on prédit que d'ici fin 2026, au moins un cabinet de mesure indépendant de Similarweb (Chartbeat, Datos, Nielsen, Comscore, ou équivalent) publiera une étude reproduisant l'effet ratio 2x à 3x sur les visites consécutives à une recommandation IA, sur un panel hors US ou hors desktop. À défaut, on traitera la mesure Similarweb comme un signal fort mais non stabilisé.

---

## Brèves

### B1. Recherche agentique : Pinterest publie l'app « Ask Pinterest » et le Pinterest MCP avec 6 partenaires alpha de la pub agentique

Pinterest a publié le 17 juin 2026 sur son [Newsroom officiel](https://newsroom.pinterest.com/news/cannes-2026/) deux briques distinctes : une application expérimentale « Ask Pinterest » et un serveur MCP (Model Context Protocol).

Ask Pinterest est une app autonome (web mobile et desktop, accès limité, US uniquement à date) accessible à `ask.pinterest.com`, distincte de l'app principale Pinterest. Elle vise les décisions de découverte produit complexes et multi-étapes (planification d'un dîner sur un budget, choix d'un cadeau personnalisé, ameublement progressif d'une pièce). Elle utilise le Taste Graph et les signaux propriétaires de Pinterest (goûts, intentions, préférences) pour générer les recommandations conversationnelles, et conserve le contexte d'une session à l'autre, complété par les boards et pins sauvegardés de l'utilisateur. Le rationnel revendiqué est de tester un mode de découverte conversationnelle sans toucher au produit principal. Détails repris par [TechCrunch](https://techcrunch.com/2026/06/17/pinterest-launches-an-experimental-ai-shopping-app-called-ask-pinterest/) et [Retail Dive](https://www.retaildive.com/news/pinterest-introduces-experimental-ai-app-ask-pinterest/823254/).

Pinterest MCP est une infrastructure de protocole agent côté annonceur, qui donne aux copilotes et outils agentiques d'agences un accès sécurisé à des données campagne, à des analytics et à des insights mots-clés ancrés dans les signaux propriétaires Pinterest. Les partenaires alpha annoncés sont PMG, Pacvue, Dentsu, Havas, Innovid by Mediaocean et Jump450 (Omnicom). Pinterest a aussi annoncé un Business Assistant et un nouveau modèle créatif Performance+ revendiquant un gain de 7,5 pct sur le volume de clics en test. Pinterest tient le « Manifestival » au Carlton Beach Club pendant Cannes Lions 2026. Couverture indépendante par [The AI Insider](https://theaiinsider.tech/2026/06/18/pinterest-releases-ask-pinterest-app-and-mcp-tools-as-ai-reshapes-product-discovery/) et [Digital Applied](https://www.digitalapplied.com/blog/advertising-mcp-servers-pinterest-microsoft-2026-guide).

Lecture. Ask Pinterest est la 1re plateforme de découverte produit IA-native distincte de la boîte de recherche principale annoncée pendant la séquence Cannes Lions 2026, avec un protocole d'orchestration explicite côté annonceur. Conjuguée à Microsoft Advertising MCP (17 juin), Shopify Catalog API (17 juin), Adobe CX skills (22 juin) et Snap MCP (19 juin), le pattern qui se dessine est celui d'un connecteur MCP côté chaque grande plateforme média ou commerce, en quelques semaines, sur la fenêtre du festival. La question business pour un consultant SEO/GEO est : laquelle de ces 5 plateformes va faire passer son MCP du stade alpha-partenaire à une mesure d'usage publique et chiffrée. Sans métrique d'usage publique, le MCP reste une annonce de protocole, pas une couche d'orchestration adoptée.

### B2. Business SEO : Anthropic transforme « ad-free Claude » en posture commerciale, et Cannes Lions la confirme côté craft

Anthropic a maintenu en 2026 le positionnement « ad-free » pour Claude, refusé publiquement le modèle publicitaire intégré qui structure la stratégie OpenAI Cannes, et capitalisé dessus côté marque. La société a diffusé en février 2026 une publicité Super Bowl LX intitulée « Time and a Place » avec le slogan « Ads are coming to AI. But not to Claude ». Selon la couverture de [Ad Age](https://adage.com/events-awards/cannes-lions/aa-ai-openai-anthropic-microsoft-brand-usage-2026/) et [Adweek](https://www.adweek.com/creativity/cannes-lions-2026-gallery-day-3/), Anthropic revendique un gain de 11 pct d'utilisateurs actifs quotidiens dans les jours suivant le passage de l'annonce : chiffre revendiqué Anthropic non audité indépendamment, à traiter comme déclaratif.

À Cannes Lions 2026, la campagne « Time and a Place » a été pré-sélectionnée en short-list dans la catégorie Film Craft, l'une des rares pré-sélections d'une société d'IA dans une catégorie habituellement dominée par les agences de création. Couverture [The Drum](https://www.thedrum.com/news/cannes-lions-contenders-anthropic-the-ordinary-icelandair-and-life360-top-predictions) et bilan [Ad Age](https://adage.com/events-awards/cannes-lions/aa-ai-openai-anthropic-microsoft-brand-usage-2026/).

Lecture. C'est la première fois qu'un acteur de l'IA générative tire un bénéfice de marque mesuré, et une reconnaissance craft, du refus explicite du modèle publicitaire. Cela ouvre une polarisation business du marché des assistants : modèle pub-financé (ChatGPT, AI Mode, Gemini) vs modèle abonnement-pur (Claude). Pour un consultant SEO/GEO, la conséquence est qu'on ne peut plus parler « du marché des assistants » comme un bloc unifié de surfaces. Selon que l'utilisateur cible se trouve sur Claude (ad-free, payant) ou ChatGPT (mixte), la nature du « être cité » diffère : sur Claude, pas de zone sponsorisée concurrente, donc citation organique = pleine. Sur ChatGPT en revanche, les formats sponsorisés introduits depuis février 2026 et étendus depuis (cf. [debut publicitaire OpenAI à Cannes Lions 2026](https://adage.com/events-awards/cannes-lions/aa-openai-chatgpt-ads-business-david-dugan/)) reconfigurent l'espace de citation organique. Cela demande une mesure de visibilité par plateforme et non par moyenne agrégée.

### B3. Actualité SEO : restitution Adweek du Day 3 de Cannes Lions, tribune partagée Google-OpenAI-LinkedIn-JPMorgan sur la découverte par les modèles

Adweek a publié le 24 juin 2026 sa [galerie Day 3 de Cannes Lions 2026](https://www.adweek.com/creativity/cannes-lions-2026-gallery-day-3/) qui restitue un événement off-site, sur la LinkedIn Rooftop, intitulé « Winning the AI Discover Era », avec un panel composé de Jessica Jensen (CMO LinkedIn), Colin Fleming (CMO OpenAI), Shiv Singh (CEO Savvy Matters), Lorraine Twohill (CMO Google) et Carla Hassan (CMO JPMorgan Chase).

Distinction à signaler. Cet événement off-site Adweek/LinkedIn est lié, mais distinct, de la session officielle [« Winning the AI Discovery Era: Marketing To Minds and Machines »](https://www.canneslions.com/festival/programme/winning-the-ai-discovery-era-marketing-to-minds-and-machines-e1-75660) inscrite au programme officiel Cannes Lions, prévue le 24 juin à 11h30 au Carlton Hotel, avec Denise Dresser (CRO OpenAI), Lorraine Twohill (CMO Google) et Carla Hassan (CMO JPMorgan Chase). Les deux thèmes se recoupent ; les deux casts se chevauchent partiellement. À l'heure d'écriture, la presse a restitué la présence et le casting de la tribune off-site, sans restituer les quotes verbatim des participants. Le contenu effectif des prises de parole reste donc partiellement non documenté.

Ce qui est neuf documentable, à ce stade. La présence publique conjointe d'un CMO Google et d'un CMO ou CRO OpenAI, sur la même tribune, sur le sujet de la découverte par les modèles, est une première à notre connaissance. Cette tribune partagée est l'illustration la plus visible de la transition décrite dans la brève B2 : Google et OpenAI ne sont plus dans deux univers parallèles côté marché publicitaire et marché de la découverte, mais sur une zone de coexistence concurrentielle. Voir aussi la couverture [PPC Land](https://ppc.land/ai-advertising-leads-cannes-lions-2026-as-openai-courts-the-croisette/) et [AdExchanger](https://www.adexchanger.com/ai/at-its-first-ever-cannes-openai-says-we-are-clearly-in-the-advertising-business-now/).

Pour un consultant SEO/GEO, l'implication pratique est limitée en l'absence des quotes. Le fait que la tribune ait eu lieu confirme un signal de marché ; le contenu attendra la restitution presse complète, attendue dans les 24 à 72 heures.

---

## Connexions doctrine

- [[concepts/metriques-visibilite-geo]] : l'étude Similarweb ouvre la 4e dimension downstream non couverte par la fiche actuelle (apparition, position, sous-métriques LLM-as-judge). Proposition de mise à jour à statuer en revue hebdo.
- [[concepts/agentic-search]] : Pinterest MCP + Snap MCP + Microsoft Advertising MCP + Shopify Catalog API + Adobe CX skills MCP confirment la couche d'orchestration agentique côté annonceur sur 5 plateformes en 5 semaines, sur la fenêtre Cannes Lions 2026.
- [[concepts/tabou-visibilite]] : la disjonction « citation IA » vs « visite consécutive » mesurée par Similarweb rappelle qu'« être cité » et « être lu » ne sont pas le même indicateur, et que parler de « visibilité » sans préciser laquelle ouvre la confusion.

---

## Prédictions ouvertes ajoutées 2026-06-25

- **P-2026-06-25-1** : d'ici fin 2026, au moins un cabinet de mesure indépendant de Similarweb (Chartbeat, Datos, Nielsen, Comscore, ou équivalent) publie une étude reproduisant un ratio de 2x à 3x sur les visites consécutives à une recommandation IA, sur un panel hors US ou hors desktop. Si non, la mesure Similarweb reste un signal fort mais non stabilisé.
- **P-2026-06-25-2** : d'ici le 31 mars 2027, au moins une des 5 plateformes MCP côté annonceur (Pinterest, Microsoft Advertising, Shopify Catalog, Adobe CX, Snap) publie une métrique d'usage publique chiffrant le volume de campagnes orchestrées via son MCP. Si non, le pattern MCP reste annonce de protocole, pas couche d'orchestration adoptée mesurable.

---

## Sources consultées

### Sources primaires
- [Similarweb : The Downstream Impact of AI Visibility](https://www.similarweb.com/corp/reports/the-downstream-impact-of-ai-visibilty/) (rapport, 21 juin 2026)
- [Pinterest Newsroom : Cannes 2026 AI tools](https://newsroom.pinterest.com/news/cannes-2026/) (17 juin 2026)
- [Cannes Lions : Winning the AI Discovery Era programme officiel](https://www.canneslions.com/festival/programme/winning-the-ai-discovery-era-marketing-to-minds-and-machines-e1-75660)

### Sources secondaires recoupées
- [Search Engine Journal : AI-Recommended Brands Saw 2.5x More Site Visits](https://www.searchenginejournal.com/ai-recommended-brands-saw-2-5x-more-site-visits-similarweb/580241/) (23 juin)
- [Search Engine Land : ChatGPT recommendations drive more brand website visits: Study](https://searchengineland.com/chatgpt-recommendations-brand-website-visits-study-480989) (Danny Goodwin, 24 juin)
- [ppc.land : Your analytics are lying: Similarweb traces AI recommendations to real traffic](https://ppc.land/your-analytics-are-lying-similarweb-traces-ai-recommendations-to-real-traffic/)
- [TechCrunch : Pinterest launches an experimental AI shopping app called 'Ask Pinterest'](https://techcrunch.com/2026/06/17/pinterest-launches-an-experimental-ai-shopping-app-called-ask-pinterest/)
- [Retail Dive : Pinterest introduces experimental AI app](https://www.retaildive.com/news/pinterest-introduces-experimental-ai-app-ask-pinterest/823254/)
- [The AI Insider : Pinterest Releases Ask Pinterest app and MCP Tools](https://theaiinsider.tech/2026/06/18/pinterest-releases-ask-pinterest-app-and-mcp-tools-as-ai-reshapes-product-discovery/)
- [Digital Applied : Pinterest and Microsoft Launch Ad MCP Servers for AI](https://www.digitalapplied.com/blog/advertising-mcp-servers-pinterest-microsoft-2026-guide)
- [Ad Age : AI at Cannes 2026: OpenAI, Anthropic and brand attitudes](https://adage.com/events-awards/cannes-lions/aa-ai-openai-anthropic-microsoft-brand-usage-2026/)
- [Adweek : Cannes Lions 2026 Gallery Day 3](https://www.adweek.com/creativity/cannes-lions-2026-gallery-day-3/)
- [The Drum : Cannes Lions contenders: Anthropic, The Ordinary, Icelandair and Life360 top predictions](https://www.thedrum.com/news/cannes-lions-contenders-anthropic-the-ordinary-icelandair-and-life360-top-predictions)
- [PPC Land : AI advertising leads Cannes Lions 2026 as OpenAI courts the Croisette](https://ppc.land/ai-advertising-leads-cannes-lions-2026-as-openai-courts-the-croisette/)
- [AdExchanger : At Its First-Ever Cannes, OpenAI Says 'We Are Clearly In The Advertising Business Now'](https://www.adexchanger.com/ai/at-its-first-ever-cannes-openai-says-we-are-clearly-in-the-advertising-business-now/)
- [Ad Age : OpenAI reveals more of its ChatGPT ads strategy at Cannes (Dugan)](https://adage.com/events-awards/cannes-lions/aa-openai-chatgpt-ads-business-david-dugan/)

---

**Voix.** Édition rédigée dans la voix propre de SyntheticBrain (vouvoiement, analyse search/IA, aucun personnage), pas la voix de Tim. Zéro métaphore, aucune personnification d'entreprise, aucun vocabulaire emprunté. Voir [[memory/voix-synthetic]].

**Rien n'est envoyé.** Ce fichier est un draft.
