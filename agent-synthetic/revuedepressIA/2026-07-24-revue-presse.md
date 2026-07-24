# Algorithme, édition du 24 juillet 2026

**Pilier info du jour :** Recherche agentique / Business SEO.

## Résumé de l'édition

- Yelp signe un accord de licence avec OpenAI le 23 juillet 2026 pour intégrer 330 M d'avis et 8 M+ de fiches d'entreprise dans les réponses ChatGPT, avec Request a Quote intégré côté marchand.
- Le cadre est explicite (contrat de licence, non-exclusif) et diffère du crawl toléré : Yelp reçoit branding et lien mais OpenAI garde le contrôle du design de l'affichage.
- CiteLens publie une mesure sur 320 requêtes acheteur en Turquie (4 moteurs IA + Google + Bing) : ChatGPT partage moins de 4 pct de ses citations avec le top-10 Bing, ce qui invalide la thèse d'un simple miroir Bing.
- Manhattan a tenu le 23 juillet une audience de trois heures sur la motion to dismiss dans Reddit v. Perplexity, avec un juge sceptique sur la capacité de Reddit à poursuivre au nom de ses utilisateurs.
- Google Ads API v25 sort le 22 juillet, retire deux ressources lifecycle, ajoute une optimisation loyalty retention et des breakdowns de durée pour l'inventaire YouTube non-skippable.

---

## Info du jour — Recherche agentique / Business SEO

### Yelp licencie 330 millions d'avis à ChatGPT : la sortie d'un éditeur local du crawl toléré vers l'accord de licence

Le 23 juillet 2026, Yelp signe un accord de licence de contenu avec OpenAI. L'accord donne à ChatGPT accès aux 330 millions d'avis cumulés de Yelp et à ses plus de 8 millions de fiches d'entreprise, ainsi qu'aux photos et notations associées. La fonction Request a Quote de Yelp arrivera dans ChatGPT peu après le lancement et permettra à un utilisateur de contacter un prestataire local pour un devis directement depuis la conversation ([SearchEngineLand 483326, Danny Goodwin, 23 juillet 2026](https://searchengineland.com/openai-yelp-deal-483326) ; [Axios, Sara Fischer, exclusive 23 juillet 2026](https://finance.yahoo.com/media-advertising/articles/exclusive-yelp-deal-pushes-local-130005436.html) ; [GuruFocus YELP News, 23 juillet 2026](https://www.gurufocus.com/news/8975503/yelp-yelp-partners-with-openai-to-enhance-chatgpt-business-data-access) ; [CryptoBriefing, 23 juillet 2026](https://cryptobriefing.com/yelp-openai-data-licensing-chatgpt/)).

Trois éléments sortent du régime habituel d'exposition d'un éditeur à un moteur IA.

**Premier élément : le cadre juridique.** L'accord est un contrat de licence explicite, pas un crawl toléré ni un opt-in via robots.txt. Les termes financiers ne sont pas divulgués. Le contrat n'est pas exclusif : Yelp peut signer des accords similaires avec d'autres opérateurs IA, et détient déjà des accords analogues avec Apple Maps et Yahoo+ ([Yahoo Finance / Axios, 23 juillet 2026](https://finance.yahoo.com/media-advertising/articles/exclusive-yelp-deal-pushes-local-130005436.html)).

**Deuxième élément : la mécanique d'attribution.** Le branding Yelp et les liens accompagnent le contenu quand OpenAI l'utilise, mais OpenAI contrôle le design de cette expérience. Autrement dit, Yelp obtient un lien retour visible dont la forme et la place dans la réponse ChatGPT dépendent d'un tiers, hors GSC et hors mesure indépendante à ce stade ([SearchEngineLand 483326](https://searchengineland.com/openai-yelp-deal-483326)). C'est un cas concret pour [[concepts/metriques-visibilite-geo]] : l'exposition dans la réponse générative est acquise contractuellement, l'observation de son affichage effectif reste à instrumenter.

**Troisième élément : la couche transactionnelle intégrée.** Request a Quote transforme la citation en génération de contact commercial pour le marchand local. Yelp ne cède pas seulement une base de contenu descriptif, il pousse un mécanisme qui rapporte au marchand un lead qualifié dans la surface ChatGPT. La logique se rapproche des couches de découverte agentique documentées côté commerce (UCP, ACP, AP2), mais ici la brique est celle du lead service, pas de la commande produit.

**Cadrage doctrine.** L'accord illustre trois lectures.

D'abord, [[concepts/agentic-search]] : le canal ChatGPT devient une surface de découverte locale par prompt, avec un mécanisme de conversion intégré côté marchand. La substitution ne se joue pas seulement sur le trafic reçu par Yelp.com, elle se joue sur la surface où l'utilisateur choisit un prestataire.

Ensuite, [[concepts/data-proprietaire]] : Yelp exécute une thèse défensive testable. Le CEO Jeremy Stoppelman précise « If you want to answer local queries, you really need Yelp » et « Ultimately, we believe that if we allow our content outside the walls of just Yelp, value does accrue back to Yelp » ([GuruFocus, 23 juillet 2026](https://www.gurufocus.com/news/8975503/yelp-yelp-partners-with-openai-to-enhance-chatgpt-business-data-access) ; verbatim reproduit par [Yahoo Finance / Axios](https://finance.yahoo.com/media-advertising/articles/exclusive-yelp-deal-pushes-local-130005436.html)). La thèse à documenter : la data propriétaire locale reste un actif quand elle est distribuée hors du site d'origine, contre l'idée courante qu'un éditeur qui cède ses données perd son moat.

Enfin, [[concepts/tabou-visibilite]] : la mesure business attendue ne sera pas une hausse de « visibilité » mais un chiffre de leads Request a Quote générés via ChatGPT, et un différentiel de revenu licence (poste « other revenue » +17 pct YoY 2025 chez Yelp selon [CryptoBriefing, 23 juillet 2026](https://cryptobriefing.com/yelp-openai-data-licensing-chatgpt/)).

**Limites documentaires.** Trois zones d'incertitude à rester attentif.

1. Aucune date précise n'est publiée pour l'apparition effective des avis Yelp dans les réponses ChatGPT US ou hors US. Les articles citent « bientôt » pour Request a Quote sans jour ni semaine.
2. Aucun chiffre de licence n'est communiqué. Le seul indicateur agrégé est la ligne « other revenue » de Yelp (+17 pct YoY 2025), dont Yelp ne ventile pas la composition entre Yahoo+, Apple Maps, OpenAI et d'autres partenaires.
3. Aucune précision sur la forme de l'affichage du lien Yelp dans les réponses ChatGPT (position, densité, taux d'affichage). OpenAI en garde le design.

**Prédictions ouvertes (voir `predictions.jsonl`).**

- **P-2026-07-24-1** : d'ici le 31 mars 2027, un deuxième éditeur de reviews grand public (TripAdvisor, G2, Trustpilot, Booking, ou équivalent) publie ou fait publier un accord de licence explicite avec OpenAI, Anthropic ou Google Gemini pour l'intégration de contenu d'avis dans une réponse générative.
- **P-2026-07-24-2** : d'ici le 30 juin 2027, un vendor de mesure GEO (Profound, Peec AI, Semrush AI Visibility Toolkit, Ahrefs Brand Radar, Athena Intelligence) publie une mesure du taux d'affichage du lien Yelp dans les citations ChatGPT sur requêtes locales US, sur panel > 500 requêtes.
- **P-2026-07-24-3** : d'ici le 31 décembre 2026, Yelp publie dans un rapport trimestriel un chiffre agrégé « revenu de licence data IA » distinct des autres partenaires (Yahoo+, Apple Maps), soit un ordre de grandeur, soit une croissance chiffrée YoY isolée.

---

## B1 — GEO

### CiteLens mesure sur 320 requêtes acheteur : ChatGPT et Bing ne partagent que 4 pct de leur top-10

CiteLens publie le 9 juillet 2026 une étude qui compare, sur 320 requêtes acheteur templatisées couvrant trois secteurs grand public du marché turc et un mesure en juin 2026, les citations de quatre moteurs IA (ChatGPT, Perplexity, Claude, Google AI Mode) aux résultats organiques Google et Bing sur les mêmes requêtes. Les citations sont normalisées au niveau du domaine enregistrable ([MarTech Series, MTS Staff Writer, 9 juillet 2026](https://martechseries.com/predictive-ai/ai-platforms-machine-learning/citelens-study-seo-decides-ai-citations-on-google-and-perplexity-not-chatgpt/) ; [EIN Presswire 925230382](https://www.einpresswire.com/article/925230382/citelens-study-seo-decides-ai-citations-on-google-and-perplexity-not-chatgpt) ; [MarTech Series version « different web »](https://martechseries.com/predictive-ai/ai-platforms-machine-learning/citelens-study-ai-search-cites-a-different-web-than-google-ranks-in-2026/) ; [National Law Review press release](https://natlawreview.com/press-releases/citelens-study-ai-search-cites-different-web-google-ranks-2026)).

Quatre résultats concrets.

D'abord, Google AI Mode obtient 93 pct de ses citations dans le top-10 organique Google et une corrélation statistique de 0,92. Perplexity suit avec 89 pct de citations dans le top-10 Google et une corrélation de 0,87. Sur ces deux moteurs, le classement organique Google prédit très largement le corpus cité.

Ensuite, ChatGPT ne prend que 30 pct de ses citations dans le top-10 Google, contre 70 pct hors top-10. La corrélation ChatGPT au classement Google est proche de zéro, tout comme la corrélation à la popularité de marque au sens usuel du terme (recherches brand).

Puis, moins de 4 pct des citations ChatGPT apparaissent dans le top-10 Bing. Ce chiffre invalide la thèse d'un simple miroir Bing pour ChatGPT, qui circulait notamment depuis la précédente période où ChatGPT utilisait officiellement Bing comme moteur de retrieval par défaut.

Enfin, Claude tire 58 pct de ses citations vers des sites adossés à Wikipedia, contre 21 pct pour ChatGPT. L'étude qualifie ce comportement Claude de tracking de la brand search demand plutôt que du classement organique.

**Cadrage doctrine.** CiteLens documente empiriquement, sur un panel limité et localisé (marché turc, secteurs grand public, sans détail public sur lesquels), ce que la doctrine SEO/GEO tenait pour hypothèse : il n'existe pas d'unique surface IA à optimiser. Google AI Mode et Perplexity restent surtout SEO-driven au sens classique ; ChatGPT et Claude opèrent sur d'autres signaux (entité, présence Wikipedia). Voir [[concepts/entites-vectorielles]] pour la partie brand/entité, et [[concepts/metriques-visibilite-geo]] pour la mesure moteur par moteur.

**Limites documentaires.** Trois caveats.

1. Le panel est explicitement limité au marché turc et à trois secteurs grand public non listés dans les diffusions presse. La transposition à un marché occidental n'est pas testée par cette étude.
2. La méthodologie 320 requêtes templatisées reste sous la barre des études longitudinales à trois ordres de grandeur supérieures (Semrush AI Visibility Toolkit 1 094 catégories, cf. édition du 22 juillet 2026). L'étude sert de mesure comparative, pas de benchmark absolu.
3. La diffusion primaire passe par MarTech Series et un communiqué de presse EIN, sans lien vers un rapport PDF détaillé côté CiteLens à ce stade. L'audit méthodologique tiers reste à faire.

**Prédiction ouverte.**

- **P-2026-07-24-4** : d'ici le 31 mars 2027, une reproduction indépendante de la mesure « ChatGPT partage moins de 5 pct de son top-10 citations avec le top-10 Bing » est publiée sur un panel > 300 requêtes en langue anglaise avec méthodologie explicite et rapport téléchargeable.

---

## B2 — Actualité SEO / Legal

### Reddit v. Perplexity : trois heures d'audience à Manhattan, un juge sceptique sur la capacité de Reddit à poursuivre pour ses utilisateurs

Le 23 juillet 2026, la US District Court du Southern District of New York (Manhattan) a tenu trois heures d'audience sur la motion to dismiss déposée par Perplexity AI Inc., SerpApi LLC et deux autres sociétés de scraping (Oxylabs UAB, AWMProxy) dans le dossier `Reddit, Inc. v. SerpApi LLC` (docket 1:25-cv-08736). Le juge, identifié par le docket comme Paul A. Engelmayer, s'est montré sceptique sur la thèse de Reddit selon laquelle la plateforme aurait qualité pour poursuivre en violation de droit d'auteur au nom de ses utilisateurs, dont le contenu est en cause ([Bloomberg Law, Reddit Defends Authority to Sue Perplexity Over Data Scraping, 23 juillet 2026](https://news.bloomberglaw.com/litigation/reddit-defends-authority-to-sue-perplexity-over-data-scraping) ; [CourtListener docket 71720563](https://www.courtlistener.com/docket/71720563/reddit-inc-v-serpapi-llc/) ; [Bloomberg Law, Perplexity Blasts Reddit Daisy Chain Site-Scraping Claims](https://news.bloomberglaw.com/ip-law/perplexity-blasts-reddits-daisy-chain-site-scraping-claims)).

Le fond du dossier : Reddit reproche à Perplexity l'achat de données Reddit à des sociétés de scraping qui les extraient via les résultats de recherche Google. Reddit demande des dommages, une interdiction permanente d'usage des données déjà extraites, et une injonction contre toute nouvelle extraction. Perplexity défend le fait que Reddit n'a pas qualité pour agir sur des données produites par ses utilisateurs et qualifie la chaîne d'imputation de « daisy chain » (chaîne de causalité trop indirecte).

**Ce que ce hearing change.** Le juge n'a pas rendu de décision, il a entendu. Le retard éventuel d'une décision favorable à Perplexity supprimerait l'un des trois axes de contentieux ouverts contre l'entreprise (les autres étant CNN sur copyright direct, et le litige Amazon-Perplexity Comet sur CFAA). Une décision qui rejette la motion consoliderait au contraire la thèse selon laquelle les plateformes peuvent poursuivre en aval de la chaîne d'extraction pour bloquer un fournisseur de données à un moteur IA. Voir aussi [[concepts/agentic-search]] pour la partie autorisation d'accès et [[concepts/tabou-visibilite]] pour l'articulation avec les autres litiges éditeur-vs-IA en cours.

**Limites documentaires.** Deux caveats.

1. Le motif exact des interventions du juge n'est pas connu publiquement à ce stade : l'article Bloomberg Law est en paywall, la couverture disponible se limite à la synthèse open (« skepticism »).
2. Aucun calendrier de décision n'est communiqué. Les motions to dismiss dans le SDNY sont typiquement décidées en plusieurs semaines à plusieurs mois selon la charge du juge Engelmayer.

**Prédiction ouverte.**

- **P-2026-07-24-5** : d'ici le 31 décembre 2026, la US District Court SDNY rend sa décision sur la motion to dismiss dans Reddit v. SerpApi. Résolution positive : décision publiée. Résolution négative : silence au 31 décembre 2026.

---

## B3 — Business SEO / PPC

### Google Ads API v25 retire deux ressources lifecycle, ajoute un objectif loyalty retention et des breakdowns durée YouTube

Le 22 juillet 2026, Google a publié la version 25 de la Google Ads API, en release principale (major release au sens API), donc avec breaking changes. La v25 retire purement les ressources et services `CustomerLifecycleGoal` et `CampaignLifecycleGoal`, qui exigeaient une réécriture du code des annonceurs qui les utilisaient ([Google Ads Developer Blog, 22 juillet 2026](https://ads-developers.googleblog.com/2026/07/announcing-v25-of-google-ads-api.html) ; [Search Engine Roundtable 41740, Barry Schwartz](https://www.seroundtable.com/google-ads-api-v-25-41740.html) ; [PPC Land, 22 juillet 2026](https://ppc.land/google-ads-api-v25-kills-two-lifecycle-goal-resources-forcing-code-rewrites/) ; [Optimixed daily recap 22 juillet 2026](https://www.optimixed.com/google-ads-api-version-25-now-out/)).

Côté nouveaux champs, la v25 ajoute des breakdowns au niveau de la durée pour l'inventaire YouTube non-skippable via un nouveau segment `ad_sub_format_type` avec les valeurs standard, max 30 s et max 60 s. Elle ajoute des métriques d'engagement social pour les publicités Shorts, un objectif d'optimisation « loyalty retention », et un accès sous consentement aux analytics de chaîne créateur.

**Cadre de support.** Les versions principales de l'API (major versions) portent un cycle de vie de douze mois. La v25 sera donc supportée jusqu'à environ juillet 2027, sauf annonce contraire. La v24.2, publiée le 25 juin 2026, reste supportée en parallèle sur sa fenêtre restante.

**Ce qui change pour l'annonceur.** Deux effets opérationnels.

1. Les annonceurs qui pilotaient l'acquisition et la rétention via `CustomerLifecycleGoal` doivent migrer vers `LifecycleGoalSettings` sur la campagne, avec un objectif d'acquisition et un mode de rétention paramétrable. La documentation de migration fait référence au champ retiré comme « déprécié depuis v22 » : la v25 en supprime l'exécution.
2. Le breakdown durée YouTube non-skippable permet aux annonceurs et aux mesures d'attribution de segmenter précisément l'inventaire non-skippable au-delà de la simple distinction skippable / non-skippable. Utile pour le pilotage CPCV et pour comparer les performances par durée d'exposition.

**Limites documentaires.** Deux caveats.

1. L'article Google Ads Developer Blog primaire renvoie une réponse partielle en récupération automatique. Les corroborations utilisées (SEJ, SE Roundtable, PPC Land) confirment le contenu principal de la release.
2. Aucun chiffre d'adoption immédiat ne circule. Les annonceurs disposent typiquement de plusieurs mois avant l'expiration des versions précédentes pour migrer.

**Prédiction ouverte.**

- **P-2026-07-24-6** : d'ici le 31 mars 2027, Google publie sur son blog développeur ou en support une communication sur l'adoption effective du champ `ad_sub_format_type` par les annonceurs sur inventaire YouTube non-skippable (nombre d'utilisateurs API, campagnes actives ou volume d'appels).

---

Draft SyntheticBrain. Rien n'a été envoyé.
