---
type: concept
title: Anti-AI Writing (anti-patterns IA)
aliases: [anti-ai-writing, anti-patterns-ia, wikipedia-signs-ai-writing]
tags: [redaction, anti-patterns, qualite, doctrine-tim]
created: 2026-04-12
updated: 2026-06-19
sources: 9
confidence: high
status: stable
---

# Anti-AI Writing (anti-patterns IA)

Ensemble de règles pour éliminer les patterns d'écriture détectables comme générés par IA. Basé sur le guide Wikipedia "Signs of AI Writing" + les règles propriétaires de Tim. Appliqué systématiquement aux étapes 6 et 8 du [[concepts/workflow-redaction-8-etapes]].

## Règle fondamentale — factuel, sans narratif

Droit au but, ultra factuel. On entre par la réponse (answer-first), jamais par une mise en situation. **Le narratif est interdit dans le contenu** : pas de storytelling, pas de « la plupart des gens font X », pas de « imagine que », pas de décor ni de scénario qui raconte une histoire avant d'arriver au fait. Faits, étapes, chiffres, position tranchée, directement. Tout paragraphe qui raconte au lieu d'affirmer un fait est à supprimer. Cumulé avec la doctrine GEO (réponse extractible, pyramide inversée) et la voix Tim ([[methode-organikk-4-piliers]]).

## Source de référence

**Fichier raw** : `raw/notes/tim-anti-ai-writing-style.md` (139 KB)

Le guide Wikipedia (descriptif, pas prescriptif) identifie les patterns statistiques des LLM — régression vers la moyenne, puffery, analyses superficielles, langage promotionnel. La logique : les LLM infèrent la suite la plus **statistiquement probable** → le résultat tend vers le générique et l'exagéré. Un contenu qui ressemble à du LLM **est par définition Low Surprise** ([[concepts/surprise-metric]]).

## Patterns interdits (synthèse Tim + Wikipedia)

### Mots interdits
"crucial", "pivotal", "groundbreaking", "comprehensive", "landscape", "vibrant", "nestled", "renowned", "il est important de noter", "n'oublions pas que", "dans un monde en pleine évolution"

### Structures interdites
- Bullet points décoratifs dans le corps du texte (prose continue obligatoire)
- Bold excessif sur les premiers mots de chaque paragraphe
- Règle de 3 systématique (3 raisons, 3 étapes, 3 avantages)
- Conclusion-résumé qui répète ce qui vient d'être dit
- Méta-intro ("Dans cet article, nous allons voir...")
- Émojis dans les titres ou le corps

### Oppositions rhétoriques interdites
Tournures qui n'apportent aucune information et sonnent « profond » à vide. Bannies : « pas X mais Y », « ce n'est pas X, c'est Y », « plutôt que », « au lieu de », « ne cherchez pas à », « l'objectif n'est pas ». On dit directement, en affirmatif, ce qu'il faut faire.
- ❌ « Racontez une histoire vraie plutôt que de poser une accroche. »
- ✅ « Ajoutez un cas client chiffré en intro. »

### Verbes d'action vagues interdits (sans objet précis)
Bannis dès qu'ils sont employés seuls : améliorer · optimiser · renforcer · travailler · développer · valoriser · mettre en avant. Toujours suivis de quoi exactement, où, et comment le mesurer.
- ❌ « Il faut optimiser la page et renforcer le maillage. »
- ✅ « Ajoute 3 liens internes depuis A, B et C vers /tarifs (ancre « tarifs formation ») pour faire remonter sa position moyenne, aujourd'hui 14. »

### Enchaînement imposé
Chaque idée suit **Constat → preuve → action**. Jamais **Vision → inspiration → storytelling** (grande idée inspirante, mise en récit, envolée). Tout conseil cite un élément concret, une action observable et un effet expliqué, sinon il n'est pas livrable.

### Patterns Wikipedia
- **Undue emphasis on significance** : "stands as", "is a testament", "a vital/significant/crucial role", "underscores its importance", "reflects broader", "evolving landscape", "indelible mark"
- **Superficial analyses** : participiales en "-ing" ("highlighting...", "ensuring...", "reflecting...")
- **Promotional language** : puffery, peacock words
- **Regression to the mean** : le spécifique remplacé par le générique ("inventor of the first train-coupling device" → "a revolutionary titan of industry")

## Pourquoi c'est un garde-fou SEO

Un contenu qui **ressemble à du LLM** a une [[concepts/surprise-metric]] ≈ 0 par définition : c'est la sortie la plus probable du modèle, donc la moins surprenante. Les [[entities/quality-raters-guidelines]] p.42 pénalisent le contenu "sans effort". Éliminer les anti-patterns IA est **un prérequis** au [[concepts/surprise-gap]], pas un bonus cosmétique.

## Pages liées

[[sources/2026-04-25-tim-ton-de-voix-extraction-terrain]] (35 patterns positifs Tim sur ~12 000 mots verbatim — volet positif complémentaire) · [[sources/2026-04-30-tim-posts-linkedin-batch]] (corpus LinkedIn cohérent avec patterns Substack) · [[sources/2026-04-13-geo-aggarwal-2024]] (confirmation empirique : Keyword Stuffing −8 % PAWC / −9 % Perplexity) · [[sources/2026-04-13-google-quality-raters-guidelines-2026]] (norme p.42 effort-less) · [[sources/2026-04-15-scan-arxiv-15-avril]] (LLMSEO Bench : black-hat 99,78 % filtré + Retrieval Collapse) · [[sources/2026-04-25-scan-arxiv-25-avril]] (validation académique étendue) · [[sources/2026-04-22-algorithme-core-update-fermes-ia]] (Core Update mars 2026 : −40 à −80 % sur fermes IA industrialisées) · [[sources/2026-03-31-tim-profil-et-regles]] · [[sources/2026-03-31-tim-workflow-redaction]] · [[concepts/workflow-redaction-8-etapes]] · [[concepts/surprise-metric]] · [[concepts/surprise-gap]] · [[concepts/answer-first-pattern]] · [[concepts/retrieval-collapse]] · [[entities/quality-raters-guidelines]] · [[entities/naver]]
