---
date: 2026-07-23
pilier_info_du_jour: Recherche agentique
piliers_breves: [GEO, Actualité SEO, Business SEO]
capture_mode: native
---

# Trafic agent Q2 2026 : 17,7 milliards de requêtes, Meta en concentre 9,1 milliards, Claude signe une progression de 111 pour cent côté referral

**Résumé en 5 points :**

- Le trafic des agents IA atteint 17,7 milliards de requêtes sur le réseau DataDome au deuxième trimestre 2026, en hausse de 45 pour cent par rapport au premier trimestre.
- Deux agents Meta concentrent 9,1 milliards de requêtes à eux seuls, avec zéro referral humain renvoyé aux sites indexés.
- Claude passe de 415 000 à 876 000 visites référées trimestrielles, soit une croissance de 111 pour cent, tandis que Grok recule de 74 pour cent.
- ChatGPT-User baisse de 6 pour cent en volume de requêtes brutes mais renvoie 17 pour cent de clics sortants humains en plus, et concentre 80 à 88 pour cent des referrals IA du réseau.
- Le protocole Model Context Protocol (MCP) émerge comme signal distinct, avec un pic proche de 500 000 requêtes par jour et une distribution répartie sur les appels `initialize`, `tools/list`, `prompts/list` et `notifications/initialized`.

---

## Info du jour — Recherche agentique

La question posée aux éditeurs depuis dix-huit mois est : combien coûte l'accueil des agents IA, et combien ils rapportent. Le rapport de DataDome publié le 16 juillet 2026 pose un premier jeu de chiffres consolidés, mesurés sur 5 000 milliards de signaux quotidiens et 400 entreprises clientes sur la fenêtre avril-juin 2026 ([DataDome, AI Traffic Report Q2 2026](https://datadome.co/threat-research/ai-traffic-report-q2-2026/)). Digiday reprend le 21 juillet en synthèse d'écosystème ([Digiday, AI visibility is no longer about referral traffic](https://digiday.com/media/in-graphic-detail-ai-visibility-is-no-longer-about-referral-traffic/)). Les deux sources sont indépendantes, la seconde ajoute une déclaration de Jérôme Segura, VP chez DataDome, qui identifie la bascule côté Meta.

Le volume brut d'abord. Q2 2026 totalise 17,7 milliards de requêtes agent sur le réseau DataDome, contre 12,2 milliards au premier trimestre. Rythme mensuel : 4,77 milliards en avril, 6,29 milliards en mai, 6,60 milliards en juin. La barre des 30 milliards a été franchie sur le cumul depuis janvier. Ces chiffres portent sur des sites protégés par DataDome, donc pondérés vers e-commerce, média et services financiers, ce qui constitue la première limite documentaire.

Les deux crawlers qui concentrent la plus grande part du volume ne sont pas ceux d'un moteur de recherche. Ce sont deux crawlers Meta. Le premier, Meta-ExternalAgent, passe de 3,1 milliards à 5,3 milliards de requêtes trimestrielles, soit une croissance de 74 pour cent. Le second, Meta-WebIndexer, passe de 1,4 milliard à 3,75 milliards, une croissance de 163 pour cent. Combinés, ils atteignent 9,1 milliards de requêtes, plus de la moitié du trafic agent du réseau. Le referral humain que Meta renvoie aux sites qu'il indexe, sur la même période, est négligeable au regard du volume consommé. Segura résume la lecture DataDome : « We're entering a new phase of the AI web. Meta is shifting from scrape once for training to continuous indexing. »

Le contraste avec les agents adossés à des assistants conversationnels est net et va dans les deux sens. ChatGPT-User, qui trace les requêtes issues du navigateur ChatGPT, recule de 6 pour cent en volume brut d'un trimestre à l'autre. Cette baisse ne signifie pas moins d'usage. Selon la même mesure DataDome, les clics sortants humains attribués à ChatGPT progressent de 17 pour cent sur la même fenêtre, et ChatGPT reste responsable de 80 à 88 pour cent des referrals IA observés dans le réseau. La bascule Claude est plus rapide encore : les visites référées trimestrielles passent de 415 000 à 876 000, soit 111 pour cent de croissance. Perplexity progresse de 37 pour cent. À l'inverse, Grok recule de 74 pour cent, sans que la cause soit tranchée dans le rapport.

Un signal secondaire mérite d'être noté. Le trafic labellisé Model Context Protocol (MCP) apparaît dans la mesure DataDome avec un pic proche de 500 000 requêtes par jour. Sa distribution interne se répartit à 20,3 pour cent sur `initialize`, 19,7 pour cent sur `tools/list`, 20,1 pour cent sur `prompts/list` et 19,1 pour cent sur `notifications/initialized`. Cette répartition suggère un trafic majoritairement en phase de découverte des capacités des serveurs plutôt qu'en usage productif d'appel d'outils. DataDome indique que 54 pour cent des clients de son réseau ont désormais adopté une politique de confiance dédiée aux agents.

Une deuxième mesure indépendante, citée par Digiday, complète le tableau. Les automates génèrent 57,4 pour cent des requêtes web contre 42,6 pour cent pour les humains sur le même échantillon Q2 2026. Ce basculement quantitatif n'est pas nouveau au sens strict, [Cloudflare Radar l'avait signalé début juin](https://blog.cloudflare.com/content-independence-day-ai-options/), mais il devient documenté avec granularité par agent identifié.

**Lecture doctrine.** Cette édition confirme deux points déjà présents dans la doctrine seo-kb sur la lecture agentique, et en durcit un troisième. Le premier est que la métrique de comptage du trafic agent (volume de requêtes) ne capte pas l'utilité économique. La seconde métrique utile est le ratio referral humain par requête agent, et il diffère par un facteur supérieur à cent entre Meta d'un côté et ChatGPT/Claude/Perplexity de l'autre. Ce que la [fiche `metriques-visibilite-geo`](https://github.com/timboussardon-sketch/seo-kb/blob/main/wiki/concepts/metriques-visibilite-geo.md) modélisait au niveau de la citation dans la réponse générative se retrouve au niveau du trafic entrant : être indexé par un crawler agent et être renvoyé comme source à un utilisateur humain sont deux mesures distinctes qui n'évoluent pas dans le même sens.

Le second point est doctrinal sur `agentic-search`. La note interne [`agentic-search`](https://github.com/timboussardon-sketch/seo-kb/blob/main/wiki/concepts/agentic-search.md) rappelle que le SEO agentique consiste à être sélectionné par l'agent pour accomplir une tâche, pas juste à être affiché. Q2 2026 ajoute une précision : les agents ne se valent pas comme canaux, et l'écart s'agrandit. Un site qui vise à être cité par un assistant conversationnel cible un volume de referral mesurable, en croissance côté Claude et Perplexity, stable en clics côté ChatGPT. Un site qui laisse passer les crawlers Meta sans politique de restriction transfère un coût d'infrastructure sans contrepartie de trafic connue à ce jour.

Le troisième point ouvre une question. MCP n'est pas encore un canal, il est un protocole d'annonce des capacités entre agents et outils. Sa distribution actuelle (majoritairement des `initialize` et `list`) indique une phase d'exploration, pas d'exécution. Il devient utile de surveiller si la part des appels productifs (`tools/call` avec suivi complet) dépasse 10 pour cent avant la fin 2026. Cette bascule signalerait qu'un agent commence à choisir quelles capacités il utilise réellement, et donc à opérer une sélection comparable à ce que Google Search fait sur des URLs.

Il reste deux limites documentaires importantes. La première : la mesure DataDome porte sur les clients de DataDome, donc surreprésente les sites protégés contre le scraping et sous-représente les sites en accès libre sans WAF. La seconde : ChatGPT-User ne compte que le navigateur ChatGPT, pas les usages API ni les agents tiers construits sur GPT. Le chiffre de 80 à 88 pour cent de part de referrals ChatGPT est donc à lire comme une part sur les referrals IA identifiables par DataDome, pas sur l'ensemble des interactions humaines qui incluent une consultation GPT en amont.

---

## Brèves

### B1 — GEO. Reddit stabilise à 4,5 pour cent des citations IA (SE Ranking, panel juin 2026)

SE Ranking publie mi-juillet une étude de citation IA centrée sur Reddit. Le protocole : 482 posts uniques, 135 subreddits, six vérifications réparties sur trois mois de mars à juin 2026, 7 307 citations enregistrées à travers AI Overviews, AI Mode, ChatGPT et Gemini ([SE Ranking, Reddit and AI Search: What Patterns Show](https://seranking.com/blog/reddit-ai-search-visibility/)). Résultat central : Reddit passe d'environ 2,3 pour cent des citations en novembre 2025 à 4,5 pour cent en juin 2026 sur ce panel, se plaçant en deuxième domaine cité, catégories confondues. Deuxième résultat notable, 42 posts (9 pour cent du panel) ont traversé les six vérifications et concentrent à eux seuls 48 pour cent des citations recueillies. Les posts « stables » reçoivent 83,4 citations en moyenne, contre 1,6 pour les posts apparus une seule fois.

Ce résultat conforte deux points de doctrine. D'abord la [fiche `fraicheur-contenu`](https://github.com/timboussardon-sketch/seo-kb/blob/main/wiki/concepts/fraicheur-contenu.md) : la fraîcheur pure ne domine pas la citation, la persistance d'une source à travers plusieurs snapshots la domine. Ensuite le raisonnement en 5 questions successives de la [fiche `agentic-search`](https://github.com/timboussardon-sketch/seo-kb/blob/main/wiki/concepts/agentic-search.md) : ce sont les mêmes posts qui reviennent au fil des passages, pas des posts frais à chaque cycle. Limite documentaire à retenir : SE Ranking est un éditeur d'outils SEO, panel restreint (482 posts), et la mesure ne différencie pas la part de citation par moteur.

### B2 — Actualité SEO. La Commission européenne ordonne à Google d'ouvrir ses données de recherche

Le 16 juillet 2026, la Commission européenne adopte deux décisions contraignantes au titre du Digital Markets Act à l'encontre d'Alphabet. La première oblige Google à ouvrir Android à des assistants IA concurrents. La seconde oblige Google à partager avec ses rivaux et avec les chatbots IA offrant une fonction de recherche des données anonymisées de recherche : requêtes, positions, clics et impressions ([Mediapost, Google Ordered By EU Commission To Share Anonymized Search Data](https://www.mediapost.com/publications/article/416625/google-ordered-by-eu-commission-to-share-anonymize.html), [Digital Markets Act developer portal, Alphabet specification proceedings](https://digital-markets-act.ec.europa.eu/developer-portal/data-access/alphabet-specification-proceedings-sharing-google-search-data_en)). Le partage doit se faire sur des termes équitables, raisonnables et non discriminatoires (FRAND).

Les moteurs de recherche rivaux et les chatbots IA avec fonction search peuvent demander les données à partir de janvier 2027. Les concurrents Android IA disposent d'un accès complet à partir d'août 2027. L'algorithme de ranking Google reste hors périmètre. Le texte ne fixe pas de sanction financière mais des exigences techniques. La lecture doctrinale renvoie à la [fiche `tabou-visibilite`](https://github.com/timboussardon-sketch/seo-kb/blob/main/wiki/concepts/tabou-visibilite.md) et à la mesure des impressions : à partir de janvier 2027, plusieurs moteurs disposeront pour la première fois d'un pointeur direct sur les clics et positions Google, et ces données pourront alimenter l'entraînement des moteurs génératifs éligibles. La conséquence attendue est un rapprochement des grilles de mesure entre engines cross-vendor. Fenêtre d'observation à surveiller : les premières demandes formelles au premier trimestre 2027.

### B3 — Business SEO. Google Ads coupe l'appel des sanctions de plus de six mois

Barry Schwartz signale le 21 juillet 2026 dans Search Engine Roundtable que Google Ads impose une limite de six mois pour contester une violation de politique depuis le compte annonceur ([Search Engine Roundtable, Google Ads Sets 6 Month Timeline For Appeals](https://www.seroundtable.com/google-ads-appeals-limit-41730.html)). Passé ce délai, l'annonceur doit ouvrir un ticket auprès du support pour tenter une contestation. La documentation officielle Google Ads reprend la mesure ([Google Ads Help, Fix a disapproved ad or appeal a policy decision](https://support.google.com/google-ads/answer/9338593)).

Cette décision produit un effet pratique documentable : les comptes qui ont accumulé des désapprobations historiques sans les traiter perdent la voie de contestation directe. Le contexte plus large est une convergence vers une gestion policy sous forme d'infrastructure automatisée, distincte du support relationnel. Un annonceur qui reçoit une désapprobation doit désormais programmer un cycle d'appel sous six mois, sans quoi la trace de la sanction n'est plus renversable via le workflow standard. Cette mesure ne modifie pas les règles de qualité elles-mêmes mais durcit leur exécution dans le temps. Un point de mesure ouvert : le taux effectif de contestations qui basculent vers le support et le taux de résolution associé, non publié à ce jour.

---

**Prédictions ouvertes ajoutées par cette édition :**

- P-2026-07-23-1 (D'ici le 31 décembre 2026, une deuxième mesure indépendante hors DataDome publie un ratio requêtes agent Meta / referrals humains supérieur à 100 000:1 sur un réseau distinct, mesuré sur un trimestre entier. Résolution positive : rapport publié avec méthodologie, panel et chiffres, hors DataDome. Résolution négative : silence prolongé.)
- P-2026-07-23-2 (D'ici le 31 mars 2027, la part de requêtes MCP labellisées `tools/call` avec suivi complet dépasse 10 pour cent du trafic MCP total mesuré par au moins une source. Résolution positive : chiffre publié avec méthodologie. Résolution négative : distribution MCP reste dominée par `initialize` / `list`.)
- P-2026-07-23-3 (D'ici le 30 juin 2027, au moins un moteur de recherche rival hors Bing et Yahoo dépose une demande formelle auprès de Google pour obtenir un accès aux données FRAND prévues par la décision européenne. Résolution positive : demande publique nommée. Résolution négative : aucune demande publique.)

---

Draft SyntheticBrain. Rien n'a été envoyé.
