---
type: source
source_type: client-note
title: "Alexia — résumé du call 4 (retour d'usage post-installation : Cowork, Notion, migration Shopify, 2026-08-03)"
aliases: [alexia-call-4-resume, alexia-call-retour-usage-cowork-notion]
client: Alexia (agence Alexandrie / alexandrie.io)
tags: [alexia, client, accompagnement-1-1, resume-call, cowork, notion, mcp, terminal, migration, shopify, maillage-interne, blocages]
created: 2026-08-03
updated: 2026-08-03
sources: 1
confidence: high
status: stable
---

# Call 4 — Retour d'usage post-installation (2026-08-03)

> Quatrième call de travail, après le [[alexia-call-cadrage|cadrage du 2026-06-10]], le [[alexia-call-1-resume|call 1 du 2026-06-24]] et le [[alexia-call-3-resume|call 3 du 2026-07-17]]. Participants : Alexia Vigo, Tim Boussardon.

## En résumé

Le call sert de bilan d'usage depuis le passage au terminal + Obsidian décidé au call 3 : Alexia n'a en réalité pas basculé, elle est restée sur Cowork (chat), pour des raisons de confiance et de confort d'usage plutôt que de blocage technique. Le call remonte les frictions concrètes rencontrées avec ce choix (connecteur Notion, déclenchement des skills, confusion de conversation, peur de connecter le CMS), reconnecte Notion en MCP en live, et pose deux prochaines étapes : comparer son process agence au pack de skills livré, et construire un dashboard client modèle.

## Problèmes rencontrés avec l'installation du système

- **Connecteur Notion cassé côté Cowork.** La reconnexion via l'icône de rafraîchissement dans les paramètres ne faisait rien (retour à l'écran « compléter les étapes de connexion » en boucle). Contournement trouvé en live : quitter complètement l'application Claude puis rouvrir le lien de connexion depuis le navigateur. Cette manipulation a fini par fonctionner, mais rien dans l'interface ne l'indiquait comme solution.
- **Skills non déclenchés dans Cowork.** Une demande d'idées de contenu (mauvais fil, client donné par erreur) est ressortie générique, sans qu'aucun skill local n'ait visiblement été mobilisé. Confirmation du diagnostic déjà posé au call 3 : dans Cowork, les skills ne se déclenchent pas systématiquement, il faut les nommer explicitement (« basé sur nos skills », « basé sur ce que tu as en local ») à chaque demande, sinon Claude part sur ses propres connaissances.
- **Confusion de conversation / de client.** Alexia a donné le mauvais fichier dans le mauvais fil de discussion (un fil « maillage interne » a reçu une demande liée à un autre client). Le système actuel d'épinglage (une épingle par sous-sujet plutôt qu'une par client) ne suffit pas à éviter l'erreur ; la question reste ouverte au sortir du call.
- **Aucune traçabilité de l'usage des skills dans Cowork.** Contrairement au terminal, impossible pour elle de vérifier après coup si un skill a été utilisé pour produire une réponse donnée — seule option : redemander explicitement à Claude s'il a utilisé tel skill.
- **Connexion CMS (Shopify) toujours pas faite.** Reste bloquée depuis le call 3 (déjà noté en action). Cette fois le blocage est nommé explicitement : ce n'est pas un obstacle technique identifié, c'est de l'appréhension (« j'ai un peu peur de le faire pour l'instant », « je m'étais même pas posé la question »).
- **Contournement manuel choisi pour la migration en cours**, au lieu du skill de maillage interne branché sur Shopify : pour le plan de redirection, elle passe par un export Matrixify fourni par une autre agence (gestion technique Shopify) et un rapprochement RECHERCHEV/VLOOKUP fait à la main entre l'ancien et le nouveau plan d'URL. Volume estimé en centaines de pages avec plusieurs liens chacune, donc plusieurs milliers de rapprochements à la main. Risque additionnel identifié pendant l'échange : certaines redirections pointent vers une page mère ou l'accueil plutôt que vers la page exacte, ce qui peut rendre l'ancre choisie inexacte — elle envisageait de recontrôler ça aussi à la main plutôt que de reconfier l'ensemble au skill.
- **Terminal toujours pas adopté**, malgré la décision prise au call 3. Raisons données telles quelles : pas de historique visible une fois la fenêtre fermée, difficulté à faire confiance sans voir ce qui se passe, interface jugée peu engageante (« c'est pas très sexy »). Elle reste sur Cowork, identifié depuis le call 3 comme l'environnement où le contexte et les skills sont le moins bien mobilisés.
- **Process agence toujours pas transmis.** Blocage déjà remonté au call 3 (audit, mots-clés, rédaction demandés par WhatsApp) : toujours pas reçu au 2026-08-03, ce qui empêche la personnalisation des workflows et la comparaison avec le pack livré.

## Ce qui a été résolu ou avancé pendant le call

- Notion reconnecté en MCP à Cowork (voir contournement ci-dessus), et testé en direct : Claude confirme pouvoir appliquer la règle raw/wiki (liens entre notes, source du document d'origine citée) à chaque nouveau document Notion, à l'identique de ce qui avait été posé sur Obsidian au call 3.
- Clarification du niveau de raisonnement à utiliser : Opus 4.8 effort élevé est inutile pour des tâches de conversation simple (ajouter un fichier, connecter un outil) ; à réserver aux tâches profondes (audit, rédaction). Alerte donnée sur la consommation de forfait : les tâches automatiques/programmées dans Cowork consomment beaucoup plus de tokens qu'une demande ponctuelle, à ne pas multiplier sans discernement sur un forfait à 20 $.
- Partage de responsabilité reposé, dans la continuité du call 3 : confier à l'IA les tâches pénibles et à faible différenciation (rapports/dashboards client, audits de maillage interne, rapprochement de redirections, corrections techniques directes sur le CMS), garder pour elle les tâches où elle fait la différence (idées de contenu, jugement éditorial, liens internes non strictement sémantiques mais utiles à l'utilisateur, contrôle final d'une migration).

## Prochaines étapes

**Alexia**
- Comparer son process réel (audit, mots-clés/idées de contenu, rédaction) au pack de skills livré : note vocale décrivant étape par étape sa méthode, à donner à Claude avec le skill correspondant en local pour lister les écarts, avant de décider ce qui est ajouté/retiré. Toute modification passe par le fichier du skill existant nommé explicitement, jamais par une copie parallèle.
- Construire un dashboard client modèle (suivi des tâches à partir des transcripts de call, statut fait/en cours/en retard, suivi de position connecté à Search Console), pensé pour être dupliqué ensuite sur tous ses comptes.
- Regarder la connexion Shopify (API) pour la migration — action reportée depuis le call 3, à traiter en testant d'abord sur une seule URL avant d'élargir.
- Envoyer les process agence (audit, mots-clés, rédaction) demandés depuis le call 3, toujours en attente.

**Tim**
- Prochain call : lundi 8h heure d'Alexia (Bangkok), à recaler par WhatsApp — Alexia indisponible du 5 au 14/08.
