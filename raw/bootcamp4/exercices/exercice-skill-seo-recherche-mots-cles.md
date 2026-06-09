---
title: "Exercice — seo-recherche-mots-cles : d'une thématique à une liste qualifiée"
bootcamp: 4
type: exercice
session: 1
skill: seo-recherche-mots-cles
cowork: oui
created: 2026-06-09
---

# Exercice — seo-recherche-mots-cles : d'une thématique à une liste qualifiée

**Niveau** : débutant · **Pré-requis** : le skill `seo-recherche-mots-cles` installé. Une thématique de ton client et, si tu en as, 1 ou 2 verbatims (call, avis, mail).

## Le cas

Tu pars d'une thématique large (« facturation pour indépendants ») et tu dois en sortir une liste de mots-clés qualifiés : chacun avec son intention, son volume et sa difficulté. La règle d'or : on n'invente jamais un chiffre. Si tu n'as pas le volume réel, le skill met `[À SOURCER]`.

## Ce que tu dois faire

**1. Prépare 3 infos minimum.**
La thématique, ce que vend ton client (l'offre), et le persona visé. Si tu as un verbatim, garde-le sous la main, ça oriente la recherche.

**2. Lance le skill.**

```text
Lance seo-recherche-mots-cles.
Thématique : facturation pour indépendants.
Offre : un logiciel de facturation simple pour auto-entrepreneurs.
Persona : indépendant non comptable qui gère seul ses factures.
Sors une liste qualifiée (intention, volume, difficulté). Volume inconnu = [À SOURCER].
```

**3. Vérifie la liste.**
Chaque ligne doit avoir une intention. Aucun volume inventé.

## Ce que tu dois obtenir   ← le « screen »

```
RECHERCHE MOTS-CLÉS — facturation pour indépendants

| Mot-clé                            | Intention    | Volume     | Difficulté |
|------------------------------------|--------------|------------|------------|
| logiciel facture auto-entrepreneur | Do           | [À SOURCER]| moyenne    |
| comment faire une facture          | Know         | [À SOURCER]| faible     |
| facture électronique obligatoire   | Know         | [À SOURCER]| moyenne    |
| relancer une facture impayée       | Know / Do    | [À SOURCER]| faible     |
| mention obligatoire facture        | Know-Simple  | [À SOURCER]| faible     |

(50 à 150 lignes selon la thématique)
```

## Vérifier que tu as réussi

- [ ] 50 lignes minimum, chacune avec une intention.
- [ ] Aucun volume ni difficulté inventé : `[À SOURCER]` si pas de donnée réelle.
- [ ] La liste va du large (Know) au précis (Do), pas que des gros termes génériques.

## Le piège

Laisser le skill « remplir » des volumes plausibles. Un volume inventé fausse toute la priorisation derrière. Mieux vaut `[À SOURCER]` honnête qu'un chiffre faux. Tu remplaceras les volumes plus tard avec Keyword Planner.

## Comment ça marche

Le skill part de la thématique et de l'offre, déploie le champ sémantique (variantes, intentions, longue traîne), puis qualifie chaque mot-clé. Il ne se connecte pas à un outil de volume : il structure la demande, à toi de brancher les vrais chiffres ensuite.

## Version WhatsApp

> Exo recherche mots-clés : donne au skill la thématique + l'offre + le persona, et dis « lance seo-recherche-mots-cles, liste qualifiée avec intention, volume = [À SOURCER] si inconnu ». Tu obtiens 50+ mots-clés du large au précis. Piège : ne le laisse jamais inventer un volume. 💪
