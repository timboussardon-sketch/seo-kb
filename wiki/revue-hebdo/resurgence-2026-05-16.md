---
type: register
title: Résurgence — data-proprietaire — 2026-05-16
aliases: [resurgence-2026-05-16]
tags: [meta, rituel, resurgence, decision]
created: 2026-05-16
updated: 2026-05-16
sources: 0
confidence: high
status: stable
---

# Résurgence — [[concepts/data-proprietaire]] — 2026-05-16

> Première édition de la résurgence espacée. Concept remonté pour la [[revue-hebdo/index|revue hebdo]] du vendredi.

## Pourquoi celui-là

- **Le hub le plus lourd du vault** : 98 backlinks (vs 64 pour [[concepts/grounding-score]], 25 pour [[concepts/persistent-wiki-vs-rag]]). Le skill pondère explicitement vers lui — c'est le plus coûteux à laisser dériver.
- `status: stable`, `confidence: high`, `updated: 2026-04-13` → apparaît comme le concept stable le plus ancien de la strate hub (33 j sans mise à jour affichée).
- Jamais ressorti en résurgence (aucune note `resurgence-*.md` antérieure : c'est la première).

## État vs aujourd'hui

**Le corps est à jour. La métadonnée a dérivé.**

1. **Drift silencieux confirmé sur le frontmatter.** `updated: 2026-04-13` est faux. `wiki/log.md:326` (batch `[2026-05-01] batch-ingest T4+T5+T6`) enregistre noir sur blanc : *« [[concepts/data-proprietaire]] — sources 19→25 »*. Le log montre une progression continue après le 13/04 : 8→9 → 14 → 19 → **25 sources**, dernier ajout daté **2026-05-01**. Le corps et le bloc *Pages liées* ont absorbé toutes les sources jusqu'au 2026-04-30 (posts-linkedin-batch, fg-formation B2B inversé, 4 modèles pSEO APIs, cluster Organikk, process B2B, scoring). Seul le champ `updated:` n'a jamais été bougé — **18 jours de retard**.
   - Conséquence systémique : ce hub à 98 backlinks fausse *tous* les signaux de fraîcheur qui le lisent — sélection de la résurgence, `audit-vault-hygiene`, règle revue-hebdo « stale si SEO volatil > 12 mois ». Un hub vivant déguisé en concept dormant.
   - `sources: 25` en frontmatter est, lui, **cohérent** (25 liens `[[sources/...]]` uniques comptés). Rien à corriger côté compte.
2. **Substance : rien ne le contredit, rien à intégrer.** Aucune source post-2026-05-01 dans `wiki/sources/` (zéro fichier `2026-05-*`). Le dernier batch (2026-05-01) est déjà digéré. Le moat « data propriétaire = avantage structurel non copiable » reste aligné avec tout l'ingéré récent (Retrieval Collapse NAVER, core update fermes IA −40/−80 %, densité de preuves > domain authority).
3. **Tension connue, hors périmètre résurgence.** [[hypotheses]] H-007 (« la data propriétaire réduit le Retrieval Collapse et augmente l'exposition réelle ») est toujours `ouvert`, sans fiche preuve. La doctrine est posée en `confidence: high` alors que son hypothèse falsifiable centrale n'est pas prouvée. Ce n'est pas un drift à trancher ici — c'est un item pour `hypotheses-validation`. Noté pour mémoire, pas coché.
4. **Wording.** Note dense, voix Tim assumée (« Si je crée le même site que vous demain, sans expertise, je serai toujours derrière »), tables + puces, registre concret. Aucune violation anti-AI-writing. Rien à corriger.

## Verdict proposé pour la revue hebdo

- [ ] Toujours juste, rien à faire
- [x] À mettre à jour : **frontmatter uniquement** — `updated: 2026-04-13` → `updated: 2026-05-01` (date réelle du dernier ajout de contenu, `wiki/log.md:326`). Le corps et `sources: 25` sont justes. Correction d'1 ligne, à exécuter post-revue. Ne pas toucher au contenu.
- [ ] À challenger : —
- [ ] Wording à corriger : —

> Note pour la revue : le vrai enjeu n'est pas ce concept (substantiellement sain) mais le **pattern** — si le plus gros hub a un `updated:` qui ment de 18 j, combien d'autres concepts maintenus via batch-ingest ont un frontmatter figé ? Candidat à un point « hygiène frontmatter » dans `audit-vault-hygiene`.

Pages liées : [[revue-hebdo/index]] · [[concepts/data-proprietaire]] · [[hypotheses]] · [[log]]
