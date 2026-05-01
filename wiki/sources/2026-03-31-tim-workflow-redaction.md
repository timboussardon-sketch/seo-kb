---
type: source
source_type: doctrine
title: Workflow rédaction 8 étapes (Article Engine)
aliases: [tim-workflow-redaction, article-engine]
tags: [doctrine-tim, workflow, redaction, surprise-gap, grounding-score]
created: 2026-04-12
updated: 2026-04-12
sources: 1
confidence: high
status: stable
---

# Workflow rédaction 8 étapes (Article Engine)

**Fichiers raw** : `raw/notes/tim-workflow-redaction.md` · `raw/notes/tim-readme-bot-instructions.md`
**Date** : ~31 mars 2026
**Temps estimé** : 1h30 à 2h30 par article

Pipeline de rédaction d'articles experts B2B. Chaque étape alimente la suivante. Cf. [[concepts/workflow-redaction-8-etapes]] pour le concept.

---

## Les 8 étapes

| # | Nom | Objectif | Frameworks intégrés |
|---|---|---|---|
| 1 | **Surprise Gap** | Identifier ce que 80% des articles disent déjà vs ce qui manque | [[concepts/surprise-gap]], [[concepts/surprise-metric]] |
| 2 | **Ancrage local** | Signaux E-E-A-T géographiques/sectoriels précis | E-E-A-T |
| 3 | **Données chiffrées** | Statistiques argumentatives (pas décoratives), sourcées obligatoirement | [[concepts/data-proprietaire]], [[concepts/information-gain]] |
| 4 | **Inversions expertes** | Corriger les croyances fausses répandues — arme fatale du Surprise Score | [[concepts/surprise-gap]] |
| 5 | **Architecture narrative** | Plan section par section, logique Low→High Surprise, passage ancré marqué | [[concepts/grounding-score]] |
| 6 | **Rédaction principale** | Prose experte 2000-2500 mots, pattern TENSION→RÉSOLUTION→PREUVE | [[concepts/anti-ai-writing]] |
| 7 | **FAQ micro-intentions** | Questions longue traîne stade "presque convaincu" — capture intentions décision | Passage Ranking, AI Overviews |
| 8 | **Article final** | Compilation, vérification anti-patterns IA, passage ancré, bloc authorship | [[concepts/anti-ai-writing]], [[concepts/grounding-score]] |

## Logique de chaînage

```
Brief → Étape 1 (Surprise Gap)
          ├→ Étape 2 (Ancrage local) ──────→ Étape 6
          ├→ Étape 3 (Données) → Étape 4 → Étape 6
          └→ Étape 5 (Architecture) → Étape 6 → Étape 7 → Étape 8
```

## Variables d'entrée

`[MOT-CLÉ]` · `[STRUCTURE HN]` · `[IDÉES]` · `[LOCALISATION]` · `[SECTEUR]` · `[AUDIENCE]`

## Principes éditoriaux

- **Surprise Gap** : apporter ce que le lecteur ne sait pas encore
- **Ancrage local** : chaque détail géographique = signal E-E-A-T
- **Données argumentatives** : chaque chiffre a une implication comportementale
- **Inversions expertes** : corriger une croyance fausse > confirmer une vérité connue
- **Low→High Surprise** : chaque section rappelle la précédente, ajoute du neuf ([[concepts/surprise-metric]])
- **Prose continue** : zéro bullet dans le corps, transitions causales

## Automatisation

Le workflow peut être automatisé via un Artifact React appelant l'API Claude en séquence (mentionné comme `editorial-workflow.jsx` dans le fichier source). En manuel : copier-coller chaque prompt dans Claude.

## Pages liées

[[concepts/workflow-redaction-8-etapes]] · [[concepts/surprise-gap]] · [[concepts/surprise-metric]] · [[concepts/grounding-score]] · [[concepts/information-gain]] · [[concepts/data-proprietaire]] · [[concepts/anti-ai-writing]] · [[concepts/ingenierie-semantique-inversee]]
