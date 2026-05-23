---
type: audit
title: "Audit vault — 2026-05-21"
aliases: [audit-vault-2026-05-21, audit-2026-05-21]
date: 2026-05-21
tags: [audit, hygiene, vault]
created: 2026-05-21
updated: 2026-05-21
status: report
---

# Audit vault — 2026-05-21

Audit de santé du vault seo-kb : intégrité de l'[[index]], liens cassés, notes orphelines, frontmatter, métadonnées. Périmètre : `wiki/` (domaine agent). 421 notes au total (197 wiki, 224 raw). Suite de l'[[audit/2026-05-11-audit|audit du 2026-05-11]].

## Verdict

Structure saine, aucun dossier cassé. Deux problèmes de fond : **dérive de l'index** (compteurs jamais suivis) et **décisions loggées non exécutées**. Tout le 🔴 et le 🟠 a été corrigé dans la foulée.

## Anomalies trouvées et corrigées

### Index désynchronisé
- Compteurs faux : Concepts 36→**50**, Entities 45→**47**, Syntheses 4→**7**, Queries 2→**4**, Briefs 1→**6**.
- Fichiers absents du catalogue, ajoutés : `purete-vectorielle`, `entites-vectorielles` (Concepts) ; `gsc` (Entities) ; `4-piliers-organikk`, `faq-geo-175-questions`, `tim-profil-doctrine` (Syntheses) ; `pseo-2026-05-13-organikk-secteur-ville`, `transfert-vault-client` (Queries) ; 5 briefs ; sections **Audits** et **Propositions** créées.

### Décision non exécutée
- `concepts/rrf.md` était `status: draft` alors que la revue-hebdo W20 (2026-05-16) avait acté `rrf draft→stable`. Corrigé (`status: stable`, `updated: 2026-05-16`).

### Frontmatter non conforme (AGENTS.md §5.1)
- 5 concepts bootcamp (`80-pourcent-pattern-strategie`, `arbitrage-plateforme-publication`, `modele-page-variable-prix`, `regle-ia-ne-le-fait-pas-je-le-fais-pas`, `scam-objection-data-aleatoire`) : schéma non standard (`name`/`date_added`/`status: actif`). Réécrits au schéma standard, `status: stable`, section `## Pages liées` ajoutée.
- 3 syntheses (`4-piliers-organikk`, `faq-geo-175-questions`, `tim-profil-doctrine`) : `created`/`updated`/`status` manquants, `type: synthese`/`statut`. Normalisés.
- `status: evolving` (hors enum) sur `confidence-score`, `muvera`, `sge` → `stable`.

### Liens cassés (wiki/)
- `[[cocon-semantique]]` → `[[maillage-systeme]]` dans la query pSEO secteur×ville.
- 7 liens `[[feedback_*]]` (mémoire hors vault) déliés en texte simple ; `feedback_anti_ai_writing` repointé sur `[[concepts/anti-ai-writing]]`.
- `[[raw/data/keyword-research-2026-05-02]]` (dossier) → `[[raw/data/keyword-research-2026-05-02/keywords-classified]]` (fichier).
- Faux positif : `[[decisions/0001-fermeture-boucles-second-cerveau\|ADR-0001]]` est une syntaxe Obsidian valide (échappement de pipe en tableau), pas un lien cassé.

### Notes manquantes créées
- `concepts/entites-vectorielles` — réclamée par 6 fichiers raw, rédigée depuis le skill `seo-entites-vectorielles`.
- `entities/gsc` — Google Search Console, entité outil.

### Fichier mal rangé
- `2026-05-05-workflow-kw-research-5-etapes.md` (`type: post`) était dans `syntheses/`. Déplacé vers `posts-linkedin/` (dossier canonique AGENTS.md §3) ; les 3 liens existants le pointaient déjà ainsi.

### Orphelines
8 notes sans lien entrant au départ → 0 après remise à l'index des syntheses, briefs, query et proposition concernés.

## Laissé en l'état (volontaire)

- **Statuts de cycle de vie spécifiques** : `living-doc` (registres/MOC), `accepted` (ADR), `report` (audits), `en-cours` (preuves), `phase-1-ready` (pSEO-strategy), `prêt-à-implémenter` (briefs). Sous-vocabulaires délibérés et cohérents, pas des violations.
- **`.obsidian.broken/`** — dossier de config Obsidian cassée à la racine. Suppression manuelle recommandée (action irréversible, non exécutée par l'agent).
- **5 sections vides** de l'index (Clusters, Quick Wins, Cannibalisation, Maillage, GSC Exports) — normal, pas encore d'outputs.

## Pages liées

[[index]] · [[log]] · [[audit/2026-05-11-audit]] · [[AGENTS]] · [[concepts/entites-vectorielles]] · [[entities/gsc]]
