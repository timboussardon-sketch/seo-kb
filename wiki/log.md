---
type: register
title: Log chronologique du vault
tags: [register, log]
created: 2026-04-11
updated: 2026-06-06
status: stable
---

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

## [2026-05-01] batch-ingest | T4 + T5 + T6 — 11 sources supplémentaires (validation "do it" Tim)

Suite directe du batch-ingest T1+T2+T3. Tim valide T4 (notes doctrinales) + T5 (scoring + agent) + T6 (sous-collections). Décision de fusion : `cluster-business-organikk-source.md` ET `2026-04-24-cluster-business-organikk-cursor.md` étant identiques → 1 source fusionnée. Décisions de skip pour T6 : `raw/notes/skill-*.md` (12 fichiers, déjà couverts par tim-skills-seo-proprietary), `raw/notes/tim-*.md` (6 fichiers, déjà couverts par les 3 sources tim-* existantes), `raw/articles/organikk-blog/` (déjà via scrape sauf process-seo-b2b-2026 ingéré séparément), `raw/articles/lost-from-old-site/` et `raw/notes/contenu-seo/` (faible valeur ajoutée vs sources existantes).

### Sources créées (11)

**T4 — Notes doctrinales (5)**
- [[sources/2026-04-24-reflexion-organikk-4-piliers]] — `doctrine`. Cadre doctrinal Organikk : 4 piliers (Surprise Gap / Grounding / pSEO / AEO) + 6 interconnexions + matrice 11 skills × 4 piliers + cadre de décision séquentiel
- [[sources/2026-04-24-cluster-business-organikk-4-piliers]] — `doctrine`. Cluster opérationnel : page pilier + 16 satellites (4 sous-piliers × 4 pages : Know-Simple/Know/Know thought leadership/Do) + 3 commerciales + roadmap 90j + 6 KPIs cluster
- [[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]] — `doctrine`. 4 modèles pSEO data-driven : Modèle 1 Empreinte SERP (Google/Claude/Gemini) · Modèle 2 Entités SERP · Modèle 5 Arbre Suggest · Modèle 6 Schema secteur. Stack 100% APIs officielles, stack interdit explicite (SerpAPI/DataForSEO/Bright Data/Apify)
- [[sources/2026-04-17-organikk-process-seo-b2b-2026]] — `article`. Article pilier Organikk publié 17 avril (HUB Pilier 1 du blog, 2400 mots). Verbatim doctrinal "ne plus vendre du trafic, vendre des leads" + test ChatGPT 2 questions + bannissement "visibilité"
- [[sources/2026-04-25-tim-ton-de-voix-extraction-terrain]] — `doctrine`. Analyse 35 patterns + 5 intros + 5 closings + structures rhétoriques + vocabulaire signature + 10 règles applicables sur ~12 000 mots verbatim Tim (5 Substack + 4 LinkedIn + Organikk + doctrine my-voice)

**T5 — Scoring + agent (2)**
- [[sources/2026-04-15-opendecoder-seo-scoring-system]] — `doctrine`. Système de scoring 4 axes (S_Pertinence dominant + S_Qualité + S_Potentiel + S_AEO) inspiré paper OpenDecoder (Mo et al. 2026). 15 prompts LLM structurés. Formule S_100 = (S_final / 2.5) × 100. Référence officielle pour audit/évaluation contenu avant publication.
- [[sources/2026-04-30-qadence-seo-agent-snapshot]] — `doctrine`. Snapshot Edge Function Supabase (Deno + 2643 LoC) — dispatcher d'agent SEO connecté GSC. 9 tools (fetch_gsc_data, score_content OpenDecoder, load_skill via embedding Gemini, update_project_memory, etc.). Patterns : skill loader sémantique + mémoire projet persistante par (user_id, domain) + agir-pas-annoncer + anti-contamination contexte projet vs choix skill.

**T6 — Sous-collections batchées (4)**
- [[sources/2026-04-30-tim-posts-linkedin-batch]] — `doctrine`. 11 posts LinkedIn (idées + posts publiés). Pattern dominant "Type A : J'ai fait X". 5 types de data propriétaire formalisés (cas client chiffré, réflexion originale, méthodologie documentée, outil interactif, signaux sociaux).
- [[sources/2026-04-30-fg-formation-pseo-cas-client]] — `client-note`. 2e client-note wiki après Victoria Garden. Angle B2B inversé : parler aux créateurs d'OF (pas aux apprenants). Densité données propriétaires : 32 indicateurs Qualiopi × 25+ secteurs × 11 OPCO = jusqu'à 8 800 combinaisons théoriques. 5 modèles pSEO documentés (Modèle 1 secteurs détaillé).
- [[sources/2026-04-30-drive-accompagnement-templates]] — `doctrine`. Kit 7 dossiers (00_Admin → 06_Livrables_Client) avec ordre d'import par call (Call 1 Fondations → Call 4-6 Contenu). Workflow migration vers Google Drive partagé client.
- [[sources/2026-04-30-scheduled-skills-cron]] — `doctrine`. 6 specs cron : revue-presse-quotidienne · raw-revue-de-presse · scan-arxiv-seo-ia (5 prompts détaillés) · recap-hebdo-vendredi · todo-quotidienne-bilan-tim · rappel-calls-1h. Articulation avec routine cloud Anthropic `trig_01Q9turzWB81Ck2i4YF3gyzN` (cron `7 7 * * *` UTC) documentée dans MIGRATION.md.

### Entities créées (2)

- [[entities/qadence-seo-agent]] — sous-cat Architectures IA / Agents (extension §4.1). Edge Function Supabase 2643 LoC, 9 tools, snapshot 2026-04-30
- [[entities/fg-formation]] — sous-cat Clients Tim. Accompagnement OF Qualiopi/OPCO, angle B2B inversé

### Concepts créés (4)

- [[concepts/methode-organikk-4-piliers]] — sous-cat AEO/GEO. **Concept umbrella** qui formalise la doctrine 4 piliers + 6 interconnexions + matrice skills + cadre de décision séquentiel
- [[concepts/mots-cles-actionnels]] — sous-cat Stratégie contenu. **Terme signature Tim** : décisionnel + transactionnel, l'utilisateur attend une action. Test "ChatGPT 2 questions"
- [[concepts/know-simple-know-do]] — sous-cat Stratégie contenu. **Framework Tim qui remplace TOFU/MOFU/BOFU** obsolète. 3 intentions × formats × Schema.org. Matrice OpenDecoder format×intention
- [[concepts/pseo-data-driven-models]] — sous-cat Maillage & architecture. **4 modèles pSEO conformes** : Empreinte SERP / Entités SERP / Suggest / Schema secteur. Stack autorisé/interdit explicite

### Entities mises à jour (2)

- [[entities/organikk-co]] — sources 3→8. Ajout des 5 sources doctrine Organikk (réflexion, cluster, pSEO data-driven, process-b2b article publié, ton-voix)
- [[entities/bootcamp-seo-ia]] — sources 6→7 (drive-accompagnement = kit livrables client bootcamp). Ajout entity-link vers fg-formation (cas client compatible)

### Concepts mis à jour (5)

- [[concepts/programmatique-pseo]] — sources 4→9 (fg-formation, pseo-data-driven, cluster-organikk, process-b2b, maillage-interne)
- [[concepts/data-proprietaire]] — sources 19→25 (5 types formalisés posts-linkedin + fg-formation B2B inversé + 4 modèles APIs officielles + cluster + process B2B + scoring)
- [[concepts/aeo]] — sources 5→9 (réflexion 4 piliers pilier 4 explicite + cluster + process B2B + scoring S_AEO)
- [[concepts/anti-ai-writing]] — sources 7→9 (volet positif 35 patterns Tim + corpus LinkedIn cohérent)

### Pages créées : 17 (11 sources + 2 entities + 4 concepts)
### Pages mises à jour : 8 (2 entities + 5 concepts + index)

### Contradictions / dépendances ouvertes

- **Paper OpenDecoder (Mo et al., 2026)** — référence centrale du scoring system, **non encore ingéré** comme source paper. À ajouter pour audit fidélité de la transposition.
- **Cluster Organikk + 4 modèles pSEO** — plans non encore implémentés au 2026-04-30. Aucune mesure post-déploiement disponible
- **Repo qadence-seo-agent** — snapshot 2026-04-30 figé, le repo continue d'évoluer (prochaine session : ré-ingester un nouveau snapshot ou diff)
- **Audit blanc Qualiopi (FG Formation)** — fichier `audit-blanc.md` lu en titre uniquement, contenu non détaillé dans la KB
- **Templates Drive Accompagnement individuels** — seul l'INDEX est ingéré, les 21 templates eux-mêmes (mvs-strategie, architecture-semantique, etc.) ne sont pas en pages wiki source distinctes
- **11 workflows automatisés** mentionnés dans drive-accompagnement non explicités (vs 10 skills propriétaires actuels — divergence comptable à clarifier)

### Skips documentés

- `raw/notes/skill-*.md` (12 fichiers : skill-brief-contenu, skill-cannibalisation, skill-cluster-aeo, skill-content-pipeline, skill-entites-vectorielles, skill-kb-semantic-search, skill-linkedin-post-tim, skill-maillage-interne(-UPDATED), skill-peurs-objections, skill-product-led-seo, skill-programmatique-pseo, skill-quick-win, skill-revue-presse-iteration, skill-workflow-article) — déjà couverts par [[sources/2026-04-12-tim-skills-seo-proprietary]]
- `raw/notes/tim-*.md` (6 fichiers : tim-about-me, tim-anti-ai-writing-style, tim-my-rules, tim-my-voice, tim-prompt-systeme, tim-readme-bot-instructions) — déjà couverts par [[sources/2026-03-31-tim-profil-et-regles]] · [[sources/2026-03-31-tim-prompt-systeme-fusionn]] · [[sources/2026-03-31-tim-workflow-redaction]]
- `raw/articles/organikk-blog/*` — 14 articles déjà couverts par [[sources/2026-04-12-organikk-blog-scrape]] (sauf `process-seo-b2b-2026.md` ingéré séparément en T4)
- `raw/articles/lost-from-old-site/` (2 HTML : analyse-niche-seo, seo-entreprise-locale) — faible valeur ajoutée doctrinale vs sources existantes
- `raw/notes/contenu-seo/` (7 fichiers : DATASET-SEO, LAST-POSTs-LK, Newsletter, SEO-IA, STRAT-SEO-2025, best-SEO-post, newsletter-cowork-seo) — l'échantillon SEO-IA.md est l'analyse Tim sur Titans/MIRAS déjà couverte par [[sources/2026-04-11-seo-ia-tim]]
- `raw/notes/archive/skills-pre-cursor-merge-2026-04-25/` — archive de versions antérieures des skills, non doctrinale

### Angle SEO identifié — convergence des 11 sources

3 axes doctrinaux que ce batch consolide en système exécutable :

1. **Méthode Organikk = système opérationnel à 4 piliers** (réflexion + cluster + pSEO data-driven + ton-de-voix) — passe de "thèse" à "produit" avec roadmap 90j et garde-fous chiffrés
2. **Scoring + agent = chaîne d'évaluation automatisable** (OpenDecoder + Qadence) — ferme la boucle production → audit → amélioration en infrastructure
3. **Vente SEO B2B 2026 cristallisée** — process B2B (article pilier) + 11 posts LinkedIn (Type A) + scheduled skills (Algorithme quotidien) + drive-accompagnement (kit livrables) + 2 cas clients pSEO (Victoria Garden + FG Formation) → couverture complète prospection → livraison

### Skills hookés à activer ensuite (suggestions)

- `seo-cluster-aeo` sur Organikk pour valider en simulation le cluster avant implémentation
- `seo-product-led` pour spécifier les 4 outils Do du cluster (calculateur Surprise / audit Grounding / générateur template pSEO / audit AEO citabilité)
- `linkedin-post-tim` sur les 8 idées Type A non encore publiées (1, 4, 6, 8 a priori les plus performantes)
- `revue-presse-iteration` sur "Méthode Organikk 4 piliers" comme thème éditorial pour la newsletter

---

## [2026-05-01] batch-ingest | 9 nouvelles sources raw/ → wiki/ (T1+T2+T3 validés par Tim)

Ingest groupé après diff `raw/` vs `wiki/sources/`. Tim valide T1 (newsletters Algorithme) + T2 (scans ArXiv) + T3 (transcripts calls). Workflow §6.1 appliqué en batch (autorisé sur demande explicite).

### Sources créées (9)

**T1 — Newsletters Algorithme (3)**
- [[sources/2026-04-11-algorithme-linkedin-2e-source-ia]] — `source_type: article`. INFO LinkedIn 2e source IA (325k prompts ALM Corp + Semrush) + Core Update mars 2026 + AI Mode 93% sans clic (Seer 25,1 M impressions) + Semrush humain 8x #1.
- [[sources/2026-04-15-algorithme-listicles-chatgpt-30pct-baisse]] — `source_type: article`. INFO listicles ChatGPT −30% (Seer 2 M citations) — survivantes = 10-20 items + signaux externes. Brèves : Core Update intermédiaires dérouillent, Addy Osmani formalise AEO côté Google Cloud (`llms.txt` / `skill.md`), LinkedIn 360Brew "authenticity update" (save 5x reach > like).
- [[sources/2026-04-22-algorithme-core-update-fermes-ia]] — `source_type: article`. Édition longue compilée : 3 INFOs (LinkedIn + IA spécialisées Profound 680 M + listicles −30%). Données nouvelles : ChatGPT vs Perplexity vs AI Mode (11% domaines communs ChatGPT/Perplexity, ChatGPT cite Wikipedia 47,9%, Perplexity cite Reddit 46,7%) + brevet Google US12536233B1 (landing page IA générée si "page design quality" insuffisant) + −40 à −80% sur sites IA industrialisés.

**T2 — Scans ArXiv (2)**
- [[sources/2026-04-15-scan-arxiv-15-avril]] — `source_type: doctrine` (compilation Tim). 5 papers : LLMSEO Bench (2603.25500, 99,78% black-hat filtré + 7 nouvelles attaques), Retrieval Collapse NAVER (2602.16136, 67% pool → 80% exposure), AgenticGEO (2603.20213), AI Search Bias (2602.13415, AI Overviews 7→229 pays), Role-Augmented G-SEO (2508.11158).
- [[sources/2026-04-25-scan-arxiv-25-avril]] — `source_type: doctrine`. 5 papers ACM Web Conf 2026 : MAGEO (2604.19516, 3 agents avec mémoire — Tsinghua/Tencent), LLMSEO Bench (réf croisée), Retrieval Collapse (analyse approfondie), Formalized Information Needs (2604.04140), LLM Reranking Positional Bias (2604.03642 — passages en bas sous-classés).

**T3 — Transcripts calls (3)**
- [[sources/2026-04-13-call-02-marrusia-cecile]] — `source_type: transcript`. Cécile freelance contenu/web ~6-7 mois, niche artisans/asso, profil presse (lecteur correcteur 10 ans).
- [[sources/2026-04-13-call-03-cecile-suite]] — `source_type: transcript`. Suite immédiate : Live Mentor 2025, blocages clients ("ils comprennent rien à ‘visibilité'"), pédagogie Tim Claude Code vs Fusion ("Fusion = 5% de ce que Claude Code fait"), prix bootcamp 590€/2 mois.
- [[sources/2026-04-15-call-10-franck-suite]] — `source_type: transcript`. Suite call-08. Franck **26 ans SEO depuis 2000**, fondateur historique `SEO.fr` (vendu début 2024 à `Netlinking.fr`). Discussion centrale : rapport Claude reçu d'un client (location véhicules), métriques agence (Top 10) vs business (réservations). Doctrine vente Tim cristallisée : "ne plus vendre du trafic, vendre des emails qualifiés". Démo Obsidian + Claude Code en partage d'écran.

### Entities créées (7)

- [[entities/linkedin]] — sous-cat Concepts-marque / Plateformes (2e source IA citée, algo 360Brew)
- [[entities/chatgpt-search]] — sous-cat Concepts-marque / Produits IA
- [[entities/perplexity]] — sous-cat Concepts-marque / Produits IA
- [[entities/google-ai-mode]] — sous-cat Algorithmes Google / Produits IA (93% sans clic, AI Overviews 7→229 pays)
- [[entities/semrush]] — sous-cat Outils SEO (étude 42k URLs humain 8x #1, étude conversion 4x ChatGPT vs Google)
- [[entities/seer-interactive]] — sous-cat Concurrents / Agences (études 2M citations ChatGPT, 25,1M impressions AI Mode)
- [[entities/naver]] — sous-cat Acteurs / organisations recherche (paper Retrieval Collapse)

### Concepts créés (3)

- [[concepts/maillage-systeme]] — sous-cat **Maillage & architecture** (nouvelle sous-catégorie). Architecture éditoriale 3 axes (topique/vectoriel/cognitif), hub/satellite, cross-pillar pollination, 6 règles de gouvernance par publication
- [[concepts/5-types-ancres]] — sous-cat Maillage & architecture. Exact / partial (60-70%) / sémantique / naming / contextuelle, avec quotas et 5 critères de validation par ancre
- [[concepts/retrieval-collapse]] — sous-cat **Métriques & GEO opérationnel**. 67% pool → 80% exposure (NAVER paper), qualité apparente stable, justification scientifique de [[concepts/data-proprietaire]] et [[concepts/e-e-a-t]]

### Entities mises à jour (5)

- [[entities/marrusia-cecile]] — sources 1→3, confidence medium→high (transcripts désormais ingérés). Profil enrichi (presse + niche artisans + ex-chargée comm asso 10 ans)
- [[entities/franck]] — sources 2→3. **Correction parcours** : 26 ans SEO depuis 2000, ex-fondateur `SEO.fr` (vendu début 2024 à `Netlinking.fr`), pas "15 ans Jumpto". Stack Mamoot AI 10€/mois ajouté.
- [[entities/jumpto]] — flag `a-verifier` ajouté. Discordance avec call-10 (Franck se présente comme freelance ex-SEO.fr, pas directeur Jumpto). À clarifier auprès de Tim.
- [[entities/bootcamp-seo-ia]] — sources 3→6 (calls 02, 03, 10 ajoutés)
- [[entities/organikk-co]] — sources 2→3 (newsletter-maillage = cas terrain blog)
- [[entities/fusionn-io]] — sources 5→6 (call-03 Cécile = positionnement Fusion vs Claude Code documenté)

### Concepts mis à jour (5)

- [[concepts/data-proprietaire]] — sources 14→19 (5 nouvelles sources convergentes : Retrieval Collapse, Core Update fermes IA, listicles densité de preuves, LinkedIn signal humain)
- [[concepts/seo-multi-plateforme]] — sources 3→6, confidence medium→high (LinkedIn 2e source IA + 360Brew + IA spécialisées)
- [[concepts/aeo]] — sources 1→5, confidence medium→high (LinkedIn "être cité vaut plus que ranker", AEO Addy Osmani Google Cloud, divergence ChatGPT/Perplexity/AI Mode)
- [[concepts/agentic-search]] — sources 4→7 (MAGEO, AgenticGEO, Role-Augmented G-SEO, AEO Addy Osmani)
- [[concepts/anti-ai-writing]] — sources 4→7 (LLMSEO Bench 99,78% filtré, Retrieval Collapse, Core Update −40 à −80% fermes IA)

### Pages créées : 19 (9 sources + 7 entities + 3 concepts)
### Pages mises à jour : 11 (5 entities + 5 concepts + index)

### Contradictions / dépendances ouvertes

- **Discordance Franck — Jumpto vs SEO.fr** : à clarifier au prochain call ou ingest. Possible parcours intermédiaire 2024-? non documenté
- **Brevet Google US12536233B1** : surveiller si déploiement (pas juste publication brevet)
- **Paper MAGEO 2604.19516** : PDF non récupéré dans `raw/etudes-seo/`, ingest paper séparé possible
- **Paper Role-Augmented G-SEO 2508.11158** : numérotation 25xx atypique, ID à revérifier ; PDF présent dans `raw/etudes-seo/arxiv-2508.11158v1.pdf` → ingest paper séparé possible si Tim demande
- **Statut inscription Cécile et Franck** : non confirmé en fin des transcripts (récap email envoyé)

### Angle SEO identifié

Convergence forte des 9 sources sur **3 axes doctrinaux** :
1. **Le contenu IA brut est mort en 2026** — Core Update (−40 à −80% fermes IA), Semrush (humain 8x #1), Retrieval Collapse (67% pool → 80% exposure), LLMSEO Bench (99,78% black-hat filtré)
2. **LinkedIn devient un canal de citation IA prioritaire B2B** — 2e source citée derrière les profils individuels, signal humain non-fakeable, 5 posts/4 semaines suffisent
3. **Bifurcation GEO artisanal vs industriel** — MAGEO (3 agents avec mémoire) + AEO Addy Osmani (`llms.txt`, `skill.md`) → les agences qui ne basculent pas vers une approche "stratégies réutilisables + data propriétaire" vont être commoditisées

Le concept [[concepts/retrieval-collapse]] devient l'argument scientifique central pour justifier la doctrine [[concepts/data-proprietaire]] auprès des prospects qui doutent ("pourquoi pas du contenu IA pour aller plus vite").

### Skills hookés à activer ensuite (suggestions)

- `revue-presse-iteration` sur Retrieval Collapse comme INFO DU JOUR
- `linkedin-post-tim` sur le pivot vente "ne plus vendre du trafic"
- `seo-brief-contenu` éventuel sur le terme "Agentic Engine Optimization" (Addy Osmani) pour devancer le SEO français

---

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

## [2026-05-05] synthese | Process KW research 5 étapes (Keyword Planner → GSC → Grok → Propriétaires → pSEO)
- déclencheur : Tim partage son process opérationnel de recherche de mots-clés (5 sources outillées) et demande sa formalisation en synthèse avec wikilinks vers la doctrine.
- type : synthesis (4e du wiki)
- source : [[syntheses/process-keyword-research-5-etapes]]
- structure : rappel des 4 piliers en intro → 5 étapes détaillées (Keyword Planner / GSC delta impressions-clics / Grok DeepSearch ◉1-4 / Données propriétaires A-B-C / pSEO matrice + 3 phases) → tableau de synthèse → livrable Google Sheet 5 critères (volume, CPC, intérêt business, difficulté, YoY) → articulation par pilier
- confidence: high — matérialise la doctrine [[concepts/mots-cles-actionnels]] + [[raw/notes/process-seo-b2b-2026]] en pipeline outillé

### Pages mises à jour (backlinks)
- [[index]] : section Syntheses 3 → 4
- [[concepts/mots-cles-actionnels]] : ajout dans Pages liées (concept central du process)
- [[concepts/methode-organikk-4-piliers]] : ajout en Cas d'application (le process est l'opérationnalisation outillée des 4 piliers en KW research)
- [[concepts/programmatique-pseo]] : ajout dans Pages liées (étape 5 = pSEO)

### Articulation doctrinale
- Étape 1 (KP) = découverte / seeder
- Étape 2 (GSC) = pilier [[concepts/grounding-score|Grounding]] (fondation)
- Étape 3 (Grok) = pilier [[concepts/surprise-gap|Surprise Gap]] + alimente [[concepts/information-gain]]
- Étape 4 (Propriétaires) = pilier transversal [[concepts/data-proprietaire]]
- Étape 5 (pSEO) = piliers [[concepts/programmatique-pseo|pSEO]] + couverture MECE [[concepts/aeo|AEO]]

### Dépendances ouvertes
- Pas de script qui ingère automatiquement les calls clients / GSC / CRM pour en extraire des KW actionnels (étape 4 reste manuelle)
- Croisement explicite entre le scrape Google Suggest existant ([[raw/data/keyword-research-2026-05-02]]) et le filtre "actionnel" de l'étape 4 non documenté — query candidate.

## [2026-05-05] skill-add | kw-research-workflow (orchestrateur 5 phases)
- déclencheur : Tim partage la spec d'un nouveau skill orchestrateur qui automatise le process KW research documenté plus tôt dans la session.
- type : skill (13e du portfolio propriétaire)
- source : [[raw/notes/skill-kw-research-workflow]]
- rôle : enchaîne 6 phases (cadrage 6 questions → KP CSV → GSC CSV → 4 WebSearch séquentielles → verbatims → pSEO → livrable Sheet scoré + synthèse 5 lignes). Cible 10-15 min.
- sous-skills appelés : `seo-quick-win` (phase 2), `seo-cannibalisation` (phase 2 si conflit), `seo-programmatique-pseo` (phase 5)
- output : `wiki/queries/kw-research-YYYY-MM-DD-slug.md` + Google Sheet `KW_Research_[Client]_[Date]` (5 colonnes scorées : volume, CPC, intérêt business 1-5, difficulté 1-5, YoY %)

### Pages mises à jour
- `AGENTS.md` §7 : "12 skills" → "13 skills" + ligne `kw-research-workflow` ajoutée à la table de hooks
- [[syntheses/process-keyword-research-5-etapes]] : encadré "Skill orchestrateur" en intro + ajout du skill et des 3 sous-skills dans Pages liées
- [[concepts/mots-cles-actionnels]] : ajout du skill dans Pages liées

### Articulation
Le skill est l'outillage de la synthèse [[syntheses/process-keyword-research-5-etapes]] (qui était la version doctrinale). Mapping : phase 0 cadrage = nouveau, phases 1→5 du skill = étapes 1→5 de la synthèse, phases 6-7 = livrable Sheet + synthèse 5 lignes (formalise le "Livrable Google Sheet — 5 critères" de la synthèse).

### Garde-fous notables (du skill)
- Phase 4 verbatims = différenciateur non-skippable ("c'est ce qui différencie le livrable d'un export Ahrefs")
- 4 WebSearch en séquence stricte, pas en parallèle (chaque search dépend du précédent)
- Pas de modèle pSEO recommandé sans data propriétaire phase 4
- Synthèse 5 lignes obligatoire AVANT le lien

## [2026-05-05] post-linkedin | Workflow KW research 5 étapes (voix Tim, ≈200 mots)
- déclencheur : Tim demande un post court pour expliquer le workflow KW research formalisé en synthèse + skill plus tôt dans la session.
- type : post
- source : [[posts-linkedin/2026-05-05-workflow-kw-research-5-etapes]]
- format : LinkedIn court ≈ 200 mots, hook anti-consensus ("ne se fait plus dans Semrush"), 5 étapes en deux lignes chacune, punchline finale sur data propriétaire non-copiable
- voix : phrases courtes, pas de hashtag, pas d'emoji, pas de règle de 3 décorative, vocabulaire signature ("vendre des leads pas du trafic", absence de "visibilité")
- premier post du dossier `wiki/posts-linkedin/` (compteur index.md 0 → 1)

### Pages mises à jour
- [[index]] : section Posts LinkedIn 0 → 1
- post lui-même : pages liées vers [[syntheses/process-keyword-research-5-etapes]], [[raw/notes/skill-kw-research-workflow]], [[concepts/mots-cles-actionnels]], [[concepts/data-proprietaire]], [[concepts/surprise-gap]], [[concepts/methode-organikk-4-piliers]], [[concepts/programmatique-pseo]], [[raw/notes/process-seo-b2b-2026]]

### À tester
- Variation avec story client en hook (Victoria Garden / FG Formation) pour activer le pilier preuve
- Mesurer engagement vs posts précédents de la batch [[sources/2026-04-30-tim-posts-linkedin-batch]]

## [2026-05-11] methode | Engine carte sémantique sans SERP (v8)
- déclencheur : Tim cherche une alternative aux outils type 1.fr (scraping SERP) pour la densité sémantique. Itéré 8 versions au cours d'une session.
- type : méthode opérationnelle
- source : [[engine-densite-semantique-sans-serp]] (raw/articles/brouillons/)
- portée : carte sémantique pure (5 couches : micro-intentions, entités, vecteurs preuves, multimodal, divergence) + cartographie concurrentielle. Aucune couche éditoriale.
- architecture : 9 phases workflow + Mode 0 (KB Bootstrap), 8 livrables, matrice de couverture
- modes : Bronze (training pur) / Silver (KB partiel) / Gold (KB structuré). Détection auto.
- éthique : zéro scraping SERP, respect robots.txt strict pour sourcing externe (arxiv, hal, OSF, INSEE, OECD, Wikipedia, docs officielles)
- feedback loop : phase 9 identifie 3-5 concepts à versionner dans /wiki/concepts/, /wiki/entities/, /wiki/competitors/ à chaque passage

### Pages mises à jour
- [[index]] : nouvelle section "Engines / Méthodes opérationnelles" (0 → 1)

### À tester
- Premier passage réel sur une vraie requête pour remplir la section "Exemple appliqué" du fichier engine
- Mode 0 KB Bootstrap sur 20+ articles Organikk pour stress-tester l'extraction des concepts atomiques

## [2026-05-16] pseo | Landing pages lead-gen sur problématique SEO (Organikk)
- déclencheur : Tim veut lister les problématiques SEO commerciales sur lesquelles ranker pour ramener des leads, déclinées sur un template de landing service unique.
- type : pSEO-strategy (skill seo-programmatique-pseo)
- source : organikk-next (strategies.ts, pages.ts, /secteurs, /templates) + seo-kb (raw/acquisition, raw/cas-clients, raw/notes/analyse-calls-prospects-bootcamp)
- output : [[queries/pseo-2026-05-16-landing-lead-gen-organikk]]
- portée : 5 modèles MECE par intention (M1 pain-first, M2 secteur B2B, M3 livrable, M4 escape, M5 praticien), 45 pages possibles phase 1
- priorisation : M1 + M3 score 17/20 → lancer en premier (conversion + données propres max, compétition faible GEO-era)
- moat : verbatims calls + chiffres cas clients + scoring propriétaire (invisibles depuis la SERP)
- anti-cannibalisation : ne re-fait pas le pSEO local métier×ville ([[pseo-2026-05-13-organikk-secteur-ville]]) — ici national/B2B/pain

### Pages mises à jour
- [[index]] : section Queries (1 → 2)

### À tester
- Valider le périmètre M1 (15 slugs) avec Tim, puis scaffolder src/app/seo/[slug]/ + strategies.ts (trafic-en-chute, pas-cite-par-chatgpt)
- Sourcer les chiffres `[DONNÉE À SOURCER]` avant toute mise en ligne (cas clients + étude conversions LLM)

## [2026-05-16] systeme | Fermeture des 3 boucles + rituel + navigation (refonte système)

- déclencheur : Tim veut le meilleur système possible — audit système + comblement des manques (docs + routines)
- décision : [[decisions/0001-fermeture-boucles-systeme]] (ADR-0001)
- hors scope explicite Tim : revue-presse-quotidienne + audit-vault-hygiene (laissés tranquilles)

### Documents créés (13)
- registres : [[hypotheses]] (10 hypothèses seedées du vault réel), [[contradictions]] (13 contradictions consolidées du log), [[ingest-backlog]] (backlog P1/P2/P3 + skips documentés)
- navigation : [[000-home]] + 5 MOCs ([[moc/moc-aeo-geo]], [[moc/moc-maillage]], [[moc/moc-vente-objections]], [[moc/moc-redaction]], [[moc/moc-methode-kb]])
- boucle preuves : [[preuves/index]], [[preuves/_template]], [[preuves/SETUP-GSC]]
- décisions : [[decisions/index]], [[decisions/_template]], [[decisions/0001-fermeture-boucles-systeme]]
- rituel : [[revue-hebdo/index]]

### Skills créés (6) — cf. §7bis AGENTS.md
- ingest-backlog-sweep (lundi), hypotheses-validation (1er du mois), preuves-feedback (à la demande), gsc-watcher (1er du mois), revue-hebdo (vendredi), resurgence-espacee (mercredi)

### Automation créée
- 5 LaunchAgents : com.timboussardon.{ingest-backlog, hypotheses-validation, revue-hebdo, resurgence, gsc-pull}
- runners dans ~/.local/bin/seo-kb/ + gsc-fetch.py (importateur Search Console API service account)
- garde-fou .gitignore : *service-account*.json

### Gouvernance
- AGENTS.md 2.5 → 2.6 (§14 trois boucles + rituel, §7bis skills système, types register|moc|decision|proof, nouveaux dossiers wiki §3)
- [[index]] : section "Système & navigation" ajoutée en tête
- mémoire obsolète canonical_vault_path corrigée : /Users/timothee/Documents/seo-kb/ (disparu) → /Users/timothee/Code/seo-kb/

### Contradictions / dépendances ouvertes
- Boucle preuves inerte tant que Tim n'a pas déposé le service account GSC ([[preuves/SETUP-GSC]]) — dégrade proprement en mode dépôt manuel via gsc-watcher
- 5 nouveaux LaunchAgents à charger via launchctl (instruction donnée à Tim)
- audit-vault-hygiene/SKILL.md contient encore l'ancien path /Users/timothee/Documents/seo-kb/ — hors scope (laissé tranquille à la demande de Tim), à corriger plus tard
- Valeur des registres conditionnée à la discipline de revue : dette assumée dans ADR-0001

## [2026-05-16] backlog | sweep — 38 en backlog (P1:16 P2:13 P3:9) + 21 drive-accompagnement parké C-006
- raw inventorié: 169 fichiers (hors journal/, revue-de-presse/, _archive/, archive/)
- corrections diff: FG-Formation-—-Base-de-Connaissances + audit-blanc + ton-de-voix-tim-organikk-substack → désormais TREATED (listés en Fichier raw de sources existantes), retirés du backlog ; newsletter-maillage-interne.md TREATED ([[sources/2026-04-30-newsletter-maillage-interne]]) mais variante -claude.md NON couverte → reste P2
- prochain lot proposé: raw/bootcamp4/session-1-mots-cles-transcript.md, raw/bootcamp4/session-2-redaction-transcript.md, raw/articles/modele-production/modele-strategie-b2b.md
- nouveaux skips: aucun

## [2026-05-16] resurgence | [[concepts/data-proprietaire]] — verdict proposé : MAJ frontmatter `updated:` 2026-04-13→2026-05-01 (corps juste, drift métadonnée 18j sur hub 98 backlinks)

## [2026-05-16] revue-hebdo | Semaine W20 — 7 décisions (édition inaugurale)
- promotions: rrf draft→stable (charge opérationnelle article-engine-pipeline, confidence reste medium) ; aucun stable→stale (vault < 40j)
- hypothèse en test: H-007 (data propriétaire vs Retrieval Collapse) → fiche preuve pSEO secteur×ville (5 articles Organikk publiés), J+30 ≈ 2026-06-15
- lot ingest W21: raw/data/keyword-research-2026-05-02/{keywords-cleaned,keywords-classified}.md (P1 oldest-first)
- contradiction à fermer W21: C-002 (ingest paper OpenDecoder Mo et al. 2026, débloque H-010)
- archivage: aucun (vault trop jeune, pas d'invention) ; tripwire sur brief Information Gain à revoir W21
- résurgence: verdict accepté — frontmatter data-proprietaire corrigé updated:→2026-05-01 (exécuté)
- fil rouge: "le moat data-propriétaire, mis à l'épreuve" — déclencheur = mesure J+30 H-007

## [2026-05-16] hypothese | revue mensuelle (inaugurale) — 1 hypothèse bougée, 0 contradiction fermée
- périmètre : registres seedés le 2026-05-16 (ADR-0001), aucun ingest depuis. Fenêtre vide hors décision revue-hebdo W20 à exécuter.
- H-007: `ouvert → en-test` (preuve: [[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]] créée — exécution de la décision [[revue-hebdo/2026-W20]] point 2 que les registres n'avaient pas répercutée)
- fiche preuve ouverte `en-cours` : cohorte 5 pages pSEO secteur×ville, jalons J+30 ≈ 2026-06-15 / J+90 ≈ 2026-08-14. Baseline GSC NON capturée (service account non déposé, [[preuves/SETUP-GSC]]) — bloquant assumé, aucune mesure inventée. H-007 ne dépassera pas `en-test` avant la baseline.
- doctrine tracée (en-test ⇒ pas de changement de `confidence:`, marqueur de traçabilité seulement) : [[concepts/data-proprietaire]] (updated 2026-05-01→2026-05-16, note "sous test" ajoutée, confidence: high inchangé) ; [[concepts/retrieval-collapse]] (updated 2026-05-01→2026-05-16, limite "inférence sous test" ajoutée)
- C-002: `ouverte → en-cours` (ingest OpenDecoder tranché W21 par revue-hebdo W20)
- C-003: `ouverte → en-cours` (première instrumentation engagée via la fiche H-007, fraction du cluster seulement)
- contradictions > 60j : aucune (la plus vieille ~33j) — pas d'escalade revue-hebdo au titre de la règle 60j
- H-009, H-010 restent `ouvert` (H-010 toujours bloquée par C-002 non encore ingérée) ; H-001 reste `heuristique` assumé

Doctrine 2026-05-16 : 1 hypothèse bougée (validé:0 invalidé:0 en-test:1) / 0 contradiction fermée (2 avancées ouverte→en-cours : C-002, C-003)

## [2026-05-18] backlog | sweep — 40 en backlog (P1:16 P2:13 P3:11) + 21 drive-accompagnement parké C-006
- inventaire: 170 raw .md (hors journal/revue-de-presse/archive). P1/P2 inchangés vs sweep 2026-05-16 ; +2 fichiers surfacés en P3
- nouveaux en P3: raw/ia-employe/recap-jour-health-2026-05-07.md (health-check ops), raw/auteurs/README.md (convention dossier) — tous deux candidats skip, à trancher par Tim (non auto-skip)
- prochain lot proposé: raw/data/keyword-research-2026-05-02/keywords-cleaned.md + keywords-classified.md (décision W21 standing, pas encore ingérée), puis bootcamp4 transcripts (session-1-mots-cles-transcript, session-2-redaction-transcript = moat terrain non rejouable)
- nouveaux skips: aucun

## [2026-05-21] note | [[concepts/angle-differenciant-mot-cle]] créé — doctrine de sélection des mots-clés
- déclencheur : prep du call bootcamp 4 · semaine 3 (démo "mots-clés anti-ChatGPT"). Gap identifié — la méthode d'identification de l'angle différenciant n'était écrite nulle part, seulement éparpillée dans [[session-2-redaction-debrief]], [[session-3-audit-prep]], [[sequencage-semaine-3]].
- type : concept (Stratégie contenu, 13e)
- contenu : on ne touche pas au head term de front (saturé + mangé par GPT + intention floue) → on descend dans l'intention → séquence d'attaque 3 horizons (mois 1-2 sous-niches / 3-6 cluster maillé = autorité topique / 6+ head term en récolte). Inclut la grille de tri anti-ChatGPT et le cas plombier comme déroulé de démo.
- sources : 6 (session-2/3 bootcamp4, sequencage-S3, briefs avocat + hôtellerie, programmatique-pseo)
- pages mises à jour : [[index]] section Concepts 35→36, Stratégie contenu 12→13

## [2026-05-21] audit | Audit santé du vault — [[audit/2026-05-21-audit-vault]]
- déclencheur : demande de Tim « fais un audit du vault SEO », puis « corrige tout ».
- périmètre : 421 notes (197 wiki, 224 raw). Liens cassés, orphelines, frontmatter, index, métadonnées.
- corrections exécutées :
  - index : compteurs recalés (Concepts 36→50, Entities 45→47, Syntheses 4→7, Queries 2→4, Briefs 1→6) ; ajout des fichiers absents du catalogue ; sections Audits + Propositions créées.
  - [[concepts/rrf]] : `draft→stable` (exécution de la décision revue-hebdo W20 restée en suspens).
  - frontmatter normalisé sur 5 concepts bootcamp (`status: actif`→`stable`, schéma AGENTS.md §5.1, ajout `## Pages liées`) + 3 syntheses (`4-piliers-organikk`, `faq-geo-175-questions`, `tim-profil-doctrine`).
  - `status: evolving`→`stable` sur [[concepts/confidence-score]], [[entities/muvera]], [[entities/sge]].
  - liens cassés réparés : `cocon-semantique`→`maillage-systeme`, 7× `feedback_*` déliés, lien dossier keyword-research→fichier.
  - notes créées : [[concepts/entites-vectorielles]] (réclamée par 6 fichiers raw), [[entities/gsc]].
  - fichier mal rangé déplacé : `2026-05-05-workflow-kw-research-5-etapes.md` (type post) `syntheses/`→`posts-linkedin/`.
- résultat : 0 lien cassé wiki/ (hors log historique), 0 orphelin, compteurs index alignés, frontmatter conforme.
- laissé volontairement : statuts de cycle de vie spécifiques (living-doc/accepted/report/en-cours/phase-1-ready), `.obsidian.broken/` (suppression manuelle).

## [2026-05-22] revue-hebdo | Semaine W21 — 7 décisions (semaine de consolidation)
- promotions : 0 draft→stable, 0 stable→stale (`rrf` déjà rattrapé par l'audit du 2026-05-21, pas par le rituel).
- hypothèse en test : aucune nouvelle — déblocage de [[hypotheses#H-007]] priorisé (déposer le service account GSC, capturer la baseline avant J+30 ≈ 2026-06-15).
- lot ingest W22 : report à l'identique du binôme keyword-research 2026-05-02 (`keywords-cleaned` + `keywords-classified`) — non exécuté en W21.
- contradiction à fermer : [[contradictions#C-007]] (décompte workflows/skills, zéro dépendance externe) ; [[contradictions#C-002]] non reconduite par inertie — à timeboxer ou assumer horizon long.
- archivage : brief [[briefs/2026-04-13-information-gain-seo-geo]] → archive (tripwire W20 : article existant antérieur au brief, brief jamais exécuté).
- résurgence : n'a pas tourné cette semaine (LaunchAgent `com.timboussardon.resurgence` non mis en service) — point 6 sans intrant, à relancer avant W22.
- fil rouge : moat data-propriétaire sur minuterie (J+30 H-007) + émergence d'un 2ᵉ fil — la doctrine de sélection des mots-clés.
- méta : 1ʳᵉ revue avec arriéré — W20 a livré 2 actions sur 4 ; W21 décide moins et plus local pour fermer le trou d'exécution nommé par l'audit du 2026-05-21.

## [2026-05-29] revue-hebdo | Semaine W22 — 8 décisions (le mécanisme d'exécution tranché)
- carry-over W21 : les 3 actions vault-internes (ingest kw-research, C-007, archive brief) **toutes non exécutées** + résurgence muette 2 mercredis + sweep backlog 11j de retard. La prédiction W21 s'est réalisée.
- promotions : 0 draft→stable (aucun nouveau draft — production allée sur Fusionn/bootcamp, pas en wiki), 0 stable→stale.
- hypothèse en test : aucune nouvelle ; **changement de chemin** sur [[hypotheses#H-007]] — capturer la baseline par export GSC **manuel** (`gsc-watcher`, pas le service account) avant J+30 ≈ 2026-06-15.
- lot ingest W23 : binôme keyword-research 2026-05-02 — 3ᵉ reconduction, cap atteint ; relancer d'abord `ingest-backlog-sweep` (11j) et attacher l'ingest au momentum Fusionn mots-clés. Pas de 4ᵉ reconduction : sinon skip documenté.
- contradiction : [[contradictions#C-007]] — poser la définition « skill propriétaire » (10 vs 13 vs 20+) **avant** le décompte ; C-002 toujours non timeboxée.
- archivage : **exécuté en séance** — brief [[briefs/2026-04-13-information-gain-seo-geo]] `draft → archived` + retiré de [[index]] (Briefs 6→5).
- résurgence : 3ᵉ semaine sans intrant ; LaunchAgent `com.timboussardon.resurgence` chargé mais ne produit rien → diag ops (wrapper/TCC), pas un report.
- fil rouge : doctrine de sélection des mots-clés **productisée** (modèle Fusionn « Liste des mots-clés pour X », 23 drafts regroundés, lead magnet) → pilier acté de fait, wiki en retard sur le produit ; candidat synthèse `doctrine-selection-mots-cles` + angle newsletter.
- méta (déc. 8) : exécution rituelle W20=1/4, W21=0/3. Remède tranché : (1) attacher les décisions au travail réel, (2) l'agent exécute en séance les décisions bureaucratiques déjà arbitrées, (3) carry-over check + cap à 1 reconduction. À intégrer au skill `revue-hebdo` si Tim valide.

## [2026-06-01] hypothese | revue mensuelle — 0 hypothèse bougée, 0 contradiction fermée
- périmètre : 16 jours depuis la revue inaugurale (2026-05-16), pas un mois plein. Aucun intrant neuf : 0 source ingérée depuis 2026-04-30, 0 export dans `raw/data/exports-gsc/`, 0 nouvelle fiche preuve. Règle dure appliquée : pas de preuve = pas de mouvement.
- H-001 reste `heuristique`, H-002 à H-010 restent `ouvert`. Aucune n'a reçu de preuve dans un sens ou l'autre.
- H-007 reste `en-test` : fiche [[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]] toujours `en-cours`, baseline non capturée. **J+30 le 2026-06-15 — dans 14 jours.** Si la baseline n'est pas posée avant, le J+30 mesure dans le vide. Chemin déjà tranché en [[revue-hebdo/2026-W22]] déc. 2 : export GSC manuel + `gsc-watcher`, pas le service account.
- H-010 reste bloquée par [[contradictions#C-002]] (paper OpenDecoder jamais ingéré).
- contradictions : aucune > 60 j, donc aucune ne remonte encore en revue hebdo. C-011/C-012 (détectées 2026-04-13, 49 j) franchissent le seuil ≈ 2026-06-12 — à trancher en W23/W24. Aucune fermeture ce mois (l'ingest OpenDecoder décidé en W20 n'a pas eu lieu).
- doctrine : aucun `confidence:` touché, aucun wording corrigé — rien n'a changé de statut.
- Doctrine 2026-06-01 : 0 hypothèse bougée (validé:0 invalidé:0 en-test:0) / 0 contradiction fermée. Goulot unique et inchangé depuis 3 revues hebdo : la baseline GSC de H-007 qui ne se capture pas.

## [2026-06-06] audit | Audit vault + liens et correctifs
- rapport: [[audit/2026-06-06-audit-vault-liens]]
- keywords/ (27): type wiki→query, MOC [[keywords/index]] créée, "Voir aussi" liens réels
- liens cassés wiki: 10→0 (pipe échappé, liens racine/skills, entité golfiller créée)
- types frontmatter: 35→0 (synthese→synthesis, article-blog→brief, cadrage→methode)
- AGENTS.md §5.1 étendu: proposition, methode, post
- index.md + log.md typés register; orphelines raccrochées au catalogue
- raw bootcamp4 backfillé; 2 canvas vides supprimés; ./kb rebuild

## [2026-06-08] backlog | sweep — 110 en backlog (P1:44 P2:29 P3:37) + 21 drive-accompagnement parké C-006
- aucun ingest depuis le sweep 2026-05-18 → +70 fichiers (bootcamp4/5, terrain commercial Organikk, Fusionn, Golfiller, batch 13 posts LinkedIn)
- sorti du backlog: raw/acquisition/modele-roadmap-premier-call.md (supprimé de raw/, vérifié git)
- prochain lot proposé: keywords-cleaned + keywords-classified (oldest P1, data mots-clés), raw/organikk/pré-call/proximit-propale.md (+ proximit-resume-call-client) (moat commercial le plus frais)
- à surveiller: raw/etudes-seo/etude-ctr-ai-overviews-gsc.md (étude externe valeur élevée, P3 mais à ingérer comme source)
- nouveaux skips: aucun (bloc docs skills/guides bootcamp4 = candidat skip groupé, à trancher par Tim)

## [2026-06-09] methode | Leexi = 1er client système IA complet (repo dédié + pack vivant)
- dossier client: raw/organikk/clients/leexi/ (fiche maître + transcript rapatrié)
- architecture 3 repos: seo-kb privé / leexi-seo transférable / organikk-seo-pack doctrine vivante (submodule)
- 8 skills portés génériciss + synchronisés (.claude/skills symlink), voix sur $VOIX_DIR
- playbook reproductible créé: [[methodes/onboarding-client-systeme-ia]]
- fix prod: questionnaire espace-leexi basculé Netlify Forms (POST 404) → Supabase client_questionnaire + admin.html
- évolution de [[queries/transfert-vault-client]] (snapshot figé → pack vivant)

## [2026-06-09] client | Leexi — dossier data complet (brief + 4 analyses + GSC)
- brief client canonique (suite IA souveraine, Leexi One sept 2026) ; audit thématique ; étude marché (deep-research 24 sources) ; étude RGPD/souveraineté ; analyse GSC + approfondie
- finding majeur: SEO hors-marque leexi.ai -43% en 6 mois (marque +45%), cause = refonte cassée (migration sans 301/canonical + cannibalisation), souveraineté = 0 clic
- tout dans le vault leexi-seo (journal: leexi-seo/Journal.md), data brute dans data/gsc/

## [2026-06-10] client | Golfiller — fiche client + analyse GSC 90j + modèles pSEO
- fiche client créée: raw/organikk/clients/golfiller.md (statut: en cours)
- pull GSC API via google_connections Fusionn (fonction edge admin-gsc-export, secret dédié)
- analyse: [[queries/2026-06-10-golfiller-gsc-90j]] — 5 480 clics / 113 965 imp top 1000, winners 100% Do
- signal pSEO: page tarifs parcours = 1 346 requêtes distinctes, 388 parcours nommés
- skill déclenché: seo-modeles-pseo → [[clusters/modeles-pseo-2026-06-10-golfiller]] (7 modèles scorés, top 3: avis modèle, prix, fiches parcours)
- cannibalisation détectée: calcul-index-golf vs calculateur-score-differentiel (famille « calcul index golf »)

## [2026-06-10] query | Golfiller analyse GSC 6 mois comparée
- source: [[sources/2026-06-10-golfiller-gsc-6mois]] (4 CSV dans raw/data/exports-gsc/golfiller-2026-06-10/)
- output: [[queries/2026-06-10-golfiller-gsc-6mois]]
- skill déclenché: analyse GSC (winners/losers + striking distance + CTR)
- findings: -23% clics (saisonnier calendrier avent -2852 + comparatif -1371), branded 43% (↑ vs 29% en 90j), pages pSEO décollent de 0, érosion non-branded pluriel (balles de golf 9,6→17,6), opportunité mère « balle de golf » pos 8,5 / 26 574 imp
- pages créées: 2 / mises à jour: index.md

## [2026-06-10] query | Golfiller entités vectorielles page « balle de golf »
- output: [[queries/entites-2026-06-10-golfiller-balle-de-golf]]
- skill déclenché: seo-entites-vectorielles
- contexte: défense pluriel (9,6->17,6) + gisement « balle de golf » pos 8,5 / 26 574 imp

## [2026-06-10] query | Golfiller — dataset sourcé vitesse de swing / distance par club
- collecte web multi-sources (14 URLs ouvertes), data mesurée uniquement (TrackMan 2023-2024, Shot Scope, Arccos, USGA/R&A 2024 Distance Report)
- output: [[queries/2026-06-10-golfiller-dataset-vitesse-distance]]
- table déclarative (vitesses par âge HackMotion) écartée du publiable, confidence low
- règle système actée par Tim: jamais de scraping sans citation, bloc Sources obligatoire en fin de page publiée
- skill déclenché: none (recherche data, modèle déjà cadré dans [[clusters/modeles-pseo-2026-06-10-golfiller]])

## [2026-06-10] brief | Golfiller page usage « balle de golf pour la distance »
- output: [[briefs/2026-06-10-balle-golf-distance]]
- skill déclenché: seo-brief-contenu

## [2026-06-10] client | Golfiller — article vitesse/distance par club produit (template officiel)
- article complet livré : calculateur fer 7 → vitesse → compression, 4 tableaux km/h-mètres, FAQ, bloc sources
- design : template Golfiller fourni par Tim (.golf-page, Bebas Neue, #4ECDC4/#F5E137), gardé en référence dans raw/golfiller/pages/
- data : 100 % depuis [[queries/2026-06-10-golfiller-dataset-vitesse-distance]], zéro extrapolation
- fiche client mise à jour (section Articles produits) : raw/organikk/clients/golfiller.md
- avant publication : handles collections + publier dans l'URL vitesse-de-swing existante (anti-cannibalisation)

## [2026-06-10] client | Alexia — call de cadrage avec Adrien archivé + résumé
- nouveau dossier client : raw/organikk/clients/alexia/ ; transcript verbatim + résumé structuré (scope, hors scope reporting, 4-5 clients représentatifs, alerting SEO demandé, limite 1000 pages actée)
- source : [[alexia-call-cadrage]] (Downloads/Alexia.md rapatrié)
- corpus voix : entrée datée ajoutée dans raw/notes/tim-my-voice.md (système vs outils, vecteurs sémantiques, emails qualifiés, limite 1000 pages)
- next : facture à renvoyer, résumé de call à envoyer, espace Notion à recevoir, choix des 4-5 clients, point mercredi

## [2026-06-10] client | Alexia — résumé de call validé et archivé (version envoyée)
- résumé final validé par Tim, envoyé à Adrien + Alexia avec la facture corrigée : [[alexia-resume-call-envoye]]
- next acté : à réception du paiement, ouvrir le drive + installer les skills dans Claude (abonnement inchangé pour le moment)

## [2026-06-10] concept | Objection confidentialité / RGPD — argumentaire standard
- nouvelle page [[concepts/objection-confidentialite-rgpd]] : réponse en 2 phrases + détail (entraînement par type de compte, DPA, minimisation, brut en local), vérifiée sur les pages officielles Anthropic
- reliée à [[moc/moc-vente-objections]] (ordre de lecture, point 9)
- même point ajouté aux deux guides 0→1 (md + HTML) et en mémoire système

## [2026-06-11] client | Victoria Garden — audit GSC complet (évolution 3 mois vs N-1)
- source: [[sources/2026-06-11-victoriagarden-gsc-export]] (137 pages, 1 645 requêtes, bruts dans raw/data/exports-gsc/victoriagarden-2026-06-11/)
- audit: [[victoriagarden-audit-gsc-2026-06-11]] (raw/organikk/clients/victoriagarden/) — clics +47% mais marque -41% et commercial -13%, croissance portée par l'événementiel (Know)
- quick wins: [[victoriagarden-quick-wins-2026-06-11]] — top 10, ~+1 500 clics/3 mois, fiches actions
- skill déclenché: seo-quick-win (boucle: run + claims + prédiction J+90 loggés, gate OK)
- tracker prestation créé: prestation/clients/victoriagarden.md

## [2026-06-11] prospect | Catherine (Canada) — call découverte archivé + proposition rédigée
- transcript intégral + fiche : raw/organikk/clients/catherine/2026-06-11-call-decouverte.md
- résumé email + proposition (gabarit Alexia, brouillon à valider par Tim) : raw/organikk/clients/catherine/2026-06-11-resume-call-proposition.md
- corpus de voix nourri (entrée datée dans raw/notes/tim-my-voice.md) : système/Tamagotchi, mots-clés anti-IA, tête/mains
- tarif énoncé : 1 500 € HT, conversion CAD + taxes à trancher avant envoi

## [2026-06-12] revue-presse | Search Console mesure les réponses IA
- output: raw/revue-de-presse/2026-06-12-revue-presse.md
- info du jour: rapports Generative AI performance GSC (3 juin, impressions only, opt-out 17 juin)
- brèves: spam policies citations IA / Perplexity 200M$ + appel Amazon / DCN vs Common Crawl / Applebot Siri
- pilier dominant: SEO
- skill déclenché: revue-presse-quotidienne + ton-de-voix-tim

## [2026-06-12] revue-hebdo | Semaine W24 — 7 décisions, 7 mouvements de registre exécutés en séance
- W23 sautée (pas d'édition le 2026-06-05), carry-over check sur W22
- promotions: 0 exécutée, 2 recos draft→stable à valider (methodes/ranker-verticale-niche-sans-backlink, methodes/cadrage-boucle-edition-algorithme)
- hypothèse en test: H-009 → en-test, fiche [[preuves/2026-06-12-golfiller-instrumentation-client]] créée en séance (baselines GSC golfiller-2026-06-10, échéances 2026-07-03 / 2026-09-01 / 2026-09-08)
- H-007: dernière fenêtre, export Organikk avant 2026-06-15 sinon en-test → ouvert en W25 (conditionnel pré-arbitré)
- lot ingest W25: golfiller-strat.md + etude-ctr-ai-overviews-gsc.md ; binôme keyword-research 2026-05-02 → skip documenté (4ᵉ non-exécution, conditionnel W22)
- contradictions: C-012 fermée (acceptée), C-007 acceptée (sortie du circuit), C-002 requalifiée ouverte (long terme)
- archivage: posts-linkedin/2026-05-05-workflow-kw-research-5-etapes draft → archived, retiré de l'index
- résurgence: 4 mercredis muets, ticket ops inchangé
- fil rouge: instrumentation client (Golfiller ledger + 2 exports GSC en 24h) ; sélection mots-clés sort du suivi rituel (résolu hors wiki)
- output: [[revue-hebdo/2026-W24]]

## [2026-06-12] audit | Audit hygiène du vault (à la demande)
- output: [[2026-06-12-audit]]
- 733 fichiers, 5 923 wikilinks : 103 cassés (60 réels), 216 orphelins (~150 structurels), 10 collisions, 0 frontmatter
- priorités : concepts/cannibalisation à créer, brouillons -v2/-v3 revuedepressIA à purger, convention slugs clients
- bonus : vault leexi-seo contrôlé (2 cassés = références seo-kb dans un repo transférable)

## [2026-06-12] maintenance | Traitement de l'audit du jour (P1 + P2 + quick wins)
- 16 brouillons -vN archivés dans agent-synthetic/revuedepressIA/_archive/ (et breves-IA/_archive/) : seule la version finale de chaque édition reste indexée
- créé : [[concepts/cannibalisation]] (types de conflit, remèdes, déclencheurs, doctrine) + entrée index
- quick wins : [[ton-de-voix-tim]] → backticks dans _loop-kit/_template/ (3 fichiers), [[maillage-interne-gsc]] → backticks dans prestation/roadmap.md
- leexi-seo : 2 wikilinks vers le vault privé retirés du call de découverte (repo transférable)
- ./kb rebuild fait (5 584 chunks)
- non tranché (décision Tim) : convention de slug pour les collisions clients (leexi/golfiller) + doublon quotidien revue-presse écrit à 2 endroits par la routine

## [2026-06-12] audit | Audit des automatisations (16 inventoriées, vérifiées par leurs outputs)
- output: [[2026-06-12-audit-automatisations]]
- cassées : GH Actions seo-kb (claude --print sans prompt, ~3 sem.), résurgence (exit 1 depuis le 16 mai), pg_cron lifecycle zombie (401 horaire), doublons breves_wall
- 8 nouvelles automatisations proposées (health check méta, export RAG auto, rebuild post-pull, purge -vN, draft jeudi LinkedIn, indexation-check mensuel, résolution prédictions, relance questionnaire)

## [2026-06-12] resurgence | [[concepts/grounding-score]] — verdict proposé
- note: [[revue-hebdo/resurgence-2026-06-12]]
- verdict proposé: à mettre à jour (opérationnalisation 4 piliers non répercutée, confidence high→medium tant que H-003 ouvert, sources 6→11)
- confirmations depuis updated: [[sources/2026-04-15-opendecoder-seo-scoring-system]] · [[sources/2026-04-25-scan-arxiv-25-avril]]
- contradiction: N

## [2026-06-12] maintenance | Réparations automatisations + 7 nouvelles mises en place
- réparé : pg_cron zombie, doublons breves_wall (+contrainte), résurgence (OK ce soir), GH Actions migrées en launchd local
- nouveaux agents : health-check lundi, autopull étendu (rebuild+exports RAG), purge-drafts dimanche, jeudi-recap, indexation-check mensuel, predictions-resolve mensuel, audit-vault + algorithme-recap locaux

## [2026-06-13] update | Qadence reconstruit sous Claude + vault RAG
- entité MAJ: [[entities/qadence-seo-agent]] (Gemini→Claude, Next.js→Vite, snapshot Gemini marqué périmé)
- agent seo-agent réécrit sous Claude Messages API (streaming SSE), vault branché via kb-search (kb_chunks pgvector)
- doctrine = table skills synchronisée verbatim depuis ~/.claude/skills (script qadence/sync-skills.py) — audit: 26 slugs identiques 100%
- front: espace compte plein écran, GSC multi-comptes (gsc-properties), lanceur de skills, design Google-mono
- fix: résolveur GSC tolérant à la fragmentation des sessions anonymes (token par site/domaine)
- journal dev détaillé: qadence/Journal.md

## [2026-06-15] backlog | sweep — 192 en backlog (P1:84 P2:38 P3:70) + 22 drive-accompagnement parké C-006
- 326 fichiers raw scannés ; bond 110 → 192 depuis le sweep 2026-06-08
- ingests réels de la semaine (arrivés ET traités dans la fenêtre) : Golfiller, Alexia, Victoria Garden, Catherine, Leexi
- moteur du bond : FG-Formation dossier client complet (40 — 32 transcripts d'appels + 8 livrables), x-playbook (4), espressio-ai refs (5), bootcamp4/exercices (26), guides/notes (3)
- prochain lot proposé: golfiller-strat.md + etude-ctr-ai-overviews-gsc.md (lot W25 voté, toujours non exécuté)
- nouveaux skips: aucun (bloc matériel pédagogique bootcamp4 = 50 fichiers, candidat skip groupé à trancher par Tim)

## [2026-06-19] ingest | Playbook Reddit (SEO + GEO)
- source_type: doctrine
- source: [[sources/2026-06-19-playbook-reddit-seo-geo]] (depuis raw/reddit-playbook/Playbook-Reddit-SEO-GEO.md, audit web 5 angles)
- entities touchées: 2 (création [[entities/reddit]], maj [[entities/perplexity]])
- concepts touchés: 1 (création [[concepts/parasite-seo]])
- pages créées: 3 / mises à jour: 2 (perplexity + index)
- contradictions: N
- angle SEO identifié: priorité GEO > parasite SEO > insights ; trou FR (pas de communauté SEO FR, pas d'étude de cas FR chiffrée) = cible étude first-party Tim

## [2026-06-19] update | Playbook Reddit enrichi (cas Qadence + protocoles + GEO défensif)
- source: [[sources/2026-06-19-playbook-reddit-seo-geo]] (maj)
- ajouts playbook raw : section terrain de test Qadence.io, §7bis 2 protocoles concrets (activation + post), §2 écrire-comme-doc + fraîcheur 90j + réputation défensive, §9 mining X.com
- 5 nouvelles sources web (audit praticiens juin 2026 : SubredditSignals, Upvote.net, Reddit GEO Playbook Medium, AuthorityTech, Redship)
- comble manques #1 (exemples concrets) et #3 (défense GEO) de l'audit de fond

## [2026-06-19] ingest | Playbook X.com (SEO + GEO), miroir du playbook Reddit
- source_type: doctrine
- source: [[sources/2026-06-19-playbook-x-seo-geo]] (restructuration de raw/x-playbook/Playbook-X-autorite-SEO-IA.md en miroir exact de la structure Reddit)
- entities touchées: 2 (création [[entities/x-twitter]], [[entities/grok]])
- concepts touchés: 0 (réutilise parasite-seo, aeo, data-proprietaire)
- pages créées: 3 / mises à jour: 1 (index)
- contradictions: N
- angle SEO identifié: X faible en SEO Google (login wall, pas de deal data) mais fort en GEO via Grok ; cas francophone inversé (communauté SEO/IA FR vivante sur X). Cas test Qadence.io commun.

## [2026-06-19] revue-hebdo | Semaine W25 — exécution des conditionnels W24
- promotions: 2 draft→stable (methodes/ranker-verticale-niche-sans-backlink, methodes/cadrage-boucle-edition-algorithme) ; 0 stable→stale
- hypothèse: H-007 en-test→ouvert (export Organikk jamais déposé au J+30 2026-06-15, fiche pseo-secteur-ville gelée baseline-jamais-capturee) ; aucune nouvelle mise en test (pas de fiche preuve)
- lot ingest: golfiller-strat + etude-ctr-ai-overviews-gsc — 1ère reconduction pour W26, skip si non exécuté
- contradiction: aucune fermée par décret (toutes event-gated) ; C-003 corrigée (zéro mesure réel suite reversal H-007)
- archivage: rien ; mislabel revues-presse/2026-04-13 (draft mais publiée) renvoyé à audit-vault-hygiene
- résurgence: verdict Grounding Score 06-12 exécuté (section Opérationnalisation sourcée, sources 6→11, confidence high→medium, updated 2026-06-19) ; mercredi 06-17 muet (ticket ops TCC ouvert)
- fil rouge: instrumentation client (J+30 Golfiller 2026-07-03) + fil neuf parasite SEO/GEO Reddit+X+Grok (cas test Qadence) — les deux gelés sur événement data

## [2026-06-22] backlog | sweep — 192 en backlog (P1:83 P2:38 P3:71)
- 331 fichiers raw scannés, backlog stable à 192 (5 déposés / 4 ingestés cette semaine)
- sorties backlog : x-playbook (4) → [[sources/2026-06-19-playbook-x-seo-geo]], reddit-playbook (1, neuf) → [[sources/2026-06-19-playbook-reddit-seo-geo]]
- entrées backlog : organikk/pré-call/hellocse, youtube/preparation-yt, leexi/keywords/recherche-2026-06-16-rgpd (P1) + organikk/mots-cles-a-traiter (P3)
- prochain lot proposé : golfiller-strat, etude-ctr-ai-overviews-gsc (lot W25 voté, toujours non exécuté), clients/fgformation/calls/SYNTHESE-appels-anonymisee
- nouveaux skips: aucun

## [2026-06-24] resurgence | [[concepts/surprise-gap]] — verdict proposé
- concept ressorti : surprise-gap (stable, updated 2026-04-13, 72j, 74 backrefs, hub prioritaire)
- état : rien ne l'a touché frontalement depuis avril ; boucle preuve désormais ouverte (exports GSC golfiller + victoria garden)
- drift : confidence: high alors que H-002 reste `ouvert` et zéro fiche preuve adossée
- verdict proposé : confidence high → medium tant que H-002 non testée ; lancer le test A/B Organikk maintenant que la plomberie GSC existe
- output : [[revue-hebdo/resurgence-2026-06-24]]
- à arbitrer en revue hebdo (vendredi)

## [2026-06-24] query | Mots-clés que les IA ne peuvent pas manger (matière newsletter)
- output: [[queries/2026-06-24-mots-cles-que-les-ia-ne-mangent-pas]]
- skill déclenché: kb-semantic-search (Phase 0 vector index)
- sources mobilisées: leexi-call-2026-05-21, mots-cles-actionnels, test-substitution-llm, product-led-seo, data-proprietaire, tabou-visibilite, revues Seer 06-16 + Averi 06-08
- angle SEO: prévalence AIO par intention (5% transactionnel vs 95% comparaison), substituable vs défendable

## [2026-06-26] revue-hebdo | Semaine W26 — 7 décisions, 4 mouvements exécutés en séance
- promotions: 2 draft→stable (entities/karpathy, entities/google-deepmind) ; 0 stable→stale
- hypothèse en test: aucune forcée (H-002 garderait le piège Organikk de H-007, reste ouvert) — vivante H-009, J+30 Golfiller à préparer pour 2026-07-03
- confidence: surprise-gap high→medium (résurgence 06-24 exécutée, aligné sur section Limites, H-002 ouvert)
- lot ingest W27: etude-ctr-ai-overviews-gsc + dossier Leexi (call 06-24 + kw RGPD) tirés par travail réel ; golfiller-strat skip documenté (2ᵉ non-exécution)
- contradiction: C-011 ouverte→acceptée (garde-fou chiffres glossaire, calque C-007)
- archivage: rien de mort ; 2 snapshots audit périmés = ressort de audit-vault-hygiene, pas ici
- fil rouge: mots-clés non mangés par l'IA (Leexi + query 06-24) → mûr pour édition Algorithme

## [2026-06-29] backlog | sweep — 201 en backlog (P1:92 P2:38 P3:71)
- 341 fichiers raw scannés (+10 vs sweep 06-22), toute la matière fraîche = terrain client Leexi + Alexia
- nouveaux P1 (10) : dossier organikk/clients/leexi/ (9 — 2 calls 06-24, livrable mots-clés business, arborescence-cocons, 5 fichiers keywords/clusters/cocons) + alexia/2026-06-24-call-1-resume
- mouvement skip : golfiller-strat sort du backlog → skip documenté (déjà acté W26, 2ᵉ non-exécution)
- prochain lot proposé : etude-ctr-ai-overviews-gsc + dossier Leexi (call 06-24 + recherche kw RGPD) — lot W27 voté en W26, toujours non exécuté, tiré par la newsletter « mots-clés non mangés »
- nouveaux skips: aucun

## [2026-07-02] doctrine | Routine quotidienne Reddit + Journal
- source: [[Playbook-Reddit-SEO-GEO]]
- pages créées: 2 (raw/reddit-playbook/Routine-quotidienne.md, raw/reddit-playbook/Journal.md)
- quotas posés: 4-6 commentaires/jour (plafond 10), 1 mention/semaine, 1 post/semaine (mar-mer 19-22h Manille), bilan vendredi, refresh 90j

## [2026-07-02] verification | Routine Reddit vérifiée contre le web
- 3 audits web parallèles (~25 sources 2025-2026) sur la routine [[Playbook-Reddit-SEO-GEO]]
- corrections: plafond commentaires 10→8, plafond dur 3 posts/semaine, fenêtre post 1h+6-10h, cross-post 6h+/3-4 subs, refresh 90j nuancé (threads cités = ~900j d'âge moyen, Semrush)
- ajouts: ciblage threads déjà positionnés Google (Perplexity source via SERP), format 120-200 mots, pas de seuil d'upvotes (80% des cités <20), liste fixe 15-20 requêtes acheteur, section 2026 (pages traduites ?tl=, Reddit Answers)

## [2026-07-02] build | Reddit Cockpit branché sur la routine
- repo ~/Code/reddit-cockpit (scrape RSS lecture seule + skill reddit-cockpit), launchd 07h50
- routine quotidienne mise à jour : étape commentaires assistée par la file queue/ du cockpit
- la machine ne publie jamais, clic manuel (même règle que x-cockpit)

## [2026-07-02] update | Playbook Reddit : couche exécution + corrections vérif web
- section « L'exécution : routine + Reddit Cockpit » ajoutée en tête du playbook (wikilinks Routine-quotidienne, Journal)
- corrections marquées dans le corps : timing (étude Upvote.net = 150 posts), 1re heure au lieu de 30 min, cross-post 6h+/3-4 subs, fraîcheur mensuelle au lieu du refresh 90j, cadence 4-6/j plafond 8
- note de fiabilité : la Routine-quotidienne fait foi sur les chiffres d'exécution

## [2026-07-03] revue-presse | Google remet des clics dans ses réponses IA
- output: raw/revue-de-presse/2026-07-03-revue-presse.md
- info du jour: liens cliquables réintégrés dans les réponses IA (recettes AI Mode 1er juillet + 5 changements de mai + rebond CTR Seer 1,3%→2,4%)
- brèves: pubs ChatGPT ouvertes UK/Japon/Corée/Brésil/Mexique / étude Kevin Indig data propriétaire et citations / retraite Fabrice Canel (Bing, IndexNow)
- pilier dominant: SEO
- skill déclenché: revue-presse-quotidienne + ton-de-voix-tim
- écarté: Cloudflare 15 septembre (déjà en brève les 26/06, 01/07 et 02/07), spam update juin (info du jour du 29/06)

## [2026-07-03] update | Qadence : conscience temporelle + DA Métriques
- entités touchées : 1 ([[entities/qadence-seo-agent]] : 2 sections ajoutées, état 2026-07-03)
- journal de dev : entrée 2026-07-03 dans qadence/Journal.md
- concepts liés : [[concepts/memory-llm-vs-wiki-persistant]] (timeline + décisions + preuves mesurées, côté produit)
- angle SEO : boucle de résultat J+14/J+30 = la « fiche preuve » du vault portée en SaaS

## [2026-07-03] design | Playbook Reddit refait en DA Reddit
- Playbook-Reddit-complet.html/pdf refaits : feed Reddit (posts votés, flairs, u/timboussardon, AutoModerator, carte communauté), IBM Plex Sans
- build.py posé dans raw/reddit-playbook/ : regénère HTML+PDF depuis les 3 .md sources

## [2026-07-03] rewrite | Playbook + routine Reddit réécrits en registre factuel
- tout le writing refait au format brèves : fait + chiffre + source datée, phrases courtes, zéro framing narratif
- titres de sections = descriptions sèches (ex. « 2. Reddit dans les moteurs génératifs » au lieu de « le vrai jackpot »)
- habillage HTML aligné (AutoModerator, sommaire, topbar) ; fix pandoc tex_math_dollars (M$/an rendus en italiques)
- DA Reddit conservée telle quelle

## [2026-07-03] rewrite | Playbook Reddit v3 : phrases complètes + corrections Tim
- phrases complètes partout (fini le télégraphique), mot « karma » banni (→ réputation)
- note de fiabilité retirée, sources déplacées en toute fin (après l'annexe routine)
- tableau quotas simplifié à 2 colonnes (Action | Quota), plus de mention d'outils dans la routine
- annexe Journal retirée du document généré (le fichier Journal.md reste le suivi)
- section 9bis ajoutée : les 8 prompts Reddit (sujets de niche depuis les questions Reddit), repris de wiki/briefs/reddit-pour-geo-2026

## [2026-07-03] update | Playbook Reddit : programme de lancement 30 jours + aération
- section 4 refaite en vrai programme de lancement de compte : 4 phases J1→J30, actions par jour, paliers chiffrés, critères de passage, interdits ; plan 90 jours réaligné (lancement = jours 1-30)
- lignes d'actions (commentaires/partager/enregistrer/signaler) retirées de tous les posts
- textes aérés : gros paragraphes découpés, espacements CSS augmentés

## [2026-07-03] edit | Playbook + routine Reddit : passe d'édition anti-IA complète
- 12 corrections verbatim de Tim + ~55 tournures compilées réécrites (« la donnée de cadrage », « le cadre de risque », « les tactiques documentées », « la conséquence opérationnelle »...)
- zéro info ni source supprimée ; voix directe rétablie (« c'est le mauvais plan », « effet de second tour », « verrouillé par contrat »)
- fix phrase orpheline en §fraîcheur (« Elle consiste à » sans antécédent)

## [2026-07-03] voix | Corpus my-voice enrichi : cartographie du slope IA
- entrée datée append-only dans raw/notes/tim-my-voice.md : les 11 corrections verbatim de Tim (playbook Reddit) + familles de tournures bannies (sujets nominaux abstraits, passifs de compilation, étiquettes creuses) + test « un expert dirait ça à voix haute ? »
- règles dures : fragments nominaux interdits même en factuel, mot « karma » banni (→ réputation)
- le skill ton-de-voix-tim lit ce corpus : les règles s'appliquent à toute rédaction future

## [2026-07-03] revue-hebdo | Semaine W27 — 7 décisions, 2 mouvements exécutés en séance
- promotions: 0 draft→stable, 0 stable→stale (refresh source playbook Reddit renvoyé à l'ingest W28)
- hypothèse en test: H-009 seule vivante — échéance J+30 Golfiller tombée le 2026-07-03 sans mesure, export GSC à déposer avant 2026-07-07 sinon `ouvert` en W28 (conditionnel pré-arbitré)
- lot ingest W28: Leexi (call 06-24 + recherche RGPD) en tête + etude-ctr-ai-overviews avec date de mort + refresh [[sources/2026-06-19-playbook-reddit-seo-geo]]
- contradiction fermée: C-004 `ouverte`→`résolue` (entité Qadence vivante = référence d'état, snapshot = photo datée)
- archivage: [[keywords/recherche-2026-06-05-consultant-seo-startup]] `draft`→`stale`
- résurgence: mercredi 2026-07-01 muet (3ᵉ, ticket ops LaunchAgent), pas de verdict à ratifier
- fil rouge: édition « mots-clés non mangés » sort en W28 ou se gèle ; fil Reddit attend les données du programme 30 jours
- output: [[revue-hebdo/2026-W27]]

## [2026-07-03] session | Playbook Reddit : version finale ligne claire + skill redaction-guide
- playbook + routine réécrits en « ligne claire » (une idée par ligne, donnée d'abord, ligne de chute), mise en page validée par Tim sur le modèle du post Trailblazer
- sections rédigées par Tim reprises verbatim : Cycle mensuel (fraîcheur), 7. Formats de contribution ; §14 Métriques réécrite (quoi/comment/quelle question) ; §7bis renvoie au prompt 8 pour les subs
- skill global `redaction-guide` créé (~/.claude/skills) : les 7 règles du rythme + structure guide + interdits + auto-check ; corpus my-voice enrichi (cartographie slope IA + échantillon canonique)
- livrable : raw/reddit-playbook/Playbook-Reddit-complet.html (DA Reddit) + .pdf, régénérables via build.py

## [2026-07-04] update | Playbook Reddit : section « Trouver tes mots-clés avant d'attaquer »
- vraies captures des vues Qadence (Performances + table Requêtes GSC), prises en local via Playwright sur le mode preview (data démo organikk.co, badge Démo visible)
- section placée avant §1 : la table Requêtes alimente les threads prioritaires (positions 4-12), les mots-clés de douleur et la liste fixe du vendredi
- build.py : images embarquées en base64 (HTML autonome), CSS figure/figcaption, break-inside avoid sur les images

## [2026-07-04] session | Playbook Reddit : benchmark guides + section Qadence + CTA, prêt pour diffusion
- benchmark de 2 guides récents (Search Engine Land, SevenSEO) + tactique Dulait : 6 ajouts sourcés (banc de test, veille positive, demande de marque, outil gratuit, relations mods, ciblage mot-clé) ; rien pris de Sorank (consigne Tim)
- section « Trouver tes mots-clés avant d'attaquer » : 2 vraies captures Qadence (Performances + table Requêtes GSC, mode démo), lien qadence.io
- CTA final en post sponsorisé Reddit (bordure orange, bouton Essayer Qadence)
- ÉTAT : guide validé pixel perfect par Tim, envoi prévu semaine du 6 juillet 2026 ; ne plus toucher au contenu sans lui ; option avant envoi = captures sur sa GSC réelle

## [2026-07-04] redaction | Newsletter process Claude recherche mots-clés
- output: newsletter-IA/2026-07-04-process-claude-recherche-mots-cles.md (draft, épisode 2 série « Mon process Claude pour... »)
- format hérité de la newsletter maillage 2026-05-06 (tableau comparatif en bloc 1)
- preuve : run réel [[keywords/recherche-2026-05-27-agence-seo]] → clustering → décisionnels (78 → 50 → 51 → 10 Tier 1)
- skill déclenché: ton-de-voix-tim (+ seo-recherche-mots-cles en source du process)

## [2026-07-05] ingest | Rattrapage scrape Algorithme (Substack) + blog Organikk
- source_type: article
- sources créées: 21 (12 Algorithme Substack du 13/05 au 01/07 + 9 blog Organikk du 25/04 au 24/06)
- Algorithme: [[sources/2026-05-13-algorithme-process-verifier-indexation]] · [[sources/2026-05-19-algorithme-10-convictions-seo]] · [[sources/2026-05-27-algorithme-methode-claude-semantique]] · [[sources/2026-06-02-algorithme-geo-pas-un-scam]] · [[sources/2026-06-05-algorithme-fin-des-backlinks-llms]] · [[sources/2026-06-09-algorithme-ia-detruire-business-seo]] · [[sources/2026-06-12-algorithme-youtube-domine-fanout]] · [[sources/2026-06-17-algorithme-creez-votre-agent-seo]] · [[sources/2026-06-19-algorithme-test-reddit-seo]] · [[sources/2026-06-24-algorithme-fin-des-mots-cles]] · [[sources/2026-06-29-algorithme-livres-ia-amazon]] · [[sources/2026-07-01-algorithme-x2-trafic-3-mois]]
- Organikk: [[sources/2026-04-25-organikk-reddit-pour-geo]] · [[sources/2026-04-29-organikk-9-skills-seo-claude]] · [[sources/2026-05-08-organikk-ranker-chatgpt-2026]] · [[sources/2026-05-12-organikk-role-consultant-seo-2026]] · [[sources/2026-05-15-organikk-ameliorer-redaction-ia-claude]] · [[sources/2026-05-27-organikk-5-skills-seo-technique-claude]] · [[sources/2026-06-03-organikk-systeme-seo-ia-complet]] · [[sources/2026-06-11-organikk-construire-agent-seo-claude]] · [[sources/2026-06-24-organikk-mots-cles-qui-ramenent-du-clic]]
- wikilinks: 6-9 sortants/fiche, 0 lien mort (vérifié)
- entities/concepts créés: 0 (manquants récurrents signalés à Tim, décision de curation à part)
- angle SEO: bascule autorité backlinks→discours/mentions, fin du mot-clé→modèle de page, agents SEO (prompt/skill/loop), data propriétaire comme seul avantage durable

## [2026-07-05] curation | Création entities/concepts récurrents manquants (post-scrape Algorithme/Organikk)
- entities créées (6): [[entities/gemini]] · [[entities/amazon-rufus]] · [[entities/shopify]] · [[entities/wikipedia]] · [[entities/ahrefs]] · [[entities/sparktoro]]
- concepts créés (5): [[concepts/query-fan-out]] · [[concepts/requete-cliquable-vs-clic]] · [[concepts/dette-cognitive]] · [[concepts/fraicheur-contenu]] · [[concepts/boucle-sortie-mesure]]
- câblage: wikilinks réciproques ajoutés dans 8 fiches sources (backrefs 2-3/nœud, 0 lien mort)
- index.md: nœuds ajoutés sous leurs sous-sections + compteurs ; concepts.json à 122 nœuds

## [2026-07-05] ingest | Scrape auto publications (Algorithme + Organikk)
- source_type: article
- sources créées: 8 ([[sources/2026-04-12-organikk-wiki-ia-obsidian-claude]], [[sources/2026-04-05-organikk-audit-seo-claude-7-phases]], [[sources/2026-03-25-organikk-etude-42000-urls-contenu-ia]], [[sources/2026-03-15-organikk-grok-seo-pipeline-data]], [[sources/2026-03-05-organikk-strategie-seo-du-moment]], [[sources/2026-02-20-organikk-information-gain-geo]], [[sources/2026-02-10-organikk-creer-bot-ia-seo]], [[sources/2026-01-28-organikk-premier-agent-seo-ia]])
- posts sautés (déjà ingérés): 22 (Algorithme: 12/12 de l'archive déjà ingérés, aucune nouveauté depuis 2026-07-01 ; Organikk: 10 récents déjà en fiche individuelle)
- posts laissés pour le prochain run (cap 8/run): 4 plus anciens Organikk — roadmap-seo-2026 (20 jan), mots-cles-seo-2026 (15 jan), strategie-seo-serrurier-lyon (12 jan), strategie-seo-agence-immobiliere-lyon (8 jan)
- note dédup: les 12 anciens Organikk (jan→avril) n'avaient pas de fiche individuelle avec clé URL — seulement l'agrégat [[sources/2026-04-12-organikk-blog-scrape]]. Fichage individuel fait pour couper le faux-"NEW" récurrent.
- wikilinks: min 2/fiche (2 à 7), 0 lien mort (vérifié)
- nœuds suggérés (à créer en curation): aucun (toutes les cibles existaient)
- angle SEO transverse: la doctrine Organikk du T1 2026 est déjà là — effort éditorial > outil de production, data propriétaire + faits atomiques comme seul avantage défendable, agent SEO spécialisé duplicable.

## [2026-07-06] backlog | sweep — 210 en backlog (P1:98 P2:38 P3:74)
- 349 fichiers raw scannés (+8 vs sweep 06-29) ; 9 net-new classés
- nouveaux P1: dossier client Victoria Garden (3), pré-call Origin 137 (1), reddit-playbook Playbook+Routine (2, source_type doctrine)
- nouveaux P3: 2 transcripts vidéo growth externes, reddit-playbook/Journal (test-terrain Qadence)
- prochain lot proposé: reddit-playbook/Playbook-Reddit-SEO-GEO (terrain vivant, reddit-cockpit quotidien + test Qadence), dossier Victoria Garden (client actif), dossier Leexi (lot W27 non exécuté, fil "mots-clés non mangés")
- nouveaux skips: aucun

## [2026-07-07] pseo | Organikk : modèles de pages corpus
- skill déclenché: seo-programmatique-pseo
- output: [[queries/pseo-2026-07-07-organikk-corpus]]
- data: GSC organikk.co 90j (edge admin-gsc-export) + inventaire vault (65 concepts, 57 entities, 90 sources)
- 6 modèles classés, P1 = bibliothèque de workflows Claude × SEO (backlog 49 mots-clés Lot 1)
- anti-cannibalisation posée avec [[corpus-qadence]] (diagnostics + lexique restent chez Qadence)

## [2026-07-07] pseo | Organikk corpus : backlogs concrets par modèle (itération 2)
- output: [[queries/pseo-2026-07-07-organikk-corpus]] (section ajoutée)
- modèle 1: 20 pages workflows mappées skill → requête, 2 trous 70/30 flagués (claude vs chatgpt, mcp seo)
- modèle 2: 13 études écrites non publiées identifiées (published: false) + 5 sujets candidats
- modèle 3: 22 concepts + 15 entities du vault non exposés sur /wiki
- modèle 4: 7 études first-party listées ; modèle 5: 6 fiches preuves candidates

## [2026-07-07] ingest | Moteurs IA : chiffres d'usage juillet 2026 + fiche Perplexity organikk
- source: [[sources/2026-07-07-moteurs-ia-chiffres-usage]] (collecte web, confidence medium sur Mistral/DeepSeek)
- entities créées: [[entities/mistral]], [[entities/deepseek]] ; enrichie: [[entities/perplexity]] (fiche d'identité)
- exposition publique: /wiki/perplexity-ai sur organikk.co (template wiki étendu : identity/facts/comparison/sources)
- trou noté: doc crawler MistralAI-User à sourcer ; Reuters DeepSeek à recouper en source primaire

## [2026-07-07] update | Fiche produit Perplexity complète (organikk /wiki)
- source enrichie: [[sources/2026-07-07-moteurs-ia-chiffres-usage]] (produit, gamme 2026, valorisation, procès, Cloudflare)
- exposition: /wiki/perplexity-ai = fiche produit complète (identité, dates clés, gamme, données, comment être cité, controverses, comparatif 6 moteurs, sources)
- template wiki organikk: champ blocks[] ajouté (réutilisable pour les autres fiches moteurs)

## [2026-07-07] pseo | Organikk : retrait fiche produit wiki + 5 modèles alternatifs (itération 3)
- décision Tim: modèle « fiche produit moteur IA » retiré du site (échoue au test de substitution LLM)
- revert organikk-next 80c582a ; la matière reste au vault ([[sources/2026-07-07-moteurs-ia-chiffres-usage]])
- nouveaux modèles M7-M11 dans [[queries/pseo-2026-07-07-organikk-corpus]] : skills téléchargeables, verdicts de test, objections de calls, observatoire mensuel, série stratégie datée

## [2026-07-07] product-led | Organikk : modèles anti-ChatGPT (clic obligatoire)
- skill déclenché: seo-product-led-seo
- output: [[queries/product-led-2026-07-07-organikk-anti-chatgpt]]
- 3 familles : transactionnel ultra-niché (5 pages offre), outils data propriétaire (5 concepts), preuve vérifiable
- signaux GSC : « bootcamp seo » 34 imp pos 30,4 sans page dédiée ; analyse-geo pos 13,6
- garde-fou : outils Organikk = démos qui vendent Tim, Fusionn garde la plateforme d'outils

## [2026-07-07] build | Organikk : outil « testeur de requête mangée » (anti-ChatGPT famille B)
- décision Tim: go sur le concept 1 de [[queries/product-led-2026-07-07-organikk-anti-chatgpt]]
- livré: /outils/testeur-requete-mangee (verdict déterministe par signaux d'intention + data vérifiée Semrush/Ahrefs/SparkToro, variantes à clic, zéro volume affiché, zéro score fabriqué)
- règle ajoutée en test: contrainte budget (« à moins de X € ») = signal décisionnel même sans autre modificateur
- commit local organikk-next, pas de push (deploy = auto sur push main, à la demande de Tim uniquement)

## [2026-07-07] update | Outil Organikk renommé « Probabilité de citation sur les LLMs »
- slug /outils/probabilite-citation-llm (jamais déployé, pas de redirection nécessaire)
- verdict enrichi : ligne « Probabilité d'une réponse IA » chiffrée par intention (Semrush oct. 2025)
- copy page validée par Tim (section calcul en 3 éléments + FAQ 4 questions)

## [2026-07-07] pseo | Organikk corpus : transposition des modèles bxble (itération 4)
- inventaire bxble : ~15 modèles en prod ; GSC 90j jeune mais lexique = modèle le plus exposé (43 pages)
- nouveaux modèles M12-M15 dans [[queries/pseo-2026-07-07-organikk-corpus]] : corpus QRG (signal GSC organikk déjà présent), base crawlers IA + générateur robots.txt, base Schema.org, différences
- leçon bxble : base finie exhaustive → outil lecteur → pages ; la longue traîne s'expose d'abord par la base

## [2026-07-07] pseo | Organikk corpus : itération 5 (N1-N4), filtre recalibré
- M12-M15 rejetés ; constat sur 4 rejets : documenter l'existant = commodité, survivent l'outil interactif appliqué au cas du visiteur et la data que Tim seul possède
- N1 pages-décision interactives, N2 bibliothèque avant/après anti-IA writing (data des sessions d'édition), N3 bancs d'essai modèles IA sur tâches SEO, N4 pipeline « trous de l'IA » (directories-data-ia opérationnalisé)

## [2026-07-07] publication | Guide Reddit SEO GEO publié sur organikk.co
- URL: https://organikk.co/blog/guide-reddit-seo-geo/ (transcription du playbook canonique, sans la section test Qadence)
- vidéo intégrée (L'influence de Reddit sur le SEO IA) + cocon maillé : hub Do du sous-pilier GEO, 6 liens déclarés dans internal-links.ts
- publiés le même jour : outil /outils/probabilite-citation-llm, article automatiser-audit-seo-claude-code, refonte design (miniatures picto, glossaire, guides teintés, nav)
- boucle preuves : poser la baseline GSC de ces URLs vers J+30 (début août 2026)

## [2026-07-10] etude-IA | Crawlers IA : GPTBot, ClaudeBot, PerplexityBot, robots.txt 2025-2026
- skill: seo-page-statistiques (SyntheticBrain)
- output: [[agent-synthetic/revuedepressIA/etudes-IA/2026-07-10-stats-crawlers-ia-gptbot-claudebot-perplexitybot-robots-txt]]
- sources vérifiées par fetch: 8 (Ahrefs, Cloudflare ×4, BuzzStream, cloro.dev, DigitalApplied, TechnologyChecker, SE Ranking)
- transformation originale: réconciliation des 3 mesures de blocage GPTBot (5,89 % web général / 13,9 % domaines visibles / 62 % éditeurs presse)
- chiffres clés: GPTBot +305 % volume mai 2024-mai 2025 ; ClaudeBot profondeur 5,2 vs GPTBot 3,8 ; blocage GPTBot = 139× moins de citations ChatGPT ; Anthropic 286 930:1 crawl/référral jan. 2025
- contre-analyse: DigitalApplied 12 sites (faible échantillon) ; corrélation ≠ causalité (blocage/citations) ; shadow crawl Perplexity-User ; llms.txt non pris en charge par Google
- [À SOURCER]: données profondeur > 100 sites, taux blocage francophone, causalité blocage contrôlée

## [2026-07-10] revue-hebdo | Semaine W28 — 7 décisions
- édition: [[revue-hebdo/2026-W28]]
- promotions: 0 draft→stable, 0 stable→stale (binôme corpus promotable à la 1re page publiée)
- hypothèses: H-009 en-test→ouvert (conditionnel W27 appliqué, J+30 Golfiller non mesuré) · H-007 ouvert→en-test (fiche [[preuves/2026-07-10-organikk-batch-juillet-data-proprietaire]], GSC organikk.co branchée via edge admin-gsc-export)
- lot ingest W29: refresh playbook Reddit en tête + Leexi avec date de mort · etude-ctr-ai-overviews-gsc skippé en séance (4 votes, édition gelée)
- contradiction fermée: aucune · C-003 débloquée de son « zéro mesure » structurel (note au registre)
- archivage: jeudi-4-infos — Tim tranche avant W29 sinon stale par défaut
- résurgence: 2026-07-08 muette (2e consécutive) → migration GH Actions avant le 2026-07-15
- fil rouge: corpus Organikk (publier + mesurer via boucle preuves) · édition « mots-clés non mangés » gelée

## [2026-07-10] preuve | organikk-batch-juillet → en-cours (H-007 en-test)
- fiche: [[preuves/2026-07-10-organikk-batch-juillet-data-proprietaire]]
- cohorte: 3 URLs publiées le 2026-07-07 (guide Reddit SEO/GEO, outil probabilite-citation-llm, article automatiser-audit-seo-claude-code)
- baseline: structurelle (URLs neuves, zéro historique GSC) + état site au run indexation 2026-07-10
- jalons: J+30 = 2026-08-06 · J+90 = 2026-10-05

## [2026-07-10] hypothese | H-009 → ouvert · H-007 → en-test
- H-009: clause de falsification W27 appliquée, fiche golfiller annotée « J+30 non mesuré », échéances J+90 seules actives
- H-007: conditions W25 remplies (sprint réel + baseline avant décision + instrument GSC en place)

## [2026-07-11] ingest | Scrape auto publications (Algorithme + Organikk)
- source_type: article
- sources créées: 7 ([[sources/2026-07-08-algorithme-redaction-claude]], [[sources/2026-07-07-organikk-guide-reddit-seo-geo]], [[sources/2026-07-07-organikk-automatiser-audit-seo-claude-code]], [[sources/2026-01-20-organikk-roadmap-seo-2026]], [[sources/2026-01-15-organikk-mots-cles-seo-2026]], [[sources/2026-01-12-organikk-seo-serrurier-lyon]], [[sources/2026-01-08-organikk-seo-agence-immobiliere-lyon]])
- posts sautés (déjà ingérés): 33 (11 Algorithme + 22 Organikk vérifiés par URL)
- wikilinks: min 2/fiche, 0 lien mort (vérifié)
- nœuds suggérés (à créer en curation): concepts/topical-authority (cité dans roadmap-seo-2026 et mots-cles-seo-2026) · concepts/cocon-semantique (pivot des 2 articles SEO local) · entities/coudac (agence citée dans redaction-claude)
- angle SEO transverse: la frontière IA/humain se précise partout — l'IA exécute (audit diff, transposition d'idées), l'humain garde la pensée, le ton et la data propriétaire ; les 4 articles de janvier montrent la doctrine déjà en place avant les posts système

## [2026-07-13] revue-presse | Avis Google Business Profile effacés par erreur
- output: raw/revue-de-presse/2026-07-13-revue-presse.md
- info du jour: avis GBP disparus (3-12 juillet, enquête Google en cours) — pilier SEO local
- brèves: GPT-5.6 + ChatGPT Work (OpenAI) / Semrush AI Visibility Index 126M prompts / llms.txt inutile selon Google
- connexion doctrine: data propriétaire (les avis Google ne sont pas un actif possédé)
- 1034 mots, checks anti-IA + anti-jargon passés

## [2026-07-13] backlog | sweep — 240 en backlog (P1:123 P2:35 P3:82)
- 373 fichiers raw scannés (+24 vs sweep 2026-07-06)
- sorties backlog : ranker-chatgpt → [[sources/2026-05-08-organikk-ranker-chatgpt-2026]], strategie-seo-serrurier-lyon → [[sources/2026-01-12-organikk-seo-serrurier-lyon]], strategie-seo-agence-immobiliere-lyon → [[sources/2026-01-08-organikk-seo-agence-immobiliere-lyon]] (scrape publications 07-05/07-11) ; etude-ctr-ai-overviews-gsc sorti par skip acté [[revue-hebdo/2026-W28]]
- ingéré à chaud sans passer par le backlog : call-14-vincent-upscale → [[sources/2026-07-09-call-14-vincent-upscale]] (couvre aussi upscale-call-vincent + upscale-preaudit)
- entrées backlog (21 P1) : sprint corpus Victoria Garden (7), pré-calls horizoncrm/simplimo/upscale-email/yalp + modèle pre-email (9), sprint corpus Golfiller (3), leexi/keywords/mots-cles-prioritaires-2026-07-09 (1), x-playbook/Modele-tweet-SEO (1)
- régularisation (9 P3, jamais comptés) : scheduled-skills ×3, fusionn/README, qadence-seo-agent/README, scoring/opendecoder, cas-clients ×2, clients/golfiller
- note comptage : P1 du sweep précédent affiché 98 mais sommant à 102 dans son propre listing — recompté from scratch
- prochain lot proposé (= lot W29 voté [[revue-hebdo/2026-W28]]) : refresh [[sources/2026-06-19-playbook-reddit-seo-geo]] (tête de lot), leexi-call-2026-06-24-notes-meet + keywords/recherche-2026-06-16-rgpd (date de mort W29) ; option : stack-corpus-victoriagarden + victoriagarden-faits-verifies-2026-07-10
- nouveaux skips: aucun (le skip etude-ctr avait été acté en W28)
