---
type: query
skill: seo-page-statistiques
title: "Claude comme moteur de citation : profil, domaines favoris, part de voix 2026"
tags: [geo, aeo, claude, citations-ia, brave-search, share-of-voice, profil-citation, editorial, social-citation]
created: 2026-06-26
updated: 2026-06-26
sources: 8
confidence: medium
status: draft
---

# Claude comme moteur de citation : profil, domaines favoris, part de voix (données 2026)

**Claude cite 11 fois moins de contenu social que Google AI Overviews.** Sur 3,25 milliards de citations analysées en mars 2026, le taux de contenu social dans les réponses de Claude atteint 3,99 % — le deuxième plus bas parmi sept moteurs. Ce chiffre n'est pas anodin : il traduit une architecture de récupération fondamentalement différente des autres moteurs génératifs, et impose une stratégie de présence distincte.

---

## Les chiffres clés (vérifiés à la source)

### Taux de citation sociale par moteur IA

Source : Profound, mars 2026, 3,25 milliards de citations, 14 pays, 7 modèles.

| Moteur IA | Taux de citation sociale |
|---|---|
| Google AI Overviews | 15,3 % |
| Google AI Mode | 14,5 % |
| Perplexity | 11,3 % |
| ChatGPT | 9,1 % |
| Microsoft Copilot | 4,3 % |
| **Claude** | **3,99 %** |
| Gemini | 3,6 % |

Claude et Gemini forment un groupe à part : tous deux évitent massivement le contenu social là où les moteurs Google et Perplexity y puisent entre 11 et 15 % de leurs citations.

### Part de voix de Claude dans les referrals B2B (trafic entrant)

Source : Goodie, panel B2B, données GA4 referrer, août 2025 – avril 2026.

| Mois | Part Claude | Part ChatGPT |
|---|---|---|
| Janvier 2026 | 11,8 % | nd |
| Février 2026 | 10,8 % | nd |
| Mars 2026 | 16,8 % | nd |
| Avril 2026 | 18,5 % | 62,6 % |

Sur ce panel, Claude est passé de 1,4 % (mai–août 2025) à 18,5 % (avril 2026) des referrals IA vers des sites B2B. La progression est statistiquement robuste : sur 30 jours, 14 marques sur 16 ont progressé (probabilité de hasard : 0,21 % au test binomial).

### Trafic web vers les plateformes IA (Similarweb)

Source : Similarweb, trafic mondial tous appareils vers les domaines des plateformes, jusqu'au 26 mai 2026.

| Période | Claude | ChatGPT |
|---|---|---|
| Juin 2025 | 1,6 % | 76,4 % |
| Janvier 2026 | 2,0 % | nd |
| Mars 2026 | 6,0 % | nd |
| Mai 2026 | 8,9 % | 52,7 % |

Claude a multiplié sa part par 5,6 en douze mois sur ce périmètre. Cette métrique mesure les visites directes aux domaines, pas les citations dans les réponses IA.

### Citations par réponse et structure de contenu cité

Source : Oltre, analyse de 2 170 URLs citées par Claude, 2026.

- Citations moyennes par réponse : 2 à 3 (contre 5 à 12 pour Perplexity, 2 à 4 pour ChatGPT)
- Extensions de domaine des URLs citées : .com (58,5 %), .ai (28,1 %), .io (5,1 %)
- Structure des URLs : chemin /blog/ (56 %), listicle /best-…, /top-…, /vs-… (47 %), page d'accueil (3 %)
- Token d'année dans l'URL (2024, 2025 ou 2026) : 24 % des URLs citées
- Grands médias généralistes (Forbes, TechCrunch, NYT, Bloomberg) : 0 URL dans cet échantillon tech
- Plateformes sociales (Reddit, LinkedIn, YouTube, Quora) : 0 URL dans cet échantillon tech

### Fraîcheur des sources journalistiques

Source : 5WPR, Citation Source Audit Q1 2026, synthèse de 680 millions de citations (6 études indépendantes, août 2024 – avril 2026).

- 36 % des citations journalistiques de Claude datent des 12 derniers mois
- Comparaison : 56 % pour ChatGPT sur le même périmètre
- Claude conserve plus longtemps la valeur de citation des publications établies

### Routing via Brave Search

Source : Profound 2025, rapporté par 5WPR — non vérifié indépendamment par 5WPR.

- 86,7 % des URLs citées par Claude lors de sessions avec navigation web active se recoupent avec les résultats organiques de Brave Search
- Ce chiffre concerne Claude avec l'outil de navigation activé (fonctionnalité optionnelle, non activée par défaut dans l'API)

---

## Analyse : Claude, moteur éditorial par architecture

### Un moteur sans canal social structurel

Le taux de 3,99 % de contenu social chez Claude n'est pas seulement une préférence éditoriale. Par défaut, Claude n'a pas accès au web en temps réel. Quand la navigation est activée via l'API Anthropic, elle passe par Brave Search — un moteur qui, structurellement, ne crawle pas Reddit, LinkedIn ou les fils X comme source prioritaire. Le faible taux de citation sociale est donc en partie une conséquence de l'infrastructure, pas uniquement du modèle.

ChatGPT, Perplexity et Google AI Overviews ont des accords directs avec Reddit (OpenAI depuis 2024, Google depuis 2024) et des partenariats de données ou crawlers dédiés aux réseaux sociaux. Claude n'a aucun accord de ce type déclaré publiquement.

### Le profil éditorial : long-form et domaines en .ai

La part de 28,1 % de domaines .ai dans les URLs citées par Claude (Oltre, 2 170 URLs) est remarquable. Elle traduit une surreprésentation des outils SaaS, des documentations techniques et des blogs de startups tech dans l'index Brave Search mobilisé par Claude. Ce profil diverge fortement de ChatGPT, qui cite Wikipedia dans 47,9 % des cas sur ses sources les plus fréquentes (Profound / Averi, 680 millions de citations).

5WPR identifie dans ses agrégations les publications suivantes comme surreprésentées chez Claude : The New York Times, The Atlantic, The New Yorker, The Economist. Ces sources sont cohérentes avec un modèle entraîné sur des corpus de haute qualité éditoriale — mais elles n'apparaissent pas dans l'analyse de 2 170 URLs tech d'Oltre. Les deux observations ne se contredisent pas : le profil change selon le domaine de requête.

### La réconciliation des chiffres sur le social

Deux chiffres coexistent dans les études disponibles pour Claude :
- 1 % de contenu social (Qwairy, 118 000 réponses, jan.–mars 2026, données vault [[sources/2026-06-20-stats-citations-ia-domaines-recouvrement]])
- 3,99 % (Profound, 3,25 milliards de citations, mars 2026)

L'écart s'explique par la définition du périmètre. Qwairy mesure les domaines uniques cités (31 244 domaines pour Claude) en classifiant "social" comme les grandes plateformes UGC (Reddit, YouTube, Facebook, Twitter/X). Profound intègre une classification plus large en 5 catégories — social, earned media, earned institutions, UGC, PR wire — et sur 14 pays, dont des marchés où les pratiques de citation varient. Le 1 % de Qwairy et le 3,99 % de Profound ne mesurent pas exactement la même chose. Profound est plus représentatif par volume (3,25 Md vs 118 000) ; Qwairy est plus récent et plus précis sur le périmètre des domaines.

---

## Pourquoi ces chiffres divergent selon la méthodologie

La part de voix de Claude varie de 2,66 % (Statcounter, visites chatbot mondiales, avril 2026) à 21,1 % (First Page Sage, part de marché utilisateurs, juin 2026) en passant par 8,9 % (Similarweb, trafic plateforme, mai 2026) et 18,5 % (Goodie, referrals B2B, avril 2026). Ces quatre chiffres ne mesurent pas le même périmètre :

| Source | Ce qui est mesuré | Résultat Claude |
|---|---|---|
| Statcounter (avr. 2026) | Visites JavaScript-tracked sur les domaines chatbots | 2,66 % |
| Similarweb (mai 2026) | Trafic web tous appareils vers les domaines IA | 8,9 % |
| Goodie (avr. 2026) | Referrals GA4 depuis Claude vers des sites B2B | 18,5 % |
| First Page Sage (juin 2026) | Part déclarée des utilisateurs de chatbots | 21,1 % |

Statcounter sous-représente les usages API (pas de JavaScript tag) et les usages mobile app. Goodie sur-représente les audiences tech/B2B. First Page Sage est survey-based. Similarweb s'arrête aux domaines directs et ignore les intégrations (Claude dans Cursor, Notion, etc.). La progression de Claude est réelle sur tous les panels ; l'amplitude exacte dépend de la population mesurée.

---

## Nos propres chiffres (données de première main)

Pas de mesure de première main disponible dans ce vault sur les citations Claude. Les fiches preuves actives ([[preuves/2026-05-16-pseo-secteur-ville-data-proprietaire]], [[preuves/2026-06-12-golfiller-instrumentation-client]]) instrumentalisent des URLs publiées mais ne mesurent pas encore les citations IA par moteur. Bloc réservé pour le jalon GSC J+30 une fois le service account branché ([[preuves/SETUP-GSC]]).

---

## Contre-analyse

### Les limites structurelles de ces données

**L'échantillon Oltre est trop petit et trop biased.** 2 170 URLs dans un périmètre tech/SaaS ne permettent pas de généraliser à l'ensemble des réponses Claude. La conclusion "0 URL de grand média" dans cet échantillon ne contredit pas les données 5WPR, mais souligne que le profil de citation change radicalement selon le domaine de la requête.

**Le routing Brave Search est "non vérifié indépendamment" par 5WPR.** Ce chiffre de 86,7 % d'overlap provient de Profound 2025 et n'a pas été reproduit par une autre équipe. L'activation de la navigation web dans Claude est une fonctionnalité optionnelle qui nécessite des outils activés côté API ou des abonnements Claude.ai spécifiques — elle ne correspond pas à l'usage standard d'un utilisateur API de base.

**Le modèle ne browse pas par défaut.** Contrairement à Perplexity (search-first par conception) ou ChatGPT avec Web Browse activé, Claude s'appuie principalement sur ses données d'entraînement. Les études de citation Claude mesurent donc en partie des connaissances figées au moment du training cutoff (janvier 2025 pour Claude 3.x) — ce qui biaise les résultats vers du contenu préexistant au cutoff.

### Le biais de l'utilisateur Claude

Claude est surreprésenté chez les développeurs, les chercheurs et les équipes B2B tech (70 % du Fortune 100 selon Anthropic). Ces utilisateurs formulent des requêtes différentes des recherches grand public sur ChatGPT. La différence de profil de citation entre Claude et ChatGPT reflète aussi une différence de population d'utilisateurs, pas uniquement une différence de modèle ou d'infrastructure.

### La position des acteurs

Anthropic communique peu sur les comportements de citation de Claude. Les données disponibles viennent quasi exclusivement d'outils tiers (Profound, Qwairy, Oltre, SE Ranking) qui ont un intérêt commercial à démontrer que le "GEO" nécessite des outils de mesure spécialisés par moteur. Ce n'est pas un motif suffisant pour invalider les données, mais c'est une raison de réserver les conclusions nuancées.

---

## FAQ

**Claude est-il activé pour la recherche web par défaut ?**
Non. Claude s'appuie sur ses données d'entraînement par défaut. La navigation web via Brave Search est disponible avec certains abonnements Claude.ai et via l'API avec les outils activés explicitement. Les études de citation mesurent les sessions avec navigation activée pour obtenir des données sur les domaines cités en temps réel.

**Qu'est-ce qui détermine si un domaine est cité par Claude ?**
Trois facteurs documentés : (1) présence dans l'index Brave Search si la navigation est active, (2) présence dans les données d'entraînement d'Anthropic, (3) signaux d'autorité (Domain Authority élevé, structure éditoriale, fraîcheur pour les contenus indexés). L'étude arXiv en santé (10 000+ citations) donne un DA médian de 92 pour les sources citées.

**Peut-on optimiser spécifiquement pour Claude ?**
Oui, avec un angle différent de Google ou Perplexity. La surreprésentation des domaines .ai et des structures /blog/ + listicle chez Claude (Oltre, 2 170 URLs) suggère que le contenu structuré, long-form, hébergé sur des domaines tech récents performe mieux que le contenu social ou les pages d'accueil. La fraîcheur URL (token d'année) compte aussi davantage que chez d'autres moteurs.

**Claude va-t-il grossir comme moteur de citation ?**
Les trajectoires Goodie (+16,7 pts en un an sur les referrals B2B) et Similarweb (×5,6 en trafic direct) indiquent une croissance rapide, depuis une base basse. À 18,5 % des referrals B2B en avril 2026, Claude est déjà le 2e moteur IA après ChatGPT sur cette population. Le lancement de Claude.ai Search (navigation par défaut) et de l'intégration avec Amazon Alexa+ pourraient accélérer cette progression sur le grand public.

---

## [À SOURCER]

- **Top 50 domaines cités spécifiquement par Claude** (avec pourcentages individuels) : le rapport 5WPR donne les 50 domaines agrégés tous moteurs confondus, pas Claude seul.
- **65 % earned media / 1 % social (Qwairy)** : ce chiffre figure dans le vault ([[sources/2026-06-20-stats-citations-ia-domaines-recouvrement]]) mais la page primaire Qwairy fetchée le 2026-06-26 ne le confirme pas numériquement. Il provient probablement de l'analyse Profound/Averi sur 680 millions de citations — à distinguer du chiffre 3,99 % de la publication Profound de mars 2026.
- **Overlap de domaines Claude / autres moteurs** : les données de recouvrement inter-moteurs disponibles (SE Ranking, Qwairy, Profound) ne désagrègent pas Claude séparément dans les paires publiées.
- **Domain Authority médian 92 (étude arXiv santé, 10 000+ citations)** : la référence arXiv n'a pas été fetchée directement lors de cette étude. Chiffre intermédiaire via AEO Vision.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté |
|---|---|---|---|---|
| "How Query Language Reshapes AI Citations" — taux de citation sociale par moteur (3,25 Md) | Profound | Mars 2026 | https://www.tryprofound.com/blog/how-query-language-reshapes-ai-citations | 2026-06-26 |
| "5W Citation Source Audit Q1 2026" — Brave routing 86,7 %, journalistic freshness 36 % | 5WPR | Juin 2026 | https://www.5wpr.com/research/citation-source-audit-q1-2026/ | 2026-06-26 |
| "AI Platform Citation Source Index 2026" — synthèse 680 M citations | 5WPR / Everything-PR | Mai 2026 | https://everything-pr.com/ai-platform-citation-source-index-2026 | 2026-06-26 |
| "How Claude Picks Sources" — analyse 2 170 URLs, .ai 28 %, listicles 47 % | Oltre | 2026 | https://www.oltre.ai/blog/how-claude-picks-sources-technical-breakdown-claude-citations/ | 2026-06-26 |
| "AI Search Traffic Report 2026" — referrals B2B Claude 18,5 % | Goodie | Juin 2026 | https://higoodie.com/blog/ai-search-traffic-report-2026/ | 2026-06-26 |
| "ChatGPT drops to 52,7% as Claude triples its AI traffic share" — Similarweb, Claude 8,9 % | PPC Land / Similarweb | Juin 2026 | https://ppc.land/chatgpt-drops-to-52-7-as-claude-triples-its-ai-traffic-share/ | 2026-06-26 |
| "Top Generative AI Chatbots by Market Share" — Claude 21,1 % juin 2026 | First Page Sage | Juin 2026 | https://firstpagesage.com/reports/top-generative-ai-chatbots/ | 2026-06-26 |
| Vault seo-kb — Qwairy 118 K réponses, Claude 31 244 domaines uniques | Qwairy (rapporté) | Jan.–mars 2026 | [[sources/2026-06-20-stats-citations-ia-domaines-recouvrement]] | 2026-06-26 |
