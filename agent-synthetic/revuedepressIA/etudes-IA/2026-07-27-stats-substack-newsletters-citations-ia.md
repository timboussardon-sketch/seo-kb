---
type: query
skill: seo-page-statistiques
status: draft
title: "Newsletters et citations IA 2025-2026 : 0,07 % des réponses pour Substack, 213 newsletters citées sur 2 millions de publications"
aliases: [stats-newsletters-ia, stats-substack-citations-ia-2026]
tags: [newsletter, substack, beehiiv, ghost, citations-ia, geo, aeo, paywall, crawlabilite]
created: 2026-07-27
updated: 2026-07-27
sources: 7
confidence: medium
---

# Newsletters et citations IA 2025-2026 : 0,07 % des réponses pour Substack, 213 newsletters citées sur 2 millions de publications

Substack héberge plus de 2 millions de publications. Les moteurs IA en citent 213. C'est le chiffre le plus brutal de ce panorama : sur la totalité du corpus Substack, moins de 0,011 % des newsletters apparaissent dans les réponses de ChatGPT, Claude, Gemini, Perplexity et Google AI Overviews — et encore, ces 213 sont des newsletters spécialisées en technologie et médias, pas un échantillon représentatif. Pour le reste de l'écosystème, qui inclut 100 000 publications monétisées, la réponse des moteurs IA est le silence.

## Les chiffres clés (vérifiés à la source)

### Substack dans le pool de citations IA

| Indicateur | Valeur | Source | Méthode |
|---|---|---|---|
| Part Substack dans les citations IA | **0,07 %** | Britopian, janvier 2026 | 1,7 million de prompts non brandés, multi-industries |
| Part Medium dans les mêmes données | **0,36 %** | Britopian, janvier 2026 | Même dataset — Medium = 5× plus cité |
| Citations Substack absolues (dataset) | **1 140** sur 1,7 M de prompts | Britopian, janvier 2026 | 8 industries : finance, voyage, auto, mode, streaming, alimentaire, B2B SaaS |
| Newsletters Substack citées régulièrement | **213** (seuil : 12 cit. min., 3 moteurs min.) | Everything-PR, déc. 2025 – mai 2026 | 60 prompts × 5 moteurs × 6 catégories |
| Total citations capturées dans l'étude EPR | **4 847** | Everything-PR, déc. 2025 – mai 2026 | Périmètre : tech, IA, médias, économie, product management, culture internet |

### L'écosystème newsletter en 2025-2026

| Plateforme | Newsletters actives | Lecteurs mensuels | Source |
|---|---|---|---|
| Substack | ~100 000 monétisées / 2 M+ publications au total | 20 M abonnés actifs (mai 2025) | Substack, Wikipedia (mars 2025 / oct. 2025) |
| Beehiiv | 65 000–75 000 | 350 M lecteurs mensuels | Beehiiv State of Newsletters 2026 |

### Effet paywall et accessibilité

- Chaque newsletter Substack avec paywall a sous-performé son nombre d'abonnés en poids de citation, parfois de manière importante (Everything-PR, 2026).
- La plateforme d'hébergement — Substack, Ghost ou Beehiiv — n'a aucun effet sur le poids de citation : seule l'accessibilité du contenu compte (Everything-PR, 2026).
- 61,7 % de toutes les citations IA sont des « citations fantômes » : la source est utilisée mais la marque n'est pas nommée dans la réponse (AuthorityTech, avril 2026, 3 981 domaines, 115 prompts, 4 moteurs).

### Les 5 newsletters qui percent dans les réponses IA

L'étude Everything-PR identifie cinq newsletters Substack qui apparaissent régulièrement sur au moins trois moteurs différents. Toutes partagent un profil identique : journalistes issus d'institutions — New York Times, Bloomberg, The Atlantic — avant de lancer leur propre publication.

1. Hub Intel (analyse secteur entertainment)
2. Mindholiday (conception de voyages)
3. OUTLET (veille business)
4. Chills, by Lauren Wolfe (journalisme d'investigation)
5. So What (analyse politique)

Aucune ne figure dans le top 10 global de l'étude, occupé par des newsletters à forte notoriété préexistante : Stratechery, Platformer, Big Technology, Slow Boring, Noahpinion, Lenny's Newsletter, The Pragmatic Engineer, Every, Garbage Day.

## L'effet paywall : la double peine structurelle

Les moteurs de recherche génératifs (présence dans les réponses IA) s'appuient sur deux sources distinctes pour décider ce qu'ils citent : les données d'entraînement (corpus figé) et le contenu récupéré en temps réel via le web. Dans les deux cas, le contenu payant pénalise la newsletter.

**Données d'entraînement.** Common Crawl, qui alimente une partie des corpus d'entraînement de GPT, Llama et d'autres modèles, ne déroule pas le JavaScript. Son robot (CCBot) capture le HTML brut avant que la vérification d'abonnement ne s'exécute — ce qui signifie que certains contenus derrière paywall se retrouvent en théorie dans les données d'entraînement (investigation The Atlantic, novembre 2025). Mais ce mécanisme est irrégulier, non systématique, et ne concerne pas la récupération en temps réel.

**Récupération en temps réel.** GPTBot, ClaudeBot, PerplexityBot tombent tous sous la règle générale du fichier robots.txt de Substack (vérification directe, juillet 2026) : aucun crawler IA n'est explicitement bloqué ni explicitement autorisé sur Substack. Ils peuvent accéder aux chemins publics, mais le JavaScript de vérification d'abonnement les bloque de facto sur les articles payants — ces bots n'exécutent pas le JavaScript.

**Résultat net.** Une newsletter à archive entièrement ouverte — même avec 40 000 abonnés — surclasse une newsletter à 800 000 abonnés dont 80 % des articles sont payants. C'est la conclusion directe de l'étude Everything-PR : le nombre d'abonnés ne prédit pas le poids de citation.

## Pourquoi ces chiffres traduisent un décalage structurel (transformation originale)

Les deux principales études sur ce sujet mesurent des objets différents, et les réconcilier produit un constat plus précis que chacune prise seule.

L'étude **Britopian** (1,7 million de prompts, 8 industries commerciales) mesure la **part de marché de Substack dans le pool total de citations IA** : 0,07 %. C'est une mesure de présence absolue.

L'étude **Everything-PR** (60 prompts, 6 catégories B2B/tech, 5 moteurs) mesure **lesquelles, parmi toutes les newsletters Substack, se font citer dans des catégories à forte concurrence rédactionnelle** : 213 sur 2 millions. C'est une mesure de sélectivité.

Ces deux chiffres ne se contredisent pas — ils décrivent deux faces du même problème. La part de marché est infime (0,07 %) parce que le ratio accessibilité/volume penche massivement du mauvais côté : la plupart des newsletters Substack sont soit entièrement paywallées, soit ne couvrent pas les sujets sur lesquels les moteurs IA reçoivent le plus de requêtes. La sélectivité est extrême (213 newsletters, dont 5 seulement atteignent plusieurs moteurs) parce que les moteurs IA appliquent implicitement un filtre d'autorité institutionnelle : les newsletters qui percent sont celles dont les auteurs ont construit leur crédibilité hors de Substack.

**Le paradoxe du rapport abonnés/citations** : la métrique d'engagement (nombre d'abonnés, taux d'ouverture de 44 % sur Substack contre 21 % pour la moyenne du marché) et la métrique de présence dans les réponses IA sont structurellement décorrélées. Un fort engagement par email n'implique pas une présence dans les réponses IA — et inversement. Les deux circuits de distribution (inbox vs. moteur IA) obéissent à des logiques opposées : l'un récompense la proximité avec le lecteur, l'autre récompense l'accessibilité des robots.

## Nos propres chiffres (données de première main)

Aucune mesure isolée de la présence de newsletters dans les réponses IA n'a été conduite sur le portefeuille de propriétés du vault. La newsletter *Algorithme* (algorithme.substack.com) est publiée sur Substack et hébergée en architecture subdomain — elle est donc soumise aux mêmes contraintes d'accessibilité que l'ensemble du corpus étudié.

Ce bloc est honnêtement réservé. Une mesure longitudinale (avant/après mise en archive complète ouverte) constituerait un test empirique direct de la thèse d'accessibilité. Ce chantier est inscrit dans la boucle sortie → apprentissage ([[preuves/index]]).

## Contre-analyse

**Biais de sélection de l'étude Everything-PR.** 60 prompts sur 6 catégories (tech, IA, médias, économie, product management, culture internet) ne représentent pas l'ensemble du spectre de requêtes. Ces catégories favorisent structurellement les newsletters spécialisées en B2B anglophone. Une newsletter de jardinage ou de finance personnelle en français avec une archive ouverte pourrait performer différemment dans son segment — mais le dataset ne le mesure pas.

**Méthodologie interne de l'étude Britopian.** L'analyse de 1,7 million de prompts est conduite par Michael Brito (Britopian) et publiée sur son propre site en janvier 2026. Aucun organisme tiers n'a validé la méthodologie, et le détail des requêtes n'est pas public. Le chiffre de 0,07 % est plausible — il est cohérent avec les ordres de grandeur d'autres études (Profound, SE Ranking) sur la concentration des citations — mais il ne doit pas être cité comme mesure indépendante.

**L'accessibilité n'est pas le seul filtre.** Les cinq newsletters régulièrement citées partagent une caractéristique que l'étude Everything-PR ne quantifie pas explicitement : leurs auteurs ont une présence documentée sur d'autres sites indexés (profils LinkedIn, articles dans la presse, citations dans des études). L'accessibilité de l'archive est nécessaire mais peut ne pas être suffisante. L'autorité préexistante de l'auteur — mesurable en liens entrants et mentions tiers — reste probablement le prédicteur dominant, comme pour les pages web classiques.

**Le bypass Common Crawl.** L'investigation de The Atlantic (novembre 2025) sur CCBot et le contenu payant introduit une nuance : une partie du contenu paywallé se retrouve dans les données d'entraînement, indépendamment du robot.txt et du JavaScript. Cela signifie que certains contenus Substack payants influencent les réponses des LLMs via la mémorisation — sans que la newsletter soit citée comme source en temps réel. L'effet "mémorisation vs. récupération" n'est pas dissociable dans les données disponibles.

**La plateforme irrélevante — sauf pour la valeur perçue de la migration.** L'étude EPR indique que Substack vs. Ghost vs. Beehiiv n'a pas d'impact sur le poids de citation. Mais cette conclusion reflète l'état d'un corpus où les auteurs qui migrent de Substack vers Ghost le font souvent en même temps qu'ils ouvrent leur archive et améliorent leur SEO on-site — les deux variables changent simultanément, rendant l'isolation difficile.

## FAQ

**Les newsletters francophones sont-elles davantage pénalisées ?**
Probablement oui, pour deux raisons cumulables. D'abord, le biais linguistique documenté des corpus d'entraînement (français = 0,16 % des données Llama 2, contre 4,7 % de la présence web francophone, étude Touvron et al. 2023). Ensuite, les catégories couvertes par les études disponibles sont quasi-exclusivement anglophones. Des données spécifiques sur les newsletters en français dans les citations IA n'existent pas à ce jour dans les études publiques consultées.

**Faut-il migrer de Substack vers Beehiiv pour améliorer sa présence dans les IA ?**
Non, selon les données disponibles. La plateforme n'est pas la variable déterminante. Ouvrir l'archive, éviter le paywall sur les contenus à forte valeur informationnelle, et construire une présence tiers documentée (mentions, liens) sont les leviers identifiés. La migration de plateforme n'apporte pas de gain intrinsèque.

**Est-ce que les newsletters bénéficient d'un accord de données spécifique avec Google ou OpenAI ?**
Aucun accord de données entre Substack et Google ou OpenAI n'est documenté publiquement à ce jour. Le contrat de données connu dans cet écosystème est celui entre Reddit et Google (60 millions de dollars par an, 2024, permettant l'accès à l'API Reddit pour l'entraînement des modèles Google).

**Comment expliquer que Medium soit cité 5× plus que Substack ?**
Medium opère un modèle hybride différent : la plupart des articles Medium sont accessibles au moins partiellement sans abonnement (3 articles gratuits par mois via le programme Partenaire), la plateforme héberge une masse de contenus techniques indexés depuis plus de 10 ans, et son architecture de domaine est unifiée (medium.com/article). Substack fragmente son contenu sur des sous-domaines individuels (auteur.substack.com), ce qui dilue l'autorité de domaine perçue par les moteurs.

## [À SOURCER]

- Part exacte des newsletters Substack avec paywall actif vs. archive entièrement ouverte (Substack ne publit pas ce ratio)
- Partenariat spécifique Google-Substack annoncé en décembre 2024 mentionné dans certaines analyses sectorielles — non confirmé à ce jour par une source primaire identifiée
- Données de citations spécifiques aux newsletters francophones dans les réponses IA (absent des études disponibles)
- Total exact de publications Substack en 2025-2026 (la donnée de 2 millions est une estimation de 2023 ; aucun chiffre officiel récent publié)
- Impact de la migration vers un domaine personnalisé sur Substack (auteur.com vs. auteur.substack.com) sur les citations IA

## Sources

| Intitulé | Organisme | Date | URL | Consulté le |
|---|---|---|---|---|
| Substack Citation Index 2026 | Everything-PR | Déc. 2025 – mai 2026 | https://everything-pr.com/the-substack-citation-index-2026 | 2026-07-27 |
| How Influential is Substack in the Generative Engines? | Britopian (Michael Brito) | Janvier 2026 | https://www.britopian.com/geo/substack-generative-engines/ | 2026-07-27 |
| Ghost Citations in AI (61.7%) | AuthorityTech.io / Search Engine Journal | Avril 2026 | https://authoritytech.io/curated/ghost-citations-ai-brand-visibility-2026 | 2026-07-27 |
| The State of Newsletters 2026 | Beehiiv | 2026 | https://www.beehiiv.com/blog/beehiiv-the-state-of-newsletters-2026 | 2026-07-27 |
| Inside the Newsletter Evolution of 2025 | Beehiiv | 2025 | https://www.beehiiv.com/blog/inside-the-newsletter-evolution-of-2025 | 2026-07-27 |
| Substack (article encyclopédique) | Wikipedia | Mis à jour mars 2025 | https://en.wikipedia.org/wiki/Substack | 2026-07-27 |
| Common Crawl and the AI Web Scraping Crisis | ScrapeTools (via The Atlantic, nov. 2025) | 2025 | https://scrapetalk.substack.com/p/common-crawl-and-the-ai-web-scraping | 2026-07-27 |
| Substack robots.txt (vérification directe) | Substack | Vérifié juillet 2026 | https://substack.com/robots.txt | 2026-07-27 |
| AI Data Licensing Deals (liste complète) | Magis / Alex Izydorczyk | 2024 | https://magis.substack.com/p/ai-data-licensing-deals | 2026-07-27 |
