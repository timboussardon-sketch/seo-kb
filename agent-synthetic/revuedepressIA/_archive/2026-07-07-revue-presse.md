# Content Signals de Cloudflare : John Mueller (Google) déclare qu'aucun crawler ni LLM n'utilise la directive

> À retenir en 15 secondes
> - Sur un fil r/TechSEO début juillet 2026, John Mueller (Google) qualifie la directive `content-signal` proposée par Cloudflare pour robots.txt de directive « made up by a CDN » sans « aucun effet » sur les crawlers ou LLMs, ni pour Google ni pour un autre acteur qu'il connaisse.
> - Cloudflare avait lancé Content Signals le 24 septembre 2025 dans le robots.txt géré (3 signaux : `search`, `ai-input`, `ai-train`), et prévoit un durcissement le 15 septembre 2026 (blocage par défaut de `ai-train` et « Agent » sur les pages porteuses de publicité chez les nouveaux clients).
> - Dans son rapport « Content Independence Day » du 1er juillet 2026, Cloudflare mesure que 52 % des requêtes crawler sont désormais liées à l'entraînement IA, contre 22 % au printemps 2025.
> - Brève 1 : le passage de l'API Content for Shopping à l'API Merchant Center le 18 août 2026 réécrit les identifiants produits synchronisés via l'app Google & YouTube de Shopify (`Shopify_XX_...` → `Shopify_ZZ_...`), avec perte d'historique.
> - Brève 2 : Bing teste un panneau superposé de détail produit sur ses résultats shopping (prix, historique, revendeurs, produits liés).
> - Brève 3 : Google déploie plus largement le bloc « Further Exploration » en pied d'AI Overview, observé depuis début juillet 2026.

Pilier de cette édition : **GEO / search IA**. La directive Content Signals était présentée par Cloudflare comme la composante manquante d'un dispositif de contrôle du web pour les crawlers IA. La position publique de John Mueller la vide de sa portée opérationnelle côté grands moteurs et grands LLMs. C'est un point de contrôle GEO que les praticiens croyaient acquis, et qui ne l'est pas.

---

## Info du jour. Ce que Mueller dit exactement

Fin de semaine du 6 juillet 2026, un utilisateur du subreddit r/TechSEO ouvre une discussion intitulée « Testing whether Content-Signal headers and llms.txt actually help with Person entity disambiguation ». La question est concrète : cette personne partage son nom avec deux autres entités plus visibles, elle cherche à savoir si activer les signaux Cloudflare et publier un fichier `llms-author.txt` améliorerait sa désambiguïsation dans les réponses générées par les LLMs. John Mueller (Google Search Central) répond publiquement sur le fil.

Trois affirmations distinctes ressortent de sa réponse, reprises par plusieurs éditeurs SEO en parallèle :

1. **Sur `llms.txt` et `llms-author.txt`.** Google ne les utilise pas. Mueller ajoute qu'il n'a connaissance d'aucun autre crawler ou LLM qui aurait confirmé les utiliser, en dehors d'outils SEO qui se contentent de vérifier la présence du fichier.
2. **Sur la directive `content-signal` de Cloudflare.** Elle est décrite comme « made up by a CDN » (littéralement, inventée par un CDN) et sans « aucun effet, pour aucun crawler ou LLM ».
3. **Sur l'ajout de ces éléments à un robots.txt.** Aucun bénéfice attendu, et une dette de maintenance ajoutée. « Just adds bloat and future maintenance to your robots.txt file. »

Recoupement disponible sur au moins quatre publications indépendantes : [Search Engine Journal, Roger Montti, 6 juillet](https://www.searchenginejournal.com/google-answers-question-about-llms-author-txt-for-seo/581547/), [Search Engine Roundtable, Barry Schwartz](https://www.seroundtable.com/google-cloudflare-content-signals-41631.html), [Optimixed](https://www.optimixed.com/google-says-cloudflare-content-signals-robots-txt-directive-has-no-effects-whatsoever/) et [Digital Phablet](https://digitalphablet.com/digital-marketing/google-states-cloudflares-robots-txt-signals-have-no-impact/). Les quatre reprises citent le même fil Reddit ; aucune ne rapporte de contradiction.

### Ce que Cloudflare avait publié, et sur quel calendrier

Content Signals a été annoncé par Cloudflare le [24 septembre 2025](https://www.cloudflare.com/press/press-releases/2025/cloudflare-gives-creators-new-tool-to-control-use-of-their-content/) et documenté sur le [blog Cloudflare](https://blog.cloudflare.com/content-signals-policy/). La proposition consiste à ajouter au `robots.txt` un bloc de préférences machine-readable pour trois usages du contenu : `search` (indexation classique renvoyant vers la page source), `ai-input` (utilisation en réponse générative directe, type AI Overview ou Perplexity) et `ai-train` (entraînement de modèles). Trois valeurs possibles par signal : `yes`, `no`, ou pas de signal.

Cloudflare a ajouté ces signaux par défaut aux robots.txt gérés côté client CDN (managed robots.txt), sans changer la posture réelle du client sur les crawlers (autorisation ou blocage). Cloudflare a annoncé le 1er juillet 2026, dans son [rapport d'anniversaire « Content Independence Day »](https://blog.cloudflare.com/agentic-internet-bot-report/), qu'à partir du **15 septembre 2026**, pour les nouveaux domaines qui rejoignent la plate-forme, les catégories « Training » et « Agent » seraient bloquées **par défaut** sur les pages porteuses de publicité, tandis que « Search » resterait autorisé par défaut.

C'est cette architecture que Mueller décrit comme sans effet côté moteurs. Ce que Cloudflare inscrit au niveau du fichier n'oblige aucun crawler tant que le crawler ne s'engage pas à respecter la sémantique de la directive. Aucun des grands crawlers de recherche générale (Googlebot, Google-Extended, Bingbot) ni des principaux crawlers IA (GPTBot d'OpenAI, ClaudeBot d'Anthropic, PerplexityBot) n'a publiquement pris cet engagement, et Cloudflare n'a publié aucun tableau d'adhésion.

### Le contexte de mesure : ce que le trafic crawler dit, indépendamment de Content Signals

Cloudflare publie de son côté des mesures d'usage crawler qui, elles, ne sont pas contestées par Google : dans le [rapport « Content Independence Day » du 1er juillet 2026](https://blog.cloudflare.com/agentic-internet-bot-report/), 52 % des requêtes crawler observées sur le réseau Cloudflare sont maintenant liées à l'entraînement IA, contre 22 % au printemps 2025. Plus de 50 % du trafic web mesuré est non humain. Cloudflare rapporte que dans certaines catégories très crawlées, le trafic humain a reculé jusqu'à 40 % en moins d'un an.

La mesure d'usage est solide. C'est le mécanisme de contrôle sémantique par-dessus qui est vide. Cloudflare peut afficher qu'un site « préfère » ne pas être utilisé pour l'entraînement, cette préférence n'a d'effet sur un crawler que si celui-ci a intégré une logique de lecture et de respect de la directive. Aucun grand acteur n'a signalé publiquement cette intégration au 7 juillet 2026, et Mueller confirme que Google ne l'a pas fait.

### Conséquences pratiques pour un responsable SEO ou GEO

Trois lectures immédiates.

D'abord, sur le robots.txt : ajouter les blocs Content Signals à un fichier `robots.txt` géré directement n'apporte pas de garantie de non-usage par les crawlers IA. Le contrôle effectivement respecté reste `User-agent` + `Allow`/`Disallow`, ou la vérification IP côté serveur, ou un contrôle d'accès applicatif. Un client Cloudflare dont le managed robots.txt a été enrichi de ces signaux par défaut, sans consigne active de blocage sur le user-agent des crawlers concernés, laisse ses pages accessibles. La directive existe comme déclaration, pas comme filtre.

Ensuite, sur `llms.txt` et `llms-author.txt` : la mesure Ahrefs sur 137 210 domaines publiée le 15 juin 2026 (voir édition [SyntheticBrain du 17 juin 2026 v2](../revuedepressIA/2026-06-17-revue-presse-v2.md)) indiquait déjà 28 % d'adoption mais 97 % des fichiers `llms.txt` recevant zéro requête bot IA en mai 2026. La position publique de Mueller consolide ce constat au niveau des standards émergents : ni Google, ni un autre crawler qui l'aurait publié, ne s'appuie sur ces fichiers. Un `llms-author.txt` publié pour la désambiguïsation d'entité personne n'aide pas côté grands moteurs et grands LLMs sur ce périmètre. Les leviers documentés pour l'entité personne restent les entités reconnues (Wikipedia, Wikidata, LinkedIn, Crunchbase), une page « à propos » schema `Person`, les mentions dans des sources tierces sur la personne et son activité.

Enfin, sur la doctrine GEO : la [[concepts/structural-information-geo|structural information GEO]] rappelle que les champs structurels reconnus par les moteurs (title, meta, headings, schema) restent le levier retrieval le plus efficace. La séquence Content Signals + `llms.txt` + `llms-author.txt` proposait d'ajouter une couche structurelle **au niveau du fichier robots.txt et de fichiers frères**, distincte du schéma page-level. Cette couche reste, pour l'instant, une déclaration sans reconnaissance par les moteurs. Le contrôle réellement respecté côté GEO reste au niveau serveur (blocage user-agent, verification, WAF) et au niveau structurel de la page (schema, Person, Organization, sameAs vers Wikidata et LinkedIn).

Le fait franchement neuf de cette édition : la position n'était pas explicite jusqu'à début juillet 2026. Elle l'est maintenant, sourcée à John Mueller sur une plate-forme publique.

### Prédictions ouvertes que ce fait complète

- **P-2026-05-30-4** (llms.txt non utilisé par Google, échéance 31 décembre 2026) : la déclaration Mueller renforce le maintien probable de cette prédiction à statut ouvert avec tendance « verified » à l'échéance.
- **P-2026-07-02-v2-3** (au moins un crawler mainstream publie une déclaration technique explicite de séparation search/agent/training au niveau user-agent ou protocole en réponse au default Cloudflare 15 septembre 2026, échéance 30 septembre 2026) : la déclaration Mueller ne constitue pas cette séparation, elle décrit l'absence d'engagement. La prédiction reste ouverte, avec un signal négatif ajouté.

### Nouvelle prédiction ouverte à partir de cette édition

- **P-2026-07-07-1** : d'ici le 15 décembre 2026, aucun des cinq grands crawlers (Googlebot / Google-Extended, Bingbot, GPTBot, ClaudeBot, PerplexityBot) ne publie un engagement documenté (blog éditeur, doc technique, changelog) à respecter la sémantique `search` / `ai-input` / `ai-train` du fichier robots.txt en tant que directive spécifique. Résolution positive : au moins un engagement documenté publié. Résolution négative : silence maintenu, Content Signals reste au stade de déclaration côté client sans exécution côté crawler.

---

## Brèves

### B1. Deadline 18 août 2026 : la migration de l'API Content for Shopping vers Merchant API réécrit les identifiants produits Shopify côté Google Merchant Center

Google achève le retrait de son ancienne API produits (Content API for Shopping) le **18 août 2026**, au profit de la Merchant API. L'application Google & YouTube maintenue par Shopify, qui synchronise les catalogues de plusieurs centaines de milliers de marchands vers Google Merchant Center, doit être réinstallée pour rester active après cette date. Effet mécanique de la réinstallation, documenté par plusieurs sources : l'identifiant produit passe du format `Shopify_XX_...` (où `XX` est le code marché : US, GB, AU, etc.) au format `Shopify_ZZ_...`.

Ce changement de clé casse la continuité côté Google. Google traite un identifiant modifié comme un produit nouveau : l'historique de performance associé au produit dans Google Merchant Center et dans les campagnes Performance Max ne se rattache plus à la nouvelle fiche. Le modèle publicitaire doit ré-apprendre. Côté visibilité organique dans les onglets Shopping et Discover, la fiche produit repart également sans historique de qualité de flux ni de signaux d'engagement.

Trois lectures utiles : [Search Engine Roundtable](https://www.seroundtable.com/google-youtube-shopify-app-sync-merchant-concerns-41627.html), le [Bidnamic explainer technique](https://www.bidnamic.com/resources/shopify-item-id-changes-google-merchant-centre) qui documente les stratégies de contournement (feed management tiers type Channable pour garder la main sur les IDs) et le [fil Shopify Community](https://community.shopify.com/t/google-youtube-app-product-id-sync-issue-sku-vs-shopify-zz-format/568811) où le problème avait déjà été observé sur certains marchés avant la deadline. La [documentation Google Merchant](https://support.google.com/merchants/answer/13693394?hl=en) couvre la sync.

Impact concentré sur les marchands Shopify utilisant l'app native Google & YouTube. Pour les marchands qui gèrent leur flux via un outil tiers (Channable, DataFeedWatch, GoDataFeed), les IDs restent stables. Un audit à faire d'ici la deadline pour tout consultant SEO/GEO qui accompagne un catalogue Shopify significatif : identifier le mode de sync, prévoir la fenêtre de bascule, et arbitrer entre réinstallation avec perte d'historique (rapide, moindre effort, réapprentissage) ou passage à un feed manager tiers (préserve les IDs, effort d'onboarding).

### B2. Bing teste un panneau de détail produit superposé sur ses résultats shopping

Microsoft Bing teste actuellement un panneau détail produit qui s'ouvre en surimpression au clic sur une fiche produit dans les résultats. Le panneau expose l'image, la description, la liste des revendeurs avec leurs prix, l'historique de prix, les produits liés. Le test est visible chez une partie des utilisateurs seulement, avec des différences selon le navigateur ([Search Engine Roundtable](https://www.seroundtable.com/bing-product-detail-overlay-41623.html), [Optimixed](https://www.optimixed.com/microsoft-bing-testing-new-product-detail-overlay-with-retailer-pricing-price-insights-more/)).

Google propose une expérience équivalente depuis plusieurs années. La lecture GEO pour un marchand qui optimise sa visibilité sur Bing Shopping : le panneau superposé isole le comparatif prix côté SERP, la sélection du revendeur se fait sans nouveau clic vers la page marchande. La position d'apparition dans le panneau (prix, disponibilité, notes) devient un critère de compétition indépendant du ranking sur la SERP elle-même. C'est une deuxième surface d'exposition sur laquelle mesurer, sur laquelle piloter les signaux de flux produit (prix, promo, disponibilité, images), et sur laquelle Bing n'a pas publié de métrique d'attribution comparable au CTR classique.

À suivre : le passage éventuel du test au déploiement général, et une éventuelle documentation Microsoft de ce que ce panneau surfacera exactement pour Bing Copilot Search.

### B3. Google élargit le bloc « Further Exploration » en pied d'AI Overview

Le bloc « Further Exploration », annoncé lors de Google I/O 2026 en mai comme l'une des cinq nouvelles façons d'explorer le web avec l'IA générative dans Search, est passé au déploiement observable début juillet 2026. Le bloc apparaît en pied d'AI Overview et propose des suggestions de sujets connexes ainsi que des liens vers des pages plus fouillées, avec une logique de continuation de recherche. Sources : [Search Engine Roundtable](https://www.seroundtable.com/google-further-exploration-41621.html) et le [Google Search I/O 2026 blog](https://blog.google/products-and-platforms/products/search/search-io-2026/) qui contenait l'annonce initiale.

Deux angles à surveiller côté GEO. D'abord la nature des URL suggérées : Google fait le choix de proposer, dans un bloc structurellement associé à la réponse générative, des destinations qui n'étaient pas nécessairement citées dans le corps de l'AI Overview. C'est une deuxième couche de visibilité, distincte de la citation dans la réponse, à mesurer et à cartographier. Ensuite l'effet sur le taux de clic sortant depuis un AI Overview : Google positionne « Further Exploration » comme une invitation à poursuivre la recherche. Si les praticiens observent que ce bloc génère effectivement du clic sortant supplémentaire, il devient un slot de visibilité GEO qui compte, à ajouter à la grille [[concepts/metriques-visibilite-geo|metriques-visibilite-geo]]. Aucune mesure d'impact CTR sur ce bloc n'a été publiée au 7 juillet 2026.

---

*Draft SyntheticBrain. Rien n'a été envoyé. Sources primaires reconstituées ci-dessus. Prochaine édition : à cadencer.*
