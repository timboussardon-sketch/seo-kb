# Corpus 6 — Actions SEO : table d'attribution

Document de travail. À remplir par Tim, puis le corpus se construit mécaniquement.

## Pourquoi ce fichier existe

Les 46 actions ci-dessous sortent de trois sources réelles : `_shared/tech/classes.ts` (repo qadence), `prestation/roadmap.md`, et les journaux des 5 trackers de `prestation/clients/`.

Ce qui est **déjà groundé** pour chacune : le prérequis, la sortie attendue, le skill mobilisé, le statut éprouvé ou doctrine, et pour le groupe C la preuve terrain chiffrée.

Ce qui **manque** : effort, sévérité, rayon d'impact, réversibilité, latence de détection. Ces colonnes n'existent dans `classes.ts` que parce que Tim les a attribuées à la main, une par une. Personne d'autre ne peut les remplir sans inventer.

Décision du 2026-07-20 : **pas de colonne durée en minutes**. Le vault n'a aucune donnée de temps passé, et `classes.ts` pose déjà la règle (« pas de poids numérique inventé »). L'effort se dit en « qui doit intervenir ».

## Le vocabulaire

Repris de `classes.ts`, sauf `effort` qui est nouveau.

**effort** — qui doit intervenir pour que ce soit fait
`agent` (l'agent l'applique) · `client_cms` (le client seul, dans son back-office) · `redaction` (il faut écrire) · `dev` (il faut toucher au code ou au serveur) · `consultant` (arbitrage humain, pas délégable)

**severity** — pour la notation, jamais pour le droit d'agir
`critical` (casse l'indexabilité ou est franchement cassé) · `minor` (finition, levier secondaire)

**blastRadius** — jusqu'où ça se propage si on se trompe
`page` · `template` · `site`

**reversibility** — combien coûte le retour arrière
`commit` (on annule, c'est fini) · `index_slow` (Google doit repasser, ça prend des semaines)

**detectionLatency** — au bout de combien de temps on voit qu'on s'est trompé
`immediate` · `crawl` · `gsc`

---

## Groupe A — actions techniques · DÉJÀ ATTRIBUÉ

Rien à faire ici. Ce groupe sert de calibrage pour remplir B et C : c'est l'échelle de Tim, en vrai.

| Action | severity | blastRadius | reversibility | detectionLatency | fixer |
|---|---|---|---|---|---|
| `title_missing` | critical | page | commit | immediate | non |
| `title_duplicate` | critical | page | commit | gsc | non |
| `title_too_long` | minor | page | commit | gsc | non |
| `meta_description_missing` | minor | page | commit | immediate | non |
| `meta_description_duplicate` | minor | page | commit | gsc | non |
| `h1_missing` | minor | page | commit | immediate | **oui** |
| `h1_multiple` | minor | page | commit | immediate | non |
| `hn_disorder` | minor | page | commit | immediate | non |
| `canonical_missing` | minor | template | commit | crawl | non |
| `canonical_to_404` | critical | page | index_slow | crawl | non |
| `og_missing` | minor | page | commit | immediate | non |
| `img_alt_missing` | minor | page | commit | immediate | non |
| `redirect_chain` | minor | site | commit | immediate | non |
| `orphan_page` | minor | site | commit | crawl | non |
| `internal_link_dead` | critical | template | commit | immediate | non |

**Point à trancher avant d'aller plus loin.** Ce groupe recoupe presque entièrement `/problemes-techniques-seo`, déjà en ligne avec 13 fiches (`redirections-en-chaine`, `liens-internes-casses`, `pages-orphelines`, `canonical-incoherente`, `title-manquant-ou-duplique`, `balises-h1-mal-structurees`…). Le publier en corpus 6 reviendrait à republier l'existant. Soit on l'exclut du corpus, soit on densifie la directory existante avec ces 5 colonnes, qui n'y figurent pas aujourd'hui.

---

## Groupe B — étapes de prestation · À ATTRIBUER (19)

Source : `prestation/roadmap.md`. Statut éprouvé = déjà fait sur un vrai client.

| # | Action | Prérequis | Sortie / vérification | Statut | effort | severity | blastRadius | reversibility | detectionLatency |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Onboarding et récupération des accès | accès GSC + GA4 + data métier | `raw/organikk/clients/<slug>.md` rempli | éprouvé | | | | | |
| 2 | Pré-call et diagnostic d'entrée | URL du prospect | doc pré-call | éprouvé | | | | | |
| 3 | Interview de cadrage | scan public fait | bloc « Ce que j'ai compris » validé | doctrine | | | | | |
| 4 | Analyse GSC 90 j et 6 mois comparés | 4 CSV GSC | winners/losers, striking distance, part hors-marque | éprouvé (golfiller) | | | | | |
| 5 | Restitution GSC au client | analyse faite | Google Doc « En résumé », jargon traduit | éprouvé (leexi) | | | | | |
| 6 | Audit d'indexation | sitemap + liste d'URLs | rapport, non indexée vs non testable | doctrine | | | | | |
| 7 | Audit Core Web Vitals | échantillon sitemap | LCP/CLS/INP mesurés contre seuils | doctrine | | | | | |
| 8 | Audit et pose des données structurées | pages cibles | JSON-LD validé, zéro schéma émis « au cas où » | doctrine | | | | | |
| 9 | Recherche de mots-clés | thématique cadrée avec le client | liste groundée Suggest + GSC, zéro volume inventé | éprouvé (leexi) | | | | | |
| 10 | Clustering par SERP | liste brute | 1 cluster = 1 page | éprouvé (leexi) | | | | | |
| 11 | Isolement des mots-clés décisionnels | clusters posés | shortlist priorisée, page et format par ligne | éprouvé (leexi) | | | | | |
| 12 | Architecture en cocons mère/fille/petite-fille | mots-clés business validés | Google Doc hiérarchisé, frontière MECE tenue | éprouvé (leexi) | | | | | |
| 13 | Modèles de pages pSEO | GSC + blog existant cartographié | modèles scorés Proximité × Intention × Faisabilité | éprouvé (golfiller) | | | | | |
| 14 | Outils gratuits Product-Led | requêtes Do identifiées | outil en ligne + capture d'email | éprouvé (golfiller) | | | | | |
| 15 | Peurs et objections | verbatims client disponibles | tableau Pain / Verbatim / Preuve atomique | éprouvé (golfiller) | | | | | |
| 16 | Entités vectorielles sur une business page | requête cible + page live | carte d'entités + gap | éprouvé (golfiller) | | | | | |
| 17 | Brief Hn | vecteurs sémantiques posés | structure seule, 1 H2 = 1 vecteur | éprouvé (leexi) | | | | | |
| 18 | Rédaction | brief validé + ton de voix | article, claims sourcés | doctrine | | | | | |
| 19 | Roadmap 30/60/90 et espace client | livrables validés | espace HTML noindex + section mots-clés rejetés | éprouvé (leexi) | | | | | |

---

## Groupe C — actions correctives · À ATTRIBUER (12)

Source : journaux des trackers. Chaque ligne a été exécutée sur un vrai site, avec sa preuve chiffrée.

| # | Action | Preuve terrain | Sortie / vérification | effort | severity | blastRadius | reversibility | detectionLatency |
|---|---|---|---|---|---|---|---|---|
| 20 | Réparer une refonte sans 301 | leexi : −43 % hors-marque en 6 mois, cause racine identifiée | les anciennes URL renvoient 301 vers la plus proche | | | | | |
| 21 | Résoudre une cannibalisation multi-URL | victoriagarden : 8 URL sur « appart hotel bordeaux », 3 348 impressions/90 j, pos. 8,8 | une seule URL remonte sur la requête en GSC | | | | | |
| 22 | Réécrire un title hors requête | leexi : 2 pages, 51 810 impressions cumulées, CTR ≤ 0,23 % | le CTR de la page bouge à J+30 | | | | | |
| 23 | Densifier une page positionnée mais sous-optimisée | leexi : 10 pages en pos. 2-16 | la page couvre les vecteurs manquants | | | | | |
| 24 | Fusionner deux pages sur la même intention | doctrine cannibalisation | une page, un 301, une intention | | | | | |
| 25 | Créer un hub et remailler | victoriagarden : chantier appart hotel | la page cible reçoit ≥ 3 liens internes entrants | | | | | |
| 26 | Défendre une business page qui perd des positions | golfiller : « balle(s) de golf », gisement 26 574 impressions | analyse d'entités livrée avant toute prod pSEO | | | | | |
| 27 | Cartographier les gabarits déjà publiés | golfiller : scrape du blog | liste des directory existants, méga-page = hub | | | | | |
| 28 | Agréger les requêtes GSC par motif métier | victoriagarden : 1 648 requêtes, séminaire = 9 454 impressions / 42 clics | le motif non traité est nommé et chiffré | | | | | |
| 29 | Monter le corpus de voix écrite du client | leexi : top 20 pages, 27 639 mots scrapés | fiche TON-DE-VOIX avec diagnostic chiffré | | | | | |
| 30 | Croiser GSC et fetch on-page live | leexi : quick wins du 02/07 | l'écart entre requête et title/H1 est constaté, pas supposé | | | | | |
| 31 | Poser un pari mesuré à J+30 | leexi : ledger de la boucle | `agent_recos` écrit, `cron-reco-outcome` re-mesure | | | | | |

---

## Après remplissage

1. Le dataset se génère depuis ce fichier, une action = une entrée.
2. Branchement dans l'agent via `MAP` de `qadence/sync-skills.py`, `--dry-run` d'abord.
3. Vérification que la carte « prochaine action » cesse d'inventer son ordre de priorité.
4. Pages publiques en dernier, et seulement si l'étape 3 montre un gain.

## Ce que ce corpus répare

`seo-agent/index.ts:558` demande aujourd'hui une carte `nba` avec `impact` de 1 à 5, `time_minutes` et `confidence` de 0 à 100. Aucun barème n'existe. `index.ts:539` demande de justifier l'ordre par « impact estimé chiffré × effort », sans échelle d'effort branchée. L'agent produit ces nombres à chaque analyse.

Liens : [[Corpus-Qadence]], [[Journal]], [[prestation/roadmap]]
