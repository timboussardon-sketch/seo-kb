# 45 études sur le GEO, et aucune ne prouve que vos techniques vous font entrer dans la réponse

_Timothée_

> **En résumé**
> - Une revue critique de 45 études GEO, publiée le 15 juillet, conclut qu'aucune technique passée en revue n'a d'effet causal démontré sur le fait d'être retrouvé par un moteur IA.
> - Le GEO sait modifier la façon dont un contenu déjà retrouvé est cité. Il ne sait pas prouver qu'il fait entrer un contenu dans la sélection. Ce sont deux problèmes différents, et le marché vend le second avec les chiffres du premier.
> - Deux comptes ChatGPT testés à la même période ne voient pas les mêmes sources : votre audit GEO mesure un compte, pas un moteur.

**Baromètre SEO IA :** jamais autant d'outils pour mesurer votre présence dans les réponses IA, et toujours aucune preuve que ce qu'ils mesurent tienne d'un compte à l'autre.

Pour vous aider à repérer les infos les + utiles :

★★★★★ impact énorme · ★★★☆☆ à surveiller · ★☆☆☆☆ anecdotique

---

## Le sujet du jour

### 45 études passées en revue, et zéro preuve d'effet causal ★★★★☆

Vous payez peut-être un outil qui vous annonce que vous êtes cité 12 % du temps sur vos requêtes. Question simple : 12 % de quoi, mesuré depuis quel compte, et est-ce que ce chiffre veut dire quelque chose le mois prochain ?

Le 15 juillet, une revue critique est parue sur arXiv. Elle passe au crible 45 études sur le GEO, tout ce qui est sorti entre novembre 2023 et juillet 2026. La conclusion tient en une phrase : aucune technique passée en revue ne montre d'effet causal stable, tenant dans le temps et d'un moteur à l'autre, sur le fait d'être retrouvé.

Attention à ce que ça ne dit pas. Ça ne dit pas que le GEO ne sert à rien.

Voilà ce que la littérature établit vraiment. Quand votre contenu est **déjà** dans le contexte du moteur, vous pouvez agir sur la façon dont il est cité et utilisé. C'est mesuré, ça marche. Ce qu'elle n'établit pas, c'est qu'une technique vous fasse **entrer** dans cette sélection. Le papier le dit même du papier fondateur du GEO, celui dont tout le marché cite les gains depuis deux ans : ses résultats sont valides, mais uniquement dans un cadre où la source était déjà présente dans le contexte. Ils n'établissent, je cite, « ni la découvrabilité organique, ni un effet durable sur le trafic ».

Deux choses de cette revue sont directement utilisables demain matin. Ce qui se reproduit le mieux d'une étude à l'autre, c'est la pertinence thématique et la position de l'information dans le contexte. Et ce qui peut vous nuire : réécrire une page pour « être citée » peut dégrader ce qui la fait retrouver. Je le répète depuis avril, et ça vient d'être corroboré par un corpus de 45 études que je n'avais pas.

**Pourquoi ça compte :** la question à poser à un prestataire GEO n'est plus « combien de citations vous me garantissez ». C'est « est-ce que vous agissez sur du contenu déjà retrouvé, ou est-ce que vous prétendez le faire entrer dans la sélection, et sur quelle preuve ». La première réponse est un métier. La seconde est une promesse que personne ne sait tenir aujourd'hui.

Source : arXiv, 15 juil. 2026 : https://arxiv.org/abs/2607.14035

Reste à savoir si on sait au moins mesurer. Spoiler : non.

### Deux comptes ChatGPT ne voient pas le même moteur ★★★★☆

Suganthan Mohanadasan a ouvert les outils de développement de son navigateur et regardé ce que ChatGPT appelle réellement quand il va chercher des sources. Il y a trouvé un champ nommé `result_source`, et un canal qu'il n'avait jamais vu passer : `bing`.

Le détail qui pique : sur ses 30 dernières conversations, soit 595 résultats, il compte `bright` 558 fois, `labrador` 21 fois, `serp` 16 fois. Et `bing` zéro fois. Pas une seule. Sa phrase : « le déploiement n'est même pas servi à mon compte ». Pendant ce temps, un autre testeur, David Konitzny, le voit se reproduire sur plusieurs prompts. Deux personnes, même moteur, même période, deux réalités.

Un preprint publié le lendemain enfonce le clou par un autre chemin. Des chercheurs ont mesuré ce qui casse quand on retire un document à un agent qui cherche en plusieurs étapes. Résultat : la pertinence d'un document « sur le papier » et son utilité réelle sont statistiquement indépendantes (corrélation de -0,026). Environ un tiers des documents qui servent vraiment à l'agent paraissent inutiles quand on les note. Ils ne sont cités nulle part, mais sans eux la réponse ne se construit pas.

**Pourquoi ça compte :** votre audit GEO mesure un compte, pas un moteur. Tant qu'un rapport ne dit pas quel compte, quel abonnement, quel pays et quelle date de relevé, vous ne pouvez comparer ni au mois dernier, ni au client d'à côté. Si vous facturez du suivi de citations IA, notez ces quatre informations dès maintenant. Sinon vous ne défendrez pas votre chiffre le jour où un directeur marketing vous demandera pourquoi il a bougé.

Sources : Suganthan, 14 juil. 2026 : https://suganthan.com/blog/how-chatgpt-picks-sources-part-2/ · arXiv, 16 juil. 2026 : https://arxiv.org/abs/2607.15253

👉 **[Tester Qadence : savez-vous si l'IA vous cite ?](https://qadence.io)**

---

## En bref

**Indexation ★★★★☆ :** John Mueller et Martin Splitt ont consacré un épisode de Search Off the Record au rapport d'indexation de la Search Console. Leur message : un volume anormal de « crawled currently not indexed » n'est pas un bug technique à corriger URL par URL, c'est un verdict de qualité sur le site entier. Mueller ne vise pas le contenu généré par IA en tant que tel, il vise le contenu générique que n'importe qui aurait pu écrire. Si vous produisez des pages en masse sans données à vous, votre budget de crawl se referme. Search Engine Roundtable, 16 juil. 2026 : https://www.seroundtable.com/google-crawled-not-indexed-quality-ai-content-41701.html

**Google ★★★☆☆ :** Google a mis à jour son guide de dépannage de la canonicalisation et donne enfin un délai. Après avoir corrigé un contenu dupliqué, comptez jusqu'à deux semaines avant que vos pages se séparent. La condition posée compte autant que le délai : la séparation est plus rapide si la différence entre le nouveau contenu et le reste du groupe est « claire et significative ». Traduction pour vos pages programmatiques : si seule la variable change, elles resteront collées. Google Search Central, 10 juil. 2026 : https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting

**AI Overviews ★★☆☆☆ :** la génération d'images descend d'AI Mode vers les AI Overviews, avec le modèle Nano Banana de Google. Déploiement dans les semaines qui viennent, en anglais, dans les régions qui gèrent déjà la création d'images. Si la réponse fabrique l'image à la demande, une image générique indexée perd sa fonction de porte d'entrée. Ce qu'une image générée ne produira jamais, c'est la photo de votre produit réel, de votre chantier réel, de votre équipe réelle. Search Engine Land, 14 juil. 2026 : https://searchengineland.com/google-ai-overviews-now-lets-you-create-image-482163

---

## Question du jour

**Vos outils de suivi de citations IA vous donnent-ils des chiffres auxquels vous vous fiez ?**

- Oui, je pilote avec
- Je regarde, mais je ne facture pas dessus
- Non, les écarts entre outils sont trop gros

---

👉 **[Trouver des leads SEO](https://organikk.co/consultant-lead-seo)**
