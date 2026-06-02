# Questions de l'agent — « comment faire mieux »

Écrit par l'agent 10 (auto-interrogation) à chaque édition. Deux niveaux :
- **Urgent** : remonté à Tim tout de suite (en bas du draft).
- **Hebdo** : groupé, présenté à la revue hebdo du vendredi.

L'agent répond lui-même à ce qu'il peut tester ; il garde pour Tim ce qui demande un arbitrage humain.

## Urgent (à trancher vite)

(vide pour l'instant)

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
