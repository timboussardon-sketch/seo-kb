---
type: revue-presse
title: Claude Code + Obsidian — le process sans complexité
aliases: [newsletter-claude-code-obsidian, algorithme-claude-terminal-obsidian]
tags: [newsletter, algorithme, claude-code, obsidian, kb, workflow, pattern-karpathy]
created: 2026-04-13
updated: 2026-04-13
sources: 3
confidence: high
status: stable
---

# Claude Code + Obsidian — le process sans complexité

*Édition Algorithme — 2026-04-13*

---

## Hook

Ce matin j'ai ingéré 18 fichiers bruts dans ma base de connaissances SEO. 2 heures. 28 sources documentées, 32 entités, 27 concepts. Tout interconnecté, tout cité, tout maintenu. Aucune ligne de code écrite. Un terminal et un dossier Obsidian.

Voici le setup, sans le jargon.

## Passage ancré

Claude Code c'est Claude, mais dans ton terminal. Au lieu de taper dans un chat web, tu tapes dans une fenêtre où l'IA voit tes fichiers locaux. Elle peut les lire, les modifier, en créer, les croiser. Obsidian c'est ton explorateur : chaque fichier est une page markdown, les `[[liens]]` forment un graphe naviguable, rien n'est verrouillé dans un SaaS. Le couple Claude Code + Obsidian transforme un dossier local en KB vivante. Les deux briques sont gratuites (Obsidian) ou à 20€/mois (Claude). Aucun plugin obligatoire, aucune API à configurer, aucun no-code. C'est littéralement un dossier avec des fichiers .md et une IA qui les relit.

## Pourquoi ça change quelque chose

Précision avant d'aller plus loin : Claude Code (v2.1.59+) et ChatGPT Memory stockent bien des préférences entre sessions. Je ne dis pas que l'IA oublie tout — je dis qu'elle ne **maintient pas** un artefact que tu possèdes. Nuance qui change tout.

Claude Code Memory charge 200 lignes de `MEMORY.md` au start. ChatGPT Memory stocke des faits courts dans un format propriétaire non exportable. Les deux servent l'IA : ils l'aident à te répondre avec plus de contexte. Ni l'un ni l'autre ne construit un wiki de 200 pages cross-référencées que tu peux lire, naviguer, versionner en git, consulter sans IA.

Claude Code + Obsidian va plus loin : tu demandes *"ingère ce rapport PDF"*, Claude le résume dans `sources/2026-04-13-rapport.md`, met à jour 10-15 pages qui le citent, ajoute l'entrée dans `log.md`. Le résultat est **tes fichiers**. Markdown brut. Ouvrables dans n'importe quel éditeur. Partageables sans Claude. L'IA n'est pas le propriétaire — c'est le mainteneur.

Andrej Karpathy a publié en 2025 un gist sur ce pattern — il l'appelle *LLM Wiki*. Son analogie : Obsidian est l'IDE, l'IA est le programmeur, le wiki est la codebase. Le point clé : **la codebase existe indépendamment du programmeur**. Si tu changes d'IA demain (Claude → Gemini → autre chose), ton wiki reste. Si tu changes d'ordinateur, `git clone` et tout est là. Memory ne t'offre pas ça.

Un humain abandonne un wiki au bout de 3 mois parce que la maintenance scale plus vite que la valeur. L'IA ne s'ennuie pas et touche 15 fichiers en un passage. Combiné avec un artefact que tu possèdes, ça devient un second cerveau exportable.


## Le setup en vrai

Tu installes Claude Code (`npm install -g @anthropic-ai/claude-code`). Tu crées un dossier. Tu ouvres Obsidian dessus. Tu lances `claude` dans ce dossier. Fin du setup.

La structure que j'utilise — copiée du pattern Karpathy adapté au SEO — tient en 3 couches :

**`raw/`** reçoit les sources brutes. Articles scrapés, exports GSC, transcripts de calls, papers. L'IA lit, ne modifie jamais.

**`wiki/`** est son terrain d'écriture. Pages par source, par entité (un algo, un outil, un prospect), par concept (AEO, Grounding Score, Surprise Gap). Elles se citent entre elles via des wikilinks.

**`AGENTS.md`** est le fichier de config. Tu lui dis comment tu veux qu'elle bosse : nommage, frontmatter YAML, règles de citation, ton de voix. Tu le fais évoluer au fil des sessions. C'est le contrat.

Trois opérations. **Ingest** — tu lui dis "ingère raw/articles/foo.md" et elle touche 10-15 pages du wiki (création de la source, mise à jour des entités mentionnées, update de l'index, append du log). **Query** — tu lui poses une question, elle drille les 5-8 pages pertinentes et répond avec citations `[[...]]`. Si la réponse a de la valeur, tu la files en page permanente. **Lint** — tu lui demandes de vérifier contradictions, claims sans source, pages orphelines. Elle te sort une todo.

## Ce que ça produit concrètement

Exemple de ce matin. J'avais 14 fichiers raw en attente d'ingest. Papers Titans/MIRAS, QRG 2026, étude SEMrush, fiche produit bootcamp, analyse de 9 calls prospects, scrapes Organikk, 7 transcripts calls. Rien de tout ça n'était dans le wiki.

2 heures plus tard, chaque paper a sa page avec résumé structuré et limites explicites. Les 9 prospects ont chacun leur entité, citables dans n'importe quel futur post. Le concept *Surprise Gap* — que j'ai formalisé il y a trois jours via une note doctrinale — est maintenant adossé au paper Titans primaire, donc sa confidence passe de "medium" à "high". Le concept *Passage Ranking* — qui était un stub abandonné — est fondé sur MIRAS. Un concept nouveau (*tabou visibilité*) capture ma doctrine de vente et pointe vers les transcripts Dev web et Cécile où le pattern est verbatim.

Aucun copier-coller depuis Claude web vers Obsidian. L'IA a écrit directement dans mes fichiers locaux. J'ai relu, validé, demandé quelques reprises.

## Les limites qu'on te vend rarement

Claude Code n'est pas gratuit. Le plan à 20€/mois de Claude couvre les usages raisonnables — une session d'ingest soutenue peut te pousser vers le plan à 90€. Prévois le budget avant de t'emballer.

Obsidian ne remplace pas un CRM, ni un outil d'audit SEO, ni Fusion. C'est une couche de réflexion et d'archive. Tu ne produis pas de rapports clients finalisés là-dedans — tu produis la matière qui les nourrit.

La KB ne compense pas une mauvaise doctrine. Si tu ingères du contenu générique scrapé sans le confronter à ta data propriétaire, ton wiki sera joli mais creux. La valeur vient de ce que tu mets dedans : calls clients, exports GSC, données terrain, intuitions datées. Pas de la structure.

Le pattern marche pour un usage individuel ou à 2-3. Pour 10+ rédacteurs avec gouvernance éditoriale partagée, tu sors du cadre et tu vas avoir besoin d'autre chose (Notion, Confluence, un vrai CMS). Karpathy le dit explicitement dans son gist.

Et tu as un coût caché : la réflexion. Une KB n'économise du temps qu'à partir de 50-100 sources. Avant, c'est un investissement. Les 10 premières sessions d'ingest prennent plus de temps qu'une note classique dans Bear ou Notion.

## Pourquoi je documente ça maintenant

Sur 9 calls prospects bootcamp ce mois-ci, **0 sur 9** utilise Claude Code correctement. La majorité utilise Claude web en conversation. Trois utilisent les Projets Claude, qui cloisonnent la mémoire par client et ne relient rien. Personne n'a un dossier local avec une config explicite.

C'est l'écart qui m'intéresse. Pas l'écart technologique — Claude Code n'est pas compliqué, cette newsletter vient de te le montrer. L'écart c'est que personne ne prend le temps de se poser, d'écrire le AGENTS.md, de construire le wiki initial. Parce qu'il n'y a pas de ROI immédiat. Parce que le premier mois tu investis sans gagner visiblement de temps. Parce que le vrai gain arrive vers la source 30, quand le wiki commence à répondre à tes queries mieux que ta mémoire.

J'ai itéré ce process pendant 6 ans. Le workflow que tu lis là est à 80% stable. Les 20% évoluent avec les outils — hier c'était Cursor, aujourd'hui Claude Code, demain autre chose. Le 80% c'est la discipline : raw immuable, wiki possédé, config explicite, log append-only.

C'est exactement ce qu'on travaille dans le Bootcamp #4 — démarrage première semaine de mai, 8 places, 590€ TTC pour 2 mois. Si cette newsletter te parle, tu sais où me trouver. Si tu préfères continuer avec Claude web, c'est ton droit. Mais ton wiki, il ne se construira pas tout seul.

---

**Canaux** — Newsletter Algorithme · [organikk.co](https://organikk.co) · [[entities/bootcamp-seo-ia]]

## Pages liées

**Sources** : [[sources/2026-04-11-karpathy-llm-wiki]] · [[sources/2026-04-13-offre-bootcamp-seo-ia]] · [[sources/2026-04-13-analyse-calls-prospects-bootcamp]]

**Concepts** : [[concepts/persistent-wiki-vs-rag]] · [[concepts/ingest-workflow]] · [[concepts/query-synthesis]] · [[concepts/obsidian-as-ide]] · [[concepts/tabou-visibilite]] · [[concepts/data-proprietaire]]

**Entities** : [[entities/karpathy]] · [[entities/obsidian]] · [[entities/bootcamp-seo-ia]] · [[entities/organikk-co]]
