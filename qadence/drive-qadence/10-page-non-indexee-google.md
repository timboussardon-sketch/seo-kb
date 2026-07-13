---
type: contenu
format: brief-hn
projet: qadence
statut: brief
requete_cible: ma page n'est pas indexée par Google
intention: Do
capacite_qadence: cron missing-pages + audit_gsc
schema: HowTo + Article
created: 2026-07-13
sources_vault: [[information-gain]], [[test-substitution-llm]], [[fraicheur-contenu]]
---

# Ma page n'est pas indexée par Google

Une page que Google n'indexe pas est souvent une page sans valeur ajoutée : elle reprend ce que le corpus existant dit déjà, un LLM la reproduirait à l'identique, et rien de neuf ne justifie sa place dans l'index.

## Une page sans valeur ajoutée ne mérite pas l'index

- Un contenu vaut par son information gain : il ajoute un chiffre, un fait vérifié, un angle unique ou une donnée terrain que le corpus n'a pas [[information-gain]]
- Le contraire est le contenu sans effort qui reprend mécaniquement l'existant, noté au plus bas par les Quality Raters [[information-gain]]

## Le test de substitution LLM révèle les pages jetables

- Demander à un LLM de produire la même réponse : s'il en génère 80 %, la page n'a pas de raison d'exister [[test-substitution-llm]]
- Une page substituable n'a aucun avantage défensif, le moteur génératif y répond directement [[test-substitution-llm]]
- Ce filtre élimine les pages-commodité : FAQ génériques, guides de quartier, listes « 10 choses à faire à X » [[test-substitution-llm]]

## Rendre la page indexable revient à lui donner ce que l'index n'a pas

- Injecter la data propriétaire ou terrain qu'un LLM ne peut pas reproduire [[test-substitution-llm]]
- Atomiser les affirmations : chaque claim découpé en fait vérifiable indépendamment [[information-gain]]
- Ajouter citations verbatim et statistiques sourcées, les deux leviers les plus forts du benchmark [[information-gain]]

## Une page ancienne et indifférenciée perd ses signaux

- La fraîcheur est un signal : à contenu équivalent, une page récente est reprise environ 3 fois plus qu'une page ancienne [[fraicheur-contenu]]
- La fraîcheur complète la pertinence sémantique et le contenu multimodal, elle ne les remplace pas [[fraicheur-contenu]]

## Lancer le diagnostic avec Qadence

- Le cron missing-pages liste les pages absentes de l'index à partir de la Search Console
- Pour chaque page, la grille de qualification applique le test de substitution avant toute réécriture [[test-substitution-llm]]
- La priorité va aux pages où ajouter de l'information gain change la donne [[information-gain]]
- La décision de réécrire, fusionner ou laisser tomber reste à toi

→ **Repérer mes pages non indexées** sur qadence.io/app
