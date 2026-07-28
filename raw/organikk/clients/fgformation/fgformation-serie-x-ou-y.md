---
type: source
source_type: client-note
title: FG Formation — Série comparative « X ou Y » sur les accompagnements Qualiopi
tags: [seo, fgformation, comparatif, pseo]
created: 2026-07-24
updated: 2026-07-24
confidence: medium
status: draft
---

# Série « X ou Y » — les accompagnements Qualiopi

> **En résumé.** Une série de pages comparatives, un duel par page, sur les différentes façons de se faire accompagner vers Qualiopi. Skill `comparatif-neutre` + règles de rédaction FG. Jamais de marques concurrentes (règle FG déjà consignée dans [[fgformation-patterns-requetes]]) : on compare des MODALITÉS d'accompagnement, pas des prestataires. FG est juge et partie sur la plupart des duels → transparence annoncée dans le chapô, et on dit où l'option FG est en retrait.

## Cadrage du périmètre

On compare les voies d'accès à la certification Qualiopi entre elles. Exclusions :

- **Les marques et prestataires nommés** (autres consultants, cabinets, logiciels). Règle FG. On compare « un consultant » à « un logiciel », jamais « FG Formation » à « [cabinet X] ».
- **RNCP ou Qualiopi** : page existante `le-guide/qualiopi-cest-quoi/rncp-ou-qualiopi/`.
- **Formateur indépendant vs organisme de formation** : page existante `formateur-independant-vs-organisme-de-formation/`.
- **Se certifier ou passer par le portage** : la page portage rédigée le 20/07 couvre déjà l'arbitrage. Un duel dédié cannibaliserait. On maille vers elle.

## Les duels proposés (ordre de production recommandé)

| # | Duel | Requête type (corpus) | Position FG |
|---|---|---|---|
| 1 | Se faire accompagner ou passer Qualiopi seul | « passer qualiopi seul ou accompagné » | Juge et partie |
| 2 | Consultant Qualiopi ou logiciel Qualiopi | « consultant ou logiciel qualiopi » | Juge et partie |
| 3 | Formation Qualiopi ou accompagnement individuel | « formation ou accompagnement qualiopi » | Double juge et partie (FG vend les deux) |
| 4 | Kit de documents Qualiopi ou accompagnement | « kit documentaire qualiopi » | Juge et partie |
| 5 | Audit blanc seul ou accompagnement complet | « audit blanc qualiopi » | Juge et partie |
| 6 | Consultant indépendant ou cabinet d'accompagnement | « quel accompagnement qualiopi choisir » (#26 du corpus) | Juge et partie |
| 7 | Accompagnement à distance ou en présentiel | dérivé des pages locales existantes | Neutre |

Candidat écarté pour l'instant : « acheter un organisme déjà certifié ou se certifier » (angle anti-fraude V10, réel sur le marché, mais sourcing lourd sur le transfert de certification — à instruire séparément).

## Adaptation du modèle « X ou Y » aux règles FG

Le modèle de page duel (figé sur Qadence le 24/07) s'applique avec ces adaptations :

- **Sources** : uniquement nos données (14 calls, audits blancs) + sources officielles (RNQ, guide de lecture V9, Légifrance). Pas de doc éditeur tiers, pas d'avis Reddit, pas de fiche fondateur — ces sections du modèle Qadence sautent.
- **Prix** : aucun barème de marché inventé. Le tarif FG renvoie à la page tarif du site. Les montants entendus en call restent de la matière (témoignages anonymisés), jamais un barème. Ce qui n'est pas publiable est marqué « non documenté publiquement ».
- **Structure FG** (règles de rédaction, §8) : réponse en tête 40-60 mots avant le premier H2, y compris quand elle dessert l'offre ; 9 H2 minimum (fan-out) ; bloc « le point où ça bloque » ; FAQ tirée des objections réelles ; bloc auteur ; bloc Sources ; notes de production à retirer avant mise en ligne.
- **Transparence** : chapô qui annonce que FG vend l'une des deux options (ou les deux, duel 3). La grille reste identique et la page nomme les cas où l'autre option est le bon choix (budget serré, OF déjà structuré, simple mise à jour documentaire…).
- **Grille stable** sur toute la série : qui fait le travail / ce qui est couvert du référentiel (32 indicateurs) / responsabilité au moment de l'audit / temps à y consacrer / coût (structure, pas montants inventés) / ce qui se passe après la certification (surveillance).
- Vouvoiement, aucun tiret cadratin, une page à la fois, validation Tim entre chaque.

## Maillage

Chaque duel maille vers : la page offre `laccompagnement-fg-formation/`, la page tarif `le-guide/qualiopi-cest-quoi/accompagnement-qualiopi-tarif/`, et les autres duels de la série au fur et à mesure. La vieille page `le-guide/choisir-bon-partenaire-certification-qualiopi/` (checklist générique faible) pourra devenir le hub « choisir son accompagnement » après refonte — chantier séparé, à proposer à François.

## Journal

- **2026-07-24** : cadrage de la série validé à produire. Sitemap re-crawlé via l'API WordPress (215 URLs) : duels RNCP/Qualiopi et formateur/OF déjà pris, aucun doublon sur les 7 duels retenus.
- **2026-07-24** : duel 1 rédigé (« Passer Qualiopi seul ou accompagné »), Tim a choisi ce point de départ. Draft dans `pages/2026-07-24-passer-qualiopi-seul-ou-accompagne.md`. Faits re-vérifiés en source primaire le jour même : décret 2019-565 (annexe 7 critères / 32 indicateurs), arrêté 6 juin 2019 en vigueur (durées d'audit, surveillance 14e-22e mois à distance, NC mineure 6 mois / majeure 3 mois, certification 3 ans), arrêté du 1er juillet 2025 sans impact.
- **2026-07-24 (suite)** : duel 1 relu avec les skills ton-de-voix-tim + copywriting après remarque de Tim (titres factuels, patterns IA corrigés, CTA contact). Règle pour toute la série : charger les deux skills AVANT de rédiger.
- **2026-07-24 (fin)** : duels 2 à 7 rédigés sur demande de Tim (« un par un le reste »). Les 7 pages sont dans `pages/` et dans le Drive client `fg-formation/modele DUEL/` (un Google Doc par duel, converti avec mise en forme). Anti-cannibalisation vérifiée : le duel 2 maille vers `avis-logiciel-qualiopi-pour-un-of/` (qui garde la reco d'outils), le duel 5 vers `le-guide/audit-blanc-qualiopi/` (qui garde le déroulé), le duel 6 vers `choisir-bon-partenaire-certification-qualiopi/` (candidate à une refonte en hub des 7 duels). Duel 3 = double juge et partie assumé (FG vend formation ET accompagnement) ; duel 7 = neutre. Aucun prix, aucune marque, verbatims anonymisés des calls. Série en attente de relecture Tim puis François avant toute intégration WordPress.
- **2026-07-24 (reprise anti-IA)** : Tim a rejeté les 7 duels en bloc (« paterne IA partout », skills copywriting/ton-de-voix pas réellement appliqués). Repasse complète des 7 pages, skills `ton-de-voix-tim` et `copywriting` rechargés en tête. Corrigé : le miroir « X fait ceci, Y fait cela » posé en chapô ET en H2 de 6 pages sur 7 (seul le duel 1 y échappait) — chaque chapô réécrit avec une construction d'ouverture distincte (question de décision, fait réglementaire, critère en tête) au lieu du gabarit répété ; antithèses rhétoriques bannies (« n'est pas X, c'est Y », « le problème n'est pas X, c'est Y », « plutôt que », « au lieu de ») réécrites en affirmatif sur les 7 pages ; personnification retirée (« les documents racontent leur propre histoire » → dates incohérentes que l'auditeur repère) ; éditorialisation retirée (« Il a raison, et un prestataire honnête doit savoir l'entendre. », « C'est le bon réflexe. ») ; une phrase creuse signalée en direct par Tim en cours de repasse (« un accompagnement apporte en général ses propres trames, adaptées avec vous » — ne disait rien de concret) réécrite avec le mécanisme réel (trames construites à partir des formations réelles du client) ; la formule « voici/ce que nos audits blancs montrent » dégonflée (répétée 5+ fois sur la série) et variée page par page ; une incohérence logique repérée en passant (duel 7 : « la surveillance en visioconférence... se répète en visioconférence ») corrigée. Aucun fait, chiffre, source ou verbatim modifié : uniquement la forme.
