---
type: synthese
title: "Audit doctrine SEO Tim 2026 — ce qui dysfonctionne"
aliases: [audit-doctrine-2026, dysfonctionnements-doctrine]
tags: [doctrine-tim, audit, meta, 4-piliers, geo, pseo]
created: 2026-06-01
updated: 2026-06-01
sources: 4
confidence: high
status: stable
---

# Audit doctrine SEO Tim 2026 — ce qui dysfonctionne

Audit critique de la doctrine (4 piliers + process B2B 2026 + règles absolues), sur pièces. Sources lues : [[concepts/methode-organikk-4-piliers]], [[sources/process-seo-b2b-2026]], [[sources/tim-my-rules]], [[concepts/metriques-visibilite-geo]].

## Verdict
Doctrine juste sur le *quoi* (acquisition > trafic, actionnel > volume, data propriétaire > outils). Trois failles structurelles : elle prescrit des KPI qu'elle ne sait pas mesurer, promet une échelle que ses propres règles qualité interdisent, et dépend d'une maturité data que la majorité des prospects n'ont pas.

## Dysfonctionnements (par gravité)

| # | Dysfonctionnement | Gravité | Où |
|---|---|---|---|
| 1 | Pilier apex (AEO) a un KPI non mesurable | Critique | `metriques-visibilite-geo` L78 : pas d'outil pour mesurer la citation sur son propre site |
| 2 | "GSC = seule source de vérité" mais GSC ne voit pas les citations IA | Critique | `tim-my-rules` L32 vs pilier 4 |
| 3 | Règle "max 30 % IA / 8 étapes" incompatible avec "scaler 1000 pages" | Critique | `tim-my-rules` L27-28 vs process B2B L83-107 |
| 4 | Prio repose sur le CPC, issu des outils rejetés | Majeur | process B2B L54 vs L22 |
| 5 | Dépendance à une stack data que les prospects n'ont pas | Majeur | process B2B L40-44 |
| 6 | "Unicité > 60 % = Google indexe" : folk-SEO présenté comme fait | Majeur | process B2B L105, viole la règle anti-invention L21 |
| 7 | "Test ChatGPT 2 questions" subjectif et qui se périme | Modéré | process B2B L158-163 |
| 8 | Zéro stratégie off-site / entité / autorité | Modéré | absent du corpus |
| 9 | Ordre contradictoire pyramide (Surprise) vs cadre d'audit (Grounding) | Mineur | `4-piliers` L26 vs L57 |

## Les 3 critiques de tête

1. **KPI fantôme.** Pilier 4 (AEO) = "taux de citation génératif", mais aucun instrument pour le mesurer et GSC ne l'expose pas. Le sommet de la pyramide est piloté à l'aveugle. Fix : tracker de citations (10-20 prompts cibles rejoués chez Perplexity/ChatGPT/Gemini, scoré façon `Imp_pos`), ou rétrograder AEO de "KPI" à "principe de structuration".

2. **La règle qualité tue le scale.** "Humain donne la réflexion, IA améliore" + "max 30 % IA" + "8 étapes" vs pSEO 30-1000 URLs. Pas les deux sur le même budget. Fix : deux régimes explicites — pages pilier (règle 30 %, 8 étapes) vs pages programmatiques (data conditionnelle + QA par échantillon).

3. **Scoring circulaire.** Bannir Semrush/Ahrefs + "le volume n'est pas un signal", mais scorer en `CPC × intent × proximité`. Le CPC vient des mêmes outils, et les actionnels longue traîne n'ont ni volume ni CPC. Fix : remplacer le CPC par un proxy maîtrisé (fréquence dans les calls clients × étage de décision).

## Contradictions internes
- Optimiser l'existant AVANT de créer (règle) vs doctrine create-first (30-50 URLs + pSEO). Hiérarchiser selon la maturité du client.
- "L'audit vient APRÈS la stratégie" (règles) vs "cadre de décision : par où commencer un audit" (4-piliers). Trancher le rôle de l'audit.
- Pyramide "Surprise d'abord" vs cadre d'audit "Grounding d'abord".

## Angle mort : le hors-site
Corpus entièrement on-page/on-site. Rien sur mentions de marque, entité Knowledge Graph, notoriété, digital PR. Or la citation LLM corrèle avec la notoriété de marque, pas seulement la qualité on-page. Corrigeable sans achat de lien : entité structurée, cohérence NAP, présence sur les corpus ingérés par les LLM.

## Ce qui tient
Recentrage trafic → acquisition (en avance). Product-Led SEO (outil = page Do = lead) : meilleur asset, difficilement copiable. Data propriétaire comme source de mots-clés : juste sur le principe. [[entities/golfiller]] prouve le système quand les conditions sont réunies.

## Quick fixes (par effort)
1. Écrire les deux régimes de production (pilier vs programmatique) avec seuil d'IA respectif.
2. Retirer ou sourcer le "unicité > 60 %".
3. Définir une cadence de re-test du "test ChatGPT" (trimestriel).
4. Brancher un tracking de citations IA minimal (10-20 prompts/mois).
5. Ajouter une couche transversale "Autorité hors-site / Entité".

## Pages liées
[[concepts/methode-organikk-4-piliers]] · [[sources/process-seo-b2b-2026]] · [[sources/tim-my-rules]] · [[concepts/metriques-visibilite-geo]] · [[concepts/product-led-seo]] · [[concepts/data-proprietaire]] · [[concepts/aeo]]
