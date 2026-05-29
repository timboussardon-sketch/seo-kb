---
slug: engine-densite-semantique-sans-serp
title: "Engine — Carte sémantique sans SERP (13 phases, cosinus simulé, Surprise Score Sémantique, skill Claude)"
author: "Timothée Boussardon"
date_added: 2026-05-11
date_updated: 2026-05-27
type: methode
audience: seo-rédacteur
topic: entites-semantiques-aeo
status: draft
version: v10
---

# Engine — Carte sémantique sans SERP

## Pourquoi la sémantique devient le verrou de visibilité IA

Pendant quinze ans, le SEO se jouait sur trois leviers : mot-clé, backlink, autorité de domaine. La sémantique restait un terme de chercheur. En 2026, c'est l'inverse — c'est devenu *le* signal sur lequel les moteurs IA arbitrent qui ressort dans une réponse générée, et qui disparaît.

Quatre études récentes convergent sur cette bascule.

**SAGEO Arena (Kim et al., Yonsei, fév. 2025 — arXiv:2602.12187).** Premier benchmark qui mesure la GEO à chaque étape du pipeline (retrieval → reranking → generation). Verdict : optimiser uniquement le body text **dégrade** la visibilité (−4.54 Hit Rate au retrieval, −16% ΔRank). Optimiser la couche structurelle (title, meta, headings, schema) apporte **+22% Hit Rate**, et combinée à l'ajout de statistiques sourcées, **+35%**. Traduction : ce que tu mets dans le corps compte moins que comment tu structures ta sémantique.

**GEO Aggarwal (KDD'24, Princeton — arXiv:2311.09735).** Premier framework formel d'optimisation pour moteurs génératifs, testé sur 10 000 requêtes. Le Keyword Stuffing est **mort** sur les LLM (zéro amélioration mesurée, parfois dégradation). À l'inverse : **Quotation Addition +41%**, **Statistics Addition +34%**, **Cite Sources +29%** sur le Position-Adjusted Word Count. Le ton autoritaire seul : +13% — bien moins efficace que la citation verbatim. La sémantique qui ressort dans les LLM est faite d'entités citées, de chiffres datés et de sources, pas de mots-clés densifiés.

**Retrieval Collapse (NAVER, ACM Web Conference 2026 — arXiv:2602.16136).** À 67% de pollution du pool de contenu par du synthétique, **80% de l'exposition** devient compromise — et le système semble continuer de tourner. Les rerankers LLM filtrent le malicieux mais ne détectent pas la dérive synthétique normale. Conséquence : les moteurs IA vont devenir critiquement dépendants des signaux d'humanité vérifiable — verbatims experts, cas terrain chiffrés, lexique signature qu'un agrégateur ne sait pas inventer.

**MAGEO (Tsinghua / Tencent, ACL 2026 Findings, avril 2026 — arXiv:2604.19516).** Démonte les approches GEO qui optimisent page par page. Propose un système de 3 agents (planificateur + éditeur + évaluateur de fidélité) qui mémorise les stratégies gagnantes et les réutilise. Gain simultané en visibilité ET en exactitude des citations sur 3 moteurs grand public. La GEO bascule de l'artisanat vers l'industriel — les playbooks réutilisables battent les bricolages ponctuels.

Quatre études, une même conclusion : la sémantique qui ressort dans les LLM n'est pas une wordlist scrapée du top 10. C'est une carte structurelle — entités pondérées, n-grams signature, preuves citées, angles divergents — qu'il faut produire en amont, pas extraire en aval. C'est exactement ce que fait l'engine ci-dessous.

---

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

## 1. Outil classique vs Claude sémantique

Les outils sémantiques du marché scrapent le top 10 Google et te listent les termes statistiquement surreprésentés. Tu deviens la moyenne lexicale de tes concurrents. Cet engine fait l'inverse : il construit la carte depuis l'intention, ta doctrine et le corpus du domaine — sans regarder ce qui ranke.

| Axe                    | Outil classique (scraping SERP)                                | Claude sémantique (sans SERP)                                                                                           |
| ---------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Méthode                | Scrape le top 10, compte les termes surreprésentés             | Décode l'intention, mobilise les entités du domaine, croise avec ta doctrine                                            |
| Source de la carte     | Le consensus du top 10 = ce que tes concurrents ont déjà écrit | Ton intention + le corpus du domaine + ton expertise propre                                                             |
| Différenciation        | Tu converges vers la moyenne lexicale du top 10                | Tu construis le standard à partir d'un angle non couvert                                                                |
| Couches couvertes      | 1-2 (mots-clés, parfois questions)                             | 11 couches (entités, n-grams, pain points, preuves, multimodal, gap analysis, divergence, FAQ, structurel, Triade SERP) |
| Expertise propriétaire | Aucune (le scraping n'a pas accès à ton vault)                 | Intègre ton KB, ta voix, tes cas clients                                                                                |
| Robustesse             | Casse à chaque mise à jour algo qui rebrasse le top 10         | Stable, ancrée sur l'intention pas sur la SERP du jour                                                                  |
| Conformité ToS         | Viole les conditions d'utilisation Google (scraping SERP)      | 100% conforme — lit uniquement ce que robots.txt autorise                                                               |
| Output rédacteur       | Wordlist à insérer dans le texte                               | Brief structuré directement exploitable par la rédaction                                                                |

Le moat ne réside pas dans l'outil — n'importe qui peut lancer cet engine. Il réside dans ce que tu donnes en input (voir partie 3).

---

## 2. Ce que Claude fait : tâches et actions

Onze tâches sémantiques, exécutées en chaîne sur une requête + un profil + ton expertise. Chacune produit un livrable directement exploitable par la rédaction.

### 1. Décode l'intention de recherche
Casse la requête en trois niveaux : intention principale ([[know-simple-know-do|Know-Simple / Know / Do]]), 3-5 sous-intentions parallèles, 15-25 micro-intentions granulaires. Reformule le profil utilisateur en une phrase tranchante. Si l'intention est `Do`, flag obligatoire : un outil interactif est requis pour viser [[fully-meets]].

### 2. Pondère les entités sémantiques
30 à 50 entités classées par type (Concept, Algo, Tool, Method, Doctrine, Person, Location), chacune avec son poids 0-1, sa densité cible dans le texte (%), une similarité cosinus *simulée* avec la requête, une justification (paper, doctrine, co-occurrence) et un statut P1/P2/P3. Aucune entité arbitraire — chacune doit pouvoir être défendue.

### 3. Repère le lexique signature
Bigrams, trigrams et expressions multi-mots du domaine, avec leur fréquence attendue sur 2000 mots et leur co-occurrence dominante. Distingue les n-grams P1 (standard du domaine) des n-grams signature P2 (vocabulaire propre au média). Force la cohérence lexicale du corps.

### 4. Sort les vrais pain points
Tableau de 10 lignes minimum : pain point précis nommé + verbatim Haute Surprise (citation experte rarement verbalisée) + preuve atomique chiffrée. Refus systématique du cliché (« je veux du ROI », « je veux des résultats »). Priorise 3 objections critiques selon fréquence × intensité × différenciation.

### 5. Génère les preuves quantitatives
Chiffres datés avec source primaire, études, papers, jurisprudences, cas terrain. Chaque preuve porte un [[confidence-score|Confidence Score]] (haute / moyenne / basse) et un Freshness Guard (< 18 mois / 18-36 mois / > 36 mois). Si confidence basse ou source douteuse : placeholder `[À SOURCER]` obligatoire. Aucun chiffre inventé pour gonfler le [[grounding-score]].

### 6. Liste les éléments multimodaux
Tableaux, schémas, captures, photos, vidéos courtes, audio, données interactives. Pour chacun : objectif sémantique + format + micro-intention couverte.

### 7. Cartographie les concurrents sans SERP
5 à 10 acteurs dominants identifiés depuis le training Claude + le KB interne + WebSearch ciblé (robots.txt OK). Pour chacun : nom + type (média / agence / expert / institution / plateforme) + angle dominant défendu + faiblesse identifiable.

### 8. Identifie les gaps marché
Trois vues complémentaires :
- **Matrice acteur × concept** — quelles entités P1 sont absentes chez les concurrents (= opportunités d'attaque)
- **Content Gap Score** — % de couverture standard du domaine + % de couverture surprise
- **Surprise Score Sémantique 0-100** — moyenne pondérée du ratio entités propriétaires, ratio verbatims experts, distance lexicale vs consensus, présence Quotation + Statistics

### 9. Construit les angles divergents
Pour chaque axe de divergence : acteur dominant ciblé + entité de la gap map attaquée + type d'inversion (paresseuse vs juste mais contre-intuitive) + forme (citation verbatim, stat propriétaire, cas terrain). Calibré sur le benchmark [[information-gain]] Aggarwal KDD'24 : Quotation Addition +41%, Statistics Addition +34%, Cite Sources +29%, ton autoritaire seul +13% seulement.

### 10. Rédige les questions FAQ stratégiques
5 à 7 questions = 5 à 7 vecteurs sémantiques distincts, chacune répondant à une micro-intention non couverte par le corps. Réponses courtes, citables isolément ([[answer-first-pattern]], AI Overview ready). La FAQ absorbe la périphérie sémantique pour préserver la [[purete-vectorielle|pureté vectorielle]] du corps.

### 11. Spécifie les contraintes structurelles
Title (≈10 mots), meta description (155 char), H1, H2 (5-8 prévus), schema.org adapté à l'intention (Article + FAQPage + LocalBusiness + HowTo + VideoObject). Pas la rédaction Hn finale, mais les contraintes sémantiques que la rédaction devra respecter. Finding SAGEO Arena 2025 ([[structural-information-geo]]) : optimiser le body seul dégrade le retrieval (−4.54 Hit Rate), structural seul +22%, structural + statistics combinés +35%.

### Tâches transverses

**Matrice de couverture finale** — vérifie qu'aucune micro-intention n'est orpheline, mappe chaque livrable sur la phase [[triade-serp|Triade SERP]] qu'il nourrit (Document Ranking / Passage Ranking / Generation).

**Feedback loop KB** — identifie les concepts originaux apparus, les angles divergents qui pourraient devenir doctrines maison, les verbatims experts à archiver. Liste de patches à appliquer au KB. Sans cette tâche, l'engine ne progresse pas — avec, il s'auto-améliore à chaque passage.

Ce que Claude ne fait pas : pas de H1 final, pas de hook, pas d'architecture Hn finale, pas de CTA, pas de prose narrative. La rédaction est une étape séparée, branchée en aval.

---

## 3. Ce que tu donnes en contexte (pour maximiser le résultat)

Plus tu donnes de matière brute, plus la carte sortie est signature. Sans expertise propriétaire, l'engine produit une carte correcte mais réplicable — n'importe qui avec Claude la produit aussi. Le moat n'est pas l'engine, c'est ce que tu y verses.

| # | Élément de contexte | Catégorie | Statut | Effet sur la carte |
|---|---|---|---|---|
| 1 | Requête cible (mot pour mot, pas de reformulation) | Requête | ✅ Obligatoire | Décode l'intention principale et les micro-intentions |
| 2 | Pays / langue (FR/FR par défaut) | Profil | ✅ Obligatoire | Vocabulaire, références culturelles, sources |
| 3 | B2B / B2C + rôle (ex. « B2B — CMO SaaS 50p ») | Profil | ✅ Obligatoire | Verrouille les verbatims et les preuves |
| 4 | Objectif (Lead Gen / Conversion / Expertise) | Profil | ✅ Obligatoire | Calibre l'Action Engine flag (intention Do) |
| 5 | Secteur (SaaS, immobilier, BTP, juridique…) | Profil | ✅ Obligatoire | Filtre les entités et les cas terrain |
| 6 | Audience (junior / expert / mixte) | Profil | ✅ Obligatoire | Calibre la profondeur lexicale |
| 7 | Localisation (ville, région ou « N/A ») | Profil | ✅ Obligatoire | Ancrage local SEO |
| 8 | Destination du KB (chemin local, structure plate ou sous-dossiers) | Sortie | ✅ Obligatoire | Sans, les patches KB en fin de run restent inertes |
| 9 | Expertise unique (une phrase signature) | Voix | ⚡ Recommandé | Active la couche divergence avec ton angle propre |
| 10 | Articles publiés (20 minimum, 30-50 idéal, 3-7 thématiques) | Corpus publié | ⚡ Recommandé | Pose la base de la voix et des positions tranchées |
| 11 | Newsletters publiées ou drafts | Corpus non publié | 💎 Densifie fort | Voix plus tranchée que sur le blog, positions assumées |
| 12 | Posts LinkedIn (les tiens, exportés) | Corpus non publié | 💎 Densifie fort | Concepts atomiques formulés en 200 mots |
| 13 | Transcripts d'interviews ou podcasts | Corpus non publié | 💎 Densifie fort | Vocabulaire signature au naturel, expressions récurrentes |
| 14 | Briefs commerciaux ou propositions client | Corpus non publié | 💎 Densifie fort | Cas terrain chiffrés, objections traitées |
| 15 | Notes Obsidian / Notion (même brouillon) | Corpus non publié | 💎 Densifie fort | Concepts en cours de formulation |
| 16 | Slides de conférences ou formations | Corpus non publié | 💎 Densifie fort | Doctrines distillées en 1-2 phrases |
| 17 | Liste de 10 expressions que tu utilises souvent | Cadrage | 🔧 Optionnel | Accélère la détection de la whitelist signature |
| 18 | Liste de 10 mots ou formules que tu bannis | Cadrage | 🔧 Optionnel | Pré-remplit la banlist sans extraction |
| 19 | Liste de 3-5 concurrents que tu refuses de citer | Cadrage | 🔧 Optionnel | Calibre l'anti-positionnement |
| 20 | 3 cas clients dont tu es fier (1 paragraphe chacun) | Cadrage | 🔧 Optionnel | Densifie les cas terrain chiffrés |

Évite, dans le corpus que tu fournis : articles génériques type « 10 best practices », contenus opportunistes SEO sans position tranchée, contenus rédigés par un freelance qui n'a pas ta voix. Ils diluent ta signature au lieu de la révéler.

### Format prompt d'invocation — Bootstrap KB

```
Lance le KB Bootstrap.

Articles publiés : [chemin du dossier ou liste d'URLs]
Matière non publiée : [chemin du dossier]
Banlist initiale (optionnel) : [...]
Whitelist initiale (optionnel) : [...]
Destination KB : [chemin]
```

Plus tu donnes de matière brute, moins tu auras à arbitrer en sortie. Sans les éléments de cadrage (lignes 17-20), Claude extrait à l'aveugle et tu valides manuellement plus de propositions.

---

## 4. Le skill entier (autonome, copier-coller direct)

Skill Claude **100% autonome**. Aucune dépendance externe, aucun vault à brancher, aucune doctrine maison à lire ailleurs. Tu copies le bloc ci-dessous dans un fichier, tu redémarres, ça marche.

### Installation (30 secondes)

1. Crée le dossier : `mkdir -p ~/.claude/skills/seo-preparation-semantique/`
2. Copie tout le bloc ci-dessous dans `~/.claude/skills/seo-preparation-semantique/SKILL.md`
3. Redémarre la session Claude Code (ou la fenêtre Claude Desktop)
4. Vérifie que le skill est chargé : `/skills` doit lister `seo-preparation-semantique`
5. Lance-le en disant « prépare la sémantique de [ta requête] »

### Premier appel — exemple

```
Lance la préparation sémantique sur « consultant seo » pour un profil B2B
indépendant en France, objectif Lead Gen, secteur SaaS, audience expert,
basé à Lyon.

Mon expertise unique : 15 ans dans le SEO B2B, j'ai vu passer 3 cycles
d'algos majeurs et je sais ce qui survit aux refontes.
```

Claude pose une seule question groupée si une variable obligatoire manque, sinon il sort la carte complète des 13 phases.

### Le skill complet (à copier dans `~/.claude/skills/seo-preparation-semantique/SKILL.md`)

````markdown
---
name: seo-preparation-semantique
description: |
  Engine autonome de préparation sémantique sans scraping SERP. Deux modes : CRÉATION (requête → carte vierge en 13 phases) et AUDIT (contenu existant → diff vs carte attendue + plan de correction P0/P1/P2).

  Format de sortie : entités sémantiques pondérées (poids 0-1 + densité cible + cosinus simulé + justification + statut P1/P2/P3), lexique signature (n-grams + co-occurrences), pain points & verbatims Haute Surprise, preuves quantitatives (Confidence Score + Freshness Guard), multimodal, cartographie concurrentielle (5-10 acteurs), Gap analysis 3 vues (Gap Competitive Map + Content Gap Score + Surprise Score Sémantique 0-100), divergence calibrée Information Gain, FAQ stratégique (5-7 vecteurs), Structural Information GEO, matrice couverture × Mapping Triade SERP, patches KB.

  Phase 0 informative (jamais bloquante) : alerte sur head term saturé / multi-intentions et propose sous-niches en annexe, mais produit toujours la carte complète.

  Embeddings simulés : cosinus Phase 2 calibré sur le corpus Claude, marqué « simulé » dans chaque sortie. Pas de vraie API embedding — honnête sur le calcul.

  TOUJOURS utiliser ce skill quand l'utilisateur dit :
  - Mode Création : "prépare la sémantique", "carte sémantique", "préparation sémantique", "engine sémantique", "tout ce que ma page doit contenir", "fais-moi l'analyse sémantique de [requête]", "lance l'engine sur [requête]", "sémantique sans SERP", "analyse sémantique [mot-clé]", "prépa sémantique [requête]", "entités pondérées [requête]", "surprise score sémantique de [requête]".
  - Mode Audit : "audite la sémantique de", "audit sémantique de cette page", "ma page couvre-t-elle [requête]", "compare ce contenu à la carte sémantique attendue", "qu'est-ce qui manque à mon article sur [requête]", "diff sémantique", "audit de couverture sémantique", "ma page ne ranke pas — qu'est-ce qui lui manque", "plan de correction sémantique".

  Ce skill remplace les outils de scraping SERP. Il produit la matière sémantique brute (carte). Il NE produit pas la rédaction, ni la structure Hn finale, ni le hook — ces étapes sont en aval.
---

# Skill — Préparation sémantique sans SERP

Engine autonome qui produit la carte sémantique complète d'une page à écrire (Mode Création) ou audite la couverture sémantique d'un contenu existant (Mode Audit). Aucun scraping de SERP. La carte se construit depuis l'intention de la requête, le corpus du domaine, et l'expertise propre fournie en input.

## Détecter le mode

- **Requête + profil seuls** → Mode **CRÉATION**.
- **Requête + profil + contenu fourni** (texte collé, chemin de fichier, ou URL publique) → Mode **AUDIT**.
- Si ambigu, demander : « Tu veux créer la carte sémantique d'une page à écrire, ou auditer un contenu existant ? »

## Inputs requis

### Mode Création

| Variable | Valeur attendue | Statut |
|---|---|---|
| Requête cible | mot pour mot | Obligatoire |
| Pays / langue | FR/FR par défaut | Obligatoire |
| B2B/B2C + rôle | « B2B — CMO SaaS 50p » | Obligatoire |
| Objectif | Lead Gen / Conversion / Expertise | Obligatoire |
| Secteur | nommé | Obligatoire |
| Audience | junior / expert / mixte | Obligatoire |
| Localisation | ville ou « N/A » | Obligatoire |
| Expertise unique | une phrase signature | Recommandé |

### Mode Audit (en plus des inputs Création)

| Variable | Valeur attendue | Statut |
|---|---|---|
| Contenu à auditer | texte collé, chemin local, ou URL publique (robots.txt OK) | Obligatoire |
| Version cible | refonte / update freshness / élargissement / migration | Recommandé |

Si une variable obligatoire manque, poser **une seule question groupée** avant de produire.

## Pipeline — 13 phases en chaîne

```
Phase 0 — Filtre stratégique (informatif, jamais bloquant)
Phase 1 — Décodage micro-intentionnel + Action Engine flag
Phase 2 — Entités sémantiques pondérées (7 colonnes)
Phase 3 — Lexique signature (n-grams + co-occurrences)
Phase 4 — Pain points & verbatims Haute Surprise
Phase 5 — Preuves quantitatives (Confidence Score + Freshness Guard)
Phase 6 — Vecteurs multimodaux
Phase 7 — Cartographie concurrentielle (5-10 acteurs)
Phase 8 — Gap analysis 3 vues (8a Gap Competitive Map / 8b Content Gap Score / 8c Surprise Score Sémantique 0-100)
Phase 9 — Divergence calibrée Information Gain
Phase 10 — FAQ stratégique (5-7 vecteurs latents)
Phase 11 — Structural Information GEO
Phase 12 — Matrice couverture × Mapping Triade SERP
Phase 13 — Feedback loop KB (patches à archiver)
```

## Format détaillé par phase

### Phase 0 — Filtre stratégique (informatif, jamais bloquant)

Trois tests en amont. L'engine ne bloque jamais, il alerte et continue.

**0.1 Test de substitution LLM** — deux questions binaires :
1. ChatGPT répond déjà à cette requête à 80% ?
2. Si oui, peut-il faire mieux que l'utilisateur ?

Verdict : PASS / WARN / WARN sévère (flag « divergence obligatoire » en Phase 9 si WARN).

**0.2 Angle différenciant** — la requête est-elle un head term tapé pour 10 intentions différentes par 100 personnes différentes (`agence SEO`, `plombier Paris`) ? Si oui : WARN + propose des sous-niches en annexe (ex. `plombier 15e urgence nuit`).

**0.3 Pureté vectorielle** — UNE intention dominante ou plusieurs ? Si plusieurs : WARN + propose découpage en N pages.

Livrable Phase 0 :

```
PHASE 0 — Filtre stratégique
- Test LLM : [PASS / WARN — raison]
- Angle différenciant : [PASS / WARN — sous-niches proposées : (1) ... (2) ...]
- Pureté vectorielle : [PASS / WARN — N intentions : (1) ... (2) ...]
Verdict global : [GO franche / GO avec avertissement]
```

L'engine continue toujours vers Phase 1.

### Phase 1 — Décodage micro-intentionnel + Action Engine flag

Trois niveaux d'intention :
- **Intention principale** : taxonomie Know-Simple / Know / Do (remplace TOFU/MOFU/BOFU)
- **Sous-intentions** : 3 à 5 questions parallèles
- **Micro-intentions** : 15 à 25 questions granulaires

Profil utilisateur reformulé en une phrase tranchante.

**Action Engine flag** : si l'intention principale = `Do`, flag obligatoire — un outil interactif (calculateur, simulateur, générateur, audit) est requis pour viser Fully Meets. Une page Know textuelle ne ranke pas sur intention Do.

### Phase 2 — Entités sémantiques pondérées (format obligatoire 7 colonnes)

30 à 50+ entités par run. Format strict :

```
| # | Entité | Type | Poids (0-1) | Densité cible (%) | Cosinus estimé requête (0-1) | Justification | Statut |
|---|---|---|---|---|---|---|---|
| 1 | `passage ranking` | Concept | 0.94 | 0.8% | 0.91 | Brique du grounding, citée dans 3 papers MIRAS | P1 critique |
| 2 | `BM25` | Algo | 0.87 | 0.3% | 0.79 | Mécanique sous-jacente du Document Ranking | P1 critique |
```

- **Type** : Person / Concept / Tool / Method / Doctrine / Event / Location / Algo
- **Poids** : > 0.8 = entité pivot, 0.5-0.8 = supportive, < 0.5 = périphérique
- **Densité cible** : pivots 0.5-1%, supportives 0.2-0.5%, périphériques < 0.2% (sur 2000 mots)
- **Cosinus estimé** : projection Claude de la similarité entité ↔ requête, **marqué « simulé »** en pied de tableau
- **Justification obligatoire** : courte (paper, doctrine, co-occurrence). Aucune entité arbitraire.
- **Statut** : P1 critique (sans, ne ranke pas) / P2 (supportif) / P3 (bonus)

Pied de tableau obligatoire : *« Cosinus simulé par projection corpus Claude, non calibré mathématiquement. Pour calibration exacte : API embeddings Voyage / Cohere / OpenAI. »*

### Phase 3 — Lexique signature (n-grams + co-occurrences)

```
| N-gram / expression | Type | Fréquence attendue (sur 2000 mots) | Co-occurrence dominante | Statut |
|---|---|---|---|---|
| « passage ancré » | bigram | 2-3x | grounding-score, featured snippet | P1 |
| « ranker dans ChatGPT » | trigram | 1-2x | AIO, citation LLM | P1 |
```

Bigrams (2 mots), trigrams (3 mots), expressions multi-mots (> 3). Co-occurrence dominante = avec quelles autres entités/concepts ce n-gram apparaît systématiquement. Statut P1 = standard du domaine / P2 = bonus signature.

### Phase 4 — Pain points & verbatims Haute Surprise

Tableau de 10 lignes minimum :

```
| Micro-intention / Pain Point | Verbatim « Haute Surprise » | Preuve atomique attendue |
|---|---|---|
| [Frein précis nommé] | [Citation experte rarement verbalisée — zéro cliché] | [Sujet + Verbe + Donnée chiffrée] |
```

**Règles verbatims** :
- Frustration experte ou technique propre au métier
- Vocabulaire signature (verrouillé sur B2B/B2C du profil)
- Refus strict du cliché (« je veux du ROI », « je veux des résultats »)

Exemple :
- ❌ Cliché : « Je veux voir des résultats concrets »
- ✅ Haute Surprise : « La dernière agence m'envoyait des rapports de 40 pages où le seul KPI lisible était le nombre de backlinks, jamais croisé avec mon CRM »

**Règles preuves atomiques** : format binaire ou chiffré, vérifiable.
- ✅ « 73% des prospects B2B refusent un devis sans estimation immédiate »
- ❌ « Nous offrons un excellent service »

**Priorisation finale** : sortir 3 objections critiques selon `fréquence × intensité × différenciation`.

### Phase 5 — Preuves quantitatives (Confidence Score + Freshness Guard)

Génération depuis le training : chiffres datés avec source primaire, études, papers, jurisprudence, cas terrain.

**Confidence Score par preuve** :

| Niveau | Critère | Action |
|---|---|---|
| Haute | Source primaire récente identifiée, paper avec DOI, organisme officiel | Utilisable telle quelle |
| Moyenne | Source connue mais non vérifiée à 100% | Utilisable + fact-check obligatoire en aval |
| Basse | Reformulation indirecte, source secondaire, donnée approximative | **Remplacer par `[À SOURCER]`** |

**Règle absolue** : si confidence basse ou source inconnue → placeholder `[À SOURCER]` obligatoire. Aucun chiffre inventé.

**Freshness Guard** :

| Âge de la donnée | Statut |
|---|---|
| < 18 mois | Preuve fraîche — OK |
| 18-36 mois | Flag « à actualiser » — utilisable mais signalée |
| > 36 mois | Omise sauf paper fondateur (étude structurante non substituable) |

Format livrable : preuve + source + confidence + datation + flag fraîcheur + micro-intention couverte.

### Phase 6 — Vecteurs multimodaux

Tableaux, schémas, captures, photos, vidéos courtes, audio, données interactives. Pour chacun : objectif sémantique + format + micro-intention couverte.

### Phase 7 — Cartographie concurrentielle sans SERP

5 à 10 acteurs dominants identifiés depuis : training Claude + WebSearch ciblé (robots.txt OK) + KB interne si fourni.

```
| Acteur | Type | Angle dominant | Faiblesse identifiable |
|---|---|---|---|
```

Type : média / agence / expert individuel / institution / plateforme. Angle dominant = la thèse défendue. Faiblesse = ce qu'ils ne traitent pas, ne disent pas, ou refusent de voir.

### Phase 8 — Gap analysis (3 vues)

**8a. Gap Competitive Map** — matrice acteur × concept (P1 critiques uniquement, sinon trop chargé) :

```
| Acteur | Entité A | Entité B | Entité C | Entité D | Entité E | Gap exploitable |
|---|---|---|---|---|---|---|
| Acteur X | ✅ | ✅ | ❌ | ✅ | ❌ | Entités C + E |
| **GAP MARCHÉ** | — | — | — | — | **0/3** | **E = gap général** |
```

Une entité avec gap commun (jamais traitée par les 3 acteurs analysés) = opportunité d'attaque prioritaire.

**8b. Content Gap Score** :

| Axe | Définition | Cible |
|---|---|---|
| Couverture standard | % entités P1 que 80%+ des concurrents traitent | ≥ 70% (franchir Document Ranking) |
| Couverture surprise | % entités P1 traitées par < 20% des concurrents | ≥ 30% (passer Information Gain) |

Verdict :
- Standard < 70% → page n'a pas la base sémantique, ne ranke pas
- Standard ≥ 70% mais Surprise < 30% → indexable mais Low Surprise, oubliée par les modèles IA
- Standard ≥ 70% ET Surprise ≥ 30% → cible idéale

**8c. Surprise Score Sémantique 0-100** — moyenne pondérée de 4 composantes :

```
30% — Ratio entités propriétaires / entités totales
20% — Ratio verbatims Haute Surprise / verbatims totaux
25% — Distance lexicale propriétaire ↔ consensus (1 - cosinus simulé)
25% — Présence Quotation Addition + Statistics Addition (preuves verbatim + chiffrées avec source)
```

Échelle :
- **0-30** = Médiocrité statistique (oubli mémoriel garanti, refonte ou abandon)
- **30-60** = Acceptable mais réplicable (améliorations P1 obligatoires)
- **60-85** = Information Gain validé (publication OK)
- **85-100** = Inversion experte maximale

Avertissement obligatoire : *« Score calibré sur projection corpus Claude. Pour calibration exacte : audit GEO avec scores algorithmiques. »*

### Phase 9 — Divergence calibrée Information Gain

Benchmark Aggarwal KDD'24 (arXiv:2311.09735) — gains PAWC mesurés vs baseline :

| Méthode | Gain PAWC |
|---|---|
| Quotation Addition (citation verbatim) | +41% |
| Statistics Addition | +34% |
| Cite Sources | +29% |
| Authoritative (ton seul) | +13% |

Privilégier les angles divergents qui s'appuient sur **citation verbatim + statistiques sourcées**, pas sur le ton autoritaire.

Pour chaque axe de divergence, exiger :
- Acteur dominant ciblé (issu Phase 7)
- Entité de la Gap Competitive Map attaquée (Phase 8a)
- Type d'inversion (paresseuse vs juste mais contre-intuitive)
- Forme (citation verbatim, stat propriétaire, cas terrain, donnée externe sourcée)

Critère final : un expert dirait *« tiens, je n'avais pas vu ça comme ça »*.

### Phase 10 — FAQ stratégique (5-7 vecteurs latents)

5 à 7 questions = 5 à 7 vecteurs sémantiques distincts. Zéro chevauchement avec le corps.

Règles strictes :
- Chaque question répond à une micro-intention **non couverte par le corps**
- Réponse courte, actionnable, citable isolément (AI Overview ready)
- Verrouillage B2B/B2C selon profil Phase 1
- Aucune question pédagogique générique (« qu'est-ce que X »)
- Priorité aux questions Know / Comparatif / Do non traitées dans le corps

La FAQ absorbe la périphérie sémantique pour préserver la pureté vectorielle du corps.

### Phase 11 — Structural Information GEO

Finding SAGEO Arena 2025 (Kim et al., Yonsei, arXiv:2602.12187) : optimiser le body seul **dégrade** le retrieval (−4.54 Hit Rate). Optimisation structurelle apporte +22% Hit Rate. Structural + Statistics combinés : **+35%**.

```
| Champ | Contrainte sémantique | Entité(s) à inclure (Phase 2) |
|---|---|---|
| Title (≈10 mots) | Mot-clé exact + différenciateur | Entité principale + angle divergence |
| Meta description (155 char) | Answer-first + bénéfice mesurable | Entité principale + verbe d'action |
| H1 | Mot-clé sémantique + promesse | Entité principale + Surprise Gap |
| H2 (5-8 prévus) | Chaque H2 = un vecteur sémantique distinct | Une entité ou concept par H2 |
| Schema.org | Type adapté à l'intention | Article + FAQPage + LocalBusiness (si géo) + HowTo (si Do) + VideoObject (si multimodal) |
```

### Phase 12 — Matrice couverture × Mapping Triade SERP

Croise micro-intentions × couches Phases 2-11. Vérifie qu'aucune micro-intention n'est orpheline.

**Mapping Triade SERP** — chaque livrable est tagué selon la phase Google qu'il nourrit :

```
| Couche produite | Phase Triade SERP cible | Mécanisme |
|---|---|---|
| Entités nommées + Structural Information | Phase 1 — Document Ranking (admission) | BM25 + RankBrain |
| Concepts structurants + preuves + grounding + n-grams | Phase 2 — Passage Ranking (densité par bloc) | DPR / Muvera + BERT |
| FAQ + answer-first + Surprise Gap | Phase 3 — Generation (AIO, citation LLM) | Grounding + Confidence Score |
```

Sans ce mapping, le rédacteur en aval ne sait pas où placer quoi.

### Phase 13 — Feedback loop KB

À la fin de chaque exécution, identifier les éléments à versionner dans le KB local (si l'utilisateur en a un) :

```
À ajouter à /concepts/ : concept-X.md (résumé en une phrase)
À ajouter à /entities/ : entité-Y.md (rôle dans le domaine)
À ajouter à /competitors/ : concurrent-Z.md (angle + faiblesse)
À ajouter à doctrine.md : doctrine-W (formulation tranchée)
À archiver dans /verbatims/ : verbatim-V.md (frustration experte rare)
À archiver dans /lexique/ : n-gram-N.md (expression signature)
```

L'utilisateur valide ou ajuste avant d'archiver. Sans cette phase, l'engine ne progresse pas — avec, il s'auto-améliore à chaque passage. Si l'utilisateur ne dispose pas d'un KB structuré, lister simplement les éléments candidats à archiver pour qu'il les copie où il veut.

## Template d'output final

```
PRÉPARATION SÉMANTIQUE — Requête : "[...]"
Profil : [B2B/B2C, rôle, secteur, objectif, audience, géo]

== PHASE 0 — Filtre stratégique (informatif) ==
- Test LLM : [PASS / WARN]
- Angle différenciant : [PASS / WARN]
- Pureté vectorielle : [PASS / WARN]
Verdict : [GO franche / GO avec avertissement]
Annexe sous-niches (si WARN) : [...]

== Livrables 1-13 ==
1. Micro-intentions (3 niveaux + profil + Action Engine flag)
2. Entités sémantiques pondérées (tableau 7 colonnes + avertissement « cosinus simulé »)
3. Lexique signature (n-grams + co-occurrences + statut P1/P2)
4. Pain points (10+ lignes) + 3 objections priorisées
5. Preuves quantitatives (Confidence Score + Freshness Guard + datation)
6. Multimodal
7. Cartographie concurrentielle (5-10 acteurs)
8. Gap analysis :
   8a. Gap Competitive Map (matrice acteur × concept)
   8b. Content Gap Score (% standard vs % surprise + verdict)
   8c. Surprise Score Sémantique : XX/100 — [verdict] + avertissement
9. Divergences (Information Gain calibré + acteur ciblé + entité attaquée)
10. FAQ stratégique (5-7 questions = 5-7 vecteurs)
11. Structural Information GEO (title / meta / H1 / H2 / schema)
12. Matrice couverture × Mapping Triade SERP
13. Patches KB à archiver
```

## Règles absolues

- **Aucun scraping SERP**, jamais. Pas Google, pas Bing, pas autre moteur.
- **Robots.txt strict** pour tout WebFetch. Si bloqué : training Claude + demande à l'utilisateur, jamais bypass.
- **Cosinus simulé toujours marqué** : sortie Phase 2 + Phase 8c avec avertissement « simulé par projection corpus Claude ».
- **Confidence Score obligatoire** sur chaque preuve chiffrée. Si basse ou inconnue → `[À SOURCER]`. Aucun chiffre inventé.
- **Freshness Guard** : preuves > 36 mois omises sauf paper fondateur.
- **Phase 0 jamais bloquante** : alerte WARN + sous-niches en annexe, produit toujours la carte complète.
- **Ne pas rédiger** : pas de H1 final, pas de hook, pas d'architecture Hn finale, pas de CTA, pas de prose narrative.
- **Une page = une intention** (pureté vectorielle). Si pluralité d'intentions Phase 0.3 → WARN + N sous-cartes en annexe.
- **Anti-cliché obligatoire** Phase 4 : pas de « je veux du ROI », pas de « je veux des résultats ».
- **Phase 2 — Justification obligatoire** : chaque entité avec sa justification courte. Pas d'entité arbitraire.

## Concepts mobilisés (définitions inline — pour usage autonome)

- **Triade SERP** : les 3 phases successives par lesquelles passe une requête sur Google moderne — Document Ranking (filtre d'admission via BM25/RankBrain), Passage Ranking (densité sémantique par bloc via DPR/Muvera/BERT), Generation (citation dans AI Overview / Featured Snippet / réponse LLM).
- **Information Gain** : standard Google formalisé dans les Quality Rater Guidelines (page 42) — un contenu sans effort qui reprend ce qui existe déjà reçoit la note la plus basse. Benchmark Aggarwal KDD'24 (arXiv:2311.09735) mesure les méthodes qui gonflent l'IG.
- **Confidence Score** : niveau de fiabilité d'une preuve chiffrée (haute / moyenne / basse) qui détermine si elle est utilisable telle quelle, à fact-checker, ou à remplacer par `[À SOURCER]`.
- **Freshness Guard** : règle d'âge des preuves — < 18 mois fraîche, 18-36 mois à flagger, > 36 mois omise (sauf paper fondateur structurel).
- **Action Engine flag** : drapeau levé en Phase 1 si l'intention est `Do` — la page doit alors embarquer un outil interactif (calculateur, simulateur, générateur, audit) pour viser la note Fully Meets des Quality Raters.
- **Pureté vectorielle** : une page = une intention. Multi-intentions dilue le vecteur sémantique et fait sortir la page du retrieval.
- **Answer-first pattern** : la réponse directe doit être en début de section/page, pas après 800 mots de mise en contexte. Validé par le finding Positional Bias des rerankers LLM (arXiv:2604.03642).
- **Grounding Score** : mesure de fidélité aux sources — critère de tri prioritaire des LLM modernes, plus important que le keyword stuffing.
- **Know-Simple / Know / Do** : taxonomie d'intention qui remplace TOFU/MOFU/BOFU pour l'ère LLM. Know-Simple = fait isolé, Know = compréhension complète, Do = action transactionnelle.
- **Surprise Gap** : la fracture entre ce que tous les concurrents disent (consensus) et ce que toi seul dis (angle propriétaire). Plus le gap est large, plus le contenu est mémorisé par les modèles IA.
- **Structural Information GEO** : finding SAGEO Arena 2025 (Kim et al., arXiv:2602.12187) — optimiser uniquement le body dégrade le retrieval, optimiser la couche structurelle (title, meta, headings, schema) + ajouter des statistiques sourcées apporte +35% Hit Rate.

## Sauvegarde (optionnel)

Si l'utilisateur dispose d'un vault structuré (Obsidian, dossier markdown organisé), proposer de sauvegarder l'output dans `<vault>/queries/prepa-semantique-YYYY-MM-DD-slug.md`. Sinon, output dans la conversation seule.

## Mode Audit — différences

En Mode Audit, chaque phase produit **3 colonnes** au lieu d'une : Attendu (calculé Mode Création) / Couvert dans le contenu actuel / Gap + action de correction.

Trois statuts par couche :
- ✅ Couvert : élément attendu présent et conforme → validation
- ❌ Gap : élément attendu absent ou non conforme → correction à planifier
- ⚠️ Hors scope : élément présent qui ne correspond à aucune couche attendue → suppression ou déplacement (FAQ, autre page)

Le statut « Hors scope » est critique : il préserve la pureté vectorielle.

**Plan de correction priorisé** livré à la fin :

```
PLAN DE CORRECTION — Contenu : "[titre/URL/chemin]"
Surprise Score Sémantique actuel : XX/100 — [verdict]

P0 — Bloquants (à corriger avant publication)
- [Phase X — Couche Y] Gap : [description] → Action : [verbe + objet précis]

P1 — Importants (avant prochaine vague de mises à jour)
- [...]

P2 — Améliorations (sur les versions suivantes)
- [...]

ÉLÉMENTS HORS SCOPE détectés :
- [Citation du contenu] → Raison : pollue le vecteur → Action : déplacer / supprimer

Score de couverture global : X/11 couches couvertes
```

- **P0** : Gap sur Phase 11 (Structural) ou phase Triade SERP entière non couverte → ne franchit pas l'admission Google
- **P1** : Gap sur Phase 4 (pain points), Phase 9 (divergence), Phase 5 (preuves), ou Surprise Score < 60 → indexée mais Low Surprise
- **P2** : Gap sur Phase 10 (FAQ), Phase 6 (multimodal), Phase 13 (patches KB) → ranke mais ne maximise pas la Triade SERP phase 3
````

> **Note pour Tim** : ce skill autonome diffère du skill actuellement installé sur ta machine (`~/.claude/skills/seo-preparation-semantique/SKILL.md`) qui contient encore une référence au doc source vault + les modes bronze/silver/gold. Si tu veux aligner ton install locale sur cette version, copie le bloc ci-dessus par-dessus le fichier existant.

---

# Annexes opérationnelles

Détails de référence : modes, phases en profondeur, formats de prompt, éthique scraping. Tout ce que la partie haute synthétise se retrouve ici en version exhaustive.

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

**Format de sortie : 7 colonnes**, 30 à 50+ entités par run.

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
| KB interne (si présent) | Qui le média référence comme concurrent ou source |
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
| Ratio entités propriétaires / entités totales | 30% | (si KB présent) entités issues du KB ÷ (entités KB + entités training standard) |
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
```

**KB Bootstrap**
```
Lance le KB Bootstrap.

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

