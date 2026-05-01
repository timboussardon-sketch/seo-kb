# Victoria Garden — Cas client

## Sources

- Scrap site : https://victoriagarden.com — 2026-04-13
- Stratégie pSEO : `~/Library/Application Support/Claude/local-agent-mode-sessions/.../strat-victoria-garden-pseo.md` (livré par Claude Code, 2026-04-13)

---

## Résumé activité (scrap site 2026-04-13)

### Type d'entreprise & secteur

Chaîne hôtelière spécialisée dans les **appartements-hôtels** (« appart'hôtels »).
Promesse : *"le confort d'un hôtel et la liberté d'un appartement"*.

### Produits / services

- Studios et appartements équipés de **kitchenettes**
- Petits-déjeuners inclus
- Services hôteliers essentiels (ménage, accueil, stationnement)
- Offres dédiées séjours professionnels et vacances

### Tarification & modèle économique

Trois formules :
- **Tarif Flexible Liberté** — annulable jusqu'à 24h avant
- **Tarif Prépayé** — −10%
- **Séjours longs** (dès 4 nuits) — −20%

Prix d'entrée : à partir de **55 €** (Pau) et **72 €** (Bordeaux).

### Présence géographique

**2 destinations** : Bordeaux et Pau (sud-ouest France).

### Cible client

- Couples, familles, groupes
- Voyageurs professionnels
- Séjours courts ET longs
- Clientèle acceptant les animaux de compagnie

### Positionnement marketing

Tagline : *"Le dépaysement n'a jamais été aussi proche"*.
Accent éditorial sur expériences locales (vignobles, musées, activités outdoor).

### Signaux de marque

- Date de fondation non visible sur le site
- Partenaires affichés : **BPI France**, **YouCare**, **Énergie d'ici**
- Contenu : blog, FAQ, manifesto
- Site multilingue : FR, EN, ES

### Structure du site

Sections principales : Destinations · Services · Offres spéciales · Entreprises / Groupes · À propos (Manifesto, Blog, FAQ)

---

## Stratégie pSEO Bordeaux (livrée 2026-04-13)

**Cible du livrable** : Victoria Garden Bordeaux uniquement (la stratégie ne couvre pas Pau).
**Auteur** : Claude Code session 2026-04-13.
**Confidence** : haute.
**Status** : actif.

### Contexte client

Résidence appart-hôtel à Bordeaux. Positionnement entre hôtel classique et location courte durée. Cible : voyageurs d'affaires, familles, séjours moyens (3-14 nuits).

**Problème** : pages statiques classiques = commodité. Les LLM peuvent générer les mêmes réponses. Aucun avantage défensif.

### Test de substitution LLM (méthode propriétaire)

Méthode : pour chaque idée de page, demander à un LLM de produire la même réponse. Si la réponse LLM est équivalente → la page n'a pas de valeur défensive.

| Idée testée | Substituable ? | Verdict |
|---|---|---|
| Calculateur budget séjour | Non — données prix réelles + dispo temps réel | Validé |
| Simulateur configuration hébergement | Non — stock réel + contraintes métier | Validé |
| Comparateur coût total séjour | Non — pricing propriétaire vs données marché | Validé |
| Planificateur séjour thématique | Non — partenariats locaux + dispo réelle | Validé |
| Calendrier événements Bordeaux | Partiellement — mais données locales + offres liées | Validé (avec données propriétaires) |
| Guide quartiers Bordeaux | Oui — tout LLM peut le faire | Rejeté |
| FAQ hébergement générique | Oui — zéro data propriétaire | Rejeté |

**Règle** : si un LLM peut produire 80 % de la page → ne pas la créer.

### Modèle 1 — Calculateur Budget Séjour

**Concept** : outil interactif où l'utilisateur entre durée + nombre de personnes + type de séjour → obtient un budget détaillé avec prix réels Victoria Garden vs alternatives.

**Variable** : type de séjour (affaires, famille, couple, groupe, longue durée…)
**Pages générées** : ~12 pages

**Mots-clés cibles**

| Mot-clé | Volume | Intention | Difficulté |
|---|---|---|---|
| budget séjour bordeaux | 320/mois | Do | Moyenne |
| coût hébergement bordeaux par nuit | 210/mois | Know | Faible |
| prix appart hotel bordeaux | 480/mois | Do | Moyenne |
| calculer budget vacances bordeaux | 140/mois | Do | Faible |

**Données propriétaires requises**
- Grille tarifaire réelle Victoria Garden (par saison, par type)
- Coûts annexes moyens (parking, petit-déj, ménage)
- Benchmark prix hôtels / Airbnb Bordeaux (scraping ou partenariat data)

**Score Fully Meets** : l'utilisateur obtient un chiffre personnalisé, pas une fourchette générique. C'est la définition de Fully Meets pour une requête Do.

**Wireframe**
```
┌─────────────────────────────────────┐
│  CALCULATEUR BUDGET SÉJOUR BORDEAUX │
├─────────────────────────────────────┤
│ Durée : [___] nuits                 │
│ Personnes : [___]                   │
│ Type : [Affaires ▼]                 │
│ Saison : [Été ▼]                    │
│                                     │
│ [CALCULER MON BUDGET]               │
├─────────────────────────────────────┤
│ Budget estimé : XXX €               │
│                                     │
│ Détail :                            │
│ • Hébergement VG : XXX €            │
│ • vs Hôtel equiv. : XXX € (+XX%)    │
│ • vs Airbnb equiv. : XXX €          │
│                                     │
│ Économie estimée : XXX €            │
│                                     │
│ [VOIR DISPONIBILITÉS]   [RÉSERVER]  │
└─────────────────────────────────────┘
```

### Modèle 2 — Simulateur Configuration Hébergement

**Concept** : l'utilisateur décrit son besoin (nombre, contraintes, préférences) → le simulateur recommande la configuration idéale parmi le stock réel.

**Variable** : profil voyageur (famille 2 enfants, couple, groupe 6, PMR, animal…)
**Pages générées** : 8-10 pages

**Mots-clés cibles**

| Mot-clé | Volume | Intention | Difficulté |
|---|---|---|---|
| appart hotel bordeaux famille | 390/mois | Do | Moyenne |
| hébergement bordeaux groupe | 170/mois | Do | Faible |
| location bordeaux PMR accessible | 90/mois | Do | Faible |

**Données propriétaires requises**
- Inventaire réel des configurations (T1, T2, T3, capacités)
- Équipements par type (cuisine, parking, PMR, animaux)
- Disponibilités temps réel (API ou export régulier)

### Modèle 3 — Comparateur Coût Total Séjour

**Concept** : tableau interactif comparant le coût TOTAL (hébergement + repas + transport + activités) entre Victoria Garden, hôtel classique et Airbnb pour un même séjour.

**Variable** : durée de séjour (3, 5, 7, 10, 14 nuits)
**Pages générées** : ~6 pages

**Mots-clés cibles**

| Mot-clé | Volume | Intention | Difficulté |
|---|---|---|---|
| comparatif hébergement bordeaux | 260/mois | Know | Moyenne |
| appart hotel ou airbnb bordeaux | 210/mois | Know | Faible |
| hôtel vs location bordeaux prix | 150/mois | Know | Faible |

**Données propriétaires requises**
- Coûts repas moyens (restaurant vs cuisine sur place)
- Coûts transport par zone
- Prix activités / visites principales Bordeaux
- Pricing concurrence (hôtels 3★, Airbnb médian)

**Wireframe — Tableau Interactif**
```
┌──────────────────────────────────────────────────┐
│     COÛT TOTAL : 7 NUITS À BORDEAUX (2 pers.)    │
├──────────────┬──────────┬──────────┬─────────────┤
│              │ VG       │ Hôtel 3★ │ Airbnb      │
├──────────────┼──────────┼──────────┼─────────────┤
│ Hébergement  │ 630 €    │ 840 €    │ 700 €       │
│ Repas        │ 180 €    │ 350 €    │ 200 €       │
│ Parking      │ Inclus   │ 105 €    │ 70 €        │
│ Ménage       │ Inclus   │ —        │ 60 €        │
├──────────────┼──────────┼──────────┼─────────────┤
│ TOTAL        │ 810 €    │ 1 295 €  │ 1 030 €     │
│ Économie     │ —        │ +60%     │ +27%        │
└──────────────┴──────────┴──────────┴─────────────┘
```

### Modèle 4 — Planificateur Séjour Thématique

**Concept** : l'utilisateur choisit un thème (vin, gastronomie, famille, sport) → planning jour par jour avec activités locales + offre Victoria Garden associée.

**Variable** : thématique (vin, gastronomie, famille, culture, sport)
**Pages générées** : ~4 pages

**Données propriétaires requises**
- Partenariats locaux (caves, restaurants, activités)
- Offres packages Victoria Garden
- Calendrier événements par thématique

### Modèle 5 — Calendrier Événements Bordeaux

**Concept** : page dynamique listant les événements à Bordeaux avec offres hébergement Victoria Garden associées à chaque événement.

**Variable** : mois/saison
**Pages générées** : 1 page principale + variantes saisonnières

**Mots-clés cibles**

| Mot-clé | Volume | Intention | Difficulté |
|---|---|---|---|
| événements bordeaux 2026 | 1 200/mois | Know | Moyenne |
| agenda bordeaux ce week-end | 2 400/mois | Know-Simple | Forte |
| que faire bordeaux [mois] | 800/mois | Know | Moyenne |

**Données propriétaires requises**
- Base événements (office de tourisme + veille manuelle)
- Offres spéciales Victoria Garden par événement
- Taux d'occupation historique par événement (pour pricing dynamique)

### Priorisation et plan 90 jours

**Phase 1 — Semaines 1-4 : Fondations**
- Calculateur Budget Séjour (Modèle 1) — impact SEO + conversion le plus immédiat
- Collecte données pricing (VG + concurrence)
- Développement composant interactif

**Phase 2 — Semaines 5-8 : Comparaison**
- Comparateur Coût Total (Modèle 3) — renforce l'argumentaire prix
- Calendrier Événements (Modèle 5) — volume de recherche élevé
- Enrichissement données locales

**Phase 3 — Semaines 9-12 : Personnalisation**
- Simulateur Configuration (Modèle 2) — conversion directe
- Planificateur Séjour (Modèle 4) — fidélisation + cross-sell
- Maillage interne entre tous les outils

### Pages déjà livrées par Claude Code

- `budget-sejour-bordeaux` — calculateur interactif (Modèle 1)
- `agenda-evenements-bordeaux-2026` — calendrier événements (Modèle 5)
- `comparatif-hebergement-bordeaux` — tableau comparatif (Modèle 3)
