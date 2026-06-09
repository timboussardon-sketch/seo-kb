---
title: "Exercice — Workflow mots-clés : trouver tes mots-clés avec le contexte"
bootcamp: 4
type: exercice-workflow
session: 1
workflow: mots-cles-6-etapes
cowork: oui
created: 2026-06-09
related:
  - "[[skill-workflow-mots-cles]]"
  - "[[session-1-mots-cles-prep]]"
---

# Exercice — Workflow mots-clés : trouver tes mots-clés avec le contexte

**Niveau** : intermédiaire · **Pré-requis** : skills `seo-recherche-mots-cles`, `seo-clustering-mots-cles`, `seo-mots-cles-decisionnels` installés. Un accès Google Keyword Planner + Search Console. 2 ou 3 calls clients (ou des verbatims) de ton client.

## Le cas

Le réflexe de débutant, c'est de taper un mot dans Keyword Planner et de prendre les gros volumes. C'est exactement ce qu'on ne fait pas. Un bon mot-clé ne se trouve pas dans un outil, il se construit à partir du **contexte** de ton client : ce que ses clients disent vraiment, les objections en call, ce qui se cherche sur Reddit. L'outil donne le volume, le contexte donne l'angle.

Cet exercice te fait passer d'une thématique à une liste de mots-clés qualifiés, en injectant du contexte à chaque étape.

## Ce que tu dois faire

L'exercice a 6 étapes. Les étapes 1-2 récupèrent la matière, les étapes 3-4 ajoutent le contexte (le plus important), les étapes 5-6 sortent et trient les mots-clés.

**1. La matière brute (Keyword Planner).**
Va sur Google Keyword Planner, tape ta thématique, exporte les idées + volumes. Tu obtiens une liste large, encore générique.

```
SCREEN — Keyword Planner (exemple : SaaS de facturation)
mot-clé                          | volume/mois
logiciel de facturation          | 12 000
facture auto-entrepreneur        | 8 100
logiciel devis facture           | 3 600
facturation électronique 2026    | 2 900
note de frais logiciel           | 1 300
```

**2. Ta data réelle (Search Console).**
Exporte tes Requêtes GSC. Repère les requêtes où tu as beaucoup d'impressions mais peu de clics : ce sont des intentions déjà à ta portée.

```
SCREEN — GSC, requêtes sous-exploitées
requête                          | impressions | clics | position
facture électronique obligatoire | 4 200       | 35    | 8,1
relancer une facture impayée     | 2 600       | 18    | 9,4
```

**3. Le vrai langage (Reddit + Grok).**
C'est ici que la plupart s'arrêtent trop tôt. Va chercher comment les gens parlent vraiment du problème. Sur Claude, colle :

```text
Cherche sur Reddit et le web comment les TPE et indépendants parlent de la
facturation : leurs galères concrètes, les mots exacts qu'ils emploient,
les questions mal répondues. Sors-moi une liste de pain points + verbatims.
```

```
SCREEN — contexte extrait
Pain points :
- "je passe 2h par mois à relancer mes impayés à la main"
- "je comprends rien à la facture électronique obligatoire"
- "mon comptable veut un format précis, je sais pas le sortir"
Vocabulaire réel : relance impayé, mention légale facture, export comptable, FEC
```

**4. Ta data propriétaire (calls clients).**
Dépose 2-3 calls ou verbatims de ton client dans Claude :

```text
Voici des calls clients. Sors les problématiques et objections récurrentes,
et le vocabulaire métier exact employé. Ne résume pas, liste-moi le concret.
```

C'est cette matière que personne d'autre n'a. Elle transforme une page générique en page que seul ton client peut écrire.

**5. Sortir et qualifier les mots-clés.**
Maintenant tu as du contexte. Lance le skill en lui donnant tout :

```text
Lance seo-recherche-mots-cles sur la thématique "facturation pour indépendants".
Contexte : [colle les pain points Reddit + les verbatims des calls + les requêtes GSC].
Sors une liste qualifiée avec intention, volume estimé et difficulté. Si tu n'as
pas le volume réel, mets [À SOURCER], n'invente jamais un chiffre.
```

**6. Trier en pages, puis garder ce qui convertit.**
Enchaîne les deux skills :

```text
Lance seo-clustering-mots-cles sur cette liste (1 cluster = 1 page).
Puis seo-mots-cles-decisionnels pour isoler les requêtes qui convertissent.
```

## Ce que tu dois obtenir   ← le « screen »

À la fin, une liste qualifiée, triée, contextualisée (exemple) :

```
MOTS-CLÉS QUALIFIÉS — facturation pour indépendants

| Mot-clé                          | Intention | Volume   | Cluster (page)        | Décisionnel |
|----------------------------------|-----------|----------|-----------------------|-------------|
| logiciel facture auto-entrepreneur| Do        | 8 100    | Logiciel facturation  | ⭐ oui      |
| relancer une facture impayée     | Do/Know   | [À SOURCER]| Relance impayés      | ⭐ oui      |
| facture électronique obligatoire | Know      | 2 900    | Facture électronique  | non         |
| mention légale facture           | Know-S    | 1 300    | Mentions légales      | non         |

Les ⭐ sont tes pages prioritaires : intention d'achat + portées par ton contexte réel.
```

## Vérifier que tu as réussi

- [ ] Tu as injecté du contexte réel (Reddit + calls), pas juste un export d'outil.
- [ ] Chaque mot-clé a une intention (Do / Know / Know-Simple).
- [ ] Aucun volume inventé : `[À SOURCER]` partout où tu n'as pas la vraie donnée.
- [ ] La liste est regroupée en clusters (1 cluster = 1 page), pas une liste à plat.
- [ ] Tu sais lesquels sont décisionnels (ceux qui convertissent).

## Le piège

Prendre les gros volumes de Keyword Planner et s'arrêter là. Un mot-clé à 12 000 de volume sans intention d'achat fait du trafic qui ne convertit pas. Un mot-clé à 200, tiré d'une objection entendue en call, amène un client. Le volume hiérarchise, il ne décide pas. Le contexte décide.

## Comment ça marche

Les outils (Keyword Planner, GSC) donnent le volume et la demande mesurée. Reddit et tes calls donnent l'angle et le vrai vocabulaire, ce que les outils ne voient pas. Les skills agrègent tout ça : `seo-recherche-mots-cles` qualifie, `seo-clustering-mots-cles` regroupe en pages, `seo-mots-cles-decisionnels` garde ce qui convertit. Le résultat est une liste que ton concurrent ne peut pas copier, parce qu'il n'a pas tes calls.

## Version WhatsApp

> Exo mots-clés avec contexte : 1) Keyword Planner (volume) 2) GSC (tes impressions sous-cliquées) 3) Reddit/Grok (« comment les gens parlent vraiment du problème », pain points + verbatims) 4) tes calls clients (objections, vocabulaire) 5) « lance seo-recherche-mots-cles avec ce contexte » 6) « clustering puis mots-cles-decisionnels ». Piège : ne prends pas juste les gros volumes, c'est le contexte (Reddit + calls) qui fait la différence. Jamais de volume inventé → [À SOURCER]. 💪
