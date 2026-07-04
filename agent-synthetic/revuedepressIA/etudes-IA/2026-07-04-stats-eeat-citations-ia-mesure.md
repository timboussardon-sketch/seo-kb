---
type: query
skill: seo-page-statistiques
title: "E-E-A-T mesurable et citations IA : benchmarks 2025-2026"
aliases:
  - stats-eeat-citations
  - eeat-mesure-ia
  - autorité-citations-llm
tags:
  - eeat
  - citations-ia
  - geo
  - aeo
  - earned-media
  - autorité
  - entités
  - schema
  - statistics
created: 2026-07-04
updated: 2026-07-04
sources: 9
confidence: high
status: draft
---

# E-E-A-T mesurable et citations IA — 4 juillet 2026

84 % des citations produites par ChatGPT, Claude et Gemini proviennent de médias tiers — journaux, sites éditoriaux, sources académiques ou gouvernementales (Muck Rack, 25 millions de liens, mai 2026). Ce chiffre résiste depuis trois éditions consécutives de l'étude, avec une fourchette stable de 82 à 89 %. De l'autre côté : ajouter du balisage structuré à une page existante ne change rien aux citations — les résultats des AI Overviews baissent même légèrement de 4,6 % dans le test contrôlé d'Ahrefs (1 885 pages, mai 2026).

Le paradoxe est là. Les études de corrélation présentent les signaux d'expertise, d'autorité et de confiance comme des prédicteurs forts des citations IA. Les tests contrôlés montrent que les leviers concrets d'optimisation (balisage schéma, balise auteur) ne produisent pas l'effet attendu. Cette étude réconcilie les trois paradigmes de mesure qui coexistent dans la littérature 2025-2026 et identifie ce qui, dans les données, explique réellement la variance.

---

## Les chiffres clés (vérifiés à la source)

### Earned media : le signal structurant

Muck Rack a analysé 25 millions de liens extraits des réponses de ChatGPT, Claude et Gemini sur 17 secteurs (mai 2026, troisième édition depuis juillet 2025). Les médias acquis (médias tiers, journalisme, académique, gouvernement) représentent 84 % des citations. Le contenu payant ou publicitaire plafonne à 0,3 %. La ventilation par plateforme révèle des comportements distincts : ChatGPT cite dans 96 % de ses réponses (5 citations en moyenne), Gemini dans 82 % (8 citations en moyenne), Claude dans 55 % (13 citations en moyenne).

Une étude contrôlée de Stacker et Scrunch mesure l'effet causal de la distribution (mars 2026, 87 articles, 30 marques, 8 plateformes IA, 2 600 prompts). Un même contenu diffusé sur des sites tiers génère un lift médian de 239 % en citations IA. 64 % des citations totales viennent des versions publiées sur des éditeurs tiers, contre 36 % pour la version hébergée sur le site de la marque. Dans 17,5 % des réponses, les IA citent exclusivement la version tierce — elles ignorent l'original.

L'étude préliminaire de décembre 2025 (8 articles, 5 plateformes, 944 combinaisons requête-plateforme) donnait un chiffre plus haut : taux de citation passant de 7,6 % (site propre uniquement) à environ 34 % après distribution, soit 325 % de hausse. L'écart avec les 239 % du mars 2026 s'explique par la taille de l'échantillon : 8 histoires contre 87, et 8 plateformes contre 5.

BuzzStream a analysé 4 millions de citations extraites de 3 600 prompts sur 10 secteurs (semaine du 27 janvier 2026, ChatGPT, Google AI Mode, AI Overviews, Gemini). Les articles de blog et de contenu éditorial représentent plus de 50 % des citations. Les publications d'information pèsent 14,09 %. Les communiqués de presse via les fils de syndication atteignent 0,04 % du total.

### Balisage structuré : corrélation sans causalité

Ahrefs a suivi 1 885 pages ayant ajouté un balisage JSON-LD entre août 2025 et mars 2026, comparées à 4 000 pages témoins, avec une fenêtre de mesure de 30 jours avant et après (mai 2026). Les résultats sur les AI Overviews : −4,6 % de citations (statistiquement significatif, odds d'observer cet écart par chance = 1/2 500). Sur AI Mode et ChatGPT : +2,4 % et +2,2 %, indiscernables du bruit. L'étude note par ailleurs que les pages déjà citées par l'IA sont trois fois plus susceptibles d'avoir du JSON-LD — corrélation documentée, mais non causale.

Digital Applied a analysé 1 000 AI Overviews sur 4 243 URLs citées et environ 50 000 URLs non citées (avril 2026, 100 requêtes × 10 classes d'intention, États-Unis, desktop). Le balisage structuré Article + BreadcrumbList est associé à un lift de 2,3 × dans la probabilité de citation ; HowTo atteint 2,8 ×. Mais cette étude est observationnelle : les pages citées avaient déjà ce balisage avant d'être citées. Ce n'est pas un test avant-après.

### Citations de sources nommées dans le corps du texte

Dans la même étude Digital Applied, les pages qui citent des sources nommées dans leur corps de texte ont une probabilité de citation 2,1 × plus élevée. Ce signal est cohérent avec la méthodologie GEO originale (Princeton, KDD 2024, détaillée dans la section suivante). L'autorité de domaine (DA) corrèle à +0,61 dans cet échantillon de pages citées. Ce coefficient est élevé, mais il souffre d'un biais de sélection : la population analysée est composée exclusivement de pages déjà citées, ce qui restreint artificiellement la variance et gonfle la corrélation.

Pour l'ensemble des marques (75 000 marques, Ahrefs), les mentions de marque sur des sites tiers corrèlent à 0,664 avec la visibilité dans les AI Overviews, contre 0,218 pour les backlinks — un rapport de 1 à 3. Ce chiffre est cohérent avec la logique earned media : l'autorité est d'abord mesurée par la présence dans des sources indépendantes, pas par la structure du site propre.

---

## Pourquoi ces chiffres divergent : trois paradigmes de mesure

La littérature 2025-2026 sur l'E-E-A-T et les citations IA repose sur trois paradigmes qui mesurent des objets différents, mais sont souvent présentés comme interchangeables.

**Premier paradigme : les études de corrélation sur des pages déjà citées.** Elles comparent les caractéristiques des pages qui apparaissent dans les réponses IA à celles qui n'y apparaissent pas. Elles produisent des ratios ou des coefficients de corrélation élevés : autorité de domaine, balisage structuré, densité d'entités. Le problème est structurel : l'échantillon de référence est déjà filtré. Les pages citées par l'IA tendent à provenir de domaines établis avec des pratiques éditoriales robustes — elles ont souvent le balisage, l'auteur nommé et la source citée parce qu'elles sont des publications professionnelles, pas parce que ces éléments les ont fait citer. Appliquer ces corrélations comme prescriptions revient à conseiller à un inconnu de porter un costume parce que les PDG portent des costumes.

**Deuxième paradigme : les études de lift par distribution.** Elles mesurent ce qui se passe quand le même contenu change de canal. La même étude, publiée sur le site de la marque puis syndiquée sur des éditeurs tiers : citation rate 7,6 % contre 34 %. Ce paradigme est le plus proche d'un vrai test causal. Il montre que le levier de la distribution (earned media) est dominant, indépendamment de l'optimisation on-page.

**Troisième paradigme : les tests contrôlés d'un seul levier.** Ahrefs ajoute du schéma et mesure l'effet : −4,6 % sur les AI Overviews. C'est le paradigme le plus rigoureux méthodologiquement, mais il isole un seul signal technique à la fois. Il ne peut pas capturer l'effet d'un signal composite comme "autorité éditoriale globale".

La réconciliation est la suivante :

| Paradigme | Exemple 2025-2026 | Ce qu'il mesure réellement |
|---|---|---|
| Corrélation sur pages citées | Digital Applied (1 000 AIO, DA +0,61) | Profil des domaines qui ont déjà une autorité accumulée |
| Lift de distribution | Stacker (87 articles, +239 %) | Effet du canal de publication sur l'accessibilité aux LLM |
| A/B test causal | Ahrefs (1 885 pages, schéma −4,6 %) | Effet marginal d'un levier technique isolé |

Ces trois objets ne se superposent pas. L'E-E-A-T au sens des Quality Rater Guidelines est un jugement humain sur la qualité d'une page dans un contexte d'intention. Les études citées ne le mesurent pas directement : elles mesurent des proxies d'autorité qui co-varient avec lui mais ne le causent pas mécaniquement.

---

## Données de première main (analyses indexées dans la base de connaissance)

Deux études académiques analysées dans la base de connaissance apportent des données expérimentales directement pertinentes. Elles sont anonymisées conformément à la politique de la base.

**GEO paper — Princeton / IIT Delhi, KDD 2024 (arXiv:2311.09735).** Premier benchmark formel du GEO, 10 000 requêtes issues de 9 jeux de données, évalué sur Perplexity.ai en production. Neuf méthodes d'optimisation ont été testées. Les deux stratégies les plus efficaces sont "Cite Sources" (+30 à 40 % de visibilité pondérée) et "Statistics Addition" (+30 à 40 %), mesurées par Position-Adjusted Word Count. Le "Keyword Stuffing" est nul. L'"Authoritative tone" est modéré et n'est efficace que sur les requêtes de type débat ou histoire. La combinaison Fluency + Statistics produit +5,5 % de plus que la meilleure stratégie isolée. Résultat clé : les deux leviers d'optimisation que ce benchmark valide causalement (citer des sources nommées, ajouter des données chiffrées dans le corps du texte) sont précisément les pratiques associées à l'E-E-A-T dans les Quality Rater Guidelines — mais l'effet passe par le contenu du texte lui-même, pas par les balises techniques ou les métadonnées auteur.

**SAGEO Arena — Yonsei University / Konkuk University, 2025 (arXiv:2602.12187).** Premier benchmark GEO qui évalue les trois étapes du pipeline (retrieval → reranking → génération), sur un corpus de 170 000 documents web avec informations structurelles complètes. Les éléments structurels (title, méta-description, headings, schéma) optimisés produisent +22 % de Hit Rate et +2,72 ΔRank au retrieval. La stratégie "Statistics" appliquée aux éléments structurels atteint +35 % de Hit Rate. En revanche, optimiser uniquement le corps du texte dégrade le retrieval de 4,54 points de Hit Rate en moyenne — les réécritures introduisent des synonymes rares qui réduisent le recouvrement lexical avec les requêtes BM25.

Ces deux études expérimentales convergent sur un point que les études de corrélation ne peuvent pas établir : les signaux d'autorité mesurables dans les citations IA ne passent pas par les métadonnées seules. L'effet se produit quand le contenu du document lui-même porte des données vérifiables et des références explicites à des sources nommées.

---

## Contre-analyse

**L'E-E-A-T n'est pas une variable indépendante mesurable.** Les Quality Rater Guidelines de Google définissent l'E-E-A-T comme un jugement contextuel porté sur une page en réponse à une intention spécifique. Il n'existe pas de score E-E-A-T standardisé ni d'API qui l'expose. Les études qui lui attribuent un coefficient de corrélation avec les citations IA — comme le coefficient de 0,81 cité par Wellows (15 847 AI Overviews, 63 secteurs) — opèrent en réalité sur un proxy composite construit par l'analyste. Ce proxy amalgame des signaux hétérogènes : présence de l'auteur, balisage structuré, ancienneté du domaine, mentions tierces. L'E-E-A-T devient un label rétroactif posé sur ce que les IA ont déjà appris à favoriser au cours de leur entraînement.

**Wellows : conflit d'intérêts.** L'étude Wellows sur les facteurs de classement des AI Overviews (r = 0,81 pour les "signaux E-E-A-T") est produite par un prestataire de services d'optimisation GEO. L'échantillon de 15 847 AI Overviews est large, mais la méthodologie de construction du score E-E-A-T composite n'est pas publiée. Ce chiffre doit être traité avec précaution : il incite à acheter des services d'optimisation E-E-A-T.

**L'effet earned media n'est pas purement un signal de qualité.** Les 84 % de citations depuis les médias tiers (Muck Rack) s'expliquent aussi par la structure des données d'entraînement des LLM : les corpus Common Crawl et C4 sur lesquels la plupart des LLM sont pré-entraînés surreprésentent les publications éditoriales établies. Le lift de distribution Stacker (+239 %) peut en partie refléter que les LLM "reconnaissent" les éditeurs tiers parce qu'ils ont vu leurs articles pendant l'entraînement — pas uniquement parce que le contenu est de meilleure qualité.

**Les tests A/B de schéma ne testent qu'un levier à la fois.** Le résultat Ahrefs (−4,6 % AI Overviews) concerne l'ajout de schéma sur des pages qui n'en avaient pas, pendant 30 jours. Il ne dit rien sur l'effet à long terme, ni sur l'effet d'une mise en place de schéma dès la création du contenu, ni sur des types de schéma spécifiques (HowTo vs Article vs Person). La corrélation de 2,3 × (Digital Applied) reste la mesure sur le parc existant. Les deux chiffres ne sont pas contradictoires : ils mesurent des moments différents dans le cycle de vie d'une page.

**Le biais de sélection de secteur.** L'étude BuzzStream porte sur une semaine de janvier 2026. L'étude GEO-16 couvre uniquement les requêtes B2B SaaS. La Stacker couvre principalement l'immobilier et la santé, où les médias tiers sont particulièrement actifs. Les études Muck Rack couvrent 17 secteurs mais ne distinguent pas les proportions earned media par secteur. Extrapoler ces chiffres à un secteur industriel de niche, où les médias tiers sont peu nombreux, est risqué.

---

## FAQ

**Faut-il un auteur nommé pour être cité par les IA ?**
Aucune étude avec une méthodologie contrôlée et publiée ne valide un effet causal d'un byline sur le taux de citation IA. La corrélation existe (les pages citées ont davantage d'auteurs nommés), mais elle est confondue avec l'autorité du domaine. Le signal expérimentalement validé le plus proche est "citer des sources nommées dans le corps du texte" (+2,1 × Digital Applied, +30 à 40 % GEO paper) — différent de "avoir un auteur nommé dans la balise auteur".

**Le balisage schéma Person ou Article aide-t-il ?**
D'après le test contrôlé d'Ahrefs (1 885 pages, 2026), ajouter du schéma après publication n'améliore pas les citations. Fabrice Canel (Microsoft Bing) a déclaré à SMX Munich 2025 que le schéma aide les LLM à comprendre le contenu — mais comprendre n'est pas équivalent à citer.

**Une fiche Wikidata garantit-elle des citations IA ?**
Wikidata est présenté dans plusieurs publications comme un accélérateur de Knowledge Panel et de citations IA. Aucune étude primaire accessible n'a encore mesuré causalement l'effet de la création d'une entrée Wikidata sur le taux de citation IA avec un groupe témoin valide. C'est une hypothèse plausible mais non établie quantitativement.

**Pourquoi les communiqués de presse ne sont-ils pas cités ?**
0,04 % des citations dans le dataset BuzzStream (4 millions de citations, janvier 2026). La raison structurelle est double : les LLM sont entraînés sur des corpus qui favorisent le contenu éditorial original ; et les fils de syndication produisent des duplications textuelles détectables, ce que les mécanismes de déduplication des LLM tendent à filtrer.

**L'E-E-A-T "fort" des pages citées par les IA veut-il dire qu'on peut l'optimiser ?**
Le chiffre de 96 % de pages citées avec des "signaux E-E-A-T forts" (Wellows) est une corrélation sur une population sélectionnée. Il indique que les domaines qui publient régulièrement des contenus de qualité éditoriale se retrouvent dans les réponses IA. Cela ne signifie pas qu'ajouter rétrospectivement des signaux E-E-A-T à une page existante produira l'effet correspondant.

---

## [À SOURCER]

Les chiffres suivants n'ont pas pu être vérifiés à la source primaire au moment de la rédaction :

- **Impact d'une fiche Wikidata sur les citations IA** : plusieurs publications avancent un multiplicateur de 2,7 × à 2,8 × pour la probabilité d'apparaître dans les AI Overviews lorsqu'une entité dispose d'un identifiant Wikidata vérifié. Aucune étude primaire avec groupe témoin n'a pu être localisée.
- **Effet byline sur le taux de citation** : amicited.com cite un ratio de 1,9 × (auteur nommé vs contenu anonyme) et 2,3 × (avec accréditations professionnelles). Aucune méthodologie, taille d'échantillon ni test statistique n'est communiqué.
- **E-E-A-T r = 0,81** (Wellows, 15 847 AI Overviews) : le coefficient est élevé et la méthodologie de construction du score composite E-E-A-T n'est pas publiée de façon vérifiable. Traiter comme indicatif uniquement.
- **15+ entités connectées = 4,8 × plus de probabilité de citation** (Wellows, même source) : même réserve méthodologique.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté |
|---|---|---|---|---|
| Generative Pulse : Earned Media Consistently Drives AI Citations, Holding at 84% | Muck Rack | Mai 2026 | https://muckrack.com/blog/what-is-ai-reading-may-2026 | 2026-07-04 |
| New Stacker Research: Earned Media Distribution Triples AI Search Visibility, Delivers 239% Median Lift in Brand Citations | Stacker / GlobeNewswire | Mars 2026 | https://www.globenewswire.com/news-release/2026/03/16/3256365/0/en/new-stacker-research-earned-media-distribution-triples-ai-search-visibility-delivers-239-median-lift-in-brand-citations.html | 2026-07-04 |
| How Earned Media Distribution Expands AI Visibility: A First Look at "Citation Lift" | Stacker | Décembre 2025 | https://stacker.com/blog/how-earned-media-distribution-expands-ai-visibility-first-look-at-citation-lift | 2026-07-04 |
| We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved. | Ahrefs | Mai 2026 | https://ahrefs.com/blog/schema-ai-citations/ | 2026-07-04 |
| What Actually Gets You Cited in AI Search (2026 Data) — 1,000 AI Overviews Analyzed | Digital Applied | Avril 2026 | https://www.digitalapplied.com/blog/we-analyzed-1000-ai-overviews-citation-pattern-study | 2026-07-04 |
| The Role of News Publications in AI Citations | BuzzStream | Janvier 2026 | https://www.buzzstream.com/blog/news-publications-ai-citations/ | 2026-07-04 |
| AI Answer Engine Citation Behavior: Bringing the GEO-16 Framework in B2B SaaS (arXiv:2509.10762) | Kumar et al. / arXiv | Septembre 2025 | https://arxiv.org/html/2509.10762v1 | 2026-07-04 |
| GEO: Generative Engine Optimization (arXiv:2311.09735) | Aggarwal et al. — Princeton / IIT Delhi | KDD 2024 | https://arxiv.org/abs/2311.09735 | (indexé dans la base de connaissance) |
| SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization (arXiv:2602.12187) | Kim et al. — Yonsei / Konkuk | Preprint 2025 | https://arxiv.org/abs/2602.12187 | (indexé dans la base de connaissance) |
