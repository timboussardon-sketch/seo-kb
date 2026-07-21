---
type: query
skill: seo-page-statistiques
title: "Schema.org et citations IA (2025-2026) : le paradoxe corrélation-causalité mesuré sur six études"
tags: [schema, structured-data, citations-ia, geo, aio, chatgpt, perplexity, ahrefs, digital-applied, airops]
created: 2026-07-21
updated: 2026-07-21
sources: 7
confidence: medium
status: draft
---

# Schema.org et citations IA (2025-2026) : le paradoxe corrélation-causalité mesuré sur six études

Les pages qui portent du balisage Article + BreadcrumbList sont 2,3 fois plus souvent citées par les AI Overviews que les pages sans balisage. Mais ajouter ce balisage sur une page déjà citée produit un recul de 4,6 %. Ces deux chiffres, tirés de deux études publiées le même mois d'avril 2026, ne se contredisent pas : ils mesurent des objets différents. Comprendre pourquoi est le seul moyen d'utiliser le balisage structuré à bon escient en 2026.

---

## Les chiffres clés (vérifiés à la source)

### Présence du balisage parmi les pages citées

L'étude AirOps Fan-Out Effect d'avril 2026 (16 851 requêtes, 353 799 pages analysées, 50 553 réponses ChatGPT) mesure les taux de citation par type de balisage sur ChatGPT. Les pages avec du JSON-LD atteignent 38,5 % de taux de citation contre 32,0 % pour les pages sans, soit un écart de 6,5 points. Par type de balisage :

| Type de balisage | Taux de citation (ChatGPT) |
|---|---|
| MedicalWebPage | 47,0 % |
| BreadcrumbList | 46,2 % |
| FAQPage | 45,6 % |
| Organization | 44,3 % |
| WebSite | 40,6 % |
| Moyenne sans JSON-LD | 32,0 % |

Ces valeurs sont observationnelles : elles décrivent les pages citées, non l'effet d'un ajout de balisage.

### Corrélation schema-citation dans les AI Overviews

Digital Applied (avril 2026, 1 000 AI Overviews analysées, 4 243 pages citées, ~50 000 pages contrôles) :
- Pages avec balisage Article + BreadcrumbList : **2,3 fois plus citées** que les équivalents non balisés.
- Pages avec balisage HowTo : **2,8 fois plus citées** sur les requêtes procédurales.
- Corrélation autorité de domaine : +0,61 (Pearson), le signal le plus fort individuellement.

Audit de 5 000 sites par Digital Applied (avril 2026, 8 CMS, 30 jours de mesure cross-plateforme) :
- 71 % des sites déploient au moins un type de balisage ; 22 % passent la validation Rich Results sans erreur.
- Corrélation balisage valide / taux de citation IA : **+0,34** (Pearson, toutes plateformes).
- Écarts observés par combinaison de balisage : Article + BreadcrumbList +47 %, Product + Offer +29 %, Organization + WebSite +18 %.

### L'effet causal mesuré par Ahrefs

Ahrefs (mai 2026, Louise Linehan et Xibeijia Guan) a suivi 1 885 pages qui ont ajouté du JSON-LD entre août 2025 et mars 2026, en les comparant à 4 000 pages contrôles par différence-en-différences (DiD) et trois tests statistiques supplémentaires. Toutes les pages de l'échantillon avaient plus de 100 citations en AI Overviews avant l'ajout de balisage. Résultats :

| Plateforme | Effet mesuré | Interprétation |
|---|---|---|
| Google AI Overviews | −4,6 % | Significatif (1 chance sur 2 500 d'être dû au hasard) |
| Google AI Mode | +2,4 % | Bruit statistique |
| ChatGPT | +2,2 % | Bruit statistique |

Tous les types de balisage ont été regroupés sans ventilation par type.

### Balisage générique vs balisage attribut-complet

Kurt Fischman (SSRN, 20 février 2026) a analysé 1 006 pages classées sur 75 requêtes et les 730 citations générées par ChatGPT et Gemini sur ces mêmes requêtes. Résultat principal :
- Balisage générique (Article, Organization, BreadcrumbList) : **aucun effet mesurable**.
- Balisage Product et Review avec attributs complets (prix, notes, spécifications renseignés) : **61,7 % de taux de citation contre 41,6 %** pour les pages à balisage générique.
- Chaque position SERP perdue réduit les chances de citation IA de 24 %.

### Déploiement sitewide : cas OtterlyAI

OtterlyAI a présenté à BrightonSEO (avril 2026) les résultats d'un déploiement de balisage sur plus de 2 000 de ses propres pages. Sur une période de trois mois :
- Google AI Overviews : +1 500 %
- Google AI Mode : +377 %
- ChatGPT, Gemini, Copilot : recul des citations
- Perplexity : aucun effet

Ce résultat n'est pas contrôlé : d'autres modifications techniques ont pu accompagner le déploiement. Les chiffres ne sont pas attribuables au seul balisage. [Source primaire non accessible par fetch — données issues de la synthèse Analyzify, qui cite le blog OtterlyAI]

---

## Pourquoi ces chiffres divergent : la transformation originale

Six jeux de données, des effets allant de +1 500 % à −4,6 %. Ces chiffres ne se contredisent pas. Ils mesurent chacun un objet différent.

### Tableau réconcilié : schema × moteur × niveau de preuve

| Étude | Scope | Plateforme | Effet mesuré | Objet réel | Niveau de preuve |
|---|---|---|---|---|---|
| Ahrefs DiD, 1 885 pages | Tous types poolés | AIO | −4,6 % | Gain marginal sur pages déjà citées | Fort (quasi-causal, DiD) |
| Ahrefs DiD | Tous types poolés | AI Mode | +2,4 % (bruit) | Idem | Fort |
| Ahrefs DiD | Tous types poolés | ChatGPT | +2,2 % (bruit) | Idem | Fort |
| Fischman/SSRN, 730 cit. | Générique (Article, Org., BC) | ChatGPT + Gemini | 0 | Effet du balisage non différencié | Modéré (empirique cross-plateforme) |
| Fischman/SSRN | Product + Review complets | ChatGPT + Gemini | 61,7 % vs 41,6 % | Effet du balisage attribut-riche | Modéré (empirique cross-plateforme) |
| Digital Applied, 4 243 URL | Article + BreadcrumbList | AIO | 2,3× | Profil des pages déjà citées | Faible (observationnel, corrélation) |
| Digital Applied, 4 243 URL | HowTo | AIO | 2,8× | Profil des pages déjà citées | Faible (observationnel, corrélation) |
| Digital Applied, 5 000 sites | Article + BreadcrumbList | AIO + Perplexity + ChatGPT | +47 % | Corrélation balisage valide / citation | Faible (observationnel) |
| Digital Applied, 5 000 sites | Product + Offer | AIO + Perplexity + ChatGPT | +29 % | Corrélation | Faible (observationnel) |
| AirOps, 353 799 pages | JSON-LD (tous types) | ChatGPT | +6,5 pp (38,5 % vs 32,0 %) | Profil pages citées sur ChatGPT | Faible (observationnel) |
| AirOps | BreadcrumbList | ChatGPT | 46,2 % de taux de citation | Profil pages citées | Faible (observationnel) |
| AirOps | FAQPage | ChatGPT | 45,6 % de taux de citation | Profil pages citées | Faible (observationnel) |
| OtterlyAI case study, 2 000+ URL | Déploiement sitewide | AIO | +1 500 % | Avant/après (effets non isolés) | Très faible (cas unique, non contrôlé) |
| OtterlyAI | Déploiement sitewide | AI Mode | +377 % | Avant/après | Très faible |
| OtterlyAI | Déploiement sitewide | ChatGPT/Gemini/Copilot | Recul | Avant/après | Très faible |
| SAGEO Arena (arXiv 2602.12187) | Struct. info (titre + meta + headings + schema) | Pipeline GEO | +22 % Hit Rate | Retrieval benchmark académique | Modéré (A/B sur corpus contrôlé) |

**Lecture de ce tableau :** plus le niveau de preuve est fort, plus l'effet mesuré est faible ou nul. Plus il est faible, plus l'effet affiché est spectaculaire. Ce schéma est classique en épidémiologie et dans la littérature SEO : les études observationnelles capturent la corrélation entre qualité globale du site et balisage, pas l'effet du balisage lui-même.

### Les trois mécanismes qui expliquent la divergence

**Mécanisme 1 : effet d'entrée vs effet marginal**
Les études observationnelles (AirOps, Digital Applied) mesurent les pages qui ont déjà été citées. Ces pages ont aussi tendance à disposer d'un balisage, d'une meilleure structure, d'une autorité plus élevée. C'est le profil de l'entrée dans le bassin des sources citables. L'étude Ahrefs teste quant à elle l'effet marginal d'ajouter du balisage sur des pages déjà bien établies dans ce bassin : cet effet est nul ou légèrement négatif.

**Mécanisme 2 : Google vs non-Google**
Google exploite explicitement les données structurées dans son pipeline de classement et de récupération (RAG). L'effet OtterlyAI est concentré sur Google AI Overviews et AI Mode. ChatGPT, Perplexity, Claude et Gemini accèdent au HTML tokenisé complet et ne disposent pas (ou ne révèlent pas) de couche de parsing spécifique au balisage schema.org. Sur ChatGPT, AirOps montre une corrélation modeste (+6,5 points), mais Ahrefs ne mesure aucun effet causal. Fischman confirme : balisage générique = 0, balisage complet (Product/Review) = effet réel sur ChatGPT et Gemini.

**Mécanisme 3 : richesse vs présence**
Fischman isole un effet que les autres études ne testent pas : le balisage attribut-complet (prix réel, note agrégée, nombre d'avis, spécifications techniques renseignées dans le schema) se différencie du balisage générique (type Article sans propriétés). Les taux de citation de 61,7 % vs 41,6 % concernent les pages avec du balisage Product/Review pleinement renseigné, pas juste la balise `@type`.

---

## Nos propres chiffres (données de première main)

Le portefeuille de sites instrumentés (propriétés françaises, GSC + tracking AI Overviews, mars à juillet 2026) ne dispose pas encore de mesure isolant l'effet du balisage structuré. Les audits techniques réalisés montrent que la majorité des propriétés déploient Article, Organization et BreadcrumbList, mais sans validation systématique par Rich Results Test. La corrélation entre validation et taux de citation AIO n'a pas encore été mesurée en interne.

Ce bloc est honnêtement réservé. Une mesure avant/après sur une propriété qui corrige ses erreurs de validation (49 points d'écart médian entre déploiement et validation clean, selon Digital Applied) constituerait un premier point de données de première main pour cet angle.

---

## Contre-analyse

**Le biais de sélection de l'étude Ahrefs est réel, mais il va dans le mauvais sens pour les optimistes.**
L'étude porte sur des pages déjà massivement citées (100+ AIO). Si le balisage avait un effet positif, c'est précisément là qu'il devrait apparaître : sur des pages déjà indexées, déjà dans le bassin, déjà visibles de Google. L'absence d'effet (voire le léger recul) sur ce profil de pages est un signal fort. Elle n'exclut pas un effet d'entrée dans le bassin pour des pages qui n'y sont pas encore, mais elle invalide l'idée que le balisage seul débloque la citation.

**L'étude OtterlyAI ne contrôle pas les effets confondants.**
Un déploiement sitewide de balisage s'accompagne souvent de corrections de structure HTML, d'amélioration des métadonnées, de refonte de templates. Le +1 500 % n'est pas attribuable au seul JSON-LD. C'est une illustration de ce qu'un refactoring technique complet peut produire, pas un test isolé du schema.

**La corrélation AirOps confond balisage et investissement technique.**
Les sites qui déploient du JSON-LD valide sont aussi les sites qui soignent leur vitesse, leur architecture, leur contenu. L'écart de 6,5 points entre pages JSON-LD et pages sans n'est pas attribuable au seul balisage. AirOps le note explicitement.

**L'effet Perplexity est le plus opaque.**
Aucune étude avec une méthodologie contrôlée et publiée ne documente un effet du balisage structuré sur les citations Perplexity. OtterlyAI ne voit aucun effet ; AirOps ne testait pas Perplexity. Cette lacune est importante pour les stratégies GEO non centrées sur Google.

**La position reste le prédicteur dominant.**
Fischman mesure une réduction de 24 % des chances de citation par position SERP perdue. AirOps mesure un ratio 4× entre la position 1 (58,4 % de citation) et la position 10 (14,2 %). Le balisage amplifie, mais ne substitue pas le classement.

---

## FAQ

**Faut-il mettre du schema sur toutes les pages en 2026 ?**
Pas de manière indiscriminée. L'effet du balisage générique (Article, Organization, BreadcrumbList) sur les citations IA est faible ou nul selon l'étude la plus rigoureuse disponible (Ahrefs DiD). L'effet du balisage attribut-complet sur les contenus e-commerce (Product + AggregateRating avec prix, notes et spécifications renseignés) est mesurable dans les données Fischman. La priorité va à la validation du balisage existant (49 points d'écart médian entre déploiement et validation selon Digital Applied) avant tout nouveau déploiement.

**Le balisage FAQPage aide-t-il à être cité ?**
Sur ChatGPT, les pages avec FAQPage affichent un taux de citation de 45,6 % contre 32,0 % pour les pages sans JSON-LD (AirOps, 353 799 pages). Mais ce chiffre est observationnel : il décrit les pages citées, pas l'effet de l'ajout du balisage. Aucune étude quasi-causale n'isole l'effet FAQPage sur ChatGPT ou Perplexity en 2026.

**HowTo schema : pour quoi et sur quel moteur ?**
Digital Applied (1 000 AI Overviews) mesure un facteur 2,8× sur les requêtes procédurales pour les pages avec HowTo schema. L'effet est observationnel et limité aux AI Overviews de Google. Aucune donnée sur l'effet HowTo pour ChatGPT, Perplexity ou AI Mode en conditions contrôlées.

**Schema.org suffit-il pour entrer dans les citations IA ?**
Non. Fischman confirme que chaque position SERP perdue retire 24 % des chances de citation IA. AirOps mesure un ratio 4× entre position 1 et position 10. Le balisage est un signal amplificateur pour les pages déjà bien classées, pas un raccourci pour les pages faibles.

**Pourquoi les chiffres vont-ils de −4,6 % à +1 500 % ?**
Parce qu'ils mesurent des choses différentes : effet marginal d'un ajout (Ahrefs), corrélation dans le profil des pages déjà citées (AirOps, Digital Applied), ou résultat d'un refactoring technique complet dont le balisage n'est qu'une composante (OtterlyAI). Le tableau de réconciliation ci-dessus détaille chaque objet de mesure.

---

## [À SOURCER]

- **OtterlyAI +1 500 % / +377 %** : page primaire (otterly.ai/blog/schema-markup-real-impact-ai-search/) non accessible par fetch (contenu JavaScript non rendu). Chiffres tirés de la synthèse Analyzify qui cite ce blog. À vérifier en lecture directe.
- **Fischman/SSRN** : page SSRN retournée en 403. Les chiffres (61,7 % vs 41,6 %, 730 citations, 75 requêtes) proviennent des résultats de recherche et d'une synthèse secondaire. À vérifier sur la page papier directement.
- **Taux de citation FAQPage sur Perplexity** : aucune étude primaire disponible en 2026.
- **Effet schema sur Claude** : non documenté dans la littérature accessible.
- **Décomposition par type de schema dans l'étude Ahrefs DiD** : l'étude ne ventile pas les résultats Article vs HowTo vs FAQPage vs Product. C'est la lacune principale de la seule étude quasi-causale disponible.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté le |
|---|---|---|---|---|
| We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved. | Ahrefs (Louise Linehan, Xibeijia Guan) | 11 mai 2026 | https://ahrefs.com/blog/schema-ai-citations/ | 2026-07-21 |
| 1,000 AI Overviews Analyzed: Citation Pattern Study | Digital Applied | Avril 2026 | https://www.digitalapplied.com/blog/we-analyzed-1000-ai-overviews-citation-pattern-study | 2026-07-21 |
| Schema Markup Adoption: 5,000-Site Audit and Findings | Digital Applied | Avril 2026 | https://www.digitalapplied.com/blog/schema-markup-adoption-5k-site-audit-2026 | 2026-07-21 |
| The Fan-Out Effect: What Happens Between a Query and a Citation | AirOps (Kevin Indig) | 13 avril 2026 | https://www.airops.com/report/the-fan-out-effect-what-happens-between-a-query-and-a-citation | 2026-07-21 |
| Does Schema Markup Predict AI Citation? A Cross-Platform Empirical Study | Kurt Fischman / SSRN | 20 février 2026 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6284518 | 2026-07-21 [403, non vérifié par fetch] |
| Schema Markup's Real Impact on AI Search | OtterlyAI | Avril 2026 | https://otterly.ai/blog/schema-markup-real-impact-ai-search/ | 2026-07-21 [page vide, non vérifié par fetch] |
| Research Revealed: Schema Markup in AI Citations (synthèse) | Analyzify | Juin 2026 | https://analyzify.com/hub/schema-markup-ai-citations-research | 2026-07-21 |
| SAGEO Arena: A Realistic Environment for GEO Evaluation (arXiv:2602.12187) | Kim et al. / Yonsei University | Février 2025 | https://arxiv.org/abs/2602.12187 | Vault : raw/etudes-seo/etude-sageo-arena-2025.md |
| GEO: Generative Engine Optimization (arXiv:2311.09735) | Aggarwal et al. / Princeton, KDD 2024 | Août 2024 | https://arxiv.org/abs/2311.09735 | Vault : raw/etudes-seo/etude-geo-aggarwal-2024.md |
