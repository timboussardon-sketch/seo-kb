# raw/auteurs/ — Posts verbatim d'auteurs externes

Ce dossier stocke des prises de parole verbatim d'auteurs externes (LinkedIn, X, Substack, newsletters, blogs) que Tim veut conserver tels quels comme matière première.

Un fichier = un post (ou une série thématique d'un même auteur, à la même date).
Un sous-dossier = un auteur. Format : `auteurs/{prenom-nom}/{YYYY-MM-DD}-{slug}.md`.

## Règle d'attribution — non négociable

**Toute citation, paraphrase, reformulation, ou réutilisation d'idée tirée d'un fichier de `raw/auteurs/` doit citer explicitement l'auteur.**

Comme on cite une étude. Jamais une phrase issue d'ici ne doit être présentée comme :
- une idée de Tim
- une idée de l'agent
- une affirmation neutre / orpheline

Le lecteur doit toujours savoir que la phrase vient de l'auteur cité, pas de Tim.

### Format de citation imposé

**Citation directe** (verbatim) — blockquote markdown avec attribution :

```markdown
> "The new buyer on the internet is an agent." — Greg Isenberg, *Notes on the agent economy*, 2026-05-13
```

**Paraphrase / reformulation** — attribution inline obligatoire :

```markdown
Greg Isenberg observe que la moitié des YC companies pivotent dans les 8 semaines post-demo-day, parce que les agents permettent de tester 5 idées dans le temps qu'il fallait avant pour en tester une. ([[auteurs/greg-isenberg/2026-05-13-notes-on-agent-economy]])
```

**Reprise d'idée** dans un argumentaire — attribution + lien :

```markdown
L'idée que "le seul moat c'est distribution + mémoire" vient de Greg Isenberg (cf. [[auteurs/greg-isenberg/2026-05-13-notes-on-agent-economy]]). Appliqué au SEO, ça donne…
```

### Ce qui est interdit

- Reprendre une formule de l'auteur sans attribution
- Mélanger une idée de l'auteur avec la voix de Tim sans marquer la frontière
- Présenter une analyse de l'auteur comme un consensus ou un fait neutre
- Citer "des experts disent que…" sans nommer l'auteur exact

### Ce qui est autorisé

- Critiquer, contester, prolonger l'idée d'un auteur — à condition de citer d'abord
- Croiser plusieurs auteurs sur un même sujet, avec attribution de chacun
- Utiliser une citation comme accroche / contre-argument dans un brief, post, article

## Frontmatter recommandé

```yaml
---
auteur: Prénom Nom
source_url: https://...           # URL d'origine si dispo
plateforme: linkedin | x | substack | newsletter | blog
date_post: YYYY-MM-DD
date_capture: YYYY-MM-DD
langue: fr | en
tags: [agent-economy, seo, ia, ...]
---
```

## Articulation avec le wiki

Une fiche `wiki/sources/...` peut référencer un post `raw/auteurs/...` exactement comme elle référence un article ou un paper, avec `source_type: article` ou `source_type: post` selon le cas. La règle d'attribution s'applique en plus de toutes les règles d'`AGENTS.md`.
