# Questions de l'agent — « comment faire mieux »

Écrit par l'agent 10 (auto-interrogation) à chaque édition. Deux niveaux :
- **Urgent** : remonté à Tim tout de suite (en bas du draft).
- **Hebdo** : groupé, présenté à la revue hebdo du vendredi.

L'agent répond lui-même à ce qu'il peut tester ; il garde pour Tim ce qui demande un arbitrage humain. C'est la sortie « auto-interrogation » de [[methodes/cadrage-boucle-edition-algorithme]] ; les arbitrages tranchés repartent dans [[directives]] et, pour la doctrine, vers la couche curée (`wiki/`).

## Urgent (à trancher vite)

(vide pour l'instant)

## Run 2026-08-03-v2 — pour la revue hebdo

- **Proposition de diff doctrine 8e dimension metriques-visibilite-geo, à valider Tim** : la fiche `wiki/concepts/metriques-visibilite-geo.md` formalise les dimensions de mesure GEO ; le run 08-02-v2 (geoSurge) proposait déjà une 7e dimension pré-recherche (couverture analyste + partenariats + association catégorie comme filtre d'éligibilité mémoire modèle). Ce run 08-03-v2 formalise une 8e dimension : le rendement conversion par citation, mesuré sur un money-query set de 50-100 requêtes de recommandation issues d'entretiens acheteurs, avec un délai d'apparition attendu de plusieurs semaines (Kevin Lee SEL 3 août + Orbit Media 22 juillet). Diff proposé : ajouter la 8e dimension à `wiki/concepts/metriques-visibilite-geo.md` avec les 3 conditions Kevin Lee (money-query set curé, balisage URL + CRM en amont de la publication, délai plusieurs semaines à absorber) + les 3 chiffres Orbit Media (0,5 pct trafic IA, 3x agrégé/7x médian ratio conversion, 82,3 pct ChatGPT du trafic IA). À valider en revue hebdo, je ne modifie pas la fiche seul (garde-fou autonomie).

- **Concept candidat wiki à créer, à valider Tim** : `wiki/concepts/money-query-set.md` (dérivé Kevin Lee 3 août 2026). Définition opérationnelle : ensemble de 50 à 100 requêtes de recommandation issues d'entretiens acheteurs réels ou de tickets sales, utilisé comme périmètre de mesure exclusive des citations IA et rattaché au pipeline via balisage URL + CRM en amont de la publication. Distinct de la mesure de citations sur un échantillon large de requêtes (bruit corrélé au trafic sans intention). Lien fort avec [[concepts/tabou-visibilite]] (opérationnalise le pivot data-driven vs visibilité) et [[concepts/data-proprietaire]] (data propriétaire produite pour un money-query set défini). À valider en revue hebdo.

- **Valider 2 nouvelles sources explore** : `orbitmedia.com` (trust 0,72 primaire, étude empirique 97 sites B2B 28,9M sessions méthodologie déclarée numérateur/dénominateur/seuil/catégorisation manuelle GA4, candidate exploit si reproduction indépendante ou 2e étude Orbit) et `blitzmetrics.com` (trust 0,55 secondary, cabinet Kevin Lee cross-ref bio auteur SEL 3 août, source complémentaire opinion sans mesure). À confirmer/retirer en revue hebdo.

- **Question méthode — convergence éditoriale un même jour** : Search Engine Land a publié 3 articles le 3 août dans la même fenêtre éditoriale (Kevin Lee GEO revenue targets + Casey Nifong measure Gemini + Adam Tanguay prompt research) qui convergent tous sur le déplacement mesure présence-visibilité vers mesure business-conversion-intention. Faut-il traiter la convergence éditoriale d'une source de référence dans la même journée comme un fait empirique à part entière (signal d'agenda éditorial coordonné susceptible d'influencer la doctrine du marché) ou strictement comme méta-observation à mentionner mais pas comme claim publiable ? Arbitrage souhaité pour cadrer les prochaines occurrences.

- **Question périmètre — Kevin Lee opinion sans data** : Kevin Lee est un signataire reconnu SEL (BlitzMetrics cofondateur) mais son éditorial 3 août ne cite aucune étude, aucun chiffre. Nous l'avons retenu comme info du jour parce que (1) l'angle recoupe explicitement une doctrine wiki (tabou-visibilite) et (2) une étude empirique publiée 2 semaines avant (Orbit Media) et une mesure du matin (Solis) fournissent la corroboration. Est-ce la ligne à tenir pour les prochains éditoriaux opinion ? Concrètement : opinion senior industry + doctrine wiki alignée + minimum 1 mesure empirique récente indépendante = publiable ; opinion senior seule sans mesure = pas publiable. Arbitrage à confirmer.

- **Question méthode — Cadence Q3 core update** : la cadence 2026 (mars, mai) rend probable un core update dans la fenêtre août-septembre. Volatilité 1-3 août seroundtable est mono-source (Barry Schwartz avec reprise Semrush Sensor + Mozcast qui sont 2 trackers indépendants dans son article) et sans confirmation Google. Faut-il ajouter Sistrix, Similarweb, RankRanger, Advanced Web Rankings, AccuRanker, AWR, Algoroo, Mozcast, Semrush Sensor comme sources explore dédiées volatility pour préparer le bilan quand un update sera confirmé ? Directive répétée non-tenue depuis 2026-06-02 (Sistrix testée puis abandonnée), à trancher.


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

## Questions ajoutées 2026-06-17 (édition Bing Webmaster Tools 4 métriques GEO)

- (autonomie data) launchcodex.com ajoutée en explore 0.65 secondaire-analyse 1er hit. Caveat technique précis sur portée Bing vs ChatGPT. À reconfirmer avec un 2e hit utile ou retrait au prochain run.
- (autonomie data) blogs.bing.com 2e hit cumulé, candidate au passage exploit (source primaire moteur). À arbitrer en revue hebdo.
- (autonomie data) pressgazette.co.uk 3e hit cumulé, promu candidate exploit confirmée (couverture trade UK régulière).
- (proposition skill - PAS appliquée sans validation Tim) ajouter une rubrique fixe « écart de couverture moteur » dans les éditions GEO quand un moteur publie une métrique inédite : forcer la lecture comparative explicite (Google vs Microsoft vs OpenAI) sur la dimension de mesure publiée. Ici testé en spontané sur Citation Share vs GSC AI reports. À discuter en revue hebdo si systématiser dans le wording_rules.
- (suivi P-2026-06-17-1) surveiller publication d'études empiriques utilisant Citation Share pendant la preview Bing Webmaster Tools sur 100+ sites. Sources à monitorer : Ahrefs Brand Radar, Semrush AI Performance Insights, Conductor, BrightEdge, SISTRIX, Onely, Digital Authority Partners.
- (suivi P-2026-06-17-3) surveiller premières affaires small claims court UK déposées sur la base d'un Search-Only Contract MOW. Sources à monitorer : Press Gazette, PPC Land, Mlex (juridique antitrust), CourthouseNews, Movement for an Open Web blog.

## 2026-06-17 v2 — questions et observations (cloud)

### Questions à Tim (revue hebdo)
- **Famille C fabricant FMCG dans ACP** : faut-il créer une fiche concept dédiée dans `wiki/concepts/` pour formaliser la typologie famille A retailer / famille B fintech / famille C fabricant dans l'architecture Agentic Commerce Protocol ? Cadre conceptuel issu de l'édition mais qui mériterait un statut doctrine stable (proposition diff skill : non, ce serait une fiche concept à créer en revue hebdo).
- **L'Oréal pages produit en ChatGPT US** : est-ce qu'un de tes clients est en position de demander à OpenAI les conditions techniques d'inscription des « enriched signals » pour pages produit ? Ce serait une donnée de terrain forte pour résoudre P-2026-06-17-v2-3 (politique de désambiguïsation).
- **Ahrefs 137K llms.txt** : tu as un test terrain llms.txt sur un client ? Si oui, croiser avec la mesure Ahrefs (notre client est-il dans les 3 pct qui ont du trafic, ou dans les 97 pct qui n'en ont pas ?) pourrait alimenter une fiche preuve hypothesis-llms-txt-inutile.

### Diffs de skill proposés
- Aucun ce run. Le cadre 3 familles ACP est un cadre conceptuel SyntheticBrain, pas un changement de skill.

### Sources découvertes (auto-ajoutées explore)
- wwd.com (0,85, trade press beauty US, primaire trade press, signature journaliste, candidate exploit en revue hebdo)
- cosmeticsbusiness.com (0,7, trade press beauty UK)
- webwire.com (0,6, press release distributor neutre)
- happi.com (0,62, trade press household personal care US)

### Observations méthodologiques
- L'angle « architecture par familles » a été testé pour la première fois dans ce run pour clore une info du jour. Le cadre tient parce que les 3 faits indépendants (Walmart 25 mars, Klarna 20 mai, L'Oréal 17 juin) ont chacun un sourcing primaire distinct. Si une 4e famille émerge dans les prochaines semaines (P-2026-06-17-v2-1), le cadre devra être révisé.
- Ahrefs llms.txt a été placé en brève B1 GEO plutôt qu'en info du jour Actualité SEO parce que la mesure empirique 137K domaines est plus forte que la quote Mueller seule. Le déplacement de cible (developer vs consumer) est l'angle d'analyse propre qui ajoute valeur au-delà du résumé d'étude.

## 2026-06-18 — questions et observations (cloud)

### Questions à Tim (revue hebdo)
- **Fiche concept manquante : TCF/publicité/éditeurs** : l'info du jour de ce run (Google IP-based ads EEA UK CH au 3 août 2026 via TCF Feature 3) n'a aucun lien doctrine direct dans `wiki/concepts/`. Faut-il créer une fiche concept dédiée à l'interaction « cadre TCF IAB Europe / publicité Google / charge de conformité éditeur » ? Ce serait utile si une 2e échéance réglementaire similaire arrive aux US (FTC, CCPA Californie) dans les 6 mois. Proposition : fiche concept en revue hebdo si fait neuf le confirme. Sinon, classement Actualité SEO suffit.
- **Hiérarchie formats cités IA** : 3 mesures indépendantes convergent maintenant sur la dominance de la recherche originale dans les citations IA (Lily Ray 13 mai 2025 52,2 pct, Seer 24 avril 2026 facteur 2,2, NP Digital 17 juin 2026 82 pct). Faut-il faire monter en `confidence: very-high` la page [[concepts/data-proprietaire]] (actuellement `high`), ou au contraire la maintenir prudente car NP Digital est déclaratif (sondage de 500 marketeurs, pas une mesure côté moteur) ? Proposition : maintenir `high` jusqu'à ce qu'une 2e mesure empirique côté moteur (équivalent à Seer R&D) reproduise le facteur 2,2 sur un autre échantillon.
- **Test terrain Google IP-based ads pour les clients européens** : tu as un client éditeur AdSense en Europe ? Si oui, vérifier que sa CMP est prête pour la TCF Feature 3 vendor 755 avant le 3 août pourrait être un service à fournir en juillet. Bonne donnée de terrain pour résoudre P-2026-06-18-2 (mesure adoption CMP) dans 90 jours.

### Diffs de skill proposés
- Aucun ce run. La méthode « 3 implications opérationnelles directes » est une technique d'angle, pas un changement de skill.

### Sources découvertes (auto-ajoutées explore)
- crowell-moring (0,7, cabinet juridique américain, analyse jurisprudence AI/copyright/contract law, source secondaire fiable)
- loeb-loeb (0,65, cabinet juridique américain, analyse en interne dossier Reddit-Anthropic)
- bleepingcomputer (0,7, source d'analyse cybersécurité/privacy reconnue, 1er hit utile)
- neilpatel-com (0,6, source primaire enquête NP Digital sur formats AI citation, 1er hit utile)

### Observations méthodologiques
- L'angle « 3 implications opérationnelles directes » a été testé sur l'info du jour Google IP-based ads. Tient parce que les 3 implications (date dure, interface CMP, déplacement charge juridique) sont chacune ancrée sur un mécanisme nommé (3 août, Feature 3 + vendor 755, EU User Consent Policy). À reproduire sur d'autres annonces produit/réglementaires où le déplacement est précisable. Si une annonce ne se prête pas à 3 implications atomiques, en nommer 1 ou 2 plutôt qu'en forcer 3.
- L'enquête NP Digital a été placée en brève B1 GEO plutôt qu'en info du jour parce que (a) GEO a été pris hier en info du jour (Bing Webmaster Tools) et la directive impose de ne pas réenchaîner sans fait franchement neuf, (b) l'enquête est déclarative ce qui pondère sa robustesse. L'approche « 3e mesure indépendante hiérarchisée vs antérieurs » est une technique d'angle qui rend le claim plus solide qu'une simple reprise.
- L'absence de lien doctrine direct sur l'info du jour (TCF/publicité/éditeurs) a été assumée explicitement dans le corps. Ne pas forcer un lien décoratif est conforme à la voix synthétique : honnêteté sur les limites de la couverture existante.

## Questions levées par l'édition 2026-06-24

### Doctrinales (à arbitrer en revue hebdo vendredi)

- **La couche B2B agent acheteur ↔ agent vendeur dans agentic-search** : zone d'ombre signalée le 23 juin, étendue le 24 juin avec TikTok Symphony Agent (annonceur → agent générateur de campagne → plateforme). La fiche [[concepts/agentic-search]] décrit la couche utilisateur final ↔ agent ↔ contenu, mais pas la couche annonceur ↔ agent créateur ↔ plateforme. Faut-il formaliser une fiche [[concepts/agentic-advertising]] distincte ? Ou étendre [[concepts/agentic-search]] avec une section dédiée à la couche B2B ? (Tim arbitre revue hebdo).
- **Sous-clusters du pattern Cannes 2026** : graphes structurels (Pinterest Taste Graph + Shopify Catalog) vs corpus communautaires-créateurs (Reddit posts/comments + TikTok creator content + performance signals). Faut-il formaliser dans la doctrine cette distinction des deux modèles d'agent publicitaire IA selon le type de corpus mobilisé ? Implication SEO : la stratégie d'optimisation diffère selon le sous-cluster (structuration de données vs activation communautaire). (Tim arbitre revue hebdo).

### Méthodologiques

- **WebSearch synthesis hallucination dates** (M-006) : faut-il systématiser un script de cross-check entre WebSearch synthesis et page primaire developers.google.com/search/updates avant d'inclure un changement de documentation Google ? Voire un audit hebdomadaire de la page Search Central updates pour tracker les changements réels vs prétendus.
- **Schwartz tracker-community gap** : la chatter praticien lourde + outils calmes pourrait justifier d'ajouter aux sources exploit un agrégateur communautaire (forum Webmaster, X SEO community, Reddit r/SEO) pour ne pas dépendre uniquement des outils SERP automatisés. À discuter.

### Sources

- 5 sources explore ajoutées ce run (newsroom.tiktok.com primaire trust 1.15 / netinfluencer.com 0.65 / hellopartner.com 0.62 / affiversemedia.com 0.6 / performancemarketingworld.com 0.7 / adexchanger.com 0.75). newsroom.tiktok.com et adexchanger.com sont candidats passage exploit en revue hebdo (autorité connue, qualité corroborée). Les autres restent en explore tant que pas de 2e hit utile documenté.


## Questions levées par l'édition 2026-06-26-v2

### Doctrinales (à arbitrer en revue hebdo vendredi)

- **Extension du filtre test-substitution-llm au-delà du texte vers l'interaction multimodale** : Project Genie (Google DeepMind) Grand Prix Digital Craft Cannes Lions 2026 le 23 juin 2026 est le cas extrême d'un outil qui génère un environnement interactif 3D complet depuis un prompt texte. Le filtre 80 pct tel que rédigé en avril 2026 (fiche [[concepts/test-substitution-llm]]) portait sur la production de texte. Proposition : élargir la formulation à « est-ce qu'un modèle générateur peut produire 80 pct de cette interaction multimodale ? ». Conséquence opérationnelle : une page calculateur sans data temps réel, un comparateur sans contrainte propriétaire (stock, partenariats, pricing exclusif), un simulateur générique, une data viz sans dataset privé, tombent désormais dans la même zone de substitution que les FAQ génériques d'hier. Le filtre étendu reste binaire : si l'outil peut être reproduit à la volée par un modèle multimodal, ne pas le créer comme page de capture. (Tim arbitre revue hebdo. Proposition de diff précis à la fiche [[concepts/test-substitution-llm]] : ajouter section « extension multimodale 2026-06-26 » avec mention Project Genie + Genie 3 + Google Maps Street View intégration comme cas extrême documenté).
- **Critère défensif résiduel Product-Led SEO : persistance / stock réel / data propriétaire** : la fiche [[concepts/product-led-seo]] liste 7 formes acceptables de produit embarqué dont « fonctionnalité de persistance (sauvegarde, tracking, progression) ». Project Genie ne dispose pas de persistance par utilisateur (au moins dans son périmètre actuel Google AI Ultra subscribers via Google Labs). Proposition : remonter explicitement le critère de persistance et de connexion à des données privées comme critère DÉFENSIF RÉSIDUEL central, distinct des 6 autres formes (calculateur, simulateur, comparateur, configurateur, générateur, data viz interactive) qui sont potentiellement substituables par UI générative. Le cas Victoria Garden documenté en avril 2026 reste valide parce que ses 4 modèles purs s'appuient sur stock réel + partenariats locaux, c'est-à-dire sur le critère data propriétaire qui sous-tend tout le reste. (Tim arbitre revue hebdo).
- **Couche sécurité agents IA et signal classement Search** : Nenad Tomašev (Senior Staff Research Scientist Google DeepMind) reconnaît publiquement le 25 juin 2026 que le déploiement large-échelle d'agents IA n'est pas suffisamment fiable aujourd'hui, et nomme 3 vecteurs d'attaque ciblant les agents : hidden tokens, dynamic cloaking, jailbreak-inducing content. Question doctrine : un site qui pratique sciemment ou via lib tierce embarquée l'un de ces 3 vecteurs devrait à terme recevoir un signal négatif au classement Search classique (couplage côté Google entre les couches de validation agent et l'indexation web). La prédiction P-2026-06-26-v2-3 force le suivi (échéance 31 décembre 2026). Si validée, formaliser une fiche [[concepts/machine-cleanliness-signal]] ou étendre la fiche [[concepts/structural-information-geo]] avec une section dédiée. Sinon, garder hors doctrine. (Tim arbitre revue hebdo).

### Méthodologiques

- **AirOps State of AI Search 2026 publié décembre 2025 = J+200+ corpus de référence vs étude fraîche** : utilisé en B3 comme corpus de référence avec caveats explicites (sample size non publié, corrélations sans causalité, variation modèle non quantifiée). Faut-il systématiser le statut « corpus de référence pondéré en lecture » pour les rapports majeurs publiés > 60 jours quand aucune mesure plus récente n'existe ? Distinction utile vs « étude fraîche < 30 jours » qui passe la porte de fraîcheur directe. (À discuter en revue hebdo).
- **Cyrus Shepard Zyppy meta-analysis 54 studies 23 facteurs (May 7 2026) trop ancien direct mais Digital Applied republication June 24 2026** : la republication par Digital Applied n'est pas une étude neuve, c'est une synthèse. Faut-il considérer une synthèse récente d'études anciennes comme une porte de fraîcheur valide, ou écarter systématiquement pour ne traiter que l'étude originale ? Choix actuel : écarter (fraîcheur < 30 jours sur l'étude originale, pas sur la synthèse). À discuter. (À discuter en revue hebdo).

### Sources

- 11 sources explore ajoutées ce run : canneslions.com (0.9, primaire org, candidate exploit revue hebdo car source primaire de référence pour Cannes Lions + autorité industrie), lbbonline.com (0.7, trade média), brandinginasia.com (0.6, trade APAC), exchange4media.com (0.62, trade India), deepmind.google (0.92, primaire vendeur Google DeepMind, candidate exploit revue hebdo car source primaire de référence pour DeepMind products + papers), selfstorming.com (0.5, plateforme campaigns library), ads-developers.googleblog.com (0.92, primaire vendeur Google Ads Developer Blog, candidate exploit revue hebdo car source primaire de référence pour API releases + changelog), eseospace.com (0.55, blog SEO), position.digital (0.55, agence digitale compilation stats), sqmagazine.co.uk (0.55, magazine SEO UK compilation), techtimes.com (0.62, presse tech, 2e hit utile, candidate exploit). 3 sources fortes pour passage exploit : canneslions.com + deepmind.google + ads-developers.googleblog.com (primaires des trois sujets traités du jour). Continuer 1 source neuve par édition pour explore.

## 2026-07-03-v2 — Questions et propositions issues du run cloud pilier GEO

### Questions à Tim (revue hebdo)

1. **Statut CiteLens** : la source est nouvelle (0.55 explore), le finding 60 pct divergence AIO vs top 10 est quantifiée mais mono-source vendeur. J'ai publié le claim ATTRIBUÉ explicitement à CiteLens (pas comme consensus mesuré) avec 4 caveats méthodologiques dans le corps + prédiction testable P-2026-07-03-v2-1 pour reproduction indépendante d'ici fin 2026. Est-ce que le seuil d'attribution vendeur single-source explicite est acceptable pour info du jour, ou tu préfères que les études vendeur single-source restent en brève avec caveat renforcé et jamais en info du jour ? Question de politique éditoriale de la voix SyntheticBrain.

2. **CiteLens Alper Tekin trust initial** : proposé 0.55 (vendeur nouveau, methodologie détaillée non publiée en annexe). Est-ce que le seuil devrait être plus bas (0.4-0.45) tant que la méthodologie complète n'est pas publiée en annexe consultable ? Question de calibration trust pour futures études vendeur GEO.

3. **Choix pilier GEO malgré 3 GEO dans 16 dernières info du jour** : la directive disait « viser Product-Led SEO OR GEO OR Business SEO ». J'ai retenu GEO car (a) fait franchement neuf CiteLens hors 3 exclusions (reasoning modes Semrush + citation-first recettes + Consensus Gap Indig), (b) doctrine directement testée (metriques-visibilite-geo + tabou-visibilite), (c) l'alternative Indig+Johnson SEL 2 juillet était redite v1 morning, (d) Business SEO récent 0702 v2 Cloudflare. Est-ce que la concentration GEO (3 sur 16, dont 2 récentes 0627 v2 + 0703 v2) est acceptable ou faut-il forcer Product-Led SEO même sans fait franchement neuf ? Question de balance piliers vs qualité fait.

4. **Nudge 4x visibility + 24 pct lift** : chiffres vendeur auto-déclarés publiés dans brève B2 avec caveat renforcé (auto-déclaré + non ventilé + duré non spécifiée + non reproduit tiers). Est-ce que le seuil « publier chiffre vendeur avec caveat » est acceptable pour la voix SyntheticBrain ou tu préfères une politique plus stricte « chiffres vendeur non ventilés = pas publiés du tout, seulement l'existence de la levée + les fonctions du produit + le protocole ACP/UCP » ? Question de politique éditoriale.

### Diffs de skill proposés (à évaluer en revue hebdo)

Aucun diff de skill proposé ce run. Le skill SKILL.md tient bien sur (a) attribution explicite vendeur single-source, (b) caveats méthodologiques ≥ 3 dans le corps, (c) prédiction testable de reproduction indépendante. Pattern reproductible pour futures études vendeur GEO/AEO documenté dans directives.md méthode confirmée 2026-07-03-v2.

### Sources découvertes ce run

- 7 nouvelles explore ajoutées : citelens.io (0.55 vendeur GEO), martechseries.com (0.6 outlet MarTech), tech.einnews.com (0.5 PR syndication), natlawreview.com (0.5 PR syndication), retailtechinnovationhub.com (0.65 primaire Scott Thompson signé), intelligentretail.tech (0.55 reprise), wwd.com (0.7 Tier-2 retail spécialisé), practicalecommerce.com (0.65 curation ecommerce). 2 candidates à surveiller pour passage exploit en revue hebdo si utilisation répétée : retailtechinnovationhub.com (primaire retail tech avec signature Scott Thompson) + wwd.com (Tier-2 spécialisé retail/mode avec Sourcing Journal).
- practicalecommerce.com est une source de curation d'outils ecommerce/martech utile pour la découverte de nouveaux acteurs à l'intersection SEO/GEO/commerce agentique. Candidate au passage exploit si 2e hit utile confirmé.

## Run 2026-07-04

### Questions à Tim (non bloquantes, à trancher en revue hebdo)

1. **Pilier Niche SEO saturé** : Google Business Profile Reviews bug = 4e Niche SEO parmi les 17 dernières info du jour (0704 + 0701 v2 + 0630 v1 + 0628 v1). C'est le pilier le plus fréquent avec Actualité SEO. Est-ce que la définition de Niche SEO du manifeste (« cas de site / cluster de niche qui s'ouvre ou qui gagne ») doit distinguer plus clairement entre (a) niche site case study d'un vertical qui gagne ou perd nettement (Gabe YMYL santé, Bing Copilot toggle, Walker Sands B2B) et (b) incident opérationnel Google qui affecte un cluster (Business Profile Reviews). Le second cas est arguably plus Actualité SEO qu'Niche SEO. Question de taxonomie.

2. **Article On-Page.ai 12 juin publié avec 22 jours de retard** : la publication a 3 semaines. Publier ce fait en brève doctrinale reste-t-il pertinent, ou faut-il durcir la règle « une brève ne peut porter un fait de plus de 10 jours sans un signal fresh qui la ré-actualise » ? Question de règle éditoriale. Le pattern On-Page.ai est utile comme point empirique aligné avec la fiche data-propriétaire, mais la fraîcheur factuelle est modérée.

3. **Pattern « fragmentation outils AI visibility » comme B3** : cette brève est doctrinale (angle tabou-visibilite mot sans unité) mais s'appuie sur des revues concurrent-contre-concurrent (Profound review Ahrefs). Le biais commercial est explicite dans les sources. Est-ce que cette famille de brèves (état de l'art commercial d'un marché avec biais éditeur explicite) est acceptable, ou faut-il durcir « une brève ne peut pas s'appuyer principalement sur des reviews cross-vendors sans une source neutre tierce » ? Question de politique éditoriale.

4. **Directive « tester une source de mesure de visibilité indépendante » = 23e édition consécutive non tenue** : Semrush Sensor, Mozcast, Wincher, AccuRanker, AWR — aucune n'a été testée. Question méta : est-ce que cette directive doit être escaladée en « ne pas publier de brève Actualité SEO sur un core update ou spam update tant que cette directive n'est pas tenue » ? Ou renoncer explicitement à cette directive si elle n'a pas de valeur ajoutée démontrée ? Question de gouvernance des directives récurrentes non tenues.

### Diffs de skill proposés (à évaluer en revue hebdo)

Aucun diff de skill proposé ce run. Le pattern « confirmation Google d'un incident opérationnel avec faux positif algorithmique admis » est documenté dans directives.md 2026-07-04 méthode confirmée : combinaison primaire journalistique verbatim + reprise indépendante hypothèses causales + expert vertical historique + verbatim porte-parole + portée qualitative explicite + doctrine multi-concepts + recommandations vouvoyantes + prédiction transparence post-incident.

### Sources découvertes ce run

- 5 nouvelles explore ajoutées : seoteric.com (0.55 agence local SEO writeup), sterlingsky.ca (0.75 Joy Hawkins expert local SEO reconnue, candidate exploit après 2e utilisation), api.on-page.ai (0.6 vendeur GEO/PLS étude proprietaire), tryprofound.com (0.6 vendeur AI visibility concurrent Ahrefs biais commercial explicite), rankability.com (0.6 blog outil AI visibility), ewrdigital.com (0.55 agence review). sterlingsky.ca est la candidate la plus forte au passage exploit en revue hebdo (Joy Hawkins référence Google Business Profile Product Expert depuis 2012, source fiable pour tout dossier local SEO / Business Profile).

## Questions ajoutées après 2026-07-12-v2

### Sources découvertes ce run

- 4 nouvelles explore ajoutées : josephcharnin.com (0.6 blog-analyse-praticien-indépendant, candidate à observer sur 2-3 prochaines éditions), unrealwebmarketing.com (0.55 blog-analyse-praticien), github.com/agentic-commerce-protocol (0.75 spécification-technique-primaire, source officielle pour tout travail sur ACP), searchsignal.online (0.6 recherche-indépendante-AI-search, à recouper avec 2e source sur 2 prochaines éditions).

### Question méthode (à trancher en revue hebdo)

- Quand une édition v1 existe déjà pour la journée (contexte cloud automatique), le run v2 doit-il chercher activement un pilier différent de v1 (comme fait ce run : v1 Business SEO → v2 GEO / search IA) ou peut-il rester sur le même pilier si le sujet est distinct ? Position tenue ce run : varier le pilier est cohérent avec la directive Tim « varier le pilier d'une édition à l'autre », et pouvoir varier même à l'intérieur d'une même journée est un avantage éditorial (couverture plus large des 4 piliers dans la semaine). À valider explicitement.

### Question sujet (à surveiller)

- Cloudflare Content Signals (mentionné 2026-07-08 P-2026-06-01-v2-1) et Cloudflare Pay Per Use (2026-07-12-v2) : deux mécaniques distinctes du même acteur qui pourraient converger à l'échéance 15 septembre 2026. Faut-il créer une fiche `wiki/concepts/cloudflare-controle-acces-llm` qui consolide les deux ? Ou garder deux traitements distincts dans le vault ? Position tenue ce run : ne pas créer de fiche, laisser la brève B2 (0708) et l'info du jour (v2 aujourd'hui) documenter deux temps distincts. À arbitrer en revue hebdo si la convergence effective se produit après le 15 septembre.

## Questions / observations 2026-07-13-v2

- **Non bloquant.** Kerhoas cite dans son article des chiffres (ChatGPT US base flat depuis septembre 2025, financials OpenAI 2025) sans donner de lien primaire. Recoupement fait de notre côté sur Zitron/FT/TechSpot pour les financials et sur TechCrunch/Sensor Tower décembre 2025 pour ChatGPT. Question : faut-il durcir la règle et systématiquement re-sourcer chaque chiffre cité par un article d'analyse tiers, même quand il paraît courant ? Proposition : oui, à mettre en observation dans `wording_rules.md` sous « chiffres relayés ».
- **Non bloquant.** Le préprint Sielinski IQRush n'est pas encore publié à la date du 11 juillet (annoncé pour la semaine suivante par Southern). Notre B1 s'appuie sur la couverture SEJ + le travail Saint-Gall indépendant. Question : quand le préprint sera publié, revient sur la brève pour ajouter le lien direct arxiv/SSRN et vérifier que la méthodologie décrite par Southern est bien la méthodologie publiée. À caler pour la revue hebdo.
- **Non bloquant.** Le workflow `youtube-claude-seo/yt_best.py --months 1` n'est pas utilisé en édition cloud (binaire local). À exécuter à la prochaine édition locale pour élargir la surface de découverte.

## Questions ajoutées après 2026-07-14-v2

### Sources découvertes ce run

- 3 nouvelles explore ajoutées : arxiv.org (0.85 primaire-academique-preprint, source de référence pour toute étude quasi-expérimentale ou paper académique en preprint, à corroborer systématiquement par reprise trade press), helpnetsecurity.com (0.7 trade-securite, utile pour infra bot detection / crawlers / agents), siliconangle.com (0.7 trade-tech, à observer sur 2-3 prochaines éditions avant décision exploit).

### Question méthode (à trancher en revue hebdo)

- Sur un preprint arXiv non peer-reviewed publié depuis moins de 10 jours, quel est le seuil de fiabilité acceptable pour en faire une info du jour ? Position tenue ce run : (a) énoncer explicitement que le paper est un preprint non peer-reviewed, (b) recouper avec au moins deux reprises indépendantes de sources exploit (ppc.land + SEJ ici), (c) vérifier au moins deux des trois affiliations d'auteurs (Shi et Zhu confirmés Bocconi, Gu non confirmable). Question : faut-il durcir en règle explicite dans `memory/wording_rules.md` ou dans `notes/` ?

### Question doctrine (à valider en revue hebdo)

- La 7e dimension implicite de [[concepts/metriques-visibilite-geo]] introduite en B3 (taux de citation qui produit effectivement une recommandation nominative de la marque, distinct de l'apparition d'URL) mérite-t-elle une fiche `wiki/concepts/citation-vs-recommandation.md` distincte, ou reste-t-elle une extension de metriques-visibilite-geo ? Position tenue ce run : traiter comme extension. Arbitrage à faire en revue hebdo (potentiel candidat pour promotion en fiche stable si un 2e cas d'usage documenté sort dans les 30 prochains jours).

### Question sujet (à surveiller)

- La mesure Bocconi ne couvre pas le mobile ni l'international, deux angles morts. Faut-il activement chercher des mesures européennes/mobile équivalentes (Similarweb, Datos, Kantar, Nielsen) pour compléter le cadre d'ici la revue hebdo ? Position : à guetter, ne pas forcer un run dédié sans mesure comparable primaire.

### Diffs de skill proposés (à évaluer en revue hebdo)

Aucun diff de skill proposé ce run.

## Questions/propositions issues du run 2026-07-16 (à trancher en revue hebdo)

### Q-2026-07-16-1 : proposer une fiche `wiki/concepts/metriques-visibilite-geo` étendue à 9 dimensions ?

**Contexte** : édition du 15 juillet 2026 a introduit une 8e dimension (« taux de citation première-partie par tâche acheteur »). Édition du 16 juillet 2026 introduit une 9e dimension (« part de citations captée par le moteur lui-même dans ses propres réponses IA »).

**Décision demandée** : valider ou refuser la formalisation en fiche wiki de ces 8e et 9e dimensions. Si validé, quel critère de spécificité au moteur (uniquement Google AI Mode aujourd'hui, faut-il un axe explicitement « spécifique-à-un-moteur » vs « transverse-tous-moteurs » ?).

**Trace** : édition 16 juillet 2026 info du jour, ledger claims C-2026-07-16-1 à 3.

### Q-2026-07-16-2 : passage de tryprofound.com en `exploit` ?

**Contexte** : tryprofound.com en `explore` depuis 2026-05-30 (trust 0.65). 5+ hits utiles cumulés. Info du jour édition 2026-07-16 portée par leur mesure primaire. Sujet corroboré par republication éditoriale SEL sans reproduction indépendante (candidate P-2026-07-16-1).

**Décision demandée** : (1) passer en `exploit` si un 2e vendor corrobore Profound d'ici décembre 2026 (résolution positive P-2026-07-16-1). (2) sinon rester en `explore` avec trust maintenu à 0.65-0.7. (3) alternative : passer en `exploit-conditionnel` avec règle explicite « toute mesure Profound est admise si corroborée par 1 source de mesure indépendante ».

**Trace** : ledger sources.jsonl hit 2026-07-16.

### Q-2026-07-16-3 : mettre à jour la lecture opérationnelle « attendre bilan tracker » après P-2026-07-02-v2-5 invalidée ?

**Contexte** : P-2026-07-02-v2-5 invalidée à J+6 (échéance 10 juillet 2026, aucun bilan large publié). Pattern « trackers ne publient pas de bilan large échantillon sous 14 jours après update Google » confirmé sur 2026 (déjà noté sur core update mai). Directive présente dans plusieurs éditions sur le mode « attendre bilan tracker » devient discutable comme priorité prochaine édition.

**Décision demandée** : soit (1) retirer la directive « attendre bilan tracker large échantillon » du champ « pistes fraîches non traitées » et remplacer par « guetter bilan tracker large uniquement post-J+14 par défaut », soit (2) maintenir la directive mais assumer un délai plus long, soit (3) ajouter la mention explicite du pattern 2026 dans les prochaines directives.

**Trace** : predictions.jsonl P-2026-07-02-v2-5-resolution.


### Q-2026-07-17-1 : formaliser un critère pilier « Business SEO côté sortie de conversion » distinct de « Business SEO côté couche opérateur » ?

**Contexte** : depuis 07-13 morning (Kasper couche opérateur mesure GEO) et 07-14 v2 (Bocconi bascule marché mesurable), le pilier Business SEO a été mobilisé sur des angles différents (mesure marché vs mesure produit). L'édition 2026-07-17 (Connected Apps AI Mode) ajoute un 3e angle : la sortie de la conversion hors site marchand. Ces trois angles partagent le pilier Business SEO mais interrogent des mécaniques différentes.

**Décision demandée** : soit (1) maintenir le pilier Business SEO comme un ensemble unique large, soit (2) introduire une sous-classification (Business SEO / marché, Business SEO / couche opérateur, Business SEO / sortie de conversion) dans les directives et le said_index pour améliorer l'anti-redite fine, soit (3) créer un pilier distinct « Commerce agentique » pour le sous-cas conversion hors site.

**Trace** : runs.jsonl 2026-07-13, 2026-07-14-v2, 2026-07-17 champ `pilier_info_jour`.

### Q-2026-07-17-2 : valider passage exploit pour les 4 sources ajoutées en pratique le 2026-07-17 ?

**Contexte** : 4 sources utilisées pour la 1re fois dans l'édition Connected Apps (company.instacart.com trust 0.72, engadget.com trust 0.65, macrumors.com trust 0.65, search-off-the-record.libsyn.com trust 0.9). company.instacart.com est un billet primaire marque, utile quand la marque annonce une intégration produit. search-off-the-record.libsyn.com est la source primaire officielle Google Search Central pour les épisodes du podcast, avec un potentiel d'usage récurrent élevé sur les prochaines éditions.

**Décision demandée** : soit (1) passer les 4 sources en exploit d'emblée, soit (2) attendre une 2e utilisation utile avant passage exploit (règle standard SyntheticBrain), soit (3) passer search-off-the-record.libsyn.com et company.instacart.com en exploit d'emblée (sources primaires marque à forte valeur documentaire) et laisser engadget.com et macrumors.com en explore.

**Trace** : sources.jsonl entrées 2026-07-17.

### Q-2026-07-17-3 : proposer une auto-check obligatoire « grep -iE 'rail\b' hors sens ferroviaire » dans la routine post-rédaction ?

**Contexte** : le mot « rail » (métaphore ferroviaire interdite dans le prompt SyntheticBrain) est apparu 4 fois dans le corps de l'info du jour du 17 juillet, loggé en mistake M-007. La liste des mots métaphoriques interdits (rails, carburant, fusée, boussole, vague, tsunami, bataille, arme, passer à la caisse, ouvrir la voie, terrain de jeu, tuyau) est vérifiée par grep post-rédaction. « rail » figure explicitement dans la liste mais l'auto-check ne s'est déclenché qu'après relecture manuelle du draft, pas dans une routine automatisée.

**Décision demandée** : soit (1) ajouter la commande `grep -iE '\b(rails?|carburant|fusée|boussole|vague|tsunami|bataille|arme|passer à la caisse|ouvrir la voie|terrain de jeu|tuyau)\b' <draft>` comme étape obligatoire du gate qualité de l'agent 7 dans la SKILL.md, soit (2) formaliser dans un script `validate-draft.sh` complémentaire à `validate.sh` (qui valide les JSONL, pas le corps du draft), soit (3) laisser en règle mémoire humaine et re-vérifier au prochain run.

**Trace** : mistakes.jsonl M-007.

### Q-2026-07-17-v2-1 : la veille communautaire (Reddit, X) est morte, on fait quoi ?

**Contexte** : l'agent de veille communautaire du run du 17 juillet après-midi n'a pu ouvrir ni Reddit ni X. Toutes les routes ont échoué : Reddit renvoie 403 en direct, en `.json` et en RSS ; WebFetch le refuse par politique ; l'archive pullpush répond 200 avec `data:[]` vide même sans filtre de date ; les mirrors redlib sont en 503/403 ou derrière une preuve de travail Anubis ; WebSearch refuse le domaine reddit.com. Côté X, nitter.net répond 200 avec un corps vide, xcancel et poast sont en 503. Conséquence : l'édition du 17 après-midi ne contient **aucun signal terrain**. C'est loggé en M-010. Le skill SyntheticBrain prévoit Reddit et X comme sources de veille, mais la capacité n'existe plus. Tant que ce n'est pas tranché, chaque édition perdra la couche « plusieurs praticiens constatent la même chose », qui est justement celle qu'aucun média SEO ne fournit.

**Décision demandée** : soit (1) Tim fournit une clé API Reddit (et éventuellement X) à mettre dans `~/.config/`, soit (2) Tim colle les threads à la main quand il en voit passer, comme il le fait déjà pour les verbatims Reddit destinés au travail mots-clés, soit (3) le skill acte que le signal terrain n'est plus disponible, retire Reddit et X de la liste des sources de l'agent 1 et cesse de compter cette couche dans `source_diversity`.

**Trace** : mistakes.jsonl M-010, runs.jsonl 2026-07-17-local-v2 champ `decisions`.

### Q-2026-07-17-v2-2 : la directive « Niche SEO prioritaire » est-elle tenable à cadence quotidienne ?

**Contexte** : l'angle Niche SEO est marqué prioritaire dans les directives depuis plusieurs éditions et n'est toujours pas tenu. Le run du 17 après-midi a cherché activement (agent explore dédié, cible n°1) et n'a trouvé qu'un seul candidat sur la fenêtre : GoGoChimp, agence CRO de Glasgow, qui revendique 3 263 citations Copilot contre 87 clics organiques Google. Rejeté après vérification : deux de ses pages donnent les mêmes chiffres pour deux fenêtres de mesure différentes (28 avril-30 juin vs 19 avril-3 juillet), donc au moins une des deux est fausse ; contradiction interne aussi sur la concentration (84 pct vs deux tiers) ; comparaison d'une part de citation mono-requête à un baseline cross-moteurs ; chaîne de sources qui pointe vers des agrégateurs. Le rejet est le bon appel. Mais la directive reste non satisfaite édition après édition, ce qui use la mémoire sans rien produire.

**Décision demandée** : soit (1) accepter que Niche SEO sorte quand la matière existe (une fois par mois environ) et retirer la mention « priorité maintenue » qui se répète sans effet, soit (2) **Tim fournit les cas de niche depuis son terrain client** (ce serait de la data first-party, donc supérieure à n'importe quelle source publique, et cohérent avec la doctrine « le corpus nourrit le bot »), soit (3) abaisser la barre de preuve pour cet angle et publier des cas en « témoignage non vérifié » clairement étiquetés (non recommandé : contredit la règle de recoupement).

**Trace** : directives.md sections 2026-07-16-v2 et 2026-07-17-v2, sources.jsonl entrée gogochimp.com 2026-07-17.

### Q-2026-07-17-v2-3 : ajouter un check d'unicité des IDs à validate.sh ?

**Contexte** : le run local de l'après-midi a alloué `M-007` à sa première erreur alors que le run cloud du matin avait déjà pris `M-007` le même jour. Deux lignes M-007 sans rapport ont coexisté dans `mistakes.jsonl`. `validate.sh` n'a rien détecté : il valide la forme JSON et le `capture_mode`, pas l'unicité des identifiants. La collision a été trouvée par hasard, en relisant `questions.md` qui mentionnait un M-007 déjà pris. Le problème vaut pour tout ledger à ID séquentiel (mistakes, claims, headlines, predictions) dès que deux runs tombent le même jour, ce qui est le cas standard depuis que le cron cloud tourne deux fois par jour.

**Diff de skill proposé** : ajouter à `validate.sh` un check qui charge chaque ledger, extrait les champs `id`, et sort non-zéro si un doublon existe. Et ajouter à la SKILL.md, agent 8 : « avant d'écrire une ligne à ID séquentiel, relire le fichier entier et prendre max(id)+1, jamais le dernier ID mémorisé en début de run ».

**Piège à éviter dans l'implémentation, vérifié sur ce run** : un check d'unicité naïf sur `predictions.jsonl` sort 6 faux positifs (P-2026-06-01-1, P-2026-06-01-v2-2, P-2026-06-06-v2-2, P-2026-06-06-v3-2, P-2026-06-10-v2-2, P-2026-06-15-2). Ce ne sont pas des collisions : ce sont des lignes de mise à jour de résolution, qui portent volontairement l'`id` de la prédiction qu'elles complètent et se distinguent par les champs `update_edition` et `status_update` au lieu de `date`, `edition` et `claim`. C'est le schéma append-only voulu. Le check ne doit donc porter que sur les lignes **définissantes** (celles qui ont un champ `claim` non vide), pas sur les lignes de mise à jour. Un check qui ignore cette distinction ferait échouer `validate.sh` sur une mémoire saine et bloquerait tous les commits.

**Décision demandée** : soit (1) appliquer le diff à `validate.sh` et à la SKILL.md, soit (2) appliquer seulement la consigne SKILL.md sans toucher au script, soit (3) laisser en règle mémoire humaine.

**Trace** : mistakes.jsonl M-011, renumérotation M-008/M-009/M-010 faite sur ce run.

### Q-2026-07-17-v2-4 : éclater le KPI du pilier 4 (AEO) de la méthode Organikk en vecteur à 4 grandeurs ?

**Contexte** : la fiche `concepts/methode-organikk-4-piliers` fait porter au pilier 4 (AEO) un KPI unique, « taux de citation dans les réponses génératives ». Le survey de 45 études du 15 juillet défend un vecteur de visibilité qui sépare explicitement quatre grandeurs qui ne bougent pas ensemble : découvrabilité (est-ce que le contenu entre dans l'ensemble retrouvé), citation (est-ce qu'il est cité une fois retrouvé), absorption factuelle (est-ce que son contenu passe dans la réponse même sans citation), résultat économique. Le papier Bridge Evidence renforce le point par un autre chemin : environ un tiers des documents causalement utiles à un agent ne ressemblent pas à des documents pertinents et n'apparaissent dans aucune réponse finale. Un taux de citation seul agrège donc quatre choses distinctes, et c'est précisément l'erreur de mesure que le survey reproche au marché.

**Décision demandée** : soit (1) modifier la fiche `methode-organikk-4-piliers` pour remplacer le KPI unique du pilier 4 par un vecteur à 4 composantes, soit (2) laisser la fiche et créer un concept séparé `vecteur-visibilite-geo` référencé depuis le pilier 4 et depuis `metriques-visibilite-geo`, soit (3) ne rien changer et considérer que le taux de citation reste le bon KPI opérationnel côté client, parce qu'il est le seul mesurable en pratique aujourd'hui.

**Trace** : claims.jsonl C-2026-07-17-v2-2 et C-2026-07-17-v2-3, édition 2026-07-17-v2 section « Connexions doctrine ».

### Q-2026-07-17-v2-5 : formaliser `metriques-visibilite-geo` avec une exigence de protocole ?

**Contexte** : la fiche `concepts/metriques-visibilite-geo` liste déjà en limites qu'aucun outil grand public ne calcule ces métriques et que les métriques 2024-2025 peuvent évoluer. Deux faits du 17 juillet durcissent la limite. Le survey rapporte que les audits commerciaux révèlent « low source overlap, substantial run-to-run variability, and persistent fidelity gaps », et propose un protocole reproductible (mesures répétées, paraphrases, contrôles, validation humaine, interférence multi-acteurs). Suganthan montre que deux comptes ChatGPT testés à la même période ne voient pas les mêmes canaux de retrieval (`bing` présent chez l'un, 0 sur 595 résultats chez l'autre). Conclusion opérationnelle : un relevé GEO qui ne documente pas le compte, son tier, sa géo et sa date de capture n'est comparable à rien.

**Décision demandée** : soit (1) ajouter à la fiche une section « Conditions de validité d'une mesure » avec les 4 éléments obligatoires (compte, tier, géo, date), soit (2) en faire une règle opposable dans les livrables clients Organikk (tout tableau de citations IA porte ces 4 mentions), soit (3) les deux.

**Trace** : claims.jsonl C-2026-07-17-v2-1 et C-2026-07-17-v2-6, predictions.jsonl P-2026-07-17-v2-1.

### Q-2026-07-17-v2-6 : le commentaire de `stable_runs_done` dans manifest.yml fait 45 605 caractères sur une ligne

**Contexte** : le champ `migration.stable_runs_done` du `manifest.yml` porte un commentaire YAML d'une seule ligne de **45 605 caractères**, dans lequel chaque run empile depuis des semaines le résumé intégral de son édition (sujet, chiffres, sources, prédictions, brèves). Le mot `stable_runs_done` apparaît 18 fois dans le fichier, presque toujours à l'intérieur de ce commentaire. Le run du 17 juillet après-midi a incrémenté le compteur à 94 sans rien ajouter au commentaire, pour ne pas aggraver le problème.

**Pourquoi c'est un problème** : (1) l'information est déjà stockée proprement et de façon requêtable dans `runs.jsonl`, avec un objet par run ; le commentaire en est une copie dégradée et non parsable. (2) Le manifest est le premier fichier que l'agent 0 lit à chaque run, donc ce bloc est rechargé en contexte à chaque édition pour zéro valeur ajoutée. (3) Un commentaire de cette taille sur une ligne rend le fichier illisible pour un humain et fragile à éditer, alors que c'est le fichier qui déclare quelle mémoire fait foi. (4) La croissance est illimitée et strictement monotone.

**Décision demandée** : soit (1) vider le commentaire et le remplacer par une ligne courte du type `# compteur de runs stables ; le detail par run vit dans ledgers/runs.jsonl`, soit (2) archiver le contenu actuel du commentaire dans un fichier `derived/stable_runs_log.md` avant de le vider (par prudence, même si le contenu est théoriquement redondant avec runs.jsonl), soit (3) laisser tel quel.

**Recommandation de l'agent** : option (2), puis inscrire dans la SKILL.md, section « Clôture du run », que l'incrément de `stable_runs_done` ne s'accompagne d'aucun commentaire, le détail allant dans `runs.jsonl`.

**Trace** : manifest.yml champ `migration.stable_runs_done`, incrémenté à 94 sans ajout de commentaire au run 2026-07-17-local-v2.


## Questions post-run 2026-07-19

- **Q-2026-07-19-1** (à valider en revue hebdo) : le SEJ passe à 4 useful hits en une seule édition (Forrester + Montti + Southern + Kaushik). Sa pondération actuelle risque de dominer la sélection. Faut-il capper explicitement une source à ≤ 2 hits par édition pour forcer la diversité, ou accepter la sur-représentation quand le SEJ concentre effectivement les faits frais de la semaine ? Tim tranche.

- **Q-2026-07-19-2** (mémoire) : le typo `décopurage` est réapparu dans l'édition 07-19 alors qu'il avait déjà été corrigé dans l'édition 07-12. Cela signale une reprise partielle du texte source lors de la rédaction. Proposition à valider : ajouter un check post-rédaction spécifique aux typos identifiés dans les 5 dernières éditions, alimenté par un fichier `memory/typos_a_surveiller.md` que l'agent maintient. Sinon, laisser le check libre.

- **Q-2026-07-19-3** (piste doctrine) : le cadre Forrester (persistance documentée sur Google + Bing, opacité sur ChatGPT) suggère une nouvelle fiche dans `wiki/concepts/` intitulée `fingerprint-persistance-cross-engine` qui articulerait les composantes du fingerprint (liens, schema, canonique, qualité par section) avec leur persistance mesurable par moteur. À valider en revue hebdo, ne pas créer seul. Rôle : compléter `metriques-visibilite-geo` par une lecture par moteur, pas par métrique.

- **Q-2026-07-19-4** (audit source) : la source `help.openai.com` (article 20001276) a été utilisée pour la 1re fois ce run comme primaire OpenAI (mise à jour app desktop). Elle mérite un statut trust = 0.85 (primaire éditeur, pas rumeur). Confirmer en revue hebdo son passage en `exploit` si un 2e hit utile suit sous 30 jours, sinon laisser `explore`.

- **Q-2026-07-20-v2-1** (corroboration data) : Perplexity Buy Now 2M shoppers actifs mensuels + 2B GMV run rate + take rate 8-12 pct rapporté par Ecommerce Times 2 juillet 2026 (repris par novadata.io). Aucun communiqué Perplexity officiel identifié ce run. Question : (a) chercher activement 2e source indépendante au prochain run (SEL, TechCrunch, Bloomberg, Reuters, Perplexity blog, S-1 futur), (b) sinon acter en revue hebdo que cette donnée reste en attente et ne peut pas devenir claim publiable tant que corroboration non trouvée. Rôle : ne pas laisser une source à fort impact en attente indéfiniment sans décision explicite.

- **Q-2026-07-20-v2-2** (règle dure explore renforcée) : à date, la règle dure explore dit qu'une source nouvelle ne suffit pas à publier un claim, il faut soit source connue soit 2 sources indépendantes dont 1 historique. La brève B3 Google Maps OpenTable retire ce run repose sur seroundtable + optimixed, deux sources connues mais optimixed republie fréquemment seroundtable — leur indépendance journalistique est faible pour un même fait cité comme scoop seroundtable. Question : (a) formaliser un critère « indépendance éditoriale entre 2 sources » dans la règle dure, (b) traiter automatiquement optimixed comme non-indépendant quand la source primaire est seroundtable (car recap). Rôle : éviter que 2 lignes de recap comptent pour 2 sources indépendantes dans la comptabilité claim.

- **Q-2026-07-20-v2-3** (concept doctrine) : la brève B1 NotebookLM/GeminiNotebook articule la limite « user-triggered fetchers pas robots.txt » avec `data-proprietaire`. Question à valider revue hebdo : cette limite mériterait-elle un concept dédié `robots-txt-non-directive-user-triggered-fetchers` dans `wiki/concepts/` pour être réutilisable en audit client sans recharger le contexte à chaque fois ? Rôle : capitaliser un point technique récurrent et sourçable (quote Google directe) plutôt que le re-citer à chaque brève.


## Questions ajoutées après 2026-07-22

- **Q-2026-07-22-1** (Kevin Indig comme source, statut) : le run 07-22 a utilisé growth-memo.com pour la 2e fois (après 07-02 sur reasoning modes). Passage exploit proposé, à valider en revue hebdo. Trust initial 0.75, à monter à 0.85 si passage confirmé.

- **Q-2026-07-22-2** (arbitrage GEO récidive) : le pilier GEO/mesure a été retenu en info du jour malgré la directive « ne pas ré-enchaîner GEO sans franchement neuf ». Justification : scale 3 ordres de grandeur (50 000 marques vs 12-50 précédentes) et question distincte (topic-level ownership longitudinal vs cross-model recognition ou category framing). Décision à valider ou à rétablir en revue hebdo : le seuil « franchement neuf » doit-il être formalisé par une règle (au moins 1 des 3 conditions : scale ×10, longitudinal, question distincte) ?

- **Q-2026-07-22-3** (surface produit non précisée) : Google annonce Gemini 3.5 Flash-Lite « rolling out in Google Search » sans préciser la surface exacte (AI Overviews, AI Mode, Deep Search, agent). Question à Tim : voulez-vous qu'on ouvre une prédiction pour chaque surface, ou une seule prédiction agrégée comme fait ? Choix agrégé retenu par défaut ce run (P-2026-07-22-3).


## Questions post-run 2026-07-25

- **Q-2026-07-25-1** (à valider en revue hebdo) : deux nouvelles sources explore ajoutées ce run — `blog.modelcontextprotocol.io` (trust 0.9, primaire mainteneurs MCP) et `workos.com/blog` (trust 0.72, secondaire technique auth). Le blog MCP est le seul primaire pour toute question de protocole (specs, release candidates, changelogs) : il mérite un passage direct en `exploit` sans attendre 2 runs corroborés, à condition que Tim valide la logique « seule source primaire officielle » = passage direct. Ou continuer la règle explore → exploit sur 2-3 runs par principe. À trancher.

- **Q-2026-07-25-2** (piste doctrine) : la spec MCP 2026-07-28 formalise 3 dépréciations (Roots, Sampling, Logging) hors du cœur du protocole, avec politique formelle de 12 mois. Cette bascule change le contrat d'usage pour les serveurs SEO existants (Semrush) ou futurs (Ahrefs, Similarweb, Screaming Frog). Proposition à valider : créer une fiche dans `wiki/concepts/` intitulée `mcp-protocole-agents` qui articule (a) les capabilities MCP par version, (b) les clients supportés, (c) les cas d'usage SEO documentés, (d) la mesure d'adoption sectorielle. Rôle : compléter `agentic-search` par une lecture protocolaire concrète, pas abstraite. À valider en revue hebdo, ne pas créer seul.

- **Q-2026-07-25-3** (règle prédiction) : P-2026-07-20-1 (reproduction Vishwakarma) est laissée ouverte ce run malgré la publication SIGIR peer-reviewed. Cette décision suppose que « publication formelle ≠ reproduction indépendante par équipe tierce ». Tim confirme-t-il cette distinction stricte, ou considère-t-il qu'une publication SIGIR peer-reviewed suffit à valider la prédiction ? La règle actuelle est stricte, à valider en revue hebdo. Si Tim assouplit, mettre à jour la définition de « validation » dans les prédictions.

- **Q-2026-07-25-4** (candidat exploit) : `digitalapplied.com` atteint 5 useful hits cumulés (ce run + runs précédents). Candidature forte au passage exploit en revue hebdo. Recommandation de l'agent : passage exploit acquis, la source produit des analyses techniques fiables et récurrentes.

- **Q-2026-07-25-5** (piste éditoriale prochaine édition) : la parution effective de MCP 2026-07-28 le 28 juillet (dans 3 jours) est un point de vérification. Faut-il prévoir une brève de vérification systématique dans l'édition du 29 juillet ou du 30 juillet (Actualité SEO), ou laisser au flux libre de l'agent la décision de couvrir la parution effective ? Recommandation de l'agent : brève systématique le 29 juillet pour valider que les changements annoncés sont bien tenus (utile pour le suivi des prédictions P-2026-07-25-1 et 2). À valider.

- **Q-2026-07-25-6** (limite du fact-check verdict par claim) : les claims C-2026-07-25-7 (adoption 9652 records) et C-2026-07-25-9 (verbatim Barbettini) sont publiés avec `independent_sources: 1` (Digital Applied unique), en attribution explicite. La règle actuelle autorise cela quand la source est historique + attribution explicite. Sur un fait chiffré d'adoption (9652 records), l'attribution suffit-elle ou faut-il durcir la règle à 2 sources indépendantes pour tout chiffre d'adoption ? À valider en revue hebdo.

- **Q-2026-07-25-7** (piste sourcing sectoriel) : aucune source française n'a émergé ce run sur MCP. La couverture technique française du protocole MCP est absente ou peu indexée. Proposition : identifier activement au prochain run une source française de référence sur les protocoles agents IA (Frenchweb, Journal du Net, Décideurs Numériques, etc.) pour équilibrer le sourcing linguistique sur un sujet international. À valider.



## Questions post-run 2026-07-27-v2

- **Q-2026-07-27-v2-1** (piste doctrine — révision fiche fraicheur-contenu) : l'étude Seer du 24 juillet 2026 impose une révision précise de [[concepts/fraicheur-contenu]] : le multiplicateur ~3× retenu est confirmé (Ahrefs juillet 2025 25,7 pct + GrowByData 3,2×) mais l'apport propre Seer est que c'est la date de mise à jour qui compte, pas la date de publication (72 pct paraissent fresh vs 42 pct réellement publiées). Proposition : mettre à jour la fiche pour (a) distinguer explicitement date-de-mise-à-jour vs date-de-publication comme deux axes de mesure séparés, (b) ajouter la variation par moteur (Gemini 78 / ChatGPT 73 / Perplexity 65 pct) et par industrie (marketplace 77-78 pct plus exigeante), (c) intégrer la mesure Seer comme source primaire de référence 2026. À valider en revue hebdo, ne pas modifier seul.

- **Q-2026-07-27-v2-2** (règle sourcing corroboration ancienne) : l'info du jour Seer 24 juillet 2026 est corroborée principalement par une étude Ahrefs de juillet 2025 (16,975M citations, un an ancien). La règle actuelle « au moins 2 sources indépendantes dont une avec historique dans sources.jsonl » est tenue (Ahrefs a un historique fort), mais la source de corroboration est un an ancienne. Question : faut-il durcir la règle en imposant que la corroboration principale ait au maximum 6 mois d'écart avec l'info fresh, ou tolérer une corroboration historique de référence datée explicitement dans le corps (comme fait ici) ? Recommandation de l'agent : tolérer une corroboration historique quand elle est explicitement datée et positionnée comme référence, sinon on écarte trop de fraîches qui prolongent des tendances documentées ailleurs. À valider.

- **Q-2026-07-27-v2-3** (règle brève adoption non-auditée) : la brève B1 sur les 10 000+ serveurs MCP repose sur une déclaration Anthropic-OpenAI-Google-Microsoft-AWS non-auditée par un tiers non-vendeur. La règle dure explore exige 2 sources indépendantes dont une historique ; ici 2 sources indépendantes (Tech Insider + The Register) sont présentes, l'ordre de grandeur est retenu au niveau déclaratif avec 4 limites méthodo explicites en corps (répartition interne/public, taux rétention, volume moyen requêtes, taux utilisation effective). Question : cette pratique de « chiffre-déclaration ordre de grandeur avec limites méthodo publiées » est-elle acceptable en brève, ou faut-il durcir la règle et exiger un chiffre audité tiers pour tout claim d'adoption chiffrée ? À valider.

- **Q-2026-07-27-v2-4** (candidat exploit) : `almcorp.com` continue de produire des hits utiles (Reddit Q1 2026 39M USD, plus rappels antérieurs). Candidature au passage exploit à évaluer en revue hebdo. Recommandation de l'agent : passage exploit acquis, la source produit des analyses financières et juridiques SEO fiables et récurrentes.

- **Q-2026-07-27-v2-5** (piste éditoriale prochaine édition) : Reddit publie ses résultats Q2 2026 le jeudi 30 juillet 2026 après clôture. La brève B2 anticipe cette publication comme fait procédural neuf. Faut-il prévoir une couverture info du jour systématique le vendredi 31 juillet 2026 sur les chiffres de licence data IA isolés + position officielle Reddit sur le renouvellement Google (pilier Business SEO fort avec fait franchement neuf attendu), ou attendre que l'agent décide de la pertinence selon la substance publiée ? Recommandation de l'agent : couverture info du jour ou brève selon la substance publiée par Reddit (chiffre isolé, verbatim direction sur renouvellement, ou silence procédural). À trancher jeudi soir.

- **Q-2026-07-27-v2-6** (règle dure explore contre Ahrefs juillet 2025) : la corroboration Ahrefs pour l'info du jour est un an ancien. Techniquement la règle dure explore/publication est tenue (Ahrefs = source connue historique + Seer = source connue historique + GrowByData = source connue historique via reprise Api Serpent + Contently). Cependant, si l'on considère « historique récent » comme <6 mois, seule Seer et GrowByData sont ≤6 mois. Question : la règle dure « au moins une source avec historique » doit-elle inclure une notion de récence pour l'historique lui-même ? Actuellement l'agent tolère un historique ancien tant qu'il est daté ; à valider si Tim veut ce durcissement ou non.

## Édition 2026-07-28 - Questions pour Tim (revue hebdo)

### Sources à discuter au passage exploit → exploit

- **novadata.io** (explore, trust 0,5) : aggregateur reprise Ecommerce Times, source non-primaire, non-audit. Utilisée ce run pour claim Perplexity Buy Now 2M/2Md USD faute de mieux, avec limites explicites. Question : garder ou retirer ? Alternative pour couvrir Ecommerce Times sans passer par un aggregateur ?
- **fool.com** (nouvelle explore, trust 0,65) : presse financiere US Motley Fool. Historique long, couverture earnings previews stocks. Candidate exploit pour couvrir plus systématiquement les résultats trimestriels Reddit/Alphabet/Meta et leur exposition à AI licensing.
- **bootcampdigital.com** (nouvelle explore, trust 0,60) : agence formation digitale US, roundup mensuel Meta/TikTok/LinkedIn. Utile pour reprise annonces vendor mais insuffisante seule. À corroborer avec source primaire vendor pour tout claim publié.

### Doctrine à formaliser potentiellement

- **Fiche doctrinale « point d'accès agent »** : la spec MCP 2026-07-28 stateless rend techniquement viable de considérer un serveur MCP comme un point d'accès distinct de la page web indexée par les crawlers. Cette distinction n'est pas encore dans [[concepts/agentic-search]]. Question : créer une fiche `wiki/concepts/point-acces-agent.md` ou étendre `agentic-search.md` ? Nécessite au moins 3-5 cas mesurés avant formalisation.
- **Doctrine « métrique containment rate »** : Meta introduit une métrique proche de ce que les vendors GEO commencent à instrumenter (Nudge, Kasper, Loftie). Question : la métrique de « conversation résolue sans transfert humain » devient-elle une dimension du filtre `test-substitution-llm` ? À poser en revue hebdo si autre vendor confirme.

### Pièges méthodologiques rencontrés ce run

- **Piège M-005 revisité** : Google AI Mode 53 langues (ALM Corp) - fait originel 5 nouvelles langues remonte septembre 2025, l'article reprend en fausse fraîcheur 2026. Écarté après vérification. Renforcement discipline : toujours ouvrir la source primaire (blog.google) pour vérifier date de première annonce avant de citer un chiffre. À noter dans mistakes.jsonl si repérage récurrent.
- **Règle dure explore borderline** : le claim Perplexity Buy Now 2M/2Md USD repose sur 2 sources coordonnées (Ecommerce Times primaire + Novadata reprise), aucune dans registre historique consolidé. La règle dure demande « 2 sources indépendantes dont au moins une a déjà un historique dans sources.jsonl ». Ni Ecommerce Times ni Novadata n'ont d'historique. Publié quand même comme brève avec limites explicites triples (source thin, pas de communication Perplexity, pas d'audit tiers), pas comme info du jour. Question Tim : la règle dure explore permet-elle ce compromis pour une brève, ou faudrait-il écarter complètement ? Précédents : 2026-07-03-v2 CiteLens 500 prompts single-vendor publié en info du jour avec limites explicites, précédent pour publication conditionnée à documentation des réserves.


## Q-2026-07-29 (auto-interrogation post-édition 07-29)

**Contexte** : L'édition 07-29 s'appuie sur une source (WebSearchAPI.ai / James Bennett) qui est mono-analyste non-vendeur mais qui exploite directement les endpoints Cloudflare Radar. Le claim principal est vérifiable en amont via Cloudflare Radar lui-même. La source explore siliconangle.com (trust 0.7) a servi de source primaire indépendante pour l'info du jour, corroborée par TechTimes (0.65) et CryptoBriefing (0.55).

**Question** : est-ce qu'une analyse mono-analyste qui exploite ouvertement une source primaire connue (Cloudflare Radar dans ce cas) doit être traitée comme corroboration indirecte de la source primaire, ou comme une source à part entière soumise à la règle des 2 sources indépendantes ? Actuellement je la considère comme 1 source distincte + Cloudflare Radar en amont validable = suffisant pour publier un chiffre, mais avec limite explicite dans le corps ("aucun autre analyste tiers non-vendeur n'a publié la même mesure").

**Proposition à valider en revue hebdo** : durcir la règle explore/publication en ajoutant un cas "corroboration par source primaire remontable" : quand une analyse exploite un endpoint public (Cloudflare Radar, developers.google.com, GSC, Ahrefs Site Explorer, Similarweb via widget public), l'analyse compte pour 1 source si l'endpoint est spécifiquement cité et vérifiable par le lecteur en un clic. Sinon, elle reste mono-source et le claim doit être flaggé fragile.

**Non bloquant** : à traiter à la prochaine revue hebdo (vendredi). L'édition 07-29 publie le chiffre avec flag explicit dans le corps.


## Q-2026-08-01-v2 (auto-interrogation post-édition 2026-08-01-v2)

**Contexte** : L'édition 08-01-v2 traite un déplacement doctrinal de Google Search Essentials (retrait d'une consigne officielle, Mueller maintient la recommandation en podcast Search Off the Record). L'événement est mineur en amplitude (une ligne retirée d'une page de documentation), mais structurel dans son mécanisme (la doctrine se retrouve exprimée uniquement dans des canaux de communication non-normatifs : blog Search Central, podcast, prises de parole individuelles Mueller/Illyes/Splitt/Sassman).

**Question 1 — création concept wiki** : le déplacement observé (consigne officielle vers canal secondaire) est un pattern qui touche plusieurs éléments de la doctrine SEO Google (types de données structurées supprimés en janvier 2026, clause internal search results retirée fin juillet 2026, distinction diminuée entre `noindex`/`nofollow`/robots.txt entre 2019 et aujourd'hui). Proposition : créer `wiki/concepts/search-essentials-doctrine-glissante.md` pour capturer ce pattern. Contenu proposé : (1) le mouvement de simplification continue depuis Search Essentials rename 2022, (2) trois exemples datés (structured data janvier 2026, clause internal search results retrait, quelque chose d'autre à identifier), (3) l'implication opérationnelle (tracer chaque recommandation à un document daté, distinguer document officiel vs communication non-normative dans les livrables), (4) l'implication doctrine (une exigence Search Essentials retirée ne signifie pas qu'elle est abandonnée, elle peut être portée par un canal moins accessible). À valider en revue hebdo.

**Question 2 — doctrine_fit faible** : ce run atteint doctrine_fit 2/5 uniquement, faute de concept précise interne wiki sur Search Essentials / crawl budget / robots.txt. Les concepts les plus proches (`e-e-a-t`, `detection-slop-coordonne`) sont des liens indirects. Question à Tim : y a-t-il un concept que je devrais retenir en priorité pour ce type de sujet, ou est-ce une réelle lacune de la doctrine wiki qu'il faut combler ? Alternative : accepter que ce type d'événement (déplacement doctrinal Google) est structurellement doctrine_fit faible et ne pas le pénaliser dans la grille.

**Question 3 — piège fake-fresh WebSearch résumés dates** : plusieurs recherches ce run ont retourné le sujet "Google internal search results" attribué à des dates incohérentes (SearchHerald agrège plusieurs mois, clickrank.ai qui attribue à Digital Phablet le podcast Google, plusieurs résumés qui parlent d'un épisode SOTR "récent" sans date précise). J'ai résolu en trouvant l'archive publique libsyn qui donne la date exacte 30 juillet 2026 pour l'épisode "Should you block your Search result pages?". Piège M-005 réplique : les résumés WebSearch pour des podcasts non datés interpolent des dates. Renforcement discipline : pour tout podcast/webinar/prise de parole, ouvrir l'archive publique du podcast (libsyn, Apple, Spotify RSS) pour vérifier la date d'épisode avant citation. Ne pas se fier à la date attribuée par WebSearch pour un podcast.

**Non bloquant** : Q1 et Q2 à traiter en revue hebdo (vendredi). Q3 renforce discipline anti-M-005 sans nouveau ledger mistakes (le piège a été détecté et évité en amont, pas commis dans l'édition).



## Q-2026-08-02-v2 (auto-interrogation post-édition 2026-08-02-v2)

**Contexte** : L'édition 08-02-v2 traite une étude vendor (geoSurge sortant de stealth) qui mesure quantitativement pour la première fois un mécanisme jusqu'ici qualitatif : le filtre mémoire pré-recherche appliqué par un modèle génératif (Gemini 3.5 Flash) avant de déclencher ses requêtes fan-out. Le résultat est de calibre doctrine (facteur 3,2 entre marques familières et inconnues, 55,7 pct vs 17,4 pct sur 3 960 réponses), mais la source est une source vendor unique (SEL Danny Goodwin est une reprise éditoriale, pas une reproduction indépendante).

**Question 1 — création concept wiki ou extension `metriques-visibilite-geo`** : le corps édition liste explicitement 6 dimensions successivement documentées de la visibilité GEO (persistance temporelle 14 juillet brandi.ai/Writesonic, recommandation nominative 14 juillet v2 Ahrefs Brand Radar, nommage marque texte vs URL 31 juillet v2 Writesonic ghost citations, propriété thématique cross-prompt 22 juillet Kevin Indig Semrush, cadence de mise à jour 27 juillet v2 Seer, auto-citation Google AI Mode 16 juillet Profound) et propose une 7e dimension pré-recherche (mémoire de marque comme filtre d'éligibilité aux fan-out queries). Proposition : soit étendre `wiki/concepts/metriques-visibilite-geo.md` avec une section « 7 dimensions documentées dans le temps » qui capture les 7 dimensions par ordre chronologique de première mesure publiée, soit créer `wiki/concepts/memoire-modele-pre-recherche.md` distinct. À trancher en revue hebdo. Ma préférence est l'extension (une seule fiche évite la fragmentation, et les 7 dimensions relèvent bien du même concept fondateur de visibilité GEO), mais création distincte serait justifiée si Tim considère la 7e dimension comme suffisamment structurellement différente (avant fan-out vs après citation).

**Question 2 — règle dure explore appliquée à un vendor sortant de stealth avec méthodologie ouverte** : geoSurge n'a aucun historique dans sources.jsonl (nouvelle source explore ce run) et vend un outil de mesure GEO. La règle dure explore demande « 2 sources indépendantes dont au moins une a déjà un historique dans sources.jsonl ». Search Engine Land (Goodwin) a historique exploit fort (trust 0,72, useful_hits 14). Cette configuration (vendor primaire nouveau + reprise éditoriale par source exploit historique) répond formellement à la règle. Mais elle repose sur le fait que la reprise SEL cite le rapport primaire, elle ne le reproduit pas. Question : est-ce que la règle dure devrait durcir un cas particulier « vendor sortant de stealth + reprise éditoriale d'une source de confiance historique » ? Proposition : oui, ajouter un cas particulier « vendor primaire nouveau » qui exige (a) publication ouverte de la méthodologie avec numérateurs/dénominateurs OU (b) une deuxième source indépendante qui reproduit ou audite la méthodologie. geoSurge coche (a). Sans (a), l'étude serait éligible en brève mais pas en info du jour.

**Question 3 — Product-Led SEO structurellement bloqué** : 9e directive consécutive de non-tenue « viser Product-Led SEO en info du jour » par manque de fait franchement neuf. Le pilier Product-Led SEO n'a pas été info du jour depuis mi-juin 2026. Les candidats identifiés cette édition (theStacc 2e cas P-2026-07-27-2, contre-cas / méta-analyse pSEO indépendante P-2026-07-27-1, nouveau outil Product-Led US, adoption mesurée Merchant Center AI Summary Insights, résolution GBP Products Pending Bug avec chiffre impact) ne se sont pas matérialisés. Question à Tim : est-ce que la directive doit être assouplie temporairement (accepter Product-Led SEO en brève plutôt qu'exiger info du jour) ou est-ce que la directive doit rester ferme et le pilier être considéré structurellement rare ? Alternative : identifier une source de découverte Product-Led SEO plus active (theStacc newsletter directe, ProductLed.com newsletter Wes Bush, Twitter/X @wesbush, Reddit r/SaaS) et en faire une source de veille explicite.

**Non bloquant** : Q1, Q2 et Q3 à traiter en revue hebdo (vendredi). Q1 (extension `metriques-visibilite-geo` avec 7e dimension) est le plus urgent, car la doctrine évolue plus vite que la formalisation wiki.


## Q-2026-08-03 (auto-interrogation post-édition 2026-08-03)

**Contexte** : L'édition 08-03 traite une synthèse Aleyda Solis (2 août) qui recouvre deux études empiriques primaires publiées antérieurement (SaaS 16 juillet, ecommerce 15 mai) et introduit le concept « corroboration threshold » pour expliquer pourquoi 84 à 93 pct du poids de citation IA en SaaS revient à des sources tierces, avec un facteur 2 entre sous-niches Accounting/Finance (16 pct first-party) et CRM/Collaboration (7-8 pct first-party). Le pilier Niche SEO priorité haute directive est tenu pour la première fois depuis un moment.

**Question 1 — création concept wiki `corroboration-threshold`** : Solis formule un concept qualitatif (« enough independent, credible sources saying similar things about you that the model becomes confident enough to commit ») sans publier de seuil numérique. Ce concept est le mécanisme causal invoqué pour expliquer la domination 3rd-party. Proposition : créer `wiki/concepts/corroboration-threshold.md` (draft) qui définit le concept comme mécanisme théorique de sélection de source par un système génératif, avec caveat explicite « seuil non chiffré publiquement, mesuré indirectement par la proportion first-party vs tierce dans la citation de sortie ». À valider en revue hebdo. Alternative : intégrer comme sous-section dans `wiki/concepts/metriques-visibilite-geo.md` (nouvelle 8e dimension mécanisme) plutôt qu'un concept distinct. Ma préférence est distinct : le concept touche le mécanisme causal (comment le système choisit), pas la métrique d'observation (que mesure-t-on).

**Question 2 — cross-ref avec 7e dimension métriques-visibilité-geo proposée en Q-2026-08-02-v2 Q1** : la 7e dimension « mémoire de marque pré-recherche » (geoSurge) et la nouvelle dimension proposée ce run « régime first-party vs tiers par sous-vertical » (Solis) sont-elles la même dimension ou deux dimensions distinctes ? Ma lecture : deux dimensions distinctes. La mémoire pré-recherche mesure l'éligibilité à être considérée comme source. Le régime first-party vs tiers mesure quelle source est effectivement citée. La première conditionne la deuxième mais elles se mesurent différemment. Question à Tim : cette lecture est-elle correcte pour la formalisation doctrine ?

**Question 3 — reproduction indépendante non-Solis prioritaire pour la boucle apprentissage** : la mesure Solis est intra-productrice (Solis publie 3 articles, dont 2 empiriques primaires et 1 synthèse). Elle atteint la règle dure explore parce qu'aleydasolis.com a un historique exploit fort (trust élevé, useful_hits historiques). Mais la validation de la thèse « facteur 2 Accounting/Finance vs CRM/Collaboration » nécessite une reproduction indépendante non-Solis. Prédiction P-2026-08-03-1 (échéance 30/06/2027) est le mécanisme de résolution. Question à Tim : est-ce que le run doit activement chercher une source alternative (Semrush AI Visibility Index, Ahrefs Brand Radar, Profound, Peec, Writesonic, autre consultant) qui aurait publié un chiffre équivalent sur les mêmes sous-verticaux SaaS, plutôt que d'attendre la prédiction ? Proposition : ajouter à la veille prochaine édition une recherche cible « 3rd-party vs first-party citation SaaS AI search » sur les 4-5 vendeurs mentionnés.

**Non bloquant** : Q1, Q2 et Q3 à traiter en revue hebdo (vendredi). Q2 est le plus urgent, car l'accumulation de dimensions non formalisées (mémoire pré-recherche + régime first-party/tiers) dilue la doctrine `metriques-visibilite-geo`.

## Q-2026-08-04-v2

### Q-2026-08-04-v2-1 — Le mot « visibility » institué par l'IAB comme label officiel : quelle nuance apporter à [[concepts/tabou-visibilite]] ?

**Statut** : à trancher en revue hebdo.

L'IAB a publié le 3 août 2026 « Measuring Visibility in the AI Era », qui institue « visibility » comme label industriel officiel de mesure de présence dans les moteurs génératifs. Or [[concepts/tabou-visibilite]] classe le mot « visibilité » comme mot à bannir dans un pitch commercial B2B services / freelance, avec pivot documenté 10 % → 50 % de closing en remplaçant par « mots-clés business / conversion / leads ».

Ces deux positions ne se contredisent pas mécaniquement : l'une relève de la mesure industrielle (catégorie utile), l'autre de la vente d'un devis à un décideur non-expert (mot qui casse la conversion). Mais elles créent une tension linguistique à documenter dans le concept.

**Proposition de diff sur `wiki/concepts/tabou-visibilite.md`** (à valider vendredi) : ajouter une section « Nuance industrie vs vente » qui note que le label institutionnel IAB est utile pour standardiser la mesure, sans le rendre acceptable comme argument de closing. Confidence : medium. À vérifier avec Tim si la nuance conforte ou fragilise la position.

### Q-2026-08-04-v2-2 — Cadre IAB comme candidat wiki/concepts/cadre-iab-4p-visibilite-ia.md ?

**Statut** : à trancher en revue hebdo.

Le cadre IAB (4 P Presence/Prominence/Portrayal/Persuasion + 2 tiers Directional/Decision-grade + seuil 50 requêtes) mériterait un concept propre dans le vault, distinct de [[concepts/metriques-visibilite-geo]] qui couvre les métriques algorithmiques (Aggarwal + SAGEO). Le cadre IAB est un cadre business, le concept metriques-visibilite-geo est un cadre technique. Les articuler l'un à l'autre est plus clair dans deux fiches qui se référencent que dans une seule.

**Proposition** : créer `wiki/concepts/cadre-iab-4p-visibilite-ia.md` (type : concept, tags : geo, mesure, iab, standard, visibilite-ia, project-eidos), avec description des 4 P, des 2 tiers, du seuil 50 requêtes, contributeurs nommés, lien vers PDF IAB. Ajouter une section « Articulation avec metriques-visibilite-geo » qui range chaque métrique Aggarwal dans un P IAB. Confidence : medium.

### Q-2026-08-04-v2-3 — Ihab Rizk (Microsoft Clarity) contributeur cadre IAB : cross-appointment à intégrer dans doctrine ?

**Statut** : signal d'observation, pas action immédiate.

MediaPost (Laurie Sullivan, 4 août) nomme Ihab Rizk (Senior Product Manager Microsoft Clarity) parmi les contributeurs du cadre IAB. Rizk est également l'auteur signataire de l'annonce Topic Insights Clarity du 9 juillet 2026 (v1 morning 08-04). Cross-appointment industriel : l'auteur d'une brique produit majeure de mesure GEO gratuite est simultanément contributeur d'un cadre normatif adopté par l'organisation professionnelle. Ce cross-appointment n'est pas discret et suggère une intention de Microsoft d'aligner sa brique produit sur le cadre normatif adopté par le marché avant d'autres.

**Observation à surveiller** : Microsoft Clarity publiera-t-il avant fin 2026 une grille de correspondance explicite entre ses colonnes (Topic Insights, Query Topics, Branded Query Segmentation) et les 4 P IAB (Presence, Prominence, Portrayal, Persuasion) ? Signal doctrine si oui : le cross-appointment était opérationnel, pas décoratif. À noter dans P-2026-08-04-v2-1 (l'outil qui bougera en premier pourrait bien être Clarity, ce qui rendrait la prédiction moins prédictive et plus attendue).


## Q-2026-08-05 (auto-interrogation post-édition 2026-08-05)

**Contexte** : L'édition 08-05 traite une synthèse Matt G. Southern SEJ (3 août 2026) qui croise deux études propriétaires (Uberall QSR Playbook mai 2026 + AthenaHQ State of AI Search Report 2026) et documente une mesure directement actionnable pour un consultant SEO local : 16,05 % des réponses IA sur un commerce local utilisent le domaine propre de la marque, 84 % viennent de sources tierces (Reddit 21,85 %, YouTube 10,32 %, sites d'avis). Nouvelle dimension doctrinale proposée : `Cit_ext(marque) = 1 - Cit_own(marque)` sur un panel de requêtes locales, distincte des 7 dimensions précédemment formalisées dans `wiki/concepts/metriques-visibilite-geo.md`.

**Question 1 — 8e dimension métriques-visibilité-geo à formaliser ou déjà formalisée en Q-2026-08-03-v2 Q1 comme « corroboration threshold » ?** : La dimension proposée ce run (part de citation domaine propre vs sources tierces, `Cit_ext` vs `Cit_own`) est-elle la même que la nouvelle dimension proposée 2026-08-03-v2 Q1 (« corroboration threshold ») ou distincte ? Ma lecture : elles se recoupent partiellement mais ne sont pas identiques. Corroboration threshold mesure le seuil qualitatif de sources indépendantes concordantes qui déclenche la confiance du modèle. `Cit_ext` mesure quantitativement la répartition domaine propre vs domaines tiers dans la sortie finale. La première est un mécanisme causal (comment le système choisit ce qu'il croit), la seconde une métrique d'observation. Elles peuvent coexister dans la même fiche `metriques-visibilite-geo.md` comme deux angles distincts : (i) `Cit_own vs Cit_ext ratio` (observation) et (ii) `corroboration threshold` (mécanisme). Question à Tim : formaliser les deux comme dimensions 8 et 9 distinctes, ou fusionner sous un même angle « signal source-based » ? Ma préférence est distinct : la mesure `Cit_own` est numériquement piloatable, le corroboration threshold est un mécanisme théorique invoqué mais non chiffré publiquement.

**Question 2 — traitement des études propriétaires vendor GEO datées de plusieurs mois** : Les données Uberall (mai 2026, 3 mois) et AthenaHQ (2026, date précise non publique) sont propriétaires, gated derrière download, méthodologie complète non ouverte en clair. L'article de Matt Southern est une synthèse éditoriale de sources qu'un consultant ne peut pas répliquer sans acheter les rapports. La règle anti-M-005 impose de dater explicitement les données > 30 jours et de flaguer la source vendor. Ce run le fait dans le corps. Mais faut-il durcir la règle pour les études propriétaires vendor GEO spécifiquement ? Proposition : ajouter à `voix-synthetic.md` ou `wording_rules.md` un cas particulier « étude vendor propriétaire » qui exige (a) datage explicite de la période de collecte (pas juste de la publication), (b) mention de l'accessibilité (gated / open) dans le corps ou en caveat final, (c) invitation à reproduire par le lecteur si possible (mini-panel de 20 requêtes sur ChatGPT + Gemini + Perplexity). Ce run coche (a) et (b) et (c). À trancher : formaliser la règle ?

**Question 3 — Product-Led SEO reste 14e directive consécutive non tenue en info du jour** : Malgré Pie / Amex Ventures / MoeGo distribué en brève ce run, aucun fait Product-Led SEO franchement neuf éligible à l'info du jour n'a été identifié depuis le 27 juillet (theStacc pSEO). La liste des candidats à surveiller est stable : theStacc 2e cas nommé (P-2026-07-27-2), contre-cas / méta-analyse pSEO indépendante (P-2026-07-27-1), 4e étude sectorielle Solis (P-2026-08-03-2), adoption mesurée Merchant Center AI Summary Insights (P-2026-08-02-3), résolution GBP Products Pending Bug avec chiffre impact (P-2026-08-01-v2-2), nouveau outil Product-Led US lancé. Question à Tim : Pie (packagé en SaaS + distribution vertical) peut-il constituer un candidat Product-Led SEO en info du jour si nous obtenons des chiffres d'adoption effective par PME utilisatrice sur le panel MoeGo 10k+ ? Autrement dit, faut-il élargir la définition de « Product-Led SEO » pour inclure les tools packagés qui outillent la citation IA (Pie AI Search) et pas seulement les cas Wise/Zapier/Canva de pages-comme-produit ?

**Non bloquant** : Q1 (8e dimension distincte ou fusionnée avec corroboration threshold), Q2 (règle vendor GEO propriétaire), Q3 (élargissement définition Product-Led SEO) à traiter en revue hebdo (vendredi). Q3 est le plus opérationnel : il conditionne le prochain sujet Product-Led SEO éligible en info du jour, qui est bloqué depuis 14 éditions.

**Diff de skill proposé** : aucun ce run. Le skill `agent-synthetic` a bien tenu la boucle sur ce cycle (briefing → veille → recoupement → fact-check → rédaction → apprentissage). La discipline anti-M-005 sur les études propriétaires anciennes datées explicitement dans le corps est un pattern reproductible qui pourrait devenir une règle explicite dans `voix-synthetic.md` (voir Q2).

**Sources nouvelles à valider en revue hebdo** : athenahq.ai (trust 0,65 vendor GEO primaire, rapport State of AI Search 2026, corroborée via SEJ Southern 3 août), globenewswire.com (trust 0,75 wire release primaire, Cequence 30 juillet), developers.cloudflare.com (trust 0,9 vendor primaire doc, Block AI Bots classification), blog.modelcontextprotocol.io (trust 0,9 primaire MCP spec 2026-07-28), martechseries.com (trust 0,7 media adtech, Pie coverage). Les 8 autres sources nouvelles (citybiz, pulse2, retailtechinnovationhub, vmblog, manilatimes, securitymea, finsmes, releasebot) sont des sources secondaires ou wire syndication (trust 0,55-0,65), à surveiller sur 2-3 hits utiles avant décision passage exploit.

## Q-2026-08-06 (revue hebdo)

### Q1 — Nouvelle fiche concept `risque-plateforme-actif-seo`

Le run 2026-08-06 documente le cas Google Blogger (bug d'enforcement automatique 4-5 août, compte à rebours à 89 jours sur des blogs de 12 à 18 ans). La doctrine actuelle `arbitrage-plateforme-publication` traite le choix de plateforme comme un arbitrage vers là où Google envoie le clic. Le cas Blogger relève d'une classe distincte : plateforme d'hébergement propriété du même moteur qui juge le contenu, risque d'enforcement automatique documenté, valeur d'actif SEO longue durée exposée.

Proposition : créer une fiche concept `wiki/concepts/risque-plateforme-actif-seo.md` distincte, avec 3 axes : (1) surface d'exposition (hébergement + juge = concentration de risque), (2) mécanisme d'enforcement (scan automatique + compte à rebours + faux positifs), (3) plan de portage (sauvegarde + domaine propriétaire + procédure de récupération). Doctrine à valider en revue hebdo.

### Q2 — Nouvelle dimension `langue-de-fetch` dans `metriques-visibilite-geo`

L'étude Serraris 5 août SEL 484251 mesure sur 272 sites Bing + 26 propriétés ChatGPT un biais anglais dans le fetch AI (ChatGPT 65-79 % pages EN, index 2,6). Cette dimension n'est pas couverte par les 3 métriques Aggarwal (Imp_wc, Imp_pos, Subjective Impression) ni par les 8 dimensions ajoutées récemment (persistance-temporelle, recommandation-nominative, nommage-marque-vs-url, propriete-thematique-cross-prompt, cadence-mise-a-jour, auto-citation, pre-recherche, cit_ext/cit_own).

Question : ajouter langue-de-fetch comme 9e dimension distincte à `metriques-visibilite-geo`, ou la fusionner dans entites-vectorielles (biais d'ancrage sémantique par langue) ? Ma préférence : dimension distincte, puisque la mesure est comportementale (quelle langue le moteur va chercher) et pas sémantique (quel vecteur est ancré).

### Q3 — Tolérance Weglot vendor SaaS pour corroboration secondaire directionnelle

Weglot rapporte un gain de +327 % en visibilité AI Overviews + ChatGPT pour sites avec traductions, utilisé dans la brève GEO comme corroboration secondaire directionnelle de Serraris. Weglot est un vendor SaaS de traductions, méthodologie non publique, chiffre marqué direction non valeur.

Question : la règle wording_rules doit-elle spécifier explicitement les cas où un vendor SaaS peut servir de corroboration secondaire directionnelle sans franchir la règle dure explore (une source explore ne suffit jamais à publier) ? Ma proposition : oui, si (a) marqué explicitement corroboration directionnelle, (b) chiffre traité comme direction pas valeur, (c) source primaire différente porte le claim principal. À trancher en revue hebdo pour formaliser dans `memory/wording_rules.md`.
