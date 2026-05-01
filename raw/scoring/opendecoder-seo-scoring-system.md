# OpenDecoder SEO Scoring System v2

## Systeme de notation de contenus SEO inspire d'OpenDecoder (Mo et al., 2026)

**Principe fondateur** : Comme OpenDecoder pondere explicitement chaque document pour guider l'attention du LLM, ce systeme pondere explicitement chaque dimension d'un contenu SEO pour guider les decisions d'optimisation.

**Principe d'execution** : Le LLM est le moteur de scoring. Aucun scraping SERP. Chaque evaluation repose sur des requetes LLM structurees qui exploitent la connaissance semantique du modele — exactement comme dans le paper ou c'est le LLM qui juge la qualite des documents, pas un outil externe.

---

## Architecture globale

**Input** : Contenu de la page (texte + structure) + mot-cle cible + (optionnel) donnees GSC

**4 scores** :
- S_Pertinence (score principal) - equivalent du Retriever Score
- S_Qualite (bonus) - equivalent du LLM Ranking Score
- S_Potentiel (bonus) - equivalent du QPP Score
- S_AEO (bonus) - extension GEO Sentinel : survie face aux moteurs IA

**Formule d'agregation** (adaptee du paper + GEO Sentinel) :

```
S_final = S_Pertinence + 0.5 x (S_Qualite + S_Potentiel + S_AEO)
S_100 = (S_final / 2.5) x 100
```

Comme dans OpenDecoder : la pertinence est dominante (coeff 1), les 3 autres sont supplementaires (coeff 0.5 chacun).
Scores bruts (0-1) utilises directement.

---
---

## SCORE 1 : S_Pertinence (Relevance Score)

> Equivalent OpenDecoder : S_Ret (Retriever Score)
> Role : Mesure l'alignement semantique entre le contenu et l'intention de recherche
> Poids dans l'agregation : DOMINANT (coefficient 1)

---

### Sous-score 1.1 : Couverture des entites (S_ent)

**Poids** : 0.40

**Source de verite** : Requete LLM (pas de scraping SERP)

**Etape A — Generation des entites attendues**

Le LLM recoit le prompt structure suivant :

```
ROLE : Expert en recherche vectorielle et SEO semantique.

REQUETE CIBLE : "[mot-cle]"

TACHE : Genere la liste exhaustive des entites qu'un moteur de recherche 
s'attend a trouver dans une page qui ranke en top 3 sur cette requete.

Classe chaque entite en 3 niveaux :
- PRIMAIRE (incontournable — toute page serieuse la mentionne)
- SECONDAIRE (attendue — renforce la pertinence)
- TERTIAIRE (experte — marque la profondeur, mais pas obligatoire)

FORMAT DE SORTIE STRICT :
PRIMAIRES: [entite1], [entite2], ...
SECONDAIRES: [entite1], [entite2], ...
TERTIAIRES: [entite1], [entite2], ...
```

**Etape B — Matching avec le contenu evalue**

Pour chaque entite generee, le LLM verifie sa presence dans le contenu :
- Present explicitement = TROUVE
- Present via synonyme proche = TROUVE (0.8)
- Absent = NON TROUVE

**Formule** :

```
S_ent = (primaires_trouvees x 3 + secondaires_trouvees x 2 + tertiaires_trouvees x 1)
        / (primaires_total x 3 + secondaires_total x 2 + tertiaires_total x 1)
```

Note : les synonymes trouves comptent a 0.8 de leur poids (un synonyme n'est pas un match parfait).

**Exemple concret** :
- Requete : "remplacer batterie voiture electrique"
- LLM genere :
  - Primaires : prix, duree de vie, kWh, garantie, Tesla = 5
  - Secondaires : reconditionne, ADEME, degradation, autonomie = 4
  - Tertiaires : SOH, BMS, cycle de charge = 3
- Contenu evalue contient : prix (exact), duree de vie (exact), kWh (exact), garantie (exact), reconditionne (exact), autonomie (exact), SOH (exact) + "capacite restante" comme synonyme de degradation (0.8)
- Calcul : primaires = 4x3=12, secondaires = 1x2 + 1x(2x0.8)=2+1.6=3.6, tertiaires = 1x1=1
- S_ent = (12 + 3.6 + 1) / (5x3 + 4x2 + 3x1) = 16.6/26 = **0.638**

---

### Sous-score 1.2 : Alignement d'intention (S_int)

**Poids** : 0.25

**Source de verite** : Requete LLM

**Etape A — Classification de l'intention**

Le LLM recoit :

```
REQUETE CIBLE : "[mot-cle]"

Classifie cette requete dans UNE intention principale :
- KNOW-SIMPLE : l'utilisateur veut une reponse factuelle courte
- KNOW : l'utilisateur veut comprendre en profondeur
- DO : l'utilisateur veut accomplir une action
- COMMERCIAL : l'utilisateur veut comparer avant de choisir

Justifie en 1 phrase.

FORMAT : INTENTION: [type] | JUSTIFICATION: [1 phrase]
```

**Etape B — Classification du format du contenu**

Le LLM analyse le contenu fourni et classifie son format :
- Reponse directe (definition, paragraphe court)
- Guide/Article (structure, etapes, explications)
- Outil/CTA (interactif, page action)
- Comparatif/Classement (tableau, versus, ranking)

**Etape C — Matrice de correspondance**

| Format du contenu \ Intention | Know-Simple | Know | Do | Commercial |
|-------------------------------|-------------|------|----|------------|
| **Reponse directe** | 1.0 | 0.4 | 0.1 | 0.2 |
| **Guide/Article** | 0.5 | 1.0 | 0.3 | 0.5 |
| **Outil/CTA** | 0.1 | 0.3 | 1.0 | 0.4 |
| **Comparatif/Classement** | 0.2 | 0.5 | 0.4 | 1.0 |

Le score est lu dans la matrice au croisement intention x format.

---

### Sous-score 1.3 : Couverture du champ semantique (S_sem)

**Poids** : 0.25

**Source de verite** : Requete LLM (pas de scraping SERP)

**Etape A — Generation des clusters semantiques attendus**

Le LLM recoit :

```
ROLE : Architecte de contenu SEO specialise en topical authority.

REQUETE CIBLE : "[mot-cle]"

TACHE : Identifie les CLUSTERS THEMATIQUES qu'une page exhaustive 
sur ce sujet DOIT couvrir pour satisfaire pleinement l'intention.

Chaque cluster = un sous-sujet coherent et distinct.
Ne liste PAS des mots-cles individuels — liste des THEMES.

Vise 5 a 10 clusters maximum.

FORMAT DE SORTIE STRICT :
CLUSTER 1: [nom du cluster] | DESCRIPTION: [ce que ce cluster doit couvrir]
CLUSTER 2: [nom du cluster] | DESCRIPTION: [ce que ce cluster doit couvrir]
...
```

**Etape B — Evaluation de la couverture**

Pour chaque cluster, le LLM evalue le contenu :
- 1.0 = cluster traite en profondeur (section dediee, details, exemples)
- 0.5 = cluster mentionne mais pas developpe (evoque en passant)
- 0 = cluster absent

**Bonus Hn** : +0.1 par cluster qui apparait dans un titre H2 ou H3 (cap total a 1.0)

**Formule** :

```
S_sem_base = somme(score_par_cluster) / nombre_total_clusters
S_sem = min(1.0, S_sem_base + 0.1 x clusters_presents_dans_Hn)
```

**Exemple** :
- Requete : "remplacer batterie voiture electrique"
- LLM genere 6 clusters : [cout/prix], [process technique], [quand remplacer], [choix prestataire], [garantie/assurance], [neuf vs reconditionne]
- Evaluation : 1 + 0.5 + 1 + 0 + 1 + 1 = 4.5
- S_sem_base = 4.5/6 = 0.75
- 3 clusters dans les Hn → +0.3
- S_sem = min(1.0, 1.05) = **1.0**

---

### Sous-score 1.4 : Signaux on-page (S_onpage)

**Poids** : 0.10

**Source de verite** : Analyse directe du contenu (pas de LLM necessaire — checklist mecanique)

**Checklist binaire** (chaque element = 0 ou 1) :

| Signal | Verification |
|--------|-------------|
| Mot-cle (ou variation tres proche) dans le H1 | Analyse du contenu |
| Mot-cle dans les 100 premiers mots | Analyse du contenu |
| Mot-cle dans au moins 1 sous-titre H2 | Analyse du contenu |
| Mot-cle dans l'URL (si disponible) | Analyse de l'URL |
| Mot-cle dans la meta description (si disponible) | Analyse des meta |

**Formule** :

```
S_onpage = elements_presents / 5
```

Note : Si URL et meta ne sont pas fournis (contenu brut uniquement), le denominateur passe a 3 (on ne penalise pas l'absence de donnees).

---

### FORMULE COMPLETE S_Pertinence

```
S_Pertinence = 0.40 x S_ent + 0.25 x S_int + 0.25 x S_sem + 0.10 x S_onpage
```

**Grille d'interpretation** :

| Score | Verdict | Action type |
|-------|---------|-------------|
| 0.85 - 1.00 | Alignement excellent | Maintenir, optimiser a la marge |
| 0.65 - 0.84 | Bon alignement | Ajouter entites/clusters manquants |
| 0.40 - 0.64 | Alignement moyen | Retravail semantique significatif |
| 0.00 - 0.39 | Desalignement | Repenser le contenu depuis l'intention |

---
---

## SCORE 2 : S_Qualite (Editorial Quality Score)

> Equivalent OpenDecoder : S_Rank (LLM Ranking Score)
> Role : Evaluation LLM de la qualite intrinseque du contenu
> Poids dans l'agregation : SUPPLEMENTAIRE (coefficient 0.5)

**Source de verite** : Le LLM analyse directement le contenu fourni. Aucune comparaison avec des pages externes — on juge le contenu sur ses propres merites.

---

### Sous-score 2.1 : Signaux E-E-A-T (S_eeat)

**Poids** : 0.35

**Prompt LLM** :

```
ROLE : Quality Rater Google appliquant les guidelines E-E-A-T.

CONTENU A EVALUER : [contenu complet]

Evalue chacun des 5 criteres suivants sur une echelle 0 / 0.5 / 1 :

1. EXPERIENCE : L'auteur a-t-il vecu/teste ce qu'il decrit ?
   0 = aucune marque d'experience
   0.5 = mention vague ("d'apres notre experience")
   1 = cas precis avec dates, chiffres, contexte personnel

2. EXPERTISE : Le niveau technique est-il adapte au sujet ?
   0 = contenu superficiel, recopiable par n'importe qui
   0.5 = correct mais sans profondeur specifique
   1 = vocabulaire expert, nuances techniques, mises en garde d'expert

3. AUTORITE : Qui parle et pourquoi c'est credible ?
   0 = pas d'auteur identifie, pas de source
   0.5 = auteur mentionne sans credentials
   1 = bio avec credentials, marque reconnue, certifications

4. CONFIANCE : Le contenu est-il transparent et source ?
   0 = affirmations gratuites, pas de sources
   0.5 = quelques sources generiques
   1 = sources primaires citees, limites reconnues, transparence

5. DONNEES : Y a-t-il des preuves quantitatives ?
   0 = aucun chiffre
   0.5 = quelques chiffres non sources
   1 = donnees precises, sourcees, datees

FORMAT : EXPERIENCE: [score] | EXPERTISE: [score] | AUTORITE: [score] | 
         CONFIANCE: [score] | DONNEES: [score]
JUSTIFICATION: [1 phrase par critere]
```

**Formule** :

```
S_eeat = (experience + expertise + autorite + confiance + donnees) / 5
```

---

### Sous-score 2.2 : Profondeur du contenu (S_depth)

**Poids** : 0.30

**Methode en 2 composantes** :

**Composante A : Couverture des sous-sujets (60%)**

Reutilise les clusters generes dans S_sem (Score 1.3). Pour chaque cluster, le LLM evalue la PROFONDEUR de traitement (pas juste la presence) :
- 0 = pas traite
- 0.5 = mentionne sans developper (<50 mots, pas d'exemples)
- 1 = traite en profondeur (>150 mots, exemples, nuances, donnees)

```
Couverture_profonde = somme(scores_profondeur) / nombre_clusters
```

**Composante B : Insights uniques (40%)**

Le LLM recoit :

```
CONTENU A EVALUER : [contenu complet]
REQUETE CIBLE : "[mot-cle]"

Evalue le niveau d'ORIGINALITE de ce contenu. 
Un contenu original apporte des informations qu'on ne trouve PAS 
dans un article generique sur ce sujet.

Cherche specifiquement :
- Donnees proprietaires (stats internes, resultats d'experience)
- Angles inedits (perspective contre-intuitive, lien inattendu)
- Elements "Haute Surprise" (concepts experts que <10% des articles couvrent)
- Methodologie unique ou framework original

Score :
0 = paraphrase standard, aucune originalite
0.25 = 1 element original mineur
0.50 = 2-3 elements originaux (donnees propres, angle unique)
0.75 = multiples insights originaux + au moins 1 element Haute Surprise
1.0 = contenu substantiellement unique, impossible a reproduire sans expertise terrain

FORMAT : SCORE: [valeur] | ELEMENTS_ORIGINAUX: [liste]
```

**Formule** :

```
S_depth = 0.60 x Couverture_profonde + 0.40 x Insights_uniques
```

---

### Sous-score 2.3 : Qualite de la structure (S_struct)

**Poids** : 0.20

**Prompt LLM** :

```
CONTENU A EVALUER : [structure Hn du contenu]

Evalue chaque critere (0 ou 1) :

1. HIERARCHIE Hn : H1 unique, H2 sequentiels, H3 subordonnes, 
   pas de saut de niveau (ex: H1 → H3 sans H2) ?

2. PASSAGE-RANKABILITE : Chaque H2 repond-il a une question distincte 
   identifiable ? (Un bot pourrait extraire chaque section comme reponse 
   autonome a une sous-question ?)

3. OPPORTUNITE FEATURED SNIPPET : Au moins 1 section est-elle formatee 
   pour la position 0 ? (definition en <50 mots, liste numerotee, 
   tableau comparatif, reponse directe)

4. ELEMENTS VISUELS STRUCTURANTS : Presence d'au moins 1 tableau, 
   liste structuree, ou element non-paragraphe ?

FORMAT : HIERARCHIE: [0/1] | PASSAGE: [0/1] | SNIPPET: [0/1] | VISUELS: [0/1]
```

**Formule** :

```
S_struct = (hierarchie + passage + snippet + visuels) / 4
```

---

### Sous-score 2.4 : Lisibilite / UX redactionnelle (S_read)

**Poids** : 0.15

**Prompt LLM** :

```
CONTENU A EVALUER : [contenu complet]

Evalue chaque critere de lisibilite (0 ou 1) :

1. PARAGRAPHES COURTS : Moyenne < 4 phrases par paragraphe ?
2. VARIATION DU RYTHME : Mix de phrases courtes et longues, pas monotone ?
3. TRANSITIONS : Connecteurs logiques entre les sections ?
4. ACTIONNABILITE : Au moins 1 takeaway actionnable ou CTA par section H2 ?

FORMAT : PARAGRAPHES: [0/1] | RYTHME: [0/1] | TRANSITIONS: [0/1] | ACTION: [0/1]
```

**Formule** :

```
S_read = (paragraphes + rythme + transitions + action) / 4
```

---

### FORMULE COMPLETE S_Qualite

```
S_Qualite = 0.35 x S_eeat + 0.30 x S_depth + 0.20 x S_struct + 0.15 x S_read
```

**Grille d'interpretation** :

| Score | Verdict | Action type |
|-------|---------|-------------|
| 0.85 - 1.00 | Qualite exceptionnelle | Contenu de reference, maintenir |
| 0.65 - 0.84 | Bonne qualite | Renforcer E-E-A-T ou profondeur |
| 0.40 - 0.64 | Qualite moyenne | Retravail editorial significatif |
| 0.00 - 0.39 | Qualite faible | Rewrite complet necessaire |

---
---

## SCORE 3 : S_Potentiel (Potential/Difficulty Score)

> Equivalent OpenDecoder : S_QPP (Query Performance Prediction)
> Role : Estime la capacite du contenu a performer face a la concurrence
> Poids dans l'agregation : SUPPLEMENTAIRE (coefficient 0.5)

**Source de verite** : Le LLM utilise sa connaissance du paysage SEO pour predire la difficulte et les opportunites. Pas de scraping SERP.

---

### Sous-score 3.1 : Paysage concurrentiel estime (S_comp)

**Poids** : 0.30

**Prompt LLM** :

```
ROLE : Consultant SEO senior avec 10 ans d'experience en analyse SERP.

REQUETE CIBLE : "[mot-cle]"

Estime le paysage concurrentiel pour cette requete. 
Base-toi sur ta connaissance du type de resultats qui rankent 
generalement pour ce type de requete.

Questions a te poser :
- Ce type de requete est-il domine par des marques/institutions ?
- Y a-t-il de la place pour des acteurs independants ?
- Le sujet est-il couvert par Wikipedia, des sites gouvernementaux ?
- Les forums/UGC sont-ils presents (signal de faible concurrence) ?
- La requete est-elle YMYL (Your Money Your Life) — barrieres E-E-A-T elevees ?

Estime le pourcentage de resultats "faibles" (forums, UGC, contenu thin, 
pages outdated) qu'on trouverait typiquement dans le top 10 pour ce type 
de requete.

FORMAT : 
ESTIMATION_FAIBLES: [nombre sur 10] 
YMYL: [oui/non]
DOMINANCE_MARQUES: [faible/moyenne/forte]
JUSTIFICATION: [2-3 phrases]
```

**Formule** :

```
S_comp = estimation_faibles / 10
```

Si YMYL = oui, appliquer un malus de -0.1 (la barriere E-E-A-T rend le ranking plus difficile meme en presence de resultats faibles) :

```
S_comp_final = max(0, S_comp - 0.1) si YMYL, sinon S_comp
```

---

### Sous-score 3.2 : Completude des formats (S_format)

**Poids** : 0.30

*Renomme de S_gap → S_format : on ne compare plus a des concurrents scraipes, on compare aux formats ATTENDUS par l'intention.*

**Prompt LLM** :

```
ROLE : UX Designer specialise en content design pour le SEO.

REQUETE CIBLE : "[mot-cle]"
INTENTION IDENTIFIEE : "[intention du S_int]"

Quels TYPES DE CONTENUS / FORMATS une page optimale devrait-elle 
inclure pour satisfaire pleinement cette intention ?

Ne liste que les formats REELLEMENT attendus pour ce type de requete.
Pas de liste generique — chaque format doit etre justifie par l'intention.

FORMAT DE SORTIE :
FORMAT 1: [type] | JUSTIFICATION: [pourquoi ce format est attendu ici]
FORMAT 2: [type] | JUSTIFICATION: [pourquoi]
...
(5 a 8 formats maximum)
```

**Etape B — Matching avec le contenu**

Le LLM verifie la presence de chaque format dans le contenu evalue :
- 1 = present
- 0 = absent

**Formule** :

```
S_format = formats_presents / formats_attendus_total
```

**Exemple** :
- Requete : "remplacer batterie voiture electrique"
- LLM genere les formats attendus : tableau prix par modele, guide etape par etape, FAQ, checklist signes d'alerte, comparatif neuf/reconditionne, coordonnees prestataires
- Contenu a : tableau prix, guide, FAQ, comparatif = 4/6
- S_format = **0.667**

---

### Sous-score 3.3 : Signaux d'opportunite (S_opp)

**Poids** : 0.25

**Prompt LLM** :

```
ROLE : Growth SEO strategiste.

REQUETE CIBLE : "[mot-cle]"
CONTENU EVALUE : [resume du contenu en 3-5 lignes]

Evalue les signaux d'opportunite pour ce contenu sur cette requete.
Score chaque signal 0 ou 1 :

1. SUJET EN EVOLUTION : Le sujet a-t-il significativement evolue 
   ces 12 derniers mois ? (nouvelles reglementations, nouveaux acteurs, 
   changement de pratiques) — Si oui, les contenus existants sont 
   probablement outdated = opportunite.

2. FORMAT DIFFERENTIANT : Le contenu propose-t-il un format que la 
   majorite des pages sur ce sujet n'ont PAS ? (calculateur, outil 
   interactif, template, video, infographie originale)

3. ANGLE INEXPLOITE : Le contenu traite-t-il un sous-angle que les 
   pages classiques sur ce sujet ignorent ? (micro-intention non couverte, 
   perspective contraire, niche specifique)

4. AVANTAGE E-E-A-T : Le contenu possede-t-il un signal d'autorite 
   ou d'experience que les contenus generiques n'ont pas ? 
   (donnees proprietaires, expertise terrain, cas client reel)

FORMAT : EVOLUTION: [0/1] | FORMAT_DIFF: [0/1] | ANGLE: [0/1] | EEAT_ADV: [0/1]
JUSTIFICATION: [1 phrase par signal]
```

**Formule** :

```
S_opp = (evolution + format_diff + angle + eeat_adv) / 4
```

---

### Sous-score 3.4 : Position actuelle (S_pos)

**Poids** : 0.15

**Source** : Donnees GSC si disponibles. Sinon, default a 0.5 (neutre).

| Position actuelle | Score |
|------------------|-------|
| 1-3 | 1.0 |
| 4-7 | 0.8 |
| 8-10 | 0.6 |
| 11-20 | 0.4 |
| 21-50 | 0.2 |
| 51-100 | 0.1 |
| Non indexe / >100 | 0.05 |
| Pas de donnees GSC | 0.5 (neutre) |

---

### FORMULE COMPLETE S_Potentiel

```
S_Potentiel = 0.30 x S_comp + 0.30 x S_format + 0.25 x S_opp + 0.15 x S_pos
```

**Grille d'interpretation** :

| Score | Verdict | Action type |
|-------|---------|-------------|
| 0.75 - 1.00 | Fort potentiel | Foncer, ROI quasi-certain |
| 0.50 - 0.74 | Potentiel modere | Investir avec optimisations ciblees |
| 0.25 - 0.49 | Potentiel limite | Effort substantiel, ROI incertain |
| 0.00 - 0.24 | Potentiel faible | Pivoter ou abandonner |

---
---

## SCORE 4 : S_AEO (Answer Engine Optimization Score)

> Pas d'equivalent direct dans OpenDecoder — extension du framework
> Role : Mesure la capacite du contenu a survivre aux filtres des moteurs IA (SGE, SearchGPT, Perplexity)
> Poids dans l'agregation : SUPPLEMENTAIRE (coefficient 0.5)
> Source : GEO Sentinel v2.1 (Boussardon) — restructure avec des rubrics calculables

**Source de verite** : Le LLM analyse le contenu sous l'angle specifique de l'extractibilite et de la memorisation par les systemes RAG/IA.

---

### Sous-score 4.1 : Surprise Score (S_surprise)

**Poids** : 0.25

*Inspire de GEO Sentinel Score 1. Eleve en score de plein droit (etait enterre a 4.2% du poids total dans S_Qualite).*

**Prompt LLM** :

```
ROLE : Detecteur de banalite algorithmique.

CONTENU A EVALUER : [contenu complet]
REQUETE CIBLE : "[mot-cle]"

Un LLM generatif (GPT, Claude, Gemini) pourrait generer une reponse 
a cette requete depuis ses donnees d'entrainement.

Ta mission : identifier ce que CE contenu apporte que l'IA ne peut PAS 
inventer. Ce sont les elements "Haute Surprise".

Criteres de Haute Surprise :
- Donnee proprietaire (stat interne, resultat d'experience perso)
- These contraire au consensus ("tout le monde dit X, la realite c'est Y")
- Detail technique que seul un praticien connait (piege, edge case, hack)
- Anecdote verifiable d'echec ou de reussite avec contexte precis

Compte le nombre d'elements Haute Surprise dans le contenu.

FORMAT :
ELEMENTS_TROUVES: [nombre]
LISTE: [element 1] | [element 2] | ...
```

**Grille de scoring** :

| Elements Haute Surprise | Score |
|------------------------|-------|
| 0 | 0.0 (contenu 100% generique, une IA fait pareil) |
| 1 | 0.25 |
| 2-3 | 0.50 |
| 4-5 | 0.75 |
| 6+ | 1.0 (contenu irreplacable par une IA) |

---

### Sous-score 4.2 : Grounding Density (S_grounding)

**Poids** : 0.30

*Inspire de GEO Sentinel Score 2. Remplace l'evaluation binaire "y a-t-il des chiffres ?" par une mesure de DENSITE quantitative.*

**Prompt LLM** :

```
ROLE : Auditeur factuel.

CONTENU A EVALUER : [contenu complet]

Compte les "preuves atomiques" presentes dans le contenu.
Une preuve atomique = un fait verifiable et precis :
- Chiffre precis + source ("79 000 OF actifs, source Cereq")
- Reference legale ("article L.6313-1 du Code du travail")
- Date specifique ("depuis janvier 2022")
- Nom propre d'entite ("CERFA n°10782*04")
- Donnee quantitative contextuelle ("56% sont des micro-structures")

NE PAS compter :
- Affirmations vagues ("beaucoup d'entreprises")
- Chiffres ronds non sources ("environ 50%")
- Opinions ("c'est la meilleure approche")

FORMAT :
NOMBRE_PREUVES: [nombre]
NOMBRE_MOTS_TOTAL: [estimation]
DENSITE: [preuves par 100 mots]
```

**Grille de scoring** :

| Densite (preuves / 100 mots) | Score |
|------------------------------|-------|
| >= 2.0 | 1.0 (excellent — le contenu est un reservoir de faits) |
| 1.5 - 1.99 | 0.8 |
| 1.0 - 1.49 | 0.6 |
| 0.5 - 0.99 | 0.3 |
| < 0.5 | 0.1 (quasi aucun fait verifiable — contenu "opinion") |

---

### Sous-score 4.3 : RAG Structurer (S_rag)

**Poids** : 0.25

*Inspire de GEO Sentinel Score 5. Mesure la lisibilite MACHINE, pas humaine (complement de S_struct qui mesure la lisibilite Google).*

**Prompt LLM** :

```
ROLE : Ingenieur RAG (Retrieval-Augmented Generation).

CONTENU A EVALUER : [structure + contenu]

Evalue si ce contenu est optimise pour etre EXTRAIT et CITE par un 
systeme RAG (ChatGPT, Perplexity, Google AI Overview).

Un retriever decoupe le contenu en passages et cherche la meilleure 
correspondance a une question. Score chaque critere 0 ou 1 :

1. PROXIMITE TITRE/REPONSE : Chaque H2 est-il suivi d'une reponse 
   directe dans les 30 premiers mots ? (pas d'intro generique avant 
   la substance)

2. SECTIONS AUTONOMES : Chaque section peut-elle etre extraite seule 
   et rester comprehensible sans le reste de la page ?

3. DONNEES STRUCTUREES : Les faits cles sont-ils dans des formats 
   extractibles ? (tableaux, listes a puces, definitions)

4. FORMAT Q&A EXPLICITE : Au moins une section utilise-t-elle le 
   format question/reponse explicite (FAQ, "Comment...?" suivi 
   d'une reponse directe) ?

FORMAT : PROXIMITE: [0/1] | AUTONOMIE: [0/1] | STRUCTURE: [0/1] | QA: [0/1]
JUSTIFICATION: [1 phrase par critere]
```

**Formule** :

```
S_rag = (proximite + autonomie + structure + qa) / 4
```

---

### Sous-score 4.4 : Freshness Guard (S_fresh)

**Poids** : 0.20

*Inspire de GEO Sentinel Score 6. Completement absent de la v1 d'OpenDecoder.*

**Prompt LLM** :

```
ROLE : Analyste de recence algorithmique.

CONTENU A EVALUER : [contenu complet]

Les moteurs IA et Google privilegient les contenus qui signalent 
explicitement leur fraicheur. Evalue les signaux temporels.

Score chaque critere 0 ou 1 :

1. ANNEE DANS LE TITRE : Le titre ou H1 contient-il une annee 
   recente (annee en cours ou annee -1) ?

2. SOURCES DATEES : Le corps du texte cite-t-il des sources 
   avec des dates recentes (<18 mois) ?

3. SIGNAL DE MISE A JOUR : Le contenu contient-il des marqueurs 
   explicites de fraicheur ? ("mis a jour en [date]", "nouveaute 2026", 
   "seuil 2026", "depuis [evenement recent]")

4. ABSENCE D'OBSOLESCENCE : Le contenu NE contient-il PAS de 
   references obsoletes presentees comme actuelles ? 
   (ancien seuil, ancienne reglementation, lien mort)

FORMAT : ANNEE_TITRE: [0/1] | SOURCES_DATEES: [0/1] | MAJ_SIGNAL: [0/1] | PAS_OBSOLETE: [0/1]
```

**Formule** :

```
S_fresh = (annee_titre + sources_datees + maj_signal + pas_obsolete) / 4
```

---

### FORMULE COMPLETE S_AEO

```
S_AEO = 0.25 x S_surprise + 0.30 x S_grounding + 0.25 x S_rag + 0.20 x S_fresh
```

**Grille d'interpretation** :

| Score | Verdict | Action type |
|-------|---------|-------------|
| 0.85 - 1.00 | IA-ready | Le contenu survivra aux filtres SGE/Perplexity |
| 0.65 - 0.84 | Bon | Quelques ajustements pour l'extractibilite |
| 0.40 - 0.64 | Vulnerable | Risque de non-citation par les moteurs IA |
| 0.00 - 0.39 | Invisible | Le contenu sera ignore par les systemes RAG |

---
---

## AGREGATION ET SCORE FINAL

### Adaptation de la normalisation du paper

Dans OpenDecoder, la max-normalisation compare N documents entre eux pour la meme requete. 
Ici on evalue 4 dimensions d'une MEME page — les scores sont deja tous entre 0 et 1.

**Decision** : Scores bruts pour l'agregation. Comparaison relative reservee a la priorisation.

### Formule d'agregation (4 scores)

```
S_final = S_Pertinence + 0.5 x (S_Qualite + S_Potentiel + S_AEO)
```

Logique inchangee : la pertinence est dominante (coefficient 1), 
les trois autres sont supplementaires (coefficient 0.5 chacun).
S_AEO a le meme poids que S_Qualite et S_Potentiel — c'est un bonus 
de meme rang, pas un score secondaire.

**Range** : 0 a 2.5

### Score final 0-100

```
S_100 = (S_final / 2.5) x 100
```

---

### Verification des comportements attendus (4 scores)

| Profil | P | Q | Pot | AEO | Score /100 | Prio |
|--------|---|---|-----|-----|-----------|------|
| Excellent partout | 0.95 | 0.90 | 0.85 | 0.90 | 91.0 | Pot |
| Page excellente | 0.90 | 0.85 | 0.70 | 0.80 | 83.0 | Pot |
| Correcte | 0.70 | 0.60 | 0.50 | 0.55 | 61.0 | Pot |
| Bon contenu, SERP dur | 0.80 | 0.75 | 0.20 | 0.70 | 65.0 | Pot |
| Pertinent mais creux | 0.85 | 0.30 | 0.50 | 0.35 | 57.0 | Qual |
| Top SEO mais invisible IA | 0.90 | 0.85 | 0.70 | 0.20 | 71.0 | AEO |
| Moyen SEO mais IA-ready | 0.60 | 0.55 | 0.45 | 0.90 | 62.0 | Pot |
| Faible partout | 0.40 | 0.35 | 0.30 | 0.25 | 34.0 | AEO |

---

## GRILLE DE DECISION FINALE

| Score /100 | Verdict | Decision |
|------------|---------|----------|
| 85-100 | Excellent | Contenu pret a performer en SEO et AEO. Monitoring. |
| 70-84 | Bon | 1-2 axes d'amelioration cibles. Quick wins probables. |
| 50-69 | Moyen | Retravail necessaire. Prioriser la dimension la plus faible. |
| 30-49 | Faible | Refonte significative ou pivot strategique. |
| 0-29 | Critique | Le contenu ne repond pas a l'intention. Recommencer. |

---

## LOGIQUE DE PRIORISATION (inspiree d'OpenDecoder)

Dans le paper, le modele "regarde d'abord les documents les mieux scores" et 
"ignore presque les documents bruit". Pour l'optimisation, on fait l'inverse : 
on travaille d'abord la dimension la plus faible car c'est la que le ROI marginal 
est le plus fort.

**Regle** : Trier les 4 scores bruts par ordre croissant → optimiser en priorite le plus bas.

**Exceptions strategiques** : 
- Si S_Potentiel < 0.25 → questionner la pertinence strategique avant tout.
- Si S_AEO < 0.30 → le contenu est invisible pour les IA. Priorite absolue si la strategie vise aussi l'AEO.

---

## PARALLELE AVEC OPENDECODER — RESUME

| OpenDecoder (RAG) | Notre systeme (SEO + AEO) |
|-------------------|---------------------------|
| S_Ret : similarite vectorielle doc/query | S_Pertinence : alignement semantique page/intention (via LLM) |
| S_Rank : LLM juge la qualite du doc | S_Qualite : LLM evalue la qualite editoriale |
| S_QPP : difficulte de la query + fiabilite | S_Potentiel : difficulte estimee + opportunites (via LLM) |
| — (pas d'equivalent) | S_AEO : survie face aux moteurs IA (GEO Sentinel) |
| Agregation : S_Ret + 0.5 x (S_Rank + S_QPP) | S_Pert + 0.5 x (S_Qual + S_Pot + S_AEO) |
| Le LLM evalue les documents | Le LLM evalue le contenu, le paysage, ET l'extractibilite IA |
| Score → poids par token → modifie l'attention | Score → poids par dimension → guide les priorites |
| Doc bruit → tokens ignores | Dimension faible → optimisation prioritaire |

---

## INVENTAIRE DES REQUETES LLM

Resume de toutes les requetes LLM necessaires pour un scoring complet :

| Etape | Requete LLM | Input | Output |
|-------|------------|-------|--------|
| 1.1A | Generation entites attendues | Mot-cle | Liste entites (P/S/T) |
| 1.1B | Matching entites | Contenu + liste entites | Scores presence |
| 1.2A | Classification intention | Mot-cle | Type d'intention |
| 1.2B | Classification format | Contenu | Type de format |
| 1.3A | Generation clusters semantiques | Mot-cle | Liste clusters |
| 1.3B | Evaluation couverture clusters | Contenu + clusters | Scores par cluster |
| 2.1 | Evaluation E-E-A-T | Contenu | 5 scores (0/0.5/1) |
| 2.2A | Profondeur par cluster | Contenu + clusters | Scores profondeur |
| 2.2B | Evaluation originalite | Contenu + mot-cle | Score insights |
| 2.3 | Evaluation structure | Structure Hn | 4 scores binaires |
| 2.4 | Evaluation lisibilite | Contenu | 4 scores binaires |
| 3.1 | Estimation paysage concurrentiel | Mot-cle | Estimation + YMYL |
| 3.2A | Generation formats attendus | Mot-cle + intention | Liste formats |
| 3.2B | Matching formats | Contenu + formats | Scores presence |
| 3.3 | Evaluation opportunites | Mot-cle + resume contenu | 4 scores binaires |
| 4.1 | Detection Haute Surprise | Contenu + mot-cle | Nombre + liste elements |
| 4.2 | Comptage preuves atomiques | Contenu | Densite preuves/100 mots |
| 4.3 | Evaluation RAG readiness | Contenu + structure | 4 scores binaires |
| 4.4 | Evaluation fraicheur | Contenu | 4 scores binaires |

**Total : 19 requetes LLM** pour un scoring complet.
Certaines peuvent etre fusionnees :
- 1.1A + 1.3A → "cartographie semantique"
- 4.1 + 2.2B → "originalite et surprise" (proches)
- 4.2 + 2.1 → "grounding et E-E-A-T" (memes signaux)
Optimisation possible : **13-15 requetes en pratique**.
