---
type: source
source_type: doctrine
title: "0 → 62 liens internes : audit maillage blog Organikk (Tim, méthode)"
aliases: [newsletter-maillage-interne, maillage-3-axes-organikk]
tags: [maillage-interne, newsletter, organikk, hub-satellite, ancres, cross-pillar, doctrine, cas-terrain]
created: 2026-04-30
updated: 2026-04-30
sources: 1
confidence: high
status: stable
---

# 0 → 62 liens internes : audit maillage blog Organikk

**Type** : note doctrinale + cas terrain (Tim sur son propre blog)
**Auteur** : Tim
**Fichier raw** : `raw/articles/newsletter-maillage-interne.md`
**Date** : 2026-04-30

## Contexte

Audit du blog Organikk (14 articles, 0 lien interne) → reconstruction complète du maillage en 62 liens internes structurés sur 3 axes. Documente la création d'un nouveau skill propriétaire `maillage-systeme` complémentaire de `maillage-interne-gsc` (cf [[sources/2026-04-12-tim-skills-seo-proprietary]]).

## Trous structurels du skill `maillage-interne-gsc` seul

| Trou | Conséquence |
|---|---|
| Pas de notion hub vs satellite | Suggestions au même niveau, autorité diluée |
| Pas de gradient d'intention | Pages "concept" pointent vers pages "outil" au lieu de l'inverse |
| Pas de mémoire entre articles | Nouvel article ne met pas à jour les anciens |

→ besoin du skill complémentaire **maillage-systeme** (architecture éditoriale d'abord, donnée GSC ensuite).

## Méthode — 3 axes simultanés

| Axe | Lecture par | Critère de validation |
|---|---|---|
| Topique | Google (sémantique classique) | Même sujet ? |
| Vectoriel | LLM (embeddings) | Ancre alignée mathématiquement avec passage cible ? |
| Cognitif | Humain | Lecteur a-t-il envie de cliquer ? |

Une ancre qui rate l'un des trois = lien gaspillé.

## Architecture appliquée — 4 piliers + 4 hubs

- **Pilier 1 — Stratégie SEO 2026** (HUB : `process-seo-b2b-2026`)
- **Pilier 2 — Outils IA & systèmes pour SEO** (HUB : `9-skills-seo-claude`)
- **Pilier 3 — SEO Local sectoriel** (HUB : `serrurier-lyon`)
- **Sous-cluster GEO** (Hub provisoire : `information-gain-seo-geo`) — devient pilier autonome au 3e article

**Règle** : un cluster < 3 articles ne devient pas pilier indépendant. Reste sous-cluster.

## 5 types d'ancres et quotas

| Type | Quand | Quota |
|---|---|---|
| Exact match | Première mention, mot-clé pilier exact | 1 max par cible |
| Partial match | Variation autour du mot-clé pilier | 60-70 % des liens entrants |
| Sémantique étendue | Reformulation de la promesse cible | Le reste |
| Naming/marque | Concept nommé par Tim | À l'unité |
| Contextuelle longue | Liens enfouis, motivés par curiosité | À l'unité |

## 5 critères de validation par ancre

1. **Promesse cible** — reflète ce que l'utilisateur va trouver, pas le H1 littéral
2. **Phrase porteuse** — phrase fluide à voix haute sans le lien
3. **Diversification** — pas déjà utilisée vers la même cible depuis ailleurs
4. **Position** — porte le verbe d'action ou le substantif central
5. **Link context** — 5 mots avant/après parlent du sujet de la cible

**Critère qui tranche** : l'ancre survit-elle à la suppression du lien ? Si oui = bonne. Si plaquée = mauvaise.

## Résultat — 62 liens, 4 typologies

| Type | Nombre | Rôle |
|---|---|---|
| Hub ↔ Satellite | 12 | Activer chaque cocon |
| Know → Do | 8 | Orienter funnel vers `/services`, `/outils`, `/coaching` |
| Cross-pillar | 6 | Anti-siloïsation |
| Sous-cluster | 2 | Densifier sous-cluster GEO |
| Pilier interne | 2 | Connecter SEO local |
| Outbound page Do | 2 | Vers pages business |

**Total** : 62 liens internes (32 outbound, 30 inbound). 0 page orpheline. 0 page dead-end. Densité moyenne 4 liens/article (sous le plafond de 5/1000 mots).

## 4 leçons réutilisables

1. **Une page mère ≠ catégorie technique** — c'est l'article le plus stratégique du pilier, qui définit le vocabulaire et reçoit le plus de liens internes
2. **Maillage Know → Do passe avant Know → Know** — pages concept doivent toujours pointer vers pages d'exécution (outil, audit, démo)
3. **Pas de "Voir aussi" en bas d'article** — contexte de lien dilué. Liens contextuels in-body uniquement
4. **Cross-pillar pollination compte autant que intra-cluster** — au moins 1 lien sortant par pilier vers un autre pilier, sinon silos thématiques

## Checklist gouvernance (à appliquer avant publication d'un nouvel article)

- [ ] ≥ 3 liens entrants depuis 3 articles existants
- [ ] ≥ 3 liens sortants vers articles existants
- [ ] ≥ 1 lien sortant vers page Do
- [ ] ≥ 1 lien sortant vers autre pilier
- [ ] Aucune ancre exact match dupliquée vers la même cible
- [ ] Tous les liens in-body, aucun en bloc "Voir aussi"

## Apports à la KB

- Formalise le concept [[concepts/maillage-systeme]] (à créer) — complémentaire au skill existant `maillage-interne-gsc`
- Introduit le concept [[concepts/5-types-ancres]] (à créer) — exact / partial / sémantique / naming / contextuelle, avec quotas chiffrés
- Documente le pattern hub/satellite avec gradient Know → Do appliqué (cohérent avec [[concepts/aeo]] et la classification Know-Simple/Know/Do du skill `seo-cluster-aeo`)
- Cas terrain documenté chiffré (62 liens, 14 articles, 4 piliers) → réutilisable comme preuve dans les calls prospection

## Limites

- Cas appliqué sur le blog de Tim uniquement — pas de réplication client publique encore
- Pas de mesure post-maillage (positions, citations IA, conversions) — les 62 liens sont fraîchement déployés
- Densité 4 liens/article : règle empirique de Tim, pas de validation académique

## Pages liées

**Concepts** : [[concepts/maillage-systeme]] · [[concepts/5-types-ancres]] · [[concepts/aeo]] · [[concepts/data-proprietaire]] · [[concepts/programmatique-pseo]]

**Entities** : [[entities/organikk-co]] · [[entities/bootcamp-seo-ia]]

**Sources** : [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[sources/2026-04-12-organikk-blog-scrape]]
