---
name: seo-cluster-aeo
description: |
  Construire des clusters sémantiques optimisés pour l'AEO (Answer Engine Optimization) et l'Agentic Search. Catégorise les pages satellites selon les intentions Know-Simple, Know et Do pour maximiser le score RRF (Reciprocal Rank Fusion).
  
  TOUJOURS utiliser ce skill quand l'utilisateur mentionne : cluster sémantique, cocon SEO, pages satellites, AEO, Answer Engine Optimization, Agentic Search, intentions de recherche, Know/Do, MECE, architecture de contenu, arborescence SEO, "quelles pages créer autour de [mot-clé]", stratégie de contenu SEO, maillage thématique, topical authority, ou veut planifier un ensemble de pages interconnectées.
---

# Clusters Sémantiques AEO / Agentic Search

Ce skill génère une architecture de contenu complète optimisée pour les moteurs de réponse (SGE, Perplexity, ChatGPT) et les agents IA autonomes.

## Quand utiliser ce skill

- Pour planifier une stratégie de contenu autour d'un mot-clé pilier
- Pour restructurer un site existant en clusters thématiques
- Pour identifier les gaps de contenu face aux concurrents
- Pour optimiser la visibilité dans les réponses IA (AEO)

## Concepts clés

### AEO (Answer Engine Optimization)
Optimisation pour les moteurs qui génèrent des réponses directes (Google SGE, Bing Copilot, Perplexity, ChatGPT avec browsing).

### Agentic Search
Optimisation pour les agents IA autonomes (MLE-STAR, AutoGPT, etc.) qui effectuent des recherches et actions pour l'utilisateur.

### Score RRF (Reciprocal Rank Fusion)
Algorithme qui combine les classements de plusieurs sources. Un cluster couvrant toutes les sous-intentions améliore le score global.

### Principe MECE
Mutuellement Exclusif, Collectivement Exhaustif. Chaque page couvre un angle unique, l'ensemble couvre toute la thématique.

## Instructions

### Étape 1 : Définir le mot-clé pilier

Demander à l'utilisateur :
1. **Le mot-clé pilier** (requête principale à dominer)
2. **Le secteur/niche** de l'entreprise
3. **Les ressources disponibles** (équipe rédaction, budget outils, données propriétaires)

### Étape 2 : Mapper les intentions selon le framework AEO

**ABANDONNER** le framework TOFU/MOFU/BOFU classique.

Utiliser les 3 types d'intentions des moteurs IA :

#### Intention "Know-Simple"
**Définition** : Questions factuelles avec réponse courte et unique.

Caractéristiques :
- Réponse en <50 mots
- Souvent affichée en Position 0 / Featured Snippet
- Les agents IA extraient directement la réponse
- Format idéal : définition, chiffre, date, nom

**Exemples** :
- "Quel est le prix moyen d'un audit SEO ?"
- "Définition du TF-IDF"
- "Durée moyenne d'une campagne SEO"

#### Intention "Know"
**Définition** : Questions nécessitant une explication approfondie.

Caractéristiques :
- Réponse longue avec structure et preuves
- Nécessite des données structurées (FAQ, How-to schema)
- Les agents IA synthétisent plusieurs sections
- Format idéal : guide, tutoriel, comparatif détaillé

**Exemples** :
- "Comment choisir une agence SEO ?"
- "Les étapes d'un audit technique complet"
- "Différences entre SEO on-page et off-page"

#### Intention "Do"
**Définition** : Micro-tâches que l'utilisateur (ou l'agent IA) veut accomplir.

Caractéristiques :
- Nécessite un outil, workflow ou action concrète
- Les agents IA autonomes peuvent l'exécuter à la place de l'humain
- Génère des leads qualifiés (échange valeur vs données)
- Format idéal : calculateur, simulateur, générateur, audit automatisé

**Exemples** :
- "Calculer le ROI d'une stratégie SEO"
- "Générer une checklist d'audit technique"
- "Simuler le trafic potentiel d'un mot-clé"

### Étape 3 : Générer le tableau du cluster

Créer un tableau avec **minimum 15 pages satellites** réparties selon les 3 intentions :

| Requête cible | Type d'intention | Format de landing page | Données structurées | Priorité |
|---------------|------------------|----------------------|--------------------| ---------|
| [Requête longue traîne] | Know-Simple / Know / Do | [Format spécifique] | [Schema.org applicable] | Haute/Moyenne/Basse |

### Règles de répartition

Distribution recommandée :
- **Know-Simple** : 20-30% (quick wins pour Position 0)
- **Know** : 40-50% (autorité thématique)
- **Do** : 20-30% (génération de leads)

### Formats de landing page par intention

#### Know-Simple
- FAQ conversationnelle (une question = une page)
- Définition enrichie avec exemple
- Tableau de données (prix, délais, stats)
- Glossaire thématique

#### Know
- Guide ultime (3000+ mots)
- Comparatif structuré (tableau + analyse)
- Étude de cas détaillée
- Tutoriel pas-à-pas avec visuels

#### Do
- Calculateur interactif (ROI, budget, temps)
- Générateur (checklist, template, brief)
- Simulateur (trafic, revenus, positionnement)
- Outil d'audit gratuit (score + recommandations)
- Quiz/assessment avec résultat personnalisé

### Étape 4 : Définir le maillage interne

Pour chaque page, identifier :
1. **Liens entrants** : quelles pages du cluster pointent vers elle
2. **Liens sortants** : vers quelles pages elle pointe
3. **Ancres recommandées** : textes d'ancre optimisés

Règles de maillage :
- La page pilier reçoit des liens de toutes les pages satellites
- Les pages "Do" reçoivent des liens des pages "Know" (parcours : apprendre → agir)
- Les pages "Know-Simple" servent de passerelles vers les pages "Know"

### Étape 5 : Priorisation et roadmap

Classer les pages par priorité selon :
1. **Volume de recherche** de la requête cible
2. **Difficulté de positionnement** (concurrence)
3. **Potentiel de conversion** (intention commerciale)
4. **Effort de production** (contenu vs outil)

## Exemple de sortie

```markdown
## Cluster sémantique - Mot-clé pilier : "[Mot-clé]"

### Architecture MECE

| Requête cible | Intention | Format | Schema.org | Priorité |
|---------------|-----------|--------|------------|----------|
| Définition [terme] | Know-Simple | FAQ + définition | FAQPage | Haute |
| Prix [service] en 2024 | Know-Simple | Tableau comparatif | Product | Haute |
| Comment [action] ? | Know | Guide 3000 mots | HowTo | Haute |
| [Service] vs [alternative] | Know | Comparatif | ItemList | Moyenne |
| Calculer [métrique] | Do | Calculateur interactif | WebApplication | Haute |
| Générer [livrable] | Do | Générateur + capture email | SoftwareApplication | Moyenne |
| ... | ... | ... | ... | ... |

### Maillage interne
[Schéma visuel des connexions entre pages]

### Roadmap de production
- **Mois 1** : Pages Know-Simple (quick wins)
- **Mois 2** : Pages Know principales
- **Mois 3** : Outils Do + page pilier
```

## Notes importantes

- Chaque page doit avoir une requête cible UNIQUE (principe MECE)
- Les pages "Do" nécessitent souvent un développement technique
- Réviser le cluster tous les 6 mois selon les évolutions de la SERP
- Les agents IA privilégient les contenus structurés et actionnables
