# Questions de l'agent — « comment faire mieux »

Écrit par l'agent 10 (auto-interrogation) à chaque édition. Deux niveaux :
- **Urgent** : remonté à Tim tout de suite (en bas du draft).
- **Hebdo** : groupé, présenté à la revue hebdo du vendredi.

L'agent répond lui-même à ce qu'il peut tester ; il garde pour Tim ce qui demande un arbitrage humain. C'est la sortie « auto-interrogation » de [[methodes/cadrage-boucle-edition-algorithme]] ; les arbitrages tranchés repartent dans [[directives]] et, pour la doctrine, vers la couche curée (`wiki/`).

## Urgent (à trancher vite)

(vide pour l'instant)

## Run 2026-06-06-v3 — pour la revue hebdo

- **Proposition de diff doctrine, à valider Tim** : la fiche `wiki/concepts/test-substitution-llm.md` formalise un filtre 80 % sur le texte (« si un LLM peut produire 80 % de la page → ne pas la créer »). L'annonce I/O 2026 de la générative UI Google (mini-apps, calculateurs, simulations, dashboards générés à la volée) déplace la frontière du filtre : un calculateur de taux hypothécaire fonctionnel passait jusqu'ici par construction le filtre (le modèle ne pouvait pas reproduire l'interaction), or Search peut désormais le produire en direct. Diff proposé : ajouter une dimension UI générative au filtre 80 %, formulée comme « si Search peut produire 80 % de l'interaction en mini-app à la demande, on ne crée pas la page », avec trois exceptions documentées (donnée propriétaire, persistance d'état dans le compte du site, accès à des stocks/API/partenariats locaux). À valider en revue hebdo, je ne modifie pas `wiki/concepts/test-substitution-llm.md` seul (garde-fou autonomie). Article wiki à mettre à jour aussi : `wiki/concepts/product-led-seo.md` (variables qui tiennent vs familles substituables).
- **Valider 9 nouvelles sources explore** : `blogs.bing.com` (0.85, primaire Microsoft Bing) et `courtlistener` (0.85, docket fédéral primaire) sont les meilleures candidates au passage exploit en revue hebdo. `law360` (0.7) candidate si on suit d'autres dossiers juridiques agentic. `interestingengineering` (0.65), `neowin` (0.65), `e-commerce.news` (0.6), `techwyse` (0.6), `fibre2fashion` (0.6), `the-ai-corner` (0.55) sont des sources de couverture/relais corroboratifs.
- **Mesure de visibilité — directive non tenue depuis 7 éditions** : Sistrix testée v2 0606 (enfin), mais aucune 2e source de mesure de visibilité indépendante n'a été ajoutée pour le bilan core update mai (Semrush Sensor, Mozcast, Wincher, AccuRanker, AWR, Algoroo). Risque opérationnel : impossible de consolider le bilan sans 2e source. À prioriser absolument la prochaine fois.
- **GEO Measurement Study de Deepak Gupta** : étude isolée (guptadeepak.com, Security Boulevard est un repost), 50 431 citations sur 90 jours, 200 prompts, 6 moteurs. Écartée du corps faute de 2e source indépendante avec historique (règle dure explore). Quand une 2e source reprendra le chiffre avec sa propre mesure, la piste devient publiable. À vigiler.
- **Claim Seer Interactive AI Mode embarque calculateurs/simulations** : lu dans un résumé (nobori.ai) qui attribue à Seer une formulation « AI Mode is no longer a static list of links, but a synthesised answer that mixes citations, direct links and, where relevant, interactive experiences (calculators, comparators, simulations generated on the fly) ». Vérification Seer primaire requise. Si confirmé, c'est une jonction forte entre Seer et l'annonce Antigravity. Si non confirmé, claim à laisser hors corps. Action : ouvrir directement seerinteractive.com et le rapport AI Mode pour vérification au prochain run local.

## Run 2026-06-02-v2 — pour la revue hebdo

- **1 source sous le seuil, laissée hors registre** : `fourweekmba` (trust 0.55, analyse « protocol wars »). Elle a porté l'interprétation « les marchands supporteront plusieurs standards », attribuée dans le corps, mais c'est une analyse d'opinion sans donnée primaire et sous le seuil d'auto-ajout (0.6). Laissée hors `sources.jsonl`. L'ajouter en explore comme source d'analyse, ou la garder hors registre ? Vigilance : son texte emploie un langage métaphorique abondant (vocabulaire de course, de murs, de rails), à ne jamais reprendre dans la rédaction.
- **Valider 6 nouvelles sources explore** : `google-cloud-blog` (0.88, primaire AP2) et `openai-blog` (0.85, primaire ACP) sont des sources primaires fortes, candidates au passage exploit ; `shopify-blog` (0.65, vendeur, mécanique catalogue utile mais chiffres self-report à traiter comme direction) ; `pymnts` (0.66, enquête acquéreurs) ; `digitalcommerce360` (0.66) et `mediapost` (0.6) sur le litige Amazon-Perplexity. Toutes corroborées. À confirmer/retirer.
- **Limite de doctrine comblée** : la fiche `agentic-search` note que l'agent qui *agit* (achat) reste mal couvert empiriquement. Cette édition apporte des faits sur ce cas (couche découverte de l'achat agentique). Faut-il enrichir `wiki/concepts/agentic-search.md` d'une section « commerce agentique : couche découverte » reliant flux structuré, attributs Merchant Center et coexistence des standards UCP/ACP/AP2 ? Proposition pour la revue hebdo (je ne modifie pas le wiki doctrine seul).
- **Périmètre payments vs search** : où poser la frontière quand un sujet de découverte agentique a une couche paiement attachée (AP2, x402, Visa TAP) ? J'ai traité la couche paiement comme contexte technique et écarté la partie crypto/réseaux de cartes comme hors périmètre. Confirmer cette ligne pour les prochaines éditions commerce agentique.

## Run 2026-06-01 — pour la revue hebdo

- **Contradiction dans la mémoire à trancher** : `memory/wording_rules.md` cite encore le skill `ton-de-voix-tim` (lignes 3 et 9 : « source = skill ton-de-voix-tim », « tutoiement, positions tranchées ») alors que `memory/voix-synthetic.md` et le SKILL imposent la voix propre de SyntheticBrain (vouvoiement, pas de personnage, ne PAS appeler `ton-de-voix-tim`). J'ai suivi `voix-synthetic.md` (qui fait foi). **Diff de skill proposé** : mettre à jour `wording_rules.md` pour retirer la référence à `ton-de-voix-tim` et au tutoiement, et pointer vers `voix-synthetic.md`. À valider en revue hebdo (je ne modifie pas le fichier seul, garde-fou autonomie).
- **2 sources sous le seuil d'auto-ajout, laissées en attente** : `pikaseo` (trust 0.58, a porté le chiffre YouTube ~16% vs Reddit ~10%, direction corroborée par CMSWire/Conductor mais figure exacte mono-origine) et `premiere.page` (trust 0.55, remontées sectorielles préliminaires FR). Les ajouter en explore ou les laisser hors registre ? Arbitrage de seuil.
- **Valider 4 nouvelles sources explore** : `abondance` (0.7, source FR de référence, candidate forte au passage exploit), `digitalapplied` (0.6), `cmswire` (0.62, relais Conductor), `searchlab` (0.6, agrégateur parts de marché). Toutes corroborées. À confirmer/retirer.
- **Claim préliminaire dans le corps** : les remontées sectorielles FR (finance, santé, e-commerce, SaaS, services locaux) sur le core update ont été gardées dans l'info du jour mais marquées explicitement comme non stabilisées (déploiement en cours, échantillon faible, sources FR peu indépendantes entre elles). Bon réflexe de transparence, ou fallait-il les écarter complètement du corps ? Arbitrage de seuil cohérent avec celui du 11 % (Averi) en v5.
- **Cadence / référence du jour** : première édition depuis les 5 versions du 30 mai. Toujours pas clarifié quelle édition fait référence pour une journée donnée (question ouverte depuis v4/v5).

## Run v5 (2026-05-30) — pour la revue hebdo

- **Cinquième édition le même jour.** v5 (publicité payante dans AI Mode / GML) produite après v2/v3/v4. Question de cadence et de versionnage toujours ouverte (voir run v4). Confirmer si une édition fait référence pour la journée.
- **Frontière sujet pub vs commerce agentique** : v5 traite la publicité payante dans la réponse (formats Gemini étiquetés Sponsored, GML 20 mai), distincte du checkout agentique organique de v3 (UCP/Universal Cart). J'ai jugé la distinction suffisante pour ne pas être une redite. À confirmer.
- **FAQ rich results dépréciés** sourcé sur une seule source (doc officielle Google Search Central, citation textuelle). J'ai considéré qu'une doc officielle de l'éditeur lui-même n'exige pas de recoupement à 2 sources indépendantes. Valider cette règle : doc primaire officielle de l'éditeur = recoupement non requis ?
- **Valider 3 nouvelles sources explore** : `ahrefs` (0.8, études quantitatives primaires, candidate forte au passage exploit), `averi` (0.62, étude 680M citations), `tryprofound` (0.6, profils de citation par moteur). Toutes corroborées. À confirmer/retirer.
- **Chiffre 11 % (Averi)** publié comme mono-étude flaguée, direction seule recoupée (Profound + Semrush). Bon réflexe ou fallait-il l'écarter complètement du corps faute de 2e source chiffrée indépendante ? Arbitrage de seuil.

## Run v4 (2026-05-30) — pour la revue hebdo

- **Trois éditions le même jour, est-ce voulu ?** v2 (Information Agents), v3 (Universal Cart), v4 (llms.txt) ont été produites le 2026-05-30. La cadence prévue est 2/jour en semaine. Confirmer la politique de versionnage et si une de ces éditions fait référence.
- **Overlap llms.txt / guide 15 mai** : l'info du jour v4 recoupe partiellement le sujet du run cloud. J'ai publié avec un hook et du matériel distincts mais baissé le novelty_score à 3. Arbitrage : était-ce le bon choix, ou aurait-il fallu basculer sur le redesign du champ de recherche (sujet plus vierge) ? Voir mistake M-004.
- **Valider 2 nouvelles sources explore** : `theseocommunity` (0.6) et `getpassionfruit` (0.6), toutes deux corroborées sur le dossier llms.txt. À confirmer en `exploit` ou retirer.
- **Sources tech généralistes mobilisées en brève** : Tom's Guide, VentureBeat, TechRadar utilisées comme corroboration secondaire (champ de recherche, parts Gemini). Non ajoutées au registre (hors spécialité SEO/search). À trancher : les garde-t-on hors registre comme corroboration ponctuelle uniquement ?

## Pour la revue hebdo

- **Rubrique fixe ?** Faut-il une section récurrente « ce qu'un agent retiendrait de cette édition » pour forcer l'angle citation à chaque numéro ?
- **Format de l'édition de l'après-midi ?** Avec 2 éditions/jour, est-ce que celle de 16h doit passer en format court (une seule info) pour ne pas cannibaliser celle du matin ?
- **Valider les 3 sources auto-ajoutées (v3) ?** `cloudflare-radar` (0.85, données primaires crawl), `similarweb-geo` (0.78), `seer-interactive` (0.75). Toutes corroborées et au-dessus du seuil. Je les garde en `explore` → à confirmer en `exploit` ou à retirer.
- **Sources mises en attente (sous le seuil / mono)** : Conductor, TechnologyChecker, ALM Corp, vertu, InfoQ. Apparues une fois, autorité moyenne ou agrégateurs. Je ne les ajoute pas en autonomie. À trancher : en intègre-t-on certaines (InfoQ semble sérieux) ?
- **Diff de skill proposé ?** Aucun pour l'instant. Quand un pattern de titraille reviendra gagnant 3 fois, je proposerai ici un diff de `ton-de-voix-tim` à valider. Piste émergente : un garde-fou explicite « vérifier date primaire » dans le socle `revue-presse-quotidienne` (le piège fraîcheur s'est représenté ce run). À formaliser en diff si ça revient une 3e fois.

## Ce qui aurait rendu cette édition (v3) meilleure

- Un chiffre de conversion du trafic IA daté de 2026 et vérifié sur primaire (au lieu de Seer 2025) aurait renforcé la brève conversion. Les données 2026 existent (Similarweb) mais je n'ai pas confirmé le primaire faute de budget de fetch. À refaire proprement quand le sujet revient.
- Un retour terrain FR (un e-commerçant français face à UCP) aurait ancré l'info du jour côté lecteur. Aucune source FR fraîche trouvée sur UCP côté marchand. Candidat veille Abondance.

## À tester par l'agent lui-même (passe en directives.md)

- Tester 1 source neuve par édition (fait au run d'amorçage avec Lumar).

## Sources découvertes en autonomie (journal)

- **2026-05-30** : `lumar` (lumar.io, industry news SEO/IA) ajoutée en statut `explore`, trust 0.62. Corroborée par blog.google et SEJ sur I/O 2026, donc au-dessus du seuil d'auto-ajout (0.6 + corroboration). À confirmer ou retirer en revue hebdo.
- **2026-05-30 (v3)** : `cloudflare-radar` (blog.cloudflare.com / Radar) ajoutée en `explore`, trust 0.85, données primaires crawl-to-refer corroborées par TechnologyChecker + SEOmator. `similarweb-geo` (similarweb.com/blog/marketing/geo) en `explore`, trust 0.78, clickstream. `seer-interactive` (seerinteractive.com/insights) en `explore`, trust 0.75, études conversion. Les trois au-dessus du seuil d'auto-ajout (0.6 + corroboration). À confirmer/retirer en revue hebdo. Note vigilance fraîcheur enregistrée dans le registre pour Seer et Cloudflare (agrégateurs qui redatent en 2026 des études 2025).

- **2026-05-30 (v4)** : `theseocommunity` (theseocommunity.com) ajoutée en `explore`, trust 0.6 ; a porté l'étude SE Ranking (39 000 domaines), la citation Mueller et l'incident d'apparition du fichier. `getpassionfruit` (getpassionfruit.com) ajoutée en `explore`, trust 0.6 ; guidance llms.txt 2026 détaillée. Les deux corroborées par Search Engine Land sur la position de Google. À confirmer/retirer en revue hebdo.

- **2026-05-30 (v5)** : `ahrefs` (ahrefs.com/blog) ajoutée en `explore`, trust 0.8 ; étude quantitative primaire sur les citations AI Overviews vs top-10 organique (863k SERP, 4M URL), corroborée par SEJ. Source SEO de référence, candidate forte au passage `exploit`. `averi` (averi.ai) ajoutée en `explore`, trust 0.62 ; étude 680M citations (11 % recouvrement ChatGPT/Perplexity), chiffre mono-étude, direction corroborée par `tryprofound`. `tryprofound` (tryprofound.com) ajoutée en `explore`, trust 0.6 ; profils de citation par moteur. Les trois à confirmer/retirer en revue hebdo.

- **2026-06-01 (v2)** : 5 sources ajoutées en `explore`, toutes corroborées au seuil. `emarketer` (emarketer.com, trust 0.72 ; faits e-commerce, blocage Amazon des crawlers OpenAI, corroborée par Decrypt). `martech` (martech.org, trust 0.7 ; analyse machine-readable brands, corroborée par commercetools + Cloudflare). `yext` (yext.com/blog, trust 0.65 ; étude 6,8M citations, donnée vendeur, corroborée par SEL mais CONTREDITE par 5W/Muck Rack, traiter ses chiffres comme dépendants de la méthodo). `decrypt` (decrypt.co, trust 0.62 ; affaire Amazon-Perplexity, corroborée par CNBC/Yahoo). `cyberscoop` (cyberscoop.com, trust 0.6 ; sursis d'appel 9e circuit, corroborée par PYMNTS). **emarketer et martech sont des sources de référence, candidates fortes au passage `exploit`.** Laissées en attente sous le seuil ou wire/vendeur : pymnts (0.58), commercetools (0.58, blog vendeur), metarouter (0.55, vendeur), prnewswire-5w + morningstar (0.55, communiqué/relais), semrush (0.6, déjà utilisé en corroboration), cnbc + yahoo-finance (0.7, presse générale fiable mais non SEO/search-spécialisée). À arbitrer en revue hebdo.

- **2026-06-01 (v3)** : 2 sources ajoutées en `explore`, corroborées au seuil. `lilyraynyc` (lilyraynyc.substack.com, trust 0.78 ; analyste SEO de référence ; étude 13 mai 2026 sur 220+ sites de contenu IA, données Ahrefs+Sistrix ; chiffres mono-étude sur échantillon auto-déclaré, attribués comme tels, direction corroborée par Glenn Gabe + doctrine interne). `almcorp` (almcorp.com, trust 0.6 ; retrait FAQ rich results début mai, corroborée par Search Engine Roundtable). **lilyraynyc et digitalapplied (déjà 3 hits utiles) sont des candidates fortes au passage `exploit`.** Laissées en attente sous le seuil : `letsdatascience` (0.55, site de synthèse, pas une source de données primaire), `ziptie` (0.5, guide conseil du « camp fraîcheur », utilisé seulement comme contre-exemple dans la brève GEO). À arbitrer en revue hebdo.

## Propositions doctrine (à valider en revue hebdo, non appliquées)

- **Signal pour `wiki/concepts/structural-information-geo.md` et `wiki/concepts/aeo.md` (v4)** : la position publique de Google (llms.txt non utilisé, AI surfaces sur le même index, SEO normal suffit) converge avec le finding SAGEO Arena (le levier au retrieval = champs structurels + schema, pas le body ni un fichier dédié). Candidat : ajouter une ligne « confirmé par la position officielle de Google sur llms.txt (Illyes 2025, guide 2026) » dans la section preuve de `structural-information-geo`. À valider.

- **Hypothèse candidate pour `wiki/hypotheses.md`** : « Avec le commerce agentique (UCP/Universal Cart), la qualité du flux produit structuré (attributs, prix, dispo, Conversational Attributes Merchant Center) devient un facteur de sélection plus fort que le contenu éditorial de la page pour les requêtes transactionnelles. » Prolonge `mots-cles-actionnels` et `agentic-search`. À tester quand des données de sélection d'agent seront publiques. Lié à la prédiction P-2026-05-30-2.
- **Signal pour `wiki/concepts/agentic-search.md`** : l'actu UCP conforte le concept (« être sélectionné par l'agent pour accomplir une tâche ») et le précise côté ACHAT (l'agent ne fait plus que lire/comparer, il transige). Candidat ajout d'une section « agent qui achète » au concept, à valider.
- **Signal pour `wiki/concepts/agentic-search.md` (v2, 2026-06-01)** : la fiche pose explicitement comme limite que « l'agentic search au sens strict (agent qui agit, pas juste génère une réponse) reste mal couvert empiriquement ». L'actu de printemps 2026 apporte du matériel empirique sur cette limite : (1) la jurisprudence Amazon-Perplexity (injonction 9 mars, sursis d'appel 17 mars) qui tranche que la permission de l'utilisateur ne vaut pas autorisation de la plateforme ; (2) le blocage `robots.txt` des robots OpenAI par Amazon (nov 2025) ; (3) le « Agent Readiness score » de Cloudflare (17 avr 2026, 200k domaines : 4 % seulement déclarent une préférence d'agents). **Candidat : ajouter à la fiche une section « accès et lisibilité : ce que l'empirie 2026 montre » avec ces faits, et lever partiellement la limite déclarée.** À valider en revue hebdo (je ne touche pas à la doctrine seul).

- **Signal pour `wiki/concepts/programmatique-pseo.md` et `wiki/concepts/data-proprietaire.md` (v3, 2026-06-01)** : l'étude Lily Ray du 13 mai 2026 (220+ sites de contenu IA : 54 % perdent ≥30 % de leur pic, 22 % ≥75 %, motif « Mount AI ») est une mesure empirique externe, à large échantillon, qui conforte la limite déjà déclarée de `programmatique-pseo` (« sans dataset propriétaire, le pSEO produit du contenu thin »). **Candidat : ajouter cette étude comme source de preuve externe dans la section preuve/limites, en complément de la source interne 2026-04-22 (−40 à −80 % sur sites IA industrialisés).** Elle renforce la prémisse côté risque de H-007 sans la valider (le jalon J+30 ~15 juin reste l'arbitre terrain). À valider en revue hebdo (je ne touche pas à la doctrine seul).
- **Désaccord à tracer pour `wiki/concepts/metriques-visibilite-geo.md`** : deux études 2026 divergent sur la fraîcheur comme facteur de citation en AI Overviews. Camp « la fraîcheur compte » (analyses type Ahrefs 17M, ~76 % des top-cités < 30 j) vs étude contrôlée Digital Applied (26 avr 2026, 4243 URL citées, ~50k témoins : médiane 14 mois, pas de corrélation récence/citation après contrôle de l'autorité de domaine, hors intention actualité). **Candidat : ouvrir une ligne de contradiction dans `wiki/contradictions` ou la fiche métriques GEO, hypothèse de résolution = effet fraîcheur confondu avec l'autorité de domaine.** À valider.

## Sous-skills créés en autonomie (journal)

Toute skill créée ou modifiée par l'agent est tracée ici, avec le commit git correspondant.

(vide pour l'instant)

---

## Run 2026-06-02 — sources découvertes et points pour la revue hebdo

- **Nouvelle source explore ajoutée** : `airops` (https://www.airops.com/report, trust 0.7). Rapports data primaires sur le search IA (étude 548 534 pages récupérées / 15 000 requêtes ChatGPT, 15 % citées). Portée dans le corps par Search Engine Land (connue) + Passionfruit. À confirmer/passer exploit en revue hebdo.
- **Candidate au passage exploit** : `getpassionfruit` atteint 3 hits utiles (synthèse GEO de 25+ études en avril 2026, en plus de la guidance llms.txt). Bonne source de synthèse, à arbitrer.
- **Sources mentionnées via synthèse, non ajoutées au registre** (citées par Passionfruit, non consultées en direct) : SparkToro (non-reproductibilité des classements de citation), Profound (instabilité temporelle ; déjà au registre comme tryprofound). Si une de ces études devient centrale dans une future édition, consulter la source primaire avant de la créditer.
- **Divergence non résolue** : l'affiliation des auteurs du preprint arXiv:2603.09296 est rapportée différemment selon les sources (Stanford vs Virginia Tech). Non assertée dans le corps. À ne pas reprendre sans vérification de la source primaire.
- **Commit du run** : `SyntheticBrain — édition 2026-06-02 + apprentissage (auto)`.

## Questions / propositions — 2026-06-03 (revue hebdo)

- **Interprétation « mono-Google » à confirmer (non bloquant).** Cette édition a pris en info du jour une fonction produit Google (rapport de performance des fonctions IA + réglage d'exclusion dans Search Console), sous le pilier GEO/search IA. J'ai jugé que l'interdiction mono-Google vise les core updates et updates d'algorithme, pas une fonctionnalité de mesure/contrôle de la présence en réponses IA, qui touche directement le sujet « comment on mesure d'être cité dans un moteur ». À valider : cette lecture est-elle conforme à ton intention, ou un produit Google doit-il aussi rester en brève ?
- **Directive non tenue depuis 5 éditions.** « Tester une source de mesure de visibilité (Sistrix / Semrush Sensor / Mozcast) » est répétée depuis le 30 mai et toujours pas exécutée. Proposition : la transformer en exigence dure du skill (au moins 1 source de mesure de visibilité consultée quand un core update est en fenêtre de bilan). Diff de skill à valider — je ne touche pas au prompt sans accord.
- **Sources vendeur-PR.** `paypal-newsroom` ajoutée en explore à 0.6, marquée source PRIMAIRE mais VENDEUR. Proposition de règle : une source de type communiqué d'entreprise ne peut jamais porter seule un claim du corps (déjà couvert par la règle dure explore + recoupement), et son trust est plafonné à 0.6 tant qu'elle n'a pas d'historique de corroboration. À valider.


## Questions / propositions — 2026-06-06 (revue hebdo)

- **Arbitrage info du jour (non bloquant).** Cette édition met Web Bot Auth (technique/infra/protocole) en info du jour, une famille que tu sous-notes en Brèves. Je l'ai gardée pour sa nouveauté réelle (fait franchement neuf, angle agentique distinct), mais le même run contenait un angle plus dans ton goût : le signal de marché DuckDuckGo + l'aveu Microsoft (bascule entre moteurs + contre-vérité mesurée). Veux-tu que la règle par défaut soit : quand un signal de marché aligné sur ton goût coexiste avec une piste infra, le signal de marché passe en info du jour et l'infra en brève ? Si oui, je l'inscris en directive dure.
- **Branchement YouTube réussi (1er run).** La source `youtube-veille` (mode découverte) a bien surfacé des pistes fraîches, toutes recoupées en primaire. Elle reste `découverte`, jamais `exploit`, et n'a porté aucun claim seule. Le garde-fou tient. RAS sauf si tu veux ajuster les requêtes par défaut de la veille élargie.
- **Réorganisation des éditions (demande Tim 2026-06-06).** Tu m'as demandé de regrouper les éditions dans un sous-dossier `revuedepressIA/revuedepress/`. Fait. Conséquence : la constante du skill agent-synthetic pointe encore vers `revuedepressIA/{date}-revue-presse.md` (racine). Je ne touche pas au prompt du skill sans ton accord (garde-fou). **Diff proposé** : changer la constante de sortie en `revuedepressIA/revuedepress/{YYYY-MM-DD}-revue-presse.md`. Valides-tu ?
- **Sources explore à arbitrer** : cloudflare-blog (0.85, primaire infra indépendant de Google) est une bonne candidate au passage exploit. ietf-datatracker (0.8) utile pour distinguer standard ouvert vs propriétaire. apptopia/variety à confirmer selon récurrence.

## Run 2026-06-06-v2 — pour la revue hebdo

- **P-2026-05-30-5 partiellement résolue.** Ouverture publicitaire AI Mode à la santé (US, anglais, restrictions de création) répond à « au moins un format pub AI Mode accessible aux annonceurs aux US d'ici fin 2026 ». Statut à trancher : (a) `resolved-partial` parce que c'est un test limité, ou (b) maintenir `open` jusqu'à généralisation hors test ? Recommandation agent : `resolved-partial`, en gardant l'œil sur P-2026-06-06-v2-1 (extension hors US/anglais ou ouverture d'une autre verticale sensible).
- **Concept doctrine à proposer.** Une fiche concept dédiée à la « pression publicitaire sur la surface IA et conséquences pour le rang organique cité » manque. Le doctrine_fit du run est tombé à 4/5 parce qu'aucune fiche n'attaque frontalement ce sujet (concepts/aeo et entities/google-ai-mode couvrent la présence en réponse IA, pas la cohabitation organique/payant dans la même surface). Tim, valides-tu la création de ce concept ? Si oui, qui le rédige (skill seo-workflow-article si article long, ou simple fiche concept) ?
- **SISTRIX promue exploit ?** Premier hit utile après 6 directives où l'ingestion d'une source de mesure de visibilité était demandée. Le bilan du core update de mai sera consolidé après le 9-11 juin. Si la qualité du signal SISTRIX se confirme sur ce bilan, je propose le passage exploit à la revue hebdo. Ok pour cette procédure ?
- **Éviter le mono-Google d'édition.** Ce run contient 3 sujets Google (info du jour AI Mode santé, brève core update, brève spam policies). Compensé par 1 brève non-Google (Cloudflare bots > humains). Faut-il durcir la règle (max 2 sujets Google par édition) ou laisser au cas par cas ? Recommandation agent : règle souple, signaler dans le log de run si ratio > 75 %.
- **Famille Tim aimée vs technique/infra.** L'info du jour de v1 (Web Bot Auth) était dans la famille technique sous-pondérée. Celle de v2 (ouverture pub santé AI Mode) est dans la famille aimée (bascule de marché publicitaire). Sur une journée à deux éditions, faire diverger les piliers a évité la saturation. À garder comme règle implicite ?

## Audit Agentic Design Patterns (2026-06-07) — propositions hors run

> Source : audit du livre *Agentic Design Patterns* (A. Gulli) + repo `atlas-agents`, demandé par Tim. Écrit par Claude hors run, pas par l'agent 10. Trois patterns évalués (Evaluation, Exception Handling, Resource-Aware) ; seul le premier a été implémenté (additif, non cassant), les deux autres sont proposés ici car ils touchent le prompt figé.

- **DÉJÀ FAIT (non cassant, additif) — `eval_health.py`.** Nouvel outil à la racine `agent-synthetic/`, LECTURE SEULE sur `ledgers/`, écrit uniquement dans `derived/eval_health.{json,md}` (vues régénérables, validées par `validate.sh`). Détecte la dérive que `calibration.md` ne voit pas : tendance `note_globale`, confiance moyenne des claims, prédictions en retard, lignes JSONL cassées → statut OK/WATCH/ESCALATE. Premier passage : **WATCH** (confiance moyenne des claims récents 0,653 < seuil 0,70). Limite connue : `note_globale` n'est loggé que sur 3 runs/14 (le reste vit dans `calibration.md` en markdown) — à terme, logguer `note_globale` systématiquement dans `runs.jsonl` rendrait la dérive bien plus fiable. Ne touche ni au skill ni aux ledgers.

- **DIFF SKILL PROPOSÉ (ch.12 Exception Handling) — câbler l'escalade.** À la clôture du run (ou agent 7), lancer `./eval_health.py` ; si `status == ESCALATE`, le draft passe en review humaine obligatoire (mention en tête du draft + entrée dans la section « Urgent » ci-dessus), pas d'auto-commit tant que non levé. Seuils dans `eval_health.py`. Bénéfice : le système te remet dans la boucle exactement quand la qualité décroche, au lieu de continuer à produire. À valider — je ne touche pas au prompt sans accord.

- **DIFF SKILL PROPOSÉ (ch.16 Resource-Aware) — router de modèle.** Quand l'agent 1 (veille) et l'agent 4 (fact-check) parallélisent via sous-agents Task, router les sous-tâches de commodité (scan exploit, dédup contre `said_index`, formatage) sur **Haiku**, et garder **Opus** pour le verdict du fact-check (agent 4) et la calibration (agent 9). Le classifieur de routing lui-même tourne sur Haiku. N'affecte pas le modèle de la session principale ; gain de coût sans perte sur le jugement. Pattern d'implémentation pillable : `atlas-agents/ch07_model_portability/online/model_router.py` (fallback + circuit breaker, ~130 lignes). À valider.

- **DIFF SKILL PROPOSÉ (ch.19 Evaluation) — logger `note_globale` en numérique dans `runs.jsonl`.** Aujourd'hui la note vit surtout dans `calibration.md` (markdown) ; `eval_health.py` ne la lit que sur 3 runs/14, donc la détection de dérive est partielle. Ajouter à l'agent 9 : écrire `note_globale` (float) dans la ligne `runs.jsonl` du run, systématiquement. Une ligne de plus, et la dérive devient fiable. Couplé : `eval_health.py` v2 ajoute déjà un rapport de complétude de schéma (advisory) — il a détecté 12 claims et 2 prédictions sans champ `claim` propre, à vérifier (lignes de calibration/meta ?). À valider.

- **NOMMAGE (consigne Tim).** La future couche « le système apprend sur Tim et son travail » s'appelle **`syntheticmemory`**. Ne jamais l'appeler « tim brain » ni « second cerveau ». La brique d'implémentation candidate : `atlas-agents/ch11_memory/memory_agent.py` (extraction auto de mémoires par un petit modèle, séparant préférence/fait) — garder la logique, brancher sur les JSONL, jeter ChromaDB.

## Questions ouvertes après 2026-06-08-v2

- **Doctrine [[concepts/product-led-seo]] — distinction stricte vs large à formaliser.** L'étude Averi du 8 juin 2026 a fait ressortir un angle doctrinal précis : la fiche actuelle laisse implicite le statut des pages-marketing produit (comparatifs « alternatives à X », pages de témoignages, pages de cas clients) qui sont également présentées comme « product-led » dans la pratique marketing mais ne tiennent pas le test de substitution LLM. Proposition à valider en revue hebdo : ajouter au § « Principe » de la fiche une distinction explicite entre **pages-fonctionnalité** (interactives, défendables, calculateur/simulateur/configurateur/comparateur côte-à-côte avec données temps réel/générateur) et **pages-marketing produit** (comparatifs éditoriaux, témoignages, listes de cas clients, /customers), avec mention que seules les premières sont défendables face aux AI Overviews selon les mesures disponibles. Le filtre 80 % du [[concepts/test-substitution-llm]] s'applique aux deux mais avec des verdicts opposés.

- **Concept candidat : composition des sources contestées dans les moteurs IA.** Soulevé à plusieurs reprises (CNN-Perplexity v1, Amazon-Perplexity, News/Media Alliance amicus). Pas de fiche dédiée à ce jour. Proposition : créer `wiki/concepts/composition-sources-contestees.md` qui décrit le mécanisme : un éditeur peut bloquer techniquement un moteur IA, contester juridiquement la composition de ses sources (CFAA, copyright, publicité mensongère), et obtenir un retrait partiel ou complet. Lien avec [[concepts/agentic-search]] et [[concepts/data-proprietaire]]. À valider en revue hebdo.

- **Concept candidat : MCP comme couche verticale d'éditeurs de données dans les moteurs génératifs.** Le lancement Semrush MCP Perplexity du 3 juin 2026 est un cas concret d'intégration verticale qui mérite une fiche distincte (différente du commerce agentique UCP/ACP/AP2). Proposition : `wiki/concepts/mcp-vertical-integration.md` qui distingue : (1) MCP de données structurées (Semrush, Ahrefs si elle suit), (2) MCP de paiement (Mastercard Agent Pay), (3) MCP d'action (Comet, agents shopping). Lien avec [[concepts/agentic-search]] qui généralise.

## Questions / observations 2026-06-10

- **Doctrine candidate** : étendre [[concepts/agentic-search]] pour formaliser la 3e route de sélection par défaut sur intention (application embarquée via MCP sur ChatGPT, Universal Cart côté Google, App Intents côté Apple-Siri-Gemini). À soumettre à la revue hebdo. La fiche actuelle couvre la sélection par signal de citation et par mémoire neuronale/persistante, mais pas la sélection contractuelle plateforme-partenaire.
- **Doctrine candidate** : étendre [[concepts/product-led-seo]] pour distinguer PLS web ouvert (concurrence avec la générative UI Search, déjà documenté 0606-v3) vs PLS embarqué (application MCP dans ChatGPT, Action dans Apple-Siri-Gemini, Universal Cart côté Google). À soumettre à la revue hebdo.
- **Doctrine candidate** : ajouter à [[concepts/metriques-visibilite-geo]] un 4e levier visuel (position du favicon dans la carte de citations) si Google généralise le test repéré par Brodie Clark. À attendre que le test passe en déploiement avant de toucher la fiche.
- **Source à revoir** : techtimes a maintenant 2 hits utiles (Apple WWDC 0609 single-source chiffres techniques + Aria ChatGPT 0610 single-source target date). À traiter avec prudence systématique : les détails techniques ou les dates précises non corroborées par d'autres sources doivent être marquées uncertain.
- **Donnée à confirmer** : la date précise « cible 9 juin » du déploiement Aria (TechTimes single-source) reste uncertain dans le corps. Si OpenAI confirme officiellement, mettre à jour la confiance du claim C-2026-06-10-3.
- **Sources primaires bloquées en cloud** : openai.com et seroundtable.com retournent 403 Forbidden côté WebFetch ce run. Travail effectué via les reprises de presse (SEL, Optimixed). À surveiller : si la fréquence augmente, prévoir un protocole de contournement (cache, MCP fetch) ou marquer plus de claims comme uncertain.

## Questions remontées au run 2026-06-11

### Question doctrine — fiche dédiée au double opt-out côté éditeur ?

L'info du jour 2026-06-11 (mise à jour documentation Applebot Apple) met en relief un mécanisme à deux étages côté publisher : (a) bloquer l'usage d'une page comme contexte de génération de réponse (Apple : `nosnippet` ; Google : `nosnippet` ; OpenAI : équivalent), (b) bloquer l'usage des contenus dans l'entraînement des modèles fondation (Apple : `Applebot-Extended` dans robots.txt ; Google : `Google-Extended` ; OpenAI : `GPTBot` disallow). Ces deux leviers existent éparse depuis 2023-2024 mais sont rarement traités comme un objet doctrine cohérent.

Proposition : créer une fiche `wiki/concepts/double-opt-out-editeur-ia.md` qui consolide :
- le mapping moteur de réponse / training-only opt-out / context-only opt-out
- le périmètre de chaque levier (page vs site)
- la question de la rétroactivité (les pages déjà ingérées sont-elles exclues ?)
- la question ouverte du routage cross-moteur (Siri AI vers Gemini : qui gouverne ?)

Question pour Tim en revue hebdo : valider la création de la fiche, ou la considérer prématurée tant que le routage cross-moteur n'est pas tranché par Apple/Google.

### Question méthode — fiche preuve interne pour le double opt-out

Si une fiche concept est créée, la suivre par une fiche preuve `wiki/preuves/` qui mesure sur le périmètre d'un client : pages avec `nosnippet`, pages avec `Disallow: Applebot-Extended`, conséquence mesurée sur la part de citation Apple Search et Siri AI (impressions, clics). Demande à Tim : la doctrine accepte-t-elle de réserver une fiche preuve à un site test avant qu'un client réel ne l'expérimente ?

### Question source — `simonwillison` candidat exploit en revue hebdo

Simon Willison a été ajouté en explore le 10 juin sur Claude Fable 5 (trust initial 0.85). Référence reconnue sur la revue technique des modèles LLM. La source n'a pas servi ce run mais reste à surveiller. Proposition : si un 2e hit utile sort dans les 10 prochains jours, promotion exploit.

### Question source — `theblock` candidat exploit en revue hebdo

The Block a été ajouté en explore le 10 juin sur Mastercard AP4M (trust initial 0.75). Référence sur les paiements crypto. À surveiller, promotion exploit si 2e hit utile sort dans le périmètre payments-search.

### Question sujet — Google reviews replies rejection study

Étude tierce publiée 4-5 juin (12 752 réponses rejetées, 92.6% sur 5-star reviews, sharp increase à partir de 2024). Le sujet est local SEO pertinent mais hors fil narratif des dernières éditions. Question pour Tim : doit-on créer une brève dédiée si une 2e étude tierce confirme le motif sur un autre périmètre, ou le sujet est-il systématiquement écarté ?

### Question process — résolution de prédiction en mode partial vs full

P-2026-06-06-v2-2 est passée de `resolved-partial` (8 juin) à `resolved` (11 juin) en 3 jours, sans intervention humaine. Le passage a été décidé par l'agent sur la base de 3 indicateurs concordants. Question pour Tim : valider que ce passage automatique full est acceptable, ou imposer un passage manuel pour toute résolution full d'une prédiction écrite par Tim.

## Questions au revue hebdo (écrit après 2026-06-12)

- **Sources candidates au passage exploit** : courthousenews.com (1 hit utile primaire reportage en salle 9e Circuit, source de référence couverture appellate fédérale, à valider exploit dès le 2e hit similaire) et heise.de (1 hit utile primaire presse tech allemande sur décision Munich AI Overviews, à valider exploit en revue hebdo).
- **Concept candidat à créer (proposition non autonome)** : `responsabilite-editoriale-ai-overview` (ou similaire), pour formaliser la couche juridique de qualification du contenu généré comme « énoncé propre » du moteur, distincte de la simple agrégation de résultats. Connecté à `metriques-visibilite-geo` (la mesure GEO va devoir intégrer la dimension responsabilité juridique). Question à Tim : créer ce concept en autonome cette semaine ou attendre une 2e décision européenne pour consolider ?
- **Concept candidat à créer (proposition non autonome)** : `cadre-juridique-acces-agent` (ou similaire), pour formaliser la « 3e route d'accès » (agent qui agit pour utilisateur loggué) distincte de la 1re (indexation crawler) et de la 2e (lecture par crawler IA). Connecté à `agentic-search` qui note la limite empirique sur les agents qui agissent. Question à Tim : créer cette fiche après l'arrêt 9e Circuit (60j-30 sep) ou en autonome cette semaine pour préparer le terrain ?
- **Méthodologie mesure GEO** : la critique méthodologique sur Brand Radar (snapshot statique vs régénération continue) est-elle suffisamment robuste pour devenir une règle d'évaluation des outils GEO dans la KB ? Si oui, ajouter à `metriques-visibilite-geo` une section « fiabilité opérationnelle » qui distingue les outils ayant publié leur méthode d'échantillonnage.
- **Distinction Visa-OpenAI vs Mastercard AP4M** : conserver les deux annonces du 10 juin comme « jour pivot infrastructure agentic commerce » dans une fiche dédiée (par exemple `infra-paiement-agentic-juin-2026`), ou laisser dans les seules brèves d'édition ? Avis Tim.

## Questions ouvertes — 2026-06-12-v2

- **Confirmation auteur The Atlantic « Sloptimized »** : le claim repose sur 3 reprises convergentes (kottke.org, Lemmy, SE Roundtable) mais l'accès direct theatlantic.com a échoué (paywall) et l'auteur précis n'a pas été confirmé. Si Tim a un abonnement The Atlantic, vérification rapide souhaitable pour citer auteur + date exacte de publication + chiffre Shopify (60 listicles vs « au moins 60 »).
- **Source FR primaire produit Google** : 8 rappels successifs pour tester Abondance, Webmarketing-com, JDN Solutions sur annonce produit Google. À programmer pour une édition Actualité SEO future si occasion fraîche.
- **Outils GEO et métrique auto-citation marque** : aucune publication outillage n'expose à ce stade un indicateur dédié à l'identification des classements auto-publiés. P-2026-06-12-v2-3 surveille. Pourrait être un sujet brève GEO d'ici fin 2026 si Profound, Otterly, Peec, Ahrefs Brand Radar ou Promptmonitor publient une telle métrique.

## Questions à Tim, écrit après 2026-06-13

- Souhaite-tu que la fiche `agentic-search` soit étendue pour intégrer explicitement la couche enterprise IT (Microsoft Agent 365 + Defender context mapping + Agent Registry détection MCP servers) en tant que nouveau levier d'identification côté machine d'origine de la requête de l'agent IA ? Cela complète l'axe « 3e mode d'accès » côté éditeur (Web Bot Auth + pay-per-crawl Cloudflare + Applebot-Extended + AP4M) par un axe côté entreprise jamais couvert dans la KB.
- Faut-il créer une fiche dédiée `gouvernance-agents-ia-enterprise` ou rester sous `agentic-search` ? Proposition de diff à valider en revue hebdo.
- La règle dure explore tient ce run : sources nouvelles (futurum, helpnetsecurity, venturebeat, ekamoira, ranketai, businesswire, technologychecker, firstpagesage) n'ont jamais publié seules un claim — chaque claim est porté soit par Microsoft blog primaire + 3+ reprises indépendantes, soit par Cloudflare Radar primaire + reprises, soit par Law360 + Courthouse News + MediaPost + OpenTools (4 sources). Cas spécifique à valider : Conductor businesswire (primaire-vendeur) seul porte le chiffre 1,08 pct AI referral, mais le claim est marqué confidence 0,7 et recoupé directionnellement avec Cloudflare Radar 0,29 pct AI search referrals. Est-ce que cette articulation « single-primary-vendor + recoupement directionnel d'ordre de grandeur » est acceptable comme application de la règle dure explore, ou faut-il exiger une 2e source indépendante avec mesure quantifiée comparable ?
- Sur la rédaction : le mot « positionné » utilisé une fois pour décrire la position commerciale Microsoft sur trois couches. Toujours OK ou à éviter dans les prochains runs (limite glissement vers personnification commerciale) ?

## Questions ajoutées après 2026-06-13-v2

- (autonomie data) BrightEdge promu exploit dès le 2e hit utile cumulé avec attribution explicite obligatoire (primaire-vendeur). À reconfirmer en revue hebdo si la qualité de la donnée tient sur la 3e citation : si non, repassage en explore.
- (autonomie data) digitalphablet.com et swipeinsight.app ajoutées en explore. swipeinsight.app rate-limited à la consultation directe, à reconfirmer avec un 2e hit utile ou retrait au prochain run.
- (proposition skill - PAS appliquée sans validation Tim) ajouter une métrique dans la grille de score : « doctrine_extension » qui mesure si l'édition étend une fiche de doctrine existante sur un axe non couvert (ici Information Agents = persistance asynchrone sur agentic-search, BrightEdge = assignation de rôle aux sources sur metriques-visibilite-geo). Notation 0-5. À discuter en revue hebdo : utile pour mesurer si l'agent enrichit la KB plutôt que la résumer.
- (proposition - PAS appliquée sans validation Tim) Considerer l'ajout d'un champ `dimensional_extension` dans claims.jsonl pour pointer explicitement quels concepts une étude empirique étend ou complète sur quel axe (ex: « metriques-visibilite-geo : nouvelle dimension assignation de rôle implicite »).

## Questions ajoutées 2026-06-14 (édition Limited Ad Serving Search)

- **Doctrine** : la fiche `[[concepts/metriques-visibilite-geo]]` couvre Imp_wc, Imp_pos, Subjective Impression. Faut-il ajouter une 4e dimension « moteur web sous-jacent du LLM » (Brave pour Claude, Bing pour ChatGPT search via Microsoft, Google pour Gemini et AI Overviews) ? La donnée Profound/Clark du 12 juin (Claude calque 86,7% sur Brave top 10) confirme que cette dimension est un levier d'optimisation distinct, pas seulement une curiosité technique. Question pour la revue hebdo.
- **Doctrine** : l'extension de la Limited Ad Serving Policy à Search introduit un parallèle explicite entre Trustworthiness (E-E-A-T) en organic et un signal équivalent appliqué à la sélection d'annonces. Faut-il créer une fiche `concepts/trust-signal-paid-organic-parallele` ou enrichir la fiche `concepts/e-e-a-t` avec une section sur les transferts paid/organic ?
- **Source explore** : tryprofound.com ajouté en explore trust 0.65 primaire-vendeur. Source de mesure GEO référence (Brand Radar undercount said 0612 + Zero Click sessions). Candidate au passage exploit après 2e hit utile, mais attribution explicite vendeur obligatoire à chaque usage.
- **Cycle hebdo creux** : sur un samedi (faible densité de news), accepter 3 brèves au lieu de 3-4 plutôt que forcer une 4e brève issue d'une source à méthodologie suspect (Tabeling SEL 12 juin). Confirmer cette discipline en revue hebdo : « 3 brèves au plancher si la 4e brève forcerait une source non solide » est-il une règle ?
- **Pilier variation** : 2 des 3 dernières info du jour sont maintenant Actualité SEO (0612-v2 + 0614). À la prochaine édition, viser explicitement Product-Led SEO (H-007 J+30 si data prête) ou Recherche agentique. Confirmer cette priorité.
