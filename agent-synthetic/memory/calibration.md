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
| 2026-05-30-v4 | 5/5 | 3/5 | 5/5 | 4/5 | 8 retenus, corps recoupé ≥2 sauf 1 fragile attribué | 4,3/5 |
| 2026-05-30-v5 | 5/5 | 4/5 | 4/5 | 4/5 | 6 claims retenus, corps recoupé ≥2 sauf FAQ (doc officielle) et 11 % (mono-étude flaguée) | 4,3/5 |

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

### Notes 2026-05-30-v4

- **Recoupement (5/5)** : info du jour (llms.txt non utilisé par Google) sur 3 sources indépendantes dont Search Engine Land (seed historique) : Illyes au Search Central Deep Dive APAC du 23 juillet 2025, Mueller (comparaison meta keywords) confirmé par 2 sources, incident d'apparition du fichier sur des pages Google sur 2 sources. Chaque brève sur ≥2 sources (Gemini : Similarweb + TechRadar + TechnologyChecker ; champ de recherche : blog.google + Tom's Guide + SEJ ; CTR AIO : SEL + Seer + SEJ).
- **Angle (3/5)** : volontairement plus bas. Overlap thématique partiel reconnu avec le run cloud du même jour, dont l'info du jour était le guide IA du 15 mai (« llms.txt inutile, AEO=SEO »). Le hook v4 est distinct (la contradiction : Google dit non, mais le fichier est apparu sur ses propres pages) et apporte du matériel neuf (citation Illyes datée, comparaison Mueller, incident, étude SE Ranking 39 000 domaines, benchmark SAGEO). Mais ce n'est pas un sujet vierge, d'où 3/5 et non 5/5.
- **Doctrine (5/5)** : lien réel et non décoratif vers `structural-information-geo` (le levier au retrieval = champs structurels + schema, pas un fichier dédié) et `aeo` (être cité = SEO normal, pas un canal séparé). La donnée empirique de la KB et la position de Google convergent.
- **Piège fraîcheur géré** : étude Seer du CTR AIO datée explicitement dans le corps (publi SEL 24 avril 2026, données jan2025-fév2026), au-delà de 30 j donc présentée comme tendance, pas comme état du jour. Parts Gemini/ChatGPT : chiffres exacts contradictoires entre Similarweb/Statcounter/agrégateurs → présentés comme divergence assumée, direction seule retenue.
- **Écarté du corps** : « planning queries +80 % » et « marques citées +35 % de clics » issus des annonces I/O (mono-source com Google ou redite avec la brève Seer plus solide). SE Ranking 39 000 domaines gardé mais marqué fragile et attribué (mono-source).
- **Prédiction ouverte** : P-2026-05-30-4 (position « llms.txt non utilisé » maintenue par Google d'ici fin 2026).

### Notes 2026-05-30-v5

- **Recoupement (5/5)** : info du jour (formats publicitaires Gemini dans AI Mode, GML du 20 mai) sur 2 sources indépendantes, dont la primaire blog.google + Search Engine Land (seed historique). Brèves : OpenAI ads (SEL x2 + SEJ), divergence citations (Averi + Profound, direction recoupée), Ahrefs 38 % (Ahrefs + SEJ), FAQ (doc officielle Google Search Central). Une seule info du corps tient sur une source unique : la dépréciation FAQ, mais c'est une doc officielle de l'éditeur lui-même (recoupement inutile), citation textuelle.
- **Angle (4/5)** : la publicité payante dans la réponse générative n'avait pas été traitée. Distinguée explicitement de v3 (checkout agentique organique via UCP) : ici l'angle est l'emplacement payé étiqueté « Sponsored », et la distinction citation organique / achat d'espace. Le rapprochement Google (GML) + OpenAI (ChatGPT ads) sur le même principe d'étiquetage est l'apport propre de l'édition.
- **Doctrine (4/5)** : lien réel vers `aeo` (la publicité ne remplace pas la citation organique : deux voies distinctes) et `agentic-search` (paiement natif UCP dans la réponse = être sélectionné pour transiger). Lien non décoratif mais l'actu publicitaire n'est pas au cœur de la doctrine GEO actuelle, d'où 4 et non 5.
- **Piège fraîcheur géré** : chiffre 11 % (Averi) explicitement présenté comme mono-étude ; seule la direction (faible recouvrement, sources distinctes) présentée comme corroborée. Caveat méthodologique d'Ahrefs (parsing amélioré → datasets non comparables) repris tel quel dans le corps.
- **Écarté du corps** : bilan gagnants/perdants du core update de mai (déploiement non clos avant ~4 juin, directive : attendre ≥1 semaine après la fin) ; chiffres d'audience I/O (2,5 Md MAU AIO, AI Mode 1 Md) redite v2/v4.
- **Prédictions ouvertes** : P-2026-05-30-5 (un format pub AI Mode sorti du stade annonce d'ici fin 2026) et P-2026-05-30-6 (recouvrement citations ChatGPT/Perplexity < 25 % confirmé d'ici fin 2026).
