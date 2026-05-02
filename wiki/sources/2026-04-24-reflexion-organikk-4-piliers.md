---
type: source
source_type: doctrine
title: "Réflexion Organikk — 4 piliers (Surprise / Grounding / pSEO / AEO)"
aliases: [reflexion-organikk-4-piliers, methode-organikk-4-piliers]
tags: [doctrine-tim, organikk, 4-piliers, surprise-gap, grounding-score, pseo, aeo, framework]
created: 2026-04-24
updated: 2026-04-24
sources: 1
confidence: high
status: stable
---

# Réflexion Organikk — 4 piliers

**Type** : doctrine cadre — structuration complète de la méthode SEO/AEO Organikk autour de 4 piliers fondamentaux et leurs interconnexions.
**Auteur** : Tim · **Fichier raw** : `raw/notes/reflexion-organikk-source.md`
**Date** : 2026-04-24

## Les 4 piliers

### 1. SURPRISE GAP — *Pourquoi on lit*
- **Fondement** : architecture Titans / MIRAS. La mémoire d'un LLM ne se met à jour que sur les inputs à **haute surprise**
- **Principe** : mesurer la divergence entre ce que dit la page et le **consensus SERP**
- **Leviers** : inversions expertes, données terrain non-sourcées ailleurs, verbatims Haute Surprise, angle conceptuel — **jamais le volume**
- **KPI** : Surprise Score par passage / par page

### 2. GROUNDING SCORE — *Pourquoi on rank*
- **Fondement** : similarité cosinus entre vecteur d'embedding de la page et vecteur de la requête (Gemini Embedding)
- **Principe** : aligner mathématiquement l'embedding via les entités sémantiques attendues
- **Leviers — 4 catégories d'entités** : (1) techniques, (2) preuves quantitatives, (3) vecteurs multimodaux, (4) divergence (couplage avec pilier 1)
- **Méthode** : Triade SERP (3 premiers résultats → vecteur dominant + divergence contrôlée)
- **KPI** : Grounding Score vs top 3 SERP

### 3. pSEO — *Comment on scale*
- **Fondement** : 1 template + 1 variable = N pages sur longue traîne
- **Principe** : industrialiser la couverture d'intention **sans jamais tomber dans le thin content**
- **Leviers — 7 règles non-négociables** : anti-thin par design, données terrain obligatoires, sourcing vérifiable, canonical strict, maillage différenciant, Surprise Score minimum, Grounding Score minimum
- **KPI** : ratio pages indexées / pages créées > 85 %

### 4. AEO — *Comment on gagne les moteurs de réponse*
- **Fondement** : RRF (Reciprocal Rank Fusion) + framework **Know-Simple / Know / Do** (remplace TOFU/MOFU/BOFU obsolètes)
- **Principe** : architecture MECE lisible par les agents IA autonomes — SGE, Perplexity, ChatGPT, Claude
- **Leviers** : cluster Know-Simple/Know/Do, Passage Ranking, bloc authorship Position 0, Product-Led SEO ([[concepts/fully-meets]]), fact-check systématique
- **KPI** : taux de citation dans réponses génératives

## Les 6 interconnexions

| Croisement | Produit |
|---|---|
| Surprise × Grounding | Contenu différenciant ET extractible |
| Surprise × pSEO | Anti-thin content par design |
| Surprise × AEO | Citation préférentielle par les LLM (ils citent ce qui diverge) |
| Grounding × pSEO | Pertinence vectorielle garantie à l'échelle |
| Grounding × AEO | Alignement sur l'intention à chaque niveau du cluster |
| pSEO × AEO | Scalabilité × couverture MECE des intentions |

## Pyramide d'exécution

```
            AEO (architecture)
           ↑
     pSEO (scale)
    ↑
  GROUNDING (pertinence)
 ↑
SURPRISE (fondation)
```

**Règle de dépendance stricte** :
- Sans **Surprise** → pages pertinentes mais génériques, ignorées par les LLM
- Sans **Grounding** → pSEO produit du thin → pénalités
- Sans **pSEO** → AEO ne couvre pas l'étendue de l'intention
- Sans **AEO** → tout le reste reste du SEO classique → invisible en Agentic Search

## Matrice skills ↔ piliers

11 skills propriétaires Tim mappés sur les 4 piliers (cohérent avec [[sources/2026-04-12-tim-skills-seo-proprietary]]) :
- `seo-workflow-article` : Surprise + Grounding + AEO
- `seo-entites-vectorielles` : Grounding + AEO
- `seo-programmatique-pseo` : Surprise + Grounding + pSEO
- `seo-cluster-aeo` : Grounding + AEO
- `seo-peurs-objections` : Surprise
- `seo-quick-win` : Grounding
- `seo-cannibalisation` : pSEO + AEO
- `maillage-interne-gsc` : pSEO + AEO
- `seo-brief-contenu` : Surprise + Grounding + AEO
- `seo-product-led-seo` : Surprise + AEO
- `article-engine-pipeline` : Surprise + Grounding + AEO

## Cadre de décision — par où commencer

1. **Audit Grounding** → s'aligne-t-elle avec l'intention ? (`seo-entites-vectorielles`)
2. **Audit Surprise** → angle unique vs SERP ? (`seo-workflow-article`, étape 1)
3. **Audit AEO** → citable par un LLM ? (bloc authorship, passage ranking)
4. **Audit pSEO** → scalable ce format ? (`seo-programmatique-pseo`)

Toujours dans cet ordre. Fondation (Surprise + Grounding) avant scalabilité (pSEO + AEO).

## Apports à la KB

- Source umbrella qui formalise pour la première fois la **doctrine Organikk** comme un système cohérent à 4 piliers + 6 interconnexions + matrice skills
- Cohérent avec [[syntheses/doctrine-seo-post-sge]] mais plus opérationnel (matrice + cadre de décision)
- Concept candidat à créer : `methode-organikk-4-piliers` (concept umbrella)
- Connecte 11 skills + 4 concepts existants ([[concepts/surprise-gap]], [[concepts/grounding-score]], [[concepts/programmatique-pseo]], [[concepts/aeo]]) en un schéma exécutable

## Pages liées

[[concepts/surprise-gap]] · [[concepts/grounding-score]] · [[concepts/programmatique-pseo]] · [[concepts/aeo]] · [[concepts/data-proprietaire]] · [[concepts/agentic-search]] · [[concepts/fully-meets]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[syntheses/doctrine-seo-post-sge]] · [[sources/2026-04-24-cluster-business-organikk-4-piliers]] · [[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]]
