---
type: source
source_type: article
title: Mon process COMPLET pour vérifier l'indexation avec Claude
aliases: [algorithme-process-verifier-indexation]
tags: [algorithme, tim, indexation, claude, seo]
created: 2026-05-13
updated: 2026-07-05
sources: 1
confidence: high
status: stable
---

# Mon process COMPLET pour vérifier l'indexation avec Claude

**Auteur** : Timothée Boussardon (algorithme.substack.com)
**Type** : newsletter / article
**URL** : https://algorithme.substack.com/p/mon-process-complet-pour-verifier
**Date publication** : 2026-05-13

## Contexte
Tim décrit sa routine d'audit d'indexation entièrement pilotée par Claude, sans outil SEO tiers payant. L'angle : une page non indexée = zéro trafic, et le spam IA aggrave les problèmes d'indexation. Il pose un skill Claude qui vérifie 9 points par URL et sort un rapport markdown priorisé, ponctuel ou planifié via `/schedule`.

## Chiffres / faits clés
- 38 % des 2 millions de pages analysées par Ahrefs (2023) n'ont jamais été indexées.
- 51 % des 4 millions de pages analysées par Onely (2024) n'ont jamais été indexées.
- Seuil de 500 URLs avant de basculer vers un outil d'indexation traditionnel.
- Claude Pro à 20 €/mois ; Claude Max à 100-200 €/mois pour les routines parallèles.
- Environ 1 heure de mise en place de la routine.
- Espacement de 3 à 5 secondes entre chaque requête Google (obligatoire).
- Fiabilité estimée de la méthode de scraping `site:` : 40 à 60 %.
- Seuil de 300 mots minimum pour éviter le classement thin content.
- Sitemap : lastmod de plus de 6 mois considéré comme périmé.
- Les 9 points vérifiés par URL : statut HTTP et redirections, robots.txt, balises noindex (HTML/header), présence et fraîcheur du sitemap, cohérence sitemap ↔ source de vérité, maillage interne, longueur de contenu, statut d'indexation Google (requête `site:`), rapport markdown.
- Sources de la liste d'URLs à monitorer : fichier local, sitemap.xml, ou API GSC.

## Citations marquantes
> "une page non indexée par Google = 0 trafic" (attribution : Tim, 2026-05-13)

> "avec le spam IA, les problèmes d'indexation se multiplient" (attribution : Tim, 2026-05-13)

> "La méthode fonctionne sur tous les CMS" (attribution : Tim, 2026-05-13)

## Angle SEO à retenir
- L'indexation redevient un levier de premier plan à mesure que le spam IA sature les index Google : vérifier avant d'optimiser.
- Un skill Claude + `/schedule` remplace un outil payant jusqu'à ~500 URLs, sans équipe technique ni dépendance au CMS.
- La distinction "non indexée" vs "non testable" (rate-limit Google) est explicite : la fiabilité `site:` plafonne à 40-60 %, à assumer dans le reporting.

## Limites
- Scrape propre et complet, article non paywallé.
- La fiabilité `site:` de 40-60 % est un estimé de Tim, non un chiffre externe vérifié.
- Les taux Ahrefs 2023 et Onely 2024 sont cités sans lien direct dans le résumé du scrape (à re-sourcer avant réemploi public).

## Pages liées
**Concepts** : [[concepts/gsc-export]] · [[concepts/cli-tools-optional]]
**Entity** : [[entities/gsc]]

**Voir aussi** (curation 2026-07-05) : [[entities/ahrefs]]
