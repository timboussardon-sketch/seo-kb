---
type: audit
title: Audit vault et liens — 2026-06-06
tags: [audit, maillage, frontmatter, vault]
created: 2026-06-06
updated: 2026-06-06
status: draft
---

# Audit vault et liens — 2026-06-06

Audit déterministe de 235 pages `wiki/` + 291 `raw/` (script `_audit_vault.py`, blocs de code et fichiers d'audit/templates exclus du comptage des liens). Correctifs reportés à une passe dédiée (« on corrige ensuite »).

## En résumé

- **Une cause systémique domine** : le dossier `wiki/keywords/` (≈27 fichiers, sorties brutes du skill kw-research) est cassé en lot — `type: wiki` invalide, 0 lien sortant, 0 lien entrant, absent de l'index. Il pèse à lui seul ~27 des 31 orphelines, ~27 des 31 sous-maillées et ~27 des 35 types invalides.
- **10 liens cassés actionnables** dans `wiki/` (les 44 autres sont dans `raw/`, immuable).
- **Taxonomie de frontmatter dérivée** : types hors AGENTS.md (`synthese` au lieu de `synthesis`, `article-blog`, `post`, `proposition`, `methode`, `cadrage`).
- **1 entité manquante** : `entities/golfiller` (cas phare référencé, page inexistante).
- **8 fichiers `raw/` sans frontmatter** (backfill possible via `./kb backfill`).
- Pas de contenu stale détecté (>12 mois, status≠stale) : 0.

## P1 — Systémique : `wiki/keywords/` cassé en lot (≈27 fichiers)

Tous les `recherche-2026-05-27-*` + `clustering/decisionnels/modeles/skills-2026-05-28-*` :
- `type: wiki` (invalide, hors taxonomie),
- 0 wikilink sortant (règle : min 2),
- 0 lien entrant (orphelines),
- absentes de `index.md`.

Diagnostic : sorties brutes du skill kw-research déposées dans `wiki/` sans intégration. Décision à prendre (voir plan).

## P2 — Frontmatter : types hors taxonomie AGENTS.md (35)

```
synthese      → devrait être synthesis (typo) : syntheses/audit-doctrine-2026.md
article-blog  → briefs/reddit-pour-geo-2026, strategie-seo-avocat-2026, strategie-seo-hotellerie-2026
post          → posts-linkedin/2026-05-05-workflow-kw-research-5-etapes
proposition   → propositions/modele-proposition-pdf, template-retainer-2h-500
methode       → methodes/ranker-verticale-niche-sans-backlink
cadrage       → methodes/cadrage-boucle-edition-algorithme
wiki          → les ~27 fichiers keywords/ (cf. P1)
```
Sans type (4) : `dashboard.md`, `log.md`, `index.md` (fichiers spéciaux à typer register/moc), `keywords/recherche-2026-06-05-consultant-seo-startup.md`.

Choix : soit corriger les fichiers vers la taxonomie existante, soit étendre AGENTS.md §5.1 avec les types légitimes manquants (`proposition`, `methode`).

## P3 — Liens cassés actionnables dans `wiki/` (10)

```
decisions/index.md            → [[decisions/0001-...|ADR-0001]]   (BUG: pipe échappé \| ; la cible existe)
sources/2026-04-30-scheduled-skills-cron.md → `MIGRATION.md` x2     (fichier racine, pas une page wiki)
keywords/clustering-2026-05-28-agence-seo.md → [[seo-mots-cles-decisionnels]], [[seo-modeles-pseo]]  (noms de SKILLS, pas des pages)
keywords/decisionnels-2026-05-28-agence-seo.md → [[seo-modeles-pseo]]
syntheses/audit-doctrine-2026.md → [[entities/golfiller]]          (ENTITÉ MANQUANTE à créer)
syntheses/tim-profil-doctrine.md → `AGENTS.md`, `AGENTS.md`, `MIGRATION.md`  (fichiers racine)
```

## P4 — Orphelines hors keywords (4 réelles)

```
dashboard.md                          (sans type ni lien entrant)
propositions/modele-proposition-pdf.md
methodes/cadrage-boucle-edition-algorithme.md
syntheses/audit-doctrine-2026.md
```
(Les rapports `audit/*` orphelins sont normaux : ce sont des feuilles.)

## P5 — `raw/` (immuable pour le contenu ; frontmatter backfillable)

8 fichiers sans frontmatter (backfill `./kb backfill --apply`) :
```
raw/revue-de-presse/2026-05-07-revue-presse-contenu.md
raw/revue-de-presse/revue-presse-2026-04-29.md
raw/revue-de-presse/revue-presse-2026-04-29-bis.md
raw/revue-de-presse/revue-presse-2026-04-25.md
raw/revue-de-presse/revue-presse-2026-04-29-ter.md
raw/revue-de-presse/2026-05-07-revue-presse-ia.md
raw/bootcamp4/fiche-skills-terminal.md
raw/bootcamp4/guide-cowork-vers-terminal.md
```
44 liens cassés dans `raw/journal/` et `raw/notes/_archive/` : références à des slugs de mémoire auto (`[[voice_anti_ai_writing]]`, `[[feedback_*]]`) et à des skills (`[[ton-de-voix-tim]]`) qui ne sont pas des pages du vault. Bruit attendu des journaux ; `raw/` étant immuable, non corrigé.

## P6 — Divers

- `decisions/_template.md`, `preuves/_template.md` : dates placeholder (normal pour des templates, à ignorer).
- Racine : `Sans titre.canvas`, `Sans titre 1.canvas` — canvas Obsidian vides, candidats à suppression.

## Plan de correction proposé (passe suivante)

1. **P1 keywords/** : trancher le sort des ≈27 fichiers (intégrer en `type: query` + 2 wikilinks + index, OU déplacer en `raw/`, OU archiver).
2. **P3** : corriger les 10 liens (pipe échappé, liens vers racine/skills en texte ou stubs), créer `entities/golfiller`.
3. **P2** : normaliser les types (`synthese`→`synthesis`, briefs, etc.) ou étendre AGENTS.md.
4. **P4** : raccrocher les orphelines à `index.md`/MOC.
5. **P5** : `./kb backfill --apply` pour les 8 `raw/`.
6. **P6** : supprimer les 2 canvas vides.
7. `./kb rebuild` final pour régénérer `concepts.json` + index vectoriel.
