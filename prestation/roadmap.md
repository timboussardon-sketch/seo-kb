# Roadmap de prestation Organikk (playbook vivant)

> Séquence ordonnée de tout ce qu'on fait sur un client SEO/GEO, du jour 0 à l'autonomie. C'est le playbook **maître** : il se nourrit de chaque tâche réelle faite sur un client (boucle d'apprentissage du skill `roadmap-prestation`). Quand un nouveau client arrive, on déroule cette liste dans l'ordre, adaptée à son cas.
>
> Doctrine : « du 0 à 1 puis autonomie », 4 piliers (status quo, mots-clés business, autorité thématique, micro-intentions). Le système finit par remplacer le consultant. Réf : [[golfiller-strat]], `raw/organikk/_MODELE-discours-commercial.md`.
>
> Statut d'une étape : **éprouvé** (déjà fait sur un vrai client) ou **doctrine** (prévu, pas encore validé terrain). MAJ par le skill, jamais à la main de mémoire.

Dernière mise à jour : 2026-06-26 (leexi étape 7 éprouvée : cocons mère/fille/petite-fille + couche GEO transversale + inventaire 5 seaux + livrable Google Doc ; étape 6 enrichie : grounding fan-out + confrontation GSC)

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
Input : 4 CSV GSC. Output : `wiki/queries/<date>-<slug>-gsc-*.md` + CSV dans `raw/data/exports-gsc/`. Skills : analyse GSC + `maillage-interne-gsc` + [[seo-cannibalisation]]. Statut : éprouvé (golfiller).
Restitution client : Google Doc qui ouvre sur « En résumé : les 3 à 5 points à retenir », jargon traduit en langage métier, chiffres uniquement issus de la data, PUIS le même diagnostic dans l'onglet Audit de l'espace client (tiles KPI, plan d'action ordonné par Tim) (éprouvé Leexi 2026-06-12).

**4. Audit d'indexation**
Vérifier statut HTTP, blocages, noindex, sitemap, maillage entrant, contenu, indexation estimée. Distinguer non indexée vs non testable.
Output : rapport indexation. Skill : `indexation-check`. Statut : doctrine.

**5. Audit technique : Core Web Vitals + données structurées**
CWV mobile sur échantillon sitemap (Lighthouse local) + audit/mise en place du JSON-LD (graphe d'entité + schémas par page).
Skills : `seo-core-web-vitals`, `seo-donnees-structurees`. Statut : doctrine.

## Phase 2 — Stratégie

**6. Mots-clés business et décisionnels**
Recherche from scratch → clustering par SERP (1 cluster = 1 page) → isolement des mots-clés décisionnels (qui convertissent).
Méthode apprise (leexi) : cadrer les clusters AVEC le client (4 chez Leexi : problématiques par persona, intention d'achat, 1 page par fonctionnalité + outils gratuits, conformité/souveraineté), puis grounding data réel : scrape Google Suggest FR sur 60-80 seeds (vraies requêtes tapées), croisement avec la GSC (clics réels), confrontation d'une éventuelle matrice pSEO externe au filtre de requêtabilité humaine (exclusions documentées : géolocalisation pour un SaaS, pages prix/support d'outils tiers). Vocabulaire : « cluster », jamais « territoire ». Zéro volume inventé ([À SOURCER] sinon).
Méthode apprise (leexi, stratégie des 3 premiers mois) : une fois les clusters cadrés, **les ordonner par fonction stratégique, pas par volume**. (1) D'abord le terrain vierge qui porte la vente (chez Leexi : souveraineté/RGPD, 0 clic GSC = aucune concurrence de classement). (2) Ensuite le cluster qui répare une perte chiffrée (chez Leexi : intégrations, là où la refonte a fait −43 % hors-marque) = fort retour rapide. (3) En parallèle les outils gratuits Product-Led (les plus rapides à sortir, générateurs de texte, ils alimentent la capture d'email). Deux patterns réutilisables : un **cluster intégration** se construit en « produit × plateforme » (1 page par plateforme majeure + 1 par CRM + 1 hub de maillage, on cible les intégrations DU produit jamais le support d'outils tiers) ; un **cluster outils gratuits** = 1 outil = 1 famille de requêtes = 1 page, priorisé en MVP par ancrage data × faisabilité. Capter aussi des **verbatims utilisateurs réels** (Reddit, PAA) pour les besoins et la réassurance — quand le crawler est bloqué, les coller à la main. Discipline anti-cannibalisation transverse aux clusters : une intention = une page (le Know « enregistrer une réunion teams » maille vers le Do « notetaker teams » ; « gratuit »/« modèle » restent au cluster outils ; le juridique au cluster conformité). Préalable technique non négociable avant d'empiler du contenu : réparer une refonte cassée (301, canonicals, maillage), sinon les nouvelles pages repartent de zéro.
Skills : `seo-recherche-mots-cles` → `seo-clustering-mots-cles` → `seo-mots-cles-decisionnels` (+ `seo-product-led-seo` pour le cluster outils gratuits). Statut : éprouvé (leexi : 4 clusters cadrés le 12/06 ~95 mots-clés, puis approfondissement par cluster ordonné — souveraineté 56 KW le 16/06, intégrations ~55 + outils gratuits ~50 le 17/06, consolidés dans `leexi-seo/production/Strategie-clusters-leexi.md`).
Méthode apprise (leexi, 2026-06-26) — **grounding + inventaire 5 seaux** : lancer la recherche en **fan-out parallèle** (un sous-agent WebSearch par branche : SERP, People Also Ask, autocomplétion réelles), puis **confronter à la GSC** pour récupérer les signaux que le Keyword Planner rate : requêtes sous-exploitées (rankées sans page dédiée, ex. `teams compte rendu réunion automatique` pos 5,3), requêtes tapées en **anglais** (ex. `best ai note taker for lawyers` → à décliner en FR), intentions distinctes du cœur produit (ex. `agent ia entreprise` 310 impr). Quand le volume FR est nul, **c'est un signal, pas un échec** : marché qui se forme → bascule en couche GEO (étape 7). Consolider tous les mots-clés dans un **inventaire complet réparti en 5 seaux** : Money / Longue traîne / Questions clients / Requêtes sous-exploitées / SERP faibles (1 mot-clé = 1 seul seau). Règles dures : comparatifs vs **outils US uniquement** (vérifier la nationalité, exclure les pairs FR/EU) ; **jamais d'achat de lien** (autorité par contenu citable + data) ; data propriétaire du client (gain de temps réel, cas chiffrés) = carburant des citations IA, à réclamer ; chiffres remontés par l'IA = à re-sourcer en primaire avant publication.

**7. Architecture : piliers, clusters AEO, maillage**
Piliers business (3 à 5), cluster/cocon sémantique Know-Simple/Know/Do, plan de maillage (hub/satellite, ancres, orphelines).
Méthode apprise (leexi, 2026-06-26) — **cocons mère/fille/petite-fille + couche GEO transversale** : structurer chaque cocon en hiérarchie lisible **page mère** (pilier) → **pages filles** (sous-thèmes) → **pages petites-filles** (les vraies requêtes), une page = une ligne. Architecture type d'un client : (1) un **cocon produit** (cœur, volume, conversion), (2) un **cocon différenciateur** (l'angle que les acteurs US/génériques ne tiennent pas, ex. conformité/RGPD/souveraineté), (3) une **COUCHE GEO transversale** (pas un 3e cocon produit) — pages « problème métier » formulées en « comment + verbe », à volume Google quasi nul mais répondues par ChatGPT/Perplexity/AI Overviews ; leur rôle est la **citation IA + le maillage vers les pages business**, pas le volume. **Test décisif anti-doublon** (à chaque page de la couche GEO) : sa requête a-t-elle une SERP distincte d'une page produit existante ? Si oui → page propre ; si non → repli en **H2/FAQ** dans la page produit (zéro cannibalisation, nourrit quand même le GEO). Le hub « agent IA entreprise » (intention agent ≠ notetaker) est un cocon autonome légitime. Frontière MECE à surveiller en priorité : la visio (gratuit vs conforme vs intégration) et l'ISO (produit vs juridique).
Livrable client de cette phase : **3-5 mots-clés business** (têtes d'autorité thématique) + les cocons, en **Google Doc** voix Tim factuelle, titres en bleu, hiérarchie mère/fille/petite-fille, finissant sur des demandes de validation (bloquer les mots-clés, valider les intitulés métier contre le terrain, fournir les cas clients chiffrés). Confronter ensuite l'overlap SERP réel (SE Ranking) avant prod.
Skills : `seo-cluster-aeo`, `maillage-systeme`. Statut : éprouvé (leexi : 3 cocons — notetaker/réunion, RGPD, couche GEO — dans `raw/organikk/clients/leexi/keywords/`, livrable Google Doc mère/fille/petite-fille).

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
Brique éprouvée (leexi) : l'assistant de l'espace client est connecté au vault Obsidian du client (RAG pgvector `kb_chunks.project`, edge functions kb-chat/kb-ingest paramétrées, prompt vouvoiement). Mise en place pour un nouveau client : copier `leexi-seo/scripts/export-kb-chat.py` dans le repo client (changer PROJECT), lancer l'export, widget de l'espace passe `project:'<slug>'`. Relancer l'export après toute session qui modifie le vault.
Statut : doctrine (brique assistant : éprouvée leexi).

**14. Roadmap 30/60/90 livrée + dashboard client**
Calendrier 2 phases, section « mots-clés rejetés » qui protège le budget. Espace client HTML (sidebar + sections numérotées), hébergé noindex, PDF du même HTML via @media print.
Règles posées le 2026-06-12 (leexi) : même DA que le site public organikk.co (palette fzn : fond #F4F5F7, cartes blanches, accent #4685F0, typo Geist stricte) ; statuts d'onglets = petits points 7 px vert/jaune, jamais de badges texte ; chaque livrable validé alimente son onglet (Audit, Mots-clés...) en version simplifiée pour le client ; widget assistant connecté au vault du client (cf. étape 13).
Fin de semaine 1 : email « premier rapport » au client (modèle verbatim : `prestation/emails.md` §2) : ce qui est en ligne, un chiffre central par onglet, l'assistant, la prochaine étape datée.
Réf : `public/espace-leexi/index.html` (à cloner pour tout nouvel espace). Statut : éprouvé (Leexi).

**15. Suivi par preuves, onboarding du bot, passage en autonomie**
GSC à J+30 / J+90 sur les pages publiées, preuves mesurées. Onboarding du bot, montée en compétence, le client repart avec son système (« le système me remplace »).
Statut : doctrine.

---

## Index clients
- [[prestation/clients/golfiller]] — e-commerce balles occasion, à l'étape 11 (brief Hn page usage ; modèles directory usage/besoin ajouté)
- [[prestation/clients/leexi]] — B2B SaaS notetaker IA, étape 7 éprouvée (3 cocons mère/fille/petite-fille : notetaker/réunion + RGPD + couche GEO transversale ; 259 mots-clés en inventaire 5 seaux ; livrable Google Doc à valider) ; espace client complet (audit + mots-clés + assistant RAG)

Pages liées : [[golfiller-strat]] · [[clusters/modeles-pseo-2026-06-10-golfiller]] · [[queries/2026-06-10-golfiller-gsc-6mois]] · [[concepts/product-led-seo]] · [[concepts/know-simple-know-do]]
