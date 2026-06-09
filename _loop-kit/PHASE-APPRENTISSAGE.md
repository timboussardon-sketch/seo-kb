# Bloc "Phase apprentissage" - a coller en fin de skill

Colle cette section a la fin de n'importe quel skill pour le transformer en boucle qui apprend.
Remplace `<BRAIN>` par le chemin du brain (ex : `content-brain/golfiller`, `loops/indexation-organikk`).

---

## Phase apprentissage (boucle)

Cette phase tourne APRES la production. Elle ne change jamais le code du skill toute seule.

1. **Briefing memoire** (debut de run, AVANT de produire) : lire `<BRAIN>/manifest.yml` puis
   `<BRAIN>/memory/` (directives, score-grid, wording_rules, questions) et `<BRAIN>/ledgers/said_index.jsonl`
   pour ne pas repeter un angle deja couvert.

2. **Production** : faire le travail du skill normalement, en appliquant directives + score-grid.

3. **Ledger date** (append-only, jamais reecrire) dans `<BRAIN>/ledgers/` :
   - `runs.jsonl` : 1 ligne {date, ce qui a ete produit, `capture_mode`: "native"}.
   - `claims.jsonl` : 1 ligne par fait/chiffre, avec sources (>=2 dont 1 primaire) et `capture_mode`.
   - `predictions.jsonl` : si le run produit du mesurable, 1 pari date {id, enonce, `resolve_by`: AAAA-MM-JJ (J+30 ou J+90)}.
   - `said_index.jsonl` : angles/sujets couverts ce run.
   - `mistakes.jsonl` : ce qui a sous-performe (rempli a la resolution, pas a la prod).

4. **Gate** : lancer `../_loop-kit/validate.sh <BRAIN>` (ou `./validate.sh`). Si echec : corriger, ne pas commit.
   Optionnel : `../_loop-kit/eval_health.py <BRAIN>` pour le signal OK / WATCH / ESCALATE.

5. **Propositions de code** : si la boucle "voudrait" changer le skill (nouvelle regle, seuil, formulation),
   elle NE le fait pas. Elle ecrit le diff propose + la raison dans `<BRAIN>/memory/questions.md`. Tim tranche a la revue.

Regle d'or : **autonome sur la data, supervise sur le code.**
