---
type: query
skill: seo-page-statistiques
status: draft
title: "Profil technique des pages citées par les IA : longueur, structure et balisage 2025-2026"
aliases: ["profil technique citations IA", "pages citées IA statistiques", "longueur contenu cité IA"]
tags: [geo, aeo, citations-ia, schema-markup, word-count, page-speed, ai-overviews, chatgpt, perplexity, seo-technique]
created: 2026-06-30
updated: 2026-06-30
sources: 6
confidence: medium
---

# Profil technique des pages citées par les IA : longueur, structure et balisage 2025-2026

53,4 % des pages citées dans les AI Overviews de Google font moins de 1 000 mots. Pendant ce temps, SE Ranking mesure que les articles dépassant 2 900 mots reçoivent 59 % de citations ChatGPT en plus que les textes courts. Ces deux chiffres sont corrects. Ils ne mesurent pas la même chose.

---

## Les chiffres clés (vérifiés à la source)

| Indicateur | Valeur | Plateforme | Source |
|---|---|---|---|
| Longueur moyenne des pages citées | 1 282 mots | AI Overviews (Google) | Ahrefs, 174 048 pages |
| Pages citées de moins de 1 000 mots | 53,4 % | AI Overviews (Google) | Ahrefs, 560 346 AIO |
| Corrélation longueur/fréquence de citation | 0,04 (quasi nulle) | AI Overviews (Google) | Ahrefs, Spearman |
| Surcitation pour articles >2 900 mots | +59 % | ChatGPT Search | SE Ranking, 129 000 domaines |
| Surcitation pour sections de 120-180 mots | +70 % | ChatGPT Search | SE Ranking, 216 524 pages |
| Citation depuis le premier tiers du contenu | 44,2 % | ChatGPT | Kevin Indig, 1,2 M réponses |
| Impact de l'ajout de schéma JSON-LD sur les citations | −4,6 % (AIO) / +2,2 % (ChatGPT) | AIO + ChatGPT | Ahrefs, 1 885 pages traitées |
| Corrélation autorité de domaine/taux de citation | +0,61 | AI Overviews | Digital Applied, 4 243 pages |
| Gain de vitesse FCP <0,4 s vs >1,13 s | 3× plus de citations | ChatGPT Search | SE Ranking, 129 000 domaines |
| Surcitation si source nommée dans le corps du texte | +2,1× | AI Overviews | Digital Applied |
| Gain "Statistics Addition" sur visibilité dans les GE | +34 % | Perplexity (production) | GEO-Bench, 10 000 requêtes |
| Optimisation structurelle (titre, meta, headings, schema) | +22 % Hit Rate retrieval | Pipeline BM25+LLM | SAGEO Arena, 170 000 docs |

---

## Ce que la longueur explique (et ce qu'elle n'explique pas)

Ahrefs a analysé 174 048 pages effectivement citées dans 560 346 AI Overviews, représentant 1 677 876 URLs. Le coefficient de Spearman entre nombre de mots et fréquence de citation est de 0,04. Ce chiffre signifie qu'à partir du moment où une page est déjà dans le bassin des candidats cités, sa longueur ne prédit pas combien de fois elle apparaîtra. Une page de 300 mots et une page de 3 000 mots ont statistiquement les mêmes chances d'être sélectionnées par Gemini dans un AI Overview.

La répartition confirme : 16,6 % des pages citées font moins de 350 mots, 36,8 % entre 350 et 1 000 mots, 30,6 % entre 1 000 et 2 000 mots, et 16 % dépassent 2 000 mots. Les pages courtes (moins de 350 mots) représentent 34 % des citations en position 1, légèrement au-dessus de leur poids relatif.

La longueur médiane varie fortement par type de contenu : 315 mots pour les pages de listing, 317 mots pour les pages "core", 387 mots pour les contenus générés par des tiers, et 1 166 mots pour les articles.

SE Ranking aboutit à une conclusion apparemment opposée : les articles dépassant 2 900 mots obtiennent en moyenne 5,1 citations ChatGPT, contre 3,2 pour les textes inférieurs à 800 mots. L'étude couvre 129 000 domaines sur 216 524 pages réparties en 20 niches, via une régression XGBoost avec analyse SHAP. Elle a été publiée en novembre 2025.

---

## La structure prime sur la longueur brute

Kevin Indig a analysé plus de 1,2 million de réponses ChatGPT pour cartographier l'origine exacte des passages cités (publication du 18 février 2026, 18 012 citations vérifiées). Résultat : 44,2 % des citations proviennent du premier tiers du contenu, 31,1 % du tiers médian, et 24,7 % du dernier tiers. La position dans la page compte plus que la longueur totale.

L'étude identifie cinq traits communs aux pages les plus citées : un langage définitif (des réponses directes sans conditionnels), une structure conversationnelle en questions/réponses avec des sous-titres clairs, une densité d'entités nommées de 20,6 % en moyenne (noms propres, organisations, dates), un niveau de subjectivité équilibré (0,47 sur l'échelle TextBlob), et une lisibilité correspondant au niveau lycée/terminale (grade 16 environ, contre 19,1 pour les pages peu citées).

La décomposition par niveau de paragraphe montre que 53 % des citations proviennent du milieu du paragraphe, 24,5 % des phrases d'ouverture, et 22,5 % des phrases de clôture.

SAGEO Arena (Yonsei University/Konkuk University, arXiv:2602.12187, février 2025) confirme et enrichit ce tableau à l'aide d'un corpus de 170 000 documents web. Le benchmark mesure chaque étape du pipeline séparément : retrieval BM25, reranking cross-encoder, génération LLM. L'optimisation des champs structurels (titre, meta description, headings H1-H3, schema.org) améliore le taux de retrieval de 22 % en moyenne. L'ajout de statistiques dans ces champs structurels pousse ce gain à 35 %. En revanche, optimiser uniquement le body text dégrade le retrieval de 4,54 % : les expansions de texte remplacent des mots courants par des synonymes rares, ce qui diminue le chevauchement lexical avec les requêtes BM25. Les réécritures longues (type AutoGEO) dégradent le retrieval de 22,35 %.

La granularité de la section compte pour ChatGPT Search : SE Ranking mesure que les pages structurées en blocs de 120 à 180 mots entre deux sous-titres obtiennent en moyenne 4,6 citations, contre 2,7 pour les pages dont les sections font moins de 50 mots, soit 70 % d'écart.

---

## L'autorité de domaine et le trafic : signaux dominants

Digital Applied a analysé 1 000 AI Overviews (4 243 pages citées, environ 50 000 pages de contrôle, avril 2026). L'autorité de domaine présente une corrélation de +0,61 avec le taux de citation — le signal le plus fort de l'étude. La présence d'une source nommée dans le corps du texte multiplie par 2,1 la probabilité de citation. La page médiane citée a 14 mois.

SE Ranking mesure un effet de seuil du trafic pour ChatGPT : à partir de 190 000 visiteurs mensuels, la corrélation avec le nombre de citations devient significative. Les domaines avec plus de 350 000 domaines référents obtiennent 8,4 citations en moyenne, contre 1,6 à 1,8 pour ceux avec 2 500 domaines référents. La vitesse de chargement s'avère un signal fort : un First Contentful Paint inférieur à 0,4 seconde correspond à 6,7 citations moyennes, contre 2,1 pour un FCP supérieur à 1,13 seconde, soit un facteur 3.

GEO-Bench (Princeton/IIT Delhi, arXiv:2311.09735, KDD 2024, 10 000 requêtes sur 25 domaines) mesure les stratégies qui augmentent la visibilité dans les moteurs génératifs. L'ajout de statistiques chiffrées améliore la visibilité de 34 % en moyenne, le sourçage d'affirmations par des citations de +41 %, et l'ajout de citations d'autorité de +30 %. Le keyword stuffing produit un gain de 0 % et tend à dégrader la visibilité. Les sites les moins bien classés initialement bénéficient le plus du GEO : pour un site en position 5, l'ajout de citations source génère +115 % de visibilité.

---

## Pourquoi ces chiffres se contredisent : trois études, trois objets différents

La contradiction apparente entre Ahrefs (longueur sans effet), SE Ranking (+59 % pour 2 900+ mots) et SAGEO Arena (long rewrites = dégradation) s'explique par trois objets de mesure distincts.

Ahrefs mesure une corrélation au sein du panier de pages déjà indexées et déjà citables par Gemini. À ce stade, la sélection par longueur a déjà eu lieu en amont : Google a filtré le contenu selon d'autres critères avant de le mettre à disposition du modèle de génération. La longueur n'explique plus rien parce qu'elle a déjà agi, ou pas.

SE Ranking mesure ChatGPT Search (mode RAG avec recherche web), un pipeline différent. Dans ce cas, les pages longues présentent plus de signaux d'autorité (plus de backlinks, plus d'ancienneté, plus de couverture thématique), et le modèle de régression XGBoost les isole comme un proxy de confiance. La longueur y est corrélée avec l'autorité, pas avec la qualité intrinsèque du contenu.

SAGEO Arena mesure le retrieval BM25, première brique du pipeline dans les systèmes de recherche augmentée. À ce stade, l'expansion du body text dilue la densité de mots-clés et nuit à la correspondance lexicale avec la requête. La longueur des champs structurels (titre court, meta description de 155 caractères) reste dense ; la longueur du corps de texte devient un handicap pour le retrieval si elle se substitue à la précision.

La synthèse : la longueur optimale dépend de la plateforme visée et de l'étape du pipeline ciblée. Pour les AI Overviews (sélection Gemini sur contenu déjà indexé), la longueur est secondaire. Pour ChatGPT Search (RAG sur index web), les longs articles d'autorité ont un avantage. Pour le retrieval BM25 en amont, les champs structurels courts et denses gagnent.

Le même raisonnement s'applique au schéma markup. L'étude Ahrefs (1 885 pages ayant ajouté du JSON-LD, 4 000 contrôles, différence-en-différences sur 7 mois) mesure l'effet causal de l'ajout de schema sur des pages déjà citées : résultat nul ou légèrement négatif pour les AI Overviews (−4,6 %). L'étude Digital Applied (corrélation entre présence de schema et taux de citation) trouve un facteur 2,3× — mais cet écart reflète probablement le fait que les sites haute autorité ont à la fois plus de schema ET plus de citations. La méthode Ahrefs est mieux armée pour isoler la causalité.

---

## Nos propres chiffres (données de première main)

Deux études du vault apportent des points de référence complémentaires.

SAGEO Arena, ingéré et annoté dans ce vault [[raw/etudes-seo/etude-sageo-arena-2025]], montre que le placement de la réponse directe dans les premiers paragraphes améliore le reranking, et que sa position plus tardive le dégrade — même à contenu identique. Ce résultat valide empiriquement le principe "answer-first" que la doctrine propriétaire applique systématiquement depuis mi-2025.

La courbe CTR réelle mesurée sur un portefeuille de 23 propriétés francophones (9 798 requêtes, 1,76 million d'impressions, mars-mai 2026, données GSC non brandées, multi-secteurs) [[raw/etudes-seo/etude-ctr-ai-overviews-gsc]] montre un CTR en position 1 de 34,2 %, contre 5,6 % en position 2, soit une chute de 84 % entre les deux premières positions. Ce profil, plus abrupt que les benchmarks publics (First Page Sage : 39,8 %, Advanced Web Ranking : 30-35 % selon la niche), suggère que sur ce portefeuille, les AI Overviews concentrent l'attention sur le premier résultat organique visible. La comparaison directe avec les taux de citation IA n'est pas disponible (GSC ne distingue pas les requêtes avec et sans AI Overview), mais l'effet de concentration reste cohérent avec les études de citation qui montrent que la position organique reste prédictive.

---

## Contre-analyse

Quatre limites méthodologiques méritent d'être formulées avant d'utiliser ces données.

Les études SE Ranking (nov. 2025) et Ahrefs portent sur des plateformes différentes (ChatGPT Search vs. AI Overviews) mesurées à des moments différents. Les interpréter comme contradictoires revient à comparer deux systèmes distincts. Les études comparant plusieurs plateformes sur les mêmes pages au même moment sont encore rares.

L'étude Digital Applied (0,61 de corrélation entre DA et citations) est de nature transversale sur 1 000 AI Overviews. L'étude Clairon, non récupérée ici mais référencée dans plusieurs analyses 2026, irait dans le sens inverse ("l'autorité de domaine prédit moins de 4 % des citations IA"). Cette divergence peut refléter des définitions différentes de "DA" (Moz vs. Ahrefs vs. SEMrush) et des corpus différents. Aucune des deux études ne mesure la même chose au sens strict.

L'étude Ahrefs sur le schema est limitée à des pages qui recevaient déjà plus de 100 citations en AI Overviews en février 2025 : elle ne s'applique pas aux pages non citées qui cherchent à entrer dans le bassin. L'effet du schema pour faire passer une page de "non citée" à "citée" reste non mesuré.

GEO-Bench date de 2024 et a été mesuré sur BingChat et Perplexity dans leurs versions de l'époque. Les architectures ont évolué (Perplexity Sonar Pro, GPT-4o Search). Les gains de +34 % à +41 % doivent être vérifiés sur les versions 2025-2026 des systèmes.

---

## FAQ

**Un contenu de 500 mots peut-il être cité dans les AI Overviews ?**
Oui. 53,4 % des pages citées dans les AI Overviews font moins de 1 000 mots (Ahrefs, 174 048 pages). La longueur n'est pas un filtre de sélection pour cette plateforme.

**Faut-il ajouter du schéma JSON-LD pour être cité par les IA ?**
L'ajout de schema sur des pages déjà citées n'améliore pas les citations et peut les réduire légèrement sur les AI Overviews (−4,6 % selon Ahrefs, 1 885 pages, différence-en-différences). La corrélation observée entre schema et citations reflète l'autorité de domaine sous-jacente, pas un effet causal du schema.

**Quelle longueur de section viser pour ChatGPT Search ?**
Les sections de 120 à 180 mots entre deux sous-titres obtiennent en moyenne 70 % de citations en plus que les sections de moins de 50 mots (SE Ranking, 129 000 domaines). Ce n'est pas une règle universelle : cela s'applique spécifiquement à ChatGPT Search en mode RAG.

**La vitesse de chargement influence-t-elle les citations IA ?**
Pour ChatGPT Search, oui. Un First Contentful Paint inférieur à 0,4 seconde correspond à 3 fois plus de citations qu'un FCP supérieur à 1,13 seconde (SE Ranking, 2025). Pour les AI Overviews, cette relation n'a pas été mesurée de façon aussi directe dans les études disponibles.

**Une page peu connue peut-elle obtenir des citations IA ?**
Oui, mais avec un effet de seuil. GEO-Bench montre que les sites en position 5 bénéficient d'un gain de +115 % avec les stratégies GEO (ajout de citations sourcées, statistiques). Les sites déjà en position 1 progressent moins car ils partent d'une base haute. Les plateformes de citation ne sont pas toutes aussi concentrées sur les grandes marques : Perplexity est plus ouverte aux nouveaux domaines que ChatGPT selon les mesures d'âge de domaine (42,3 % de sources >15 ans pour Perplexity vs. 31,2 % pour Copilot).

---

## [À SOURCER]

- **FAQ schema 3.2× lift pour les AI Overviews** : cité par Frase.io qui l'attribue à "Search Engine Land", sans lien direct ni méthodologie divulguée. Chiffre non vérifiable depuis une source primaire avec l'accès disponible.
- **Statut HTTP 96,45 % de codes 200** pour les pages citées en AI Overviews : chiffre apparu dans des résumés de recherche, non retrouvé dans les études primaires fetchées. Peut provenir de Digital Applied ou d'une étude secondaire.
- **Profondeur de lien interne des pages citées** : aucune étude vérifiable trouvée. Donnée absente de toutes les sources primaires consultées.
- **Données HTTPS spécifiques** (taux de pages HTTPS vs HTTP citées) : non trouvées dans les études primaires. La prévalence générale de HTTPS (>98 % du web indexé par Google) rend ce signal peu discriminant, mais l'absence de mesure directe sur les citations IA est à noter.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté |
|---|---|---|---|---|
| Short vs. Long Content in AI Overviews: The Data Says Both Work | Ahrefs | 2026 | https://ahrefs.com/blog/short-vs-long-content-in-ai-overviews/ | 2026-06-30 |
| We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved. | Ahrefs | 2026 | https://ahrefs.com/blog/schema-ai-citations/ | 2026-06-30 |
| ChatGPT citations come from the first third of content: Study (Kevin Indig) | Search Engine Land | 2026-02-18 | https://searchengineland.com/chatgpt-citations-content-study-469483 | 2026-06-30 |
| How to Optimize for ChatGPT (129,000 domains study) | SE Ranking | 2025-11-24 | https://seranking.com/blog/how-to-optimize-for-chatgpt/ | 2026-06-30 |
| 1,000 AI Overviews Analyzed: Citation Pattern Study | Digital Applied | 2026-04 | https://www.digitalapplied.com/blog/we-analyzed-1000-ai-overviews-citation-pattern-study | 2026-06-30 |
| SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization | Yonsei University / Konkuk University | 2025-02 | https://arxiv.org/abs/2602.12187 | (vault: raw/etudes-seo/etude-sageo-arena-2025.md) |
| GEO: Generative Engine Optimization (GEO-Bench, 10 000 requêtes) | Princeton University / IIT Delhi (KDD '24) | 2024-08 | https://arxiv.org/abs/2311.09735 | (vault: raw/etudes-seo/etude-geo-aggarwal-2024.md) |
