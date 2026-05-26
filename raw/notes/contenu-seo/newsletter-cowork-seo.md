---
type: source
source_type: doctrine
title: "Comment créer ton système SEO avec Claude Cowork"
aliases: []
tags: []
created: 2026-04-25
updated: 2026-04-25
sources: 0
confidence: medium
status: draft
---

# Comment créer ton système SEO avec Claude Cowork

📝 Cette semaine, pas de veille. Je te montre comment j'ai construit mon propre système SEO à l'intérieur de Claude Cowork — et pourquoi ça change tout pour les consultants.

---

J'ai passé les dernières semaines à construire quelque chose que je n'avais jamais réussi à faire avec aucun outil SEO : un assistant qui connaît ma méthode, mes clients, mes règles, et qui produit du travail que je n'ai pas besoin de reprendre à zéro.

Ce n'est pas un chatbot. Ce n'est pas un prompt magique. C'est un système.

Et je vais te montrer exactement comment le construire.

## Le problème avec les outils IA actuels

Tu ouvres ChatGPT. Tu lui donnes un mot-clé. Il te sort un article. Tu le lis. Tu le jettes. Tu recommences avec un prompt plus long. Il te sort un article un peu moins mauvais. Tu le retouches pendant 2h. Au final, tu aurais été plus rapide en écrivant toi-même.

Le problème n'est pas l'IA. Le problème, c'est que tu lui donnes zéro contexte.

Sans contexte, tu exploites 30 % de l'IA. Mais surtout, tu augmentes drastiquement le risque d'hallucination. Chaque session repart de zéro. L'IA ne sait pas qui tu es, ce que tu vends, comment tu écris, ni quelles sont tes règles.

Claude Cowork résout ce problème.

## Ce que Cowork change : la mémoire de projet

Cowork te permet de créer un "Projet" — un espace permanent où tu glisses tes fichiers de contexte, tes données, tes instructions. L'IA ne repart jamais de zéro. Elle sait qui tu es, ce que tu fais, et comment tu veux travailler.

Concrètement, voici ce que j'ai dans mon projet SEO :

**3 dossiers de contexte :**

Un dossier "Bot instruction" avec mon workflow de rédaction en 8 étapes, mon ton de voix, mes anti-patterns IA (la liste Wikipedia des signes d'écriture IA que je veux éviter à tout prix), et un README qui résume le pipeline.

Un dossier "Contenu SEO" avec ma stratégie SEO 2026, mes newsletters précédentes et mes recherches sur le GEO (Titans, MIRAS, Surprise Score).

Un dossier client (dans mon cas, FG Formation) avec la base de connaissances complète : positionnement, templates de pages, cas clients, transcription d'audit blanc.

**Des skills installés :**

Chaque skill est un module autonome que Cowork déclenche automatiquement quand je lui demande quelque chose. "Trouve-moi les quick wins" → il lance le skill Quick Win. "Crée-moi un brief pour ce mot-clé" → il lance le skill Brief de contenu.

J'en ai 7 aujourd'hui : Quick Win, Cannibalisation, Brief & Structure Hn, Audit GSC, Mots-clés Décisionnels, Score GEO, Content Gaps. Chaque skill suit un raisonnement en étapes avec un format de sortie obligatoire. Pas de blabla. Des tableaux, des scores, des actions concrètes.

## Comment construire ton propre système en 3 étapes

**Étape 1 — Tes fichiers de contexte**

Crée 3 fichiers fondamentaux :

`about-me.md` — Ton contexte pro. Ton secteur, tes clients, ton positionnement. Claude sait qui tu es sans que tu te représentes à chaque session.

`my-voice.md` — Ton style d'écriture. Extrait de tes meilleurs contenus (newsletters, articles, podcasts). Claude utilise ton vocabulaire et évite les patterns IA.

`my-rules.md` — Tes règles. Ce que tu fais, ce que tu ne fais pas, tes valeurs, ta vision. Claude pose des questions avant d'agir en fonction de ce fichier.

Ces 3 fichiers, tu les rédiges une fois et tu les réutilises pour chaque nouveau projet, chaque nouveau client.

**Étape 2 — Ton workflow**

Un workflow, c'est un enchaînement de prompts où chaque étape alimente la suivante. Le mien fait 8 étapes pour un article :

Surprise Gap (ce qui manque sur le web) → Ancrage local (signaux terrain) → Données chiffrées (stats sourcées) → Inversions expertes (croyances fausses à corriger) → Architecture narrative (plan section par section) → Rédaction (prose continue, pas de bullet dans le corps) → FAQ micro-intentions → Article final compilé.

Le tout prend entre 1h30 et 2h30 par article. L'IA ne rédige pas seule. Elle exécute chaque étape avec tes données, ton ton, tes règles. Tu valides à chaque étape.

**Étape 3 — Tes skills**

Un skill, c'est un prompt structuré avec un déclencheur, un raisonnement en étapes, un format de sortie et des critères de qualité. Cowork le déclenche automatiquement quand tu poses la bonne question.

Tu n'as pas besoin de 20 skills. Commence par 3 :

Le skill Quick Win — tu uploades ton export GSC, il identifie les pages en position 4-15 avec un delta CTR négatif et te sort un tableau d'actions concrètes par URL.

Le skill Brief de contenu — tu donnes un mot-clé, il te construit la structure Hn basée sur les vecteurs sémantiques, pas sur la copie des concurrents.

Le skill Content Gap — il identifie les angles que personne ne traite. Les prix que personne n'affiche. Les questions que personne ne pose. C'est là que se trouvent les vrais gains.

## Ce qui change par rapport à ChatGPT

Le contexte persiste. Tu ne te répètes plus jamais.

Les skills se déclenchent automatiquement. Tu décris ton besoin, Cowork choisit le bon outil.

Le workflow est séquentiel. Chaque étape utilise le résultat de la précédente. Pas de copier-coller entre 8 fenêtres de chat.

Tes données restent dans ton projet. Export GSC, base de connaissances client, cas clients — tout est accessible sans ré-upload.

Et surtout : Cowork exécute des commandes shell. Il peut lire un CSV de 50 000 lignes, croiser des données, générer des tableaux. C'est un assistant qui calcule, pas juste un assistant qui rédige.

## Le vrai sujet derrière tout ça

On ne parle pas d'un outil de plus. On parle d'un changement de modèle.

Jusqu'ici, un consultant SEO vendait son temps. Analyse, rédaction, reporting — tout se mesurait en heures. Avec un système comme celui-là, tu vends ton expertise, pas ton temps. Tes skills, tes prompts, tes données propriétaires — c'est ton avantage compétitif. L'IA exécute. Toi, tu décides.

Et c'est exactement ce qui va séparer les consultants qui survivent de ceux qui se font remplacer.

Pas besoin d'être développeur. Pas besoin de savoir coder. Il faut juste savoir ce que tu sais, le formaliser, et le donner à manger à une IA qui ne l'oubliera pas.

---

**Réservé aux plus motivés.**

1/ On crée votre propre système SEO IA : [Pré-audit offert](https://organikk.co/services)

2/ L'outil qui trouve tes mots-clés pour ChatGPT, Gemini, YouTube : [Fusionn.io](https://fusionn.io/)

⇢ Tu as apprécié cette édition et le format te plaît ? Like 💙 la newsletter pour que je puisse rédiger sur des sujets similaires. MERCI !
