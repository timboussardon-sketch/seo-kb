---
type: bootcamp-session-prep
bootcamp: 4
session: 4
topic: automatisations-posture-livraison
date: 2026-05-28
status: prep
tags:
  - bootcamp4
  - session-4
  - automatisations
  - posture-seo
  - livraison-skills
related:
  - "[[sequencage-semaine-4]]"
  - "[[skill-roadmap-pseo]]"
  - "[[skill-preparation-semantique]]"
  - "[[install-repo-skills-cowork]]"
  - "[[skills-checklist-bootcamp4]]"
  - "[[session-3-audit-prep]]"
  - "[[observations-whatsapp-bootcamp]]"
---

# Session 4 · Call · Prep

Run-of-show du call S4. Trois skills à présenter, une posture à poser, une annonce de livraison. Objectif du call : montrer que la semaine ferme la boucle (on automatise et on livre un système), et redresser la posture commerciale avant que les participants aillent vendre.

## Ordre du call

0. Ouverture · bilan des 4 semaines (le chemin parcouru)
1. Prompt revue de presse (la veille qui tourne seule)
2. To do list (le suivi qui se reconstruit seul)
3. Roadmap client (le plan qu'on vend)
4. Posture SEO : on ne vend pas de trafic
5. Obsidian + lien GitHub : je veux tout vous donner

On ouvre sur le bilan (orienter, célébrer le chemin), puis trois démos (concret), puis la posture (le cadre mental), puis l'annonce livraison (le cadeau). On ouvre sur la fierté, on finit sur le cadeau.

---

## 0. Ouverture · bilan des 4 semaines

C'est le dernier call. On prend deux minutes pour regarder le chemin avant de poser les dernières briques. En quatre semaines, vous n'avez pas collectionné des outils. Vous avez monté une chaîne complète.

**Semaine 1 · Mots-clés.** On a tué l'idée du mot-clé unique. Ce qui ranke, c'est un nuage de micro-intentions assemblé en vecteur sémantique. Vous êtes passés de "quel mot-clé" à "quelle couverture".

https://fusionn.co/blog/liste-des-mots-cles-redacteur-web

**Semaine 2 · Rédaction.** Le brief qui conditionne tout, le workflow qui rédige bout en bout, le fact-check qui ancre l'autorité, le scoring qui mesure la surprise et le grounding. Vous produisez un article qui ne ressemble pas à du ChatGPT.



**Semaine 3 · Audit.** Diagnostiquer un site avec la seule data Google : indexation, quick wins, cannibalisation, maillage. Et le filtre anti-ChatGPT, on ne cible que ce que l'IA ne peut pas manger à votre place.


**Semaine 4 · Le système.** Cette semaine on a outillé les deux bouts qui manquaient : les données structurées et l'audit de perf de vos pages (page speed) qui la rendent irréprochable, et la roadmap qui ordonne la production.

**Le fil rouge des quatre semaines** : on ne court pas après le volume, on construit des pages décisionnelles qui convertissent, et on les produit avec un système qui tourne. C'est ça qui vous distingue d'une agence qui pond du contenu au kilo.

Ce que vous avez maintenant, ce n'est pas 21 skills isolés. C'est une chaîne : trouver → préparer → rédiger → auditer → baliser → optimiser → planifier. Chaque maillon nourrit le suivant. Aujourd'hui on pose les dernières briques, on cadre comment vous le vendez, et je vous donne tout.

---

## 1. Prompt revue de presse

**Ce que c'est** : une veille automatique qui sort chaque jour un brief avec des chiffres et des études sourcés sur une thématique. C'est le système qui fait tourner ma newsletter Algorithme. On le rebranche sur la thématique du client.

**Pourquoi ça compte** : la fraîcheur est un signal. Une page qui s'appuie sur un chiffre de la semaine, sourcé, bat une page figée. Et ça nourrit le Surprise Score sans que tu passes tes journées à scraper. Le contenu reste vivant tout seul.

**À montrer en live** : lancer le prompt sur une thématique (la mienne ou celle d'un participant), montrer la sortie datée avec les liens sources. Montrer que c'est exploitable directement en rédaction (ça repart dans `article-engine-pipeline`).

**Le piège à dire** : on ne publie jamais la veille brute. Elle alimente, elle ne remplace pas. Un chiffre sort dans une page seulement s'il est sourcé et vérifiable, sinon il dégrade la note (même règle qu'au fact-check de la S2). La veille te donne la matière, toi tu valides.

**Sur le Drive** : deux docs, la revue de presse client (à trous, à rebrancher sur la thématique du client) et la revue de presse SEO/IA (le brief quotidien sur notre niche).

---

## 2. To do list

**Ce que c'est** : le skill `todo` reconstruit ta todo en lisant tes transcripts Claude Code des 7 derniers jours. Pas un task manager que tu alimentes à la main. Un miroir de ce que tu as vraiment fait.

**Pourquoi ça compte pour vous** : vous enchaînez des sessions Claude toute la journée (audit, rédaction, prospection). Personne ne tient une todo en parallèle, c'est du double travail. Le skill te rend un point clair de ce que tu as livré cette semaine (utile pour facturer un client), les chantiers en cours à reprendre, et les intentions que tu as verbalisées mais pas exécutées.

**À montrer en live** : lancer `/todo`, montrer le découpage ✅ FAIT / 🔄 EN COURS / 📋 À FAIRE. Insister : c'est généré, pas saisi.

**Le piège à dire** : skill terminal uniquement. Il lit le système de fichiers local (`~/.claude/projects/`). Si tu es sur Cowork pur sans terminal, tu ne peux pas le lancer tel quel. Les Cowork, MP, on voit une alternative.

---

## 3. Roadmap client

**Ce que c'est** : le skill `seo-roadmap-pseo`. Tu donnes une thématique (ou une liste de mots-clés) + la Money Page du client, il sort un calendrier de production sur 90 jours, en deux phases.

**La logique 2 phases (à marteler)** :
- Phase 1, transactionnel et décisionnel d'abord. Les pages qui convertissent, celles qui paient le SEO dès le premier mois. C'est ça qui justifie le budget au client.
- Phase 2, informationnel bas de funnel ensuite. Les pages proches de la décision qui alimentent Phase 1 par maillage. Jamais d'informationnel pur, ça se fait manger par ChatGPT.

L'ordre n'est pas négociable. Si tu commences par l'informationnel, tu fabriques de l'autorité que tu ne monétises pas, et le client ne voit pas de retour.

**À montrer en live** : lancer sur un cas client réel avec sa Money Page. Montrer la sortie : synthèse exécutive, calendrier par mois, et surtout la section "mots-clés rejetés".

**L'angle commercial (le point fort)** : la section "mots-clés rejetés" explique au client pourquoi tu ne produis PAS certaines pages. Ça prouve que tu ne factures pas du volume au kilo, que tu protèges son budget contre les pages que l'IA va dévorer. C'est ton argument anti-agence-qui-pond-200-articles-inutiles.

**Le piège à dire** : pas de roadmap sans Money Page identifiée. Si le client ne sait pas où il convertit, le skill bloque. Et pas de volume inventé : sans data GSC/Ahrefs, le skill met `[À SOURCER]`. Ne présente jamais une roadmap avec des chiffres inventés à un client.

**Ce que ça boucle** : ce skill assemble toute la chaîne du bootcamp. Mots-clés (S1) → prépa sémantique (S4) → rédaction (S2) → audit (S3) → et la roadmap qui ordonne tout dans le temps. C'est la synthèse.

Montrer pour leexi : https://mail.google.com/mail/u/0/#search/leexi/KtbxLzFzVwczpxGSWGkZDqvPQwDDtrZPFg?projector=1&messagePartId=0.1

---

## 4. Posture SEO : on ne vend pas de trafic

C'est le moment le plus important du call. Pas une démo, un cadrage mental. Si les participants partent vendre avec la mauvaise posture, tous les skills du monde ne les sauveront pas.

**Le piège du consultant SEO classique** : vendre du trafic. "Je vais vous ranker", "je vais vous amener X visiteurs", "on vise la position 1". Problème : le trafic est devenu une promesse que tu ne contrôles plus. Les AI Overviews répondent à la place du site, ChatGPT mange l'informationnel, Google bouge ses critères tous les mois. Tu vends une métrique qui ne t'appartient pas. Le jour où elle baisse pour une raison externe, tu es mort aux yeux du client.

**Ce qu'on vend à la place** : un système qui automatise une partie de leur SEO. Pas une promesse de position, une machine. On leur installe quelque chose qui prépare la sémantique, qui rédige, qui balise, qui mesure, qui fait la veille, et qui tourne sans eux. Le trafic, c'est la conséquence du système, pas le produit qu'on vend.

**Ce que le client achète vraiment** :
- Du temps récupéré (il arrête de faire à la main ce qui tourne tout seul)
- De l'autonomie (le système reste chez lui, il n'est pas pieds et poings liés à une agence)
- Un actif (le système est un livrable tangible, pas une promesse en l'air)

**La phrase à leur donner pour vendre** : "Je ne vous vends pas des promesses de position. Je vous installe un système que vous gardez, qui automatise la préparation, la rédaction, le balisage et le suivi de votre SEO. Le trafic, c'est ce qui en sort, pas ce que je facture."

**Pourquoi c'est plus solide** : une promesse de trafic, si l'algo bouge, tu sautes. Un système installé, c'est livré, ça tient quoi qu'il arrive, et ça se re-vend en accompagnement (mois 2, optimisation, nouveaux clusters). Tu passes d'une obligation de résultat impossible à tenir à une obligation de moyens que tu maîtrises à 100%.

**Lien avec la semaine** : c'est exactement ce qu'on a outillé. La roadmap (skill 3) n'est pas un plan de trafic, c'est un plan de production d'un système. La veille (skill 1) et la todo (skill 2) sont des briques de ce système qui tourne seul.

---

## 5. Obsidian + lien GitHub : je veux tout vous donner

**Montrer l'Obsidian** : ouvrir le vault en partage d'écran. Leur montrer que tout mon système vit là (les skills, la doctrine, la KB, les workflows). L'idée à faire passer : ce n'est pas magique, c'est organisé. Chaque skill est un fichier, chaque décision est notée. C'est ça qui rend Claude pertinent, le contexte accumulé.

**L'annonce** : je veux arrêter de vous donner les skills un par un en copier-coller. Je veux tout vous donner d'un coup, via un lien GitHub que vous donnez directement à votre Claude. Vous pointez votre Claude sur le repo, et vous avez l'intégralité des skills, à jour. Quand j'améliore un skill chez moi, vous récupérez la nouvelle version sans rien refaire.

**Le bénéfice pour eux** : une source unique, maintenue. Plus de "j'ai loupé le bundle de la semaine 2". Plus de versions courtes vs longues qui traînent. Tout, au même endroit, toujours à jour.

**Ce qui reste à caler (à dire honnêtement ou à garder pour moi)** : le repo est privé pour l'instant. Je dois trancher comment vous y donner accès (lien direct, ZIP sur le Drive, ou accès collaborateur). La procédure d'install complète arrive dans un doc dédié. Cf. [[install-repo-skills-cowork]] pour le pas-à-pas (Mac, Windows, Cowork).

**Note** : ne pas promettre une date si ce n'est pas calé. Annoncer l'intention et la valeur, livrer le lien quand c'est propre (repo curé des skills internes, README ajouté).

---

## Notes pour Tim (interne)

- **Ordre voulu** : bilan d'ouverture → 3 démos (revue de presse, todo, roadmap) → posture → annonce GitHub. Le bilan oriente et célèbre le chemin (c'est le dernier call), les démos pour le concret, la posture au milieu pour le cadre, l'annonce à la fin pour finir sur le cadeau. Si le temps manque, la posture (point 4) est non-négociable, c'est elle qui change leur manière de vendre. Une démo peut sauter, pas la posture. Le bilan peut se raccourcir à 1 minute si besoin, mais ne le coupe pas, c'est l'ouverture émotionnelle du dernier call.
- **Roadmap = jamais testé en prod.** Lance-le une fois AVANT le call sur un cas réel (un de tes clients) pour ne pas découvrir un bug en live. Cf. note de [[skill-roadmap-pseo]].
- **Todo terminal-only** : 2-3 participants sont sur Cowork pur (Lydia, Gregory possiblement). Préviens-les en amont que la démo todo ne sera pas reproductible chez eux tel quel, qu'ils ne décrochent pas.
- **Revue de presse client = bundle à trous pas finalisé.** Le doc Drive existe mais "le rebrancher sur la thématique du client" n'est pas documenté en pas-à-pas (cf. note [[sequencage-semaine-4]]). Si tu démontres en live, prépare le cas à l'avance, ne l'improvise pas.
- **Posture : c'est ta doctrine, parle-en avec tes mots.** Les talking points du point 4 sont une trame, pas un script à lire. C'est le moment où ton expérience terrain (Train Luxe Afrique, Golfiller, les clients qui ont vu leur trafic bouger) rend le propos crédible. Donne un exemple réel de toi qui as arrêté de vendre du trafic.
- **GitHub : ne promets pas de date.** Le repo n'est pas encore curé (skills internes Organikk/bxble/fusionn dedans) ni public. Annonce l'intention et la valeur, livre quand c'est propre. Le doc d'install [[install-repo-skills-cowork]] est prêt, le ZIP via le script `bundle-skills-bootcamp.sh` aussi.
- **Lien avec le J5 du séquençage** : ce call EST le J5 de [[sequencage-semaine-4]]. La démo "de la matière première au plan qu'on vend" prévue au séquençage = l'enchaînement prépa sémantique → page → roadmap. Cohérent avec l'ordre ci-dessus.
- **Normalisation** : doc sans em-dashes (règle maison).
