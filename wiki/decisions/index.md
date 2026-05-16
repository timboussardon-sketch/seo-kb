---
type: register
title: Journal de décisions (ADR)
aliases: [decisions, adr-index, journal-decisions]
tags: [meta, decision, adr]
created: 2026-05-16
updated: 2026-05-16
sources: 0
confidence: high
status: living-doc
---

# Journal de décisions (ADR)

> Les "pourquoi on a décidé X" étaient noyés dans [[log]] et dans le versioning d'[[index|AGENTS.md]]. Dans six mois, impossible de reconstituer le raisonnement derrière une structure du système. Une ADR fige le contexte, la décision, et surtout les alternatives écartées, au moment où c'est encore frais.
>
> Une ADR n'est pas un compte rendu d'action (ça, c'est [[log]]). C'est une décision structurante : un choix d'architecture KB, d'automation, de doctrine ou de business qui contraint les choix futurs. Nouveau modèle à créer → ADR. Skill ou routine ajouté → ADR si le choix avait des alternatives sérieuses.

## Statuts

- `proposed` : en discussion
- `accepted` : en vigueur
- `superseded` : remplacée par une ADR plus récente (lien vers elle, on ne supprime jamais)
- `deprecated` : abandonnée sans remplacement

## Registre

| ADR | Titre | Statut | Date |
|---|---|---|---|
| [[decisions/0001-fermeture-boucles-second-cerveau\|ADR-0001]] | Fermeture des trois boucles ouvertes du second cerveau | `accepted` | 2026-05-16 |

Pages liées : [[index]] · [[log]] · [[hypotheses]] · [[ingest-backlog]]
