---
type: source
source_type: doctrine
title: "◈ Article Engine — Workflow Rédactionnel en 8 Prompts"
aliases: []
tags: []
created: 2026-04-12
updated: 2026-04-12
sources: 0
confidence: medium
status: draft
---

# ◈ Article Engine — Workflow Rédactionnel en 8 Prompts

> Pipeline de rédaction d'articles experts B2B. Chaque prompt alimente le suivant.

---

## Structure du workflow

| # | Fichier | Rôle | Input | Output vers |
|---|---------|------|-------|------------|
| 1 | `01_surprise-gap.md` | ⚡ Surprise Gap | Brief initial | 2, 3, 5 |
| 2 | `02_ancrage-local.md` | 📍 Ancrage local | Brief + Étape 1 | 6 |
| 3 | `03_donnees-chiffrees.md` | 📊 Données chiffrées | Brief + Étape 1 | 4, 5, 6 |
| 4 | `04_inversions-expertes.md` | 🔄 Inversions expertes | Brief + Étapes 1, 3 | 5, 6 |
| 5 | `05_architecture-narrative.md` | 🏗️ Architecture narrative | Brief + Étapes 1, 3, 4 | 6, 8 |
| 6 | `06_redaction-principale.md` | ✍️ Rédaction | Brief + Étapes 2, 3, 4, 5 | 7, 8 |
| 7 | `07_faq-micro-intentions.md` | 🎯 FAQ | Brief + Étape 6 | 8 |
| 8 | `08_article-final.md` | ✅ Article final | Brief + Étapes 5, 6, 7 | **LIVRABLE** |

---

## Variables à renseigner dans chaque prompt

```
[MOT-CLÉ]       → Le mot-clé principal de l'article
[STRUCTURE HN]  → La hiérarchie H1/H2/H3 de l'article
[IDÉES]         → Angles et idées à ne pas oublier
[LOCALISATION]  → Zone géographique ciblée
[SECTEUR]       → Secteur d'activité
[AUDIENCE]      → Qui va lire cet article
```

---

## Logique de chaînage

```
Brief
  └─► Étape 1 (Surprise Gap)
        ├─► Étape 2 (Ancrage local) ──────────────────► Étape 6
        ├─► Étape 3 (Données) ──────► Étape 4 ────────► Étape 6
        │                      └────────────────────────► Étape 5
        └──────────────────────────────────────────────► Étape 5
                                                              │
                                                              ▼
                                                         Étape 6 (Rédaction)
                                                              │
                                                              ▼
                                                         Étape 7 (FAQ)
                                                              │
                                                              ▼
                                                         Étape 8 (Article final)
```

---

## Pattern de rédaction appliqué (Étape 6)

Chaque paragraphe suit ce schéma interne :

```
TENSION (donnée ou observation qui dérange)
  → RÉSOLUTION (la logique à adopter)
    → PREUVE (chiffre, exemple ancré, référence terrain)
```

---

## Principes éditoriaux du workflow

- **Surprise Gap** : apporter ce que le lecteur ne sait pas encore, pas ce qu'il sait déjà
- **Ancrage local** : chaque détail géographique/sectoriel précis = signal E-E-A-T
- **Données argumentatives** : chaque chiffre a une implication comportementale directe
- **Inversions expertes** : corriger une croyance fausse > confirmer une vérité connue
- **Low→High Surprise** : chaque section rappelle la précédente, ajoute quelque chose de nouveau
- **Prose continue** : zéro bullet dans le corps, zéro phrase creuse, transitions causales
