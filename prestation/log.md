# Log roadmap-prestation

Append-only. Format : ## [YYYY-MM-DD] <client> | étape N | action

## [2026-06-10] système | bootstrap
- création prestation/ (roadmap.md maître, clients/, _template.md, log.md)
- roadmap seedée : 15 étapes en 5 phases (cadrage, diagnostic data, stratégie, production, système+autonomie)
- skill roadmap-prestation créé dans ~/.claude/skills/

## [2026-06-10] golfiller | étape 3 | analyse GSC 90j + 6 mois comparée
## [2026-06-10] golfiller | étape 8 | 7 modèles pSEO scorés

## [2026-06-10] golfiller | étape 10 | entités vectorielles page Money « balle de golf »
- output: [[queries/entites-2026-06-10-golfiller-balle-de-golf]]
- skill: seo-entites-vectorielles ; étape 10 doctrine -> éprouvée
- next: B modèle page par marque, C titres fiches produit, puis brief Hn -> content-brain

## [2026-06-10] golfiller | étape 8 | scrape blog + nouveau modèle directory usage/besoin
- méthode: lire le blog (directory déjà publiés) + croiser GSC non couvert
- output: [[clusters/modeles-pseo-2026-06-10-golfiller]] (section modèle additionnel usage/besoin)
- retenu par Tim: usage/besoin uniquement (écarté: local magasin, handicap, perso)
- next: étape 11 brief Hn page « balle de golf pour la distance » (template usage)

## [2026-06-10] golfiller | étape 11 | brief Hn page usage « balle de golf pour la distance »
- output: [[briefs/2026-06-10-balle-golf-distance]]
- skill: seo-brief-contenu ; template réplicable (contrôle, vent, durabilité, budget)
- next: prod via content-brain (étape 12)

## [2026-06-10] golfiller | étape 12 | article rédigé (draft) « balle de golf pour la distance »
- output: content-brain/golfiller/outputs/2026-06-10-balle-golf-distance.md
- skill: content-brain ; gate PASS-sous-réserve (distances par profil [À SOURCER] = bloqueur publication)
- claims verified: tech compression (3 sources), prix catalogue (proprio). écarté: distances par profil
- prédiction P-golfiller-2026-06-10-1 ouverte (pos <10 sur « balle pour la distance » à J+90)

## [2026-06-10] golfiller | étape 12 | enrichissement article (scrape data site)
- ajout table distance/vitesse de swing (claim 014, scrapée de la page vitesse-de-swing du site = data propriétaire)
- gate passe à PASS (~95%) ; reste seul [À SOURCER] : distance comparée PAR modèle (launch monitor)

## [2026-06-10] golfiller | étape 12 | version HTML/CSS de l'article (Shopify-ready)
- output: content-brain/golfiller/outputs/2026-06-10-balle-golf-distance.html (CSS scopé .gf-article, tableaux stylés, liens internes réels, bloc Sources)
- référencé dans entities/golfiller.md (section Articles produits)

## [2026-06-10] golfiller | étape 12 | set usage complet HTML/CSS (4 pages dupliquées)
- pages: contrôle, vent, durabilité, budget (+ distance déjà faite) = modèle directory usage complet
- output: content-brain/golfiller/outputs/2026-06-10-balle-golf-*.html (Shopify-ready, CSS scopé)
- said_index: 4 lignes (anti-cannib, 1 page = 1 besoin)

## [2026-06-11] alexia | étape 1 | premier email d'onboarding capturé
- création prestation/emails.md (modèles d'emails vivants)
- §1 premier email (envoi dashboard + 3 docs contexte + vidéo) = exemple Alexia verbatim
- roadmap.md étape 1 enrichie : renvoi vers emails.md §1

## [2026-06-18] alexia | setup | repo alexia-seo + skills + workflow mots-clés
- repo ~/Code/alexia-seo sur modèle leexi-seo (pack submodule + .claude/skills symlink)
- pack organikk-seo-pack enrichi : portage seo-recherche-mots-cles + seo-clustering-mots-cles + seo-brief-contenu → 11 skills, chaîne mots-clés complète (pushé)
- 3 docs contexte récupérés du Drive → brain/voix-alexia/ ; data/clients/ multi-client (5 pilotes)
- AGENTS.md + WORKFLOW-MOTS-CLES.md rédigés ; tracker clients/alexia.md créé
- état réel des docs : about-me complet, my-voice rempli (tutoiement clients, pattern CONSTAT→ISOLATION→ACTION, liste noire stricte), my-rules partiel ([À COMPLÉTER])
- piège évité : 1er tirage du Drive lisait un doublon my-voice vide ; vrai doc = 1NnrIBs…
- next : Alexia choisit le 1er compte → workflow mots-clés (export GSC) ; compléter les trous de my-rules

## [2026-06-12] leexi | tracker | création du tracker prestation (reprise client)
- état consolidé depuis leexi-seo/Journal.md (session 1 du 2026-06-09)
- étapes 1-3 faites + amorce 6 + étape 14 (espace client DA Leexi)
- en attente d'arbitrage : Bloc 1 réparation refonte vs Bloc 3 souveraineté

## [2026-06-12] leexi | étape 3 | restitution GSC en Google Doc (5 points clés en intro)
- doc : https://docs.google.com/document/d/1Xw0cvggBsokPz_nKAJUCY-EuewdkYJkTcBlSQne6cUg/
- roadmap.md étape 3 enrichie : format de restitution Google Doc + En résumé
- arbitrage bloc 1 (refonte) vs bloc 3 (souveraineté) toujours en attente

## [2026-06-12] leexi | étape 3+14 | diagnostic GSC publié dans l'onglet Audit de l'espace client
- même contenu que le Google Doc, en DA Leexi (tiles, sections numérotées, plan 4 blocs)
- déployé sur organikk.co (noindex)

## [2026-06-12] leexi | étape 6 | recherche mots-clés 4 clusters (data réelle Suggest + GSC)
- output: leexi-seo/production/recherche-mots-cles-2026-06-12.md + onglet Mots-clés espace client (Live)
- skill: seo-recherche-mots-cles ; suite: seo-clustering-mots-cles

## [2026-06-12] leexi | étape 6+8 | matrice pSEO (CSV Tim) confrontée à la data + réconciliation modèles×clusters
- retenus : comparatifs/migration, intégrations, problématiques, cas d'usage métier, outils gratuits, sécurité C4, tutoriels vidéo
- écartés : géolocalisation (requêtabilité humaine), prix/support d'outils tiers (impressions sous-exploitées)
- output : section 05 onglet Mots-clés + production/recherche-mots-cles-2026-06-12.md

## [2026-06-12] leexi | plan | ordre d'exécution arrêté par Tim
- 1) optimisation des 20 meilleures pages business, 2) mots-clés proches de l'intention d'achat, 3) modèles programmatique SEO
- remplace le plan en 4 blocs du diagnostic ; réparations refonte absorbées par l'étape 1

## [2026-06-12] leexi | étape 14 | assistant de l'espace connecté au vault client (RAG scopé project=leexi)
- kb_chunks.project + match filtré + prompt client vouvoiement ; 109 chunks (16 fichiers)
- règle durable : un assistant d'espace client répond sur le vault DU client, sinon pas de widget

## [2026-06-12] leexi | étape 14 | email de livraison de jalon (brouillon Gmail) + modèle capitalisé (emails.md §2)
- annonce : semaine du 15 juin = liste des 50 meilleurs mots-clés + stratégie étape par étape

## [2026-06-12] leexi | playbook | passe de capitalisation complète de la session
- étape 6 passée éprouvée (méthode clusters + Suggest + GSC + filtre matrice pSEO)
- étape 13 : brique assistant RAG client (export-kb-chat.py) éprouvée
- étape 14 : DA = site public (fzn), points de statut, email premier rapport §2, alimentation des onglets
- étape 3 : restitution = Google Doc + onglet Audit

## [2026-06-16] leexi | étape 6 | approfondissement cluster mots-clés RGPD
- 56 KW groundés data réelle (WebSearch PAA + variantes), 24 Do / 30 Know / 2 Know-Simple, 8 sous-clusters
- cadrage Tim : traduction juridique = feature produit → Do (pages de conversion, pas que de l'autorité)
- output : raw/organikk/clients/leexi/keywords/recherche-2026-06-16-rgpd.md
- next : seo-clustering-mots-cles puis seo-mots-cles-decisionnels sur les 24 Do

## [2026-06-17] leexi | étape 6 | stratégie de mots-clés des 3 premiers mois (3 clusters ordonnés)
- méthode capitalisée: ordonner les clusters par fonction (terrain vierge qui porte la vente > cluster qui répare une perte chiffrée > outils gratuits rapides), pattern cluster intégration "produit × plateforme", pattern cluster outils gratuits "1 outil = 1 page" priorisé en MVP, verbatims utilisateurs réels (Reddit collé main), discipline anti-cannibalisation transverse, préalable technique = réparer la refonte
- clusters: 2 intégrations (~55 KW), 3 outils gratuits Product-Led (~50 KW, 4 MVP) ; cluster 1 souveraineté/RGPD déjà fait le 16/06
- output: leexi-seo/production/Strategie-clusters-leexi.md (doc unique) + recherche-mots-cles-cluster2-integrations + recherche-mots-cles-cluster3-outils-gratuits + cluster3-outils-gratuits + besoins-reddit-cluster2
- skills: seo-recherche-mots-cles + seo-product-led-seo
- next: réparer la refonte (301/canonicals/maillage) -> clustering par SERP clusters 2/3 -> specs 4 MVP (data Leexi anonymisée) -> briefs Teams + Google Meet

## [2026-06-26] leexi | étape 6+7 | restructure 3 cocons + standardisation méthode mots-clés
- étape 6 : inventaire 259 mots-clés (fan-out WebSearch + confrontation GSC), 5 seaux
- étape 7 : architecture 3 cocons mère/fille/petite-fille (notetaker + RGPD + couche GEO transversale), arbitrage cannibalisation ; couche GEO ≠ cocon produit (décision)
- livrable client : Google Doc 4 mots-clés business + cocons à valider
- capitalisé dans roadmap.md : étape 6 (grounding fan-out + GSC + 5 seaux), étape 7 passée éprouvée (cocons mère/fille/petite-fille + couche GEO + test cannibalisation SERP)

## [2026-07-01] alexia | étape 1 | Kit d'accompagnement livré + runbook capitalisé (Annexe A roadmap)
- vault embarque tous les skills (skills-a-partager/, fichiers <nom>.md), ton-de-voix-tim retiré, slug client neutralisé
- SKILLS.md + WORKFLOWS.md ajoutés aux zips ; déployé organikk.co, vérifié live
- process reproductible ajouté : roadmap.md Annexe A « monter le kit d'accompagnement »

## [2026-07-01] système | étape 2b — interview de cadrage client
- nouvelle étape Phase 0 (2b) : gate de compréhension du contexte avant l'audit
- batterie resserrée ~20 questions (8 thèmes) + protocole interactif : prestation/interview-cadrage.md
- format = l'agent interviewe Tim (AskUserQuestion, hypothèses pré-remplies via seo-pre-audit)
- roadmap.md (étape 2b), _template.md (section Cadrage), skill roadmap-prestation mis à jour
- statut : doctrine (pas encore éprouvé sur un client)

## [2026-07-01] système | cadrage étendu — signaler les manques + kit client
- interview-cadrage.md : l'agent couvre tout le contexte + angles business, et SIGNALE explicitement les docs/accès manquants (section dédiée dans la sortie + gate)
- kit d'accompagnement : nouveau workflow client-facing `workflow-cadrage` (1er des workflows), généré par alexia-seo/build-dataset.py → embarqué kit + vault Obsidian
- dashboard Alexia : workflow cadrage en tête (section Workflows + roadmap semaine 1 « Cadrage, setup & data »), compteurs 34 skills / 4 workflows
- kit + vault régénérés en LOCAL (build-dataset.py + build-vault.py) ; PAS déployé, PAS de push (organikk = prod sur push main)

## [2026-07-03] catherine | étape 1 | espace client ouvert (questionnaire seul)
- dashboard public/catherine-accompagnement/ (gabarit Alexia) : Questionnaire ouvert, 8 onglets verrouillés
- réponses conservées en ligne : upsert Supabase `client_selections` (doc_key `catherine-accompagnement`, debounce 900 ms) + localStorage, la version la plus récente gagne au chargement
- lecture côté Organikk : catherine-accompagnement/admin.html (auto-refresh 30 s, copie totale)
- questionnaire adapté au call découverte : rapports clients + « par où commencer », rien de pré-rempli
- _headers : bloc noindex ajouté ; commit local 774c378, PAS poussé (organikk = prod sur push main)
- tracker créé : clients/catherine.md

## [2026-07-03] catherine | étape 1 | déployé sur organikk.co (push validé par Tim)
- organikk.co/catherine-accompagnement/ et admin.html en ligne (200), X-Robots-Tag noindex vérifié

## [2026-07-27] raphael | onboarding | espace client créé
- espace-raphael-fitness/ dans organikk-next (clone espace-leexi) : proposition, collecte, diagnostic, stratégie + 3 onglets à venir
- tracker créé : clients/raphael.md
- commit organikk-next 67d71be, PAS poussé (organikk = prod sur push main)
