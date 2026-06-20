---
type: concept
title: Preuve atomique (claim)
aliases: [preuve-atomique, claim, claim atomique, preuve]
tags: [synthetic-brain, fact-check, methode, sources]
created: 2026-06-20
updated: 2026-06-20
confidence: high
status: stable
---

# Preuve atomique (claim)

L'unité vérifiée de la méthode SyntheticBrain : une affirmation **atomique** (un seul fait), rattachée à sa source, qu'on peut confirmer ou réfuter seule. C'est la brique qui empêche le contenu de glisser vers le générique ou l'halluciné.

## Critères d'un claim valide
- **≥ 2 sources** indépendantes (détection du sourcing circulaire), idéale **primaire**.
- **Anti-fraîcheur** : on borne la date et on écarte le périmé.
- **Fait ≠ interprétation** : on sépare la donnée vérifiable de la lecture qu'on en fait.
- Verdict par claim : Confirmé / Fragile / Non vérifiable / Contredit, puis action (garder / reformuler / mieux sourcer / retirer).

Lié à : [[grounding-score|Grounding]] (preuve chiffrée et sourcée), [[information-gain]] (apport réel d'info). Outillé par les skills `breves-factcheck` et la boucle de fact-check de `agent-synthetic` / `content-brain`.
