---
name: seo-workflow-article
description: >
  Workflow complet pour créer un article SEO de A à Z en 8 étapes séquentielles.
  Pipeline éditorial : Surprise Gap → Ancrage local → Données chiffrées → Inversions expertes 
  → Architecture narrative → Rédaction → FAQ → Compilation finale.
  
  TOUJOURS utiliser ce skill quand l'utilisateur mentionne : créer un article, rédiger un contenu,
  workflow article, pipeline éditorial, "aide-moi à écrire un article sur [sujet]",
  "je veux rédiger un article complet", création de contenu SEO, article de A à Z,
  brief + rédaction, ou demande un processus structuré pour produire un article optimisé.
---

# Skill — Workflow Création Article Complet

## Rôle

Pipeline en 8 étapes séquentielles pour produire un article SEO complet, différenciant, et prêt à publier. Chaque étape alimente la suivante — impossible de sauter une étape sans dégrader le résultat final.

**Temps estimé** : 1h30 à 2h30 par article selon complexité.

---

## Vue d'ensemble du pipeline

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

---

## Frameworks intégrés

| Framework | Étapes | Fonction |
|-----------|--------|----------|
| **Surprise Score** (Titans/MIRAS) | 1, 4, 5, 6 | Élément High Surprise en début/fin de chaque section |
| **Grounding Score** (Triade SERP) | 5, 6, 8 | Passage ancré 150-200 mots + bloc authorship ~50 mots |
| **Anti-AI Writing** | 6, 8 | Élimination des patterns IA détectables |
| **Sourcing obligatoire** | 3 | Chaque chiffre tracé jusqu'à sa source |
| **E-E-A-T local** | 2 | Signaux géographiques précis, acteurs nommés |

---

## Avant de commencer : le brief

L'agent DOIT collecter ces variables avant de lancer le workflow :

```
MOT-CLÉ      : [Le mot-clé principal — ex: "accompagnement qualiopi lyon"]
STRUCTURE HN : [La hiérarchie H1/H2/H3 de l'article]
IDÉES        : [Angles, données, points à ne pas oublier]
LOCALISATION : [Zone géographique — ex: "Lyon, Rhône-Alpes"]
SECTEUR      : [Secteur d'activité — ex: "formation professionnelle"]
AUDIENCE     : [Qui va lire — ex: "consultants qui veulent créer leur OF"]
```

---

## ÉTAPE 1 — SURPRISE GAP

### Objectif
Identifier ce que 80% des articles disent déjà vs ce qui manque sur le web. Diagnostic éditorial — sans lui, tu écris un article de plus qui n'apporte rien.

### Raisonnement
1. Lister les 5 angles les plus communs sur ce sujet (ce que 80% des articles disent déjà)
2. Identifier 5 informations vraies et sous-exploitées que les articles dominants omettent
3. Pour chaque info sous-exploitée, expliquer POURQUOI elle est absente (trop technique ? dérange un business model ? trop récente ?)
4. Classer ces 5 infos par "gradient de surprise" : de la plus attendue à la plus inattendue

### Format de sortie
```
ANGLES SATURÉS : [liste des 5 angles communs]

SURPRISE GAP :
1. [Info sous-exploitée — gradient faible] — Raison de l'absence : [...]
2. [Info sous-exploitée — gradient moyen] — Raison de l'absence : [...]
3. [Info sous-exploitée — gradient moyen-haut] — Raison de l'absence : [...]
4. [Info sous-exploitée — gradient haut] — Raison de l'absence : [...]
5. [Info sous-exploitée — gradient maximal] — Raison de l'absence : [...]

RECOMMANDATION : [angle principal pour maximiser la différenciation]
```

---

## ÉTAPE 2 — ANCRAGE LOCAL

### Objectif
Générer les signaux E-E-A-T géographiques et sectoriels précis. Un article "Qualiopi Lyon" ne doit pas être un article "Qualiopi France" avec "Lyon" collé dans le titre.

### Raisonnement
Pour la zone [LOCALISATION], identifier :
1. Autorité compétente locale (DREETS, etc.) — nom exact, adresse
2. OPCO les plus actifs dans cette zone (et pourquoi)
3. Tissu économique local : secteurs dominants, nombre d'acteurs
4. Acteurs locaux (concurrents, partenaires, réseaux)
5. Spécificités réglementaires ou pratiques liées à cette zone
6. 2-3 formulations d'ancrage naturelles (pas de keyword stuffing)

**IMPORTANT** : Si une donnée n'est pas trouvable → `[DONNÉE À SOURCER]` plutôt qu'inventer.

### Format de sortie
Liste structurée avec chaque élément sourcé.

---

## ÉTAPE 3 — DONNÉES CHIFFRÉES

### Objectif
Collecter les statistiques argumentatives — pas décoratives. Chaque chiffre doit servir un argument, pas remplir un paragraphe.

### Raisonnement
Pour chaque donnée (8 à 12 au total) :
1. **LE CHIFFRE** : valeur exacte
2. **LA SOURCE** : organisme + rapport + année — OBLIGATOIRE
3. **L'ARGUMENT** : quelle thèse ce chiffre soutient
4. **LE CONTEXTE** : ce qui rend ce chiffre surprenant ou significatif

Catégories à couvrir :
- Taille / croissance du marché
- Données réglementaires (taux de conformité, non-conformités)
- Données économiques (coûts, revenus, rentabilité)
- Données comportementales (ce que font vraiment les acteurs)

**Sources acceptées** : DARES, France Compétences, Céreq, INSEE, rapports OPCO, Jaune budgétaire, ministère du Travail.

**INTERDIT** : arrondir, extrapoler, ou citer une source sans l'avoir vérifiée.

---

## ÉTAPE 4 — INVERSIONS EXPERTES

### Objectif
Identifier les croyances fausses répandues et les corriger. Arme fatale du Surprise Score — rien ne génère plus de gradient de surprise qu'un "ce que vous croyez est faux".

### Raisonnement
Identifier 5 inversions expertes :

Pour chaque inversion :
1. **CROYANCE RÉPANDUE** : ce que la plupart des gens pensent
2. **RÉALITÉ** : ce qui est vrai, avec preuve ou explication
3. **POURQUOI L'ERREUR PERSISTE** : qui a intérêt à maintenir cette croyance ?
4. **FORMULATION DIRECTE** : phrase percutante utilisable telle quelle

Critères de sélection :
- L'inversion doit être VRAIE et vérifiable (pas une opinion)
- Elle doit concerner directement l'audience cible
- Elle doit avoir un impact sur une décision concrète (pas un fun fact)

---

## ÉTAPE 5 — ARCHITECTURE NARRATIVE

### Objectif
Construire le plan détaillé section par section en appliquant la logique Low→High Surprise (mémoire associative : continuité contextuelle + surprise informationnelle).

### Raisonnement
Pour chaque section de la structure Hn :

```
TITRE : [titre exact — respecte la hiérarchie Hn]
RAPPEL : [lien logique avec la section précédente — continuité]
CONTENU : [quelles données, inversions, ancrage local intégrer ici]
SURPRISE : [l'élément nouveau qui justifie cette section — High Surprise]
TRANSITION : [comment cette section prépare la suivante]
```

Principes :
- L'accroche crée une tension cognitive immédiate
- Chaque section a une raison d'exister distincte (pas de redondance)
- Les inversions et données sont réparties stratégiquement
- Les éléments High Surprise sont en début ET fin de section (primauté/récence)

### Éléments à marquer dans le plan
- **Passage ancré** : 150-200 mots extractible en Featured Snippet (dans les 300 premiers mots)
- **Bloc d'authorship** : ~50 mots extractible en Position 0 / AI Overview

---

## ÉTAPE 6 — RÉDACTION PRINCIPALE

### Objectif
Rédiger l'article complet en prose experte. Ton : autorité sans arrogance. Pattern : Tension → Résolution → Preuve.

### Références stylistiques
- **The Economist** pour la densité
- **Paul Graham** pour la clarté
- Traiter le lecteur comme un professionnel intelligent qui manque d'information précise

### Règles absolues de rédaction

**OBLIGATOIRE :**
- Prose continue uniquement — PAS de bullet points dans le corps
- Pattern Tension → Résolution → Preuve sur chaque idée principale
- ZÉRO phrase creuse : chaque phrase apporte une info ou déplace l'argument
- Transitions causales : "C'est pourquoi...", "Or...", "Ce n'est pas un hasard si..."
- Ton direct, jamais condescendant, jamais promotionnel
- Longueur : 2000-2500 mots minimum

**ANTI-PATTERNS IA À ÉVITER (obligatoire) :**
- ❌ "il est important de noter", "n'oublions pas que", "dans un monde en pleine évolution"
- ❌ "crucial", "pivotal", "groundbreaking", "comprehensive", "landscape"
- ❌ La "règle de 3" systématique (3 raisons, 3 étapes, 3 avantages)
- ❌ Bold excessif sur les premiers mots de chaque paragraphe
- ❌ Listes à puces avec headers bold dans le corps du texte
- ❌ Conclusion-résumé qui répète ce qui vient d'être dit
- ❌ Émojis dans les titres ou le corps

**GROUNDING SCORE :**
- Passage ancré de 150-200 mots à haute densité sémantique dans les 300 premiers mots
- Bloc de ~50 mots qui répond à 100% de la requête principale

---

## ÉTAPE 7 — FAQ MICRO-INTENTIONS

### Objectif
Générer les questions longue traîne du lecteur au stade "presque convaincu" — capture SEO des intentions de décision avancée.

### Raisonnement
Générer 6-8 questions FAQ :

Pour chaque question :
```
QUESTION : [telle qu'un vrai utilisateur la poserait dans Google]
INTENTION : [ce qu'il veut vraiment savoir derrière]
RÉPONSE : [2-3 phrases directes, sans détour]
```

Critères :
- **PRÉCISES** : pas des questions de débutant mais de quelqu'un qui a compris le cadre
- **ACTIONNABLES** : chaque question révèle une intention de décision
- **DISTINCTES** : aucun chevauchement entre questions
- **NON TRAITÉES** dans le corps de l'article (complémentaires, pas redondantes)

Classer par priorité d'intention de conversion (la plus qualifiée en premier).

---

## ÉTAPE 8 — ARTICLE FINAL (COMPILATION)

### Objectif
Compiler tous les éléments en un article final propre, cohérent, prêt à copier-coller.

### Checklist de compilation

1. ☐ Intégrer l'article avec les titres exacts de la structure Hn
2. ☐ Ajouter la FAQ en fin d'article sous "Questions fréquentes" (H2)
3. ☐ Vérifier la fluidité des transitions — corriger les ruptures
4. ☐ Supprimer les répétitions d'idées entre sections
5. ☐ Contrôler que chaque section respecte Tension → Résolution → Preuve
6. ☐ Vérifier qu'il n'y a AUCUN pattern IA (relire la liste anti-patterns)
7. ☐ Vérifier la présence du passage ancré (150-200 mots) dans les 300 premiers mots
8. ☐ Vérifier la présence du bloc d'authorship (~50 mots) extractible

### Ce que l'agent NE FAIT PAS à cette étape
- Réécrire massivement le contenu
- Changer le ton ou le style
- Ajouter des bullet points là où il y a de la prose
- Ajouter une intro méta ("Dans cet article, nous allons voir...")
- Ajouter une conclusion-résumé

**L'article commence directement par le H1 et se termine par la FAQ. Aucun méta-commentaire.**

---

## Ce que l'agent NE DOIT PAS faire (global)

❌ Sauter une étape du pipeline — chaque étape alimente la suivante

❌ Rédiger sans avoir fait le Surprise Gap — c'est écrire un article de plus

❌ Inventer des données chiffrées — tout doit être sourcé ou marqué `[DONNÉE À SOURCER]`

❌ Copier la structure des concurrents — le Surprise Gap sert exactement à éviter ça

❌ Utiliser des patterns IA détectables — voir liste anti-patterns étape 6

❌ Produire un article sans passage ancré ni bloc d'authorship

❌ Mélanger les outputs des étapes — chaque étape a son format de sortie distinct

---

## Critère de qualité

L'article final est **bon** si :

1. Le **Surprise Gap** est identifié et exploité (pas un article de plus)
2. L'**ancrage local** est réel et précis (pas "[Ville]" copié-collé)
3. Toutes les **données sont sourcées** (ou marquées à sourcer)
4. Au moins **3 inversions expertes** sont distribuées dans l'article
5. Le **passage ancré** (150-200 mots) est présent dans les 300 premiers mots
6. Le **bloc d'authorship** (~50 mots) est extractible en Position 0
7. **AUCUN pattern IA** n'est détectable
8. La **FAQ** contient 6-8 questions de décision avancée
9. L'article fait **2000-2500 mots minimum** en prose continue
