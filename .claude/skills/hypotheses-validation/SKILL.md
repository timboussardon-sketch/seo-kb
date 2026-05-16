---
name: hypotheses-validation
description: |
  Revue mensuelle du registre des hypothèses et des contradictions. Confronte chaque hypothèse non validée aux sources ingérées depuis la dernière revue, fait avancer les statuts (ouvert → en-test → validé/invalidé), répercute sur le confidence des pages doctrine, ferme les contradictions tranchées.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "validation hypothèses", "revue mensuelle doctrine", "quelles hypothèses ont avancé", "fais le point sur la doctrine", "revue contradictions", ou quand le LaunchAgent com.timboussardon.hypotheses-validation se déclenche.
---

# Hypotheses Validation — revue mensuelle de la doctrine

Vault : `/Users/timothee/Code/seo-kb/`. Tu mets à jour `wiki/hypotheses.md`, `wiki/contradictions.md`, et les pages doctrine impactées.

## OBJECTIF

Empêcher la doctrine de rester un corpus de convictions. Chaque mois, on force le passage : une hypothèse a-t-elle reçu une preuve, dans un sens ou l'autre ? Une contradiction s'est-elle tranchée ? C'est ce qui transforme [[concepts/data-proprietaire]] en moat opposable.

## ÉTAPE 1 — PÉRIMÈTRE TEMPOREL

```bash
cd /Users/timothee/Code/seo-kb
grep "^## \[" wiki/log.md | tail -40
git log --since="35 days ago" --diff-filter=A --name-only --pretty=format: | grep '^wiki/sources/' | sort -u
```

Identifie les sources ingérées et les [[preuves/index|fiches preuve]] créées ou mises à jour depuis ~35 jours.

## ÉTAPE 2 — CONFRONTER CHAQUE HYPOTHÈSE

Lis `wiki/hypotheses.md`. Pour chaque H-XXX `ouvert` ou `en-test` :

- Une fiche `wiki/preuves/*.md` la concerne-t-elle ? Quel verdict ?
- Une source ingérée ce mois apporte-t-elle un benchmark, une donnée terrain, un test qui pèse pour ou contre ?
- Statut à faire évoluer ? `ouvert` → `en-test` (test lancé) → `validé` / `invalidé` (preuve à l'appui) ; ou `heuristique` si non prouvable mais cohérent et explicitement assumé.

Règle dure : pas de fiche preuve exploitable = pas de passage à `validé`/`invalidé`. On ne valide jamais sur du ressenti.

## ÉTAPE 3 — RÉPERCUTER SUR LA DOCTRINE

Pour toute hypothèse qui change de statut, va sur les pages doctrine listées dans sa ligne :

- `validé` : retirer les mentions "non validé", ajuster `confidence:` vers le haut, dater l'`updated:`
- `invalidé` : corriger le wording, baisser `confidence:`, et ouvrir une entrée dans `wiki/contradictions.md` pour tracer la dette doctrinale à nettoyer
- Mettre à jour le tableau de bord en tête de `wiki/hypotheses.md`

## ÉTAPE 4 — REVUE DES CONTRADICTIONS

Lis `wiki/contradictions.md`. Pour chaque ligne `ouverte` / `en-cours` :

- Un ingest ou une clarification l'a-t-il fermée ? → `résolue` + lien vers la page/source qui la ferme
- Sans mouvement depuis > 60 jours → la marquer pour décision en [[revue-hebdo/index|revue hebdo]] (fermer, déléguer à un ingest, ou `acceptée`)
- Ne jamais supprimer une ligne résolue : trace d'audit

## ÉTAPE 5 — LOG + RÉSUMÉ

Append dans `wiki/log.md` :

```
## [YYYY-MM-DD] hypothese | revue mensuelle — X hypothèses bougées, Y contradictions fermées
- H-XXX: ouvert → en-test (preuve: [[preuves/...]])
- C-XXX: ouverte → résolue
- doctrine corrigée: [[concepts/...]] (confidence ajusté)
```

Termine par : `Doctrine [date] : X hypothèses bougées (validé:a invalidé:b en-test:c) / Y contradictions fermées`

## CONTRAINTES

- Pas d'invention de preuve. Une hypothèse sans donnée reste `ouvert`, même si elle "semble vraie".
- Toute correction de page doctrine doit être tracée (log + `updated:`). On ne réécrit pas l'histoire en silence.
- Si une hypothèse `invalidé` casse une synthèse, le signaler explicitement dans le résumé, ne pas masquer.
- Respecter l'anti-AI-writing §11 sur tout texte ajouté aux pages.
