---
type: source
source_type: doctrine
title: "TODO du [jour, date complète en français]"
aliases: []
tags: []
created: 2026-04-25
updated: 2026-04-25
sources: 0
confidence: medium
status: draft
---

---
name: todo-quotidienne-bilan-tim
description: Génère chaque matin une TODO structurée : bilan d'hier, bilan de la semaine, plan de demain et plan de la semaine prochaine, basé sur les sessions passées avec Tim.
---

Tu dois produire chaque matin une TODO quotidienne pour Tim (Timothée Boussardon, consultant SEO/IA) sous forme de document récapitulatif structuré, en français.

## OBJECTIF
Créer un fichier Markdown qui résume :
1. **Hier** : ce qui a été fait hier (tâches accomplies, décisions prises, livrables produits)
2. **Semaine écoulée** : récapitulatif des 7 derniers jours (projets avancés, thèmes récurrents, victoires)
3. **Demain** : ce que Tim doit faire demain (tâches prioritaires, engagements, suites à donner)
4. **Semaine prochaine** : plan pour les 7 prochains jours (projets à lancer, échéances, objectifs)

## ÉTAPES D'EXÉCUTION

### Étape 1 — Récupérer le contexte des sessions passées
Utilise l'outil `mcp__session_info__list_sessions` pour obtenir la liste des sessions récentes de Tim.

### Étape 2 — Lire les transcripts pertinents
Pour chaque session des 7 derniers jours, utilise `mcp__session_info__read_transcript` pour extraire :
- Les tâches accomplies (fichiers créés, posts écrits, analyses SEO menées, briefs produits, etc.)
- Les décisions prises et les directions choisies
- Les engagements pris pour la suite ("je dois faire X", "la semaine prochaine je vais Y", "à faire demain")
- Les projets en cours et leur état d'avancement
- Les thèmes récurrents (SEO, IA, GEO, LinkedIn, revue de presse, clients, outils)

Concentre-toi surtout sur les sessions d'hier (J-1) et de cette semaine (J-7 à J-1).

### Étape 3 — Identifier les tâches futures
À partir des sessions, déduis :
- Ce qui a été explicitement planifié pour demain ou la semaine prochaine
- Les suites logiques des projets en cours (ex: si brief SEO produit hier → rédaction à prévoir)
- Les tâches récurrentes de Tim (revue de presse "Algorithme", posts LinkedIn, suivis clients)

### Étape 4 — Produire le livrable
Crée un fichier Markdown dans `/sessions/youthful-wizardly-turing/mnt/outputs/` nommé `todo-YYYY-MM-DD.md` (date du jour).

Structure du fichier :

```
# TODO du [jour, date complète en français]

## ✅ Hier — [date J-1]
[Liste des réalisations d'hier, format bullet points courts et factuels]

## 📅 Semaine écoulée — [date J-7] au [date J-1]
[Synthèse par thème/projet, pas un simple dump chronologique]
### Projets avancés
### Livrables produits
### Thèmes dominants

## 🎯 Aujourd'hui / Demain
[Tâches prioritaires, format actionnable : verbe + objet + deadline]
- [ ] ...
- [ ] ...

## 🚀 Semaine prochaine — [date J+1] au [date J+7]
[Plan par jour si possible, sinon par thème]

## 💡 Notes & signaux
[Thèmes récurrents, projets qui stagnent, opportunités à saisir]
```

### Étape 5 — Livrer
Finis ta réponse en partageant le lien vers le fichier :
`[Voir la TODO du jour](computer:///sessions/youthful-wizardly-turing/mnt/outputs/todo-YYYY-MM-DD.md)`

Ajoute 2-3 phrases maximum de synthèse : le point le plus important d'hier, la priorité n°1 aujourd'hui.

## CONTRAINTES
- **Langue** : français uniquement
- **Ton** : direct, factuel, pas de blabla (style Tim : phrases courtes, zéro bullshit)
- **Pas de remplissage** : si une section est vide (ex: pas de session hier), dire "Rien d'identifié" plutôt qu'inventer
- **Ne jamais inventer** des tâches qui ne sont pas explicitement dans les sessions — si tu déduis, précise "(déduit de…)"
- **Dates** : utilise `date` via Bash pour obtenir la date exacte du jour et calculer J-1, J-7, J+1, J+7
- **Contexte métier Tim** : SEO, AEO/GEO, IA, agentic search, Google Search Console, maillage interne, cocon sémantique, LinkedIn, newsletter "Algorithme", clients SEO

## FALLBACK
Si aucune session n'est trouvée sur la période, produis quand même le fichier avec la mention "Pas de session enregistrée sur cette période" et propose 2-3 tâches récurrentes génériques (revue de presse, post LinkedIn, veille SEO).