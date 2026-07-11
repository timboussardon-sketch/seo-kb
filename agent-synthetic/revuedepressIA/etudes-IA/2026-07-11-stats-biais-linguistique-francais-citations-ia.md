---
type: query
skill: seo-page-statistiques
title: "Langue française et citations IA : le français représente 4,7 % du web et 0,16 % des données d'entraînement des LLMs (2023-2026)"
aliases: ["biais-linguistique-francais-ia", "contenu-francophone-citations-ia", "francais-llm-training-data"]
tags: [geo, aeo, biais-linguistique, francais, llm, training-data, citations-ia, seo-france]
created: 2026-07-11
updated: 2026-07-11
sources: 9
confidence: medium
status: draft
---

# Langue française et citations IA : 4,7 % du web contre 0,16 % des données d'entraînement (2023-2026)

Le français représente 4,7 % des pages indexées dans Common Crawl (juin 2026). Dans les données d'entraînement de Llama 2, le modèle le plus documenté publiquement, ce taux tombe à 0,16 %. Facteur de compression : 29x. Ce déséquilibre ne disparaît pas à la génération : une source anglophone perd 55,3 % de sa visibilité dans les citations IA quand la requête est posée en français, selon une étude Weglot de juin 2026.

---

## Les chiffres clés (vérifiés à la source)

### Présence du français sur le web

W3Techs mesure la langue de contenu de 10 millions de sites chaque jour. En juillet 2026 :

- Anglais : 49,6 % des sites web
- Français : 4,6 % des sites web
- Espagnol : 6,1 %, Allemand : 6,0 %, Japonais : 5,0 %

Le corpus Common Crawl (CC-MAIN-2026-25), utilisé comme base de pré-entraînement par la plupart des grands modèles, donne un résultat cohérent : anglais à 40,8 %, français à 4,7 %. L'écart entre W3Techs (tous les sites) et Common Crawl (pages crawlées) reflète les différences de couverture de crawl — les deux convergent autour de 4,7 % pour le français.

### La compression dans les données d'entraînement

Llama 2 (Meta, 2023) est le seul modèle majeur à avoir publié la distribution complète de ses langues de pré-entraînement (Touvron et al., arXiv:2307.09288, tableau de distribution linguistique) :

| Langue | Part dans Llama 2 | Part dans Common Crawl (2026) |
|---|---|---|
| Anglais | 89,7 % | 40,8 % |
| Français | 0,16 % | 4,7 % |
| Allemand | 0,17 % | 5,9 % |
| Espagnol | 0,13 % | — |
| Chinois | 0,13 % | 4,6 % |

Facteur de compression anglais → Llama 2 : 89,7 / 40,8 = +2,2x (amplification).  
Facteur de compression français → Llama 2 : 0,16 / 4,7 = ÷29 (réduction).

Ce rapport de 29x entre présence web réelle et représentation dans les données d'entraînement est la mesure la plus directe du biais de construction — et non simplement du biais naturel dû à la domination de l'anglais sur internet.

BLOOM (BigScience, 176 milliards de paramètres) a fait un choix délibérément différent dans son corpus ROOTS (1,61 téraoctets, 46 langues, arXiv:2211.05100) :

| Langue | Part dans BLOOM/ROOTS |
|---|---|
| Anglais | ~30 % |
| Français | ~13 % |
| Espagnol | ~11 % |

À 13 %, le français reste sous-représenté par rapport à ses locuteurs (300 millions de natifs), mais le rapport anglais/français passe de 89,7 / 0,16 = 561 dans Llama 2 à 30 / 13 = 2,3 dans BLOOM. L'ordre de grandeur change complètement.

### L'impact sur les citations IA

Weglot (Rayne Aguilar, 2 juin 2026) a analysé 6 844 citations générées par trois modèles (GPT 5.4 Mini, Claude Haiku 4.5, Gemini 3.1 Flash) à partir de 750 requêtes couvrant des sujets disponibles en plusieurs langues (anglais, français, japonais, espagnol) :

- Les sources disponibles uniquement en anglais (ex. Britannica) perdent **55,3 %** de leur visibilité dans les citations quand la requête est posée en français (contre −23,4 % en espagnol et −80,6 % en japonais).
- Claude utilise ses connaissances internes sans citer de source externe dans **66,6 %** des réponses en français, contre **42,7 %** sur les mêmes sujets posés en anglais.
- Le taux d'utilisation de la version localisée de Wikipédia (fr.wikipedia.org pour une requête en français) varie fortement selon le modèle : GPT 5.4 Mini 24,4 %, Claude Haiku 4.5 8,4 %, Gemini 3.1 Flash 6,2 %.

Profound (mars 2026, 3,25 milliards de citations, 7 modèles, 14 pays dont la France) a confirmé l'effet de la langue sur la composition du graphe de citations : « la langue d'une requête peut reconfigurer l'ensemble des sources citées — quels domaines apparaissent, avec quelle fréquence ». Sur ChatGPT, les taux de citation de contenu social diminuent sur tous les marchés non anglophones étudiés.

---

## Pourquoi ces chiffres ne se corrigent pas d'eux-mêmes

La présence du français à 4,7 % dans Common Crawl est stable depuis plusieurs années — le web francophone ne croît pas assez vite pour combler l'écart avec l'anglais. Ce qui aggrave le problème côté formation des modèles, c'est que le post-entraînement (instruction tuning, préférence humaine) reproduit le même déséquilibre que le pré-entraînement : compar:IA, plateforme publique du gouvernement français lancée pour collecter des données de préférence en français, avait recueilli 600 000 prompts au 7 février 2026 (89,14 % en français, 8,55 % en anglais). En miroir, les grandes plateformes de feedback (Chatbot Arena, RLHF utilisé par OpenAI et Anthropic) sont dominées par des panelistes anglophones.

Le résultat opérationnel est une chaîne à trois étapes :

1. Moins de données d'entraînement en français → le modèle maîtrise moins bien la langue dans ses dimensions culturelles et locales.
2. Lors de la génération, le modèle préfère citer des sources en anglais (disponibles en plus grande quantité dans ses corpus) ou n'en cite aucune.
3. Les éditeurs francophones reçoivent moins de trafic issu des moteurs IA — sans que ce soit lié à la qualité de leur contenu.

Le benchmark SAGEO Arena (Yonsei University, arXiv:2602.12187) montre que les informations structurelles (balisage sémantique, titres Hn, schémas) améliorent de 22 % le taux de récupération dans les moteurs génératifs. Mais cette amélioration suppose que le document soit d'abord présent dans l'index vectoriel du modèle — une condition plus difficile à remplir quand la langue est sous-représentée à l'entraînement. SearchLLM (Xiaohongshu, KDD 2026, arXiv:2603.10473) établit par ailleurs que le grounding factuel est le premier verrou avant tout critère de qualité : un contenu non validé par le modèle comme factuel ne passe pas en citation, quelle que soit sa pertinence formelle. Ce filtre est plus discriminant pour les langues sous-représentées dans les données d'entraînement.

---

## Nos propres chiffres (données de première main)

Ce bloc est réservé. Le vault ne contient pas de mesure directe des taux de citation des domaines .fr par les moteurs IA anglophones, ni de données GSC segmentées par requêtes francophones vs anglophones sur les propriétés suivies. Le protocole pour remplir cette lacune figure dans [[preuves/SETUP-GSC]] : un export mensuel segmenté par langue de requête permettrait de mesurer l'évolution des impressions et du CTR depuis l'introduction des AI Overviews en France.

---

## Contre-analyse

**La qualité de génération en français a rattrapé l'anglais sur les benchmarks généraux.** CARTE (arXiv:2606.01995, juin 2026, 1 075 questions sur des connaissances ancrées en France), mesure Gemini 3 Flash à 92,4 % en français sur questions générales — un score comparable aux meilleures performances en anglais. La dégradation réelle n'apparaît que sur les connaissances intra-nationales (références régionales, variations linguistiques locales) et sur les benchmarks de compréhension nuancée (French MMLU : −16 à −33 % de précision vs MMLU anglais, llm-stats.com, 12 000 questions, 14 domaines).

**Les données de Llama 2 datent de 2023.** Depuis, les modèles ont significativement élargi leurs corpus multilingues : Llama 3.1 (juillet 2024), Mistral NeMo (juillet 2024), GPT-4o (mai 2024) ont tous communiqué sur leurs capacités multilingues renforcées, sans publier de tableau de distribution comparable à celui de Llama 2. La sous-représentation de 0,16 % est la dernière mesure publiée ; la réalité actuelle pourrait être sensiblement différente pour les modèles 2025-2026.

**Le biais de citation n'est pas que linguistique.** L'étude Weglot porte sur des sujets dont l'autorité de référence mondiale est en anglais (Britannica pour la culture générale anglophone). Sur des sujets à ancrage géographique français (gastronomie, droit français, littérature), les modèles pourraient inverser la tendance et privilégier les sources locales. Aucune étude publiée ne mesure cet effet différentiellement.

**Les AI Overviews ne sont pas encore en France.** En juin 2026, Google confirme leur déploiement imminent en France (Sébastien Missoffe, directeur général de Google France, 24 juin 2026), mais la contrainte légale des droits voisins — qui oblige à rémunérer les éditeurs — a différé le lancement. Sans AI Overviews généralisés, le principal vecteur d'exposition mesuré aux États-Unis (25,8 % des requêtes déclenchent un AI Overview) n'est pas encore actif sur le marché le plus directement concerné par ce biais.

---

## FAQ

**Le biais de 29x est-il permanent ?**  
Non. BLOOM a choisi 13 % de français en 2022. D'autres modèles pourraient faire ce choix. Mais tant que les grandes plateformes de RLHF restent majoritairement anglophones et que les corpus de post-entraînement reproduisent le biais du web, la correction ne se fait pas mécaniquement.

**Un site francophone doit-il écrire en anglais pour être cité ?**  
Pas nécessairement. Les requêtes en français privilegient les sources en français (Weglot montre que le modèle adapte sa sélection de sources à la langue de la requête). Le problème n'est pas la langue du contenu en elle-même, c'est l'étroitesse du corpus francophone de référence dans les modèles — qui réduit la base de sources disponibles pour la génération en français.

**Est-ce différent selon le moteur IA ?**  
Oui. Perplexity, qui crawle activement le web en temps réel, est moins dépendant des corpus d'entraînement statiques. ChatGPT, Gemini et Claude, dont les corpus de base sont constitués à l'entraînement, sont plus exposés à ce biais structurel. Profound (mars 2026) confirme que les modèles de Google montrent une bidirectionnalité selon la langue de la requête — soit parce que Google indexe activement les contenus locaux.

**Mistral est français — est-ce que ça change quelque chose ?**  
Mistral AI (fondé en 2023 à Paris) a publié Mistral NeMo et d'autres modèles avec une attention documentée à la qualité en français. Le benchmark CARTE place Mistral NeMo à 74,3 % sur la connaissance ancrée en France — correct, mais inférieur à Gemini 3 Flash (92,4 %). L'origine française de l'équipe fondatrice n'implique pas mécaniquement un corpus d'entraînement plus équilibré.

---

## [À SOURCER]

- Part exacte du français dans les corpus d'entraînement de Llama 3.1, GPT-4o, Gemini 1.5 Pro (2024-2025) : aucun des trois n'a publié de tableau de distribution comparable à celui de Llama 2.
- Taux de citations des domaines .fr par ChatGPT et Perplexity sur des requêtes posées en français : les études publiées (Profound, SE Ranking, Ahrefs) ne désagrègent pas par TLD francophone.
- Effet différentiel selon la catégorie thématique (culture française, droit, cuisine) : pas d'étude publiée sur ce découpage.
- Données de la plateforme compar:IA sur l'impact du français dans les benchmarks de préférence après intégration de ses 600 000 prompts dans les modèles partenaires.

---

## Sources

1. **Common Crawl Language Statistics** — Common Crawl Foundation — CC-MAIN-2026-25 — https://commoncrawl.github.io/cc-crawl-statistics/plots/languages — consulté le 2026-07-11
2. **Usage Statistics of Content Languages for Websites** — W3Techs — juillet 2026 — https://w3techs.com/technologies/overview/content_language — consulté le 2026-07-11
3. **Llama 2: Open Foundation and Fine-Tuned Chat Models** (tableau de distribution linguistique) — Hugo Touvron et al., Meta — arXiv:2307.09288 — juillet 2023 — https://arxiv.org/abs/2307.09288
4. **Language Ranker: A Metric for Quantifying LLM Performance Across High and Low-Resource Languages** (cite le tableau Llama 2) — arXiv:2404.11553 — avril 2024 — https://arxiv.org/html/2404.11553v3 — consulté le 2026-07-11
5. **BLOOM: A 176B-Parameter Open-Access Multilingual Language Model** — BigScience Workshop — arXiv:2211.05100 — novembre 2022 — https://arxiv.org/html/2211.05100 — consulté le 2026-07-11
6. **Do LLMs Prefer Wikipedia? We Analyzed 6,844 Citations Across Claude, Gemini, and GPT to Find Out** — Rayne Aguilar, Weglot — 2 juin 2026 — https://www.weglot.com/blog/wikipedia-llm-visibility — consulté le 2026-07-11
7. **How Query Language Reshapes AI Citations** — Profound — mars 2026 — https://www.tryprofound.com/blog/how-query-language-reshapes-ai-citations — consulté le 2026-07-11
8. **compar:IA: The French Government's LLM Arena to Collect French-Language Human Prompts and Preference Data** — arXiv:2602.06669 — février 2026 — https://arxiv.org/html/2602.06669 — consulté le 2026-07-11
9. **CARTE: A Benchmark for Mapping Language Model Knowledge Across France** — arXiv:2606.01995 — juin 2026 — https://arxiv.org/html/2606.01995v1 — consulté le 2026-07-11
