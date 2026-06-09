# Loop Kit - rendre n'importe quel skill auto-apprenant

Kit reutilisable qui generalise le pattern SyntheticBrain (`../agent-synthetic/`) et content-brain
(`../content-brain/`) a tout le systeme. Objectif : que chaque workflow important tourne en boucle
fermee **briefing -> production -> apprentissage**, avec une memoire qui fait foi et un gate de validation.

## Les 3 couches (strictes)
- `ledgers/` : faits observes, append-only (runs, claims, predictions, mistakes, said_index). On n'efface jamais.
- `memory/` : interpretations durables (directives, score-grid, wording_rules, questions). Ne se durcissent qu'a la revue humaine.
- `derived/` : vues calculees, regenerables (eval_health, dashboard). Jamais ecrites a la main.

## Adopter la boucle sur un skill (bootstrap)
1. Creer le brain : `cp -r _loop-kit/_template loops/<nom>` (ou `content-brain/<projet>` pour la prod contenu).
2. Remplacer `__LOOP_NAME__` et `__CADENCE__` dans `manifest.yml` et les `memory/*.md`.
3. Coller le bloc de `PHASE-APPRENTISSAGE.md` a la fin du SKILL.md concerne, avec `<BRAIN>` = chemin du brain.
4. Renseigner le perimetre et la source de verite dans `memory/directives.md`.
5. (Optionnel) Creer une routine planifiee qui appelle le skill a la cadence voulue.

## Validation et sante
- `./validate.sh <brain>` : gate avant commit (JSONL parse + `capture_mode` sur runs/claims).
- `./eval_health.py <brain>` : statut OK / WATCH / ESCALATE (predictions en retard, claims non verifies).

## Regle d'or
**Autonome sur la data, supervise sur le code.** La boucle ecrit librement ses ledgers et derived.
Tout changement de skill passe par `memory/questions.md` et l'aval de Tim. Jamais d'auto-edition de code.

## Deja boucles (ne pas refaire)
- `agent-synthetic/` (Algorithme), `content-brain/` (prod contenu), `gsc-watcher` + `preuves-feedback` (resolution GSC), `hypotheses-validation`.

## A boucler (Chantier 1)
- `indexation-check`, `maillage-interne-gsc`, `seo-cannibalisation`, `seo-quick-win`, `linkedin-journal`.
