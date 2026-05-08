---
slug: newsletter-agent-ia-verifier-indexation-seo
title: "L'audit d'indexation qui se fait sans vous, chaque mois"
author: "Timothée Boussardon"
date_added: 2026-05-02
source_local: "/Users/timothee/Documents/seo-kb/raw/articles/newsletter-agent-ia-verifier-indexation-seo.md"
type: newsletter
audience: cmo
topic: agents-ia-seo
status: draft-v2-cmo
---

# L'audit d'indexation qui se fait sans vous, chaque mois

> **Pour qui** : CMO, head of growth, dirigeants qui paient une équipe ou une agence pour publier du contenu et qui veulent savoir ce que Google en fait — sans devoir y passer eux-mêmes.

Vendredi dernier, mon équipe a publié 30 pages d'un coup sur organikk.co. Bonne nouvelle. Mauvaise nouvelle : je ne saurai pas avant deux semaines combien d'entre elles auront vraiment été récupérées par Google. Et si je veux le savoir, je dois ouvrir Google Search Console, copier-coller 30 URLs une par une, attendre l'inspecteur, prendre des notes. Compter une bonne heure de boulot. Tous les mois.

Honnêtement ? On ne le fait jamais. Vous publiez, vous publiez, vous publiez, et vous ne savez plus ce qui rentre vraiment dans Google. Vous payez votre prestataire SEO 1 500 € / mois pour de la stratégie, et vous n'avez pas la base : la liste des pages qui marchent vs celles qui dorment.

J'ai mis fin à ça avec un robot logiciel — ce qu'on appelle un "agent IA" — qui se réveille tout seul à la date que je lui donne, vérifie tout, et m'envoie un rapport sur GitHub. Mise en place : 15 minutes une fois. Coût récurrent : zéro.

Voici comment ça marche, et comment vous pouvez en avoir un pour votre marque.

> **📸 Screenshot 1 à insérer ici** :
> Capture du dashboard `claude.ai/code/routines` montrant l'agent `wiki-indexation-check` planifié, avec la date "16 mai 2026" et le statut "Enabled".
> *Pourquoi* : preuve immédiate que l'agent existe et qu'il est planifié.

---

## Pourquoi ça compte (le calcul économique)

Faisons le calcul à la main pour 30 pages publiées par mois :

| Méthode | Temps | Coût mensuel | Précision |
|---|---|---|---|
| Vous le faites vous-même | 1h | Votre temps | Variable (vous oubliez) |
| Vous demandez à un junior à 35 €/h | 1h × 35 € | **35 € / mois × 12 = 420 €/an** | Bonne |
| Vous demandez à votre agence SEO | Inclus dans le forfait | Mais pas fait, ou fait mal | Aléatoire |
| Un agent IA dédié | 15 min de setup, 1 fois | **0 €/mois après setup** | Excellente |

L'écart économique est ridicule. Mais le vrai gain n'est pas là. Le vrai gain : vous arrêtez de vous fier au "ça doit être bon, on a publié". Vous savez. Et savoir, c'est ce qui sépare un CMO qui décide d'un CMO qui devine.

---

## PARTIE 1 — Ce que fait l'agent (vu de votre fauteuil)

L'agent est un programme qui tourne tout seul, sur des serveurs distants. Il ne touche pas à votre ordinateur, il ne touche pas à votre site. Il regarde, il note, il vous envoie un rapport.

Ce qu'il vérifie pour vous, en six points :

### 1. Toutes les pages répondent bien

Il essaie d'ouvrir chacune des 30 pages, comme le ferait un visiteur. Si une page renvoie une erreur 404 ou un message du serveur, il le note. C'est le check qui attrape les pages cassées par un déploiement mal contrôlé — typiquement quand votre dev pousse du code et qu'une page disparaît sans que personne ne s'en rende compte.

### 2. Toutes les pages sont déclarées à Google

Google ne devine pas vos URLs : vous les lui annoncez via un fichier appelé "sitemap". L'agent ouvre votre sitemap et vérifie que vos 30 nouvelles pages y sont bien listées. Si une page est absente, Google ne la trouvera jamais — c'est mécanique.

### 3. Google les a-t-il vraiment prises en compte ?

C'est la question centrale. L'agent demande à Google, page par page : "tu connais cette URL ?". Et il note la réponse.

> **📸 Screenshot 2 à insérer ici** :
> Capture du fichier `reports/wiki-indexation-2026-05-16.md` ouvert dans VSCode ou Obsidian, montrant le tableau "Détail par fiche" avec les colonnes URL, HTTP, Sitemap, Indexation Google.
> *Pourquoi* : montrer le livrable concret au CMO.

Limite à connaître : sans accès officiel à Google Search Console (qu'on peut brancher dans un second temps, voir partie 2), l'agent fait une estimation. Il a raison environ 4 fois sur 10. Pas 100 %. Donc on traite le résultat comme un indicateur, pas comme une vérité absolue. C'est pour ça que dans le rapport, l'agent distingue clairement "non indexée" et "non testable" — il ne ment pas par omission.

### 4. Les pages sont-elles bien reliées entre elles ?

Une page seule, sans aucun lien depuis le reste de votre site, c'est ce qu'on appelle une "page orpheline". Google la voit moins bien, vos visiteurs ne la trouvent jamais. L'agent vérifie que vos 30 nouvelles pages sont bien reliées : que d'autres pages pointent vers elles, et qu'elles pointent vers d'autres pages. Si une page est isolée, c'est signalé.

### 5. ChatGPT et Perplexity vous citent-ils ?

C'est le check le plus moderne, le plus important pour 2026. Quand un utilisateur pose une question à ChatGPT ou Perplexity sur votre sujet, est-ce que ces moteurs IA citent votre marque comme source ? L'agent teste cinq questions stratégiques et note si votre nom de domaine apparaît dans les réponses.

C'est le nouveau référencement. Ne pas le mesurer en 2026, c'est piloter une voiture en regardant uniquement le rétroviseur.

### 6. Tout est consigné dans un rapport propre

À la fin, l'agent compile tout dans un document texte clair, qu'il dépose sur GitHub (la plateforme où vit le code de votre site). Vous recevez une notification par email. Vous ouvrez, vous lisez, vous décidez.

> **📸 Screenshot 3 à insérer ici** :
> Capture de l'email GitHub "Pull request opened — Report — Indexation wiki au J+14".
> *Pourquoi* : illustrer que le CMO ne se déplace pas, le rapport vient à lui.

> **📸 Screenshot 4 à insérer ici** :
> Capture de la PR sur github.com avec la section "Synthèse" du rapport markdown rendue dans l'interface GitHub : "HTTP 200 : 30/30, Sitemap : 30/30, Indexation Google : 18/30 estimés..."
> *Pourquoi* : montrer le livrable final, format de communication clair.

Ce qu'il **ne fait pas** : aucune action sur votre site, aucune soumission forcée à Google, aucune modification de quoi que ce soit. Il observe et rapporte. C'est volontaire — un agent qui peut "réparer" tout seul est un agent qui peut tout casser. On garde le contrôle.

---

## PARTIE 2 — Comment vous en avez un pour votre marque (4 étapes)

Vous n'avez pas besoin de coder. Vous avez besoin de quelqu'un dans votre équipe (ou un freelance) qui sait :

- ouvrir un terminal
- avoir un compte GitHub
- lire des consignes en français

Si votre prestataire SEO refuse de faire ça, c'est un signal sur votre prestataire SEO.

### Étape 1 — Lister les pages à surveiller dans un fichier

Vous (ou votre tech) crée un petit fichier dans le code de votre site qui liste les URLs à surveiller. Pour Organikk, c'est un fichier texte qui contient les 30 URLs des fiches du wiki.

Si votre site a été fait par une agence et que vous n'avez pas accès au code, demandez-leur de créer ce fichier. C'est 5 minutes pour eux.

> **📸 Screenshot 5 à insérer ici** :
> Capture du fichier `src/data/wiki.ts` ouvert dans VSCode, montrant la structure des 30 entrées (slug, term, category).
> *Pourquoi* : démystifier le "code" — c'est juste une liste structurée.

### Étape 2 — Décrire à l'agent ce qu'il doit faire

L'agent a besoin d'instructions précises, en français. Vous (ou votre tech) écrivez un document qui dit : "Va lire ce fichier, fais ces vérifications, écris-moi le rapport sous cette forme, ne touche à rien d'autre."

C'est cette étape qui fait la différence entre un agent qui marche et un agent qui plante. Un bon CMO investit ici. Pas dans la technique — dans la clarté des consignes.

> **📸 Screenshot 6 à insérer ici** :
> Capture du fichier de prompt agent ouvert, montrant les sections "Mission", "Étapes", "Contraintes" en markdown.
> *Pourquoi* : montrer que les "instructions à l'IA" ressemblent à une fiche de poste, pas à du code.

### Étape 3 — Programmer le réveil de l'agent

Une fois les consignes écrites, vous donnez à l'agent une date et une heure de réveil. Une fois (par exemple : "dans deux semaines, vendredi à 9h"), ou récurrent (par exemple : "le 1er de chaque mois").

Côté technique : ça se fait en une seule commande dans Claude Code (l'outil qu'on utilise pour gérer les agents). Comptez 2 minutes.

> **📸 Screenshot 7 à insérer ici** :
> Capture du terminal Claude Code après avoir tapé `/schedule` montrant l'écran de configuration du nouveau agent (nom, date, repo, modèle).
> *Pourquoi* : démystifier "la commande" — c'est un assistant qui pose des questions.

### Étape 4 — Lire le rapport et décider

À la date prévue, l'agent se réveille, fait son boulot pendant 5 à 10 minutes, et vous laisse une notification GitHub. Vous ouvrez le rapport. Trois sections seulement à regarder :

- **Synthèse** en haut : les chiffres clés en 5 lignes.
- **Anomalies détectées** : ce qui ne va pas, avec une recommandation par anomalie.
- **Recommandations** : 3 à 5 actions à prioriser pour le mois suivant.

Le reste du rapport (détail page par page) est de la documentation. Vous le gardez en référence, vous ne le lisez pas en entier.

> **📸 Screenshot 8 à insérer ici** :
> Capture des trois sections "Synthèse / Anomalies / Recommandations" du rapport markdown rendues côte à côte (capture longue ou trois captures verticales empilées).
> *Pourquoi* : montrer ce qui mérite réellement l'attention du CMO — 3 sections, 30 secondes de lecture.

---

## Pour aller plus loin : le vrai accès Google

L'estimation Google de l'agent est correcte mais imparfaite (4 sur 10). Si vous gérez un site important (e-commerce, média, SaaS avec plus de 500 pages), vous voulez du 100 % fiable. C'est possible en branchant l'agent à Google Search Console via ce que Google appelle son "API officielle".

Côté CMO, ce que vous devez savoir :

- C'est gratuit chez Google.
- Ça demande à votre tech 30 minutes de setup une fois (créer un compte d'accès dédié dans la console Google Cloud, lui donner permission sur votre Search Console, stocker la clé d'accès dans un endroit sécurisé sur GitHub).
- Une fois fait, l'agent vous donne le statut officiel de chaque page : indexée, découverte mais pas indexée, crawlée mais pas indexée, 404. Plus aucune devinette.

Pour un site de 30 pages comme le wiki Organikk, l'estimation suffit. Pour un site de 5 000 pages, c'est obligatoire.

---

## Le piège à éviter (le seul, mais important)

Beaucoup de gens veulent un agent qui "corrige tout seul". Page non indexée ? Que l'agent la soumette à Google. Page non maillée ? Que l'agent ajoute des liens automatiquement.

C'est une fausse bonne idée. Un agent qui modifie automatiquement votre site est un agent qui peut le casser à 3h du matin un dimanche, sans que vous le sachiez. Et l'expérience montre qu'il finit toujours par le faire.

Le bon design : l'agent observe, mesure, rapporte. **Vous** décidez. **Vous** ou votre équipe exécutez. C'est plus lent en apparence, mais c'est la seule façon de garder le contrôle de votre marque.

---

## À retenir

Trois choses :

1. **Vous payez déjà pour ne pas savoir.** Que ce soit votre temps, celui d'un junior ou celui d'une agence : vous payez pour publier sans mesurer. Un agent qui mesure pour vous coûte 0 € par mois après 15 minutes de setup.
2. **Le bon agent est passif.** Il observe, il rapporte. Il ne corrige rien. Cette discipline est ce qui le rend fiable.
3. **Le ROI est immédiat.** À partir du moment où votre rapport mensuel arrive automatiquement dans votre GitHub, vous arbitrez avec des chiffres. Vos arbitrages s'améliorent. Vos investissements SEO commencent à se payer.

C'est tout ce qu'il y a à comprendre.

---

## Annexe — Liste des screenshots à produire

À shooter avant publication (ou à laisser tel quel pour la version Obsidian privée) :

1. Dashboard Claude Code routines avec l'agent planifié
2. Le rapport `reports/wiki-indexation-2026-05-16.md` ouvert dans VSCode/Obsidian
3. Email GitHub "Pull request opened"
4. La PR GitHub avec la section "Synthèse" rendue
5. Le fichier `src/data/wiki.ts` ouvert dans VSCode
6. Le fichier de prompt agent ouvert (sections Mission/Étapes/Contraintes)
7. Le terminal Claude Code après `/schedule` (écran de configuration)
8. Les sections Synthèse/Anomalies/Recommandations du rapport rendu côte à côte
