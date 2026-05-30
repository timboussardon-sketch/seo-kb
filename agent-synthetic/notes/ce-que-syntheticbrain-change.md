---
type: note
title: "Ce que SyntheticBrain change vs la revue de presse classique"
date: 2026-05-30
tags: [synthetic-brain, doctrine, meta]
---

# Ce que SyntheticBrain change vs la revue de presse classique

La revue de presse classique (`revue-presse-quotidienne`) est **sans mémoire**. Chaque matin elle repart de zéro : elle scanne, elle rédige, elle oublie. Le lendemain, elle ne sait pas ce qu'elle a dit la veille, ne sait pas si elle avait raison, ne sait pas quelles sources lui ont donné du bon ou du bruit. Elle répète. Elle ne progresse pas.

SyntheticBrain garde cette revue de presse comme **moteur d'écriture** (il l'enveloppe, il ne la remplace pas) et ajoute autour ce qu'une revue classique n'a jamais eu.

## 1. Une mémoire qui survit entre les éditions

Avant : rien ne persistait. Maintenant : chaque édition lit ce que les précédentes ont appris (`ledgers/`, `memory/`) et écrit ce qu'elle apprend pour la suivante. C'est la différence entre répéter et progresser.

Preuve : l'édition v3 (Universal Cart) a lu que v2 avait déjà traité « Information Agents » et a choisi un autre angle toute seule pour éviter la redite.

## 2. Il cherche de nouvelles sources tout seul

Avant : liste de sources figée dans le script. Maintenant : à chaque édition il part des sujets chauds et va chercher qui fait autorité dessus. Au premier jour il a découvert et qualifié 4 sources neuves seul (Lumar, Cloudflare Radar, Similarweb, Seer), avec un score de confiance. La liste vit, grossit, se nettoie. Règle dure : une source nouvelle peut lancer une piste mais ne suffit jamais à publier un claim.

## 3. Il se contre-checke au niveau du claim, pas de la source

Avant : « la source a l'air sérieuse, je cite ». Maintenant : chaque affirmation devient une ligne traçable (`claims.jsonl`) avec un verdict vérifié / réfuté / incertain. Au premier jour il a écarté 2 stats lui-même : une étude hors fenêtre de fraîcheur et un chiffre contradictoire entre deux sources.

## 4. Il se note et apprend de ses erreurs

Avant : aucune mesure de qualité, aucune trace d'erreur. Maintenant : une grille de score à chaque édition (`calibration.md`) plus un journal d'erreurs (`mistakes.jsonl`). Exemple : il a détecté seul que les résumés de recherche web redatent en 2026 des études de 2025, et a écrit sa propre règle pour ne plus se faire avoir.

## 5. Il fait des prédictions datées et se vérifie

Avant : des opinions jamais confrontées au réel. Maintenant : des prédictions avec date d'échéance (`predictions.jsonl`). À l'échéance, il vérifie s'il avait raison et ajuste sa confiance. L'intuition devient calibration mesurable.

## 6. Il tient à la doctrine

Avant : actu pure. Maintenant : il relie chaque sujet aux concepts du vault (`wiki/concepts/`) via `./kb search`. L'actu devient une grille de lecture Boussardon, pas un empilement de news.

## En une phrase

La revue classique **écrit** une newsletter. SyntheticBrain **tient un laboratoire** qui écrit une newsletter et devient meilleur à chaque numéro : il se souvient, il enquête, il se contredit quand il a tort, il se note, et il garde tout en git, auditable et réversible.

## Garde-fous

- Périmètre strict : SEO, IA, LLM, Google, moteurs de recherche, search marketing. Rien d'autre.
- Liens de sources toujours affichés dans le corps.
- Autonomie sur la data, jamais sur le code sans diff validé en revue hebdo.
- Rien n'est envoyé : SyntheticBrain produit un draft dans `syntheticrevuepress/`.
