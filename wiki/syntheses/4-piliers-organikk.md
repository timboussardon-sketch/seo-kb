---
title: 4 Piliers Organikk — Réflexion fondatrice
auteur: Timothée Boussardon
date: 2026-04-24
type: doctrine
statut: vivant
objet: Structuration complète de la réflexion SEO/AEO Organikk articulée autour de 4 piliers fondamentaux et leurs interconnexions.
source_originale: raw/notes/reflexion-organikk-source.md (fichier source Cursor de Tim — ingéré 2026-04-25)
---

# RÉFLEXION ORGANIKK — 4 Piliers

**Auteur :** Timothée Boussardon
**Date :** 2026-04-24
**Objet :** Structuration complète de la réflexion SEO/AEO Organikk articulée autour de 4 piliers fondamentaux et leurs interconnexions.

---

## 1. SURPRISE GAP — Pourquoi on lit

**Fondement théorique :** architecture Titans / MIRAS. La mémoire d'un LLM ne se met à jour que sur les inputs à haute surprise. Ce qui est déjà consensus traverse le modèle sans laisser de trace.

**Principe opérationnel :** mesurer la divergence entre ce que dit la page et le consensus SERP. Ce que personne n'a dit > ce que tout le monde dit mieux.

**Leviers :**
- Inversions expertes (retourner une vérité admise)
- Données terrain non-sourcées ailleurs (propriétaires)
- Verbatims Haute Surprise (pain points, objections inattendues)
- Angle conceptuel systématique — jamais le volume

**KPI :** Surprise Score par passage / par page.

---

## 2. GROUNDING SCORE — Pourquoi on rank

**Fondement théorique :** similarité cosinus entre le vecteur d'embedding de la page et le vecteur d'embedding de la requête (modèles Google type Gemini Embedding).

**Principe opérationnel :** aligner mathématiquement l'embedding via les entités sémantiques attendues par l'intention cible.

**Leviers — 4 catégories d'entités :**
- Techniques (jargon métier, termes spécialistes)
- Preuves quantitatives (chiffres, benchmarks, ratios)
- Vecteurs multimodaux (images, tableaux, vidéos, schémas)
- Divergence (éléments à Haute Surprise qui éloignent du centroïde SERP — couplage avec pilier 1)

**Méthode :** Triade SERP (analyse des 3 premiers résultats pour extraire le vecteur dominant, puis divergence contrôlée).

**KPI :** Grounding Score vs. top 3 du SERP.

---

## 3. pSEO — Comment on scale

**Fondement théorique :** 1 template + 1 variable = N pages sur longue traîne.

**Principe opérationnel :** industrialiser la couverture d'intention sans jamais tomber dans le thin content. Chaque page doit mériter son indexation individuellement.

**Leviers — 7 règles non-négociables :**
- Anti-thin content par design (minimum de valeur unique par page)
- Données terrain obligatoires (pas de génération LLM brute)
- Sourcing vérifiable
- Canonical strict
- Maillage différenciant (pas de patterns répétitifs)
- Surprise Score minimum par page
- Grounding Score minimum par page

**Pipeline :** identifier modèle scalable → matrice priorisation → mots-clés par modèle → exécution 90 jours.

**KPI :** ratio pages indexées / pages créées > 85 %.

---

## 4. AEO — Comment on gagne les moteurs de réponse

**Fondement théorique :** RRF (Reciprocal Rank Fusion) + framework Know-Simple / Know / Do (remplace TOFU/MOFU/BOFU, obsolètes à l'ère de l'Agentic Search).

**Principe opérationnel :** architecture MECE (Mutually Exclusive, Collectively Exhaustive) lisible par les agents IA autonomes — SGE, Perplexity, ChatGPT, Claude.

**Leviers :**
- Cluster sémantique Know-Simple / Know / Do
- Passage Ranking (structure Hn optimisée pour extraction atomique)
- Bloc authorship extractible Position 0 (~50 mots)
- Product-Led SEO pour décrocher la note "Fully Meets" des Quality Raters
- Fact-check et sourcing systématique (les LLM citent les sources vérifiables)

**KPI :** taux de citation dans les réponses génératives (Perplexity, ChatGPT, Google AI Overviews).

---

## LES 6 INTERCONNEXIONS

| Croisement | Produit |
|---|---|
| Surprise × Grounding | Contenu à la fois différenciant ET extractible |
| Surprise × pSEO | Anti-thin content par design — chaque page apporte un angle |
| Surprise × AEO | Citation préférentielle par les LLM (ils citent ce qui diverge) |
| Grounding × pSEO | Pertinence vectorielle garantie à l'échelle |
| Grounding × AEO | Alignement sur l'intention à chaque niveau du cluster |
| pSEO × AEO | Scalabilité × couverture MECE des intentions |

---

## PYRAMIDE D'EXÉCUTION

```
            AEO (architecture)
           ↑
     pSEO (scale)
    ↑
  GROUNDING (pertinence)
 ↑
SURPRISE (fondation)
```

**Règle de dépendance stricte :**
- Sans Surprise, le Grounding ne sert à rien → pages pertinentes mais génériques, ignorées par les LLM.
- Sans Grounding, le pSEO produit du thin → pénalités.
- Sans pSEO, l'AEO ne couvre pas l'étendue de l'intention → cluster incomplet.
- Sans AEO, tout le reste reste du SEO classique → invisible en Agentic Search.

---

## MATRICE DES SKILLS ↔ PILIERS

| Skill | Surprise | Grounding | pSEO | AEO |
|---|:---:|:---:|:---:|:---:|
| seo-workflow-article | ✅ | ✅ | — | ✅ |
| seo-entites-vectorielles | — | ✅ | — | ✅ |
| seo-programmatique-pseo | ✅ | ✅ | ✅ | — |
| seo-cluster-aeo | — | ✅ | — | ✅ |
| seo-peurs-objections | ✅ | — | — | — |
| seo-quick-win | — | ✅ | — | — |
| seo-cannibalisation | — | — | ✅ | ✅ |
| maillage-interne-gsc | — | — | ✅ | ✅ |
| seo-brief-contenu | ✅ | ✅ | — | ✅ |
| seo-product-led-seo | ✅ | — | — | ✅ |
| article-engine-pipeline | ✅ | ✅ | — | ✅ |

---

## CADRE DE DÉCISION — Par où commencer ?

1. **Audit Grounding** → la page s'aligne-t-elle avec l'intention ? (`seo-entites-vectorielles`)
2. **Audit Surprise** → apporte-t-elle un angle unique vs. SERP ? (`seo-workflow-article`, étape 1)
3. **Audit AEO** → est-elle citable par un LLM ? (bloc authorship, passage ranking)
4. **Audit pSEO** → peut-on scaler ce format ? (`seo-programmatique-pseo`)

Toujours dans cet ordre. La fondation (Surprise + Grounding) avant la scalabilité (pSEO + AEO).

---

*Réflexion vivante — mise à jour à mesure que les moteurs évoluent.*
