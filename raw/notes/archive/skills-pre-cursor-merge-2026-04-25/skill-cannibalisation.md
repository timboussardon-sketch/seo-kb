---
type: skill
source_type: doc-interne
title: "Skill : Cannibalisation SEO"
aliases: ["Cannibalisation", "keyword-cannibalism"]
tags: ["skill", "cannibalisation", "gsc", "architecture", "maillage"]
created: "2026-04-12"
updated: "2026-04-12"
sources: []
confidence: haute
status: actif
---

# Skill — Cannibalisation SEO

## Quand déclencher
Deux pages se concurrencent sur les mêmes mots-clés ou intentions. Chutes de positions inexpliquées, CTR qui stagne malgré le volume.

> Trigger : "cannibalisation", "deux pages sur le même mot-clé", "je rankais mieux avant", "pages en compétition interne".

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Export GSC Requêtes — filtré par URL, 90j | ✅ Oui |
| Liste des URLs (scraping ou sitemap) | Recommandé |
| Contexte stratégique (pilier vs satellite) | Recommandé |

## Pipeline (5 étapes)

1. **Identifier les conflits** — requêtes qui déclenchent 2+ URLs dans la GSC
2. **Classifier le type** :
   - **(A) Mot-clé exact** — deux pages sur la même requête précise
   - **(B) Même intention** — deux pages répondent à la même intention
   - **(C) Proximité sémantique** — sujets proches sans conflit direct
   - **(Triade SERP)** — opportunité, pas conflit
3. **Analyser les métriques** — position, impressions, clics, CTR par page
4. **Évaluer l'architecture** — pilier vs satellite, objectif business
5. **Recommander l'action** :

| Situation | Action |
|-----------|--------|
| Type A + perdante faible | Redirection 301 |
| Type A + deux fortes | Fusion + 301 |
| Type B + micro-intentions distinctes | Différenciation + maillage croisé |
| Type C | Renforcement maillage vers pilier |
| Triade SERP | Aucune action — optimiser chaque angle |

## Output obligatoire

```
CANNIBALISATION DÉTECTÉE
Requête : '[requête]' — Type : (A/B/C/Triade)
| URL | Position | Impressions | Clics | CTR | Statut |

→ Diagnostic : [explication]
→ Action : [action précise + 3 étapes d'implémentation]
```

## Règles absolues

- ❌ Recommander une 301 sans analyser les métriques des deux pages
- ❌ Traiter toutes les cannibalisations de la même façon
- ❌ Confondre duplication de contenu et cannibalisation
- ❌ Fusionner des pages avec micro-intentions distinctes
- ✅ Identifier les Triades SERP comme opportunités, pas comme problèmes

## Concepts liés

[[triade-serp]] · [[rrf]] · [[maillage-interne]] · [[intention-recherche]] · [[gsc-export]]
