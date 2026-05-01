---
type: synthesis
title: Doctrine SEO post-SGE — thèse unifiée
aliases: [doctrine-seo-post-sge, these-unifiee-seo-ia]
tags: [synthese, doctrine-tim, seo-ia, geo, grounding-score, surprise-gap, titans]
created: 2026-04-12
updated: 2026-04-12
sources: 8
confidence: medium
status: stable
---

# Doctrine SEO post-SGE — thèse unifiée

**Première synthèse** de cette KB. Compile 8 sources, 13 concepts, et 9 entities en une thèse opérationnelle. `confidence: medium` — la plupart des mécanismes sont des hypothèses par transfert d'architecture, soutenus par un seul benchmark empirique (arxiv:2311.09735).

---

## Le problème (2026)

La rédaction SEO est devenue une **commodité**. Claude, GPT-4, et les LLM en général produisent du contenu qui surpasse le rédacteur moyen. 90 % des articles SEO générés par IA sont des reformulations de contenu existant [[sources/2026-03-17-algorithme-pourquoi-article-ne-rank-pas]].

Les [[entities/quality-raters-guidelines]] p.42 classent ce contenu "sans effort" à la **note la plus basse** [[sources/2026-03-11-algorithme-data-claude-perplexity]]. Google déploie en mars 2026 une Core Update qui renforce les signaux E-E-A-T et l'autorité thématique [[sources/2026-03-06-algorithme-etude-citation-ia]].

Le SEO passe d'un **SEO de rédaction** à un **SEO d'information** [[sources/2026-03-17-algorithme-pourquoi-article-ne-rank-pas]].

---

## Le cadre architectural : pourquoi c'est structurel, pas conjoncturel

### L'architecture Titans/MIRAS ([[entities/titans]], [[entities/google-deepmind]])

L'architecture Titans introduit la **test-time memorization** : le modèle mémorise pendant l'inférence uniquement les infos à fort **gradient de surprise** [[concepts/surprise-metric]] [[sources/2026-04-11-seo-ia-tim]].

3 couches de mémoire :
- **Core** (attention court-terme) — focus immédiat
- **Neural Memory** (long-terme) — faits marquants à fort gradient
- **Persistent Memory** — connaissances fixes (marques fortes, faits invariants)

Le **Weight Decay** (forgetting gate) efface les contenus anciens → le biais de récence n'est pas un réglage arbitraire de Google mais une **contrainte architecturale** [[concepts/weight-decay]].

### Caveat

Titans/MIRAS est une architecture de **recherche DeepMind**, pas de Google Search en production. Toutes les implications SEO sont des **hypothèses par transfert** [[sources/2026-04-11-seo-ia-tim]]. Si Google Search n'adopte jamais cette architecture, le cadre perd son mécanisme. Mais la logique reste utile comme heuristique car elle est **cohérente avec les observations empiriques** (benchmark GEO, biais de récence Metehan, QRG p.42).

---

## Les 4 piliers de la doctrine

### Pilier 1 — Grounding Score : proximité + divergence

[[concepts/grounding-score]] = similarité cosinus intention ↔ page (pertinence vectorielle). Mais la pertinence seule est insuffisante — une page 100 % pertinente mais redondante a un gradient ≈ 0. Le **sweet spot** est **grounded et surprenant** : vecteur proche de l'intention + faits nouveaux à chaque section.

**5 mots-clés vectoriels** (pas sémantiques) de ton produit → découper en micro-intentions → pages prioritaires [[sources/2026-03-17-algorithme-pourquoi-article-ne-rank-pas]].

### Pilier 2 — Surprise Gap : l'info manquante

[[concepts/surprise-gap]] = apporter l'information que l'intention de la query suggère mais que le modèle n'a pas dans sa Persistent Memory. C'est cette info qui déclenche un fort gradient de surprise et force la mémorisation.

> "Le SEO consiste à apporter l'information manquante qui force le modèle à mettre à jour ses poids en temps réel pour inclure ta marque dans sa réponse." [[sources/2026-04-11-seo-ia-tim]]

L'ère de la **singularité informationnelle** : la compétition ne se joue plus sur le volume/qualité rédactionnelle mais sur l'**unicité** de l'info.

### Pilier 3 — Information Gain : le standard mesurable

[[concepts/information-gain]] = la version officielle Google du même concept. Benchmark empirique (arxiv:2311.09735, 10 000 requêtes, 25 domaines) [[sources/2026-03-06-algorithme-etude-citation-ia]] :

| Stratégie | Impact visibilité IA |
|---|---|
| **Citations** | **+41 %** |
| **Statistiques** | **+30 %** |
| **Sources d'autorité** | **+30 %** |

Ce sont les **seuls chiffres empiriques** de cette KB liant une stratégie de contenu à une mesure de visibilité IA. L'IA vérifie par **atomisation** — chaque claim est découpé en fait isolé et vérifié indépendamment.

### Pilier 4 — Data Propriétaire : le moat

[[concepts/data-proprietaire]] = chiffre terrain, résultat client, observation unique. C'est la **matière première** du Surprise Gap et de l'Information Gain. Sans data propriétaire, pas de gradient de surprise suffisant.

> "Si je crée le même site que vous demain, sans expertise, je serai toujours derrière." [[sources/2026-03-04-algorithme-lancer-site-sans-cms]]

---

## Le framework opérationnel : Ingénierie Sémantique Inversée

[[concepts/ingenierie-semantique-inversee]] — framework propriétaire de Tim, mis à jour à la lumière de Titans/MIRAS :

| Brique | Évolution Titans | Action |
|---|---|---|
| Vecteurs sémantiques | **Vecteurs de surprise** | Divergence, pas juste pertinence |
| Document ranking | **Neural Memory Entry** | High gradient au **début et à la fin** |
| Micro-intentions | **Outlier Handling (YAAD)** | Data structurée **impeccable** |
| Cluster sémantique | **Associative Memory Chain** | Low surprise contextuelle + High surprise informationnelle |

**SEO multi-plateforme** : site + YouTube + LinkedIn [[concepts/seo-multi-plateforme]]. YouTube est cité dans ~30 % des AI Overviews [[entities/youtube]]. Le SEO IA est multi-vectoriel (texte, image, son).

---

## L'infrastructure : le pattern wiki persistant

[[concepts/persistent-wiki-vs-rag]] (pattern Karpathy) n'est pas juste une méthode de gestion de connaissances — c'est un **mode de production de contenu GEO-optimisé par construction** [[queries/2026-04-12-wiki-pattern-vs-grounding-score]] :

- **Agrégation** → enrichit le vecteur de grounding
- **Updates incrémentaux** → maintient le gradient de surprise non nul
- **Fraîcheur** → résiste au weight decay
- **Sources citées** → satisfait le benchmark information gain
- **Structure Associative Memory Chain** → produite naturellement par le wiki

---

## Grille de confiance

| Composant | Base | Confiance |
|---|---|---|
| Architecture Titans/MIRAS (surprise metric, weight decay) | Paper Google DeepMind | `high` (paper solide) |
| Transfert Titans → Google Search/SGE | Hypothèse Tim | `low` (non confirmé en prod) |
| Benchmark +41%/+30%/+30% | Étude arxiv:2311.09735, 10k queries | `high` |
| Biais de récence 1-5 ans | Citation secondaire Metehan | `low` (non ingéré) |
| QRG p.42 "sans effort" = pénalisé | Google officiel | `high` |
| Wiki persistant > page statique pour GEO | Inférence structurelle | `low` (non testé) |
| Data propriétaire = moat compétitif | Observation Tim + logique | `medium` |

**Confiance globale de la synthèse : `medium`**. Le cadre est **cohérent et testable**, mais l'élément central (transfert Titans → SEO) repose sur une hypothèse non validée.

---

## Questions ouvertes (futures queries/sources)

1. **Test terrain wiki entity vs page statique** — valider l'hypothèse grounding + surprise → plus citée
2. **Article Metehan freshness scoring** — solidifier weight decay + biais de récence
3. **Paper retrieval vectoriel SGE** — confirmer ou infirmer le transfert Titans
4. **Export GSC** pour data propriétaire — démontrer le compoundage appliqué au monitoring
5. **Synthèse multi-clients** — le framework tient-il sur différents secteurs (B2B, e-commerce, local) ?

---

## Pages liées

**Sources** : [[sources/2026-04-11-karpathy-llm-wiki]] · [[sources/2026-04-11-seo-ia-tim]] · [[sources/2026-03-06-algorithme-etude-citation-ia]] · [[sources/2026-03-11-algorithme-data-claude-perplexity]] · [[sources/2026-03-17-algorithme-pourquoi-article-ne-rank-pas]] · [[sources/2026-03-04-algorithme-lancer-site-sans-cms]] · [[sources/2026-02-27-algorithme-youtube-ai-overviews]] · [[sources/2026-03-13-algorithme-agents-seo-consultants]]

**Concepts** : [[concepts/grounding-score]] · [[concepts/surprise-metric]] · [[concepts/surprise-gap]] · [[concepts/information-gain]] · [[concepts/data-proprietaire]] · [[concepts/weight-decay]] · [[concepts/ingenierie-semantique-inversee]] · [[concepts/seo-multi-plateforme]] · [[concepts/persistent-wiki-vs-rag]]

**Entities** : [[entities/titans]] · [[entities/google-deepmind]] · [[entities/youtube]] · [[entities/quality-raters-guidelines]] · [[entities/metehan]]

**Query** : [[queries/2026-04-12-wiki-pattern-vs-grounding-score]]
