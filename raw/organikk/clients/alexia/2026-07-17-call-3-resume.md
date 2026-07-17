---
type: source
source_type: client-note
title: "Alexia — résumé du call 3 (passage au terminal + Obsidian, 2026-07-17)"
aliases: [alexia-call-3-resume, alexia-call-terminal-obsidian]
client: Alexia (agence Alexandrie / alexandrie.io)
tags: [alexia, client, accompagnement-1-1, resume-call, terminal, obsidian, claude-code, workflow, mots-cles, migration, shopify]
created: 2026-07-17
updated: 2026-07-17
sources: 1
confidence: high
status: stable
---

# Call 3 — Passage au terminal et branchement Obsidian (2026-07-17)

> Troisième call de travail, après le [[alexia-call-cadrage|cadrage du 2026-06-10]] et le [[alexia-call-1-resume|call 1 du 2026-06-24]]. Participants : Alexia Vigo, Tim Boussardon. Transcript brut : `call alexia 3.md`.

## En résumé

Alexia travaillait encore dans le chat Claude, où les connecteurs écrasent les skills et où les réponses restent génériques. Le call bascule son installation sur le terminal branché à un coffre Obsidian unique (« base SEO »), et pose la règle qui structure la suite : tout rendu devient un fichier dans le coffre, sinon le système n'apprend rien. Les trois premières semaines du programme sont bouclées, on passe à la personnalisation des workflows. Blocage à lever : Tim attend toujours les process agence (audit, mots-clés, rédaction) demandés par WhatsApp.

## Point de situation

- Alexia est débordée et termine rarement ses journées à jour. C'est la douleur que le système doit traiter.
- Elle sent que Claude ressort des éléments de son ton de voix et de ses skills, mais pas assez souvent. Cause identifiée : elle passe encore majoritairement par le chat plutôt que par Cowork ou le terminal.
- Le chat mélange les contextes, donc il rend des réponses génériques. Cowork relie les projets entre eux, le terminal travaille directement dans le coffre.

## Deux cas concrets passés en revue

### Métadescriptions Shopify réécrites à la main

Alexia devait retirer la mention de livraison offerte d'une vingtaine de fiches produits. Le partage du Google Sheet a échoué deux fois, elle est passée par un CSV, et l'opération a pris environ une heure.

Verdict de Tim : sur ce type de tâche, la valeur de l'IA disparaît si le CMS n'est pas connecté. Il faut passer par le terminal et brancher l'API Shopify, pour dire « sur toutes les fiches produits, retire telle mention » et laisser l'agent écrire. Deuxième point : ces tâches d'exécution ne nourrissent pas le système, donc elles ne méritent pas ce temps-là. Sans connexion CMS, les tests de CTR sur les titres et métadescriptions restent hors de portée.

### Sous-collections prêt-à-porter (automne-hiver 26)

Alexia a fait produire par Claude un tableau de mots-clés pour les sous-collections de la prochaine saison, à partir des lookbooks et de la liste des références. Résultat correct mais générique.

En regardant la conversation, le diagnostic est net : aucun skill n'a été déclenché, le connecteur Semrush a pris toute la place. Ce qui sort de Semrush, ce sont des mots-clés que le client trouve lui-même. Trois corrections :

- Relancer la recherche en nommant explicitement le workflow mots-clés du coffre.
- Découper par catégorie. Pull, gilet et cardigan tiennent ensemble ; robe et pull, non. Le lot complet est trop large pour une seule passe.
- Nourrir avec la donnée réelle : fiches produits scrapées, descriptifs de catégories et lookbooks convertis en Markdown, échanges client.

Le partage de responsabilité qui en découle : Claude agrège la donnée fastidieuse, Alexia va chercher les mots-clés qu'il ne peut pas trouver. Ceux qui demandent une connexion (le coloris « forêt » qui est un pantalon vert, la jupe qui ouvre sur le kilt) restent son travail, et c'est là qu'elle se différencie sur les résultats de recherche.

## Méthode posée

- **Une conversation par client**, épinglée, avec le projet Claude SEO et le dossier du client rattachés. Ce qui compte, c'est l'historique, pas le projet.
- **Les projets se découpent par tâche, pas par client** : rédaction, audit, veille. Un projet ne vaut le coup que s'il y a du contenu de référence à donner. Pour la rédaction, un seul projet suffit : les clients partagent presque tous le même ton de voix, celui qui compte est le ton anti-IA.
- **Tout rendu devient un fichier** dans le coffre, jamais un simple lien Drive. Un audit stocké sur le Drive ne sera pas relu lors de l'audit suivant ; un audit en local sert de base au suivant.
- **Un dossier par client**, avec des noms de fichiers uniques. Deux dossiers portant le même nom et l'agent se trompe de cible.
- **Les skills se déclenchent sur des mots déclencheurs**, et pas systématiquement dans Cowork. Il faut connaître les principaux pour repérer un rendu qui ne colle pas, et redemander explicitement le skill.
- **Les skills sont vivants** : quand une section manque ou ne correspond pas à sa méthode, Alexia demande la modification du skill.
- **Un coffre par client à terme** : 10 000 fiches produits dans le coffre système SEO le dégradent. Le système SEO garde un résumé par client, chaque client a son coffre.

## Migration client — plan de redirection

C'est le prochain chantier réel d'Alexia, avec un plan de redirection à produire dans l'urgence.

- Skill audit d'indexation disponible : statut 301 ou 404 par page. Le lancer avant redirection, puis après, pour comparer.
- Limiter à environ 100 URL prioritaires. Le scraping de 500 URL coûte cher en tokens.
- Pour le rapprochement ancienne ↔ nouvelle URL : donner la liste des nouvelles URL et le sitemap, demander un tableau de correspondance sémantique. Ça fonctionne, mais la vérification humaine reste obligatoire.
- Une fois Shopify connecté, l'agent réécrit les URL lui-même. Étape de contrôle imposée : valider le tableau dans un Google Sheet (par Alexia, éventuellement par le client) avant d'autoriser l'écriture sur Shopify. Le système d'Alexia n'est pas encore assez entraîné pour écrire sans relecture.

## Installation terminée pendant le call

- Coffre Obsidian ouvert sur le dossier Claude complet, coffre en double supprimé pour éviter les confusions de chemin.
- Coffre renommé **base SEO** : le mot « vault » entre en collision avec le vocabulaire Obsidian, et le nom d'Organikk n'a rien à faire dans son système si elle veut le revendre plus tard.
- Terminal connecté au coffre, avec la règle raw / wiki intégrée : tout nouveau document créé respecte la structure et crée des liens entre fichiers.
- Notion : la connexion via l'app Claude ne vaut pas pour le terminal. À rebrancher en local via API, indépendamment.
- Permissions : Tim transmet la commande d'accès complet, à passer en fin de conversation. Avertissement donné, une commande d'achat a déjà été passée à sa place sur un site où sa carte était enregistrée.

## Ce que le terminal change

- Les conversations ne persistent pas. En début de session, demander un résumé du client ; créer une tâche qui écrit un résumé en fin de conversation.
- Plusieurs conversations en parallèle sur un même client : dix recherches de mots-clés lancées par catégorie pendant qu'elle travaille sur autre chose.
- Automatisations visées : audits d'indexation hebdomadaires déposés dans le dossier client, lecture Search Console, notes de préparation d'appel, scraping des derniers articles de blog à la création d'un dossier client.
- Le terminal reste un espace de commande. On lance, on ne lit pas, on ouvre le document produit à la fin.

## Prochaines étapes

**Tim**
- Envoyer la note du call (à déposer en Markdown dans le terminal, pas en lien Drive).
- Transmettre la commande de permissions complètes.
- Personnaliser les workflows audit, mots-clés et rédaction dès réception des process agence. Le workflow suivi passe en dernier (Alexia ne fait pas les rapports, ils restent chez l'agence).

**Alexia**
- Envoyer ses process agence sur l'audit, les mots-clés et la rédaction, plus des exemples d'audits et de rapports mensuels récents. Demandé par WhatsApp, toujours pas reçu, et ça bloque la personnalisation des workflows.
- Travailler un client dans le terminal, garder les autres sur Cowork le temps de prendre la main.
- Créer un dossier par client, et faire un test complet : scraper les 10 derniers articles de blog d'un client vers le coffre, lancer un audit, vérifier que les fichiers atterrissent au bon endroit.
- Relancer la recherche de mots-clés du prêt-à-porter par catégorie, en nommant le workflow du coffre.
- Regarder la connexion Shopify (API) pour la migration.
