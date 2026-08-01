---
edition: 2026-08-01
pilier_info_du_jour: Recherche agentique
piliers_breves: [Business SEO, Actualite SEO, GEO]
capture_mode: native
---

# Algorithme — édition du 1er août 2026

## Un précédent DMCA § 1201 pour les moteurs génératifs : Reddit contre Perplexity survit à la motion to dismiss

### Résumé

- Le juge fédéral Paul A. Engelmayer (SDNY) refuse le 31 juillet 2026 de rejeter les demandes DMCA anti-circumvention de Reddit contre Perplexity et SerpApi. Les faits partent en discovery.
- Le § 1201(a) survit contre les deux défendeurs. Le § 1201(b) trafficking contre SerpApi, la concurrence déloyale et l'enrichissement sans cause sont écartés.
- Le juge considère que Reddit constitue un "global digital on-line marketplace for copyrighted works" au sens du DMCA, et que SearchGuard de Google qualifie comme mesure technique de contrôle d'accès.
- Le titre RDDT termine la séance en baisse de 22 %, plus forte chute quotidienne depuis l'IPO. Deux facteurs distincts pèsent : la décision, et la guidance publiée la veille sur le ralentissement de la croissance utilisateurs US du T2. L'attribution à la seule décision reste partielle.
- Ailleurs : OpenAI teste dans Ads Manager un type de campagne qui envoie l'utilisateur vers un Business Agent au lieu d'un site externe. Google Analytics ajoute un diagnostic pour les identifiants agrégés manquants.

---

## Info du jour — Recherche agentique

Le juge fédéral Paul A. Engelmayer, Southern District of New York, a refusé le 31 juillet 2026 la motion to dismiss de Perplexity et SerpApi dans l'affaire Reddit v. Perplexity. Les demandes anti-circumvention formulées au titre du § 1201(a) du Digital Millennium Copyright Act survivent contre les deux défendeurs. L'affaire passe à la phase de discovery, où le fond des pratiques alléguées de contournement d'accès sera examiné avec preuves.

Ce qui a été écarté : la demande § 1201(b) de trafficking contre SerpApi, la concurrence déloyale et l'enrichissement sans cause contre Perplexity et SerpApi. Ce qui reste : la théorie centrale de Reddit, qui reproche aux défendeurs d'avoir contourné des protections techniques d'accès pour aspirer les publications de la communauté à grande échelle, en changeant continuellement d'adresses IP pour échapper aux dispositifs de Reddit et de Google.

Le raisonnement du juge est le point saillant pour un consultant SEO ou GEO. Engelmayer considère que Reddit "epitomizes the 'global digital on-line marketplace for copyrighted works' that the DMCA sought to promote" et que ses préjudices tombent "within the zone of interests" que le § 1201 protège. Il ajoute, pour l'instant, que SearchGuard, le dispositif de contrôle d'accès de Google, qualifie comme "technological measure" au sens de la loi ([MLex](https://www.mlex.com/mlex/artificial-intelligence/articles/2508237), [Cryptopolitan 31/07/2026](https://www.cryptopolitan.com/judge-strikes-perplexity-ai-defense-reddit/), [Reuters via TradingView](https://www.tradingview.com/news/reuters.com,2026:newsml_L6N43X10V:0-perplexity-ai-loses-bid-to-toss-reddit-lawsuit-over-data-scraping/), [Law.com New York Law Journal](https://www.law.com/newyorklawjournal/2026/07/31/reddits-dmca-claims-against-perplexity-serpapi-survive-ai-scraping-challenge/), [Bloomberg Law](https://news.bloomberglaw.com/litigation/reddit-defends-authority-to-sue-perplexity-over-data-scraping)).

Pourquoi c'est un fait qui pèse pour la pratique. Jusqu'à cette décision, les théories juridiques opposées aux acteurs de la recherche générative reposaient principalement sur le droit d'auteur classique (Nikkei, Asahi, Encyclopedia Britannica, New York Times contre OpenAI et Anthropic sur le training), ou sur le CFAA côté injonctions préliminaires (Amazon v. Perplexity Comet). Engelmayer valide qu'un moteur qui aspire des contenus derrière des mesures d'accès techniques pour construire une réponse générative peut engager la responsabilité anti-circumvention, indépendamment de la question du fair use sur la réutilisation du texte. La décision est procédurale, pas encore substantielle sur le fond, mais elle ouvre la discovery à un examen des pratiques d'IP rotation, du volume de requêtes vers Reddit et des flux entre SerpApi et les modèles Perplexity, éléments jusqu'ici invisibles au public.

Ce que la doctrine du vault retient. La décision confirme un point du concept [[concepts/data-proprietaire]] : la valeur juridique d'un corpus dépend de deux choses distinctes, sa nature copyrightable et le dispositif technique qui contrôle son accès. La position de Reddit tient parce qu'il combine les deux, contenu utilisateur sous CLUF et protections d'accès actives. Un site qui expose ses contenus sans mesure d'accès formelle n'a pas ce levier. La décision alimente aussi [[concepts/agentic-search]] côté opérateur : la lecture agentique à grande échelle (ici, résolutions de requêtes en direct pour construire une réponse) peut être remise en cause au titre du droit d'accès, pas seulement du droit d'auteur.

Un lecteur qui note où se situe l'incertitude. Le juge dit "for now" sur la qualification de SearchGuard comme mesure technique protégée. Le discovery peut la refermer, ou la conforter. Aucun chiffre financier n'a été publié par la cour à ce stade sur les dommages potentiels. La réaction du titre RDDT (baisse de 22 % à la clôture du 31 juillet, plus forte chute quotidienne enregistrée, [StockTwits](https://stocktwits.com/news-articles/markets/equity/reddit-advances-copyright-suit-against-perplexity-in-crusade-against-ai-data-scraping/cZN4LCgRJPu), [Gurufocus](https://www.gurufocus.com/news/8995709/reddit-stock-plunges-22-as-us-user-growth-slows)) combine deux facteurs, la décision et la guidance sur le ralentissement de la croissance utilisateurs US du T2. L'attribution du recul à la seule décision est fragile ; Gurufocus attribue le mouvement principal à la croissance utilisateurs US et au volatile search referrals, la décision jouant un rôle amplificateur.

Pour un consultant qui gère un site à corpus propriétaire, la lecture opérationnelle est simple. La décision augmente la surface de recours d'un éditeur contre un moteur qui aspire ses contenus derrière un contrôle d'accès. Elle ne dit rien sur les sites qui exposent leurs contenus librement. Elle ne dit rien sur le fair use au fond. Elle dit qu'un juge fédéral accepte d'examiner en discovery la théorie que le contournement systématique d'un dispositif d'accès pour alimenter un moteur génératif peut violer le § 1201(a) du DMCA. C'est un précédent procédural qui va peser sur les négociations de licence dans les six à douze mois qui viennent, notamment sur les contrats Reddit-Google et Reddit-OpenAI qui expirent au premier semestre 2027 ([SEL couverture antérieure Reddit-Google](https://searchengineland.com/reddit-and-usa-today-face-google-exit-as-search-traffic-drops-28-482701)).

## Brèves

### B1 — Recherche agentique + Business SEO — OpenAI teste un type de campagne "Agent" dans Ads Manager

Barry Schwartz repère le 31 juillet 2026 sur [Search Engine Roundtable](https://www.seroundtable.com/chatgpt-ads-business-agent-41801.html) qu'OpenAI a ajouté dans son Ads Manager un type de campagne nommé "Agent" en test, qui envoie les utilisateurs de ChatGPT vers une conversation avec un Business Agent au lieu d'un site externe. Anu Adegbola documente le même jour sur [Search Engine Land](https://searchengineland.com/openai-ads-business-agent-484141) qu'OpenAI scrape le site du business pour construire un profil de contexte (questions clients fréquentes, informations support, contexte général) avant de proposer la campagne. Le format reste au stade test, aucun chiffre d'usage publié.

Ce que ça change côté SEO. L'unité de destination d'une publicité passe du couple URL de landing plus formulaire vers une conversation instrumentée. Un annonceur qui active ce format perd le contrôle éditorial fin qu'il avait sur sa page de destination : la réponse conversationnelle est construite par OpenAI à partir du corpus scrapé de son site, pas rédigée par lui. Le concept [[concepts/agentic-search]] gagne une variante concrète côté opérateur ChatGPT, distincte du checkout agentique Google UCP couvert en éditions précédentes (l'UCP concerne l'achat organique, ici c'est l'annonce payante). Rappel à valider avec le prochain drop OpenAI : la publicité "Business Agent" n'a pas encore d'API, pas encore de métrique d'usage publique, pas encore d'annonce officielle OpenAI hors interface Ads Manager. Reprise Optimixed le 31 juillet ([Optimixed](https://www.optimixed.com/openai-appears-to-be-building-chatbot-native-ads-that-launch-ai-agents/)).

### B2 — Actualité SEO — Google Analytics ajoute un diagnostic pour identifiants agrégés manquants

Anu Adegbola documente le 31 juillet 2026 sur [Search Engine Land](https://searchengineland.com/google-analytics-adds-campaign-diagnostics-for-missing-aggregate-identifiers-484132), repris par [Optimixed](https://www.optimixed.com/google-analytics-adds-campaign-diagnostics-for-missing-aggregate-identifiers/), que Google Analytics ajoute une alerte qui identifie les URL sans identifiants agrégés (GBRAID et gad_). Ces paramètres servent de secondaire à Google quand le Google Click Identifier (GCLID) n'est pas récupérable, avec les UTM en dernier recours. Sans eux, les visites Google Ads sont attribuées par erreur à la source Organic, ce qui gonfle mécaniquement le trafic référencement naturel et dilue l'attribution payante.

Pour un consultant qui audite une propriété GA4 sur un compte Google Ads actif, l'ajout de ce diagnostic donne un point de contrôle nouveau : une part du trafic déclaré "Organic" dans les rapports peut être en réalité du payant mal identifié. Le fix est procédural (vérifier auto-tagging GCLID, cohérence GBRAID pour les campagnes iOS SKAdNetwork, présence UTM en fallback), le fait notable est que Google le rend visible côté rapport GA4 sans avoir besoin d'un audit tiers. Google n'a pas publié à ce stade de communication officielle sur developers.google.com : le fait est documenté par SEL et Optimixed uniquement, à confirmer dans les prochains jours.

### B3 — GEO — Presque la moitié des requêtes Google montrent une AI Overview

Le 30 juillet 2026, [Barry Schwartz sur Search Engine Roundtable](https://www.seroundtable.com/almost-half-of-google-searches-have-ai-overviews-41787.html) documente que les AI Overviews apparaissent désormais sur 43 à 48 % des requêtes Google, selon la nature de la requête, contre 25 à 30 % au lancement en 2024 ([Position Digital](https://www.position.digital/blog/ai-seo-statistics/), [eSEOspace](https://eseospace.com/blog/how-ai-overviews-impact-seo-2026/)). Le seuil de 50 % n'a pas été franchi mais la fenêtre se resserre.

Pour la doctrine [[concepts/metriques-visibilite-geo]], ce n'est pas un fait franchement neuf. La prévalence AIO est mesurée par plusieurs outils depuis fin 2024 ([BrightEdge](https://www.brightedge.com/ai-overviews), [Semrush](https://www.semrush.com/blog/ai-overviews-impact/), [Conductor](https://www.conductor.com/state-of-aeo-geo/)) sur des panels non comparables. Le fait daté ici est la reprise cohérente à 43-48 % dans plusieurs outils indépendants fin juillet 2026, qui consolide la trajectoire à la hausse observée depuis six mois. Aucun consensus méthodologique n'existe encore sur la prévalence "vraie" à un instant t : la variance des panels reste dominante.

---

## Prédictions

- **P-2026-08-01-1** : la discovery Reddit v. Perplexity produira publiquement un chiffre de rotation IP ou de volume de requêtes SerpApi vers Reddit avant le 30 juin 2027 (confidence 0,40).
- **P-2026-08-01-2** : au moins un autre grand publisher parmi USA Today, Reuters, People Inc., The Economist ou Politico déposera une plainte DMCA § 1201 contre un fournisseur de recherche générative avant le 31 décembre 2026 (confidence 0,45).
- **P-2026-08-01-3** : OpenAI publiera une métrique publique d'usage du type de campagne Business Agent (nombre de conversations lancées, taux de complétion, ou premier client nommé) avant le 31 décembre 2026 (confidence 0,30).

---

Draft SyntheticBrain. Rien n'a été envoyé.
