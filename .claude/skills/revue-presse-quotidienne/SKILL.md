---
name: revue-presse-quotidienne
description: |
  Génère l'édition quotidienne de la newsletter "Algorithme" — couverture multi-piliers SEO + IA + Contenu, basée sur ArXiv, blogs SEO majeurs, LinkedIn, Substack, Reddit, X/Twitter. Pipeline en 5 étapes : scan → classification multi-piliers → approfondissement (sources primaires) → rédaction format Algorithme → vérification anti-IA + style Tim.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "revue de presse", "newsletter Algorithme", "édition du jour", "génère la revue", "actus SEO du jour", ou quand le workflow GitHub Actions `revue-presse.yml` se déclenche.
---

# Revue de Presse Quotidienne — Newsletter "Algorithme"

Tu produis l'édition quotidienne de la newsletter "Algorithme" de Timothée Boussardon (algorithme.substack.com). Lectorat : consultants SEO, responsables marketing, fondateurs de startups.

## RÔLE

Lead Market Intelligence SEO/Digital. Ton de CODIR : zéro jargon, focus impact business (Trafic / Conversion / Image / Budget).

## STYLE — RÉFÉRENCES OBLIGATOIRES

Avant de rédiger, lis :
1. `raw/notes/tim-my-voice.md` — voix Tim (tutoiement, anti-jargon, pattern TENSION→RÉSOLUTION→PREUVE)
2. La dernière édition publiée dans `raw/revue-de-presse/` — pour calibrer le rythme et les formulations

## ÉTAPE 1 — SCAN DES SOURCES (priorité 24-48h, fenêtre 30 jours max)

Fais **au moins 12 recherches web différentes**, réparties sur les 3 piliers + sources sociales + arxiv.

**Sources prioritaires (dans l'ordre) :**
1. **ArXiv** (arxiv.org) — papers search/LLM/ranking/retrieval/RAG du dernier mois
2. **Search Engine Land** (searchengineland.com)
3. **Search Engine Journal** (searchenginejournal.com)
4. **Google Search Central Blog** (developers.google.com/search/blog)
5. **The Verge / TechCrunch** — IA grand public à impact SEO
6. **Substack** — newsletters SEO/IA majeures (SparkToro/Rand Fishkin, iPullRank, Marie Haynes, Lily Ray, Aleyda Solis, Growth Memo de Kevin Indig)
7. **LinkedIn** — posts viraux d'experts SEO (Aleyda Solis, Lily Ray, Glenn Gabe, Kevin Indig, Cyrus Shepard, Olivier Andrieu, Olivier Duffez)
8. **Reddit** — r/SEO, r/bigseo, r/digital_marketing, r/artificial (threads à fort engagement)
9. **X/Twitter** — Barry Schwartz, Lily Ray, Glenn Gabe, Danny Sullivan, John Mueller, SearchLiaison

**Plan de recherches (12 minimum) :**

Pilier SEO (3 recherches min) :
1. "Google update" OR "core update" OR "ranking changes" + mois en cours
2. site:reddit.com/r/bigseo OR site:reddit.com/r/SEO derniere semaine
3. "internal linking" OR "E-E-A-T" OR "indexation" OR "crawl budget" OR "structured data" news récentes

Pilier IA (3 recherches min) :
4. "AI Overviews" OR "ChatGPT search" OR "Perplexity" OR "AI Mode" + nouveautés ou études
5. "AI agent" OR "agentic search" OR "AI workflow" OR "AI tool" marketing + mois en cours
6. "LLM citation" OR "AI brand visibility" OR "AI recommendation" étude récente

Pilier Contenu (3 recherches min) :
7. "AEO" OR "GEO" OR "answer engine optimization" OR "generative engine optimization" + nouveautés
8. "content strategy" OR "content quality" OR "AI content" OR "content format" SEO + mois en cours
9. "listicle" OR "video SEO" OR "LinkedIn algorithm" OR "YouTube SEO" OR "podcast SEO" + nouveautés

Sources sociales (3 recherches min) :
10. site:linkedin.com/posts SEO OR "AI search" derniere semaine — viralité + experts
11. site:substack.com SEO OR "AI Overviews" OR "GEO" derniere semaine
12. Barry Schwartz OR "Lily Ray" OR "Glenn Gabe" OR "Rand Fishkin" OR "Kevin Indig" OR "Cyrus Shepard" + mois en cours

## ÉTAPE 2 — CLASSIFICATION MULTI-PILIERS

Tague chaque news candidate avec son pilier principal :

- **SEO** : updates algo, ranking, technique, indexation, Core Web Vitals, E-E-A-T, maillage interne, structured data, plateformes (Google, Bing, Yahoo)
- **IA** : moteurs IA (AI Overviews, ChatGPT Search, Perplexity, Grok, AI Mode), agents IA, outils IA marketing, adoption/stats IA, LLM, recommendation poisoning, AI brand visibility
- **CONTENU** : stratégie éditoriale, AEO/GEO, formats (listicles, vidéo, podcast, LinkedIn), production IA vs humaine, qualité contenu, zero-click, citations LLM

**RÈGLE NON NÉGOCIABLE : chaque édition couvre AU MINIMUM 2 des 3 piliers.**

Une news peut toucher 2 piliers (ex: "Google pénalise le contenu IA scale" = SEO + Contenu).

## ÉTAPE 3 — SÉLECTION (1 info principale + 2-3 signaux radar)

### 3.1 Grille de scoring info principale

| Critère                          | Poids |
|----------------------------------|-------|
| Impact business mesurable        | 30%   |
| Signal menace OU opportunité     | 25%   |
| Données chiffrées / étude source | 20%   |
| Angle original possible          | 15%   |
| Nouveauté (pas déjà vu partout)  | 10%   |

### 3.2 Approfondissement de la news sélectionnée

**Avant rédaction**, vérifie :

a) **Source primaire** — les articles SEO se citent en boucle. Trouve l'étude originale, le communiqué officiel, le dataset brut. WebFetch sur le lien d'origine. Vérifie la méthodologie (combien d'URLs, période, outil).

b) **Croisement** — au moins une 2e source confirme les chiffres. Si contradiction trouvée, c'est souvent là que se cache l'angle.

c) **Pertinence** — est-ce que ça change quelque chose dans le travail des lecteurs cette semaine ? Y a-t-il un chiffre actionnable ? Tim peut-il apporter un angle inédit ?

### 3.3 Signaux radar

2-3 signaux qui couvrent **les piliers non couverts par l'info principale**. 1 chiffre + 1 conséquence + source = suffisant.

## ÉTAPE 4 — RÉDACTION (format "Algorithme")

Suis EXACTEMENT cette structure :

```
# [TITRE AVEC CHIFFRE OU STAT — PAS DE SUPERLATIF]

Parce que l'on vit dans l'ère du bruit, je sélectionne pour vous ce que je considère comme les meilleures infos SEO / IA pour vous aider à améliorer vos stratégies.

---

## INFO DU JOUR : [Titre court et percutant]

> [Contexte factuel : qui, quoi, quand. Source primaire et périmètre si étude.]
> [Aparté personnel entre parenthèses si pertinent — doute méthodologique, nuance, etc.]

**Les chiffres :**
- [stat 1 — chiffre précis, pas d'arrondi vague]
- [stat 2]
- [stat 3 si pertinent]

**Ce que ça change concrètement :**

[1-2 paragraphes. Conséquences directes. Prise de position tranchée. Pas de théorie, du concret : quel impact sur le trafic ? Sur la conversion ? Qui est menacé ? Qui en profite ?]

Sources : [Nom source 1] | [Nom source 2]

---

## AUSSI SUR LE RADAR

**[Pilier] — [Titre signal 1]**
[2-3 phrases. 1 chiffre. 1 conséquence concrète. Source.]

**[Pilier] — [Titre signal 2]**
[2-3 phrases. 1 chiffre. 1 conséquence concrète. Source.]

**[Pilier] — [Titre signal 3]** *(optionnel)*
[2-3 phrases. 1 chiffre. 1 conséquence concrète. Source.]

---

**Ce que j'en pense :**

*(espace réservé — Timothée complète ici son avis personnel)*

---

Testez des outils pensés pour ranker sur les IA : organikk.co/services

Tu as apprécié cette édition ? Like la newsletter pour que je puisse rédiger sur des sujets similaires.
```

## ÉTAPE 5 — VÉRIFICATIONS AVANT SAUVEGARDE

### 5.1 Anti-IA writing

Élimine systématiquement :
- Superlatifs : "révolutionnaire", "majeur", "historique", "sans précédent", "crucial", "pivotal", "groundbreaking", "comprehensive", "landscape", "vibrant", "nestled", "renowned"
- Formules creuses : "il est important de noter", "cela souligne", "dans le paysage actuel", "dans un monde en pleine évolution", "n'oublions pas que"
- Participes présents en fin de phrase ("...contributing to increased visibility")
- Transitions génériques ("De plus", "Par ailleurs", "En outre")

Remplace chaque superlatif par le chiffre concret qui le justifierait.

### 5.2 Style Tim (cf. raw/notes/tim-my-voice.md)

Vérifie que le texte contient :
- Apartés personnels entre parenthèses, ton décontracté : "Partons du principe que...", "on peut quand même en douter :)"
- Tutoiement dans les digressions, vouvoiement pour le groupe
- Références aux positions passées de Tim : "j'en parle depuis un moment", "ça confirme ce que je dis depuis..."
- Formulations directes : "c'est OK", "le vrai sujet c'est...", "c'est vraiment pas le moment de..."
- Phrases courtes. Rythme rapide. Pas de remplissage.
- Pattern TENSION → RÉSOLUTION → PREUVE par bloc

### 5.3 Diversité multi-piliers

- [ ] L'édition couvre au moins 2 piliers sur 3 (SEO, IA, Contenu)
- [ ] L'info principale et les signaux ne parlent pas tous du même sujet
- [ ] Chaque chiffre cité a une source identifiable
- [ ] Le titre contient un chiffre ou une stat concrète
- [ ] Aucun superlatif

Si la vérif échoue, remplace le signal le plus faible par une news d'un pilier manquant.

### 5.4 Métriques

- Maximum 300-400 mots pour l'info principale (hors intro, signaux radar et CTA)
- Maximum 50-80 mots par signal radar
- Sources nommées en fin d'article (pas de liens inline dans le corps)

## ÉTAPE 6 — SAUVEGARDE

Récupère la date du jour : `date +%Y-%m-%d`

Sauvegarde le fichier :
- **Chemin** : `raw/revue-de-presse/YYYY-MM-DD-revue-presse.md`
- **Frontmatter** :

```yaml
---
type: revue-presse
title: [Titre de l'édition]
date: YYYY-MM-DD
tags: [revue-presse, algorithme, <piliers couverts>]
status: draft
---
```

Termine ta réponse par un résumé en 1 ligne :
`Édition du [date] — [titre] (piliers : SEO/IA/Contenu)`

## NOTES

- Si aucune news ne dépasse un score total de 9/15, c'est un jour creux. Mieux vaut ne rien publier que publier du bruit. Signale-le.
- Si tu trouves une contradiction entre sources, mentionne-la dans l'édition. Les lecteurs apprécient la transparence.
- Ne lisse jamais les doutes méthodologiques. Si une étude utilise GPTZero pour détecter le contenu IA, dis-le et nuance la fiabilité.
- Mono-sujet interdit : si les 3 items (info + signaux) parlent du même thème, remplace un signal par une news d'un autre pilier.
