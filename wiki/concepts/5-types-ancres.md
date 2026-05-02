---
type: concept
title: 5 types d'ancres internes (et leurs quotas)
aliases: [5-types-ancres, types-ancres, ancres-diversifiees]
tags: [maillage-interne, ancres, anchor-text, doctrine-tim]
created: 2026-05-01
updated: 2026-05-01
sources: 1
confidence: high
status: stable
---

# 5 types d'ancres internes

Cinq types d'ancres possibles pour un lien interne, **avec quotas** et critères de validation. Documenté dans le cas terrain blog Organikk ([[sources/2026-04-30-newsletter-maillage-interne]]).

## Tableau des 5 types

| Type | Quand l'utiliser | Quota par cible |
|---|---|---|
| **Exact match** | Première mention, mot-clé pilier exact | 1 max |
| **Partial match** | Variation autour du mot-clé pilier | 60-70 % des liens entrants |
| **Sémantique étendue** | Reformulation de la promesse cible | Le reste |
| **Naming/marque** | Concept que tu as nommé | À l'unité |
| **Contextuelle longue** | Liens enfouis, motivés par la curiosité | À l'unité |

## 5 critères de validation par ancre

1. **Promesse cible** — l'ancre reflète ce que l'utilisateur va trouver, pas le H1 littéral
2. **Phrase porteuse** — la phrase reste fluide à voix haute sans le lien
3. **Diversification** — ancre pas déjà utilisée vers la même cible depuis ailleurs
4. **Position** — l'ancre porte le verbe d'action ou le substantif central
5. **Link context** — les 5 mots avant/après parlent du sujet de la cible

**Critère qui tranche** : l'ancre survit-elle à la suppression du lien ? Si la phrase reste informative et que tu peux retirer le lien sans rien casser → ancre bonne. Si elle est plaquée → fausse.

## Cas terrain — page hub `process-seo-b2b-2026`

5 liens entrants, 5 ancres différentes :

| Source | Ancre | Type |
|---|---|---|
| ma-strategie-seo-du-moment | "le process B2B complet derrière cette stratégie" | partial |
| roadmap-seo-2026 | "process SEO B2B 2026" | exact |
| mots-cles-seo-2026 | "ma méthode pour ramener du lead qualifié" | sémantique |
| 9-skills-seo-claude | "le process B2B que ces skills servent" | contextuel |
| serrurier-lyon | "comment cette méthode tient en SEO local" | sémantique |

Aucune ancre dupliquée. Un seul exact match, sur la première mention.

## Pages liées

[[sources/2026-04-30-newsletter-maillage-interne]] · [[concepts/maillage-systeme]] · [[concepts/aeo]]
