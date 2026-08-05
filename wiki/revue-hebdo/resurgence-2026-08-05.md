---
type: register
title: Résurgence — Wiki persistant vs RAG — 2026-08-05
tags: [resurgence, meta, rag, persistent-wiki]
created: 2026-08-05
updated: 2026-08-05
status: stable
---

# Résurgence — [[concepts/persistent-wiki-vs-rag]] — 2026-08-05

## Pourquoi celui-là

`updated: 2026-04-11` — 116 jours sans retouche, le concept fondateur du vault jamais réexaminé depuis sa création le jour du bootstrap. 33 backlinks : c'est le concept le plus référencé du vault après avoir exclu les hubs déjà passés en résurgence (`data-proprietaire` 2026-05-16, `grounding-score` 2026-06-12, `surprise-gap` 2026-06-24, `information-gain` 2026-07-15 — tous hors fenêtre 8 semaines sauf les deux derniers, écartés). Concept structurel : toute l'architecture `AGENTS.md` (§3, §7ter) en découle.

## État vs aujourd'hui

Le concept pose un argument d'échelle explicite de [[entities/karpathy]] : *"pour ~100 sources / quelques centaines de pages, un simple `index.md` suffit — pas besoin d'infrastructure RAG à base d'embeddings"*. Le concept-frère [[concepts/cli-tools-optional]] (même source, même date) anticipait la suite : *"quand ça grossit, un moteur de recherche sur les markdown devient l'outil le plus évident à ajouter"*.

Vérification factuelle aujourd'hui : `wiki/sources/` compte **110 fichiers** — le vault a franchi le seuil des ~100 sources que la source elle-même désignait comme le point de bascule. Et le tooling a effectivement émergé : commit `2026-05-26 "Sync vault : infra index ./kb + backfill frontmatter raw/"` a introduit `.claude/vector-store/` (ChromaDB, embeddings `paraphrase-multilingual-mpnet-base-v2`) + `.claude/index/concepts.json`, documentés en §7ter d'`AGENTS.md`. C'est exactement la trajectoire que [[concepts/cli-tools-optional]] prédisait — mais ni ce concept ni [[concepts/persistent-wiki-vs-rag]] n'ont été mis à jour pour l'acter.

Le point important : ce n'est pas un simple "la prédiction s'est réalisée, cocher la case". Le vault n'a pas remplacé le wiki par du RAG — il a superposé les deux. `./kb search` fait de la recherche cosinus sur des embeddings (RAG au sens strict), mais chaque chunk garde ses métadonnées frontmatter (type, tags, status, confidence) pour un filtrage déterministe avant la recherche sémantique, et le graphe `concepts.json` (wikilinks, backrefs) reste la structure atomique de référence. Le cadrage binaire "wiki persistant **vs** RAG" du concept ne tient plus tel quel : la réalité observée est un système hybride où le RAG sert de couche de récupération *au-dessus* d'un wiki qui reste la structure qui compile et maintient le savoir. La distinction qui compte n'est plus "wiki ou RAG" mais "qui compile" (le wiki, une fois, en continu) vs "qui récupère" (le vector store, à chaque query) — ce sont deux couches complémentaires, pas deux architectures concurrentes.

Par ailleurs :
- **H-004** (`wiki/hypotheses.md`) — "une page entity/wiki est mieux citée en SGE qu'une page statique" — reste `ouvert`, jamais testé depuis sa création le 2026-04-12. Pas de drift ici, juste confirmation que la boucle apprentissage n'a pas encore produit de preuve dessus.
- La question ouverte du concept (*"les moteurs génératifs sont-ils du RAG stateless ou maintiennent-ils un état persistant ?"*) reste non résolue : aucune source ingérée depuis le 2026-04-11 ne l'adresse frontalement.
- La "Limite importante" déjà notée dans le concept (*"la source ne benchmarke pas les deux approches"*) tient toujours — rien depuis n'a apporté de données comparatives MRR/latence/coût.

## Verdict proposé pour la revue hebdo

- [ ] Toujours juste, rien à faire
- [x] À mettre à jour : reformuler le cadrage "wiki persistant vs RAG" en "wiki persistant + RAG comme couches complémentaires", documenter le franchissement du seuil ~100 sources (110 aujourd'hui) et l'infra `./kb` (ChromaDB, 2026-05-26) comme confirmation empirique de [[concepts/cli-tools-optional]], et croiser avec §7ter d'`AGENTS.md` + le skill `kb-semantic-search`. Mettre à jour [[concepts/cli-tools-optional]] en miroir (même correction).
- [ ] À challenger : [quelle source/hypothèse l'attaque]
- [ ] Wording à corriger : [quelle règle]

## [2026-08-05] resurgence | [[concepts/persistent-wiki-vs-rag]] — verdict proposé

Résurgence 2026-08-05 : concepts/persistent-wiki-vs-rag — verdict : à mettre à jour, le vault a franchi le seuil ~100 sources (110) et bâti l'infra RAG (./kb, ChromaDB, 2026-05-26) que le concept jugeait non nécessaire à cette échelle — le cadrage binaire doit devenir "couches complémentaires" (à arbitrer en revue hebdo).
