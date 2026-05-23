---
slug: engine-densite-semantique-sans-serp
title: "Engine — Carte sémantique sans SERP (13 phases, cosinus simulé, Surprise Score Sémantique, skill Claude)"
author: "Timothée Boussardon"
date_added: 2026-05-11
date_updated: 2026-05-23
type: methode
audience: seo-rédacteur
topic: entites-semantiques-aeo
status: draft
version: v10
---

# Engine — Carte sémantique sans SERP

## À quoi sert cet engine

Tu lui donnes une requête. Il te sort la carte sémantique complète : tout ce que ton article doit contenir au niveau sens, sans regarder ce qui ranke déjà sur Google.

Alternative aux outils qui te listent des mots à intégrer après scraping du top 10. Ici, zéro scraping SERP. La carte se construit depuis l'intention, l'expertise propre du média, et des sources externes autorisées.

**Ce que l'engine fait — 11 couches sémantiques actives** :

1. Micro-intentions (3 niveaux + Action Engine flag)
2. Entités sémantiques pondérées (poids 0-1 + densité cible % + cosinus simulé + justification + statut P1/P2/P3)
3. Lexique signature (bigrams, trigrams, expressions multi-mots, co-occurrences)
4. Pain points & verbatims Haute Surprise
5. Vecteurs de preuves quantitatives (Confidence Score + Freshness Guard)
6. Vecteurs multimodaux
7. Cartographie concurrentielle (5-10 acteurs)
8. Gap analysis (3 vues) : Gap Competitive Map / Content Gap Score / **Surprise Score Sémantique 0-100**
9. Divergence Haute Surprise (calibrée [[information-gain]] — benchmark Aggarwal KDD'24)
10. FAQ stratégique FM (5-7 vecteurs latents, answer-first)
11. Structural Information GEO (title / meta / H / schema)

Plus une Phase 0 informative en amont, une Phase 12 (matrice couverture × mapping [[triade-serp]]) et une Phase 13 (feedback loop KB).

**Ce que l'engine NE fait PAS.** Pas de hook. Pas de H1 rédigé. Pas d'architecture Hn finale. Pas de CTA. Pas de closing. Pas de cluster (engine = une page, une intention — voir [[purete-vectorielle]]). La rédaction est une étape séparée, branchée en aval.

**Phase 0 informative (pas bloquante).** Sur head term saturé ou pluralité d'intentions, l'engine alerte mais **produit malgré tout la carte complète** + propose les sous-niches en annexe. Tu décides ensuite si tu exploites la carte large ou si tu relances sur une sous-niche.

**Embeddings simulés.** Le cosinus Phase 2 est une projection Claude calibrée sur son corpus appris, marquée « simulé » dans chaque sortie. Pas de vraie API embedding — honnête sur ce que Claude peut / ne peut pas faire.

---

## CE QUE L'UTILISATEUR DONNE

### Obligatoire

**1. La requête cible.** La query mot pour mot.

**2. Le profil utilisateur (6 variables).** Sans ces 6 variables, l'engine pose une seule question groupée avant de produire.

| Variable | Exemple de valeur | Rôle |
|---|---|---|
| Pays / langue | FR/FR par défaut | Vocabulaire, références culturelles, sources |
| B2B / B2C + rôle | « B2B — CMO SaaS 50p » ou « B2C — particulier 30-50 ans » | Verrouille les verbatims et les preuves |
| Objectif | Lead Gen / Conversion / Expertise FM | Calibre l'Action Engine flag en Phase 1 |
| Secteur | SaaS, immobilier, BTP, juridique… | Filtre les entités et les cas terrain |
| Audience (expertise) | junior / expert / mixte | Calibre la profondeur lexicale |
| Localisation | Ville, région, ou « N/A » | Ancrage local SEO |

### Recommandé

**3. La couche d'expertise unique.** Une phrase. Ce que toi tu sais et que personne d'autre n'écrira sur le sujet. Si vide, Claude propose 5 angles divergents en Phase 9.

---

## MODES BRONZE / SILVER / GOLD

L'engine détecte automatiquement le niveau de matière disponible et adapte la profondeur de ses livrables.

### Détection automatique du mode

| Conditions détectées | Mode activé |
|---|---|
| Aucun KB, juste une requête et une expertise | Bronze |
| KB partiel (quelques notes ou doctrines) | Silver |
| KB structuré (wiki, notes, doctrines, concepts versionnés) | Gold |

L'utilisateur peut forcer un mode plus bas.

### Ce que produit chaque mode par couche sémantique

| Couche | Bronze | Silver | Gold |
|---|---|---|---|
| Micro-intentions | Complet (training) | Complet | Complet |
| Banlist / whitelist | Non | Partielle | Oui (documentée dans le KB) |
| Entités sémantiques pondérées | 30-40, training seul | 40-50, + KB partiel | 50+, + entités propriétaires + doctrines |
| Lexique signature (n-grams) | Standard du domaine | + n-grams KB partiels | + lexique signature documenté |
| Pain points / verbatims | Génériques | + verbatims partiels du KB | + verbatims signature et data terrain |
| Preuves quantitatives | Training + sourcing externe | Idem | Idem + cas terrain propriétaires |
| Multimodal | Générique | Générique | + patrons multimodaux signature |
| Cartographie concurrentielle | Training + sourcing externe | Idem | Idem + références internes |
| Gap analysis | Score estimé | Score + KB | Score + KB + doctrines |
| Divergence Haute Surprise | Limitée (training) | Moyenne | Forte (anti-positionnements maison) |
| FAQ stratégique FM | Standard | Standard + KB | + questions issues des bootcamps / sessions clients |
| Structural Information GEO | Standard | Standard | + patterns title / meta éprouvés sur le média |

### Sur quoi Claude s'appuie selon le mode

**Mode Bronze.**
| Source | Rôle |
|---|---|
| Training du modèle | Connaissance générale, frameworks publics, études connues |
| Sourcing externe autorisé (robots.txt compliant) | Études récentes, papers, rapports publics |
| Input requête (Q1) | Décodage intentionnel |
| Input expertise unique (Q2) | Seule couche propriétaire qualitative |

**Mode Silver.**
| Source | Rôle |
|---|---|
| Training + sourcing externe | Idem Bronze |
| KB partiel | Concepts en cours de constitution, doctrines isolées |
| Input expertise unique | Couche propriétaire qualitative |

**Mode Gold.**
| Source | Rôle |
|---|---|
| Training + sourcing externe | Idem Bronze |
| KB structuré (wiki, notes, doctrines) | Concepts propriétaires, banlist documentée, doctrines maison |
| Input expertise unique | Couche propriétaire qualitative (souvent déjà partiellement dans le KB) |

### Le moat n'est pas l'engine, c'est le KB

Engine Bronze : carte correcte mais réplicable. N'importe qui avec Claude peut produire la même.

Engine Gold : carte signature, irréplicable. Le moat tient au KB qui le nourrit.

**Conséquence opérationnelle.** Chaque article rédigé doit déposer un atome de concept dans le KB. Sinon Bronze à vie. Voir Phase 13 (feedback loop). Pour un utilisateur Bronze qui veut passer Silver/Gold vite, voir Mode 0 (KB Bootstrap).

---

## MODE 0 — KB BOOTSTRAP

Opération préalable à l'engine principal. Sert à constituer un KB en quelques heures à partir de matière existante.

### Ce que tu dois donner en input (pour maximiser le résultat)

#### 1. Articles publiés (obligatoire)

| Critère | Minimum | Idéal |
|---|---|---|
| Volume | 20 articles | 30 à 50 articles |
| Format | URLs ou fichiers Markdown / HTML | Markdown brut dans un dossier local |
| Diversité de sujets | 3 thématiques couvertes | 5 à 7 thématiques |
| Positionnement | Articles où tu prends position | Articles avec concepts ou frameworks originaux |

Évite : articles génériques "10 best practices", articles d'opportunisme SEO sans position, contenus rédigés par un freelance sans ta voix.

#### 2. Matière non publiée (recommandé)

Ces matériaux densifient le KB beaucoup plus que les articles seuls. Donne-les si tu les as.

| Type | Pourquoi c'est précieux |
|---|---|
| Newsletters publiées ou drafts | Voix plus tranchée que sur le blog, positions assumées |
| Posts LinkedIn (les tiens, exportés) | Concepts atomiques formulés en 200 mots |
| Transcripts d'interviews ou podcasts | Vocabulaire signature au naturel, expressions récurrentes |
| Briefs commerciaux ou propositions client | Cas terrain chiffrés, objections traitées |
| Notes Obsidian / Notion existantes (même brouillon) | Concepts en cours de formulation |
| Slides de conférences ou de formations | Doctrines distillées en 1-2 phrases |

#### 3. Inputs de cadrage (optionnel mais accélère le tri)

| Input | Effet |
|---|---|
| Liste de 10 expressions que tu utilises souvent | Accélère la détection de la whitelist signature |
| Liste de 10 mots ou formules que tu bannis | Pré-remplit la banlist sans extraction |
| Liste de 3-5 concurrents / médias que tu refuses de citer | Calibre l'anti-positionnement |
| 3 cas clients dont tu es fier (1 paragraphe chacun) | Densifie les cas terrain chiffrés |

#### 4. Destination du KB (obligatoire)

| Item | Détail |
|---|---|
| Chemin local | Là où Claude va créer les fichiers (ex. `/Users/toi/Code/mon-kb/`) |
| Structure préférée | Plate ou par sous-dossiers (`/concepts/`, `/entities/`, `/competitors/`) |

### Format prompt d'invocation

```
Lance Mode 0 KB Bootstrap.

Articles publiés : [chemin du dossier ou liste d'URLs]
Matière non publiée : [chemin du dossier]
Banlist initiale (optionnel) : [...]
Whitelist initiale (optionnel) : [...]
Destination KB : [chemin]
```

Plus tu donnes de matière brute, moins tu auras à arbitrer en sortie. Sans les inputs de cadrage, Claude extrait à l'aveugle et tu valides manuellement plus de propositions.

---

## MODE AUDIT — Auditer un contenu existant

Mode alternatif au Mode Création (qui est le mode par défaut). L'engine ne part plus d'une requête vierge : il croise les 11 couches sémantiques attendues avec ce qui est effectivement dans un contenu existant, et sort un diff par couche + un plan de correction priorisé.

### Mode Création vs Mode Audit

| Mode | Input supplémentaire | Output |
|---|---|---|
| **Création** (défaut) | — | 11 livrables vierges + matrice + patches KB |
| **Audit** | Le contenu à auditer | 11 livrables × 3 colonnes (Attendu / Couvert / Gap) + plan de correction priorisé P0/P1/P2 |

### Inputs supplémentaires pour le Mode Audit

| Variable | Format accepté | Obligatoire |
|---|---|---|
| Contenu à auditer | Texte markdown collé, chemin de fichier local, URL publique (robots.txt OK) | Oui |
| Version cible | Refonte / mise à jour annuelle / élargissement d'intention / migration de template | Recommandé — calibre la sévérité de l'audit |

### Workflow Mode Audit (les 13 phases enrichies)

Chaque phase produit 3 colonnes au lieu d'une.

| Couche | Attendu (calculé Mode Création) | Couvert dans le contenu actuel | Gap + action de correction |

Pour chaque couche, après avoir généré l'attendu (training + KB), Claude scanne le contenu et identifie trois statuts :

| Statut | Définition | Action |
|---|---|---|
| ✅ Couvert | L'élément attendu est présent et conforme | Validation, aucune action |
| ❌ Gap | L'élément attendu est absent ou non conforme | Correction à planifier |
| ⚠️ Hors scope | L'élément présent ne correspond à aucune couche attendue (pollue le vecteur sémantique) | Suppression ou déplacement (FAQ, autre page) |

Le statut « Hors scope » est critique : il préserve la [[purete-vectorielle]]. Plus le contenu présente d'éléments hors scope, plus son vecteur s'éloigne de la cible.

### Plan de correction priorisé (livrable supplémentaire Mode Audit)

À la fin du run, Claude produit un tableau de correction priorisé sur 3 niveaux.

| Priorité | Critère | Effet si ignoré |
|---|---|---|
| **P0 — Bloquant** | Gap sur Phase 11 (Structural Information GEO) ou phase Triade SERP entière non couverte | La page ne franchit pas le filtre d'admission Google (Document Ranking) |
| **P1 — Important** | Gap sur Phase 4 (pain points), Phase 9 (divergence/Surprise Gap), Phase 5 (preuves quantitatives), ou Surprise Score Sémantique < 60 | La page entre dans la SERP mais reste en Low Surprise → oubliée par les modèles IA |
| **P2 — Amélioration** | Gap sur Phase 10 (FAQ FM), Phase 6 (multimodal), Phase 13 (patches KB non versionnés) | La page ranke mais ne maximise pas la Triade SERP phase 3 (Generation, citation LLM, AIO) |

Format de sortie :

```
PLAN DE CORRECTION — Contenu : "[titre/URL/chemin]"
Requête cible : "[...]"

Surprise Score Sémantique actuel : XX/100 — [verdict]

P0 — Bloquants (à corriger avant publication ou refonte)
- [Phase X — Couche Y] Gap : [description précise]
  → Action : [verbe + objet précis + emplacement dans la page]

P1 — Importants (à corriger avant la prochaine vague de mises à jour)
- [Phase X — Couche Y] Gap : [...]
  → Action : [...]

P2 — Améliorations (à corriger sur les versions suivantes)
- [Phase X — Couche Y] Gap : [...]
  → Action : [...]

ÉLÉMENTS HORS SCOPE détectés (à sortir du corps) :
- [Citation du contenu] → Raison : pollue le vecteur sur intention [Z] → Action : déplacer en FAQ / sortir en page dédiée / supprimer

Score de couverture global : X/11 couches couvertes
```

### Différence vs `seo-geo-audit`

`seo-geo-audit` note **7 scores algorithmiques** (Surprise, Grounding, Content Effort, RRF, RAG Structurer, Freshness Guard, Action Engine) sur 100, sort un verdict global (Citable / Fragile / À retravailler / Médiocrité Statistique). C'est un audit de **qualité par score**.

Mode Audit de cet engine audite la **couverture des 11 couches sémantiques**, produit un diff par couche et un plan de correction priorisé P0/P1/P2. C'est un audit de **complétude par couche**.

Usage combiné recommandé :
1. **Mode Audit** d'abord : que manque-t-il à mon contenu ? (couverture)
2. **seo-geo-audit** ensuite : à quel point ce qui est présent est-il robuste ? (qualité)

### Quand utiliser quel mode

| Situation | Mode |
|---|---|
| Nouvelle page à créer | Création |
| Refonte d'un article qui ne ranke pas | Audit (+ geo-audit en complément) |
| Mise à jour annuelle (déclenchée par Freshness Guard) | Audit |
| Élargissement de l'intention d'une page existante | Audit avec « version cible » spécifiée |
| Migration d'un contenu vers un nouveau template | Audit (sortie alimente le brief de refonte) |
| Vérification post-rédaction avant publication | Audit + seo-geo-audit combinés |

### Format prompt d'invocation — Mode Audit

```
Lance l'engine carte sémantique sans SERP (v10) — Mode AUDIT.

Requête cible : [...]
Profil utilisateur : [6 variables]

Contenu à auditer : [texte markdown collé | chemin de fichier | URL publique]
Version cible (optionnel) : [refonte / update freshness / élargissement / migration]

Expertise unique (optionnel) : [...]
Mode forcé (optionnel) : [bronze / silver / gold]
```

---

## PHASE 0 — FILTRE STRATÉGIQUE (INFORMATIF, non bloquant)

L'engine analyse en amont trois dimensions de la requête. **Il ne bloque jamais la production de la carte** — il alerte et propose des sous-niches en annexe si besoin. C'est à l'utilisateur de décider s'il exploite la carte large ou s'il relance sur une sous-niche.

### 0.1 Test de substitution LLM

Deux questions binaires (cf. [[mots-cles-actionnels]], [[test-substitution-llm]]) :

1. **Q1.** Est-ce que ChatGPT répond déjà à cette requête à 80% ?
2. **Q2.** Si oui, est-ce qu'il peut faire mieux que toi ?

| Q1 | Q2 | Verdict | Effet sur l'engine |
|---|---|---|---|
| Non | — | ✅ PASS | Continue Phase 1 normalement |
| Oui | Non | ⚠️ WARN (expertise unique critique) | Continue, mais flag « divergence obligatoire » en Phase 9 |
| Oui | Oui | ⚠️ WARN sévère | Continue, mais sortie complétée d'une recommandation forte « pivoter la requête » |

### 0.2 Angle différenciant — head term saturé ?

Test : la requête est-elle un head term générique (`agence SEO`, `plombier Paris`, `avocat divorce`) ? (cf. [[angle-differenciant-mot-cle]])

| Test | Verdict |
|---|---|
| Head term générique tapé pour 10 intentions différentes par 100 personnes différentes | ⚠️ WARN — sous-niches proposées en annexe |
| Sous-niche identifiable (urgence / moment / type d'intervention / micro-zone) | ✅ PASS |

Doctrine terrain : `plombier 15e urgence nuit` bat `plombier Paris`. La prime va à l'ultra-niche.

### 0.3 Verrou pureté vectorielle

Test : la requête porte-t-elle UNE intention dominante ou plusieurs ? (cf. [[purete-vectorielle]])

| Requête | Intention(s) | Verdict |
|---|---|---|
| « comment choisir une agence SEO » | 1 (choix) | ✅ PASS — page pure |
| « tout savoir sur le SEO » | N intentions diluées | ⚠️ WARN — propose découpage en N pages en annexe |

Doctrine : *une page = une pureté vectorielle*. Sur head term multi-intentions, l'engine produit la carte large mais signale les N intentions séparables.

### Livrable Phase 0

```
PHASE 0 — Filtre stratégique
- Test LLM : [PASS / WARN — raison]
- Angle différenciant : [PASS / WARN — sous-niches proposées : (1) ... (2) ...]
- Pureté vectorielle : [PASS / WARN — N intentions détectées : (1) ... (2) ...]

→ Verdict global : [GO franche / GO avec avertissement]

ANNEXE — Sous-requêtes conformes proposées (si WARN angle ou pureté) :
| # | Sous-requête | Intention | Pertinence profil | Action recommandée |
| ... | ... | ... | ... | ... |
```

L'engine continue ensuite vers Phase 1, quel que soit le verdict. La WARN sert d'avertissement, pas de blocage.

---

## CE QUE CLAUDE FAIT (workflow détaillé, 13 phases)

### Phase 1. Décodage micro-intentionnel + Action Engine flag

Trois niveaux d'intention.

- **Intention principale.** [[know-simple-know-do]] (Know-Simple / Know / Do — pas TOFU/MOFU/BOFU).
- **Sous-intentions.** 3 à 5 questions parallèles.
- **Micro-intentions.** 15 à 25 questions granulaires.

Profil utilisateur reformulé en une phrase tranchante à partir des 6 variables du profil.

**Action Engine flag.** Si l'intention principale = `Do`, l'engine flag obligatoirement qu'un outil interactif (calculateur, simulateur, générateur, audit — cf. [[product-led-seo]]) est requis pour viser [[fully-meets]]. Une page Know textuelle ne ranke pas sur intention Do en 2026.

**Livrable.** Tableau à 3 niveaux + profil + drapeau Action Engine si Do.

### Phase 2. Entités sémantiques pondérées (avec cosinus simulé + justification)

**Format de sortie : 7 colonnes**, 30 à 50 entités par run (50+ en mode Gold).

| # | Entité | Type | Poids (0-1) | Densité cible (%) | Cosinus estimé requête (0-1) | Justification | Statut |
|---|---|---|---|---|---|---|---|
| 1 | `passage ranking` | Concept | 0.94 | 0.8% | 0.91 | Brique opérationnelle du grounding, citée dans 3 papers MIRAS | P1 critique |
| 2 | `BM25` | Algo | 0.87 | 0.3% | 0.79 | Mécanique sous-jacente du Document Ranking | P1 critique |
| 3 | `cocon sémantique` | Méthode | 0.72 | 0.5% | 0.68 | Doctrine cluster AEO + cooccurrence forte maillage | P2 |

**Définitions** :
- **Type** : Person / Concept / Tool / Method / Doctrine / Event / Location / Algo
- **Poids (0-1)** : estimation Claude de la pertinence sémantique pour la requête. > 0.8 = entité pivot, 0.5-0.8 = entité supportive, < 0.5 = entité périphérique.
- **Densité cible (%)** : fréquence d'occurrence attendue dans un texte 2000 mots. Entités pivots : 0.5-1% ; supportives : 0.2-0.5% ; périphériques : < 0.2%.
- **Cosinus estimé requête (0-1)** : projection Claude de la similarité cosinus entité ↔ requête, calibrée sur le corpus appris. **Marqué « simulé »** dans chaque sortie — pas de vrai calcul vectoriel.
- **Justification** : pourquoi cette entité est dans la liste (paper, doctrine, co-occurrence forte, etc.). Bloque les ajouts arbitraires.
- **Statut** : P1 critique (sans, la page ne ranke pas) / P2 (supportif) / P3 (bonus).

**Avertissement obligatoire** : sortie incluant en pied de tableau « *Cosinus simulé par projection corpus Claude, non calibré mathématiquement. Pour calibration exacte : API embeddings Voyage/Cohere/OpenAI.* »

**Livrable.** Tableau 7 colonnes + total entités + ratio P1/P2/P3.

### Phase 3. Lexique signature (n-grams, co-occurrences, expressions multi-mots)

Au-delà des entités unitaires, le **vocabulaire métier** est porté par des expressions multi-mots. L'engine produit le tableau des n-grams attendus.

| N-gram / expression | Type | Fréquence attendue (sur 2000 mots) | Co-occurrence dominante | Statut |
|---|---|---|---|---|
| « passage ancré » | bigram | 2-3x | grounding-score, featured snippet | P1 |
| « cocon sémantique » | bigram | 1-2x | maillage interne, autorité topique | P1 |
| « consultant seo b2b indépendant » | trigram | 1x | sous-niche, freelance | P2 |
| « ranker dans ChatGPT » | trigram | 1-2x | AIO, citation LLM | P1 |

**Règles** :
- Bigrams : expressions à 2 mots du domaine (`passage ranking`, `data propriétaire`)
- Trigrams : expressions à 3 mots ou plus (`workflow rédaction 8 étapes`)
- Expressions multi-mots : > 3 mots, généralement formulations signature ou métier
- **Co-occurrence dominante** : avec quelles autres entités/concepts ce n-gram apparaît systématiquement. Force la cohérence sémantique du corps.
- **Statut P1 / P2** : P1 = n-gram qu'on attend dans n'importe quelle page sur le sujet ; P2 = bonus signature ou angle.

**Livrable.** Tableau n-grams + colonne « co-occurrence dominante » + ratio P1/P2.

### Phase 4. Pain points & verbatims Haute Surprise

Couche psychologique souvent oubliée des outils de scraping SERP. Tableau de 10 lignes minimum.

| Micro-intention / Pain Point | Verbatim « Haute Surprise » | Preuve atomique attendue |
|---|---|---|
| Frein précis (nommé) | Citation experte rarement verbalisée — zéro cliché | Sujet + Verbe + Donnée chiffrée vérifiable |

**Règles verbatims** :
- Frustration experte ou technique propre au métier du persona
- Vocabulaire signature (verrouillé sur le rôle B2B/B2C du profil)
- Connaissance terrain qu'un initié reconnaît
- **Refus du cliché** : pas de « je veux des résultats », pas de « je veux du ROI »

Exemple de transformation :
- ❌ Cliché : « Je veux voir des résultats concrets »
- ✅ Haute Surprise : « La dernière agence m'envoyait des rapports de 40 pages où le seul KPI lisible était le nombre de backlinks, jamais croisé avec mon CRM »

**Règles preuves atomiques** :
- Format binaire ou chiffré, vérifiable
- ✅ « 73% des prospects B2B refusent un devis sans estimation immédiate »
- ❌ « Nous offrons un excellent service »

**Priorisation finale.** 3 objections critiques selon `fréquence × intensité × différenciation`.

**Livrable.** Tableau pain points complet + 3 objections priorisées.

### Phase 5. Vecteurs de preuves quantitatives (Confidence Score + Freshness Guard)

Génération depuis le training Claude :
- Chiffres datés avec source primaire
- Études connues, sondages, brevets, papers, jurisprudence
- Cas terrain chiffrés

**[[confidence-score]] par preuve** (haute / moyenne / basse) :

| Niveau | Critère | Action |
|---|---|---|
| Haute | Source primaire récente identifiée, paper avec DOI, organisme officiel | Preuve utilisable telle quelle |
| Moyenne | Source connue mais non vérifiée à 100% au moment de la génération | Preuve utilisable + fact-check obligatoire en aval |
| Basse | Reformulation indirecte, source secondaire, donnée approximative | **Remplacer par `[À SOURCER]`** |

**Règle absolue.** Si la confidence est `basse` ou si Claude ne sait pas, **placeholder `[À SOURCER]` obligatoire**. Aucun chiffre inventé pour gonfler le [[grounding-score]].

**[[freshness-guard|Freshness Guard]] intégré.** Chaque preuve porte une date. Trois filtres :

| Âge de la donnée | Statut |
|---|---|
| < 18 mois | Preuve fraîche — OK |
| 18-36 mois | Flag « à actualiser » — utilisable mais signalée |
| > 36 mois | Omise sauf si paper fondateur (étude structurante non substituable) |

**Sourcing externe.** Voir section « Éthique scraping » plus bas — WebSearch + WebFetch robots.txt compliant uniquement, aucun scraping SERP, jamais.

**Livrable.** Tableau preuves : preuve + source + confidence + datation + flag fraîcheur + micro-intention couverte.

### Phase 6. Vecteurs multimodaux

- Tableaux, schémas, captures, photos, vidéos courtes, audio, données interactives
- Pour chaque élément : objectif sémantique + format + micro-intention couverte

**Livrable.** Tableau multimodal.

### Phase 7. Cartographie concurrentielle sans SERP

Sans scraping de la SERP, l'engine identifie les acteurs qui dominent le sujet, pour calibrer la divergence (Phase 8 et 9).

**Trois sources de cartographie**

| Source | Rôle |
|---|---|
| Training Claude | Qui Claude associe spontanément à ce sujet |
| KB interne (si Silver / Gold) | Qui le média référence comme concurrent ou source |
| WebSearch ciblé (robots.txt compliant) | Qui apparaît dans les sources académiques et institutionnelles |

**Output Phase 7**

Tableau des 5 à 10 acteurs dominants, avec pour chacun :
- Nom + type (média, agence, expert, institution, plateforme)
- Angle dominant (la thèse qu'ils défendent sur le sujet)
- Faiblesse identifiable (ce qu'ils ne traitent pas, ne disent pas, ou refusent de voir)

**Livrable.** Tableau cartographie concurrentielle (alimente directement la Phase 8a).

### Phase 8. Gap analysis — 3 vues

Phase pivot. Croise les couches Phase 2 (entités) + Phase 7 (concurrents) pour produire trois vues complémentaires.

#### 8a. Gap Competitive Map (matrice acteur × concept)

Matrice acteur × concept (P1 critique uniquement, sinon trop chargé).

| Acteur | Entité A | Entité B | Entité C | Entité D | Entité E | Gap exploitable |
|---|---|---|---|---|---|---|
| Acteur X | ✅ | ✅ | ❌ | ✅ | ❌ | Entités C + E |
| Acteur Y | ✅ | ❌ | ✅ | ✅ | ❌ | Entités B + E |
| Acteur Z | ❌ | ✅ | ✅ | ❌ | ❌ | Entités A + D + E |
| **GAP MARCHÉ** | — | — | — | — | **0/3** | **E = gap général exploitable** |

**Lecture.** Une entité avec un gap commun (jamais traitée par les 3 acteurs analysés) = opportunité d'attaque prioritaire.

#### 8b. Content Gap Score

Quantifie la couverture sémantique attendue en deux axes.

| Axe | Définition | Cible |
|---|---|---|
| **Couverture standard** | % d'entités P1 que 80%+ des concurrents traitent (= plancher du domaine) | ≥ 70% requis pour franchir Document Ranking |
| **Couverture surprise** | % d'entités P1 traitées par < 20% des concurrents (= zone de divergence) | ≥ 30% requis pour passer Information Gain |

**Verdict** :
- Standard < 70% → la page n'a pas la base sémantique du domaine, elle ne ranke pas
- Standard ≥ 70% mais Surprise < 30% → page indexable mais Low Surprise, mémorisation IA faible
- Standard ≥ 70% ET Surprise ≥ 30% → cible idéale, Information Gain validé

#### 8c. Surprise Score Sémantique 0-100

Mesure quantifiée du gradient de divergence sémantique entre :
- Le consensus (ce que tout le monde dit sur le sujet)
- Ton angle (ce que toi seul dis)

**Formule** (moyenne pondérée de 4 composantes) :

| Composante | Poids | Mesure |
|---|---|---|
| Ratio entités propriétaires / entités totales | 30% | (KB Gold) entités issues du KB ÷ (entités KB + entités training standard) |
| Ratio verbatims Haute Surprise / verbatims totaux | 20% | (Phase 4) verbatims experts rares ÷ verbatims totaux |
| Distance lexicale moyenne propriétaire ↔ consensus | 25% | (simulée Claude) cosinus moyen entités propriétaires ↔ entités consensus, inversé (1 - cosinus) |
| Présence Quotation Addition + Statistics Addition | 25% | (Phase 5) % de preuves citées en verbatim avec source + % preuves chiffrées avec source |

**Échelle** :

| Score | Verdict | Action |
|---|---|---|
| 0-30 | **Médiocrité statistique** | Oubli mémoriel garanti. Refonte ou abandon. |
| 30-60 | Acceptable mais réplicable | Améliorations P1 obligatoires avant publication. |
| 60-85 | Information Gain validé | Zone organikk.co. Publication OK, optimisations P2 possibles. |
| 85-100 | Inversion experte maximale | Zone bootcamp 4 / newsletters Algorithme — Surprise Gap pleinement exploité. |

**Avertissement obligatoire** : sortie incluant « *Score calibré sur projection corpus Claude. Pour calibration exacte : audit GEO Sentinel (skill seo-geo-audit, 7 scores algorithmiques).* »

**Livrable Phase 8.** 8a Matrice + 8b Tableau couverture standard/surprise + 8c Score 0-100 + verdict.

### Phase 9. Vecteur de divergence (Haute Surprise) — calibré Information Gain

Calibré sur la Gap Competitive Map (Phase 8a) ET sur le standard [[information-gain]] (QRG Google p.42 : *no effort content* = note la plus basse).

**Doctrine de calibration** (benchmark Aggarwal KDD'24, arxiv 2311.09735) :

| Méthode | Gain PAWC vs baseline |
|---|---|
| Quotation Addition (citation verbatim) | **+41%** |
| Statistics Addition | **+34%** |
| Cite Sources | **+29%** |
| Authoritative (ton autoritaire seul) | **+13%** seulement |

L'engine privilégie les angles divergents qui s'appuient sur **citations verbatim + statistiques propriétaires**, pas sur le ton autoritaire.

**Pour chaque axe de divergence, exiger** :
- Acteur dominant ciblé (issu Phase 7)
- Entité de la Gap Competitive Map (Phase 8a) — l'angle attaque un gap général du marché
- Type d'inversion (paresseuse vs juste mais contre-intuitive)
- Forme du contenu (citation verbatim, stat propriétaire, cas terrain, donnée externe sourcée)

Critère : un expert dirait *« tiens, je n'avais pas vu ça comme ça »*.

**Livrable.** Tableau divergences classées par force d'inversion × Information Gain mesurable, avec colonnes « se positionne contre [acteur X] » et « attaque gap [entité Y de la map] ».

### Phase 10. FAQ stratégique FM

5 à 7 questions FAQ = 5 à 7 vecteurs sémantiques distincts (chaque question active un vecteur unique, zéro chevauchement).

**Règles strictes** (héritées de `article-engine-pipeline` Phase 3) :
- Chaque question répond à une **micro-intention latente non couverte par le corps**
- Réponse courte, actionnable, citable isolément ([[answer-first-pattern]], AI Overview ready)
- Verrouillage B2B/B2C selon le profil utilisateur Phase 1
- Aucune question pédagogique générique (« qu'est-ce que X »)
- Priorité aux questions Know / Comparatif / Do qui couvrent les angles que le corps ne traite pas

La FAQ absorbe la périphérie sémantique pour que la pureté vectorielle du corps soit préservée.

**Livrable.** Tableau 5-7 questions + réponses citables + vecteur sémantique couvert + Confidence Score sur les chiffres cités.

### Phase 11. Structural Information GEO

Spécifications des champs structurels (title, meta, headings, schema) — pas la rédaction Hn finale, mais les **contraintes sémantiques** que la rédaction devra respecter.

**Doctrine** (finding SAGEO Arena 2025, cf. [[structural-information-geo]]) : optimiser le body seul **dégrade** le retrieval (−4.54 Hit Rate). L'optimisation structurelle apporte **+22% Hit Rate** au retrieval. Structural + Statistics combinés : **+35%**.

**Livrable.** Tableau spécifications structurelles :

| Champ | Contrainte sémantique | Entité(s) à inclure (issues Phase 2) |
|---|---|---|
| Title (≈10 mots) | Mot-clé exact + différenciateur | Entité principale + angle de divergence |
| Meta description (155 char) | Réponse directe answer-first + bénéfice mesurable | Entité principale + verbe d'action |
| H1 | Mot-clé sémantique + promesse | Entité principale + Surprise Gap signalé |
| H2 (5-8 prévus) | Chaque H2 = un vecteur sémantique distinct | Une entité ou un concept par H2 |
| Schema.org | Type adapté à l'intention | Article + FAQPage + LocalBusiness (si géo) + HowTo (si Do) + VideoObject (si multimodal vidéo) |

### Phase 12. Matrice de couverture + Mapping Triade SERP

Croise les micro-intentions avec les couches sémantiques produites Phases 2-11. Vérifie qu'aucune micro-intention n'est orpheline.

**Mapping [[triade-serp|Triade SERP]].** Chaque livrable est tagué selon la phase Google qu'il nourrit.

| Couche produite | Phase Triade SERP cible | Mécanisme sous-jacent |
|---|---|---|
| Entités nommées + Structural Information | **Phase 1 — Document Ranking** (filtre d'admission) | BM25 + RankBrain |
| Concepts structurants + preuves + grounding + n-grams | **Phase 2 — Passage Ranking** (densité par bloc) | DPR / Muvera + BERT |
| FAQ stratégique + answer-first + Surprise Gap | **Phase 3 — Generation** (FS, AIO, citation LLM) | Grounding + Confidence Score |

Sans ce mapping, le rédacteur en aval ne sait pas où placer quoi.

**Livrable.** Matrice micro-intentions × couches + colonne Triade SERP par livrable.

### Phase 13. Feedback loop KB

À la fin de chaque exécution, Claude identifie les éléments à versionner dans le KB :

- 3 à 5 concepts originaux apparus dans la carte
- 1 à 3 angles divergents qui pourraient devenir doctrines maison
- Nouveaux mots ou expressions à intégrer en whitelist signature
- Nouveaux n-grams signature détectés
- Cas terrain chiffrés non encore documentés
- Acteurs concurrents identifiés à versionner dans /wiki/competitors/
- Verbatims Haute Surprise validés à archiver

**Livrable.** Liste de patches à appliquer au KB.

```
À ajouter à /wiki/concepts/ :
- concept-X.md (résumé en une phrase)

À ajouter à /wiki/entities/ :
- entité-Y.md (rôle dans le domaine)

À ajouter à /wiki/competitors/ :
- concurrent-Z.md (angle + faiblesse identifiée)

À ajouter à doctrine.md :
- doctrine-W (formulation tranchée)

À archiver dans /raw/verbatims/ :
- verbatim-V.md (frustration experte rare)

À archiver dans /wiki/lexique/ :
- n-gram-N.md (expression signature détectée)
```

L'utilisateur valide ou ajuste avant d'archiver. Sans cette phase, l'engine ne progresse pas. Avec, il s'auto-améliore à chaque passage.

---

## OUTPUT FINAL

Treize livrables (+ matrice de couverture + verdicts Phase 0 et 8c).

0. **Verdict Phase 0** (filtre stratégique informatif : PASS / WARN + annexe sous-niches si WARN)
1. Tableau micro-intentions (3 niveaux + profil + Action Engine flag)
2. **Tableau entités sémantiques pondérées (7 colonnes — poids + densité + cosinus simulé + justification + statut)**
3. **Tableau lexique signature (n-grams, co-occurrences, expressions multi-mots)**
4. Tableau pain points & verbatims Haute Surprise (+ 3 objections priorisées)
5. Tableau preuves quantitatives (Confidence Score + Freshness Guard)
6. Tableau multimodal
7. Tableau cartographie concurrentielle
8. **Phase 8 Gap analysis** : 8a Gap Competitive Map + 8b Content Gap Score + **8c Surprise Score Sémantique 0-100**
9. Tableau divergences Haute Surprise (calibrées Information Gain, positionnées contre acteurs + gaps)
10. Tableau FAQ stratégique FM (5-7 questions = 5-7 vecteurs)
11. Tableau Structural Information GEO (title / meta / H / schema)
12. Matrice couverture × Mapping Triade SERP
13. Liste patches KB à archiver

Aucun H1 final, aucun hook, aucune prose, aucun CTA.

---

## Éthique scraping et robots.txt

L'engine ne scrape jamais la SERP. C'est son principe fondateur.

Pour les autres formes de lecture web, règles strictes :

| Action | Règle |
|---|---|
| Lecture du KB local | Autorisée, c'est l'environnement de l'utilisateur. |
| Lecture d'un site tiers (média, blog, ressource publique) | **Uniquement si le robots.txt l'autorise pour l'agent utilisé.** |
| Lecture d'une étude / paper public (arxiv, hal, OSF, sites académiques) | Autorisée si robots.txt ouvert + respect du rate limit. |
| Scraping forcé contre une interdiction robots.txt | **Interdit.** Pas de bypass, pas de user-agent forgé, pas de contournement. |
| Scraping SERP Google / Bing / autres moteurs | **Interdit.** Violation ToS. |

Si une source potentiellement utile est bloquée par robots.txt, l'engine se rabat sur :
1. La connaissance training de Claude sur le sujet
2. Une demande explicite à l'utilisateur pour qu'il fournisse manuellement l'extrait (copier-coller)
3. L'omission documentée

Pas d'autre voie.

---

## Format prompt d'invocation

**Engine principal — Mode Création**
```
Lance l'engine carte sémantique sans SERP (v10).

Requête : [...]
Profil utilisateur :
- Pays/langue : [FR/FR par défaut]
- B2B/B2C + rôle : [...]
- Objectif : [Lead Gen / Conversion / Expertise FM]
- Secteur : [...]
- Audience (expertise) : [junior / expert / mixte]
- Localisation : [ville ou N/A]

Expertise unique (recommandé) : [une phrase]
Mode forcé (optionnel) : [bronze / silver / gold]
Sourcing externe (optionnel) : [oui / non, oui par défaut]
```

**Engine principal — Mode Audit**
```
Lance l'engine carte sémantique sans SERP (v10) — Mode AUDIT.

Requête cible : [...]
Profil utilisateur : [6 variables]
Contenu à auditer : [texte | chemin | URL]
Version cible (optionnel) : [refonte / update freshness / élargissement / migration]
Expertise unique (optionnel) : [...]
Mode forcé (optionnel) : [bronze / silver / gold]
```

**Mode 0 KB Bootstrap**
```
Lance Mode 0 KB Bootstrap.

Articles sources : [liste d'URLs ou chemin de dossier]
Destination KB : [chemin où créer les fichiers]
```

Si une info obligatoire manque, Claude pose une seule question groupée avant de produire.

---

## En aval de cet engine

La carte produite alimente la rédaction. Le rédacteur (humain ou skill éditorial) :

- Décide de l'architecture Hn à partir des micro-intentions et du tableau Structural Information GEO (Phase 11)
- Choisit le hook à partir du tableau divergence (Phase 9)
- Ordonne les blocs en fonction du profil utilisateur (Phase 1) et du mapping Triade SERP (Phase 12)
- Intègre les preuves (Phase 5) et entités (Phase 2 + Phase 3 lexique) en prose
- Spécifie les visuels à produire (Phase 6)
- Place les questions FAQ (Phase 10) en fin de page

Ces décisions relèvent d'un engine éditorial distinct (`seo-brief-contenu` puis `article-engine-pipeline`), ou d'une rédaction manuelle.

---

## Différence vs un outil de scraping SERP

Un outil de scraping te file une liste de termes statistiquement surreprésentés dans le top 10. Tu deviens la moyenne lexicale de tes concurrents.

Cet engine te file une carte typée de tout ce qui doit être présent pour traiter le sujet en profondeur, indépendamment de ce qui ranke. Tu construis le standard, tu ne le rattrapes pas.

---

## Section « Exemple appliqué » — à remplir au premier vrai test

À remplir :
- Requête testée
- Profil utilisateur saisi
- Mode détecté (Bronze / Silver / Gold)
- Verdict Phase 0 (filtre stratégique informatif)
- Décodage micro-intentionnel produit
- Tableau entités pondérées (avec cosinus simulé)
- Tableau n-grams
- Pain points & verbatims produits
- Sources externes consultées (et celles bloquées par robots.txt)
- Cartographie concurrentielle produite
- Phase 8 (3 vues + Surprise Score Sémantique 0-100)
- Tableaux Phases 9-11 produits
- Matrice de couverture finale + mapping Triade SERP
- Patches KB suggérés en Phase 13

---

# SKILL CLAUDE — `seo-preparation-semantique`

Section opérationnelle. Installé dans `/Users/timothee/.claude/skills/seo-preparation-semantique/SKILL.md` (v10 synchronisé).

```yaml
---
name: seo-preparation-semantique
description: |
  Engine de préparation sémantique sans scraping SERP. Deux modes : CRÉATION (requête → carte vierge en 11 couches) et AUDIT (contenu existant → diff vs carte attendue + plan de correction P0/P1/P2).

  Format de sortie (v10) : entités sémantiques pondérées (poids 0-1 + densité cible + cosinus simulé + justification + statut), lexique signature (n-grams + co-occurrences), pain points & verbatims Haute Surprise, preuves quantitatives (Confidence Score + Freshness Guard), multimodal, cartographie concurrentielle, Gap analysis 3 vues (Gap Competitive Map + Content Gap Score + Surprise Score Sémantique 0-100), divergence calibrée Information Gain, FAQ stratégique FM, Structural Information GEO, matrice couverture × Mapping Triade SERP, patches KB.

  Phase 0 informative (jamais bloquante) : alerte sur head term saturé / multi-intentions et propose sous-niches en annexe, mais produit toujours la carte complète.

  Embeddings simulés : cosinus Phase 2 calibré sur le corpus Claude, marqué « simulé » dans chaque sortie. Pas de vraie API embedding — honnête sur le calcul.

  TOUJOURS utiliser ce skill quand l'utilisateur dit :
  - Mode Création : "prépare la sémantique", "carte sémantique", "préparation sémantique", "engine sémantique", "tout ce que ma page doit contenir", "fais-moi l'analyse sémantique de [requête]", "lance l'engine sur [requête]", "sémantique sans SERP", "analyse sémantique [mot-clé]", "prépa sémantique [requête]", "entités pondérées [requête]", "surprise score sémantique de [requête]".
  - Mode Audit : "audite la sémantique de", "audit sémantique de cette page", "ma page couvre-t-elle [requête]", "compare ce contenu à la carte sémantique attendue", "qu'est-ce qui manque à mon article sur [requête]", "diff sémantique", "audit de couverture sémantique", "ma page ne ranke pas — qu'est-ce qui lui manque", "plan de correction sémantique".

  Ce skill remplace les outils de scraping SERP (Surfer, NeuronWriter, etc.). Il se branche en amont de `seo-brief-contenu` (qui construit la structure Hn) et de `article-engine-pipeline` (qui rédige). Il NE produit pas la rédaction, ni la structure Hn finale, ni le hook. Il produit la matière sémantique brute qui les alimente.

  Diffère de `seo-entites-vectorielles` (4 catégories d'entités seulement, pas de Gap analysis, pas de Surprise Score Sémantique, pas de n-grams) en couvrant 13 phases dont la Gap analysis 3 vues. Diffère de `seo-geo-audit` qui note 7 scores algorithmiques de qualité — ici on mesure la complétude par couche, pas la qualité par score. Les deux s'enchaînent : Audit (couverture) puis geo-audit (qualité).
---

# Skill — Préparation sémantique sans SERP (v10)

## Détecter le mode

Si l'utilisateur fournit **uniquement une requête + un profil** → Mode **CRÉATION**.

Si l'utilisateur fournit **en plus un contenu** (texte collé, chemin de fichier `*.md` / `*.html`, ou URL publique) → Mode **AUDIT**.

Si ambigu, demander : « Tu veux créer la carte sémantique d'une page à écrire, ou auditer un contenu existant ? »

## Input requis — Mode Création

| Variable | Valeur attendue | Obligatoire |
|---|---|---|
| Requête cible | mot pour mot | Oui |
| Pays / langue | FR/FR par défaut | Oui |
| B2B/B2C + rôle | « B2B — CMO SaaS 50p » | Oui |
| Objectif | Lead Gen / Conversion / Expertise FM | Oui |
| Secteur | nommé | Oui |
| Audience (expertise) | junior / expert / mixte | Oui |
| Localisation | ville ou « N/A » | Oui |
| Expertise unique | une phrase | Recommandé |
| Mode forcé | bronze / silver / gold | Optionnel |

## Input requis — Mode Audit (en plus des inputs Création)

| Variable | Valeur attendue | Obligatoire |
|---|---|---|
| Contenu à auditer | texte markdown collé, chemin local, URL publique (robots.txt OK) | Oui |
| Version cible | refonte / update freshness / élargissement d'intention / migration | Recommandé |

Si une variable obligatoire manque, Claude pose **une seule question groupée** avant de produire.

## Pipeline (13 phases)

```
Phase 0 — Filtre stratégique (informatif, jamais bloquant)
   │  alerte WARN éventuelle + annexe sous-niches
   ▼ GO toujours
Phase 1 — Décodage micro-intentionnel + Action Engine flag
Phase 2 — Entités sémantiques pondérées (poids + densité + cosinus simulé + justif + statut)
Phase 3 — Lexique signature (n-grams + co-occurrences)
Phase 4 — Pain points & verbatims Haute Surprise
Phase 5 — Preuves quantitatives (Confidence Score + Freshness Guard)
Phase 6 — Vecteurs multimodaux
Phase 7 — Cartographie concurrentielle sans SERP (5-10 acteurs)
Phase 8 — Gap analysis 3 vues :
   8a. Gap Competitive Map (matrice acteur × concept)
   8b. Content Gap Score (% standard vs % surprise)
   8c. Surprise Score Sémantique 0-100
Phase 9 — Divergence calibrée Information Gain (Quotation +41%, Stats +34%, Sources +29%)
Phase 10 — FAQ stratégique FM (5-7 vecteurs latents)
Phase 11 — Structural Information GEO (title/meta/H/schema)
Phase 12 — Matrice couverture × Mapping Triade SERP
Phase 13 — Feedback loop KB (patches à archiver)
```

## Règles absolues

- **Aucun scraping SERP**, jamais. Pas Google, pas Bing, pas autre moteur.
- **Robots.txt strict** pour tout WebFetch. Si bloqué : training Claude + demande à l'utilisateur, jamais bypass.
- **Cosinus simulé toujours marqué** : chaque sortie Phase 2 + Phase 8c doit inclure l'avertissement « *simulé par projection corpus Claude, non calibré mathématiquement* ».
- **Confidence Score obligatoire** sur chaque preuve chiffrée. Si basse ou inconnue → placeholder `[À SOURCER]`. Aucun chiffre inventé pour gonfler le Grounding Score.
- **Freshness Guard** : preuves > 36 mois omises sauf paper fondateur.
- **Phase 0 jamais bloquante** : alerte WARN éventuelle + propose sous-niches en annexe, mais produit toujours la carte complète.
- **Ne pas rédiger** : pas de H1 final, pas de hook, pas d'architecture Hn finale, pas de CTA, pas de prose narrative.
- **Une page = une intention** (pureté vectorielle). Si pluralité d'intentions détectée Phase 0.3, signaler en WARN + proposer N sous-cartes en annexe.
- **Anti-cliché obligatoire** dans la couche pain points : pas de « je veux du ROI », pas de « je veux des résultats ».
- **Phase 2 — Justification obligatoire** : chaque entité doit avoir une justification courte (paper, doctrine, co-occurrence). Pas d'entité arbitraire.

## Output obligatoire

13 tableaux livrables + matrice de couverture mappée sur la Triade SERP + Surprise Score Sémantique 0-100 + verdict global + liste patches KB.

Format markdown structuré, prêt à alimenter `seo-brief-contenu` (structure Hn) ou `article-engine-pipeline` (rédaction complète).

## Enchaînement workflow

**En amont** : aucun (c'est la première brique).

**En aval, selon objectif** :
- `seo-brief-contenu` → structure Hn complète à partir de la carte
- `article-engine-pipeline` → rédaction complète à partir de la carte (passe par seo-workflow-article)
- `seo-product-led-seo` → si Action Engine flag déclenché (intention Do)
- `seo-donnees-structurees` → implémentation JSON-LD à partir de la Phase 11
- `seo-geo-audit` → en aval d'une rédaction, audit qualité 7 scores (complémentaire à Mode Audit qui mesure la couverture)

## Sauvegarde

Output dans `wiki/queries/prepa-semantique-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md (vault seo-kb).

## Concepts liés

[[purete-vectorielle]] · [[triade-serp]] · [[information-gain]] · [[surprise-gap]] · [[surprise-metric]] · [[grounding-score]] · [[confidence-score]] · [[mots-cles-actionnels]] · [[angle-differenciant-mot-cle]] · [[data-proprietaire]] · [[fully-meets]] · [[passage-ranking]] · [[structural-information-geo]] · [[answer-first-pattern]] · [[freshness-guard]] · [[rrf]] · [[aeo]] · [[know-simple-know-do]] · [[product-led-seo]] · [[anti-ai-writing]]
```
