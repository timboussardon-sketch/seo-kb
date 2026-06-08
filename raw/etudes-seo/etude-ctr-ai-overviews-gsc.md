---
type: etude
source_type: first-party
title: "Protocole — CTR réel × AI Overviews sur portefeuille GSC (FR)"
aliases: ["etude ctr ai overviews", "ctr aio gsc", "barometre ctr aio"]
tags: ["etude-originale", "first-party", "gsc", "ctr", "ai-overviews", "sge", "protocole"]
created: 2026-06-02
updated: 2026-06-02
sources: ["GSC — table google_connections (53 propriétés connectées via Fusionn)", "edge function gsc-fetch / _shared/gsc.ts"]
confidence: moyenne
status: niveau-1-chiffré
echantillon: "23 propriétés exploitables · 9 798 requêtes · 1,76M impressions · 29 628 clics"
periode: "2026-03-01 → 2026-05-30 (90 j)"
---

# Protocole — CTR réel × AI Overviews sur portefeuille GSC (FR)

> **Nature** : étude originale first-party, data [[entities/gsc|GSC]] propriétaire (portefeuille de sites connectés à [[entities/fusionn-io|Fusionn]]). Alimente nos [[concepts/metriques-visibilite-geo|métriques de visibilité GEO]] : le CTR réel face aux [[entities/sge|AI Overviews]] est une mesure maison du créneau.
> **Statut** : PROTOCOLE prêt. Aucune donnée extraite à ce jour (voir « Exécution »). Aucun chiffre n'est avancé tant que l'extraction n'est pas faite.
> **Pourquoi** : créneau Lily Ray (« It works until it doesn't ») mais en **français** et avec **du clic réel**, là où personne ne chiffre. La data first-party est le 2e prédicteur de citation par ChatGPT, donc l'étude est aussi un asset GEO. Voir [[2026-06-02-pilote-logs-fusionn-ce-que-les-seo-tapent]] pour le pilote précédent.

## Le point dur méthodo (à régler avant tout)

**GSC ne dit PAS si une requête a déclenché un AI Overview.** L'API Search Console ne contient aucun champ « AIO présent ». On ne peut donc pas, avec GSC seul, faire un « CTR avec AIO vs sans AIO ». Toute étude qui prétend le faire à partir de GSC seul ment ou bricole. Il faut un **signal externe de présence d'AIO par requête**.

Conséquence : on découpe en deux niveaux.

## Niveau 1 — Publiable avec GSC seul (à faire en premier)

**Question** : à quoi ressemble la courbe de CTR réel par position en 2026, sur un vrai portefeuille FR, et comment a-t-elle bougé ?

- **Métrique** : CTR moyen pondéré par les impressions, par bucket de position (1, 2, 3, 4-5, 6-10, 11-20).
- **Comparaison** : vs les courbes publiques de référence (Advanced Web Ranking, GSC historiques). L'angle « le CTR position 1 en 2026 sur nos sites » suffit à se faire citer.
- **Segmentation** : par type d'intention (Know vs Do, via marqueurs de requête), et par type de site (éditorial vs transactionnel).
- **Déjà publiable seul.** N'attend pas le Niveau 2.

### Résultats — extraction du 2026-06-02

**Périmètre** : 31 propriétés connectées, 29 répondent, **23 avec data exploitable**. Fenêtre **2026-03-01 → 2026-05-30 (90 j)**, `dataState: final`. Filtres : requêtes branded exclues (184), seuil ≥ 30 impressions (46 574 requêtes longue traîne écartées). Reste : **9 798 requêtes, 1 755 778 impressions, 29 628 clics**. CTR pondéré par impressions.

**Composition** : portefeuille multi-secteurs (e-commerce, services, formation, traduction, immobilier…), majoritairement FR mais pas pur FR (présence de sites .mg Madagascar et de sites de traduction DE/multilingue). Répartition saine : plus gros site = 15,4 % des impressions, top 3 = 41 %. À décrire tel quel, ne pas le vendre comme « 100 % FR ».

**CTR réel par position (global)** :

| Position | CTR | Impressions | Requêtes |
|---|---|---|---|
| 1 | **34,2 %** | 41 746 | 143 |
| 2 | 5,6 % | 38 518 | 183 |
| 3 | 4,6 % | 34 686 | 292 |
| 4-5 | 2,2 % | 180 750 | 857 |
| 6-10 | 0,9 % | 660 871 | 3 099 |
| 11-20 | 0,3 % | 425 902 | 2 442 |
| 21+ | 0,1 % | 373 305 | 2 782 |

**Le chiffre tête de gondole** : CTR position 1 = 34 %, puis **falaise immédiate à 5,6 % en position 2** (contre ~15 % sur les courbes publiques classiques). Tout ce qui n'est pas la 1re place est massivement sous-cliqué.

**Caveats à publier avec les chiffres** :
- Les positions 1-3 ne pèsent que ~6,5 % des impressions du portefeuille (ces sites rankent surtout en 6-21+). Le CTR pos1 repose donc sur une base plus étroite (143 requêtes), pondérée par quelques grosses requêtes.
- CTR pondéré impressions (somme clics / somme impressions par bucket), pas une moyenne de CTR ligne à ligne.
- Position = position moyenne GSC sur 90 j (une requête à « position 2,0 » a pu osciller entre 1 et 3).
- Le split **Do/Know est trop maigre côté Do** (bucket pos1 Do = 10 requêtes, bruité) : ne pas publier la courbe Do en l'état. La courbe **Know** (l'essentiel du volume) suit le global. Pour une vraie segmentation intention, élargir l'échantillon ou classer par SERP.
- La pos2 anormalement basse est un **constat, pas une explication**. Hypothèse à tester au Niveau 2 (features SERP / AIO qui écrasent tout sous la 1re place), sans l'affirmer.

**Reproduction** : edge function `admin-gsc-study` (repo newFusionn), `{ scope: 'all', days: 90, minImpressions: 30 }`. Sortie agrégée anonyme + détail perSite réservé au contrôle interne.

## Niveau 2 — CTR × AI Overviews (nécessite un signal AIO)

**Question** : sur les requêtes où un AIO est présent, de combien le CTR s'effondre vs requêtes équivalentes sans AIO ?

Options pour obtenir la présence d'AIO par requête (à choisir, par ordre de coût) :
1. **Échantillon manuel** : relever à la main la présence d'AIO sur un échantillon de N requêtes top-impressions (lent mais honnête, suffisant pour un premier chiffre).
2. **API SERP tierce** (DataForSEO, SerpApi…) qui expose le bloc AI Overview : fiable, payant, scalable.
3. **Proxy imparfait** : chute brutale de CTR à position stable + impressions stables comme indice indirect. À ne publier que clairement étiqueté « proxy », jamais comme mesure directe.

Règle : le Niveau 2 ne sort que si la source AIO est nommée et reproductible.

## Données disponibles

- **53 connexions GSC** dans `google_connections` (sites de Tim + sites clients), réparties sur plusieurs comptes utilisateurs Fusionn.
- Propriétés **Tim** exploitables sans souci de confidentialité : organikk.co, golfiller.fr, fusionn.io, bxble.com, qadence.io, epargnoo, tethys-education, etc.
- Propriétés **clients** : utilisables uniquement en **agrégé anonymisé** (jamais de nom de site/marque dans la sortie publiée).

## Extraction (spécification)

- **Via** `gsc-fetch` (refresh OAuth géré côté edge) ou requête `searchAnalytics.query` directe.
- **Dimensions** : `query` + `page` (et relevé de la position moyenne, clics, impressions).
- **Fenêtre** : gelée, ex. un trimestre plein 2026, `dataState: final`.
- **rowLimit** : élevé (plusieurs milliers) par propriété, paginé.
- **Filtres d'hygiène** :
  - exclure les requêtes **branded** (nom du site/marque).
  - exclure la **homepage** et les requêtes de navigation.
  - seuil d'impressions minimal par requête pour éviter le bruit (ex. ≥ 50 impressions sur la fenêtre).
- **Agrégation** : CTR pondéré impressions par bucket de position, jamais une moyenne de CTR brute (qui surpondère la longue traîne).

## Anonymisation et éthique

- Sortie publiée = **agrégat uniquement**, aucun nom de site client, aucune requête identifiante.
- Aucune marque, aucun concurrent nommé (cohérent [[feedback_pas_de_marques_directories_seo]]).
- Aucun chiffre inventé. Donnée manquante = annoncée comme manquante.

## Exécution (ce qu'il manque pour lancer)

**FAIT (2026-06-02)** : edge function **`admin-gsc-study`** créée et déployée (repo newFusionn, `supabase/functions/admin-gsc-study/`). Réservée aux ADMIN_EMAILS, avec bypass serveur-à-serveur si le bearer porte le claim `role: service_role`. Utilise `GOOGLE_CLIENT_ID/SECRET` (secrets edge) + service role sur `google_connections`, refresh OAuth par propriété, requête `searchAnalytics`, agrégation CTR-par-bucket pondérée impressions. Params : `scope` ('own' | 'all' | `sites[]`), `days`, `minImpressions`, `rowLimit`, `brandTerms`. Rejouable chaque trimestre = baromètre.

Le Niveau 1 est donc chiffré (voir « Résultats » ci-dessus). Reste à faire : le Niveau 2 (signal AIO).

## Sortie attendue

- Une page dédiée optimisée GEO (l'asset citable), pas qu'un post.
- 1-2 chiffres tête de gondole formulables en une phrase (ex. « CTR position 1 = X % sur N requêtes FR au T2 2026 »).
- Méthodo transparente affichée : N, période, filtres, source AIO si Niveau 2.

## Suite

- Trancher la source AIO (échantillon manuel pour démarrer).
- Construire l'edge function d'extraction admin (voie 1).
- Geler la fenêtre, lancer le Niveau 1, valider l'angle, puis enrichir Niveau 2.
