---
type: register
title: Backlog d'ingest
aliases: [ingest-backlog, backlog, raw-non-traite, file-ingest]
tags: [meta, ingest, capture, pipeline, backlog]
created: 2026-05-16
updated: 2026-05-16
sources: 0
confidence: high
status: living-doc
---

# Backlog d'ingest

> Le ratio raw→wiki est sous 1 : il y a plus de matière capturée que de matière digérée, et rien ne suivait le retard. Le goulot d'un second cerveau, c'est exactement ce trou entre capture et traitement. Ce registre le rend visible et trié, pour qu'un ingest soit toujours un choix conscient, pas un oubli.
>
> Régénéré chaque semaine par le skill `ingest-backlog-sweep` (diff `raw/` vs `wiki/sources/`). Les skips documentés dans [[log]] (lignes ~385-393, ~467) sont reportés ici une bonne fois pour qu'on ne les re-litige pas à chaque sweep. Le prochain lot à ingérer est proposé en [[revue-hebdo/index|revue hebdo]].
>
> Méthode : un fichier `raw/` est "traité" quand un `wiki/sources/*.md` le couvre (directement ou via une source agrégée documentée). Sinon il est dans le backlog. Un fichier peut être explicitement `skip` (faible valeur doctrinale, déjà couvert, archive).

## Priorité 1 — Données terrain propriétaires non capturées (le moat qui fuit)

Ce sont les sources qui justifient l'existence de la KB : du terrain unique, non rejouable, qui alimente directement la doctrine et le discours commercial. Les laisser non traitées, c'est laisser fuir le moat.

| Fichier raw | Pourquoi prioritaire |
|---|---|
| `raw/bootcamp4/session-1-mots-cles-transcript.md` (93 Ko) | Transcript brut bootcamp live = data terrain pédagogique unique. Aucun équivalent wiki |
| `raw/bootcamp4/session-2-redaction-transcript.md` (48 Ko) | Idem session 2 rédaction |
| `raw/bootcamp4/session-2-redaction-debrief.md` · `session-2-redaction-resume-participants.md` | Debrief + retours participants = verbatims objections/peurs réels |
| `raw/bootcamp4/observations-whatsapp-bootcamp.md` | Blocages et questions du groupe = matière directe pour [[concepts/avatar-freelance-sans-systeme]] et [[concepts/cercle-vicieux-temps-structure]] |
| `raw/bootcamp4/session-1-mots-cles-prep.md` · `session-1-mots-cles-nouveautes.md` · `sequencage-semaine-2.md` · `session-3-audit-prep.md` | Préparations et nouveautés pédagogiques bootcamp 4 |
| `raw/articles/modele-production/modele-strategie.md` · `modele-strategie-b2b.md` · `modele-mots-cles.md` | Modèles de production scalables (le coeur du livrable). Croise [[concepts/programmatique-pseo]] et [[concepts/pseo-data-driven-models]] |
| `raw/acquisition/modele-roadmap-premier-call.md` | Livrable premier call = asset commercial structurant, lié à [[syntheses/workflow-complet-consultant-seo-ia]] |

## Priorité 2 — Contenu publié non bouclé (boucle preuves)

Articles et newsletters publiés qui n'ont ni source wiki ni [[preuves/index|fiche preuve]]. Sans eux, la boucle sortie→apprentissage ne tourne pas : on publie et on ne mesure jamais.

| Fichier raw | Action |
|---|---|
| `raw/articles/organikk-blog/strategie-seo-avocat-paris.md` · `strategie-seo-hotel-paris.md` · `strategie-seo-paysagiste-paris.md` | Articles pSEO secteur×ville récents, hors scrape 2026-04-12. Source + [[preuves/index]] |
| `raw/articles/organikk-blog/strategie-seo-serrurier-lyon.md` · `strategie-seo-agence-immobiliere-lyon.md` | Idem Lyon |
| `raw/articles/organikk-blog/ranker-chatgpt.md` | Article AEO récent hors scrape. Source + preuve |
| `raw/articles/algorithme/newsletter-agent-ia-verifier-indexation-seo.md` · `newsletter-maillage-interne.md` · `newsletter-maillage-interne-claude.md` | Newsletters publiées non sourcées |
| `raw/articles/brouillons/methode-lead-gen-seo.md` · `préparation-seo-vs-google-ads.md` · `préparation-ranker-chatgpt.md` · `préparation-newsletter-indexation-2026-05-11.md` | Brouillons devenus ou en passe de devenir contenu publié |

> Note boucle preuves : pour chaque article publié de P2, créer la source ET la [[preuves/index|fiche preuve]] qui le relie à l'hypothèse doctrinale qu'il teste (ex. les pSEO secteur×ville testent [[hypotheses#H-002]] et [[hypotheses#H-007]]).

## Priorité 3 — À traiter selon valeur

| Fichier raw | Note |
|---|---|
| `raw/auteurs/greg-isenberg/2026-05-13-notes-on-agent-economy.md` | Auteur externe. Source `source_type: article` + respect strict §13 attribution |
| `raw/notes/process-redaction-5-piliers.md` | Process rédaction généralisable, à croiser avec [[concepts/workflow-redaction-8-etapes]] (vérifier doublon/évolution) |
| `raw/bootcamp4/ton-de-voix-worksheet.md` | Worksheet ton de voix, croise [[concepts/anti-ai-writing]] |
| `raw/articles/brouillons/engine-densite-semantique-sans-serp.md` | Déjà partiellement couvert par [[engine-densite-semantique-sans-serp]] — vérifier si diff à ingérer |
| `raw/notes/drive-accompagnement/` (templates individuels) | Voir [[contradictions#C-006]] : statut `acceptée`, ingest à la demande seulement |

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
