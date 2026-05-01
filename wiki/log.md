# Log

> Journal chronologique append-only. Parseable via `grep "^## \[" wiki/log.md`.

## [2026-04-11] bootstrap | Init du vault
- AGENTS.md v1.0 créé
- stubs wiki/ (index.md, log.md) créés
- prochaine étape : ingest de raw/articles/karpathy-llm-wiki.md

## [2026-04-11] schema-upgrade | AGENTS.md v1.0 → v2.0 SEO-first
- remplacement complet du schéma par la version SEO-first
- ajout §2 doctrine propriétaire de Tim (factuel, zéro bullshit, angle original, preuves atomiques)
- ajout §4 taxonomie SEO avec sous-catégories entities (algos / outils / acteurs / concurrents / QRG / concepts-marque) et source_type (article / paper / doc-google / gsc-export / client-note / transcript / test-terrain)
- ajout §7 hooks vers les 12 skills SEO propriétaires
- frontmatter : ajout `source_type` (obligatoire pour type=source) + `aliases`
- tentative d'ingest v1.0 avortée puis nettoyée via git reset + git clean (7 fichiers partiels supprimés)

## [2026-04-11] ingest | LLM Wiki (Karpathy)
- source_type: article
- source: [[sources/2026-04-11-karpathy-llm-wiki]]
- entities touchées: 4
- concepts touchés: 5
- pages créées: 10 / mises à jour: 1
- contradictions: N (aucune KB préexistante à confronter)
- angle SEO identifié: fondationnel — source méta qui justifie la méthodologie de cette KB ; pas d'angle SEO opérationnel direct. Applications (RAG vs wiki dans SGE/ChatGPT Search/Perplexity ; compoundage appliqué aux exports GSC ; convergence doctrinale avec §2 AGENTS.md) renvoyées à des queries dédiées, nourries par d'autres sources à venir.

Détail :
- entities créées (4): [[entities/karpathy]] (Acteurs), [[entities/obsidian]] (Outils SEO), [[entities/vannevar-bush]] (Acteurs historiques), [[entities/notebooklm]] (Concepts-marque / Produits IA)
- concepts créés (5): [[concepts/persistent-wiki-vs-rag]], [[concepts/ingest-workflow]], [[concepts/query-synthesis]], [[concepts/cli-tools-optional]], [[concepts/obsidian-as-ide]] — tous sous la rubrique "Méthode KB / Fondations" (nouvelle sous-catégorie concepts, la §8 ne prévoyait que AEO-GEO / SEO technique / Stratégie contenu ; aucune ne fittait une source méta)
- index mis à jour: [[index]] (création des subcategories v2.0 de §8)
- synthèse: reportée (décision : attendre 2-3 sources qui se croisent avant de compiler)

## [2026-04-11] angle-pivot | Karpathy LLM Wiki — angle 1 → angle 4
- source concernée: [[sources/2026-04-11-karpathy-llm-wiki]]
- ancien angle: 1 (meta / fondationnel)
- nouvel angle retenu: 4 (wiki compilé ↔ Grounding Score)
- raison: Tim préfère un angle opérationnel spéculatif fertile plutôt qu'un constat méta inerte
- modif: section "Implications SEO" de la source page réécrite (garde "rien dans la source ne mentionne Grounding Score — c'est une inférence structurelle depuis cette KB")
- dépendance ouverte: pas encore de [[concepts/grounding-score]] dans le wiki. À créer quand un paper retrieval vectoriel, une doc Google neural matching, ou un test terrain viendra la nourrir.
- query cible à filer plus tard: wiki-pattern-vs-grounding-score

## [2026-04-11] schema-upgrade | AGENTS.md v2.0 → v2.1
- ajout: 8e `source_type` → `doctrine` dans §4.3 et §5.1
- définition: analyse propriétaire de Tim, thèse perso, cross-référence de papers, hypothèses SEO/IA non encore validées
- motif: `raw/notes/seo-ia-tim.md` ne fittait aucun des 7 types précédents (ni article publié, ni paper académique, ni doc Google, ni export GSC, ni note client, ni transcript, ni test terrain pur)
- impact: permet d'ingérer proprement les notes doctrinales de Tim sans forcer une catégorie impropre

## [2026-04-11] schema-upgrade | AGENTS.md v2.1 → v2.2
- ajout §4.1: sous-catégorie "Architectures IA" pour entities (titans, miras, mamba-2, transformer, gpt-4)
- précision §4.1: concepts-marque étendu avec notebooklm et google-deepmind
- motif: `entities/titans` ne fittait aucune sous-catégorie existante (ni Algo Google — Titans est DeepMind Research, pas Search, ni Outil SEO, ni Concept-marque au sens strict)
- impact: permet de nommer les architectures de recherche IA citées dans les analyses SEO/GEO sans les confondre avec les algos en production

## [2026-04-11] ingest | Analyse Titans/MIRAS → SEO (Tim)
- source_type: doctrine
- source: [[sources/2026-04-11-seo-ia-tim]]
- entities touchées: 3 (toutes créées)
- concepts touchés: 5 (tous créés)
- pages créées: 9 / mises à jour: 2
- contradictions: N (compoundage avec concepts Karpathy existants, pas de contradiction)
- angle SEO identifié: angle 4 nourri structurellement — l'hypothèse "wiki compilé ↔ Grounding Score" (source Karpathy) trouve ici son mécanisme (surprise metric + weight decay + neural memory). concepts/grounding-score enfin créé. Rétro-link karpathy appliqué.

Détail :
- entities créées (3): [[entities/google-deepmind]] (Concepts-marque), [[entities/titans]] (Architectures IA v2.2), [[entities/metehan]] (Acteurs, confidence low — article non ingéré)
- concepts créés (5): [[concepts/surprise-metric]] (AEO/GEO), [[concepts/grounding-score]] (AEO/GEO), [[concepts/weight-decay]] (SEO technique), [[concepts/surprise-gap]] (Stratégie contenu), [[concepts/ingenierie-semantique-inversee]] (Stratégie contenu)
- pages mises à jour: [[index]] (nouvelles sous-catégories + entrées), [[sources/2026-04-11-karpathy-llm-wiki]] (section Implications SEO rétro-linkée)
- dépendances ouvertes: article Metehan sur freshness scoring (confidence low tant que non ingéré)
- queries à filer: wiki-pattern-vs-grounding-score (matériau dispo), surprise-gap-application-briefs, persistent-vs-neural-memory-strategie

## [2026-04-12] batch-ingest | 6 newsletters Algorithme (fév-mars 2026)
- source_type: article (x6)
- sources:
  - [[sources/2026-02-27-algorithme-youtube-ai-overviews]] — YouTube 30% AI Overviews
  - [[sources/2026-03-04-algorithme-lancer-site-sans-cms]] — Test terrain indexation 3j
  - [[sources/2026-03-06-algorithme-etude-citation-ia]] — Benchmark GEO +41%/+30%/+30% + AI Overview -15%
  - [[sources/2026-03-11-algorithme-data-claude-perplexity]] — Data propriétaire + fact-checking + Low Surprise QRG p.42
  - [[sources/2026-03-13-algorithme-agents-seo-consultants]] — GEO basiques Hn +22% + agents SEO + GSC brand
  - [[sources/2026-03-17-algorithme-pourquoi-article-ne-rank-pas]] — SEO rédaction → SEO information
- entities créées: 2 (youtube, quality-raters-guidelines)
- concepts créés: 3 (data-proprietaire, information-gain, seo-multi-plateforme)
- pages créées: 11 / mises à jour: 1 (index)
- contradictions: N (compoundage pur avec les 10 concepts existants)
- angle SEO identifié: les 6 newsletters se croisent et nourrissent directement les concepts existants (surprise-metric, surprise-gap, grounding-score, weight-decay) avec des données empiriques (+41% citations, -15% AI Overview, +22% Hn retrieval) et des concepts opérationnels (data-proprietaire, information-gain, seo-multi-plateforme). Le réseau se densifie considérablement — chaque nouveau concept est lié à 3-5 concepts existants.

## [2026-04-12] query | Wiki persistant optimise-t-il structurellement le Grounding Score ?
- output: [[queries/2026-04-12-wiki-pattern-vs-grounding-score]]
- skill déclenché: none
- réponse: oui structurellement (5 mécanismes identifiés), non validé empiriquement. Test terrain proposé : page wiki entity vs page statique, mesurer citation IA.
- cette query était flaggée depuis l'ingest karpathy (angle 4). Matériau suffisant après 8 sources ingérées.

## [2026-04-12] synthesis | Doctrine SEO post-SGE — thèse unifiée
- output: [[syntheses/doctrine-seo-post-sge]]
- première synthèse de la KB, compile 8 sources + 13 concepts + 9 entities
- 4 piliers : grounding score, surprise gap, information gain, data propriétaire
- cadre architectural : Titans/MIRAS (hypothèse par transfert, confidence medium)
- infrastructure : pattern wiki persistant (Karpathy) comme mode de production GEO-optimisé
- grille de confiance incluse : benchmark +41%/+30% = high, transfert Titans → SEO = low
- questions ouvertes : test terrain wiki vs statique, article Metehan, paper retrieval SGE, export GSC

## [2026-04-12] batch-ingest | 7 bot instructions Tim (profil, règles, workflow, prompt, anti-AI)
- source_type: doctrine (x3 sources groupées depuis 7 fichiers raw)
- sources:
  - [[sources/2026-03-31-tim-profil-et-regles]] — about-me + my-rules + my-voice (3 fichiers)
  - [[sources/2026-03-31-tim-workflow-redaction]] — workflow 8 étapes + readme (2 fichiers)
  - [[sources/2026-03-31-tim-prompt-systeme-fusionn]] — prompt système Fusionn (1 fichier)
  - fichier raw anti-ai-writing-style (139 KB) intégré via concept, pas source page séparée
- entities créées: 1 (fusionn-io)
- concepts créés: 2 (workflow-redaction-8-etapes, anti-ai-writing)
- pages créées: 6 / mises à jour: 2 (index, ingenierie-semantique-inversee)
- contradictions: N
- angle SEO: les bot instructions documentent l'opérationnalisation complète du framework Tim. Le workflow 8 étapes est le pipeline qui produit du contenu GEO-optimisé selon la doctrine. Le wiki passe de "thèse théorique" à "système exécutable documenté".

## [2026-04-12] ingest | 10 skills SEO propriétaires (hooks §7 AGENTS.md)
- source_type: doctrine
- source: [[sources/2026-04-12-tim-skills-seo-proprietary]]
- 10 skills documentés : brief-contenu, cannibalisation, cluster-aeo, entites-vectorielles, maillage-interne, peurs-objections, product-led-seo, programmatique-pseo, quick-win, workflow-article
- pages créées: 1 / mises à jour: 1 (index)
- contradictions: N
- concepts transversaux identifiés : surprise-gap (7/10 skills), grounding-score (6/10), data-proprietaire (6/10), information-gain (5/10)
- liens rouges détectés : e-e-a-t, fully-meets, aeo, agentic-search, passage-ranking, rrf — concepts §4.2 AGENTS.md pas encore créés comme pages wiki. TODO pour prochain lint ou session stubs.

## [2026-04-12] stubs | 6 concept stubs (liens rouges → bleus)
- pages créées: 6 (e-e-a-t, fully-meets, aeo, agentic-search, passage-ranking, rrf)
- toutes en status: draft, confidence: low ou medium
- motif: résoudre les 6 liens rouges détectés lors de l'ingest des skills
- impact: 0 liens rouges dans Obsidian, graph view complètement connectée

## [2026-04-13] batch-ingest | 4 papers (titans, miras, QRG 2026, semrush)
- source_type: paper (x3) + doc-google (x1, QRG)
- sources créées:
  - [[sources/2026-04-13-titans-architecture-google-deepmind]] — citation primaire paper, upgrade des 5 concepts dérivés (surprise-metric, weight-decay, surprise-gap, grounding-score, information-gain) qui transitaient via seo-ia-tim (doctrine)
  - [[sources/2026-04-13-miras-architecture]] — extension Titans, fondement architectural passage-ranking (chaque H2 = vecteur), affine grounding-score
  - [[sources/2026-04-13-google-quality-raters-guidelines-2026]] — `doc-google`, source primaire normative pour e-e-a-t / fully-meets / anti-ai-writing / data-proprietaire (Experience pillar)
  - [[sources/2026-04-13-semrush-llm-conversion-study]] — preuve quantitative GEO 4x conversion ChatGPT vs Google, nourrit aeo / data-proprietaire / seo-multi-plateforme
- entités créées: 1 ([[entities/miras]])
- entités mises à jour: 2 (titans +1 source, quality-raters-guidelines +1 source, TODO QRG résolu)
- concepts mis à jour: 12 (surprise-metric promu confidence medium→high ; passage-ranking, e-e-a-t, fully-meets, aeo passés draft→stable, low→medium/high ; data-proprietaire 4→6 sources ; grounding-score +section MIRAS multi-résolution ; etc.)
- pages créées: 5 (4 sources + 1 entité) / mises à jour: 13 (12 concepts + 2 entités + index ; e-e-a-t/fully-meets/aeo/passage-ranking ne sont plus stubs)
- contradictions: N (compoundage pur)
- angle SEO identifié: les 4 papers consolident la base théorique de la doctrine. Titans/MIRAS transforment 5 concepts "transferts doctrinaux" (confidence medium via seo-ia-tim) en concepts "fondés sur paper primaire" (confidence higher). QRG transforme 4 stubs en concepts normatifs Google. Semrush apporte la première data dure de conversion GEO. La KB passe de "thèse construite" à "thèse sourcée".
- dépendances ouvertes: papers Titans/MIRAS sans lien original (préprints internes selon le raw) ; étude SEMrush sans lien public ; transfert architecture → ranking Google jamais confirmé publiquement

## [2026-04-13] batch-ingest | 3 notes bootcamp (offre, analyse calls, cas clients)
- source_type: doctrine (x2) + test-terrain (x1)
- sources créées:
  - [[sources/2026-04-13-offre-bootcamp-seo-ia]] — fiche produit complète bootcamp #4
  - [[sources/2026-04-13-analyse-calls-prospects-bootcamp]] — avatar + 6 douleurs + objections (9 calls)
  - [[sources/2026-04-13-cas-clients-resultats]] — preuves chiffrées Tim (test-terrain, 1h30→45min, 10→50% closing, top 2 balle de golf)
- entités créées: 1 ([[entities/bootcamp-seo-ia]], nouvelle sous-catégorie "Offres / Produits Tim")
- entités mises à jour: 1 ([[entities/fusionn-io]] +2 sources)
- concepts créés: 4 (nouvelle sous-catégorie Concepts "Vente / Peurs-Objections") :
  - [[concepts/avatar-freelance-sans-systeme]] (7/10 profils, umbrella avatar bootcamp)
  - [[concepts/cercle-vicieux-temps-structure]] (douleur #3, 8/10)
  - [[concepts/peur-train-ia]] (douleur #4, métaphore partagée 5+ prospects)
  - [[concepts/tabou-visibilite]] (doctrine vente, pivot closing 10→50%)
- concepts mis à jour: 1 ([[concepts/data-proprietaire]] 6→8 sources avec connexion argument vente)
- pages créées: 8 (3 sources + 1 entité + 4 concepts) / mises à jour: 3 (fusionn, data-proprietaire, index)
- contradictions: N (cohérence doctrinale Tim)
- angle SEO identifié: le batch alimente directement le **skill peurs-objections** (hook §7 AGENTS.md) avec matériau structuré (avatar + douleurs + objections + verbatims). Les transcripts sous-jacents (call-01..09) seront ingérés au batch 4 avec création des entities prospects individuelles — l'analyse est une "vue agrégée" qui pointera rétrospectivement vers eux. Connexion forte avec data-proprietaire : Tim vend la data (terrain + cas) vs "visibilité" — argument commercial et doctrine de contenu convergent.
- dépendances ouvertes: 9 entities prospects à créer au batch 4 ; résultats participants bootcamps #1/#2/#3 non documentés ; taux conversion call → inscription non mesuré

## [2026-04-13] batch-ingest | 2 scrapes Organikk (blog + glossaire)
- source_type: article (x2) — articles publiés sur organikk.co
- sources créées:
  - [[sources/2026-04-12-organikk-blog-scrape]] — 12 articles blog (audit 7 phases, SEMrush 42k pages, Grok pipeline, études cas serrurier/immo Lyon, etc.)
  - [[sources/2026-04-12-organikk-glossaire-scrape]] — 78 termes SEO/GEO/LLM (référence terminologique publique Tim)
- entités créées: 1 ([[entities/organikk-co]], sous-catégorie "Offres / Produits Tim")
- pages créées: 3 / mises à jour: 1 (index)
- contradictions: N (cohérence définitionnelle vérifiée sur 9 concepts majeurs entre glossaire public et KB interne — léger affinement "passage" vs "page" sur grounding-score, aligné avec l'ingest MIRAS ; divergence mineure sur MIRAS où le glossaire simplifie "multi-résolution" en "mémoire long-terme" — à surveiller)
- angle SEO identifié: le site Organikk est le **laboratoire public** de la doctrine KB. Les 12 articles sont à la fois matériau de vente (CTA bootcamp omniprésents), preuve de méthode (application skills sur cas) et signal E-E-A-T. Chiffres nouveaux : étude SEMrush 42k pages (80% positions #1 = humain, 9% IA ; contenu IA édité = 4% perf du 100% humain ; contenu IA brut ranke 23% plus bas) — **confirme normativement la p.42 QRG effort-less**. Le glossaire expose 7-8 termes candidats futurs (Perplexity AI, HCU, Topical Authority, Knowledge Graph personnel) non encore en KB — à créer quand des sources primaires viendront les nourrir.
- dépendances ouvertes: chiffres glossaire non sourcés (40% AI Overviews clics, 15M req/jour Perplexity, 90-99% autorité 301) à flagger avant réutilisation ; études de cas Lyon sans résultats clients chiffrés

## [2026-04-13] batch-ingest | 7 transcripts calls prospects bootcamp #4
- source_type: transcript (x7)
- sources créées (7):
  - [[sources/2026-04-13-call-01-arnaud]] · [[sources/2026-04-13-call-04-jamel]] · [[sources/2026-04-13-call-05-dev-web]] · [[sources/2026-04-13-call-06-juliette]] · [[sources/2026-04-13-call-07-christophe]] · [[sources/2026-04-13-call-08-franck]] · [[sources/2026-04-13-call-09-julien]]
- ⚠️ transcripts vides (2): raw/transcripts/call-02-marrusia-cecile.md et raw/transcripts/call-03-cecile-suite.md font 0 octet. Profil Cécile couvert uniquement via l'analyse-calls (citations secondaires, confidence low).
- entités créées (10, nouvelle sous-catégorie "Acteurs / Prospects Bootcamp" + 2 entités entreprises tierces):
  - Prospects (8): arnaud, marrusia-cecile, jamel, dev-web-anon, juliette, christophe, franck, julien
  - Entreprises tierces: audopass (Christophe), jumpto (Franck)
- pages créées: 17 (7 sources + 10 entités) / mises à jour: 1 (index)
- contradictions: N
- angle SEO identifié: les transcripts **individualisent** le matériau agrégé de l'analyse-calls batch 2. Chaque prospect devient un nœud citable dans les futures productions (skill peurs-objections, posts LinkedIn, syntheses vente). Audopass = **cas GEO in the wild** empirique unique (1/30 produits convertit via ChatGPT) → gisement pour test terrain "pourquoi ça ne réplique pas" à relier à l'angle 4 Karpathy ([[queries/2026-04-12-wiki-pattern-vs-grounding-score]]). Christophe apporte aussi le **contre-message senior** qui neutralise la peur du train IA pour les profils 40+/avec historique — à intégrer dans le copy marketing.
- dépendances ouvertes: Cécile profil fragile (transcripts vides, confidence low) ; Franck/Julien transcripts s'arrêtent avant closing (pas d'info sur réaction prix) ; data Audokit non chiffrée (combien de conversions ChatGPT, sur quel volume) ; statut final d'inscription de chaque prospect non consolidé dans la KB — Jamel seul confirmé inscrit via citation transcript Christophe

## [2026-04-13] skill revue-presse-iteration | Newsletter Claude Code + Obsidian sans complexité
- output: [[revues-presse/2026-04-13-claude-code-obsidian-sans-complexite]]
- skill déclenché: revue-presse-iteration (hook §7 AGENTS.md)
- angle: documenter publiquement le setup utilisé ce matin (2h, 18 fichiers raw → 28 sources / 32 entités). Angle terrain, pas théorique.
- passage ancré: §2 (setup technique minimal, 150 mots, dans les 300 premiers) — optimisé Featured Snippet / AI Overview
- doctrine appliquée: anti-AI writing (prose continue, pas de règle de 3, pas de méta-intro, pas de conclusion-résumé, pas d'emojis) ; factuel (chiffres de la session du matin, 6 ans d'itération, 0/9 prospects utilisent Claude Code correctement) ; pas de "visibilité" ; limites explicites avant CTA
- status: draft (à relire par Tim avant publication Substack)
- 2026-04-13 relu et validé par Tim → status: stable ; correction date bootcamp "dernière semaine d'avril" → "première semaine de mai" (cohérence avec décalage 1er mai férié discuté dans [[sources/2026-04-13-call-07-christophe]])

## [2026-04-13] skill linkedin-post-tim | Post LinkedIn teaser — supprimé
- output initial: posts-linkedin/2026-04-13-claude-code-0-sur-9.md (supprimé à la demande de Tim)
- motif suppression: non documenté

## [2026-04-13] ingest | Stratégie pSEO Victoria Garden Bordeaux (1er client-note de la KB)
- source_type: client-note (premier de la KB)
- source: [[sources/2026-04-13-victoria-garden-pseo]]
- entité créée: 1 ([[entities/victoria-garden]], nouvelle sous-catégorie "Clients Tim" sous Acteurs)
- concept créé: 1 ([[concepts/test-substitution-llm]] — méthode propriétaire formalisée à partir du livrable : filtre binaire "si LLM produit 80% → ne pas créer", 5 idées validées / 2 rejetées sur le cas VG)
- concepts mis à jour: 2 (data-proprietaire 8→9 sources, fully-meets 1→2 sources avec exemple opérationnel calculateur budget)
- pages créées: 3 / mises à jour: 3 (data-proprietaire, fully-meets, index)
- contradictions: N
- angle SEO identifié: la stratégie VG matérialise la doctrine en livrable opérationnel — test substitution LLM = opérationnalisation binaire de [[concepts/data-proprietaire]] et [[concepts/surprise-gap]]. 5 modèles pSEO chacun adossé à des données propriétaires identifiées (pricing, stock, partenariats, événements). 3 pages déjà livrées par Claude Code (calculateur budget, agenda événements, comparateur coût) — gisement de mesure terrain à venir (positions, trafic, conversions). Premier vrai test grandeur nature de la doctrine [[syntheses/doctrine-seo-post-sge]] sur un client réel.
- dépendances ouvertes: volumes mots-clés sans source explicite (Semrush/Ahrefs interne à confirmer) ; baseline trafic VG Bordeaux pré-pSEO non documentée ; résultats 3 pages livrées non encore mesurés ; stratégie scope Bordeaux uniquement, équivalent Pau à venir

## [2026-04-13] batch-ingest | 2 méga-prompts pSEO opérationnels (produit/service + non-produit)
- source_type: doctrine (x2)
- sources créées:
  - [[sources/2026-04-13-prompt-pseo-produit-service]] — méga-prompt e-commerce/SaaS/services, 7 règles non-négociables, structure XML 5 balises (role/context/task/rules/constraints)
  - [[sources/2026-04-13-prompt-pseo-non-produit]] — variante média/éditorial, +1 règle anti-substitution + Étape 0 obligatoire (Test ChatGPT 3 questions + 7 exemples pass/fail)
- concepts créés: 2
  - [[concepts/programmatique-pseo]] — 1 template × 1 variable = N pages longue traîne, 4 sources convergentes
  - [[concepts/product-led-seo]] — produit embarqué = page (calculateur/simulateur/configurateur), Fully Meets structurel
- concepts mis à jour: 1 ([[concepts/test-substitution-llm]] 1→2 sources : VG = cas d'application, prompt non-produit = formalisation systémique avec 3 questions)
- pages créées: 4 / mises à jour: 2 (test-substitution-llm, index)
- contradictions: N (les 2 prompts sont explicitement complémentaires, leur différentiel est documenté dans le prompt non-produit lui-même)
- angle SEO identifié: les 2 prompts opérationnalisent les concepts test-substitution-llm + programmatique-pseo + product-led-seo en interface concrète skill → livrable. La doctrine passe de "principe" à "mode d'emploi reproductible". Le critère différenciant prompt-A vs prompt-B n'est PAS le secteur du client, c'est la présence d'une donnée que seul le client possède (moat naturel produit/service vs absence de moat naturel non-produit). Cas Victoria Garden = matérialise le prompt produit/service avec ses 7 règles + bonus test substitution importé du non-produit (5/7 idées validées).
- dépendances ouvertes: prompts non testés sur sites non-produit dans la KB (média/blog/annuaire) — manque cas d'application analogue à VG ; règle 3 sourcing <3 ans peut être stricte sur secteurs réglementaires stables ; pas de mécanisme de fallback documenté si une donnée propriétaire annoncée par client n'existe pas vraiment

## [2026-04-13] skill seo-brief-contenu | Brief article organikk — Information Gain SEO/GEO
- output: [[briefs/2026-04-13-information-gain-seo-geo]]
- skill déclenché: seo-brief-contenu (hook §7 AGENTS.md)
- concept cible: [[concepts/information-gain]] (5 sources convergentes, confidence high)
- gap identifié via croisement KB ↔ scrap organikk ([[sources/2026-04-12-organikk-blog-scrape]]) : aucun article organikk ne couvre l'info gain comme sujet principal
- angle brief: "le benchmark +41% qui change la règle GEO" — hook data-driven factuel (étude arxiv 2311.09735, 10k requêtes, +41%/+30%/+30%)
- structure: passage ancré 150-200 mots + bloc authorship 50 mots + 7 H2 + FAQ + CTA, ~2500 mots cibles
- 7 règles non-négociables appliquées (contenu unique, zéro hallucination, sourcing <3 ans, canonical, maillage différenciant, Surprise Score, Grounding Score)
- placeholders factuels flaggés: volumes mots-clés à vérifier Fusion/Semrush ; SERP top 10 à scraper avant rédaction ; exemple Tesla à adapter au secteur cible ; image OG à produire
- status: draft (brief prêt à exécuter, rédaction à faire)

## [2026-04-13] batch-ingest | 5 papers GEO/search LLM (Aggarwal, Jin/CORE, Chen/RAID, Kim/SAGEO, Wu/SearchLLM)
- source_type: paper (x5)
- sources créées:
  - [[sources/2026-04-13-geo-aggarwal-2024]] — paper fondateur GEO, KDD '24, source primaire du benchmark cité jusqu'ici via newsletter
  - [[sources/2026-04-13-core-ranking-jin-2025]] — CORE, manipulation de ranking LLM via review-based (Top-1 80%+), ProductBench
  - [[sources/2026-04-13-raid-gseo-2025]] — RAID G-SEO, 4W Deep Reflection, +4.72 Subjective Impression, AAAI 2026
  - [[sources/2026-04-13-sageo-arena-2025]] — SAGEO Arena, 170k docs, pipeline complet, structural info +22% Hit Rate
  - [[sources/2026-04-13-searchllm-2026]] — SearchLLM RedNote/Xiaohongshu, A/B prod +1.03% VCR, gated aggregation
- entités créées: 3 (nouvelle sous-catégorie "Ressources / Benchmarks")
  - [[entities/geo-bench]] (Aggarwal, 10k requêtes)
  - [[entities/product-bench]] (CORE, 15 catégories e-commerce)
  - [[entities/sageo-arena-benchmark]] (Kim, 170k docs pipeline complet)
- concepts créés: 4
  - [[concepts/metriques-visibilite-geo]] — Imp_wc, Imp_pos (PAWC), Subjective Impression (formalisation Aggarwal + extension Sageo)
  - [[concepts/answer-first-pattern]] — 3 sources convergentes (Aggarwal via Imp_pos, Sageo via placement, SearchLLM via Answer Firstness validé A/B)
  - [[concepts/structural-information-geo]] — title/meta/schema dominent body text au retrieval (finding Sageo unique)
  - [[concepts/4w-deep-reflection]] — méthode RAID opérationnelle Who/What/Why/How pour intent-modeling
- concepts mis à jour (7):
  - [[concepts/information-gain]] 5→6 sources + **correction chiffres** : Quotation +41 %, Stats +34 %, Fluency +30 %, Cite Sources +29 %, Authoritative **seulement +13 %** (pas 30 % comme la newsletter disait)
  - [[concepts/data-proprietaire]] 9→14 sources (les 5 papers convergent sur data propriétaire comme gate GE)
  - [[concepts/anti-ai-writing]] 3→4 sources — Keyword Stuffing −8 % confirmé empiriquement par Aggarwal
  - [[concepts/grounding-score]] 4→6 sources, confidence medium→high
  - [[concepts/passage-ranking]] 1→3 sources, confidence medium→high
  - [[concepts/agentic-search]] 1→4 sources, draft→stable, low→high
  - [[concepts/surprise-gap]] 2→4 sources, confidence medium→high
- sources mises à jour (2):
  - [[sources/2026-03-06-algorithme-etude-citation-ia]] — **downgradée en source secondaire** avec flag confidence medium (chiffres imprécis vs paper primaire)
  - [[briefs/2026-04-13-information-gain-seo-geo]] — corrections chiffres + ajout de la méthode Quotation Addition distincte de Cite Sources + méta description mise à jour avec Keyword Stuffing −8 %
- pages créées: 12 (5 sources + 3 entités + 4 concepts) / mises à jour: 10 (7 concepts + 1 source source-secondaire-flag + 1 brief + index)
- contradictions résolues: chiffres "+41%/+30%/+30%" de la newsletter Algorithme #3 imprécis par rapport au paper primaire — correction propagée à information-gain + brief + flag source secondaire
- angle SEO identifié: les 5 papers **forment un système cohérent** qui consolide la doctrine GEO de Tim. Aggarwal pose la base empirique et les métriques. Sageo étend en pipeline complet. RAID ajoute la méthode d'intent-modeling. CORE démontre le pouvoir du contenu textuel seul (ni backlinks ni domain authority). SearchLLM valide en production avec A/B test. Implications majeures : (1) GEO démocratise le SEO (sites rank 5 gagnent +100 %, top 1 perdent) — aligne sur positionnement bootcamp freelance/PME ; (2) le couple "Quotation Addition (+41 %) + Statistics (+34 %)" est le plus efficace empiriquement — oriente les briefs vers extraction de citations verbatim plutôt que vers ajout de liens ; (3) le schema markup + title + meta restent critiques (+22 % Hit Rate) — pas un reliquat SEO classique ; (4) l'answer-first pattern est désormais validé A/B en prod, plus seulement une best practice.
- dépendances ouvertes: aucune des études ne couvre l'agentic search au sens strict (agents qui agissent vs qui génèrent des réponses) ; arxiv ID 2603.10473 SearchLLM à revérifier (numérotation future atypique) ; pas de test sur corpus français ; reranking reste un bottleneck non résolu par toutes les méthodes (plafond effective rate à 70 %)

## [2026-04-13] correction doctrine | Newsletter Claude Code + Obsidian — formulation imprécise corrigée
- déclencheur : fact-check d'un lecteur pointant que ChatGPT Memory (OpenAI fév 2024) et Claude Code Memory (v2.1.59+, documentée code.claude.com/docs/fr/memory) existent et persistent entre sessions
- problème : la newsletter disait "Sur Claude web, chaque conversation redémarre à zéro" — factuellement faux au sens strict
- correction appliquée à [[revues-presse/2026-04-13-claude-code-obsidian-sans-complexite]] : section "Pourquoi ça change quelque chose" réécrite pour reconnaître l'existence de Memory et recentrer le point sur la distinction Memory (pour l'IA, 200 lignes MEMORY.md chargées, format propriétaire non exportable) vs Wiki (pour l'utilisateur, markdown bruts, git, navigation sans IA)
- concept créé : [[concepts/memory-llm-vs-wiki-persistant]] — verrouille la distinction factuelle (tableau 9 axes)
- mémoire leçon : vérifier la précision des formulations absolues sur les capacités LLM avant publication. Les features évoluent vite.

## [2026-04-14] schema-upgrade | AGENTS.md v2.2 → v2.3 (§11 anti-AI-writing obligatoire)
- déclencheur : Tim a audité mes rédactions récentes (propositions de titres newsletter) et constaté que j'appliquais partiellement [[concepts/anti-ai-writing]] — règle de 3 systématique, bullet points décoratifs, bold excessif en début de ligne
- ajout §11 dans AGENTS.md : règle de rédaction obligatoire avec 10 points d'auto-check avant livraison, déclencheurs explicites (rédige/écris/réécris/améliore/draft/corrige), workflow en 4 étapes, cas d'exception documentés (tableaux structurels, protocoles numérotés, code, citations)
- ajout règle 11 dans le résumé §10 : pointeur vers §11
- impact : toute demande de rédaction Tim → je dois relire [[concepts/anti-ai-writing]] avant de produire ET auto-vérifier après. Flag explicite si un point n'a pas pu être tenu (avec justification).

## [2026-04-14] schema-upgrade | AGENTS.md v2.3 → v2.4 (§12 workflow article obligatoire) + skill seo-workflow-article installé
- déclencheur : Tim a confirmé la règle "si tu dois réécrire ou rédiger un article, obligatoire de lancer ce workflow article, ne jamais fais sans"
- skill installé : ~/.claude/skills/seo-workflow-article/SKILL.md (généré à partir de raw/notes/skill-workflow-article.md, frontmatter Claude Code ajouté avec name + description triggers)
- ajout §12 dans AGENTS.md : règle de process pour articles longs (1500+ mots), distinction claire avec §11 (forme vs process), cas d'exception documentés (titre seul, hook, post court, brouillon rapide)
- ajout règle 12 dans le résumé §10
- distinction articulée : seo-workflow-article = 8 étapes seules / article-engine-pipeline = 5 phases complètes (RRF + FAQ + workflow + factcheck) qui invoque seo-workflow-article en phase 4
- impact : toute demande article complète déclenche maintenant un appel skill explicite, pas une réponse "à la main"

## [2026-04-15] cleanup | Revue de presse Algorithme déplacée raw/articles → wiki/revues-presse
- déclencheur : Tim avait stocké le draft dans raw/articles/ par convention, mais c'était une violation §3 (raw/ immuable) puisque le fichier était activement édité
- déplacement : raw/articles/algorithme-revue-presse-2026-04-13.md → [[revues-presse/2026-04-13-algorithme-revue-presse]]
- ajout frontmatter complet (type, status: draft, dates)
- ajout 4e brève AUSSI SUR LE RADAR : A-RAG (arxiv 2602.03442) — vérification factuelle des 3 outils cités (keyword search, semantic search, chunk read) confirmée via WebFetch arxiv
- emplacement final cohérent avec §7 AGENTS.md skill `revue-presse-iteration` qui prévoit déjà wiki/revues-presse/
- impact : à l'avenir, tout draft de newsletter Algorithme va directement dans wiki/revues-presse/ avec status: draft, jamais dans raw/

## [2026-04-15] doctrine-add | OpenDecoder SEO Scoring System v2 — référence officielle
- nouveau dossier raw/ : `raw/scoring/`
- fichier ajouté : `raw/scoring/opendecoder-seo-scoring-system.md` (947 lignes)
- inspiration : paper OpenDecoder (Mo et al., 2026) — non encore ingéré en KB, à ajouter si disponible pour audit fidélité de la transposition
- structure : 3 scores (Pertinence + Qualité + Potentiel) + agrégation S_final = S_Pert + 0.5 × (S_Qual + S_Pot) → S_100 = (S_final/2) × 100
- 15 prompts LLM structurés couvrant : entités attendues, classification intention, clusters sémantiques, signaux on-page, E-E-A-T, profondeur, structure Hn, lisibilité, paysage concurrentiel, formats attendus, opportunités, position GSC
- règle d'usage : utiliser systématiquement ce scoring pour toute évaluation/audit de contenu avant publication. Pas de scoring ad-hoc. Mise à jour du fichier uniquement sur instruction explicite Tim.
- déclencheurs : "score ce contenu", "évalue cette page", "audit avant publication", "scoring SEO", "note cette rédaction", "évalue son potentiel LLM/IA"
- mémoire session ajoutée : feedback_scoring_opendecoder_reference.md
- articulation : intervient APRÈS la rédaction par `seo-workflow-article` ou `article-engine-pipeline` comme garde-fou. §11 anti-AI-writing s'applique en parallèle pendant l'évaluation S_Qualite sous-score 2.4. Skill `kb-semantic-search` utilisable en amont pour vérifier ce que la KB sait déjà sur la requête cible.

## [2026-04-15] ingest | Call 13 — Caroline (employée agence web marketing)
- source_type: transcript
- source: [[sources/2026-04-15-call-13-caroline]]
- entité créée: 1 ([[entities/caroline]], sous-catégorie "Acteurs / Prospects Bootcamp" — 9 prospects désormais)
- pages créées: 2 / mises à jour: 2 (index, log)
- contradictions: N
- findings notables:
  (1) Profil atypique — ni freelance, ni entrepreneur web, ni directeur agence. Employée SEO agence. Possible **nouvelle variante D** de [[concepts/avatar-freelance-sans-systeme]] à formaliser si d'autres cas similaires. Pour l'instant, 1 cas = pas assez pour formaliser.
  (2) Niveau IA le plus avancé côté prospect à date — utilise déjà Claude Projects + skills personnalisés + combinaison multi-LLM (Claude + Gemini). Tim confirme en direct : "tout le monde n'en est pas là".
  (3) Première objection "pourquoi Claude uniquement" dans les 13 calls. Réponse Tim (Claude B2B vs ChatGPT B2C + seul à permettre du local) à formaliser comme argument type.
  (4) Signal transition freelance : "à un moment donné, j'aimerais [le freelance]". Double-usage du bootcamp (agence court terme + freelance moyen terme).
  (5) Décision hiérarchique (supérieurs à convaincre) = point de friction absent chez les freelances.
- dépendances ouvertes:
  - calls 10, 11, 12 absents de raw/transcripts/ — à récupérer si ils existent
  - transcription très mal nettoyée (typos, ponctuation cassée) — parsing mot-à-mot difficile
  - nom d'agence Caroline + nom de famille non donnés dans le transcript
  - statut final inscription non confirmé à la fin du call

## [2026-04-15] cleanup | Récupération call 10 + correction 2 erreurs factuelles index
- déclencheur : Tim demande "récupère dans dossier bootcamp call". Audit du dossier source `~/Documents/CLAUDE/SEO/Bootcamp CALL/` révèle 2 erreurs propagées dans la KB depuis l'ingest initial.

### Récupération
- nouveau fichier raw : `raw/transcripts/call-10-franck-suite.md` (34.5 Ko, copié du dossier source)
- contenu : suite du call-08 avec Franck. Parcours SEO depuis 2000, époque pré-Pingouin
- pas d'ingest formel (page wiki source) — règle session "copier ≠ ingérer", à demander explicitement si voulu

### Correction erreur #1 — calls 02 et 03 NON vides
- fait : flag "transcripts bruts vides (0 octet)" présent dans index.md et entities/marrusia-cecile.md depuis l'ingest 2026-04-13
- réalité : fichiers remplis (14.7 Ko et 44 Ko, présents depuis le 12 avril 2026 selon timestamps)
- cause probable : erreur d'inspection initiale (peut-être les fichiers étaient effectivement vides au moment de la 1re vérif puis remplis ensuite par Tim sans que l'index soit mis à jour)
- correction propagée : index.md (flag retiré), entities/marrusia-cecile.md (confidence low → medium, mention "transcripts vides" remplacée par "Sources brutes disponibles, ingest formel à faire")

### Correction erreur #2 — calls 11/12 absents (vérifié)
- audit dossier source bootcamp : pas de fichier nommé "call 11" ni "call 12". Numérotation sautée par Tim entre call-10 et call-13-caroline.
- correction propagée : index.md (flag mis à jour de "calls 10/11/12 absents" à "calls 11/12 absents — n'existent pas dans dossier source, numérotation sautée")

### Pages mises à jour
- index.md : section Transcripts réécrite (status raw + flags corrigés)
- entities/marrusia-cecile.md : confidence + mention sources brutes

### Dépendances ouvertes
- Ingest formel calls 02, 03, 10 non fait. À demander explicitement si Tim veut les pages wiki sources (call-02-marrusia, call-03-cecile-suite, call-10-franck-suite). Pour l'instant : matériau brut disponible mais pas synthétisé en page wiki.
