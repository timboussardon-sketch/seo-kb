# Revue hebdo SyntheticBrain (vue dérivée)

Synthèse calculée par l'agent 9 à partir des ledgers, présentée à Tim à la revue du vendredi. Vue dérivée, pas une source de vérité : tout vient des `ledgers/`.

## Semaine en cours (au 2026-06-01)

Édition du 2026-06-01 (cloud), première depuis les cinq versions du 30 mai. Sujet du jour : fin de déploiement du core update de mai 2026 (lancé le 21 mai, fin ~4 juin), traité par les faits procéduraux (deuxième core update de 2026, cadence resserrée 6-7 semaines, absence de billet de blog d'accompagnement, communication minimale du Search Liaison) plutôt que par une liste gagnants/perdants jugée prématurée. Brèves : échéancier de retrait des résultats enrichis FAQ (juin/août 2026), déplacement de la composition des sources dans les moteurs de réponse après le litige Reddit-Perplexity (YouTube passe devant Reddit), mise en perspective des parts de marché (search IA ~0,9 % des visites, Google ~90 %).

Note qualité : 4,1/5 (novelty modeste 3/5, semaine sans événement neuf, beaucoup de matériel en redite avec les éditions du 30 mai). Décision méthodo confirmée : assumer un angle « ce que les données ne disent pas encore » + faits procéduraux plutôt que forcer la nouveauté ou publier un bilan avant la fin du déploiement. Abondance (source FR de référence) enfin testée et ajoutée en explore, directive d'amorçage tenue.

Édition du 2026-06-01-v2 (cloud), pilier **Recherche agentique** (variation voulue : le run du matin était pilier Actualité SEO). Info du jour : la visibilité auprès des agents devient un problème d'accès et de lisibilité, pas seulement de citation. Trois faits : jurisprudence Amazon-Perplexity (injonction du 9 mars 2026, juge Chesney, CFAA ; permission utilisateur ≠ autorisation plateforme ; sursis d'appel 9e circuit le 17 mars), blocage des robots OpenAI par Amazon dans `robots.txt` (nov 2025), « Agent Readiness score » de Cloudflare (17 avr 2026 : 4 % seulement des sites déclarent une préférence d'agents). Actionnable : entité `@id`, JSON-LD, vocabulaires d'action. Brèves : contradiction Yext (86 % brand-managed, oct 2025) vs 5W/Muck Rack (85,5 % earned media, mai 2026) sur l'origine des citations (leçon : dépend de la méthodo) ; données propriétaires/format structuré et taux de citation (BrightEdge/Averi, **premier traitement du pilier Product-Led SEO**) ; trafic IA e-commerce +805 % Black Friday 2025. Note qualité : 4,2/5 (novelty 4/5, angle propre comblant une limite empirique déclarée de la doctrine agentic-search ; clickbait et redite faibles). 5 sources explore ajoutées (emarketer, martech, yext, decrypt, cyberscoop).

## Semaine précédente (au 2026-05-30)

Cinq éditions le 2026-05-30 (run d'amorçage v2, cloud, v3, v4, v5). Sujets couverts, tous dans le périmètre search/IA :
- v2 : Information Agents (agents qui lisent), AI Mode > 1 Md MAU, Gemini 3.5 Flash, core update du 21 mai, Expert Advice AIO.
- v3 : commerce agentique (Universal Cart / UCP, agents qui achètent), fin du core update, crawl-to-refer Cloudflare, conversion trafic IA vs volume.
- v4 : llms.txt non utilisé par la recherche IA de Google (lien doctrine SAGEO + AEO), parts Gemini vs ChatGPT, redesign du champ de recherche I/O, CTR AIO en hausse pour les pages citées (Seer).
- v5 : formats publicitaires payants dans AI Mode / AI Overviews (Google Marketing Live 20 mai, étiquetés Sponsored), publicités OpenAI dans ChatGPT, divergence de citations ChatGPT/Perplexity (Averi 680M, 11 %), Ahrefs 38 % des citations AIO dans le top-10 organique, dépréciation des résultats enrichis FAQ (7 mai 2026).

Note qualité moyenne de la semaine : ~4,4/5. Point d'attention : cinq éditions le même jour (cadence prévue 2/jour), à arbitrer ; un overlap thématique partiel entre v4 et le run cloud (llms.txt / guide du 15 mai), tracé en mistake M-004.

## Prédictions ouvertes à suivre

- P-2026-06-01-1 : les perdants du core update de mai partagent un déficit de signaux structurés (vs vertical unique), confirmé par une analyse à large échantillon d'ici 2026-06-30 (échéance courte).
- P-2026-06-01-2 : YouTube reste devant Reddit comme première source sociale citée dans les moteurs de réponse d'ici fin 2026.
- P-2026-05-30-1 : Expert Advice augmente la part de citations de première main (échéance 2026-07-15).
- P-2026-05-30-2 : une vente via checkout agentique UCP rapportée avant 2026-09-30.
- P-2026-05-30-3 : Googlebot sous 27 % du crawl IA d'ici fin 2026.
- P-2026-05-30-4 : Google maintient « llms.txt non utilisé » d'ici fin 2026.
- P-2026-05-30-5 : un format pub AI Mode (Conversational Discovery Ads / Highlighted Answers) sorti du stade annonce et accessible aux annonceurs US d'ici fin 2026.
- P-2026-05-30-6 : recouvrement de domaines cités ChatGPT/Perplexity confirmé < 25 % par une nouvelle mesure d'ici fin 2026.
- P-2026-06-01-v2-1 : la part de sites déclarant une préférence d'usage pour les agents IA dans `robots.txt` dépasse 4 % (mesure Cloudflare) d'ici fin 2026.
- P-2026-06-01-v2-2 : l'appel Amazon-Perplexity au 9e circuit n'est pas tranché au fond avant 2026-09-30.

## À trancher par Tim (issu de `memory/questions.md`)

- **Contradiction mémoire (nouveau 2026-06-01)** : `wording_rules.md` cite encore `ton-de-voix-tim` et le tutoiement, en contradiction avec `voix-synthetic.md` (qui fait foi : vouvoiement, voix propre). Diff proposé : nettoyer `wording_rules.md`. À valider.
- Cadence et versionnage : 5 éditions le 30 mai (prévu 2/jour). Une édition fait-elle référence pour la journée ? Format de l'édition de l'après-midi (court vs complet) ?
- Rubrique fixe « ce qu'un agent retiendrait » ?
- Règle à valider : une doc primaire officielle de l'éditeur (ex. Google Search Central sur la dépréciation FAQ) dispense-t-elle du recoupement à 2 sources indépendantes ?
- Seuil mono-étude : le chiffre 11 % (Averi) publié comme mono-étude flaguée avec direction recoupée, ou à écarter du corps faute de 2e source chiffrée ?
- Sources `explore` à confirmer ou retirer : `lumar` (0.62), `cloudflare-radar` (0.85), `similarweb-geo` (0.78), `seer-interactive` (0.75), `theseocommunity` (0.6), `getpassionfruit` (0.6), `ahrefs` (0.8, candidate exploit), `averi` (0.62), `tryprofound` (0.6), et nouvelles du run 2026-06-01 : `abondance` (0.7, FR de référence, candidate exploit), `digitalapplied` (0.6), `cmswire` (0.62), `searchlab` (0.6). En attente sous le seuil : `pikaseo` (0.58), `premiere.page` (0.55). Nouvelles du run 2026-06-01-v2 : `emarketer` (0.72, candidate exploit), `martech` (0.7, candidate exploit), `yext` (0.65, vendeur, chiffres dépendants de la méthodo), `decrypt` (0.62), `cyberscoop` (0.6). En attente sous le seuil ou wire/vendeur : `pymnts` (0.58), `commercetools` (0.58), `metarouter` (0.55), `prnewswire-5w` (0.55), `morningstar` (0.55), `semrush` (0.6), `cnbc`/`yahoo-finance` (0.7, presse générale).
- Sources tech généralistes (Tom's Guide, VentureBeat, TechRadar, BleepingComputer, PPC.land) : corroboration ponctuelle hors registre, ou intégration ?

## Propositions doctrine (issu de `memory/questions.md`)

- Confirmer le concept `agentic-search` côté « agent qui achète » (UCP, v3) et « agent qui transige dans la réponse via paiement natif » (formats pub AI Mode, v5).
- Ajouter à `structural-information-geo`/`aeo` la convergence avec la position Google sur llms.txt (v4).
- Signal pour `aeo` (v5) : la réponse générative de Google contient désormais deux voies distinctes, citation organique et emplacement payé étiqueté Sponsored. La doctrine AEO ne couvre que la première ; préciser la frontière.
- Signal pour `agentic-search` (v2, 2026-06-01) : ajouter une section empirique « accès et lisibilité » qui lève partiellement la limite déclarée de la fiche (« agent qui agit mal couvert empiriquement »), avec la jurisprudence Amazon-Perplexity, le blocage `robots.txt`, le Cloudflare Agent Readiness et les vocabulaires d'action (`OrderAction`/`ReserveAction`).

## Diffs de skill proposés

Aucun appliqué. Piste récurrente : garde-fou « vérifier la date de la source primaire » dans le socle `revue-presse-quotidienne` (piège fraîcheur revenu en v3, géré en v4 et v5). À formaliser en diff si ça revient une 3e fois (seuil atteint, à arbitrer en revue hebdo).

## Erreurs récurrentes repérées (issu de `ledgers/mistakes.jsonl`)

- M-001 : mémoire qui mélangeait faits et interprétations. Corrigé par la restructuration ledgers/memory/derived.
- M-002 : ligne JSONL malformée (run cloud). Corrigé, `validate.sh` obligatoire avant commit.
- M-003 : fichier édition écrasé par une redirection d'erreur git. Corrigé, plus de `2>&1` vers un fichier de donnée.
- M-004 : redite partielle de l'info du jour (v4 vs run cloud). Fix : scanner `runs.jsonl` (sujet_info_jour) avant de figer le sujet, pas seulement `said_index.jsonl`.
