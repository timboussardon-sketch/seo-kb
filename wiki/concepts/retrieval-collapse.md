---
type: concept
title: Retrieval Collapse (effondrement du retrieval IA)
aliases: [retrieval-collapse, effondrement-retrieval, ai-pollution-pool]
tags: [doctrine-tim, geo, ia, retrieval, contenu-ia, naver, paper]
created: 2026-05-01
updated: 2026-05-01
sources: 2
confidence: high
status: stable
---

# Retrieval Collapse

Phénomène d'effondrement progressif du retrieval LLM quand le pool web se pollue de contenu généré par IA. Concept formalisé empiriquement par [[entities/naver]] (paper arxiv 2602.16136, ACM Web Conference 2026).

## Mécanique

- À **67 % de pollution du pool**, on atteint **>80 % d'exposition contaminée** dans les réponses LLM
- **La précision des réponses reste stable** — le système semble en bonne santé pendant qu'il dérive vers du synthétique en circuit fermé
- Les rerankers LLM suppriment mieux le contenu malicieux que BM25 (19 % d'exposition) **mais ne détectent PAS la dérive synthétique normale**
- Conclusion : les moteurs IA ont un **besoin existentiel de signaux d'humanité vérifiable** pour ne pas s'effondrer

## Pourquoi c'est doctrinal

- Validation académique frontale de [[concepts/data-proprietaire]] et [[concepts/e-e-a-t]] (Experience humaine vérifiable)
- Justifie scientifiquement pourquoi : (1) les fermes d'articles IA seront détectées et rétrogradées (cf Core Update mars 2026, [[sources/2026-04-22-algorithme-core-update-fermes-ia]]), (2) calls clients / screenshots GSC / verbatims terrain deviennent les nouveaux "vecteurs gagnants", (3) [[entities/linkedin]] comme 2e source IA prend tout son sens — signal humain non-fakeable à grande échelle
- Argument vente direct : "le risque pour ton site n'est pas de mal ranker, c'est d'être noyé dans un pool synthétique invisible"

## Implications pour la doctrine

- Bascule de 30 % du budget contenu vers data propriétaire (calls, screenshots GSC, verbatims clients)
- LinkedIn comme 2e source de signal humain pour le B2B
- Préférer le test substitution LLM ([[concepts/test-substitution-llm]]) à 80 % de contenu reformulé reformulable
- Cohérence avec le Core Update mars 2026 (-40 à -80 % sur les sites IA industrialisés sans supervision éditoriale)

## Limites

- Étude unique à date (NAVER, 2026), pas encore reproduite par d'autres labos
- Modélisation théorique du pool web — pas encore de tracking longitudinal du web réel
- Pas de prescription opérationnelle dans le paper (les implications doctrinales sont des inférences Tim)

## Pages liées

[[sources/2026-04-15-scan-arxiv-15-avril]] · [[sources/2026-04-25-scan-arxiv-25-avril]] · [[sources/2026-04-22-algorithme-core-update-fermes-ia]] · [[concepts/data-proprietaire]] · [[concepts/e-e-a-t]] · [[concepts/anti-ai-writing]] · [[concepts/surprise-gap]] · [[concepts/test-substitution-llm]] · [[entities/naver]] · [[entities/linkedin]]
