# Cluster sémantique — "SEO AEO pour l'ère des LLM"

> **Site** : organikk.co
> **Date** : 2026-04-24
> **Source** : `reflexion-organikk.md` (4 piliers : Surprise Gap · Grounding Score · pSEO · AEO)
> **Objectif business** : générer des leads qualifiés (conseil + formation) via l'autorité sémantique sur le croisement SEO × IA générative.
> **Ligne directrice** : chaque page = une micro-intention, angle conceptuel, jamais du volume.

---

## 1. Architecture — page pilier + 4 sous-piliers

```
                  [PAGE PILIER]
           Méthode SEO AEO — les 4 piliers
                        |
      ┌─────────┬───────┴────────┬─────────┐
      ▼         ▼                ▼         ▼
 SOUS-PILIER 1  SOUS-PILIER 2  SOUS-PILIER 3  SOUS-PILIER 4
  Surprise Gap  Grounding Score    pSEO         AEO
      |              |              |            |
    [4 sat.]      [4 sat.]      [4 sat.]     [4 sat.]
```

**Page pilier** : `/methode-seo-aeo` — "La méthode SEO AEO Organikk : 4 piliers pour l'ère des LLM"
Reprend et synthétise `reflexion-organikk.md`. Hub de maillage. Intention : Know (lecteur qui veut comprendre la philosophie) → CTA vers page service.

---

## 2. Cluster complet — 16 pages satellites + 3 pages commerciales

### AXE 1 — Surprise Gap

| # | Requête cible | URL | Intention | Format | Schema.org | Priorité business |
|---|---|---|---|---|---|---|
| 1.1 | "surprise score seo" | `/surprise-score-seo-definition` | Know-Simple | FAQ + définition 50 mots | `FAQPage` + `DefinedTerm` | Moyenne |
| 1.2 | "mesurer divergence contenu ia" | `/mesurer-surprise-score-page` | Know | Guide méthode + captures | `HowTo` + `Article` | Haute |
| 1.3 | "architecture titans mémoire llm" | `/titans-miras-seo` | Know (thought leadership) | Essai technique | `ScholarlyArticle` | Haute |
| 1.4 | "calculateur surprise score gratuit" | `/outils/calculateur-surprise-score` | **Do** | Outil interactif | `WebApplication` | **Très haute** |

### AXE 2 — Grounding Score

| # | Requête cible | URL | Intention | Format | Schema.org | Priorité business |
|---|---|---|---|---|---|---|
| 2.1 | "grounding score définition" | `/grounding-score-definition` | Know-Simple | FAQ + définition | `FAQPage` | Moyenne |
| 2.2 | "entités sémantiques seo" | `/optimiser-entites-semantiques` | Know | Guide 4 catégories (techniques/preuves/multimodal/divergence) | `HowTo` | Haute |
| 2.3 | "similarité cosinus google embeddings" | `/seo-vectoriel-cosinus-expliqué` | Know (thought leadership) | Guide expert | `ScholarlyArticle` | Haute |
| 2.4 | "audit entités sémantiques url" | `/outils/audit-grounding-score` | **Do** | Outil (URL → score + recommandations) | `WebApplication` | **Très haute** |

### AXE 3 — pSEO

| # | Requête cible | URL | Intention | Format | Schema.org | Priorité business |
|---|---|---|---|---|---|---|
| 3.1 | "programmatic seo définition" | `/programmatic-seo-definition` | Know-Simple | FAQ | `FAQPage` | Basse |
| 3.2 | "pseo anti thin content" | `/7-regles-pseo-anti-thin` | Know | Guide 7 règles | `HowTo` | Haute |
| 3.3 | "pseo vs content seo" | `/pseo-vs-content-seo-quand-choisir` | Know (transactionnel) | Comparatif + matrice décision | `Article` | **Très haute** |
| 3.4 | "générateur template pseo" | `/outils/generateur-template-pseo` | **Do** | Outil (variable + template → structure HTML) | `WebApplication` | **Très haute** |

### AXE 4 — AEO

| # | Requête cible | URL | Intention | Format | Schema.org | Priorité business |
|---|---|---|---|---|---|---|
| 4.1 | "aeo vs seo différence" | `/aeo-vs-seo-difference` | Know-Simple | FAQ + tableau 100 mots | `FAQPage` | Haute |
| 4.2 | "être cité par chatgpt perplexity" | `/etre-cite-par-chatgpt-perplexity` | Know (fort volume) | Guide étape par étape | `HowTo` | **Très haute** |
| 4.3 | "know simple know do framework" | `/framework-know-simple-know-do` | Know (thought leadership unique) | Essai + comparaison avec TOFU/MOFU/BOFU | `Article` | Haute |
| 4.4 | "audit aeo citation llm gratuit" | `/outils/audit-aeo-citabilité` | **Do** | Outil (URL → score citabilité LLM) | `WebApplication` | **Très haute** |

### PAGES COMMERCIALES (conversion directe)

| # | Requête cible | URL | Intention | Format | Schema.org | Priorité business |
|---|---|---|---|---|---|---|
| C.1 | "agence seo ia" / "consultant seo aeo" | `/services/conseil-seo-aeo` | Do | Page service + cas clients + CTA | `Service` + `Organization` | **Très haute** |
| C.2 | "formation seo ia générative" | `/formation-seo-aeo` | Do | Page formation + programme + CTA | `Course` + `EducationalOccupationalProgram` | **Très haute** |
| C.3 | "audit seo 360 ia" | `/services/audit-seo-360` | Do | Page service + livrables + CTA | `Service` | **Très haute** |

---

## 3. Maillage interne — règles appliquées

### Flux de liens

```
[Page pilier] ←─────── tous les satellites (1 lien sortant minimum)
    │
    ├──→ Sous-pilier 1 (Surprise) ──→ 1.1 → 1.2 → 1.3 → 1.4 (Do)
    ├──→ Sous-pilier 2 (Grounding) ──→ 2.1 → 2.2 → 2.3 → 2.4 (Do)
    ├──→ Sous-pilier 3 (pSEO)     ──→ 3.1 → 3.2 → 3.3 → 3.4 (Do)
    └──→ Sous-pilier 4 (AEO)      ──→ 4.1 → 4.2 → 4.3 → 4.4 (Do)

Chaque page Do ──→ Page commerciale (C.1, C.2 ou C.3)
Chaque page Know-Simple ──→ Page Know du même axe
Chaque page Know ──→ Page Do du même axe (règle skill)
Pages commerciales ──→ Pilier uniquement (pas de fuite)
```

### Ancres types (à varier, pas d'exact match répété)

- Vers pilier : "méthode 4 piliers", "réflexion SEO AEO", "framework Organikk"
- Vers sous-pilier : "optimisation vectorielle", "mesurer la divergence éditoriale", "scaler sans thin content"
- Vers Do : "calculer le score", "auditer sa page", "générer un template"
- Vers commercial : "accompagnement conseil", "programme de formation", "audit complet"

---

## 4. Roadmap priorisée — 90 jours

### Mois 1 — Fondations (autorité + conversion immédiate)

| Ordre | Page | Raison |
|---|---|---|
| 1 | Pilier `/methode-seo-aeo` | Hub de maillage obligatoire avant tout |
| 2 | C.1 `/services/conseil-seo-aeo` | Destination de conversion — indispensable avant traffic |
| 3 | C.2 `/formation-seo-aeo` | Destination formation |
| 4 | C.3 `/services/audit-seo-360` | Destination audit |
| 5 | 1.4 Calculateur Surprise Score | Premier lead magnet (Do) |
| 6 | 2.4 Audit Grounding Score | Second lead magnet (Do) |

**Sortie Mois 1** : 6 pages en ligne, funnel de conversion complet, 2 outils actifs.

### Mois 2 — Captation AEO + Know commerciaux

| Ordre | Page | Raison |
|---|---|---|
| 7 | 4.2 Être cité par ChatGPT/Perplexity | Fort volume + intention commerciale |
| 8 | 3.3 pSEO vs content SEO | Requête transactionnelle (comparatif) |
| 9 | 4.4 Audit AEO citabilité | Troisième outil (Do) |
| 10 | 4.1 AEO vs SEO | Captation Know-Simple à fort volume |
| 11 | 1.2 Mesurer Surprise Score | Alimente le calculateur (1.4) |
| 12 | 2.2 Optimiser entités sémantiques | Alimente l'audit (2.4) |

**Sortie Mois 2** : 12 pages, 3 outils, 2 pages comparatives qui convertissent.

### Mois 3 — Thought leadership + scale

| Ordre | Page | Raison |
|---|---|---|
| 13 | 1.3 Titans/MIRAS SEO | Positionnement autorité scientifique |
| 14 | 2.3 SEO vectoriel cosinus | Positionnement autorité technique |
| 15 | 3.4 Générateur template pSEO | Quatrième outil (Do) |
| 16 | 3.2 Les 7 règles pSEO | Guide référence de l'axe 3 |
| 17 | 4.3 Framework Know-Simple/Know/Do | Différenciation doctrinale unique |
| 18 | 1.1, 2.1, 3.1 (FAQ axes restants) | Captation AEO résiduelle |

**Sortie Mois 3** : 19 pages, 4 outils, autorité doctrinale établie sur les 4 piliers.

---

## 5. KPI de succès du cluster

| Métrique | Cible 90 jours | Cible 180 jours |
|---|---|---|
| Pages indexées / créées | > 90 % | > 95 % |
| Citations LLM (Perplexity, ChatGPT, Google AIO) | 3+ pages citées | 10+ pages citées |
| Leads générés via outils (C.1 + C.2 + C.3) | 20+ leads | 80+ leads |
| Grounding Score moyen cluster | > 0,75 | > 0,85 |
| Surprise Score moyen cluster | > 0,60 | > 0,70 |
| Taux de conversion page Do → page commerciale | > 8 % | > 12 % |

---

## 6. Principes MECE respectés

- **Mutuellement exclusif** : aucun doublon d'angle. Chaque page = une micro-intention unique.
- **Collectivement exhaustif** : les 4 piliers + Know-Simple/Know/Do couvrent l'intégralité de l'intention "SEO pour l'IA".
- **Revue à 6 mois** (prochaine : 2026-10-24) pour combler les gaps détectés via GSC + requêtes LLM.

---

## 7. Différenciation via Surprise Gap — angles doctrinaux uniques à Organikk

Chaque page Know du cluster intègre **au minimum un angle à Haute Surprise** non couvert par le SERP actuel :

| Axe | Angle unique Organikk |
|---|---|
| Surprise | Lien Titans/MIRAS ↔ SEO (aucun acteur n'en parle) |
| Grounding | Framework 4 catégories d'entités (techniques/preuves/multimodal/divergence) |
| pSEO | 7 règles non-négociables anti-thin formalisées |
| AEO | Framework Know-Simple/Know/Do qui remplace TOFU/MOFU/BOFU |

Sans ces angles = pages Know génériques → ignorées par les LLM → échec du cluster AEO.

---

*Cluster vivant — à réviser après chaque vague d'indexation.*
