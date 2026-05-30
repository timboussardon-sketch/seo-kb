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
| 2026-05-30-v3 | 5/5 | 5/5 | 5/5 | 4/5 | corps 100% recoupé ≥2 sources | 4,7/5 |

### Notes du run d'amorçage (2026-05-30-v2)

- **Recoupement** : info du jour (Information Agents) triple-sourcée (blog.google primaire + Lumar + SEJ). Brèves sur 1 à 2 sources.
- **Angle** : choisi distinct de l'édition du matin (guide AEO du 15 mai) pour éviter la redite. Information Agents = angle frais et méta.
- **Fact-check, ce qui a été écarté du corps** : étude Yext « 86 % de citations brand-managed » (octobre 2025, hors fenêtre fraîcheur 30 j) ; chiffre d'overlap citations vs top-10 organique (BrightEdge, conflit 54 % vs 17 % selon méthode, mono-source) ; le « +157 % » de renvois ChatGPT laissé en qualitatif (mono-analyse). Conforme à la règle anti-hallucination.
- **À surveiller** : pas encore de signal lecteur (engagement.jsonl vide tant que l'envoi n'est pas branché).

### Notes 2026-05-30-v3

- **Recoupement (5/5)** : info du jour (commerce agentique / Universal Cart / UCP) sur primaire Google (blog.google 19 mai) + Search Engine Land (20 mai) + docs Google Merchant. Chaque brève sur ≥2 sources indépendantes (core update : SEL + SEJ ; Cloudflare : Radar + TechnologyChecker ; conversion : Seer + Similarweb).
- **Angle (5/5)** : commerce agentique = l'agent qui ACHÈTE, explicitement distingué des Information Agents (qui lisent) traités en v2. Angle « ton flux produit devient ta vitrine » non vu ailleurs dans la presse FR.
- **Doctrine (5/5)** : branché sur `mots-cles-actionnels` (transactionnel = seuls KW qui font du CA) et `agentic-search` (être sélectionné par l'agent pour accomplir une tâche). Phrase doctrine « on ne vend plus du trafic, on vend de la performance ».
- **Piège anti-hallucination déjoué** : les résumés de WebSearch dataient à tort de 2026 des études de 2025 (Seer juin 2025 / Cloudflare juillet 2025). Vérif sur source primaire → Seer daté honnêtement dans le corps, Cloudflare repivoté sur les données fraîches du 18 mai 2026. Leçon enregistrée dans le registre (note sur seer-interactive et cloudflare-radar).
- **Écarté du corps** : ratios crawl-to-refer précis type 13 528:1 (cités par agrégateurs mais non confirmés sur primaire à la bonne fenêtre) → remplacés par la formulation corroborée « des dizaines de milliers de pages pour un visiteur ». Parts ChatGPT 68 % / Gemini 18 % (Similarweb, données janv. 2026, hors fenêtre 30 j) → non utilisées comme brève.
- **Prédictions ouvertes** : P-2026-05-30-2 (vente via checkout agentique avant 2026-09-30) et P-2026-05-30-3 (Googlebot sous 27 % du crawl IA d'ici fin 2026).
