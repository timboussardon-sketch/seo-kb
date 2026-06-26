---
client: leexi
type: cluster
theme: Cocon 3 — Problématiques IA métier (par fonction + secteur)
date: 2026-06-26
statut: architecture validée — cocon plein (décision révisée 2026-06-26)
pilier: l'IA qui résout un problème de métier → citation IA + conversion
related:
  - "[[leexi]]"
  - "[[cocon-1-notetaker-reunion]]"
  - "[[cocon-2-prise-de-notes-rgpd]]"
---

# Cocon 3 — Problématiques IA métier

> **Décision révisée 2026-06-26.** Le Cocon 3 est un **cocon plein**, pas une couche résiduelle. Son angle propre : la **problématique métier résolue par l'IA**, organisée par fonction (Sales, CS, Recrutement) et par secteur.
>
> **Ce qui le distingue du Cocon 1 (et lève la cannibalisation)** : le Cocon 1 cible la requête **produit** (`compte rendu rendez-vous commercial` = il cherche l'outil). Le Cocon 3 cible la requête **problème métier** (`comment automatiser le suivi de mes calls commerciaux`, `IA pour le suivi commercial` = il décrit sa douleur, pas le produit). Intentions différentes, pages différentes, personas au même métier mais à un autre étage de conscience.
>
> **Orientation GEO** : ces requêtes ont peu de volume Google FR mais sont massivement répondues par ChatGPT / Perplexity / AI Overviews. Le cocon vise donc la **citation IA** d'abord, et maille vers la page produit (cocon 1/2) qui convertit.
>
> **Seule règle anti-doublon** : si une requête est *littéralement* la même qu'une page produit du cocon 1 (`compte rendu X`), on garde la page produit et on traite l'angle « comment… » en section dedans. Sinon, page propre ici.

## Cadrage
- **Mère** : le hub « agent IA / IA pour les équipes en entreprise » (problème métier, pas page produit).
- **Format** : answer-first, problème en H1, réponse extractible (procédure / tableau), data propriétaire Leexi, CTA vers la page business.
- **Mesure** : citations IA + trafic référent (ChatGPT/Perplexity) + leads assistés par maillage.

---

## Branche A — IA pour les commerciaux (Sales)
| Page (problème métier) | Maille vers |
|---|---|
| comment automatiser le compte rendu d'un call commercial | Usage Sales (cocon 1) + essai |
| comment remplir son CRM après un rendez-vous sans saisie manuelle | Intégrations CRM + essai |
| comment suivre les objections clients sur tout le pipeline | Usage Sales + essai |
| automatiser le reporting commercial avec l'IA (tête à confirmer SERP) | Usage Sales + essai |
| IA pour le suivi commercial (tête à confirmer SERP) | Hub + intégrations CRM |

## Branche B — IA pour le Customer Success
| Page (problème métier) | Maille vers |
|---|---|
| comment réussir un onboarding client sans prendre de notes | Usage CS + essai |
| comment préparer un QBR à partir des verbatims clients | Cas clients + essai |
| comment ne plus oublier les actions de suivi après une réunion client | Essai |
| IA pour le suivi client (tête à confirmer SERP) | Hub + usage CS |

## Branche C — IA pour les RH / recrutement
| Page (problème métier) | Maille vers |
|---|---|
| comment structurer le débrief d'un entretien sans biais | Usage recrutement + essai |
| comment comparer deux candidats sur les mêmes critères | Usage recrutement + essai |
| comment gagner du temps sur les comptes rendus d'entretien | Usage recrutement + essai |
| IA pour le recrutement (tête à confirmer SERP) | Hub + usage recrutement |

## Branche D — Problématique IA par secteur
| Page (problème métier) | Maille vers |
|---|---|
| comment gérer les comptes rendus de mission en cabinet de conseil | Secteur conseil (cocon 1) + essai |
| comment automatiser les comptes rendus de rendez-vous client en cabinet comptable | Secteur comptable (cocon 1) + essai |
| comment automatiser le PV d'un conseil municipal / instance publique | Secteur public (cocon 1) + démo |

## Branche E — Hub agent IA (définition / choix)
> Signal GSC `agent ia entreprise` (310 impr, pos 4,1). Tête de cocon, maille vers tout le reste.

| Page | Maille vers |
|---|---|
| qu'est-ce qu'un agent IA en entreprise | Hub → branches métier |
| différence entre assistant IA et agent IA en entreprise | Hub → assistant réunion |
| assistant IA pour les réunions d'équipe : quel outil choisir | Assistant de réunion IA + essai |
| meilleur agent IA pour entreprise / PME (comparatif 2026) | Comparatif + tarifs |
| agent IA pour équipe commerciale / sales | Branche A + intégrations CRM |
| comment utiliser un agent IA pour automatiser les comptes rendus | Pont vers le cocon 1 (compte rendu auto) |

---

## Maillage interne
- **Hub → branches métier → pages problème** ; chaque page problème maille vers la page produit (cocon 1/2) qui convertit.
- **Discipline anti-doublon** : une SERP = une page. Si `comment automatiser le compte rendu d'un call commercial` partage la SERP de `compte rendu rendez-vous commercial` (cocon 1), garder la page produit et y intégrer l'angle « comment » en section. À vérifier en overlap SERP réel.

## Données à re-sourcer avant publication (aucun chiffre inventé)
- « 61 % appliquent les actions décidées en réunion » (attribué HBR par l'IA) → source primaire ou retrait.
- « PV de conseil municipal : 2-4 h → -70/-80 % » → re-sourcer.
- Stats d'usage Leexi (gain de temps réel) = data propriétaire à fournir, carburant de citation IA.

## Roadmap
- **Vague 1** : hub agent IA (définition + assistant réunion d'équipe) + débrief sans biais + CRM sans saisie (les plus citables).
- **Vague 2** : objections pipeline, onboarding sans notes, QBR verbatims, actions de suivi, têtes métier (IA pour le suivi commercial / client / recrutement) après confirmation SERP.
- **Vague 3** : les 3 problématiques sectorielles.
