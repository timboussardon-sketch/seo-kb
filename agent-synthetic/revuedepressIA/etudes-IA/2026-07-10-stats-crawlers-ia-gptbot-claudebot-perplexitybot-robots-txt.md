---
type: query
skill: seo-page-statistiques
title: "Crawlers IA 2025-2026 : fréquence, profondeur et taux de blocage robots.txt"
aliases: ["crawlers IA statistiques", "GPTBot ClaudeBot blocage robots.txt", "AI bots crawl 2026", "GPTBot statistiques", "taux de blocage crawlers IA"]
tags: [seo, ia, geo, crawlers-ia, robots-txt, gptbot, claudebot, perplexitybot, llms-txt]
created: 2026-07-10
updated: 2026-07-10
sources: 8
confidence: high
status: draft
---

# Crawlers IA 2025-2026 : GPTBot en tête du volume, ClaudeBot 37 % plus profond, et bloquer un crawler divise les citations par 139

En janvier 2025, le crawler d'Anthropic effectuait 286 930 requêtes pour chaque visiteur renvoyé vers un site. Ce ratio résume le déséquilibre entre extraction et redistribution qui caractérise l'économie des bots IA aujourd'hui. Les réactions varient selon la taille des sites : seulement 5,89 % du web général bloque GPTBot, contre 13,9 % des sites les plus visibles, et 62 % des grands éditeurs de presse. Or les études mesurent désormais un coût direct : les sites qui bloquent GPTBot reçoivent en médiane 139 fois moins de citations dans ChatGPT que ceux qui l'autorisent.

---

## Les chiffres clés (vérifiés à la source)

**Volume et parts de marché**

- GPTBot a progressé de 2,2 % à 7,7 % de l'ensemble du trafic de crawlers entre mai 2024 et mai 2025, soit +305 % en volume de requêtes. [[sources/cloudflare-from-googlebot-to-gptbot]]
- ChatGPT-User (bot de récupération en temps réel d'OpenAI) a grimpé de 0,1 % à 1,3 % sur la même période, soit +2 825 %. [[sources/cloudflare-from-googlebot-to-gptbot]]
- PerplexityBot : +157 490 % en parts de marché, depuis une base quasi nulle (< 0,01 % → 0,2 %). [[sources/cloudflare-from-googlebot-to-gptbot]]
- En juillet 2025, GPTBot représente 11,7 % des requêtes de bots vérifiés (hors Googlebot), ClaudeBot 9,9 %. [[sources/cloudflare-crawlers-click-ai-bots-training]]

**Finalité du crawl**

- 79-80 % de l'activité totale des crawlers IA est dédiée à l'entraînement de modèles en juillet 2025, contre 72 % un an plus tôt. [[sources/cloudflare-crawlers-click-ai-bots-training]]
- En juin 2026, Cloudflare distingue trois catégories : entraînement seul (52,3 %), usage mixte (35,7 %), recherche seule (9,3 %). La part du trafic incluant une composante d'entraînement reste donc supérieure à 88 %. [[sources/technologychecker-robots-txt-report]]

**Fréquence et profondeur**

- GPTBot revisite les pages à fort trafic toutes les 2,4 jours en médiane, ramenées à 1,6 jour quand un en-tête `Last-Modified` récent est détecté. [[sources/digitalapplied-30-day-log-study]]
- ClaudeBot explore en profondeur : profondeur moyenne de navigation de 5,2 niveaux contre 3,8 pour GPTBot. Il revisite toutes les 6,8 jours. [[sources/digitalapplied-30-day-log-study]]
- PerplexityBot : aucun crawl programmé en arrière-plan. Il n'explore qu'en réponse à une requête utilisateur, avec des pics pouvant atteindre 240 requêtes par minute. [[sources/digitalapplied-30-day-log-study]]

**Ratios crawl/référral**

- Janvier 2025 : Anthropic (ClaudeBot) génère 286 930 requêtes par visite renvoyée. [[sources/cloudflare-crawlers-click-ai-bots-training]]
- Juillet 2025 : ce ratio tombe à 38 065:1 (-86,7 %), signe de la montée en puissance des usages de Claude dans les navigateurs. [[sources/cloudflare-crawlers-click-ai-bots-training]]
- OpenAI (GPTBot + ChatGPT-User) : 1 217:1 en janvier, 1 091:1 en juillet 2025 (-10 %). [[sources/cloudflare-crawlers-click-ai-bots-training]]
- Perplexity : 54:1 en janvier, 194:1 en juillet (+256 %). Perplexity renvoie proportionnellement plus de trafic que les autres plateformes IA. [[sources/cloudflare-crawlers-click-ai-bots-training]]

**Taux de blocage robots.txt**

- Sur ~140 millions de sites (Ahrefs, août 2023 - décembre 2024) : GPTBot bloqué sur 5,89 %, CCBot 5,85 %, ClaudeBot 5,74 %, PerplexityBot 5,61 %. [[sources/ahrefs-ai-bot-block-rates]]
- Croissance annuelle des règles de blocage spécifiques à ClaudeBot : +32,67 %, la plus forte parmi les crawlers IA. GPTBot : +13,38 %. [[sources/ahrefs-ai-bot-block-rates]]
- Parmi 1 058 domaines à forte visibilité (cloro.dev, juillet 2026) : ClaudeBot 15,4 %, GPTBot 13,9 %, PerplexityBot 8,6 %, OAI-SearchBot 3,4 %. [[sources/cloro-dev-gptbot-blocking]]
- Dans les 100 premiers éditeurs de presse (BuzzStream, juillet 2025) : ClaudeBot 69 %, PerplexityBot 67 %, GPTBot 62 %, OAI-SearchBot 49 %. [[sources/buzzstream-publishers-block-ai]]

**Effet du blocage sur les citations**

- Domaines bloquant GPTBot : médiane de 0,003 citations ChatGPT par position Google détenue. Domaines qui l'autorisent : 0,417. Ratio : 139 fois moins. [[sources/cloro-dev-gptbot-blocking]]
- L'effet est spécifique au crawler bloqué : les sites qui bloquent PerplexityBot reçoivent 0 citation Perplexity en médiane, contre 1,167 pour les non-bloquants. [[sources/cloro-dev-gptbot-blocking]]

**Conformité robots.txt et crawl fantôme**

- GPTBot, ClaudeBot, Google-Extended et PerplexityBot affichent 100 % de conformité aux directives robots.txt sur 30 jours de logs (12 sites, DigitalApplied). [[sources/digitalapplied-30-day-log-study]]
- Bytespider (ByteDance) et cohere-ai : 96-99 % de conformité. [[sources/digitalapplied-30-day-log-study]]
- ChatGPT-User et Perplexity-User génèrent en revanche ~690 hits par jour et par site indépendamment du robots.txt, car ces agents sont déclenchés par un utilisateur réel. Ils ne sont pas soumis aux mêmes règles que les crawlers d'entraînement. [[sources/digitalapplied-30-day-log-study]]

**llms.txt : adoption et effet mesuré**

- 10,13 % des domaines analysés ont mis en place un fichier llms.txt (SE Ranking, 300 000 domaines). [[sources/seranking-llms-txt]]
- Aucune corrélation avec la fréquence de citation par les moteurs IA. Retirer llms.txt comme variable améliore la précision du modèle prédictif. [[sources/seranking-llms-txt]]
- Gary Illyes (Google) a confirmé en juillet 2025 que Google ne prend pas en charge llms.txt et ne prévoit pas de le faire.

---

## Volume, parts de marché : le reclassement de 2025

En mai 2024, Bytespider (ByteDance) dominait les crawlers IA avec 22,8 % du trafic. En mai 2025, il est tombé à 2,9 % (-85 %), et GPTBot est passé de la neuvième à la troisième place tous crawlers confondus, derrière Googlebot et Bingbot.

Parmi les seuls crawlers IA, GPTBot détient 30 % du trafic en mai 2025, ClaudeBot 21 %, Meta-ExternalAgent 19 %, Amazonbot 11 %.

Ce basculement n'est pas homogène selon les secteurs. En août 2025, le secteur informatique / électronique (ordinateurs, composants) concentre plus de 40 % du trafic combiné de GPTBot et Amazonbot. Le commerce en ligne absorbe 26,3 % des requêtes de bots vérifiés. Les éditeurs de presse présentent une distribution plus équilibrée, avec GPTBot à 17,4 % et ChatGPT-User à 14,9 % de leur trafic IA.

---

## Fréquence et profondeur : trois stratégies d'exploration distinctes

L'étude de logs de DigitalApplied (12 sites, 30 jours, mars-avril 2026) permet de différencier les comportements.

GPTBot opère en mode étendu : 4 200 requêtes par site et par jour en médiane, exploration en largeur (breadth-first), profondeur de 3,8 niveaux, revisites toutes les 2,4 jours. Il représente 14 % de la charge CPU sur les petits sites (moins de 5 000 pages), et seulement 3 % sur les grands.

ClaudeBot est structurellement différent : 1 800 requêtes par jour, mais exploration en profondeur (depth-first) à 5,2 niveaux, revisites espacées à 6,8 jours. Il cible les arborescences de contenu plutôt que la surface.

PerplexityBot n'a pas de cycle d'exploration programmé. Il intervient en rafales de 240 requêtes par minute lorsqu'une question utilisateur le déclenche. Ce comportement de récupération à la demande l'assimile davantage à un agent de recherche en temps réel qu'à un robot de moisson.

Google-Extended se comporte comme une version allégée de Googlebot (540 requêtes par jour, cycle de 14 jours), limité aux propriétaires qui n'ont pas activé de blocage opt-in.

---

## Ratios crawl/référral : l'extraction nette d'Anthropic

Le ratio crawl-pour-référral mesure combien de pages un crawler explore pour chaque visite qu'il renvoie effectivement vers les éditeurs. Anthropic affiche les valeurs les plus déséquilibrées.

En janvier 2025, ClaudeBot réalise 286 930 requêtes par visite référée. Ce chiffre spectaculaire traduit le fait que Claude n'avait pas de navigateur web actif au début de 2025 : le crawler entraînait les modèles mais ne generait pas de trafic sortant. D'ici juillet 2025, l'écart se réduit à 38 065:1 (-86,7 %) à mesure que Claude.ai intègre des capacités de navigation.

OpenAI stabilise autour de 1 100:1, reflet d'un produit (ChatGPT Search) qui allie exploration et redistribution depuis plus longtemps. Perplexity va dans la direction opposée : son ratio passe de 54:1 à 194:1 sur la même période, signe que la croissance de son volume de crawl dépasse celle de ses visites référées.

---

## Pourquoi les taux de blocage varient d'un facteur 10 selon la taille du site

C'est la transformation originale de cette étude : trois corpus mesurent le même taux de blocage GPTBot, et les résultats divergent d'un facteur 10.

| Corpus | Sites analysés | Blocage GPTBot | Méthode |
|---|---|---|---|
| Ahrefs (web général) | ~140 millions | 5,89 % | Robots.txt tous domaines |
| cloro.dev (domaines visibles) | 1 058 | 13,9 % | Robots.txt sources IA citées |
| BuzzStream (presse) | 100 | 62 % | Robots.txt top publishers |

Les trois études ne mesurent pas la même population. Plus un site génère de trafic et plus il a de valeur à protéger, plus la probabilité de blocage est élevée. Ce gradient n'est pas linéaire : il devient abrupt au-dessus d'un seuil de visibilité.

Le même écart s'observe entre bots d'entraînement et bots de récupération. Dans le corpus cloro.dev, CCBot (entraînement) est bloqué sur 17,8 % des sites contre seulement 3,4 % pour OAI-SearchBot (récupération en temps réel). Chez les éditeurs de presse (BuzzStream), 79 % bloquent au moins un bot d'entraînement, 71 % au moins un bot de récupération. Les éditeurs distinguent désormais clairement les deux usages.

La taille du site explique aussi l'asymétrie dans les règles d'autorisation explicite. En mai 2026, GPTBot apparaît dans 5,65 % des règles ALLOW de la base Cloudflare, contre 4,71 % des règles DISALLOW : pour la première fois, le web dans sa globalité accueille formellement GPTBot plus souvent qu'il ne le repousse. Ce basculement n'est pas perceptible dans les corpus de grandes marques.

---

## Nos propres chiffres (données de première main)

Le vault documente deux éléments de première main sur ce sujet.

**L'incident Perplexity (août 2025).** Cloudflare a accusé Perplexity d'avoir exploré des sites ayant explicitement bloqué PerplexityBot via leur robots.txt. Perplexity a contesté l'interprétation. L'enquête a mis en évidence que Perplexity-User (agent déclenché par un utilisateur réel posant une question) contournait structurellement les directives robots.txt, puisque ces agents ne sont pas soumis au même régime d'exclusion que les bots d'entraînement. Cet incident a conduit Cloudflare à retirer temporairement Perplexity de sa liste de bots vérifiés. Il illustre la distinction fonctionnelle entre crawler d'entraînement (robots.txt contraignant) et agent de récupération en temps réel (robots.txt non contraignant).

**Robots.txt du site Algorithme.** La propriété concernée autorise explicitement GPTBot, OAI-SearchBot, PerplexityBot et Google-Extended via des règles `Allow: /` individuelles. Ce choix reflète la stratégie documentée dans cette étude : les données de cloro.dev indiquent qu'autoriser les crawlers de récupération est la condition nécessaire pour figurer dans les réponses des moteurs IA.

---

## Contre-analyse

**Biais d'échantillon sur les logs de crawl.** L'étude DigitalApplied (12 sites) fournit les seules données de profondeur et de fréquence disponibles publiquement, mais sa taille d'échantillon reste faible. Les 4 B2B SaaS, 3 sites e-commerce, 3 agences et 2 éditeurs représentent un profil particulier ; les résultats peuvent différer sensiblement pour des sites de presse, des wikis ou des portails gouvernementaux.

**Blocage et citations : corrélation ou causalité ?** L'étude cloro.dev montre une différence de citations entre sites bloquants et non-bloquants (0,003 vs 0,417), mais ne contrôle pas la qualité et l'autorité des domaines. Les sites qui bloquent les bots IA sont souvent des éditeurs de presse imposant des accords commerciaux : ils pourraient être moins cités pour d'autres raisons structurelles (accès payant, format peu fragmentable). La causalité directe n'est pas démontrée.

**Le paradoxe de la conformité robots.txt.** La conformité à 100 % des grands bots (GPTBot, ClaudeBot, PerplexityBot) concerne leurs crawlers d'entraînement déclarés. Elle ne couvre pas les agents utilisateur associés (ChatGPT-User, Perplexity-User), qui accèdent aux pages en temps réel à la demande des utilisateurs et ne sont pas soumis aux mêmes exclusions. Bloquer PerplexityBot n'empêche pas un utilisateur de Perplexity d'accéder à la page via Perplexity-User. Le robots.txt offre donc un contrôle partiel sur la présence dans les réponses IA.

**llms.txt : un standard sans adoption côté consommateur.** La conformité des crawlers IA au fichier llms.txt reste anecdotique. Google (Gary Illyes, juillet 2025) refuse explicitement de l'implémenter. SE Ranking mesure zéro corrélation entre présence du fichier et citations. Seul Anthropic (Claude.ai) déclare respecter les directives llms.txt dans ses flux de récupération, sans données publiques sur la fréquence de lecture effective.

---

## FAQ

**Bloquer GPTBot via robots.txt empêche-t-il d'être cité dans ChatGPT ?**
Pas systématiquement, mais les données indiquent un coût significatif. Les domaines bloquant GPTBot reçoivent 139 fois moins de citations ChatGPT par position Google détenue (médiane 0,003 vs 0,417, cloro.dev, 1 058 sites). Bloquer GPTBot (entraînement) n'affecte pas OAI-SearchBot (récupération temps réel), qui lui n'est bloqué que sur 3,4 % des sites visibles.

**ClaudeBot explore-t-il plus profondément que GPTBot ?**
Oui, selon l'étude de logs DigitalApplied (12 sites, 30 jours) : ClaudeBot atteint une profondeur moyenne de 5,2 niveaux contre 3,8 pour GPTBot. En contrepartie, ClaudeBot visite moins fréquemment (toutes les 6,8 jours contre 2,4 jours pour GPTBot) et génère moins de requêtes par jour (1 800 vs 4 200).

**PerplexityBot respecte-t-il le robots.txt ?**
PerplexityBot (crawler d'indexation) a affiché 100 % de conformité sur les 30 jours observés. Perplexity-User (agent temps réel) ne l'est pas soumis au même régime, ce que l'incident de l'été 2025 a mis en évidence.

**Le fichier llms.txt améliore-t-il la visibilité dans les réponses IA ?**
Les données disponibles ne le démontrent pas. Sur 300 000 domaines analysés par SE Ranking, aucune corrélation n'est mesurable entre adoption de llms.txt et fréquence de citation. Retirer la variable llms.txt du modèle prédictif améliore sa précision.

**Quelle plateforme renvoie le plus de trafic vers les éditeurs ?**
Perplexity présente le ratio crawl/référral le plus favorable parmi les grandes plateformes IA : 54:1 en janvier 2025, 194:1 en juillet. À titre de comparaison, Anthropic affichait 286 930:1 en janvier.

---

## [À SOURCER]

- Données de profondeur de crawl sur un échantillon plus large (> 100 sites). L'étude DigitalApplied repose sur 12 sites ; ses chiffres de profondeur (5,2 / 3,8) sont les seuls disponibles publiquement mais doivent être traités comme indicatifs.
- Taux de blocage des crawlers IA spécifique aux sites francophones. Toutes les études disponibles mesurent des populations anglophones ou globales non désagrégées.
- Effet causal du blocage sur les citations, contrôlé par autorité de domaine et qualité de contenu (une étude type diff-en-diff ou RCT n'existe pas encore).
- Fréquence réelle de récupération de llms.txt par GPTBot et OAI-SearchBot, avec logs vérifiables côté serveur.
- Volume de crawl 2026 pour Meta-ExternalAgent et Amazonbot, absents des études récentes sur les ratios crawl/référral.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté |
|---|---|---|---|---|
| The AI Bots That ~140 Million Websites Block the Most | Ahrefs | décembre 2024 | https://ahrefs.com/blog/ai-bot-block-rates/ | 2026-07-10 |
| The crawl-to-click gap: Cloudflare data on AI bots, training, and referrals | Cloudflare | août 2025 | https://blog.cloudflare.com/crawlers-click-ai-bots-training/ | 2026-07-10 |
| The crawl before the fall: understanding AI's impact on content providers | Cloudflare | juillet 2025 | https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar/ | 2026-07-10 |
| A deeper look at AI crawlers: breaking down traffic by purpose and industry | Cloudflare | août 2025 | https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/ | 2026-07-10 |
| From Googlebot to GPTBot: who's crawling your site in 2025 | Cloudflare | juin 2025 | https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/ | 2026-07-10 |
| Cloudflare Radar 2025 Year in Review | Cloudflare | janvier 2026 | https://blog.cloudflare.com/radar-2025-year-in-review/ | 2026-07-10 |
| Which News Sites Block AI Crawlers in 2025? | BuzzStream | avril 2026 | https://www.buzzstream.com/blog/publishers-block-ai-study/ | 2026-07-10 |
| Do Sites That Block GPTBot Get Cited Less by ChatGPT? | cloro.dev | juillet 2026 | https://cloro.dev/research/ai-crawler-blocks/ | 2026-07-10 |
| We Analyzed robots.txt Across Cloudflare's Network | TechnologyChecker | juin 2026 | https://technologychecker.io/blog/robots-txt-ai-crawlers-blocking-report | 2026-07-10 |
| Agentic Crawler Behavior: 30-Day Site Log Study 2026 | DigitalApplied | mai 2026 | https://www.digitalapplied.com/blog/agentic-crawler-behavior-30-day-site-log-study | 2026-07-10 |
| LLMs.txt: Why Brands Rely On It and Why It Doesn't Work | SE Ranking | 2026 | https://seranking.com/blog/llms-txt/ | 2026-07-10 |
