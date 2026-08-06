---
type: query
skill: seo-page-statistiques
title: "Hallucinations et citations erronées dans les moteurs IA : quatre phénomènes que l'industrie confond (2025-2026)"
aliases: ["hallucinations IA citations", "citations fantômes moteurs IA", "taux hallucinations ChatGPT Perplexity Grok"]
tags: [hallucinations, citations-ia, geo, moteurs-ia, fiabilite, perplexity, chatgpt, grok, citations-fantomes, newsguard, cjr]
created: 2026-08-06
updated: 2026-08-06
sources: 8
confidence: medium
status: draft
---

# Hallucinations et citations erronées dans les moteurs IA : quatre phénomènes que l'industrie confond (2025-2026)

*2026-08-06*

Perplexity se trompe 37 % du temps sur les citations de presse. Grok 3 génère des URLs inexistantes dans 77 % des cas. Les chatbots produisent des affirmations factuellement fausses dans 35 % des réponses sur l'actualité. Et 61,7 % des citations sources émises par les moteurs IA n'incluent pas le nom de la marque dans le texte. Ces quatre chiffres circulent tous sous le terme « hallucination », mais ils mesurent des réalités distinctes. Les confondre revient à comparer des thermomètres et des balances.

---

## Les chiffres clés (vérifiés à la source)

### Erreurs de citation dans la presse (Tow Center / CJR, fév. 2025)

La Tow Center for Digital Journalism de l'université Columbia a soumis 1 600 requêtes à huit plateformes de recherche IA, portant sur 200 articles issus de 20 éditeurs de presse. Plus de 60 % des réponses étaient incorrectes, toutes plateformes confondues.

| Plateforme | Taux d'erreur | Type dominant |
|---|---|---|
| Perplexity (libre + Pro) | 37 % | Misattribution |
| DeepSeek | 57,5 % (115/200) | Misattribution |
| ChatGPT Search | 67 % (134/200) | Mauvaise identification d'article |
| Google Gemini | > 50 % | URLs fabriquées ou cassées |
| Grok 2 | n. c. | Liens vers page d'accueil |
| Grok 3 | 94 % | 77 % d'URLs vers pages d'erreur (154/200) |

Claude (Anthropic) n'a pas été testé dans cette étude. Copilot est inclus dans l'agrégat >60 %, mais son taux individuel n'a pas été publié séparément.

L'erreur dominante, contrairement à l'idée reçue, n'est pas l'URL inventée de toutes pièces. C'est la misattribution : une URL réelle, fonctionnelle, créditée d'une affirmation qu'elle ne contient pas. Les URLs entièrement fabriquées existent mais caractérisent surtout Grok 3 et Gemini dans ce corpus.

### Fausses affirmations factuelles dans l'actualité (NewsGuard, août 2024 – avr. 2025)

NewsGuard teste mensuellement dix à onze chatbots sur des sujets d'actualité complexes. En août 2024, le taux de fausses affirmations était de 18 %. En août 2025, il atteint 35 % — quasi-doublement en un an. En parallèle, le taux de non-réponse est passé de 31 % (août 2024) à 0 % (août 2025) : les moteurs répondent désormais à tout.

En avril 2025, sur un panel de onze chatbots (ChatGPT-4, Grok, Pi, Le Chat, Copilot, Meta AI, Claude, Gemini, Perplexity, DeepSeek, You.com), le taux combiné fausses affirmations + non-réponses atteignait 41,5 %. Le rapport ne désagrège pas les résultats par modèle.

### Citations fantômes et invisibilité de marque (AuthorityTech, avr. 2026)

Sur 3 981 domaines, 115 requêtes et quatre moteurs IA dans 14 pays, 61,7 % des citations sources ne font pas apparaître le nom de la marque dans le corps de la réponse. Le domaine est référencé comme source, l'URL est réelle, mais la marque est absente du texte. AuthorityTech nomme ce phénomène « ghost citation ».

Ce n'est pas une hallucination au sens classique. Aucune URL n'est inventée. Seulement 13,2 % des apparences cumulent à la fois une citation et une mention de marque dans la réponse. Perplexity est le moteur qui produit le plus souvent des citations avec mention de marque (dans le corpus testé) ; ChatGPT génère le plus de citations sans mention.

### Références bibliographiques académiques (arXiv 2505.18059, mai 2025)

Huit chatbots (ChatGPT, Claude, Copilot, DeepSeek, Gemini, Grok, Le Chat, Perplexity, tous en version gratuite) ont été testés sur 400 références bibliographiques réparties dans cinq domaines scientifiques (santé, ingénierie, sciences expérimentales, sciences sociales, humanités). Résultats :

- 26,5 % de références entièrement correctes
- 33,8 % partiellement correctes
- **39,8 % erronées ou fabriquées**

Grok et DeepSeek sont les seuls à n'avoir produit aucune référence entièrement fausse. Copilot, Perplexity et Claude affichent les taux les plus élevés d'hallucination bibliographique. Les articles de revues scientifiques présentent un taux de fabrication plus élevé que les livres, probablement parce que les chatbots privilégient les formats qu'ils reconnaissent le mieux dans leur mémoire paramétrique.

### Domaine médical (2025-2026, données agrégées)

Dans les vignettes cliniques sans aide contextuelle, les taux d'hallucination mesurent 64,1 à 67,6 % (études MedRxiv 2025). Avec des prompts structurés, ce taux baisse d'environ 33 %. Les citations fabriquées (DOI, auteurs, titres d'articles) dépassent 45 % dans les tâches de rédaction médicale assistée. GPT-4o sans aide contextuelle atteint 53 % d'erreurs cliniques ; GPT-5 en mode réflexif descend à 4,8 %.

---

## Pourquoi ces chiffres divergent : quatre phénomènes distincts sous un même mot

Voici la réconciliation des mesures qui semblent se contredire.

| Phénomène | Définition | Étude de référence | Taux observé |
|---|---|---|---|
| **Misattribution de citation** | URL réelle, affirmation fausse attribuée | CJR/Tow Center, fév. 2025 | 37 % (Perplexity) à 94 % (Grok 3) |
| **URL fabriquée ou cassée** | Lien inexistant ou menant à une page d'erreur | CJR/Tow Center, fév. 2025 | Grok 3 : 77 % ; Gemini : >50 % |
| **Affirmation factuelle fausse** | Réponse incorrecte, source présente ou non | NewsGuard, août 2025 | 35 % (agrégat, 10-11 chatbots) |
| **Citation fantôme** | Source citée, marque absente du texte | AuthorityTech, avr. 2026 | 61,7 % |
| **Référence bibliographique fabriquée** | DOI / auteurs / titre inexistants | arXiv 2505.18059, mai 2025 | 39,8 % (toutes plateformes) |

Ces phénomènes ne s'additionnent pas simplement et ne désignent pas le même risque. Une page peut être citée avec une URL réelle (pas d'URL fabriquée), nommer la marque dans le texte (pas de citation fantôme), mais attribuer à l'article une affirmation qu'il ne contient pas (misattribution). Trois dimensions indépendantes, une seule réponse apparemment « correctement sourcée ».

---

## Le paradoxe des classements inversés par cas d'usage

Un résultat traverse ces études de façon cohérente : les plateformes se classent dans l'ordre inverse selon ce qu'on mesure.

Perplexity est le meilleur sur les citations de presse (37 % d'erreur, CJR, le plus faible du panel) mais figure parmi les pires sur les références bibliographiques académiques (taux le plus élevé dans l'étude arXiv 2505.18059, confirmé par une étude orthopédique de Springer Nature sur 3 150 références). Grok 3 est le pire sur les citations de presse (94 %) mais Grok est l'un des deux seuls chatbots à produire zéro référence bibliographique fausse. DeepSeek affiche 57,5 % d'erreurs de misattribution dans la presse mais fait partie des deux meilleurs en bibliographie académique.

L'explication architecturale est cohérente. Perplexity repose sur de la recherche web en temps réel (récupération de pages depuis le web, dite RAG — pour Retrieval-Augmented Generation). Cela lui permet de retrouver des articles de presse récents mais ne lui donne pas accès aux bases académiques payantes, dont les articles sont rarement librement indexables. Grok et DeepSeek ont une mémoire paramétrique plus solide sur les faits académiques stables, mais peinent à naviguer le paysage des éditeurs de presse avec leurs URLs dynamiques et leur gestion des droits.

Ce paradoxe a une implication concrète : il n'existe pas un « meilleur moteur IA » pour la fiabilité des sources. La plateforme la moins risquée dépend du type de requête.

---

## Nos propres chiffres (données de première main)

Ce portefeuille ne dispose pas de mesure directe de taux d'hallucination sur des propriétés contrôlées. Ce bloc est réservé honnêtement.

Une donnée de contexte est disponible dans le vault : l'étude SearchLLM (Wu et al., Xiaohongshu / USTC / HKUST, KDD 2026, arXiv:2603.10473 — [[raw/etudes-seo/etude-searchllm-2026]]) documente un système de recherche générative en production à grande échelle sur RedNote. Le système traite le factual grounding comme une contrainte de niveau inférieur non négociable : si un seul score de vérification factuelle échoue, la récompense d'ensemble tombe à zéro, bloquant toute optimisation comportementale. La détection d'hallucination intégrée atteint 85-95 % de précision contre 49-89 % pour les approches génériques. Ce chiffre n'est pas un taux d'hallucination des réponses mais une mesure de la détection en amont, et il indique que les opérateurs de moteurs en production prennent la mesure du problème au niveau de l'infrastructure.

---

## Contre-analyse

**Les modèles évoluent trop vite pour que les taux soient stables.** L'étude CJR date de février 2025, Grok 3 était en bêta, Gemini et ChatGPT Search n'étaient pas dans les versions actuelles. Les quatre plateformes ont changé depuis. Les taux publiés sont des photographies d'un instant, pas des constantes.

**Il n'existe pas de définition standardisée d'hallucination.** Chaque étude mesure un objet différent. Le 37 % du CJR (misattribution dans la presse) et le 35 % de NewsGuard (fausses affirmations factuelles) ne se superposent pas. Le 39,8 % d'arXiv (références bibliographiques fabriquées) mesure un troisième phénomène. Additionner ces chiffres n'a pas de sens.

**L'accès au web réduit fortement les hallucinations.** Les modèles avec navigation web réduisent leurs taux de 73 à 86 % sur les benchmarks standardisés. GPT-5 sans navigation web affiche 47 % d'hallucinations sur SimpleQA ; avec navigation, 9,6 %. L'architecture détermine autant le taux que le modèle lui-même.

**La hausse 2024-2025 de NewsGuard reflète en partie un changement de comportement, pas uniquement une dégradation factuelle.** En août 2024, les chatbots refusaient 31 % des questions. En août 2025, ce taux est à 0 %. Les moteurs répondent désormais à tout, y compris ce qu'ils ignorent. La hausse mécanique du taux de fausses affirmations est en partie l'envers de la disparition des non-réponses.

**Les mesures de NewsGuard portent sur des sujets délibérément complexes.** Les prompts ciblent des thèmes de vérification active (désinformation en circulation, fausses affirmations politiques). Ces 35 % ne sont pas représentatifs d'un usage général de recherche d'information.

**Perplexity n'est pas exempt du problème de droits.** Perplexity fait l'objet de litiges actifs (dont une procédure du New York Times, décembre 2025) pour crawl sans autorisation. Les bonnes performances sur les citations de presse dans le CJR ne préjugent pas de la légalité de l'accès aux sources.

---

## FAQ

**Quel moteur IA commet le moins d'erreurs sur les citations de presse ?**
Perplexity (libre et Pro), avec 37 % d'erreurs dans l'étude Tow Center de février 2025. Toutes les autres plateformes testées dépassent 50 %.

**Quel moteur fabrique le plus d'URLs inexistantes ?**
Grok 3 (bêta, fév. 2025) : 154 citations sur 200 mènent à des pages d'erreur (77 %). Gemini dépasse 50 % de liens fabriqués ou cassés dans le même corpus.

**La situation s'aggrave-t-elle ?**
Sur les fausses affirmations factuelles (NewsGuard), le taux a quasi-doublé entre août 2024 et août 2025 (18 % → 35 %), mais cette hausse est partiellement mécanique : les chatbots qui refusaient de répondre avant tentent désormais tout. Sur les benchmarks de synthèse documentaire, les meilleurs modèles descendent sous 1 % (Gemini 2.0 Flash : 0,7 % sur Vectara HHEM). L'image d'ensemble n'est pas univoque.

**Dans quel domaine les hallucinations sont-elles les plus graves ?**
Le domaine médical combine taux élevé (64-67 % sans aide contextuelle sur des vignettes cliniques) et conséquences directes sur les décisions de soin. Le domaine juridique présente des taux de 58 à 88 % sur des cas de tribunaux fédéraux réels.

**Claude est-il fiable pour les citations ?**
Claude n'a pas été testé dans l'étude CJR sur les citations de presse. Dans l'étude arXiv sur les références bibliographiques (8 chatbots, mai 2025), Claude figure parmi les plateformes aux taux les plus élevés d'hallucination, avec Copilot et Perplexity. Claude ne propose pas de liens sources par défaut dans son mode conversationnel standard.

**Une seule métrique suffit-elle pour choisir un moteur IA ?**
Non. Perplexity est le meilleur pour les citations de presse et le pire pour les références académiques. Grok est le pire pour les citations de presse et le meilleur en bibliographie. La plateforme la moins risquée dépend du type de recherche effectuée.

---

## [À SOURCER]

- Microsoft Copilot : taux d'erreur précis dans l'étude CJR (agrégat >60 % uniquement, non désagrégé)
- Perplexity Pro vs Perplexity libre : taux d'erreur séparés dans CJR (fournis groupés)
- Springer Nature / Indian Journal of Orthopaedics (2026) : Reference Hallucination Score ChatGPT 1,81, Gemini 4,01, Perplexity 6,51 sur 3 150 références — chiffres issus du résumé de recherche secondaire, source primaire derrière paywall, non fetché directement
- NewsGuard : taux par modèle individuel (août 2025 fourni en agrégat uniquement, pas de tableau par chatbot accessible)
- Données France / Europe : aucune étude équivalente au CJR sur des éditeurs francophones identifiée

---

## Sources

1. **AI Search Has a Citation Problem** — Tow Center for Digital Journalism, Columbia University, Mars 2025. https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php (consulté 2026-08-06)

2. **AI False Claim Monitor, August 2025** — NewsGuard, 4 septembre 2025. https://www.newsguardtech.com/ai-monitor/august-2025-ai-false-claim-monitor/ (consulté 2026-08-06)

3. **AI False Claim Monitor, April 2025** — NewsGuard, 2025. https://www.newsguardtech.com/ai-monitor/april-2025-ai-misinformation-monitor/ (consulté 2026-08-06)

4. **61% of AI Citations Are Ghost Citations** — AuthorityTech (Kevin Indig / Growth Memo, via Search Engine Journal), Avril 2026. https://authoritytech.io/curated/ghost-citations-ai-brand-visibility-2026 (consulté 2026-08-06)

5. **Assessing the performance of 8 AI chatbots in bibliographic reference retrieval: Grok and DeepSeek outperform ChatGPT, but none are fully accurate** — arXiv:2505.18059, Mai 2025. https://arxiv.org/abs/2505.18059 (consulté 2026-08-06)

6. **Medical AI Hallucination Rates 2026: HealthBench, Clinical Vignettes, ChatGPT vs Med-PaLM** — Presenc.ai (agrégat d'études MedRxiv 2025 et OpenAI HealthBench, Avril 2026). https://presenc.ai/research/medical-ai-hallucination-rates-2026 (consulté 2026-08-06)

7. **Latest AI Hallucination Rates & Benchmarks (août 2026)** — Suprmind (agrégat Vectara HHEM, FACTS, AA-Omniscience, CJR). https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/ (consulté 2026-08-06)

8. **SearchLLM: Aligning Large Language Models with Searcher Preferences** — Wu et al., Xiaohongshu / USTC / HKUST, KDD 2026. arXiv:2603.10473. Données de première main vault : [[raw/etudes-seo/etude-searchllm-2026]]
