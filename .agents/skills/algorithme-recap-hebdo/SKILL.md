---
name: algorithme-recap-hebdo
description: |
  Synthèse hebdomadaire des 7 dernières revues de presse "Algorithme". Identifie la tendance dominante, le consensus inter-experts, les désaccords, le pilier le plus chaud, et 1-2 angles à creuser la semaine suivante. Output dans wiki/syntheses/.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "récap hebdo", "synthèse semaine Algorithme", "résumé revue de presse semaine", "best of de la semaine", ou quand le workflow GH Actions algorithme-recap-hebdo.yml se déclenche.
---

# Récap Hebdo — Newsletter "Algorithme"

Tu produis une synthèse stratégique de la semaine SEO/IA pour Tim, à partir de ses 7 dernières revues de presse quotidiennes.

## ENTRÉE

Le dossier `raw/revue-de-presse/` contient une édition par jour, format `YYYY-MM-DD-revue-presse.md`.

## STYLE

Lis avant de rédiger : `raw/notes/tim-my-voice.md`. Voix Tim non négociable.

## ÉTAPE 1 — RÉCUPÉRATION DES 7 DERNIÈRES ÉDITIONS

Date du jour : `date -u +%Y-%m-%d`. Numéro semaine ISO : `date -u +%G-W%V`.

Liste les fichiers `raw/revue-de-presse/*.md` modifiés dans les 7 derniers jours :

```bash
find raw/revue-de-presse -name "*-revue-presse.md" -mtime -7 -type f | sort
```

Si moins de 5 éditions trouvées, signale-le et continue avec ce qu'il y a. Si 0 édition, abandonne et écris "Pas assez de matière cette semaine pour un récap" dans le fichier de sortie.

## ÉTAPE 2 — PARSING ÉDITION PAR ÉDITION

Pour chaque édition, extrais en mémoire :
- **Titre** (ligne `# ...` du fichier)
- **Info principale** : sujet (1 phrase synthétique), pilier (SEO / IA / CONTENU), chiffre clé, source primaire
- **Signaux radar** : pour chacun, sujet + pilier + chiffre + source

## ÉTAPE 3 — ANALYSE TRANSVERSALE

### 3.1 Tendance dominante
Quel sujet/thème revient dans le plus d'éditions cette semaine ? Compte les occurrences sémantiques (ex: "AI Overviews" mentionné dans 5/7 éditions).

### 3.2 Pilier le plus chaud
Sur les 7 infos principales + 14-21 signaux radar, quel pilier (SEO / IA / CONTENU) capte le plus de volume ? Donne le ratio (ex: 12/27 = 44% IA).

### 3.3 Consensus inter-experts
Quelles assertions sont confirmées par 2+ sources distinctes cette semaine ? Liste-les. Ex: "Le CTR organique chute de 60%+ avec une AI Overview — confirmé par Ahrefs ET Search Engine Journal."

### 3.4 Désaccords / contradictions
Quels points font débat ? Ex: "Rand Fishkin enterre les ultimate guides, mais Aleyda Solis défend encore le format pillar page." Si pas de désaccord identifié, écris "Pas de désaccord notable cette semaine."

### 3.5 Signaux faibles
2-3 sujets cités UNE SEULE FOIS mais qui ont l'air importants (à creuser plus tard). Ex: "A-RAG mentionné dans 1 édition seulement, mais c'est un papier ArXiv qui mérite une vraie note dans wiki/concepts/."

### 3.6 Angles à creuser
Sur la base des sujets dominants + signaux faibles, propose 1-2 angles de contenu pour Tim la semaine suivante. Format : "Angle : [titre provocateur] — pourquoi maintenant : [tension du marché qui le justifie]."

## ÉTAPE 4 — RÉDACTION

Output : `wiki/syntheses/algorithme-week-YYYY-WNN.md` (numéro de semaine ISO).

Format strict :

```markdown
---
type: synthese
title: Algorithme — Récap semaine NN (YYYY-MM-DD au YYYY-MM-DD)
date: YYYY-MM-DD
week: YYYY-WNN
tags: [synthese, algorithme, recap-hebdo, <piliers couverts>]
status: draft
sources_count: N
---

# Récap semaine NN — [titre punchy qui résume la semaine]

> Synthèse des N revues de presse Algorithme entre le YYYY-MM-DD et le YYYY-MM-DD.

## Tendance dominante

[1 paragraphe. La grosse histoire de la semaine, qui revient le plus. Voix Tim, position tranchée.]

## Pilier dominant : [SEO / IA / Contenu] — N% du volume

[2-3 phrases. Pourquoi ce pilier domine cette semaine, et ce que ça veut dire.]

## Ce qui fait consensus

- **[Assertion 1]** — confirmé par [source A], [source B]. (chiffre clé : X%)
- **[Assertion 2]** — confirmé par [source A], [source B]. (chiffre clé : X%)
…

## Ce qui fait débat

- **[Sujet]** — [Expert A] dit X, [Expert B] dit Y. Tim's take : [position de Tim si extractible des éditions, sinon "à trancher"].

## Signaux faibles à surveiller

- **[Signal 1]** — cité 1 fois mais important parce que [raison]. À creuser : [piste concrète].
- **[Signal 2]** — …

## Angles à creuser semaine prochaine

### Angle 1 : [titre provocateur]
**Pourquoi maintenant** : [tension du marché qui le justifie]
**Format suggéré** : [post LinkedIn / article / brief / nouvelle entité wiki]

### Angle 2 : [titre]
…

---

## Index des éditions de la semaine

- [[YYYY-MM-DD-revue-presse|YYYY-MM-DD]] — [titre court]
- [[YYYY-MM-DD-revue-presse|YYYY-MM-DD]] — [titre court]
…

---

*Récap auto-généré chaque dimanche soir à partir de `raw/revue-de-presse/`. Pour traiter les angles : ouvre wiki/queries/ et créé un brief, ou wiki/posts-linkedin/ pour un draft.*
```

## ÉTAPE 5 — RÉSUMÉ

Termine par :

```
Récap semaine NN — [titre punchy]
- Tendance : [phrase]
- Pilier dominant : [SEO/IA/Contenu] (N%)
- Angle prio à creuser : [titre angle 1]
```

## CONTRAINTES

- **Voix Tim** : pas de tournure "il convient de noter", pas de superlatifs creux. Tutoiement dans les apartés, vouvoiement pour le groupe.
- **Pas de copy-paste** : tu **synthétises**, tu ne re-cites pas le contenu des éditions in extenso. Densité > exhaustivité.
- **Chiffres précis** : si tu cites un chiffre dans une assertion consensus, vérifie qu'il vient bien des éditions parsées (pas d'invention).
- **Si moins de 5 éditions** : adapte la synthèse, n'invente pas pour combler.
- **Pas de redondance** avec la dernière édition** : la synthèse doit apporter un angle transversal, pas répéter l'édition du jour.
