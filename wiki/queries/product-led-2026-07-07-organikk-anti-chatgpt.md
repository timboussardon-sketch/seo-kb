---
type: query
title: "Organikk : modèles de pages anti-ChatGPT (clic obligatoire)"
aliases: [organikk-anti-chatgpt, product-led-organikk-2026-07]
tags: [organikk, product-led, anti-chatgpt, geo, mots-cles-decisionnels, pseo]
created: 2026-07-07
updated: 2026-07-07
sources: 3
confidence: medium
status: stale
updated: 2026-08-07
---

# Organikk : modèles de pages anti-ChatGPT

> Passé `stale` le 2026-08-07 ([[revue-hebdo/2026-W32]] point 5), même bascule et même date de mort que [[queries/pseo-2026-07-07-organikk-corpus]] — voir cette page pour le détail de la décision.

Skill `seo-product-led-seo`, suite de [[queries/pseo-2026-07-07-organikk-corpus]] (itérations 1-3 écartées ou partielles). Filtre appliqué : la doctrine anti-ChatGPT de Tim. Aucun mot-clé sur lequel ChatGPT peut se mettre ; il reste les requêtes où le clic est obligatoire. Trois familles survivantes : transactionnel ultra-niché, outil sur data propriétaire, preuve vérifiable.

Rappel data : les AI Overviews se déclenchent sur ~91 % des requêtes informationnelles et 2 à 10 % des transactionnelles (Semrush, échantillon 10 M de mots-clés, cité dans l'article mots-clés du blog). La GSC Organikk montre déjà des impressions transactionnelles non servies : « bootcamp seo » (34 imp, pos 30,4), « agence seo b2b » (29 imp, pos 37), « simulateur roi du seo » (6 imp, pos 40).

## Famille A : transactionnel ultra-niché (le clic est l'achat)

Le chercheur veut un prestataire, un programme ou un créneau, pas une explication. ChatGPT peut décrire un audit, il ne peut pas l'exécuter ni se vendre à la place de Tim.

Modèle : **1 page offre par livrable nommé**, avec périmètre exact, délai, livrable montré (extrait réel anonymisé), preuve chiffrée, point de conversion unique.

| Page | Requêtes visées | Signal existant |
|---|---|---|
| Audit GEO 48h (livrable montré) | audit geo, audit citations ia, audit seo ia | CTA « audit 48h » déjà sur le site, sans page dédiée requêtable |
| Bootcamp Claude Code SEO | bootcamp seo, formation claude code seo, formation seo ia | « bootcamp seo » 34 imp pos 30,4 : la demande existe, la page ne rank pas |
| Setup système Claude + Obsidian (0 à 1) | installer claude code seo, second cerveau seo, setup obsidian seo | wording « 0 à 1 puis autonomie » déjà vendu en call |
| Sprint maillage interne | prestation maillage interne, audit maillage | décline leenq + skill maillage |
| Accompagnement async (Loom + WhatsApp) | consultant seo async, accompagnement seo à distance | process commercial déjà 100 % async |

## Famille B : outils sur data propriétaire (le clic est l'usage)

Garde-fou anti-cannibalisation : Fusionn est la plateforme d'outils gratuits. Les outils Organikk restent des démos courtes qui vendent Tim et renvoient vers Fusionn pour la version connectée.

Les 5 concepts (pipeline du skill) :

| Solution Produit | Micro-intention « Do » | Surprise Gap | Confidence Score (preuves) | Action de conversion |
|---|---|---|---|---|
| Détecteur d'AI writing FR : colle ton texte, score contre la checklist Tim | « détecter texte ia », « humaniser un texte ia pour le seo » | Checklist éditoriale FR terrain (mots bannis, patterns Wikipedia, fragments), pas un score de perplexité générique | Checklist déjà éprouvée sur toutes les prods Organikk/clients | Rapport complet par email → accompagnement rédaction |
| Testeur de requête mangée : tape un mot-clé, verdict « l'IA mange ou pas » + variantes qui gardent le clic | « mot-clé mangé par l'ia », « requête qui ramène du clic » | Méthode requête-cliquable-vs-clic + data zéro-clic par intention (l'outil statique existe, on le rend interactif) | Data Semrush/SparkToro déjà sourcée sur /outils/zero-clic-par-intention | Liste complète de variantes par email → recherche mots-clés |
| Analyseur d'export GSC dans le navigateur : upload CSV, quick wins 3-15 + cannibalisation | « analyser export search console », « quick wins gsc » | Seuils et méthode des skills quick-win et cannibalisation | Cas Golfiller mesuré (analyse 90 j) | « Fais-le tourner chaque mois » → article workflow + Fusionn pour la version connectée |
| Scoreur de passage citable : colle un passage + la requête, score answer-first et densité de preuves | « être cité par les ia », « optimiser un passage » | Grille geo-audit (2 preuves/100 mots, réponse < 30 mots après le titre) | Upgrade de /outils/analyse-geo (8 imp pos 13,6 : proche du top 10) | Audit GEO 48h |
| Générateur de brief anti-IA : requête → structure Hn + entités à couvrir | « générer un brief seo avec l'ia », « brief éditorial seo » | Pipeline seo-brief-contenu (vecteurs attendus, ce que les concurrents n'ont pas dit) | Briefs déjà livrés en prestation | Brief complet par email → prestation contenu |

## Famille C : la preuve vérifiable (le clic est la vérification)

Sur « exemple de site qui ranke sans backlink » ou « cas seo chiffré », ChatGPT génère des cas plausibles mais invérifiables. Une capture GSC datée ne se génère pas. Modèle : galerie de cas avec la preuve à l'écran (Golfiller devant les sites majeurs sur « balle de golf », data à l'appui). Petit volume, mais chaque visite est un prospect chaud, et c'est la seule famille qui fabrique des citations IA en plus des clics (les moteurs citent ce qu'ils ne peuvent pas produire).

## Priorisation

1. **Bootcamp + audit GEO en pages offre (famille A)** : la demande est déjà dans la GSC, aucune page ne la sert, coût = 2 pages.
2. **Testeur de requête mangée (famille B)** : l'outil incarne la doctrine, la data est déjà sur le site, et chaque résultat démontre l'expertise mieux qu'un argumentaire.
3. **Détecteur d'AI writing FR** : la requête est grosse et l'angle FR terrain est vide.
4. Famille C en flux, une preuve à la fois.

Règle du skill à respecter : tester chaque outil en MVP avant d'investir, version agent-friendly (endpoint JSON) pour l'Agentic SEO.

Liens : [[queries/pseo-2026-07-07-organikk-corpus]] · [[concepts/requete-cliquable-vs-clic]] · [[concepts/product-led-seo]] · [[concepts/test-substitution-llm]] · [[concepts/know-simple-know-do]]
