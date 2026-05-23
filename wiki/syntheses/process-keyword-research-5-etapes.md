---
type: synthesis
title: "Process de recherche de mots-clés — 5 étapes (Keyword Planner → GSC → Grok → Propriétaires → pSEO)"
aliases: [process-keyword-research, workflow-mots-cles, kw-research-5-etapes, process-mots-cles-business]
tags: [synthese, workflow, mots-cles, keyword-research, organikk, doctrine-tim, b2b, pseo]
created: 2026-05-05
updated: 2026-05-05
sources: 5
confidence: high
status: stable
---

# Process de recherche de mots-clés — 5 étapes

Pipeline opérationnel pour passer de "je cherche des mots-clés" à "j'ai un système de génération de trafic". Articule les outils volumiques classiques avec la data propriétaire et le pSEO, sous le contrôle des [[concepts/methode-organikk-4-piliers|4 piliers Organikk]]. Opérationnalise [[raw/notes/process-seo-b2b-2026]] côté exécution outillée.

> **Skill orchestrateur** : [[raw/notes/skill-kw-research-workflow]] automatise les 5 étapes ci-dessous (cadrage 6 questions → CSV KP → CSV GSC → 4 WebSearch séquentielles → verbatims → pSEO → Google Sheet scoré + synthèse 5 lignes). Cible : 10-15 min vs 2-3 sessions manuelles.

---

## Rappel — Les 4 piliers Organikk

Toute recherche de mots-clés doit servir au moins un pilier. Sinon le mot-clé ne mérite pas d'exister.

| # | Pilier | Question | KPI | Concept |
|---|---|---|---|---|
| 1 | **Surprise Gap** | Pourquoi on lit | Surprise Score par passage / page | [[concepts/surprise-gap]] |
| 2 | **Grounding Score** | Pourquoi on rank | Grounding Score vs top 3 SERP | [[concepts/grounding-score]] |
| 3 | **pSEO** | Comment on scale | Pages indexées / créées > 85 % | [[concepts/programmatique-pseo]] |
| 4 | **AEO** | Comment on gagne les moteurs de réponse | Taux de citation dans réponses génératives | [[concepts/aeo]] |

Pyramide stricte : **Surprise → Grounding → pSEO → AEO**. Sans Surprise = pages génériques ignorées par les LLM. Sans Grounding = pSEO produit du thin. Sans pSEO = AEO ne couvre pas l'intention. Sans AEO = SEO classique invisible en Agentic Search. Détail : [[concepts/methode-organikk-4-piliers]].

---

## Étape 1 — Google Keyword Planner

**Volume marché + idées de mots-clés.**

### Pourquoi cette source

Seul outil qui donne les volumes de recherche réels de Google. Sert à découvrir des mots-clés et valider le potentiel volume d'un sujet. À utiliser comme générateur de seeds, pas comme source de vérité (cf. limites en [[concepts/mots-cles-actionnels]] : la majorité des mots-clés qui convertissent en B2B n'ont pas de volume mesurable).

### Mode 1 — Recherche par mots-clés

Accès : `Google Ads > Outils > Keyword Planner > Trouver de nouveaux mots-clés`.
- Saisir 3-5 mots-clés seeds : les termes que le client utilise naturellement pour décrire son activité.
- Filtrer par pays / langue pour éliminer le bruit.
- Télécharger le CSV avec toutes les suggestions.

### Mode 2 — Recherche par site

- Saisir l'URL du site du client ou celle d'un concurrent direct. Google analyse le contenu et suggère les mots-clés associés.
- Astuce : entrer l'URL d'une page spécifique (pas le domaine) pour des résultats plus ciblés.
- Tester 2-3 concurrents pour découvrir des angles qu'ils couvrent et pas le client.

### Ce qu'on récupère

| Colonne | Utilité | Action |
|---|---|---|
| Mot-clé | Idées brutes | Garder ceux à intention business |
| Volume mensuel | Taille du marché | Indicatif — pas un critère de choix |
| Concurrence | Difficulté Ads (pas SEO) | Concurrence haute = sujet monétisable |
| Tendance 3 mois | Saisonnalité | Repérer les sujets en hausse |

### Attention

Le Keyword Planner donne le volume, pas l'intention. Un mot-clé à 10 000 recherches/mois sans intention business = 0 lead. Le filtre intention se fait à l'étape 2 (GSC) puis 4 (verbatims).

---

## Étape 2 — Google Search Console

**Données réelles + quick wins.**

### Pourquoi cette source

La GSC est la seule source de vérité. Elle montre ce que Google pense déjà du site — les requêtes, les pages associées, et le delta entre visibilité et résultat. Cohérent avec [[concepts/triade-serp]] (alignement SERP réel ≠ projection outil).

### Export des données

- Période : 3 derniers mois
- Métriques : Clics + Impressions + CTR + Position moyenne
- Export 1 — Requêtes : toutes les requêtes, par impressions décroissantes
- Export 2 — Pages : toutes les pages indexées
- Export 3 — Requêtes × Pages : le croisement requête / URL

### Analyse — Le delta impressions / clics

Le signal clé n'est pas le volume. C'est le delta entre impressions et clics.

| Signal | Lecture | Action |
|---|---|---|
| Impressions élevées + clics faibles | Google te montre mais personne ne clique | Optimiser title + meta |
| Position 3-12 + impressions élevées | Proche du top 3 = quick win | Optimiser la page existante |
| CTR élevé + impressions faibles | Niche où tu es pertinent | Créer plus de contenu |
| Requête sans page dédiée | Google t'associe sans page | Créer la page = content gap |

### Règle d'or

On optimise l'existant **avant** de créer du nouveau. Les quick wins sont toujours la première action. Cf. doctrine "ne plus vendre du trafic, vendre des leads" en [[raw/notes/process-seo-b2b-2026]].

---

## Étape 3 — Grok + DeepSearch

**Data fraîche X + web que personne n'a compilée.**

### Pourquoi cette source

Grok est le seul LLM branché en temps réel sur X (Twitter). Il récupère les données terrain, retours praticiens et débats en cours que ni le Keyword Planner ni la GSC ne voient. C'est un guide de **sourcing**, pas de rédaction. Le but : alimenter le pilier [[concepts/surprise-gap|Surprise Gap]] avec des angles que les concurrents n'ont pas vus, et nourrir l'[[concepts/information-gain]].

### ◉ 1 — Cartographier le consensus

But : savoir ce que tout le monde dit déjà sur le sujet. C'est ce que l'article ne doit **pas** répéter.

```
Sujet : [SUJET]
Donne-moi le consensus actuel :
- Ce que ChatGPT et Gemini répondent quand on pose la question
- Les chiffres et stats qui reviennent partout
Format : les 5-7 affirmations les plus répétées + les stats les plus citées avec leur source d'origine.
```

Output : la réponse moyenne du web = le bruit. Le ◉ 2 va chercher le signal.

### ◉ 2 — Scanner X via DeepSearch (30 derniers jours)

But : trouver ce que les praticiens partagent sur X et que personne n'a compilé dans un article.

```
Active DeepSearch. Sujet : [SUJET]
Cherche uniquement sur X, 30 derniers jours :
1. Chiffres concrets partagés par des praticiens (résultats A/B, % réussite, métriques, cas clients)
2. Retours terrain négatifs ou échecs documentés
3. Débats entre experts — qui dit quoi et pourquoi
4. Questions posées qui n'obtiennent pas de bonne réponse
Pour chaque trouvaille : donnée exacte, @handle, date, lien. Format tableau.
```

Output : micro-données fraîches, retours réels, controverses en cours.

### ◉ 3 — Stats web récentes (< 60 jours)

But : compléter les données X avec des études et stats vérifiables.

```
Sujet : [SUJET]
Cherche sur le web les données les plus récentes (< 60 jours) :
1. Études ou rapports publiés en 2025-2026 avec chiffres précis
2. Stats qui CONTREDISENT les idées reçues du ◉ 1
3. Sources primaires uniquement
Pour chaque stat : chiffre exact, source primaire, date, lien. Format tableau.
```

Output : croisement X + web = mix terrain + académique unique.

### ◉ 4 — Croiser pour trouver les gaps utilisateurs

But : faire émerger les vrais gaps. Pas des gaps de contenu mais des gaps utilisateurs.

```
À partir des données terrain (◉ 2) et des stats web (◉ 3), identifie :
1. Les 3 infos les plus surprenantes qui contredisent le consensus du ◉ 1
2. Les sujets discutés activement sur X mais absents des résultats IA
3. Les questions fréquentes sur X sans bonne réponse web
4. Les données que personne n'a croisées ensemble
Format : tableau [Angle | Source X | Source Web | Pourquoi c'est un gap]
```

Output : liste d'angles exclusifs. L'info existe mais personne ne l'a structurée.

### Logique des 4 prompts

Consensus (◉ 1) = le bruit → Terrain X (◉ 2) = le signal → Stats web (◉ 3) = la preuve → Croisement (◉ 4) = les angles exclusifs. Chaque prompt dépend du précédent. Sortie alimente directement le [[concepts/surprise-gap]] de l'article.

---

## Étape 4 — Données propriétaires

**L'avantage compétitif que personne ne peut copier.**

### Pourquoi cette source

Les données propriétaires révèlent des mots-clés qu'aucun outil ne connaît — parce qu'ils viennent du langage réel des clients, pas des algorithmes. C'est le pilier transversal de la méthode (cf. [[concepts/data-proprietaire]]) qui alimente Surprise + Grounding + pSEO + AEO. Cohérent avec la doctrine [[concepts/mots-cles-actionnels]] : "ton vrai mot-clé est dans tes calls clients, pas dans Keyword Planner."

### Source A — Contenu existant du client

- Articles de blog, pages services, études de cas : quels sujets génèrent de l'engagement ?
- Emails envoyés aux prospects : quels arguments reviennent le plus ?
- Posts LinkedIn / réseaux sociaux : lesquels ont le plus d'interactions ?

### Source B — Interviews et verbatims clients

- Calls de découverte : noter les mots exacts utilisés par les prospects. *« Comment tu décrirais ton problème à un collègue ? »* → mots-clés naturels.
- Témoignages clients : les phrases avant / après révèlent les pain points.
- Questions fréquentes en call / email : chaque question récurrente = un article potentiel.

### Source C — Données métier exclusives

- Chiffres internes : taux de conversion, benchmarks, stats sectorielles.
- Process propriétaires : méthodologies, frameworks, grilles.
- Cas clients anonymisés : résultats concrets = preuve.

### Comment extraire les mots-clés

1. Collecter 10-20 verbatims (calls, emails, témoignages).
2. Repérer les formulations récurrentes — ce sont les mots-clés longue traîne.
3. Croiser avec la GSC : est-ce que ces formulations apparaissent déjà ?
4. Si non : créer du contenu pour créer la demande.

### Pourquoi c'est décisif

Un concurrent peut copier tes mots-clés Keyword Planner. Il ne peut pas copier les verbatims de **tes** clients. C'est ça, l'[[concepts/information-gain]]. Filtre final avant rédaction : [[concepts/test-substitution-llm]] (si un LLM produit 80 % du contenu sans la data propriétaire → ne pas créer la page).

---

## Étape 5 — SEO programmatique (pSEO)

**Template + variable = des centaines de pages qui rankent.**

### Pourquoi cette source

Le pSEO transforme les mots-clés identifiés aux étapes 1-4 en système scalable. 1 template × 1 variable = des centaines de pages longue traîne qui captent du trafic là où personne ne se positionne. Détail : [[concepts/programmatique-pseo]] et [[concepts/pseo-data-driven-models]]. Référence opérationnelle : [[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]].

### Le principe

- Formule : 1 template + 1 variable qui change = des centaines de pages uniques.
- Chaque page cible une requête ultra-spécifique (longue traîne).
- Source de données : les bases de données propriétaires du client (secteurs, localisations, indicateurs, catégories…).

### Identifier les modèles scalables

Pour chaque modèle, définir :

| Élément | Description | Exemple |
|---|---|---|
| Pattern d'URL | `[site]/[prefixe]/[variable]` | `site.com/formation/[secteur]` |
| Head term (fixe) | La partie qui ne change pas | "Créer un OF en" |
| Modificateur (variable) | Ce qui rend chaque page unique | langues, coaching, BTP… |
| Nombre de pages | Estimation réaliste | 25-35 pages par modèle |
| Source de données | Base qui alimente la variable | Liste secteurs, OPCO, régions |

### Matrice de priorisation des modèles

Chaque modèle est évalué sur 4 critères :

1. **Volume total estimé** — somme des volumes de toutes les pages du modèle.
2. **Effort de création** — combien de données uniques faut-il par page ?
3. **Compétition SERP** — qui est déjà positionné sur ces requêtes ?
4. **Potentiel conversion** — est-ce que la page mène à une action business ? (cf. [[concepts/know-simple-know-do]] / [[concepts/product-led-seo]]).

### Exécution

- **Phase 1 (J1-J30)** : lancer le modèle prioritaire (meilleur ratio impact / effort).
- **Phase 2 (J30-J60)** : mesurer, itérer, lancer le 2ᵉ modèle.
- **Phase 3 (J60-J90)** : scale — modèles restants + optimisation des existants.

### Clé du succès

Chaque page générée doit apporter de la valeur unique. **Pas de thin content.** La variable doit créer du contenu réellement différent d'une page à l'autre (OPCO différents, réglementations différentes, marchés différents). Garde-fou : passer par le test [[concepts/fully-meets]] des Quality Raters avant de scaler.

---

## Synthèse — Les 5 sources assemblées

| Étape | Source | Donne | Limite | Quand | Output |
|---|---|---|---|---|---|
| 1 | Keyword Planner | Volumes, idées | Pas d'intention | Début | Seeds bruts |
| 2 | GSC | Données réelles | Que l'existant | Si 3 mois data | Quick wins |
| 3 | Grok DeepSearch | Data X + web | Sourcing, pas rédaction | Après GSC | Angles exclusifs |
| 4 | Propriétaires | Verbatims, process | Effort de collecte | En continu | Content gaps |
| 5 | pSEO | Pages scalables | Besoin BDD | Après stratégie | Centaines de pages |

### Parcours type en session 1

Étape 1 (15 min) → Étape 2 (20 min) → Étape 3 (intro, à faire en async) → Étape 4 (10 min, homework) → Étape 5 (intro, développé en session 2-3).

**Résultat final** : un tableau de mots-clés décisionnels classé par intention + une liste de modèles pSEO priorisés. Le client passe de *« je cherche des mots-clés »* à *« j'ai un système de génération de trafic »*.

### Livrable Google Sheet — 5 critères de priorisation

Pour chaque mot-clé sortant du pipeline, scorer sur :

1. **Volume** (Keyword Planner / Semrush)
2. **CPC** (proxy intention commerciale)
3. **Intérêt business** (proximité offre, scoring manuel 1-5)
4. **Difficulté** (KD Semrush ou estimation manuelle)
5. **YoY** (tendance 12 mois)

Filtre final cohérent avec [[concepts/mots-cles-actionnels]] : `CPC × intent × proximité offre`. Éliminer tout mot-clé orphelin par rapport à l'offre.

---

## Articulation avec la doctrine

- **Étape 1 (KP)** alimente surtout la *découverte* — peu d'enjeu doctrinal, juste un seeder.
- **Étape 2 (GSC)** est la fondation [[concepts/grounding-score|Grounding]] : on travaille avec ce que Google a déjà compris du site.
- **Étape 3 (Grok)** alimente le [[concepts/surprise-gap|Surprise Gap]] et l'[[concepts/information-gain]].
- **Étape 4 (Propriétaires)** est le pilier transversal [[concepts/data-proprietaire]] — alimente les 4 piliers.
- **Étape 5 (pSEO)** matérialise le pilier scale + accroche l'[[concepts/aeo|AEO]] via couverture MECE des intentions.

L'ordre des étapes respecte la pyramide d'exécution : on ne touche pas au pSEO tant que les fondations Surprise + Grounding ne sont pas posées sur les mots-clés piliers.

---

## Pages liées

[[raw/notes/skill-kw-research-workflow]] · [[concepts/methode-organikk-4-piliers]] · [[concepts/mots-cles-actionnels]] · [[concepts/surprise-gap]] · [[concepts/grounding-score]] · [[concepts/programmatique-pseo]] · [[concepts/aeo]] · [[concepts/data-proprietaire]] · [[concepts/information-gain]] · [[concepts/test-substitution-llm]] · [[concepts/triade-serp]] · [[concepts/know-simple-know-do]] · [[concepts/product-led-seo]] · [[concepts/fully-meets]] · [[concepts/pseo-data-driven-models]] · [[raw/notes/process-seo-b2b-2026]] · [[raw/notes/skill-quick-win]] · [[raw/notes/skill-cannibalisation]] · [[raw/notes/skill-programmatique-pseo]] · [[sources/2026-04-17-organikk-process-seo-b2b-2026]] · [[sources/2026-04-25-pseo-data-driven-organikk-4-modeles]] · [[raw/data/keyword-research-2026-05-02/keywords-classified]]
