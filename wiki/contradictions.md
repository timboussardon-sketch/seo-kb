---
type: register
title: Registre des contradictions et dépendances ouvertes
aliases: [contradictions, dette-doctrinale, dependances-ouvertes]
tags: [meta, doctrine, lint, contradictions, dette]
created: 2026-05-16
updated: 2026-06-19
sources: 0
confidence: high
status: living-doc
---

# Registre des contradictions et dépendances ouvertes

> [[log]] note `contradictions: Y/N` à chaque ingest, et chaque batch finit par une section "Contradictions / dépendances ouvertes". Le problème : ces alertes restent enterrées dans un fichier append-only de 600 lignes. Personne ne les revoit. Ce registre les consolide pour qu'elles se ferment au lieu de s'accumuler en dette silencieuse.
>
> Une contradiction = deux pages qui se contredisent, OU un chiffre non sourcé qui circule, OU une dépendance non résolue (source citée mais non ingérée, plan non implémenté donc non mesuré). Le lint SEO (§6.3 AGENTS.md) alimente ce registre, il ne le remplace pas.
>
> Cadence : revue mensuelle avec [[hypotheses]] via le skill `hypotheses-validation`. Toute contradiction non bougée depuis 60j remonte en [[revue-hebdo/index|revue hebdo]] pour décision (fermer, déléguer à un ingest, ou accepter explicitement comme limite connue).

## Statuts

- `ouverte` : identifiée, aucune action engagée
- `en-cours` : un ingest, un test ou une clarification est planifié
- `résolue` : tranchée, avec lien vers la page ou l'ingest qui la ferme
- `acceptée` : limite connue assumée, on ne la ferme pas mais on la documente pour ne pas la re-litiger

## Tableau de bord

| ID | Contradiction / dépendance | Statut | Détectée | Action attendue |
|---|---|---|---|---|
| C-001 | Discordance parcours Franck : Jumpto vs SEO.fr | `ouverte` | 2026-05-01 | Clarifier au prochain call/ingest |
| C-002 | Paper OpenDecoder (Mo et al., 2026) jamais ingéré alors qu'il fonde le scoring | `ouverte` | 2026-04-30 | Item long terme — re-litiger seulement si [[hypotheses#H-010]] redevient critique |
| C-003 | Cluster Organikk + 4 modèles pSEO non implémentés, zéro mesure post-déploiement | `en-cours` | 2026-04-30 | Mesurer après déploiement → [[preuves/index]] |
| C-004 | Snapshot qadence-seo-agent figé au 2026-04-30, le repo évolue | `ouverte` | 2026-04-30 | Ré-ingest snapshot ou diff |
| C-005 | Audit blanc Qualiopi FG Formation lu en titre seulement | `ouverte` | 2026-04-30 | Détailler le contenu en source |
| C-006 | 21 templates Drive Accompagnement : seul l'INDEX est en wiki source | `acceptée` | 2026-04-30 | Limite assumée, ingest à la demande |
| C-007 | "11 workflows automatisés" (drive-accompagnement) vs 10 skills documentés | `acceptée` | 2026-04-30 | Limite assumée [[revue-hebdo/2026-W24]] : jamais citer un décompte de skills sans le recompter depuis AGENTS.md §7 au moment de l'usage |
| C-008 | Brevet Google US12536233B1 : publication ≠ déploiement | `ouverte` | 2026-05-01 | Surveiller déploiement réel |
| C-009 | Papers MAGEO (2604.19516) et Role-Augmented G-SEO (2508.11158) non ingérés | `ouverte` | 2026-05-01 | Ingest papers si Tim valide la priorité |
| C-010 | Statut inscription bootcamp Cécile / Franck non confirmé | `ouverte` | 2026-05-01 | Confirmer via suivi prospects |
| C-011 | Chiffres glossaire non sourcés (40% AIO clics, 15M req/j Perplexity, 90-99% autorité 301) | `ouverte` | 2026-04-13 | Sourcer ou flaguer `confidence: low` avant réutilisation |
| C-012 | Glossaire simplifie MIRAS "multi-résolution" en "mémoire long-terme" | `acceptée` | 2026-04-13 | Vulgarisation assumée du glossaire public ; divergence documentée dans la source, référence canonique = [[entities/miras]] |
| C-013 | Reranking : plafond effective rate ~70% non résolu par aucune méthode étudiée | `acceptée` | 2026-04-25 | Limite scientifique connue, à citer comme telle |

## Détail des contradictions actives

### C-001 — Franck : Jumpto vs SEO.fr

[[entities/jumpto]] porte un flag `a-verifier`. Au call-08 Franck est rattaché à Jumpto ; au call-10 il se présente comme ex-fondateur de SEO.fr (vendu début 2024 à Netlinking.fr), profil freelance. [[entities/franck]] a été corrigé en ce sens mais le parcours intermédiaire 2024-? n'est pas documenté. Risque : citer le mauvais rattachement dans une analyse prospects. Action : trancher au prochain contact, fermer le flag sur [[entities/jumpto]].

### C-002 — OpenDecoder jamais ingéré

[[sources/2026-04-15-opendecoder-seo-scoring-system]] est la référence canonique du scoring SEO (4 axes, 15 prompts LLM), mais le paper primaire OpenDecoder (Mo et al., 2026) n'a jamais été ingéré comme source `paper`. Tant qu'il ne l'est pas, on ne peut pas auditer la fidélité de la transposition. Bloque [[hypotheses#H-010]]. Action : ingest prioritaire.

`en-cours` depuis le 2026-05-16 : [[revue-hebdo/2026-W20]] point 4 a tranché l'ingest du paper primaire en W21 (action bornée, distincte du lot d'ingest W21). Statut `résolue` à poser quand le paper est ingéré et la transposition auditée formule par formule.

Repassée `ouverte` le 2026-06-12 ([[revue-hebdo/2026-W24]]) : aucune action engagée en 4 semaines, `en-cours` ne reflétait plus la réalité. Requalifiée item long terme — l'ingest se déclenche si [[hypotheses#H-010]] redevient critique (audit du scoring demandé par un client ou un contenu publié), pas par reconduction rituelle.

### C-003 — Cluster Organikk non mesuré

Le cluster business Organikk et les 4 modèles pSEO ([[sources/2026-04-24-cluster-business-organikk-4-piliers]], [[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]]) sont planifiés mais l'implémentation et la mesure post-déploiement manquent. C'est la dépendance qui bloque la moitié des hypothèses du registre : sans pages publiées et mesurées, [[hypotheses#H-002]], [[hypotheses#H-003]], [[hypotheses#H-007]] restent `ouvert`. Action : alimenter [[preuves/index]] dès les premières pages en ligne.

`en-cours` depuis le 2026-05-16 : la cohorte pSEO secteur×ville déjà publiée devait engager la première instrumentation sans attendre le déploiement complet du cluster — fiche [[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]] (H-007 passé `en-test`). La contradiction ne se ferme que quand le cluster complet est déployé et mesuré ; cette fiche n'en couvre qu'une fraction (5 pages, H-007 seule).

Mise à jour 2026-06-19 ([[revue-hebdo/2026-W25]]) : la fraction d'instrumentation revendiquée n'a jamais produit de donnée — baseline GSC `organikk.co` jamais capturée, H-007 repassée `ouvert`, fiche gelée. C-003 reste `en-cours` mais sur du vrai zéro mesure, pas sur une progression partielle. Elle ne bougera que sur un sprint de contenu Organikk réel avec baseline capturée avant intervention, jamais par reconduction.

### C-007 — Décompte workflows vs skills

drive-accompagnement parle de "11 workflows automatisés", la KB documente 10 (puis 13) skills propriétaires. Divergence comptable jamais réconciliée. Risque : incohérence dans un livrable client ou une page commerciale. Action : poser la liste canonique, lien vers [[sources/2026-04-12-tim-skills-seo-proprietary]].

Passée `acceptée` le 2026-06-12 ([[revue-hebdo/2026-W24]]), en application du conditionnel posé en [[revue-hebdo/2026-W22]] (désignée W21 et W22, non bougée : on la sort du circuit, on ne la reconduit pas). Le fond : « skill propriétaire » n'a pas de définition stable et l'inventaire réel évolue plus vite que tout décompte (20+ skills `seo-*` installés au 2026-06-12). Limite assumée avec garde-fou : ne jamais citer un décompte de skills dans un livrable ou une page commerciale sans le recompter depuis AGENTS.md §7 au moment de l'usage. Si Tim pose un jour la définition canonique, la ligne pourra passer `résolue`.

### C-011 — Chiffres glossaire non sourcés

Le glossaire Organikk ([[sources/2026-04-12-organikk-glossaire-scrape]]) avance 40% de clics AI Overviews, 15M requêtes/jour Perplexity, 90-99% de transfert d'autorité sur 301. Aucune source primaire. Règle §5.4 violée : pas de source = pas d'affirmation. Action : sourcer ou marquer `confidence: low` partout où ces chiffres sont repris, ne jamais les mettre dans un contenu publié sans source (croise la règle [[concepts/data-proprietaire]] et l'interdiction de chiffres non sourcés).

## Quand une contradiction se ferme

1. Trancher (ingest, test, clarification client)
2. Passer le statut `résolue` + lien vers la page/source qui la ferme
3. Si elle révèle une erreur doctrinale propagée, corriger les pages concernées et le noter
4. Logguer : `## [YYYY-MM-DD] contradiction | C-XXX résolue`
5. Garder la ligne (ne pas supprimer) : l'historique des contradictions fermées est une trace d'audit

Pages liées : [[log]] · [[hypotheses]] · [[index]] · [[ingest-backlog]] · [[revue-hebdo/index]]
