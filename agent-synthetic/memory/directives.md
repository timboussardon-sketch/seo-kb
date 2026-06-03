# Directives pour la prochaine édition

> PÉRIMÈTRE STRICT (Tim, 2026-05-30) : SEO, IA, LLM, Google, moteurs de recherche, search marketing. RIEN D'AUTRE. Test : « ça change la façon dont on est trouvé/lu/cité dans un moteur ? » Sinon, écarter.
>
> LIENS DE SOURCES (Tim, 2026-05-30) : TOUJOURS afficher le lien cliquable de chaque source dans le corps.
>
> PILIERS DE SUJETS (Tim, 2026-06-01) : chaque édition s'ancre sur l'un des 4 piliers, identifié explicitement dans le corps — (1) Agentic search, (2) Product-Led SEO, (3) GEO / search IA, (4) Actualité SEO. Varier le pilier d'une édition à l'autre, ne pas rester bloqué sur le même. INTERDICTION DU MONO-SUJET GOOGLE : un core update ou une update d'algorithme Google ne peut être qu'une brève dans « Actualité SEO », JAMAIS l'info du jour. Angles principaux à privilégier : Agentic search, Product-Led SEO, GEO. Cette liste fait foi ; si Tim la change, c'est ici qu'on la met à jour.


Écrit par l'agent 9 (calibration) à la fin de chaque édition. Lu par l'agent 0 (briefing) au début de la suivante. Garder court et actionnable.

## Édition 0 (amorçage, 2026-05-30)

Pas encore d'historique. Première édition à produire sans biais de boucle. Objectifs d'amorçage :

- Tenir les 4 critères de qualité dès la première : recoupement, angle inédit, lien doctrine, hook intelligent.
- Pour chaque info retenue, exiger au moins 2 sources indépendantes (recoupement).
- Lier au moins une info à un concept de la doctrine via `./kb search`.
- Tester le mode explore : trouver au moins 1 source nouvelle, hors liste socle, et la noter dans `source_registry.jsonl`.
- Logger au moins 1 prédiction datée dans `predictions.jsonl`.

## Directives pour la prochaine édition (écrit après 2026-05-30-v5)

- **Anti-redite (mis à jour v5)** : déjà traités, ne pas reprendre sans fait nouveau → « guide AEO du 15 mai », « Information Agents I/O » (v2), « commerce agentique / Universal Cart / UCP » (v3), Cloudflare crawl-to-refer (v3), conversion trafic IA vs volume (v3), « llms.txt non utilisé par Google » + champ de recherche redessiné I/O + parts Gemini vs ChatGPT + CTR AIO recovery Seer (v4), **« formats publicitaires payants dans AI Mode / GML 20 mai » + « ads ChatGPT OpenAI » + « divergence citations ChatGPT/Perplexity Averi 680M » + « Ahrefs 38 % citations AIO top-10 » + « dépréciation résultats enrichis FAQ » (v5)**. Voir `said_index.jsonl`.
- **Distinction à garder en tête (v5)** : la publicité payante dans la réponse générative (formats Gemini étiquetés Sponsored) est un sujet distinct du checkout agentique organique (UCP, v3). Ne pas confondre les deux dans une prochaine édition.
- **Leçon v4 maintenue (vérifier l'overlap avant de figer l'info du jour)** : lire `runs.jsonl` champ `sujet_info_jour`/`sujets_candidats` des runs récents (cloud inclus), pas seulement `said_index.jsonl`. Voir mistake M-004.
- **Pistes fraîches non encore traitées (candidates prochaine édition)** : bilan de fin de déploiement du core update de mai (attendre ≥1 semaine après le ~4 juin) ; premières ventes mesurées via checkout agentique UCP (résout P-2026-05-30-2) ; remontées terrain sur le bloc Expert Advice des AIO (résout P-2026-05-30-1, échéance 2026-07-15) ; suivi de la mise à disposition des formats pub AI Mode aux annonceurs (résout P-2026-05-30-5) ; tester une source FR de référence (Abondance), toujours pas fait.
- **Suivre en priorité** :
  - Bilan du core update de mai (déploiement clos vers le 4 juin). Candidat brève « bilan » si des verticaux gagnants/perdants nets se dégagent dans les données publiques, ≥1 semaine après la fin.
  - Premières remontées terrain sur le checkout agentique UCP/Universal Cart (déploiement US « cet été »). Un chiffre de ventes via agent → info du jour forte (résout P-2026-05-30-2).
  - Disponibilité effective des formats pub AI Mode (Conversational Discovery Ads, Highlighted Answers) pour les annonceurs, et premiers retours sur la frontière organique/payant dans la réponse (résout P-2026-05-30-5).
  - Nouvelle mesure de recouvrement de citations entre moteurs (suite Averi/Profound) : guetter une étude postérieure pour résoudre P-2026-05-30-6.
- **Prédictions ouvertes à surveiller** : P-1 (Expert Advice / citations première main, 2026-07-15), P-2 (vente checkout agentique, 2026-09-30), P-3 (Googlebot < 27 % crawl IA, 2026-12-31), P-4 (llms.txt non utilisé maintenu, 2026-12-31), P-5 (format pub AI Mode sorti du stade annonce, 2026-12-31), P-6 (recouvrement citations ChatGPT/Perplexity < 25 %, 2026-12-31).
- **Sources** : 3 sources ajoutées en explore ce run (ahrefs 0.8, averi 0.62, tryprofound 0.6). Les confirmer/retirer en revue hebdo. ahrefs est une source SEO de référence, bonne candidate au passage exploit. Continuer 1 source neuve/édition. Tester enfin une source FR de référence (Abondance) la prochaine fois.

## À tester (issu de questions.md)

- Rubrique fixe « ce qu'un agent retiendrait » pour forcer l'angle citation (à valider en revue hebdo).

## À éviter (issu des critiques passées)

- Empiler des stats mono-source de blogs marketing. Toujours recouper avant de mettre un chiffre dans le corps.
- **Piège fraîcheur confirmé v3** : les résumés de WebSearch redatent en 2026 des études de 2025. RÈGLE : pour tout chiffre clé, ouvrir la source primaire et vérifier la date de publication ET la période de mesure avant de l'écrire. Si l'étude a > 30 j, soit on la date explicitement dans le corps, soit on ne la met pas en brève.

## Directives pour la prochaine édition (écrit après 2026-06-01)

- **Anti-redite (mis à jour 2026-06-01)** : ajouter à la liste à ne pas reprendre sans fait nouveau → « core update mai : fin de déploiement + faits procéduraux (absence de billet, cadence 6-7 sem) » (2026-06-01), « échéancier de retrait des résultats enrichis FAQ juin/août » (2026-06-01), « composition des sources moteurs de réponse : litige Reddit-Perplexity, YouTube devant Reddit » (2026-06-01), « parts de marché search IA vs Google/Bing StatCounter » (2026-06-01). Voir `said_index.jsonl`.
- **PRIORITÉ prochaine édition (le bilan reporté)** : le déploiement du core update de mai se termine ~4 juin. Dès qu'une analyse à large échantillon sort (SISTRIX/Lily Ray attendue ~5 juin, Sistrix Visibility, Semrush Sensor stabilisé), produire le bilan gagnants/perdants par vertical. Cela résout P-2026-06-01-1 (profil des perdants : déficit de signaux structurés vs vertical unique). C'est l'info du jour la plus forte disponible à court terme. Attendre la fin du déploiement + données stables, ne pas publier de liste avant le 4 juin.
- **Pistes fraîches non traitées (candidates)** : premières ventes mesurées via checkout agentique UCP (résout P-2026-05-30-2) ; remontées terrain sur le bloc Expert Advice des AIO (résout P-2026-05-30-1, 2026-07-15) ; disponibilité effective des formats pub AI Mode aux annonceurs (résout P-2026-05-30-5) ; nouvelle mesure de recouvrement de citations entre moteurs (résout P-2026-05-30-6).
- **Sources** : Abondance enfin testée (directive tenue), ajoutée en explore 0.7, corroborée, bonne candidate au passage exploit en revue hebdo (source FR de référence). 3 autres explore ajoutées (digitalapplied, cmswire, searchlab). Continuer 1 source neuve/édition. Pour le bilan core update, viser une source de mesure de visibilité (Sistrix, Semrush Sensor, Mozcast) comme nouvelle source explore data.
- **Méthode confirmée 2026-06-01** : quand la semaine n'offre pas d'événement neuf, l'angle « ce que les données ne disent pas encore » + faits procéduraux est préférable à la redite ou à une liste gagnants/perdants prématurée. Assumer un novelty_score modeste (3/5) plutôt que de forcer.

## Prédictions ouvertes à surveiller (mis à jour 2026-06-01)

- P-2026-06-01-1 (profil des perdants core update mai = déficit signaux structurés, 2026-06-30, échéance courte).
- P-2026-06-01-2 (YouTube reste devant Reddit en citations moteurs de réponse, 2026-12-31).
- Plus les P-2026-05-30-1 à 6 déjà listées.

## Directives pour la prochaine édition (écrit après 2026-06-01-v2)

- **Anti-redite (mis à jour 2026-06-01-v2)** : ajouter à la liste à ne pas reprendre sans fait nouveau → « recherche agentique : accès/autorisation des marques pour les agents (jurisprudence Amazon-Perplexity, blocage robots.txt OpenAI, Cloudflare agent-readiness, lisibilité machine @id/JSON-LD/Action) » (v2), « contradiction Yext vs 5W/Muck Rack sur brand-managed vs earned media » (v2), « données propriétaires/format structuré et taux de citation, BrightEdge/Averi » (v2), « trafic IA e-commerce +805 % Black Friday 2025 » (v2). Voir said_index.jsonl.
- **Variation des piliers (à tenir)** : deux derniers piliers d'info du jour = Actualité SEO (matin) puis Recherche agentique (v2). Prochaine édition : viser plutôt GEO ou Product-Led SEO en info du jour pour ne pas répéter l'agentique. Product-Led SEO n'a encore jamais été l'info du jour, c'est un angle à privilégier (calculateur/simulateur/générateur qui se classe sur requête « Do », score Fully Meets des Quality Raters).
- **PRIORITÉ reportée toujours en attente** : le bilan gagnants/perdants du core update de mai (déploiement clos ~4 juin). Dès qu'une analyse large échantillon stable sort (SISTRIX/Lily Ray, Semrush Sensor, Mozcast), produire le bilan en brève du pilier Actualité SEO (jamais en info du jour : interdiction du mono-sujet Google). Résout P-2026-06-01-1 (échéance 2026-06-30).
- **Pistes fraîches non traitées (candidates)** : premières ventes mesurées via checkout agentique UCP (résout P-2026-05-30-2) ; suite de l'appel Amazon-Perplexity au 9e circuit (résout P-2026-06-01-v2-2) ; adoption mesurée des préférences d'agents dans robots.txt / Content Signals (résout P-2026-06-01-v2-1) ; bloc Expert Advice AIO (résout P-2026-05-30-1, 2026-07-15) ; disponibilité effective des formats pub AI Mode (résout P-2026-05-30-5).
- **Sources** : 5 explore ajoutées (emarketer 0.72, martech 0.7, yext 0.65, decrypt 0.62, cyberscoop 0.6). martech et emarketer sont des sources de référence, candidates au passage exploit en revue hebdo. Continuer 1 source neuve/édition. Tester encore une source de mesure de visibilité (Sistrix, Semrush Sensor, Mozcast) pour le bilan core update.
- **Méthode confirmée v2** : quand aucun événement de la semaine en cours n'est disponible, un angle de synthèse opérationnelle (décomposer un phénomène en conditions concrètes et actionnables) ancré sur la donnée datée la plus récente, avec dates affichées, vaut mieux qu'une fausse fraîcheur. Novelty 4/5 atteignable sans événement neuf si l'angle est vraiment propre.

## Prédictions ouvertes ajoutées 2026-06-01-v2

- P-2026-06-01-v2-1 (part de sites déclarant une préférence d'agents IA dans robots.txt > 4 %, 2026-12-31).
- P-2026-06-01-v2-2 (appel Amazon-Perplexity non tranché au fond avant 2026-09-30).

## Directives pour la prochaine édition (écrit après 2026-06-01-v3)

- **Anti-redite (mis à jour 2026-06-01-v3)** : ajouter à la liste à ne pas reprendre sans fait nouveau → « déclin du contenu IA mis à l'échelle / étude Lily Ray 220+ sites du 13 mai (54/39/22 %) / motif Mount AI » (v3), « données originales = 2e prédicteur de citation ChatGPT, SEL nov 2025 52,2 % » (v3), « effet fraîcheur sur citation AIO contesté, Digital Applied médiane 14 mois / pas de corrélation après contrôle autorité de domaine » (v3), « schema 2,3× citation AIO vs position Google aucun markup requis » (v3), « éligibilité Universal Cart : attribut native_commerce + profil /.well-known/ucp » (v3). Voir said_index.jsonl.
- **Variation des piliers (à tenir)** : trois dernières info du jour = Actualité SEO (matin) → Recherche agentique (v2) → Product-Led SEO (v3). Prochaine édition : viser plutôt GEO / search IA en info du jour (pilier non encore pris en info du jour récemment), ou un angle Actualité SEO si un événement net sort. Ne pas réenchaîner Product-Led SEO sans fait nouveau.
- **PRIORITÉ reportée toujours en attente** : bilan gagnants/perdants du core update de mai (déploiement clos ~4 juin). Dès qu'une analyse large échantillon stable sort (SISTRIX/Lily Ray, Semrush Sensor, Mozcast), produire le bilan en BRÈVE du pilier Actualité SEO, jamais en info du jour (interdiction mono-Google). Résout P-2026-06-01-1 (échéance 2026-06-30).
- **Boucle preuve à surveiller (interne)** : la fiche preuve pSEO data-propriétaire (H-007) a son jalon J+30 vers le 2026-06-15. Si elle est renseignée, c'est un fait interne fort pour une édition Product-Led SEO ou data-propriétaire (mais attendre un fait neuf, ne pas re-traiter le pilier sans).
- **Pistes fraîches non traitées (candidates)** : premières ventes mesurées via checkout agentique UCP (résout P-2026-05-30-2) ; bloc Expert Advice AIO (résout P-2026-05-30-1, 2026-07-15) ; disponibilité effective des formats pub AI Mode (résout P-2026-05-30-5) ; nouvelle mesure de recouvrement de citations entre moteurs (résout P-2026-05-30-6) ; adoption préférences d'agents robots.txt/Content Signals (résout P-2026-06-01-v2-1).
- **Sources** : 2 explore ajoutées (lilyraynyc 0.78, almcorp 0.6). lilyraynyc et digitalapplied sont des candidates au passage exploit en revue hebdo (sources data utiles, plusieurs hits). Continuer 1 source neuve/édition. Tester encore une source de mesure de visibilité (Sistrix, Semrush Sensor, Mozcast) pour le bilan core update.
- **Méthode confirmée v3** : relier un fait d'actualité daté (étude récente) à une page de doctrine interne précise donne un doctrine_fit 5/5 et une novelty 4/5 sans forcer. Quand on cite un chiffre contre-intuitif (Digital Applied : la fraîcheur ne prédit pas la citation), présenter le désaccord entre études plutôt que de trancher ; c'est conforme à la voix (assumer l'incertitude).

## Prédictions ouvertes ajoutées 2026-06-01-v3

- P-2026-06-01-v3-1 (déclin durable >50% confirmé par une étude indépendante de Lily Ray d'ici fin 2026).
- P-2026-06-01-v3-2 (effet fraîcheur sur citation AIO reste contesté après contrôle de l'autorité de domaine, fin 2026).

## Directives pour la prochaine édition (écrit après 2026-06-02)

- **Anti-redite (mis à jour 2026-06-02)** : ajouter à la liste à ne pas reprendre sans fait nouveau → « écart récupération vs citation / 85 % des pages récupérées par ChatGPT non citées / AirOps 548 534 pages 15 000 requêtes 15 % » (2026-06-02), « fan-out queries 89,6 % → 43 233 / page classée 1re citée 43,2 % » (2026-06-02), « taxonomie en 4 étapes de l'échec de citation, arXiv:2603.09296 » (2026-06-02), « instabilité des classements de citation IA, SparkToro non-reproductibilité + Profound 40-60 %/mois » (2026-06-02), « Bing inscrit GEO dans ses consignes officielles 27 fév., balises NOARCHIVE/NOCACHE/Copilot » (2026-06-02). Voir said_index.jsonl.
- **PRIORITÉ prochaine édition (le bilan enfin mûr)** : le déploiement du core update de mai se termine vers le 4 juin ; Google recommande d'attendre ≥7 jours, donc des données stables vers le 11 juin. Dès qu'une analyse large échantillon stable sort (SISTRIX/Lily Ray, Semrush Sensor, Mozcast), produire le bilan gagnants/perdants par vertical en BRÈVE du pilier Actualité SEO, jamais en info du jour (interdiction mono-Google). Résout P-2026-06-01-1 (échéance 2026-06-30). Pour cela, tester enfin une source de mesure de visibilité (Sistrix, Semrush Sensor, Mozcast) comme nouvelle source explore data, directive répétée non encore tenue.
- **Variation des piliers (à tenir)** : quatre dernières info du jour = Actualité SEO (0601 matin) → Recherche agentique (v2) → Product-Led SEO (v3) → GEO/search IA (2026-06-02). Prochaine édition : viser plutôt Recherche agentique avec un FAIT NEUF (première vente mesurée via UCP, suite appel Amazon-Perplexity) ou Actualité SEO si le bilan core update sort, pour ne pas réenchaîner GEO sans fait nouveau. Ne pas reprendre l'écart récupération/citation sans nouvelle mesure.
- **Boucle preuve interne à surveiller** : la fiche preuve pSEO data-propriétaire (H-007) a son jalon J+30 vers le 2026-06-15. Si renseignée, fait interne fort pour une édition Product-Led SEO ou data-propriétaire (attendre un fait neuf, ne pas re-traiter le pilier sans).
- **Pistes fraîches non traitées (candidates)** : premières ventes mesurées via checkout agentique UCP (résout P-2026-05-30-2) ; bloc Expert Advice AIO (résout P-2026-05-30-1, 2026-07-15) ; disponibilité effective des formats pub AI Mode (résout P-2026-05-30-5) ; adoption préférences d'agents robots.txt/Content Signals (résout P-2026-06-01-v2-1) ; suite appel Amazon-Perplexity 9e circuit (résout P-2026-06-01-v2-2).
- **Sources** : airops ajoutée en explore (0.7, étude data primaire, candidate exploit). getpassionfruit à 3 hits, candidate au passage exploit en revue hebdo (bonne source de synthèse GEO). Continuer 1 source neuve/édition. Toujours pas testé : Sistrix/Semrush Sensor/Mozcast (mesure de visibilité, utile pour le bilan core update).
- **Méthode confirmée 2026-06-02** : relier une mesure empirique récente (AirOps) à une page de doctrine interne précise (metriques-visibilite-geo, pipeline par étape) donne doctrine_fit 5/5 et novelty 4/5 sans forcer. Quand un preprint apporte un cadre utile mais une seule source, le présenter comme cadre et garder la charge probante sur les sources empiriques corroborées ; ne jamais publier un chiffre non extractible avec fiabilité (ici, le taux de réparation du preprint, volontairement omis).

## Prédictions ouvertes ajoutées 2026-06-02

- P-2026-06-02-1 (part des pages récupérées finissant citées < 30 % confirmée par une mesure indépendante, 2026-12-31).
- P-2026-06-02-2 (instabilité temporelle des citations IA > 30 %/mois documentée sur ≥1 moteur, 2026-12-31).

## Directives pour la prochaine édition (écrit après 2026-06-02-v2)

- **Anti-redite (mis à jour 2026-06-02-v2)** : ajouter à la liste à ne pas reprendre sans fait nouveau → « couche découverte du commerce agentique : flux produit structuré comme unité de découverte vs page web, attributs conversationnels Merchant Center, découverte multi-interfaces ChatGPT/Copilot/AI Mode/Gemini/Shop, Shopify Catalog » (v2), « coexistence des standards UCP/ACP/AP2, AP2 60+ partenaires couche paiement, coût des intégrations multiples » (v2), « PYMNTS 75 acquéreurs retard marchands » (v2), « Shopify trafic IA ×8 / commandes IA ×15 depuis janv 2025 (vendeur, fragile) » (v2), « amicus EFF/Mozilla 9 avril Amazon-Perplexity » (v2). Voir said_index.jsonl.
- **Variation des piliers (à tenir)** : cinq dernières info du jour = Actualité SEO (0601 matin) → Recherche agentique accès (0601 v2) → Product-Led SEO (0601 v3) → GEO/écart récupération-citation (0602 matin) → Recherche agentique découverte (0602 v2). Prochaine édition : viser GEO/search IA avec un fait neuf, ou Actualité SEO si le bilan core update sort, ou Product-Led SEO. NE PAS réenchaîner Recherche agentique sans fait nouveau (deux des cinq dernières y sont déjà). Ne pas reprendre la couche découverte du commerce agentique sans fait neuf.
- **PRIORITÉ prochaine édition (bilan core update enfin mûr)** : déploiement clos vers le 4 juin, données stables vers le 11 juin (consigne Google ≥7 j). Dès qu'une analyse large échantillon stable sort (SISTRIX/Lily Ray, Semrush Sensor, Mozcast), produire le bilan gagnants/perdants par vertical en BRÈVE du pilier Actualité SEO, jamais en info du jour (interdiction mono-Google). Résout P-2026-06-01-1 (échéance 2026-06-30). Tester ENFIN une source de mesure de visibilité (Sistrix, Semrush Sensor, Mozcast) comme nouvelle source explore data : directive répétée sur 4 éditions, toujours non tenue, à prioriser.
- **Boucle preuve interne à surveiller** : fiche preuve pSEO data-propriétaire (H-007), jalon J+30 vers le 2026-06-15. Si renseignée, fait interne fort pour une édition Product-Led SEO (attendre un fait neuf, ne pas re-traiter le pilier sans).
- **Pistes fraîches non traitées (candidates)** : premières ventes mesurées via checkout agentique UCP, toujours aucun chiffre de vente publié (P-2026-05-30-2, 2026-09-30) ; décision au fond Amazon-Perplexity 9e circuit, Amazon devait répondre vers le 22 avril, guetter la suite (P-2026-06-01-v2-2, 2026-09-30) ; bloc Expert Advice AIO (P-2026-05-30-1, 2026-07-15) ; disponibilité effective des formats pub AI Mode (P-2026-05-30-5) ; adoption préférences d'agents robots.txt/Content Signals (P-2026-06-01-v2-1).
- **Sources** : 6 explore ajoutées ce run (google-cloud-blog 0.88, openai-blog 0.85, shopify-blog 0.65, pymnts 0.66, digitalcommerce360 0.66, mediapost 0.6). google-cloud-blog et openai-blog sont des sources primaires, bonnes candidates au passage exploit en revue hebdo. fourweekmba (analyse, trust 0.55) NON ajoutée, sous le seuil, notée en questions.md. Continuer 1 source neuve/édition.
- **Méthode confirmée 2026-06-02-v2** : sur un pilier sans événement neuf de la semaine, décomposer un phénomène en variables actionnables (ici, trois déplacements de l'objet à optimiser pour l'achat agentique) et combler une limite explicite d'une fiche de doctrine donne doctrine_fit 5/5 et novelty 4/5 sans forcer. Toujours marquer les chiffres vendeur comme direction attribuée, jamais comme valeur de référence ; séparer le fait (existence des standards) de la lecture (issue probable du marché).

## Prédictions ouvertes ajoutées 2026-06-02-v2

- P-2026-06-02-v2-1 (aucun standard de commerce agentique > 70 % des transactions mesurées, UCP et ACP coexistent, 2026-12-31).
- P-2026-06-02-v2-2 (structure/complétude du flux produit documentée comme prédicteur de la sélection par un agent acheteur, 2026-12-31).

## Directives pour la prochaine édition (écrit après 2026-06-03)

- **Anti-redite (mis à jour 2026-06-03)** : ajouter à la liste à ne pas reprendre sans fait nouveau → « rapport de performance des fonctions IA dans Search Console (impressions/pages/pays/appareils/dates, sans clic) » (2026-06-03), « réglage d'exclusion des AI Overviews/AI Mode/AI Overviews dans Discover, séparé de la recherche classique, non signal de classement, déploiement UK d'abord » (2026-06-03), « contexte CMA UK 28 janvier 2026 sur les contrôles d'opt-out éditeurs » (2026-06-03), « sur-comptage des impressions GSC reconnu le 3 avril 2026, ~11 mois, correction en cours » (2026-06-03), « core update mai 2026 : déploiement terminé le 2 juin, lecture fiable ~9 juin » (2026-06-03), « lancement Hey Savi/PayPal achat agentique UK + Debenhams » (2026-06-03), « sondage SEL 33,2 % d'intention de blocage des fonctions IA » (2026-06-03). Voir said_index.jsonl.
- **Variation des piliers (à tenir)** : six dernières info du jour = Actualité SEO (0601 matin) → Recherche agentique accès (0601 v2) → Product-Led SEO (0601 v3) → GEO écart récupération-citation (0602 matin) → Recherche agentique découverte (0602 v2) → GEO mesure first-party de la présence IA (0603). Prochaine édition : viser Product-Led SEO (pas en info du jour depuis le 0601 v3) ou Actualité SEO avec un fait net. NE PAS réenchaîner GEO ni Recherche agentique en info du jour sans fait franchement neuf.
- **PRIORITÉ enfin mûre côté Actualité SEO** : le core update de mai est CLOS depuis le 2 juin ; la fenêtre de lecture fiable des données s'ouvre vers le 9 juin. Dès qu'une analyse large échantillon stable sort (SISTRIX/Lily Ray, Semrush Sensor, Mozcast), produire le bilan gagnants/perdants par vertical en BRÈVE du pilier Actualité SEO, jamais en info du jour (interdiction mono-Google). Résout P-2026-06-01-1 (échéance 2026-06-30, proche). Pour cela, tester ENFIN une source de mesure de visibilité (Sistrix, Semrush Sensor, Mozcast) comme nouvelle source explore data : directive répétée sur 5 éditions, toujours non tenue, à prioriser absolument la prochaine fois.
- **Boucle preuve interne à surveiller** : fiche preuve pSEO data-propriétaire (H-007), jalon J+30 vers le 2026-06-15. Si renseignée, fait interne fort pour une édition Product-Led SEO (attendre un fait neuf, ne pas re-traiter le pilier sans).
- **Pistes fraîches non traitées (candidates)** : premières ventes mesurées via checkout agentique UCP, toujours aucun chiffre de vente publié (P-2026-05-30-2, 2026-09-30) ; décision au fond Amazon-Perplexity 9e circuit (P-2026-06-01-v2-2, 2026-09-30) ; bloc Expert Advice AIO (P-2026-05-30-1, 2026-07-15) ; disponibilité effective des formats pub AI Mode (P-2026-05-30-5) ; extension mondiale du réglage d'exclusion IA hors UK (résout en partie P-2026-06-03-1) ; premières lectures du nouveau rapport de performance IA une fois corrigé le sur-comptage d'impressions.
- **Sources** : 4 explore ajoutées (9to5google 0.7, ppc.land 0.65, paypal-newsroom 0.6 source PRIMAIRE mais VENDEUR à traiter avec réserve, retail-systems 0.6). 9to5google est une bonne candidate au passage exploit en revue hebdo (couverture Google fiable, corroboration indépendante). Continuer 1 source neuve/édition. TOUJOURS PAS testé : Sistrix/Semrush Sensor/Mozcast (mesure de visibilité), désormais directement utile pour le bilan core update enfin mûr.
- **Méthode confirmée 2026-06-03** : sur une annonce produit Google, l'angle qui distingue ce que l'outil mesure de ce qu'il ne mesure pas, mis en regard d'une fiche de doctrine précise (`metriques-visibilite-geo` : apparition vs densité/position de citation), donne doctrine_fit 5/5 et novelty 4/5 sans forcer. Intégrer la réserve de fiabilité (sur-comptage d'impressions du 3 avril) comme caveat daté plutôt que la taire renforce la rigueur. Un rapport Google sur les fonctions IA n'est PAS un core update : il peut être info du jour sous le pilier GEO sans violer l'interdiction mono-Google, car il porte sur la mesure de la présence en réponses IA, pas sur un changement d'algorithme.

## Prédictions ouvertes ajoutées 2026-06-03

- P-2026-06-03-1 (taux d'exclusion effectif des éditeurs des fonctions IA < 15 %, nettement sous le 33,2 % d'intention déclarée du sondage SEL, 2026-12-31).
- P-2026-06-03-2 (le rapport de performance des fonctions IA de Search Console n'inclura toujours pas de donnée de clic séparée, 2026-12-31).
