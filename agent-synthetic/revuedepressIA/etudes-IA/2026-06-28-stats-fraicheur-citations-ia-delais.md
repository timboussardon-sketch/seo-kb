---
type: query
skill: seo-page-statistiques
status: draft
title: "Fraîcheur et citations IA en 2026 : âge moyen des pages citées, délais d'indexation et biais par plateforme"
aliases: ["fraîcheur contenu IA", "délai indexation IA", "age pages citées IA", "recency bias AI search"]
tags: [geo, citations-ia, fraicheur, indexation, perplexity, chatgpt, ai-overviews, statistiques, 2026]
created: 2026-06-28
updated: 2026-06-28
sources: 8
confidence: medium
---

# Fraîcheur et citations IA en 2026 : âge moyen des pages citées, délais d'indexation et biais par plateforme

*28 juin 2026*

Les pages citées par les moteurs IA ont en moyenne 2,9 ans d'ancienneté — pas quelques semaines. L'avantage de fraîcheur des IA sur l'organique Google existe (25,7 %), mais il masque des écarts massifs entre plateformes : ChatGPT cite des pages vieilles de 958 jours en moyenne, Google AI Overviews des pages vieilles de 1 432 jours, soit le même profil que les résultats organiques classiques. La fraîcheur n'est pas un signal universel : c'est un signal conditionnel, qui dépend de la plateforme, du type de requête et du mécanisme mesuré.

---

## Les chiffres clés (vérifiés à la source)

### Âge moyen des pages citées par les moteurs IA

Étude Ahrefs Brand Radar, juillet 2025, 16,975 millions d'URLs cités sur 6 systèmes :

| Plateforme | Âge moyen depuis publication |
|---|---|
| ChatGPT (citations directes) | **958 jours** (~2,6 ans) |
| ChatGPT (références) | 1 023 jours |
| Copilot | 1 056 jours |
| Gemini | 1 118 jours |
| Perplexity | 1 166 jours (~3,2 ans) |
| Google AI Overviews | 1 432 jours (~3,9 ans) |
| **Moyenne IA (toutes plateformes)** | **1 064 jours** |
| Résultats organiques Google (référence) | 1 432 jours |

Avantage fraîcheur des IA sur l'organique : **25,7 %** pour la date de publication, **13,1 %** pour la date de dernière mise à jour (909 jours vs 1 047 jours).

Ahrefs lui-même note : « L'âge moyen des pages citées est encore 2,9 ans. Comme la recherche traditionnelle, les IA préfèrent le contenu établi. »

### Distribution par année de publication (Seer Interactive, juin 2025, 5 000+ URLs)

| Plateforme | Part des citations de 2025 | Part des citations 2023-2025 |
|---|---|---|
| Perplexity | **50 %** | 80 % |
| Google AI Overviews | **44 %** | 85 % |
| ChatGPT | **31 %** | 71 % |

Au niveau global (toutes plateformes confondues) : 65 % des hits des robots IA portent sur du contenu publié dans l'année écoulée, 79 % sur les deux dernières années, 89 % sur les trois dernières années.

### Lift de fraîcheur par la mise à jour (SE Ranking, 2025)

- Contenu mis à jour dans les 3 derniers mois : **2 fois plus souvent cité** par ChatGPT que le contenu non mis à jour.
- Pages mises à jour dans les 2 derniers mois : **28 % plus souvent citées** par Google AI Mode que les pages non touchées depuis plus de 2 ans.

### Injection temporelle par les IA dans leurs sous-requêtes (Qwairy, 2026, 102 018 requêtes)

Les moteurs IA ajoutent automatiquement l'année en cours dans **28,1 % de leurs sous-requêtes** de récupération, même quand l'utilisateur n'a pas mentionné de date. Le terme « 2026 » apparaît **184 fois plus souvent** que « 2025 » dans les sous-requêtes générées.

### Délais d'indexation estimés

- Perplexity (index propriétaire 200+ milliards d'URLs) : nouveau contenu surfaçable **dans les jours** suivant le crawl [À SOURCER : estimation Parse.gl, pas de mesure directe publiée]
- ChatGPT Search (via index Bing) : délai typique **2 à 6 semaines** après amélioration du rang Bing, selon Conbersa (2026)
- Google AI Overviews : pas de délai spécifique documenté indépendamment de l'index Google

---

## Trois mécanismes de fraîcheur, trois profils de résultats

Les chiffres sur la fraîcheur semblent contradictoires selon les études. Une page médiane citée par AI Overviews a 14 mois (DigitalApplied) ; 50 % des citations IA ont moins de 13 semaines (Amsive/Lily Ray). Ces deux chiffres sont vrais : ils mesurent des réalités différentes.

Il faut distinguer trois mécanismes :

**Mécanisme 1 — La fraîcheur de récupération (pré-sélection)**

Avant de choisir quoi citer, les moteurs IA lancent des sous-requêtes internes. Qwairy montre que 28,1 % de ces sous-requêtes incluent automatiquement l'année courante. Le pool de pages candidates est donc déjà biaisé vers le récent, indépendamment de tout critère de qualité. C'est le mécanisme le plus diffus et le plus universel.

**Mécanisme 2 — La fraîcheur de sélection (post-récupération)**

Une fois dans le pool de candidats, l'âge de la page influence-t-il la sélection finale ?

La réponse varie fortement selon la plateforme :

- Pour ChatGPT (browse en temps réel via Bing) : oui, avec un multiplicateur mesuré de 2× pour les pages mises à jour dans les 3 derniers mois (SE Ranking).
- Pour Google AI Overviews sur des requêtes informationnelles : non. DigitalApplied (1 000 AI Overviews, avril 2026) trouve que la fraîcheur de la page « n'a aucun effet mesurable » sur l'inclusion dans les citations. L'âge médian des pages citées par AIO est de 14 mois, et la corrélation dominante reste l'autorité du domaine (+0,61).

**Mécanisme 3 — La fraîcheur de corpus (structure globale)**

Au niveau agrégé, le corpus de ce que les IA citent est structurellement plus jeune que ce que Google classe en organique (1 064 jours vs 1 432 jours). Mais cet écart global masque le fait que la grande majorité du contenu cité est du contenu établi, pas du contenu récent.

**La réconciliation** : les études qui documentent un fort effet de fraîcheur (Amsive : 50 % < 13 semaines ; SE Ranking : 2×) mesurent des plateformes de navigation en temps réel sur des requêtes d'actualité ou commerciales. Les études qui trouvent un effet faible (DigitalApplied, Ahrefs dans leur propre caveat) mesurent soit des AI Overviews sur des requêtes informationnelles établies, soit le corpus global qui reste dominé par du contenu de 2 à 3 ans.

Deux réalités coexistent : la mise à jour produit un effet réel sur ChatGPT et Perplexity pour des requêtes sensibles à l'actualité, et n'a pratiquement aucun effet sur AIO pour des requêtes informationnelles où l'autorité l'emporte.

---

## Nos propres chiffres (données de première main)

L'étude SearchLLM (Xiaohongshu/RedNote, KDD 2026), ingérée dans ce vault, apporte un éclairage issu d'un système de recherche générative en production à grande échelle (données réelles, non simulées).

Le système de reward de SearchLLM place le **factual grounding en gate principale non-négociable** (Layer I) : si un contenu ne passe pas la vérification de factualité et de cohérence logique, son score global tombe à zéro — indépendamment de sa fraîcheur. La fraîcheur n'intervient qu'au Layer II (objectifs comportementaux), nettement en dessous dans la hiérarchie.

Ce finding confirme la lecture inverse des données agrégées : les moteurs IA citent du contenu récent non parce que la récence est un signal fort, mais parce que le contenu récent tend à être mieux sourcé et structuré. La corrélation fraîcheur/citation reflète en partie une corrélation fraîcheur/qualité formelle, pas une préférence directe pour la nouveauté.

---

## Contre-analyse

Quatre raisons de ne pas surpondérer la fraîcheur dans une stratégie de citation IA.

**1. DigitalApplied (avril 2026) : fraîcheur = zéro effet sur AI Overviews**

Sur 1 000 AI Overviews analysées et 4 243 URLs uniques (avril 8-22, 2026), la fraîcheur de la page ne montre « aucun effet mesurable » sur l'inclusion dans les citations. La corrélation dominante est l'autorité de domaine (+0,61). L'âge médian des pages citées est de 14 mois — ce qui n'est pas du contenu vieux, mais pas non plus de la publication de la semaine. Pour les AI Overviews, l'ancienneté et l'établissement priment.

**2. Ahrefs reconnaît lui-même le paradoxe**

Malgré l'avantage de 25,7 %, Ahrefs note explicitement : « La moyenne d'âge citée est encore 2,9 ans. Comme la recherche traditionnelle, les IA préfèrent le contenu établi. » L'avantage de fraîcheur est réel mais modéré ; il ne transforme pas les IA en moteurs d'actualité.

**3. Les multiplicateurs viraux sont sans source primaire**

Le chiffre « 4,3× de citations supplémentaires pour le contenu récent » a été débunké par DigitalApplied : « Ce chiffre viral ne renvoie à aucune étude primaire et ne doit pas être répété. » La même mise en garde s'applique au « 3,2× pour le contenu < 30 jours » qui circule largement sans source vérifiable.

**4. L'injection temporelle est un biais de récupération, pas de sélection**

Qwairy (28,1 % de sous-requêtes avec injection de l'année) montre que la fraîcheur intervient au stade de la récupération. Les IA demandent des pages récentes à leur index — mais ce n'est pas la même chose que de sélectionner les pages récentes parmi les candidates. La sélection finale obéit à d'autres critères (autorité, structure, sourcing). Confondre les deux mécanismes surévalue l'effet de la fraîcheur sur la citation finale.

---

## FAQ

**Combien de temps faut-il pour qu'une page nouvelle soit citée par les moteurs IA ?**
La seule estimation documentée concerne ChatGPT Search : 2 à 6 semaines après l'amélioration du rang Bing (Conbersa, 2026). Pour Perplexity, le délai serait de quelques jours après crawl, mais aucune mesure indépendante ne le confirme. Google AI Overviews suit vraisemblablement le cycle d'indexation habituel de Google. Utiliser IndexNow pour pousser les mises à jour vers Bing accélère la chaîne pour ChatGPT.

**Faut-il mettre à jour son contenu pour être cité par les IA ?**
Pour ChatGPT sur des requêtes sensibles à l'actualité : oui, la mise à jour dans les 3 mois produit un lift mesuré de 2× (SE Ranking). Pour les requêtes informationnelles sur Google AIO : l'autorité de domaine compte davantage que la fraîcheur. La mise à jour reste utile car le contenu structuré et sourcé tend à mieux performer dans les deux cas.

**Perplexity favorise-t-il vraiment les contenus plus récents que ChatGPT ?**
En termes d'âge absolu, non : Perplexity cite en moyenne des pages vieilles de 1 166 jours, contre 958 jours pour ChatGPT. Mais en termes de distribution annuelle, Perplexity a la plus forte proportion de citations de 2025 (50 %) contre 31 % pour ChatGPT. Ces deux mesures sont cohérentes : Perplexity est actif sur des requêtes d'actualité (50 % de 2025) tout en ayant une longue traîne de contenu établi qui tire sa moyenne vers le haut.

**L'âge d'un contenu est-il un signal direct dans les algorithmes de citation IA ?**
Pas directement. Les preuves pointent vers une corrélation indirecte : (1) les sous-requêtes de récupération incluent l'année courante pour 28 % d'entre elles, biaisant le pool ; (2) le contenu récent tend à être mieux structuré et plus sourcé, ce qui satisfait les véritables critères de sélection (factual grounding, authority, schema). La fraîcheur est un signal de qualité corrélé, pas un critère de sélection autonome.

---

## [À SOURCER]

- **« 3,2× plus de citations pour le contenu publié dans les 30 derniers jours »** : chiffre largement repris dans l'écosystème GEO, mais sans étude primaire identifiable. À ne pas citer tel quel. Le multiplicateur le plus fiable disponible est le 2× de SE Ranking sur 3 mois pour ChatGPT.
- **Délai d'indexation Perplexity « dans les jours »** : estimation citée par Parse.gl, sans protocole de mesure publié. Plausible compte tenu de l'architecture de crawl de Perplexity, mais non vérifiable à ce stade.
- **Différence entre « 67 % de lift » (Parse.gl) et « 2× = 100 % de lift » (SE Ranking)** pour les pages mises à jour dans les 3 mois : les deux chiffres proviennent de mesures différentes (nombre absolu de citations vs probabilité d'être cité). Non réconciliés à ce stade.

---

## Sources

1. **New Study: AI Assistants Prefer to Cite "Fresher" Content (17 Million Citations Analyzed)** — Ahrefs, juillet 2025. https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/ — consulté le 28 juin 2026.

2. **Study: AI Brand Visibility and Content Recency** — Seer Interactive, juin 2025. https://www.seerinteractive.com/insights/study-ai-brand-visibility-and-content-recency — consulté le 28 juin 2026.

3. **1,000 AI Overviews Analyzed: Citation Pattern Study** — DigitalApplied, avril 2026. https://www.digitalapplied.com/blog/we-analyzed-1000-ai-overviews-citation-pattern-study — consulté le 28 juin 2026.

4. **70+ AI Search Stats for 2026** — SE Ranking, 2025-2026. https://seranking.com/blog/ai-statistics/ — consulté le 28 juin 2026.

5. **Content Freshness & AI Citations Guide (2026)** — Qwairy, 2026. https://www.qwairy.co/blog/content-freshness-ai-citations-guide — consulté le 28 juin 2026.

6. **The 2026 State of AI Search** — AirOps, 2026. https://www.airops.com/report/the-2026-state-of-ai-search — consulté le 28 juin 2026.

7. **Bing Indexing Optimization: Why 87% of ChatGPT Citations Come From Bing** — Conbersa, 2026. https://www.conbersa.ai/learn/bing-indexing-optimization-for-chatgpt — consulté le 28 juin 2026.

8. **Content Freshness and AI Search: Why 50% of AI Citations Are Under 13 Weeks Old** — Salespeak (citant Lily Ray / Amsive Digital), 2026. https://salespeak.ai/aeo-news/content-freshness-ai-search — consulté le 28 juin 2026.

9. **SearchLLM: Aligning Large Language Models with Searcher Preferences** — Wu et al., Xiaohongshu Inc. / USTC / HKUST, KDD 2026. arXiv:2603.10473. [Ingéré dans raw/etudes-seo/etude-searchllm-2026.md]
