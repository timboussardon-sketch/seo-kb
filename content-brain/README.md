# content-brain — labo d'apprentissage de la production de contenu

Même mécanique que SyntheticBrain (`../agent-synthetic/`), appliquée à la **production SEO/contenu** au lieu de la newsletter. Un **brain par projet/client** : `content-brain/<project>/`.

Le skill `/content-brain` (dans `~/.claude/skills/content-brain/`) enveloppe `article-engine-pipeline`. Il lit la mémoire du projet au début, produit le contenu, fact-checke au niveau du claim, passe le gate de publication, puis écrit les ledgers et apprend. Le contenu qu'il produit applique la doctrine de bout en bout, celle posée dans [[syntheses/workflow-complet-consultant-seo-ia]].

## 3 couches (strictes)
- `ledgers/` : faits observés, append-only (claims, predictions, mistakes, said_index, runs).
- `memory/` : interprétations durables ([[directives]], [[score-grid]], [[wording_rules]], [[questions]]) qui ne se durcissent qu'après revue humaine.
- `derived/` : vues calculées ([[dashboard]]).

## Bootstrap d'un projet
Copier `_template/` vers `content-brain/<project>/`, remplacer `__PROJECT__` dans manifest/memory.

## Boucle de preuve
Chaque contenu logge ses `claims` (data réelle), une `prediction` datée (resolve_by J+30/J+90) et un `score`. Les pulls GSC (`gsc-watcher`, `preuves-feedback`) résolvent les prédictions. Au bout de quelques mois, la prod devient la meilleure source de doctrine, montrable à un prospect.

## Validation
`./validate.sh <project>` avant tout commit (JSONL + capture_mode). Autonome sur la data, jamais sur le code : le brain propose un diff de skill dans `memory/questions.md`, Tim valide.
