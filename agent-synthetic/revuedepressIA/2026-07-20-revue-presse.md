# Algorithme. 2026-07-20

## Résumé

- Un papier Sprinklr présenté à SIGIR 2026 (Melbourne, ouverture ce 20 juillet) mesure ce qui fait qu'un moteur IA cite une source plutôt qu'une autre sur 252 000 essais et 6 modèles. Quatre facteurs dominent partout : pertinence topique, prix affiché, horodatage récent, position 1 vs position 2 dans le contexte injecté.
- Le finding « horodatage récent aide de façon consistante » entre en tension explicite avec l'étude Digital Applied (fraîcheur non prédicteur après contrôle d'autorité de domaine, prédiction ouverte P-2026-06-01-v3-2).
- L'édition contredit le raccourci fréquent selon lequel le formatage seul (bullets, gras, encadrés) déplace les citations : sur ce protocole contrôlé, les changements de forme purs n'ont pratiquement pas d'effet.
- Brève : SurfacedBy publie 127 198 citations mesurées sur 5 moteurs IA sur 11 647 domaines. Les moteurs ne s'accordent que sur 2,7 pct des domaines. Étude mono-source à traiter comme direction attribuée.
- Brève : volatilité SERP Google élevée mi-juillet (11 et 18) sans confirmation Google. Seroundtable documente le 11 juillet, un observateur secondaire documente le 18. Fenêtre d'audit à ouvrir avant d'attribuer un mouvement à un changement de site.

## Info du jour. GEO / mesure cross-engine. Ce qu'un protocole contrôlé mesure, quand deux sources se disputent la citation

Pilier de l'édition : **GEO / search IA**.

**Le fait, daté.** Rahul Vishwakarma, Shushant Kumar et Ratnesh Jamidar (Sprinklr) publient sur arXiv le 25 mai 2026 le papier « What Gets Cited: Competitive GEO in AI Answer Engines » ([arXiv:2605.25517](https://arxiv.org/abs/2605.25517)). Le papier est présenté cette semaine à la 49e conférence ACM SIGIR (20-24 juillet 2026, Melbourne), publié aux actes ACM ([doi:10.1145/3805712.3808445](https://doi.org/10.1145/3805712.3808445)). SIGIR reste la conférence de référence en recherche d'information, ce qui donne au papier une visibilité pratique dans la communauté qui construit les moteurs de réponse.

**Ce qui est mesuré.** Les auteurs construisent un banc d'essai RAG à deux documents : ils injectent dans le contexte du modèle exactement deux sources candidates différant sur un seul facteur à la fois, puis mesurent laquelle des deux le modèle cite en premier dans sa réponse. 100 blogs produits anonymisés couvrant 50 catégories B2C fournissent la base. 1 440 scénarios sont générés, chacun décliné en 3 paraphrases (4 320 paires scénario-requête), avec ordre des sources contre-balancé pour isoler le biais de position. Cinq tirages répétés par condition portent le total à 252 000 essais. Six modèles sont testés : Gemini 2.5 Flash, GPT-5 Nano, GPT-5 Mini, GPT-5.2, Claude 3.5 Sonnet, Kimi K2 Thinking.

**Les 4 facteurs qui dominent partout.** Sur les 18 facteurs testés, quatre produisent un effet unanime dans les 6 modèles, avec un odds ratio (OR) très supérieur à 100 : (a) la non-correspondance topique entre requête et source, (b) l'absence d'information de prix explicite, (c) un horodatage ancien vs récent, (d) la position dans le contexte (position 1 vs position 2 des deux documents injectés). Les auteurs les qualifient de « gatekeeper factors » (facteurs de passage) : si une source y échoue, elle perd la citation même quand tout le reste est bon.

**Les facteurs secondaires.** Cinq autres facteurs produisent un effet significatif dans 4 modèles ou plus, avec des OR variables entre modèles : spécifications manquantes (OR 8,6 à 243), lacunes de mots-clés (OR 6 à 40), langage prudent (« it might », « peut-être ») vs affirmatif (OR 2,7 à 754), affirmations sans preuve chiffrée (OR 2,1 à infini), absence de comparaison offerte (OR 1,6 à 7,5). Deux modèles se comportent en tout-ou-rien (Gemini 2.5 et Claude 3.5 activent 67 à 78 pct de leurs facteurs significatifs avec OR supérieur à 10 000). Kimi K2 Thinking est le plus sensible (83 pct des facteurs significatifs). La famille GPT est stable à travers ses variantes.

**Le facteur qui n'a pas d'effet.** Les modifications de forme pures (bullet vs prose, gras présent ou absent, encadré vs paragraphe continu) n'ont pratiquement pas d'effet sur la sélection de citation dans ce protocole. C'est un point rare, à noter : plusieurs guides GEO recommandent de reformater son contenu comme premier travail d'optimisation. Sur ce banc d'essai, ce reformatage ne rapporte rien s'il n'est pas accompagné d'un travail sur les 4 facteurs de passage.

**Le désaccord ouvert entre études.** Le finding « horodatage récent aide de façon consistante » entre en tension avec l'étude [Digital Applied juin 2026](https://www.digitalapplied.com/blog/ai-search-citation-ranking-factors-2026-data-study) selon laquelle la fraîcheur ne prédit pas la citation AIO une fois l'autorité de domaine contrôlée. La différence de protocole explique probablement l'écart : Vishwakarma isole la fraîcheur toutes choses égales par ailleurs sur un banc RAG à deux sources, Digital Applied observe la corrélation en conditions naturelles où l'autorité et la fraîcheur sont corrélées. Les deux mesurent des grandeurs différentes. La prédiction ouverte [[predictions#P-2026-06-01-v3-2]] (fraîcheur reste contestée après contrôle d'autorité, fin 2026) n'est pas résolue par Vishwakarma, mais elle devient plus lisible : la question n'est pas « est-ce que la fraîcheur aide » (oui, en contrôle contrefactuel), mais « combien reste-t-il d'effet fraîcheur quand un site autoritaire ancien et un site récent moyen se disputent la citation en conditions réelles ». Ce n'est plus la même question.

**Angle SEO/GEO.** Pour un consultant qui audit une page qui perd des citations sur ChatGPT, Perplexity, Gemini ou Google AI Mode, la grille de lecture est utilisable telle quelle. Vérifier d'abord les 4 facteurs de passage (pertinence topique visible dès l'intro, prix affiché quand la page vend, date de mise à jour explicite, position vraisemblable au retrieval mesurée par un audit d'ordre des sources renvoyées). Ensuite les facteurs secondaires (spécifications concrètes, vocabulaire affirmatif dans les phrases centrales, chiffres et preuves plutôt que promesses, comparaisons explicites avec au moins une alternative nommée). Ne pas passer 3 semaines sur du reformatage de bullets seul : ce protocole indique que le gain attendu est proche de zéro.

**Lien avec la doctrine du wiki.**

- [[concepts/metriques-visibilite-geo]] : le protocole à deux documents mesure directement `Imp_pos` (position pondérée) en isolation. Le finding « position 1 vs 2 est un facteur unanime » chiffre ce qui restait qualitatif dans la fiche : la pondération décroissante par position n'est pas une intuition, c'est un facteur premier dans la sélection.
- [[concepts/fraicheur-contenu]] : la fiche marque un chiffre grand public (« contenu de moins de 3 mois cité 3 fois plus »). Vishwakarma confirme la direction en contrôle contrefactuel et documente le désaccord avec Digital Applied en conditions naturelles. La fiche doctrine passe de `confidence: medium` à `confidence: medium-high` sur la partie « en contrôle contrefactuel », `confidence: low` sur la partie « en conditions naturelles ».
- [[concepts/structural-information-geo]] : le finding « la forme seule n'a pas d'effet » recoupe côté RAG le finding SAGEO Arena « body text seul ne suffit pas ». Deux protocoles différents, même verdict de premier ordre : ce qui compte n'est pas le maquillage du corps, c'est le signal porté par les champs structurels et par le contenu factuel.
- [[concepts/grounding-score]] : le facteur « pertinence topique » est la mesure canonique du grounding sur ce banc. Vishwakarma rend visible que la similarité cosinus intention/page n'est pas décorative : quand deux sources sont injectées ensemble, celle qui rate le topique perd la citation même si tout le reste va bien.

**Limites documentaires.**

1. Le banc d'essai est contrôlé : deux sources injectées à la fois, un facteur qui varie, ordre contre-balancé. Ce n'est pas le protocole du retrieval réel où N sources arrivent, avec des interactions entre elles. Les OR mesurés ne se transposent pas 1 pour 1 en gain de citation observable sur ChatGPT ou Gemini en production.
2. Les 100 blogs produits anonymisés couvrent 50 catégories B2C. Le résultat ne dit rien sur les requêtes YMYL santé, sur les requêtes B2B techniques longues, ni sur les requêtes info-only sans intention d'achat.
3. Le pilote interne Sprinklr est mentionné qualitativement (« retour positif des équipes ») sans chiffre. À lire comme signal de mise en pratique, pas comme mesure.
4. Un des modèles testés (Claude 3.5 Sonnet) date d'octobre 2024 et n'est plus la version courante. Les auteurs n'incluent pas Claude Opus 4.6/4.8 ni Fable 5. Les résultats concernent le modèle testé, pas la famille entière.

**Prédictions ouvertes ce run.**

- P-2026-07-20-1 : d'ici le 31 mars 2027, une équipe universitaire ou vendor publie une reproduction du banc à deux documents Vishwakarma sur un panel étendu (au moins Claude Opus 4.6 ou 4.8, GPT-5.5 ou 5.6, Gemini 3.5, et un modèle open source) avec les 4 facteurs de passage confirmés ou invalidés explicitement.
- P-2026-07-20-2 : d'ici le 31 décembre 2026, une étude en conditions réelles (retrieval multi-sources, requêtes en production sur au moins 3 moteurs) tranche le désaccord « effet fraîcheur en contrôle contrefactuel vs en conditions naturelles » avec un chiffre comparable à Vishwakarma et Digital Applied sur au moins un vertical B2C.
- P-2026-07-20-3 : d'ici le 30 septembre 2026, un éditeur d'outil GEO grand public (Peec AI, Semrush AI Visibility Toolkit, Athena Intelligence, Profound, Ahrefs Brand Radar) reprend la grille des 4 facteurs de passage Vishwakarma comme dimension explicite d'audit dans son produit.

---

## Brèves

### Brève 1. GEO / mesure. SurfacedBy publie 127 198 citations mesurées sur 5 moteurs IA, avec 2,7 pct d'accord entre eux

Ali Khallad (SurfacedBy) publie le 27 juin 2026, mise à jour le 8 juillet, une étude de 16 400 réponses IA collectées entre le 29 mars et le 27 juin 2026 sur ChatGPT, Claude, Gemini, Perplexity et Google AI Mode. Elle totalise 127 198 citations vers 11 647 domaines distincts, sur requêtes d'intention commerciale (acheteur, catégorie de produit) ([surfacedby.com](https://surfacedby.com/blog/ai-citation-study-engine-overlap)).

Les chiffres reportés :

- Nombre moyen de sources par réponse : Gemini 11,0. Perplexity 8,6. Google AI Mode 7,8. Claude 6,8. ChatGPT 3,7.
- Recouvrement entre moteurs : 69,6 pct des domaines cités le sont par un seul moteur, 16,3 pct par deux, 7,4 pct par trois, 4,1 pct par quatre, 2,7 pct (309 domaines) par les 5.
- Répartition par type de source : vendor / produit / longue traîne 90,6 pct. YouTube 4,9 pct. Reddit 1,8 pct. GitHub 0,7 pct. Wikipedia sous 0,6 pct.
- YouTube par moteur : Google AI Mode 11,2 pct. Perplexity 8,8 pct. Gemini 2,2 pct. ChatGPT 1,6 pct. Claude 0,0 pct.
- Concentration : les 10 domaines les plus cités totalisent 20,6 pct des citations, les 100 premiers 42 pct. 42,9 pct des domaines cités ne le sont qu'une seule fois sur toute la période.

**Portée et limites.** SurfacedBy est un éditeur d'outil de mesure de visibilité IA. L'étude est mono-source (aucune reprise éditoriale tierce à date de rédaction), sur périmètre commercial (les mix changeraient sur santé, actualité ou général), sur une fenêtre de trois mois. Traiter comme direction attribuée à SurfacedBy, pas comme valeur consensus. Le finding « 2,7 pct d'accord entre 5 moteurs » recoupe cependant en direction le finding cross-engine plus ancien (69 pct pas d'accord vs 31 pct au moins deux moteurs). L'écart entre Claude (0 pct YouTube) et Google AI Mode / Perplexity (11 et 9 pct) est le point exploitable : quand un audit client dépend disproportionnellement de YouTube, ses citations sur Claude seront nulles à design.

**Angle GEO.** À croiser avec Vishwakarma info du jour : SurfacedBy mesure la répartition observée en production. Vishwakarma mesure les mécaniques qui produisent une citation à conditions contrôlées. Les deux ensemble donnent une grille de travail : appliquer la grille Vishwakarma (facteurs de passage + facteurs secondaires) sur les sources qui, selon SurfacedBy, dominent le mix moteur-cible du client.

Sources : [SurfacedBy](https://surfacedby.com/blog/ai-citation-study-engine-overlap).

### Brève 2. Actualité SEO. Volatilité SERP Google mi-juillet, deux fenêtres non confirmées à documenter avant d'agir

Search Engine Roundtable publie le 11 juillet 2026 sur une volatilité observée cette semaine-là ([SE Roundtable 41676](https://www.seroundtable.com/google-search-ranking-volatility-july-11th-41676.html)), avec des tracker tiers relayant un mouvement inhabituel. Barry Schwartz qualifie le mouvement d'unconfirmed, sans annonce Google, sans corrélation évidente avec un déploiement documenté. Un observateur secondaire ([digitalphablet.com 19 juillet](https://digitalphablet.com/digital-marketing/weekend-google-search-rankings-fluctuations-july-18th-update/)) documente une seconde fenêtre autour du 18 juillet en croisant 10 tracker (AccuRanker, Algoroo, Mozcast, SEMrush, Serpstat, SimilarWeb, Sistrix, Wincher, Wireboard, Zutrix) avec un pic de volatilité commun le samedi 18 juillet.

**Portée et limites.**

1. Aucune confirmation Google (dashboard status, blog développeurs, Search Liaison) sur les fenêtres 11 juillet et 18 juillet à ce jour.
2. Le seul document tiers reprenant le 18 juillet est digitalphablet.com. Trust source : 0,85 dans l'index interne, sur reprises secondaires. Les tracker cités sont eux primaires mais leurs chiffres agrégés dans un tiers ne remplacent pas une observation client contrôlée.
3. Fenêtre distincte du core update mai 2026 (clos le 2 juin) et du spam update juin 2026 (24 au 26 juin, clos). Ne pas ranger un mouvement de mi-juillet sous une update fermée.

**Angle SEO.** Pour un consultant qui reçoit une alerte client cette semaine, la lecture est : ouvrir un audit fenêtré (baseline 4 juillet, comparaison 11 juillet, comparaison 18 juillet, comparaison 20 juillet) sur les requêtes clés du client avant d'attribuer un mouvement à un changement de site publié entre-temps. Les cas où le site n'a rien changé et bouge quand même vont être plus fréquents que d'habitude jusqu'à confirmation Google, ou jusqu'à ce que la fenêtre se stabilise (compter au moins 7 jours après le 18 juillet pour lecture stable, soit à partir du 25 juillet).

Sources : [SE Roundtable 41676](https://www.seroundtable.com/google-search-ranking-volatility-july-11th-41676.html), [digitalphablet.com](https://digitalphablet.com/digital-marketing/weekend-google-search-rankings-fluctuations-july-18th-update/).

### Brève 3. GEO / mesure. Le désaccord fraîcheur, résumé pour un audit

Le lien direct entre l'info du jour (Vishwakarma : fraîcheur aide de façon consistante en contrôle contrefactuel) et le corpus interne (Digital Applied juin 2026 : fraîcheur ne prédit plus après contrôle d'autorité de domaine) est utile en propre. Pour un audit client dans un contexte concurrentiel où plusieurs sources autoritaires anciennes concurrencent une source récente moins autoritaire, les deux résultats se combinent, ils ne se contredisent pas.

**Ce que ça donne opérationnellement.**

1. Si le client publie sur un domaine à autorité forte (backlinks, ancienneté, couverture schema mature), la fraîcheur est un multiplicateur : mise à jour régulière = citation plus fréquente, dans le sens Vishwakarma.
2. Si le client publie sur un domaine à autorité faible, la fraîcheur seule n'obtient pas la citation en conditions naturelles : les sources autoritaires anciennes gardent la main, dans le sens Digital Applied.
3. La règle utile : mesurer la fraîcheur en propre (date de dernière mise à jour explicite, delta jours vs la source concurrente citée) mais ne l'inscrire au budget qu'en présence d'une autorité mesurée en propre déjà installée (`Imp_wc`, `Imp_pos`, référentiel Aggarwal 2024).

Sources : [Digital Applied juin 2026](https://www.digitalapplied.com/blog/ai-search-citation-ranking-factors-2026-data-study), [arXiv Vishwakarma](https://arxiv.org/abs/2605.25517), [[concepts/fraicheur-contenu]], [[concepts/metriques-visibilite-geo]].

---

Draft SyntheticBrain. Rien n'a été envoyé.
