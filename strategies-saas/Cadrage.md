# Cadrage : SaaS « Bibliothèque de stratégies SEO/GEO »

> Nom de travail : à figer (shortlist plus bas). Statut : cadrage initial, 2026-06-28.

## En résumé

Un micro-SaaS qui fait pour le SEO/GEO ce que TrendTrack fait pour l'e-commerce, mais en retournant l'ADN : on ne track pas une marque à copier, on track un **pattern observable** sourcé. Chaque stratégie = une mécanique + sa preuve datée + un score Effort × Impact + « comment l'appliquer à ton site sans copier personne ». Alimenté par le flux Algorithme (SyntheticBrain), donc pas de crawler lourd à construire. Le produit ne publie rien seul : il propose des cartes en draft, Tim valide.

## Pourquoi ce pivot (vs cloner TrendTrack)

TrendTrack/Whoscale = « trouve qui gagne, copie la créa ». Logique extractive, orientée copie d'un acteur nommé. Ça entre en conflit frontal avec :

- La doctrine Bible : *Concurrence - business* (« tu ne prends rien, tu contribues »), *Business* (« l'Agapè crée la valeur chez l'autre »), *Capitalisme chrétien* (« fructifier, pas dominer »).
- Les règles SEO déjà posées : jamais de vol de contenu, pas de marques/concurrents nommés dans les contenus, doctrine de prod orientée contenu original (Surprise Gap).

Le pivot garde la promesse (« vois ce qui marche maintenant ») et change l'unité : un principe, pas une cible à dépouiller. On donne la mécanique, l'utilisateur crée sa propre valeur.

## Modèle de données : la carte stratégie

| Champ | Contenu |
|---|---|
| Titre | Description sèche de la mécanique (ton-de-voix-tim, pas de punchline) |
| Levier | technique / contenu / GEO-citation / maillage / pSEO / schema / fraîcheur |
| Mécanique | Ce qui marche, expliqué en clair |
| Preuve | Source primaire datée (doc Google, étude, capture AI Overview, étude first-party) |
| Fiabilité | 🟢 Confirmé / 🟡 Témoignage / 🟠 Débat / 🔵 Analyse |
| Statut | émergent / confirmé / en déclin |
| Fraîcheur | Date + signal de péremption (un pattern algo a une durée de vie) |
| Score | Effort × Impact → Priorité (grille Fusionn) |
| Application | « Comment tu le poses sur ton site », orienté contenu original |
| Sources | Bloc obligatoire, visible |

## Sources d'alimentation (tout public, jamais de back-office d'un acteur nommé)

1. Flux quotidien SyntheticBrain / Algorithme (déjà opérationnel)
2. Docs et changelogs Google / Chromium / brevets
3. Études publiques (Ahrefs, Cloudflare, Shopify…), datées et créditées
4. Observation directe AI Overviews / Perplexity / SearchGPT sur des clusters
5. Études first-party de Tim (`raw/etudes-seo/`) : la vraie différence

## Garde-fous éthiques (affichés dans le produit, pas cachés)

1. On track un pattern, jamais une marque nommée à copier.
2. Toute carte porte une source datée + bloc Sources visible.
3. L'action pousse vers du contenu original, jamais « copie cette page ».
4. Zéro donnée aspirée sans crédit, zéro volume inventé.
5. Terminologie GEO correcte partout.

## Architecture produit (hybride public / gated)

Le SaaS mange sa propre nourriture : chaque carte a une version publique indexable et citable (le tool qui ranke prouve les stratégies qu'il vend), et une profondeur réservée derrière auth.

- **Public (indexable, citable, capture email)** : titre, mécanique résumée, fiabilité, source, schema Dataset/Article. Sert l'autorité SEO/IA et l'acquisition.
- **Gated (payant)** : playbook d'application complet, score Effort × Impact, filtres avancés, feed quotidien des nouvelles cartes, export.

## Stack proposée

- **Front** : Next.js (App Router). Choisi pour le SSG/SSR : les cartes publiques doivent être indexables et citables par les IA. C'est le seul des repos de Tim où le SEO du produit lui-même compte.
- **Données + auth** : Supabase (réutilise l'écosystème Qadence/Fusionn).
- **Ingestion** : routine distante quotidienne qui drafte 1-2 cartes depuis le flux Algorithme. Validation humaine avant publication (même boucle que les brèves).
- **Deploy** : Netlify (cohérent avec Organikk/Fusionn).

## V1 (périmètre minimal)

1. Schéma Supabase `strategies` + RLS (lecture publique sur champs publics, gated sur le reste).
2. 20-30 cartes seed écrites à la main depuis le vault + flux Algorithme.
3. UI de consultation filtrable (levier / fiabilité / fraîcheur / priorité).
4. Pages publiques par carte (schema, bloc Sources).
5. Capture email + auth basique.
6. Routine de draft quotidien (proposition, pas publication auto).

## Décisions ouvertes

- Nom + domaine.
- Modèle de prix.
- Gratuit total au lancement (autorité d'abord) vs gated dès J0.
