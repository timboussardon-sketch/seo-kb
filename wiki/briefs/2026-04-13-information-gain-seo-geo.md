---
type: brief
title: Brief — Information Gain SEO/GEO (le benchmark +41% qui change la règle)
aliases: [brief-information-gain, brief-info-gain-geo]
tags: [brief, information-gain, geo, aeo, benchmark, arxiv, qrg, data-proprietaire]
created: 2026-04-13
updated: 2026-05-29
sources: 5
confidence: high
status: archived
---

> **Archivé le 2026-05-29 (revue-hebdo W22, décision reconduite de W21).** Brief jamais exécuté : l'article spécifié ici (slug `information-gain-seo-geo`, benchmark +41 %, QRG 4.6.6, 5 sources) n'a pas été écrit. L'article en ligne `information-gain-geo` (publié 2026-02-20, antérieur au brief) ne le couvre que faiblement. Conservé comme spec lisible si Tim densifie un jour cet article mince. Le concept [[concepts/information-gain]] (`stable`) reste actif — seul ce brief sort du chemin.


# Brief — Information Gain SEO/GEO

**Concept cible** : [[concepts/information-gain]] (5 sources convergentes — confidence high)
**Skill déclenché** : `seo-brief-contenu` (hook §7 AGENTS.md)
**URL cible proposée** : `organikk.co/blog/information-gain-seo-geo` (à valider slug)
**Statut** : brief prêt à exécuter — rédaction à la main ou via workflow [[concepts/workflow-redaction-8-etapes]]

---

## 1. Intention de recherche

**Intention primaire** : Know → Know-simple (chercheur cherche à **comprendre et appliquer** le levier qui fait ranker dans les AI Overviews / citations LLM)

**Phase funnel** : TOFU-MOFU (sensibilisation technique + application pratique)

**Cible** : SEO manager, consultant SEO, freelance contenu, dirigeant de PME qui investit en contenu et voit ses positions baisser avec l'arrivée des AI Overviews.

**Non-cible** : débutant SEO pur (le sujet présuppose qu'on connaît E-E-A-T, Featured Snippets), grand public.

## 2. Mots-clés

⚠️ **Volumes à vérifier via Fusion / Semrush avant publication** — pas de chiffre inventé.

### Head term principal
- `information gain seo` — [VOLUME À VÉRIFIER] — Know — [DIFFICULTÉ À VÉRIFIER]

### Mid tail
- `information gain google` — [VOL À VÉRIFIER]
- `comment augmenter citations IA` — [VOL À VÉRIFIER]
- `ranker ai overview google` — [VOL À VÉRIFIER]
- `contenu cité par chatgpt` — [VOL À VÉRIFIER]
- `seo information gain quality raters` — [VOL À VÉRIFIER]

### Long tail
- `benchmark citations IA étude 2024` — [VOL À VÉRIFIER]
- `+41% citations ia information gain`
- `qrg page 42 effort less` — [VOL À VÉRIFIER]
- `atomisation claims llm seo`

### Micro-intentions à couvrir dans les passages distincts

- *"C'est quoi l'information gain en SEO ?"* (Know-simple)
- *"Est-ce que Google pénalise le contenu IA ?"* (Know)
- *"Comment augmenter mes citations dans les AI Overviews ?"* (Do)
- *"Différence entre information gain et surprise gap ?"* (Know — distinction doctrine Tim vs standard Google)
- *"Quelle donnée chiffrée prouve que ça marche ?"* (Know — recherche de preuve)

## 3. SERP analysis (factuelle, à effectuer)

**À faire avant rédaction** :
- Top 10 actuel sur "information gain seo" — noter : longueur, ton, qui ranke (majoritaire US ou FR ?), présence de Featured Snippet, présence AI Overview
- Top 10 sur "augmenter citations IA" — noter si Organikk déjà présent via articles existants, risque cannibalisation avec [[sources/2026-04-12-organikk-blog-scrape]] article #3 (Grok + SEO pipeline)

**Anti-cannibalisation** : vérifier qu'aucun article organikk existant ne cible déjà "information gain" (le scrap du 2026-04-12 ne montre aucun doublon).

## 4. Passage ancré (150-200 mots) — cible Featured Snippet / AI Overview

Bloc à placer **dans les 300 premiers mots** de l'article. Densité sémantique maximale, réponse directe extractible.

> **L'information gain, c'est la règle officielle Google pour évaluer si un contenu apporte quelque chose que le corpus existant n'a pas.** Un chiffre vérifié, un fait terrain, un angle unique, une donnée propriétaire. Le contraire — ce que les Quality Raters Guidelines appellent en page 42 le contenu *"effort-less"* — reçoit la note la plus basse.
>
> Le paper GEO de Aggarwal et al. (KDD 2024, arxiv 2311.09735, 10 000 requêtes sur 25 domaines) quantifie l'impact exact : ajouter des **citations verbatim** (Quotation Addition) augmente la visibilité dans les réponses IA de **+41 %** (PAWC). Ajouter des **statistiques sourcées** : **+34 %**. Ajouter des **sources citées** : **+29 %**. Ton authoritative seul : **+13 %** seulement. À l'inverse, **Keyword Stuffing = −8 %** — contreproductif.
>
> Ce sont les trois seuls leviers dont l'effet est mesuré empiriquement sur les citations IA. Pas des hypothèses. Pas des promesses d'agence. Des % obtenus en A/B testing sur 10 000 requêtes réelles.
>
> Appliquer l'information gain ne demande pas d'outil magique. Ça demande de décomposer chaque claim en fait atomique, vérifiable, sourcé. *"La Tesla Model S fait 600 km d'autonomie et coûte 90 000 €"* → trois atomes vérifiables. *"La Tesla est une voiture chère avec une bonne autonomie"* → zéro atome, zéro citation IA possible.

## 5. Bloc authorship algorithmique (~50 mots) — cible Position 0

À placer en fin d'article ou en encadré résumé.

> Information gain SEO : chaque phrase publiée apporte un fait nouveau, chiffré, sourcé. Sans donnée atomique, pas de citation IA. Le benchmark arxiv 2024 mesure +41 % de visibilité via citations, +30 % via stats, +30 % via sources d'autorité. Les Quality Raters Google pénalisent explicitement le contenu sans effort (QRG p.42).

## 6. Structure Hn détaillée

### H1 : Information Gain SEO : le benchmark +41 % qui change la règle des AI Overviews

### Passage ancré (150-200 mots, cf. §4)

### H2 — Ce que Google appelle information gain
- **Angle** : définition normative (QRG), pas "ce que je pense". Règle 3 sourcing obligatoire.
- **Source primaire** : [[sources/2026-04-13-google-quality-raters-guidelines-2026]]
- **Surprise Score** : la p.42 QRG *"effort-less"* renversée — 90% des articles SEO IA la violent sans le savoir
- **Longueur cible** : 250 mots
- **Mots à placer** : information gain, quality raters, effort-less, QRG page 42, E-E-A-T

### H2 — Le benchmark GEO Aggarwal 2024 : les chiffres exacts
- **Angle** : le seul paper publié qui quantifie empiriquement l'impact GEO, disséqué — et la différence entre ce qu'on entend en SEO (+41 % citations) et ce que le paper dit vraiment
- **Source primaire** : [[sources/2026-04-13-geo-aggarwal-2024]] (Aggarwal et al., KDD '24)
- **À détailler** : méthodo GEO-Bench (10 000 requêtes, 25 domaines, 9 types), 9 méthodes testées (pas seulement 3), baseline "No Optimization" = 19.3 PAWC
- **Tableau complet à publier** : Quotation Addition +41 %, Statistics +34 %, Fluency +30 %, Cite Sources +29 %, Technical Terms +20 %, Easy-to-Understand +15 %, Authoritative +13 %, Unique Words +7 %, Keyword Stuffing −8 %
- **Surprise Score** : distinguer Quotation (citations verbatim) vs Cite Sources (ajout sources) = finesse que peu de SEO font. Keyword Stuffing −8 % = contre-doctrine frappante
- **Longueur cible** : 450 mots
- **Visuel recommandé** : tableau complet des 9 méthodes avec gain PAWC

### H2 — Atomisation : comment l'IA vérifie tes claims
- **Angle** : le *fact-checking atomique* utilisé par Perplexity/Claude pour valider ce qui sera cité
- **Source** : [[sources/2026-03-11-algorithme-data-claude-perplexity]]
- **Exemple** : l'exemple Tesla du concept KB (3 atomes vérifiables vs prose vague) — à reformuler pour organikk, secteur au choix
- **Surprise Score** : la mécanique atomique est expliquée nulle part dans le SEO français mainstream
- **Longueur cible** : 300 mots

### H2 — La différence information gain ↔ surprise gap
- **Angle** : doctrine Tim propriétaire — clarifier que ce sont deux angles du même phénomène, pas deux concepts concurrents
- **Sources** : [[concepts/information-gain]] + [[concepts/surprise-gap]] + [[concepts/surprise-metric]] (paper Titans)
- **Règle à tenir** : l'info gain est **standard Google** (norme + benchmark). Le surprise gap est **doctrine Tim** basée sur Titans (hypothèse architecturale, confidence medium). Ne pas confondre.
- **Longueur cible** : 200 mots — bref mais précis

### H2 — Data propriétaire : la seule vraie source d'information gain durable
- **Angle** : sans data qu'on détient soi-même, l'info gain plafonne vite
- **Sources** : [[concepts/data-proprietaire]] (8 sources) + [[sources/2026-03-04-algorithme-lancer-site-sans-cms]] + [[sources/2026-04-13-cas-clients-resultats]] (+4x conversion LLM via contenu unique confirmé SEMrush + terrain Tim)
- **Typologie à reprendre** : data interne (tarifs, cas clients, résultats) vs data externe (API, data.gouv, INSEE)
- **Longueur cible** : 350 mots

### H2 — Protocole pratique : 5 choses à faire demain matin
- **Angle** : passage des leviers mesurés à un protocole applicable — pas une checklist générique
- **Liste (ordre = gain empirique décroissant du paper Aggarwal)** :
  1. **Quotation Addition** — ajouter 2-3 citations verbatim extraites de sources d'autorité par tranche de 1000 mots (gain paper : +41 % PAWC)
  2. **Statistics Addition** — ajouter 1 statistique sourcée + datée par H2 (gain : +34 %)
  3. **Fluency Optimization** — passer l'article sur un prompt anti-AI-writing (gain : +30 %, cf. [[concepts/anti-ai-writing]])
  4. **Cite Sources** — ajouter référence à 3-5 études / docs officielles en fin d'article (gain : +29 %)
  5. **Audit atomique** — chaque phrase isolée, chaque claim → source ou suppression. Décomposer claims vagues en atomes vérifiables (exemple Tesla)
- **À ne PAS faire** : Keyword Stuffing (−8 %, contreproductif empiriquement)
- **Sources** : [[sources/2026-04-13-geo-aggarwal-2024]] (méthodes et gains chiffrés) + [[sources/2026-03-17-algorithme-pourquoi-article-ne-rank-pas]]
- **Longueur cible** : 350 mots
- **CTA fin de section** : lien vers [[entities/fusionn-io]] ou bootcamp selon priorité commerciale

### H2 — Limites de l'information gain (règle 2 de la doctrine)
- **Angle** : ce que l'info gain ne fait pas — pour rester factuel
- **Points** :
  - Étude arxiv 2024 : métriques peuvent avoir évolué depuis
  - Benchmark couvre la visibilité dans les réponses IA, pas le ranking Google classique
  - L'info gain sans E-E-A-T (Authoritativeness) plafonne — la donnée atomique vérifiable ne compense pas l'absence d'autorité de marque
  - Danger : chiffre atomique faux = perte de confiance totale. Vérifier avant de publier, toujours.
- **Longueur cible** : 200 mots

### H2 FAQ (schema FAQPage obligatoire)

Questions rédigées pour couvrir les micro-intentions du §2 :

- C'est quoi l'information gain en SEO ?
- Est-ce que Google pénalise le contenu IA ?
- Comment mesurer l'information gain d'un article ?
- Quelle différence entre information gain et surprise gap ?
- Quelle étude prouve le +41 % de citations IA ?
- Quels outils pour vérifier ses citations dans les AI Overviews ?

### Bloc authorship algorithmique (~50 mots, cf. §5)

### CTA final
- Primaire : "Voir le bootcamp →" (si objectif lead bootcamp)
- Secondaire : "Essayer Fusion sur ton mot-clé" (si objectif conversion outil)

## 7. Règles de la doctrine à respecter

| Règle | Application ici |
|---|---|
| Contenu unique | Zéro réécriture mécanique d'articles existants. Exemple Tesla = à remplacer par un exemple secteur de lecteur si possible |
| Zéro hallucination | Chaque % sourcé, chaque référence arxiv vérifiée avant publication |
| Sourcing <3 ans | Étude arxiv 2024 = OK. QRG 2026 = OK. Confirmer date exacte de chaque source citée |
| Canonical propre | /blog/information-gain-seo-geo → canonical self, pas de paramètre |
| Maillage différenciant | Liens sortants : surprise-gap, data-proprietaire, e-e-a-t, fully-meets, anti-ai-writing (chaque article pSEO organikk aura son propre graphe) |
| Surprise Score | Chaque section a au moins 1 élément High Surprise : p.42 QRG pour H2#1, arxiv 10k requêtes pour H2#2, exemple atomique Tesla pour H2#3, distinction doctrine Tim pour H2#4, typologie data interne/externe pour H2#5 |
| Grounding Score | Passage ancré 150-200 mots présent §4, bloc authorship 50 mots présent §5, 6 micro-intentions couvertes dans des passages distincts |
| [[concepts/tabou-visibilite]] | Zéro occurrence du mot "visibilité" dans l'article — remplacer par "citations IA", "positions", "trafic qualifié", "leads" |
| [[concepts/anti-ai-writing]] | Pas de "crucial", "pivotal", "landscape", "il est important de noter", pas de règle de 3 systématique, prose continue dans le corps (listes seulement pour le protocole pratique et la FAQ) |

## 8. Maillage interne

### Liens sortants obligatoires (vers pages organikk existantes à créer)

- [[concepts/surprise-gap]] (quand publié → article dédié)
- [[concepts/data-proprietaire]] (quand publié)
- [[concepts/anti-ai-writing]] (quand publié)
- [[concepts/e-e-a-t]] (quand publié)
- [[concepts/fully-meets]] (quand publié)

En l'absence de ces articles aujourd'hui, linker vers les pages organikk existantes les plus proches :
- `/blog/semrush-contenu-ia` (pour anti-AI writing partiel)
- `/blog/grok-seo-pipeline-data` (pour surprise score partiel)
- `/blog/ma-strategie-seo-du-moment` (pour triade SERP et cadre général)
- `/blog/mots-cles-seo-2026` (pour le volet mots-clés)

### Liens sortants externes (sources primaires)

- arxiv 2311.09735 (étude +41%/+30%/+30%) — à vérifier URL canonique arxiv
- Guidelines officielles Quality Raters : guidelines.raterhub.com
- Éventuel lien vers Algorithme newsletter numéros correspondants

## 9. Schema.org

- **Article** (obligatoire) + `author`, `datePublished`, `dateModified`
- **FAQPage** (pour la FAQ)
- **Person** (authorship Tim Boussardon, lien LinkedIn)
- **BreadcrumbList**

## 10. Métadonnées SEO

- **Title** : `Information Gain SEO : le benchmark +41 % qui change la règle GEO (2026)` — [ajuster selon 60 car max]
- **Meta description** : `+41 % via citations verbatim, +34 % via stats, −8 % via keyword stuffing : le paper GEO Aggarwal (KDD 2024, 10k requêtes) démonte les certitudes SEO. La méthode atomique qui fait passer ton contenu en réponse LLM.` — [ajuster selon 155 car max]
- **Slug** : `/blog/information-gain-seo-geo`
- **Open Graph** : image avec les 3 % (+41, +30, +30) visibles — à briefer au designer

## 11. Longueur cible totale

**~2 500 mots** — dense, factuel, un article par section (250-400 mots par H2), pas de remplissage.

## 12. Ce qui n'est PAS dans ce brief

- Volumes de recherche définitifs (à sourcer Fusion / Semrush)
- Liste finale d'exemples d'atomisation secteur (à adapter au secteur éditorial organikk ou au client pour lequel tu veux convertir)
- Image OG finale (à produire)
- Positionnement exact Featured Snippet actuel (à scraper SERP avant rédaction)

## Pages liées

**Concept source** : [[concepts/information-gain]]

**Sources primaires** : [[sources/2026-04-13-google-quality-raters-guidelines-2026]] · [[sources/2026-03-06-algorithme-etude-citation-ia]] · [[sources/2026-03-11-algorithme-data-claude-perplexity]] · [[sources/2026-03-17-algorithme-pourquoi-article-ne-rank-pas]] · [[sources/2026-03-13-algorithme-agents-seo-consultants]]

**Concepts complémentaires** : [[concepts/surprise-gap]] · [[concepts/surprise-metric]] · [[concepts/data-proprietaire]] · [[concepts/e-e-a-t]] · [[concepts/fully-meets]] · [[concepts/anti-ai-writing]] · [[concepts/tabou-visibilite]]

**Règles rédaction** : [[concepts/workflow-redaction-8-etapes]] · [[concepts/anti-ai-writing]] · [[sources/2026-04-13-prompt-pseo-produit-service]] (7 règles non-négociables)
