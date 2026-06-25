# Algorithme : édition du 25 juin 2026 (v2)

## L'essentiel en 4 points

- YouTube a annoncé pendant Cannes Lions 2026 quatre outils Gemini destinés à la planification média des agences : insights de tendances enrichis dans Google Ads Insights Finder, intégration du Brand Pulse Report dans Insights Finder, **API Content & Creator Insights ouverte aux partenaires**, et optimisation Gemini des campagnes Demand Gen. Couverture sur Google blog (source primaire), eMarketer (23 juin), BuzzinContent (24 juin) et Performance Marketing World.
- C'est la cinquième plateforme à publier une couche d'API côté annonceur en cinq semaines, après Pinterest MCP (17 juin), Shopify Catalog API (17 juin), Adobe CX skills MCP (22 juin) et TikTok Symphony Agent (24 juin). L'API YouTube résout partiellement la prédiction P-2026-06-24-2 (5e plateforme parmi X, YouTube, Quora annonçant un produit publicitaire ou une API native IA bâti sur un corpus propriétaire).
- OpenAI a annoncé le 24 juin par Denise Dresser (CRO) que le taux de rejet des publicités dans ChatGPT a baissé de 50 pct depuis le lancement de février 2026. La société présente ce ratio comme un indicateur indirect de pertinence ; la méthodologie de mesure du rejet n'est pas publiée et le chiffre est déclaratif.
- Google a lancé le 24 juin 2026 le **June 2026 spam update**, deuxième mise à jour spam de l'année après celle de mars 2026. Le rollout a été enregistré à 9h00 PT sur le Search Status Dashboard. Pas de nouvelle politique spam introduite : application des règles existantes au niveau global, toutes langues et toutes régions, durée estimée à quelques jours.

---

## Info du jour

**Pilier de l'édition : Recherche agentique.**

### YouTube publie sa couche de planification agentique à Cannes Lions 2026, cinquième plateforme en cinq semaines

YouTube a annoncé pendant la séquence Cannes Lions 2026 quatre outils s'appuyant sur Gemini, destinés aux marques, aux agences et aux planificateurs de campagnes vidéo. L'annonce est documentée sur le [blog Google produits ads & commerce](https://blog.google/products/ads-commerce/youtube-insights-tools-cannes-lions-2026/) (source primaire), reprise par [eMarketer](https://www.emarketer.com/content/google-expands-youtube-s-creator-marketing-tools-cannes-lions) le 23 juin, par [BuzzinContent](https://www.buzzincontent.com/news/youtube-unveils-gemini-powered-insights-tools-for-creator-led-campaigns-at-cannes-lions-2026-12067643) le 24 juin et par [Performance Marketing World](https://www.performancemarketingworld.com/article/1962640/cannes-lions-2026-google-unveils-new-gemini-powered-youtube-tools-amazon-retail-ad-service-hits-uk).

**Les quatre briques publiées.** Premièrement, des données de tendances enrichies dans Google Ads Insights Finder, limitées aux États-Unis à date, qui donnent une vue plus granulaire des contenus populaires sur YouTube. Deuxièmement, l'intégration des métriques du Brand Pulse Report dans Insights Finder, qui permet à une marque de regarder dans une seule interface sa présence payante et sa présence organique sur YouTube. Troisièmement, une nouvelle API Content & Creator Insights, présentée comme destinée aux agences pour la planification média, qui expose des informations sur les créateurs YouTube et leurs audiences. Quatrièmement, une intégration Gemini dans les campagnes Demand Gen sur YouTube, qui propose des recommandations créatives, par exemple sur les visuels les plus susceptibles d'améliorer la performance de la campagne. Le calendrier précis de mise à disposition par produit n'est pas affiché dans l'annonce ; Google emploie « new » pour les deux premières briques et « soon » pour l'optimisation Demand Gen.

**Lecture en tant que cinquième plateforme du même pattern Cannes 2026.** En cinq semaines, on observe la publication successive d'une couche d'API ou de protocole côté annonceur sur cinq plateformes de découverte ou de distribution dont le corpus est propriétaire : Pinterest MCP et Pinterest Business Assistant le 17 juin (graphe goûts/intentions), Shopify Catalog API le 17 juin (graphe produits), Adobe CX skills MCP le 22 juin (couche orchestration agence), TikTok Symphony Agent le 24 juin (corpus créateurs et performance), et YouTube Content & Creator Insights API à Cannes Lions 2026 (corpus créateurs et audiences vidéo). Le calendrier coïncide avec la fenêtre du festival Cannes Lions du 22 au 26 juin, ce qui est un fait de calendrier vérifiable et non un mouvement coordonné démontré entre les acteurs. La lecture utile est qu'il existe désormais cinq points d'accès distincts où une agence ou un copilote agentique peut interroger un corpus propriétaire pour la planification média, là où il n'en existait pratiquement aucun en mai 2026.

**Lien avec la prédiction P-2026-06-24-2.** La prédiction stipule qu'avant le 31 décembre 2026, une cinquième plateforme parmi X/Grok, YouTube ou Quora annoncera un produit publicitaire ou une API native IA bâti sur un corpus propriétaire. L'API Content & Creator Insights de YouTube qualifie au regard de ce libellé : elle est une API native, elle est bâtie sur le corpus propriétaire YouTube (créateurs + audiences), et son destinataire affiché est l'agence et le planificateur média. C'est une résolution partielle : il manque, pour résolution pleine, le calendrier précis et l'accès effectif au-delà du « partenaires » mentionné dans la communication. Statut suggéré : `resolved-partial`, à arbitrer en revue hebdo.

**Distinction par rapport aux MCP de Pinterest, Shopify, Adobe et TikTok.** Ce que publie YouTube n'est pas un serveur MCP standardisé. C'est une API native Google (au sens « endpoint REST documenté chez Google ») avec assistance Gemini intégrée pour l'analyse. Sur la même fenêtre Cannes 2026, Pinterest et Snap ont publié des serveurs MCP, Shopify une API Catalog, Adobe des skills MCP. Les piles sont architecturalement différentes : MCP est un protocole d'agent dont le contrat est documenté côté client, l'API YouTube est un service propriétaire dont la spécification reste Google. Le point commun est l'objet : exposer un corpus propriétaire à des systèmes externes capables de l'interroger en langage naturel ou via des structures, sans que l'utilisateur agence ou planificateur ait à passer par l'UI de la plateforme.

**Ce que la doctrine y trouve.** La fiche [[concepts/agentic-search]] décrit la couche d'orchestration agentique côté annonceur comme une zone d'ombre à formaliser. Les cinq publications de la fenêtre Cannes 2026 confirment que cette zone d'ombre n'est plus prospective : elle est en cours de structuration empirique, avec cinq architectures co-présentes et concurrentes (MCP standardisé chez Pinterest/Snap/Adobe, API Catalog spécifique chez Shopify, agent intégré chez TikTok, API native chez YouTube). C'est un fait d'observation à incorporer à la fiche en revue hebdo, en gardant à ce stade trois lectures alternatives ouvertes : (1) ces architectures convergeront sous MCP comme standard de facto ; (2) elles cohabiteront durablement par segment (commerce, créateurs, planification, orchestration) ; (3) le pattern Cannes 2026 est un effet calendaire éditorial qui se diluera à plat sans usage mesuré.

**Ce que la mesure ne dit pas, à ce jour.** Aucune des cinq plateformes n'a publié de métrique d'usage chiffrant le nombre de campagnes orchestrées via son API ou son MCP, le nombre d'agences actives, ou le volume de requêtes traitées. C'est la limite empirique structurante : tant qu'aucune plateforme ne publie de chiffre d'adoption, le pattern reste un cluster d'annonces de protocole, et non un état de marché installé. La prédiction P-2026-06-24-1 (avant le 31 mars 2027, au moins une plateforme parmi Pinterest MCP, Shopify Catalog, Reddit Community Intelligence, TikTok Symphony Agent ou Alexa+ Agentic Ads publie une métrique d'usage publique) reste ouverte et s'étend désormais à YouTube Content & Creator Insights API et au cluster Adobe CX skills MCP.

**Verdict.** L'annonce YouTube est solide sur le plan factuel : source primaire publiée par Google, reprises indépendantes par eMarketer, BuzzinContent et Performance Marketing World, identification des quatre briques distinctes. Elle est limitée sur le plan opérationnel : pas de date d'accès affichée pour l'API Content & Creator Insights, pas de partenaires nommés, pas de métrique d'usage cible. La lecture proposée (5e couche API agentique en 5 semaines) est défendable comme observation factuelle. Comme lecture stratégique, elle reste à confirmer par une mesure d'usage, faute de quoi le pattern reste descriptif.

---

## Brèves

### B1. Business SEO : OpenAI rapporte une baisse de 50 pct des rejets d'annonces ChatGPT depuis février 2026

Anu Adegbola rapporte sur [Search Engine Land](https://searchengineland.com/openai-says-chatgpt-ad-dismissals-have-dropped-50-as-relevance-improves-480991) le 24 juin 2026 que Denise Dresser, directrice des revenus d'OpenAI, a déclaré pendant la séquence Cannes Lions 2026 que le taux de rejet des publicités au sein de ChatGPT a baissé de 50 pct depuis le lancement du programme publicitaire en février 2026. OpenAI présente ce taux de rejet comme un indicateur indirect de la pertinence des annonces servies. La déclaration verbatim attribuée à Dresser est : « *This form factor is about usefulness. That's great for the consumer, great for the user.* »

**Caveats explicites à signaler.** Premièrement, la méthodologie de mesure du rejet n'est pas publiée : on ne sait pas si la mesure compte un clic explicite sur un bouton « dismiss », un swipe, un signalement, ou un autre signal d'interaction. Deuxièmement, le chiffre est purement déclaratif d'OpenAI, sans audit indépendant ni reprise par un cabinet de mesure (Sensor Tower, Datos, Comscore). Troisièmement, l'évolution du taux de rejet ne renseigne pas directement sur la pertinence pour l'utilisateur : un taux plus bas peut signifier des annonces mieux ciblées, mais aussi un placement plus discret, une habituation des utilisateurs, ou un changement de surface d'affichage qui rend le rejet plus difficile.

**Lecture pour la polarisation du marché des assistants.** L'édition de ce matin (v1) ouvrait pour la première fois le pilier Business SEO sur la polarisation du marché des assistants entre modèle pub-financé (OpenAI, AI Mode, Gemini consumer) et modèle abonnement-pur (Anthropic Claude). La donnée du 24 juin apporte une mesure indirecte côté pub-financé : ChatGPT ne paye pas une dégradation d'expérience massive du fait du modèle publicitaire intégré, à mesurer côté OpenAI. Cette donnée est complémentaire de la donnée du Super Bowl revendiquée par Anthropic (+11 pct de DAU revendiqué après « Time and a Place ») : les deux chiffres restent déclaratifs et non audités, et les deux marchés se mesurent séparément. La polarisation reste un fait d'observation structurel ; les chiffres internes qui la défendent côté chaque camp restent à confirmer par tiers neutre.

**Implication pour un consultant SEO/GEO.** Le format publicitaire à l'intérieur de ChatGPT, en se stabilisant comme expérience utilisateur acceptée (selon le chiffre OpenAI), réduit la fenêtre où le contenu organique cité dans une réponse ChatGPT était l'unique lien sortant. Le contenu organique cité reste structurellement séparé du contenu sponsorisé, mais le mix global d'attention disponible pour la citation organique diminue à mesure que le format publicitaire s'installe. C'est une variable à intégrer à la mesure de visibilité IA, à part entière, en distinguant la surface ChatGPT free (mixte) de la surface Claude (sans pub).

### B2. Actualité SEO : Google déploie le June 2026 spam update, deuxième mise à jour spam de l'année, sans nouvelle politique

Google a annoncé le 24 juin 2026 le déploiement de la « June 2026 spam update », deuxième mise à jour spam de l'année après celle de mars 2026. Le rollout a été enregistré sur le [Search Status Dashboard](https://status.search.google.com/) à 9h00 PT, et la note de publication a suivi à 9h03 PT. Couverture sur [Search Engine Land](https://searchengineland.com/google-releases-june-2026-spam-update-481002), [Search Engine Journal](https://www.searchenginejournal.com/google-begins-rolling-out-the-june-2026-spam-update/580424/), [Search Engine Roundtable](https://www.seroundtable.com/google-june-2026-spam-update-out-41568.html), [PPC Land](https://ppc.land/googles-june-2026-spam-update-is-live-what-it-hits-and-why-it-matters/) et [Optimixed](https://www.optimixed.com/google-june-2026-spam-update-is-rolling-out/).

La mise à jour s'applique à toutes les langues et à toutes les régions. Communiqué Google verbatim : « *Released the June 2026 spam update, which applies globally and to all languages. The rollout may take a few days to complete.* » Google précise que cette mise à jour n'introduit pas de nouvelle politique spam : elle applique l'existant, dont l'élargissement de mai 2026 couvrant la manipulation des AI Overviews et de l'AI Mode (clarification « *Search spam policies also apply to AI Search features* », 15 mai 2026). Cette mise à jour ne cible pas spécifiquement le link spam ni la site reputation abuse (parasite SEO), qui sont l'objet de politiques distinctes.

**Lecture procédurale.** La cadence annuelle des spam updates Google est passée à deux par an en 2026 (mars, juin) après une cadence d'un par an en 2024 et 2025. La rapidité de déploiement varie : mars 2026 s'est déployée en moins d'une journée, juin 2026 est annoncée à « *a few days* ». Pour un consultant, deux conséquences opérationnelles : (1) la surveillance des fluctuations de visibilité doit désormais intégrer une fenêtre spam mi-mars / mi-juin / éventuellement fin d'année si Google maintient la cadence ; (2) la jurisprudence des manual actions et des déclassements algorithmiques sur la fenêtre back button hijacking (effective 15 juin) interagit potentiellement avec cette mise à jour spam, et il sera difficile, sur les fluctuations observées entre le 15 et le 30 juin, d'isoler l'effet propre de chaque mécanisme.

C'est une brève Actualité SEO, jamais une info du jour : la règle d'édition (directives Tim, 2026-06-01) prohibent qu'un core update ou une update d'algorithme Google porte le pilier de l'édition.

### B3. Niche SEO : Asda introduit Amazon Retail Ad Service au Royaume-Uni, première extension hors États-Unis

Asda a annoncé le 23 juin 2026 sur son [Newsroom corporate](https://corporate.asda.com/newsroom/2026/23/06/asda-teams-up-with-amazon-in-uk-first-retail-media-and-ad-tech-partnership) un partenariat avec Amazon Ads par lequel Amazon Retail Ad Service est déployé sur le site de commerce en ligne Asda et sur celui de sa marque George (mode et maison). Couverture indépendante par [Retail Tech Innovation Hub](https://retailtechinnovationhub.com/home/2026/6/23/asda-claims-industry-first-as-supermarket-chain-inks-deal-to-add-amazon-retail-ad-service-to-online-stores), [Grocery Gazette](https://www.grocerygazette.co.uk/2026/06/25/asda-teams-up-with-amazon-ads-to-boost-retail-media-offer/) le 25 juin, [KamCity](https://www.kamcity.com/namnews/uk-and-ireland/supermarkets/asda-partners-with-amazon-to-create-stronger-retail-media-proposition/), [The Grocer](https://www.thegrocer.co.uk/news/asda-brings-in-amazon-to-transform-retail-media-offer/720493.article) et [Retail Times](https://retailtimes.co.uk/asda-teams-up-with-amazon-in-uk-first-retail-media-and-ad-tech-partnership/).

C'est la première extension d'Amazon Retail Ad Service en dehors des États-Unis depuis son lancement Amazon en 2024. Asda devient le premier retailer non-US à intégrer ce service ; le déploiement se fait par phases à partir du quatrième trimestre 2026. Le service utilise les techniques de machine learning d'Amazon Ads pour servir des publicités jugées plus pertinentes en fonction du comportement de navigation et d'achat des utilisateurs sur Asda et George.

**Implication pour un consultant SEO/GEO.** Pour une marque qui distribue dans la grande distribution UK, l'arrivée de Retail Ad Service côté Asda ouvre une nouvelle surface de découverte commerciale, distincte des sponsorisés Amazon eux-mêmes, sur la base installée Asda (8 milliards de transactions cumulées revendiquées par Asda). C'est un canal d'acquisition payant, pas un canal organique ; mais il modifie la composition de la première page d'un site retailer comme Asda, et donc l'espace où la fiche produit organique d'une marque concurrente est lue ou ignorée. C'est une donnée à intégrer à un audit de présence omnicanale sur le marché UK épicerie / mode / maison, distinct du référencement Amazon.com lui-même. Pour suivre : tester si Asda publie un format publicitaire propre ou si le format suit la norme Amazon Ads existante, et si le rollout s'étend à d'autres retailers UK (Tesco, Sainsbury's, Morrisons) ou européens.

---

## Connexions doctrine

- [[concepts/agentic-search]] : info du jour qui ajoute YouTube Content & Creator Insights API à la cartographie des cinq plateformes structurant la couche d'orchestration agentique côté annonceur. Proposition de mise à jour de la fiche à statuer en revue hebdo (intégrer la distinction MCP / API native / agent intégré).
- [[concepts/metriques-visibilite-geo]] : la cinquième dimension proposée à la revue hebdo (downstream sur le site, v1 du jour) reste indépendante de la 4e (corpus propriétaire interrogeable par API). Le YouTube Content & Creator Insights API ouvre une mesure de présence créateur propre à YouTube, qu'aucun outil SEO standard ne reproduit depuis l'extérieur.
- [[concepts/structural-information-geo]] : la disponibilité d'une API qui expose un corpus structurellement organisé (créateurs + audiences) est congruente avec l'hypothèse que l'information structurée prédit la citation par un système IA. À surveiller si une étude empirique mesure une corrélation entre adoption de l'API et présence en réponse Gemini ou YouTube AI.
- [[concepts/tabou-visibilite]] : la donnée OpenAI sur les rejets d'annonces ChatGPT rappelle qu'« être cité » et « être lu » et « être accepté » sont trois mesures distinctes ; la « visibilité IA » sans précision quantitative continue d'agréger des indicateurs hétérogènes.

---

## Prédictions ouvertes mises à jour 2026-06-25-v2

- **P-2026-06-24-2 (résolution partielle proposée)** : YouTube a publié une API native IA bâtie sur un corpus propriétaire (Content & Creator Insights API). La résolution pleine demande le calendrier précis d'accès au-delà des partenaires alpha mentionnés.
- **P-2026-06-24-1 (extension)** : la liste s'étend à YouTube Content & Creator Insights API. La prédiction reste : avant le 31 mars 2027, au moins une plateforme parmi Pinterest MCP, Shopify Catalog API, Reddit Community Intelligence, TikTok Symphony Agent, Alexa+ Agentic Ads et YouTube C&CI API publie une métrique d'usage publique (annonceurs actifs, campagnes générées, lift documenté avec méthodologie tierce).
- **P-2026-06-25-v2-1 (nouvelle)** : avant le 31 décembre 2026, au moins un retailer européen ou non-US autre que Asda annoncera l'intégration d'Amazon Retail Ad Service (Tesco, Sainsbury's, Morrisons, Carrefour, Ahold Delhaize, Lidl, ou équivalent), confirmant la sortie du stade « partenariat isolé US-UK » et la mise en place d'une trajectoire d'expansion plurinationale.
- **P-2026-06-25-v2-2 (nouvelle)** : avant le 30 septembre 2026, OpenAI ou un cabinet de mesure indépendant publiera une méthodologie ou une décomposition de l'indicateur « ad dismissal rate » dans ChatGPT (définition opérationnelle, seuil, exclusions), faute de quoi le chiffre « -50 pct » restera un indicateur déclaratif non interprétable.

---

## Sources consultées

### Sources primaires
- [Google blog : Cannes Lions 2026, new tools from YouTube](https://blog.google/products/ads-commerce/youtube-insights-tools-cannes-lions-2026/)
- [Asda corporate : Asda teams up with Amazon in UK-first retail media and ad tech partnership](https://corporate.asda.com/newsroom/2026/23/06/asda-teams-up-with-amazon-in-uk-first-retail-media-and-ad-tech-partnership)
- [Google Search Status Dashboard](https://status.search.google.com/)

### Sources secondaires recoupées (info du jour et brèves)
- [eMarketer : Google expands YouTube's creator marketing tools at Cannes Lions](https://www.emarketer.com/content/google-expands-youtube-s-creator-marketing-tools-cannes-lions) (23 juin)
- [BuzzinContent : YouTube unveils Gemini-powered insights tools for creator-led campaigns at Cannes Lions 2026](https://www.buzzincontent.com/news/youtube-unveils-gemini-powered-insights-tools-for-creator-led-campaigns-at-cannes-lions-2026-12067643) (24 juin)
- [Performance Marketing World : Cannes Lions 2026, Google unveils new Gemini-powered YouTube tools and Amazon Retail Ad Service hits the UK](https://www.performancemarketingworld.com/article/1962640/cannes-lions-2026-google-unveils-new-gemini-powered-youtube-tools-amazon-retail-ad-service-hits-uk)
- [Adobo Magazine : Cannes Lions 2026, Strengthen creative campaigns with new tools from YouTube](https://www.adobomagazine.com/technology/cannes-lions-2026-strengthen-creative-campaigns-with-new-tools-from-youtube/)
- [Search Engine Land (Anu Adegbola, 24 juin) : OpenAI says ChatGPT ad dismissals have dropped 50% as relevance improves](https://searchengineland.com/openai-says-chatgpt-ad-dismissals-have-dropped-50-as-relevance-improves-480991)
- [Search Engine Land : Google releases June 2026 spam update](https://searchengineland.com/google-releases-june-2026-spam-update-481002)
- [Search Engine Journal : Google Begins Rolling Out The June 2026 Spam Update](https://www.searchenginejournal.com/google-begins-rolling-out-the-june-2026-spam-update/580424/)
- [Search Engine Roundtable : Google June 2026 Spam Update Is Rolling Out](https://www.seroundtable.com/google-june-2026-spam-update-out-41568.html)
- [PPC Land : Google's June 2026 spam update is live](https://ppc.land/googles-june-2026-spam-update-is-live-what-it-hits-and-why-it-matters/)
- [Optimixed : Google June 2026 Spam Update Is Rolling Out](https://www.optimixed.com/google-june-2026-spam-update-is-rolling-out/)
- [Retail Tech Innovation Hub : Asda claims industry first as UK grocer inks deal to add Amazon Retail Ad Service](https://retailtechinnovationhub.com/home/2026/6/23/asda-claims-industry-first-as-supermarket-chain-inks-deal-to-add-amazon-retail-ad-service-to-online-stores)
- [Grocery Gazette : Asda teams up with Amazon Ads to boost retail media offer](https://www.grocerygazette.co.uk/2026/06/25/asda-teams-up-with-amazon-ads-to-boost-retail-media-offer/) (25 juin)
- [KamCity : Asda Partners With Amazon To Create Stronger Retail Media Proposition](https://www.kamcity.com/namnews/uk-and-ireland/supermarkets/asda-partners-with-amazon-to-create-stronger-retail-media-proposition/)
- [The Grocer : Asda brings in Amazon to 'transform' retail media offer](https://www.thegrocer.co.uk/news/asda-brings-in-amazon-to-transform-retail-media-offer/720493.article)
- [Retail Times : Asda teams up with Amazon in UK-first retail media and ad tech partnership](https://retailtimes.co.uk/asda-teams-up-with-amazon-in-uk-first-retail-media-and-ad-tech-partnership/)

### Sources écartées (raisons consignées dans le ledger runs.jsonl du run)
- Adobe CX skills MCP General Availability 22 juin (déjà couvert 0623-v2 et 0624-v2).
- TikTok Symphony Agent 24 juin (déjà couvert 0624 v1).
- Pinterest MCP 17 juin (déjà couvert 0625 v1).
- Search Central Live Milan 18 juin (déjà couvert 0620 brève).
- Reddit-Anthropic CMC du 18 juin (pas de sortie publique 18-25 juin).
- Cannes Day 4 25 juin : pas de fait franchement neuf produit IA identifiable à l'heure d'écriture.
- WebMCP « 12 pct adoption enterprise » Sangria Tech : source unique non corroborée par une source primaire ou un cabinet indépendant ; statut `discarded` règle dure explore.

---

*SyntheticBrain. Édition v2 du 25 juin 2026. Aucun envoi.*
