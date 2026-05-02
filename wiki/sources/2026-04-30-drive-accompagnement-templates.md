---
type: source
source_type: doctrine
title: "Drive Accompagnement SEO — structure 7 dossiers + templates client"
aliases: [drive-accompagnement, accompagnement-seo-templates]
tags: [doctrine-tim, accompagnement, templates, drive, livrables-client, claude-cowork, bootcamp]
created: 2026-04-30
updated: 2026-04-30
sources: 1
confidence: high
status: stable
---

# Drive Accompagnement SEO — templates client

**Type** : kit complet de templates et documents à transmettre lors d'un accompagnement client SEO + Claude Cowork. Structure prête pour migration vers Google Drive partagé.
**Auteur** : Tim · **Fichier raw** : `raw/notes/drive-accompagnement/INDEX.md` + tous les sous-dossiers `00_Admin` à `06_Livrables_Client`
**Date** : 2026-04-30 (intégré comme source wiki à cette date)

## Architecture — 7 dossiers

```
Accompagnement SEO [Nom Client]/
  ├── 00_Admin           — Pilotage du programme
  ├── 01_Strategie       — Stratégie SEO
  ├── 02_Systeme_IA      — Stack IA complète
  ├── 03_Contenu         — Production de contenu
  ├── 04_Data            — Données & analyse
  ├── 05_Ressources      — Référence
  └── 06_Livrables_Client — Sortie
```

## Inventaire des templates par dossier

### 00_Admin — Pilotage
- `roadmap-accompagnement.md` — 6 phases : Fondations → Autonomie
- `suivi-calls.md` — Template documentation par call
- `decisions-log.md` — Journal décisions stratégiques

### 01_Strategie — Stratégie SEO
- `mvs-strategie.md` — MVS sur 3 horizons temporels
- `architecture-semantique.md` — Clusters sémantiques + cocon
- `mots-cles-decisionnels.md` — Analyse GSC par intention

### 02_Systeme_IA — Stack IA
- `setup-cowork.md` — Installation Claude Cowork
- `fichiers-contexte-template.md` — about-me / my-voice / my-rules
- `skills-a-installer.md` — 7 skills SEO + progression
- `workflows-ia.md` — 11 workflows automatisés

### 03_Contenu — Production
- `template-brief.md` — Brief complet avec structure Hn
- `template-article.md` — Article 8 étapes avec checklist
- `modeles-de-pages.md` — 6 modèles de pages

### 04_Data — Données & analyse
- `guide-export-gsc.md` — Extraction données GSC
- `template-analyse-quick-wins.md` — Analyse opportunités
- `exports-gsc/` — Dossier CSV

### 05_Ressources — Référence
- `methodo-seo-ia.md` — Fondamentaux condensés
- `anti-patterns-ia.md` — Checklist anti-IA avant publication
- `glossaire-seo-ia.md` — Termes expliqués

### 06_Livrables_Client — Sortie
- `checklist-livraison.md` — Checklist livrables fin d'accompagnement

## Workflow de migration vers Drive

1. **Créer la structure** sur Google Drive (dossier racine + 7 sous-dossiers)
2. **Convertir .md → Google Docs** (copier contenu, créer Google Doc même nom, coller, formater)
3. **Partager avec le client** (clic droit → Partager → "Éditeur" → envoyer lien)

## Ordre d'import par appel

| Call | Dossiers à importer en priorité |
|---|---|
| **Call 1 (Fondations)** | 00_Admin/roadmap + 00_Admin/suivi-calls + 02_Systeme_IA/setup-cowork + 02_Systeme_IA/fichiers-contexte-template |
| **Call 2-3 (Stratégie)** | 01_Strategie/mvs-strategie + 01_Strategie/architecture-semantique + 01_Strategie/mots-cles-decisionnels |
| **Call 4-6 (Contenu)** | 03_Contenu/template-brief + 03_Contenu/template-article + 02_Systeme_IA/skills-a-installer + 02_Systeme_IA/workflows-ia |
| Suite | 04_Data + 05_Ressources + 06_Livrables_Client |

## Apports à la KB

- Premier kit **systématisé** d'accompagnement client documenté — opérationnalise le bootcamp ([[entities/bootcamp-seo-ia]]) en livrables concrets transmissibles
- 7 phases de roadmap → cohérent avec le format 30+30 jours du bootcamp (mois 1 collectif + mois 2 perso)
- 11 workflows automatisés mentionnés (non détaillés dans l'INDEX) — extension du corpus skill ([[sources/2026-04-12-tim-skills-seo-proprietary]] couvrait 10 skills, ici on parle de 11 workflows)
- Référence "anti-patterns-ia" alignée sur [[concepts/anti-ai-writing]]
- Référence "glossaire-seo-ia" alignée sur [[sources/2026-04-12-organikk-glossaire-scrape]] (78 termes publics) — possible pendant interne pour le client

## Limites

- Documents individuels (templates) non lus en détail dans la KB — seul l'INDEX est ingéré
- Pas de mesure de l'efficacité de la migration Drive (taux d'utilisation client après transmission)
- "11 workflows automatisés" non explicités → à formaliser comme concept séparé si Tim valide
- "6 phases" de roadmap mentionnées dans `roadmap-accompagnement.md` non détaillées ici
- Pas de versioning des templates (risque de désynchro avec les skills installés à `~/.claude/skills/`)

## Pages liées

[[sources/2026-04-12-tim-skills-seo-proprietary]] · [[entities/bootcamp-seo-ia]] · [[concepts/anti-ai-writing]] · [[concepts/workflow-redaction-8-etapes]] · [[concepts/data-proprietaire]] · [[concepts/cli-tools-optional]] · [[sources/2026-04-12-organikk-glossaire-scrape]] · [[entities/organikk-co]]
