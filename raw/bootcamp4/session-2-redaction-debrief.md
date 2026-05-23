---
type: bootcamp-session-debrief
bootcamp: 4
session: 2
date: 2026-05-15
duration: ~70 min
status: debrief
tags:
  - bootcamp4
  - session-2
  - rédaction
  - debrief
  - patterns
related:
  - "[[session-2-redaction-prep]]"
  - "[[session-2-redaction-transcript]]"
  - "[[observations-whatsapp-bootcamp]]"
  - "[[opendecoder-seo-scoring-system]]"
---

# Session 2 · Rédaction · Debrief du call

Synthèse du call S2 du 15 mai 2026 : ce qui a été dit en plus du `session-2-redaction-prep`, les questions sorties du groupe, les nouveaux concepts introduits en live, et les actions à mener pour la suite.

À utiliser comme base pour : le Google Doc résumé à envoyer aux participants, l'enrichissement du `session-2-redaction-prep` avec les clarifications live, la maj du `observations-whatsapp-bootcamp` avec les nouvelles questions, l'alimentation du `session-3-audit-prep` à venir.

---

## Nouveaux concepts ou clarifications introduits en live

Pas dans le prep doc en amont, sortis pendant le call et à intégrer.

### 1. Skill vs Workflow · règle d'usage à expliciter

Tim a passé du temps à distinguer les deux et a affirmé : "moi j'utilise plus les skills que les workflows". Un workflow = un process complet à lancer une fois. Un skill = à appeler ensuite seul quand il manque juste une brique (ex : trouver les mots-clés manquants sans relancer tout le workflow mots-clés).

**À ajouter dans le prep** : un encart "quand lancer un workflow vs juste un skill" en haut du §2.

### 2. La règle des 50% est nuancée selon le type de page

Position de Tim en live : **50% rédaction max pour les pages piliers**, mais **100% OK pour les modèles de page** (pSEO).

Ça nuance l'étape 4 du prep doc qui disait 40-50% sans qualifier. À préciser : c'est pour les pages piliers / fondamentales. Pour les modèles, on lui laisse beaucoup plus, on rédige nous-mêmes ~5-10%.

### 3. Fact-check à l'étape 5 ET à la sortie, pas seulement entre 50% et 100%

Le prep doc positionnait le fact-check après les 50% écrits par Claude. Tim a précisé en live : **fact-checker à l'étape 5 (validation structure Hn enrichie) parce qu'il y a déjà de la data dans les suggestions de Claude**, puis re-fact-checker à la sortie finale.

Plus le contenu est long, moins Perplexity / Grok fact-checkent bien. Donc fact-check par petites bouchées vaut mieux que fact-check d'un texte 2500 mots.

### 4. Grok Deep Search n'est plus accessible gratuitement (300€/mois)

Changement de doctrine annoncé en live : **Perplexity Deep Search devient le tool de fact-check par défaut** (20€/mois, partiellement gratuit). Grok reste pour les signaux sociaux (scraping tweets) sur les mots-clés, pas pour le fact-check.

À mettre à jour partout où on disait "Grok ou Perplexity au choix" → "Perplexity Deep Search en priorité, Grok pour les signaux X".

### 5. Pureté vectorielle · concept central à formaliser

Sorti en réponse à Jamel sur la FAQ. Une page = une pureté vectorielle. Pas qu'un mot-clé. Sur "agence SEO" tu donnes pas un outil audit + un cas client BTP + 10 sujets — tu noies l'intention. La FAQ sert pour les ouvertures connexes (ex : backlinks vs contenu) sans casser la pureté du corps.

Lié au fait que **plus le contenu est long, plus tu risques de pas être cité par les LLMs** (études récentes, à sourcer pour le prep doc).

**À ajouter dans le prep §2 ou §3** : sous-section "Pureté vectorielle" + référence aux études sur la longueur.

### 6. Intention de recherche utilisateur vs intention LLM

Précision live : sur "agence SEO", l'utilisateur attend "comment choisir la meilleure agence". Le LLM attend en plus "comparatif freelance vs agence". Ces deux sont déjà séparées dans le skill `seo-brief-contenu`. À expliciter dans le prep §2 étape 1.

### 7. README par client · fichier des règles d'itération

Pattern partagé en réponse à Jamel : **pour chaque client, créer un README qui agrège toutes tes remarques d'itération** ("pour ce client, jamais de chiffre en intro", "pas de jargon", "ne cite pas la loi X"). C'est un fichier de mémoire des règles spécifiques au client, lu par Claude à chaque conversation sur ce client.

Pas dans le prep doc, à formaliser et ajouter au workflow rédaction. Tim a dit "viens en 1V1" à Jamel = pas dérouler en plénière, mais à formaliser pour les autres.

### 8. Stratégie anti-ChatGPT · grille de tri des mots-clés

Sorti en réponse à Cécile sur "que vont devenir les sites des artisans". Tim a énoncé clairement sa doctrine actuelle :

> "Aujourd'hui moi j'ai des stratégies anti-ChatGPT. Je ne fais plus aucun mot-clé sur lequel ChatGPT peut se mettre."

Filtre clé pour les modèles de page :
- **Informationnel** → mangé par GPT
- **Comparatif** → grande chance mangé
- **Simulateur** → demain mangé
- **Outil basé data propriétaire** → safe
- **Transactionnel / décisionnel ultra-niché** → safe
- **Expérience interactive sur la page** → safe

À ajouter au §4 modèles de page comme grille de tri opérationnelle.

### 9. L'exemple hôtel · récupération email + partenariats

Tim a déroulé l'exemple complet du modèle séjours personnalisés pour hôtel : outil interactif sur la page → utilisateur remplit dates / type de festival / budget → "donne ton e-mail pour recevoir l'itinéraire" → email récupéré → si client, data utilisée pour partenariats locaux (alerte SMS "ce soir, allez manger là").

C'est un cas d'école parfait du "SEO récupère la data pour augmenter le panier moyen, pas juste créer des pages". À mettre en case study dans le prep §4 ou dans une note séparée `case-study-hotel-sejours.md`.

### 10. ChatGPT a votre historique → ultra-personnalisation des pages

Insight critique : ChatGPT connaît votre fiche d'impôts, votre situation pro, votre famille. Quand vous tapez "séjour Bordeaux pas trop cher", il personnalise. **Donc demain on aura une page par persona ultra-spécifique**, pas une page générique.

Implication SEO : les mots-clés du futur ne sont plus dans SEMRush ou les PAA, ils sont dans les calls clients et les SAV.

À formaliser dans le prep ou dans un doc séparé pour la S3.

### 11. Hubs + Directories · architecture de site post-LLM

Sorti en réponse à Juliette ("articles ou pages ?"). Tim a montré organikk.co :
- Hub "Stratégies SEO par typologie" → page mère + N pages spécifiques (directory)
- Hub "Actualité SEO" → 1 étude par page, 1 mot-clé par étude
- Pour hôtel : hub "Où manger", hub "Quoi visiter", hub "Séjours personnalisés"

Format : page mère explique l'angle, contient le contenu d'autorité, puis liste les pages spécifiques comme une catégorie e-commerce avec filtres.

À ajouter dans le prep §4 comme architecture de référence.

### 12. Score Claude qui s'auto-améliore

Tim a précisé le mécanisme : Claude garde les scores en mémoire. Si un article a fait 88 et a été cité par GPT, il sait que 88 = note moyenne pour cette thématique. Il fait -90 sur le prochain → il sait qu'il doit améliorer. **Le standard d'exigence monte avec le temps**.

Implication : scorez systématiquement vos pages fondamentales. C'est pas le score qui compte, c'est la trajectoire et la mémoire.

### 13. Suivi citations LLM · Analytique, pas un outil "AI tracker"

> "Pour le scraping LLM, vous allez pas prendre un outil, c'est bidon. La plupart des outils sont bidon, j'espère que personne en produit ici."

Recommandation : suivi à la main avec les clients, ou via Analytique (à creuser, Tim a mentionné mais sans démo). Le data peut être redonnée à Claude pour qu'il sache si les articles à 88 sont effectivement cités.

### 14. "Si t'es pas bon en SEO, Claude sera pas bon"

Phrase à retenir et à reprendre dans le résumé Google Doc. Pose clairement que le bootcamp ne remplace pas l'expertise SEO, il la démultiplie.

---

## Questions et réactions du groupe pendant le call

À fusionner dans `observations-whatsapp-bootcamp.md` ou conserver ici en archive du call.

### Christophe · combien de temps prend une rédaction

Question implicite : tu nous dis 45 min, mais en pratique combien ?

Réponse Tim : 45 min pour les contenus standard. **1h30 à 2h pour les contenus fondamentaux**. 1h pour 5 pages de modèle (quand le système est rodé). À mettre dans le prep pour gérer les attentes.

### Jamel · README par client (cf. supra)

Question pertinente, Tim a répondu mais en mode "viens en 1V1". À formaliser pour le groupe.

### Cécile · le web devient inaccessible aux artisans

Vraie inquiétude éthique exprimée. Tim a recadré : la prime va à l'ultra-niche et l'expertise prouvée. Plombier 15e urgence de nuit > plombier Paris. Star of Service démonté = Google ne veut plus de marketplace, il veut des artisans locaux. Réponse à creuser, c'est un sujet qui va remonter dans le bootcamp et hors bootcamp (drama Déborah LinkedIn).

### Cécile · que vont devenir les sites artisans / asso / artistes sans SEO

Tim : Claude va faire la commodité, personne ne paiera pour la commodité. Vous arrivez pour la brique au-dessus. Stratégies anti-ChatGPT (cf. supra).

### Juliette · architecture site, articles ou pages

Réponse : hubs + directories (cf. supra). Question fondamentale qui va revenir, mérite un article ou une formation.

### Julien · plusieurs clients dans Claude

Une conversation par client, une seule. Claude est infini en théorie, fenêtre 1M tokens, vide et résumé derrière. Sur Claude Code (terminal) la limite saute en pratique.

### Romain · projet vs conversation, instructions

Confirmation : un projet par client, une seule conversation dans ce projet, instructions du projet respectées mais pas toujours, ton de voix à redonner manuellement à chaque rédaction.

### Question anonyme · documents .md pas pris en compte

Solution : redonner les fichiers en début de conversation, même s'ils sont dans le dossier local. Une fois qu'il les a vus dans la conv courante, il les oublie plus.

### Caroline · suivi citations LLM via Claude

Confirmation que oui, donner à Claude les articles cités pour qu'il calibre son standard. Outil Analytique mentionné.

### Question · workflow rédaction = mise à jour de skill

Question coupée au transcript ("non j'avais une question sur la mise à jour des skills"). À reprendre en MP ou en S3.

---

## Action items pour Tim

À traiter dans les jours qui suivent le call.

1. **Google Doc résumé** à envoyer au groupe (template du S1 résumé). Sections : ce qu'on a vu (5 étapes + fact-check + scoring + modèles), nouvelles règles (anti-ChatGPT, hubs + directories, README par client), prochaine étape S3 audit.

2. **Mettre à jour le `session-2-redaction-prep`** avec :
   - La nuance 50% piliers / 100% modèles
   - Fact-check à l'étape 5 ET à la sortie
   - Perplexity Deep Search en priorité (vs Grok payant)
   - Pureté vectorielle en sous-section
   - Intention LLM vs intention utilisateur dans le brief
   - README par client dans le workflow rédaction
   - Stratégie anti-ChatGPT comme grille de tri
   - Hubs + Directories dans §4 modèles de page
   - Cas hôtel séjours personnalisés en case study

3. **Maj `observations-whatsapp-bootcamp`** avec les questions du call (Christophe temps, Cécile éthique web, Juliette architecture, suivi citations LLM).

4. **Lien Drive** : le workflow rédaction n'avait pas été mis en MD en plus du skill. Tim a dit "je vous le remettrai en MD". À faire et envoyer au groupe.

5. **Études à sourcer** :
   - L'étude qui dit que plus le contenu est long, moins il est cité par les LLMs
   - L'étude qui fonde le scoring `opendecoder-seo-scoring-system` (Tim a dit "50 pages, je pourrais vous la donner")

6. **1V1 Jamel** sur le README par client.

7. **Préparer le S3 audit** en intégrant les questions de fond posées (Cécile, Juliette) dans le cadrage.

8. **Skill mise à jour** : la question coupée à la fin du transcript ("question sur la mise à jour des skills") à reprendre via WhatsApp ou en S3.

---

## Citations marquantes pour le Google Doc / posts LinkedIn

- "Si vous êtes pas bon en SEO, Claude sera pas bon."
- "Demain tout le monde va être capable de demander à Claude le content gap sur sa niche. Tout le monde. L'idée c'est d'utiliser Claude pour avoir une seconde couche."
- "Au départ on se dit oui je vais lui donner des choses à faire et à la fin on lui donne plus rien, on lui dit rédige rédige, et en fait vous perdez complètement votre réflexion."
- "Plus vous êtes capable de trouver ou de casser les patterns sur une SERP, meilleur sera votre contenu. Répéter ce que les autres ont dit, il le fait déjà."
- "Si l'IA rédige mieux que vous, vous avez aucune raison de rédiger ce contenu."
- "Le standard de rédaction jusqu'à 100 peut pas être atteint avec l'IA. C'est forcément vous qui ajoutez des choses à la main."
- "Claude va faire la commodité, personne ne paiera pour la commodité. Vous arrivez pour la brique supplémentaire."
- "On crée pas un article par un article. On crée une cohérence sémantique pour votre client."
- "Aujourd'hui moi j'ai des stratégies anti-ChatGPT. Je ne fais plus aucun mot-clé sur lequel ChatGPT peut se mettre."
- "Vous êtes plus uniquement des SEO qui créent des pages qui servent à rien, mais des SEO qui récupèrent la data pour améliorer l'expérience client."

---

## Risques / signaux faibles à surveiller

- **Cécile** a exprimé un vrai malaise éthique ("hyper choquée"). À ne pas écraser, à intégrer dans la doctrine bootcamp (le SEO de la commodité meurt, on en fait pas une fatalité, on construit la couche au-dessus).
- **Niveau technique du groupe disparate** : Cécile et d'autres ont demandé plusieurs fois "qu'est-ce qu'un hub", "comment on fait", "c'est du chinois". Tim a renvoyé en MP plusieurs fois. Surveiller que ces participants ne décrochent pas en S3.
- **Le terminal / Obsidian** : Tim a dit "c'est pas pour tout le monde, c'est technique". Bien cadrer pour qu'on ne perde pas la moitié du groupe en S4 sur Obsidian.
- **Pas de transcript / replay Google Meet** disponible (Anne a demandé). À fournir avec le Google Doc résumé.
