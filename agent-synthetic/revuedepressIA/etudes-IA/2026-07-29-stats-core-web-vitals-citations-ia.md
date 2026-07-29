---
type: query
skill: seo-page-statistiques
status: draft
title: "Core Web Vitals et citations IA 2025-2026 : le FCP fait 3,2× pour ChatGPT, mais l'autorité fait 5×"
aliases: ["core web vitals citations ia", "vitesse page citations ia", "LCP CLS INP ai overviews", "page speed chatgpt perplexity citations"]
tags: [geo, aeo, citations-ia, core-web-vitals, page-speed, fcp, lcp, inp, cls, chatgpt, ai-overviews, seo-technique, confound]
created: 2026-07-29
updated: 2026-07-29
sources: 5
confidence: medium
---

# Core Web Vitals et citations IA 2025-2026 : le FCP fait 3,2× pour ChatGPT, mais l'autorité fait 5×

Un First Contentful Paint inférieur à 0,4 seconde correspond à 3,2 fois plus de citations ChatGPT qu'un FCP dépassant 1,1 seconde. Sur Google AI Overviews en revanche, la corrélation entre vitesse de chargement (LCP) et probabilité de citation plafonne à −0,18 sur 107 352 pages. Ces deux chiffres coexistent sans se contredire. Ils mesurent des mécanismes distincts, sur des moteurs distincts. Et dans les deux cas, l'autorité de domaine reste un prédicteur supérieur à la vitesse, que les études n'isolent pas.

---

## Les chiffres clés (vérifiés à la source)

| Indicateur | Valeur | Moteur | Source |
|---|---|---|---|
| Citations ChatGPT moy., FCP <0,4 s | 6,7 | ChatGPT Search | SE Ranking, 129 000 domaines |
| Citations ChatGPT moy., FCP >1,1 s | 2,1 | ChatGPT Search | SE Ranking, 129 000 domaines |
| Ratio de citations entre FCP extrêmes | 3,2× | ChatGPT Search | SE Ranking, 129 000 domaines |
| Citations ChatGPT moy., INP <0,4 s | 1,6 (le plus bas) | ChatGPT Search | SE Ranking, 129 000 domaines |
| Citations ChatGPT moy., INP 0,8-1,0 s | 4,5 (le plus haut) | ChatGPT Search | SE Ranking, paradoxe |
| Corrélation Spearman LCP / visibilité AIO | −0,12 à −0,18 | Google AIO + AI Mode | Dan Taylor, SALT.agency, 107 352 pages |
| Corrélation Spearman CLS / visibilité AIO | −0,05 à −0,09 | Google AIO + AI Mode | Dan Taylor, SALT.agency, 107 352 pages |
| Domaines cités AIO passant les 3 CWV | 56,8 % | Google AIO | PageSpeedMatters, 74 domaines |
| Web moyen (toutes origines) passant les 3 CWV | ~40 % | Référence web | CrUX / Web Almanac 2025 |
| Taux de passage LCP "good" parmi pages citées AIO | 74,3 % | Google AIO | PageSpeedMatters |
| Taux de passage LCP "good" web global (mobile) | 62 % | Référence web | DigitalApplied, CrUX mai 2026 |
| Citations ChatGPT moy., domaines >350 000 référents | 8,4 | ChatGPT Search | SE Ranking, même dataset |
| Citations ChatGPT moy., domaines ~2 500 référents | 1,6-1,8 | ChatGPT Search | SE Ranking, même dataset |
| Ratio autorité (haute vs basse) dans même dataset | ~5× | ChatGPT Search | SE Ranking, calcul interne |

---

## Pourquoi FCP fait 3× pour ChatGPT et presque rien pour Google AIO

La divergence entre SE Ranking (FCP 3,2×, ChatGPT) et Dan Taylor (LCP −0,12, Google AIO) n'est pas une contradiction. Les deux moteurs crawlent différemment.

ChatGPT Search envoie GPTBot au moment de la requête, sur des pages non encore dans son cache. Le crawler IA doit charger, parser et extraire le contenu en temps réel. Un site lent ou rendu uniquement via JavaScript sera partiellement ou totalement inaccessible au moment de la récupération. Le FCP mesure précisément le délai avant que le premier contenu textuel soit disponible. Un FCP long correspond concrètement à un crawler qui attend et qui, passé un certain seuil, abandonne la page. C'est un effet de crawlabilité, pas un signal de pertinence.

Google AI Overviews s'appuient sur l'index Googlebot existant. Googlebot a déjà crawlé les pages lors de ses passages réguliers. La vitesse du site au moment de la génération de la réponse IA ne joue pas. La faible corrélation mesurée par Dan Taylor (−0,12 à −0,18) reflète cet écart mécanique : pour Google AIO, la vitesse n'est pas un filtre de sélection, elle était un prérequis au moment du crawl, pas de la réponse.

Cette distinction explique également pourquoi PageSpeedMatters observe que 56,8 % des domaines cités dans les AI Overviews passent les Core Web Vitals contre ~40 % en moyenne web. Ces sites ne sont pas cités parce qu'ils sont rapides. Ils sont cités parce qu'ils sont reconnus (Wikipedia, sites gouvernementaux, universités), et ces institutions investissent dans des infrastructures bien maintenues.

---

## L'effet confondant autorité-vitesse

PageSpeedMatters documente les vitesses de chargement des domaines les plus cités dans les AI Overviews : Wikipedia à 0,8 seconde, les sites gouvernementaux à 0,9 seconde, les pages universitaires entre 1,1 et 1,2 seconde. Ce sont les mêmes domaines qui concentrent le plus de citations IA sur tous les moteurs.

Ces organisations ont en commun une infrastructure techniquement mature : réseaux de distribution de contenu, architectures statiques, équipes dédiées à la performance. Leur vitesse est une conséquence de leur taille et de leurs moyens, pas une cause de leur citation.

Dans les propres données de SE Ranking, l'écart dû à l'autorité (nombre de domaines référents) est plus grand que l'écart dû à la vitesse. Les domaines avec plus de 350 000 domaines référents obtiennent en moyenne 8,4 citations ChatGPT, contre 1,6 à 1,8 pour ceux avec 2 500 domaines référents. C'est un facteur 5×, contre 3,2× pour le FCP. L'autorité prédit mieux la citation que la vitesse, dans le même dataset, sans que ni l'étude SE Ranking ni l'étude Dan Taylor n'aient contrôlé explicitement l'une par l'autre.

La corrélation vitesse-citation existe. Sa cause probable est que les domaines les plus cités sont aussi les mieux financés techniquement. L'étude manquante serait un modèle multivarié qui contrôle simultanément vitesse et autorité sur le même corpus. Aucune étude publiée à ce jour ne l'a réalisé.

---

## Le paradoxe INP

SE Ranking mesure un résultat contre-intuitif sur le délai de réponse interactive (INP) : les pages avec un INP inférieur à 0,4 seconde obtiennent en moyenne 1,6 citations ChatGPT, soit le score le plus bas de toute la distribution. Les pages avec un INP modéré entre 0,8 et 1,0 seconde obtiennent 4,5 citations, soit le score le plus haut.

Une interprétation plausible : un INP parfait correspond à des pages très réactives mais peu riches en contenu (pages de liste, formulaires, interfaces d'application). Ces pages ont peu de texte extractible. Un INP modéré correspond davantage à des pages d'articles longus avec du JavaScript de mise en page, qui ralentissent légèrement l'interactivité mais portent plus de contenu dense.

Ce paradoxe rappelle que les Core Web Vitals ont été conçus pour mesurer l'expérience utilisateur humaine, pas la capacité d'extraction des crawlers IA. Les deux métriques ne convergent pas systématiquement.

---

## Pourquoi ces chiffres divergent : trois études, trois objets distincts

| Étude | Moteur | Méthode | Corrélation mesurée |
|---|---|---|---|
| SE Ranking (nov. 2025, 129 000 domaines) | ChatGPT Search | XGBoost SHAP | FCP 3,2× (effet large) |
| Dan Taylor (jan. 2026, 107 352 pages) | Google AIO + AI Mode | Spearman | LCP −0,12 à −0,18 (effet faible) |
| PageSpeedMatters (mai 2026, 74 domaines) | Google AIO | Distribution CrUX | 56,8 % vs 40 % pass rate |

Les trois études mesurent des objets différents :

SE Ranking quantifie l'effet de la vitesse sur le nombre de citations pour ChatGPT, en contrôlant 20 autres variables par régression. La vitesse est ici un signal de crawlabilité.

Dan Taylor mesure la corrélation entre les scores CWV d'une page et sa présence dans les AI Overviews de Google. La corrélation est faible parce que Googlebot a déjà résolu le problème de crawlabilité en amont.

PageSpeedMatters compare la distribution des taux de passage CWV entre les domaines cités et le web général. Il ne mesure pas une corrélation par page, mais la composition du pool de domaines cités. Un pool plus rapide en moyenne que le web s'explique par la composition de ce pool (institutions, médias de référence, encyclopédies), pas par un mécanisme de sélection par la vitesse.

Réconciliation : la vitesse de chargement est un prérequis de crawlabilité (effet réel pour ChatGPT) mais pas un signal de sélection direct (effet nul à faible pour Google AIO). L'apparente surcitation des sites rapides reflète la composition du pool de référence, lui-même dominé par des domaines à haute autorité qui sont aussi bien maintenus techniquement.

---

## Nos propres données (données de première main)

Le portefeuille de propriétés suivi dans ce vault n'inclut pas de mesure isolée des Core Web Vitals croisée avec les taux de citation IA par URL. La fiche preuve active ([[preuves/2026-07-10-organikk-batch-juillet-data-proprietaire]]) suit les impressions et clics GSC sur un batch publié en juillet 2026, sans instrumentation CWV parallèle. Ce bloc est réservé honnêtement. Le protocole à mettre en place serait : extraire les scores CrUX par URL depuis la GSC ou PageSpeed Insights API, les croiser avec les citations IA détectées via Brand Radar ou Profound, sur un minimum de 50 URLs avec ancienneté comparable. Ce n'est pas en place à date.

---

## Contre-analyse

**1. La corrélation SE Ranking ne contrôle pas l'autorité.** Le modèle XGBoost identifie le FCP comme variable importante, mais dans un dataset où les sites rapides sont statistiquement aussi les sites les plus liés. Un contrôle simultané par autorité de domaine réduirait probablement l'effet FCP. SE Ranking publie séparément l'effet autorité (5× sur les liens référents) mais ne croise pas les deux dans un modèle unique.

**2. La corrélation Dan Taylor est statistiquement quasi nulle.** Une corrélation de Spearman entre −0,12 et −0,18 est proche de zéro. Sur 107 352 pages, le coefficient peut être significatif statistiquement tout en n'étant pas opérationnellement significatif. Dan Taylor lui-même conclut que les CWV "agissent comme une contrainte, pas un levier de croissance". Il reconnaît que l'étude ne contrôle pas l'autorité.

**3. L'échantillon PageSpeedMatters est trop restreint.** 74 domaines sur 13 requêtes informationnel (santé, finance, culture générale) ne représentent pas la distribution des requêtes citant des sources variées. L'échantillon surreprésente les requêtes où Wikipedia et les sites gouvernementaux dominent, ce qui gonfle mécaniquement le taux de passage CWV des sites cités.

**4. Vitesse et crawlabilité ne sont pas synonymes.** Les timeouts GPTBot sont documentés par des sources secondaires (1 à 5 secondes selon plusieurs publications), sans confirmation par une source primaire OpenAI. Un site avec un FCP de 0,8 seconde peut être entièrement crawlable. La discontinuité n'est pas à 0,4 seconde mais vraisemblablement plus haute, au niveau du timeout de rendu JavaScript.

**5. Le paradoxe INP invalide une lecture linéaire.** Si "plus vite = plus de citations", un INP parfait devrait maximiser les citations. Ce n'est pas ce que mesure SE Ranking. La relation n'est pas monotone, ce qui suggère que la vitesse interact avec le type de contenu d'une façon que les études de corrélation ne capturent pas.

---

## FAQ

**Les Core Web Vitals sont-ils un facteur de citation pour les AI Overviews de Google ?**
Pas directement. Les AIO s'appuient sur l'index Googlebot, pas sur la vitesse live. La corrélation observée (−0,12 à −0,18 pour le LCP) est trop faible pour être un signal opérationnel. En revanche, un site qui ne passe pas le crawl Googlebot n'entre pas dans le pool, et la vitesse conditionne la qualité de ce crawl.

**Faut-il viser un FCP inférieur à 0,4 seconde pour apparaître dans ChatGPT ?**
Le seuil de 0,4 seconde est le percentile le plus favorable observé par SE Ranking, pas un critère binaire. La relation est continue. Ce qui compte est d'éviter les extrêmes bas (FCP >1,1 seconde) qui correspondent à des pages difficiles ou impossibles à crawler à la requête. Un FCP entre 0,4 et 0,8 seconde couvre la majorité du gain documenté.

**Pourquoi les sites gouvernementaux et universitaires sont-ils cités et rapides à la fois ?**
Ils bénéficient d'une infrastructure publique financée (réseaux nationaux, CDN institutionnels, architectures statiques) et d'une haute autorité institutionnelle accumulée. Ce sont deux propriétés corrélées mais causalement distinctes. Leur vitesse n'est pas la raison pour laquelle les moteurs IA les citent.

**Les crawlers IA abandonnent-ils les pages lentes ?**
Plusieurs publications évoquent des timeouts entre 1 et 5 secondes pour GPTBot et PerplexityBot. Aucune documentation primaire d'OpenAI ou d'Anthropic ne confirme ces seuils à date. L'abandon d'une page par un crawler IA privée de source primaire est donc [À SOURCER]. Ce qui est confirmé : les pages rendues uniquement par JavaScript sont moins bien crawlées, quelle que soit leur vitesse TTFB.

---

## [À SOURCER]

- **Timeouts GPTBot et PerplexityBot** : plusieurs sources secondaires citent 1 à 5 secondes. Aucune documentation officielle OpenAI ou Anthropic vérifiable par fetch à date. À surveiller dans les mises à jour des pages robots.txt et documentation développeurs.
- **Corrélation LCP/AIO contrôlée par DA** : aucune étude publiée à ce jour ne croise simultanément vitesse et autorité de domaine dans un modèle multivarié sur les pages citées par les moteurs IA.
- **Données France / Europe** : toutes les études citées sont sur des corpus anglophones (US principalement). L'effet vitesse sur les pages citées en français n'est pas documenté.
- **Distribution CWV par catégorie de contenu** pour les pages citées : aucune étude ne ventile LCP/INP/CLS séparément pour les articles de blog, les pages institutionnelles, les pages e-commerce dans le contexte des citations IA.
- **Taux de passage CWV des pages citées par ChatGPT et Perplexity** : PageSpeedMatters ne couvre que Google AIO. Aucune étude équivalente sur ChatGPT Search ou Perplexity publiée à date.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté |
|---|---|---|---|---|
| "How to Optimize for ChatGPT: Skip LLMs.txt, Earn Trust on Quora & Reddit" | SE Ranking | Nov. 2025 | https://seranking.com/blog/how-to-optimize-for-chatgpt/ | 2026-07-29 |
| "What 107,000 pages reveal about Core Web Vitals and AI search" | Search Engine Land (Dan Taylor, SALT.agency) | 13 jan. 2026 | https://searchengineland.com/core-web-vitals-ai-search-visibility-analysis-467456 | 2026-07-29 |
| "Are AI Overview Citations Fast? 57% Pass Core Web Vitals" | PageSpeedMatters | Mai 2026 | https://www.pagespeedmatters.com/resources/data-studies/ai-overview-citation-speed | 2026-07-29 |
| "Core Web Vitals Benchmarks 2026: What Good Looks Like" | DigitalApplied | 2026 | https://www.digitalapplied.com/blog/core-web-vitals-benchmarks-2026-pass-rate-reference | 2026-07-29 |
| "Core Web Vitals Data Study: Insights from 8M+ Sites" | TryAnalyze.ai | 2025 | https://www.tryanalyze.ai/blog/core-web-vitals-data-study | 2026-07-29 |
