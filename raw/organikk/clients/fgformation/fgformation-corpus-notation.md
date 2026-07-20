---
client: FG Formation
type: Notation des corpus (mode LISTE, skill qadence-directory appliqué à FG)
source: [[fgformation-modele-corpus]] · [[fgformation-personas-problematiques]] · [[fgformation-patterns-requetes]] · [[fgformation-modeles-pseo]]
doctrine: [[feedback-corpus-avant-pages]] · [[feedback-doctrine-vault-decide-jamais-ia]]
date: 2026-07-20
relié: [[fgformation]]
---

# Notation des corpus — FG Formation

> **En résumé.** Passage des 6 corpus du modèle FG (plus 9 candidats nouveaux) dans les 5 filtres durs et la notation /10 du skill `qadence-directory`. Résultat : 4 corpus passent, 2 sont bloqués au filtre de couverture vault, 5 sont éliminés. Le mieux noté n'est pas dans la liste d'origine : c'est le corpus des **non-conformités par indicateur**, tiré des 5 audits blancs de François, qui se greffe sur les 32 pages indicateurs déjà en ligne. Deux constats de terrain priment sur la notation : le `robots.txt` de fgformation.fr interdit ClaudeBot et GPTBot, et le Corpus 1 du modèle est déjà publié. Aucun chiffre inventé.

---

## 0. Deux blocages constatés le 2026-07-20

### Le site interdit les deux principaux crawlers de LLM

Relevé sur `https://www.fgformation.fr/robots.txt` :

```
User-agent: *          Allow: /
User-agent: ClaudeBot  Disallow: /
User-agent: GPTBot     Disallow: /
```

La doctrine corpus dit que le corpus est lu par le moteur au moment de répondre. Chez FG, ClaudeBot et GPTBot sont refusés à la porte. Tant que ces deux lignes restent, tout corpus construit pour être cité par les LLM est payé et non lu. C'est le premier arbitrage à rendre, avant d'écrire une seule fiche.

À vérifier avec François avant de toucher au fichier : ce blocage peut être un choix assumé (protection du contenu contre l'entraînement) ou un réglage hérité d'un plugin. Les deux se traitent différemment.

### Le Corpus 1 du modèle est déjà en ligne

`fgformation-modele-corpus.md` liste le référentiel Qualiopi annoté comme corpus à construire, priorité 1. Le crawl montre que les pages existent :

| Ce qui existe | URL | Ce que le modèle prévoyait |
|---|---|---|
| 32 pages indicateurs | `/le-guide/qualiopi-cest-quoi/indicateur-1` à `indicateur-32` | Corpus 1, à construire |
| Lexique en page unique | `/lexique-qualiopi/` | Corpus 2, à construire en fiches |
| Liste des certificateurs | `/les-organismes-certificateurs-qualiopi/` | Corpus 2 (volet acteurs) |
| Pages villes (8) | Paris, Lyon, Grenoble, Chambéry, Boulogne, Marseille, Bordeaux, Saint-Denis | non prévu |
| Pages métier / domaine | `creer-of-rh`, `creer-organisme-formation-langues`, `creer-un-centre-de-formation-btp`, `devenir-formateur-anglais-independant`, `devenir-formateur-excel`, `auto-ecole-cpf` | modèle scalable, entamé |

Conséquence : le chantier Corpus 1 devient un chantier de densification et d'annotation des pages existantes, pas une création. Le budget de construction se reporte ailleurs.

Écart vault à trancher : le modèle du 14/07 pose l'ordre « finis d'abord (lexique + référentiel), puis professions + financements, puis situations ». Le terrain déplace cet ordre, puisque le référentiel est publié et que la matière propriétaire (les audits blancs) est disponible maintenant. La note ci-dessous propose un autre ordre. C'est Tim qui tranche, pas moi.

---

## 1. Les candidats retenus (tableau classé)

| Corpus | URL proposée | Ce que le moteur en fait | Taille | Note /10 |
|---|---|---|---|---|
| **Non-conformités par indicateur** | `/le-guide/non-conformites/[indicateur]` | Répond à « pourquoi je me fais retoquer sur l'indicateur 12 » avec un motif réel constaté, pas une paraphrase du référentiel | 32 fiches | **10** |
| **Situations terrain** | `/situations/[métier ou secteur]` | Reconnaît la situation du visiteur dans son vocabulaire et l'oriente vers le bon arbre | ~40 fiches, 2 arbres | **10** |
| **Lexique sigles et acteurs** | `/lexique/[sigle]` | Donne une définition atomique reliée à l'action à mener, au lieu d'une page fourre-tout | ~30 fiches | **8** |
| **Financements croisés** | `/financements/[dispositif]` | Répond à « telle formation est-elle finançable par tel dispositif, et à quelles conditions » | ~12 fiches + croisements | **7** |

## 2. Détail par corpus retenu

### Non-conformités par indicateur — 10/10

**Valeur agent (4).** Aujourd'hui les 32 pages indicateurs expliquent l'exigence. Personne ne dit ce qui fait sauter l'indicateur en audit réel. C'est exactement la question que tape un OF sous pression, et c'est la seule chose qu'un LLM ne peut pas déduire du référentiel public. Le corpus sert aussi l'offre d'audit blanc (Spoke B noté 8 dans `fgformation-modeles-pseo`) et le futur quiz.

**Couverture vault (3).** Les 5 transcripts `audit-blanc-*.md` du dossier `calls/`, plus l'article existant sur les 18 non-conformités relevées en audit de surveillance, plus les pages `non-conformites-audit-de-surveillance` et `certification-suspendue-audits-de-surveillance`. La matière est là, elle demande une session de dépouillement, pas une session d'écriture.

**Demande (2).** Les requêtes se tapent par numéro d'indicateur et par motif. Le format `[Résolu] non-conformité indicateur X` est un moule observé sur les forums métier (cf. `fgformation-patterns-requetes`, section forums).

**Frein (0).** Le référentiel national est stable. Un motif de non-conformité constaté ne périme pas.

**Ce qui rend ce corpus le mieux placé.** Le coût de la page est déjà payé deux fois : François produit cette matière en faisant son métier, et les 32 pages d'accueil des indicateurs existent déjà pour l'accrocher. C'est de la data propriétaire greffée sur une structure publiée.

### Situations terrain — 10/10

**Valeur agent (4).** C'est le corpus qui fait la conversion. Le prospect ne tape pas Qualiopi, il tape son blocage. Sans ce corpus, le site répond à la catégorie et rate la situation.

**Couverture vault (3).** Les 14 calls dépouillés, les 9 personas de `fgformation-personas-problematiques`, la banque de verbatims, les ~45 problématiques candidates. La matière la plus dense du dossier.

**Demande (2).** Longue traîne mécanique par métier, secteur et statut. Les pages déjà en ligne sur `creer-of-rh`, `langues`, `btp` montrent que le moule tourne.

**Frein (0).** Re-balayable à chaque nouveau call, sans dette.

**Réserve.** Deux arbres strictement séparés, formateur indépendant et organisme de formation. Le vault est explicite : aucun lien croisé entre les deux au niveau des pages de conversion.

### Lexique sigles et acteurs — 8/10

**Valeur agent (2).** Un LLM sait déjà définir le CPF. La valeur n'est pas la définition, elle est dans le lien entre le sigle, l'autorité qui le délivre et l'action que FG mène dessus. Note basse assumée sur ce critère.

**Couverture vault (3).** Le vocabulaire est présent dans les calls, notamment le persona P3 qui débarque sans le jargon, et la page `/lexique-qualiopi/` existante fournit la base.

**Demande (2).** Le pattern A de `fgformation-patterns-requetes` est le plus volumineux du dossier.

**Frein (0).** Corpus fini, curé une fois.

**Le vrai chantier.** Le lexique existe en une page unique. Une page qui contient trente définitions n'est extractible sur aucune d'elles. Le travail est d'éclater cette page en fiches et de rediriger, pas de repartir de zéro.

### Financements croisés — 7/10

**Valeur agent (3).** C'est le point où les réponses génériques se trompent le plus souvent, parce que les conditions varient par dispositif et par statut. Le corpus alimente aussi le pattern le plus décisionnel du dossier, celui du contournement (« financer sans Qualiopi »).

**Couverture vault (2).** Les calls couvrent CPF, OPCO, EDOF, FIFPL et les refus EDOF vécus. Il manque le sourcing officiel des conditions, à prendre en source primaire.

**Demande (2).** Croisement domaine par dispositif, longue traîne réelle.

**Frein (-1).** Les règles de financement bougent, EDOF en premier. Sans plan de relecture daté, la valeur baisse.

---

## 3. Bloqués au filtre 2 (couverture vault insuffisante)

Ces deux corpus sont recevables sur le fond. La matière n'est pas dans le vault aujourd'hui, donc la fiche ne se fait pas et on note le trou.

| Corpus | Ce qui manque | Ce qu'il faut avant de le relancer |
|---|---|---|
| **Data first-party FG** (taux de réussite, délais réels, motifs de refus chiffrés) | Aucune donnée agrégée. Le vault a du qualitatif, pas du quantitatif. | Poser le schéma de collecte maintenant, même vide, et laisser accumuler. Publication différée. Aucun chiffre ne se publie tant que le volume n'est pas là. |
| **Professions réglementées** (obligation de formation par profession) | Une seule situation dans les calls (association A) et une mention de la décision CNB. Le reste demande une recherche réglementaire externe, profession par profession. | Sourcer en source primaire les 6 à 8 professions visées, ou renoncer. Le risque d'écrire du droit approximatif est réel sur ce corpus. |

---

## 4. Éliminés, avec le motif

| Corpus | Filtre qui l'élimine | Motif |
|---|---|---|
| Pages villes supplémentaires | 1 (besoin réel) | Aucune réponse ne s'améliore. Un accompagnement Qualiopi ne dépend pas de la ville. Les 8 pages existantes ne justifient pas d'étendre le moule. |
| Annuaire des certificateurs Qualiopi | 3 (grounding) | La liste bouge et la maintenir est un engagement permanent. Deux pages existent déjà, elles suffisent. |
| Comparatif des logiciels pour OF | 3 et 1 | Périssable, hors métier de FG, et une page d'avis existe déjà. |
| Chronologie des versions du référentiel (v8, v9, arrêtés) | 3 (grounding) | Utile mais périssable par nature, et le blog en couvre déjà des morceaux. À traiter en mise à jour d'articles existants. |
| Glossaire IA et GEO | 1 et 5 | Aucun rapport avec ce que cherche un prospect FG. |

---

## 5. Recommandation

**Avant tout corpus : trancher le `robots.txt`.** Le reste en dépend.

**Puis, dans cet ordre :**

1. **Non-conformités par indicateur.** Meilleur rapport valeur sur effort du dossier. La structure d'accueil existe (32 pages en ligne), la matière existe (5 audits blancs), et le corpus alimente une offre déjà packagée.
2. **Situations terrain.** Le moteur de conversion, à lancer en parallèle dès que le premier est cadré.
3. **Éclatement du lexique** en fiches, avec redirections depuis la page unique.
4. **Financements**, une fois le sourcing primaire fait.
5. **Schéma de collecte de la data FG**, à poser tôt même vide.

Cet ordre diverge de celui de `fgformation-modele-corpus.md`, qui plaçait le lexique et le référentiel en premier. La raison est factuelle : le référentiel est déjà publié et les audits blancs sont disponibles maintenant. Arbitrage à valider par Tim.

---

## Journal

- **2026-07-20** : passage des corpus FG dans les 5 filtres durs et la notation /10 (skill `qadence-directory` appliqué au client). 4 corpus retenus, 2 bloqués au filtre de couverture vault, 5 éliminés. Deux constats de terrain relevés par crawl : `robots.txt` bloque ClaudeBot et GPTBot, et le Corpus 1 du modèle est déjà en ligne (32 pages indicateurs + lexique + certificateurs). Nouveau candidat sorti en tête, absent du modèle du 14/07 : les non-conformités par indicateur, tirées des 5 audits blancs. Prochain : arbitrage `robots.txt`, puis mode BUILD sur le corpus retenu.
