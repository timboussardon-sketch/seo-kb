---
date: 2026-06-07
type: revue-presse
agent: SyntheticBrain
pilier_info_jour: GEO / search IA
sources_independantes: 11
claims_verified: 16
status: draft
---

# Google ajoute deux étiquettes aux liens cités par AI Mode et AI Overviews : Preferred et Highly Cited

**À retenir en 3 minutes :**

- Le 27 mai 2026, Google a étendu Preferred Sources, jusque-là réservé à Top Stories, à AI Mode et AI Overviews, avec un badge « Preferred » apposé sur les liens cités quand ils correspondent aux sources choisies par l'utilisateur ([blog.google](https://blog.google/products-and-platforms/products/search/original-high-quality-content-search/), [9to5google](https://9to5google.com/2026/05/27/google-ai-mode-preferred-sources/)).
- Plus de 345 000 sources uniques ont déjà été sélectionnées par les utilisateurs, près de quatre fois le chiffre de fin 2024 ; Google déclare que les utilisateurs cliquent deux fois plus sur les liens portant le badge Preferred ([blog.google](https://blog.google/products-and-platforms/products/search/original-high-quality-content-search/), [ppc.land](https://ppc.land/google-brings-preferred-sources-into-ai-overviews-and-ai-mode-today/)).
- Au même moment, Google étend le label « Highly Cited » (introduit en 2022 dans Top Stories) à plus d'articles dans les résultats classiques. Ce label signale l'article que les autres publications citent comme source primaire ([blog.google](https://blog.google/products-and-platforms/products/search/original-high-quality-content-search/), [androidheadlines](https://www.androidheadlines.com/2026/05/google-ai-search-updates-preferred-sources-highly-cited.html)).
- Le core update Google de mai 2026 s'est terminé le 2 juin après douze jours. Bilan SISTRIX au 5 juin (US) : agrégateurs et plateformes de syndication en repli ; sites à contenu propre, YouTube, Facebook, Yelp en hausse ([SISTRIX](https://www.sistrix.com/blog/may-2026-core-update-visibility-analysis-and-data-updates/), [Search Engine Land](https://searchengineland.com/google-may-2026-core-update-rollout-is-now-complete-479119)).
- ChatGPT a franchi le seuil du milliard d'utilisateurs actifs mensuels sur son application en mai 2026, selon Sensor Tower repris par Reuters le 2 juin, environ trois ans après son lancement ([investing.com via Reuters](https://www.investing.com/news/stock-market-news/chatgpt-app-hits-1-billion-monthly-active-users-in-record-time-data-shows-4723123)).

---

## Info du jour | Pilier GEO / search IA

*Entité : [[entities/google-ai-mode]].*

### Ce que Google a annoncé le 27 mai et ce que ça déplace

Le 27 mai 2026, Google a annoncé deux changements simultanés dans la manière dont AI Mode et AI Overviews exposent les liens cités. Le premier change étend Preferred Sources, fonctionnalité jusqu'ici limitée à Top Stories, à l'ensemble des réponses générées par AI Mode et AI Overviews. Le second étend le label « Highly Cited », introduit en 2022 dans Top Stories, à plus d'articles dans les résultats de recherche classiques ([blog.google](https://blog.google/products-and-platforms/products/search/original-high-quality-content-search/)).

Preferred Sources est une fonctionnalité d'opt-in pour l'utilisateur final. Le lecteur sélectionne, dans les paramètres de personnalisation de Search, les sites qu'il souhaite voir prioritarisés. Quand ces sites apparaissent dans une réponse d'AI Mode ou d'AI Overviews, ils portent un badge « Preferred » visible à côté du lien. Google indique que plus de 345 000 sources uniques ont déjà été ajoutées par les utilisateurs, près de quatre fois le chiffre de fin 2024 ([blog.google](https://blog.google/products-and-platforms/products/search/original-high-quality-content-search/), [9to5google](https://9to5google.com/2026/05/27/google-ai-mode-preferred-sources/)). Google déclare également que les utilisateurs sont deux fois plus susceptibles de cliquer sur un lien portant le label Preferred que sur un lien sans badge ([blog.google](https://blog.google/products-and-platforms/products/search/original-high-quality-content-search/), [ppc.land](https://ppc.land/google-brings-preferred-sources-into-ai-overviews-and-ai-mode-today/)).

Le label « Highly Cited » fonctionne sur un mécanisme différent. Il est calculé par Google, pas déclaré par l'utilisateur. Le label est posé sur les articles fréquemment cités par d'autres publications. Selon la documentation officielle, l'objectif est de signaler le « primary reporting » que d'autres articles référencent ensuite ([blog.google](https://blog.google/products-and-platforms/products/search/original-high-quality-content-search/), [androidheadlines](https://www.androidheadlines.com/2026/05/google-ai-search-updates-preferred-sources-highly-cited.html)). Le label peut désormais apparaître sur la page de résultats de recherche classique, en plus de Top Stories. Google indique qu'un article peut porter les deux badges simultanément ([themobileindian](https://themobileindian.com/news/google-adds-preferred-sources-in-ai-overviews-and-ai-mode-introduces-highly-cited-labels)).

Une troisième pièce accompagne ce déploiement : un nouveau carrousel de Preferred Sources qui s'affiche pour les requêtes sur des sujets en cours d'évolution, avec des contenus issus de forums et discussions en ligne en plus des éditeurs traditionnels ([blog.google](https://blog.google/products-and-platforms/products/search/original-high-quality-content-search/), [9to5google](https://9to5google.com/2026/05/27/google-ai-mode-preferred-sources/)).

Sur la question du classement, deux lectures coexistent à ce stade. PPC Land, citant l'annonce officielle, indique que ces deux mécanismes ne fonctionnent pas (encore) comme des signaux de classement et que la sélection des sources continue de dépendre des signaux algorithmiques habituels ([ppc.land](https://ppc.land/google-brings-preferred-sources-into-ai-overviews-and-ai-mode-today/)). 9to5Google indique que Google travaille à transformer Preferred Sources en signal de classement pour ses fonctionnalités IA, sans calendrier annoncé ([9to5google](https://9to5google.com/2026/05/27/google-ai-mode-preferred-sources/)). Les deux lectures sont compatibles : l'état actuel est un affichage différencié, l'état visé est l'intégration au signal de sélection.

### Ce que cela change pour la doctrine GEO

La fiche [[concepts/metriques-visibilite-geo]] de la base décompose la visibilité dans les réponses IA en trois familles de métriques : Imp_wc (fréquence des phrases citant la source), Imp_pos (pondération par la position dans la réponse), Subjective Impression (sept critères évalués par LLM-as-judge). Toutes sont calculées sur le contenu de la réponse et la mécanique de classement algorithmique.

Preferred Sources introduit une dimension qui n'est captée par aucune de ces trois familles : un signal d'autorité déclarative, exogène à l'algorithme, fondé sur la sélection explicite de l'utilisateur. Highly Cited reste, lui, dans le périmètre algorithmique, mais sur une logique de concentration de citations entre éditeurs plutôt que d'autorité de domaine au sens classique.

Trois conséquences pratiques se dégagent.

Première conséquence : si Preferred Sources devient un signal de classement, comme l'annonce 9to5google, l'optimisation devra inclure une dimension d'incitation à l'opt-in côté utilisateur. La page « comment être ajouté en source préférée » devient un objet à traiter au même titre que les pages de présentation de marque. Cette dimension dépasse l'AEO classique tel que défini dans [[concepts/aeo]], qui se concentre sur le mécanisme de citation par le moteur, pas par l'utilisateur.

Deuxième conséquence : Highly Cited récompense l'article que d'autres publications citent comme source primaire. Sur le périmètre éditorial, cela suggère que la qualité du primary reporting (donnée originale, témoignage direct, document source) est mesurée par la concentration de liens entrants dans un délai court. C'est cohérent avec la lecture de la fiche [[concepts/data-proprietaire]] : la donnée propre se documente par la reprise par les tiers, pas seulement par l'autorité de domaine.

Troisième conséquence : les deux signaux ajoutent une couche de tri visible dans la réponse, distincte du rang. Un site cité sans badge est dans la réponse, mais sans le marqueur d'autorité que Google laisse l'utilisateur ou les autres éditeurs lui apposer. À CTR comparé deux fois plus élevé (selon Google) pour les liens Preferred, ce marquage devient une variable de performance à mesurer dans Search Console (qui a introduit son rapport IA le 3 juin 2026, sans donnée de clic).

À cinq mois de l'échéance de la prédiction P-2026-05-30-5 (formats publicitaires AI Mode sortis du stade annonce), ce déploiement non-publicitaire confirme la cadence de production de Google sur l'enveloppe d'AI Mode : trois changements visibles sur la même semaine (publicité santé, Preferred Sources, Highly Cited).

---

## Brèves

### Bilan SISTRIX du core update Google de mai 2026 | pilier Actualité SEO

Le core update Google de mai 2026 s'est déployé du 21 mai au 2 juin 2026, soit environ douze jours, et Google a confirmé sa clôture officielle le 2 juin ([Search Engine Land](https://searchengineland.com/google-may-2026-core-update-rollout-is-now-complete-479119)). Les outils de mesure de volatilité ont enregistré des valeurs élevées : Semrush 78/100, SISTRIX 65/100, Accuranker 72/100 ([xpert.digital](https://xpert.digital/en/google-update-from-may-2026-completed/)).

L'analyse SISTRIX publiée le 5 juin (échantillon US, fenêtre 21 mai - 5 juin) liste les variations de l'indice de visibilité par domaine. Côté pertes en pourcentage : zalesoutlet.com (-66,74 %), freepik.com (-63,09 %), onetonline.org (-60,07 %), thereciperebel.com (-58,38 %), aerotek.com (-57,06 %). Côté gains en pourcentage : freepeoplesearch.com (+267,24 %), upstart.com (+224,56 %), stinehome.com (+210,19 %), pokerstrategy.com (+178,23 %), fresha.com (+175,69 %) ([SISTRIX](https://www.sistrix.com/blog/may-2026-core-update-visibility-analysis-and-data-updates/)).

Sur les variations en valeur absolue de visibilité, les écarts les plus marqués vont à youtube.com (+591,66), facebook.com (+200,10) et yelp.com (+180,51) côté gains ; macys.com (-41,61), substack.com (-9,68), aarp.org (-9,56) côté pertes ([SISTRIX](https://www.sistrix.com/blog/may-2026-core-update-visibility-analysis-and-data-updates/)).

Le motif identifié par SISTRIX et repris dans la couverture SEJ correspond à un mouvement déjà observé en mars : repli des sites d'agrégation, d'offres d'emploi et de comparaison ; hausse des plateformes vidéo et sociales établies, et de sites à contenu propre ([SISTRIX](https://www.sistrix.com/blog/may-2026-core-update-visibility-analysis-and-data-updates/), [Search Engine Journal](https://www.searchenginejournal.com/googles-may-core-update-complete-after-volatile-rollout/577704/)). Les secteurs YMYL (santé, finance) et les pages produit e-commerce à contenu mince figurent parmi les zones les plus volatiles.

Ce bilan reste à consolider avec au moins une 2e source de mesure de visibilité indépendante après la fenêtre de stabilisation des données (que Google recommande de fixer à au moins sept jours après la fin du déploiement, soit ~9 juin), ce qui correspond à la prédiction P-2026-06-06-v2-2.

### Mastercard met son outillage Agent Pay en production fin juin | pilier Recherche agentique

Annoncée le 27 janvier 2026, la suite d'outils agentic de Mastercard, baptisée Mastercard Agent Pay, est attendue en mise en service auprès des clients commerciaux d'ici la fin juin 2026 ([Payments Dive](https://www.paymentsdive.com/news/mastercard-offers-agentic-ai-tools/811350/)). Mastercard est partenaire de Google sur le protocole de commerce universel (UCP) et d'OpenAI sur ses protocoles de commerce agentique.

Le mécanisme repose sur des « Agentic Tokens » qui lient une carte tokenisée à un agent spécifique, à une portée marchande définie et à une politique de consentement explicite. L'agent (ChatGPT, Microsoft Copilot ou autre) peut finaliser une commande sans jamais manipuler le numéro de carte en clair ([European Financial Review](https://www.europeanfinancialreview.com/visa-mastercard-race-to-build-ai-agents-fornext-commerce-shift/), [Payments Dive](https://www.paymentsdive.com/news/mastercard-offers-agentic-ai-tools/811350/)).

Cette mise en service complète la pile agentique côté paiement, après le travail sur les couches découverte et checkout traité dans les éditions précédentes (UCP, ACP, AP2). La consolidation à observer : quels agents IA seront les premiers à intégrer Agent Pay en production réelle, et selon quelle répartition (Google vs OpenAI vs Microsoft). À ce stade, Mastercard cite plusieurs partenariats parallèles sans calendrier d'intégration agent-par-agent ([Payments Dive](https://www.paymentsdive.com/news/mastercard-offers-agentic-ai-tools/811350/)).

### ChatGPT à 1 milliard d'utilisateurs actifs mensuels sur l'app | pilier Actualité IA / search IA

ChatGPT a franchi le seuil du milliard d'utilisateurs actifs mensuels sur son application en mai 2026, selon les estimations de la société d'intelligence de marché Sensor Tower, reprises par Reuters le 2 juin ([Reuters via Investing.com](https://www.investing.com/news/stock-market-news/chatgpt-app-hits-1-billion-monthly-active-users-in-record-time-data-shows-4723123)). L'app aurait atteint ce cap environ trois ans après son lancement, devançant la cadence de Google Maps, TikTok, Instagram et YouTube sur la même mesure.

Le chiffre concerne l'application mobile, pas l'usage web ni l'API ; il ne mesure pas la part qui correspond à un usage de recherche au sens strict. Il consolide néanmoins la position de ChatGPT comme premier point d'entrée IA grand public, à comparer aux 2,5 milliards d'utilisateurs mensuels d'AI Overviews et au milliard d'utilisateurs mensuels d'AI Mode revendiqués par Google à I/O 2026.

Pour mémoire, à la même date, Claude est estimé à 56 millions d'utilisateurs actifs mensuels globaux, avec une croissance annuelle d'environ 640 %, contre 62 % pour ChatGPT ([Reuters via Investing.com](https://www.investing.com/news/stock-market-news/chatgpt-app-hits-1-billion-monthly-active-users-in-record-time-data-shows-4723123)). La hiérarchie des trafics IA reste donc fortement concentrée, mais la croissance relative se diffuse.

---

## Rappel rituel

Ce draft n'est pas publié. Trois prédictions ont été ouvertes ou maintenues ouvertes ce run :
- P-2026-06-07-1 (Preferred Sources devient signal de classement effectif dans AI Mode/AI Overviews d'ici fin 2026)
- P-2026-06-07-2 (Mastercard Agent Pay intégré en production à au moins un agent IA majeur avec annonce officielle avant le 2026-09-30)
- Suivi P-2026-05-30-5 (formats publicitaires AI Mode hors stade annonce) consolidé par ce run.

Pilier de l'info du jour : GEO / search IA. Brèves : Actualité SEO + Recherche agentique + Actualité IA / search IA. Variation des piliers tenue par rapport à 2026-06-06-v3 (Product-Led SEO).
