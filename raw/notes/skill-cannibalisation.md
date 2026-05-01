---
name: seo-cannibalisation
description: >
  Détecter et résoudre les cas de cannibalisation entre pages SEO. Identifier quand 
  plusieurs pages se concurrencent sur les mêmes mots-clés ou intentions, classifier 
  le type de conflit, et recommander l'action corrective appropriée.
  
  TOUJOURS utiliser ce skill quand l'utilisateur mentionne : cannibalisation, pages qui 
  se mangent entre elles, keyword cannibalism, "deux pages sur le même mot-clé", 
  "je rankais mieux avant", "ma page principale baisse alors que j'ai publié un article similaire",
  "comment savoir si mes pages se concurrencent", chutes de positions inexpliquées, 
  conflit entre pages, pages en compétition interne, ou uploade des données GSC montrant 
  plusieurs URLs sur les mêmes requêtes.
---

# Skill 02 — Cannibalisation SEO

## Rôle

Détecter les cas de cannibalisation entre pages (par intention ou par mot-clé direct), les classer par type de risque, et recommander une action corrective précise — sans simplifier à outrance une problématique qui est, par nature, complexe.

---

## Réflexion appliquée (méthode Boussardon)

- Il existe **plusieurs types de cannibalisation** : par mot-clé direct, par intention de recherche proche, par similarité sémantique. Ne pas les confondre.

- La cannibalisation **n'est pas toujours un problème** — parfois deux pages se complètent. L'agent doit distinguer conflit réel et coexistence saine.

- Le **diagnostic doit précéder la solution**. Comparer les URLs en GSC avant de recommander une action.

- La solution **n'est jamais binaire** : fusionner, rediriger, différencier ou supprimer — chaque cas a sa réponse propre.

- Vérifier si le conflit apparent n'est pas en réalité une opportunité de **"Triade SERP"** (cibler plusieurs positions sur la même requête avec des angles complémentaires).

---

## Données requises

| Source | Description | Obligatoire |
|--------|-------------|-------------|
| Export GSC Requêtes | Filtré par URL, 90 jours — pour identifier quelles pages apparaissent sur les mêmes requêtes | ✅ Oui |
| Liste des URLs | Scraping ou sitemap — pour croiser les pages thématiquement proches | Recommandé |
| Contexte stratégique | Pages piliers vs pages satellites | Recommandé |

**Minimum viable :** Export GSC requêtes + au moins 2 URLs suspectes à comparer.

---

## Raisonnement de l'agent (étapes obligatoires)

L'agent DOIT suivre ces étapes **dans l'ordre** avant de répondre :

### Étape 1 — Identifier les conflits

Identifier les requêtes déclenchant plusieurs URLs dans la GSC :
- Filtrer par requête
- Repérer les requêtes où 2+ pages apparaissent
- Lister les paires/groupes de pages en conflit

### Étape 2 — Classifier le type de cannibalisation

| Type | Description | Exemple |
|------|-------------|---------|
| **(A) Mot-clé exact** | Deux pages ciblent exactement le même mot-clé | /serrurier-paris et /serrurier-paris-urgence sur "serrurier paris" |
| **(B) Même intention** | Deux pages répondent à la même intention utilisateur | /prix-serrure et /tarif-serrurier sur l'intention "combien ça coûte" |
| **(C) Proximité sémantique** | Deux pages couvrent des sujets très proches sans conflit direct | /guide-serrure-3-points et /comparatif-serrures |
| **(Triade SERP)** | Opportunité, pas conflit — les pages couvrent des corpus distincts | /accident-voiture et /accident-voiture-veteran (micro-intentions différentes) |

### Étape 3 — Analyser les métriques

Pour chaque page en conflit, relever :

| Métrique | Page A | Page B |
|----------|--------|--------|
| Position moyenne | | |
| Impressions | | |
| Clics | | |
| CTR | | |

→ Identifier la **page gagnante** (meilleure performance globale)

### Étape 4 — Évaluer l'architecture stratégique

Déterminer le rôle de chaque page dans le cluster :
- **Page pilier** (doit gagner) vs **Page satellite** (doit soutenir)
- Quelle page est la plus alignée avec l'objectif business ?
- Quelle page a le meilleur potentiel de conversion ?

### Étape 5 — Recommander l'action corrective

| Situation | Action recommandée |
|-----------|-------------------|
| Type A + page perdante faible | **Redirection 301** de la perdante vers la gagnante |
| Type A + deux pages fortes | **Fusion** du contenu + 301 |
| Type B + micro-intentions distinctes | **Différenciation** des angles + maillage croisé |
| Type C + complémentarité | **Renforcement du maillage** vers la page pilier |
| Triade SERP | **Aucune action** — optimiser chaque page sur son angle |

**NE PAS répondre avant d'avoir complété chaque étape.**

---

## Format de sortie OBLIGATOIRE

### Tableau de diagnostic

```
CANNIBALISATION DÉTECTÉE

Requête ciblée : '[requête]'
Type : (A/B/C/Triade) [Description]

| URL | Position | Impressions | Clics | CTR | Statut |
|-----|----------|-------------|-------|-----|--------|
| /page-1 | X.X | X XXX | XXX | X.X% | Page gagnante |
| /page-2 | X.X | X XXX | XXX | X.X% | Page perdante |
```

### Diagnostic et action

```
→ Diagnostic : [Explication du conflit]

→ Action recommandée : [Action précise avec justification]

→ Implémentation :
  1. [Étape concrète 1]
  2. [Étape concrète 2]
  3. [Étape concrète 3]
```

---

## Exemple de sortie attendue

```
CANNIBALISATION DÉTECTÉE

Requête ciblée : 'serrurier paris urgence'
Type : (B) Même intention de recherche

| URL | Position | Impressions | Clics | CTR | Statut |
|-----|----------|-------------|-------|-----|--------|
| /serrurier-paris | 4.2 | 9 200 | 380 | 4.1% | Page gagnante |
| /urgence-serrurier-paris | 8.7 | 4 100 | 62 | 1.5% | Page perdante |

→ Diagnostic : Les deux pages ciblent la même intention urgente. 
  La page /serrurier-paris capte l'essentiel du trafic.
  La page /urgence dilue l'autorité sans apporter de valeur distincte.

→ Action recommandée : DIFFÉRENCIATION (pas fusion)
  Les micro-intentions sont distinctes : urgence générique vs urgence nuit/weekend.
  
→ Implémentation :
  1. Repositionner /urgence-serrurier-paris sur l'angle "nuit et weekend" exclusivement
  2. Modifier le H1 : "Serrurier Paris Nuit & Weekend — Intervention 23h-6h"
  3. Ajouter maillage interne depuis /urgence vers /serrurier-paris (ancre : "serrurier paris")
  4. Supprimer les mentions "urgence jour" de /urgence pour éviter le chevauchement
```

---

## Cas particulier : Triade SERP (faux positif)

```
ANALYSE — Requête : 'indemnisation accident voiture'

| URL | Position | Angle couvert |
|-----|----------|---------------|
| /accident-voiture | 3.2 | Guide général indemnisation |
| /accident-voiture-veteran | 7.1 | Spécificités pour vétérans |

→ Diagnostic : PAS DE CANNIBALISATION
  Les deux pages couvrent des corpus distincts (général vs spécifique).
  Google les affiche toutes deux car elles répondent à des micro-intentions différentes.
  
→ Action : Aucune. Opportunité de Triade SERP.
  Optimiser chaque page sur son angle pour maximiser le score RRF.
```

---

## Ce que l'agent NE DOIT PAS faire

❌ Recommander systématiquement une redirection 301 sans analyser les métriques des deux pages

❌ Ignorer le type de cannibalisation — traiter toutes les cannibalisations de la même façon

❌ Confondre **duplication de contenu** et **cannibalisation** — ce sont deux problèmes différents

❌ Analyser les pages en silo, sans tenir compte de leur rôle dans le cluster sémantique

❌ Proposer une solution avant d'avoir classifié le type de conflit (A/B/C/Triade)

❌ Fusionner des pages avec des micro-intentions distinctes — c'est détruire de la valeur

---

## Critère de qualité

La sortie est **bonne** si :

1. Chaque paire en conflit est **classifiée par type** (A/B/C/Triade SERP)
2. La **page gagnante est identifiée** avec justification chiffrée (position, clics, CTR)
3. L'**action recommandée est différente** selon le type détecté
4. L'implémentation contient **au moins 3 étapes concrètes**
5. Les cas de **Triade SERP sont identifiés** comme opportunités (pas comme problèmes)
