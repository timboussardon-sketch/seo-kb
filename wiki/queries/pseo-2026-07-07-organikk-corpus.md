---
type: pseo-strategy
title: "Organikk : modèles de pages corpus pour ranker"
aliases: [pseo-organikk-corpus, modeles-organikk]
tags: [organikk, pseo, corpus, geo, aeo, claude, data-proprietaire]
created: 2026-07-07
updated: 2026-07-07
sources: 4
confidence: medium
status: draft
---

# Organikk : modèles de pages corpus pour ranker

Application de la doctrine [[corpus-qadence|Corpus]] (corpus d'abord, pages en sous-produit) au site organikk.co. Skill `seo-programmatique-pseo`, données du 2026-07-07.

## État des lieux (data réelle)

GSC organikk.co, 90 jours (export edge `admin-gsc-export`) : 63 clics sur la home, quasi tout branded (« timothée boussardon », « organikk.co »). Aucune page ne capte encore de longue traîne. Deux signaux non-branded : « quality rater guidelines » (95 impressions, position 71 sur la page outil) et le cluster secteurs (« agence seo avocats paris », « consultant seo avocat », « agence seo sophrologue », « freelance seo sea hotellerie », impressions unitaires mais réelles).

Matière propriétaire disponible : vault seo-kb (65 concepts, 57 entities, 90 sources), 23 skills SEO documentés, 22 études `/statistiques` en prod avec pipeline d'ingest, brèves quotidiennes, ~30 propriétés GSC connectées à Fusionn, instrumentation Golfiller, boucle preuves (fiches J+30/J+90), backlog de 49 mots-clés qualifiés ([[raw/organikk/mots-cles-a-traiter|mots-clés à traiter]]).

## Le produit d'Organikk

Le produit, c'est le système de Tim : le vault + les skills + les preuves terrain. L'accompagnement et le bootcamp vendent ce système. La doctrine corpus dit : les pages qui rankent sont l'exposition publique de la matière que le système produit déjà pour fonctionner. Le coût des pages est déjà payé.

## Les 6 modèles, classés

### 1. Bibliothèque de workflows Claude × SEO (priorité absolue)

- **Corpus** : les 23 skills SEO de Tim + les transcripts de sessions réelles + les résultats mesurés (Golfiller, Fusionn, bxble). Le corpus existe à 100 %, il fait tourner la prestation et le bootcamp.
- **Pages** : 1 page par workflow. Pattern `/systeme/[workflow]`. H1 = « [Tâche SEO] avec Claude Code : le workflow complet ». Chaque page contient le pipeline réel, les prompts/commandes exacts, un cas mesuré en GSC, les limites constatées.
- **Requêtes** (backlog Lot 1, quasi vierges en FR) : « comment utiliser claude code pour le seo », « claude code audit seo », « connecter claude code à google search console », « claude code maillage interne », « automatiser la recherche de mots-clés avec l'ia », « créer un agent seo ia », « générer des pages programmatiques avec claude », « créer un skill claude code seo ».
- **Taille** : ~25-35 pages, corpus fini.
- **Avantage** : personne en FR ne publie des workflows qu'il fait réellement tourner, avec la preuve GSC dessous. Une IA qui répond « comment utiliser claude code pour le seo » n'a que ce corpus à citer.
- **Conversion** : CTA accompagnement + bootcamp sur chaque page, l'intention Do/Décision est déjà dans la requête.

### 2. Études statistiques en flux (industrialiser l'existant)

- **Corpus** : la veille quotidienne (brèves) fait déjà remonter les études. Chaque étude majeure devient une page `/statistiques` via `scripts/ingest-etude.mjs`. 22 pages en prod.
- **Pages** : requêtes « [sujet] chiffres / statistiques / taux 2026 ». Cadence cible : 2-4 études/mois, tirées des brèves.
- **Avantage** : le coût est payé par la veille. Pages extractibles, conçues pour la citation IA (claims atomiques, sources datées).
- **Taille** : illimité, en flux.

### 3. Wiki concepts GEO/IA, extension vault

- **Corpus** : 65 concepts + 57 entities dans le vault, 39 seulement exposés sur `/wiki`. L'écart est du stock prêt à publier (règle 70/30 déjà satisfaite par construction).
- **Pages** : +60-80 fiches atomiques. Requêtes Know-Simple : « grounding score seo », « rrf », « passage ranking », « agentic search », définitions GEO encore vierges en FR.
- **Avantage** : le vocabulaire propriétaire (grounding score, inversion expertise, triade SERP) n'a qu'une seule source possible. Maillage automatique vers les workflows (modèle 1) et les études (modèle 2).

### 4. Benchmarks first-party (l'actif incopiable)

- **Corpus** : ~30 propriétés GSC connectées à Fusionn + pipeline Qadence + instrumentations (Golfiller). Anonymisation à réception + DPA, comme sur les dashboards.
- **Pages** : études originales chiffrées. « CTR réel par position en 2026 sur N sites FR », « CTR × AI Overviews » (déjà planifiée, [[project-etudes-originales]]), « effet mesuré d'un maillage interne sur 90 jours ».
- **Avantage** : Haute Surprise maximale, c'est le seul modèle que personne ne peut répliquer. C'est lui qui force la citation IA et les liens entrants naturels.
- **Taille** : 5-10 pages/an, différé partiel (dépend du volume de sites).

### 5. Fiches preuves publiques (cas mesurés)

- **Corpus** : la boucle preuves du vault (J+30/J+90, data GSC réelle). Chaque test terrain validé devient une page cas.
- **Pages** : « ranker sur [requête] sans backlink : les chiffres », « ce que 90 jours de pSEO secteur ont donné ». Pattern `/resultats/[cas]`.
- **Avantage** : E-E-A-T réel, personne ne publie ses J+90. Petit volume de requêtes, forte conversion, alimente tous les autres modèles en preuves.
- **Taille** : en flux, 1 page par preuve validée.

### 6. Secteurs × pSEO décisionnel (conditionné à la data)

- **Corpus** : à construire par secteur (requêtes Suggest via l'outil Fusionn, verbatims Reddit, peurs-objections). Le vault est mince par secteur : la règle 70/30 bloque tant que la data secteur n'est pas construite.
- **Pages** : « consultant seo [secteur] ». La GSC montre déjà des impressions (avocat, sophrologue, hôtellerie, habitat) sur 2 pages secteurs seulement.
- **Verdict** : signal réel mais modèle à ne lancer que secteur par secteur, quand un client du secteur paie la construction du corpus (même mécanique que le corpus-sujet Qadence : le travail client paie la page).

## Matrice de priorisation

| Modèle | Pages | Data dispo | Effort | Potentiel positions | Conversion | Priorité |
|---|---|---|---|---|---|---|
| 1. Workflows Claude × SEO | 25-35 | 100 % (skills + preuves) | Moyen | Fort (requêtes vierges FR) | Forte (Do/Décision) | P1 |
| 2. Études statistiques | flux | 100 % (pipeline en prod) | Faible | Fort (citations IA) | Moyenne | P1 |
| 3. Wiki concepts étendu | 60-80 | 100 % (vault) | Faible | Moyen (Know-Simple) | Faible directe | P2 |
| 4. Benchmarks first-party | 5-10/an | 60 % (agrégation à poser) | Fort | Très fort (Haute Surprise) | Forte (autorité) | P2 |
| 5. Fiches preuves publiques | flux | 80 % (boucle preuves) | Faible | Faible volume | Très forte | P2 |
| 6. Secteurs décisionnels | 1/secteur | 20 % (à construire) | Fort | Moyen | Forte | P3 conditionné |

Anti-cannibalisation : la bibliothèque de diagnostics GSC et le lexique des modificateurs restent chez Qadence ([[corpus-qadence]]). Organikk ne les duplique pas, il pointe vers Qadence.

## Plan 90 jours

Semaines 1-2 : structurer le corpus workflows (inventaire des 23 skills, sélection des 10 premiers, gabarit de page validé sur 1 pilote : « comment utiliser claude code pour le seo »).
Semaines 3-6 : publier 8-10 pages workflows, chacune avec cas mesuré. Cadence études maintenue (2/mois). Fiche preuve posée sur le pilote (baseline GSC).
Semaines 7-10 : extension wiki (+30 fiches vault), maillage workflows ↔ wiki ↔ études. Schéma d'agrégation des benchmarks first-party posé (anonymisation).
Semaines 11-13 : lot 2 workflows (10 pages), première étude originale publiée (CTR × AI Overviews), lecture GSC du pilote (J+60).

Montée en charge pilotée par la Search Console, jamais de déversement massif.

## Backlogs concrets par modèle (ajout 2026-07-07, itération 2)

### Modèle 1 : les pages workflows, skill par skill

Chaque page part d'un skill qui tourne réellement. 20 pages couvertes à 100 % par la matière existante.

| Page (H1 indicatif) | Skill(s) source | Requête cible (Lot 1) |
|---|---|---|
| Comment utiliser Claude Code pour le SEO (pilier/hub) | tous | comment utiliser claude code pour le seo |
| Connecter Claude Code à Google Search Console | maillage-interne-gsc, seo-quick-win | connecter claude code à google search console |
| Automatiser un audit SEO avec Claude Code | seo-geo-audit, seo-pre-audit | claude code audit seo |
| Claude Code pour le maillage interne | maillage-interne-gsc, maillage-systeme | claude code maillage interne |
| Automatiser la recherche de mots-clés avec l'IA | seo-recherche-mots-cles | automatiser la recherche de mots-clés avec l'ia |
| Clusteriser une liste de mots-clés avec Claude | seo-clustering-mots-cles | 1 cluster = 1 page |
| Isoler les mots-clés qui convertissent avec l'IA | seo-mots-cles-decisionnels | mots-clés décisionnels |
| Générer un brief SEO avec l'IA | seo-brief-contenu | générer un brief seo avec l'ia |
| Rédiger un article SEO avec Claude (workflow 8 étapes) | seo-workflow-article | rédiger un article seo avec claude |
| Éviter le AI writing en SEO | anti-ai-writing (concept vault) | éviter le ai writing en seo, humaniser un texte ia |
| Générer des pages programmatiques avec Claude | seo-programmatique-pseo, seo-roadmap-pseo | générer des pages programmatiques avec claude |
| Concevoir des pages satellites décisionnelles | seo-modeles-pseo | pages satellites, money page |
| Détecter la cannibalisation avec Claude + GSC | seo-cannibalisation | cannibalisation seo |
| Trouver ses quick wins dans la GSC avec Claude | seo-quick-win | quick wins gsc |
| Auditer l'indexation d'un site avec Claude Code | indexation-check | audit indexation |
| Construire un cluster AEO avec l'IA | seo-cluster-aeo | cluster aeo, topical authority |
| Cartographier les entités sémantiques d'une page | seo-entites-vectorielles | entités sémantiques, grounding score |
| Générer ses données structurées avec Claude | seo-donnees-structurees (+ outil en ligne) | données structurées ia |
| Connecter Obsidian à Claude (base de connaissances SEO) | kb-semantic-search + architecture vault | connecter obsidian à claude, rag seo |
| Créer un agent SEO IA / un skill Claude Code SEO | architecture skills (9-skills déjà bloggé) | créer un agent seo ia, créer un skill claude code seo |

Trous 70/30 identifiés : « claude vs chatgpt pour le seo » (comparatif, pas de skill dessous, matière à produire d'abord) et « mcp seo » (concept présent mais pas de workflow documenté au vault).

### Modèle 2 : études statistiques

Coup zéro : 13 études déjà écrites, `published: false`, à passer en revue puis publier (ai-overviews-ctr, ctr-par-position-google, parts-marche-moteurs-ia, contenu-ia-seo-classements, eeat-citations-ia-mesure, fraicheur-citations-ia-delais, profil-technique-pages-citees-ia, longueur-requetes-conversationnelles, usage-grand-public-chatgpt, ia-entreprise-france, seo-local-ia-presence-reponses, budgets-seo-reallocation-ia, sanctions-cnil-rgpd).

Nouvelles études candidates (sujets qui remontent dans les brèves, sources publiques agrégables) : crawl des bots IA sur les sites (GPTBot, ClaudeBot, données Cloudflare), trafic référent envoyé par ChatGPT/Perplexity aux sites, part des requêtes conversationnelles dans le Search, statistiques d'adoption des agents IA en entreprise, chiffres du Search e-commerce (Rufus, comparateurs IA).

### Modèle 3 : wiki, le stock prêt à publier

Concepts du vault non exposés (~22 publiables tels quels) : query-fan-out, query-synthesis, structural-information-geo, ingenierie-semantique-inversee, test-substitution-llm, preuve-atomique, data-proprietaire, directories-data-ia, requete-cliquable-vs-clic, weight-decay, fraicheur-contenu, parasite-seo, seo-multi-plateforme, persistent-wiki-vs-rag, memory-llm-vs-wiki-persistant, know-simple-know-do, 5-types-ancres, angle-differenciant-mot-cle, anti-ai-writing, confidence-score, pseo-data-driven-models, metriques GEO (métriques présence/reco/fréquence).

Entities du vault non exposées (~15 fiches) : google-ai-mode, chatgpt-search, perplexity, notebooklm, gemini, grok, amazon-rufus, geo-bench, sageo-arena-benchmark, miras, neural-matching, bert, rankbrain, mum, bm25.

Restent internes (doctrine ou perso, pas de page) : tabou-visibilite, peur-train-ia, avatar-*, boucle-sortie-mesure, ton-de-voix-tim, 4w-deep-reflection, regle-ia-ne-le-fait-pas-je-le-fais-pas.

### Modèle 4 : benchmarks first-party, les études à poser

1. Pilote logs : les bots IA dans les logs serveur (déjà cadrée, [[project-etudes-originales]]).
2. CTR × AI Overviews sur les propriétés connectées (prochaine étude planifiée).
3. CTR réel par position 2026, agrégé multi-propriétés FR (version first-party de l'étude sourcée en draft).
4. Requête cliquable vs clic : part des impressions au-delà de la position 10 qui ne produisent jamais un clic (adosse le concept vault du même nom).
5. Délai médian entre publication et premier clic d'une page neuve (Golfiller, Fusionn, organikk : trois âges de site).
6. Effet mesuré d'un chantier de maillage interne à J+90 (data leenq + fiches preuves).
7. pSEO vs éditorial : répartition réelle des clics par type de page (Golfiller, 388 parcours nommés en GSC).

Prérequis commun : schéma d'agrégation anonymisé + DPA, seuil minimal de propriétés par chiffre publié.

### Modèle 5 : fiches preuves publiques

1. Ranker sur une verticale e-commerce sans un seul backlink : les chiffres Golfiller à 6 mois (striking distance « balle de golf », branded +43 %).
2. Anatomie d'un tableau de données à 5 652 clics (le tableau de compression Golfiller).
3. 90 jours de pSEO métier × ville : ce que la GSC montre ([[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]]).
4. Un corpus de 31 170 versets devenu des pages : le cas bxble (concordance → pages Versets).
5. Le pilote workflows Organikk à J+60 (à créer : baseline posée au lancement du modèle 1).
6. Cas client pSEO Qualiopi, ~100 pages sur 2 arbres (FG Formation, publication conditionnée à l'anonymisation + accord).

## Résumé exécutif

Organikk a un site jeune (GSC quasi entièrement branded) mais une matière propriétaire que les autres sites n'ont pas : 23 skills qui tournent réellement, un vault de 122 nœuds, un pipeline d'études en prod et ~30 propriétés GSC agrégables. Le modèle n°1 à lancer est la bibliothèque de workflows Claude × SEO : le corpus existe à 100 %, les 49 requêtes du backlog sont quasi vierges en FR, l'intention est décisionnelle, et chaque page se prouve avec de la data GSC réelle. Les études statistiques continuent en flux, le wiki s'étend sur le stock du vault, et les benchmarks first-party se préparent en tâche de fond : c'est le seul actif incopiable, celui qui forcera les citations IA.

Liens : [[corpus-qadence]], [[raw/golfiller/Corpus-Golfiller|corpus-golfiller]], [[concepts/surprise-gap]], [[concepts/grounding-score]], [[preuves/index]]
