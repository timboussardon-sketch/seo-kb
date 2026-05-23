---
type: concept
title: "Mots-clés actionnels (décisionnels + transactionnels)"
aliases: [mots-cles-actionnels, mots-cles-decisionnels, requetes-actionnelles, actionnels]
tags: [doctrine-tim, mots-cles, b2b, conversion, anti-trafic, do-intent, terme-signature]
created: 2026-05-01
updated: 2026-05-01
sources: 4
confidence: high
status: stable
---

# Mots-clés actionnels

**Terme signature de Tim**. Un mot-clé actionnel est à la fois **décisionnel** ET **transactionnel** : l'utilisateur attend une action à la fin (prise de contact, demande de démo, téléchargement, devis, achat). Il ne veut pas juste s'informer.

## Définition opérationnelle

> "Un mot-clé actionnel est à la fois décisionnel et transactionnel. L'utilisateur attend une action à la fin : prise de contact, demande de démo, téléchargement d'outil, devis, achat. Il ne veut pas juste s'informer. Il veut avancer vers une décision. Ce sont les seuls mots-clés qui génèrent du CA en SEO B2B aujourd'hui." — [[sources/2026-04-17-organikk-process-seo-b2b-2026]]

## Pourquoi le terme existe

L'IA mange les requêtes informationnelles. ChatGPT, Perplexity et Google AI Mode répondent aux "qu'est-ce que X" et aux "top 10 des Y" en interface IA, sans clic vers le site. Les mots-clés qui survivent sont ceux où **l'utilisateur veut faire**, pas juste lire :
- Calculer
- Simuler
- Comparer
- Décider
- Demander
- Tester

## Test décisionnel "ChatGPT 2 questions"

Tim formalise un test binaire pour décider d'attaquer ou pas un mot-clé :

1. **Q1** : Est-ce que ChatGPT peut répondre à cette requête ?
2. **Q2** : Si oui, est-ce qu'il peut faire mieux que moi ?

Si oui aux deux → la page est morte avant d'exister. Sinon → opportunité (surtout si intent d'action).

Cohérent avec [[concepts/test-substitution-llm]] (filtre binaire pré-production "si LLM produit 80 % → ne pas créer").

## Articulation avec les autres concepts

- **Vs [[concepts/programmatique-pseo]]** : les mots-clés actionnels sont la matière première du pSEO B2B (ville × service, secteur × cas d'usage, concurrent × alternative, etc.)
- **Vs [[concepts/product-led-seo]]** : un mot-clé actionnel "calculer X" devient une page Product-Led (calculateur), pas un article. C'est le format qui valide [[concepts/fully-meets]] des Quality Raters
- **Vs [[concepts/tabou-visibilite]]** : ne plus vendre du trafic = ne plus optimiser pour des mots-clés informationnels génériques. Vendre des leads = optimiser pour des mots-clés actionnels
- **Vs [[concepts/aeo]]** : "Do" dans Know-Simple/Know/Do = exactement un mot-clé actionnel

## Sources internes Tim pour les trouver (pas Semrush/Ahrefs)

Cohérent avec [[concepts/data-proprietaire]] — les mots-clés actionnels ne sont pas dans les outils SEO classiques, ils sont dans :
- Calls clients (Gong, Modjo, Attention) — formulations exactes que tapent vos prospects
- Tickets SAV (Zendesk, Freshdesk)
- Chat support (Intercom, Crisp)
- Avis G2, Trustpilot, Capterra
- CRM (champ "raison du deal perdu")
- Commentaires LinkedIn sous vos posts et ceux des concurrents
- Communautés Slack/Discord B2B sectorielles
- GSC croisée CRM sur deals closed

## KPIs qui valident un mot-clé actionnel

- **Bannis** : position moyenne · trafic total · impressions
- **Installés** : Leads SQL par URL · Revenue par cluster sémantique · CAC par mot-clé · Deals influencés SEO en attribution multi-touch (pas du last-click)

## Validation pré-rédaction

Croiser GSC + CRM sur les deals déjà closed → remonter aux sessions organiques qui ont généré des opportunités → identifier les requêtes gagnantes → les scaler sur des pages dédiées. **Scoring combiné** : `CPC × intent × proximité offre`. Éliminer tout mot-clé qui a un bon CPC mais une distance produit trop grande.

## Pages liées

[[syntheses/process-keyword-research-5-etapes]] · [[raw/notes/skill-kw-research-workflow]] · [[sources/2026-04-17-organikk-process-seo-b2b-2026]] · [[concepts/data-proprietaire]] · [[concepts/programmatique-pseo]] · [[concepts/product-led-seo]] · [[concepts/tabou-visibilite]] · [[concepts/test-substitution-llm]] · [[concepts/aeo]] · [[concepts/fully-meets]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[sources/2026-04-30-tim-posts-linkedin-batch]] · [[sources/2026-04-30-fg-formation-pseo-cas-client]]
