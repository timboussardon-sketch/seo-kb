# Revue hebdo SyntheticBrain (vue dérivée)

Synthèse calculée par l'agent 9 à partir des ledgers, présentée à Tim à la revue du vendredi. Vue dérivée, pas une source de vérité : tout vient des `ledgers/`.

## Semaine en cours (au 2026-06-02)

Édition du 2026-06-02 (cloud), pilier **GEO / search IA** (variation tenue : les trois info du jour précédentes étaient Actualité SEO → Recherche agentique → Product-Led SEO). Info du jour : être récupéré par un moteur génératif n'est pas être cité. Sur 15 000 requêtes soumises à ChatGPT, 548 534 pages sont récupérées et 15 % seulement sont citées dans la réponse (AirOps, mi-mars 2026, repris par Search Engine Land le 13 mars). La citation se joue après le retrieval, le long d'une chaîne (récupération → reclassement → extraction → attribution) formalisée par un preprint du 11 mars (arXiv:2603.09296) et recoupée par une synthèse Passionfruit (avril 2026, qui reprend les 85 % et y ajoute citations fantômes + instabilité des classements). Faits chiffrés : page classée 1re sur Google citée 43,2 % du temps, fan-out 89,6 % des requêtes → 43 233 requêtes effectives. Lien doctrine 5/5 : metriques-visibilite-geo distingue déjà le Hit Rate au retrieval de la citation finale (pipeline SAGEO par étape) ; les 15 % d'AirOps en sont la version empirique. Brèves : core update mai en fin de déploiement (statut au 2 juin, bilan gagnants/perdants encore non exploitable, reste une brève Actualité SEO) ; instabilité des classements de citation IA (SparkToro non-reproductibilité, Profound 40-60 %/mois) ; Bing inscrit GEO dans ses consignes officielles (27 fév. 2026, « le GEO ne garantit pas les citations comme le SEO ne garantit pas les positions »). Note qualité : ~4,3/5 (novelty 4/5, doctrine_fit 5/5, redite et clickbait faibles). 1 source explore ajoutée (airops 0.7). Prédictions : P-2026-06-02-1 (part récupérées→citées < 30 % d'ici fin 2026), P-2026-06-02-2 (instabilité > 30 %/mois documentée d'ici fin 2026).

## Éditions du 2026-06-01

Édition du 2026-06-01 (cloud), première depuis les cinq versions du 30 mai. Sujet du jour : fin de déploiement du core update de mai 2026 (lancé le 21 mai, fin ~4 juin), traité par les faits procéduraux (deuxième core update de 2026, cadence resserrée 6-7 semaines, absence de billet de blog d'accompagnement, communication minimale du Search Liaison) plutôt que par une liste gagnants/perdants jugée prématurée. Brèves : échéancier de retrait des résultats enrichis FAQ (juin/août 2026), déplacement de la composition des sources dans les moteurs de réponse après le litige Reddit-Perplexity (YouTube passe devant Reddit), mise en perspective des parts de marché (search IA ~0,9 % des visites, Google ~90 %).

Note qualité : 4,1/5 (novelty modeste 3/5, semaine sans événement neuf, beaucoup de matériel en redite avec les éditions du 30 mai). Décision méthodo confirmée : assumer un angle « ce que les données ne disent pas encore » + faits procéduraux plutôt que forcer la nouveauté ou publier un bilan avant la fin du déploiement. Abondance (source FR de référence) enfin testée et ajoutée en explore, directive d'amorçage tenue.

Édition du 2026-06-01-v2 (cloud), pilier **Recherche agentique** (variation voulue : le run du matin était pilier Actualité SEO). Info du jour : la visibilité auprès des agents devient un problème d'accès et de lisibilité, pas seulement de citation. Trois faits : jurisprudence Amazon-Perplexity (injonction du 9 mars 2026, juge Chesney, CFAA ; permission utilisateur ≠ autorisation plateforme ; sursis d'appel 9e circuit le 17 mars), blocage des robots OpenAI par Amazon dans `robots.txt` (nov 2025), « Agent Readiness score » de Cloudflare (17 avr 2026 : 4 % seulement des sites déclarent une préférence d'agents). Actionnable : entité `@id`, JSON-LD, vocabulaires d'action. Brèves : contradiction Yext (86 % brand-managed, oct 2025) vs 5W/Muck Rack (85,5 % earned media, mai 2026) sur l'origine des citations (leçon : dépend de la méthodo) ; données propriétaires/format structuré et taux de citation (BrightEdge/Averi, **premier traitement du pilier Product-Led SEO**) ; trafic IA e-commerce +805 % Black Friday 2025. Note qualité : 4,2/5 (novelty 4/5, angle propre comblant une limite empirique déclarée de la doctrine agentic-search ; clickbait et redite faibles). 5 sources explore ajoutées (emarketer, martech, yext, decrypt, cyberscoop).

Édition du 2026-06-01-v3 (cloud), pilier **Product-Led SEO** (première fois en info du jour ; les deux info du jour précédentes étaient Actualité SEO puis Recherche agentique, variation tenue). Info du jour : le contenu produit en masse par IA perd l'essentiel de son trafic, alors que les pages dont la valeur est une fonction (calculateur, simulateur) ou une donnée propriétaire résistent. Deux études datées et indépendantes : Lily Ray (13 mai 2026, 220+ sites de contenu IA, 54 % perdent ≥30 % du pic, 22 % ≥75 %, motif « Mount AI » de Glenn Gabe) et Search Engine Land (19 nov 2025, données originales = 2e prédicteur de citation ChatGPT, 52,2 % des contenus cités), recoupées par le benchmark GEO arXiv:2311.09735 et l'étude contrôlée Digital Applied. Lien doctrine 5/5 : la doctrine seo-kb sépare déjà pSEO-sans-données (= thin) et product-led/data-propriétaire (= avantage non reproductible), instrumentée par H-007 (en-test, jalon J+30 ~15 juin 2026). Brèves : désaccord entre études sur la fraîcheur comme facteur de citation AIO (Digital Applied conteste : médiane 14 mois, pas de corrélation après contrôle de l'autorité de domaine) ; corrélation schema/citation AIO (2,3×) face à la position Google « aucun markup requis » ; condition d'éligibilité d'Universal Cart (attribut native_commerce + profil /.well-known/ucp), angle nouveau distinct de l'annonce. Note qualité : 4,4/5 (novelty 4/5, doctrine_fit 5/5, redite et clickbait faibles). 2 sources explore ajoutées (lilyraynyc 0.78, almcorp 0.6). Prédictions : P-2026-06-01-v3-1 (déclin durable confirmé d'ici fin 2026), P-2026-06-01-v3-2 (effet fraîcheur reste contesté après contrôle DA).

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

---

## Instantané 2026-06-02-v2 (régénéré agent 9)

- **Édition du jour (v2)** : pilier Recherche agentique, info du jour = couche découverte du commerce agentique (flux structuré comme unité de découverte, multi-interfaces, coexistence des standards UCP/ACP/AP2). Note globale 4,4/5 (recoupement 5, angle 4, doctrine 5, hook 4).
- **Variation des piliers sur 5 éditions** : Actualité SEO → Recherche agentique (accès) → Product-Led SEO → GEO (récupération/citation) → Recherche agentique (découverte). Recherche agentique pris 2 fois sur 5 ; prochaine édition à orienter GEO, Actualité SEO ou Product-Led SEO.
- **Sources** : 38 sources au registre, 6 ajoutées ce run (2 primaires fortes : google-cloud-blog 1.09, openai-blog 1.09). Candidates exploit en revue hebdo : ahrefs, lilyraynyc, digitalapplied, getpassionfruit, abondance, emarketer, martech, airops, google-cloud-blog, openai-blog.
- **Dette récurrente** : aucune source de mesure de visibilité (Sistrix/Semrush Sensor/Mozcast) toujours pas testée après 4 éditions ; bloquante pour le bilan core update attendu mi-juin.
- **Prédictions ouvertes** : 16 au total, dont 2 nouvelles ce run (P-2026-06-02-v2-1 coexistence des standards, P-2026-06-02-v2-2 flux produit prédicteur de sélection par agent). Aucune échue à résoudre au 2026-06-02.

---

## Mise à jour 2026-06-03 (pré-revue hebdo)

**Piliers d'info du jour de la semaine** : Actualité SEO (0601 matin) → Recherche agentique accès (0601 v2) → Product-Led SEO (0601 v3) → GEO écart récupération-citation (0602 matin) → Recherche agentique découverte (0602 v2) → GEO mesure first-party de la présence IA (0603). Bonne rotation, deux occurrences GEO et deux Recherche agentique sur six ; Product-Led SEO sous-représenté (1 fois), à privilégier la semaine prochaine.

**Fait marquant 0603** : Google ouvre une mesure de première main de l'apparition d'un site en AI Overviews/AI Mode (rapport Search Console) et un réglage d'exclusion séparé de la recherche classique, déployé d'abord au Royaume-Uni après l'exigence de l'autorité de concurrence britannique (28 janv. 2026). Réserve : la métrique d'impression est en cours de correction (sur-comptage reconnu le 3 avril 2026).

**Core update mai** : déploiement clos le 2 juin. Lecture fiable ~9 juin. Le bilan gagnants/perdants (brève Actualité SEO, jamais info du jour) devient enfin produisible dès qu'une analyse large échantillon stable sort. Résout l'échéance proche P-2026-06-01-1 (2026-06-30).

**Sources** : passages exploit à arbitrer — ahrefs, abondance, getpassionfruit, digitalapplied, lilyraynyc, emarketer, martech, google-cloud-blog, openai-blog, 9to5google (toutes à plusieurs hits ou à forte autorité). Directive Sistrix/Mozcast toujours non tenue.

**Prédictions à échéance proche** : P-2026-06-01-1 (profil des perdants core update, 2026-06-30).
