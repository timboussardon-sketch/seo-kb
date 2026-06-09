---
name: gsc-watcher
description: |
  Traite tout export Search Console déposé dans raw/data/exports-gsc/ (gsc-*.csv), qu'il vienne d'un export manuel ou du fetch API automatique, et met à jour les fiches preuves correspondantes (baseline / jalon J+30 / J+90). Source-agnostique : un seul chemin de traitement, deux alimentations possibles. Nourrit la boucle sortie → apprentissage.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "traite la GSC", "j'ai déposé un export GSC", "mets à jour les preuves avec la GSC", "watcher GSC", "boucle preuves GSC", ou quand le LaunchAgent com.timboussardon.gsc-pull se déclenche.
---

# GSC Watcher — alimenter la boucle preuves depuis la Search Console

Vault : `/Users/timothee/Code/seo-kb/`. Tu lis `raw/data/exports-gsc/*.csv` (capture, lecture seule) et tu écris dans `wiki/preuves/`.

## OBJECTIF

La GSC est la seule source de vérité (jamais Semrush/Ahrefs, jamais d'estimation, règle §5.4). Ce skill prend ce qui est dans `raw/data/exports-gsc/` et le déverse dans les fiches preuves, sans se soucier de savoir si le CSV vient d'un export manuel de Tim ou du `gsc-fetch.py` automatique. Format de nommage attendu : `gsc-requetes-pages-YYYY-MM-DD.csv`, `gsc-pages-YYYY-MM-DD.csv`, `gsc-requetes-YYYY-MM-DD.csv`, `gsc-auto-YYYY-MM-DD.csv`.

## ÉTAPE 1 — INVENTAIRE DES EXPORTS

```bash
cd /Users/timothee/Code/seo-kb
ls -t raw/data/exports-gsc/gsc-*.csv 2>/dev/null | head -10
```

Repère les exports non encore reflétés dans les fiches (compare la date de l'export à la dernière mesure consignée dans chaque fiche). Si aucun export, dis-le et arrête-toi proprement (pas d'invention).

## ÉTAPE 2 — CHARGER LES FICHES EN ATTENTE

```bash
grep -l "status: en-cours" wiki/preuves/*.md 2>/dev/null | grep -v _template
```

Pour chaque fiche `en-cours`, lis le frontmatter : `contenu` (URL ou source), `publie_le`, `jalon_30j`, `jalon_90j`, `hypothese`. Détermine quel jalon est dû (date du jour ≥ jalon et case non remplie).

## ÉTAPE 3 — APPARIER URL ↔ LIGNES GSC

Parse le CSV (colonnes typiques : `page`, `query`, `clicks`, `impressions`, `ctr`, `position`). Pour chaque fiche, retrouve les lignes dont la `page` correspond à l'URL du contenu (match exact d'URL, sinon chemin). Agrège : position moyenne et impressions/clics sur les requêtes cibles déclarées dans la fiche, sinon top requêtes de la page.

Si aucune ligne ne matche une URL attendue : ne pas inventer, marquer la fiche `bruitée` avec la raison ("URL absente de l'export, page peut-être non encore indexée ou trafic nul").

## ÉTAPE 4 — REMPLIR LE JALON

Remplis le tableau du jalon dû (J+30 ou J+90) avec les valeurs réelles et le Δ vs baseline. Si la baseline est vide et que c'est le premier export après publication, remplis la baseline. Date de mesure = date de l'export GSC, pas date du jour.

Quand un jalon final (J+90) est rempli : pose le verdict (`concluante` / `non-concluante` / `bruitée`) en deux phrases ancrées sur les chiffres (§11, zéro storytelling), passe `status:` en conséquence.

## ÉTAPE 5 — RÉPERCUTER SUR LA DOCTRINE

- Mets à jour la table "Fiches" de `wiki/preuves/index.md`
- Si verdict posé : mets à jour la ligne de l'hypothèse dans `wiki/hypotheses.md` (statut + lien fiche) et le tableau de bord
- Si `non-concluante` : ouvre une entrée dans `wiki/contradictions.md`
- Append `wiki/log.md` : `## [YYYY-MM-DD] preuve | gsc-watcher — N fiches mises à jour, M verdicts`

Termine par : `GSC watcher [date] : N fiches mises à jour (baseline:a J+30:b J+90:c) — M verdicts — hypothèses touchées : …`

## ÉTAPE 6 — RÉSOUDRE LES PRÉDICTIONS DES BRAINS (content-brain + loops)

En plus des fiches preuves, ce skill résout les prédictions datées des brains qui ont la GSC comme source de vérité.

Cibles : `content-brain/*/ledgers/predictions.jsonl` et `loops/*/ledgers/predictions.jsonl` (seulement les boucles dont `memory/directives.md` déclare la GSC en source).

Pour chaque prédiction `status:"open"` dont `resolve_by` ≤ date de l'export :
1. Apparier `target_query` et/ou `page` aux lignes de l'export (même logique qu'ÉTAPE 3).
2. Calculer la valeur réelle (position moyenne, clics, impressions, CTR) sur la fenêtre de l'export.
3. Comparer au `claim` falsifiable et à `baseline`, poser un `verdict` :
   - `hit` : claim vérifié.  `partial` : amélioration réelle mais sous le seuil.  `miss` : pas d'amélioration ou régression.  `no_data` : URL/requête absente de l'export (page non indexée ou trafic nul), ne jamais inventer.
4. Mettre la prédiction à jour EN PLACE (seule mutation autorisée du ledger) : `status:"resolved"` + `measured:{...}` + `verdict` + `resolved_at` (= date de l'export).
5. Si `miss` ou `partial` : append une ligne dans `mistakes.jsonl` du même brain (ce qui a sous-performé + hypothèse à revoir).
6. Régénérer la santé : `../_loop-kit/eval_health.py <brain>` puis gate `../_loop-kit/validate.sh <brain>`.
7. Si un verdict remet en cause une directive : NE PAS éditer le skill, écrire le diff proposé dans `<brain>/memory/questions.md` (règle d'or : autonome sur la data, supervisé sur le code).

Idempotent : une prédiction déjà `resolved` est ignorée ; `no_data` reste `open` (re-tentée au prochain export) mais loggée.

Termine aussi par : `GSC watcher predictions [date] : K brains, R résolues (hit:a partial:b miss:c no_data:d)`

## CONTRAINTES

- Lecture seule sur `raw/data/exports-gsc/`. Jamais réécrire un export.
- Zéro chiffre inventé. Pas de ligne GSC pour une URL = `bruitée` argumentée, jamais une estimation.
- Une fiche ne passe `concluante`/`non-concluante` que si sa prédiction était falsifiable AVANT la mesure (voir le template). Sinon `bruitée` + reformuler la prédiction.
- Idempotent : relancer le skill sur le même export ne doit pas dupliquer les mesures (vérifier la date de mesure déjà consignée).
- Anti-AI-writing §11 sur tout texte ajouté.
