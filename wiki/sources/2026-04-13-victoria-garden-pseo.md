---
type: source
source_type: client-note
title: Stratégie pSEO — Victoria Garden Bordeaux
aliases: [victoria-garden-pseo, vg-bordeaux-strategy]
tags: [client-note, victoria-garden, bordeaux, appart-hotel, pseo, product-led, calculateur]
created: 2026-04-13
updated: 2026-04-13
sources: 1
confidence: high
status: stable
---

# Stratégie pSEO — Victoria Garden Bordeaux

**Client** : [[entities/victoria-garden]]
**Type** : note client / livrable stratégique (`source_type: client-note` — première source de ce type dans la KB)
**Fichier raw** : `raw/cas-clients/victoria-garden.md`
**Auteur livrable** : Claude Code session 2026-04-13
**Périmètre** : Victoria Garden Bordeaux uniquement (Pau hors scope)

---

## Contexte client

Résidence appart-hôtel à Bordeaux. Positionnement entre hôtel classique et location courte durée. Cible : voyageurs d'affaires, familles, séjours moyens 3-14 nuits.

**Problème identifié** : pages statiques classiques = commodité. Les LLM peuvent générer les mêmes réponses. Aucun avantage défensif.

## Méthode propriétaire — Test de substitution LLM

Avant de créer une page, demander à un LLM de produire la même réponse. Si la réponse LLM est équivalente → la page n'a pas de valeur défensive et n'est pas créée. Cf. [[concepts/test-substitution-llm]] (nouveau concept formalisé à partir de cette source).

**Règle** : si un LLM peut produire 80 % de la page → ne pas la créer.

### Application — 7 idées testées

| Idée | Substituable ? | Verdict |
|---|---|---|
| Calculateur budget séjour | Non — prix réels + dispo temps réel | Validé |
| Simulateur configuration hébergement | Non — stock réel + contraintes métier | Validé |
| Comparateur coût total séjour | Non — pricing propriétaire vs marché | Validé |
| Planificateur séjour thématique | Non — partenariats locaux + dispo | Validé |
| Calendrier événements Bordeaux | Partiellement — données locales + offres liées | Validé |
| Guide quartiers Bordeaux | Oui — tout LLM peut le faire | Rejeté |
| FAQ hébergement générique | Oui — zéro data propriétaire | Rejeté |

**5 validés / 2 rejetés.** Filtre net qui matérialise la doctrine [[concepts/data-proprietaire]] et [[concepts/surprise-gap]] en décision opérationnelle binaire.

## 5 modèles pSEO retenus

### Modèle 1 — Calculateur Budget Séjour

- **Variable** : type de séjour (affaires, famille, couple, groupe, longue durée)
- **Pages générées** : ~12
- **Mots-clés cibles** (volumes/intentions sourcés du livrable) :
  - "budget séjour bordeaux" — 320/mois — Do — moyenne
  - "coût hébergement bordeaux par nuit" — 210/mois — Know — faible
  - "prix appart hotel bordeaux" — 480/mois — Do — moyenne
  - "calculer budget vacances bordeaux" — 140/mois — Do — faible
- **Données propriétaires requises** : grille tarifaire VG par saison/type, coûts annexes (parking/petit-déj/ménage), benchmark concurrence Bordeaux
- **Connexion [[concepts/fully-meets]]** : l'utilisateur obtient un chiffre personnalisé, pas une fourchette générique → Fully Meets pour requête Do

### Modèle 2 — Simulateur Configuration Hébergement

- **Variable** : profil voyageur (famille 2 enfants, couple, groupe 6, PMR, animal)
- **Pages générées** : 8-10
- **Mots-clés** : "appart hotel bordeaux famille" (390/mois), "hébergement bordeaux groupe" (170/mois), "location bordeaux PMR accessible" (90/mois)
- **Données propriétaires** : inventaire configurations (T1/T2/T3), équipements par type, dispo temps réel

### Modèle 3 — Comparateur Coût Total Séjour

- **Variable** : durée séjour (3, 5, 7, 10, 14 nuits)
- **Pages générées** : ~6
- **Mots-clés** : "comparatif hébergement bordeaux" (260/mois), "appart hotel ou airbnb bordeaux" (210/mois), "hôtel vs location bordeaux prix" (150/mois)
- **Données propriétaires** : coûts repas (resto vs cuisine sur place), transport par zone, prix activités Bordeaux, pricing concurrence (hôtels 3★, Airbnb médian)

### Modèle 4 — Planificateur Séjour Thématique

- **Variable** : thématique (vin, gastronomie, famille, culture, sport)
- **Pages générées** : ~4
- **Données propriétaires** : partenariats locaux (caves, restaurants, activités), packages VG, calendrier événements par thématique

### Modèle 5 — Calendrier Événements Bordeaux

- **Variable** : mois/saison
- **Pages générées** : 1 page principale + variantes saisonnières
- **Mots-clés** : "événements bordeaux 2026" (1 200/mois), "agenda bordeaux ce week-end" (2 400/mois), "que faire bordeaux [mois]" (800/mois)
- **Données propriétaires** : base événements (office tourisme + veille manuelle), offres VG par événement, taux occupation historique

## Plan 90 jours

**Phase 1 (semaines 1-4)** : Calculateur Budget Séjour + collecte données pricing + dev composant interactif
**Phase 2 (semaines 5-8)** : Comparateur Coût Total + Calendrier Événements + enrichissement données locales
**Phase 3 (semaines 9-12)** : Simulateur Configuration + Planificateur Séjour + maillage interne

## Pages déjà livrées par Claude Code (état 2026-04-13)

- `budget-sejour-bordeaux` — calculateur interactif (Modèle 1)
- `agenda-evenements-bordeaux-2026` — calendrier événements (Modèle 5)
- `comparatif-hebergement-bordeaux` — tableau comparatif (Modèle 3)

3 pages livrées sur ~31 prévues à terme (12+10+6+4+1 selon les 5 modèles).

## Importance KB

Première **source `client-note`** de la KB. Première application opérationnelle complète du skill `seo-programmatique-pseo` + `seo-product-led-seo` sur un client réel. Le **test de substitution LLM** est un livrable méthodologique réutilisable au-delà de Victoria Garden — formalisé en [[concepts/test-substitution-llm]].

## Limites

- Volumes mots-clés affichés sans source explicite (probablement Semrush/Ahrefs interne — à confirmer)
- Pas de mesure de baseline trafic Victoria Garden Bordeaux avant pSEO
- Stratégie limitée à Bordeaux — équivalent Pau non documenté
- Résultats des 3 pages déjà livrées non encore mesurés (positions, trafic, conversions)
- Données propriétaires "requises" listées par modèle mais leur disponibilité actuelle côté client non spécifiée

## Pages liées

**Entity** : [[entities/victoria-garden]]

**Concepts** : [[concepts/test-substitution-llm]] · [[concepts/fully-meets]] · [[concepts/data-proprietaire]] · [[concepts/surprise-gap]] · [[concepts/grounding-score]]

**Skills mobilisés** (cf. [[sources/2026-04-12-tim-skills-seo-proprietary]]) : programmatique-pseo · product-led-seo · entites-vectorielles · quick-win · maillage-interne · cluster-aeo
