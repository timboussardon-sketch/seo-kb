---
type: moc
title: MOC — Méthode KB et système
aliases: [moc-methode-kb, moc-systeme, moc-kb]
tags: [moc, kb, systeme, meta]
created: 2026-05-16
updated: 2026-05-16
sources: 0
confidence: high
status: living-doc
---

# MOC — Méthode KB et système

> Le système qui produit tout le reste. À relire avant de modifier le schéma ou d'ajouter une routine. La décision fondatrice de la dernière refonte : [[decisions/0001-fermeture-boucles-systeme]].

## Ordre de lecture

1. [[concepts/persistent-wiki-vs-rag]] — pourquoi un wiki maintenu par LLM bat un RAG stateless
2. [[sources/2026-04-11-karpathy-llm-wiki]] — le pattern fondateur
3. [[concepts/ingest-workflow]] — 1 source → 10-15 pages touchées
4. [[concepts/query-synthesis]] — les questions filées comme pages permanentes
5. [[concepts/memory-llm-vs-wiki-persistant]] — la distinction mémoire vs wiki
6. [[concepts/obsidian-as-ide]] — Obsidian = IDE, LLM = programmeur
7. [[queries/2026-04-12-wiki-pattern-vs-grounding-score]] — la question méta encore ouverte

## Les boucles fermées (refonte 2026-05-16)

- Capture → traitement : [[ingest-backlog]] (sweep hebdo)
- Doctrine → validation : [[hypotheses]] + [[contradictions]] (validation mensuelle)
- Sortie → apprentissage : [[preuves/index]] (manuel)
- Édition → édition (en cadrage) : [[methodes/cadrage-boucle-edition-algorithme]] — SyntheticBrain, la boucle qui rend Algorithme meilleure d'une édition à l'autre
- Décision : [[decisions/index]]
- Rituel : [[revue-hebdo/index]] (vendredi) + résurgence (mercredi)

## Plomberie

[[index]] (catalogue) · [[log]] (journal append-only) · [[000-home]] (carte d'entrée) · AGENTS.md (schéma, racine repo)

## Ce qui n'est pas tranché ici

- [[hypotheses#H-004]] page entity/wiki mieux citée que page statique (`ouvert`) — l'hypothèse méta sur laquelle repose tout le pari
- Le système d'automation a 8 LaunchAgents : surveiller le dashboard pour les jobs en échec

Pages liées : [[000-home]] · [[decisions/index]] · [[hypotheses]] · [[contradictions]] · [[ingest-backlog]]
