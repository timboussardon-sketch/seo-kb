---
type: register
title: Backlog d'ingest
aliases: [ingest-backlog, backlog, raw-non-traite, file-ingest]
tags: [meta, ingest, capture, pipeline, backlog]
created: 2026-05-16
updated: 2026-07-13
last_sweep: 2026-07-13
sources: 0
confidence: high
status: living-doc
---

# Backlog d'ingest

> Le ratio raw→wiki est sous 1 : il y a plus de matière capturée que de matière digérée, et rien ne suivait le retard. Le goulot d'un système, c'est exactement ce trou entre capture et traitement. Ce registre le rend visible et trié, pour qu'un ingest soit toujours un choix conscient, pas un oubli.
>
> Régénéré chaque semaine par le skill `ingest-backlog-sweep` (diff `raw/` vs `wiki/sources/`). Les skips documentés dans [[log]] (lignes ~385-393, ~467) sont reportés ici une bonne fois pour qu'on ne les re-litige pas à chaque sweep. Le prochain lot à ingérer est proposé en [[revue-hebdo/index|revue hebdo]].
>
> **Lot W30 voté le 2026-07-17** ([[revue-hebdo/2026-W29]] point 3) : **Victoria Garden** (10 fichiers P1, dont le sprint corpus) — seul client à chantier vivant, GSC qui coule, diagnostics chiffrés, et sujet du conditionnel [[hypotheses#H-009]]. Trois arbitrages joints : Leexi **skippé** (date de mort atteinte, voir Skips), skip `golfiller-strat` **dégelé** mais rattaché au J+90 du 2026-09-01, refresh de [[sources/2026-06-19-playbook-reddit-seo-geo]] **attaché au J+30 de H-007** (2026-08-06) au lieu d'être revoté chaque semaine. Règle posée après cinq cycles : le rituel ne fait pas exécuter les ingests, le travail les fait exécuter — un ingest se rattache désormais à une échéance datée ou à un chantier vivant, jamais à un vote hebdomadaire.
>
> Méthode : un fichier `raw/` est "traité" quand un `wiki/sources/*.md` le couvre (directement ou via une source agrégée documentée). Sinon il est dans le backlog. Un fichier peut être explicitement `skip` (faible valeur doctrinale, déjà couvert, archive).

> **Sweep 2026-07-13** : 373 fichiers `raw/` scannés (+24 vs sweep précédent), backlog à **240** (P1:123 P2:35 P3:82). **Sorties (4)** : le scrape publications du 2026-07-05/07-11 a fiché individuellement 3 articles P2 — `ranker-chatgpt` → [[sources/2026-05-08-organikk-ranker-chatgpt-2026]], `strategie-seo-serrurier-lyon` → [[sources/2026-01-12-organikk-seo-serrurier-lyon]], `strategie-seo-agence-immobiliere-lyon` → [[sources/2026-01-08-organikk-seo-agence-immobiliere-lyon]] ; le transcript `call-14-vincent-upscale` a été ingéré à chaud le 2026-07-09 ([[sources/2026-07-09-call-14-vincent-upscale]], qui couvre aussi `upscale-call-vincent` et `upscale-preaudit`) sans jamais entrer au backlog. `etude-ctr-ai-overviews-gsc` est sorti par skip acté [[revue-hebdo/2026-W28]]. **Entrées (21 P1 + 9 P3 de régularisation)** : sprint corpus **Victoria Garden** (7 fichiers du 07-10/11 : `corpus-modele/` ×3, `pages-motif/` ×3, `faits-verifies`) — première transposition client du pattern corpus Organikk ; **pré-calls frais** (9 : horizoncrm ×3, simplimo ×3, upscale-email, yalp-video, `_MODELE-pre-email-avant-call`) ; **sprint corpus Golfiller** (3 : `Corpus-Golfiller` + 2 modèles — un sprint Golfiller réel existe, condition de dégel du skip `golfiller-strat` à trancher en revue hebdo) ; **Leexi** +1 (`mots-cles-prioritaires-2026-07-09`) ; **X playbook** +1 (`Modele-tweet-SEO`, 5e fichier du dossier dont les 4 autres sont sortis via [[sources/2026-06-19-playbook-x-seo-geo]]). En P3, régularisation de 9 fichiers anciens jamais comptés par les sweeps précédents (scheduled-skills ×3, README fusionn/qadence, scoring opendecoder, cas-clients ×2, note client golfiller). Note comptage : le P1 affiché 98 au sweep précédent sommait en réalité à 102 dans son propre listing — recompté ici depuis zéro. Le lot W29 voté en [[revue-hebdo/2026-W28]] (refresh playbook Reddit en tête + Leexi avec date de mort) est repris tel quel en prochain lot. **Nouvelle matière non digérée (9 fichiers)** : dossier client frais **Victoria Garden** (appart-hôtel Bordeaux, 3 fichiers P1 : `analyse-semantique-appart-hotel-bordeaux`, `brief-hub-appart-hotel-bordeaux`, `journal-appart-hotel-bordeaux`) — client actif produit en une session complète (analyse sémantique + brief hub + journal), aucun `wiki/sources/`. Le **pré-call Origin 137** (`organikk/pré-call/origin137.md`, o137.ai — moat commercial frais, P1). Le **dossier `raw/reddit-playbook/`** (3 fichiers) : `Playbook-Reddit-SEO-GEO.md` (`source_type: doctrine`, 36 sources — doctrine propriétaire parasite-SEO/GEO, référence canonique du skill `redaction-guide` validée [[log]] 2026-07-03) et `Routine-quotidienne.md` (`source_type: doctrine`, routine opérationnelle) → P1 ; `Journal.md` (`source_type: test-terrain`, tracker Qadence live) → P3. Enfin **2 transcripts vidéo externes growth** (`transcripts/video-growth-saas-ia-distribution`, `-influencer-flywheel-jedi` — playbooks distribution/influence, tagués qadence, valeur non-SEO-core) → P3. **Reddit est du terrain vivant** : le skill `reddit-cockpit` tourne en quotidien, le test Qadence.io est en cours — le playbook est le candidat d'ingest le plus tiré par du travail réel. Le lot W27 voté en W26 (`etude-ctr-ai-overviews-gsc` + dossier Leexi, tirés par la newsletter « mots-clés non mangés ») n'est **toujours pas exécuté** — repris en prochain lot ci-dessous. Le gros bloc reste **FG-Formation** (40 fichiers, [[sources/2026-04-30-fg-formation-pseo-cas-client]] ne couvre que les 2 notes `raw/notes/fg-formation/`). Backlog > 80 → on liste les 15 premiers par tier (oldest-first) et on agrège le reste par groupe.

## Priorité 1 — Données terrain propriétaires non capturées (le moat qui fuit) — 123

Ce sont les sources qui justifient l'existence de la KB : du terrain unique, non rejouable, qui alimente directement la doctrine et le discours commercial. Les laisser non traitées, c'est laisser fuir le moat. Oldest-first, 15 premiers listés.

| Fichier raw | Date | Pourquoi prioritaire |
|---|---|---|
| `raw/bootcamp4/sequencage-semaine-2.md` | 2026-05-12 | Séquençage semaine 2, structure pédagogique |
| `raw/bootcamp4/session-1-mots-cles-nouveautes.md` | 2026-05-12 | Nouveautés pédagogiques mots-clés |
| `raw/articles/modele-production/modele-strategie-b2b.md` | 2026-05-15 | Modèle de production stratégie B2B scalable (cœur du livrable commercial) |
| `raw/articles/modele-production/modele-strategie.md` | 2026-05-15 | Modèle de production stratégie scalable (cœur du livrable) |
| `raw/bootcamp4/observations-whatsapp-bootcamp.md` | 2026-05-15 | Blocages et questions du groupe = matière directe pour [[concepts/avatar-freelance-sans-systeme]] et [[concepts/cercle-vicieux-temps-structure]] |
| `raw/bootcamp4/session-2-redaction-debrief.md` | 2026-05-16 | Debrief session rédaction = verbatims objections/peurs réels |
| `raw/bootcamp4/session-2-redaction-transcript.md` | 2026-05-16 | Transcript brut session 2 rédaction = data terrain pédagogique unique |
| `raw/bootcamp4/session-3-audit-prep.md` | 2026-05-21 | Préparation pédagogique bootcamp 4 session 3 audit |
| `raw/bootcamp4/session-3-audit-transcript.md` | 2026-05-21 | Transcript brut session 3 audit = data terrain pédagogique unique |
| `raw/bootcamp4/session-2-redaction-resume-participants.md` | 2026-05-22 | Retours participants = verbatims peurs/blocages terrain |
| `raw/bootcamp4/session-3-audit-debrief.md` | 2026-05-22 | Debrief session audit = verbatims objections terrain |
| `raw/bootcamp4/session-3-audit-resume-participants.md` | 2026-05-22 | Retours participants session audit = verbatims |
| `raw/bootcamp4/sequencage-semaine-3.md` | 2026-05-26 | Séquençage semaine 3, structure pédagogique |
| `raw/articles/modele-production/modele-mots-clés.md` | 2026-05-27 | Modèle de production scalable. Croise [[concepts/programmatique-pseo]] et [[concepts/pseo-data-driven-models]] |
| `raw/bootcamp4/sequencage-semaine-4.md` | 2026-05-28 | Séquençage semaine 4, structure pédagogique |

**+ 108 autres P1, par groupe :**

- **Reddit — playbook publié, refresh voté** (2 entrées) : `reddit-playbook/Playbook-Reddit-SEO-GEO.md` — le playbook est désormais **publié** (guide organikk.co du 2026-07-07, fiché [[sources/2026-07-07-organikk-guide-reddit-seo-geo]]) mais la fiche doctrine [[sources/2026-06-19-playbook-reddit-seo-geo]] a deux versions de retard : **refresh voté tête de lot W29** ([[revue-hebdo/2026-W28]] point 3), crée au passage `concepts/parasite-seo` + `entities/reddit`. + `Routine-quotidienne.md` (routine opérationnelle quotidienne, toujours sans source).
- **X playbook — modèle tweet** (2026-07-06, 1 fichier) : `x-playbook/Modele-tweet-SEO.md` — modèle opérationnel de tweet SEO, 5e fichier du dossier ; les 4 autres sont sortis du backlog au sweep du 2026-06-22 via [[sources/2026-06-19-playbook-x-seo-geo]].
- **Victoria Garden — dossier client + sprint corpus** (2026-07-01 → 07-11, 10 fichiers) : livrable initial (`victoriagarden-analyse-semantique-appart-hotel-bordeaux-2026-07-01`, `-brief-hub-`, `-journal-`) + **sprint corpus frais** (`corpus-modele/` : `000-corpus-modele`, `5-modeles-corpus-victoriagarden`, `stack-corpus-victoriagarden` ; `pages-motif/` : `page-animaux-bordeaux`, `page-hospitalisation-bordeaux`, `page-mutation-bordeaux` ; `victoriagarden-faits-verifies-2026-07-10`). Première transposition client du pattern corpus Organikk (itérations pSEO du [[log]] 2026-07-07). Les exports GSC de juin (`-audit-gsc-`, `-quick-wins-2026-06-11`) sont couverts par [[sources/2026-06-11-victoriagarden-gsc-export]]. Aucun `wiki/sources/` pour le reste.
- **Origin 137 — pré-call** (2026-07-04, 1 fichier) : `organikk/pré-call/origin137.md` (o137.ai, `type: pre-call` — pré-audit prospection LinkedIn, moat commercial frais).
- **Leexi — dossier client complet** (2026-05-21 → 07-09, 13 fichiers) : `clients/leexi/leexi.md` (note maître client), `leexi-call-2026-05-21`, `leexi-call-2026-06-24` + `-notes-meet` (3 calls de découverte SaaS notetaker RGPD), `livrable-mots-cles-business`, `arborescence-cocons` (architecture de cocons), `keywords/` (7 : `recherche-2026-06-16-rgpd`, `clusters-2026-06-26`, `cocon-1-notetaker-reunion`, `cocon-2-prise-de-notes-rgpd`, `cocon-3-middle-funnel-metier`, `liste-mots-cles-complete`, `mots-cles-prioritaires-2026-07-09` neuf). Calls réels + livrables mots-clés produits, mobilisés dans [[queries/2026-06-24-mots-cles-que-les-ia-ne-mangent-pas]] mais aucun ingéré en `wiki/sources/`. **Sous-lot `notes-meet` + `recherche-rgpd` reconduit en W29 avec date de mort** ([[revue-hebdo/2026-W28]] point 3) : ingest cette semaine ou skip documenté.
- **Golfiller — sprint corpus** (2026-07-06 → 07-09, 3 fichiers) : `golfiller/Corpus-Golfiller.md` + `modeles/corpus-2-facette-grade.md` + `modeles/corpus-5-distances-par-profil.md` — modèles de production corpus pSEO. **Un sprint Golfiller réel existe** : c'est exactement la condition de dégel posée par le skip `golfiller-strat` ([[revue-hebdo/2026-W26]]) — à trancher en revue hebdo, sans reclasser le skip ici.
- **Alexia — dossier client** (2026-06-10 → 06-24, 3 fichiers) : `clients/alexia/2026-06-10-call-cadrage-adrien`, `-resume-call-envoye`, `2026-06-24-call-1-resume` — calls de cadrage archivés en raw (actions `client` au [[log]]) mais sans `wiki/sources/`.
- **FG-Formation — dossier client complet** (2026-06-13, 40 fichiers) : `clients/fgformation/calls/` (32 — audits blancs ×5, coachings ×6, R1 ×3, RDV ×17, `SYNTHESE-appels-anonymisee`) + 8 livrables (`fgformation` maître, `-clusters`, `-gsc-quickwins`, `-modeles-pseo`, `-mots-cles`, `-mots-cles-decisionnels`, `-mots-cles-recherche-exhaustive`, `-personas-problematiques`). **Le plus gros bloc terrain frais de tout le backlog** : 32 transcripts d'appels réels = matière brute pour [[concepts/avatar-freelance-sans-systeme]] et le discours commercial, + livrables pSEO produits. Aucun équivalent wiki.
- **Terrain commercial Organikk pré-call** (2026-06-08 → 07-10, 21 fichiers) : `centrale-directe` (×3), `proximit` (×5 : call-damien, propale, propale-1-1, resume-call-client, fiche), `pangaea-sports` (×2), `ears-360`, `_MODELE-pre-call` + **9 neufs** : `horizoncrm` (×3 : fiche, email, propale), `simplimo` (×3 : fiche, email, propale), `upscale-email` (le call et le pré-audit Upscale sont couverts par [[sources/2026-07-09-call-14-vincent-upscale]]), `yalp-video`, `_MODELE-pre-email-avant-call` — calls + résumés + propales réels, le moat commercial le plus frais, alimente [[syntheses/workflow-complet-consultant-seo-ia]].
- **Bootcamp 4 — fin sessions 1, 2 & 4** (5 fichiers) : `session-1-mots-cles-prep`, `session-1-mots-cles-transcript`, `session-2-redaction-prep`, `session-4-automatisations-chat`, `session-4-call-prep` — transcripts + prep restants, même valeur que les sessions déjà listées.
- **Acquisition / pré-call frais** (2026-06-16 → 06-20, 2 fichiers) : `organikk/pré-call/hellocse.md` (call découverte CSE/SaaS fait, propale + chiffrage à envoyer — moat commercial frais), `youtube/preparation-yt.md` (masterclass SEO-Claude + plan de chaîne YouTube, lead gen Organikk/Fusionn/Qadence). _(La recherche mots-clés RGPD Leexi est désormais comptée dans le dossier Leexi ci-dessus.)_
- **Bootcamp 5** (2026-05-30 → 06-08, 3 fichiers) : `cadrage`, `calls-prospects`, `propal-remi` — cadrage du nouveau bootcamp + appels prospects + propale réelle.
- **Discours / stratégie commerciale** (2 fichiers) : `_MODELE-discours-commercial` (2026-06-08), `strategie-commerciale-fusionn-2026-05-23` — modèle de pitch + stratégie produit Fusionn.
- **Fusionn** : `etude utilisation fusionn.md` (2026-06-08) — data terrain produit.
- **Transcript terrain** : `raw/transcripts/video-erreur-ia-137-pages.md` (2026-06-09) — transcript vidéo erreur IA / indexation 137 pages.

## Priorité 2 — Contenu publié non bouclé (boucle preuves) — 35

Articles, newsletters et posts publiés qui n'ont ni source wiki ni [[preuves/index|fiche preuve]]. Sans eux, la boucle sortie→apprentissage ne tourne pas : on publie et on ne mesure jamais. Sorties de ce sweep : `ranker-chatgpt`, `strategie-seo-serrurier-lyon` et `strategie-seo-agence-immobiliere-lyon`, fichés individuellement par le scrape publications (les fiches preuves restent à ouvrir pour chacun). Oldest-first, 12 premiers listés.

| Fichier raw | Date | Action |
|---|---|---|
| `raw/articles/brouillons/préparation-newsletter-indexation-2026-05-11.md` | 2026-05-13 | Prep de la newsletter indexation |
| `raw/articles/organikk-blog/strategie-seo-avocat-paris.md` | 2026-05-15 | pSEO secteur×ville hors scrape. Source + preuve |
| `raw/articles/organikk-blog/strategie-seo-hotel-paris.md` | 2026-05-15 | Idem Paris. Source + preuve |
| `raw/articles/organikk-blog/strategie-seo-paysagiste-paris.md` | 2026-05-15 | Idem Paris. Source + preuve |
| `raw/articles/algorithme/newsletter-agent-ia-verifier-indexation-seo.md` | 2026-05-16 | Newsletter publiée non sourcée (agent IA / indexation) |
| `raw/articles/algorithme/newsletter-maillage-interne-claude.md` | 2026-05-22 | Variante "claude" de la newsletter maillage, **non couverte** par [[sources/2026-04-30-newsletter-maillage-interne]] |
| `raw/articles/brouillons/preparation-semantique-2026-05-23-consultant-seo.md` | 2026-05-23 | Prep sémantique consultant SEO — brouillon en passe de devenir contenu |
| `raw/articles/brouillons/préparation-newsletter-maillage-2026-05-06.md` | 2026-05-26 | Prep de la newsletter maillage (publiée déjà sourcée [[sources/2026-04-30-newsletter-maillage-interne]]) — vérifier diff |
| `raw/articles/posts-linkedin/post-linkedin-audit-sans-semrush.md` | 2026-05-26 | Post publié hors batch — source + [[preuves/index]] |
| `raw/articles/posts-linkedin/post-linkedin-episode-2-site-claude.md` | 2026-05-26 | Idem post publié hors batch |
| `raw/articles/posts-linkedin/post-linkedin-grok-seo.md` | 2026-05-26 | Idem post publié hors batch |
| `raw/articles/posts-linkedin/post-linkedin-linkedin-source-ia.md` | 2026-05-26 | Idem post publié hors batch |

**+ 23 autres P2, par groupe :**

- **Posts LinkedIn** (17 fichiers) : batch 2026-06-01 (`_index-batch-2026-06-01` + `post-linkedin-9-skills-seo`, `-3-skills-recherche-mots-cles`, `-claude-remplace-consultant`, `-guide-complet-systeme-autonome`, `-these-80-pourcent-consultant`, `-maillage-62-liens-30min`, `-maillage-interne-skill`, `-methode-claude-semantique`, `-audit-semantique-sans-outil`, `-indexation-hebdo`, `-site-ia-100-pagespeed`, `-top1-balle-de-golf`) + hors-batch (`-mots-cles-llm`, `-role-seo-claude`, `-seo-kb-obsidian`, `-surprise-score-workflow`) — posts publiés non couverts par [[sources/2026-04-30-tim-posts-linkedin-batch]]. Chacun appelle une [[preuves/index|fiche preuve]].
- **Brouillons / prep** (6 fichiers) : `engine-densite-semantique-sans-serp`, `golfiller-conversations`, `methode-lead-gen-seo`, `préparation-post-golfiller-strat-seo`, `préparation-ranker-chatgpt`, `préparation-seo-vs-google-ads` — brouillons en passe de devenir contenu publié.

> Note boucle preuves : pour chaque article publié de P2, créer la source ET la [[preuves/index|fiche preuve]] qui le relie à l'hypothèse doctrinale qu'il teste (ex. les pSEO secteur×ville testent [[hypotheses#H-002]] et [[hypotheses#H-007]]).

## Priorité 3 — À traiter selon valeur — 82 (+ drive-accompagnement parké)

15 premiers listés, oldest-first.

| Fichier raw | Date | Note |
|---|---|---|
| `raw/auteurs/greg-isenberg/2026-05-13-notes-on-agent-economy.md` | 2026-05-13 | Auteur externe. Source `source_type: article` + respect strict §13 attribution |
| `raw/data/strategies-b2b/centre-formation-ia/sources.md` | 2026-05-15 | Liste de sources adossée à l'article pSEO P2 — à ingérer avec lui, pas seule |
| `raw/data/strategies-paris/avocat/sources.md` | 2026-05-15 | Idem, adossé à `strategie-seo-avocat-paris` (P2) |
| `raw/data/strategies-paris/hotel/sources.md` | 2026-05-15 | Idem, adossé à `strategie-seo-hotel-paris` (P2) |
| `raw/data/strategies-paris/paysagiste/sources.md` | 2026-05-15 | Idem, adossé à `strategie-seo-paysagiste-paris` (P2) |
| `raw/ia-employe/recap-jour-health-2026-05-07.md` | 2026-05-16 | `type: health-check` de l'automation recap-jour (statut OK). Méta/ops — **candidat skip**, à trancher par Tim |
| `raw/bootcamp4/skill-indexation-check-cowork.md` | 2026-05-18 | Doc skill formation Cowork→terminal. Valeur doctrinale ~nulle vs skills installés |
| `raw/bootcamp4/skill-indexation-check.md` | 2026-05-18 | Idem doc skill formation |
| `raw/bootcamp4/skill-maillage-systeme.md` | 2026-05-18 | Idem doc skill formation |
| `raw/bootcamp4/skill-donnees-structurees.md` | 2026-05-19 | Idem doc skill formation |
| `raw/bootcamp4/skill-maillage-gsc-cannibalisation.md` | 2026-05-19 | Idem doc skill formation |
| `raw/bootcamp4/skill-workflow-mots-cles.md` | 2026-05-21 | Idem doc skill formation |
| `raw/fusionn/2026-05-21-fix-premium-front-serveur.md` | 2026-05-21 | Note dev Fusionn — **candidat skip** |
| `raw/articles/brouillons/linkedin-trend-research-semaine-2-avril-2026.md` | 2026-05-26 | Notes trend research. Pas de source — vérifier valeur doctrinale |
| `raw/bootcamp4/SKILL-revue-presse-bootcamp.md` | 2026-05-26 | Doc skill formation revue de presse — bloc candidat skip |

**+ 67 autres P3, par groupe :**

- **Régularisation sweep 2026-07-13** (9 fichiers anciens jamais comptés par les sweeps précédents, à vérifier) : `notes/scheduled-skills/` (×3 : `SKILL-rappel-calls-1h`, `SKILL-recap-hebdo-vendredi`, `SKILL-scan-arxiv-seo-ia` — docs skills planifiés, même nature que le bloc candidat skip bootcamp4), `fusionn/README.md` (**candidat skip**, doc ops), `agents/qadence-seo-agent/README.md` (doc agent Qadence — à vérifier), `scoring/opendecoder-seo-scoring-system.md` (système de scoring propriétaire — à vérifier, possible P1 doctrine), `cas-clients/victoria-garden.md` + `notes/cas-clients-resultats.md` (notes cas clients/résultats — à vérifier, possible doublon avec le dossier VG et possible P1 data terrain), `organikk/clients/golfiller.md` (note client Golfiller — à rattacher au sprint corpus P1 si dégel).

- **Transcripts vidéo growth externes** (2026-07-04, 2 fichiers) : `transcripts/video-growth-saas-ia-distribution` (playbook distribution SaaS IA), `transcripts/video-influencer-flywheel-jedi` (playbook influenceurs B2B). Matière growth/distribution tagguée qadence, hors SEO-core — valeur pour la stratégie produit, pas la doctrine SEO. À ingérer si un fil Qadence/Fusionn le tire.
- `raw/reddit-playbook/Journal.md` (2026-07-02) — `source_type: test-terrain`, tracker du test Qadence.io, document vivant (`status: draft`). À ne pas ingérer seul : il boucle avec le playbook Reddit (P1) une fois la data terrain constituée → **fiche preuve** plutôt que source.

- **Matériel pédagogique bootcamp 4** (50 fichiers, **bloc candidat skip groupé**) : `bootcamp4/exercices/` (26 — exercices skills + workflows), `bootcamp4/skill-*` (11 docs skill formation), `bootcamp4/` docs-guides (13 : `SKILL-revue-presse-{client-template,theme-seo}`, `IMPLEMENTATION-COWORK`, `install-repo-skills-cowork`, `fiche-skills-terminal`, `guide-cowork-vers-terminal`, `passer-cowork-vers-terminal`, `plan-exercices-workflows-skills`, `bundle-todo`, `skills-checklist-bootcamp4`, `workflow-audit-bootcamp4`, `ton-de-voix-worksheet`). Matériel du projet formation Cowork→terminal, faible valeur doctrinale SEO vs skills déjà installés. À trancher par Tim en revue hebdo.
- **Références concurrent espressio-ai** (2026-06-11, 5 fichiers) : `blog`, `home`, `index`, `offre`, `plan-adaptation-organikk` — scrape concurrent + plan d'adaptation. À ingérer comme `entities/` concurrent si valeur retenue.
- **Notes / guides** (4 fichiers) : `notes/fable-5-agentique-seo` (2026-06-11 — architecture IA citée, valeur doctrinale), `notes/guide-construire-agent-seo-claude` (2026-06-11), `notes/guide-skills-seo-0-a-1` (2026-06-10), `notes/process-redaction-5-piliers` (2026-05-26 — à croiser avec [[concepts/workflow-redaction-8-etapes]], vérifier doublon).
- `raw/golfiller/pages/_template-golfiller-NOTE.md` (2026-06-10) — template/design de référence Golfiller — **candidat skip**.
- `raw/todo/todo-actuelle.md` (2026-05-26) — todo de travail, valeur doctrinale ~nulle — **candidat skip**.
- `raw/organikk/mots-cles-a-traiter.md` (2026-06-16) — liste opérationnelle de mots-clés à traiter (client-note Organikk), document de travail vivant — **candidat skip** ou à absorber dans un workflow KW réel, à trancher par Tim.

| `raw/notes/drive-accompagnement/` (22 templates individuels, INDEX déjà ingéré [[sources/2026-04-30-drive-accompagnement-templates]]) | — | Voir [[contradictions#C-006]] : statut `acceptée`, ingest à la demande seulement. **Parké**, non compté dans le backlog actif |

## Skips documentés (ne pas re-litiger)

Reportés depuis [[log]]. Le sweep hebdo doit les ignorer sauf décision explicite de Tim en revue hebdo.

- `raw/notes/skill-*.md` — couverts par [[sources/2026-04-12-tim-skills-seo-proprietary]]
- `raw/notes/tim-*.md` (about-me, my-rules, my-voice, prompt-systeme, readme-bot, anti-ai-writing-style) — couverts par [[sources/2026-03-31-tim-profil-et-regles]] · [[sources/2026-03-31-tim-prompt-systeme-fusionn]] · [[sources/2026-03-31-tim-workflow-redaction]]
- `raw/articles/organikk-blog/` (14 articles du scrape 2026-04-12) — couverts par [[sources/2026-04-12-organikk-blog-scrape]] (sauf les articles récents listés en P2, hors scrape)
- `raw/notes/contenu-seo/` (DATASET-SEO, LAST-POSTs-LK 7 Mo, STRAT-SEO-2025 853 Ko, Newsletter 63 Ko, SEO-IA, best-SEO-post, newsletter-cowork-seo) — faible valeur doctrinale vs sources existantes ; SEO-IA couvert par [[sources/2026-04-11-seo-ia-tim]]
- `raw/notes/archive/` — versions antérieures des skills, non doctrinal
- `raw/articles/lost-from-old-site/` — faible valeur ajoutée
- Fichiers vides (`raw/todo/todo-2026-04-25.md` 0 octet)
- `raw/data/keyword-research-2026-05-02/` (binôme `keywords-cleaned.md` + `keywords-classified.md`) — skip acté [[revue-hebdo/2026-W24]] en application du conditionnel [[revue-hebdo/2026-W22]] point 3 : 4 reconductions (W20→W24) sans ingest, la doctrine de sélection des mots-clés s'est consolidée entre-temps via Fusionn et le terrain client. Ce binôme ne passe pas par le rituel ; ré-ingest seulement si un travail réel le réclame.
- ~~`raw/golfiller/golfiller-strat.md`~~ — **skip dégelé le 2026-07-17** ([[revue-hebdo/2026-W29]] point 3). La condition posée en [[revue-hebdo/2026-W26]] était « ré-ingest seulement attaché à un sprint Golfiller réel » : un sprint réel a eu lieu du 2026-07-06 au 2026-07-09 (3 fichiers corpus produits). Condition factuellement remplie, le skip tombe. Le fichier repasse en P1 comme un bloc avec les 3 fichiers du sprint, mais **le sprint est clos et rien ne le tire aujourd'hui** : le bloc s'attache à l'échéance J+90 Golfiller du 2026-09-01 (engagement daté au ledger), pas au lot de la semaine. Dégelé n'est pas prioritaire.
- `raw/organikk/clients/leexi/leexi-call-2026-06-24-notes-meet.md` + `raw/organikk/clients/leexi/keywords/recherche-2026-06-16-rgpd.md` — skip acté [[revue-hebdo/2026-W29]] en application de la date de mort posée en [[revue-hebdo/2026-W28]] point 3 : voté W27 (tiré par la newsletter « mots-clés non mangés »), reconduit W28 et W29, jamais exécuté. Aucune session Leexi n'a repris, le fil éditorial qui les tirait est gelé. Même doctrine que le binôme kw-research, `golfiller-strat` et `etude-ctr` : sort du circuit rituel. Ré-ingest seulement attaché à une reprise client Leexi réelle. Le reste du dossier Leexi (11 fichiers) reste en P1, non skippé.
- `raw/etudes-seo/etude-ctr-ai-overviews-gsc.md` — skip acté [[revue-hebdo/2026-W28]] en application de la date de mort posée en [[revue-hebdo/2026-W27]] point 3 : voté W24 (lot W25), reconduit W25, W26 et W27, jamais exécuté. Cet ingest n'existait que pour donner son chiffre manquant à l'édition « mots-clés non mangés » ([[queries/2026-06-24-mots-cles-que-les-ia-ne-mangent-pas]]) ; l'édition n'est pas sortie en W28 et le fil éditorial est gelé. Ré-ingest seulement si le fil se dégèle et qu'une édition en cours de rédaction le réclame.

## Méthode du sweep hebdo

1. Lister `raw/**/*.md` hors `journal/`, `revue-de-presse/`, `_archive/`, `archive/`
2. Pour chaque, chercher un `wiki/sources/*.md` correspondant (slug, aliases, titre, ou source agrégée documentée dans [[log]])
3. Exclure les skips documentés ci-dessus
4. Classer le reste en P1/P2/P3 selon : data terrain unique (P1) > contenu publié non bouclé (P2) > reste (P3), oldest-first dans chaque tier
5. Mettre à jour ce fichier + proposer le prochain lot en [[revue-hebdo/index]]
6. Logguer : `## [YYYY-MM-DD] backlog | sweep — N en backlog (P1:x P2:y P3:z)`

Pages liées : [[log]] · [[index]] · [[hypotheses]] · [[preuves/index]] · [[revue-hebdo/index]]
