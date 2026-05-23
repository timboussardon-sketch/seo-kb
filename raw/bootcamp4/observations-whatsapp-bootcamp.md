---
type: bootcamp-observations
bootcamp: 4
source: WhatsApp Bootcamp SEO (5 mai 2026 → 15 mai 2026)
date: 2026-05-15
tags:
  - bootcamp4
  - observations
  - blocages
  - questions-participants
  - whatsapp
related:
  - "[[session-1-mots-cles-prep]]"
  - "[[session-2-redaction-prep]]"
  - "[[sequencage-semaine-2]]"
---

# Observations · Blocages et questions du groupe WhatsApp

Synthèse des 720 messages du chat WhatsApp Bootcamp SEO entre le 4 mai et le 15 mai 2026. Classement par fréquence de retour, avec qui a soulevé le sujet et la réponse apportée si elle a été tranchée.

À utiliser comme base pour : préparer les calls (devancer les questions), prioriser les contenus à clarifier post-bootcamp, identifier ce qui mérite un mini-tuto vidéo, repérer les signaux faibles de désengagement.

---

## 1 · Stockage des fichiers et synchro multi-device

Le sujet qui revient le plus, débattu par Lydia, Gregory, Cécile, Tony pendant plusieurs heures les 12-13 mai. Bloque concrètement le travail.

- Cowork stocke ses historiques et ses skills dans `C:\Users\...\AppData\Local\Packages` côté Windows, pas dans le dossier de travail visible.
- Impossible à synchroniser nativement via OneDrive, Drive, iCloud : c'est un dossier système.
- Comment travailler sur plusieurs machines : Gregory change de PC le week-end, Lydia s'inquiète du remplacement de son laptop.
- Confusion permanente entre "dossier de travail" et "dossier système". Cécile résume : "il le met où il veut, je ne sais plus où est la bonne version".
- Solutions tentées dans le chat : FreeFileSync planifié, demande à Claude de lister tous les skills et copier vers un autre dossier synchronisé, ou zipper et déposer sur le drive.
- Côté Mac le problème ne se pose pas : Tim a changé de Mac avant le bootcamp, le transfert s'est fait facilement.

Action possible : un mini-tuto Windows dédié au remap du dossier de travail vers un dossier synchronisable, ou la procédure officielle pour changer de machine sans tout reconfigurer.

## 2 · Installation des skills · ce qui passe ou pas dans Compétences

Multiple personnes (Stephanie, Angélique, Anne, Alexandre) se retrouvent à 5 skills sur 9 sans comprendre pourquoi.

- Différence entre "skill créé en local" dans `/skills/` du dossier de travail et "skill apparaissant dans Paramètres → Capacités → Compétences". Lydia a posté le bon chemin pour vérifier visuellement.
- Faut-il cliquer sur un bouton après création ? Alexandre : "il fallait cliquer sur un btn pour ajouter chaque skill dans les Compétences".
- Skill Creator vs simple copier-coller : Tim conseille le copier-coller, mais Skill Creator pose des questions supplémentaires qui ne sont pas dans le doc et déstabilise.
- Version courte vs annexe longue du doc : Gregory et Angélique ont créé les skills avec la version courte, puis ont découvert l'annexe et ont dû tout recommencer. Méthode validée par Angélique : dire à Claude de mettre à jour les skills existants avec l'annexe seule, sans tout refaire.

Action possible : sur le doc Setup Claude (J1), un encart visible sur "comment vérifier qu'un skill est bien dans Compétences" + un encart sur la version à utiliser (privilégier l'annexe complète dès le départ).

## 3 · Conversion des contenus existants en .md

Demande implicite de J3 (stocker tous tes contenus) qui frustre.

- "J'ai des centaines de créations sur LinkedIn et WordPress, je vais y passer la journée" (Gregory, repris par Stephanie).
- Solutions partagées : export XML WordPress + Claude pour compiler, convertisseur Zamzar Word → MD, copier-coller dans Google Docs et télécharger en MD.
- Question sous-jacente : est-ce vraiment indispensable, ou Claude peut récupérer les contenus en ligne via le plugin Chrome ? La frontière n'a pas été tranchée explicitement.

Action possible : ajouter dès J3 un workflow "Claude récupère tes contenus existants" via Chrome + plugin officiel WP, pour éviter la conversion manuelle.

## 4 · Choix du modèle et consommation de tokens

Vraie inquiétude budgétaire, revient au moins cinq fois.

- "J'ai grillé tous les tokens de session" (Stephanie en J1) → conseil : Sonnet plutôt qu'Opus.
- "Haiku 4.5 suffisant pour les skills ?" (Alexandre, deux fois) → réponse : non, Haiku c'est pour petites tâches, Opus pour les workflows complexes.
- Plusieurs participants explosent leur quota Opus en travaillant sur les docs (Angélique).
- Renvoi vers le post Substack de Ruben sur l'économie de tokens.

Action possible : ajouter sur la page Setup J1 un encart "modèle à utiliser par phase" (Sonnet pour install, Opus pour rédaction et workflows lourds, Haiku jamais sauf petites tâches one-shot).

## 5 · Connexion à WordPress

Bloque la moitié du groupe.

- Cécile bloquée parce qu'il n'y a pas "WordPress.fr".
- Lydia ".org" qui n'arrive pas à connecter Cowork malgré plusieurs essais.
- Distinction pas claire entre connecteur Chrome (simule un humain, lourd en tokens, sécurité limitée) et plugin MCP officiel (machine à machine, possibilités infinies, demande un peu de code).
- Romain a partagé son plugin custom + tuto sur romainfillatre.fr, et le plugin officiel `enable-abilities-for-mcp` qui couvre 40 habilities. Plugin chemin de référence : github.com/WordPress/mcp-adapter.
- Romain peut éventuellement faire une démo en S4.

Action possible : intégrer un mini-module S2 ou S3 sur la connexion WordPress, avec la procédure step-by-step en s'appuyant sur le tuto de Romain.

## 6 · Comment remplir et placer About / Rules / Voice

Deux questions distinctes qui ressortent.

- "On les remplit pour nous ou pour le client ?" (Gregory : son ton naturel n'est pas indiqué pour ses clients). Réponse Tim : pour le client, mais Claude peut adapter par projet si on lui donne le contexte client.
- Champs trop "personal branding" pour des stratégies B2B (Gregory : "pas simple").
- Où poser les 3 docs : Customize > Context dans Claude (suggestion de Claude à Cécile), ou dans le dossier de travail, ou les deux ? Pas tranché clairement dans le chat.
- Doit-on les supprimer du Cowork une fois importés ? (Alexandre).
- Lena : a fait remplir par Claude question par question à voix haute, terminé les 3 docs en 15 minutes. Méthode à propager.

Action possible : un encart "comment remplir vite et bien" dans le doc J2, avec la technique Lena (questions vocales) + clarifier le placement (Customize Context oui ou non).

## 7 · Persistance et contexte entre conversations

Frustration de fin de semaine 1, exprimée par Gregory et Cécile principalement.

- "Cowork a du mal à comprendre qui lui parle et ce que j'attend de lui" (Gregory après 1 semaine).
- Claude ne tient pas le contexte tout le temps, il faut lui redonner les docs (Cécile).
- Mélange des clients dans une même conversation. Solution Gregory : prompt qui force Claude à deviner le client puis confirmer par QCM avant chaque tâche.
- Règle "une seule conversation par projet" pas encore intégrée par le groupe, à pousser en S2.

Action possible : faire de la règle "une conversation par projet" un point central du call S2 (déjà prévu dans `session-2-redaction-prep.md` §1).

## 8 · Fact-checking et fiabilité

Sujet ouvert par Christophe, central pour la suite.

- "Claude a récupéré des infos archi fausses sur différentes sources" quand on lance un brief sans donner de data (Christophe, 11 mai).
- "Améliorer le skill brief avec fact-check ou chaîner un autre skill ?" → réponse Tim : phase de fact-checking arrive dans la rédaction via Perplexity.
- "Vérifier que Claude ne pompe pas de près des sources" (Cécile) → réponse Tim : ajouter une règle fondamentale "interdiction de XXX".
- Doute global de Lydia : "Est-ce que ce qu'il fait et ce qu'il me dit a du sens ?".

Action possible : déjà couvert par l'étape 5 du workflow rédaction (`session-2-redaction-prep.md` §2). Insister sur le pourquoi : pas la peine de bâtir 1500 mots de plus sur des fondations hallucinées.

## 9 · Doute sur la valeur ajoutée vs leur process actuel

Signaux faibles à ne pas ignorer.

- Gregory en début de S2 : "J'ai un peu l'impression de refaire ce que j'avais déjà, mais en moins bien".
- Lydia : "Pareil ici. J'enregistre tous ces skills et je repars faire tous mes trucs à la main".
- C'est typique de la vallée du désespoir à mi-installation. Le système commence à produire en S2-S3, c'est là que la valeur va sauter aux yeux.

Action possible : verbaliser cette phase au call S2 ("vous êtes peut-être en train de douter, c'est normal, voici quand ça bascule"). Et donner un quick win très concret en S2 que le process habituel ne donne pas (ex : article scoré, brief enrichi avec data propriétaire, etc.).

## 10 · Petits points techniques récurrents

- **Google Keyword Planner sans CB** : le mode expert n'est plus visible dans l'interface, contournement via "Aide → mode expert" trouvé par Tony pendant la visio S1. Google fait juste une empreinte CB de 10 € sans prélèvement si pas de campagne.
- **Sandbox / Bash workspace bloqué** : Lydia depuis deux jours, Anthropic pas en panne officielle (status.claude.com). Désinstaller / réinstaller suggéré par Tony.
- **Transcription vidéo YouTube quand pas de voix** (Christophe) → YouTube natif et TurboScribe inutiles, NotebookLM fait un résumé visuel correct.
- **Création de skill sur ton de voix** : Tim a expliqué que LinkedIn et rédaction arrivent après, à personnaliser sur chaque participant.

---

## Côté positif · ce qui a marché

À ne pas perdre de vue, vu la longueur des blocages listés ci-dessus.

- **Entraide forte** : Stephanie, Romain, Tony, Lydia répondent en moins de 5 min aux questions des autres. Le canal joue son rôle.
- **Romain** a partagé un plugin WordPress custom + tuto complet, va potentiellement faire une démo S4.
- **Anthony** propose son système de prospection IA pour S4.
- **Tony** partage handy.computer (Whisper local gratuit), trouve la solution mode expert KW Planner en live.
- **Angélique** trouve la méthode pour upgrader les skills déjà créés via l'annexe sans tout recommencer. Méthode propagée à Gregory, Christelle, qui sont sauvés.
- **Lena** trouve la technique des questions vocales pour remplir les 3 docs en 15 min.
- **Christophe** valide le skill `seo-brief-contenu` sur un cas réel, satisfait du résultat.
- **Gregory** a bossé toute une journée avec les skills sur une optimisation homepage : "ça marche bien".

Le groupe est productif, curieux, prêt à entraider. Les blocages listés sont des frictions techniques sur l'install, pas des doutes sur la pertinence du système.

---

## Profils identifiés

Pour mémoire et pour calibrer les explications à venir.

- **Devs confirmés** : Stephanie (dev WP 15 ans), Julien (dev WP freelance 11 ans), Romain (gen leads + plugin builder), Christophe (Odopass, 30 ans).
- **Marketers IA-friendly** : Anthony, Caroline (team lead SEO/GEO), Franck (15 ans SEO), Christelle, Marussia, Lena.
- **Profils plus novices technique** : Cécile (éditorial reconverti), Gregory (com généraliste reconverti), Angélique, Alexandre, Jean Jacques, Anne, Lydia (SEO mais autodidacte sans agence).
- **Profils geo distants** : Lydia au Québec (6h de décalage, toujours en retard sur les threads en live), Greg à Lisbonne, Christophe à Madrid.

À garder en tête pour les explications techniques : 30 à 40% du groupe découvre le local, AppData, MCP, Markdown. Les autres aident, mais ils ne devraient pas porter cette charge seuls.
