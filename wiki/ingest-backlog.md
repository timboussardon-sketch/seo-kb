---
type: register
title: Backlog d'ingest
aliases: [ingest-backlog, backlog, raw-non-traite, file-ingest]
tags: [meta, ingest, capture, pipeline, backlog]
created: 2026-05-16
updated: 2026-05-18
last_sweep: 2026-05-18
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

## Priorité 1 — Données terrain propriétaires non capturées (le moat qui fuit) — 16

Ce sont les sources qui justifient l'existence de la KB : du terrain unique, non rejouable, qui alimente directement la doctrine et le discours commercial. Les laisser non traitées, c'est laisser fuir le moat. Oldest-first.

| Fichier raw | Date | Pourquoi prioritaire |
|---|---|---|
| `raw/data/keyword-research-2026-05-02/keywords-cleaned.md` (10 Ko) | 2026-05-02 | Recherche de mots-clés brute = data terrain. Croise [[concepts/mots-cles-actionnels]] |
| `raw/data/keyword-research-2026-05-02/keywords-classified.md` (12 Ko) | 2026-05-02 | Idem, classifiée par intention. Matière directe pour modèle mots-clés |
| `raw/bootcamp4/session-1-mots-cles-prep.md` (22 Ko) | 2026-05-07 | Préparation pédagogique bootcamp 4 session 1 |
| `raw/bootcamp4/sequencage-semaine-2.md` (8 Ko) | 2026-05-12 | Séquençage semaine 2, structure pédagogique |
| `raw/bootcamp4/session-1-mots-cles-nouveautes.md` (9 Ko) | 2026-05-12 | Nouveautés pédagogiques mots-clés |
| `raw/bootcamp4/session-1-mots-cles-transcript.md` (93 Ko) | 2026-05-12 | Transcript brut bootcamp live = data terrain pédagogique unique. Aucun équivalent wiki |
| `raw/acquisition/modele-roadmap-premier-call.md` (11 Ko) | 2026-05-14 | Livrable premier call = asset commercial structurant, lié à [[syntheses/workflow-complet-consultant-seo-ia]] |
| `raw/articles/modele-production/modele-mots-clés.md` (12 Ko) | 2026-05-14 | Modèle de production scalable. Croise [[concepts/programmatique-pseo]] et [[concepts/pseo-data-driven-models]] |
| `raw/bootcamp4/observations-whatsapp-bootcamp.md` (11 Ko) | 2026-05-15 | Blocages et questions du groupe = matière directe pour [[concepts/avatar-freelance-sans-systeme]] et [[concepts/cercle-vicieux-temps-structure]] |
| `raw/articles/modele-production/modele-strategie.md` (25 Ko) | 2026-05-15 | Modèle de production stratégie scalable (cœur du livrable) |
| `raw/articles/modele-production/modele-strategie-b2b.md` (28 Ko) | 2026-05-15 | Modèle de production stratégie B2B scalable (cœur du livrable commercial) |
| `raw/bootcamp4/session-2-redaction-prep.md` (30 Ko) | 2026-05-15 | Préparation pédagogique bootcamp 4 session 2 rédaction |
| `raw/bootcamp4/session-3-audit-prep.md` (2 Ko) | 2026-05-16 | Préparation pédagogique bootcamp 4 session 3 audit |
| `raw/bootcamp4/session-2-redaction-debrief.md` (14 Ko) | 2026-05-16 | Debrief session rédaction = verbatims objections/peurs réels |
| `raw/bootcamp4/session-2-redaction-resume-participants.md` (24 Ko) | 2026-05-16 | Retours participants = verbatims peurs/blocages terrain |
| `raw/bootcamp4/session-2-redaction-transcript.md` (48 Ko) | 2026-05-16 | Transcript brut session 2 rédaction = data terrain pédagogique unique |

## Priorité 2 — Contenu publié non bouclé (boucle preuves) — 13

Articles et newsletters publiés qui n'ont ni source wiki ni [[preuves/index|fiche preuve]]. Sans eux, la boucle sortie→apprentissage ne tourne pas : on publie et on ne mesure jamais. Oldest-first.

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

> Note boucle preuves : pour chaque article publié de P2, créer la source ET la [[preuves/index|fiche preuve]] qui le relie à l'hypothèse doctrinale qu'il teste (ex. les pSEO secteur×ville testent [[hypotheses#H-002]] et [[hypotheses#H-007]]).

## Priorité 3 — À traiter selon valeur — 11 (+ drive-accompagnement parké)

| Fichier raw | Date | Note |
|---|---|---|
| `raw/articles/brouillons/linkedin-trend-research-semaine-2-avril-2026.md` | 2026-04-25 | Notes trend research (ex `linkedin-trend-research-SEO-LLM-…` supprimé, renommé). Pas de source — vérifier valeur doctrinale |
| `raw/notes/process-redaction-5-piliers.md` | 2026-05-02 | Process rédaction généralisable, à croiser avec [[concepts/workflow-redaction-8-etapes]] (vérifier doublon/évolution) |
| `raw/ia-employe/recap-jour-health-2026-05-07.md` | 2026-05-07 | `type: health-check` de l'automation recap-jour (statut OK). Méta/ops, valeur doctrinale ~nulle — **candidat skip**, à trancher par Tim (pas auto-skip car non documenté). À vérifier |
| `raw/articles/brouillons/engine-densite-semantique-sans-serp.md` | 2026-05-11 | Aucune page wiki `engine-densite-semantique-sans-serp` n'existe (réf orpheline dans [[log]]/[[index]]) — brouillon non traité, vérifier si à ingérer |
| `raw/bootcamp4/ton-de-voix-worksheet.md` | 2026-05-12 | Worksheet ton de voix, croise [[concepts/anti-ai-writing]] |
| `raw/auteurs/README.md` | 2026-05-13 | Convention du dossier `raw/auteurs/` (règle d'attribution §13). Process/navigation, pas de matière doctrinale — **candidat skip**, à trancher par Tim. À vérifier |
| `raw/auteurs/greg-isenberg/2026-05-13-notes-on-agent-economy.md` | 2026-05-13 | Auteur externe. Source `source_type: article` + respect strict §13 attribution |
| `raw/data/strategies-paris/{avocat,hotel,paysagiste}/sources.md` · `raw/data/strategies-b2b/centre-formation-ia/sources.md` (4 fichiers) | — | Listes de sources/citations adossées aux articles pSEO P2 — à ingérer avec eux, pas seules. À vérifier |
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
