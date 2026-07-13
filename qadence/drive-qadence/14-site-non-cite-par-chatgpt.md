---
type: contenu
format: brief-hn
projet: qadence
statut: brief
requete_cible: mon site n'est pas cité par ChatGPT
intention: Do
capacite_qadence: Visibilité IA (test citations ChatGPT/Gemini) · score_geo
schema: Article + FAQPage
created: 2026-07-13
sources_vault: [[geo]], [[metriques-visibilite-geo]], [[grounding-score]], [[structural-information-geo]], [[test-substitution-llm]], [[methode-organikk-4-piliers]]
---

# Pourquoi votre site n'est pas cité par ChatGPT

ChatGPT ne cite pas un site pour trois raisons qui se diagnostiquent séparément : il ne le récupère pas, la page est mal alignée avec l'intention, ou son contenu est reproductible par le modèle.

## Être cité par ChatGPT ne dépend pas de votre position Google

- Être récupéré, compris et cité par un LLM est un travail distinct du classement par liens [[geo]]
- Le ranking classique donne une position unique par URL, il ne mesure pas la citation dans une réponse générative [[metriques-visibilite-geo]]
- Une même URL peut être citée 0, 1 ou N fois dans une réponse [[metriques-visibilite-geo]]
- La source est exposée dans la réponse directe même sans clic vers le site [[metriques-visibilite-geo]]

## Première cause : le site n'est pas récupéré

- Les champs structurels (title, meta, headings, schema) sont le levier de récupération le plus efficace, pas le corps de texte [[structural-information-geo]]
- Un title vague ne donne aucun signal au retrieval, il faut l'entité cible plus un chiffre ou un modificateur de spécificité [[structural-information-geo]]
- Réécrire seulement le corps de texte dégrade la récupération car le chevauchement lexical baisse [[structural-information-geo]]
- Le schema markup type les entités (Article, FAQPage, Product) et rend la page récupérable [[structural-information-geo]]

## Deuxième cause : la page est mal alignée avec l'intention

- Le grounding mesure la proximité vectorielle entre l'intention de la requête et la page [[grounding-score]]
- Une page hors-sujet a un vecteur trop éloigné, elle n'est pas servie [[grounding-score]]
- Une page pertinente mais redondante n'apporte aucun gradient, elle est ignorée [[grounding-score]]
- Le grounding se calcule au niveau du passage le plus pertinent, pas sur la moyenne diluée du document [[grounding-score]]

## Troisième cause : la page est substituable par le modèle

- Si un LLM produit 80 % de la page, il répond directement et ne cite pas la source [[test-substitution-llm]]
- Les pages-commodité (FAQ génériques, guides sans donnée) ne créent aucun avantage défensif [[test-substitution-llm]]
- La donnée propriétaire (data terrain, prix réels, configurations de stock) rend une page non substituable [[test-substitution-llm]]
- Le test se refait périodiquement : ce qu'un LLM ne génère pas aujourd'hui, il le générera dans six mois [[test-substitution-llm]]

## Ce que la Surprise et le Grounding règlent ensemble

- La méthode Organikk pose le Grounding (pourquoi on rank) et la Surprise (pourquoi on lit) comme piliers cumulatifs [[methode-organikk-4-piliers]]
- Un début de réponse cité pèse plus qu'une citation en fin, selon la pondération décroissante de Imp_pos [[metriques-visibilite-geo]]
- La densité de phrases citables augmente la présence de la source dans la réponse [[metriques-visibilite-geo]]

## Lancer le diagnostic avec Qadence

- La fonctionnalité Visibilité IA de Qadence interroge ChatGPT et Gemini pour voir si votre site ressort comme source citée sur vos requêtes [[metriques-visibilite-geo]]
- Le score GEO agrège les trois causes : récupération structurelle, alignement d'intention, singularité du contenu [[geo]]
- Chaque écart pointe vers un levier précis à corriger, pas vers un constat général [[geo]]

→ **Lancer le diagnostic Visibilité IA** sur qadence.io/app
