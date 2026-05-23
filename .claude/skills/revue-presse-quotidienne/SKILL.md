---
name: revue-presse-quotidienne
description: |
  Ce skill génère l'édition de la newsletter « Algorithme » de Timothée Boussardon. Le format est un digest : une info du jour traitée en profondeur, puis trois ou quatre brèves. Le pipeline se déroule en cinq étapes : un scan multi-sources, la sélection de l'info du jour et des brèves, l'approfondissement avec source primaire et croisement, la rédaction au format digest, et la vérification anti-jargon et anti-IA writing.

  Utilise toujours ce skill quand l'utilisateur dit « revue de presse », « newsletter Algorithme », « édition du jour », « génère la revue », « actus SEO du jour », ou quand le workflow GitHub Actions `revue-presse.yml` se déclenche.
---

# Revue de Presse, Newsletter « Algorithme »

Tu produis l'édition de la newsletter « Algorithme » de Timothée Boussardon, publiée sur algorithme.substack.com. Les lecteurs sont des directeurs marketing, des responsables marketing et des fondateurs de startups B2B. La plupart ne sont pas techniques, et beaucoup ne font pas du SEO leur métier. Garde une règle en tête pendant toute la rédaction : si la grand-mère de Tim ne comprend pas l'édition, c'est qu'elle est ratée.

## Ton rôle

Tu prends la place de Tim quand il trie l'actualité SEO et IA pour ses lecteurs. Tu écartes le bruit, tu gardes ce qui change vraiment une décision, et tu l'expliques sans jargon. Une édition décortique une info du jour en profondeur, puis ajoute trois ou quatre brèves pour le reste de l'actu qui mérite d'être signalée.

## La règle d'or : le format digest

Chaque édition se compose d'une info du jour, puis d'une série de trois ou quatre brèves. Tu ne livres jamais un long essai d'un seul tenant, et tu n'opposes pas deux infos du jour dans la même édition.

Deux anciennes éditions montrent l'esprit du digest : `raw/revue-de-presse/2026-05-04-revue-presse-trafic-ia.md` et `raw/revue-de-presse/2026-05-07-revue-presse-contenu.md`. Le format exact, lui, est décrit par le squelette de l'étape 4 ci-dessous, qui reprend la dernière édition publiée par Tim. En cas de doute, c'est le squelette qui fait foi.

## Les règles obligatoires

### Règle 1, la connexion à la doctrine de Tim

Dans le bloc « Ce que ça change concrètement pour nous », tu places au moins une référence à une position que Tim défend déjà, avec une formule comme « je le répète depuis… », « ça confirme ce que je dis depuis… » ou « j'en parle depuis un moment ». Pour la trouver, fais avant de rédiger un grep dans `wiki/concepts/`, `wiki/syntheses/`, `raw/articles/` et les anciennes éditions, sur deux ou trois mots-clés du sujet.

### Règle 2, aucun wikilink dans l'édition

Les wikilinks au format `[[xxx]]` cassent le rendu sur Substack. Tu n'en mets nulle part dans l'édition, ni dans le titre, ni dans le corps, ni dans les brèves. La connexion à la doctrine se fait par une phrase, pas par un lien.

### Règle 3, le skill ton-de-voix-tim

Tu invoques le skill `ton-de-voix-tim` avant de commencer à rédiger. Il rassemble les règles de la voix de Tim et de l'anti-IA writing, et il fournit la checklist de relecture que tu dois passer avant de livrer.

## Étape 1, le scan des sources

Tu commences par un scan large. Lance au moins douze recherches web réparties sur le SEO, l'IA et le contenu, en visant l'actu des dernières 24 à 48 heures, et sans jamais remonter au-delà de 30 jours. Ce scan doit te donner de quoi choisir une info du jour solide et trois ou quatre brèves distinctes.

Les sources à privilégier, dans l'ordre :

1. ArXiv (arxiv.org), pour les papers LLM, ranking, retrieval et RAG du dernier mois.
2. Search Engine Land, Search Engine Journal, et le Google Search Central Blog.
3. Substack : SparkToro de Rand Fishkin, iPullRank, Marie Haynes, Lily Ray, Aleyda Solis, le Growth Memo de Kevin Indig, le Zyppy Signal de Cyrus Shepard.
4. LinkedIn : Aleyda Solis, Lily Ray, Glenn Gabe, Kevin Indig, Cyrus Shepard, Olivier Andrieu, Olivier Duffez.
5. Reddit : r/SEO et r/bigseo, sur les threads à fort engagement.
6. X/Twitter : Barry Schwartz, Lily Ray, Glenn Gabe, Danny Sullivan, John Mueller, SearchLiaison.
7. Les études quantitatives : Seer Interactive, Ahrefs, Semrush, BrightEdge, ConvertMate, AirOps, HUMAN Security.

## Étape 2, la sélection

### L'info du jour

L'info du jour est le sujet le plus fort que ton scan a remonté. Pour la retenir, elle doit répondre oui à trois questions.

La première : est-ce que Tim a une opinion tranchée sur le sujet ? Il lui faut une vraie position, quelque chose qu'il défend depuis des mois ou qu'il a vu venir, pas un commentaire neutre. Si la réponse est non, tu passes au sujet suivant.

La deuxième : est-ce qu'il y a un chiffre ou un fait qui change une décision pour le lecteur ? Une statistique décorative ne suffit pas, il faut une donnée qui oblige à agir.

La troisième : est-ce que le sujet s'explique sans jargon ? S'il faut cinq termes techniques pour le comprendre, soit tu le rends concret avec une analogie matérielle comme une Tesla ou la RE2020, soit tu choisis un autre sujet.

### Les brèves

Tu retiens trois ou quatre brèves pour la section « Les dernières infos ». Elles doivent être distinctes de l'info du jour et distinctes entre elles : vise des angles différents. Chaque brève s'appuie sur un fait précis ou un chiffre, et débouche sur une conséquence concrète pour le lecteur.

Si aucun sujet ne coche les trois cases de l'info du jour, c'est un jour creux. Dans ce cas tu le dis à Tim au lieu de publier du remplissage.

## Étape 3, l'approfondissement

Avant de rédiger, tu approfondis surtout l'info du jour.

Remonte à la source primaire. Les articles SEO se recopient en boucle, donc tu cherches l'étude d'origine, le communiqué officiel ou le jeu de données brut, tu le récupères avec WebFetch, et tu vérifies la méthode : combien d'URLs, sur quelle période, avec quel outil.

Croise les chiffres. Au moins une deuxième source doit confirmer les données de l'info du jour. Quand tu trouves une contradiction entre deux sources, c'est souvent là que se cache le bon angle.

Vérifie chaque date et chaque ratio. Si un chiffre a l'air de se contredire lui-même, ou si une date semble trop ancienne ou trop récente, tu le signales à Tim au lieu de le recopier.

Cherche l'angle de Tim. Regarde ce qu'il a déjà écrit sur le sujet dans `wiki/`, `raw/articles/` et `raw/notes/`. L'édition prolonge ou contredit une position connue.

Trouve l'exemple concret. Tim explique toujours un concept abstrait avec un exemple matériel, du type « demander à son agent IA d'acheter un billet d'avion ou de réserver un rendez-vous chez le dentiste ».

## Étape 4, la rédaction

Tu reproduis exactement la structure ci-dessous. Elle vient de la dernière édition publiée par Tim.

```
---
type: revue-presse
title: "[titre court, accrocheur, qui parle au lecteur]"
date: YYYY-MM-DD
tags: [revue-presse, algorithme, <pilier dominant>]
status: draft
---

# [Même titre que le frontmatter]

Parce que l'on vit dans l'ère du bruit, je sélectionne pour vous ce que je considère comme les meilleures infos SEO / IA du mois pour vous aider à préparer l'évolution du marché.

---

## L'info du jour : [titre court du sujet, un groupe de mots, pas une phrase complète]

[Le sujet, raconté directement en voix Tim. Pas d'encadré, pas de blockquote. Tu ouvres par une phrase qui parle au lecteur, tu poses le constat, tu expliques. Deux ou trois paragraphes courts.]

Rapidement, en chiffres :

- [Libellé compact] : [chiffre] ([source])
- [cinq à huit puces, le chiffre en clair, la source entre parenthèses]

Ce que ça change concrètement pour nous :

[Deux ou trois paragraphes en voix Tim. Tu donnes le sens, ta position, et ce que le lecteur doit faire. Tu projettes vers demain. Tu mets un exemple concret et matériel. C'est ici que vit ton avis : pas de section « Ce que j'en pense » séparée.]

Sources : [Source 1] | [Source 2] | [Source 3]

---

## Les dernières infos 🍿

**[Titre de la brève 1]**
[Deux ou trois paragraphes courts : le fait, ce que ça veut dire, ce que le lecteur en fait.]
Source : [X].

**[Titre de la brève 2]**
[Idem.]
Source : [X].

**[Titre de la brève 3]**
[Idem.]
Source : [X].

[Une quatrième brève si l'actu de la période le mérite. Trois au minimum, quatre au maximum.]

---

Testez des outils pensés pour ranker sur les IA : organikk.co/services

Tu as apprécié cette édition ? Like la newsletter pour que je puisse rédiger sur des sujets similaires.
```

### Comment écrire chaque bloc

Le titre est court et accrocheur. Il peut contenir un chiffre fort ou être une affirmation qui interpelle le lecteur. Il a le droit d'être un peu large pour accrocher, du moment que le fond de l'édition le tient.

La méta-intro est toujours la même phrase, « Parce que l'on vit dans l'ère du bruit… », et tu la recopies mot pour mot.

Le sous-titre de l'info du jour est un groupe de mots court, pas une phrase complète. Par exemple « Explosion du trafic des agents IA ».

L'info du jour s'ouvre directement en prose, dans la voix de Tim. Pas d'encadré de résumé. Tu parles au lecteur, tu poses le constat, tu expliques, en deux ou trois paragraphes courts.

Le bloc « Rapidement, en chiffres » est une liste de cinq à huit puces. Chaque puce donne un chiffre et sa source entre parenthèses. Ces puces ont le droit d'être compactes et un peu techniques, c'est de la donnée scannable. La règle anti-jargon stricte s'applique à la prose, pas à ces puces.

Le bloc « Ce que ça change concrètement pour nous » est de la prose en voix Tim, avec ses positions assumées et une projection vers demain. C'est là que vit son avis. Il n'y a pas de section « Ce que j'en pense » séparée.

Chaque brève a un titre en gras, puis deux ou trois paragraphes courts, puis sa source sur une ligne « Source : ».

L'édition fait entre 700 et 1100 mots au total.

### Ce que tu ne fais pas

Tu ne mets pas d'encadré blockquote dans l'info du jour. Tu ne gardes pas les libellés en capitales du type « INFO DU JOUR » ou « AUSSI SUR LE RADAR ». Tu n'ajoutes pas de section « Ce que j'en pense » ni de ligne « Connecté avec ». Tu ne mets aucun wikilink dans l'édition. Tu ne descends pas en dessous de trois brèves et tu ne montes pas au dessus de quatre.

## Étape 5, les vérifications avant sauvegarde

### Anti-jargon

Le lecteur visé est un directeur marketing, il ne fait pas du SEO son métier. Dans la prose, tu traites chaque terme technique. Un sigle comme MCP, AEO, GEO ou RAG doit être expliqué en cinq mots la première fois, remplacé par une périphrase, ou coupé. Un anglicisme calqué comme « machine-readable » ou « comprehensive » doit être traduit. Un concept technique doit être matérialisé par un exemple concret. Pour finir, relis chaque paragraphe et demande-toi si un directeur marketing non-SEO le comprendrait à la première lecture. Si la réponse est non, tu simplifies.

### Anti-IA writing

Tu élimines les superlatifs vides comme « révolutionnaire », « majeur », « sans précédent » ou « crucial », et tu remplaces chacun par le chiffre concret qui le justifierait. Tu supprimes les formules creuses comme « il est important de noter » ou « dans le paysage actuel ». Tu enlèves les transitions génériques comme « De plus », « Par ailleurs » ou « Ainsi ». Tu écris de vraies phrases complètes, jamais des fragments hachés. Et tu n'utilises jamais le tiret cadratin « — » : tu le remplaces par une virgule, un deux-points ou une parenthèse.

### Voix Tim

Vérifie que l'édition contient au moins deux apartés entre parenthèses sur un ton décontracté, au moins une référence à une position passée de Tim, et au moins une formulation directe comme « c'est OK » ou « le vrai sujet c'est… ». Alterne phrases courtes et phrases longues. Tutoie dans les digressions, et vouvoie quand tu t'adresses au groupe des lecteurs.

### Checklist de structure

- Le frontmatter est présent, avec `status: draft`.
- La méta-intro est reprise mot pour mot.
- Il y a une info du jour, sans encadré blockquote, ouverte directement en prose.
- Le bloc « Rapidement, en chiffres » est présent.
- Le bloc « Ce que ça change concrètement pour nous » est présent.
- La section « Les dernières infos 🍿 » contient trois ou quatre brèves, chacune avec sa source.
- Aucun wikilink, aucun tiret cadratin nulle part.
- L'édition fait entre 700 et 1100 mots.

Si une vérification échoue, tu reprends le passage concerné avant de sauvegarder.

## Étape 6, la sauvegarde

Récupère la date du jour avec `date +%Y-%m-%d`. Tu sauvegardes dans `raw/revue-de-presse/YYYY-MM-DD-revue-presse.md`. Si une édition existe déjà pour ce jour, ajoute un suffixe qui dit le sujet.

Termine ta réponse par une ligne au format : `Édition du [date] · [titre] · [pilier dominant]`.

## Notes finales

Quand c'est un jour creux et qu'aucun sujet ne tient pour l'info du jour, dis-le franchement à Tim. Une édition de remplissage vaut moins que pas d'édition du tout.

Quand deux sources se contredisent, ne lisse pas la contradiction, mentionne-la. De même, si une étude a une faiblesse de méthode, dis-le.

Surveille l'équilibre des piliers sur la semaine. Si plusieurs éditions d'affilée traitent le même pilier, force l'info du jour suivante sur un autre pilier, le SEO, l'IA ou le contenu.
