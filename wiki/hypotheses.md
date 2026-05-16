---
type: register
title: Registre des hypothèses
aliases: [hypotheses, registre-hypotheses, hypotheses-non-validees]
tags: [meta, doctrine, validation, hypotheses, moat]
created: 2026-05-16
updated: 2026-05-16
sources: 0
confidence: high
status: living-doc
---

# Registre des hypothèses

> Toute la doctrine de cette KB repose sur des transferts d'architecture (Titans/MIRAS → Google Search) et des intuitions terrain. Beaucoup sont marquées "non validé" un peu partout dans le wiki. Tant qu'elles restent éparpillées en note de bas de page, elles ne se font jamais trancher. Ce registre les rassemble en programme de recherche : une ligne = une affirmation testable + comment on la tranche + son statut.
>
> Règle : une hypothèse ne passe pas `validé` ou `invalidé` sans une [[preuves/index|fiche preuve]] qui pointe vers une donnée terrain, un test, ou un benchmark. Pas de preuve = ça reste `ouvert`. C'est ce registre qui transforme "data propriétaire" d'un argument commercial en moat réel. Voir [[concepts/data-proprietaire]] et [[concepts/persistent-wiki-vs-rag]].
>
> Cadence de revue : mensuelle via le skill `hypotheses-validation`. Mention en [[revue-hebdo/index|revue hebdo]] de toute hypothèse passée `en-test`.

## Statuts

- `ouvert` : énoncée, aucune preuve dans un sens ou l'autre
- `en-test` : un test terrain / une instrumentation est en cours, lien vers [[preuves/index]]
- `validé` : preuve terrain à l'appui, devient doctrine applicable
- `invalidé` : preuve contraire, la doctrine qui en dépend doit être corrigée
- `heuristique` : non prouvable directement mais utile et cohérent avec les observations, on l'assume comme heuristique et on l'assume comme telle

## Tableau de bord

| ID | Hypothèse (résumé) | Statut | Pages doctrine qui en dépendent | Preuve |
|---|---|---|---|---|
| H-001 | Google Search/SGE utilise en prod une mémoire type Titans/MIRAS (surprise metric, weight decay) | `heuristique` | [[concepts/surprise-metric]] · [[concepts/weight-decay]] · [[syntheses/doctrine-seo-post-sge]] | — |
| H-002 | Un Surprise Gap fort augmente la mémorisation et la citation par les LLM | `ouvert` | [[concepts/surprise-gap]] · [[concepts/surprise-metric]] | — |
| H-003 | Le Grounding Score (cosinus intention↔page + divergence) prédit la citation IA | `ouvert` | [[concepts/grounding-score]] · [[concepts/methode-organikk-4-piliers]] | — |
| H-004 | Une page "entity / style wiki" est mieux citée en SGE qu'une page statique équivalente | `ouvert` | [[concepts/persistent-wiki-vs-rag]] · [[queries/2026-04-12-wiki-pattern-vs-grounding-score]] | — |
| H-005 | structural-information-geo (title/meta/schema > body, +22% Hit Rate) se généralise au contenu français | `ouvert` | [[concepts/structural-information-geo]] | — |
| H-006 | Google applique un biais de récence fort (obs. Metehan, `use_freshness_scoring_profile`) | `ouvert` | [[concepts/weight-decay]] · [[entities/metehan]] | — |
| H-007 | La data propriétaire réduit le Retrieval Collapse et augmente l'exposition réelle | `en-test` | [[concepts/data-proprietaire]] · [[concepts/retrieval-collapse]] | [[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]] |
| H-008 | L'answer-first pattern (validé A/B Xiaohongshu) tient sur Google/IA en français | `ouvert` | [[concepts/answer-first-pattern]] | — |
| H-009 | Les résultats commerciaux Tim (1h30→45min, closing 10→50%, top 2) tiennent sur un échantillon instrumenté, pas seulement auto-rapporté | `ouvert` | [[sources/2026-04-13-cas-clients-resultats]] | — |
| H-010 | Le scoring 4 axes transpose fidèlement le paper OpenDecoder (Mo et al., 2026) | `ouvert` | [[sources/2026-04-15-opendecoder-seo-scoring-system]] | — |

## Détail

### H-001 — Transfert Titans/MIRAS vers Google Search en production

Énoncé : les moteurs génératifs (SGE, AI Overviews) intègrent une mécanique de mémoire neurale proche de Titans/MIRAS, ce qui justifie [[concepts/surprise-metric]] et [[concepts/weight-decay]] comme leviers SEO.

Statut `heuristique`. C'est l'hypothèse mère de toute la [[syntheses/doctrine-seo-post-sge|doctrine 4 piliers]]. Titans/MIRAS est un papier Google DeepMind Research, pas une confirmation de Google Search en prod ([[sources/2026-04-11-seo-ia-tim]]). On ne pourra jamais la prouver causalement de l'extérieur. Décision : on l'assume comme heuristique parce qu'elle reste cohérente avec les observations indépendantes (benchmark GEO [[sources/2026-04-13-geo-aggarwal-2024]], biais de récence [[entities/metehan]], QRG p.42 [[entities/quality-raters-guidelines]]). Ce qui se teste, ce ne sont pas les internals de Google : ce sont les prédictions opérationnelles qui en découlent (H-002 à H-008).

Comment on avance : on arrête de chercher à valider le transfert lui-même. On valide ou on casse ses conséquences testables une par une.

### H-002 — Surprise Gap et citation LLM

Énoncé : un article qui contient une information à fort gradient (un chiffre, une inversion, une donnée terrain qu'aucune autre source ne porte) est davantage mémorisé et cité par les moteurs génératifs.

Test pour trancher : publier sur Organikk deux contenus comparables, un avec un Surprise Gap propriétaire net (donnée terrain Tim), un sans. Mesurer à 30/90j les citations IA (ChatGPT, Perplexity, AI Mode) et les positions. Instrumenter via [[preuves/index]]. Pages : [[concepts/surprise-gap]].

### H-003 — Grounding Score prédictif de la citation

Énoncé : la proximité cosinus intention↔page augmentée d'une composante de divergence prédit la probabilité d'être cité par une IA.

Test : sur un lot de pages publiées, calculer le Grounding Score a priori, comparer au taux de citation IA constaté à 90j. Corrélation = signal. Pages : [[concepts/grounding-score]] · [[concepts/methode-organikk-4-piliers]].

### H-004 — Page entity/wiki vs page statique

Énoncé : structurer une page comme une entité de wiki persistant (dense en liens, atomique, sourcée) la rend plus citable qu'une page statique classique sur la même intention. Hypothèse posée dès [[sources/2026-04-11-karpathy-llm-wiki]], structurée mais jamais testée ([[queries/2026-04-12-wiki-pattern-vs-grounding-score]]).

Test : deux pages Organikk sur la même intention, l'une en format entité dense, l'autre en article classique. Citations IA à 90j.

### H-005 — Généralisation FR de structural-information-geo

Énoncé : le finding SAGEO Arena (title/meta/schema dominent le body, +22% Hit Rate, [[sources/2026-04-13-sageo-arena-2025]]) tient sur du contenu français. Validé corpus anglophone uniquement.

Test : sur le corpus Organikk FR, comparer le poids des signaux structurels vs body sur les pages citées vs non citées.

### H-006 — Biais de récence Google

Énoncé : les résultats top 10 Google sont systématiquement plus récents de 1 à 5 ans (obs. [[entities/metehan]], param interne `use_freshness_scoring_profile`). Citation secondaire de Tim, non vérifiée indépendamment, `confidence: medium` sur [[concepts/weight-decay]].

Test : échantillon de requêtes Organikk pertinentes, distribution des dates de publication du top 10 vs reste. Si écart net et stable, signal.

### H-007 — Data propriétaire contre Retrieval Collapse

Énoncé : le Retrieval Collapse (67% du pool capte 80% de l'exposition, NAVER [[sources/2026-04-25-scan-arxiv-25-avril]]) frappe moins les pages portant une donnée propriétaire unique. C'est l'argument scientifique central vendu aux prospects ([[concepts/data-proprietaire]] · [[concepts/retrieval-collapse]]).

Statut `en-test` depuis le 2026-05-16 (décision [[revue-hebdo/2026-W20]] point 2, exécutée en revue mensuelle). Fiche : [[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]]. Cohorte = 5 pages pSEO secteur×ville déjà publiées (sans attendre le déploiement du cluster, [[contradictions#C-003]]). Jalons J+30 ≈ 2026-06-15, J+90 ≈ 2026-08-14. Réserve dure : baseline GSC non capturée tant que le service account n'est pas déposé ([[preuves/SETUP-GSC]]) — H-007 ne peut pas dépasser `en-test` avant que la baseline et les jalons soient renseignés.

Test : suivre l'exposition réelle (citations IA, impressions) des pages Organikk à data propriétaire vs pages génériques sur 90j.

### H-008 — Answer-first en français

Énoncé : le pattern réponse-directe en 2-3 phrases en tête de page, validé A/B en production sur Xiaohongshu ([[concepts/answer-first-pattern]]), tient sur Google/IA en français.

Test : A/B sur pages Organikk, présence vs absence du bloc answer-first, mesure position 0 et citations IA.

### H-009 — Résultats commerciaux instrumentés

Énoncé : les preuves chiffrées du discours commercial (1h30→45min de rédaction, closing 10→50%, top 2 sur balle de golf, [[sources/2026-04-13-cas-clients-resultats]]) tiennent sur un échantillon mesuré, pas seulement auto-rapporté. `confidence: medium` par défaut sur la source.

Test : instrumenter sur les prochains clients (Victoria Garden, FG Formation) une mesure tierce avant/après, archivée dans [[preuves/index]]. C'est ce qui transforme un argument de vente en preuve opposable.

### H-010 — Fidélité du scoring à OpenDecoder

Énoncé : le système de scoring 4 axes ([[sources/2026-04-15-opendecoder-seo-scoring-system]]) transpose fidèlement le paper OpenDecoder (Mo et al., 2026), qui n'est pas encore ingéré comme source paper. Croise [[contradictions#C-002]].

Test : ingérer le paper primaire, auditer la fidélité de la transposition formule par formule.

---

## Quand une hypothèse change de statut

1. Créer ou mettre à jour la [[preuves/index|fiche preuve]] correspondante
2. Passer le statut ici + dans le tableau de bord
3. Sur les pages doctrine listées, ajuster le `confidence:` et le wording (un `validé` enlève le "non validé", un `invalidé` impose une correction documentée)
4. Logguer dans [[log]] : `## [YYYY-MM-DD] hypothese | H-XXX → validé/invalidé`
5. Si `invalidé` : ouvrir une entrée dans [[contradictions]] pour tracer la dette doctrinale à corriger

Pages liées : [[index]] · [[contradictions]] · [[preuves/index]] · [[ingest-backlog]] · [[concepts/data-proprietaire]]
