---
type: source
source_type: doctrine
title: "10 Skills SEO propriétaires (hooks §7 AGENTS.md)"
aliases: [tim-skills-seo, skills-proprietary]
tags: [doctrine-tim, skills, seo, geo, aeo, operationnel]
created: 2026-04-12
updated: 2026-04-12
sources: 1
confidence: high
status: stable
---

# 10 Skills SEO propriétaires

**Fichiers raw** : `raw/notes/skill-*.md` (10 fichiers, ~30 KB total)
**Date** : 12 avril 2026

Les 10 skills qui correspondent aux hooks §7 d'`AGENTS.md` v2.2. Chaque skill a un trigger, un pipeline structuré, un output obligatoire, et des règles absolues. Ils sont les **briques opérationnelles** du framework [[concepts/ingenierie-semantique-inversee]].

---

## Inventaire des skills

### 1. Brief de Contenu & Structure Hn
**Trigger** : "brief", "structure Hn", "plan de page"
**Pipeline** : 7 étapes — décoder requête → lister vecteurs sémantiques → micro-intentions → construire Hn → contenu par H2 → signaux E-E-A-T → format multimodal
**Règle clé** : chaque H2 = un vecteur sémantique attendu par Google. Au moins 1 H2 doit générer un [[concepts/surprise-gap]].
**Fichier** : `raw/notes/skill-brief-contenu.md`

### 2. Cannibalisation SEO
**Trigger** : "cannibalisation", "deux pages sur le même mot-clé"
**Pipeline** : 5 étapes — identifier conflits → classifier (A: mot-clé exact / B: même intention / C: proximité / Triade SERP) → analyser métriques → évaluer architecture → recommander action (301, fusion, différenciation, ou rien)
**Règle clé** : les Triades SERP sont des **opportunités**, pas des problèmes.
**Fichier** : `raw/notes/skill-cannibalisation.md`

### 3. Clusters Sémantiques AEO
**Trigger** : "cluster", "cocon", "AEO", "topical authority"
**Pipeline** : 5 étapes — mot-clé pilier → mapper intentions (Know-Simple / Know / Do) → tableau cluster (min 15 pages) → maillage → roadmap
**Règle clé** : TOFU/MOFU/BOFU est **obsolète** pour l'AEO. Remplacé par Know-Simple / Know / Do. Pages "Do" = outils interactifs, pas du texte.
**Fichier** : `raw/notes/skill-cluster-aeo.md`

### 4. Entités Vectorielles SEO
**Trigger** : "entités sémantiques", "vecteurs SEO", "[[concepts/grounding-score]]", "similarité cosinus"
**Pipeline** : 4 étapes — requête cible → tableau entités (Techniques / Preuves Quantitatives / Multimodaux / Divergence Haute Surprise) → gap concurrentiel → implémentation
**Règle clé** : format preuve quantitative obligatoire "73% des entreprises B2B" — jamais "beaucoup d'entreprises". Test Haute Surprise : si un concurrent peut copier en 5 min → pas de surprise.
**Fichier** : `raw/notes/skill-entites-vectorielles.md`

### 5. Maillage Interne GSC
**Trigger** : "maillage", "liens internes", "cocon SEO", "GSC + structure"
**Pipeline** : 5 étapes — données GSC → diagnostiquer structure (mères/filles/orphelines) → plan maillage → prioriser (score urgence) → recommandations
**Règle clé** : page mère = **minimum 10 citations** depuis filles/petites-filles. Maillage par intention (Know→Do) en plus du sémantique.
**Fichier** : `raw/notes/skill-maillage-interne.md`

### 6. Peurs & Objections B2B
**Trigger** : "objections", "peurs prospects", "pain points", "freins à l'achat"
**Pipeline** : 4 étapes — contexte → tableau analyse (10+ lignes : pain point / verbatim Haute Surprise / preuve atomique) → prioriser top 3 → recommandations contenu
**Règle clé** : verbatims = frustrations expertes rarement verbalisées, vocabulaire métier. Jamais des clichés. Preuves atomiques au format Sujet + Verbe + Donnée.
**Fichier** : `raw/notes/skill-peurs-objections.md`

### 7. Product-Led SEO
**Trigger** : "Product-Led SEO", "calculateur", "simulateur", "outil gratuit", "Fully Meets"
**Pipeline** : 5 étapes — thématique → micro-intentions "Do" → 5 concepts d'outils → évaluer faisabilité → spécifications techniques
**Règle clé** : pattern de conversion = valeur gratuite (résultat partiel) → gate email → upsell audit. Prévoir version "agent-friendly" avec API/embed pour l'Agentic SEO.
**Fichier** : `raw/notes/skill-product-led-seo.md`

### 8. SEO Programmatique (pSEO)
**Trigger** : "pSEO", "programmatique", "template + variable", "pages scalables"
**Pipeline** : 5 étapes — identifier modèles scalables (5 min) → matrice priorisation → mots-clés par modèle → plan 90 jours → résumé exécutif
**Règle clé** : anti-thin content = chaque variable change le contenu réel, max 30% texte identique. Au moins 1 élément High Surprise par section + passage ancré obligatoire.
**Fichier** : `raw/notes/skill-programmatique-pseo.md`

### 9. Quick Win SEO
**Trigger** : "quick win", "gains rapides", "pages position 3-12", "CTR faible"
**Pipeline** : 6 étapes — filtrer pos 3-15 → trier impressions → calculer gap CTR → croiser intention → prioriser → leviers
**Règle clé** : proposer du nouveau contenu **AVANT** d'épuiser les quick wins existants = interdit. Toujours inclure 1 exemple avant/après de densification atomique.
**Fichier** : `raw/notes/skill-quick-win.md`

### 10. Workflow Création Article Complet
**Trigger** : "créer un article", "workflow article", "article de A à Z"
**Pipeline** : 8 étapes identiques au [[concepts/workflow-redaction-8-etapes]] — Surprise Gap → Ancrage local → Données → Inversions → Architecture → Rédaction → FAQ → Final
**Règle clé** : prose continue, TENSION→RÉSOLUTION→PREUVE, 2000-2500 mots, passage ancré 150-200 mots, bloc authorship ~50 mots, 0 pattern IA.
**Fichier** : `raw/notes/skill-workflow-article.md`

---

## Concepts transversaux aux 10 skills

| Concept | Skills qui l'utilisent |
|---|---|
| [[concepts/surprise-gap]] | 1, 3, 4, 6, 7, 8, 10 (7/10) |
| [[concepts/grounding-score]] | 1, 4, 6, 7, 8, 10 (6/10) |
| [[concepts/data-proprietaire]] | 3, 4, 6, 7, 8, 9 (6/10, via "preuves atomiques") |
| [[concepts/information-gain]] | 1, 3, 4, 9, 10 (5/10, via sourcing obligatoire) |
| [[concepts/anti-ai-writing]] | 10 (1/10, mais appliqué à tout output rédactionnel) |
| [[concepts/workflow-redaction-8-etapes]] | 10 (skill = le workflow lui-même) |
| [[concepts/ingenierie-semantique-inversee]] | Tous (framework parent) |

## Concepts référencés mais pas encore créés dans le wiki

Les skills référencent des concepts listés en §4.2 d'`AGENTS.md` qui n'ont **pas encore de page** :
- `e-e-a-t` — cité dans 6+ skills
- `fully-meets` — cité dans skills 3, 6, 7
- `aeo` / `agentic-search` — cités dans skills 3, 7
- `passage-ranking` — cité dans skills 1, 4
- `rrf` — cité dans skills 2, 3, 8

Ces pages apparaîtront en **liens rouges** dans Obsidian → TODO pour un futur ingest ou une session de création de stubs.

## Pages liées

[[concepts/ingenierie-semantique-inversee]] · [[concepts/workflow-redaction-8-etapes]] · [[concepts/surprise-gap]] · [[concepts/grounding-score]] · [[concepts/data-proprietaire]] · [[concepts/information-gain]] · [[concepts/anti-ai-writing]] · [[entities/fusionn-io]] · [[syntheses/doctrine-seo-post-sge]]
