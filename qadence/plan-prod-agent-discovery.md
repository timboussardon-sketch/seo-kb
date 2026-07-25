# Plan de prod — Agent Discovery

Rédigé le 2026-07-25. Cadre non négociable : Discovery est un agent autonome à côté de watcher/quickwin/cannibal. On ne touche ni à seo-agent ni au chat. Cadence hebdo (mercredi 6h). Le LLM ne découvre jamais rien : SQL → stats → validation → rédaction.

Mission de l'agent : découvrir des lois sur le site. Pas des erreurs, des lois. Chaque découverte doit être impossible ou très coûteuse à trouver à la main.

## Décisions du 25/07 (Tim)

**Architecture d'intelligence — Claude aux deux bouts, la stat au milieu.**
Claude planificateur en début de run (contexte du site + mémoire des découvertes → choisit et paramètre les hypothèses à tester, en propose de nouvelles), la stat en juge (SQL + seuils + réplication : Claude n'a pas le droit de vote), Claude interprète en fin de run (rédige la réflexion, relie les découvertes, hiérarchise par importance business). Même socle Claude que le produit, sans toucher à seo-agent. L'agent garde la mémoire de ce qu'il a testé par site : il ne repart jamais de zéro.

**Cadence par SITE (jamais quotidien sur un site)** : premier passage à J+1 après la mise en projet du site, puis tous les 7 jours. Mécanique : ticker quotidien 6h15 (`cron-discovery` + RPC `discovery_due_sites`) qui ne ramasse que les sites dus, plafonds 8 sites/user et 150/tick. EN PROD depuis le 25/07 (migration 20260725000005).

**Stockage du résultat et de la réflexion — 5 niveaux, tout dans l'existant.**
1. `agent_runs` : le passage (déjà).
2. `discoveries` enrichie (énoncé, chiffres+périmètre, réflexion rédigée, score, cycle de vie) : le carnet de recherche, mémoire longue de l'agent.
3. `project_events` + `project_memory` : la découverte entre dans la conscience temporelle que le chat LIT DÉJÀ → l'agent conversationnel peut expliquer chaque découverte sans qu'on modifie seo-agent ni le chat. **CÂBLÉ le 25/07 (niveau 1, vérifié en prod)** : chaque publication écrit le journal (`project_events` type `discovery` → section timeline du prompt), un fait (`project_memory` clé `analyse:<dkey>` → section faits, retiré à l'extinction), et la notification existante alimente la section signaux. Niveau 2 (plus tard, ÉVALS obligatoires car prompt modifié) : section dédiée « Découvertes de l'agent » dans le bloc temporel + libellé `discovery` dans EVENT_LABEL + outil `get_discoveries` pour répondre aux « pourquoi ? » avec le raisonnement complet.
4. `optimizations` : l'action dérivée (bouton Corriger, déjà).
5. Compte-rendu email + cloche : la diffusion (déjà).

---

## État au 25/07 (Phase 0, livrée)

- Régime tendances v1 : groupes de requêtes par token, 14j vs 14j, agrégation 100 % SQL (`discovery_token_trends` sur `rank_history`).
- Seuils durs : ≥ 5 requêtes, ≥ 200 impressions, variation ≥ 30 % ET ≥ 100 impressions. 3 publications max par run. Droit au silence.
- Cycle de vie (`discoveries`) : signal → confirmée (retrouvée au run suivant) → éteinte (21j d'absence). Jamais deux publications de la même chose.
- Surfaces : `optimizations` type `discovery`, cloche, compte-rendu email.
- Enrôlé par défaut sur 762 projets. Testé réel : golfiller.fr « slope » +98 %, leexi.ai « meet » −40 %.

---

## Phase 1 — Le registre d'hypothèses (le moteur devient extensible)

Objectif : passer d'une famille codée en dur à un registre déclaratif que l'on nourrit chaque semaine.

1. Registre `discovery_hypotheses` (fichier TS versionné dans le worker, pas une table au départ) : id, famille, régime (tendance / loi), fonction SQL, seuils, données minimales requises, patron de phrase.
2. Le worker itère le registre : pour chaque hypothèse, il vérifie que le site a la masse requise, il teste, il jette ou il publie. Une hypothèse = un test = un verdict.
3. Correction des tests multiples : le seuil de publication monte avec le nombre d'hypothèses testées (sinon, 100 tests fabriquent mécaniquement des fausses lois). Règle simple v1 : seuil de variation relevé de 30 % à 40 % dès que le registre dépasse 20 hypothèses, et priorité au score.
4. Score de découverte : impact (volume touché) × confiance (ampleur + réplication) × nouveauté (jamais vue / confirmée / réactivée). Stocké dans `discoveries.metrics`, sert au tri et au choix des 3 publiées.

Nouvelles familles de tendances (même infra `rank_history` + `gsc_daily_snapshots`, zéro collecte nouvelle) :
- Par répertoire d'URL (`/blog/` vs `/produit/` vs `/guide/`) : quel type de pages monte, lequel décroche.
- Par page : pages individuelles en accélération ou décrochage soutenu (streak ≥ 10 jours sur 14).
- CTR vs position : la courbe CTR/position du site devient une baseline propriétaire ; les groupes de requêtes qui sous-cliquent par rapport à leur propre courbe sont une découverte (« à position égale, ce cluster clique 2× moins »).
- Volatilité : les clusters dont les positions oscillent le plus (signal d'une SERP en mouvement = fenêtre d'opportunité).

Livrable : ~15 hypothèses actives. Effort : 1 à 2 jours.

## Phase 2 — Les lois de pages (données propriétaires élargies)

Objectif : le deuxième régime, celui du « pourquoi » : relier les caractéristiques des pages à leur performance.

1. Features par page : réutiliser le crawl technique existant (`tech_pages.facts`) et le compléter : nombre de mots, présence FAQ, vidéo, tableau, listes, schema, profondeur, liens entrants éditoriaux (`tech_links.editorial`), date de mise à jour.
2. GSC par PAGE (pas seulement par requête) : les crons ont déjà les tokens Google ; une collecte hebdo dimension page alimente `gsc_page_daily`. C'est la brique qui manque pour croiser « caractéristique × performance ».
3. Lois testées quand le site a ≥ 80 pages avec données : les pages à FAQ font-elles plus de CTR à position égale ; les contenus 900-1200 mots battent-ils les 2000+ ; les pages à ≥ 5 liens entrants montent-elles plus vite ; les pages fraîches (< 90j) surperforment-elles.
4. Stratification obligatoire par intention (Know/Do, colonne `pages.intent` quand disponible) et par répertoire : jamais une loi globale si elle disparaît dans les strates (piège corrélation/confusion).
5. Wording : toujours « sur ton site, sur cette période, les pages avec X font Y » — jamais « X cause Y ».

Livrable : régime lois actif sur les sites qui ont la masse, silencieux ailleurs. Effort : 2 à 3 jours.

## Phase 3 — La boucle de curiosité (l'agent devient chercheur)

Objectif : chaque découverte engendre ses questions filles. C'est la boucle d'auto-apprentissage, en déterministe.

1. Patron de drill-down fixe : toute découverte confirmée génère automatiquement ses hypothèses filles — par répertoire, par intention, par bande de position, par ancienneté de page, avant/après la dernière Google Update (calendrier des updates tenu à la main, il sort déjà dans les brèves).
2. File `discovery_queue` : les filles attendent le run suivant, testées comme les autres, avec les mêmes seuils. Une fille validée affine la loi mère (« vrai uniquement sur les pages Know du blog »).
3. Option LLM en générateur d'hypothèses candidates (jamais en juge) : une fois par mois, le LLM lit le contexte du site et propose 10 hypothèses au registre ; elles ne publient rien tant que la stat n'a pas tranché. Une hypothèse hallucinée meurt en silence, coût nul en confiance.
4. Publication des extinctions : la mort d'une tendance confirmée est une découverte (« l'avantage FAQ a disparu depuis la Core Update de juin »). Déjà détecté en base (statut ended), il ne manque que la publication.

Livrable : le registre grossit tout seul, les lois se raffinent. Effort : 2 jours.

## Phase 4 — Surfaces et rétention

1. **Vue « Analyses » (décision Tim 25/07 : l'utilisateur consulte les analyses visuellement).** Nouvelle vue plein écran sur le patron d'AccountPage (aucun contact avec le chat) :
   - accès depuis la Sidebar + depuis la notification de la cloche ;
   - par projet, la timeline des découvertes en cartes : énoncé + chiffres + périmètre, état visible (Signal / Tendance confirmée / Éteinte), mini-graphique 14j vs 14j (barres bleues, DA sobre existante : #4F6BFF, Geist, jamais de scroll horizontal) ;
   - la **réflexion de l'agent dépliable** sur chaque carte (le carnet de recherche : ce qui a été testé, sur quoi, ce qui a été écarté) ;
   - bouton « Corriger » (réutilise le mécanisme du panneau Recommandations) ;
   - pied de vue : historique des passages de l'agent (agent_runs) — quand il est passé, ce qu'il a trouvé, quand il repasse.
2. Ligne Discovery dans le panneau Autonomes (toggle + i18n FR/EN, pastille couleur). L'utilisateur voit l'agent, peut le couper.
3. Compte-rendu email : la découverte passe EN TÊTE quand il y en a une, avec lien vers la vue Analyses. C'est la promesse de retour : « qu'est-ce que Qadence a découvert cette semaine ? »
4. Cycle de vie visible partout : Signal / Tendance confirmée / Éteinte — même grammaire de fiabilité que les brèves.

Effort : 2 jours (la vue est le gros morceau).

## Phase 5 — Convergence (plus tard, pas avant que le reste tourne)

- Découvertes composites : quand deux familles pointent le même objet (le sujet X monte ET ses pages sous-cliquent), publier la conclusion croisée avec un score renforcé.
- Croisement entre utilisateurs (« sur les sites comparables au tien... ») : uniquement anonymisé et agrégé, cadre DPA à écrire avant la première ligne de code.

---

## Mesures de succès

- % d'utilisateurs enrôlés recevant ≥ 1 découverte par semaine (cible : > 50 %).
- Taux d'ouverture des comptes-rendus AVEC découverte vs sans.
- Clics « Corriger » sur les découvertes vs les recommandations classiques.
- Rétention J7/J30 des cohortes (référence : 6,3 % / 7,3 % mesurés le 24/07).
- Taux de survie des signaux (part des signaux qui deviennent des tendances confirmées) : s'il est < 30 %, les seuils sont trop bas, on publie du bruit.

## Garde-fous permanents

- Chiffres réels + périmètre dans chaque phrase, jamais de causalité affirmée.
- Droit au silence : une semaine sans découverte forte = pas de publication.
- Réplication temporelle obligatoire avant le statut confirmé : le temps est le jeu de test.
- Le LLM rédige ou propose, il ne valide jamais.

## Calendrier proposé

- Semaine du 28/07 : Phases 1 et 2.
- Semaine du 04/08 : Phases 3 et 4.
- Fin août : première lecture des mesures, décision Phase 5.
