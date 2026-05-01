---
type: source
source_type: paper
title: Titans — Architecture à mémoire neurale (Google DeepMind)
aliases: [titans-paper, titans-architecture]
tags: [architecture-ia, google-deepmind, neural-memory, surprise-metric, weight-decay, geo, aeo]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: high
status: stable
---

# Titans — Architecture à mémoire neurale (Google DeepMind)

**Auteurs** : [[entities/google-deepmind]]
**Type** : paper recherche (preprint / publication interne, lien non disponible dans la source)
**Fichier raw** : `raw/papers/titans-architecture-google-deepmind.md`
**Date** : 2024-2025

---

## Contexte

Architecture neurale introduisant la **test-time memorization** : le modèle décide en temps réel ce qu'il retient. Fondation théorique de toute la doctrine SEO post-SGE de Tim — jusqu'ici relayée via [[sources/2026-04-11-seo-ia-tim]] (doctrine). Cette page est la **citation primaire paper** que les concepts dérivés référençaient transitivement.

## Méthode

Architecture en 3 couches, mécanismes de mémorisation et d'oubli adaptatif. Le raw note Tim ne détaille pas le protocole expérimental du paper original — les benchmarks (BABILong, contextes 2M+ tokens, comparatif GPT-4 / Mamba-2 / Transformer++) sont rapportés dans [[entities/titans]] mais non vérifiables ici sans accès au paper source.

## Chiffres clés

- **3 couches** : Core (attention) / Neural Memory (long-term, MLP profond) / Persistent Memory (faits invariants)
- **Surprise Metric** : gradient d'écart mémoire ↔ input → arbitre stockage / oubli
- **Weight Decay** : oubli adaptatif gérant la capacité finie

Aucun chiffre empirique propre dans le raw ; les benchmarks détaillés vivent dans [[entities/titans]].

## Résumé structuré

### Mécanique centrale

- **Low surprise** = info attendue → gradient faible → non stockée. Cf. [[concepts/surprise-metric]].
- **High surprise** = info inattendue → stockage permanent en Neural Memory.
- **Weight Decay** = forgetting gate, efface les signaux moins pertinents au fil du temps. Cf. [[concepts/weight-decay]].

### Implications structurelles SEO

Le contenu "consensus" (basse surprise) est oublié par les LLM. Le contenu avec **data propriétaire unique** (haute surprise) est mémorisé — fondement architectural du [[concepts/surprise-gap]] (80% consensus + 20% data unique) opérationnalisé par Tim.

### Pourquoi cette source compte

Avant ingest, les 5 concepts dérivés ([[concepts/surprise-metric]], [[concepts/weight-decay]], [[concepts/surprise-gap]], [[concepts/grounding-score]], [[concepts/information-gain]]) citaient [[sources/2026-04-11-seo-ia-tim]] (doctrine, confidence medium). L'ingest paper :
- Donne une **citation primaire paper** aux 5 concepts
- Justifie l'upgrade structurel : la mécanique vient du paper, l'application SEO reste hypothèse Tim (transfert non validé)

## Limites

- **Lien original non disponible** dans le raw — paper interne / preprint cité de mémoire par Tim
- **Pas de protocole expérimental détaillé** dans le raw — uniquement les conclusions
- **Transfert vers SEO non confirmé publiquement** : aucune source officielle Google ne confirme que Search/SGE utilise Titans. L'application reste hypothèse architecturale par analogie.

## Implications SEO

Cf. [[syntheses/doctrine-seo-post-sge]] (4 piliers) et [[queries/2026-04-12-wiki-pattern-vs-grounding-score]].

L'angle dominant : produire du contenu **high-surprise + grounded** = combinaison [[concepts/grounding-score]] (pertinence cosine) × [[concepts/surprise-metric]] (gradient d'information). Une page 100% pertinente mais redondante = gradient ≈ 0 = oubliée.

## Pages liées

**Entities** : [[entities/titans]] · [[entities/google-deepmind]]

**Concepts** : [[concepts/surprise-metric]] · [[concepts/weight-decay]] · [[concepts/surprise-gap]] · [[concepts/grounding-score]] · [[concepts/information-gain]]

**Sources** : [[sources/2026-04-11-seo-ia-tim]] (doctrine dérivée) · [[sources/2026-04-13-miras-architecture]] (extension Titans)
