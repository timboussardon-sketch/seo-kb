---
type: note
title: "Appliquer la mécanique SyntheticBrain à la prod SEO et au contenu"
date: 2026-05-30
tags: [synthetic-brain, doctrine, meta, seo, content-ops]
---

# Appliquer la mécanique SyntheticBrain à la prod SEO et au contenu

Note de réflexion. Ce qui rend SyntheticBrain utile, ce n'est pas la newsletter, c'est sa **mécanique de raisonnement**. Elle est transférable presque telle quelle à la production SEO et à la rédaction. Rien n'est construit à ce stade : c'est une note de cadrage.

## L'idée centrale

SyntheticBrain ne devient pas plus intelligent. Il tient un laboratoire : prompt figé et auditable, apprentissage dans une mémoire séparée, lue au début et enrichie à la fin. La mécanique de la boucle est décrite dans [[methodes/cadrage-boucle-edition-algorithme]]. Trois couches strictes : `ledgers/` (faits observés, append-only), `memory/` (interprétations durables, qui ne se durcissent qu'après validation humaine), `derived/` (vues calculées). On ne mélange jamais « j'ai mesuré » et « je pense ».

La boucle est déjà appliquée à la **doctrine** (revue-hebdo, hypotheses-validation, preuves-feedback, gsc-watcher, resurgence). Le manque : elle n'est pas appliquée à la **production de contenu client / Fusionn**. Le saut à faire est le même que celui de SyntheticBrain : passer d'un artefact écrit puis oublié à un artefact qui apprend de lui-même.

## Le mapping

| Mécanique SyntheticBrain | Application SEO / rédaction |
|---|---|
| Le claim est l'unité de qualité, pas la source (verdict vérifié/réfuté/incertain, sources, confiance) | Chaque chiffre / fait d'une page devient une ligne `claims.jsonl` du projet. Tue le slope IA, nourrit le Grounding Score. Seuls les `verified` entrent dans le corps. |
| Exploit + Explore sur les sources, trust score, règle dure « une source neuve lance une piste mais ne publie jamais seule » | Exploit = data connue (GSC, calls, SAV). Explore = chercher activement de nouvelles sources de verbatims / [[concepts/data-proprietaire]]. Structure le contexte propriétaire au lieu du feeling. |
| Prédictions datées + résolution → calibration | Publier une page = parier qu'elle rankera / sera citée sur telle requête. Logge la prédiction avec `resolve_by` J+30/J+90. gsc-watcher en résout déjà une partie. À l'échéance, on sait quels angles tiennent, mesuré. |
| Mistakes ledger (type / symptôme / cause / fix) | Chaque page qui sous-performe = une ligne. Au bout de 30 pages, une doctrine d'erreurs empirique, pas théorique. C'est ce qui différencie d'un acteur qui repart de zéro à chaque mission. |
| Grille de score mesurable + quality gate avant sortie | Gate de publication : Surprise Gap, densité de data réelle, intention décisionnelle, title intrigant vs racoleur. Le seo-geo-audit, mais systématisé et loggé dans le temps. |
| Anti-redite (`said_index`) | Index des angles/intentions déjà couverts par client. Avant de créer une page, vérifier qu'on ne reprogramme pas une cannibalisation. |
| capture_mode native vs reconstructed | Ne jamais confondre une mesure prise en direct (GSC réelle) et une estimation reconstruite après coup. C'est la règle anti-hallucination. |
| Prompt figé, humain au contrôle, tout en git | Les skills SEO sont le prompt figé. L'apprentissage vit dans la mémoire projet, pas dans les skills. L'agent propose un diff, validation en revue hebdo. Autonome sur la data, jamais sur le code. |

## Le plus gros levier

Un **content brain par projet** (ou un pour Fusionn), calqué sur l'archi SyntheticBrain : `ledgers/` (claims, predictions, mistakes, said_index) + `memory/` (directives, grille de score) + `derived/` (dashboard). Chaque page produite logge ses claims, une prédiction datée et un score. Chaque pull GSC résout les prédictions. Au bout de quelques mois, la prod devient la meilleure source de doctrine, et c'est montrable à un prospect : « voilà ce que mes pages ont prédit, voilà ce qui s'est réalisé ».

80 % des briques existent déjà (gsc-watcher, preuves-feedback, hypotheses-validation). Ce qui manque : les organiser en un même labo append-only au niveau de la production, pas seulement de la doctrine.

## Pistes de premier pas (non décidées)

- Brancher le fact-check au niveau du claim sur `article-engine-pipeline` (sortie : un `claims.jsonl` par article).
- Un skill `content-brain` qui enveloppe le pipeline article comme `agent-synthetic` enveloppe `revue-presse-quotidienne`.
- Réutiliser la grille de score de `calibration.md` comme gate de publication contenu.

## Liens

- [[syntheses/workflow-complet-consultant-seo-ia]] — le workflow consultant où cette mécanique s'enclenche côté production.
- [[methodes/cadrage-boucle-edition-algorithme]] — la boucle d'origine, transférée ici à la prod.
