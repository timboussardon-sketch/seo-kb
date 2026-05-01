---
source: "https://organikk.co/blog/wiki-ia-obsidian-claude"
slug: wiki-ia-obsidian-claude
title: "Créer un système propriétaire pour son SEO avec Claude + Obsidian, Organikk"
author: "Timothée Boussardon"
date_published: 2026-04-12
date_scraped: 2026-04-30
description: "Claude se connecte à Obsidian, ingère ton contenu et génère automatiquement les liens pour que tu ne redémarres jamais une conversation IA depuis zéro. Un système de mémoire synthétique qui exploite 10 ans d'expertise SEO sans saturation de tokens."
type: article-blog-organikk
---

# Créer un système propriétaire pour son SEO avec Claude + Obsidian, Organikk

On connaît tous ce problème : à chaque nouvelle session, une IA repart presque de zéro. Presque, parce que Claude lit les premières lignes de ton fichier CLAUDE.md au démarrage. Il connaît tes règles, ton contexte, tes préférences. Mais avec 200+ pages de connaissances accumulées, un seul fichier mémoire ne suffit plus. La fenêtre de contexte explose, la cohérence se dégrade, et tu finis par choisir quoi sacrifier.

La mémoire synthétique résout ce problème. En branchant [[cli-tools-optional|Claude Code]] sur un dossier [[obsidian-as-ide|Obsidian]], tu crées un **wiki que l'IA maintient elle-même**, un wiki qui se densifie, s'interconnecte et se bonifie à chaque source ajoutée. Concrètement, toutes tes connaissances SEO (fiches clients, exports GSC, notes de meeting, résultats passés) deviennent mobilisables par Claude en quelques secondes, **sans jamais halluciner** puisque l'IA raisonne sur tes propres fichiers. Le setup tient en trois étapes, coûte 20 euros par mois pour Claude plus Obsidian gratuit, et ne demande aucune ligne de code. Ce qui change, c'est que **tes 10 ans d'expertise deviennent un avantage compétitif structurel** que l'IA exploite au lieu de l'ignorer.

## 01 ·Ce que je pense de notre utilisation de l'IA en tant que consultant SEO

Il y a un écueil dans lequel beaucoup de SEO sont en train de tomber : se dire "OK, Claude va tout faire à ma place, je lâche un vocal, et regarde, c'est génial". Sauf que non. Pas exactement.

Selon une étude sectorielle 2026, 70% des équipes SEO disent que l'IA accélère leur production de contenu. Seulement 19% disent qu'elle améliore la qualité. Voilà le vrai problème. La vitesse n'est pas un avantage compétitif quand tout le monde a accès au même outil. Ce qui reste, c'est la qualité, et la qualité vient de ce que toi tu sais, pas de ce que l'IA sait.

Savoir prendre des raccourcis sur Claude, limiter sa réflexion, ne pas construire, ça te transforme en exécutant de ta propre IA. En réalité, on peut très vite devenir l'assistant de notre propre assistant.

J'en parle depuis un moment, mais certaines études sérieuses le confirment : le contenu full IA rank mal, avec des positions en top 1 seulement 9% du temps, contre 80% pour le contenu humain ou hybride selon une étude sectorielle qui a analysé 42 000 URLs. Ok, à partir de la position 5, l'écart se resserre. Mais personne ne vise la position 5. Évidemment ici ce n'est pas une question IA vs humain, mais c'est la qualité des données que l'on est capable de donner et le workflow de rédaction, pour par exemple venir fact checker les informations distillées dans son contenu, ou la mise à jour des données.

Créer un système SEO, c'est assembler deux choses que l'IA ne produit pas toute seule : **de la [[data-proprietaire|data propriétaire]]** et l'architecture qui s'améliore à chaque contenu. C'est ça, la mémoire synthétique. Pas seulement savoir prompter. Parce que si un vocal suffit à générer un prompt qui génère lui-même un workflow, il n'y a plus d'avantage à prompter. Demain, un ado de 15 ans le fera aussi bien que toi. Ce qu'il n'aura pas, c'est 6 ans de données terrain.

Aujourd'hui, tout le monde te dit qu'il n'a jamais été aussi simple de faire du SEO. Demande à n'importe quel consultant, il te dira le contraire. La compétition est plus forte, l'IA mange le contenu généraliste, et il reste les mots-clés business là où la compétition est maximale. Le March 2026 Core Update vient de le confirmer : Google filtre le contenu IA produit à grande échelle sans supervision humaine et renforce le poids de l'[[information-gain]], le contenu qui apporte quelque chose de neuf.

Je pense que l'erreur serait de simplifier ton usage de l'IA. Personnellement, je fais tout le contraire. Je construis un système propriétaire pensé pour tenir les cinq prochaines années, même si tout va très vite. Commencer par constituer une vraie mémoire en local, collecter de la bonne data pour faire la différence sur la SERP.

On veut toujours des raccourcis. Même en se disant "je ne tomberai pas dans le piège", petit à petit, on y tombe. Moi le premier. Je m'étais dit : "je ne donnerai jamais de contenu à rédiger à l'IA". Puis, plus le système performe, plus on se dit : "ah ouais, c'est pas mal ce qu'il écrit". Sauf que plus tu délègues, plus ton système doit être solide. Si tu délègues beaucoup et construis peu, tu bâtis un château de cartes que le prochain modèle fera tomber.

## 02 ·La mémoire synthétique avec Claude Cowork

Claude Cowork résout 80% du problème de mémoire. Il garde en mémoire tes fichiers de contexte, tes skills, et l'IA connaît tes règles, ta réflexion, tes stratégies.

Concrètement, comment ça fonctionne ? Tu as un fichier local qui s'alimente automatiquement à chaque projet : tes stratégies, tes cas clients, tes données, tes résultats précédents. Ton agent Claude peut interroger tout ça à tout moment. Pour faire simple, ce que tu as construit en 10 ans de pratique SEO devient mobilisable par Claude en 10 secondes.

Mais Cowork a une limite : il excelle pour les sessions conversationnelles longues sur un sujet unique. Une rédaction de contenu. Une analyse d'export GSC. Une itération sur un brief. Quand tu as besoin d'ingérer 10, 15, 20 fichiers d'un coup et de les interconnecter entre eux, il faut passer à autre chose.

C'est là que le couple Claude Code + Obsidian entre en jeu.

## 03 ·Le LLM Wiki Pattern : l'idée venue de Karpathy

### Audit SEO & GEO sous 48h.

30 min en visio. Je reviens avec une analyse de vos opportunités réelles.

[Réserver 30 min →](https://cal.com/tim-boussardon-yzrrb1/30min)

Andrej Karpathy, ex-directeur IA chez Tesla, cofondateur d'OpenAI, fondateur d'Eureka Labs. Quand il publie quelque chose, l'industrie écoute.

En 2024, il a décrit un concept qu'il appelle **le LLM Wiki Pattern**. L'idée : au lieu de faire du [[persistent-wiki-vs-rag|RAG]] classique (où l'IA cherche dans tes fichiers à chaque question et oublie tout après la conversation), tu lui fais maintenir un wiki qu'elle enrichit elle-même. Le wiki persiste. Il se densifie à chaque source ajoutée. Il devient une mémoire cumulée que tu peux interroger à tout moment.

La différence avec le RAG, c'est que l'IA ne redécouvre pas tes connaissances à chaque question. Elle raisonne sur un wiki structuré qu'elle a elle-même compilé. Karpathy a observé que sur un corpus d'environ 100 articles (soit environ 400 000 mots), cette approche surpasse le RAG en qualité de réponse.

Pour être honnête, la comparaison wiki vs RAG n'est pas aussi tranchée que certains articles le laissent croire. Une étude benchmark (LaRA, Li et al. 2025) montre que les deux approches donnent le même résultat dans 60% des cas. Le wiki gagne sur un corpus statique de taille moyenne. Au-delà, ou sur des corpus très dynamiques, le RAG reprend l'avantage. C'est complémentaire, pas un remplacement.

Le point de départ, c'est un gist publié par Karpathy : un fichier texte de quelques centaines de lignes qui décrit comment configurer une IA pour qu'elle maintienne ce type de wiki. C'est son fichier AGENTS.md de référence. Tu n'as pas besoin de le comprendre ligne par ligne. Tu le donnes à lire à Claude, et il s'en sert comme base pour construire ton propre système.

Le fichier source de Karpathy

Tu n'as pas besoin de le comprendre ligne par ligne. Tu le donnes à lire à Claude, et il s'en sert comme base pour construire ton propre système.

## 04 ·Installer le système : 3 étapes

Voilà comment j'ai mis en place mon wiki SEO avec Claude Code et Obsidian, de zéro.

Aucune ligne de code écrite. Aucun plugin obligatoire, aucune API à configurer, aucun no-code. C'est littéralement un dossier avec des fichiers markdown et une IA qui les relit.

Pour ceux qui connaissent déjà Obsidian (1,5 million d'utilisateurs actifs en 2026, 2 700 plugins dans l'écosystème) : le problème historique, c'est que tout le maillage entre les notes se fait à la main. Chronophage, pas toujours évident de faire des rapprochements sémantiques quand tu atteins des centaines de contenus. Claude vient de régler ce problème.

Côté budget : Claude Pro à 20 euros par mois, Obsidian gratuit. Comparé aux outils SaaS de gestion de connaissances SEO qui facturent entre 50 et 300 euros par mois, le rapport qualité-prix est sans comparaison. Et tes données restent en local, rien ne part sur un serveur tiers.

## 05 ·Ce que ça génère concrètement

Ce week-end, j'ai ingéré 18 fichiers bruts dans ma base de connaissances SEO accumulée depuis plus de 6 ans de pratique. Des audits, des cas clients, des résultats de campagnes, des exports GSC, des notes stratégiques.

À partir de ces 18 fichiers, Claude a généré 28 sources documentées, 32 entités et 27 concepts. Tous interconnectés entre eux (c'est la grosse différence avec un simple dossier de fichiers). Le graphe de connaissances qui se dessine dans Obsidian montre les relations entre les concepts, les cas clients, les stratégies.

Le graphe généré automatiquement à partir de 18 fichiers bruts.

Exemple de fiche générée et linkée automatiquement par Claude.

Le fonctionnement est simple. Tu dis à Claude "ingère ce rapport PDF". Il le résume dans un fichier markdown structuré. Tu lui demandes plus tard "qu'est-ce qu'on sait sur la conversion LLM ?". Il va lire ce qu'il a écrit la semaine dernière, croiser avec tes autres sources, et te répondre avec une synthèse appuyée sur ta data, pas sur du contenu internet générique.

## 06 ·La limite à connaître

Ce combo Claude Code + Obsidian ne compense pas une mauvaise base de contenu. C'est le point que personne ne mentionne dans les tutoriels enthousiastes. Si tu ingères du contenu générique scrapé, faux ou obsolète, sans le confronter à ta data propriétaire, ton wiki sera joli mais creux. Et les stratégies qui en sortent seront génériques, exactement ce qu'il faut éviter pour ranker en 2026.

Le vrai sujet, c'est que le système est reproductible par n'importe qui. Le gist de Karpathy est open source. Claude Code est accessible à tous pour 20 euros. Obsidian est gratuit. Ton avantage compétitif n'est pas dans l'outil. Il est dans ce que tu y injectes.

Or la majorité des consultants SEO n'ont pas de data propriétaire à injecter. Ils utilisent les mêmes outils SaaS, les mêmes datasets, les mêmes APIs que leurs concurrents. Si tu ingères dans ton wiki le même type de contenu que tout le monde produit, tu obtiens le même type de recommandations que tout le monde.

C'est pour ça que je dis depuis un moment : commencer par construire ta data avant d'automatiser ta production. Tes audits, tes cas clients, tes résultats mesurés sur tes propres campagnes, tes observations terrain. C'est ça qui nourrit un wiki qui performe. Le reste, c'est du bruit.

## 07 ·Claude Cowork vs Claude Code + Obsidian : faut-il choisir ?

Avec le temps, les deux ont des use cases très différents.

Claude Code + Obsidian excelle quand tu travailles sur 10 à 15 fichiers en une seule session. L'ingestion en masse, la création de liens entre des dizaines de sources, la construction d'un graphe de connaissances. C'est difficile voire impossible dans Claude Cowork, qui n'est pas fait pour traiter autant de fichiers simultanément.

Claude Cowork excelle pour les sessions conversationnelles longues sur un sujet unique. Rédaction de contenu, analyse d'un export GSC, itération sur un brief. Tu parles, il répond, tu affines, il ajuste. C'est fluide, rapide, pensé pour ce mode de travail.

Le pont entre les deux, c'est tes skills. Les fichiers de compétences que tu crées dans l'un sont utilisables dans l'autre. Ta doctrine SEO, tes workflows, tes règles de rédaction, tout ça circule entre les deux outils.

Aujourd'hui, j'utilise les deux. Ce n'est pas un remplacement, c'est un complément. Et c'est cette combinaison qui fait que le système s'améliore à chaque utilisation au lieu de repartir de zéro.

## Questions fréquentes

Claude Pro coûte 20 euros par mois. Obsidian est gratuit. Pour une utilisation intensive via l'API, compte environ 100 à 200 euros par mois en tokens. En comparaison, les suites SaaS SEO génériques facturent entre 50 et 300 euros par mois chacune, et tu n'as pas la main sur la data. Le wiki en local te coûte moins cher et garde tes données chez toi.

Claude Code lit et écrit directement dans ton système de fichiers local. Pas d'upload, pas de copier-coller, pas de plugin intermédiaire. Tu pointes Claude vers ton dossier Obsidian et il travaille dedans. ChatGPT n'a pas cet accès natif au filesystem, ce qui complique la maintenance d'un wiki local interconnecté.

Ouvre un terminal dans ton dossier Obsidian. Lance Claude Code. Il détecte automatiquement les fichiers markdown du vault. Tu peux aussi installer le plugin Claudian pour piloter Claude directement depuis la barre latérale d'Obsidian, sans quitter l'application.

Non, si tu l'utilises correctement. Google pénalise le contenu IA produit à grande échelle sans supervision humaine, c'est ce que le March 2026 Core Update a confirmé. Un wiki qui compile ta data propriétaire et sert de base à une rédaction supervisée, c'est exactement l'inverse du contenu IA scale. Tu utilises l'IA comme un outil, pas comme un rédacteur autonome.

Le graphe de connaissances Obsidian montre les relations entre tes pages. Les notes les plus connectées deviennent tes pages piliers, les notes périphériques deviennent les pages satellites. C'est de la planification de cocon sémantique assistée par l'IA, alimentée par ta propre structure de connaissances.

C'est la limite à surveiller. Karpathy a observé que le wiki surpasse le RAG jusqu'à environ 100 articles. Au-delà, le coût en tokens augmente et le risque de contexte pollué grandit. La solution : structurer ton wiki en domaines thématiques avec un fichier index par domaine, pour que Claude ne charge que la partie pertinente au lieu de tout relire à chaque session.

---

**Connecté avec :** [[cli-tools-optional]] · [[obsidian-as-ide]] · [[data-proprietaire]] · [[information-gain]] · [[persistent-wiki-vs-rag]]
