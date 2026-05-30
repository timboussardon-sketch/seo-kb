# Revue hebdo SyntheticBrain (vue dérivée)

Synthèse calculée par l'agent 9 à partir des ledgers, présentée à Tim à la revue du vendredi. Vue dérivée, pas une source de vérité : tout vient des `ledgers/`.

## Semaine en cours (au 2026-05-30)

Quatre éditions le 2026-05-30 (run d'amorçage v2, cloud, v3, v4). Sujets couverts, tous dans le périmètre search/IA :
- v2 : Information Agents (agents qui lisent), AI Mode > 1 Md MAU, Gemini 3.5 Flash, core update du 21 mai, Expert Advice AIO.
- v3 : commerce agentique (Universal Cart / UCP, agents qui achètent), fin du core update, crawl-to-refer Cloudflare, conversion trafic IA vs volume.
- v4 : llms.txt non utilisé par la recherche IA de Google (lien doctrine SAGEO + AEO), parts Gemini vs ChatGPT, redesign du champ de recherche I/O, CTR AIO en hausse pour les pages citées (Seer).

Note qualité moyenne de la semaine : ~4,4/5. Point d'attention : un overlap thématique partiel entre v4 et le run cloud (llms.txt / guide du 15 mai), tracé en mistake M-004.

## Prédictions ouvertes à suivre

- P-2026-05-30-1 : Expert Advice augmente la part de citations de première main (échéance 2026-07-15).
- P-2026-05-30-2 : une vente via checkout agentique UCP rapportée avant 2026-09-30.
- P-2026-05-30-3 : Googlebot sous 27 % du crawl IA d'ici fin 2026.
- P-2026-05-30-4 : Google maintient « llms.txt non utilisé » d'ici fin 2026.

## À trancher par Tim (issu de `memory/questions.md`)

- Rubrique fixe « ce qu'un agent retiendrait » ?
- Format de l'édition de l'après-midi (court vs complet) ? Cadence de versionnage (3 à 4 éditions le 30 mai) ?
- Sources `explore` à confirmer ou retirer : `lumar` (0.62), `cloudflare-radar` (0.85), `similarweb-geo`, `seer-interactive`, et nouvelles du run v4 `theseocommunity` (0.6), `getpassionfruit` (0.6).
- Sources tech généralistes (Tom's Guide, VentureBeat, TechRadar) : corroboration ponctuelle hors registre, ou intégration ?

## Propositions doctrine (issu de `memory/questions.md`)

- Confirmer le concept `agentic-search` côté « agent qui achète » (UCP, v3).
- Ajouter à `structural-information-geo`/`aeo` la convergence avec la position Google sur llms.txt (v4).

## Diffs de skill proposés

Aucun appliqué. Piste récurrente : garde-fou « vérifier la date de la source primaire » dans le socle `revue-presse-quotidienne` (piège fraîcheur revenu en v3 et géré en v4). À formaliser en diff si ça revient une 3e fois.

## Erreurs récurrentes repérées (issu de `ledgers/mistakes.jsonl`)

- M-001 : mémoire qui mélangeait faits et interprétations. Corrigé par la restructuration ledgers/memory/derived.
- M-002 : ligne JSONL malformée (run cloud). Corrigé, `validate.sh` obligatoire avant commit.
- M-003 : fichier édition écrasé par une redirection d'erreur git. Corrigé, plus de `2>&1` vers un fichier de donnée.
- M-004 : redite partielle de l'info du jour (v4 vs run cloud). Fix : scanner `runs.jsonl` (sujet_info_jour) avant de figer le sujet, pas seulement `said_index.jsonl`.
