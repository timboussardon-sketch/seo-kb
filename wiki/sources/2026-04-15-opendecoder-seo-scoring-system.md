---
type: source
source_type: doctrine
title: "OpenDecoder SEO Scoring System v2 — système de notation 4 axes"
aliases: [opendecoder-scoring, seo-scoring-system, opendecoder-v2]
tags: [doctrine-tim, scoring, audit, opendecoder, llm-judge, qualite-contenu]
created: 2026-04-15
updated: 2026-05-01
sources: 1
confidence: high
status: stable
---

# OpenDecoder SEO Scoring System v2

**Type** : système de notation propriétaire de Tim, inspiré du paper OpenDecoder (Mo et al., 2026). Référence officielle pour tout audit/évaluation de contenu SEO avant publication.
**Fichier raw** : `raw/scoring/opendecoder-seo-scoring-system.md` (947 lignes)
**Date** : ajouté à la KB le 2026-04-15 (cf log entry `doctrine-add`), formalisé comme source wiki le 2026-05-01

## Principe fondateur

> Comme OpenDecoder pondère explicitement chaque document pour guider l'attention du LLM, ce système pondère explicitement chaque dimension d'un contenu SEO pour guider les décisions d'optimisation.

**Principe d'exécution** : le LLM est le moteur de scoring. Aucun scraping SERP. Chaque évaluation repose sur des **requêtes LLM structurées** qui exploitent la connaissance sémantique du modèle — exactement comme dans le paper où c'est le LLM qui juge la qualité des documents, pas un outil externe.

## Architecture globale

**Input** : contenu de la page (texte + structure) + mot-clé cible + (optionnel) données GSC

**4 scores** :
- **S_Pertinence** (dominant) — équivalent du Retriever Score
- **S_Qualité** (bonus) — équivalent du LLM Ranking Score
- **S_Potentiel** (bonus) — équivalent du QPP Score
- **S_AEO** (bonus) — extension GEO Sentinel (survie face aux moteurs IA)

**Formule d'agrégation** (adaptée du paper + GEO Sentinel) :

```
S_final = S_Pertinence + 0.5 × (S_Qualité + S_Potentiel + S_AEO)
S_100   = (S_final / 2.5) × 100
```

Pertinence = coeff 1 (dominant). Les 3 autres = coeff 0.5 chacun.

## Score 1 — S_Pertinence (Relevance Score, dominant)

Équivalent OpenDecoder S_Ret. Mesure l'alignement sémantique contenu ↔ intention.

| Sous-score | Poids | Méthode |
|---|---|---|
| 1.1 Couverture des entités (S_ent) | 0.40 | LLM génère entités attendues (primaires/secondaires/tertiaires) puis matche avec le contenu |
| 1.2 Alignement d'intention (S_int) | 0.25 | LLM classifie intention (Know-Simple/Know/Do/Commercial) puis matrice format×intention |
| 1.3 Couverture du champ sémantique (S_sem) | 0.25 | LLM génère 5-10 clusters thématiques attendus puis évalue couverture (1.0/0.5/0) + bonus Hn |
| 1.4 Signaux on-page (S_onpage) | 0.10 | (mot-clé exact dans title/H1/URL/early-body, etc.) |

## Score 2 — S_Qualité (LLM Ranking Score)

Mesure la qualité éditoriale et l'expertise perçue par un LLM-juge.

Sous-scores indicatifs :
- 2.1 Profondeur d'expertise (verbatim experts, cas chiffrés, méthodes nommées)
- 2.2 Originalité (différentiation vs centroïde SERP — cohérent avec [[concepts/surprise-gap]])
- 2.3 Lisibilité (rythme, longueur phrases, anti-AI-writing — cohérent avec [[concepts/anti-ai-writing]])
- 2.4 Sourcing et factualité (chiffres + sources primaires)

## Score 3 — S_Potentiel (QPP Score)

Estimation du potentiel de gain via croisement de signaux SERP/GSC.

Sous-scores indicatifs :
- 3.1 Position GSC actuelle vs faisabilité top 3
- 3.2 Concurrence (gap d'autorité, qualité contenus rangs 1-10)
- 3.3 Volume + CPC + intention transactionnelle (cohérent avec mots-clés actionnels [[sources/2026-04-17-organikk-process-seo-b2b-2026]])

## Score 4 — S_AEO (GEO Sentinel extension)

Survie face aux moteurs IA — propre à Tim, pas dans le paper original.

Sous-scores indicatifs :
- 4.1 Citabilité LLM (passages atomiques 100-150 mots, format extractible)
- 4.2 Bloc authorship Position 0 (~50 mots)
- 4.3 Schema.org adapté (FAQPage, HowTo, Article, etc.)
- 4.4 Ancrage data propriétaire (signaux humains non-fakeable)

## 15 prompts LLM structurés

Le système couvre 15 prompts prédéfinis pour : entités attendues, classification intention, clusters sémantiques, signaux on-page, E-E-A-T, profondeur, structure Hn, lisibilité, paysage concurrentiel, formats attendus, opportunités, position GSC, etc. Chaque prompt a un format de sortie strict pour parsing automatique.

## Règle d'usage

- **Utiliser systématiquement** ce scoring pour toute évaluation/audit de contenu **avant publication**
- **Pas de scoring ad-hoc** parallèle
- Mise à jour du fichier `raw/scoring/opendecoder-seo-scoring-system.md` **uniquement sur instruction explicite Tim**

## Articulation avec les autres skills

- **APRÈS** rédaction par `seo-workflow-article` ou `article-engine-pipeline` → garde-fou évaluation finale
- §11 anti-AI-writing s'applique en parallèle pendant l'évaluation S_Qualité sous-score 2.3
- `kb-semantic-search` utilisable en amont pour vérifier ce que la KB sait déjà sur la requête cible
- Skill chaîné avec [[entities/qadence-seo-agent]] (tool `score_content` qui appelle l'engine OpenDecoder v2 — obligatoire après tout livrable contenu)

## Déclencheurs

"score ce contenu", "évalue cette page", "audit avant publication", "scoring SEO", "note cette rédaction", "évalue son potentiel LLM/IA"

## Apports à la KB

- Première formalisation d'un **système de scoring quantifié 4 axes** propriétaire à Tim, inspiré du paper OpenDecoder
- Connecte deux mondes : la rédaction (skills `seo-workflow-article` et al.) et l'évaluation (cet OpenDecoder)
- Validation académique du **LLM-as-Judge** pour le scoring SEO (vs scraping SERP avec outils tiers)
- Cohérent avec [[concepts/grounding-score]] (le S_Pertinence dominant, c'est exactement le concept)
- Cohérent avec [[concepts/surprise-gap]] (le sous-score originalité 2.2)

## Limites

- Paper OpenDecoder (Mo et al., 2026) **non encore ingéré** en KB — à ajouter pour audit fidélité de la transposition
- 15 prompts détaillés mais pas de benchmark public sur la fiabilité du scoring vs juges humains
- Coefficient 0.5 sur les 3 scores secondaires : choix empirique de Tim, pas validé statistiquement
- Pas de mesure terrain à date (combien de pages auditées, taux de corrélation score → ranking)

## Pages liées

[[entities/qadence-seo-agent]] (tool `score_content` appelle ce système) · [[concepts/grounding-score]] · [[concepts/surprise-gap]] · [[concepts/anti-ai-writing]] · [[concepts/data-proprietaire]] · [[concepts/aeo]] · [[concepts/passage-ranking]] · [[concepts/fully-meets]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[sources/2026-04-13-titans-architecture-google-deepmind]] · [[sources/2026-04-13-miras-architecture]]
