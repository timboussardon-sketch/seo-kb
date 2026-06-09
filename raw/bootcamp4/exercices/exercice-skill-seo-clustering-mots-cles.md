---
title: "Exercice — seo-clustering-mots-cles : transformer une liste en pages"
bootcamp: 4
type: exercice
session: 1
skill: seo-clustering-mots-cles
cowork: oui
created: 2026-06-09
---

# Exercice — seo-clustering-mots-cles : transformer une liste en pages

**Pré-requis** : le skill `seo-clustering-mots-cles` installé. Une liste brute de mots-clés (la sortie de `seo-recherche-mots-cles`, ou un export Keyword Planner).

## Le cas

Tu as une liste de 80 mots-clés en vrac. La question n'est pas « lesquels garder », c'est « lesquels vont sur la même page ». La règle : deux mots-clés qui affichent le même top 10 dans Google ont la même intention, donc une seule page. Sinon tu crées deux pages qui se cannibalisent.

## Ce que tu dois faire

**1. Récupère ta liste brute.**
Colle la sortie de `seo-recherche-mots-cles` ou ton export Keyword Planner.

**2. Lance le skill.**

```text
Lance seo-clustering-mots-cles sur cette liste. Regroupe par intention de SERP
(1 cluster = 1 page). Pour chaque cluster, donne le mot-clé pivot et signale-moi
toute cannibalisation potentielle.
[colle la liste]
```

**3. Lis les clusters.**
Chaque cluster = une future page, avec un mot-clé pivot (le principal).

## Ce que tu dois obtenir   ← le « screen »

```
CLUSTERS — facturation pour indépendants

Cluster « Logiciel de facturation » (pivot : logiciel facture auto-entrepreneur)
  - logiciel facture auto-entrepreneur
  - meilleur logiciel facturation indépendant
  - appli facture micro-entreprise
  → 1 page

Cluster « Relance des impayés » (pivot : relancer une facture impayée)
  - relancer une facture impayée
  - modèle relance facture
  - lettre de relance impayé
  → 1 page

⚠️ Cannibalisation possible : "logiciel devis facture" et "logiciel facturation"
   pourraient viser la même page. À fusionner ou différencier.
```

## Vérifier que tu as réussi

- [ ] Chaque cluster a un mot-clé pivot clair.
- [ ] 1 cluster = 1 page, pas deux clusters sur la même intention.
- [ ] Les cannibalisations potentielles sont signalées.
- [ ] Tu pourrais nommer l'URL de chaque cluster sans hésiter.

## Le piège

Faire un cluster par mot-clé. Si tu te retrouves avec 80 clusters pour 80 mots-clés, tu n'as pas clusterisé : tu vas créer 80 pages qui se marchent dessus. Le bon nombre de clusters est bien plus petit que le nombre de mots-clés.

## Comment ça marche

Le skill regroupe par partage de SERP : si deux requêtes affichent les mêmes résultats, Google considère que c'est la même intention, donc une seule page suffit. À défaut de données SERP, il utilise l'intention et la proximité sémantique comme proxy. Le pivot est le mot-clé le plus représentatif du groupe.

## Version WhatsApp

> Exo clustering : colle ta liste brute et dis « lance seo-clustering-mots-cles, 1 cluster = 1 page, donne le pivot et signale les cannibalisations ». Chaque cluster devient une page. Piège : ne fais pas un cluster par mot-clé, sinon tu crées des pages qui se cannibalisent. 💪
