# Roadmap de prestation Organikk (playbook vivant)

> Séquence ordonnée de tout ce qu'on fait sur un client SEO/GEO, du jour 0 à l'autonomie. C'est le playbook **maître** : il se nourrit de chaque tâche réelle faite sur un client (boucle d'apprentissage du skill `roadmap-prestation`). Quand un nouveau client arrive, on déroule cette liste dans l'ordre, adaptée à son cas.
>
> Doctrine : « du 0 à 1 puis autonomie », 4 piliers (status quo, mots-clés business, autorité thématique, micro-intentions). Le système finit par remplacer le consultant. Réf : [[golfiller-strat]], `raw/organikk/_MODELE-discours-commercial.md`.
>
> Statut d'une étape : **éprouvé** (déjà fait sur un vrai client) ou **doctrine** (prévu, pas encore validé terrain). MAJ par le skill, jamais à la main de mémoire.

Dernière mise à jour : 2026-06-10 (golfiller étape 10)

---

## Phase 0 — Cadrage et accès

**1. Onboarding et récupération des accès + data propriétaire**
Récupérer : accès Search Console + GA4, et la data métier (transcripts de calls commerciaux, tickets SAV, e-mails, CRM, avis clients, ton de voix). Sans data propriétaire en input, le système ne tourne pas, c'est le pré-requis non négociable.
Premier contact post-vente : envoi du dashboard client + 3 docs de contexte à remplir (about-me, my-rules, my-voice) + vidéo explicative. Modèle d'email : `prestation/emails.md` §1 (exemple Alexia 2026-06-11).
Input client : accès + exports. Output : `raw/organikk/clients/<slug>.md`. Skills : aucun. Statut : éprouvé.

**2. Pré-call et diagnostic d'entrée**
Document pré-call : résumé, diagnostic, angle, état SEO (sitemaps, indexation grossière), pSEO multi-axes pressenti, roadmap 90j, notes. Réf format : `raw/organikk/pré-call/<prospect>.md`.
Output : doc pré-call. Skills : aucun (gabarit pré-call). Statut : éprouvé.

## Phase 1 — Diagnostic data

**3. Analyse GSC (la première vraie passe data)**
Export pages + requêtes, en 90 jours ET en 6 mois comparé. En sortir : winners/losers, part branded vs non-branded, striking distance (pos 5-15, fortes impressions), CTR faible en bonne position, érosion de position, signaux pSEO (long tail sur une URL).
Input : 4 CSV GSC. Output : `wiki/queries/<date>-<slug>-gsc-*.md` + CSV dans `raw/data/exports-gsc/`. Skills : analyse GSC + [[maillage-interne-gsc]] + [[seo-cannibalisation]]. Statut : éprouvé (golfiller).
Restitution client : Google Doc qui ouvre sur « En résumé : les 3 à 5 points à retenir », jargon traduit en langage métier, chiffres uniquement issus de la data (éprouvé Leexi 2026-06-12).

**4. Audit d'indexation**
Vérifier statut HTTP, blocages, noindex, sitemap, maillage entrant, contenu, indexation estimée. Distinguer non indexée vs non testable.
Output : rapport indexation. Skill : `indexation-check`. Statut : doctrine.

**5. Audit technique : Core Web Vitals + données structurées**
CWV mobile sur échantillon sitemap (Lighthouse local) + audit/mise en place du JSON-LD (graphe d'entité + schémas par page).
Skills : `seo-core-web-vitals`, `seo-donnees-structurees`. Statut : doctrine.

## Phase 2 — Stratégie

**6. Mots-clés business et décisionnels**
Recherche from scratch → clustering par SERP (1 cluster = 1 page) → isolement des mots-clés décisionnels (qui convertissent).
Skills : `seo-recherche-mots-cles` → `seo-clustering-mots-cles` → `seo-mots-cles-decisionnels`. Statut : doctrine.

**7. Architecture : piliers, clusters AEO, maillage**
Piliers business (3 à 5), cluster/cocon sémantique Know-Simple/Know/Do, plan de maillage (hub/satellite, ancres, orphelines).
Skills : `seo-cluster-aeo`, `maillage-systeme`. Statut : doctrine.

**8. Modèles de pages pSEO (Money Page + Spokes)**
Modèles scalables 1 template + 1 variable, scoring Proximité × Intention × Faisabilité, roadmap pSEO 90j. Repérer la long tail validée par la GSC (parcours nommés, modèles de produit, profils). Méthode apprise (golfiller) : scraper le blog existant pour cartographier les directory déjà publiés (méga-page = hub), PUIS croiser avec les familles de requêtes GSC NON couvertes pour sortir de NOUVEAUX modèles (ex. balle par usage/besoin), et poser un garde-fou anti-cannibalisation entre axes proches (profil vs usage).
Skills : `seo-modeles-pseo`, `seo-programmatique-pseo`, `seo-roadmap-pseo`. Statut : éprouvé (golfiller : 7 modèles scorés, cf. [[clusters/modeles-pseo-2026-06-10-golfiller]]).

**9. Product-Led SEO (outils gratuits)**
Calculateurs, simulateurs, générateurs sur requêtes Do, capture d'e-mail, note Fully Meets.
Skill : `seo-product-led-seo`. Statut : éprouvé (golfiller : calculateurs index/score décollent).

**10. Angle de conversion : peurs/objections + entités vectorielles**
Pain points et verbatims Haute Surprise, puis entités sémantiques attendues par requête (Grounding Score, gap). Sur une Money Page qui perd des positions, l'analyse d'entités passe en priorité (défense + reconquête), même avant la prod pSEO.
Skills : `seo-peurs-objections`, `seo-entites-vectorielles`. Statut : éprouvé (golfiller : page « balle de golf », cf. [[queries/entites-2026-06-10-golfiller-balle-de-golf]]).

## Phase 3 — Production

**11. Briefs éditoriaux**
Structure Hn optimisée Passage Ranking, dérivée des vecteurs sémantiques, pas des concurrents.
Skill : `seo-brief-contenu`. Statut : doctrine.

**12. Rédaction (apprenante par projet)**
Pipeline complet + boucle d'apprentissage par client (claims, prédictions J+30/J+90, gate de publication), ton de voix client.
Skills : `content-brain` (enveloppe `article-engine-pipeline`), `ton-de-voix-tim`. Statut : doctrine.

## Phase 4 — Système et autonomie

**13. Mise en place du système SEO-IA propriétaire**
Bot construit sur la data + le ton de voix du client, skills, mémoire. Le système produit articles, newsletters, posts, supports commerciaux.
Statut : doctrine.

**14. Roadmap 30/60/90 livrée + dashboard client**
Calendrier 2 phases, section « mots-clés rejetés » qui protège le budget. Espace client HTML en DA Leexi (sidebar + sections numérotées), hébergé noindex, PDF du même HTML.
Réf : `public/espace-leexi/index.html`. Statut : éprouvé (Leexi).

**15. Suivi par preuves, onboarding du bot, passage en autonomie**
GSC à J+30 / J+90 sur les pages publiées, preuves mesurées. Onboarding du bot, montée en compétence, le client repart avec son système (« le système me remplace »).
Statut : doctrine.

---

## Index clients
- [[prestation/clients/golfiller]] — e-commerce balles occasion, à l'étape 11 (brief Hn page usage ; modèles directory usage/besoin ajouté)
- [[prestation/clients/leexi]] — B2B SaaS notetaker IA, fin de phase 1 (GSC diagnostiquée : refonte cassée, −43 % hors-marque) ; arbitrage réparation refonte vs territoire souveraineté en cours

Pages liées : [[golfiller-strat]] · [[clusters/modeles-pseo-2026-06-10-golfiller]] · [[queries/2026-06-10-golfiller-gsc-6mois]] · [[concepts/product-led-seo]] · [[concepts/know-simple-know-do]]
