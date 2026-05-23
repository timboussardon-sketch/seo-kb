---
name: pSEO Organikk — stratégie SEO {secteur} {ville}
date: 2026-05-13
type: pseo-strategy
status: phase-1-ready
template: src/app/blog/[slug]/page.tsx (figé)
deploy_target: src/data/articles.ts (organikk-next)
parent_articles:
  - strategie-seo-serrurier-lyon
  - strategie-seo-agence-immobiliere-lyon
---

# pSEO Organikk — Stratégie SEO {secteur} {ville}

## 0. Test de substitution LLM (obligatoire variante non-produit / éditorial)

**Question** : un LLM peut-il répondre "comment faire du SEO pour un serrurier à Lyon" sans lire mes pages ?

Réponse honnête : oui, mais avec une réponse *générique* (4 conseils plats : NAP, GBP, avis, contenu local). Mon avantage compétitif :

1. **Données terrain ville** : prix m² par arrondissement, volume de transactions, densité concurrentielle Google Maps comptée à la main, salaire médian INSEE
2. **Simulateur Product-Led** intégré (calcul de prix, estimation, audit gratuit) → LLM ne peut pas générer ça
3. **Inversions méthodologiques** propres à ma doctrine (Surprise Gap, Triade SERP, Algorithmic Authorship) que les LLM ne ressortent pas spontanément
4. **Authorship Organikk** (E-E-A-T) — la signature compte pour Quality Raters

→ Test passé. Le pSEO se justifie SI chaque page contient au moins 2 de ces 4 leviers.

## 1. Modèle unique retenu : **"Stratégie SEO {secteur} {ville}"**

Pourquoi un seul modèle et pas 5 ? Parce que les concepts du méga-prompt (matrice 30 MC, Triade SERP, Passage Ranking, etc.) ne sont rentables qu'en *long format unique*. Multiplier les modèles courts diluerait le Surprise Score et tomberait dans le thin content que la règle #1 du skill interdit.

| Élément | Valeur |
|---|---|
| Pattern URL | `/blog/strategie-seo-{secteur}-{ville}` |
| Head term | "stratégie SEO" |
| Modificateur | secteur × ville |
| Pages possibles phase 1 | **40 pages** (8 secteurs × 5 villes) |
| Pages possibles long terme | 200+ (10 secteurs × 20 villes) |
| Source données | INSEE (population, salaire), CCI (entreprises), Pages Jaunes (concurrence), Google Maps (densité), bases sectorielles publiques |
| Template fixe | 13 sections (cf. articles parents) |
| Sections 100% variables | H2 #2 (marché local), H2 #4 (cocon sémantique), H2 #5 (ancrage), H2 #7 (outil Product-Led) |
| Sections 30-50% variables | H2 #1 (vue d'ensemble), H2 #3 (6 facteurs ranking — *paraphrase obligatoire*), H2 #6 (roadmap) |
| Sections quasi-fixes | H2 #9 (erreurs), H2 #10 (checklist), FAQ (5 Q&A adaptées) |
| Avantage non copiable | Simulateur sectoriel + doctrine Boussardon + données terrain sourcées |
| Schema.org | Article + LocalBusiness (Organikk) + FAQPage |

**Règle anti-duplicate** : viser **max 25% texte identique** entre deux pages (objectif plus strict que les 30% du skill). Les 6 facteurs de ranking doivent être *réécrits* secteur par secteur — pas copiés. Exemple : "Passage Ranking" pour serrurier parle de fragments d'urgence ("porte claquée 2h du matin"), pour immobilier parle de fragments transactionnels ("estimer un T3 Lyon 6"), pour avocat parlerait de fragments de qualification juridique ("rupture conventionnelle préavis 2026").

## 2. Matrice de priorisation des secteurs

Scoring sur 25 points. Critères :
- **ACV** : panier moyen unitaire (1=<200€ · 5=>5000€)
- **Urgence** : intention transactionnelle immédiate (1=info · 5=appel sous 2h)
- **Concurrence SEO locale faible** (inversé : 5=déserte · 1=saturée par Hellopros/PagesJaunes/Wizishop)
- **Simulateur Product-Led** : faisabilité d'un outil interactif différenciant (1=non · 5=évident)
- **Volume de leads** : taille marché ville moyenne FR (1=niche · 5=mass-market)

| # | Secteur | ACV | Urg. | Concu. faible | Simul. | Volume | **Total** | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | Serrurier | 3 | 5 | 2 | 5 | 4 | **19** | ✅ FAIT |
| 2 | Agence immobilière | 5 | 3 | 1 | 5 | 5 | **19** | ✅ FAIT |
| 3 | **Constructeur maison individuelle** | 5 | 2 | 3 | 5 | 3 | **18** | 🎯 Priorité 1 |
| 4 | **Plombier** | 3 | 5 | 2 | 4 | 4 | **18** | 🎯 Priorité 1 |
| 5 | **Avocat (divorce / droit travail)** | 5 | 3 | 3 | 4 | 3 | **18** | 🎯 Priorité 1 |
| 6 | **Cuisiniste** | 5 | 2 | 4 | 5 | 2 | **18** | 🎯 Priorité 1 |
| 7 | **Chauffagiste / PAC** | 4 | 4 | 3 | 4 | 3 | **18** | 🎯 Priorité 1 |
| 8 | **Couvreur** | 4 | 4 | 3 | 4 | 3 | **18** | 🎯 Priorité 2 |
| 9 | **Architecte d'intérieur** | 5 | 1 | 4 | 4 | 2 | **16** | 🎯 Priorité 2 |
| 10 | **Constructeur piscine** | 5 | 2 | 4 | 4 | 2 | **17** | 🎯 Priorité 2 |
| 11 | Électricien | 3 | 4 | 2 | 3 | 4 | 16 | Phase 3 |
| 12 | Dentiste / Orthodontiste | 4 | 3 | 2 | 3 | 4 | 16 | Phase 3 |
| 13 | Chirurgien esthétique | 5 | 2 | 4 | 3 | 2 | 16 | Phase 3 |
| 14 | Courtier prêt immobilier | 3 | 3 | 3 | 5 | 3 | 17 | 🎯 Priorité 2 |
| 15 | Notaire | 4 | 2 | 5 | 2 | 3 | 16 | Phase 3 |
| 16 | Expert-comptable | 4 | 2 | 3 | 4 | 4 | 17 | 🎯 Priorité 2 |
| 17 | Garagiste / Carrossier | 3 | 4 | 1 | 3 | 5 | 16 | Phase 3 |
| 18 | Vétérinaire | 2 | 4 | 3 | 2 | 4 | 15 | Skip |
| 19 | Auto-école | 2 | 2 | 1 | 3 | 4 | 12 | Skip |
| 20 | Déménageur | 3 | 4 | 2 | 5 | 4 | 18 | 🎯 Priorité 2 |
| 21 | Paysagiste | 3 | 2 | 3 | 4 | 3 | 15 | Phase 3 |
| 22 | Wedding planner | 4 | 1 | 4 | 3 | 2 | 14 | Skip |
| 23 | Photographe mariage | 3 | 1 | 2 | 2 | 3 | 11 | Skip |
| 24 | Kiné / Ostéopathe | 2 | 3 | 1 | 1 | 4 | 11 | Skip |
| 25 | Psy / Coach | 2 | 2 | 2 | 1 | 3 | 10 | Skip |
| 26 | Agence digitale B2B | 5 | 1 | 1 | 4 | 2 | 13 | Skip (concurrence Organikk) |
| 27 | Cabinet recrutement | 4 | 2 | 3 | 3 | 2 | 14 | Skip |
| 28 | Climatisation | 4 | 3 | 3 | 4 | 3 | 17 | 🎯 Priorité 2 |
| 29 | Diagnostic immobilier (DPE) | 2 | 3 | 3 | 5 | 4 | 17 | 🎯 Priorité 2 |
| 30 | Coach sportif | 2 | 2 | 1 | 2 | 3 | 10 | Skip |

### 8 secteurs retenus pour la phase 1 (les nouveaux, hors serrurier/immo déjà faits)

1. **Constructeur maison individuelle** (ACV 200-400k€, simulateur = "estimer coût terrain+maison")
2. **Plombier** (urgence + maillage avec serrurier déjà publié)
3. **Avocat** (très ACV, simulateur "estimer indemnités prudhommes / pension alimentaire")
4. **Cuisiniste** (ACV 10-30k€, simulateur "estimer prix cuisine sur-mesure")
5. **Chauffagiste PAC** (ACV 8-18k€, simulateur "estimer aides MaPrimeRénov + coût PAC")
6. **Courtier prêt immobilier** (simulateur "capacité d'emprunt 2026")
7. **Cuisiniste** déjà compté · remplacer par **Constructeur piscine** (ACV 30-80k€, simulateur "coût piscine selon dimensions")
8. **Expert-comptable** (B2B, simulateur "estimer coût compta selon CA et statut")

Note : "déménageur" et "diagnostic immobilier" sont reportés en phase 2 — bons scores mais ACV faible pour le premier sweep.

## 3. Top villes prioritaires

Critères : population (1-5) · pouvoir d'achat médian INSEE (1-5) · densité concurrence Google Maps faible (1-5 inversé — 5 = créneau) · volume de recherche local estimé (1-5).

| # | Ville | Pop. | PA | Concu. faible | Volume | **Total** | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | **Lyon** | 5 | 4 | 2 | 5 | **16** | ✅ ancrage (2 articles faits) |
| 2 | **Paris** | 5 | 5 | 1 | 5 | **16** | 🎯 Phase 1 (mais découper par arrondissements en phase 2) |
| 3 | **Bordeaux** | 4 | 4 | 4 | 4 | **16** | 🎯 Phase 1 |
| 4 | **Marseille** | 5 | 3 | 3 | 5 | **16** | 🎯 Phase 1 |
| 5 | **Toulouse** | 4 | 4 | 4 | 4 | **16** | 🎯 Phase 1 |
| 6 | **Nantes** | 4 | 4 | 4 | 4 | **16** | 🎯 Phase 1 |
| 7 | **Nice** | 4 | 4 | 3 | 4 | **15** | 🎯 Phase 2 |
| 8 | Lille | 4 | 3 | 3 | 4 | 14 | Phase 2 |
| 9 | Aix-en-Provence | 3 | 5 | 4 | 3 | 15 | Phase 2 |
| 10 | Annecy | 3 | 5 | 4 | 3 | 15 | Phase 2 (PA très haut, niche premium) |
| 11 | Strasbourg | 4 | 3 | 4 | 3 | 14 | Phase 2 |
| 12 | Montpellier | 4 | 3 | 3 | 4 | 14 | Phase 2 |
| 13 | Rennes | 4 | 4 | 4 | 3 | 15 | Phase 2 |
| 14 | Versailles | 2 | 5 | 4 | 3 | 14 | Phase 2 (PA très haut, secteurs cuisiniste/archi) |
| 15 | Grenoble | 3 | 4 | 4 | 3 | 14 | Phase 3 |
| 16 | Tours | 3 | 3 | 4 | 2 | 12 | Phase 3 |
| 17 | Reims | 3 | 3 | 4 | 2 | 12 | Phase 3 |
| 18 | Toulon | 3 | 3 | 3 | 3 | 12 | Phase 3 |
| 19 | Dijon | 3 | 3 | 4 | 2 | 12 | Phase 3 |
| 20 | Angers | 3 | 3 | 4 | 2 | 12 | Phase 3 |

### 5 villes retenues phase 1

Paris · Bordeaux · Marseille · Toulouse · Nantes (+ Lyon déjà couverte).

## 4. Liste finale phase 1 — 40 combinaisons

Matrice **8 secteurs × 5 nouvelles villes = 40 pages**, plus 8 pages "secteur × Lyon" (à publier en premier pour bénéficier de l'autorité Lyon déjà construite avec serrurier/immo). **Total phase 1 = 48 pages.**

| Secteur \ Ville | Lyon | Paris | Bordeaux | Marseille | Toulouse | Nantes |
|---|---|---|---|---|---|---|
| Serrurier | ✅ fait | + | + | + | + | + |
| Agence immo | ✅ fait | + | + | + | + | + |
| Plombier | 1 | 2 | 3 | 4 | 5 | 6 |
| Avocat | 7 | 8 | 9 | 10 | 11 | 12 |
| Constructeur maison | 13 | 14 | 15 | 16 | 17 | 18 |
| Cuisiniste | 19 | 20 | 21 | 22 | 23 | 24 |
| Chauffagiste PAC | 25 | 26 | 27 | 28 | 29 | 30 |
| Constructeur piscine | 31 | 32 | 33 | 34 | 35 | 36 |
| Courtier prêt immo | 37 | 38 | 39 | 40 | 41 | 42 |
| Expert-comptable | 43 | 44 | 45 | 46 | 47 | 48 |

48 combinaisons numérotées par ordre de priorité de production.

## 5. Plan d'exécution 90 jours

Cadence cible : **16 pages / mois** = 4 / semaine. Avec l'aide du skill `seo-workflow-article` + variabilisation du template, ~2h30 par page (vs 5-6h en greenfield). Budget temps : ~40h/mois.

### Mois 1 (M0) — Pages 1 à 16 : Lyon (8) + 8 plus performantes ailleurs

Semaine 1 : Plombier Lyon · Avocat Lyon · Cuisiniste Lyon · Chauffagiste Lyon
Semaine 2 : Constructeur maison Lyon · Piscine Lyon · Courtier Lyon · Expert-comptable Lyon
Semaine 3 : Plombier Paris · Plombier Bordeaux · Avocat Paris · Avocat Bordeaux
Semaine 4 : Cuisiniste Paris · Cuisiniste Bordeaux · Chauffagiste Paris · Chauffagiste Bordeaux

**Pourquoi commencer par Lyon ?** Maillage interne immédiat avec les 2 articles existants → boost autorité topique. Quand on publie *plombier Lyon*, on linke vers *serrurier Lyon* (cluster "urgence locale Lyon").

### Mois 2 (M1) — Pages 17 à 32 : Marseille + Toulouse

Semaine 5 : Plombier MAR · Avocat MAR · Cuisiniste MAR · Chauffagiste MAR
Semaine 6 : Construct. maison MAR · Piscine MAR · Courtier MAR · Comptable MAR
Semaine 7 : Plombier TLS · Avocat TLS · Cuisiniste TLS · Chauffagiste TLS
Semaine 8 : Construct. maison TLS · Piscine TLS · Courtier TLS · Comptable TLS

### Mois 3 (M2) — Pages 33 à 48 : Nantes + finalisations + refresh

Semaine 9 : Plombier NTS · Avocat NTS · Cuisiniste NTS · Chauffagiste NTS
Semaine 10 : Construct. NTS · Piscine NTS · Courtier NTS · Comptable NTS
Semaine 11 : Pages restantes Paris/Bordeaux (construct. maison, piscine, courtier, comptable)
Semaine 12 : **Refresh M0** — mettre à jour les 16 pages mois 1 avec données INSEE et premiers retours GSC. Maillage croisé final.

### Prérequis techniques avant M0

1. ✅ Template figé `src/app/blog/[slug]/page.tsx` (déjà OK)
2. **À faire** : créer 6 composants simulateur React (1 par secteur) dans `src/components/` :
   - `PlombierSimulateurMockup.tsx` (déjà pattern serrurier)
   - `AvocatSimulateurMockup.tsx` (indemnités prudhommes / pension alimentaire)
   - `CuisinisteSimulateurMockup.tsx` (prix cuisine sur-mesure)
   - `ChauffagisteSimulateurMockup.tsx` (PAC + MaPrimeRénov)
   - `ConstructeurMaisonSimulateurMockup.tsx` (terrain + maison)
   - `PiscineSimulateurMockup.tsx` (dimensions + matériau)
   - `CourtierSimulateurMockup.tsx` (capacité emprunt)
   - `ComptableSimulateurMockup.tsx` (coût compta selon CA)
3. **À faire** : étendre l'union type `{ type: 'mockup'; variant }` dans `articles.ts` pour accepter les 8 variants
4. **À faire** : créer 1 fiche de sources INSEE/CCI par couple secteur×ville pour ne pas refaire la recherche à chaque page

### Budget conversion attendu (hypothèses prudentes)

- 48 pages × 2000 impressions/mois en cruise après M9 = 96k impressions/mois
- CTR moyen position 3-8 sur requêtes transactionnelles = 4%  → ~3800 visiteurs/mois
- Taux conversion visiteur → lead audit gratuit = 1,5% (intention transactionnelle haute) → **~57 leads/mois**
- À €4-8k panier audit Organikk : ROI ~10x sur 12 mois

## 6. Mots-clés décisionnels par cellule

Pattern primaire (le H1) : `Stratégie SEO {secteur} {ville}`

Pour chaque cellule, viser **15 longues traînes** (matrice 30 MC = 15 primaires + 15 satellites secondaires que le cocon couvrira). Voici les patterns réutilisables :

### Pattern A — Décisionnels (top 5 par cellule)
- `stratégie seo {secteur} {ville}` (H1 — Know→Do)
- `seo {secteur} {ville}` (Do)
- `agence seo {secteur}` (Do)
- `référencement {secteur} {ville}` (Do)
- `seo local {secteur} {ville}` (Do)

### Pattern B — Comparatifs (3 par cellule)
- `comment référencer un cabinet de {secteur} à {ville}`
- `meilleure agence seo {secteur}`
- `{secteur} {ville} google première page`

### Pattern C — Problème (3 par cellule)
- `pourquoi mon site {secteur} ne ranke pas`
- `concurrence seo {secteur} {ville}`
- `combien coûte le seo pour un {secteur}`

### Pattern D — Tactique (4 par cellule)
- `cocon sémantique {secteur}`
- `fiche google business {secteur} {ville}`
- `mots-clés {secteur} {ville}`
- `passage ranking {secteur}` (signature doctrine Boussardon)

**Anti-cannibalisation interne** : si Organikk publie déjà `agence-seo-{ville}` au niveau service, la page `strategie-seo-{secteur}-{ville}` doit canonicaliser correctement et linker vers le service. Pas l'inverse.

## 7. Règles spécifiques au pSEO Organikk (les 7 du skill, calibrées)

1. **Anti-thin** : ≤ 25% texte identique entre 2 pages. Les blocs "6 facteurs de ranking 2026" doivent être *réécrits par secteur*, pas templatés.
2. **Données terrain** : interdiction de chiffres inventés. Pour chaque ville × secteur, sourcer :
   - Population INSEE (année 2023 ou 2024)
   - Nombre d'entreprises du secteur (CCI ou base SIRENE)
   - Densité concurrentielle Google Maps (compter à la main les fiches dans rayon 5km du centre)
   - Salaire médian / pouvoir d'achat ville INSEE
   - Prix moyen prestation secteur (source pro : UFC-Que Choisir, FFB, ordre pro)
3. **Sourcing visible** : chaque chiffre inline = ` _(INSEE, 2024)_ `
4. **Canonical** : 1 URL = 1 contenu. Pas de paramètres trackers indexés.
5. **Maillage différenciant** : 
   - Page `plombier-{ville}` linke vers `serrurier-{ville}` + `chauffagiste-{ville}` (cluster urgence/habitat)
   - Page `cuisiniste-{ville}` linke vers `architecte-{ville}` + `constructeur-maison-{ville}` (cluster rénovation)
   - Page `avocat-{ville}` linke vers `expert-comptable-{ville}` + `courtier-{ville}` (cluster pro libérale)
   - Jamais le même paquet de 3 liens entre deux pages.
6. **Surprise Score haut** : chaque page = au moins 1 inversion non-évidente. Exemples pré-réfléchis :
   - Plombier : "le SEO plombier 2026 est gagné non par les mots-clés urgence mais par les guides post-incident (fuite réparée, comment éviter récidive)"
   - Avocat : "l'avocat divorce qui ranke à Paris n'est pas celui qui parle de divorce, c'est celui qui chiffre la garde alternée"
   - Cuisiniste : "le cuisiniste qui ranke ne vend pas des cuisines, il vend de la projection (configurateur 3D + visite virtuelle showroom)"
   - Constructeur piscine : "Google récompense les constructeurs qui publient leurs ratés (corrosion, sols argileux) — pas leurs réussites"
7. **Grounding Score** : par page, 1 passage ancré 150-200 mots (avec coordonnées géo de la ville, quartiers cités, prix locaux) + 1 bloc authorship 50 mots (signature Organikk + métier auteur).

## 8. Mécanismes anti-duplicate concrets (template-level)

Pour éviter que les 48 pages se ressemblent au niveau Passage Ranking :

| Section du template | Variation imposée |
|---|---|
| Intro thèse | Reformuler complètement — angle d'attaque ≠ par secteur |
| H2 #1 Vue d'ensemble | Métrique reine *différente* (urgence → temps de réponse ; ACV élevé → coût acquisition ; B2B → mandat) |
| H2 #2 Marché local | Chiffres ville-secteur uniques, sourcés INSEE/CCI |
| H2 #3 6 facteurs ranking | Mêmes 6 facteurs MAIS chaque facteur appliqué à un cas du secteur — pas une définition générique |
| H2 #4 Cocon sémantique | 6 sous-cocons propres au secteur (urgence ≠ luxe ≠ régulé) |
| H2 #5 Ancrage local | Quartiers, monuments, syndic types, profil client local |
| H2 #6 Roadmap 9 mois | Phase 1 ≠ par secteur (urgence = bottom-funnel d'abord ; ACV élevé = pages mères avant satellites) |
| H2 #7 Simulateur | Outil dédié secteur, screenshot mockup différent |
| H2 #8 Matrice 30 MC | Liste 100% spécifique secteur×ville |
| H2 #9 Erreurs | Anti-patterns du secteur (≠ génériques) |
| H2 #10 Checklist S1 | Tâches activables par un pro du secteur (ex : avocat = barreau + plaidoyer publié ; plombier = sticker véhicule + photo intervention) |
| FAQ | 5 Q/R adaptées (3 sectorielles + 2 méthodologiques) |

## 9. Résumé exécutif (5 phrases)

Organikk déploie un système programmatique unique : 48 pages "stratégie SEO {secteur} {ville}" publiées en 90 jours, couvrant 8 secteurs B2C à fort ACV ou urgence × 6 villes (Lyon + 5 métropoles FR). Chaque page = 2500+ mots avec données INSEE/CCI sourcées, un simulateur Product-Led codé en React et la doctrine Boussardon (Passage Ranking + Surprise Gap + Triade SERP). L'avantage non copiable tient à trois leviers : données terrain ville par ville, simulateurs interactifs sectoriels (impossibles à générer par LLM), inversions méthodologiques propres à Organikk. Le premier modèle à lancer = **Plombier Lyon** (semaine 1, maillage immédiat avec serrurier Lyon publié, simulateur clonable du mockup serrurier existant). Cible business : 57 leads d'audit/mois en cruise après M9, ROI 10x sur 12 mois.

## 10. Prochaine étape opérationnelle

Le user doit valider :
1. La liste des 8 secteurs (modifications possibles avant lancement M0)
2. L'ordre des 6 villes
3. Le fait de coder les 8 mockups simulateurs *avant* M0 ou de les ajouter en M2 (option : démarrer sans simulateur sur 4 secteurs B2B où le mockup est moins critique)

Une fois validé → invoquer le skill `seo-workflow-article` (8 étapes) pour la **page #1 = Plombier Lyon**, en partant du brief structuré que ce document fournit.

---

**Concepts liés** : [[surprise-gap]] · [[passage-ranking]] · [[grounding-score]] · [[fully-meets]] · [[product-led-seo]] · [[maillage-systeme]] · [[e-e-a-t]] · [[triade-serp]]
