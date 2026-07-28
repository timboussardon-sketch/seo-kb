---
type: query
skill: seo-page-statistiques
status: draft
title: "Wikipedia dans les citations IA 2025-2026 : premier domaine cité ou sur-cité ?"
tags: [wikipedia, citations-ia, memorisation, rag, perplexity, chatgpt, google-aio, donnees-entrainement, llm]
created: 2026-07-28
updated: 2026-07-28
sources: 12
confidence: medium
---

# Wikipedia dans les citations IA 2025-2026 : premier domaine cité ou sur-cité ?

**7,8 % de toutes les citations de ChatGPT pointent vers Wikipedia.** Contre 0,6 % pour Google AI Overviews. Et selon les sources et les métriques, ce chiffre varie d'un facteur 33 selon la plateforme et la méthode de mesure. Ce n'est pas une contradiction : c'est l'histoire d'un même site web dont le destin diverge radicalement selon l'architecture du moteur qui le cite.

## Les chiffres clés (vérifiés à la source)

### Wikipedia au runtime : part dans les citations

| Source de mesure | Plateforme | Métrique | Wikipedia | Champ / Période |
|---|---|---|---|---|
| Ahrefs Brand Radar | ChatGPT | Mention share | **16,3 %** | 957K prompts, juin 2025 |
| Ahrefs Brand Radar | Perplexity | Mention share | **12,5 %** | 953,5K prompts, juin 2025 |
| Ahrefs Brand Radar | Google AI Overviews | Mention share | **8,4 %** | 76,7M AIO, juin 2025 |
| Profound | ChatGPT | Volume total citations | **7,8 %** | 680M citations, août 2024 – juin 2025 |
| Profound | Google AI Overviews | Volume total citations | **0,6 %** | 680M citations, même période |
| Profound | Perplexity | Top 10 des domaines | Absent | 680M citations, même période |
| Semrush | Tous moteurs | % réponses contenant au moins une citation | **26,3 %** | 150K+ citations, juin 2025 |
| Everything-PR / 5WPR | Tous moteurs | Rang global | **#2** derrière Reddit | 680M+ citations, août 2024 – avril 2026 |

Wikipedia est premier domaine cité sur ChatGPT (Profound, 7,8 %) et sur les trois moteurs simultanément (Ahrefs, mention share). Britannica, son concurrent encyclopédique le plus proche, pointe à la **49e place** dans le classement consolidé Everything-PR.

### Wikipedia dans les données d'entraînement

| Corpus / Modèle | Part Wikipedia (brut) | Facteur d'upsampling | Exposition effective |
|---|---|---|---|
| The Pile — EleutherAI (2021) | 1,53 % | ×3 | ~4,6 % du corpus d'entraînement |
| LLaMA 1 — Touvron et al. (2023) | **4,5 %** des tokens | ×1 (non précisé) | 4,5 % |
| GPT-3 — Brown et al. (2020) | ~3 % (3 milliards de tokens) | ×1 (dans un total pondéré) | 3 % |
| Llama 2 — Touvron et al. (2023) | Non divulgué | — | — |
| GPT-4 | Non divulgué | — | — |

The Pile attribue à Wikipedia le **facteur d'upsampling le plus élevé** de ses 22 composants. Les concepteurs ont décidé de faire lire le corpus Wikipedia trois fois au modèle là où la plupart des autres sources ne sont vues qu'une fois. Le signal : à volume égal, Wikipedia est jugé plus utile que Common Crawl pour la qualité factuelle.

### Impact sur le trafic Wikipedia

- Wikimedia Foundation (oct. 2025) : **−8 % de pages vues humaines** par rapport aux mêmes mois de 2024, attribué aux moteurs génératifs qui répondent directement sans rediriger vers la source
- DataReportal : trafic de recherche organique vers Wikipedia passé de 5,8 milliards de visites (jan. 2022) à 4,3 milliards (mars 2025), soit **−26 % en trois ans**
- Trafic bot sur Wikipedia : **88 milliards de pages vues** générées par des robots en 2025, contre un trafic humain en recul
- English Wikipedia : **7,2 millions d'articles** (juillet 2026), soit 5,2 milliards de mots

## Pourquoi ces chiffres divergent-ils d'un facteur 33 ?

La dispersion apparente (0,6 % vs 26,3 %) masque trois objets de mesure distincts que les études confondent.

**Objet 1 — Mention share (Ahrefs)** : quelle proportion des requêtes a produit une réponse qui cite Wikipedia au moins une fois ? Une réponse peut citer dix sources : si Wikipedia en fait partie, la réponse est comptée. Résultat : 16,3 % des prompts ChatGPT.

**Objet 2 — Volume de citation (Profound)** : Wikipedia représente-t-il 7,8 % de l'ensemble des liens de citation émis par ChatGPT, toutes réponses confondues ? Si une réponse cite dix sources, chacune pèse 1/10. Résultat : 7,8 %.

**Objet 3 — Présence dans un corpus de réponses analysées (Semrush)** : Wikipedia apparaît-il dans la réponse, que ce soit en citation explicite ou en reformulation ? Plus permissif. Résultat : 26,3 %.

**Réconciliation des deux chiffres ChatGPT (16,3 % vs 7,8 %)** : si l'on suppose que 16,3 % des réponses ChatGPT citent Wikipedia exactement une fois, et que ces réponses génèrent en moyenne 2,1 citations au total, alors Wikipedia représente 16,3 / (16,3 × 2,1) × 100 = 7,8 % de l'ensemble des citations. Les deux chiffres sont cohérents et impliquent que ChatGPT **cite Wikipedia seul** dans la majorité des réponses où il le cite, contre une moyenne de deux autres sources dans les réponses sans Wikipedia. Ce n'est pas de la fréquence, c'est de la concentration.

## Le multiplicateur entraînement → runtime

En croisant la part de Wikipedia dans les données d'entraînement avec sa part dans les citations à l'exécution, un écart systématique apparaît :

| Moteur | Part d'entraînement (estimée) | Part runtime (citation volume) | Multiplicateur |
|---|---|---|---|
| ChatGPT (GPT-3 baseline) | ~3 % | 7,8 % (Profound) | ×2,6 |
| Moteurs sur corpus LLaMA-type | ~4,5 % | 12,5 % (Ahrefs, Perplexity mention share) | ×2,8 |
| Google AI Overviews | Non divulgué | 0,6 % (Profound) | [À SOURCER] |

Wikipedia est cité à **2,6 à 2,8 fois** sa proportion dans les données d'entraînement. Deux interprétations, non exclusives : (1) la mémoire paramétrique (ce que le modèle a appris) et la récupération en temps réel (RAG) s'additionnent sur Wikipedia, au lieu de se substituer ; (2) les requêtes factuelles, sur-représentées dans les études de citation, déclenchent systématiquement Wikipedia quelle que soit la plateforme.

Ce multiplicateur ne peut pas être décomposé proprement avec les données disponibles. Il n'existe pas, à ce jour, de protocole public qui isole la part de mémorisation de la part de récupération pour un domaine donné, sur un moteur commercial.

## Données de première main

Aucune mesure propriétaire isolée sur Wikipedia n'a été effectuée dans le portefeuille client de ce vault. Les analyses maison portent sur le trafic GSC entrant, pas sur les citations sortantes des moteurs.

Le vault contient en revanche des données sur la corrélation entre présence encyclopédique et citations IA : les sources [[wiki/sources/2026-03-06-algorithme-etude-citation-ia]] et [[wiki/sources/2026-04-13-geo-aggarwal-2024]] documentent que les pages éditorialement proches du format Wikipedia (claim + source nommée + structure H2) obtiennent un lift de citation. Sans aller jusqu'à mesurer wikipedia.org spécifiquement, cela conforte le mécanisme.

## Contre-analyse

**1. Le biais de requête invisibilise l'écart réel.** Toutes les études de citation utilisent des requêtes factuelles ou informationnelles pour constituer leur échantillon. Les requêtes commerciales, locales et transactionnelles, qui constituent la majorité du trafic de recherche, déclenchent beaucoup moins Wikipedia. Le 7,8 % de Profound sur un corpus de 680 millions de citations n'est pas représentatif du trafic global ; il reflète un mix de requêtes orienté connaissance.

**2. L'architecture du moteur prime sur la qualité du contenu.** Google AI Overviews cite Wikipedia à 0,6 % en volume, contre 7,8 % pour ChatGPT — non parce que Wikipedia est moins pertinent pour Google, mais parce que Google favorise ses propres propriétés (YouTube, Reddit en réponse UGC, ses propres pages Knowledge) et gère différemment la récupération encyclopédique. L'écart de ×13 entre les deux plateformes pour le même domaine illustre que la citation IA est une décision d'architecture autant qu'une décision de pertinence.

**3. La mémorisation vs récupération reste inséparable.** Les moteurs comme ChatGPT Search utilisent les deux mécanismes simultanément. Quand une réponse cite wikipedia.org, impossible de savoir si le modèle a récupéré cette page en temps réel (RAG) ou si le lien vient d'un template mémorisé pendant l'entraînement. Des travaux académiques sur la contamination RAG (RePCS, arXiv 2506.15513, juin 2025) commencent à diagnostiquer ce problème, mais pas encore à l'échelle des moteurs commerciaux.

**4. Britannica à la 49e place ne signifie pas que la qualité encyclopédique est récompensée.** Britannica a la même rigueur éditoriale que Wikipedia, souvent supérieure. Son score plus bas tient à son accès partiel (paywall) et à sa faible représentation dans les corpus d'entraînement ouverts, pas à sa qualité. La citation IA récompense l'accessibilité et la masse textuelle, pas la fiabilité intrinsèque.

**5. La baisse du trafic humain n'est pas un zéro-sum.** Les −26 % de trafic de recherche vers Wikipedia depuis 2022 et les 88 milliards de vues bot en 2025 ne signifient pas que l'audience de Wikipedia s'est évaporée. Ils signifient que le passage par Wikipedia est de plus en plus médiatisé par les moteurs IA, non que l'information cesse d'être consultée. La Wikimedia Foundation note que ChatGPT est devenu le premier référent de trafic entrant pour Wikipedia en juin 2025 — une inversion complète du rôle habituel.

## FAQ

**Wikipedia est-il intentionnellement favorisé par les moteurs IA ?**
Pas selon les documents publics disponibles. Sa sur-représentation dans les citations découle de sa présence massive dans les données d'entraînement (The Pile ×3, LLaMA 1 à 4,5 %), de son accessibilité totale aux crawlers et de son format structuré (titres H2, définitions en tête de section) qui facilite l'extraction sémantique.

**Mettre à jour une page Wikipedia améliore-t-il les citations IA ?**
La corrélation est documentée (50 % des marques les plus citées ont une page Wikipedia, selon une étude de 58 questions sur 4 LLMs). La causalité n'est pas prouvée : les marques suffisamment notables pour avoir une Wikipedia bien entretenue ont généralement aussi plus de mentions sur d'autres domaines à haute autorité.

**Wikidata et DBpedia sont-ils cités ?**
Wikidata alimente les graphes de connaissance de Google (Knowledge Panels, entités Gemini) mais n'apparaît pas comme domaine de citation direct dans les études disponibles. DBpedia n'apparaît dans aucun classement consulté.

**Wikipedia verra-t-il ses citations reculer ?**
La baisse de 0,6 % pour Google AI Overviews (vs 7,8 % ChatGPT) suggère que les moteurs à récupération large diversifient leurs sources. Si les moteurs génératifs évoluent vers plus de RAG et moins de mémoire paramétrique, l'avantage concurrentiel de Wikipedia (sa sur-représentation dans l'entraînement) diminue — et il n'a pas de meilleure protection que son accessibilité ouverte.

## [À SOURCER]

- **Part de Wikipedia dans les données d'entraînement de Llama 2** : Meta n'a pas divulgué la composition précise du corpus. Marqué [À SOURCER], aucun chiffre avancé.
- **Part de Wikipedia dans les données d'entraînement de GPT-4** : OpenAI n'a divulgué aucune donnée de composition. Marqué [À SOURCER].
- **Taux de citation Wikipedia sur Claude (Anthropic)** : les études disponibles ne publient pas ce chiffre individuellement pour Claude. Une étude Profound de 14 pays et 7 modèles mentionne Claude mais sans détail Wikipedia.
- **Citations Wikidata et DBpedia dans les moteurs IA** : aucune étude primaire trouvée avec des chiffres quantifiés.
- **Multiplicateur entraînement → runtime pour Google AI Overviews** : la composition des données d'entraînement de Gemini n'est pas publique.

## Sources

| Intitulé | Organisme | Date | URL | Consulté le |
|---|---|---|---|---|
| Top 10 Most Cited Domains by AI Assistants | Ahrefs | Juin 2025 | https://ahrefs.com/blog/top-10-most-cited-domains-ai-assistants | 2026-07-28 |
| AI Platform Citation Patterns | Profound | Août 2024 – juin 2025 | https://www.tryprofound.com/blog/ai-platform-citation-patterns | 2026-07-28 |
| ChatGPT's New Gatekeepers (State of AI Citations 2026) | 5W Public Relations via PRNewswire | Avril 2026 | https://www.prnewswire.com/news-releases/chatgpts-new-gatekeepers-wikipedia-reddit-and-the-sites-now-shaping-what-america-buys-302778843.html | 2026-07-28 |
| AI Platform Citation Source Index 2026 | Everything-PR | Avril 2026 | https://everything-pr.com/ai-platform-citation-source-index-2026 | 2026-07-28 |
| Ranked: The Most Cited Websites by AI Models | Visual Capitalist (données Semrush) | Juin 2025 | https://www.visualcapitalist.com/ranked-the-most-cited-websites-by-ai-models/ | 2026-07-28 |
| The Pile: An 800GB Dataset of Diverse Text for Language Modeling | EleutherAI — Gao et al. | Janvier 2021 | https://ar5iv.labs.arxiv.org/html/2101.00027 | 2026-07-28 |
| LLaMA: Open and Efficient Foundation Language Models | Meta AI — Touvron et al. | Février 2023 | https://arxiv.org/abs/2302.13971 | 2026-07-28 |
| Language Models are Few-Shot Learners (GPT-3) | OpenAI — Brown et al. | 2020 | https://arxiv.org/abs/2005.14165 | 2026-07-28 |
| New User Trends on Wikipedia | Wikimedia Foundation | Octobre 2025 | https://wikimediafoundation.org/news/2025/10/17/new-user-trends-on-wikipedia/ | 2026-07-28 |
| AI and LLMs Have Changed Wikipedia's Importance Forever | Jake Orlowitz / WikiBlueprint via Medium | Mai 2026 | https://medium.com/wikiblueprint/ai-and-llms-have-changed-wikipedias-importance-forever-8ef85d847bf0 | 2026-07-28 |
| Wikipedia:Size of Wikipedia | English Wikipedia | Juillet 2026 | https://en.wikipedia.org/wiki/Wikipedia:Size_of_Wikipedia | 2026-07-28 |
| What We Know About the Impact of Wikipedia on ChatGPT Search Results | ALLMO.ai | 2025 | https://allmo.ai/articles/what-we-know-about-the-impact-of-wikipedia-on-chatgpt-search-results | 2026-07-28 |
