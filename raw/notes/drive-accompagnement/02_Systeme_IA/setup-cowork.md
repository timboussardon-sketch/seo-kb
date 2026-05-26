---
type: source
source_type: doctrine
title: "Setup Claude Cowork — Guide d'installation"
aliases: []
tags: []
created: 2026-04-25
updated: 2026-04-25
sources: 0
confidence: medium
status: draft
---

# Setup Claude Cowork — Guide d'installation

> Ton environnement IA SEO personnel. À configurer lors du Call 1.

---

## Étape 1 — Installation de base

- [ ] Installer Claude Desktop (claude.ai/download)
- [ ] Activer Cowork Mode
- [ ] Sélectionner ton dossier de travail principal
- [ ] Vérifier l'accès aux fichiers locaux

---

## Étape 2 — Fichiers contexte

3 fichiers à créer dans `.claude/` ou dans ton workspace :

### about-me.md
> Ton identité professionnelle, ce que tu fais, pour qui, tes liens.

**Contenu à remplir** :
- Identité :
- Ce que tu fais :
- Positionnement :
- Clients types :
- Liens (site, réseaux, prise de RDV) :

### my-voice.md
> Ton ton de voix, tes patterns de rédaction, tes interdits.

**Contenu à remplir** :
- Principes fondamentaux du ton :
- Ce que tu fais systématiquement :
- Ce que tu ne fais JAMAIS :
- Pattern de rédaction :
- Format article :
- Format newsletter / LinkedIn :

### my-rules.md
> Tes règles de travail, ta vision, tes priorités.

**Contenu à remplir** :
- Règles de sourcing :
- Règles de rédaction :
- Règles SEO :
- Vision / philosophie :
- Priorités par horizon temporel :

---

## Étape 3 — Structure du workspace

```
📂 Ton-dossier-de-travail/
  ├── .claude/
  │   └── skills/          → Tes skills SEO installés
  ├── contexte/            → about-me, my-voice, my-rules
  ├── briefs/              → Briefs de contenu
  ├── articles/            → Articles produits
  ├── data/                → Exports GSC, analyses
  └── templates/           → Modèles de pages
```

---

## Étape 4 — Vérification

- [ ] Claude peut lire tes fichiers contexte
- [ ] Claude connaît ton ton de voix
- [ ] Claude respecte tes règles
- [ ] Un test de brief rapide fonctionne
