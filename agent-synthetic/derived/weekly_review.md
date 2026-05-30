# Revue hebdo SyntheticBrain (vue dérivée)

Synthèse calculée par l'agent 9 à partir des ledgers, présentée à Tim à la revue du vendredi. Vue dérivée, pas une source de vérité : tout vient des `ledgers/`.

## Semaine en cours (au 2026-05-30)

Cinq éditions le 2026-05-30 (run d'amorçage v2, cloud, v3, v4, v5). Sujets couverts, tous dans le périmètre search/IA :
- v2 : Information Agents (agents qui lisent), AI Mode > 1 Md MAU, Gemini 3.5 Flash, core update du 21 mai, Expert Advice AIO.
- v3 : commerce agentique (Universal Cart / UCP, agents qui achètent), fin du core update, crawl-to-refer Cloudflare, conversion trafic IA vs volume.
- v4 : llms.txt non utilisé par la recherche IA de Google (lien doctrine SAGEO + AEO), parts Gemini vs ChatGPT, redesign du champ de recherche I/O, CTR AIO en hausse pour les pages citées (Seer).
- v5 : formats publicitaires payants dans AI Mode / AI Overviews (Google Marketing Live 20 mai, étiquetés Sponsored), publicités OpenAI dans ChatGPT, divergence de citations ChatGPT/Perplexity (Averi 680M, 11 %), Ahrefs 38 % des citations AIO dans le top-10 organique, dépréciation des résultats enrichis FAQ (7 mai 2026).

Note qualité moyenne de la semaine : ~4,4/5. Point d'attention : cinq éditions le même jour (cadence prévue 2/jour), à arbitrer ; un overlap thématique partiel entre v4 et le run cloud (llms.txt / guide du 15 mai), tracé en mistake M-004.

## Prédictions ouvertes à suivre

- P-2026-05-30-1 : Expert Advice augmente la part de citations de première main (échéance 2026-07-15).
- P-2026-05-30-2 : une vente via checkout agentique UCP rapportée avant 2026-09-30.
- P-2026-05-30-3 : Googlebot sous 27 % du crawl IA d'ici fin 2026.
- P-2026-05-30-4 : Google maintient « llms.txt non utilisé » d'ici fin 2026.
- P-2026-05-30-5 : un format pub AI Mode (Conversational Discovery Ads / Highlighted Answers) sorti du stade annonce et accessible aux annonceurs US d'ici fin 2026.
- P-2026-05-30-6 : recouvrement de domaines cités ChatGPT/Perplexity confirmé < 25 % par une nouvelle mesure d'ici fin 2026.

## À trancher par Tim (issu de `memory/questions.md`)

- Cadence et versionnage : 5 éditions le 30 mai (prévu 2/jour). Une édition fait-elle référence pour la journée ? Format de l'édition de l'après-midi (court vs complet) ?
- Rubrique fixe « ce qu'un agent retiendrait » ?
- Règle à valider : une doc primaire officielle de l'éditeur (ex. Google Search Central sur la dépréciation FAQ) dispense-t-elle du recoupement à 2 sources indépendantes ?
- Seuil mono-étude : le chiffre 11 % (Averi) publié comme mono-étude flaguée avec direction recoupée, ou à écarter du corps faute de 2e source chiffrée ?
- Sources `explore` à confirmer ou retirer : `lumar` (0.62), `cloudflare-radar` (0.85), `similarweb-geo` (0.78), `seer-interactive` (0.75), `theseocommunity` (0.6), `getpassionfruit` (0.6), et nouvelles du run v5 `ahrefs` (0.8, candidate exploit), `averi` (0.62), `tryprofound` (0.6).
- Sources tech généralistes (Tom's Guide, VentureBeat, TechRadar, BleepingComputer, PPC.land) : corroboration ponctuelle hors registre, ou intégration ?

## Propositions doctrine (issu de `memory/questions.md`)

- Confirmer le concept `agentic-search` côté « agent qui achète » (UCP, v3) et « agent qui transige dans la réponse via paiement natif » (formats pub AI Mode, v5).
- Ajouter à `structural-information-geo`/`aeo` la convergence avec la position Google sur llms.txt (v4).
- Signal pour `aeo` (v5) : la réponse générative de Google contient désormais deux voies distinctes, citation organique et emplacement payé étiqueté Sponsored. La doctrine AEO ne couvre que la première ; préciser la frontière.

## Diffs de skill proposés

Aucun appliqué. Piste récurrente : garde-fou « vérifier la date de la source primaire » dans le socle `revue-presse-quotidienne` (piège fraîcheur revenu en v3, géré en v4 et v5). À formaliser en diff si ça revient une 3e fois (seuil atteint, à arbitrer en revue hebdo).

## Erreurs récurrentes repérées (issu de `ledgers/mistakes.jsonl`)

- M-001 : mémoire qui mélangeait faits et interprétations. Corrigé par la restructuration ledgers/memory/derived.
- M-002 : ligne JSONL malformée (run cloud). Corrigé, `validate.sh` obligatoire avant commit.
- M-003 : fichier édition écrasé par une redirection d'erreur git. Corrigé, plus de `2>&1` vers un fichier de donnée.
- M-004 : redite partielle de l'info du jour (v4 vs run cloud). Fix : scanner `runs.jsonl` (sujet_info_jour) avant de figer le sujet, pas seulement `said_index.jsonl`.
