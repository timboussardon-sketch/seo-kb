---
type: revue-presse
title: Algorithme, édition 16 juillet 2026 (cloud après-midi)
date: 2026-07-16
edition: 2026-07-16-v2
pilier: Recherche agentique
status: draft
sources: 9
confidence: high
tags: [revue-presse, algorithme, recherche-agentique, geo, seo, perplexity, agents-ia]
---

# Perplexity publie SPACE, un runtime d'agent qui garde une session ouverte jusqu'à une semaine

## En bref

- Perplexity a lancé le 15 juillet SPACE, un runtime d'exécution pour son agent Computer qui isole chaque tâche dans une micro-VM Firecracker et sépare la session (état persistant) du sandbox (unité d'exécution jetable).
- Trois capacités structurantes pour un agent qui opère sur le web : pause, reprise et dérivation d'une session, snapshots mémoire pris pendant l'exécution, isolation stricte des identifiants hors du sandbox.
- Perplexity indique que 100 pct du trafic de production de Computer bascule vers SPACE, avec une durée de rétention documentée jusqu'à une semaine sur un canal (SiliconAngle).
- Pour un site, un agent authentifié peut désormais opérer sur plusieurs jours en gardant son contexte, sans que la couche applicative ait de moyen simple de distinguer cette session persistante d'un usage humain habituel.
- Deux brèves Actualité SEO et une brève GEO complètent l'édition (Google Job Indexing API 10 à 12 mois sans approbation de quota, 4 types de dégradation de contenu, toggle « masquer les résultats sponsorisés » testé dans Google Shopping).

---

## L'info du jour. Perplexity SPACE : le runtime d'agent devient une couche produit à part entière (pilier Recherche agentique)

Le 15 juillet 2026, Perplexity a annoncé SPACE, un environnement d'exécution destiné à faire tourner son agent Computer sur des tâches longues, avec un modèle de sécurité conçu pour les agents plutôt que pour des serveurs d'application classiques. L'annonce est faite via le blog Perplexity ([Secure sandboxes for agents](https://www.perplexity.ai/hub/blog/secure-sandboxes-for-agents)) et le compte X officiel ([Perplexity AI, 15 juillet](https://x.com/perplexity_ai/status/2077432518081744979)). La couverture indépendante corrobore trois points structurants.

**Premier point, l'unité d'isolement.** Chaque tâche s'exécute dans une instance de [Firecracker microVM](https://firecracker-microvm.github.io/), le mini-hyperviseur open source publié par AWS pour Lambda et Fargate. Une micro-VM par tâche donne un système d'exploitation propre à chaque agent, un noyau isolé et un temps de démarrage court, selon [SiliconAngle (Kyt Dotson, 15 juillet 12h00 EDT)](https://siliconangle.com/2026/07/15/perplexity-launches-secure-sandbox-make-ai-agents-secure-powerful/) et [AI Business (15 juillet)](https://aibusiness.com/agentic-ai/perplexity-ai-introduces-sandbox-for-agents). AlphaSignal rapporte une latence médiane de création de sandbox de 60 ms contre 185 ms sur l'ancien système, et une latence P90 de 89 ms contre 447 ms ([AlphaSignal, SPACE runs secure long-running agents 5x faster](https://alphasignal.ai/news/perplexity-s-space-runs-secure-long-running-agents-5x-faster)). Ces chiffres viennent d'une seule source secondaire ; à traiter comme direction attribuée tant qu'un tiers indépendant ne les vérifie pas.

**Deuxième point, la séparation session ou sandbox.** SPACE distingue explicitement l'unité d'exécution (le sandbox, jetable) de l'unité de continuité (la session, persistante). Une session peut être mise en pause, reprise ou dérivée en plusieurs sandboxes parallèles, avec des snapshots mémoire pris pendant l'exécution ([VentureBeat](https://venturebeat.com/technology/perplexity-takes-its-computer-ai-agent-into-the-enterprise-taking-aim-at), [SiliconAngle](https://siliconangle.com/2026/07/15/perplexity-launches-secure-sandbox-make-ai-agents-secure-powerful/), [Digital Today](https://www.digitaltoday.co.kr/en/view/82016/perplexity-launches-space-security-sandbox-for-ai-agents)). SiliconAngle documente une rétention pouvant aller jusqu'à une semaine et une fréquence de snapshots par minute ; ces deux chiffres restent mono-source, à confirmer par une deuxième documentation. VentureBeat précise que SPACE a été construit en dix semaines et fait déjà tourner 100 pct du trafic de production de Perplexity Computer.

**Troisième point, les identifiants.** Mots de passe, clés et jetons ne sont pas stockés dans le sandbox : ils restent chez l'utilisateur (gestionnaire de mots de passe, KMS) et ne sont injectés qu'au moment d'un usage précis, selon [SiliconAngle](https://siliconangle.com/2026/07/15/perplexity-launches-secure-sandbox-make-ai-agents-secure-powerful/) et [AI Business](https://aibusiness.com/agentic-ai/perplexity-ai-introduces-sandbox-for-agents). L'utilisateur conserve la clé de chiffrement des données du sandbox et peut couper l'accès à tout moment. Cette architecture répond à un problème documenté depuis fin 2025 : les sandboxes agent existantes soit isolent bien l'exécution mais exposent les identifiants, soit gèrent des sessions courtes mais ne tiennent pas la durée nécessaire à un agent opérationnel.

**Pourquoi ça concerne un site.** Trois implications lisibles pour la présence d'une marque dans les moteurs et les agents.

Premièrement, la géométrie de la visite non humaine se modifie. Avec une session qui peut durer jusqu'à une semaine, un agent qui se connecte à un service B2B ne se comporte plus comme un crawler ni comme un utilisateur ponctuel : il reprend son travail au point où il s'était arrêté, avec les mêmes cookies, la même mémoire de la conversation et le même identifiant. Un site ne peut plus, avec les moyens standards (user-agent, taux de requêtes, comportement de session), distinguer cette session persistante d'un usage humain habituel.

Deuxièmement, l'affaire [Amazon contre Perplexity au 9e Circuit](https://www.searchenginejournal.com/amazon-vs-perplexity-the-cfaa-case-that-decides-whether-ai-agents-can-visit-your-website/575499/) devient plus concrète. Amazon soutient que l'accès de Comet à des pages authentifiées viole le Computer Fraud and Abuse Act, même quand l'utilisateur a explicitement autorisé l'agent. Les plaidoiries ont eu lieu le 11 juin 2026, la cour n'a pas encore statué ([Courthouse News, Perplexity AI asks Ninth Circuit to allow shopping tool on Amazon](https://www.courthousenews.com/perplexity-ai-asks-ninth-circuit-to-allow-shopping-tool-on-amazon/), [CourtListener docket 3:25-cv-09514](https://www.courtlistener.com/docket/71874820/amazoncom-services-llc-v-perplexity-ai-inc/)). SPACE prépare le terrain opérationnel : Perplexity industrialise l'infrastructure pour qu'un agent tienne des tâches longues chez ses utilisateurs. La question juridique n'a pas bougé, mais la capacité technique, elle, avance sans attendre.

Troisièmement, la doctrine [[concepts/agentic-search]] gagne une variable supplémentaire. L'objet à optimiser n'est plus seulement la page ou le flux produit ; c'est aussi la stabilité de l'interaction quand un agent revient plusieurs jours de suite. Un site avec une session courte, un CAPTCHA fréquent ou un rate-limit strict devient plus coûteux à intégrer pour un agent que le site voisin. Cela recoupe la doctrine [[concepts/data-proprietaire]] : la partie que le site expose de façon prédictible à un agent devient une donnée propriétaire opérationnelle, distincte du contenu indexable classique.

**Limites documentaires à publier.** Trois éléments ne sont pas encore vérifiables au 16 juillet.

- La rétention à une semaine et la fréquence de snapshots à la minute sont documentées par une seule source secondaire ([SiliconAngle](https://siliconangle.com/2026/07/15/perplexity-launches-secure-sandbox-make-ai-agents-secure-powerful/)). Le billet primaire Perplexity ne renvoie pas de contenu accessible aux crawlers publics au moment de la rédaction.
- Les chiffres d'adoption (1,25 million de créations de sandbox et 11,9 millions de reconnexions sur une semaine de déploiement interne) proviennent aussi de SiliconAngle seule et couvrent l'usage interne de Perplexity, pas des tiers.
- Aucune comparaison indépendante côté [Anthropic Claude Cowork](https://www.anthropic.com/), [OpenAI ChatGPT Work](https://openai.com/chatgpt/enterprise/) ou [Google GKE Agent Sandbox](https://cloud.google.com/blog/products/containers-kubernetes/introducing-gke-agent-sandbox) ne permet aujourd'hui de mettre en regard des temps de création, des durées de session ou des politiques d'identifiants. Les analyses secondaires ([AI Business](https://aibusiness.com/agentic-ai/perplexity-ai-introduces-sandbox-for-agents), [FourWeekMBA](https://fourweekmba.com/ai-perplexity-space-agent-runtime-sandbox/)) nomment les concurrents sans chiffres comparables.

**Deux prédictions vérifiables.**

- P-2026-07-16-v2-1 : un autre fournisseur commercial d'agent (Anthropic, OpenAI ou Google Cloud) publie, avant fin 2026, une architecture de sandbox longue durée avec une fenêtre de rétention documentée ≥ 1 semaine et une isolation des identifiants hors du sandbox.
- P-2026-07-16-v2-2 : un éditeur ou un marchand nommé publie, avant le 31 mars 2027, une politique différenciée pour « agents avec session authentifiée persistante », distincte de sa politique crawler et de sa politique utilisateur humain (règles de rate-limit, obligation de signaler l'agent, contrôles d'usage).

**Lecture opérationnelle** (à considérer comme une lecture, pas comme une consigne définitive).

- Éditeurs et marchands : cartographier ce qui, dans votre site, casse une session longue (CAPTCHA silencieux, rate-limit strict, re-authentification), et décider si vous voulez le maintenir pour un agent authentifié ou l'adoucir.
- SEO et GEO : la variable [[concepts/metriques-visibilite-geo]] gagne une lecture supplémentaire. La stabilité d'une intégration agent devient un facteur de sélection, au même titre que la couverture de citations dans les réponses génératives.
- Analytics : un agent qui garde sa session sur une semaine explose les définitions classiques de « visite » et « visiteur unique ». La doctrine [[concepts/tabou-visibilite]] reste utile : la visite d'un agent n'est pas une visite humaine, et sa mesure ne se transpose pas.

---

## Brèves

### B1. Google Job Indexing API : « soumis » n'est pas « indexé » (Actualité SEO)

Nick LeRoy a publié le 16 juillet à 8h00 sur Search Engine Land ([Google's job Indexing API isn't the shortcut you think it is](https://searchengineland.com/google-job-indexing-api-shortcut-482427)) une analyse factuelle du fonctionnement réel de l'API. Trois points chiffrés à retenir.

L'API accepte seulement deux types de données structurées : JobPosting et BroadcastEvent (livestream). Toute autre URL soumise renvoie une réponse « acceptée » sans être crawlée ni indexée. Le quota par défaut à l'onboarding est de 200 requêtes par jour ; l'augmentation passe par un formulaire de demande dont les délais historiques étaient de 2 à 3 semaines.

Depuis 10 à 12 mois, LeRoy documente qu'aucune demande d'augmentation de quota n'a été approuvée pour un opérateur légitime, y compris ses propres sites SEOJobs.com et PPCJobs.com sur une demande déposée six mois avant l'article. Il pointe vers un outil gratuit qu'il maintient, [Job Indexing Health Check sur SEOJobs.com](https://seojobs.com/tools/job-indexing-health-check/), qui compare la réponse `getMetadata` de l'API à ce que Google Search Console remonte. Verdict opérationnel : la réponse HTTP 200 signifie « notification reçue », pas « URL indexée », et l'écart entre les deux devient la métrique à surveiller pour un job board.

Contexte, non repris dans cet article : John Mueller avait indiqué en mai sur Bluesky que le formulaire de quota est « inondé par des blogs qui se font passer pour des sites légitimes » (source : [SEO for Lunch, Google's laughing at you using its web indexing (job) API](https://www.seoforlunch.com/p/google-job-indexing-api), cité par Alexander Chukovski).

### B2. Quatre types de dégradation de contenu, dont une propre aux surfaces IA (Actualité SEO ou GEO)

Ashish Jacob a publié le 16 juillet à 9h00 sur Search Engine Land ([4 types of content decay and how to fix each one](https://searchengineland.com/content-decay-types-fix-482486)) une taxonomie en quatre catégories, qui distingue pour la première fois de façon nette la dégradation liée aux surfaces IA.

- **Ranking Decay** : la position se dégrade sous la pression concurrentielle ou l'obsolescence du contenu. Clics et impressions baissent ensemble.
- **Zero-Click Capture** : catégorie nouvelle. Clics en baisse, impressions stables ou en hausse, position tenue. La cause est le remplissage de la réponse directe par les AI Overviews et les fonctionnalités SERP. C'est la seule catégorie qui isole la dégradation propre aux surfaces IA de la dégradation classique.
- **Intent Drift** : Google réinterprète la requête (préférence pour la vidéo, les tableaux comparatifs), les clics baissent alors que la position tient.
- **Demand Decay** : le volume de recherche sur le sujet baisse, indépendamment de la qualité de la page.

Données de cadrage rappelées par l'article : moins d'une recherche Google sur trois envoie un clic à un site, environ 68 pct de recherches se terminent sans clic (contre environ 60 pct deux ans avant), et sur les requêtes déclenchant un AI Overview, le premier résultat organique perd environ 58 pct de ses clics. Sources citées dans l'article : [SparkToro](https://sparktoro.com/), [Ahrefs](https://ahrefs.com/) et [BrightEdge](https://www.brightedge.com/). L'article rappelle aussi la suppression du paramètre `&num=100` en septembre 2025, qui a réduit le sur-comptage des impressions par des bots.

Utilité doctrinale : Zero-Click Capture propose un cadre mesurable pour ce que la fiche [[concepts/metriques-visibilite-geo]] appelle la « part de citations captée par le moteur lui-même ». La dégradation propre aux surfaces IA devient une catégorie identifiable au niveau de la page.

### B3. Google teste le toggle « masquer les résultats sponsorisés » dans Google Shopping (Actualité SEO)

Barry Schwartz a documenté le 15 juillet 2026 sur Search Engine Roundtable ([Google Testing Hide Sponsored Products In Google Shopping](https://www.seroundtable.com/google-tests-hide-sponsored-products-41689.html)) que Google confirme tester une bascule « Hide / Show sponsored results » à l'intérieur de l'interface Google Shopping, avec Ginny Marvin (Google Ads Liaison) qui répond publiquement. La fonction avait été déployée dans les résultats principaux de Search en octobre 2025.

Deux implications pour la partie Shopping et pour la lecture Search + Ads.

- Pour un annonceur Shopping, la part visible des Product Listing Ads dépend maintenant, en partie, d'un choix utilisateur explicite. La comparaison entre CPC engagé et impression payante devient plus tendue si une fraction non négligeable des utilisateurs bascule le toggle sur « masquer ».
- Pour un vendeur mesurant sa présence dans les AI Overviews et AI Mode, l'exposition côté Shopping et côté surfaces IA suit désormais deux logiques distinctes : la partie Shopping peut être masquée à la volée par l'utilisateur, la partie citation IA ne l'est pas. La séparation opérationnelle des deux mesures devient utile.

L'article ne donne pas de date de généralisation ni de part d'utilisateurs actifs sur le toggle historique dans Search. À attendre : un chiffre d'usage réel avant de tirer une conclusion sur l'impact structurel.

---

Draft SyntheticBrain, 16 juillet 2026 (cloud après-midi). Rien n'a été envoyé.
