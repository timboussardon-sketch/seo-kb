# Roadmap de prestation Organikk (playbook vivant)

> Séquence ordonnée de tout ce qu'on fait sur un client SEO/GEO, du jour 0 à l'autonomie. C'est le playbook **maître** : il se nourrit de chaque tâche réelle faite sur un client (boucle d'apprentissage du skill `roadmap-prestation`). Quand un nouveau client arrive, on déroule cette liste dans l'ordre, adaptée à son cas.
>
> Doctrine : « du 0 à 1 puis autonomie », 4 piliers (status quo, mots-clés business, autorité thématique, micro-intentions). Le système finit par remplacer le consultant. Réf : [[golfiller-strat]], `raw/organikk/_MODELE-discours-commercial.md`.
>
> Statut d'une étape : **éprouvé** (déjà fait sur un vrai client) ou **doctrine** (prévu, pas encore validé terrain). MAJ par le skill, jamais à la main de mémoire.

Dernière mise à jour : 2026-07-01 (étape 2b ajoutée : interview de cadrage client, gate de compréhension avant l'audit ; batterie + protocole dans `prestation/interview-cadrage.md`)

---

## Phase 0 — Cadrage et accès

**1. Onboarding et récupération des accès + data propriétaire**
Récupérer : accès Search Console + GA4, et la data métier (transcripts de calls commerciaux, tickets SAV, e-mails, CRM, avis clients, ton de voix). Sans data propriétaire en input, le système ne tourne pas, c'est le pré-requis non négociable.
Premier contact post-vente : envoi du dashboard client + 3 docs de contexte à remplir (about-me, my-rules, my-voice) + vidéo explicative. Modèle d'email : `prestation/emails.md` §1 (exemple Alexia 2026-06-11).
Le montage technique du kit livré au client (dashboard + kit skills + vault Obsidian zippé) suit un process reproductible : **cf. Annexe A — Runbook « monter le kit d'accompagnement »** (éprouvé Alexia 2026-07-01).
Input client : accès + exports. Output : `raw/organikk/clients/<slug>.md`. Skills : aucun. Statut : éprouvé.

**2. Pré-call et diagnostic d'entrée**
Document pré-call : résumé, diagnostic, angle, état SEO (sitemaps, indexation grossière), pSEO multi-axes pressenti, roadmap 90j, notes. Réf format : `raw/organikk/pré-call/<prospect>.md`.
Output : doc pré-call. Skills : aucun (gabarit pré-call). Statut : éprouvé.

**2b. Interview de cadrage client**
Après la signature, avant de produire quoi que ce soit : l'agent confirme qu'il a **bien compris le contexte**. Il fait tourner le scan public de `seo-pre-audit` pour former ses hypothèses, puis **interviewe Tim** en rounds thématiques (batterie resserrée ~20 questions, 8 thèmes : business, cible, différenciation/data propriétaire, état SEO, data/accès, objectif, voix/tabous, relation). Chaque question part d'une hypothèse tirée du public que Tim confirme ou corrige ; l'inconnu devient « à poser au client », jamais une invention.
Gate : produire un bloc « Ce que j'ai compris » (15 lignes max) et le faire valider par Tim avant l'étape 3. Le cadrage oriente ce qu'on cherche dans la GSC.
Batterie + protocole complet : `prestation/interview-cadrage.md`. Sortie stockée dans `clients/<slug>.md` section « Cadrage (interview) ».
Version client-facing embarquée dans le kit d'accompagnement : le workflow `workflow-cadrage` (généré par `alexia-seo/build-dataset.py`, 1er des workflows du kit + du vault Obsidian, présenté en tête du dashboard). C'est l'entrée du kit : Claude interroge l'utilisateur sur tout le contexte puis liste les docs/accès manquants.
Input : scan public + réponses. Output : bloc cadrage validé + liste des manques. Skills : `seo-pre-audit` (scan), `roadmap-prestation` (orchestration), `workflow-cadrage` (kit client). Statut : doctrine.

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
Méthode apprise (leexi, 2026-06-26) — **cocons mère/fille/petite-fille + couche GEO transversale** : structurer chaque cocon en hiérarchie lisible **page mère** (pilier) → **pages filles** (sous-thèmes) → **pages petites-filles** (les vraies requêtes), une page = une ligne. Architecture type d'un client : (1) un **cocon produit** (cœur, volume, conversion), (2) un **cocon différenciateur** (l'angle que les acteurs US/génériques ne tiennent pas, ex. conformité/RGPD/souveraineté), (3) un **cocon « problématiques IA métier »** (cocon plein, pas une couche résiduelle) — angle propre : le **problème de métier résolu par l'IA**, organisé par fonction (Sales/CS/Recrutement) + secteur + hub « agent IA entreprise ». Ce qui le distingue du cocon produit et lève la cannibalisation : le cocon produit cible la requête **produit** (`compte rendu rendez-vous commercial`), le cocon métier cible la requête **problème** (`comment automatiser le suivi de mes calls commerciaux`, `IA pour le suivi commercial`). Volume Google FR faible mais forte réponse des IA → orienté **citation IA + maillage vers les pages business**. **Seule règle anti-doublon** : si une requête est *littéralement* identique à une page produit (`compte rendu X`), garder la page produit et y intégrer l'angle « comment… » en H2/FAQ ; sinon page propre dans le cocon métier (à confirmer en overlap SERP réel). Frontière MECE à surveiller en priorité : la visio (gratuit vs conforme vs intégration) et l'ISO (produit vs juridique).
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
- [[prestation/clients/alexia]] — accompagnement 1:1 consultante SEO (agence e-commerce), setup système ; kit d'accompagnement complet livré (dashboard + kit skills + vault Obsidian avec tous les skills) — client de référence de l'Annexe A

---

## Annexe A — Runbook détaillé : monter le kit d'accompagnement (dashboard + vault + skills)

> Ce qu'on livre à CHAQUE nouveau client pour qu'il branche la doctrine et les skills dans son Claude (Cowork ou Claude Code). Process reproductible à l'identique, commande par commande. **Éprouvé : Alexia (2026-07-01).** Suivre les étapes dans l'ordre : chacune finit par un **point de contrôle** à vérifier avant de passer à la suite.
>
> Convention : `<slug>` = identifiant client (ex. `alexia`). Remplacer partout. Les commandes sont copiables telles quelles après avoir posé la variable `SLUG`.

### A.0 — Les 3 artefacts livrés (vue d'ensemble)

| Artefact | Fichier | Rôle | Format skill |
|---|---|---|---|
| **Dashboard** | `organikk-next/public/<slug>-accompagnement/index.html` (+ `dataset.html`) | Page d'accueil client : install, workflows, livrables | — |
| **Kit « dataset »** | `public/<slug>-accompagnement/alexia-dataset.zip` + repo privé `alexia-seo-kit` | Chemin d'install PROPRE des skills (déjà `SKILL.md`) | `SKILL.md` |
| **Vault Obsidian** | `public/<slug>-accompagnement/vault-seo-organikk.zip` | Doctrine complète + skills lisibles dans Obsidian | `<nom>.md` |

Le dashboard sert les deux zips en téléchargement. Le vault et le kit portent les mêmes skills, à deux formats : le kit pour brancher vite, le vault pour lire/naviguer dans Obsidian.

### A.1 — Prérequis (une fois)

```bash
# repos et venv attendus
ls ~/Code/organikk-next          # site (Netlify auto-deploy sur push main)
ls ~/Code/alexia-seo             # générateur du kit (build-dataset.py)
ls ~/Code/alexia-seo-kit         # repo skills poussé, cloné par le client
ls ~/Code/seo-kb/.venv/bin/python  # venv qui a pyyaml + modules du vault
```

Pose les variables de session (réutilisées dans tout le runbook) :

```bash
SLUG=alexia                                   # <-- slug du client
ON=~/Code/organikk-next
PUB="$ON/public/${SLUG}-accompagnement"
KIT=~/Code/alexia-seo-kit
```

### A.2 — Étape 1 : dashboard client

Cloner le dashboard d'un client existant, puis adapter.

```bash
cp -R "$ON/public/alexia-accompagnement" "$PUB"     # gabarit de référence = Alexia
```

À adapter dans `$PUB/index.html` : nom du client, contexte, voix, liens des workflows (Google Docs), libellés de téléchargement. **Garder** `<meta name="robots" content="noindex,nofollow,noarchive,nosnippet" />` sur chaque page (`index.html`, `dataset.html`) — un espace client ne s'indexe jamais.

**Point de contrôle** : `grep -c 'noindex' "$PUB/index.html" "$PUB/dataset.html"` > 0 sur chaque fichier.

**Variante « phase de démarrage »** (éprouvé Catherine 2026-07-03) : quand le client n'a pas encore répondu au questionnaire, ouvrir le dashboard avec le SEUL onglet Questionnaire actif (tous les autres `locked: true`) et persister les réponses en ligne : upsert Supabase `client_selections` (projet fusionn, `doc_key = '<slug>'`, debounce ~900 ms, la version la plus récente gagne au chargement) en plus du localStorage. Ajouter un `admin.html` (clone de `catherine-accompagnement/admin.html`) pour lire les réponses côté Organikk, et le bloc noindex du slug dans `public/_headers`. Gabarit de référence : `public/catherine-accompagnement/`.

### A.3 — Étape 2 : kit skills « dataset » (source des skills)

Le kit est généré, pas assemblé à la main. Il produit les skills au bon format `SKILL.md` + les catalogues `SKILLS.md` / `WORKFLOWS.md`, et sert de source à l'étape vault.

```bash
cd ~/Code/alexia-seo
./build-dataset.sh          # lance build-dataset.py (venv seo-kb) PUIS git push alexia-seo-kit
```

Ce que ça fait : régénère `~/Code/alexia-seo-kit/` (34 dossiers de skills + `seo-doctrine/` + `SKILLS.md` + `WORKFLOWS.md`), écrit le zip miroir `alexia-dataset.zip` sur le dashboard, puis commit + push le repo kit.

**Point de contrôle** — la sortie doit afficher :
```
garde-fou fuite client : ✓ aucun
```
Si elle affiche « ✗ FUITE CLIENT détectée », le build s'arrête : corriger la source du skill fautif avant de continuer (cf. A.5, piège `\b`).

> Limite connue : `build-dataset.py` écrit un chemin **codé en dur** (`ZIP_DST = .../alexia-accompagnement/alexia-dataset.zip`). Pour un autre slug, éditer `ZIP_DST` (et le nom du repo `OUT`) avant de lancer, ou copier le zip produit vers `$PUB/`. TODO : paramétrer par `SLUG`.

### A.4 — Étape 3 : vault Obsidian zippé

**Automatisé** depuis 2026-07-01 par `alexia-seo/build-vault.py` (une commande) :

```bash
cd ~/Code/alexia-seo && ./build-vault.sh "$SLUG"
```

Le script part de la doctrine du zip vault existant (baseline), ré-injecte TOUS les skills du kit (sauf `ton-de-voix-tim`), renomme chaque `SKILL.md` en `<nom>.md`, régénère `SKILLS.md` / `WORKFLOWS.md` / la section skills de `000-START-HERE.md`, lance les garde-fous confidentialité (A.5) et re-zippe. Idempotent. Il **ne déploie pas** : il écrit le zip, le push reste explicite (A.6). Sortie attendue : `garde-fou confidentialité : ✓ aucun`.

> Le détail ci-dessous documente ce que fait le script (utile pour débugger ou monter un vault à la main si besoin). Le déroulé manuel se fait dans un dossier de travail jetable.

```bash
WORK="$(mktemp -d)"; cd "$WORK"
unzip -q "$PUB/vault-seo-organikk.zip"        # -> $WORK/vault-seo-organikk/
V="$WORK/vault-seo-organikk"
SAP="$V/skills-a-partager"
```

**3a. Peupler `skills-a-partager/` avec TOUS les skills** (depuis le kit de l'étape 2) :

```bash
rm -rf "$SAP"; mkdir -p "$SAP"
for d in "$KIT"/*/; do name=$(basename "$d"); cp -R "$d" "$SAP/$name"; done
find "$SAP" -name .DS_Store -delete
```

**3b. Retirer la voix perso de Tim** (jamais chez un client) :

```bash
rm -rf "$SAP/ton-de-voix-tim"
```

**3c. Renommer chaque `SKILL.md` en `<nom>.md`** (sinon 30+ fichiers « SKILL » illisibles dans Obsidian) :

```bash
for d in "$SAP"/*/; do n=$(basename "$d"); [ -f "$d/SKILL.md" ] && mv "$d/SKILL.md" "$d/$n.md"; done
find "$SAP" -maxdepth 2 -name SKILL.md      # doit être VIDE
```

**3d. Catalogues + porte d'entrée.** Copier les catalogues générés par le kit et adapter leur intro au contexte vault :

```bash
cp "$KIT/SKILLS.md" "$KIT/WORKFLOWS.md" "$V/"
```
Puis éditer à la main :
- `SKILLS.md` / `WORKFLOWS.md` : intro « les skills sont dans `skills-a-partager/`, pour les activer copie-les dans `~/.claude/skills/` **en renommant en `SKILL.md`** ». Retirer la fiche `ton-de-voix-tim` de `SKILLS.md` (elle n'est plus dans le pack) et ajuster le compte.
- `000-START-HERE.md` : section « Les skills et workflows » qui pointe vers `skills-a-partager/` (nb de skills), `SKILLS.md`, `WORKFLOWS.md`, avec la consigne de renommage à l'install.

**3e. Re-zipper avec le wrapper `vault-seo-organikk/`** (structure exacte du zip d'origine) :

```bash
cd "$WORK"; find . -name .DS_Store -delete
rm -f "$PUB/vault-seo-organikk.zip"
zip -rqX "$PUB/vault-seo-organikk.zip" vault-seo-organikk -x '*.DS_Store'
```

**Point de contrôle** :
```bash
unzip -l "$PUB/vault-seo-organikk.zip" | grep -c 'skills-a-partager/[^/]*/SKILL.md'   # = 0 (tout renommé)
unzip -l "$PUB/vault-seo-organikk.zip" | grep -cE 'skills-a-partager/[^/]+/[^/]+\.md'  # = nb de skills
```

### A.5 — Étape 4 : garde-fous confidentialité (OBLIGATOIRE avant deploy)

Deux catégories de fuite : **clients privés** (Leexi, FG Formation → jamais nulle part) et **slugs internes** (`feedback_<client>_...` dans les skills). Golfiller est un cas **public** : toléré dans la doctrine (`wiki/`, `raw/`), jamais dans un fichier de skill.

```bash
# 1) clients privés : doit être VIDE partout dans le vault
grep -rliE "leexi|fg.?formation" "$V"

# 2) slugs/refs dans les skills livrés : doit être VIDE (scan SANS \b, cf. piège)
grep -rliE "leexi|fg.?formation|golfiller" "$SAP"
```

Si le second scan remonte un fichier, ouvrir et **neutraliser la référence** (ex. remplacer `` (cf. `feedback_golfiller_sources_sites_marques` : …) `` par une formulation générique), puis re-zipper (A.3e) et re-scanner. **Ne pas déployer tant que les deux scans ne sont pas vides.**

### A.6 — Étape 5 : deploy + vérification live

`organikk.co` auto-déploie sur push `main` (Netlify). Règle dure : le push = la prod → obtenir le feu vert de Tim.

```bash
cd "$ON"
git add "public/${SLUG}-accompagnement/"
git commit -m "Kit d'accompagnement <slug> : dashboard + kit skills + vault (tous les skills)"
git push origin HEAD
```

Vérifier **en live** (Netlify propage en ~40-60 s → boucler 2-3 fois) :

```bash
cd "$(mktemp -d)"; curl -s -o v.zip "https://organikk.co/${SLUG}-accompagnement/vault-seo-organikk.zip"
echo "skills          : $(unzip -l v.zip | grep -cE 'skills-a-partager/[^/]+/[^/]+\.md')"
echo "SKILL.md restants: $(unzip -l v.zip | grep -c 'skills-a-partager/[^/]*/SKILL.md')"   # doit être 0
echo "ton-de-voix-tim : $(unzip -l v.zip | grep -c 'skills-a-partager/ton-de-voix-tim/')"  # doit être 0
```

### A.7 — Étape 6 : libellés du dashboard

Mettre à jour dans `$PUB/index.html` (deux endroits : le corps du step « Récupère le vault » et le sous-titre du bouton de téléchargement) : **nb de notes de doctrine**, **nb de skills**, **taille du zip**. Idem `dataset.html` si présent. Distinguer proprement : « notes » = fichiers `.md` de doctrine ; le nombre d'**entrées** du zip (dossiers + `.obsidian`) est plus grand, ne pas le confondre avec les notes.

### A.8 — Checklist finale

- [ ] Dashboard cloné, adapté, `noindex` sur toutes les pages
- [ ] `build-dataset.sh` OK (« fuite client : ✓ aucun »), repo kit poussé
- [ ] Vault : tous les skills dans `skills-a-partager/`, fichiers `<nom>.md` (0 `SKILL.md`), `ton-de-voix-tim` retiré
- [ ] `SKILLS.md` / `WORKFLOWS.md` / `000-START-HERE.md` à jour (comptes + consigne de renommage)
- [ ] Scans confidentialité vides (clients privés + slugs dans les skills)
- [ ] Push organikk-next (feu vert Tim) + vérif live curl OK
- [ ] Libellés dashboard à jour (notes + skills + taille)
- [ ] Tracker client + `log.md` mis à jour (boucle d'apprentissage)

### A.9 — Pièges & dette technique

- **Regex `\b` — RÉSOLU (2026-07-01)** : le `sanitize()` de `build-dataset.py` utilisait `\b(...)\b`, qui **rate les slugs collés aux underscores** (`feedback_golfiller_sources_...`). Corrigé en frontières « lettres » `(?<![a-z])(...)(?![a-z])` (attrape underscore/chiffre comme frontière). `build-vault.py` applique le même scan. Le double scan de A.5 reste une ceinture de sécurité.
- **Build vault reproductible — RÉSOLU (2026-07-01)** : `alexia-seo/build-vault.py` automatise l'étape A.4 (baseline doctrine + injection skills + renommage + catalogues + garde-fous + zip, idempotent). L'ancien assemblage manuel n'est plus la voie normale.
- **`build-dataset.py` mono-client** : `ZIP_DST` et le repo `OUT` sont codés en dur sur Alexia. Paramétrer par `SLUG` avant multi-clients.
- **Nom de fichier skill** : `SKILL.md` (nom exact) est requis pour le déclenchement auto Claude/Cowork. Les `<nom>.md` du vault sont **uniquement** pour la lecture Obsidian → l'install doit les renommer en `SKILL.md`. Le kit dataset, lui, est déjà au bon format : c'est le chemin d'install à recommander.
- **Deux chemins d'install** : kit dataset (rapide, déjà `SKILL.md`) vs vault (lisible, à renommer). Ne pas les confondre dans la com client.
- **Cache CDN** : après deploy, un ancien zip peut rester en cache navigateur → re-télécharger avec `?v=2`. La vérif `curl` tape l'origine et voit la vraie version.

Statut : éprouvé (Alexia).

## Annexe B — Runbook : créer le Drive client (modèle Leexi)

Référence vivante : Drive « Leexi — SEO (Organikk) », créé le 2026-07-03 → https://drive.google.com/drive/folders/12_5gi10IpJbLTCyrzSpnGGkrmf8yLdDF. C'est L'EXEMPLE à répliquer quand Tim dit « crée le drive client ».

### B.1 — Principes

- Le Drive est un **miroir lisible** du vault client : la source de vérité reste le vault, chaque doc Drive est un export daté. Après toute évolution majeure d'un doc canonique, régénérer son export.
- **Docs canoniques uniquement** (ceux listés dans la home du vault), jamais les versions supersédées : le Drive doit rester scannable par le client.
- Nettoyage à l'export : frontmatter YAML retiré, wikilinks aplatis en texte simple. Conversion markdown → Google Doc via MCP Drive (`create_file`, contentMimeType `text/markdown`).
- Les sheets d'exécution validés (redirections, sélections de mots-clés…) sont **copiés dans le dossier** concerné : la copie dans le Drive devient la canonique.

### B.2 — Structure (numérotée, dans l'ordre de lecture)

- `00 — Lisez-moi` : navigation, résumé de la stratégie en un paragraphe, règles d'exécution (jamais de 410 → 301, zéro chiffre sans source, gate ton de voix avant CMS, rien publié sans validation), liste des validations en attente.
- `01 — Stratégie` : brief client canonique, stratégie SEO-GEO, livrable mots-clés business + cocons validé.
- `02 — Mots-clés et cocons` : liste complète groundée, clustering page à page, un doc par cocon.
- `03 — Analyses` : GSC approfondie, audit thématique, étude de marché, études juridiques/secteur.
- `04 — Quick wins` : liste des pages à optimiser + réécritures (drafts à valider).
- `05 — Élagage et redirections` : audit d'élagage + sheet d'exécution 301 + audits de redirections historiques.
- `06 — Ton de voix` : la fiche maître du client.
- `07 — Optimisation par mot-clé` : un sous-dossier par mot-clé travaillé (vecteurs sémantiques + brief Hn dedans), micro-intentions transverses à la racine du 07. Ajout de Tim le 03/07 : dès qu'on entre en production page par page, le rangement par mot-clé prime sur le rangement par type de doc.

### B.3 — Exécution

1. Créer racine + sous-dossiers via MCP Drive (mimeType folder).
2. Paralléliser les exports par agents : un agent par lot de 4-5 docs, chaque agent lit → nettoie → `create_file` avec parentId.
3. Copier les sheets validés dans leur dossier (`copy_file`).
4. Le MCP Drive n'a **pas d'outil de suppression ni de déplacement** : signaler à Tim les doublons restés à la racine, c'est lui qui supprime.
5. Fin de course : lien du Drive en tête de la home du vault client, entrée Journal, et email client « suivi en direct » (modèle §3 de `prestation/emails.md`).

Statut : éprouvé (Leexi, 2026-07-03).

Pages liées : [[golfiller-strat]] · [[clusters/modeles-pseo-2026-06-10-golfiller]] · [[queries/2026-06-10-golfiller-gsc-6mois]] · [[concepts/product-led-seo]] · [[concepts/know-simple-know-do]]
