# Gate de publication — grille de score (content-brain)

Notée avant de publier chaque contenu, loggée dans `ledgers/runs.jsonl`. Le contenu ne sort que si le gate passe. Calquée sur la calibration de SyntheticBrain, adaptée à la production SEO/GEO.

| Axe | Mesure | Seuil de sortie |
|---|---|---|
| `surprise_gap` | angle inédit / inversion expertise, ce que les autres n'ont pas dit (0-5) | ≥ 3 |
| `data_density` | nb de claims `verified` portés par de la data réelle (GSC, calls, SAV, étude propriétaire) | ≥ 2, et 0 chiffre non sourcé |
| `decisional_intent` | la page vise une requête Do / décisionnelle, pas un informationnel mangé par les LLM (0-5) | ≥ 3 |
| `grounding` | densité d'entités attendues + passage extractible (réponse nette sous la question) (0-5) | ≥ 3 |
| `title_intel` | titre intelligent qui prouve la valeur, jamais racoleur (faible/moyen/élevé clickbait_risk) | clickbait faible |
| `anti_ia_writing` | check anti-IA writing passé (zéro mot banni, zéro tiret cadratin, zéro métaphore) | pass |
| `cannibalisation_risk` | proximité d'intention vs `said_index.jsonl` du projet | faible |

Règle dure : tout claim qui entre dans le corps est `verified` dans `claims.jsonl` (source réelle, ≥2 sources indépendantes OU une source à historique/data propriétaire). Un `uncertain` se creuse ou s'écarte, jamais publié. Aucun chiffre inventé : sinon `[À SOURCER]`.
