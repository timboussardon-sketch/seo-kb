# Calibration — score de l'agent dans le temps

Écrit par l'agent 9 après chaque édition. Confronte le travail de l'agent à la réalité. C'est la mesure honnête de « est-ce que l'agent s'améliore ».

## Les 4 critères (note /5 par édition)

1. **Recoupement** : part des infos du corps corroborées par au moins 2 sources indépendantes.
2. **Angle inédit** : l'édition sort-elle quelque chose que les autres n'ont pas vu ?
3. **Lien doctrine** : l'actu est-elle reliée aux concepts de Tim ?
4. **Hook intelligent** : le titre prouve-t-il la valeur sans être racoleur ?

## Signaux de vérité-terrain

- **Interne** : taux de survie au fact-check, justesse des prédictions échues (voir `predictions.jsonl`).
- **Data réelle** : opens et clics (voir `engagement.jsonl`, branché plus tard).

## Journal des scores

| Édition | Recoupement | Angle | Doctrine | Hook | Survie fact-check | Note globale |
|---|---|---|---|---|---|---|
| 2026-05-30-v2 | 4/5 | 5/5 | 4/5 | 4/5 | 4 retenues / 6 candidates | 4,2/5 |

### Notes du run d'amorçage (2026-05-30-v2)

- **Recoupement** : info du jour (Information Agents) triple-sourcée (blog.google primaire + Lumar + SEJ). Brèves sur 1 à 2 sources.
- **Angle** : choisi distinct de l'édition du matin (guide AEO du 15 mai) pour éviter la redite. Information Agents = angle frais et méta.
- **Fact-check, ce qui a été écarté du corps** : étude Yext « 86 % de citations brand-managed » (octobre 2025, hors fenêtre fraîcheur 30 j) ; chiffre d'overlap citations vs top-10 organique (BrightEdge, conflit 54 % vs 17 % selon méthode, mono-source) ; le « +157 % » de renvois ChatGPT laissé en qualitatif (mono-analyse). Conforme à la règle anti-hallucination.
- **À surveiller** : pas encore de signal lecteur (engagement.jsonl vide tant que l'envoi n'est pas branché).
