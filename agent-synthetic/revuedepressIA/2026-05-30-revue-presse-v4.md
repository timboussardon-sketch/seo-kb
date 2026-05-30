---
type: revue-presse
title: "llms.txt et recherche IA : Google confirme qu'il n'utilise pas ce fichier, malgré son apparition sur ses propres pages"
date: 2026-05-30
tags: [revue-presse, algorithme, geo, llms-txt, aeo]
status: draft
edition: synthetic-brain-v4
---

# llms.txt et recherche IA : Google confirme qu'il n'utilise pas ce fichier, malgré son apparition sur ses propres pages

**L'essentiel en 4 points**
- Google répète qu'il n'utilise pas le fichier `llms.txt` pour la visibilité dans Search, AI Mode et AI Overviews : ces surfaces s'appuient sur le même index que la recherche classique.
- L'apparition d'un `llms.txt` sur des pages de Google fin 2025 a entretenu la confusion, mais les porte-parole de l'équipe Search ont confirmé qu'il ne s'agissait pas d'un signal d'adoption.
- Côté données, la recherche interne de la KB (benchmark SAGEO Arena) indique que le levier de visibilité qui fonctionne est l'optimisation des champs structurels (title, meta, headings, schema), pas un fichier dédié aux IA.
- Trois autres faits cette semaine : Gemini gagne des parts d'usage face à ChatGPT (chiffres divergents selon la mesure), Google a redessiné son champ de recherche pour des requêtes plus longues et multimodales, et le CTR des AI Overviews remonte pour les pages citées.

---

## L'info du jour : Google maintient que `llms.txt` ne sert pas sa recherche IA

Le fichier `llms.txt` est un format proposé par une partie de la communauté pour donner aux modèles de langage une version simplifiée d'un site, à la manière d'un `robots.txt` orienté IA. La question revient à chaque cycle d'actualité : faut-il en publier un pour être mieux cité dans les réponses générées ? Pour la recherche de Google, la réponse documentée est non.

Gary Illyes, de l'équipe Search, l'a déclaré au Search Central Live Deep Dive Asie-Pacifique du 23 juillet 2025 : « Google ne supporte pas `llms.txt` et n'a pas l'intention de le faire. » Selon la même intervention, pour apparaître dans un AI Overview, il suffit d'appliquer les pratiques SEO habituelles, sans technique séparée dédiée aux moteurs génératifs. John Mueller, également de Google, a comparé `llms.txt` au `meta keywords`, une balise abandonnée depuis longtemps, en notant qu'aucun service d'IA ne consomme le fichier et que les robots ne le demandent pas. Source : [Search Engine Land : Google says normal SEO works and llms.txt won't be used](https://searchengineland.com/google-says-normal-seo-works-for-ranking-in-ai-overviews-and-llms-txt-wont-be-used-459422) · [Passionfruit : Should I create an llms.txt file (2026)](https://www.getpassionfruit.com/blog/should-i-create-an-llms.txt-file-google-s-2026-guidance-explained) · [The SEO Community : Consensus on llms.txt](https://theseocommunity.com/resources/blog/llms-txt-should-we-or-not).

La confusion vient d'un épisode précis. Fin 2025, un fichier `llms.txt` est apparu sur des pages de Google, ce qui a fait penser que différentes équipes de l'entreprise avançaient en ordre dispersé. Barry Schwartz a relayé la découverte, et la spéculation a porté sur une éventuelle divergence interne. Les porte-parole de l'équipe Search ont depuis confirmé que cette présence ne valait pas adoption. Source : [The SEO Community](https://theseocommunity.com/resources/blog/llms-txt-should-we-or-not) · [Search Engine Roundtable : Google does not endorse llms.txt](https://www.seroundtable.com/google-does-not-endorse-llms-txt-40789.html).

La position a été reprise dans le guide d'optimisation pour la recherche IA publié par Google le 15 mai 2026, qui classe `llms.txt` parmi les tactiques sans effet sur la visibilité. Le raisonnement est technique : AI Overviews et AI Mode tirent leurs réponses du même index que le classement classique, donc un fichier que ce système ne lit pas n'a pas d'effet sur la présence dans les réponses. Source : [Passionfruit](https://www.getpassionfruit.com/blog/should-i-create-an-llms.txt-file-google-s-2026-guidance-explained) · [Lumar : AI Search & SEO Industry News, mai 2026](https://www.lumar.io/blog/industry-news/seo-ai-search-industry-news-may-2026-google-io-core-update-ai-mode-more/).

Les faits, en clair :

- Google ne supporte pas `llms.txt` pour Search, AI Mode et AI Overviews, position énoncée par Gary Illyes le 23 juillet 2025 et maintenue depuis ([Search Engine Land](https://searchengineland.com/google-says-normal-seo-works-for-ranking-in-ai-overviews-and-llms-txt-wont-be-used-459422)).
- John Mueller a comparé le fichier au `meta keywords` abandonné ; aucun service d'IA ne le consomme, les robots ne le demandent pas ([Passionfruit](https://www.getpassionfruit.com/blog/should-i-create-an-llms.txt-file-google-s-2026-guidance-explained), [The SEO Community](https://theseocommunity.com/resources/blog/llms-txt-should-we-or-not)).
- Un `llms.txt` est apparu sur des pages de Google fin 2025, sans valoir adoption ([Search Engine Roundtable](https://www.seroundtable.com/google-does-not-endorse-llms-txt-40789.html)).
- Le guide IA de Google du 15 mai 2026 liste `llms.txt` parmi les tactiques sans effet ([Lumar](https://www.lumar.io/blog/industry-news/seo-ai-search-industry-news-may-2026-google-io-core-update-ai-mode-more/)).

Ce que cela change concrètement :

Pour la recherche de Google, publier un `llms.txt` n'apporte pas de visibilité supplémentaire dans les réponses IA. Cela ne signifie pas que le fichier est inutile partout : d'autres systèmes peuvent décider de le lire, et certains outils en publient déjà. Mais le présenter comme un prérequis pour être cité par Google n'est pas confirmé par les faits actuels.

Cette position recoupe ce que mesure la doctrine interne. Le benchmark SAGEO Arena (170 000 documents, voir [[concepts/structural-information-geo]]) montre que le levier le plus efficace au retrieval est l'optimisation des champs structurels (title, meta, headings, schema markup), avec un gain de Hit Rate jusqu'à +35 % quand on y ajoute des données chiffrées, alors que réécrire le corps de texte dégrade le retrieval. Le concept [[concepts/aeo]] de la KB pose la même logique : être cité dans les réponses IA passe par le travail SEO et structurel, pas par un canal séparé. Autrement dit, la donnée empirique et la position de Google convergent : l'effort utile porte sur la structure et le contenu indexés, pas sur un fichier parallèle.

Un point d'appui à manier avec prudence, car il vient d'une seule étude : une analyse de SE Ranking sur 39 000 domaines ne trouve pas de corrélation entre la présence d'un `llms.txt` et la fréquence de citation par les IA. La formulation des auteurs reste ouverte (« pas encore »), donc cela mesure l'état actuel, pas une impossibilité future. Source : [The SEO Community](https://theseocommunity.com/resources/blog/llms-txt-should-we-or-not).

Recommandation opérationnelle : ne pas prioriser la production d'un `llms.txt` pour viser la recherche IA de Google. Mettre l'effort sur les title, meta, headings et le schema markup (`Article`, `FAQPage`, `Product`, `Dataset`), et sur l'information distinctive que contient la page. Si vous publiez un `llms.txt` pour d'autres systèmes, traitez-le comme un test mesuré, pas comme un facteur de classement acquis.

---

## Aussi sur le radar

**Gemini gagne des parts d'usage face à ChatGPT, mais les chiffres dépendent de l'outil de mesure**
Plusieurs jeux de données convergent sur une direction : la part de ChatGPT recule sur plusieurs mois et celle de Gemini progresse. Les valeurs exactes, en revanche, divergent fortement selon la méthode. Le clickstream de Similarweb situe ChatGPT autour de 56,7 % du trafic IA générative en mars 2026 contre 25,5 % pour Gemini. Statcounter, qui mesure les référents, donne ChatGPT à 76,9 % des renvois de chatbots en avril 2026, à son plus bas niveau enregistré. D'autres agrégateurs publient des répartitions différentes encore. Aucune valeur unique n'est donc fiable en l'état, mais la tendance est corroborée.

Conséquence pour la visibilité dans les moteurs génératifs : optimiser pour un seul assistant crée un risque de dépendance. Si Gemini gagne des utilisateurs, en particulier via l'intégration dans Android, Chrome et Workspace, viser uniquement ChatGPT laisse de côté une audience croissante. Le travail de visibilité gagne à être vérifié sur plusieurs moteurs, pas un seul. Sources : [Similarweb : Gen AI Stats 2026](https://www.similarweb.com/blog/marketing/geo/gen-ai-stats/) · [TechRadar : ChatGPT referral share](https://www.techradar.com/pro/new-figures-claim-chatgpt-usage-at-all-time-low-as-quitgpt-movement-dents-popularity-with-gemini-perplexity-and-copilot-all-stealing-market-share) · [TechnologyChecker : Search Engine Market Share 2026](https://technologychecker.io/blog/search-engine-market-share).

**Google a redessiné le champ de recherche pour des requêtes plus longues et multimodales**
À sa conférence I/O du 19 mai, Google a présenté un nouveau champ de recherche qu'il décrit comme son plus gros changement de cet élément depuis plus de 25 ans. Le champ s'agrandit pendant la saisie, accepte du texte, des images, des fichiers, des vidéos et des onglets Chrome comme entrées, et propose des suggestions générées par IA au-delà de l'autocomplétion. Le déploiement a commencé dans les pays et langues où AI Mode est disponible.

Pour le SEO, l'implication porte sur la nature des requêtes. Un champ qui encourage des saisies plus longues et descriptives déplace une partie du trafic vers des requêtes précises et conversationnelles, où la réponse exacte à une intention détaillée compte davantage que le positionnement sur un mot-clé court. Sources : [blog.google : Search I/O 2026](https://blog.google/products-and-platforms/products/search/search-io-2026/) · [Tom's Guide](https://www.tomsguide.com/ai/google-gemini/google-search-box-just-got-the-biggest-makeover-in-nearly-30-years) · [Search Engine Journal : SEO Pulse](https://www.searchenginejournal.com/seo-pulse-google-launches-core-update-amid-i-o-ai-search-overhaul/575676/).

**Le CTR des AI Overviews remonte, et les pages citées en captent l'essentiel**
Une mise à jour de l'étude de Seer Interactive, relayée par Search Engine Land le 24 avril 2026, mesure que le taux de clic sur les pages des AI Overviews est remonté de 1,3 % en décembre 2025 à 2,4 % en février 2026. Sur les SERP qui affichent un AI Overview, les pages citées dans le bloc reçoivent environ 120 % de clics par impression de plus que les pages non citées de la même page de résultats. L'étude porte sur 53 marques et plus de 5 millions de requêtes, de janvier 2025 à février 2026.

Ce chiffre est daté de février 2026 et publié fin avril, donc il faut le lire comme une mesure de tendance, pas comme l'état du jour. Il confirme une orientation déjà identifiée : sur une requête où Google affiche un AI Overview, la présence dans les citations du bloc est ce qui ramène des clics. Sources : [Search Engine Land : AI Overviews CTR recovery](https://searchengineland.com/google-ai-overviews-ctr-recovery-study-475566) · [Seer Interactive : AIO Impact on Google CTR 2026](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update) · [Search Engine Journal : AI Overview CTR fell 61% but clicks didn't collapse](https://www.searchenginejournal.com/ai-overview-ctr-fell-61-but-clicks-didnt-collapse/572993/).

---

*Édition produite par SyntheticBrain. Rien n'a été envoyé. Draft à relire.*
