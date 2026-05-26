---
type: source
source_type: doctrine
title: "Workflow Complet : Créer un Article de A à Z"
aliases: []
tags: []
created: 2026-04-12
updated: 2026-04-12
sources: 0
confidence: medium
status: draft
---

# Workflow Complet : Créer un Article de A à Z

> Basé sur l'ensemble des conversations précédentes. Pipeline en 8 étapes séquentielles — chaque étape alimente la suivante.

---

## VUE D'ENSEMBLE

```
INPUT : Mot-clé + Structure Hn + Idées + Localisation + Secteur + Audience
  │
  ├─► Étape 1 — Surprise Gap (ce qui manque sur le web)
  │     ├─► Étape 2 — Ancrage local (signaux terrain)
  │     ├─► Étape 3 — Données chiffrées (stats argumentatives)
  │     │     └─► Étape 4 — Inversions expertes (contre-intuitifs)
  │     │
  │     └─────────► Étape 5 — Architecture narrative (plan section par section)
  │                       └─► Étape 6 — Rédaction principale (prose experte)
  │                             └─► Étape 7 — FAQ micro-intentions
  │                                   └─► Étape 8 — Article final compilé
  │
OUTPUT : Article complet prêt à publier
```

**Temps estimé** : 1h30 à 2h30 par article (selon la longueur et la complexité du sujet).

---

## AVANT DE COMMENCER : LE BRIEF

Avant de lancer le workflow, remplis ces variables. Elles alimentent TOUS les prompts.

```
MOT-CLÉ        : [Le mot-clé principal — ex: "accompagnement qualiopi lyon"]
STRUCTURE HN    : [La hiérarchie H1/H2/H3 de l'article — copiée depuis ta recherche SERP ou ta stratégie]
IDÉES           : [Angles, données, points à ne pas oublier]
LOCALISATION    : [Zone géographique — ex: "Lyon, Rhône-Alpes"]
SECTEUR         : [Secteur d'activité — ex: "formation professionnelle"]
AUDIENCE        : [Qui va lire — ex: "consultants et coachs qui veulent créer leur OF et obtenir Qualiopi"]
```

---

## ÉTAPE 1 — SURPRISE GAP

### Objectif
Identifier ce que 80% des articles disent déjà vs ce qui manque sur le web. C'est le diagnostic éditorial — sans lui, tu écris un article de plus qui n'apporte rien.

### Prompt

```
Tu es un stratège éditorial senior spécialisé dans les marchés B2B français.

Sujet : "[MOT-CLÉ]"
Structure Hn : [STRUCTURE HN]
Idées initiales : [IDÉES]
Localisation : [LOCALISATION]
Secteur : [SECTEUR]
Audience : [AUDIENCE]

Ta mission : identifier le Surprise Gap éditorial de ce sujet.

1. Liste les 5 angles les plus communs sur ce sujet (ce que 80% des articles disent déjà).
2. Identifie 5 informations vraies et sous-exploitées que les articles dominants omettent — données qui dérangent, contre-intuitifs, nuances d'expert terrain.
3. Pour chaque info sous-exploitée, explique POURQUOI elle est absente (trop technique ? dérange un business model ? trop récente ?).
4. Classe ces 5 infos par "gradient de surprise" : de la plus attendue à la plus inattendue.

Format de sortie :
- ANGLES SATURÉS : [liste]
- SURPRISE GAP : [5 éléments classés par gradient croissant]
- RECOMMANDATION : quel angle principal donner à l'article pour maximiser la différenciation
```

### Ce que tu obtiens
Un diagnostic clair : voilà ce que tout le monde dit, voilà ce que personne ne dit, voilà l'angle de ton article.

### Lien Surprise Score
Cette étape alimente directement le Surprise Score (Règle 6) — les éléments High Surprise identifiés ici seront placés en début et fin de chaque section dans l'article final.

---

## ÉTAPE 2 — ANCRAGE LOCAL

### Objectif
Générer les signaux E-E-A-T géographiques et sectoriels précis qui ancrent l'article dans une réalité terrain. Un article "Qualiopi Lyon" ne doit pas être un article "Qualiopi France" avec "Lyon" collé dans le titre.

### Prompt

```
Tu es un expert en ancrage géographique pour le SEO local B2B.

Sujet : "[MOT-CLÉ]"
Localisation : [LOCALISATION]
Secteur : [SECTEUR]
Audience : [AUDIENCE]

Surprise Gap (Étape 1) : [COLLER OUTPUT ÉTAPE 1]

Ta mission : produire les éléments d'ancrage local à intégrer dans l'article.

Pour la zone [LOCALISATION], identifie :
1. DREETS compétente (nom exact, adresse si possible)
2. OPCO les plus actifs dans cette zone (et pourquoi)
3. Tissu économique local : secteurs d'activité dominants, nombre d'OF déclarés si disponible
4. Acteurs locaux de la formation (concurrents, partenaires, réseaux)
5. Spécificités réglementaires ou pratiques liées à cette zone
6. 2-3 formulations d'ancrage naturelles (pas du keyword stuffing — des phrases qui sonnent comme un local qui parle)

IMPORTANT : si tu ne trouves pas une donnée, mets [DONNÉE À SOURCER] plutôt qu'inventer.

Format : liste structurée, chaque élément avec sa source si connue.
```

### Ce que tu obtiens
Un kit d'ancrage local prêt à injecter dans la rédaction — noms, lieux, chiffres locaux, formulations naturelles.

---

## ÉTAPE 3 — DONNÉES CHIFFRÉES

### Objectif
Collecter les statistiques argumentatives — pas décoratives. Chaque chiffre doit servir un argument, pas remplir un paragraphe.

### Prompt

```
Tu es un data analyst spécialisé en données sectorielles B2B françaises.

Sujet : "[MOT-CLÉ]"
Secteur : [SECTEUR]
Audience : [AUDIENCE]

Surprise Gap (Étape 1) : [COLLER OUTPUT ÉTAPE 1]

Ta mission : identifier les données chiffrées à fort impact argumentatif pour cet article.

Pour chaque donnée :
1. LE CHIFFRE : [valeur exacte]
2. LA SOURCE : [organisme + rapport + année — OBLIGATOIRE]
3. L'ARGUMENT : [quelle thèse ce chiffre soutient dans l'article]
4. LE CONTEXTE : [ce qui rend ce chiffre surprenant ou significatif]

Identifie 8 à 12 données dans ces catégories :
- Taille / croissance du marché
- Données réglementaires (taux de conformité, non-conformités fréquentes)
- Données économiques (coûts, revenus, rentabilité)
- Données comportementales (ce que font vraiment les acteurs du marché)

Sources acceptées : DARES, France Compétences, Céreq, INSEE, rapports OPCO, Jaune budgétaire, ministère du Travail.

INTERDIT : arrondir, extrapoler, ou citer une source sans l'avoir vérifiée. Si la donnée n'est pas trouvable → [DONNÉE À SOURCER + source recommandée].
```

### Ce que tu obtiens
Un tableau de données sourcées, chacune liée à un argument précis. Prêt à injecter dans la rédaction.

### Lien Règle 5
Cette étape applique directement la Règle 5 (Sourcing obligatoire) — chaque chiffre est tracé jusqu'à sa source.

---

## ÉTAPE 4 — INVERSIONS EXPERTES

### Objectif
Identifier les croyances fausses répandues sur le sujet et les corriger. C'est l'arme fatale du Surprise Score — rien ne génère plus de gradient de surprise qu'un "ce que vous croyez est faux, et voici pourquoi".

### Prompt

```
Tu es un expert terrain avec 15 ans d'expérience dans [SECTEUR].

Sujet : "[MOT-CLÉ]"
Audience : [AUDIENCE]

Surprise Gap (Étape 1) : [COLLER OUTPUT ÉTAPE 1]
Données chiffrées (Étape 3) : [COLLER OUTPUT ÉTAPE 3]

Ta mission : identifier 5 inversions expertes — des croyances répandues qui sont fausses ou trompeuses.

Pour chaque inversion :
1. CROYANCE RÉPANDUE : [ce que la plupart des gens pensent]
2. RÉALITÉ : [ce qui est vrai, avec preuve ou explication]
3. POURQUOI L'ERREUR PERSISTE : [qui a intérêt à maintenir cette croyance ?]
4. FORMULATION DIRECTE : [une phrase percutante qui résume l'inversion — utilisable telle quelle dans l'article]

Critères de sélection :
- L'inversion doit être VRAIE et vérifiable (pas une opinion)
- Elle doit concerner directement l'audience cible
- Elle doit avoir un impact sur une décision concrète (pas un fun fact)
```

### Ce que tu obtiens
5 "bombes éditoriales" prêtes à être distribuées dans l'article pour maximiser le Surprise Score section par section.

---

## ÉTAPE 5 — ARCHITECTURE NARRATIVE

### Objectif
Construire le plan détaillé section par section en appliquant la logique Low→High Surprise (mémoire associative : continuité contextuelle + surprise informationnelle à chaque section).

### Prompt

```
Tu es un architecte éditorial expert en structure d'articles à fort taux de lecture complète.

Sujet : "[MOT-CLÉ]"
Structure Hn : [STRUCTURE HN]
Localisation : [LOCALISATION]
Audience : [AUDIENCE]

Surprise Gap (Étape 1) : [COLLER OUTPUT ÉTAPE 1]
Données chiffrées (Étape 3) : [COLLER OUTPUT ÉTAPE 3]
Inversions expertes (Étape 4) : [COLLER OUTPUT ÉTAPE 4]

Ta mission : construire le plan narratif détaillé en respectant la structure Hn fournie.

Pour chaque section, utilise CE FORMAT :

TITRE : [titre exact — respecte la hiérarchie Hn]
RAPPEL : [lien logique avec la section précédente — continuité]
CONTENU : [quelles données, inversions, ancrage local intégrer ici]
SURPRISE : [l'élément nouveau qui justifie cette section — High Surprise]
TRANSITION : [comment cette section prépare la suivante]

Principes :
- L'accroche crée une tension cognitive immédiate (le lecteur doit ressentir "je ne savais pas ça")
- Chaque section a une raison d'exister distincte (pas de redondance)
- Les inversions et données sont réparties stratégiquement — pas concentrées au début
- La progression suit la logique mentale du LECTEUR, pas la logique administrative du sujet
- Les éléments High Surprise sont en début et fin de section (primauté/récence)

Termine par : ce que le lecteur doit ressentir/décider après avoir lu l'article complet.
```

### Ce que tu obtiens
Le plan complet section par section, avec pour chaque section : ce qu'il faut dire, quelle donnée utiliser, quel élément de surprise, et comment enchaîner.

### Lien Grounding Score
C'est ici que tu identifies quel passage sera le "passage ancré" (150-200 mots, extractible en Featured Snippet) et le "bloc d'authorship" (~50 mots, extractible en Position 0). Marque-les dans le plan.

---

## ÉTAPE 6 — RÉDACTION PRINCIPALE

### Objectif
Rédiger l'article complet en prose experte. Ton : autorité sans arrogance. Pattern : Tension → Résolution → Preuve.

### Prompt

```
Tu es un rédacteur expert en contenu B2B à forte valeur informative. 
Modèle de référence : l'Economist pour la densité, Paul Graham pour la clarté.
Tu traites le lecteur comme un professionnel intelligent qui manque d'information précise.

Sujet : "[MOT-CLÉ]"
Structure Hn : [STRUCTURE HN]
Localisation : [LOCALISATION]
Audience : [AUDIENCE]

Plan narratif (Étape 5) : [COLLER OUTPUT ÉTAPE 5]
Données chiffrées (Étape 3) : [COLLER OUTPUT ÉTAPE 3]
Inversions expertes (Étape 4) : [COLLER OUTPUT ÉTAPE 4]
Ancrage local (Étape 2) : [COLLER OUTPUT ÉTAPE 2]

RÈGLES ABSOLUES DE RÉDACTION :
- PAS de bullet points dans le corps du texte — prose continue uniquement
- PAS de headers autres que les H2/H3 de la structure Hn
- Pattern obligatoire : Tension → Résolution → Preuve sur chaque idée principale
- ZÉRO phrase creuse : chaque phrase apporte une info ou déplace l'argument
- Transitions causales : "C'est pourquoi...", "Or...", "Ce n'est pas un hasard si..."
- Ton : direct, jamais condescendant, jamais promotionnel
- Longueur : 2000-2500 mots minimum

ANTI-PATTERNS IA À ÉVITER (obligatoire) :
- JAMAIS : "il est important de noter", "n'oublions pas que", "dans un monde en pleine évolution"
- JAMAIS : "crucial", "pivotal", "groundbreaking", "comprehensive", "landscape"
- JAMAIS : la "règle de 3" systématique (3 raisons, 3 étapes, 3 avantages)
- JAMAIS : bold excessif sur les premiers mots de chaque paragraphe
- JAMAIS : listes à puces avec headers bold dans le corps du texte
- JAMAIS : conclusion-résumé qui répète ce qui vient d'être dit
- JAMAIS : émojis dans les titres ou le corps

PASSAGE ANCRÉ (Grounding Score) :
- Intègre un passage de 150-200 mots à haute densité sémantique dans les 300 premiers mots de l'article — ce passage doit être extractible en Featured Snippet.
- Intègre un bloc de ~50 mots qui répond à 100% de la requête principale — conçu pour extraction en Position 0 / AI Overview.

Rédige l'article complet maintenant. Commence directement par le contenu, pas par un méta-commentaire.
```

### Ce que tu obtiens
L'article rédigé en prose continue, 2000-2500 mots, prêt à être finalisé.

---

## ÉTAPE 7 — FAQ MICRO-INTENTIONS

### Objectif
Générer les questions longue traîne du lecteur au stade "presque convaincu" — capture SEO des intentions de décision avancée.

### Prompt

```
Tu es un spécialiste SEO sémantique expert en intentions de recherche B2B.

Sujet : "[MOT-CLÉ]"
Localisation : [LOCALISATION]
Audience : [AUDIENCE]

Article rédigé (Étape 6) : [COLLER OUTPUT ÉTAPE 6]

Ta mission : générer 6-8 questions FAQ qui capturent les micro-intentions au stade "presque convaincu".

Critères :
- PRÉCISES : pas des questions de débutant mais de quelqu'un qui a compris le cadre général
- ACTIONNABLES : chaque question révèle une intention de décision
- DISTINCTES : aucun chevauchement entre questions
- NON TRAITÉES dans le corps de l'article (complémentaires, pas redondantes)

Format par question :
QUESTION : [telle qu'un vrai utilisateur la poserait dans Google]
INTENTION : [ce qu'il veut vraiment savoir derrière]
RÉPONSE : [2-3 phrases directes, sans détour, sans "il est important de noter"]

Classe les questions par priorité d'intention de conversion (la plus qualifiée en premier).
```

### Ce que tu obtiens
6-8 blocs Question/Réponse prêts à être intégrés en fin d'article, optimisés pour le Passage Ranking et les AI Overviews.

---

## ÉTAPE 8 — ARTICLE FINAL (COMPILATION)

### Objectif
Compiler tous les éléments en un article final propre, cohérent, prêt à copier-coller.

### Prompt

```
Tu es un éditeur senior avec 20 ans d'expérience en presse économique B2B.
Tu lis l'article avec l'œil du LECTEUR final, pas de l'auteur.

Sujet : "[MOT-CLÉ]"
Structure Hn : [STRUCTURE HN]

Plan narratif (Étape 5) : [COLLER OUTPUT ÉTAPE 5]
Article rédigé (Étape 6) : [COLLER OUTPUT ÉTAPE 6]
FAQ (Étape 7) : [COLLER OUTPUT ÉTAPE 7]

Ta mission : produire la VERSION FINALE de l'article.

CHECKLIST DE COMPILATION :
1. Intégrer l'article avec les titres exacts de la structure Hn
2. Ajouter la FAQ en fin d'article sous le titre "Questions fréquentes" (H2)
3. Vérifier la fluidité des transitions — corriger les ruptures
4. Supprimer les répétitions d'idées entre sections
5. Contrôler que chaque section respecte Tension → Résolution → Preuve
6. Vérifier qu'il n'y a AUCUN pattern IA (relire la liste anti-patterns de l'Étape 6)
7. Vérifier la présence du passage ancré (150-200 mots) dans les 300 premiers mots
8. Vérifier la présence du bloc d'authorship (~50 mots) extractible en Position 0

CE QUE TU NE FAIS PAS :
- Réécrire massivement le contenu
- Changer le ton ou le style
- Ajouter des bullet points là où il y a de la prose
- Ajouter une intro méta ("Dans cet article, nous allons voir...")
- Ajouter une conclusion-résumé

L'article commence directement par le H1 et se termine par la FAQ.
Aucun méta-commentaire. Juste l'article.
```

### Ce que tu obtiens
L'article final, prêt à copier-coller dans ton CMS.

---

## RÉCAPITULATIF : CHECKLIST RAPIDE

```
☐ Remplir le brief (mot-clé, Hn, idées, localisation, secteur, audience)
☐ Étape 1 — Surprise Gap → diagnostic éditorial
☐ Étape 2 — Ancrage local → signaux terrain
☐ Étape 3 — Données chiffrées → stats sourcées
☐ Étape 4 — Inversions expertes → contre-intuitifs
☐ Étape 5 — Architecture narrative → plan section par section
☐ Étape 6 — Rédaction principale → article complet en prose
☐ Étape 7 — FAQ micro-intentions → questions longue traîne
☐ Étape 8 — Article final → compilation et vérification
☐ Relecture manuelle finale (vérifier les [DONNÉE À SOURCER], les anti-patterns IA, la cohérence)
```

---

## FRAMEWORKS INTÉGRÉS DANS CE WORKFLOW

| Framework | Où il intervient | Ce qu'il fait |
|---|---|---|
| **Surprise Score** (Titans/MIRAS) | Étapes 1, 4, 5, 6 | Chaque section contient un élément High Surprise en début/fin. Structure mémoire associative. |
| **Grounding Score** (Triade SERP) | Étapes 5, 6, 8 | Passage ancré 150-200 mots + bloc authorship ~50 mots + micro-intentions couvertes |
| **Anti-AI Writing** (Wikipedia Signs) | Étape 6, 8 | Élimination systématique des patterns IA détectables |
| **Sourcing obligatoire** (Règle 5) | Étape 3 | Chaque chiffre tracé jusqu'à sa source d'autorité |
| **E-E-A-T local** | Étape 2 | Signaux géographiques précis, acteurs nommés, références locales |

---

## AUTOMATISATION

Ce workflow peut être automatisé dans un Artifact React qui appelle l'API Claude en séquence — tu entres le brief, tu cliques "Lancer", les 8 étapes tournent en live et l'article final apparaît. On l'a déjà construit dans une conversation précédente (voir `editorial-workflow.jsx`).

Pour l'utiliser en manuel : copie-colle chaque prompt dans Claude l'un après l'autre, en collant le résultat de l'étape précédente dans la suivante.
