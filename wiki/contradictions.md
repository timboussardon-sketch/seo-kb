---
type: register
title: Registre des contradictions et dépendances ouvertes
aliases: [contradictions, dette-doctrinale, dependances-ouvertes]
tags: [meta, doctrine, lint, contradictions, dette]
created: 2026-05-16
updated: 2026-07-24
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
| C-001 | Discordance parcours Franck : Jumpto vs SEO.fr | `acceptée` | 2026-05-01 | Limite assumée [[revue-hebdo/2026-W29]] : jamais citer le rattachement de Franck (Jumpto vs SEO.fr) sans le re-vérifier au moment de l'usage |
| C-002 | Paper OpenDecoder (Mo et al., 2026) jamais ingéré alors qu'il fonde le scoring | `ouverte` | 2026-04-30 | Item long terme — re-litiger seulement si [[hypotheses#H-010]] redevient critique |
| C-003 | Cluster Organikk + 4 modèles pSEO non implémentés, zéro mesure post-déploiement | `en-cours` | 2026-04-30 | Mesurer après déploiement → [[preuves/index]] |
| C-004 | Snapshot qadence-seo-agent figé au 2026-04-30, le repo évolue | `résolue` | 2026-04-30 | Fermée [[revue-hebdo/2026-W27]] : [[entities/qadence-seo-agent]] maintenue vivante fait référence d'état, le snapshot est une photo datée |
| C-005 | Audit blanc Qualiopi FG Formation lu en titre seulement | `en-cours` | 2026-04-30 | Ingest attaché au lot FG-Formation W31 ([[revue-hebdo/2026-W30]] point 4) |
| C-006 | 21 templates Drive Accompagnement : seul l'INDEX est en wiki source | `acceptée` | 2026-04-30 | Limite assumée, ingest à la demande |
| C-007 | "11 workflows automatisés" (drive-accompagnement) vs 10 skills documentés | `acceptée` | 2026-04-30 | Limite assumée [[revue-hebdo/2026-W24]] : jamais citer un décompte de skills sans le recompter depuis AGENTS.md §7 au moment de l'usage |
| C-008 | Brevet Google US12536233B1 : publication ≠ déploiement | `ouverte` | 2026-05-01 | Surveiller déploiement réel |
| C-009 | Papers MAGEO (2604.19516) et Role-Augmented G-SEO (2508.11158) non ingérés | `ouverte` | 2026-05-01 | Ingest papers si Tim valide la priorité |
| C-010 | Statut inscription bootcamp Cécile / Franck non confirmé | `acceptée` | 2026-05-01 | Limite assumée [[revue-hebdo/2026-W29]] : jamais citer un décompte d'inscriptions bootcamp sans le re-vérifier au moment de l'usage |
| C-011 | Chiffres glossaire non sourcés (40% AIO clics, 15M req/j Perplexity, 90-99% autorité 301) | `acceptée` | 2026-04-13 | Limite assumée [[revue-hebdo/2026-W26]] : jamais publier ces 3 chiffres sans source primaire ; sourcer au moment de l'usage |
| C-012 | Glossaire simplifie MIRAS "multi-résolution" en "mémoire long-terme" | `acceptée` | 2026-04-13 | Vulgarisation assumée du glossaire public ; divergence documentée dans la source, référence canonique = [[entities/miras]] |
| C-013 | Reranking : plafond effective rate ~70% non résolu par aucune méthode étudiée | `acceptée` | 2026-04-25 | Limite scientifique connue, à citer comme telle |

## Détail des contradictions actives

### C-001 — Franck : Jumpto vs SEO.fr

[[entities/jumpto]] porte un flag `a-verifier`. Au call-08 Franck est rattaché à Jumpto ; au call-10 il se présente comme ex-fondateur de SEO.fr (vendu début 2024 à Netlinking.fr), profil freelance. [[entities/franck]] a été corrigé en ce sens mais le parcours intermédiaire 2024-? n'est pas documenté. Risque : citer le mauvais rattachement dans une analyse prospects.

`acceptée` depuis le 2026-07-17 ([[revue-hebdo/2026-W29]] point 4), en bloc avec C-010 — même objet, même cause. Ouverte 77 jours en attente d'un contact qui n'est jamais venu et qu'aucun bootcamp en cours ne provoquera. Calque C-007 / C-011 : quand une contradiction attend une information que rien ne produit, on la convertit en garde-fou à l'usage plutôt que de la laisser figurer indéfiniment en dette active. Accepter n'est pas résoudre. Limite : **jamais citer le rattachement de Franck sans le re-vérifier au moment de l'usage**. Le flag `a-verifier` sur [[entities/jumpto]] reste et porte désormais la limite au lieu d'attendre un call. Repasse `ouverte` si un contact réel apporte le parcours 2024-?.

### C-010 — Statut inscription bootcamp Cécile / Franck

Le statut d'inscription au bootcamp de Cécile et de Franck n'a jamais été confirmé (détecté le 2026-05-01, suivi prospects). Risque : citer un décompte d'inscrits faux dans le discours commercial ou une analyse de conversion.

`acceptée` depuis le 2026-07-17 ([[revue-hebdo/2026-W29]] point 4), en bloc avec C-001. Même diagnostic : aucun bootcamp en cours ne produira la confirmation, l'attente est indéfinie. Limite : **jamais citer un décompte d'inscriptions bootcamp sans le re-vérifier au moment de l'usage**, exactement comme C-007 impose de recompter les skills depuis AGENTS.md §7. Repasse `ouverte` si un cycle bootcamp reprend et rend les statuts vérifiables.

### C-005 — Audit blanc Qualiopi FG Formation lu en titre seulement

`raw/notes/fg-formation/audit-blanc.md` n'a jamais été détaillé en source, et le dossier FG Formation compte aussi 5 transcripts d'audits blancs individuels (`clients/fgformation/calls/audit-blanc-{marc-d,paul-g,julie-h,nadia-r,karim-b}.md`) jamais ingérés — le point P1 du backlog resté en tête de liste depuis mai.

Passée `en-cours` le 2026-07-24 ([[revue-hebdo/2026-W30]] point 4) : le dossier n'est plus une hypothèse de travail, il alimente une livraison réelle. Le duel publié `raw/organikk/clients/fgformation/pages/2026-07-24-audit-blanc-seul-ou-accompagnement-complet.md` cite directement la matière audit blanc pour opposer les deux voies (seul vs accompagné) — un contenu client sort avec une source que la KB ne connaît qu'en titre. Ferme quand le lot FG-Formation du point 3 ingère `audit-blanc.md` + les 5 transcripts individuels dans `wiki/sources/`.

### C-002 — OpenDecoder jamais ingéré

[[sources/2026-04-15-opendecoder-seo-scoring-system]] est la référence canonique du scoring SEO (4 axes, 15 prompts LLM), mais le paper primaire OpenDecoder (Mo et al., 2026) n'a jamais été ingéré comme source `paper`. Tant qu'il ne l'est pas, on ne peut pas auditer la fidélité de la transposition. Bloque [[hypotheses#H-010]]. Action : ingest prioritaire.

`en-cours` depuis le 2026-05-16 : [[revue-hebdo/2026-W20]] point 4 a tranché l'ingest du paper primaire en W21 (action bornée, distincte du lot d'ingest W21). Statut `résolue` à poser quand le paper est ingéré et la transposition auditée formule par formule.

Repassée `ouverte` le 2026-06-12 ([[revue-hebdo/2026-W24]]) : aucune action engagée en 4 semaines, `en-cours` ne reflétait plus la réalité. Requalifiée item long terme — l'ingest se déclenche si [[hypotheses#H-010]] redevient critique (audit du scoring demandé par un client ou un contenu publié), pas par reconduction rituelle.

### C-003 — Cluster Organikk non mesuré

Le cluster business Organikk et les 4 modèles pSEO ([[sources/2026-04-24-cluster-business-organikk-4-piliers]], [[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]]) sont planifiés mais l'implémentation et la mesure post-déploiement manquent. C'est la dépendance qui bloque la moitié des hypothèses du registre : sans pages publiées et mesurées, [[hypotheses#H-002]], [[hypotheses#H-003]], [[hypotheses#H-007]] restent `ouvert`. Action : alimenter [[preuves/index]] dès les premières pages en ligne.

`en-cours` depuis le 2026-05-16 : la cohorte pSEO secteur×ville déjà publiée devait engager la première instrumentation sans attendre le déploiement complet du cluster — fiche [[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]] (H-007 passé `en-test`). La contradiction ne se ferme que quand le cluster complet est déployé et mesuré ; cette fiche n'en couvre qu'une fraction (5 pages, H-007 seule).

Mise à jour 2026-06-19 ([[revue-hebdo/2026-W25]]) : la fraction d'instrumentation revendiquée n'a jamais produit de donnée — baseline GSC `organikk.co` jamais capturée, H-007 repassée `ouvert`, fiche gelée. C-003 reste `en-cours` mais sur du vrai zéro mesure, pas sur une progression partielle. Elle ne bougera que sur un sprint de contenu Organikk réel avec baseline capturée avant intervention, jamais par reconduction.

Mise à jour 2026-07-10 ([[revue-hebdo/2026-W28]]) : le blocage « zéro mesure » n'est plus structurel. La propriété GSC `organikk.co` est connectée (edge `admin-gsc-export` de Fusionn, première donnée réelle au run indexation du 2026-07-10) et un sprint réel a produit un batch publié le 2026-07-07, instrumenté par [[preuves/2026-07-10-organikk-batch-juillet-data-proprietaire]] (H-007 repassée `en-test`). C-003 reste `en-cours` : elle ne se ferme qu'au déploiement mesuré du cluster complet, et le batch de juillet n'en couvre qu'une fraction — mais c'est la première fraction mesurable, pas revendiquée.

### C-004 — Snapshot Qadence figé (résolue)

Passée `résolue` le 2026-07-03 ([[revue-hebdo/2026-W27]]). La dette supposée — un snapshot du 2026-04-30 qui divergeait du repo vivant — est résolue par la pratique constatée : [[entities/qadence-seo-agent]] est maintenue à jour au fil du travail réel (3 sources, dernière mise à jour 2026-07-03 : conscience temporelle + DA Métriques) et c'est l'entité, pas le snapshot, qui fait référence d'état courant. [[sources/2026-04-30-qadence-seo-agent-snapshot]] est requalifié en photo datée, ce qui est le rôle normal d'une source. Aucun ré-ingest de snapshot n'est nécessaire tant que l'entité suit le repo.

### C-007 — Décompte workflows vs skills

drive-accompagnement parle de "11 workflows automatisés", la KB documente 10 (puis 13) skills propriétaires. Divergence comptable jamais réconciliée. Risque : incohérence dans un livrable client ou une page commerciale. Action : poser la liste canonique, lien vers [[sources/2026-04-12-tim-skills-seo-proprietary]].

Passée `acceptée` le 2026-06-12 ([[revue-hebdo/2026-W24]]), en application du conditionnel posé en [[revue-hebdo/2026-W22]] (désignée W21 et W22, non bougée : on la sort du circuit, on ne la reconduit pas). Le fond : « skill propriétaire » n'a pas de définition stable et l'inventaire réel évolue plus vite que tout décompte (20+ skills `seo-*` installés au 2026-06-12). Limite assumée avec garde-fou : ne jamais citer un décompte de skills dans un livrable ou une page commerciale sans le recompter depuis AGENTS.md §7 au moment de l'usage. Si Tim pose un jour la définition canonique, la ligne pourra passer `résolue`.

### C-011 — Chiffres glossaire non sourcés

Le glossaire Organikk ([[sources/2026-04-12-organikk-glossaire-scrape]]) avance 40% de clics AI Overviews, 15M requêtes/jour Perplexity, 90-99% de transfert d'autorité sur 301. Aucune source primaire. Règle §5.4 violée : pas de source = pas d'affirmation. Action : sourcer ou marquer `confidence: low` partout où ces chiffres sont repris, ne jamais les mettre dans un contenu publié sans source (croise la règle [[concepts/data-proprietaire]] et l'interdiction de chiffres non sourcés).

Passée `acceptée` le 2026-06-26 ([[revue-hebdo/2026-W26]]), même traitement que C-007 : sourcer rétroactivement trois chiffres d'un glossaire scrapé ne vaut pas un sprint, et ils ne sont repris dans aucun contenu publié à ce jour. Limite assumée avec garde-fou dur : ces trois chiffres ne sortent jamais dans un contenu publié sans source primaire vérifiée au moment de l'usage. Si un de ces chiffres devient nécessaire à une édition, on le source ou on le coupe — on ne le ressort pas du glossaire tel quel. Ligne conservée pour la trace d'audit.

## Quand une contradiction se ferme

1. Trancher (ingest, test, clarification client)
2. Passer le statut `résolue` + lien vers la page/source qui la ferme
3. Si elle révèle une erreur doctrinale propagée, corriger les pages concernées et le noter
4. Logguer : `## [YYYY-MM-DD] contradiction | C-XXX résolue`
5. Garder la ligne (ne pas supprimer) : l'historique des contradictions fermées est une trace d'audit

Pages liées : [[log]] · [[hypotheses]] · [[index]] · [[ingest-backlog]] · [[revue-hebdo/index]]
