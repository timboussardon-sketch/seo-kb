---
type: source
source_type: article
title: "DATA avec Claude + Perplexity (Algorithme #4)"
aliases: [algorithme-data-claude-perplexity]
tags: [newsletter-algorithme, data-proprietaire, fact-checking, low-surprise, quality-raters]
created: 2026-04-12
updated: 2026-04-12
sources: 1
confidence: high
status: stable
---

# DATA avec Claude + Perplexity

**Newsletter** : Algorithme #4 · **Date** : 11 mars 2026 · **Auteur** : Tim
**URL** : `https://algorithme.substack.com/p/data-avec-claude-perplexity`
**Fichier raw** : `raw/articles/algorithme/algorithme-data-claude-perplexity.md`

## Données clés

### Low Surprise confirmé par les Quality Raters
- "Republier ce qui existe déjà, c'est du **Low Surprise**. Le modèle LLM le lit, ne le mémorise pas, et l'oublie." → **confirmation directe** de [[concepts/surprise-metric]] dans le vocabulaire de Tim
- **[[entities/quality-raters-guidelines]] p.42** : un contenu "sans effort" qui reprend mécaniquement des informations existantes → **note la plus basse**. "Détruit tous ceux qui créent du contenu IA sans contexte, sans data, sans expertise."

### Data propriétaire = le moat
- Pour être cité : apporter de la **data propriétaire** = chiffre terrain, résultat client, observation unique ([[concepts/data-proprietaire]])
- **Données internes** (tarifs, services, procédures) : les plus risquées car hallucinations = fausse promesse commerciale
- **Données externes** (météo, événements, distances) : plus faciles à sourcer via API (climate-data.org, .gouv…)

### Vérification atomique par les IA
- L'IA **atomise** chaque affirmation. Exemple Tesla : "autonomie 600 km + coûte 90 000 €" → 3 atomes vérifiés séparément (modèle, autonomie, prix)
- Si tu écris "la Tesla est une voiture chère avec une bonne autonomie" → **tu ne seras pas cité** (pas assez atomique)
- → Confirme [[concepts/information-gain]] : l'IA reward la précision, pas la prose

### Process fact-checking Perplexity
- Prompt fact-checking complet fourni (isoler affirmations vérifiables, verdict exact/approximatif/faux, reformulation sécurisée, sources tierces)
- Règle d'or : données internes = validées par toi seul. Données scrapées = validées par source tierce. Ne pas mélanger.
- Stockage dans NotebookLM ou projet Claude pour réutilisation

## Apports à la KB

- **Première mention de "Low Surprise" par Tim** dans un contexte SEO publié → ancre [[concepts/surprise-metric]] hors du paper Titans, dans la pratique quotidienne
- Le process fact-checking est un workflow opérationnel qui renforce la §2 d'`AGENTS.md` (preuves atomiques)
- La vérification atomique = la version SEO-praticien du "gradient d'information" théorique de [[concepts/surprise-metric]]

## Pages liées

[[concepts/surprise-metric]] · [[concepts/data-proprietaire]] · [[concepts/information-gain]] · [[entities/quality-raters-guidelines]] · [[concepts/surprise-gap]]
