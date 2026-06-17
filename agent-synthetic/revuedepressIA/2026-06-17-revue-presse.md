---
date: 2026-06-17
edition: 2026-06-17
pilier: GEO
agent: SyntheticBrain
voix: synthetic
status: draft
---

# Algorithme — édition du 17 juin 2026

Bing ouvre quatre métriques de visibilité GEO en preview globale, le toggle opt-out CMA britannique entre en service côté Google, Meta installe un AI Mode dans Facebook Search et 31 éditeurs UK lancent un contrat de scraping payant à 500 livres l'article. La mesure de la citation devient un objet outillé chez deux moteurs ; la friction réglementaire et contractuelle remonte côté éditeurs.

## En tête (3 à 5 points capitaux)

- Bing Webmaster Tools ouvre **Intents, Topics, Citation Share et Compare** en preview globale le 16 juin, première mesure officielle de la part de citation d'un site dans les réponses générées par Bing et Copilot ([blog Bing](https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare), [Search Engine Land](https://searchengineland.com/bing-webmaster-tools-updates-ai-reporting-with-intents-topics-citation-share-and-compare-480277), [Search Engine Journal](https://www.searchenginejournal.com/bing-rolls-out-ai-citation-share-in-webmaster-tools/579547/)).
- Le toggle Google **Search Console permettant aux éditeurs UK de sortir d'AI Overviews, d'AI Mode et d'AI Overviews dans Discover entre en vigueur aujourd'hui 17 juin**, sans impact déclaré sur le classement organique et sans application à Gemini standalone ([PPC Land](https://ppc.land/google-reacts-to-uk-order-with-a-search-console-ai-opt-out-toggle/), [TechCrunch](https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/), [Computing](https://www.computing.co.uk/news/2026/google-to-let-publishers-opt-out-of-ai-search-features-while-remaining-in-search-results)).
- **Meta installe AI Mode dans Facebook Search** le 16 juin, réponses générées à partir des Groups, Reels et posts publics de l'écosystème Meta, sans documentation publique du mode de sélection des sources ([Search Engine Land](https://searchengineland.com/meta-ai-mode-facebook-search-480393)).
- **Le Movement for an Open Web lance les Search-Only Contracts** le 15 juin avec 31 éditeurs UK et un tarif standard de 500 livres par article scrapé, recouvrement via Moneyclaim.gov.uk à environ 50 livres de frais ([PPC Land](https://ppc.land/uk-publishers-bill-ai-scrapers-500-per-article-using-county-courts/), [Press Gazette](https://pressgazette.co.uk/news/publishers-to-bill-ai-firms-for-unwanted-scraping-and-take-them-to-court-if-they-dont-pay/)).

---

## Info du jour — pilier GEO

### Bing Webmaster Tools ouvre quatre métriques de visibilité GEO en preview globale

Le 16 juin 2026, Microsoft a annoncé la mise en preview globale de quatre nouvelles fonctions d'AI Performance dans Bing Webmaster Tools : Intents, Topics, Citation Share, Compare. L'annonce est signée Krishna Madhavan, Meenaz Merchant, Saral Nigam et Trishna Shah, product managers Microsoft AI, sur le [blog Bing](https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare). [Search Engine Land](https://searchengineland.com/bing-webmaster-tools-updates-ai-reporting-with-intents-topics-citation-share-and-compare-480277) (Barry Schwartz) et [Search Engine Journal](https://www.searchenginejournal.com/bing-rolls-out-ai-citation-share-in-webmaster-tools/579547/) (Matt G. Southern) rapportent le déploiement le même jour. Les quatre fonctions sortent en preview pour tous les comptes Bing Webmaster Tools, sur l'ensemble des marchés où le dashboard AI Performance était disponible depuis février 2026.

**Citation Share.** La métrique affiche le pourcentage de citations attribuées à votre site sur l'ensemble des citations affichées par Bing et Copilot pour une grounding query donnée. Si Bing affiche dix sources pour une requête et que votre site est cité trois fois, la métrique vaut 30 %. Microsoft décrit cette mesure comme « observational, not competitive » : elle n'expose ni le nom des sites concurrents ni leur trafic. C'est la première mesure officielle de part de citation publiée par un moteur, sept jours après l'effectivité du toggle d'opt-out côté Google (brève 1).

**Intents.** Une classification des grounding queries en huit familles visibles à ce stade : Informational, Commercial, Navigational, Learn and Solve, Research, Creation, Local, et « more ». La taxonomie complète n'est pas encore publiée. Search Engine Journal a documenté un total de 15 catégories prévues, sur la base d'une présentation Krishna Madhavan au SEO Week New York d'avril 2026. Microsoft précise que la classification reste en maturation : « Intents and Topics classifications are still maturing ».

**Topics.** Un regroupement de grounding queries en clusters thématiques. Exemple donné par Microsoft : « solar panels », « solar energy efficiency » et « residential solar installation » sont regroupés sous un topic « Solar Energy ». Cette agrégation rapproche l'unité de mesure côté éditeur de celle qu'utilise un agent générateur, qui ne raisonne pas par mot-clé exact mais par concept.

**Compare.** Une fonction de comparaison période contre période. Vous pouvez superposer 30 jours glissants avec les 30 jours précédents, ou définir des plages personnalisées. C'est la première fonction de Bing Webmaster Tools qui permet de mesurer une dérive temporelle de la citation IA sur son propre périmètre.

**Pourquoi ce déploiement compte.** Bing devient le premier moteur grand public à publier une métrique de part de citation par requête, avec un caveat explicite : la mesure est observational, elle ne révèle pas les concurrents et n'est pas un score de classement. Cette précaution méthodologique rejoint la doctrine [[concepts/metriques-visibilite-geo]] : la mesure choisie détermine la conclusion, et exposer un classement comparatif aurait recréé un système de positions équivalent au ranking organique. Microsoft assume une position de mesure de visibilité brute, sans classement.

L'écart avec Google Search Console reste net. GSC a ouvert ses AI performance reports le 3 juin 2026 pour un sous-ensemble d'éditeurs UK, avec une métrique d'impressions et de clics dans les AI features, sans équivalent de Citation Share par grounding query. Microsoft ouvre une seconde dimension : non plus seulement « combien de fois mon site a été vu dans une réponse IA », mais « quelle part des sources citées sur cette grounding query mon site représente ». Cette dimension manquait dans la trousse Google.

**Limites documentées.** Microsoft ne publie pas la méthodologie de calcul de Citation Share au-delà de la formule de ratio. La taxonomie complète des Intents et la logique d'attribution des Topics restent opaques. La mention « still maturing » suggère un signal instable les premiers mois. La couverture est Bing et Copilot uniquement, pas ChatGPT (qui s'appuie pourtant en partie sur l'index Bing). [Launchcodex](https://launchcodex.com/blog/seo-geo-ai/bing-webmaster-tools-ai-citation-share-geo/) note que la mesure ne couvre pas non plus les citations OpenAI alimentées par Bing : la part Citation Share est une mesure de visibilité dans les surfaces Microsoft, pas dans l'écosystème Bing au sens large.

**Implication opérationnelle.** Pour un éditeur ou une marque, deux signaux exploitables dès demain. Premièrement, mesurer la Citation Share par Intent et par Topic permet d'identifier les zones de surreprésentation (où votre marque domine 40 % des citations sur une grounding query) et les zones d'invisibilité (où votre site est absent malgré un classement organique fort). Deuxièmement, l'angle Compare ouvre la mesure de l'impact d'une publication ou d'un repackaging de contenu sur la Citation Share, en dehors du référentiel d'impressions et de clics classique. Le test concret : suivre 30 jours, modifier un titre ou ajouter une section ancrée, comparer les 30 jours suivants. C'est la première fois qu'un moteur outille cette boucle.

**Lien doctrine.** La preview officialise une seconde dimension de la mesure de visibilité GEO, à côté des trois métriques formalisées par [[concepts/metriques-visibilite-geo]] (Imp_wc, Imp_pos, Subjective Impression). Citation Share s'inscrit dans la même famille observationnelle, mais opère au niveau requête plutôt qu'au niveau réponse. Pour [[concepts/structural-information-geo]], la grounding query devient l'unité de mesure de l'optimisation des champs structurels (title, meta, headings, schema) : on ne mesure plus « est-ce que mon schéma classe », on mesure « est-ce que mon schéma me fait monter en Citation Share sur la grounding query qui me concerne ». Pour [[concepts/agentic-search]], le découpage Intents/Topics fournit le premier mapping public d'une intention agentique côté éditeur.

---

## Brèves

### Brève 1 — Pilier Actualité SEO. Le toggle opt-out Google Search Console entre en vigueur aujourd'hui pour les éditeurs UK

Annoncée le 3 juin 2026, l'option du Search Console permettant aux éditeurs britanniques de retirer leur contenu d'AI Overviews, d'AI Mode et d'AI Overviews dans Discover entre en vigueur aujourd'hui 17 juin 2026. [PPC Land](https://ppc.land/google-reacts-to-uk-order-with-a-search-console-ai-opt-out-toggle/) (Luis Rijo, 3 juin), [TechCrunch](https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/) (3 juin) et [Computing](https://www.computing.co.uk/news/2026/google-to-let-publishers-opt-out-of-ai-search-features-while-remaining-in-search-results) (3 juin) ont documenté la fenêtre. La fonction est testée d'abord sur un sous-ensemble d'éditeurs UK, sous l'ordre contraignant émis par la Competition and Markets Authority le 3 juin 2026 dans le cadre du Digital Markets, Competition and Consumers Act 2024.

Trois points à retenir. Premièrement, l'opt-out ne s'applique pas à Gemini standalone : un éditeur qui retire son contenu peut continuer à voir ses URL surgir dans des réponses Gemini hors Search. Deuxièmement, Google déclare que l'activation du toggle n'affectera pas le classement dans Search classique. Troisièmement, la question de l'interaction avec les Information Agents (déployés globalement le 12 juin pour les abonnés Google AI Ultra) n'a pas été documentée publiquement par Google au 16 juin. La fenêtre de mesure de l'adoption s'ouvre aujourd'hui : Press Gazette, CMA reporting et SISTRIX seront à surveiller dans les sept jours, sur la base d'une intention déclarée de 33,2 % des éditeurs interrogés par Search Engine Land en mai. Google doit livrer les contrôles substantiels d'ici décembre 2026 et les contrôles page-level d'ici mars 2027.

### Brève 2 — Pilier GEO. Meta lance AI Mode dans Facebook Search

Le 16 juin, Meta a déployé un AI Mode dans Facebook Search. La fonction génère une réponse en langage naturel à partir des posts publics, des Groups et des Reels de l'écosystème Meta. [Search Engine Land](https://searchengineland.com/meta-ai-mode-facebook-search-480393) (Danny Goodwin, 16 juin) rapporte que Meta n'a pas publié la logique de sélection des contenus inclus dans une réponse. Aucune date de bascule globale n'est publiée, aucune liste de régions ou de langues n'est fournie, aucune procédure d'opt-out éditeur externe n'est documentée.

L'angle SEO est étroit, et c'est précisément ce qui en fait un fait à suivre. Facebook Search n'a jamais été un moteur de découverte ouvert : la nouveauté est qu'une réponse générative repose désormais sur l'index propriétaire Meta, sans rappel des sources publiques tierces. Pour une marque qui dépendait du classement Facebook (pages, fiches lieux, posts publics), la métrique pertinente passe de « rank dans la timeline Search » à « apparition dans la réponse AI Mode ». Pour les marques qui ne dépendaient pas de Facebook Search, l'effet est nul à court terme. La question de la portée réelle d'un tel moteur de découverte fermé reste ouverte ; aucun chiffre d'usage n'a été publié par Meta. Un rapprochement nominal avec Google AI Mode est tentant mais trompeur : Meta s'appuie sur son index social, Google sur l'index web. Les deux objets ne se substituent pas.

### Brève 3 — Pilier Actualité SEO. Le Movement for an Open Web lance les Search-Only Contracts à 500 livres l'article

Le 15 juin 2026, le Movement for an Open Web (MOW) a publié les Search-Only Contracts, un cadre contractuel adopté par 31 éditeurs UK fondateurs, dont Candr Media (Trusted Reviews), F-At (road.cc, off.road.cc, ebiketips.co.uk). [PPC Land](https://ppc.land/uk-publishers-bill-ai-scrapers-500-per-article-using-county-courts/) (Luis Rijo, 15 juin) et [Press Gazette](https://pressgazette.co.uk/news/publishers-to-bill-ai-firms-for-unwanted-scraping-and-take-them-to-court-if-they-dont-pay/) (Dominic Ponsford, 15 juin) ont documenté le lancement.

Le mécanisme tient en trois pièces. Premièrement, l'éditeur ajoute des conditions contractuelles dans son robots.txt et ses conditions d'utilisation, qui interdisent le copiage de contenu pour entraîner ou alimenter un modèle génératif, hors indexation Search. Deuxièmement, l'éditeur prouve l'usage en interrogeant le chatbot suspecté et en enregistrant la réponse comme élément de preuve. Troisièmement, l'éditeur facture 500 livres par article et, en cas de non-paiement, dépose une plainte à Moneyclaim.gov.uk pour environ 50 livres de frais, traitée en county court small claims sans recours obligatoire à un avocat spécialisé. Tim Cowen, cofondateur MOW : « This is a straightforward approach to dealing with the complexities of payment for content online ». Chris Dicker, CEO Candr Media : « For too long the AI companies have had a free hand to steal our content, traffic and IP ». L'Association of Online Publishers, la Professional Publishers Association, Thinkbox, Impress et la Football Writers' Association soutiennent l'initiative.

C'est la première tentative de mise en place d'un tarif standard public adossé à un mécanisme de recouvrement accessible aux petits éditeurs. La barre d'entrée juridique passe d'un litige IP (plusieurs dizaines de milliers de livres, plusieurs années) à un small claim (50 livres, quelques semaines). Aucune réponse publique d'OpenAI, de Google ou d'Anthropic au 15 juin. Les premières affaires attendues à l'automne donneront un signal sur la portée réelle du dispositif, qui dépend de la qualité de la preuve par interrogation directe du chatbot, point qui n'a pas encore été testé devant un county court britannique.

---

## Hypothèses et prédictions ajoutées ce run

- **P-2026-06-17-1** : au moins une étude indépendante publie une mesure de Citation Share sur 100+ sites pendant la preview Bing Webmaster Tools, avec décomposition par Intent et par Topic, avant 31 décembre 2026.
- **P-2026-06-17-2** : Google ajoute une métrique équivalente de part de citation par grounding query à GSC AI performance reports avant 31 décembre 2026, en réponse au déploiement Microsoft.
- **P-2026-06-17-3** : au moins une décision en small claims court UK statue sur la validité d'un Search-Only Contract dans le cadre du dispositif MOW avant 31 mars 2027.

## Sources mobilisées

- [Bing blog — New AI Visibility Insights in Bing Webmaster Tools](https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare) (Krishna Madhavan, Meenaz Merchant, Saral Nigam, Trishna Shah, 16 juin 2026, primaire)
- [Search Engine Land — Bing Webmaster Tools updates AI reporting](https://searchengineland.com/bing-webmaster-tools-updates-ai-reporting-with-intents-topics-citation-share-and-compare-480277) (Barry Schwartz, 16 juin 2026)
- [Search Engine Journal — Bing Rolls Out AI Citation Share](https://www.searchenginejournal.com/bing-rolls-out-ai-citation-share-in-webmaster-tools/579547/) (Matt G. Southern, 16 juin 2026)
- [Launchcodex — Bing Webmaster Tools just made GEO measurable](https://launchcodex.com/blog/seo-geo-ai/bing-webmaster-tools-ai-citation-share-geo/)
- [PPC Land — Google reacts to UK order with a Search Console AI opt-out toggle](https://ppc.land/google-reacts-to-uk-order-with-a-search-console-ai-opt-out-toggle/) (Luis Rijo, 3 juin 2026)
- [TechCrunch — Publishers will be able to opt out of AI Search, thanks to new regulation](https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/) (3 juin 2026)
- [Computing — Google to let publishers opt out of AI Search features while remaining in search results](https://www.computing.co.uk/news/2026/google-to-let-publishers-opt-out-of-ai-search-features-while-remaining-in-search-results) (3 juin 2026)
- [Search Engine Land — Meta launches AI Mode in Facebook search to answer questions](https://searchengineland.com/meta-ai-mode-facebook-search-480393) (Danny Goodwin, 16 juin 2026)
- [PPC Land — UK publishers bill AI scrapers £500 per article using county courts](https://ppc.land/uk-publishers-bill-ai-scrapers-500-per-article-using-county-courts/) (Luis Rijo, 15 juin 2026)
- [Press Gazette — Publishers to bill AI firms for unwanted scraping and take them to court if they don't pay](https://pressgazette.co.uk/news/publishers-to-bill-ai-firms-for-unwanted-scraping-and-take-them-to-court-if-they-dont-pay/) (Dominic Ponsford, 15 juin 2026)
