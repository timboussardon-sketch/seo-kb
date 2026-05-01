---
type: source
source_type: test-terrain
title: Cas clients & résultats — Preuves terrain chiffrées
aliases: [cas-clients, resultats-terrain, preuves-chiffrees-tim]
tags: [test-terrain, preuves, stats, vente, benchmark, claude-cowork]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: medium
status: stable
---

# Cas clients & résultats — Preuves terrain chiffrées

**Auteur** : Timothée Boussardon
**Type** : recueil de mesures terrain (`source_type: test-terrain`)
**Fichier raw** : `raw/notes/cas-clients-resultats.md`

---

## Contexte

Matériau chiffré consolidé pour le discours commercial Tim. Citation primaire pour toutes les stats de vente — rédaction, closing, positions, conversions LLM. Les chiffres sont **auto-rapportés** (non audités par tiers) → `confidence: medium` par défaut.

## Chiffres clés (résultats Tim)

### Rédaction — Productivité

- **Avant Claude Cowork** : ~1h30 par article
- **Après Claude Cowork** : ~45 minutes par article
- **Gain** : ÷2, soit ~20h économisées/mois sur un volume de 50 articles
- Mentionné dans 8 des 9 calls prospects (calls 1, 2, 3, 5, 6, 7, 8, 9)

### Création de sites — Claude Code

- **3 sites créés en 1 mois** avec Claude Code
- **Avant** : 2-3 mois par site
- Mentionné calls 1 (Arnaud) et 7 (Christophe)

### Closing — Vente SEO

- **Avant** : ~10% taux de closing
- **Après** : ~50% taux de closing
- **Facteur causal** : donner la roadmap data-driven au prospect (mots-clés, CPC, volume) vs vendre de la "visibilité". Cf. [[concepts/tabou-visibilite]].
- Mentionné calls 5 (Dev web) et 6 (Juliette)

### Positions — SEO organique

- **"Balle de golf"** : **top 2 devant Décathlon et Amazon**
- Workflow utilisé **depuis 6 ans** (itéré, pas changé) → preuve durabilité 2-3 ans+
- Cité dans quasi tous les calls comme proof point dominant

### Conversion LLM

- **4x plus de conversions** via ChatGPT vs Google organique
- Source externe : [[sources/2026-04-13-semrush-llm-conversion-study]]
- **Confirmation terrain Tim** : mêmes chiffres observés chez ses clients
- Caractéristique : très peu de visites mais taux de conversion "énormissime"
- Mentionné call 7 (Christophe) qui confirme le pattern sur un de ses produits Audopass

### Process clients — Rapports

- **Avant** : calls hebdomadaires avec chaque client (chronophage)
- **Après** : prompt Claude Cowork résume la semaine → email auto
- *"Je fais plus de calls"* — Tim, call 4 (Jamel)

## Résultats prospects (pré-bootcamp)

### Christophe (Audopass / Audokit)

- **Un produit convertit déjà via ChatGPT** (tracking attribution + confirmation client)
- Double vérification : outils d'attribution + question post-achat
- **Limite** : n'arrive pas à répliquer sur 20-30 autres produits
- **Insight** : le contenu ciblé (spécifique au produit qui convertit) semble être le différenciateur — à connecter avec [[concepts/data-proprietaire]] et [[concepts/surprise-gap]]

### Arnaud (sites voyage train)

- Top 1-2-3 sur "Train Luxe Afrique"
- **Forte baisse depuis août 2025**
- Hypothèse Tim : shift vers recherches IA (pas de fichier LLM, pas de page IA optimisée)
- Clientèle 65-80 ans (moins IA) mais Google copie les LLM → impact indirect

### Julien (Webmaster WordPress Paris)

- Site bien référencé (sa source principale de leads)
- Perdu quelques positions sur "Webmaster freelance Paris" (était 3e)
- Utilise [[entities/fusionn-io]] → a repris quelques positions après refonte

## Preuves externes recoupées

- **YouTube dans AI Overviews** : 30% des sources (cf. [[sources/2026-02-27-algorithme-youtube-ai-overviews]])
- **Benchmark GEO arxiv** : +41% citations, +30% stats, +30% sources d'autorité (cf. [[sources/2026-03-06-algorithme-etude-citation-ia]])
- **Étude SEMrush** : 4x conversion LLM (cf. [[sources/2026-04-13-semrush-llm-conversion-study]])

## Métriques à tracker (bootcamps futurs)

### Par participant
- Temps rédaction avant/après (min/article)
- Articles produits/mois avant/après
- Positions gagnées (top 10, top 3)
- Taux closing avant/après
- Clients SEO récurrents avant/après
- Progression Claude : Projets → Cowork → Code
- NPS

### Bootcamp global
- Taux complétion (combien finissent les 2 mois)
- Taux recommandation (bouche-à-oreille)
- Taux renouvellement / upsell
- Nombre de skills personnalisés créés

## Limites

- **Tous les chiffres sont auto-rapportés par Tim** — pas d'audit tiers
- **"Top 2 balle de golf"** : SERP volatile, position peut bouger quotidiennement
- **"10→50% closing"** : échantillon de calls non précisé (période ? nombre total ?)
- **"1h30→45min"** : mesure individuelle, pas comparable inter-rédacteur
- **Résultats participants bootcamps précédents pas documentés** — TODO à capter édition #4
- `confidence: medium` tant que pas d'audit externe ou de replication participants

## Pages liées

**Concepts** : [[concepts/data-proprietaire]] · [[concepts/workflow-redaction-8-etapes]] · [[concepts/tabou-visibilite]] · [[concepts/surprise-gap]] · [[concepts/seo-multi-plateforme]]

**Entities** : [[entities/fusionn-io]] · [[entities/bootcamp-seo-ia]] · [[entities/youtube]]

**Sources** : [[sources/2026-04-13-semrush-llm-conversion-study]] · [[sources/2026-04-13-offre-bootcamp-seo-ia]] · [[sources/2026-04-13-analyse-calls-prospects-bootcamp]] · [[sources/2026-02-27-algorithme-youtube-ai-overviews]] · [[sources/2026-03-06-algorithme-etude-citation-ia]]
