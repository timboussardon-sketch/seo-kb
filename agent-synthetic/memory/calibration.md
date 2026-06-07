# Calibration — score de l'agent dans le temps

Écrit par l'agent 9 après chaque édition. Confronte le travail de l'agent à la réalité. C'est la mesure honnête de « est-ce que l'agent s'améliore ».

## Les 4 critères (note /5 par édition)

1. **Recoupement** : part des infos du corps corroborées par au moins 2 sources indépendantes.
2. **Angle inédit** : l'édition sort-elle quelque chose que les autres n'ont pas vu ?
3. **Lien doctrine** : l'actu est-elle reliée aux concepts de Tim ?
4. **Hook intelligent** : le titre prouve-t-il la valeur sans être racoleur ?

## Signaux de vérité-terrain

- **Interne** : taux de survie au fact-check, justesse des prédictions échues (voir `predictions.jsonl`).
- **Data réelle** : opens et clics (voir `engagement.jsonl`, branché plus tard).

## Journal des scores

| Édition | Recoupement | Angle | Doctrine | Hook | Survie fact-check | Note globale |
|---|---|---|---|---|---|---|
| 2026-05-30-v2 | 4/5 | 5/5 | 4/5 | 4/5 | 4 retenues / 6 candidates | 4,2/5 |
| 2026-05-30-v3 | 5/5 | 5/5 | 5/5 | 4/5 | corps 100% recoupé ≥2 sources | 4,7/5 |
| 2026-05-30-v4 | 5/5 | 3/5 | 5/5 | 4/5 | 8 retenus, corps recoupé ≥2 sauf 1 fragile attribué | 4,3/5 |
| 2026-05-30-v5 | 5/5 | 4/5 | 4/5 | 4/5 | 6 claims retenus, corps recoupé ≥2 sauf FAQ (doc officielle) et 11 % (mono-étude flaguée) | 4,3/5 |
| 2026-06-01 | 5/5 | 3/5 | 4/5 | 4/5 | 7 claims retenus tous recoupés ≥2 ; 1 claim préliminaire (secteurs FR) gardé avec caveat explicite, pas compté comme établi | 4,1/5 |
| 2026-06-02-v2 | 5/5 | 4/5 | 5/5 | 4/5 | 6 claims retenus ; corps recoupé ≥2 sources avec historique (info du jour), 1 chiffre vendeur (Shopify x8/x15) marqué fragile et attribué, 1 lecture (FourWeekMBA) attribuée | 4,4/5 |
| 2026-06-06-v3 | 5/5 | 4/5 | 5/5 | 4/5 | 15 claims retenus (4 info du jour + 3 Web IQ + 3 Amazon-Perplexity + 2 Adobe + 3 doctrine/réutilisables) ; corps recoupé ≥2 sources indépendantes pour chaque claim publié ; 5 claims écartés (Liz Reid redite, GEO Measurement isolée, Goodie Claude mono-source, Seer claim non confirmé, Glenn Gabe redite matin) | 4,6/5 |

### Notes 2026-06-06-v3

- **Recoupement (5/5)** : info du jour portée par primaire blog.google + 3 secondaires indépendantes (getpassionfruit, interestingengineering, techwyse) avec corroboration sur exemples cités. Brève Web IQ : primaire blogs.bing.com + 4 secondaires indépendantes (SEL, SEJ, PPC.land, Neowin). Brève Amazon-Perplexity : 4 sources indépendantes (SEJ, MediaPost, Law360, docket CourtListener primaire). Brève Adobe : primaire Adobe + 2 secondaires (e-commerce.news, dbbnwa). Règle dure explore tenue : aucune source nouvelle isolée ne porte un claim.
- **Angle (4/5)** : 1re fois que la générative UI I/O 2026 est traitée sous l'angle Product-Led SEO. La doctrine product-led-seo + filtre test-substitution-llm fournit le cadre d'évaluation et permet de mesurer ce que l'annonce déplace dans le filtre. Pas 5/5 car l'annonce générative UI date de mai 2026 et a déjà été couverte par d'autres sources sous d'autres angles ; le neuf est la doctrine, pas le fait.
- **Doctrine (5/5)** : ancrage direct sur product-led-seo (thèse centrale), test-substitution-llm (filtre à réécrire), data-proprietaire (défense qui tient), fully-meets (score max product-led). Cas Victoria Garden documenté dans la KB sert de référence opérationnelle. Lien doctrine non décoratif.
- **Fact-check, ce qui a été cadré** : chiffre Adobe Q1 2026 marqué « base clients Adobe » et « direction agrégée, pas état universel du marché » ; rappel Seer 93 % sans clic AI Mode mis en regard plutôt que claim neuf ; quote Liz Reid « biggest upgrade » écartée du corps car déjà citée v4 0530 (redite). Le claim que AI Mode embarquerait des calculateurs/simulations en direct selon Seer (lu dans le résumé nobori.ai) écarté faute de confirmation Seer primaire.
- **Méthode** : sur une annonce de plate-forme déjà couverte par la presse, le levier de différenciation est la doctrine propriétaire (product-led-seo + test-substitution-llm + cas Victoria Garden) qui mesure ce que l'annonce déplace dans le filtre. Trois défenses identifiées (donnée propriétaire, persistance d'état, accès stocks) bornent le sujet sans forcer une thèse univoque. Conforme à la voix (assumer l'incertitude là où le déploiement n'a pas eu lieu).
- **Prédictions ouvertes** : P-2026-06-06-v3-1 (filtre étendu à l'UI générative), P-2026-06-06-v3-2 (perte mesurée sur calculateur substituable vs résistance des pages branchées sur données propriétaires).

### Notes du run d'amorçage (2026-05-30-v2)

- **Recoupement** : info du jour (Information Agents) triple-sourcée (blog.google primaire + Lumar + SEJ). Brèves sur 1 à 2 sources.
- **Angle** : choisi distinct de l'édition du matin (guide AEO du 15 mai) pour éviter la redite. Information Agents = angle frais et méta.
- **Fact-check, ce qui a été écarté du corps** : étude Yext « 86 % de citations brand-managed » (octobre 2025, hors fenêtre fraîcheur 30 j) ; chiffre d'overlap citations vs top-10 organique (BrightEdge, conflit 54 % vs 17 % selon méthode, mono-source) ; le « +157 % » de renvois ChatGPT laissé en qualitatif (mono-analyse). Conforme à la règle anti-hallucination.
- **À surveiller** : pas encore de signal lecteur (engagement.jsonl vide tant que l'envoi n'est pas branché).

### Notes 2026-06-02-v2

- **Recoupement (5/5)** : info du jour portée par sources indépendantes avec historique, blog.google (primaire, 11 janv. 2026) et Search Engine Land (secondaire, 20 mai 2026) pour les attributs de découverte, plus Google Cloud et OpenAI (primaires) pour l'existence et les dates des standards UCP/ACP/AP2. Règle dure explore tenue : aucune source nouvelle ne porte seule un claim.
- **Angle (4/5)** : pilier Recherche agentique, angle de la couche de découverte de l'achat agentique (unité = flux structuré, multi-interfaces, multi-standards). Distinct du 0601-v2 (accès adversarial/autorisation), du 0530-v3 (annonce UCP/checkout) et du 0601-v3 (éligibilité native_commerce). Comble une limite explicite de la fiche `agentic-search` (l'agent qui agit, mal couvert empiriquement) sur le cas de l'achat.
- **Doctrine (5/5)** : ancrage réel sur `agentic-search` (sélection par l'agent vs liste de liens), liens secondaires non décoratifs `product-led-seo` (version agent-friendly API/embed) et `know-simple-know-do` (pages Do exécutables par un agent).
- **Fact-check, ce qui a été cadré** : chiffres Shopify x8/x15 attribués comme direction vendeur, pas valeur de référence ; issue « marchands supportant plusieurs standards » donnée comme lecture FourWeekMBA, le fait corroboré étant l'existence de standards distincts. Écartés du périmètre : extension crypto x402/stablecoins d'AP2 et détails Visa TAP/Mastercard (couche paiement, hors search).
- **Méthode** : faute d'événement neuf de la semaine sur ce pilier, synthèse opérationnelle ancrée sur les faits datés les plus récents (GML 20 mai, amicus EFF/Mozilla 9 avril) plutôt que fausse fraîcheur. Novelty 4/5 atteinte sans événement neuf.

### Notes 2026-05-30-v3

- **Recoupement (5/5)** : info du jour (commerce agentique / Universal Cart / UCP) sur primaire Google (blog.google 19 mai) + Search Engine Land (20 mai) + docs Google Merchant. Chaque brève sur ≥2 sources indépendantes (core update : SEL + SEJ ; Cloudflare : Radar + TechnologyChecker ; conversion : Seer + Similarweb).
- **Angle (5/5)** : commerce agentique = l'agent qui ACHÈTE, explicitement distingué des Information Agents (qui lisent) traités en v2. Angle « ton flux produit devient ta vitrine » non vu ailleurs dans la presse FR.
- **Doctrine (5/5)** : branché sur `mots-cles-actionnels` (transactionnel = seuls KW qui font du CA) et `agentic-search` (être sélectionné par l'agent pour accomplir une tâche). Phrase doctrine « on ne vend plus du trafic, on vend de la performance ».
- **Piège anti-hallucination déjoué** : les résumés de WebSearch dataient à tort de 2026 des études de 2025 (Seer juin 2025 / Cloudflare juillet 2025). Vérif sur source primaire → Seer daté honnêtement dans le corps, Cloudflare repivoté sur les données fraîches du 18 mai 2026. Leçon enregistrée dans le registre (note sur seer-interactive et cloudflare-radar).
- **Écarté du corps** : ratios crawl-to-refer précis type 13 528:1 (cités par agrégateurs mais non confirmés sur primaire à la bonne fenêtre) → remplacés par la formulation corroborée « des dizaines de milliers de pages pour un visiteur ». Parts ChatGPT 68 % / Gemini 18 % (Similarweb, données janv. 2026, hors fenêtre 30 j) → non utilisées comme brève.
- **Prédictions ouvertes** : P-2026-05-30-2 (vente via checkout agentique avant 2026-09-30) et P-2026-05-30-3 (Googlebot sous 27 % du crawl IA d'ici fin 2026).

### Notes 2026-05-30-v4

- **Recoupement (5/5)** : info du jour (llms.txt non utilisé par Google) sur 3 sources indépendantes dont Search Engine Land (seed historique) : Illyes au Search Central Deep Dive APAC du 23 juillet 2025, Mueller (comparaison meta keywords) confirmé par 2 sources, incident d'apparition du fichier sur des pages Google sur 2 sources. Chaque brève sur ≥2 sources (Gemini : Similarweb + TechRadar + TechnologyChecker ; champ de recherche : blog.google + Tom's Guide + SEJ ; CTR AIO : SEL + Seer + SEJ).
- **Angle (3/5)** : volontairement plus bas. Overlap thématique partiel reconnu avec le run cloud du même jour, dont l'info du jour était le guide IA du 15 mai (« llms.txt inutile, AEO=SEO »). Le hook v4 est distinct (la contradiction : Google dit non, mais le fichier est apparu sur ses propres pages) et apporte du matériel neuf (citation Illyes datée, comparaison Mueller, incident, étude SE Ranking 39 000 domaines, benchmark SAGEO). Mais ce n'est pas un sujet vierge, d'où 3/5 et non 5/5.
- **Doctrine (5/5)** : lien réel et non décoratif vers `structural-information-geo` (le levier au retrieval = champs structurels + schema, pas un fichier dédié) et `aeo` (être cité = SEO normal, pas un canal séparé). La donnée empirique de la KB et la position de Google convergent.
- **Piège fraîcheur géré** : étude Seer du CTR AIO datée explicitement dans le corps (publi SEL 24 avril 2026, données jan2025-fév2026), au-delà de 30 j donc présentée comme tendance, pas comme état du jour. Parts Gemini/ChatGPT : chiffres exacts contradictoires entre Similarweb/Statcounter/agrégateurs → présentés comme divergence assumée, direction seule retenue.
- **Écarté du corps** : « planning queries +80 % » et « marques citées +35 % de clics » issus des annonces I/O (mono-source com Google ou redite avec la brève Seer plus solide). SE Ranking 39 000 domaines gardé mais marqué fragile et attribué (mono-source).
- **Prédiction ouverte** : P-2026-05-30-4 (position « llms.txt non utilisé » maintenue par Google d'ici fin 2026).

### Notes 2026-05-30-v5

- **Recoupement (5/5)** : info du jour (formats publicitaires Gemini dans AI Mode, GML du 20 mai) sur 2 sources indépendantes, dont la primaire blog.google + Search Engine Land (seed historique). Brèves : OpenAI ads (SEL x2 + SEJ), divergence citations (Averi + Profound, direction recoupée), Ahrefs 38 % (Ahrefs + SEJ), FAQ (doc officielle Google Search Central). Une seule info du corps tient sur une source unique : la dépréciation FAQ, mais c'est une doc officielle de l'éditeur lui-même (recoupement inutile), citation textuelle.
- **Angle (4/5)** : la publicité payante dans la réponse générative n'avait pas été traitée. Distinguée explicitement de v3 (checkout agentique organique via UCP) : ici l'angle est l'emplacement payé étiqueté « Sponsored », et la distinction citation organique / achat d'espace. Le rapprochement Google (GML) + OpenAI (ChatGPT ads) sur le même principe d'étiquetage est l'apport propre de l'édition.
- **Doctrine (4/5)** : lien réel vers `aeo` (la publicité ne remplace pas la citation organique : deux voies distinctes) et `agentic-search` (paiement natif UCP dans la réponse = être sélectionné pour transiger). Lien non décoratif mais l'actu publicitaire n'est pas au cœur de la doctrine GEO actuelle, d'où 4 et non 5.
- **Piège fraîcheur géré** : chiffre 11 % (Averi) explicitement présenté comme mono-étude ; seule la direction (faible recouvrement, sources distinctes) présentée comme corroborée. Caveat méthodologique d'Ahrefs (parsing amélioré → datasets non comparables) repris tel quel dans le corps.
- **Écarté du corps** : bilan gagnants/perdants du core update de mai (déploiement non clos avant ~4 juin, directive : attendre ≥1 semaine après la fin) ; chiffres d'audience I/O (2,5 Md MAU AIO, AI Mode 1 Md) redite v2/v4.
- **Prédictions ouvertes** : P-2026-05-30-5 (un format pub AI Mode sorti du stade annonce d'ici fin 2026) et P-2026-05-30-6 (recouvrement citations ChatGPT/Perplexity < 25 % confirmé d'ici fin 2026).

### Notes 2026-06-01

- **Recoupement (5/5)** : info du jour (core update mai, fin de deploiement) sur 4 sources independantes dont 2 seeds historiques (SEL, SEJ) + Search Engine Roundtable + Abondance. Faits proceduraux (2e core update, absence de billet, cadence 6-7 sem) recoupes SEL/SEJ/Digital Applied. Brèves : FAQ (SEL + SEJ + Passionfruit), composition des sources (SEJ + CMSWire/Conductor + PikaSEO), parts de marche (Digital Applied + Searchlab). Chaque info du corps sur >=2 sources independantes.
- **Angle (3/5)** : pas d'evenement totalement neuf cette semaine ; le materiel disponible recoupait beaucoup de themes deja traites (I/O, ads ChatGPT, recouvrement citations, FAQ). Angle retenu = la discipline d'attendre la fin du deploiement et les faits proceduraux (absence de billet, cadence resserree) plutot qu'une liste gagnants/perdants prematuree. Honnete et utile, mais novelty modeste : 3/5. Plusieurs sujets ecartes pour redite (loggues dans runs.jsonl sources_rejetees).
- **Doctrine (4/5)** : lien reel vers structural-information-geo (champs structurels = levier retrieval, coherent avec un update qui recompense le contenu citable/structure), pas decoratif. Pas force sur les brèves.
- **Hook (4/5)** : titre nomme l'evenement date et signale la posture (savoir que le rollout finit ~4 juin, pourquoi le bilan est premature). Non racoleur.
- **Ce qui a ete ecarté du corps** : remontees sectorielles FR gardees en preliminaire avec caveat, jamais comme constat etabli (deploiement en cours, echantillon faible, sources FR peu independantes entre elles). Figure "86% de chute immediate des citations Reddit" non retenue (mono-origine cmswire/pikaseo) au profit du -23% Conductor et du depassement YouTube, mieux corrobores.
- **Sources** : directive de l'amorcage enfin honoree, Abondance testee et ajoutee en explore (trust 0.7), corroboree. 3 autres explore ajoutees (digitalapplied, cmswire, searchlab). 2 sources sous le seuil laissees en attente dans questions.md (pikaseo 0.58, premiere.page 0.55).
- **Prediction nouvelle a echeance courte** : P-2026-06-01-1 (profil des perdants du core update, resolve_by 2026-06-30) permettra une boucle de calibration rapide des fin juin.

### Notes 2026-06-01-v2

- **Pilier (variation tenue)** : le run du matin etait pilier ACTUALITE SEO (core update). Cette edition prend pilier RECHERCHE AGENTIQUE, et traite Product-Led SEO pour la 1re fois en breve. Variation des piliers respectee, aucune edition centree sur un update Google.
- **Recoupement (5/5)** : info du jour sur sources multiples et independantes. Jurisprudence Amazon-Perplexity : Decrypt + CNBC + Yahoo Finance, sursis d'appel sur CyberScoop + PYMNTS. Blocage robots.txt OpenAI : eMarketer + Decrypt. Lisibilite machine : MarTech + commercetools. Seule exception signalee dans le corps : Cloudflare agent-readiness = source primaire unique a historique (trust 0.85). Breve GEO : Yext + SEL d'un cote, 5W/Muck Rack + Morningstar de l'autre (la contradiction elle-meme est l'objet). Breve Product-Led SEO : Averi/BrightEdge + Semrush (direction recoupee, chiffres exacts attribues).
- **Angle (4/5)** : angle propre = la visibilite agentique se decompose en acces autorise + lisibilite machine, distinct de la seule citation. Distinct de v3 (Google UCP, checkout cooperatif) : ici l'angle est l'acces adversarial (gating, blocage, jurisprudence) et la readiness mesuree. Comble une limite explicite de la fiche doctrine agentic-search (agent qui AGIT mal couvert empiriquement). Pas 5/5 car aucun evenement de fin mai : ancrage sur Cloudflare (17 avr) + jurisprudence (mars), dates affichees honnetement.
- **Doctrine (4/5)** : lien reel et non decoratif vers agentic-search (comble sa limite empirique declaree) et data-proprietaire (breve Product-Led SEO). Proposition d'ajout d'une section empirique a agentic-search posee en questions.md.
- **Hook (4/5, clickbait faible)** : titre nomme les deux conditions concretes (autorise + lisible), prouve l'analyse, aucune promesse creuse.
- **Piege fraicheur gere** : Yext date oct 2025 explicitement, ecarte de l'info du jour, recycle en breve comme cote d'une contradiction avec une etude de mai 2026. Trafic +805% date nov 2025 (Black Friday) explicitement dans le corps. Cloudflare 17 avr 2026, jurisprudence mars 2026 datees.
- **Sources** : 5 nouvelles explore corroborees au seuil (emarketer 0.72, decrypt 0.62, martech 0.7, yext 0.65, cyberscoop 0.6) ; 8 sous le seuil ou wire/vendeur laissees en attente dans questions.md. martech candidate exploit en revue hebdo.
- **Predictions nouvelles** : P-2026-06-01-v2-1 (part de sites declarant une preference d'agents > 4% d'ici fin 2026) et P-2026-06-01-v2-2 (appel Amazon-Perplexity non tranche au fond avant fin sept 2026).

### Notes 2026-06-01-v3

- **Pilier (variation tenue, directive honoree)** : les deux info du jour precedentes etaient Actualite SEO (matin) puis Recherche agentique (v2). Cette edition prend pilier PRODUCT-LED SEO pour la 1re fois en info du jour, comme demande par la directive v2. Aucune edition centree sur un update Google.
- **Recoupement (source_diversity 9/5 sur l'echelle, tres bon)** : info du jour sur deux etudes datees et independantes (Lily Ray 13 mai 2026 ; Search Engine Land 19 nov 2025), plus benchmark academique arXiv:2311.09735 et etude controlee Digital Applied 26 avr 2026. Chiffres Lily Ray (54/39/22%) attribues comme mono-etude sur echantillon oriente ; direction corroboree (Glenn Gabe Mount AI, doctrine interne -40 a -80%, Let's Data Science). Chaque info du corps sur >=2 sources independantes ou une source a historique.
- **Angle (novelty 4/5)** : angle propre = relier un fait neuf (etude Lily Ray, declin mesure du contenu IA a l'echelle) a la these strategique du Product-Led SEO (ce qui resiste = donnee propre + fonction non reproductible). Pas une redite : aucune edition anterieure n'avait traite l'etude Lily Ray ni mis Product-Led SEO en info du jour. La breve Product-Led de v2 portait sur donnees proprietaires/citation (BrightEdge/Averi) ; ici l'angle est le contraste declin-volume vs durabilite-donnee, distinct.
- **Doctrine (5/5)** : lien reel et exact. La doctrine seo-kb separe deja explicitement pSEO-sans-data (= thin content, limite declaree de programmatique-pseo) et product-led/data-proprietaire (= avantage non reproductible), et teste cette ligne sur le terrain (H-007 en-test, fiche preuve, jalon J+30 ~15 juin 2026). L'etude Lily Ray renforce la premisse cote risque. Ancrage non decoratif.
- **Hook (clickbait faible)** : titre nomme le pilier et le mecanisme (volume IA en recul / donnee propre et pages-outils qui resistent), sans chiffre choc en tete (variante avec le 54% ecartee pour eviter la sur-affirmation mono-etude). Aucune metaphore.
- **Piege fraicheur gere** : etude SEL datee nov 2025 (>30j) signalee explicitement dans le corps ; etude Digital Applied avr 2026, Lily Ray mai 2026, datees. La breve GEO traite frontalement le desaccord sur la fraicheur plutot que de reciter un chiffre "fraicheur" non controle.
- **Zero metaphore verifie** : evite "moat" (douve), "s'effondre/s'ecroule", "vague", "rails". Termes litteraux : "avantage structurel non reproductible", "perd l'essentiel de son trafic", "recul prononce".
- **Ecarte du corps / redite** : 5W Citation Source Index 680M (redite v5+matin), 126K pages indexees (mono-source promo), Profound Series C (hors perimetre), bilan gagnants/perdants core update (reporte, deploiement non clos). Loggues dans runs.jsonl sources_rejetees.
- **Sources** : 2 nouvelles explore corroborees au seuil (lilyraynyc 0.78, almcorp 0.6). lilyraynyc et digitalapplied candidates exploit en revue hebdo. 2 sous le seuil laissees en attente (letsdatascience 0.55, ziptie 0.5).
- **Predictions nouvelles** : P-2026-06-01-v3-1 (declin durable confirme par une etude independante d'ici fin 2026) et P-2026-06-01-v3-2 (effet fraicheur reste conteste apres controle DA).

### Notes 2026-06-02

- **Pilier (variation tenue, directive v3 honoree)** : les trois info du jour precedentes etaient Actualite SEO (0601 matin) -> Recherche agentique (v2) -> Product-Led SEO (v3). Cette edition prend pilier GEO / search IA, non pris en info du jour recemment, comme demande. Le core update mai reste une BREVE Actualite SEO (interdiction mono-Google respectee).
- **Angle (novelty 4/5)** : angle propre = l'ecart entre etre RECUPERE et etre CITE par un moteur generatif (85% des pages recuperees par ChatGPT ne sont pas citees, AirOps). Distinct des themes GEO deja traites : composition des sources (v2, 0601), recouvrement ChatGPT/Perplexity (v5), schema 2.3x (v3), fraicheur contestee (v3). Ici le sujet est la CONVERSION retrieval->citation et la chaine multi-etapes de selection, jamais traite. Reframe la metrique de visibilite (suivre la part citee, pas le classement).
- **Recoupement (source_diversity 8/5, bon)** : info du jour sur 3 sources independantes de nature differente : mesure empirique (AirOps, reprise par Search Engine Land 13 mars, source connue), cadre academique (arXiv:2603.09296, 11 mars), synthese de litterature (Passionfruit avr 2026, reprend independamment les 85%). Regle dure explore respectee : AirOps (nouvelle) portee par SEL (connue, historique) + 3e source. Breve core update : SEL + SEJ + Roundtable (3 connues). Breve Bing : SEJ (connue, mise a jour officielle verifiable). Breve GEO instabilite : Passionfruit synthetisant SparkToro + Profound, chiffres attribues aux etudes d'origine.
- **Doctrine (5/5)** : lien reel et exact vers metriques-visibilite-geo (Hit Rate au retrieval distinct de la citation finale, pipeline SAGEO par etape ; table 'ranking classique != GEO'). La decomposition en 4 etapes du preprint et les 15% d'AirOps sont la version empirique de ce pipeline theorique. Lien secondaire grounding-score (etape extraction). retrieval-collapse cite comme mecanisme DISTINCT (pollution du pool), explicitement non confondu. Ancrage non decoratif.
- **Hook (clickbait faible)** : titre porte la mesure (15% des pages que ChatGPT consulte apparaissent) et reframe l'enjeu (recupere != cite), prouve l'analyse, aucune promesse creuse. Variantes par la negative (85% ecartees) et vague (point de decision) ecartees.
- **Piege fraicheur gere** : AirOps et arXiv dates mi-mars 2026 (>30j) signales explicitement ; Passionfruit avr 2026 ; Bing 27 fev 2026 date. Seule la breve core update porte sur un evenement en cours (deploiement au 2 juin). Aucune fausse fraicheur.
- **Zero metaphore verifie** : evite "goulot d'etranglement", "moteur", "course", "tunnel". Termes litteraux : "etape qui decide", "chaine de selection", "ecart entre recuperation et citation", "consultees puis ecartees".
- **Ecarte du corps / redite** : 5W Citation Source Index 680M (redite v5/0601), Google I/O search agents + Gemini 3.5 Flash + Personal Intelligence (redite I/O, pas de fait operationnel neuf isolable), Perplexity+PayPal / "OpenAI arrete Instant Checkout" (commerce agentique deja traite + fait mono-source non confirme), bilan gagnants/perdants core update (reporte, donnees non stables). Loggues dans runs.jsonl.
- **Reserve assumee** : preprint arXiv = une seule source academique, presente comme CADRE et non fait ; aucun chiffre de reparation publie (non extractible du PDF, non hallucine). Affiliation des auteurs non assertee (sources divergentes Stanford vs Virginia Tech).
- **Sources** : 1 nouvelle explore corroboree au seuil (airops 0.7, etude data primaire portee par SEL+Passionfruit). search-engine-land/journal et getpassionfruit montent (compteurs + last_useful 2026-06-02). getpassionfruit candidate exploit en revue hebdo (3 hits, bonne source de synthese GEO).
- **Predictions nouvelles** : P-2026-06-02-1 (part des pages recuperees finissant citees < 30% confirmee par une mesure independante d'ici fin 2026) et P-2026-06-02-2 (instabilite temporelle des citations > 30%/mois documentee d'ici fin 2026).

## Édition 2026-06-03 (pilier GEO / search IA)

| Axe | Valeur |
|---|---|
| source_diversity | 9 sources indépendantes (SEL, 9to5Google, Google Search Central doc, PPC Land, getpassionfruit, SEJ, Search Engine Roundtable, PayPal Newsroom, Retail Systems) |
| claim_density | info du jour 5 claims verified / 3 brèves 1 chacune |
| novelty_score | 4/5 (mesure first-party de l'apparition en réponses IA + réglage d'exclusion séparé de la recherche, sujet non traité ; angle = ce que le rapport mesure vs ne mesure pas, mis en regard de la doctrine GEO) |
| doctrine_fit | 5/5 (`metriques-visibilite-geo` : apparition vs densité/position de citation `Imp_wc`/`Imp_pos`, limite « pas d'outil pour mesurer sur son propre site ») |
| redite_risk | faible (thème absent de said_index ; core update et agentique repris en brèves avec faits neufs datés) |
| clickbait_risk | faible (titre descriptif, mot « visibilité » évité) |

Note méthode : info du jour portée par 2 sources indépendantes (SEL + 9to5Google) + doc Google primaire pour l'ancien contrôle nosnippet, règle dure explore respectée. La réserve de mesure (sur-comptage des impressions reconnu le 3 avril 2026) a été intégrée comme caveat daté plutôt que tue, ce qui renforce la rigueur sans casser l'angle. Sondage SEL 33,2 % traité comme source unique à historique, attribué comme intention déclarée (pas comportement observé), placé en brève et non en claim porteur. Directive « tester une source de mesure de visibilité (Sistrix/Semrush Sensor/Mozcast) » toujours non tenue, à reporter.

## Calibration notation Brèves — 2026-06-03 (retour de Tim)

Premier retour terrain sur la grille `notation.md`. Tim : **« Gemini dépasse Perplexity est une grosse info »** → brève #4, que ma grille avait mise à 4,25 (coupe), aurait dû être **gardée/top**. Deux dérives de mon échelle corrigées :

- **Solidité — ne pas confondre « agrégé » et « fragile ».** Une donnée d'agence **corroborée par ≥2 agences indépendantes** qui concordent (ici Similarweb + Trakkr + AIVIS sur la montée de Gemini) vaut **Solidité 4**, pas 3. Le 3 est réservé à la source d'agence **unique** ou non recoupée. (Je sur-pénalisais l'origine agence même quand le fait était recoupé.)
- **Envie — une bascule de hiérarchie entre moteurs est une grosse info.** Un renversement de part de trafic/marché entre moteurs (qui dépasse qui) change la stratégie de tout le monde → **Envie 5**, pas 4. Je sous-notais le hook des faits structurels au profit des faits « spectaculaires ».

Re-score #4 après correction : Solidité 4, Envie 5, Original 4, Doctrine 4, +0,5 consensus = **4,75 → gardée** (au niveau de la #5). Échelle ajustée en conséquence pour les prochaines éditions ; règles ajoutées à `notation.md`.

## Calibration Brèves 2026-06-03 (session de verdicts en direct) — profil de goût

Tim a annoté en direct les brèves v2/v3. Bilan : je sur-notais systématiquement le **technique/infra**, l'**opérationnel** et le **niche produit**, et je sous-notais un **événement frais à enjeu** (CNN) en le confondant avec du déjà-vu thématique. Règles ajoutées à `notation.md` : porte fraîcheur ; Envie ≤2 pour technique/infra et conseil d'hygiène ; Pertinence/Doctrine ≤2 pour niche/produit ; « événement frais ≠ déjà-vu thématique ».

**Familles qu'il AIME** (viser haut) : conflits éditeurs/créateurs vs moteurs IA (procès/licences/copyright), bascules de marché entre moteurs, données de résultat business (conversion/revenu), contre-vérités mesurées, **nouveaux business/modèles en SEO-GEO**, **tendances GEO/SEO sur les réseaux sociaux (voix des praticiens/utilisateurs)**.

**Familles qu'il REJETTE** : technique/infra (crawl, 402, robots, protocoles), conseils d'hygiène (« complétez vos données »), niche/cycle de vie produit, vieux/déjà-vu.

Survivants de l'édition du jour après son goût : trafic IA convertit mieux (5/5), Gemini > Perplexity, CNN vs Perplexity (promu). Autorité de domaine = tentatif. → 3 confirmés. Confirme que le seuil 4,5 + son goût donnent peu de brèves/jour : prochaine veille à orienter vers les familles aimées, et probablement élargir la fenêtre à ~7 jours.

## Calibration Brèves 2026-06-03 (suite) — conflits, clarté, ton

- **Conflits éditeurs↔IA = pas une famille récurrente.** Tim a adoré CNN (affaire concrète, marquante) mais a jugé « null » la méta-observation « le marché se scinde, certains signent, d'autres attaquent ». Règle : au plus une affaire judiciaire marquante et concrète, jamais une méta-observation vague ni un thème de conflit répété. Le « qui monétise le contenu » passe mieux par l'angle business (modèles de rémunération) que conflit.
- **Clarté de l'intérêt (nouvelle porte implicite).** Sur la brève Reddit/RSL : « on comprend rien à l'intérêt de l'info ». Si l'on ne voit pas immédiatement pourquoi ça compte pour un consultant SEO/IA, on écarte. L'intérêt doit être évident en une phrase.
- **Ton : neutre et journalistique.** Retour Tim : « parle neutre et journaliste, pas d'émotion ni d'envolée lyrique, respecte la voix SyntheticBrain ». Bannir les formules d'auteur et chutes punchy (ex. « rater la marche », « être nommé ne suffit pas, encore faut-il être cliquable », « le métier qui paie est celui qui... »). Structure de chaque brève : fait → mécanisme → portée, décrits littéralement. Pas de métaphore, pas de chute rhétorique.

Édition v5 réécrite en conséquence (conflit + Reddit retirés, ton neutre, 10 brèves ≥ 4,5).


## Édition Algorithme 2026-06-06 — 1er run avec YouTube comme source de découverte

Grille : source_diversity 11, claim_density « info du jour 2 claims verified / 3 brèves », novelty 4/5, doctrine_fit 4/5, redite_risk faible, clickbait_risk faible. Gate équilibré passé.

- **Branchement YouTube testé avec succès.** La veille vidéo élargie (requêtes search/IA larges, pas seulement Claude×SEO) a surfacé 4 pistes publiées après recoupement primaire (Web Bot Auth, Ask.com, Search profiles, DuckDuckGo) et 1 piste écartée (montage Princeton/15 mai). Source `youtube-veille` en mode découverte : 1er hit utile loggé, jamais promue en exploit, aucun claim porté par la seule vidéo.
- **Tension de goût à arbitrer (honnête).** L'info du jour est Web Bot Auth, famille **technique/infra/protocole** que Tim sous-note explicitement en Brèves (calibration 2026-06... du 2026-06-03 : « Envie ≤2 pour technique/infra », rejet de « crawl, robots, protocoles »). Choisie ici comme info du jour Algorithme par exception « fait franchement neuf » de la directive, et par analogie avec le 0603 (rapport GSC, aussi technique, accepté en info du jour). MAIS un angle plus aligné sur le goût de Tim existait dans le même run : le signal de marché DuckDuckGo + l'aveu Microsoft (« l'IA résume et réduit les clics »), qui relève des familles AIMÉES (bascule entre moteurs, contre-vérité mesurée). Décision : garder Web Bot Auth en info du jour pour la nouveauté, signaler à Tim qu'il peut préférer basculer ce signal de marché en info du jour et reléguer Web Bot Auth en brève. À trancher en revue.

## Édition Algorithme 2026-06-06-v2 — ouverture publicitaire AI Mode à la santé (pilier Actualité SEO)

Grille : source_diversity 12, claim_density « info du jour 2 claims verified / 3 brèves (1-2 chacune, total 6 claims) », novelty 4/5, doctrine_fit 4/5, redite_risk faible, clickbait_risk faible. Gate équilibré passé.

- **Pilier respecté.** Directive après v1 du jour (Recherche agentique, Web Bot Auth) : viser Product-Led SEO ou Actualité SEO. Choix Actualité SEO, validé par la fenêtre fraîche (1-2 juin sur l'info du jour, 2-5 juin sur les brèves) et la disponibilité d'une famille aimée de Tim (bascule de marché publicitaire, verticale sensible qui s'ouvre).
- **Prédiction résolue partiellement.** P-2026-05-30-5 (« au moins un format publicitaire AI Mode sortira du stade annonce et accessible aux annonceurs aux US d'ici fin 2026 ») est partiellement validée par C-2026-06-06-v2-1 : un format est accessible, mais en test limité (US uniquement, anglais uniquement, santé uniquement, créations restreintes). Statut suggéré : `resolved-partial` à confirmer par Tim en revue, ou maintenir `open` jusqu'à généralisation hors test.
- **Directive SISTRIX enfin tenue après 6 répétitions.** Source primaire de mesure de visibilité (top 200 winners/losers US+UK, ~1M SERPs/jour) intégrée pour la première fois, sur le sujet exact pour lequel elle était demandée (bilan core update mai). À surveiller comme candidate exploit en revue hebdo si le bilan finalisé confirme la qualité du signal.
- **Doctrine fit 4/5, pas 5/5.** Les concepts mobilisés (aeo, google-ai-mode, data-proprietaire, e-e-a-t, agentic-search) sont reliés correctement mais sans qu'aucune fiche ne donne un angle décisif. Pour atteindre 5/5, il aurait fallu relier l'ouverture publicitaire santé à une fiche dédiée (ex. doctrine sur la cohabitation organique/payant dans la réponse IA, qui n'existe pas encore). Candidat de fiche à proposer à Tim : « pression publicitaire sur la surface IA, conséquences pour le rang organique cité ».
- **Risque d'over-Google.** 3 brèves Google dans la même édition (info du jour AI Mode santé, brève core update, brève spam policies). Compensé par 1 brève non-Google substantielle (Cloudflare bots > humains). À surveiller : éviter une édition future à 4 sujets Google.
- **Quoi améliorer.** L'angle business du test santé (cibles publicitaires, taille du marché US santé, marge des plateformes pub santé) aurait pu être chiffré avec une source business (eMarketer, Insider Intelligence). Cette piste a été identifiée mais non explorée pour ne pas dépasser le périmètre fact-check à verdict.

## Édition Algorithme 2026-06-07 — deux étiquettes Preferred et Highly Cited dans AI Mode et AI Overviews (pilier GEO / search IA)

Grille : source_diversity 11, claim_density « info du jour 6 claims verified / 3 brèves (3+3+2, total 10 claims) », novelty 4/5, doctrine_fit 5/5, redite_risk faible, clickbait_risk faible. Gate équilibré passé.

- **Pilier respecté.** Directive après 0606-v3 (Product-Led SEO) : viser GEO/search IA avec un fait franchement neuf. Choix Preferred Sources + Highly Cited (annonce 27 mai 2026, 11 jours), recoupé sur 5 sources indépendantes dont blog.google primaire. Le pilier varie correctement vs les éditions récentes (Product-Led 0606-v3, Actualité 0606-v2, agentique 0606, GEO 0603).
- **Doctrine fit 5/5 atteint.** Le lien avec [[concepts/metriques-visibilite-geo]] est précis et opérationnel : Preferred Sources sort du champ des 3 métriques existantes (Imp_wc, Imp_pos, Subjective Impression), introduisant un signal d'autorité déclarative par l'utilisateur. Highly Cited reste algorithmique mais sur une logique de concentration de citations entre éditeurs distincte de l'autorité de domaine classique. Cette décomposition est ce qui distingue l'édition d'un résumé de presse.
- **Goût de Tim partiellement servi.** L'info du jour relève de la famille « nouveau modèle de visibilité dans la réponse IA », plutôt que d'une bascule de marché ou d'un conflit éditeur/IA. Compensé par les brèves : Actualité SEO (motif gagnants/perdants core update, donnée de business via SISTRIX), Recherche agentique (mise en service Mastercard fin juin, business pur), Actualité IA (ChatGPT 1Md MAU, bascule de marché documentée). L'équilibre brèves respecte les familles aimées.
- **Prédiction P-2026-05-30-5 marquée comme consolidée par ce run** mais distincte du présent fait (formats publicitaires AI Mode vs étiquettes éditoriales). Pas de résolution supplémentaire.
- **Quoi améliorer.** L'angle « combien de sites profitent déjà du badge Preferred et avec quel CTR mesuré côté éditeur » n'a pas pu être chiffré côté source tierce (Google publie le 2× sans méthodologie). Une mesure indépendante (Ahrefs, Semrush, Sistrix sur un échantillon) clarifierait l'effet réel. À garder en veille pour une prochaine édition.
- **Sources nouvelles utiles.** 8 ajoutées en explore : xpert.digital (récap volatilité multi-outils), sensor-tower (données primaires apps mobiles), androidheadlines, themobileindian (relais annonce Google), paymentsdive (press B2B paiements, primaire), europeanfinancialreview, reuters-via-investing, usnews-money. paymentsdive et reuters-via-investing sont des candidates au passage exploit en revue hebdo (sources de référence pour fintech et wire respectivement).
