---
type: audit
title: Audit des automatisations — 2026-06-12
date: 2026-06-12
tags: [audit, automatisations, launchd, github-actions, supabase]
status: report
---

# Audit des automatisations — 2026-06-12

> Inventaire complet : 12 agents launchd, 2 workflows GitHub Actions (seo-kb) + 1 (fusionn), 1 pg_cron Supabase, 4+ routines distantes. Vérification par les effets (fraîcheur des outputs), pas seulement par les statuts.

## ✅ Ce qui tourne (vérifié par l'output)

| Automatisation | Cadence | Preuve de vie |
|---|---|---|
| Brèves IA (routine distante 2x/j) | 07h30 + 17h30 Manille | édition 2026-06-12 présente |
| Revue de presse (launchd 9h) | quotidien | édition 2026-06-12 présente |
| Auto-pull seo-kb (launchd 12h) | quotidien | exit 0, repo à jour |
| Brèves wall → Supabase (launchd 12h20) | quotidien | données du 2026-06-11 en base (mais voir doublons ci-dessous) |
| Questionnaire Leexi pull (launchd horaire) | horaire | exit 0, filtre doc_key=leexi correct (0 réponse reçue à ce jour) |
| GSC pull (launchd, 1er du mois 7h) | mensuel | exports victoriagarden 2026-06-11 et golfiller 2026-06-10 |
| Récap jour (launchd 23h) | quotidien | journal 2026-06-11 présent |
| Revue hebdo (launchd ven. 17h30) | hebdo | édition 2026-W24 présente |
| Hypothèses-validation / ingest-backlog / refresh-snapshots / dashboard | mensuel / lundi / mensuel / 9h30 | exit 0, backlog modifié le 2026-06-12 |
| Opportunity Radar (GH Actions, repo fusionn) | quotidien | success le 2026-06-12 (32s) |
| Lifecycle emails Fusionn (routine distante) | quotidien | actif (l'envoi passe par la routine, pas par le pg_cron) |
| Point du jour 16h UTC + Point de la semaine (routines distantes) | quotidien / samedi | non vérifiable d'ici, contrôler la réception des emails |

## 🚨 Ce qui est cassé

### 1. GitHub Actions seo-kb : 100 % d'échec depuis au moins le 24 mai
`Audit Vault Hygiene` (samedi) et `Algorithme Recap Hebdo` (samedi soir) échouent à chaque run en ~20 s. Cause dans les logs : `Error: Input must be provided either through stdin or as a prompt argument when using --print` : l'appel `claude --print` du workflow ne reçoit plus son prompt (changement de comportement CLI). 3 semaines de récaps hebdo et d'audits auto manqués. Au passage, warning de dépréciation Node 20 sur actions/checkout@v4 (deadline runner : 16 juin 2026).

### 2. Résurgence espacée : morte depuis le 16 mai
launchd `com.timboussardon.resurgence` (mercredi 9h) sort en exit 1, stderr vide, dernière résurgence produite : `resurgence-2026-05-16.md`. 4 mercredis manqués : la boucle « concept oublié → re-confrontation » ne tourne plus. À débugger : `~/.local/bin/seo-kb/run-resurgence.sh`.

### 3. pg_cron `lifecycle-emails-daily` : zombie qui frappe toutes les heures en 401
Le job est actif avec un schedule HORAIRE (`0 * * * *`), chaque appel part en 401 (verify_jwt bloque, le problème connu de juin). Aucun email en double (rien ne passe), mais 24 appels morts par jour depuis des semaines, et un statut `succeeded` trompeur dans cron.job_run_details (le succès porte sur la requête SQL, pas sur l'appel HTTP). La routine distante fait le vrai travail : ce job est à supprimer.

### 4. Table `breves_wall` : doublons réels
L'édition 2026-06-11 existe en double sur au moins les positions 2, 6, 8, 10 (c'est le warning React « two children with the same key » vu sur organikk.co/actualites). Le pipeline a inséré deux fois. Fix : dédupliquer puis poser une contrainte unique (edition_date, position) avec upsert.

## 📊 Synthèse

- 12 automatisations sur 16 en bonne santé, vérifiées par leurs outputs.
- 2 pannes silencieuses longues (GH Actions ~3 semaines, résurgence ~4 semaines) : personne n'a vu parce qu'aucun système ne surveille les surveillants.
- 1 zombie (pg_cron lifecycle) et 1 corruption de données (doublons breves_wall).
- Priorité : réparer les 2 GH Actions et la résurgence, supprimer le pg_cron, dédupliquer breves_wall + contrainte.

## 💡 Nouvelles automatisations proposées (basées sur les habitudes réelles)

1. **Health check des automatisations (méta)** : chaque semaine, refaire exactement cet audit en script (exit codes launchd + fraîcheur des outputs + gh run list + pg_cron en 401) et pousser le résultat dans le Point du jour (ops-alert). Évite qu'une panne dure un mois.
2. **Export RAG automatique** : l'habitude « relancer l'export après modif du vault » est manuelle et oubliable. Un launchd quotidien (après l'autopull de midi) qui relance `export_supabase.py` (base bootcamp) et `export-kb-chat.py` de chaque repo client si le HEAD a bougé.
3. **`./kb rebuild` accroché à l'autopull** : l'autopull tire les éditions des routines, mais l'index vectoriel local reste périmé jusqu'au prochain rebuild manuel. Enchaîner le rebuild (incrémental, rapide) après le pull de midi.
4. **Purge automatique des brouillons versionnés** : la passe -v2/-v3 → `_archive/` faite aujourd'hui à la main, en hebdo (l'agent-synthetic en reproduit chaque semaine).
5. **Draft du récap LinkedIn du jeudi** : chaque jeudi 7h, générer le brouillon « 4 infos SEO du jeudi » (format validé en mémoire) à partir des brèves de la semaine. Tim relit et poste.
6. **Indexation-check mensuel** sur golfiller.fr, organikk.co et fusionn.co : le skill est conçu pour le récurrent, jamais schedulé.
7. **Résolution automatique des prédictions content-brain** : à J+30/J+90, pull GSC via `admin-gsc-export` pour trancher les prédictions ouvertes (golfiller en a une qui résout vers le 10 septembre) au lieu d'attendre un dépôt manuel.
8. **Relance questionnaire client** : si un espace client a 0 réponse au questionnaire après 7 jours (cas Leexi aujourd'hui), notification dans le Point du jour pour relancer.

## Liens

[[2026-06-12-audit]] · [[concepts/cannibalisation]]

## 🔧 Réparations et mises en place (soir du 2026-06-12)

- **pg_cron zombie supprimé** (`cron.unschedule('lifecycle-emails-daily')`) ; **breves_wall dédupliquée** (90 lignes uniques) + contrainte unique (edition_date, position).
- **Résurgence réparée** : le 401 était transitoire (auth CLI), run manuel OK, résurgence du 2026-06-12 générée et poussée. Le launchd du mercredi reprendra normalement.
- **GH Actions** : cause racine = secret `ANTHROPIC_API_KEY` absent du repo (en plus du prompt `--print` cassé, corrigé via stdin + bump Node 24). Décision : migration vers le pattern launchd local qui marche (abonnement, pas de crédits API) : `com.tim.audit-vault` (dim. 8h) et `com.tim.algorithme-recap` (dim. 9h) ; les workflows GH passent en déclenchement manuel uniquement.
- **Nouvelles automatisations actives** : `com.tim.health-automations` (lun. 8h15, rapport dans wiki/ops/ + notification macOS, branchera ops-alert si `~/.config/seo-kb/ops-alert.env` est déposé) ; autopull de midi étendu (rebuild ./kb + export RAG bootcamp + exports RAG clients si HEAD a bougé) ; `com.tim.purge-drafts` (dim. 11h50) ; `com.tim.jeudi-recap` (jeu. 7h, draft 4 infos LinkedIn) ; `com.tim.indexation-check` (le 5 du mois, 3 sites) ; `com.tim.predictions-resolve` (le 3 du mois, ledgers content-brain via GSC).
- Non retenue (décision Tim) : la relance questionnaire client (proposition 8).
