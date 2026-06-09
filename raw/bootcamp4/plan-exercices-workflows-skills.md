---
title: "Plan d'action — Exercices testables par workflow et par skill (bootcamp)"
bootcamp: 4
type: plan
created: 2026-06-09
usage: "Plan pour créer des exercices que les participants exécutent eux-mêmes, illustrés comme la fiche Passer de Cowork à terminal. À valider avant production."
related:
  - "[[passer-cowork-vers-terminal]]"
  - "[[skills-checklist-bootcamp4]]"
  - "[[workflow-audit-bootcamp4]]"
---

# Plan d'action — Exercices bootcamp (par workflow et par skill)

## En résumé

On a tout le matériel : 4 workflows (sessions 1 à 4), ~23 skills documentés, un dashboard React, et le gabarit pédagogique de [[passer-cowork-vers-terminal]]. Ce qui manque, ce sont des exercices que le participant fait lui-même, avec un cas réel et un résultat attendu visible (le « screen »).

Le plan : un gabarit d'exercice unique (dérivé de la fiche Cowork), un cas fil rouge partagé (mêmes données pour tous), 4 exercices « workflow » (capstones de session) + un micro-exercice par skill, et un pilote de 2 exercices à valider avant de produire le reste.

## 1. Le gabarit d'un exercice

Repris de la fiche Cowork (étapes numérotées, blocs de code, vérification inline, « comment ça marche », version WhatsApp), avec en plus un bloc résultat attendu (le « screen »).

```
# Exercice — [Skill ou Workflow] : [titre 5 mots max]
Niveau · Durée ~X min · Pré-requis (skill installé, export GSC fourni...)

## Le cas
2-3 phrases : la situation, les données fournies (du cas fil rouge).

## Ce que tu dois faire
1. [action] + le prompt/commande exact à coller (bloc de code)
2. [action] ...

## Ce que tu dois obtenir   ← le « screen »
Le résultat attendu, montré : capture ou exemple d'output réel
(tableau, page, sortie terminal). C'est la référence pour s'auto-évaluer.

## Vérifier que tu as réussi
- [ ] critère mesurable 1
- [ ] critère 2

## Le piège
L'erreur classique (ex : laisser le skill inventer un volume).

## Comment ça marche
L'explication mécanique en 2-3 phrases.

## Version WhatsApp
Résumé compact copiable.
```

## 2. La question des « screens » (à trancher avec toi)

La fiche Cowork de référence n'a aucune capture : elle marche au texte + blocs de code. Pour les exercices, il y a deux types de visuels, et ils ne se produisent pas pareil :

- **Captures de résultat (output d'un skill)** : un tableau de quick wins, un brief, un rapport d'audit. Je les génère moi-même en montrant l'output réel exemple. Pas besoin de vraie capture, c'est reproductible et ça se met à jour sans re-photographier.
- **Captures d'interface (Obsidian, Claude Code en action, GSC)** : là il faut une vraie capture d'écran. Je ne peux pas la prendre. Deux options : soit on simule la session en bloc de code (comme la fiche Cowork), soit tu prends les captures une fois (réutilisables sur tous les exercices).

Ma reco : par défaut, **zéro vraie capture** (sessions simulées en bloc de code + outputs exemples), exactement comme la fiche Cowork qui marche très bien sans. On ajoute de vraies captures seulement là où l'interface est incontournable (ex : où cliquer dans GSC). À toi de confirmer.

## 3. Le cas fil rouge (décision clé)

Pour que tous les participants travaillent sur la même base et puissent comparer leur résultat au corrigé, il faut un seul cas partagé : un site exemple avec son export GSC, son sitemap, quelques verbatims. Options :
- Réutiliser/enrichir le `dataset-5-etapes.html` déjà dans le dashboard.
- Créer un cas anonymisé dédié (un SaaS fictif crédible) avec data réaliste.

Sans cas fil rouge, chaque participant part de son propre client et il n'y a pas de corrigé comparable. À cadrer.

## 4. Inventaire des exercices

### 4 exercices « workflow » (capstones de session, 30-45 min)

| # | Workflow | Ce que le participant produit |
|---|---|---|
| W1 | Du mot-clé au vecteur (S1) | Le Google Sheet 5 critères scoré, à partir de la thématique du cas |
| W2 | Rédiger une page incarnée (S2) | Un article avec arrêt à 50% + relecture + fact-check, scoré OpenDecoder |
| W3 | Auditer un site (S3) | Le rapport client en 3 horizons (8 phases sur le cas) |
| W4 | Installer le système (S4) | Roadmap 90j + todo automatique + revue de presse branchée |

### Micro-exercices par skill (10-15 min chacun)

| Session | Skill | Exercice (ce qu'on teste) | Cowork ? |
|---|---|---|---|
| S1 | seo-recherche-mots-cles | thématique → 50 mots-clés qualifiés | ✅ |
| S1 | seo-clustering-mots-cles | liste brute → clusters (1 = 1 page) | ✅ |
| S1 | seo-mots-cles-decisionnels | isoler les requêtes qui convertissent | ✅ |
| S1 | seo-cluster-aeo | pilier → 15 spokes | ✅ |
| S1 | seo-entites-vectorielles | requête → entités + gap | ✅ |
| S1 | seo-modeles-pseo | Money Page → spokes priorisés | ✅ |
| S1 | seo-peurs-objections | persona → pain points + verbatims | ✅ |
| S1 | seo-product-led-seo | thématique → idée d'outil interactif | ✅ |
| S2 | seo-brief-contenu | requête → brief Hn | ✅ |
| S2 | article-engine-pipeline | brief → article (arrêt 50%) | ✅ |
| S2 | seo-programmatique-pseo | data → 5 modèles scalables + gates | ✅ |
| S2 | seo-preparation-semantique | requête + verbatims → matière brief | ✅ |
| S2 | ton-de-voix (perso) | réécrire un paragraphe à sa voix | ✅ |
| S3 | indexation-check | sitemap → statut d'indexation | terminal/Cowork |
| S3 | seo-quick-win | export GSC → top quick wins | ✅ |
| S3 | seo-cannibalisation | export GSC → pages en conflit | ✅ |
| S3 | maillage-systeme | liste d'URLs → plan de maillage | ✅ |
| S3 | maillage-interne-gsc | GSC → hiérarchie mère/fille | ✅ |
| S3 | seo-core-web-vitals | sitemap → audit Lighthouse | terminal |
| S3 | seo-donnees-structurees | page → JSON-LD | ✅ principes |
| S4 | seo-roadmap-pseo | Money Page → roadmap 90j | ✅ |
| S4 | todo | transcripts → todo datée | terminal |
| S4 | revue-presse-quotidienne | thématique → brief sourcé | via Action |

Note : `audit-engine-pipeline` et `article-engine-pipeline` sont les orchestrateurs, donc couverts par les capstones W3 et W2. Les exercices terminal-only (core-web-vitals, todo) sont marqués pour ne pas piéger les participants Cowork.

## 5. Où ça vit

- **Source markdown** : un fichier par exercice dans `seo-kb/raw/bootcamp4/exercices/` (versionné, éditable, c'est la vérité).
- **Rendu dashboard** : page HTML par session dans le dashboard (`exercices-s1.html`...), ou un onglet « Exercices » dans `index.html`, au design Organikk. Les outputs exemples s'affichent en bloc, les captures éventuelles en image.
- **Kit participant** : ajouter le cas fil rouge (data) dans le `seo-kit-starter.zip`.

## 6. Plan de build (phasé)

1. **Pilote (2 exercices, à valider d'abord)** : 1 capstone (W3 audit, le plus visuel) + 1 micro-skill (seo-quick-win, output très parlant). On fige le gabarit et le rendu sur ces deux-là.
2. **Cas fil rouge** : créer/figer le jeu de données partagé.
3. **Batch S1** puis **S2**, **S3**, **S4** : les micro-exercices par session.
4. **Capstones** W1, W2, W4.
5. **Intégration dashboard** + mise à jour du zip.

## 7. Décisions à trancher avant de lancer

1. **Screens** : sessions simulées en bloc de code (reco) ou vraies captures que tu fournis ?
2. **Cas fil rouge** : enrichir `dataset-5-etapes` ou créer un SaaS fictif dédié ?
3. **Granularité** : un exercice par skill (23) + 4 capstones, ou seulement les 4 capstones + quelques skills clés ?
4. **Rendu** : pages HTML dans le dashboard, ou d'abord les markdown sources (plus rapide à produire et relire) ?
5. **Go pilote** : je produis les 2 exercices pilotes pour valider le format ?
