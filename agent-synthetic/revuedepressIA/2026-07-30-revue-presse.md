---
type: revue-presse
title: Algorithme — 30 juillet 2026
date: 2026-07-30
edition: 2026-07-30-revue-presse
agent: SyntheticBrain
draft: true
---

# Algorithme — édition du 30 juillet 2026

## Résumé

- Anthropic a envoyé simultanément `Disallow: /share/*` dans robots.txt ET `X-Robots-Tag: none` sur les mêmes URLs, ce qui a empêché Google de lire l'instruction `noindex` et laissé des conversations Claude apparaître dans l'index.
- John Mueller a rappelé sur Bluesky le 29 juillet 2026 qu'il n'existe pas d'ordre de priorité publié pour résoudre des métadonnées contradictoires : la seule doctrine défendue par Google est de corriger le conflit, pas de tester son comportement.
- Meta a publié le 29 juillet 2026 après clôture ses résultats Q2 2026 : chiffre d'affaires 60,8 Md USD (+28 pct), run rate Advantage+ 75 Md USD, 1 M+ entreprises utilisent Meta Business Agents chaque semaine, action -9,64 pct après clôture sur guidance et capex.
- Microsoft teste sur Bing l'affichage direct des prix sur les images produits dans les résultats organiques (repéré par Barry Schwartz le 29 juillet 2026), au lieu des étoiles de note et du prix en dessous.

---

## Info du jour — Actualité SEO — Chez Anthropic, robots.txt a bloqué le crawler avant qu'il ne puisse lire le noindex censé masquer les chats Claude

Entre le 25 et le 27 juillet 2026, plusieurs conversations Claude que des utilisateurs pensaient partager en privé sont apparues dans les résultats Google via l'opérateur `site:claude.ai/share`. Le contenu allait de CV et notes techniques à des rapports médicaux nominatifs, résumés d'essais cliniques, revues d'employés, clés d'API et identifiants de connexion, selon les inspections de [404 Media, TechCrunch, Search Engine Journal](https://www.searchenginejournal.com/indexed-claude-chats-show-why-disallow-is-not-noindex/583852/), [TechRepublic](https://www.techrepublic.com/article/news-claude-shared-chats-google-search/) et l'analyse technique de [Daniel J. Glover, publiée le 26 juillet 2026](https://danieljamesglover.com/blog/2026-07-26-shared-claude-conversations-google/).

Le mécanisme n'est pas nouveau, mais il est mal compris. Le robots.txt d'Anthropic contient bien `Disallow: /share/*` sous `User-agent: *`. Les pages `claude.ai/share/*` envoient aussi un en-tête HTTP `X-Robots-Tag: none`, qui a la même portée que `noindex, nofollow` selon la [documentation Google sur les balises meta robots](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag). Les deux directives sont légitimes séparément. Combinées sur la même URL, elles s'annulent : l'instruction `noindex` est présente dans l'en-tête HTTP, mais robots.txt interdit à Googlebot de lire cet en-tête. Le crawler n'ouvre pas la page et ne voit donc jamais la consigne. Comme un lien externe suffit à inscrire l'URL dans l'index (URL-only listing, sans snippet), le résultat apparaît dans les SERP.

La documentation Google est explicite sur ce point : « la page ou la ressource ne doit pas être bloquée par un fichier robots.txt (...) si la page est bloquée par un fichier robots.txt (...) l'analyseur ne verra jamais la règle noindex » (extrait cité par [Daniel J. Glover, 26 juillet 2026](https://danieljamesglover.com/blog/2026-07-26-shared-claude-conversations-google/)). John Mueller le rappelle dans plusieurs threads publics : les pages bloquées par robots.txt peuvent apparaître en résultats sans être crawlées si d'autres pages y renvoient. Martin Splitt recommande de ne jamais mélanger `robots.txt Disallow` et `noindex` sur la même URL, réaffirmé dans la couverture de [Search Engine Journal du 27 juillet 2026](https://www.searchenginejournal.com/indexed-claude-chats-show-why-disallow-is-not-noindex/583852/).

Deux détails renforcent le diagnostic. D'abord, Anthropic connaît le bon schéma : le chemin `/public/artifacts/*` est laissé crawlable dans le robots.txt et sert une balise `<meta name="robots" content="noindex, nofollow">` dans le HTML, configuration correcte qui permet à Google de lire et respecter l'instruction. Le pattern qui a échoué sur `/share/*` est donc bien une erreur, pas une méconnaissance générale ([Daniel J. Glover, 26 juillet 2026](https://danieljamesglover.com/blog/2026-07-26-shared-claude-conversations-google/)). Ensuite, un précédent est documenté : en septembre 2025, [Elephas Resources](https://elephas.app/resources/claude-shared-chats-google-indexed) rapporte qu'environ 600 conversations Claude avaient déjà été indexées par Google via le même chemin, sans qu'un correctif structurel ait été apporté depuis. Le volume exact de l'incident de juillet 2026 n'est pas quantifié publiquement au-delà de « des centaines » attribuées à un thread Reddit non vérifié indépendamment. Anthropic a mis à jour ses paramètres et a demandé aux moteurs de retirer les résultats à partir du 28 juillet ([Search Engine Land, Barry Schwartz](https://searchengineland.com/google-indexed-claude-chats-because-anthropic-didnt-block-your-private-chats-from-search-engines-483748), [Slashdot](https://yro.slashdot.org/story/26/07/28/0052221/tons-of-peoples-claude-chats-and-creations-are-exposed-on-google)).

L'implication opérationnelle SEO est doctrinale, pas conjoncturelle. Pour un consultant qui audite un site, la règle est constante : `robots.txt Disallow` empêche le crawl, jamais l'indexation. Toute directive d'indexation (`noindex` via meta ou `X-Robots-Tag`) suppose que la page soit crawlable. Si vous voulez qu'une URL ne soit pas indexée, vous devez soit laisser Googlebot la lire et servir `noindex` dessus, soit protéger la page derrière une authentification, soit la retirer entièrement. Coupler Disallow et noindex sur la même URL est un anti-pattern classique documenté depuis plus d'une décennie. Le cas Anthropic n'ajoute pas de connaissance nouvelle sur la mécanique, mais il illustre ce que produit l'erreur à grande échelle sur des URLs qui contiennent des données personnelles sensibles, générées par des utilisateurs d'un produit LLM. La différence avec un site classique est que l'unité indexée n'est plus une page éditoriale mais une conversation utilisateur.

Le sujet a été prolongé sur un plan doctrinal le 29 juillet 2026. Sur Bluesky, en réponse à une question sur des conflits de métadonnées produit posée par Sebastián Galanternik, John Mueller a écrit : « There's no publicly defined order of precedence for metadata reconciliation here – if you're giving conflicting metadata, you should fix it, not analyze if it'll work regardless » ([Search Engine Journal, Matt G. Southern, 29 juillet 2026](https://www.searchenginejournal.com/googles-mueller-fix-conflicting-metadata-dont-test-it/584055/), [Search Engine Roundtable, Barry Schwartz, 29 juillet 2026](https://www.seroundtable.com/google-precedence-metadata-conflicts-41778.html)). Le contexte immédiat concernait des conflits d'availability sur des fiches produit, mais la formulation est générale : Google ne publie pas de règle de priorité et n'a pas l'intention de le faire, parce que les poids et filtres varient. Corriger, ne pas tester. La consigne s'applique directement au pattern qui a laissé les chats Claude visibles.

Lien doctrine : ce cas complète [[concepts/e-e-a-t]] côté Trustworthiness (la crédibilité d'un opérateur LLM est diminuée quand des données personnelles utilisateur apparaissent en SERP par erreur d'indexation) et [[concepts/agentic-search]] (la sortie d'un LLM, quand elle est publiée sur le web via un lien partageable, devient un objet indexable au même titre qu'une page éditoriale, avec les mêmes règles). Il pose une question ouverte pour [[concepts/metriques-visibilite-geo]] : les moteurs de réponse générative citent-ils des URLs `claude.ai/share/*` ou `chatgpt.com/share/*` dans leurs propres réponses ? Aucune mesure publique n'existe à ce jour, la question reste à instrumenter.

Prédictions :

- P-2026-07-30-1 : au moins un autre opérateur d'agent conversationnel de premier plan (OpenAI, Google Gemini, Microsoft Copilot, Perplexity) sera documenté publiquement avec un cas d'indexation involontaire de conversations partagées liées à un même conflit `Disallow` + `noindex` avant le 30 juin 2027 (confidence 0,45).
- P-2026-07-30-2 : Anthropic publiera dans un billet officiel ou un post-mortem d'incident un compte précis du nombre de conversations `/share/*` indexées par Google entre le 25 et le 28 juillet 2026 avant le 31 décembre 2026 (confidence 0,20).
- P-2026-07-30-3 : Google mettra à jour publiquement sa page primaire `developers.google.com/search/docs/crawling-indexing/robots-meta-tag` avec un exemple explicite du conflit `Disallow` + `X-Robots-Tag: none` avant le 31 mars 2027 (confidence 0,25).

---

## Brève 1 — Business SEO — Meta Q2 2026 : Advantage+ atteint un run rate annualisé de 75 Md USD, 1 million d'entreprises utilisent les Business Agents chaque semaine

Meta a publié le 29 juillet 2026 après clôture des marchés US ses résultats du deuxième trimestre 2026 : chiffre d'affaires 60,8 Md USD, en hausse de 28 pct sur un an, dépassant le consensus, avec un résultat net de 15,848 Md USD en baisse de 14 pct sur un an et un bénéfice par action de 6,18 USD sous le consensus à 7,22 USD. Le titre a perdu 9,64 pct en après-marché sur la révision à la hausse du capex annuel (fourchette 130-145 Md USD contre 125-145 précédemment). Sources : [Meta PR Newswire](https://www.prnewswire.com/news-releases/meta-reports-second-quarter-2026-results-302838214.html), [Investing.com](https://www.investing.com/news/company-news/meta-q2-2026-slides-revenue-surges-28-as-ai-spending-pressures-profits-93CH-4821966), [StockTitan](https://www.stocktitan.net/news/META/meta-reports-second-quarter-2026-hkjfhayj8l0v.html), [InfoTechLead](https://infotechlead.com/digital/meta-q2-2026-revenue-jumps-28-to-60-8-bn-as-ai-capex-reaches-31-1-bn-and-user-base-hits-3-6-bn-97368), [GuruFocus](https://www.gurufocus.com/news/8988880/meta-platforms-inc-meta-q2-2026-earnings-call-highlights-revenue-surges-28-to-608-billion-but-heavy-ai-spending-pressures-margins).

Trois chiffres pertinents pour un consultant SEO/GEO. La suite publicitaire pilotée par IA Advantage+ a atteint un run rate annualisé de 75 Md USD ce trimestre selon la présentation aux analystes ([Investing.com](https://www.investing.com/news/company-news/meta-q2-2026-slides-revenue-surges-28-as-ai-spending-pressures-profits-93CH-4821966), [InfoTechLead](https://infotechlead.com/digital/meta-q2-2026-revenue-jumps-28-to-60-8-bn-as-ai-capex-reaches-31-1-bn-and-user-base-hits-3-6-bn-97368)). Plus de 9 millions de petites entreprises ont utilisé au moins un outil publicitaire génératif de Meta au cours du trimestre, avec adoption de l'outil de génération d'images plus que doublée sur trois mois. Les Business Agents Meta, déjà comptés à 1 M+ entreprises fin juillet dans des reprises tierces couvertes en brève B3 de l'édition du 28 juillet 2026, sont désormais confirmés officiellement à plus d'un million d'entreprises utilisatrices chaque semaine sur WhatsApp et Messenger.

Meta chiffre en outre l'apport LLM sur ses signaux publicitaires : +8,3 pct de clics publicitaires et +15,7 pct de conversions attribués aux améliorations des systèmes de recommandation Facebook liées aux modèles de langage sur le trimestre ([Investing.com](https://www.investing.com/news/company-news/meta-q2-2026-slides-revenue-surges-28-as-ai-spending-pressures-profits-93CH-4821966)). Ce sont les premiers chiffres officiels d'un opérateur publicitaire à cette échelle qui isolent une contribution LLM sur les métriques de conversion, ce qui répond partiellement à la prédiction ouverte P-2026-07-28-5 (audit tiers Meta Business Agents restant en attente). Guidance Q3 2026 : 61-64 Md USD, croissance dans le milieu à haut de la fourchette 20 pct, effet de change défavorable estimé à -1 pct.

Lien doctrine : [[concepts/data-proprietaire]] (Meta expose des métriques d'attribution internes que peu d'annonceurs peuvent recouper), [[concepts/tabou-visibilite]] (chiffre Advantage+ 75 Md USD run rate = résultat mesurable, distinct d'une métrique de « visibilité »).

Prédiction : P-2026-07-30-4 : un troisième trimestre consécutif de croissance du run rate Advantage+ au-dessus de 70 Md USD annualisé sera publié au T3 2026 le 29 octobre 2026 (confidence 0,55).

---

## Brève 2 — Actualité SEO — John Mueller sur Bluesky, 29 juillet : corriger un conflit de métadonnées, ne pas tester son comportement

En réponse à une question de Sebastián Galanternik sur des conflits d'availability entre l'affichage produit, le HTML servi et les données structurées de fiches en free listings, John Mueller a écrit sur Bluesky le 29 juillet 2026 : « There's no publicly defined order of precedence for metadata reconciliation here – if you're giving conflicting metadata, you should fix it, not analyze if it'll work regardless » et « All of these can have different weights & filters, plus they'll change over time » ([Search Engine Journal, Matt G. Southern, 29 juillet 2026](https://www.searchenginejournal.com/googles-mueller-fix-conflicting-metadata-dont-test-it/584055/), [Search Engine Roundtable, Barry Schwartz, 29 juillet 2026](https://www.seroundtable.com/google-precedence-metadata-conflicts-41778.html), [Optimixed reprise](https://www.optimixed.com/google-does-not-publish-searchs-precedence-for-metadata-during-conflicts/)).

Trois conflits sont cités dans le fil : availability produit (page vs HTML vs feed), valeurs de date (date visible vs `dateModified` vs `lastmod` sitemap) et prix (page vs feed vs schema). Mueller confirme qu'il n'existe pas d'ordre de priorité publié et que Google n'a pas prévu d'en publier un, parce que les poids et filtres varient et évoluent. La consigne opérationnelle est directe : lever le conflit à la source, ne pas s'en remettre à un arbitrage interne mal documenté. La déclaration recouvre le cas Anthropic Claude de l'info du jour, mais elle s'applique en priorité aux fiches produit e-commerce où trois surfaces (site, HTML, feed Merchant Center) coexistent et doivent servir la même vérité.

Lien doctrine : [[concepts/product-led-seo]] pour les fiches produit e-commerce, [[concepts/e-e-a-t]] côté Trustworthiness (cohérence des métadonnées comme signal de fiabilité).

---

## Brève 3 — Actualité SEO — Bing teste l'affichage du prix directement sur les images produits en résultats organiques

Barry Schwartz a repéré le 29 juillet 2026 un test de Microsoft Bing dans les résultats organiques : l'affichage du prix apparaît désormais superposé sur l'image produit elle-même, et non plus sous l'image à côté des étoiles de notation comme actuellement. Un second test associé montre deux rangées d'images produits sous un même bloc résultat. Sources : [Search Engine Roundtable, Barry Schwartz](https://www.seroundtable.com/bing-pricing-product-images-41765.html), [Optimixed reprise](https://www.optimixed.com/microsoft-bing-testing-pricing-on-product-images/).

Le test est repéré en organique, distinct des formats Bing Shopping Ads payants. Aucune capture d'écran n'est fournie par le repérage, aucun périmètre géographique n'est communiqué, aucune adoption n'est mesurée à ce stade. Le déplacement du prix sur l'image place l'information d'achat au même niveau visuel que l'image du produit, ce qui pourrait modifier le comportement de clic sur les résultats produits en organique Bing, sans que le sens de la variation (positif ou négatif pour l'éditeur produit) soit établi.

Lien doctrine : [[concepts/passage-ranking]] au sens élargi (le prix affiché sur l'image devient un composant lisible en aperçu du résultat, comparable à un extrait de contenu qualifiant la fiche produit avant clic).

Prédiction : P-2026-07-30-5 : Microsoft Bing publiera l'affichage du prix sur image produit en général availability sur au moins un marché (US, UK, DE, FR) avant le 31 mars 2027 (confidence 0,40).

---

*Draft SyntheticBrain. Rien n'a été envoyé.*
