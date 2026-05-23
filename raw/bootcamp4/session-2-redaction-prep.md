---
type: bootcamp-session-prep
bootcamp: 4
session: 2
topic: rédaction-scoring-modèles-page
date: 2026-05-13
duration: 70 min
status: prep
tags:
  - bootcamp4
  - session-2
  - rédaction
  - workflow
  - fact-check
  - scoring
  - modeles-de-page
  - pseo
related:
  - "[[session-1-mots-cles-prep]]"
  - "[[sequencage-semaine-2]]"
  - "[[ton-de-voix-worksheet]]"
  - "[[seo-brief-contenu]]"
  - "[[article-engine-pipeline]]"
  - "[[seo-workflow-article]]"
  - "[[seo-entites-vectorielles]]"
  - "[[seo-programmatique-pseo]]"
  - "[[opendecoder-seo-scoring-system]]"
---

# Session 2 · Rédaction, scoring, modèles de page · Prep

Idée directrice : un bon article ne vient pas du workflow tout seul, il vient de ce que tu lui injectes avant et de comment tu l'arrêtes en cours de route. La rédaction industrielle ne se mesure pas en mots produits, elle se mesure en surprise délivrée et en vecteur sémantique aligné.

Cadrage du call : ils ont déjà le workflow rédaction depuis mercredi. Aujourd'hui, on leur montre **comment mieux rédiger avec l'IA aidé de ce workflow**. Pas une présentation du workflow lui-même, une présentation de la méthode autour du workflow.

Ordre du call :
1. Le contexte d'abord (sans contexte, tout le reste s'effondre) + la règle "une seule conversation par projet"
2. La méthode rédaction en 5 étapes (brief → data propriétaire → idées perso → workflow 50% → fact-checking)
3. Le scoring · `opendecoder-seo-scoring-system` (S_Pertinence + règle des 3 bonus)
4. Les modèles de page (passer de l'article unique au système scalable)

---

## 1 · Le contexte avant tout

Avant de parler workflow, on insiste sur ce qui fait 80% du résultat : ce que tu donnes à Claude au moment où tu lances la rédaction. Sans contexte, ton vecteur reste générique. Même vecteur que les 50 autres pages sur la requête = nulle part dans la SERP. La divergence du vecteur crée le Surprise Gap. C'est elle que Google et les moteurs de réponse repèrent pour décider qui citer.

Quatre sources alimentent ce contexte, dans cet ordre de priorité.

**Calls clients.** Verbatims, objections réelles, vocabulaire des prospects. La seule source qui donne le langage non filtré du marché. Ni la SERP ni les outils SEO ne remontent ça.

**Études de marché et données propriétaires.** Chiffres, segments, taux, parts de marché. Le grounding factuel qui transforme un avis en assertion citable. Une étude DARES vaut dix posts LinkedIn.

**Reddit.** Pain points, vocabulaire péjoratif, métaphores. Une couche de langage que Google n'indexe qu'en surface et que ChatGPT a peu vue. Source de micro-intentions invisibles dans la SERP.

**Grok mode expert.** Data fraîche X, Reddit et forums spécialisés en temps réel. Le complément que ChatGPT n'a pas, parce que sa fenêtre de connaissance est coupée.

Concrètement, avant de lancer la rédaction, tu injectes dans Claude :
1. Le brief du jour 1 (avec sa structure Hn — on y revient)
2. Le worksheet ton de voix rempli + le doc complémentaire fourni avec le skill rédaction
3. Le dossier client : data propriétaire, calls, verbatims
4. Les 3-5 concurrents analysés (ce qu'ils disent / ce qu'ils ne disent pas)

Sans ces quatre inputs, Claude écrit avec son corpus moyen. Avec, il écrit avec toi.

### Règle non-négociable · une seule conversation Claude par projet

C'est la règle qui change tout et que personne n'applique au démarrage. Le brief, le ton de voix, l'enrichissement, la rédaction, le fact-check, le scoring : tout reste dans **la même conversation Claude**, pour **un projet donné** (un client = une conversation, un site = une conversation).

Pourquoi :
- Le contexte s'accumule. Chaque tour de conversation augmente le grounding sur le client.
- Le ton de voix se stabilise. Plus la conversation avance, plus Claude reproduit ton ton.
- Les corrections se propagent. Une correction faite au tour 5 reste valable au tour 50.
- Les références entre les pages tiennent. Quand tu rédiges l'article 8, Claude se souvient de l'article 3 et peut mailler.

Conséquence pratique : tu ne lances pas une nouvelle conversation à chaque nouvelle requête. Tu reprends la conversation existante pour ce client, et tu continues. Si tu commences un nouveau client, c'est une nouvelle conversation, dédiée.

> Règle simple : si tu ouvres une nouvelle conversation Claude sans contexte injecté, tu n'es pas en train de rédiger, tu es en train de générer. Ce n'est pas la même chose.

---

## 2 · La méthode rédaction · 5 étapes

Cinq étapes, dans l'ordre. Chacune nourrit la suivante. Si tu sautes une étape, la suivante s'effondre.

### Étape 1 · Le brief

Tout commence par le brief. Tu lances `seo-brief-contenu` sur la requête cible et tu lui demandes explicitement la structure Hn complète **dans la même demande**. Hn dans le brief, pas après, pas en livrable séparé. Brief sans structure Hn validée = brief incomplet, donc article qui retombe dans le format LLM moyen.

Pourquoi la structure Hn est centrale : c'est le squelette sémantique de ta page. La liste des micro-intentions que ta page doit couvrir, dans l'ordre où elles s'enchaînent logiquement. Sans elle, Claude structure à sa façon par défaut. Intro mou, trois sous-titres décoratifs, conclusion qui résume. Le format LLM moyen. Tu retombes dans la commodité.

Ce que doit contenir une structure Hn valide :
- Couverture exhaustive des micro-intentions de la requête (cf session 1)
- Hiérarchie d'intention respectée (Know-Simple en début pour répondre vite, Know au milieu pour approfondir, Do en fin pour convertir)
- Un H2 dédié au passage ancré (extractible en Featured Snippet)
- Une section FAQ à la fin, pas en milieu de page (micro-intentions long-tail)
- Au moins un H2 qui couvre l'angle absent de la SERP (Surprise Gap)

Tu valides la structure Hn avant tout. Si elle ne te plaît pas, tu la corriges manuellement et tu réinjectes la version corrigée. Tu ne lances jamais la suite sur une structure faiblarde.

### Étape 2 · Nourrir le brief avec ta data propriétaire

La structure Hn est validée. Avant la rédaction, tu nourris chaque H2 avec la matière objective que tu possèdes déjà. C'est l'étape qui transforme un brief générique en brief client.

Si tu sautes cette étape, ton article s'appuie sur le corpus moyen de Claude. Avec elle, il s'appuie sur ce que personne d'autre n'a sous la main.

Pour chaque H2, tu cherches dans tes archives et tu colles dans le brief :

| Type de matière | Source | Pourquoi |
|---|---|---|
| Donnée chiffrée propriétaire | CRM, dashboard interne, étude commandée | Grounding factuel non-copiable |
| Verbatim client | Calls clients, emails, témoignages | Langage réel du marché |
| Cas client | Projets passés, études internes, dataset 6 ans | Preuve, pas opinion |
| Entité technique précise | NLP sur la requête, base de connaissance | Vecteur sémantique aligné |
| Donnée terrain Reddit / Grok | Prompts Reddit, Grok mode expert | Micro-intentions invisibles dans la SERP |

Règle simple : un H2 sans matière propriétaire = un H2 sur lequel tu vas écrire de la commodité. Tu reviens à tes archives, tu trouves la matière, tu colles dans le brief sous le H2 concerné. Si rien ne sort, tu remets le H2 lui-même en question.

À la fin de cette étape, ton brief ressemble plus à un dossier de presse qu'à un sommaire. C'est le signe que l'étape 2 est bien faite.

### Étape 3 · Ajouter tes idées perso dans le brief

La data objective est en place. Maintenant tu ajoutes ta couche subjective : tes inversions, tes positions tranchées, ton point de vue éditorial. Cette étape, personne ne peut la faire à ta place.

Plus tu mets de toi dans le brief, plus l'article aura une voix qui ne ressemble à personne. C'est ici que ton ton de voix entre dans l'article avant même que Claude écrive un mot.

Pour chaque H2, tu te poses 3 questions :
1. Quelle position tranchée j'ai sur ce sous-sujet, que les autres n'osent pas formuler ?
2. Quelle inversion experte je peux poser (le consensus dit X, ma data dit Y) ?
3. Quel exemple concret je peux raconter ici (1 client, 1 cas vécu, 1 chiffre interne) ?

Tu colles les réponses dans le brief, sous le H2 concerné. Pas en bloc séparé. Dans le brief, au bon endroit, pour que Claude les voie au moment où il rédige cette section précise.

Garde-fou : si tu n'as pas d'opinion tranchée sur un H2, c'est probablement que ce H2 ne devrait pas exister sur cette page. Tu le retires, ou tu le délègues à un satellite que tu écriras plus tard. Mieux vaut une page courte avec une voix, qu'une page longue qui dilue.

### Étape 4 · Lancer le workflow rédaction · arrêter à 50%

Le brief est complet : structure Hn validée, data propriétaire injectée par H2, idées perso ajoutées section par section. Tu lances le skill rédaction reçu mercredi, en joignant le doc complémentaire fourni avec et le worksheet ton de voix rempli, **dans la même conversation Claude que le brief**.

Tu lances. Mais tu ne laisses PAS Claude finir l'article d'un coup.

Tu arrêtes à 40-50%. Sur un article cible 2000-2500 mots, tu arrêtes à 1000-1200 mots.

Pourquoi la règle des 50% :
- Le LLM dérive après ~1000 mots. Il retombe dans son corpus moyen, recycle ses tournures, perd ton ton de voix.
- Plus tu laisses écrire d'un coup, plus la dérive s'accumule sans contrôle.
- Tu veux vérifier que les fondations tiennent avant de bâtir le reste.
- Tu veux fact-checker la matière déjà produite avant que d'éventuelles hallucinations contaminent les 50% suivants.

Sur ces 1000-1200 premiers mots, tu relis avec 4 questions :
1. Le ton de voix tient-il ? (compare avec ton worksheet)
2. Le Surprise Gap est-il visible dans les 300 premiers mots ?
3. Y a-t-il un tic LLM qui s'est glissé (jargon creux, méta-intro, faux enthousiasme) ?
4. La data propriétaire et les idées perso injectées à l'étape 2 et 3 sont-elles effectivement présentes ?

Si non à l'un des quatre, tu reprends ici, avant d'aller plus loin. Pas après.

### Étape 5 · Fact-check Perplexity, puis finir l'article

Tu prends le morceau de 1000-1200 mots produit à l'étape 4 et tu le donnes à Perplexity (ou Grok) pour fact-check.

Prompt à coller :

```
Rôle : Spécialiste du Fact-Checking et de la consolidation de l'autorité du contenu.

Objectif : Intégrer des sources précises (URL) ou des chiffres vérifiés directement dans le texte d'origine, là où l'affirmation est la plus forte et nécessite une preuve factuelle immédiate.

Ressources fournies :
Le Texte à Modifier : ([Insérer ici le texte complet d'origine])

Raisonnement : Pensez étape par étape à l'endroit optimal de chaque ajout de source/chiffre dans le texte.

Consignes d'intégration :
Placement : Placez chaque source (URL) ou chaque chiffre là où il apporte le plus de crédibilité ou de précision à l'affirmation la plus proche.
Formatage Strict : Vous devez encadrer uniquement l'ajout (le chiffre ou l'URL) par des guillemets doubles français : « [Chiffre ou URL] ».
Priorité : Donnez la priorité aux chiffres précis ou aux URL des sources primaires qui valident des faits spécifiques.
```

Pourquoi maintenant, pas à la fin de la rédaction :
- Détecter une hallucination à 1000 mots évite d'en bâtir 1500 de plus sur des fondations fausses
- Les sources injectées par Perplexity / Grok deviennent une matière supplémentaire pour la suite
- Tu réinjectes le morceau fact-checké à Claude avant qu'il continue, il s'appuie dessus pour la deuxième moitié

Perplexity vs Grok :

| Tu utilises | Quand |
|---|---|
| Perplexity | Sujets institutionnels, études académiques, rapports officiels, données macro |
| Grok | Sujets terrain, débats récents X, retours pratiques, signaux émergents |
| Les deux en parallèle | Sujet complexe ou polarisé, tu croises les outputs |

Garde-fou absolu : tu vérifies manuellement chaque source. Hallucinations possibles. Une URL morte ou un chiffre inventé tue plus de crédibilité qu'il n'en apporte. Tu ouvres, tu vérifies, si le doute persiste tu retires.

**Finir l'article.** Tu reviens à Claude (toujours la même conversation). Tu lui donnes le morceau fact-checké avec ses sources « » et la consigne : "termine l'article en respectant la structure Hn, en gardant le même ton, en utilisant les sources fact-checkées comme matière, et sans répéter ce qui a déjà été dit". Tu laisses produire les 50% restants, et tu relis avec la même grille des 4 questions qu'à l'étape 4.

Vérifications finales avant de considérer l'article comme livré :
- **Passage ancré** présent dans les 300 premiers mots (150-200 mots auto-suffisants, extractible Featured Snippet)
- **Bloc d'authorship** (~50 mots) à la fin ou dans une zone extractible, conçu pour Position 0 / AI Overview
- **FAQ stratégique** en bas de page (micro-intentions long-tail)
- **Ton de voix tenu** sur l'ensemble, pas juste le début
- **Mots interdits absents** (relire avec ta liste noire du worksheet)

Article livré. On passe au scoring.

---

## 3 · Le scoring · `opendecoder-seo-scoring-system`

Le scoring n'est pas une affaire d'intuition. On a un système propriétaire calqué sur le paper OpenDecoder (Mo et al., 2026) : `opendecoder-seo-scoring-system`. Quatre scores qui s'agrègent en une note sur 100, et un principe central : la pertinence domine, trois bonus la complètent. C'est la "règle des 3" : 1 score dominant (S_Pertinence) + 3 scores bonus (S_Qualite, S_Potentiel, S_AEO) qui s'ajoutent à coefficient 0.5.

Cadrage pour le call : on ne déroule pas les 19 sous-prompts en live. On donne l'architecture, on montre la formule, on montre comment lire le verdict, on montre comment prioriser. Les participants lanceront le skill complet en autonomie après le call, sur leur article de la semaine.

### Formule d'agrégation

```
S_final = S_Pertinence + 0.5 × (S_Qualite + S_Potentiel + S_AEO)
S_100 = (S_final / 2.5) × 100
```

S_Pertinence porte la base (coefficient 1). Les 3 autres ajoutent du bonus (coefficient 0.5 chacun). Un article peut être impeccable côté éditorial, IA ou marché, mais si la pertinence est faible, le score plafonne. À l'inverse, une pertinence forte ne suffit pas : un contenu pertinent mais creux ne dépassera pas 60.

### Score 1 · S_Pertinence · dominant

Mesure : alignement sémantique entre la page et l'intention de recherche. Équivalent du Retriever Score d'OpenDecoder.

Quatre sous-scores :
- Couverture entités (40%) : primaires, secondaires, tertiaires détectées par requête LLM
- Alignement intention (25%) : Know-Simple / Know / Do / Commercial croisé avec le format de contenu
- Couverture champ sémantique (25%) : clusters thématiques attendus traités en profondeur, bonus Hn
- Signaux on-page (10%) : mot-clé dans H1, 100 premiers mots, H2, URL, meta

C'est le score qu'on regarde en premier. En dessous de 0.65, on ne publie pas, on retravaille la sémantique avant de juger le reste.

### Score 2 · S_Qualite · bonus

Mesure : qualité éditoriale intrinsèque, jugée par LLM en mode Quality Rater. Équivalent du LLM Ranking Score.

Quatre sous-scores :
- E-E-A-T (35%) : Experience, Expertise, Autorité, Confiance, Données, chacun noté 0 / 0.5 / 1
- Profondeur (30%) : couverture des clusters à fond + insights uniques détectés
- Structure (20%) : hiérarchie Hn, passage-rankabilité, opportunité Featured Snippet, éléments visuels
- Lisibilité (15%) : longueur des paragraphes, rythme, transitions, actionnabilité

C'est ici que ton ton de voix, ta data propriétaire et tes inversions des étapes 2 et 3 du workflow rédaction sont scorés.

### Score 3 · S_Potentiel · bonus

Mesure : capacité de la page à performer face à la SERP estimée et à l'effort déjà engagé. Équivalent du Query Performance Prediction d'OpenDecoder.

Quatre sous-scores :
- Paysage concurrentiel estimé (30%) : % de résultats faibles dans le top 10, malus YMYL -0.1
- Complétude des formats (30%) : tableau, FAQ, comparatif, checklist, attendus par l'intention
- Signaux d'opportunité (25%) : sujet en évolution, format différenciant, angle inexploité, avantage E-E-A-T
- Position actuelle (15%) : donnée GSC si disponible, sinon neutre 0.5

C'est le score qui te dit si l'effort de rédaction va effectivement convertir en visibilité.

### Score 4 · S_AEO · bonus

Mesure : survie face aux moteurs IA (SGE, SearchGPT, Perplexity, AI Overview). Extension du framework, source GEO Sentinel v2.1.

Quatre sous-scores :
- Surprise (25%) : éléments Haute Surprise qu'une IA ne peut pas inventer
- Grounding Density (30%) : densité de preuves atomiques par 100 mots
- RAG Structurer (25%) : extractibilité par un système RAG (proximité titre/réponse, sections autonomes, données structurées, format Q&A)
- Freshness Guard (20%) : année dans le titre, sources datées, signal de mise à jour, absence d'obsolescence

C'est le score qui te dit si ta page sera citée par les LLMs ou paraphrasée à ta place.

### Grille de décision finale

| Score /100 | Verdict | Décision |
|---|---|---|
| 85-100 | Excellent | Prêt à performer en SEO et AEO. Monitoring. |
| 70-84 | Bon | 1-2 axes d'amélioration ciblés. Quick wins probables. |
| 50-69 | Moyen | Retravail nécessaire. Prioriser la dimension la plus faible. |
| 30-49 | Faible | Refonte significative ou pivot stratégique. |
| 0-29 | Critique | Le contenu ne répond pas à l'intention. Recommencer. |

### Règle de priorisation

Une fois les 4 scores en main, tu travailles d'abord la dimension la plus faible. C'est l'inverse d'OpenDecoder côté inference (qui priorise les documents les mieux scorés). Côté optimisation, le ROI marginal est sur le maillon faible.

Deux exceptions stratégiques :
- Si S_Potentiel < 0.25, tu questionnes la pertinence stratégique du sujet avant tout. Peut-être que cette requête ne vaut pas l'effort.
- Si S_AEO < 0.30, la page est invisible pour les IA. Priorité absolue si la stratégie GEO est en jeu.

### Livrable scoring

À la sortie, tu dois pouvoir énoncer 2 axes d'amélioration concrets, formulés au niveau du sous-score, pas du score global. Du précis :
- "S_ent à 0.55 : ajouter les entités secondaires sur la garantie et l'autonomie dans le H2 pricing"
- "S_surprise à 0.25 : injecter le verbatim client du cas Lyon dans le H2 sur l'intégration"
- "S_format à 0.40 : ajouter le tableau comparatif neuf / reconditionné absent aujourd'hui"

Ces 2 axes alimentent la v2 de l'article. Ils alimentent aussi ton Claude au fil du temps : plus tu scores, plus il apprend ce qui marche chez toi.

---

## 4 · Les modèles de page · scaler le système

Tu sais produire UN bon article qui passe le scoring. Question suivante : comment passer à 100 articles, à 500 pages, sans tomber dans la moulinette à thin content que Google a sanctionnée depuis le Helpful Content Update et que les moteurs IA continuent de filtrer.

La réponse, c'est le **modèle de page**. Pas un template creux où on change juste le nom de la ville, mais une architecture éditoriale qui branche une base de données propriétaire et génère des pages uniques, utiles, denses en valeur réelle. C'est le terrain du Programmatic SEO version 2026.

Le principe en une ligne :

```
Template (fixe) + Variable (base de données) = N pages organiques uniques
```

Skill associé qu'on lance en autonomie après le call : `seo-programmatique-pseo`. Le call sert à donner la grille de lecture, pas à dérouler le skill en live.

### Les 3 couches d'un bon modèle de page

**Couche 1 · Base de données structurée propriétaire.** Pas un fichier Excel bâclé. Une source de vérité avec champs typés : variables principales, attributs secondaires, preuves chiffrées, exemples sectoriels, limites, cas d'usage. Airtable, Notion, Supabase, peu importe le support tant que la donnée est propre et propriétaire. Si tes données viennent d'un scrap public, ton modèle est copiable, donc commodité.

**Couche 2 · Logique conditionnelle.** Le contenu change selon les valeurs des variables, pas seulement leur affichage. Un paragraphe si le prospect est PME, un autre si c'est ETI. Un bloc technique si le cas d'usage demande de l'API, un autre si c'est no-code. Sans cette ramification, ta page 12 est la même que ta page 1 avec un mot changé. Google le voit, les LLMs ne te citent pas.

**Couche 3 · Couche éditoriale humaine ou IA supervisée.** Exemples nommés, anecdotes datées, données chiffrées réelles, captures d'écran, témoignages. C'est ce qui empêche la page d'être une copie lexicale de sa voisine et en fait une ressource à part entière. Si tu fais 100% IA non supervisée sur les 3 couches, tu produis du contenu IA générique, Google et SearchGPT le sanctionnent.

### Pipeline en 5 étapes du skill `seo-programmatique-pseo`

1. **Identifier les modèles scalables** (minimum 5). Pour chaque modèle : architecture (pattern URL + head term + modificateur + nombre de pages possibles + source de données), template de page (H1 avec variable, sections, CTA, Schema.org), SEO et intent (phase funnel, intention, 10 exemples de requêtes, compétition), avantage compétitif (ce que les concurrents ne peuvent pas copier).
2. **Matrice de priorisation** : pages possibles × effort × impact SEO × potentiel conversion × données disponibles.
3. **Mots-clés par modèle** : 10 à 15 longues traînes par modèle, avec intention, phase funnel, niveau de compétition.
4. **Plan d'exécution 90 jours** : semaine par semaine, avec prérequis techniques (data prête, template codé, indexation surveillée).
5. **Résumé exécutif** : 5 phrases qui posent la priorité et le modèle #1 à lancer en premier.

### Les 7 règles non-négociables du pSEO 2026

Ces 7 règles séparent un pSEO qui ranke d'un pSEO qui se fait punir par Google ou ignorer par les LLMs.

1. **Anti-thin content** : chaque variable change le contenu réel, pas juste le H1. Maximum 30% de texte identique entre deux pages du même modèle.
2. **Données terrain** : zéro hallucination, zéro chiffre inventé. Si tu n'as pas la donnée, tu mets `[DONNÉE À SOURCER]` et tu n'avances pas avant qu'elle soit comblée.
3. **Sourcing obligatoire** : chaque chiffre cité = source + organisme + année. Sans ça, ton Grounding Score chute.
4. **Canonical propre** : une URL = un contenu = une canonical. Si deux variables produisent le même contenu, tu fusionnes.
5. **Maillage différenciant** : chaque page pointe vers un ensemble différent de pages internes, pas le même bloc footer dupliqué N fois.
6. **Surprise Score** : au moins 1 élément Haute Surprise par section (data propriétaire, inversion experte, exemple unique).
7. **Grounding Score** : 1 passage ancré 150-200 mots extractible Featured Snippet + 1 bloc authorship ~50 mots extractible Position 0 / AI Overview, sur chaque page générée.

Le scoring `opendecoder-seo-scoring-system` s'applique à chaque page programmatique. Une page pSEO est une page comme une autre côté qualité, elle passe par les 4 scores et le S_100.

### Modèles qui marchent en B2B

Six modèles éprouvés. Volumes indicatifs, à confirmer avec la GSC du client ou Keyword Planner :

| Modèle | Pattern d'URL | Volume long-tail typique | Intention | Data nécessaire |
|---|---|---|---|---|
| Comparatif | `/[outil-A]-vs-[outil-B]` | 50-500/mois par paire | Know + Do | Spécifications, prix, cas d'usage des deux outils |
| Tarifs | `/tarifs-[outil]` | 100-1000/mois | Do | Pricing détaillé, paliers, conditions, comparaison rapport qualité-prix |
| Outil pour secteur | `/[outil]-pour-[secteur]` | 30-300/mois | Know + Do | Cas clients du secteur, vocabulaire métier, contraintes réglementaires |
| Comment faire X avec Y | `/comment-[tâche]-avec-[outil]` | 50-500/mois | Know | Tutoriels pas-à-pas, captures, étapes vérifiées |
| Avis | `/[outil]-avis` | 200-2000/mois | Know + Do | Avis client réels, scoring objectif, points forts et faibles |
| Alternative | `/alternative-[outil]` | 100-1500/mois | Do | Liste d'alternatives, comparatif, USP par alternative |

Pour chaque modèle, l'avantage compétitif réel = ta data propriétaire. Sans cas clients documentés sur "outil pour le BTP", tu ne pourras pas écrire de page "outil pour le BTP" qui ne soit pas générique.

### Variantes selon le type de site

- **Site avec offre produit ou service** (e-commerce, SaaS, agence) : variante "produit/service" du skill, qui priorise le CTA conversion et le maillage cross-sell vers les pages business.
- **Site média, éditorial, communautaire** (sans offre directe) : variante "non-produit" du skill, qui ajoute en **Étape 0 obligatoire un Test de Substitution LLM**. La question à se poser : si je colle ce contenu dans ChatGPT et que je lui demande de le résumer, est-ce que la valeur survit ? Si l'IA produit pareil ou mieux sans ta page, le modèle est faux dès le départ et il ne survivra pas à 6 mois de SearchGPT et d'AI Overview.

### Critères de priorisation d'un modèle

Avant de lancer un modèle, on l'évalue sur 4 axes :

1. **Volume total estimé** : somme des volumes longue traîne de toutes les pages générables. Un modèle à 30 pages × 200/mois est souvent meilleur qu'un modèle à 5 pages × 1000/mois, parce que la cannibalisation interne est plus faible.
2. **Effort de création** : combien de données uniques par page ? Plus la couche éditoriale est dense, plus l'effort par page est élevé, mais plus le modèle est défensible.
3. **Compétition SERP** : qui est déjà positionné sur ces requêtes ? Si Google domine avec ses propres SERP features (cartes, comparatif natif, AI Overview), le ROI chute brutalement.
4. **Potentiel conversion** : la page mène-t-elle à une action business identifiée ? Sans CTA vers une offre, le modèle alimente du trafic qui ne convertit pas et finit en dette technique.

Règle absolue : pas deux modèles sur le même angle (anti-cannibalisation). Le modèle "alternative-[outil]" et le modèle "[outil]-vs-[concurrent]" peuvent se cannibaliser, à designer ensemble dès le départ pour différencier l'intention et le maillage.

### Garde-fous absolus avant de scaler

Si tu peux générer la page automatiquement sans donnée propriétaire ni couche éditoriale, **ne la fais pas**. Le pSEO de mauvaise qualité a tué des sites entiers depuis 2022. Une page doit apporter une valeur unique réelle, sinon Google sanctionne le domaine entier (Helpful Content Update, Spam Update successifs).

Trois étapes non-négociables avant de lancer la production massive :

1. **5 pages manuelles avant de scaler.** Tu produis 5 pages à la main, intégralement, en suivant le template. Tu vérifies qu'elles tiennent debout, qu'elles n'ont pas l'air dupliquées, qu'elles rankent ou commencent à s'indexer dans les 3 semaines. Si oui, tu scales. Si non, le modèle est faux et tu reprends le template avant de produire la page 6.
2. **Indexation gate.** Avant de pousser les 100 pages suivantes, tu vérifies l'indexation des 5 premières via la GSC. Si seulement 2 sur 5 sont indexées sous 3 semaines, le signal de qualité envoyé à Google est insuffisant. Tu retravailles le template avant de produire en masse.
3. **Scoring sur les 5 premières.** Chaque page passe par `opendecoder-seo-scoring-system`. S_100 sous 65 sur l'une des 5 = le template est faiblard, à reprendre avant de scaler. Tu attaques en priorité la dimension la plus basse (S_Pertinence ou S_AEO en général sur les modèles pSEO).

Le but n'est pas de produire vite. Le but est de produire UN modèle qui produit lentement, mais bien, et qui transforme ton site en système qui compose tout seul. Une fois le modèle validé, tu peux pousser 50 nouvelles pages par mois sans toucher au template, juste en ajoutant des lignes à ta base de données propriétaire.

---

## 5 · Ce que les participants amènent au call

Pour que le call ne soit pas une conférence à sens unique, chacun arrive avec :
- Son article produit cette semaine (brut + fact-checké)
- Ses 4 scores via `opendecoder-seo-scoring-system` : S_Pertinence + S_Qualite + S_Potentiel + S_AEO, et le S_100 agrégé
- Ses 2 axes d'amélioration identifiés sur la dimension la plus faible
- 1 question concrète sur laquelle il bloque

Format de la session de 70 min :
- 5 min · Cadrage du contexte (rappel : contexte = matière première)
- 25 min · Méthode rédaction · 5 étapes (avec démo live sur 1 cas)
- 10 min · Scoring sur 1 cas participant en live
- 15 min · Modèles de page (théorie + 2 exemples B2B concrets)
- 15 min · Q&R et patterns d'erreur observés sur la semaine

---

## Notes pour Tim (interne)

- **Risque #1** : sauter le contexte pour aller vite à la démo workflow. Tenir 5 min sur le contexte est non-négociable, c'est le levier #1 de qualité de sortie.
- **Risque #2** : les participants vont vouloir tout faire en un seul prompt. La règle des 50% est contre-intuitive, insister avec un avant/après visuel pendant la démo. Le message bootcamp de mercredi annonçait déjà "ne le laissez pas rédiger 100%", donc le call doit livrer la méthode concrète qui explique le pourquoi et le comment.
- **Risque #3** : les participants vont ouvrir une nouvelle conversation Claude pour chaque article ou chaque tâche. Insister sur la règle "une seule conversation par projet". Montrer en live ce qui se passe quand on perd le contexte (régénération à zéro, ton de voix qui dérive).
- **Démo live** : préparer un brief enrichi et lancer la rédaction en partage d'écran, arrêter à 50%, montrer la dérive si on continue, montrer le fact-check Grok en parallèle.
- **Cas pratique modèles de page** : sortir 2 exemples concrets de la base Organikk ou des comptes coachés (anonymisés). Les participants doivent voir une page programmatique de qualité vs une page programmatique creuse côte à côte.
- **Validation post-call** : demander à chacun de publier la v1 de son article cette semaine, avec un follow-up score à J+7 pour mesurer le delta.
- **Transition vers semaine 3** : annoncer que la semaine prochaine on attaque le maillage interne + la mesure (GSC, scoring de cohorte). Les modèles de page de cette semaine deviennent les piliers de la prochaine architecture.
