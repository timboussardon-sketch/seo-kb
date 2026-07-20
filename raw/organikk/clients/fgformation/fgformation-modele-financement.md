---
client: FG Formation
type: Modèle pSEO « Financement » (template + variable) — skill seo-programmatique-pseo
source: [[fgformation-mots-cles]] (cluster P2) · [[fgformation-corpus-notation]] · calls/SYNTHESE-appels-anonymisee
doctrine: [[feedback-corpus-avant-pages]] · [[feedback-jamais-mentir-features-verifiees]]
date: 2026-07-20
relié: [[fgformation]]
---

# Modèle « Financement » — FG Formation

> **En résumé.** Un seul modèle de page, décliné sur le cluster P2 « Débloquer des ventes / financement ». La question commune aux 9 requêtes est toujours la même : **qui paie cette formation, à quelle condition, et combien reste à la charge du client**. Le template répond dans cet ordre, avec un chiffrage réel tiré des calls, puis bascule sur la décision (autofinancement, portage, certification) et son seuil. Le différenciant n'est pas la page, c'est le tableau de prise en charge et les seuils de bascule que François donne à l'oral depuis des années et que personne n'a écrits. Une requête du cluster repose sur une prémisse fausse et doit être retraitée avant rédaction. Tous les montants issus des calls sont marqués à confirmer : ce sont des paroles de praticien en rendez-vous, pas des barèmes sourcés.

---

## 0. Le point à trancher avant d'écrire

La ligne du cluster P2 dit : `faire financer une formation sans être qualiopi` → « Réponse = impossible → CTA Qualiopi ».

Cette réponse est fausse, et le vault le dit lui-même ailleurs. `calls/SYNTHESE-appels-anonymisee.md` pose l'inverse en toutes lettres :

> Être Qualiopi n'est pas obligatoire pour un sous-traitant, sauf sur une formation financée par le CPF. Hors CPF, un OF certifié peut sous-traiter à un non-certifié (indicateur 27). Donc la page ne ment pas avec « tu dois être Qualiopi » : elle dit la vérité, puis bascule sur le vrai levier décisionnel.

Trois voies de financement existent sans être certifié : le client paie de sa poche, le client passe par un organisme de portage, ou la formation sort du champ des fonds mutualisés. Écrire « impossible » ferait mentir la page sur sa première phrase, celle que les moteurs extraient.

La réponse honnête convertit mieux, et c'est celle que François donne au téléphone : ce n'est pas interdit, c'est coûteux. Le portage prend 15 à 20 % du chiffre d'affaires dans les conditions normales, jusqu'à 40 ou 50 % dans les cas constatés, plus un droit d'entrée. La page vend le calcul, pas l'interdiction.

Deux notes du vault se contredisent (`fgformation-mots-cles` contre la synthèse des appels). C'est à Tim de trancher laquelle fait foi. Le modèle ci-dessous est construit sur la version de la synthèse, parce qu'elle est plus récente et adossée aux verbatims.

---

## 1. Le modèle

**Un template, une variable.**

```
Template : la page « Faire financer [X] »
Variable : le couple (situation de financement, statut du payeur)
```

La variable n'est pas décorative. Elle change le montant pris en charge, l'organisme qui paie, le reste à charge et la décision recommandée. Deux pages du modèle ne partagent que le squelette.

**Pattern d'URL** : `/financement/[slug]`
**Page pivot du cluster** : `/financement/` (hub qui liste les situations et porte le lien vers l'accompagnement)
**Point de conversion** : diagnostic ou devis, selon l'étage du funnel.

### Les deux couches

| Couche | Rôle | Nature | Volume |
|---|---|---|---|
| **Couche 1 — les 9 pages douleur** | l'entrée. Une requête = une situation de blocage vécue | curée une fois depuis les calls | 9 pages |
| **Couche 2 — la matrice de prise en charge** | le volume. `faire financer une formation quand on est [statut]` | balayée depuis le corpus financements | ~10 à 14 pages |

La couche 2 n'a de sens qu'après la couche 1. Les 9 pages posent les entités (dispositifs, seuils, voies) que la matrice décline ensuite.

---

## 2. Le template de page

Structure Hn fixe, contenu variable. L'ordre n'est pas négociable : la réponse d'abord, le calcul ensuite, la décision en dernier.

| Bloc | Contenu | Ce qui varie d'une page à l'autre |
|---|---|---|
| **H1** | la requête telle qu'elle se tape | tout |
| **Réponse en tête** (40-60 mots, dans les 300 premiers) | le verdict honnête, y compris quand il dessert l'offre | tout |
| **H2 — Qui paie, et combien** | tableau : dispositif, qui le gère, condition Qualiopi, plafond, reste à charge | tout (c'est le cœur non copiable) |
| **H2 — Les trois voies** | autofinancement client, portage, certification en propre | les montants et le verdict |
| **H2 — À partir de quand ça bascule** | le seuil chiffré qui fait pencher d'une voie à l'autre | le seuil |
| **H2 — Le cas réel** | une situation anonymisée tirée des calls, avec ses chiffres | la situation |
| **Passage ancré** (150-200 mots) | le raisonnement complet, autonome, extractible | tout |
| **FAQ** | 3 à 5 questions issues des PAA et des objections des calls | tout |
| **Bloc authorship** (~50 mots) | qui écrit, sur quelle pratique, depuis quand | fixe |
| **CTA** | diagnostic (étage Problème) ou devis (étage Décision) | l'étage |

### Le bloc qui fait la page : « Qui paie, et combien »

C'est le seul bloc que les pages déjà classées ne peuvent pas répliquer, parce qu'il demande d'avoir mené les rendez-vous. Format imposé :

| Dispositif | Qui le gère | Qualiopi exigé | Ordre de grandeur pris en charge | Reste à charge type |
|---|---|---|---|---|
| OPCO | branche professionnelle | oui | `[À CONFIRMER]` | calculé |
| FIF PL | profession libérale | oui | `[À CONFIRMER]` | calculé |
| AGEFICE | dirigeants non salariés | oui | `[À CONFIRMER]` | calculé |
| CPF | Caisse des dépôts | oui, sans exemption sous-traitant | `[À CONFIRMER]` | calculé |
| France Travail | demandeur d'emploi | oui | `[À CONFIRMER]` | calculé |
| Fonds propres du client | le client | non | sans objet | 100 % |
| Portage par un OF certifié | l'organisme porteur | non pour vous | sans objet | commission + droit d'entrée |

**Règle de sourcing.** Les ordres de grandeur cités dans les calls (prise en charge horaire OPCO, plafonds FIF PL et AGEFICE, coût d'audit, fourchette d'accompagnement) sont des paroles de François en rendez-vous commercial. Ils sont exploitables comme matière, pas comme barème publiable. Avant mise en ligne, chaque montant passe par une source primaire ou par une validation écrite de François. Tant que ce n'est pas fait, la case reste `[À CONFIRMER]` et la page ne se publie pas avec un chiffre approximatif.

---

## 3. Les 9 pages de la couche 1

Reprise du cluster P2, avec l'angle de traitement et ce qui alimente chaque page.

| # | Requête | Intention | Funnel | Angle de traitement | Matière disponible |
|---|---|---|---|---|---|
| 1 | faire financer une formation sans être qualiopi | Know | Problème | Réponse honnête : c'est possible, voici les trois voies et ce qu'elles coûtent. Prémisse à corriger (§0) | synthèse des appels, indicateur 27, verbatims portage |
| 2 | mes clients ne peuvent pas financer ma formation | Know | Problème | Page douleur. Le blocage n'est pas commercial, il est administratif | verbatim des deals en suspens, cas du client qui paie de sa poche |
| 3 | qualiopi pour débloquer les financements opco | Do | Décision | Le mécanisme : ce que Qualiopi ouvre exactement, et ce qu'il n'ouvre pas | correction récurrente de FG sur l'idée fausse |
| 4 | combien de temps pour obtenir qualiopi | Know | Décision | Objection délai frontale. La peur documentée est « six mois » | peur transversale relevée dans la synthèse |
| 5 | obtenir qualiopi rapidement | Do | Décision | Le chemin court réel, sans promettre un délai qu'on ne tient pas | temps de préparation cité en call |
| 6 | qualiopi est-ce rentable | Know | Problème | Page ROI. Le calcul, pas l'argument | coût de certification et de cycle, tarif jour direct contre sous-traitance |
| 7 | qualiopi à partir de combien de clients c'est rentable | Know | Problème | Le seuil chiffré. La question la mieux posée du cluster | seuils de bascule donnés en call |
| 8 | sortir de la sous-traitance pour facturer en direct | Do | Décision | Recoupe le cluster P1. Écart de tarif entre direct et sous-traitance | écart de tarif jour, taux de commission constatés |
| 9 | faire héberger sa formation par un organisme qualiopi | Know | Problème | Le portage expliqué sans le vendre ni le démolir : coût réel, perte de fichier client, charge de travail conservée | plusieurs cas de portage, dont deux organismes porteurs défaillants |

**Cannibalisation à surveiller.** Les pages 4 et 5 traitent la même intention sous deux formulations, et les pages 6 et 7 aussi. À passer en `seo-clustering-mots-cles` avant rédaction : soit une page par paire avec la variante en H2, soit deux pages avec des angles réellement disjoints. Les pages 1, 8 et 9 se recoupent également autour du passage en direct.

---

## 4. La couche 2 (la matrice)

`faire financer une formation quand on est [statut]`

La variable est le statut du bénéficiaire, parce que c'est lui qui détermine l'organisme financeur. Un artisan, une profession libérale et un salarié ne frappent pas à la même porte, n'ont pas le même plafond et n'ont pas le même reste à charge. Le contenu change donc réellement d'une page à l'autre.

Statuts identifiés dans les calls : profession libérale, dirigeant non salarié, artisan ou commerçant, salarié d'une PME, demandeur d'emploi, micro-entrepreneur, association, service formation interne d'entreprise.

Chaque page reprend le template, avec son tableau de prise en charge propre et son cas réel. Le maillage part de chaque page de statut vers la page douleur correspondante et vers le hub.

**Condition de lancement.** Cette couche ne démarre pas tant que les montants du tableau ne sont pas sourcés. Sans eux, la matrice produit huit pages qui disent la même chose autrement, ce qui est exactement le contenu creux que le modèle doit éviter.

---

## 5. Le maillage

Chaque page pointe vers un ensemble différent, sinon le maillage devient un pied de page dupliqué.

- Chaque page douleur pointe vers les **dispositifs** qu'elle cite, jamais vers tous.
- Chaque page dispositif pointe vers les **statuts** qui peuvent le mobiliser.
- Les pages 1, 8 et 9 pointent vers la page de conversion de l'arbre formateur indépendant.
- Les pages 2 et 3 pointent vers la page de conversion PME.
- Le hub `/financement/` est le seul point qui liste tout.

Aucun lien croisé entre l'arbre formateur indépendant et l'arbre organisme de formation au niveau des pages de conversion, conformément à `fgformation-modeles-pseo`.

---

## 6. Écart assumé avec le skill

Le skill `seo-programmatique-pseo` demande au minimum cinq modèles scalables et une matrice de priorisation entre eux. La demande porte sur un seul modèle, le modèle Financement. Le livrable le traite donc en profondeur plutôt que d'en produire quatre autres qui n'ont pas été demandés. Les autres modèles restent listés dans `fgformation-modeles-pseo`.

---

## 7. Ce qu'il faut avant de rédiger la première page

1. **Trancher la prémisse de la requête 1** (§0). Deux notes du vault se contredisent.
2. **Faire valider les montants par François**, dispositif par dispositif, ou les sourcer en source primaire. C'est le blocage dur : sans le tableau chiffré, le modèle perd ce qui le rend non copiable.
3. **Passer les 9 requêtes en clustering** pour fusionner les paires 4/5 et 6/7.
4. **Décider du sort du `robots.txt`** (cf. `fgformation-corpus-notation`). ClaudeBot et GPTBot sont toujours en `Disallow`.
5. **Choisir la page pilote.** Recommandation : la requête 7, `qualiopi à partir de combien de clients c'est rentable`. Elle est la mieux posée du cluster, la réponse est un seuil chiffré que François donne déjà à l'oral, et elle fige le bloc « Qui paie, et combien » qui sert ensuite aux huit autres.

---

## Journal

- **2026-07-20** : formalisation du modèle « Financement » (skill `seo-programmatique-pseo`) à partir du cluster P2 de [[fgformation-mots-cles]]. Un template, deux couches (9 pages douleur curées, matrice par statut ensuite). Bloc différenciant identifié : le tableau de prise en charge et les seuils de bascule, tirés des calls, à faire valider avant publication. Contradiction relevée dans le vault sur `faire financer une formation sans être qualiopi` : la note mots-clés dit « impossible », la synthèse des appels dit l'inverse et documente les trois voies. Arbitrage laissé à Tim. Pilote recommandé : la requête sur le seuil de rentabilité.
