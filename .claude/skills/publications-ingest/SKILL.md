---
name: publications-ingest
description: |
  Ce skill scrape les dernières pages publiées par Tim sur ses deux canaux (la newsletter « Algorithme » sur algorithme.substack.com et le blog organikk.co/blog), détecte celles qui ne sont pas encore dans le vault, et crée une fiche source `wiki/sources/` par nouvelle page avec des wikilinks vers les entities/concepts existants. Puis il met à jour `wiki/index.md`, `wiki/log.md` et relance `./kb rebuild`.

  Utilise ce skill quand l'utilisateur dit « scrape mes publications », « ingère les dernières pages d'Algorithme / d'Organikk », « rattrape mes articles », « mets à jour les sources publiées », ou quand le runner `run-publications-ingest.sh` / le launchd `com.timboussardon.publications-ingest` se déclenche.
---

# Publications-ingest — scrape + ingest des canaux publiés de Tim

Tu ingères dans le vault SEO les pages que Tim a publiées sur ses deux canaux, comme des **sources** (`source_type: article`). Ce n'est pas de la rédaction : tu résumes fidèlement, tu chiffres, tu relies. Tu appliques la doctrine d'ingest de `AGENTS.md` (§6.1) et les conventions de fichiers (§5).

Les deux canaux :
- **Algorithme** (Substack) : archive = `https://algorithme.substack.com/archive?sort=new`
- **Organikk** (blog) : listing = `https://organikk.co/blog`

## Étape 1 — Cartographier l'existant (dédup)

Avant tout, liste ce qui est déjà ingéré pour ne rien retraiter :

```
ls wiki/sources/ | grep -E "algorithme|organikk"
```

La **clé de dédup fiable est l'URL du post**, pas le nom de fichier. Chaque fiche stocke sa ligne `**URL** : ...`. Pour chaque post candidat, vérifie s'il est déjà ingéré :

```
grep -rl "<url-exacte-du-post>" wiki/sources/ 2>/dev/null
```

Si ça renvoie un fichier, le post est déjà ingéré → tu le sautes.

## Étape 2 — Récupérer les listings et filtrer les nouveautés

WebFetch l'archive Substack et le listing du blog. Pour chacun, récupère titre + date + URL de chaque post visible. Croise avec l'étape 1 : ne gardes que les **posts absents du vault**.

Garde-fous :
- Traite au maximum **8 nouveaux posts par run** (les plus récents d'abord). S'il y en a davantage, traite les 8 plus récents et note dans le log les posts plus anciens laissés pour le run suivant.
- Si zéro nouveau post : n'écris rien, logue « aucune nouveauté », et termine proprement (l'étape 5 et 6 sont sautées, pas de rebuild inutile).

## Étape 3 — Scraper et écrire une fiche par post

Pour chaque nouveau post : WebFetch l'URL, extrais titre, contenu, chiffres, thèses, citations marquantes (< 15 mots). Le Substack peut être partiellement paywallé — si le contenu est tronqué, prends ce qui est public et mets `confidence: medium` en le notant dans « Limites ».

Écris `wiki/sources/YYYY-MM-DD-<canal>-<slug>.md` (`<canal>` = `algorithme` ou `organikk`, `<slug>` = kebab-case court du titre, sans accents) :

```
---
type: source
source_type: article
title: <Titre lisible>
aliases: [<slug-court>]
tags: [<algorithme|organikk>, tim, <2-4 tags pertinents : seo, ia, geo, aeo, claude, ...>]
created: <date de publication>
updated: <date du jour>
sources: 1
confidence: high | medium
status: stable
---

# <Titre>

**Auteur** : Timothée Boussardon (<algorithme.substack.com | organikk.co/blog>)
**Type** : newsletter / article
**URL** : <url>
**Date publication** : <date>

## Contexte
<2-4 phrases : sujet, angle>

## Chiffres / faits clés
<bullets factuels avec chiffres et, si utile, source citée par le post>

## Citations marquantes
> "<citation verbatim < 15 mots>" (attribution : Tim, <date>)

## Angle SEO à retenir
<1-3 bullets : l'insight exploitable, l'inversion d'expertise>

## Limites
<qualité du scrape, paywall, claims non vérifiés>

## Pages liées
**Entity** : [[entities/...]]
**Concepts** : [[concepts/...]]
```

## Étape 4 — Wikilinks : ne lier QUE des pages existantes

Récupère la liste **à jour** des cibles autorisées au moment du run (ne travaille jamais de mémoire) :

```
ls wiki/entities/ | sed 's/\.md$//'
ls wiki/concepts/ | sed 's/\.md$//'
```

Règles :
- Minimum **2 wikilinks sortants** par fiche, tous présents dans ces deux listes.
- **Ne crée AUCUNE page entity/concept** dans ce skill (run non supervisé : risque de nœuds bâclés). Si tu voudrais lier une cible qui n'existe pas, ne l'invente pas.
- Collecte les cibles manquantes récurrentes et **liste-les dans l'entrée de log** (section « nœuds suggérés ») pour que Tim les crée en curation supervisée.
- Après avoir écrit toutes les fiches, fais un check anti-lien-mort :

```
for f in <fichiers créés>; do grep -oE '\[\[(entities|concepts)/[a-z0-9-]+\]\]' "$f" | sed -E 's/\[\[|\]\]//g'; done | sort -u | while read l; do [ -f "wiki/$l.md" ] || echo "DEAD: $l"; done
```

Corrige tout `DEAD` avant de continuer.

## Étape 5 — Mettre à jour l'index et le log

- `wiki/index.md` : ajoute chaque nouvelle fiche sous `### Articles`, en ordre chronologique, format `- [[sources/<slug>]] — <résumé 12 mots>`. Ajuste le compteur `### Articles (N)` et `## Sources (N)`.
- `wiki/log.md` : append une entrée (format strict `## [YYYY-MM-DD] action | titre`) :

```
## [YYYY-MM-DD] ingest | Scrape auto publications (Algorithme + Organikk)
- source_type: article
- sources créées: N (liste des [[sources/...]])
- posts sautés (déjà ingérés): M
- wikilinks: min 2/fiche, 0 lien mort (vérifié)
- nœuds suggérés (à créer en curation): <liste ou "aucun">
- angle SEO transverse: <1 phrase>
```

## Étape 6 — Reconstruire l'index

```
./kb rebuild
```

## Étape 7 — Rapport

Résumé inline : nombre de fiches créées, lesquelles, posts sautés, nœuds suggérés. En run non supervisé, ce rapport part dans le log du runner ; le commit/push est géré par le runner, pas par toi.

## Rappels doctrine
- `raw/` immuable, écriture uniquement dans `wiki/`.
- Tous les chiffres ont leur source (ici, le post lui-même via la ligne `**URL**`).
- Pas d'invention de chiffres. Pas de wikilink vers une page absente.
- Zéro rédaction promotionnelle : tu résumes une source, tu ne réécris pas l'article.
