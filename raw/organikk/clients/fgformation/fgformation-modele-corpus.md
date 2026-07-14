---
client: FG Formation
type: Modèle corpus (corpus avant pages) — doctrine pSEO de Tim appliquée à FG
source: [[fgformation-patterns-requetes]] · [[fgformation-modeles-pseo]] · [[fgformation-personas-problematiques]]
doctrine: [[feedback-corpus-avant-pages]]
date: 2026-07-14
relié: [[fgformation]]
---

# Modèle corpus — FG Formation

> **En résumé.** On arrête de raisonner « pages SEO ». On applique la doctrine corpus (validée le 06/07, modèle bxble / qadence) : on part du besoin en **données** du moteur — Google, les LLM qui doivent citer FG, et le futur quiz/assistant d'éligibilité — on construit ces corpus **une fois**, chaque corpus sert à la fois l'accompagnement réel de FG et les pages, et le SEO redevient le sous-produit. Six couches de corpus, chacune = un dataset typé + un template (jamais un fichier par page). Les 22 patterns de requêtes du doc précédent ne sont plus le chantier : ils sont ce que **chaque corpus produit mécaniquement** en sortie. Deux corpus sont finis et curés une fois (référentiel, lexique), un est balayé depuis la matière propriétaire (les 14 calls), un s'accumule (la data first-party FG). Aucun volume inventé, chiffres en `[À SOURCER]`, deux arbres (formateur indépendant / organisme de formation) portés dans les corpus de situation.

---

## 1. Le principe appliqué à FG

La règle : on ne conçoit jamais des pages. On se demande de quelles données le bot a besoin pour mieux répondre sur Qualiopi / NDA / CPF, on construit ce corpus, il le lit au moment de répondre, et on l'expose en pages.

Pour FG, le « bot » a trois visages, et le même corpus les sert tous les trois — c'est ce qui rend le coût déjà payé.

- **Le moteur de recherche et les LLM.** Pour citer FG dans une AI Overview ou une réponse ChatGPT sur « faut-il Qualiopi pour former des avocats », le modèle a besoin d'un corpus dense, sourcé, structuré en entités (indicateurs, dispositifs, acteurs, professions). Un corpus stable ne pourrit pas : le référentiel Qualiopi ne change pas tous les mois.
- **Le prospect, via le quiz / l'assistant d'éligibilité.** Le lead magnet « Qualiopi est-il fait pour moi ? » ([[fgformation-modeles-pseo]], hub de capture) a besoin exactement des mêmes données pour segmenter le visiteur vers le bon arbre. Le quiz n'est pas un chantier à part : c'est le corpus rendu interactif.
- **FG lui-même, dans son accompagnement.** François a déjà besoin de maîtriser le référentiel, les sigles, les motifs de refus, les dispositifs de financement pour faire son métier. Le corpus est le carburant du produit avant d'être celui de la page. Coût marginal de la page quasi nul.

On refuse tout corpus dont le grounding est coûteux ou périssable (contre-exemple rejeté ailleurs : les relevés de citations IA, trop chers, changent tout le temps). Ici, tout est stable ou déjà produit par le métier.

---

## 2. La stack corpus FG (le tableau maître)

Six couches. Chaque ligne : l'équivalent dans le modèle canonique (bxble / qadence), le besoin qu'elle couvre, le dataset typé qui la matérialise, sa nature (fini-curé / balayé / accumulé), le template de page qui en sort, et les patterns de [[fgformation-patterns-requetes]] qu'elle alimente.

| # | Corpus | Équiv. canonique | Dataset typé | Nature | Template de page | Patterns alimentés | Arbre |
|---|---|---|---|---|---|---|---|
| **1** | **Référentiel Qualiopi annoté** | Concordance bxble (balayage d'un corpus normé) | 7 critères × 32 indicateurs : libellé officiel, exigence, preuves attendues, erreurs classiques, spécificité par type d'action | Fini / curé une fois (RNQ national, stable) | 1 page / indicateur + 1 page / critère + hub référentiel | B (liste), A (déf), U (erreurs), Q (checklist) | Transverse |
| **2** | **Lexique sigles & acteurs** | Lexique Strong's (fini, curé, longue traîne) | ~25-40 entrées : NDA, EDOF, RNCP, RS, BPF, OPCO, CPF, DREETS, COFRAC, France Compétences, RNQ, FIFPL… — définition, rôle, qui délivre/contrôle, à quoi ça sert, lien action | Fini / curé une fois | 1 page / sigle + 1 page / acteur | A (déf), R (acteurs), F (comparaison RNCP↔RS) | Transverse |
| **3** | **Corpus des situations terrain** | Concordance balayée + data propriétaire | Personas × métiers × secteurs × statuts, tirés des **14 calls** : déclencheur, blocage, vocabulaire propre, solution FG | Balayé depuis les calls (re-balayable quand de nouveaux calls arrivent) | 1 page / cas d'usage (le moteur de conversion) | M (cas d'usage), L (déblocage), N (transition), G (choix), I (coût) | **A et B séparés** |
| **4** | **Corpus réglementaire par profession** | (unique à FG) | Professions réglementées × obligation déontologique de formation (avocats/CNB, experts-comptables, notaires, professions de santé…) : qui impose, depuis quand, ce que ça implique | Fini / curé depuis la réglementation | 1 page / profession | J (obligation oui/non), R (acteurs), C (chronologie) | Corpus / autorité |
| **5** | **Corpus des financements** | Connexions curées bxble | Dispositifs × conditions : CPF, OPCO, FIFPL, France Travail, plan de développement… — qui finance, conditions, prérequis (Qualiopi ? RNCP ?) | Fini / curé une fois | 1 page / dispositif + 1 page / croisement `domaine × dispositif` | V (sans / contournement), M (financement), I (coût) | Transverse + B |
| **6** | **Data first-party FG** | Benchmarks GSC qadence (couche 4) | Taux de réussite des accompagnements FG, délais réels d'instruction observés, motifs de refus rencontrés | Accumulé depuis la pratique (à produire, schéma à poser tôt) | Pages statistiques citables par les IA | D (statistiques) | Corpus / autorité |

Les couches se nourrissent : une page de situation (3) cite les indicateurs (1), les sigles (2) et les dispositifs (5) → le maillage interne naît du corpus, on ne le bricole pas après coup.

---

## 3. Détail par corpus

### Corpus 1 — Référentiel Qualiopi annoté

C'est la concordance de FG : un corpus source normé et fini (le Référentiel National Qualité, 7 critères, 32 indicateurs) qu'on balaie une fois pour en tirer, par indicateur, une fiche dense. Chaque fiche n'est pas une paraphrase du texte officiel : elle ajoute la valeur que seul un praticien a — les preuves réellement attendues, les erreurs qui font sauter l'indicateur à l'audit, la variation selon le type d'action (formation, bilan de compétences, VAE, apprentissage). C'est ce qui la rend non copiable et citable. Le corpus sert l'audit blanc que FG fait déjà avec ses clients (calls `audit-blanc-*`). Sortie : une longue traîne mécanique de ~32 pages indicateurs + 7 pages critères, plus le hub.

### Corpus 2 — Lexique sigles & acteurs

L'équivalent Strong's : fini, curé une fois, longue traîne massive à coût marginal nul. Le secteur est saturé de sigles opaques qui bloquent le débutant total (persona P3). Chaque entrée pose une entité et la relie aux autres. C'est le corpus le plus cité par les LLM (définition atomique = réponse directe). Il fusionne le pattern A (définition) et le pattern R (acteurs : qui délivre, qui contrôle), parce qu'un sigle et son organisme de tutelle sont la même fiche vue des deux côtés.

### Corpus 3 — Corpus des situations terrain (le moteur de conversion)

La vraie [[concepts/data-proprietaire|data propriétaire]] : les 14 calls décortiqués en [[fgformation-personas-problematiques|10 personas]], eux-mêmes déclinés en métiers (vente, cybersécurité, coiffure, FLE, HSE, massage, management…), secteurs (industrie, automobile, santé, BTP, IT…) et statuts. On le balaie comme une concordance : une variable = une page, avec le vocabulaire et l'exemple propres à la situation (principe hôtel Bordeaux). C'est le seul corpus à **deux arbres strictement séparés** — formateur indépendant (arbre A) et organisme de formation (arbre B) ne partagent ni intention ni public. Re-balayable : chaque nouveau call de François enrichit le dataset, donc les pages.

### Corpus 4 — Corpus réglementaire par profession

Unique à FG, fini, curé depuis la réglementation. L'obligation de formation varie par profession (décision CNB fin 2023 pour les avocats, obligations déontologiques des experts-comptables, DPC pour les professions de santé). Chaque page répond à une question binaire — « faut-il Qualiopi pour former des [profession] » — avec une réponse tranchée dès l'ouverture. Registre FAQ, très cité par les LLM. Rôle : corpus d'autorité qui fait remonter le reste.

### Corpus 5 — Corpus des financements

Les connexions curées : dispositifs de financement croisés avec leurs conditions réelles. C'est lui qui alimente le pattern V (contournement, « financer sans Qualiopi »), le plus décisionnel, en donnant la réponse honnête (souvent : non, ou seulement via tel dispositif). Croisé avec les domaines (IA, cybersécurité, management), il produit les pages « rendre une formation [domaine] finançable via [dispositif] ».

### Corpus 6 — Data first-party FG

L'équivalent de la couche GSC de qadence : la seule donnée que personne d'autre n'a. Taux de réussite des accompagnements FG, délais réellement observés, motifs de refus rencontrés sur le terrain. À produire (schéma à poser tôt, publication quand le volume est là). C'est ce qui débloque le pattern D (statistiques) sans jamais inventer un chiffre : une page statistique FG devient une donnée propriétaire non copiable et un aimant à citations. Tant que le volume n'est pas là, le pattern D reste en `[À SOURCER]` et ne se publie pas.

---

## 4. Ordre de construction

On suit l'ordre du modèle : les corpus finis et gratuits d'abord (ils améliorent l'accompagnement FG immédiatement et posent l'autorité), le balayé ensuite (il convertit), l'accumulé en continu.

1. **Corpus 2 (lexique) + Corpus 1 (référentiel).** Finis, curés une fois, coût déjà payé par le métier. Ils posent toutes les entités que le reste va relier. Socle de corpus.
2. **Corpus 4 (professions) + Corpus 5 (financements).** Finis eux aussi, forte autorité, alimentent les patterns binaires très cités.
3. **Corpus 3 (situations).** Le moteur de conversion, balayé depuis les calls, à lancer en parallèle du socle car les pages de conversion rankent mieux quand le corpus autour est dense (doctrine « corpus avant pages »).
4. **Corpus 6 (data FG).** S'accumule dès qu'on pose le schéma de collecte ; publication différée.

---

## 5. Ce que ça change concrètement

Le doc [[fgformation-modeles-pseo]] listait ~80-90 pages comme un décompte de chantier. Le modèle corpus dit la même cible autrement : ces pages ne sont plus à « écrire une par une », elles sont la **projection de six datasets**. On ne rédige pas 32 pages d'indicateurs, on curate un dataset de 32 lignes et on écrit un template. Le quiz d'éligibilité et le futur assistant lisent les mêmes datasets. Trois conséquences :

- Pas de thin content ni de prose IA : les pages sont denses par construction (relevés, tableaux, concordances).
- Le maillage est natif : une page de situation cite ses indicateurs, ses sigles, ses dispositifs parce que le corpus est lié.
- L'anti-hallucination est structurelle : la page cite le dataset au lieu d'inventer, comme le bot récupère au lieu de deviner.

---

## Prochaines étapes

1. **Figer le dataset du Corpus 2 (lexique)** : lister les ~25-40 entrées (sigle, définition, acteur, rôle, lien action) → passage en `seo-programmatique-pseo` pour template + source de données. Le plus rapide, coût quasi nul, débloque tout de suite les entités.
2. **Figer le dataset du Corpus 1 (référentiel)** : les 32 indicateurs annotés (exigence, preuves, erreurs, variation par type d'action), en s'appuyant sur les audits blancs déjà faits par FG.
3. **Poser le schéma du Corpus 6 (data FG)** tôt, même vide, pour commencer à accumuler taux et motifs de refus réels.
4. **Balayer le Corpus 3 (situations)** depuis les 14 calls en un dataset `métier / secteur / statut × déclencheur / blocage / solution`, deux arbres séparés.

## Journal

- **2026-07-14** : cadrage du modèle corpus FG (doctrine [[feedback-corpus-avant-pages]], modèle bxble/qadence). Six corpus définis (référentiel, lexique, situations, professions, financements, data first-party), chacun mappé à un dataset typé + template + patterns alimentés + nature (fini-curé / balayé / accumulé). Reframe : les ~80-90 pages de [[fgformation-modeles-pseo]] deviennent la projection de six datasets, pas un chantier page à page. Ordre de construction posé (finis d'abord, balayé ensuite, accumulé en continu). Prochain : figer le dataset lexique (Corpus 2) en `seo-programmatique-pseo`.
