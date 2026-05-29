---
title: "Préparation sémantique sans SERP (skill distribuable + pédagogie)"
bootcamp: 4
semaine: 4
type: skill-distribuable
usage: "Bundle Drive. Skill distribuable. Engine de préparation sémantique sans scraping SERP : la matière brute qui alimente le brief et la rédaction. SKILL.md nettoyé des refs vault perso (doc source + chemin de sauvegarde) pour fonctionner chez les participants."
related:
  - "[[skill-donnees-structurees]]"
  - "[[skill-core-web-vitals]]"
  - "[[skill-roadmap-pseo]]"
  - "[[skills-checklist-bootcamp4]]"
---

# Le skill qui remplace Surfer et NeuronWriter (sans scraper la SERP)

Salut à tous,

Ce skill, c'est ton engine de préparation sémantique. Tu lui donnes une requête + un profil, il te sort tout ce que ta page doit contenir pour ranker : les entités pondérées, le lexique signature, les pain points, les preuves chiffrées à aller chercher, la gap analysis vs les concurrents, et un Surprise Score sémantique sur 100. Sans jamais scraper Google.

C'est la première brique d'une page. Tu le lances AVANT le brief et AVANT la rédaction. Sa sortie alimente `seo-brief-contenu` (qui construit la structure Hn) puis `article-engine-pipeline` (qui rédige).

## Pourquoi sans SERP

Les outils type Surfer ou NeuronWriter scrapent le top 10 et te disent "mets ces mots parce que tes concurrents les ont". Résultat : tu écris la même page que tout le monde, et tu te fais manger par l'AI Overview qui résume le consensus en trois phrases. Ce skill fait l'inverse : il te donne la carte sémantique attendue ET il calcule ta divergence (ton Information Gain), c'est-à-dire ce que tu dis que personne d'autre ne dit. C'est ça qui te fait citer par les moteurs de réponse, pas la conformité au top 10.

## Les 2 modes

- **Création** : tu donnes une requête + un profil, il sort la carte sémantique vierge d'une page à écrire.
- **Audit** : tu donnes en plus un contenu existant (texte, fichier, URL), il sort le diff entre ce que ta page couvre et la carte attendue, avec un plan de correction P0/P1/P2.

Le mode est détecté tout seul selon ce que tu fournis. Si tu donnes juste une requête = Création. Si tu colles aussi un contenu = Audit.

## Le piège à éviter

Le cosinus et le Surprise Score sont **simulés** par projection sur le corpus de Claude, pas calculés par une vraie API d'embeddings. Le skill le marque lui-même dans chaque sortie. Ne va pas vendre ces chiffres à un client comme une mesure mathématique exacte : c'est une estimation calibrée, utile pour prioriser, pas une vérité absolue. Pour la mesure dure, c'est `seo-geo-audit` (7 scores algorithmiques).

Autre piège : ce skill NE rédige PAS. Pas de H1, pas de hook, pas de structure Hn finale, pas de prose. Il sort la matière première. Si tu veux la structure, c'est `seo-brief-contenu`. Si tu veux l'article, c'est `article-engine-pipeline`.

---

## Procédure d'install / vérification

Vraie nouvelle install, un seul fichier.

1. Dossier `~/.claude/skills/seo-preparation-semantique/`
2. `SKILL.md` = le bloc entre `=====` ci-dessous
3. Relance Claude, vérifie avec `/skills` (tu dois voir `seo-preparation-semantique`)

Déclenchement : il part dès que tu dis "prépare la sémantique", "carte sémantique", "préparation sémantique", "analyse sémantique de [requête]", "tout ce que ma page doit contenir", "audite la sémantique de [page]", "qu'est-ce qui manque à mon article sur [requête]", ou tu l'appelles avec `/seo-preparation-semantique`.

Premier essai conseillé : lance-le en mode Création sur une requête de ton client, tu verras la profondeur de la carte. Puis lance-le en mode Audit sur une de tes pages existantes qui ne ranke pas, il te dira ce qui lui manque.

=====

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

Ce SKILL.md est auto-suffisant : le pipeline des 13 phases, le format détaillé de la Phase 2 (entités pondérées) et de la Phase 8c (Surprise Score Sémantique), ainsi que le format de l'Output obligatoire sont définis ci-dessous. Pour les phases dont le tableau n'est pas détaillé ici, suivre la structure de la section « Output obligatoire » en fin de skill.

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

## Format Phase 2 — Entités sémantiques pondérées (7 colonnes)

Format obligatoire :

```
| # | Entité | Type | Poids (0-1) | Densité cible (%) | Cosinus estimé requête (0-1) | Justification | Statut |
|---|---|---|---|---|---|---|---|
| 1 | `passage ranking` | Concept | 0.94 | 0.8% | 0.91 | Brique du grounding, citée dans 3 papers MIRAS | P1 critique |
| ... | ... | ... | ... | ... | ... | ... | ... |
```

Type : Person / Concept / Tool / Method / Doctrine / Event / Location / Algo.
Poids > 0.8 = pivot. Densité pivots 0.5-1%, supportives 0.2-0.5%, périphériques < 0.2%.
**Cosinus marqué « simulé »** dans pied de tableau obligatoire.
**Justification obligatoire** par entité.
30-50 entités par run (50+ en Gold).

## Format Phase 8c — Surprise Score Sémantique

Formule :
```
Surprise Score Sémantique = pondération de 4 composantes :
  30% — Ratio entités propriétaires / entités totales (KB Gold)
  20% — Ratio verbatims Haute Surprise / verbatims totaux
  25% — Distance lexicale moyenne propriétaire ↔ consensus (1 - cosinus simulé)
  25% — Présence Quotation Addition + Statistics Addition (% preuves verbatim/chiffrées avec source)
```

Échelle :
- 0-30 = Médiocrité statistique (oubli mémoriel)
- 30-60 = Acceptable mais réplicable
- 60-85 = Information Gain validé
- 85-100 = Inversion experte maximale

**Avertissement obligatoire** : « *Score calibré sur projection corpus Claude. Pour calibration exacte : audit GEO Sentinel (skill seo-geo-audit, 7 scores algorithmiques).* »

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

```
PRÉPARATION SÉMANTIQUE — Requête : "[...]"
Profil : [B2B/B2C, rôle, secteur, objectif, audience, géo]
Mode détecté : [Bronze / Silver / Gold]

== PHASE 0 — Filtre stratégique (informatif) ==
- Test LLM : [PASS / WARN]
- Angle différenciant : [PASS / WARN — sous-niches proposées en annexe]
- Pureté vectorielle : [PASS / WARN — N intentions]
Verdict : [GO franche / GO avec avertissement]
Annexe sous-niches (si WARN) : [...]

== Livrables 1-13 ==
1. Micro-intentions (3 niveaux + profil + Action Engine flag)
2. Entités sémantiques pondérées (7 colonnes : entité/type/poids/densité/cosinus/justif/statut)
3. Lexique signature (n-grams + co-occurrences + statut)
4. Pain points + 3 objections priorisées
5. Preuves quantitatives (Confidence Score + Freshness Guard)
6. Multimodal
7. Cartographie concurrentielle (5-10 acteurs)
8. Gap analysis :
   8a. Gap Competitive Map (matrice acteur × concept)
   8b. Content Gap Score (% standard vs % surprise)
   8c. Surprise Score Sémantique : XX/100 — [verdict]
9. Divergences (Information Gain calibré)
10. FAQ stratégique FM (5-7 vecteurs)
11. Structural Information GEO (title/meta/H/schema)
12. Matrice couverture × Triade SERP
13. Patches KB à archiver
```

## Enchaînement workflow

**En amont** : aucun (c'est la première brique).

**En aval, selon objectif** :
- `seo-brief-contenu` → structure Hn complète à partir de la carte
- `article-engine-pipeline` → rédaction complète à partir de la carte (passe par seo-workflow-article)
- `seo-product-led-seo` → si Action Engine flag déclenché (intention Do)
- `seo-donnees-structurees` → implémentation JSON-LD à partir de la Phase 11
- `seo-geo-audit` → en aval d'une rédaction, audit qualité 7 scores (complémentaire à Mode Audit qui mesure la couverture)

## Sauvegarde

Output dans `wiki/queries/prepa-semantique-YYYY-MM-DD-slug.md` si une KB / un vault existe, sinon dans le dossier de travail actuel.

## Concepts liés

`purete-vectorielle` · `triade-serp` · `information-gain` · `surprise-gap` · `surprise-metric` · `grounding-score` · `confidence-score` · `mots-cles-actionnels` · `data-proprietaire` · `passage-ranking` · `structural-information-geo` · `freshness-guard` · `rrf` · `aeo` · `know-simple-know-do` · `product-led-seo` · `anti-ai-writing`

=====

## Note pour Tim (interne)

- **Nettoyage effectué pour distribution.** Deux refs vault perso retirées du SKILL.md verbatim :
  1. Ligne d'origine 31 : pointait vers `raw/articles/brouillons/engine-densite-semantique-sans-serp.md` dans `/Users/timothee/Code/seo-kb/` avec "Lire ce doc avant la première exécution". Remplacée par une note d'auto-suffisance (le pipeline + formats Phase 2/8c + Output sont dans le SKILL.md). Les participants n'ont pas ce doc de 1245 lignes, la dépendance cassait le skill chez eux.
  2. Ligne d'origine 179 : chemin de sauvegarde `wiki/queries/...` "selon hook §7 AGENTS.md (vault seo-kb)". Généralisée en "si une KB / un vault existe, sinon dossier de travail actuel". Les participants n'ont ni ton AGENTS.md ni ta structure wiki.
  3. Concepts liés : wikilinks `[[...]]` convertis en backticks (pas de graphe Obsidian chez eux, les `[[ ]]` créeraient des liens morts).
- **Perte de qualité acceptée.** Le doc source de 1245 lignes détaille des formats de tableaux pour les phases 1, 3-7, 9-13 que le SKILL.md ne reproduit pas in extenso. Pour la distribution, Claude reconstruit ces tableaux depuis la structure de l'Output obligatoire. Suffisant pour un usage bootcamp. Si tu veux la version pleine, c'est un skill à 2 fichiers (SKILL.md + le doc source en référence), mais ça alourdit l'install et expose ton brouillon. Reco : garder la version auto-suffisante.
- **Statut bundle.** Tu m'avais dit en début de session que `seo-preparation-semantique` n'était PAS dans le bundle bootcamp (perso à toi). Changement de plan : tu le donnes aujourd'hui dans le pack des 4. J'ai mis à jour ce statut. Pense à le rajouter dans `[[skills-checklist-bootcamp4]]` si tu veux que la checklist reste cohérente (je peux le faire).
- **Skill technique.** Sortie dense (13 phases, Surprise Score, cosinus simulé). Risque que les participants moins avancés soient noyés. Cadrer en intro de session : "vous n'avez pas besoin de comprendre les 13 phases, vous avez besoin de savoir que la sortie alimente le brief et la rédaction". Le détail est pour ceux qui veulent creuser.
- **Normalisation.** Doc sans em-dashes dans la pédagogie (règle maison). Le bloc SKILL.md est reproduit depuis `~/.claude/skills/seo-preparation-semantique/` AVEC les 3 nettoyages ci-dessus (donc PAS strictement verbatim — c'est la version dé-vault-isée, comme pour `seo-donnees-structurees`).
