---
type: query
skill: seo-page-statistiques
status: draft
title: "Autorité et liens entrants des pages citées par les IA : profil off-page des sources préférées 2025-2026"
aliases: ["off-page citations IA", "autorité domaine citations IA", "backlinks pages citées IA", "referring domains IA citations"]
tags: [geo, aeo, citations-ia, backlinks, domain-authority, referring-domains, tld, chatgpt, perplexity, ai-overviews, ai-mode, seo-offpage]
created: 2026-07-07
updated: 2026-07-07
sources: 6
confidence: medium
---

# Autorité et liens entrants des pages citées par les IA : profil off-page des sources préférées 2025-2026

Un portefeuille de 129 000 domaines montre que ChatGPT accorde aux liens entrants un poids 2,2 fois plus élevé qu'AI Mode de Google. Les mentions de marque sur YouTube prédisent la visibilité dans les réponses IA mieux que les backlinks, sur toutes les plateformes. Ces deux faits remettent en cause l'idée que l'autorité off-page agit de manière uniforme sur l'ensemble des moteurs génératifs.

---

## Les chiffres clés (vérifiés à la source)

| Indicateur | Valeur | Plateforme | Source |
|---|---|---|---|
| Coefficient SHAP des domaines référents | 1,21 | ChatGPT Search | SE Ranking, 129 000 domaines |
| Coefficient SHAP des domaines référents | 0,56 | Google AI Mode | SE Ranking, 2,3 M pages |
| Citations moyennes : ≤2 500 domaines référents | 1,6 à 1,8 | ChatGPT Search | SE Ranking |
| Citations moyennes : seuil 32 000 domaines référents | 2,9 → 5,6 (doublement) | ChatGPT Search | SE Ranking |
| Citations moyennes : ≥350 000 domaines référents | 8,4 | ChatGPT Search | SE Ranking |
| Citations moyennes : <300 domaines référents | 2,5 | Google AI Mode | SE Ranking |
| Citations moyennes : ≥24 000 domaines référents | 6,8 | Google AI Mode | SE Ranking |
| Corrélation mentions YouTube / visibilité IA | 0,737 (ChatGPT), 0,740 (AI Mode), 0,712 (AIO) | 3 plateformes | Ahrefs, 75 000 marques |
| Corrélation mentions de marque sur sites tiers / visibilité | 0,664 (ChatGPT), 0,709 (AI Mode), 0,656 (AIO) | 3 plateformes | Ahrefs, 75 000 marques |
| Corrélation Domain Rating / visibilité IA | 0,266 (ChatGPT), 0,285 (AI Mode), 0,326 (AIO) | 3 plateformes | Ahrefs, 75 000 marques |
| Corrélation nombre de backlinks / visibilité AIO | 0,218 | AI Overviews | Ahrefs, 75 000 marques |
| Corrélation nombre de domaines référents / visibilité AIO | 0,295 | AI Overviews | Ahrefs, 75 000 marques |
| Corrélation autorité de domaine (DA) / taux de citation | +0,61 (Pearson, niveau page) | AI Overviews | Digital Applied, 4 243 pages |
| Part des pages citées en AIO classées dans le top 10 organique | 38 % | AI Overviews | Ahrefs, 4 M URLs |
| Part des pages citées en AIO hors top 100 organique | 31 % | AI Overviews | Ahrefs |
| TLD des citations ChatGPT : .com | 80,41 % | ChatGPT | Profound, 680 M citations |
| TLD des citations ChatGPT : .org | 11,29 % | ChatGPT | Profound, 680 M citations |
| TLD des citations ChatGPT : .uk / .io / .ai / .net | 2,16 / 1,67 / 1,13 / 1,01 % | ChatGPT | Profound |
| Citations moyennes si .gov ou .edu | 3,2 | ChatGPT | SE Ranking (vs 4,0 pour .com) |
| Marques du 4e quartile de mentions | 169 mentions IA (médiane) | AI Overviews | Ahrefs |
| Marques avec zéro mention dans les réponses IA | 26 % | AI Overviews | Ahrefs, 75 000 marques |

---

## Comment les plateformes pondèrent les liens entrants différemment

SE Ranking a mesuré l'importance de chaque facteur via une analyse SHAP (méthode de jeu coopératif qui isole la contribution marginale de chaque variable dans un modèle XGBoost). Le chiffre clé : le nombre de domaines référents obtient un coefficient SHAP de 1,21 pour ChatGPT Search et de 0,56 pour AI Mode de Google, soit un écart de 2,2×.

La raison tient à l'architecture des deux systèmes. ChatGPT Search fonctionne en mode RAG (génération augmentée par récupération) : le modèle requête directement le web et utilise les liens entrants comme proxy de crédibilité, de la même façon qu'un moteur de recherche traditionnel. AI Mode de Google s'appuie sur l'index web de Google, où la qualité de la page a déjà été filtrée en amont ; les liens entrants ont donc moins à prouver.

Pour AI Mode, c'est le trafic du domaine qui est premier (SHAP 0,63 contre 0,62 pour ChatGPT), un signal synthétique qui agrège popularité et fraîcheur sans dépendre directement du profil de liens.

---

## Les seuils de domaines référents : effets de pallier plutôt que linéarité

L'effet n'est pas linéaire. Pour ChatGPT Search, SE Ranking identifie deux points d'inflexion :

- **0-2 500 domaines référents** : 1,6 à 1,8 citations moyennes par requête. La présence dans les réponses de ChatGPT est marginale.
- **Seuil de 32 000 domaines référents** : citations qui passent de 2,9 à 5,6, soit un quasi-doublement. Franchir ce seuil représente donc le changement d'état le plus observable.
- **350 000+ domaines référents** : 8,4 citations. Ce profil correspond aux grands médias, aux plateformes de référence et aux sites institutionnels.

Pour AI Mode, les seuils sont différents et moins contrastés : les domaines avec moins de 300 domaines référents obtiennent 2,5 citations, ceux avec plus de 24 000 en obtiennent 6,8. L'effet de seuil existe, mais la pente est moins raide.

La confiance du domaine (Domain Trust, une métrique combinant quantité et qualité des liens) renforce cet effet : en dessous de 43, ChatGPT accorde 1,6 citation en moyenne ; au-delà de 90, les domaines haute confiance atteignent près de 8,4 citations. Le seuil de 77 est le premier pallier où les bénéfices deviennent perceptibles.

---

## YouTube et mentions de marque : les signaux off-page qui dominent

L'étude Ahrefs sur 75 000 marques (décembre 2025, Spearman) reclasse les signaux off-page dans un ordre inattendu pour les praticiens SEO :

- **Mentions YouTube** : corrélation 0,737 (ChatGPT), 0,740 (AI Mode), 0,712 (AI Overviews). Le signal le plus fort, toutes plateformes confondues.
- **Mentions de marque sur sites tiers** : corrélation 0,664 à 0,709 selon la plateforme.
- **Domain Rating (DR)** : corrélation 0,266 à 0,326. Signal modéré, présent mais relégué en cinquième position.
- **Nombre de backlinks** : corrélation 0,218 en AI Overviews.

L'écart entre YouTube (0,737) et les backlinks (0,218) est de 3,4×. Autrement dit, une marque qui multiplie ses présences éditoriales — mentions de journalistes, vidéos d'analyse, couvertures de communautés — génère un signal de confiance bien plus prédictif qu'une campagne de netlinking classique, pour ce qui est des citations IA.

La dispersion par quartile illustre l'effet de concentration : les marques du dernier quartile (les plus mentionnées) obtiennent 169 mentions médianes en AI Overviews, contre 14 pour le 3e quartile, 3 pour le 2e, et 0 pour le 1er. 26 % des 75 000 marques étudiées sont totalement absentes des réponses IA de Google.

---

## Distribution des TLD : le .com reste dominant, mais le .edu ne surperforme pas

Sur l'ensemble des 680 millions de citations tracées par Profound entre août 2024 et juin 2025, le .com représente 80,41 % des citations de ChatGPT. Le .org arrive en 2e position avec 11,29 %. Les TLD technologiques récents (.io à 1,67 %, .ai à 1,13 %) sont présents mais marginaux en volume.

Un détail contre-intuitif : les domaines .gov et .edu obtiennent en moyenne 3,2 citations dans ChatGPT contre 4,0 pour les domaines commerciaux (SE Ranking). La confiance institutionnelle associée à ces extensions ne se traduit pas par une surcitation dans les résultats. L'explication probable : ChatGPT favorise les sources à forte présence en ligne et trafic élevé, critères sur lesquels les sites institutionnels sont structurellement désavantagés face aux grands médias commerciaux.

Seule la distribution TLD de ChatGPT est disponible à la source ; les comparaisons par TLD pour Perplexity et AI Mode n'ont pas été trouvées dans les études primaires consultées (voir [À SOURCER]).

---

## Pourquoi ces chiffres se contredisent : trois cadres de mesure pour un même signal

La littérature produit trois valeurs très différentes pour « l'effet de l'autorité de domaine sur les citations IA » :

- **r = 0,61** (Digital Applied, avril 2026, Pearson, niveau page, 4 243 URLs citées vs ~50 000 contrôles) — corrélation forte
- **r = 0,326** (Ahrefs, mai 2025, Spearman, niveau marque, 75 000 marques, DR de la marque vs mentions totales en AIO) — corrélation modérée
- **r = 0,18** (Wellows/Clairon, 2026, attribué à « AI Mode Boost 2025 ») — corrélation faible (méthodologie non détaillée, voir [À SOURCER])

Ces trois chiffres ne mesurent pas le même objet.

Digital Applied mesure la corrélation entre le DA d'une page spécifique et la probabilité que cette page figure dans un AI Overview. C'est le signal de sélection au niveau de l'URL individuelle : l'autorité de la page détermine si elle entre ou non dans le bassin des sources citables.

Ahrefs mesure la corrélation entre le Domain Rating global d'une marque et la fréquence à laquelle cette marque est citée dans les réponses IA. L'unité d'analyse est la marque, et le DR est la métrique du domaine principal, pas de la page citée. À ce niveau, des signaux de notoriété plus larges (mentions, YouTube) absorbent une grande partie de la variance.

SE Ranking (SHAP) mesure l'importance relative du nombre de domaines référents pour prédire le volume de citations, parmi les pages déjà dans la course. Ses thresholds décrivent un effet de seuil, pas une corrélation linéaire.

La synthèse : l'autorité de domaine agit comme filtre d'entrée (effet fort au niveau page, r=0,61), mais comme prédicteur de volume, elle est supplantée par les signaux de notoriété de marque (YouTube, mentions). Avoir des liens suffit pour être citable ; avoir des mentions partout détermine combien de fois on l'est.

---

## Nos propres chiffres (données de première main)

Deux éléments du vault éclairent le mécanisme.

L'étude CORE (arXiv:2602.03608, UIUC/HKUST, 2025), ingérée dans ce vault [[raw/etudes-seo/etude-core-ranking-2025]], montre que dans les moteurs génératifs, le LLM reproduit quasi systématiquement l'ordre du retrieval initial (PSR baseline = 0 % sans manipulation). Le contenu textuel peut renverser cet ordre, mais le retrieval en est le point de départ. Ce mécanisme explique pourquoi les liens entrants conservent un rôle : ils alimentent le ranking organique, qui devient l'ordre d'entrée dans le retrieval. L'étude SAGEO Arena [[raw/etudes-seo/etude-sageo-arena-2025]] confirme que le retrieval BM25 est la première brique, optimisable via les champs structurels — l'autorité de domaine agit en amont de cette brique via le ranking organique.

Par ailleurs, les données CTR mesurées sur un portefeuille de 23 propriétés francophones [[raw/etudes-seo/etude-ctr-ai-overviews-gsc]] montrent une concentration brutale sur la position 1 (34,2 % de CTR vs 5,6 % en position 2, soit une chute de 84 %). Cette dynamique de concentration dans les résultats organiques se retrouve dans les citations IA : 38 % des pages citées en AI Overviews sont classées dans le top 10, et le top quartile des marques Ahrefs capture 169 mentions médianes contre 0 pour le quartile inférieur. La concentration n'est pas propre à un canal, elle traverse les deux systèmes.

---

## Contre-analyse

Quatre limites structurelles à garder en tête avant d'utiliser ces données.

**Biais de sélection dans les études SE Ranking.** Les seuils de domaines référents (32 000 pour ChatGPT, 24 000 pour AI Mode) sont construits sur des domaines actifs dans 20 niches thématiques sélectionnées. Les secteurs peu représentés dans les jeux de données (institutionnel, local, éditions de niche) peuvent se comporter différemment. Les effets de seuil mesurés sont des médianes par segment, pas des lois causales universelles.

**Causalité inversée sur le DR.** La corrélation r=0,61 de Digital Applied (DA vs taux de citation) pourrait refléter que les sites bien liés publient davantage de contenu structuré, actualisé et sourcé — et que c'est ce contenu qui est cité, pas l'autorité elle-même. L'étude est transversale, pas un A/B test causal. L'étude Ahrefs sur les pages ajoutant du schema markup (1 885 pages, différence-en-différences, vérifiée dans l'étude précédente de ce vault) illustre exactement ce piège : corrélation forte en transversal, effet causal nul ou négatif en longitudinal.

**Hétérogénéité des définitions d'autorité.** Moz DA, Ahrefs DR et Semrush Authority Score ne sont pas interchangeables. Digital Applied utilise « un proxy d'autorité tiré d'un dataset de liens tiers » sans préciser la source. Comparer une corrélation Pearson avec Moz DA à une corrélation Spearman avec Ahrefs DR revient à comparer deux instruments différents sur deux échantillons différents.

**Architecture divergente des plateformes.** ChatGPT Search, AI Mode, Perplexity et Claude ont des pipelines de récupération distincts (web crawl, index Google, Bing, corpus d'entraînement). Les SHAP values de SE Ranking sont des points de mesure sur un instant T, sur une architecture T, avec les versions de modèles disponibles en novembre 2025 (ChatGPT) et en 2026 (AI Mode). Les évolutions de modèles modifient le poids relatif de ces signaux sans préavis.

---

## FAQ

**Les backlinks restent-ils utiles pour les citations IA en 2026 ?**
Oui, mais leur rôle est indirect. Ils alimentent le ranking organique, qui détermine l'ordre d'entrée dans le retrieval des moteurs génératifs. Les études Ahrefs montrent que 38 % des pages citées en AI Overviews figurent dans le top 10 organique, et SAGEO Arena confirme que le retrieval initial est quasi déterminant pour la sélection finale. Mais le nombre de domaines référents n'est plus le premier signal : les mentions YouTube (corrélation 0,737) et les mentions sur sites tiers (0,664) le surpassent largement.

**ChatGPT et AI Mode de Google valorisent-ils les liens de la même façon ?**
Non. Le SHAP des domaines référents est de 1,21 pour ChatGPT Search et de 0,56 pour AI Mode, soit un écart de 2,2×. ChatGPT Search, qui opère comme un moteur RAG sur le web ouvert, utilise les liens comme proxy direct de crédibilité. AI Mode s'appuie sur l'index de Google, où la qualité a déjà été filtrée, et privilégie le trafic du domaine (SHAP 0,63) plutôt que les liens bruts.

**Quel est le seuil minimum de domaines référents pour apparaître régulièrement dans ChatGPT ?**
SE Ranking identifie un doublement des citations autour de 32 000 domaines référents (de 2,9 à 5,6 citations moyennes). En dessous de 2 500 domaines référents, les citations restent marginales (1,6 à 1,8). Ce seuil est propre au corpus testé et ne constitue pas une règle universelle.

**Les extensions .edu et .gov sont-elles avantagées dans les citations IA ?**
Non, selon les mesures SE Ranking : les domaines .gov et .edu obtiennent 3,2 citations en moyenne contre 4,0 pour les domaines commerciaux (.com) dans ChatGPT. Le prestige institutionnel ne compense pas leur moindre présence en termes de trafic et de mentions.

**Un petit site peut-il obtenir des citations IA sans profil de liens fort ?**
L'étude Ahrefs montre que 31 % des pages citées en AI Overviews ne figurent pas dans le top 100 organique, ce qui indique une ouverture à des sources sans fort historique SEO. Mais 26 % des 75 000 marques étudiées ont zéro mention en AI Overviews, et la concentration est très forte dans le quartile supérieur. La stratégie la plus efficace reste de construire des mentions de marque sur des sites tiers crédibles plutôt que de se concentrer exclusivement sur les backlinks.

---

## [À SOURCER]

- **TLD de Perplexity et AI Mode** : des sources secondaires mentionnent que Perplexity aurait la plus forte part de .edu (3,2 %) et de ccTLD (4,4 %) parmi les moteurs IA, mais aucune étude primaire fetchée ne fournit le tableau par plateforme. La donnée Profound (680 M citations) ne couvre que ChatGPT pour le TLD.
- **DA r=0,18** (Wellows/Clairon, avril 2026) : l'article Clairon attribue ce chiffre à « AI Mode Boost 2025 » sans lien vers l'étude originale ni précision sur la méthodologie, le corpus ou les plateformes couvertes. La valeur r=0,18 est cohérente avec Ahrefs (DR r=0,266-0,326), mais le sourçage n'est pas vérifiable depuis une source primaire.
- **« 47 % des citations AIO viennent de pages classées hors top 5 »** : cité dans le résumé de l'article Wellows, attribué à « AI Mode Boost 2025 ». Chiffre non trouvé dans les études primaires fetchées (Ahrefs mesure 38 % dans le top 10 et 31 % hors top 100, ce qui est cohérent mais pas identique).
- **Perplexity faveur des sites haute autorité (+40 % par rapport aux blogs intermédiaires)** : affirmé dans un agrégat de plusieurs études, sans isolation d'une source primaire vérifiable. À confirmer depuis une étude Profound, SE Ranking ou LLM Pulse avec corpus Perplexity dédié.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté |
|---|---|---|---|---|
| How to Optimize for ChatGPT: 20 ranking factors from 129,000 domains | SE Ranking | 2025-11-24 | https://seranking.com/blog/how-to-optimize-for-chatgpt/ | 2026-07-07 |
| How to Optimize for AI Mode: Google Visibility Matters 3× More Than Content | SE Ranking | 2026 | https://seranking.com/blog/how-to-optimize-for-ai-mode/ | 2026-07-07 |
| Top Brand Visibility Factors in ChatGPT, AI Mode, and AI Overviews (75k Brands Studied) | Ahrefs | 2025-12-12 | https://ahrefs.com/blog/ai-brand-visibility-correlations/ | 2026-07-07 |
| An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied) | Ahrefs | 2025-05-26 | https://ahrefs.com/blog/ai-overview-brand-correlation/ | 2026-07-07 |
| Update: 38% of AI Overview Citations Pull From The Top 10 | Ahrefs | 2026 | https://ahrefs.com/blog/ai-overview-citations-top-10/ | 2026-07-07 |
| 1,000 AI Overviews Analyzed: Citation Pattern Study | Digital Applied | 2026-04 | https://www.digitalapplied.com/blog/we-analyzed-1000-ai-overviews-citation-pattern-study | 2026-07-07 |
| AI Platform Citation Patterns: How ChatGPT, Google AI Overviews, and Perplexity Source Information | Profound | 2025 | https://www.tryprofound.com/blog/ai-platform-citation-patterns | 2026-07-07 |
| CORE: Controlling Output Rankings in Generative Engines | UIUC/HKUST/Intel Labs (Jin et al.) | 2025-02 | https://arxiv.org/abs/2602.03608 | (vault: raw/etudes-seo/etude-core-ranking-2025.md) |
