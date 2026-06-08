---
type: register
title: Backlog d'ingest
aliases: [ingest-backlog, backlog, raw-non-traite, file-ingest]
tags: [meta, ingest, capture, pipeline, backlog]
created: 2026-05-16
updated: 2026-06-08
last_sweep: 2026-06-08
sources: 0
confidence: high
status: living-doc
---

# Backlog d'ingest

> Le ratio raw→wiki est sous 1 : il y a plus de matière capturée que de matière digérée, et rien ne suivait le retard. Le goulot d'un système, c'est exactement ce trou entre capture et traitement. Ce registre le rend visible et trié, pour qu'un ingest soit toujours un choix conscient, pas un oubli.
>
> Régénéré chaque semaine par le skill `ingest-backlog-sweep` (diff `raw/` vs `wiki/sources/`). Les skips documentés dans [[log]] (lignes ~385-393, ~467) sont reportés ici une bonne fois pour qu'on ne les re-litige pas à chaque sweep. Le prochain lot à ingérer est proposé en [[revue-hebdo/index|revue hebdo]].
>
> Méthode : un fichier `raw/` est "traité" quand un `wiki/sources/*.md` le couvre (directement ou via une source agrégée documentée). Sinon il est dans le backlog. Un fichier peut être explicitement `skip` (faible valeur doctrinale, déjà couvert, archive).

> **Sweep 2026-06-08** : aucun ingest entre le sweep du 2026-05-18 et aujourd'hui (cf. [[log]], dernier `batch-ingest` = 2026-05-01). Un mois de production bootcamp4/bootcamp5, terrain commercial Organikk (calls + propales réels), Fusionn, Golfiller et un batch de 13 posts LinkedIn se sont accumulés non digérés. Le backlog passe de 40 à 110 fichiers. C'est exactement le moat qui fuit, rendu visible. `modele-roadmap-premier-call.md` sort du backlog : fichier supprimé de `raw/acquisition/` (vérifié git). Backlog > 80 → on liste les 15 premiers par tier (oldest-first) et on agrège le reste par groupe.

## Priorité 1 — Données terrain propriétaires non capturées (le moat qui fuit) — 44

Ce sont les sources qui justifient l'existence de la KB : du terrain unique, non rejouable, qui alimente directement la doctrine et le discours commercial. Les laisser non traitées, c'est laisser fuir le moat. Oldest-first, 15 premiers listés.

| Fichier raw | Date | Pourquoi prioritaire |
|---|---|---|
| `raw/data/keyword-research-2026-05-02/keywords-cleaned.md` | 2026-05-02 | Recherche de mots-clés brute = data terrain. Croise [[concepts/mots-cles-actionnels]] |
| `raw/data/keyword-research-2026-05-02/keywords-classified.md` | 2026-05-02 | Idem, classifiée par intention. Matière directe pour modèle mots-clés |
| `raw/bootcamp4/session-1-mots-cles-prep.md` | 2026-05-07 | Préparation pédagogique bootcamp 4 session 1 |
| `raw/bootcamp4/sequencage-semaine-2.md` | 2026-05-12 | Séquençage semaine 2, structure pédagogique |
| `raw/bootcamp4/session-1-mots-cles-nouveautes.md` | 2026-05-12 | Nouveautés pédagogiques mots-clés |
| `raw/bootcamp4/session-1-mots-cles-transcript.md` | 2026-05-12 | Transcript brut bootcamp live = data terrain pédagogique unique. Aucun équivalent wiki |
| `raw/articles/modele-production/modele-mots-clés.md` | 2026-05-14 | Modèle de production scalable. Croise [[concepts/programmatique-pseo]] et [[concepts/pseo-data-driven-models]] |
| `raw/bootcamp4/observations-whatsapp-bootcamp.md` | 2026-05-15 | Blocages et questions du groupe = matière directe pour [[concepts/avatar-freelance-sans-systeme]] et [[concepts/cercle-vicieux-temps-structure]] |
| `raw/articles/modele-production/modele-strategie.md` | 2026-05-15 | Modèle de production stratégie scalable (cœur du livrable) |
| `raw/articles/modele-production/modele-strategie-b2b.md` | 2026-05-15 | Modèle de production stratégie B2B scalable (cœur du livrable commercial) |
| `raw/bootcamp4/session-2-redaction-prep.md` | 2026-05-15 | Préparation pédagogique bootcamp 4 session 2 rédaction |
| `raw/bootcamp4/session-3-audit-prep.md` | 2026-05-16 | Préparation pédagogique bootcamp 4 session 3 audit |
| `raw/bootcamp4/session-2-redaction-debrief.md` | 2026-05-16 | Debrief session rédaction = verbatims objections/peurs réels |
| `raw/bootcamp4/session-2-redaction-resume-participants.md` | 2026-05-16 | Retours participants = verbatims peurs/blocages terrain |
| `raw/bootcamp4/session-2-redaction-transcript.md` | 2026-05-16 | Transcript brut session 2 rédaction = data terrain pédagogique unique |

**+ 29 autres P1 (nouveaux depuis le 2026-05-18), par groupe :**

- **Bootcamp 4 — sessions 3 & 4** (2026-05-21 → 05-30, 6 fichiers) : `session-3-audit-transcript`, `session-3-audit-debrief`, `session-3-audit-resume-participants`, `sequencage-semaine-3`, `sequencage-semaine-4`, `session-4-automatisations-chat`, `session-4-call-prep` — transcripts + verbatims + séquençage = data terrain pédagogique unique, même valeur que les sessions 1-2.
- **Bootcamp 5** (2026-05-30 → 06-07, 3 fichiers) : `cadrage`, `calls-prospects`, `propal-remi` — cadrage du nouveau bootcamp + appels prospects + propale réelle.
- **Terrain commercial Organikk** (2026-06-04 → 06-07, 16 fichiers) : `pré-call/` (9 — calls + résumés + propales réels : centrale-directe, proximit/Damien, propales 1-1), `clients/fgformation-*` (5 — livrables client : mots-clés décisionnels, modèles pSEO, personas), `_MODELE-discours-commercial`, `strategie-commerciale-fusionn-2026-05-23` — le moat commercial le plus frais, alimente [[syntheses/workflow-complet-consultant-seo-ia]] et le discours d'acquisition.
- **Fusionn** : `etude utilisation fusionn.md` (2026-06-04) — data terrain produit.
- **Golfiller** : `golfiller-strat.md` (2026-06-02) — stratégie SEO client, cas terrain.
- `raw/transcripts/call-leexi-ai.md` (2026-05-21) — transcript terrain non ingéré.

## Priorité 2 — Contenu publié non bouclé (boucle preuves) — 29

Articles, newsletters et posts publiés qui n'ont ni source wiki ni [[preuves/index|fiche preuve]]. Sans eux, la boucle sortie→apprentissage ne tourne pas : on publie et on ne mesure jamais. Oldest-first, 15 premiers listés.

| Fichier raw | Date | Action |
|---|---|---|
| `raw/articles/organikk-blog/strategie-seo-serrurier-lyon.md` | 2026-04-30 | pSEO secteur×ville hors scrape 2026-04-12. Source + [[preuves/index]] |
| `raw/articles/organikk-blog/strategie-seo-agence-immobiliere-lyon.md` | 2026-04-30 | Idem Lyon. Source + preuve |
| `raw/articles/algorithme/newsletter-agent-ia-verifier-indexation-seo.md` | 2026-05-02 | Newsletter publiée non sourcée (agent IA / indexation) |
| `raw/articles/brouillons/préparation-newsletter-maillage-2026-05-06.md` | 2026-05-06 | Prep de la newsletter maillage (newsletter publiée déjà sourcée [[sources/2026-04-30-newsletter-maillage-interne]]) — vérifier diff |
| `raw/articles/brouillons/methode-lead-gen-seo.md` | 2026-05-08 | Brouillon devenu / en passe de devenir contenu publié |
| `raw/articles/algorithme/newsletter-maillage-interne-claude.md` | 2026-05-08 | Variante "claude" de la newsletter maillage, **non couverte** par [[sources/2026-04-30-newsletter-maillage-interne]] (qui ne couvre que la version non-claude) |
| `raw/articles/organikk-blog/ranker-chatgpt.md` | 2026-05-08 | Article AEO récent hors scrape. Source + preuve |
| `raw/articles/brouillons/préparation-ranker-chatgpt.md` | 2026-05-08 | Prep de l'article ranker-chatgpt |
| `raw/articles/brouillons/préparation-seo-vs-google-ads.md` | 2026-05-12 | Brouillon en passe de devenir contenu publié |
| `raw/articles/brouillons/préparation-newsletter-indexation-2026-05-11.md` | 2026-05-13 | Prep de la newsletter indexation |
| `raw/articles/organikk-blog/strategie-seo-paysagiste-paris.md` | 2026-05-15 | pSEO secteur×ville hors scrape. Source + preuve |
| `raw/articles/organikk-blog/strategie-seo-hotel-paris.md` | 2026-05-15 | Idem Paris. Source + preuve |
| `raw/articles/organikk-blog/strategie-seo-avocat-paris.md` | 2026-05-15 | Idem Paris. Source + preuve |
| `raw/articles/brouillons/preparation-semantique-2026-05-23-consultant-seo.md` | 2026-05-23 | Prep sémantique consultant SEO — brouillon en passe de devenir contenu |
| `raw/articles/brouillons/préparation-post-golfiller-strat-seo.md` | 2026-06-04 | Prep du post Golfiller (adossé à `golfiller-strat` en P1) |

**+ 14 autres P2 (nouveaux depuis le 2026-05-18), par groupe :**

- **Batch posts LinkedIn 2026-06-01** (2026-06-04, 13 fichiers, `_index-batch-2026-06-01` + 12 posts hors batch 2026-04-30) : `post-linkedin-9-skills-seo`, `-3-skills-recherche-mots-cles`, `-claude-remplace-consultant`, `-guide-complet-systeme-autonome`, `-these-80-pourcent-consultant`, `-maillage-62-liens-30min`, `-maillage-interne-skill`, `-methode-claude-semantique`, `-audit-semantique-sans-outil`, `-indexation-hebdo`, `-site-ia-100-pagespeed`, `-top1-balle-de-golf` — posts publiés non couverts par [[sources/2026-04-30-tim-posts-linkedin-batch]]. Chacun appelle une [[preuves/index|fiche preuve]].
- `raw/articles/brouillons/golfiller-conversations.md` (2026-06-04) — conversations brutes Golfiller, matière du post.

> Note boucle preuves : pour chaque article publié de P2, créer la source ET la [[preuves/index|fiche preuve]] qui le relie à l'hypothèse doctrinale qu'il teste (ex. les pSEO secteur×ville testent [[hypotheses#H-002]] et [[hypotheses#H-007]]).

## Priorité 3 — À traiter selon valeur — 37 (+ drive-accompagnement parké)

15 premiers listés, oldest-first.

| Fichier raw | Date | Note |
|---|---|---|
| `raw/articles/brouillons/linkedin-trend-research-semaine-2-avril-2026.md` | 2026-04-25 | Notes trend research. Pas de source — vérifier valeur doctrinale |
| `raw/notes/process-redaction-5-piliers.md` | 2026-05-02 | Process rédaction généralisable, à croiser avec [[concepts/workflow-redaction-8-etapes]] (vérifier doublon/évolution) |
| `raw/ia-employe/recap-jour-health-2026-05-07.md` | 2026-05-07 | `type: health-check` de l'automation recap-jour (statut OK). Méta/ops — **candidat skip**, à trancher par Tim |
| `raw/articles/brouillons/engine-densite-semantique-sans-serp.md` | 2026-05-11 | Aucune page wiki `engine-densite-semantique-sans-serp` n'existe (réf orpheline dans [[log]]/[[index]]) — brouillon non traité, vérifier si à ingérer |
| `raw/bootcamp4/ton-de-voix-worksheet.md` | 2026-05-12 | Worksheet ton de voix, croise [[concepts/anti-ai-writing]] |
| `raw/auteurs/README.md` | 2026-05-13 | Convention du dossier `raw/auteurs/` (§13). Process/navigation — **candidat skip**, à trancher par Tim |
| `raw/auteurs/greg-isenberg/2026-05-13-notes-on-agent-economy.md` | 2026-05-13 | Auteur externe. Source `source_type: article` + respect strict §13 attribution |
| `raw/bootcamp4/skill-indexation-check-cowork.md` | 2026-05-18 | Doc skill formation Cowork→terminal (cf. projet formation). Valeur doctrinale ~nulle vs skills installés |
| `raw/bootcamp4/skill-indexation-check.md` | 2026-05-18 | Idem doc skill formation |
| `raw/bootcamp4/skill-maillage-systeme.md` | 2026-05-18 | Idem doc skill formation |
| `raw/bootcamp4/skill-donnees-structurees.md` | 2026-05-19 | Idem doc skill formation |
| `raw/bootcamp4/skill-maillage-gsc-cannibalisation.md` | 2026-05-19 | Idem doc skill formation |
| `raw/bootcamp4/skill-workflow-mots-cles.md` | 2026-05-21 | Idem doc skill formation |
| `raw/fusionn/README.md` | 2026-05-21 | Process/ops produit Fusionn — **candidat skip** |
| `raw/fusionn/2026-05-21-fix-premium-front-serveur.md` | 2026-05-21 | Note dev Fusionn — **candidat skip** |

**+ 22 autres P3 (nouveaux / divers), par groupe :**

- **Docs skills/guides bootcamp 4** (2026-05-26 → 06-07, ~16 fichiers) : `SKILL-revue-presse-{bootcamp,client-template,theme-seo}`, `skill-{audit-engine-pipeline,core-web-vitals,preparation-semantique,roadmap-pseo,todo}`, `bundle-todo`, `skills-checklist-bootcamp4`, `workflow-audit-bootcamp4`, `IMPLEMENTATION-COWORK`, `install-repo-skills-cowork`, `fiche-skills-terminal`, `guide-cowork-vers-terminal`, `passer-cowork-vers-terminal` — matériel pédagogique du projet formation Cowork→terminal, faible valeur doctrinale SEO vs skills déjà installés. **Bloc candidat skip groupé**, à trancher par Tim en revue hebdo.
- `raw/etudes-seo/etude-ctr-ai-overviews-gsc.md` (2026-06-04) — **étude externe CTR AI Overviews / GSC, valeur doctrinale élevée** : à ingérer comme source `paper`/`etude`, pas P1 (pas propriétaire) mais à ne pas laisser traîner.
- `raw/todo/todo-actuelle.md` (2026-05-26) — todo de travail, valeur doctrinale ~nulle — **candidat skip**.
- `raw/data/strategies-paris/{avocat,hotel,paysagiste}/sources.md` · `raw/data/strategies-b2b/centre-formation-ia/sources.md` (4 fichiers) | Listes de sources/citations adossées aux articles pSEO P2 — à ingérer avec eux, pas seules.

| `raw/notes/drive-accompagnement/` (21 templates individuels, INDEX déjà ingéré [[sources/2026-04-30-drive-accompagnement-templates]]) | — | Voir [[contradictions#C-006]] : statut `acceptée`, ingest à la demande seulement. **Parké**, non compté dans le backlog actif |

## Skips documentés (ne pas re-litiger)

Reportés depuis [[log]]. Le sweep hebdo doit les ignorer sauf décision explicite de Tim en revue hebdo.

- `raw/notes/skill-*.md` — couverts par [[sources/2026-04-12-tim-skills-seo-proprietary]]
- `raw/notes/tim-*.md` (about-me, my-rules, my-voice, prompt-systeme, readme-bot, anti-ai-writing-style) — couverts par [[sources/2026-03-31-tim-profil-et-regles]] · [[sources/2026-03-31-tim-prompt-systeme-fusionn]] · [[sources/2026-03-31-tim-workflow-redaction]]
- `raw/articles/organikk-blog/` (14 articles du scrape 2026-04-12) — couverts par [[sources/2026-04-12-organikk-blog-scrape]] (sauf les articles récents listés en P2, hors scrape)
- `raw/notes/contenu-seo/` (DATASET-SEO, LAST-POSTs-LK 7 Mo, STRAT-SEO-2025 853 Ko, Newsletter 63 Ko, SEO-IA, best-SEO-post, newsletter-cowork-seo) — faible valeur doctrinale vs sources existantes ; SEO-IA couvert par [[sources/2026-04-11-seo-ia-tim]]
- `raw/notes/archive/` — versions antérieures des skills, non doctrinal
- `raw/articles/lost-from-old-site/` — faible valeur ajoutée
- Fichiers vides (`raw/todo/todo-2026-04-25.md` 0 octet)

## Méthode du sweep hebdo

1. Lister `raw/**/*.md` hors `journal/`, `revue-de-presse/`, `_archive/`, `archive/`
2. Pour chaque, chercher un `wiki/sources/*.md` correspondant (slug, aliases, titre, ou source agrégée documentée dans [[log]])
3. Exclure les skips documentés ci-dessus
4. Classer le reste en P1/P2/P3 selon : data terrain unique (P1) > contenu publié non bouclé (P2) > reste (P3), oldest-first dans chaque tier
5. Mettre à jour ce fichier + proposer le prochain lot en [[revue-hebdo/index]]
6. Logguer : `## [YYYY-MM-DD] backlog | sweep — N en backlog (P1:x P2:y P3:z)`

Pages liées : [[log]] · [[index]] · [[hypotheses]] · [[preuves/index]] · [[revue-hebdo/index]]
