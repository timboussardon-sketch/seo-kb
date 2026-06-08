---
type: etude
source_type: first-party
title: "Pilote — Ce que les SEO tapent vraiment dans un outil (logs Fusionn)"
aliases: ["pilote logs fusionn", "etude requetes seo fusionn"]
tags: ["etude-originale", "first-party", "fusionn", "requetes", "intention", "data-interne"]
created: 2026-06-02
updated: 2026-06-02
sources: ["Fusionn — table search_history (lecture service role)"]
confidence: faible
status: pilote
echantillon: 146
periode: "2026-05-21 → 2026-06-02 (12 j)"
---

# Pilote — Ce que les SEO tapent vraiment dans un outil (logs Fusionn)

> **Nature** : étude originale first-party (data propriétaire [[entities/fusionn-io|Fusionn]]), pas un digest de paper externe. C'est de la [[concepts/data-proprietaire|data propriétaire]] transformée en asset GEO.
> **Statut** : PILOTE. Non publiable en l'état (N trop faible, période trop courte, biais audience/comptes internes non purgés).
> **Pourquoi cette étude** : la data originale ou propriétaire est le 2e prédicteur de citation par ChatGPT (Search Engine Land, 19 nov. 2025). Produire nos propres études = contenu partageable + asset GEO. Voir aussi la veille du 13 mai 2026 (étude Lily Ray sur le risque du contenu IA).

## Méthodo

- **Source** : table `search_history` de Fusionn (projet Supabase `fwhfnzbtlddzfxbsejyf`), lecture seule via service role.
- **Champs** : `keyword`, `search_mode`, `view_type`, `created_at`, `user_id`.
- **Échantillon** : 146 recherches, 34 utilisateurs distincts, du 2026-05-21 au 2026-06-02 (12 j).
- **Intention** : heuristique lexicale sur la requête tapée (marqueurs décisionnels vs informationnels), pas une classification SERP. À considérer comme indicatif.
- **Heures** : relevées en UTC (non recalées Paris).
- **Limites assumées** : voir section « Biais ».

## Résultats bruts

**Volume / usage**
- 146 recherches, 34 users, 12 j → 12,2 recherches/jour, 4,3 par user en moyenne.
- Répartition par user : 47,1 % font 1 seule recherche, 38,2 % en font 2-3, 8,8 % font 11+. Médiane = 2. Max = 27 (un seul compte).

**Longueur des requêtes**
- Moyenne : 3,42 mots.
- 1 mot : 2,7 % · 2 mots : 46,6 % · 3 mots : 25,3 % · 4 mots : 6,8 % · 5 mots : 2,7 % · 6+ : 15,8 %.
- **78,5 % des requêtes font 3 mots ou moins.**

**Intention (heuristique lexicale)**
- Marqueur décisionnel/business (prix, agence, consultant, comparatif, ville…) : **41,1 %**.
- Marqueur informationnel (comment, pourquoi, guide, définition…) : **5,5 %**.
- Sans marqueur (neutre) : 53,4 %.

**Rythme**
- Par jour : jeudi 23,3 % + vendredi 23,3 % = **46,6 % sur 2 jours**. Dimanche 3,4 %.
- Par heure (UTC) : activité concentrée 05h-15h, creux le soir. Outil de jour ouvré.

**Premier onglet ouvert (`view_type`)**
- table (clusters) 87,0 % · youtubeKeywords 6,2 % · redditKeywords 2,7 % · reste < 2 % chacun.

**Mode de recherche**
- site 97,3 % · keyword 2,7 %. (Artefact, voir biais.)

**Top thèmes (mots, hors stopwords)**
- seo 39, consultant 24, agence 18, formation 15, b2b 11, copywriting 10, logiciel 8, crm 7, paris 7, geo 7.

## Lecture : signaux vs artefacts

**Vrais signaux (robustes, indépendants du produit)**
- **Brièveté** : 78,5 % des requêtes ≤ 3 mots. Solide.
- **Décisionnel >> informationnel** (41 % vs 5,5 %). Colle à la doctrine [[mots-cles-decisionnels]] : qui ouvre un outil SEO chasse du business, pas de la définition. Angle le plus exploitable.
- **Cadence jour ouvré** (jeu+ven = 47 %). Intéressant mais N faible.

**Artefacts à ne pas publier tels quels**
- **Mode site 97 %** : c'est le mode par défaut de l'UI, pas un choix. Ne rien en conclure.
- **Top thèmes (seo, consultant, agence)** : biais d'audience. Les users actuels sont des SEO, dont le compte interne le plus actif (27 recherches). Ça mesure l'audience, pas le marché.
- **N = 146 / 12 j** : pilote, pas étude. Un chiffre se retourne avec 10 recherches de plus.

## Verdict

Non publiable en l'état. À transformer en **baromètre récurrent** (trimestriel) une fois réunies les conditions ci-dessous.

## Conditions pour en faire une vraie étude

1. **Volume** : viser quelques milliers de recherches (idéalement 2 000+).
2. **Purge** : exclure les comptes internes / test (mywaymalte, tim.boussardon, etc.) avant calcul.
3. **Période gelée** : fenêtre fixe et annoncée (ex. un trimestre plein).
4. **Heures recalées** Europe/Paris.
5. **Intention** : si on garde l'heuristique, l'afficher comme telle ; sinon classer via SERP.
6. **Diffusion** : page dédiée optimisée GEO (l'asset citable) + post, pas qu'un screenshot.

## Suite

- Première étude **publiable** prioritaire : CTR réel × présence d'AI Overviews sur les 20+ propriétés GSC (data volumineuse et non biaisée, créneau Lily Ray en FR). Voir [[etude-ctr-ai-overviews-gsc]] (à créer).
- Garder ce pilote comme protocole du futur baromètre « Ce que les SEO analysent vraiment ».

## Requête de reproduction

Données tirées le 2026-06-02 via un script Node ad hoc (fetch REST + service role sur `search_history`, pagination 1000, agrégations en JS). Reproductible en relançant la même extraction sur une fenêtre gelée.
