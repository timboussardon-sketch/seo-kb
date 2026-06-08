---
type: source
source_type: strategie
title: "Golfiller, stratégie SEO (cas concret croisé à la doctrine)"
aliases: [golfiller-strat-source]
tags: [golfiller, pseo, product-led, do-vs-know, surprise-gap, information-gain, grounding-score, triade-serp, autorite-thematique, strategie]
created: 2026-06-01
updated: 2026-06-01
sources: 1
confidence: medium
status: draft
---

# Golfiller, stratégie SEO

Stratégie Golfiller croisée avec la doctrine Obsidian. Le cas concret (balles de golf d'occasion) sert d'illustration aux frameworks ; les frameworks expliquent **pourquoi** les moves fonctionnent. Log de travail brut séparé : [[golfiller-conversations]]. Version généralisée et réutilisable : [[ranker-verticale-niche-sans-backlink]].

## Objectif et contexte

[[entities/golfiller|Golfiller]] (golfiller.fr), e-commerce de balles de golf d'occasion / reconditionnées. Objectif : autorité thématique sur une verticale de niche défendable, les balles de golf d'occasion, plutôt qu'un affrontement frontal avec les gros acteurs. Résultat : première position sur "balle de golf", devant Décathlon et Amazon, sans acheter un seul lien.

État : projet pSEO actif sur les requêtes slope / handicap, base de ~40 parcours français (slope + SSS), calculateur de handicap interactif (formule FFGolf), page HTML sémantique brute (calculateur + tableau filtrable + sections par parcours). À venir : extension à ~100 parcours, Phase 2 pSEO (une URL par parcours) si la pilier performe.

## La stratégie lue à travers la doctrine

### 1. Triade SERP : à quelle phase chaque move agit
Le modèle [[triade-serp]] décompose la sélection d'un résultat. La strat Golfiller agit aux trois niveaux :
- **Phase 1, Document Ranking** : on ne vise pas le head term généraliste tenu par les gros (autorité de domaine qu'on n'a pas). On descend sur la verticale "balle de golf occasion" où le filtre d'admission est franchissable. C'est la condition d'entrée, sans elle rien ne compte.
- **Phase 2, Passage Ranking** : chaque page pSEO est construite pour que ses passages (blocs Hn de 150-200 mots) soient des vecteurs sémantiques denses, évalués individuellement. Un tableau ou une section de parcours = un passage qui peut ranker seul.
- **Phase générative (citation IA)** : c'est là que jouent le [[surprise-gap]] et l'[[information-gain]] (voir plus bas). Ranker ne suffit plus, il faut être **cité**.

### 2. Know-Simple / Know / Do : pourquoi le "Do" gagne
[[know-simple-know-do]] remplace TOFU/MOFU/BOFU. Les pages winners de Golfiller sont toutes des **"Do"** (calculer, consulter, comparer), pas des "Know" (lire). Raison doctrinale : une intention "Do" exige un **format** (outil, calculateur, tableau) qu'un LLM ne peut pas exécuter à la place de l'utilisateur sur la page. Les "Know" informationnels se font manger par les AI Overviews ; les "Do" résistent. C'est la traduction concrète de l'anti-ChatGPT. Les pages "Do" sont aussi les seules à viser le [[concepts/fully-meets|Fully Meets]] des Quality Raters.

### 3. Entités vectorielles + Grounding Score : comment construire la page
[[entites-vectorielles]] : chaque page se construit sur 4 catégories d'entités, pas une densité de mots-clés.
- **Entités techniques** : le vocabulaire obligatoire (slope, SSS, index, compression, carry…) qui fait passer la Phase 1.
- **Preuves quantitatives** : chiffres sourcés (data Trackman, PGA Tour, FFGolf) au format `chiffre + unité + contexte`. Elles montent le [[concepts/confidence-score]] de l'IA.
- **Vecteurs multimodaux** : le format attendu par une intention "Do". Un calculateur, un comparateur, un tableau filtrable. Une page "Do" sans outil a un vecteur **incomplet**. C'est exactement le Product-Led SEO.
- **Divergence (Haute Surprise)** : voir ci-dessous.

L'objectif n'est pas la proximité vectorielle maximale mais le [[grounding-score]] optimal = **proximité + divergence**. Ni hors-sujet, ni redondant avec ce que le modèle sait déjà.

### 4. Surprise Gap + Information Gain : ce qui fait mémoriser et citer
[[surprise-gap]] (thèse Tim) : apporter l'information manquante qui force le modèle à mettre à jour ses poids en temps réel pour inclure la marque dans sa réponse. Concrètement chez Golfiller, la Haute Surprise vient de la **data propriétaire agrégée des clients** (distances réelles par profil, données de compression croisées) et des **angles contrariens** ("une joueuse LPGA swingue comme un amateur homme mais envoie 40 yards plus loin", "Scheffler n°1 mondial mais 51e en vitesse").

C'est la version théorique (architecture Titans / [[surprise-metric]]) de ce que [[information-gain]] mesure côté Google : un contenu qui **ajoute ce que le corpus n'a pas** obtient la meilleure note ; un contenu "sans effort" qui recopie obtient la pire. Le benchmark GEO le chiffre : ajouter des citations verbatim sourcées = **+41 %** de visibilité (Quotation Addition), ajouter des statistiques = +34 %. Test de la Haute Surprise : si un concurrent recopie l'angle en 5 minutes, ce n'en est pas.

### 5. RRF + micro-intentions : couvrir toute la grappe
[[rrf]] : un cluster qui couvre **toutes les sous-intentions** d'un sujet améliore le score de fusion global, et la fraîcheur sémantique compte (un contenu nouveau à fort gradient de surprise l'emporte sur un ancien redondant). D'où la logique pSEO : une page pilier + des satellites qui adressent chaque micro-intention de la verticale (slope, index, compression, distance par club, choix de balle…).

### 6. Data propriétaire : le carburant de tout
[[data-proprietaire]] : sans donnée unique injectée dans les pages (data clients, base parcours construite à la main, relevés terrain), on retombe dans le corpus moyen de l'IA, donc dans la commodité. C'est elle qui alimente à la fois les preuves quantitatives, la Haute Surprise et les outils interactifs.

## Analyse GSC : les pages winners

Preuve terrain que le "Do" gagne. Les 3 pages qui sur-performent partagent l'intention "Do" :

| Page | Clics | Position | Intention |
|---|---|---|---|
| Tableau comparatif de compression des balles | 5 652 | 7,17 | Consulter un tableau pour décider |
| Calcul d'index de golf | 1 816 | 11,77 | Calculer son index (77 786 impressions) |
| Slope de votre golf | — | — | Consulter une valeur précise |

Lecture doctrinale : ce sont des vecteurs multimodaux "Do", à fort Passage Ranking, qu'aucun LLM ne remplace. Le réflexe transférable : lire la GSC, isoler le pattern des winners, le répliquer.

## 5 opportunités d'outils (vecteurs multimodaux "Do", priorisées GSC)

1. **Calculette / simulateur d'index interactif** — /calcul-index-golf déjà à 1 816 clics, pos 11,77, 77 786 impressions. Grappe captable ~20 000 impressions/mois. Inputs : score brut, SSS, slope. Output : index différentiel + projection 8 cartes. Conversion : email pour sauvegarder, upsell pack balles adapté à l'index.
2. **Quiz "Quelle balle pour vous ?" (profileur)** — page texte existante (1 330 clics, pos 8,45, 23 151 impressions) à transformer en quiz. 5-7 questions → reco produit + filtre collection. Conversion native, tech la plus simple.
3. **Carte de score interactive / calcul du différentiel** — grappe adjacente sous-traitée. Carte digitale trou par trou + calcul auto + PDF. Différenciant fort en e-commerce.
4. **Tableau de distance de clubs par profil** — réplique du format "tableau" gagnant. Filtrable (niveau, sexe, âge). Haute Surprise : data agrégée clients.
5. **Comparateur de balles côte à côte (dynamique)** — le tableau de compression statique cartonne ; le rendre dynamique (sélection 2-3 balles → specs en parallèle). Bonus pSEO : URLs /comparer/pro-v1-vs-pro-v1x.

### Priorisation

| Outil | Volume captable | Difficulté tech | ROI conversion | Priorité |
|---|---|---|---|---|
| Calculette index/handicap | ~20k imp | Moyenne | Moyen | 1 |
| Quiz "quelle balle" | ~5k imp | Faible | Très fort | 2 |
| Carte de score digitale | ~2k imp | Moyenne | Faible | 3 |
| Comparateur balles dynamique | ~5k imp | Forte | Fort | 4 |
| Tableau distance clubs | ~1k imp | Faible | Faible | 5 |

Reco si un seul outil : le **quiz "Quelle balle"** (tech simple, conversion directe, monte le CTR de la page existante).

## Créer un modèle de page et le lancer en production

La logique pSEO de Golfiller tient en une phrase : 1 template + 1 variable qui change = N pages uniques, chacune sur une requête longue traîne. Le produit, c'est la combinaison **base de données × structure de page**, pas le texte écrit à la main. Méthode, telle qu'appliquée ici :

1. **Choisir le modèle (template + variable).** Le template "page parcours" se décline sur la variable "parcours" (base de ~40 parcours français : slope + SSS). Autres variables activables sur la même verticale : la balle (comparateur côte à côte), le profil (tableau de distances de clubs). Chaque combinaison vise une micro-intention distincte, ce qui évite la cannibalisation.

2. **Garantir l'unicité réelle, pas le copier-coller.** Règle non négociable : plus de 70 % du contenu change entre deux pages, et la transformation porte sur le fond, pas seulement sur la variable. Sur une page parcours, ce sont le slope, le SSS, les sections propres au parcours qui changent. Une génération à variable bête (même page, on change le nom) se fait downgrader ou désindexer par le Helpful Content en quelques jours.

3. **Injecter la data propriétaire.** La valeur vient des chiffres eux-mêmes (base parcours construite à la main, data clients agrégée), pas du commentaire éditorial. Stack APIs officielles, zéro intermédiaire de scraping interdit. C'est ce qui alimente à la fois les preuves quantitatives, la Haute Surprise et le calculateur.

4. **Construire en HTML sémantique brut.** Calculateur de handicap (formule FFGolf) + tableau filtrable + sections par parcours, balises natives uniquement, zéro CSS ni JS superflu. Objectif : chaque bloc Hn est un passage dense, rankable seul ([[triade-serp|Passage Ranking]]).

5. **Lancer par paliers, piloté par la GSC.** On démarre par un pilote (page pilier + base ~40 parcours), on mesure en Search Console, et on n'étend (Phase 2 : une URL par parcours, extension à ~100 parcours) que si la pilier performe. On ne déverse jamais des centaines de pages d'un coup : on valide le modèle sur un échantillon, puis on industrialise.

Cette discipline (modèle scalable + unicité réelle + data propriétaire + montée en charge mesurée) est la version généralisable du cas : voir [[ranker-verticale-niche-sans-backlink]] et le catalogue [[pseo-data-driven-models]].

## Trouver ces mots-clés avec Fusionn (pratique)

Le repérage des requêtes "Do" décrit plus haut n'a rien d'artisanal une fois Fusionn branché. Le réflexe transférable du cas Golfiller (lire la donnée, isoler le pattern des winners, le répliquer) est précisément ce que l'outil enchaîne. Parcours concret, onglet par onglet :

1. **Lancer la recherche sur la verticale.** Seed minimal ("balle de golf occasion", "index golf", "slope parcours"). Si la propriété GSC golfiller.fr est branchée (sélecteur de propriété), le scoring s'appuie sur la vraie data du site et pas sur un défaut. C'est la condition pour que la suite serve à quelque chose.

2. **Onglet Mots-clés (groupe Comprendre).** La liste qualifiée arrive avec son scoring business et sa colonne Volume. On trie par potentiel de conversion pour faire remonter le décisionnel ("calculer", "comparer", "consulter") au-dessus de l'informationnel. C'est le tri "Do" vs "Know" automatisé : on garde ce qui résiste aux AI Overviews.

3. **Onglet Micro-intentions.** Il éclate la grappe en sous-intentions réelles (slope, index, compression, distance par club, choix de balle). C'est la matière du RRF : couvrir toute la grappe plutôt qu'une requête isolée, et repérer les trous que personne n'adresse.

4. **Onglet Outils (groupe Produire).** Il propose les vecteurs multimodaux "Do" associés à la grappe : calculateur, comparateur, quiz. C'est le Product-Led SEO sorti de force, le format qu'un LLM ne peut pas exécuter à la place de l'utilisateur. Exactement les 5 opportunités listées plus haut, mais générées au lieu d'être devinées.

5. **Onglet Stratégie programmatique (groupe Décider).** Les playbooks regroupent les pages à produire en lots scorés et priorisés (P0 d'abord). C'est la traduction directe de "1 template + 1 variable = N pages" sur la verticale : une URL par parcours, par balle, par profil.

6. **Onglet Analyse / entités.** Pour chaque page retenue, il liste les entités obligatoires (slope, SSS, compression…) et le gap à combler, pour viser le grounding score au lieu d'une densité de mots-clés.

Ce que Fusionn ne fait pas à ta place : choisir la verticale défendable, injecter la data propriétaire (relevés clients, base parcours), trancher la Haute Surprise. Ce qu'il fait : le travail répétitif de croiser donnée, intention et sémantique pour faire remonter les requêtes "Do" qu'on aurait ratées à la main, et les ranger en lots prêts à produire.

## Les skills à utiliser

Chaque étape du parcours, du cadrage du modèle à la page, a son skill propriétaire. Description complète de chacun :

### [[skill-programmatique-pseo]] (`/seo-programmatique-pseo`)
Conception de systèmes de contenu programmatique : 1 template + 1 variable = des centaines ou milliers de pages qui rankent chacune sur une longue traîne. Le produit, c'est la combinaison base de données × structure de page. On raisonne à la fois comme un ingénieur produit (data → template → pages) et comme un SEO senior (intention → SERP → conversion).
**Pipeline.** Identifier les modèles scalables (5 minimum) → matrice de priorisation → mots-clés par modèle → plan d'exécution 90 jours → résumé exécutif.
**Règle.** 7 règles non négociables : anti-thin content, données terrain, sourcing, canonical, maillage différenciant, Surprise Score, Grounding Score.

### `/seo-modeles-pseo`
Conception des modèles de pages satellites décisionnelles (Spokes) autour d'une page business. On génère des requêtes Ultra Business (Do) réellement tapées par un humain en situation de décision, puis on les classe a posteriori en catégories de page. La page business capte l'intention de conversion ; les Spokes captent chacun une requête décisionnelle distincte et renvoient l'utilisateur et le link equity vers elle. Génération par intention, jamais par catégorie.
**Pipeline.** Cadrer la page business + son point de conversion → générer les requêtes par intention → filtre de requêtabilité humaine → scorer (Proximité × Intention × Faisabilité) et dédupliquer → tableau priorisé des modèles de Spokes.
**Règle.** Anti-hallucination : aucun volume inventé, le décisionnel se repère à ses modificateurs.

### [[skill-roadmap-pseo]] (`/seo-roadmap-pseo`)
Construit une roadmap SEO 30/60/90 jours à partir d'une thématique ou d'une liste qualifiée de mots-clés. Découpe la production en deux phases, dans cet ordre : Phase 1 (transactionnels et décisionnels, les pages qui paient le SEO et ne se font pas manger par les LLMs) puis Phase 2 (informationnels bas de funnel qui alimentent le maillage vers Phase 1). Doctrine anti-ChatGPT : on ne produit pas pour des requêtes qu'un AI Overview va dévorer. Sortie présentable telle quelle à un décideur.
**Pipeline.** Cadrer la page business + point de conversion → importer ou générer la liste de mots-clés → classifier en 2 phases avec filtre anti-LLM → prioriser chaque phase par (volume × conversion × faisabilité) → calendrier 30/60/90 avec rythme réaliste (3 à 5 pages/semaine pour 1-2 rédacteurs).

### [[skill-product-led-seo]] (`/seo-product-led-seo`)
Conception d'outils interactifs (calculateurs, simulateurs, générateurs, audits, comparateurs) pour dominer les requêtes transactionnelles "Do" et obtenir la note "Fully Meets" des Quality Raters. Le produit génère lui-même trafic et conversions ; l'outil porte un Surprise Gap (data propriétaire unique) qui force les modèles IA à mémoriser la marque.
**Pipeline.** Analyser la thématique → identifier les micro-intentions Do (calculer, simuler, générer, auditer, comparer, planifier) → générer 5 concepts d'outils (avec Surprise Gap + Confidence Score) → évaluer la faisabilité → spécifications techniques.

### [[skill-entites-vectorielles]] (`/seo-entites-vectorielles`)
Cartographie des entités sémantiques nécessaires pour qu'une page s'aligne mathématiquement avec l'intention ciblée (similarité cosinus / Grounding Score). Les moteurs comparent les pages aux requêtes via embeddings ; cette carte dit quels termes la page doit contenir, et où.
**Pipeline.** Définir la requête cible (intention + niveau d'expertise) → générer le tableau d'entités en 4 catégories (techniques, preuves quantitatives, vecteurs multimodaux, divergence / Haute Surprise) → analyser le gap concurrentiel → recommandations d'implémentation par zone (H1, corps, FAQ).

### [[skill-preparation-semantique]] (`/seo-preparation-semantique`)
Engine de préparation sémantique sans scraping SERP. Deux modes : Création (requête → carte vierge en 11 couches) et Audit (contenu existant → diff vs carte attendue + plan de correction P0/P1/P2). Sortie riche : entités sémantiques pondérées (poids 0-1, densité cible, cosinus simulé, justification, statut), lexique signature, pain points et verbatims Haute Surprise, preuves quantitatives (Confidence Score + Freshness Guard), multimodal, cartographie concurrentielle, Gap analysis en 3 vues, divergence calibrée Information Gain, FAQ stratégique, matrice couverture × Triade SERP.
**Note.** Embeddings simulés, marqués comme tels dans chaque sortie (pas de vraie API embedding).

### [[skill-quick-win]] (`/seo-quick-win`)
Identification des opportunités SEO rapides depuis les données GSC : pages en position 3-12 à fortes impressions et CTR sous-performant. Priorité à l'optimisation de l'existant avant la création de contenu.
**Pipeline.** Filtrer (positions 3-15, exclure branded + homepage) → trier par impressions → calculer le gap CTR → croiser avec l'intention → prioriser → lister les leviers (title, méta, H1, FAQ en haut de page, densification atomique).

Fusionn (partie précédente) est la surface qui orchestre ces skills sur une interface ; en direct dans le vault, ce sont les mêmes commandes `/seo-*` lancées une à une.

## Approche et habitudes de travail (côté Tim)

- **Communication** : très concise, attend qu'on infère l'intention à partir d'instructions minimales.
- **Précision des livrables** : "HTML brut" = zéro CSS, zéro JS, zéro classe, balises sémantiques natives uniquement.
- **Communications client** : séparer ce qui est livré, ce que le client fait seul, ce qui se traite ensemble. Honnête sur le travail en attente.
- **Cadrage stratégique** : un langage qui reflète la vraie intention ("bâtir une autorité thématique sur une verticale" plutôt que "éviter les mots-clés des autres").
- **Langue** : français, tutoiement côté client.
