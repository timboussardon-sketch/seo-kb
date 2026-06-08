---
name: ingest-backlog-sweep
description: |
  Sweep hebdomadaire du backlog d'ingest. Diffe raw/ contre wiki/sources/, classe le raw non traité en P1/P2/P3, met à jour wiki/ingest-backlog.md, propose le prochain lot à ingérer. Ne touche pas raw/. Respecte les skips documentés.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "sweep backlog", "quoi ingérer", "raw non traité", "backlog d'ingest", "qu'est-ce qui reste à digérer", ou quand le LaunchAgent com.timboussardon.ingest-backlog se déclenche.
---

# Ingest Backlog Sweep — radar hebdo sur le raw non digéré

Vault : `/Users/timothee/Code/seo-kb/`. Tu mets à jour `wiki/ingest-backlog.md`. Lecture seule sur `raw/` (règle d'or §3 AGENTS.md).

## OBJECTIF

Rendre visible le trou capture→traitement. Pas d'ingest automatique : tu produis le registre trié et tu proposes le prochain lot. C'est Tim (ou un ingest explicite §6.1) qui décide.

## ÉTAPE 1 — INVENTAIRE RAW

```bash
cd /Users/timothee/Code/seo-kb
find raw -name "*.md" \
  -not -path "*/journal/*" \
  -not -path "*/revue-de-presse/*" \
  -not -path "*/_archive/*" \
  -not -path "*/archive/*" \
  | sort > /tmp/raw-files.txt
wc -l /tmp/raw-files.txt
```

## ÉTAPE 2 — CE QUI EST DÉJÀ TRAITÉ

Pour chaque fichier raw, cherche un `wiki/sources/*.md` correspondant : slug commun, ou cité dans le frontmatter/corps d'une source, ou couvert par une source agrégée documentée dans `wiki/log.md` (les batch-ingest listent les fichiers absorbés). Lis la section "Skips documentés" de `wiki/ingest-backlog.md` et la zone ~lignes 385-393 / ~467 de `wiki/log.md` : ces fichiers sont exclus définitivement, ne les reclasse pas.

```bash
ls wiki/sources/*.md | sed 's#.*/##; s#\.md$##' > /tmp/wiki-source-slugs.txt
grep -oE 'raw/[^ )`]+\.md' wiki/log.md | sort -u > /tmp/raw-cited-in-log.txt
```

## ÉTAPE 3 — CLASSER LE BACKLOG

Le reste = backlog. Classe en trois tiers, oldest-first dans chaque tier (`stat -f '%Sm' -t %Y-%m-%d <file>`) :

- **P1 — données terrain propriétaires** : bootcamp live, transcripts calls non ingérés, modèles de production, cas clients, acquisition. Le moat qui fuit.
- **P2 — contenu publié non bouclé** : articles Organikk hors scrape, newsletters publiées, brouillons devenus contenu. Chacun appelle aussi une [[preuves/index|fiche preuve]].
- **P3 — reste** : auteurs externes, notes process, worksheets, doublons potentiels à vérifier.

Ne jamais reclasser un skip documenté sans une instruction explicite de Tim.

## ÉTAPE 4 — METTRE À JOUR LE REGISTRE

Réécris les sections P1/P2/P3 de `wiki/ingest-backlog.md` (garde la méthodo, l'intro et la section "Skips documentés" intactes sauf nouveau skip validé par Tim). Mets `updated:` à la date du jour. Compte par tier.

## ÉTAPE 5 — PROPOSER LE PROCHAIN LOT

Recommande 1 à 3 fichiers P1 (à défaut P2) à ingérer la semaine prochaine, avec en une phrase l'angle SEO ou la valeur terrain attendue. Cette reco est reprise telle quelle par le skill `revue-hebdo` le vendredi.

## ÉTAPE 6 — LOG + RÉSUMÉ

Append dans `wiki/log.md` :

```
## [YYYY-MM-DD] backlog | sweep — N en backlog (P1:x P2:y P3:z)
- prochain lot proposé: fichier1, fichier2
- nouveaux skips: aucun / liste
```

Termine par une ligne : `Backlog [date] : N total (P1:x P2:y P3:z) — prochain lot : …`

## CONTRAINTES

- Lecture seule sur `raw/`. Aucune création de source ici : ce skill cartographie, il n'ingère pas.
- Pas d'invention : si un fichier est ambigu (traité ou pas), le mettre en P3 avec la mention "à vérifier", jamais l'inventer comme traité.
- Si le backlog dépasse 80 fichiers, lister les 15 premiers par tier et agréger le reste en "+N autres".
- Respecter strictement les skips documentés. Un nouveau skip ne s'ajoute que sur décision explicite de Tim, et se note dans la section dédiée du registre.
