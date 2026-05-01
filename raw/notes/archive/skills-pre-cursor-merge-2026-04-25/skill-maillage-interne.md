---
type: skill
source_type: doc-interne
title: "Skill : Maillage Interne GSC"
aliases: ["Maillage interne", "cocon sémantique", "maillage-gsc"]
tags: ["skill", "maillage", "cocon-semantique", "gsc", "pagerank-interne"]
created: "2026-04-12"
updated: "2026-04-12"
sources: []
confidence: haute
status: actif
---

# Skill — Maillage Interne GSC

## Quand déclencher
Analyse et optimisation du maillage interne depuis les données GSC. Hiérarchie page mère/fille/petite-fille selon la méthode Boussardon.

> Trigger : "maillage interne", "liens internes", "cocon SEO", "pages orphelines", "GSC + structure de site", fichier GSC uploadé.

## Philosophie (méthode Boussardon)

> "Le maillage interne, c'est la puissance. Et ça part de tes mots-clés."

- Page mère = **au moins 5 citations** depuis des pages filles/petites-filles
- Le maillage part de la stratégie de mots-clés → le cocon est la conséquence
- Priorité : transactionnel > décisionnel > informationnel
- Maillage **par intention (Know → Do)** en plus du maillage sémantique

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Export GSC Pages — URL, Clics, Impressions, CTR, Position | ✅ Oui |
| Export GSC Requêtes par page | Recommandé |
| Période 3–6 mois | Recommandé |

## Pipeline (5 étapes)

1. **Récupérer les données GSC** — export Pages + Requêtes par URL
2. **Diagnostiquer la structure** :
   - Pages mères potentielles (impressions élevées, pos 4–15, requête transactionnelle)
   - Pages sous-maillées (bonne position mais CTR faible)
   - Pages orphelines (aucune thématique secondaire dans GSC)
3. **Construire le plan de maillage** — hiérarchie mère/fille/petite-fille + règles Know→Do
4. **Prioriser** — score urgence = (Impressions × 0.4) + (Potentiel position × 0.4) + (Business value × 0.2)
5. **Générer les recommandations** — page source + page destination + ancre + contexte + priorité

## Structure hiérarchique

```
Page Mère (mot-clé principal business)
├── Page Fille 1 (requête secondaire transactionnelle)
│   ├── Page Petite-Fille A (longue traîne / micro-intention)
│   └── Page Petite-Fille B
└── Page Fille 2
```

Règle Know → Do : chaque page Know doit pointer vers au moins 1 page Do thématiquement reliée.

## Output obligatoire

Pour chaque action :
- Page source (intention Know/Do/Know+Do)
- Page destination + intention
- Nature du lien (sémantique ou intentionnel Know→Do)
- Ancre recommandée (jamais "cliquez ici")
- Contexte d'insertion
- Priorité (Haute/Moyenne/Faible)

## Règles absolues

- ❌ Automatiser à 100% — le maillage part de la stratégie, pas des outils
- ❌ Mailler sans tenir compte de l'intention (sémantique ≠ intentionnel)
- ❌ Répéter la même ancre sur toutes les pages filles
- ✅ 10 citations minimum pour une page mère "active"

## Concepts liés

[[cocon-semantique]] · [[pagerank-interne]] · [[intention-recherche]] · [[cannibalisation]] · [[gsc-export]]
