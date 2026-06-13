# Décryptage de l'algorithme Grok de X (Phoenix)

> Compagnon de [[Playbook-X-autorite-SEO-IA]]. Étude de l'algo de recommandation de X depuis le passage sous Grok (xAI), open-sourcé le 20 janvier 2026.
> Audit web juin 2026. Source primaire : repo `github.com/xai-org/x-algorithm` (Apache 2.0, Rust ~57 % / Python ~43 %).

---

## En résumé

X a jeté son ancien algo « à la main » (features et heuristiques codées une par une) et l'a remplacé par **un seul modèle transformer**, dérivé de Grok, baptisé en interne **Phoenix**. Le changement de paradigme tient en une phrase de Musk : *« Grok lit littéralement chaque post et regarde chaque vidéo (100M+/jour) pour matcher les users avec ce qui les intéresse le plus. »*

Conséquences concrètes pour toi :

1. **L'algo comprend le sens, pas les mots-clés.** Plus besoin de hashtags ni de bourrage de mots-clés. Grok lit ton post comme un lecteur humain. Ça récompense la **clarté et la substance**, pas les astuces.
2. **Il prédit ~15 comportements** (réponse, repost, bookmark, dwell, follow… et les négatifs : block, mute, report) et combine ces probabilités en un score unique. Ton job : maximiser les signaux positifs forts (conversation, bookmark, dwell) et ne jamais déclencher les négatifs.
3. **La cohérence thématique est récompensée mécaniquement.** Le modèle te range dans des clusters d'intérêt. Rester dans ta niche search/IA = jusqu'à ~3x plus de distribution hors réseau. Le compte fourre-tout est puni par construction.
4. **Le ton compte maintenant.** Grok lit le sentiment : le constructif est distribué plus large, le combatif/outrage est réduit même s'il génère de l'engagement. Bonne nouvelle pour un positionnement d'autorité pédagogique.

⚠️ **À retenir avant tout le reste (vérifié dans le code source)** : j'ai lu le code du repo. Il publie l'architecture et la *formule* de scoring, mais **aucun poids chiffré**. Dans le code (`ranking_scorer.rs`), chaque poids est chargé à l'exécution via `params.get(FavoriteWeight)`, `params.get(ReplyWeight)`, etc. : les valeurs vivent dans le système de feature-switches de xAI, qui n'est **pas** dans le repo public. Donc tous les « réponse = +13.5 », « conversation = 75x un like » qui circulent sont des estimations reverse-engineerées par la communauté, **impossibles à confirmer depuis la source**. Utilise-les comme ordre de grandeur, jamais comme vérité.

---

## 1. Le changement de paradigme

Avant : un empilement de modèles spécialisés + des centaines de règles écrites à la main (le fameux « heavy ranker » de 2023, les boosts/malus codés en dur).

Depuis janvier 2026 : *« suppression de toutes les heuristiques »*. Un transformer unique apprend la pertinence directement à partir des séquences d'engagement des utilisateurs. C'est exactement la même logique qu'un LLM, appliquée au feed.

Ce que ça implique :
- **Le contenu est lu sémantiquement** (texte, image, vidéo). Grok « comprend l'essence » du post.
- **Les hacks de surface meurent** : hashtags, keyword stuffing, formats-gimmicks. Ce qui survit, c'est le fond.
- **Musk s'est engagé à ré-open-sourcer le code toutes les ~4 semaines** avec des notes développeur. À surveiller : ça veut dire que l'algo bouge vite, et qu'on peut suivre les changements à la source.

---

## 2. L'architecture en 7 étapes (d'après le repo)

Le pipeline « For You » :

1. **Query Hydration** : récupère ton contexte (historique d'engagement, comptes suivis).
2. **Candidate Sourcing** : rassemble les posts candidats depuis deux moteurs :
   - **Thunder** = in-network (comptes que tu suis).
   - **Phoenix Retrieval** = out-of-network (découverte par ML).
   Sur ~100-500M posts/jour, on descend à ~1500 candidats.
3. **Candidate Hydration** : enrichit chaque candidat (métadonnées, auteur, média).
4. **Pre-Scoring Filters** : vire les doublons, posts trop vieux, auteurs bloqués, mots-clés mutés, déjà-vus.
5. **Scoring** : applique les rankers (dont Phoenix) en séquence.
6. **Selection** : trie par score, garde le top-K.
7. **Post-Selection Filters** : derniers contrôles de visibilité (c'est là que se jouent les déboosts/filtres de visibilité).

**Détail technique clé** : « candidate isolation in ranking ». Chaque candidat est scoré *seulement* contre ton contexte utilisateur, **pas** les uns contre les autres. Score stable et cacheable. Traduction stratégique : ton post est jugé sur sa pertinence pour chaque user, pas dans une course directe contre les autres posts du feed.

---

## 3. Phoenix : le cœur transformer

- Modèle transformer basé sur l'architecture Grok.
- Le repo livre une version **mini Phoenix pré-entraînée (~3 Go via Git LFS)** + le pipeline d'inférence + « Grox » (le pipeline de compréhension de contenu) + le framework de candidats.
- Il **prédit une série d'actions** par post, puis combine leurs probabilités.

**Les actions réellement scorées (lues dans `ranking_scorer.rs`, plus fines que les « 15 » souvent citées) :**

*Positives* : favorite (like), reply, retweet, photo_expand, click, profile_click, **vqv** (video quality view), share, **share_via_dm**, **share_via_copy_link**, dwell, quote, quoted_click, quoted_vqv, **cont_dwell_time** (durée de lecture continue), cont_click_dwell_time, follow_author.

*Négatives* : not_interested, block_author, mute_author, report, **not_dwelled** (scrollé sans s'arrêter).

Trois enseignements que seul le code révèle :
- **`not_dwelled` est un signal négatif explicite.** Un hook faible ne fait pas que « rater » : il te pénalise activement. Les gens qui scrollent ton post sans s'arrêter te coûtent du score.
- **Le partage privé est tracké à part** (`share_via_dm`, `share_via_copy_link`). Le post qu'on s'envoie en DM ou dont on copie le lien est un signal positif distinct. Le contenu « à faire suivre à un collègue » vaut cher.
- **La vidéo (`vqv`) n'est pondérée que si la durée dépasse un minimum** (`MIN_VIDEO_DURATION_MS`). Les micro-vidéos ne touchent pas le poids vidéo.

---

## 4. La formule de scoring

Le repo l'écrit noir sur blanc :

```
Score final = Σ (poids_i × P(action_i))
```

- Les actions positives (like, repost, share…) ont des poids positifs.
- Les actions négatives (block, mute, report) ont des poids négatifs.
- **Les valeurs des poids ne sont PAS divulguées** dans le repo.

**Poids estimés qui circulent (reverse-engineering communautaire, à prendre avec des pincettes) :**

| Action | Poids estimé | Statut |
|---|---|---|
| Like | +1 (référence) | estimation |
| Profile visit | ~+12 | estimation |
| Link click | ~+11 | estimation |
| Dwell time | ~+10 | estimation |
| Bookmark | ~+10 | estimation |
| Reply | ~+13.5 | estimation |
| Conversation à double sens (il te répond, tu réponds) | ~+75 | estimation |
| Block / mute / report | fortement négatif | structurel |

Même si les chiffres exacts sont incertains, **la hiérarchie est solide et recoupée partout** : conversation >> bookmark ≈ dwell ≈ profile visit > like. Une poignée de réponses à forte valeur sous un gros compte bat cent réponses bidon (Grok note la substance sur une échelle qualitative, pas le volume).

---

## 4bis. Deux mécaniques que seul le code source prouve

En lisant `ranking_scorer.rs`, deux choses qu'on ne devine pas dans les articles de vulgarisation, et qui valident directement des conseils du playbook :

**1. Le cap de diversité par auteur est mathématique, pas vague.**
Le code applique un multiplicateur à chaque post d'un même auteur dans ton calcul :
```
multiplicateur = (1 - floor) × decay^position + floor
```
`position` = le rang de ce post parmi ceux du même auteur. Donc ton 2e post vu par un même user est multiplié par un facteur < 1, le 3e encore moins, etc. (décroissance géométrique jusqu'à un plancher `floor`). **C'est la preuve chiffrée que poster en rafale se cannibalise.** Espacer, c'est respecter ce decay. Le README le confirme : « Author Diversity Scorer : Attenuate repeated author scores to ensure feed diversity. »

**2. Le hors-réseau est sous-pondéré, sauf si tu colles à un topic.**
Les posts out-of-network (découverte) sont multipliés par un `effective_oon` weight, donc **désavantagés par défaut** face au contenu in-network. Mais le code prévoit une exception nette : si le post matche des topics (`topic_ids` non vide), il utilise `TopicOonWeightFactor` à la place. Traduction : **rester collé à un topic identifiable (search/IA/GEO) améliore mécaniquement ta distribution auprès de gens qui ne te suivent pas.** La cohérence thématique n'est pas un conseil mou, c'est dans la formule. (La découverte elle-même passe par un système à deux tours, User Tower + Candidate Tower, qui matche par similarité d'embeddings : encore une fois, c'est le *sens* de ton contenu qui te place, pas des mots-clés.)

---

## 5. Le temps : décroissance et fenêtre

- **Demi-vie ~6h** : un post perd environ la moitié de son potentiel de visibilité toutes les 6 heures.
- **Fenêtre critique : 30-60 premières minutes.** La vélocité d'engagement précoce déclenche (ou non) la distribution élargie.
- **Seuil 24h** : passé 24h, même un bon post n'a quasi plus de poussée algorithmique.

Implication : tu postes quand ton audience est réveillée, et tu es dispo dans l'heure qui suit pour alimenter la conversation (tes propres réponses aux réponses = tu crées des conversations à double sens, le signal le plus fort).

---

## 6. Ce qui est solide vs ce qui est contesté (anti-tunnel)

Je sépare net, parce que plusieurs sources se contredisent et c'est important de ne pas bâtir une stratégie sur du sable.

**Vérifié directement dans le code source (le plus haut niveau de preuve) :**
- Architecture transformer unique (Phoenix, porté de Grok-1), suppression de toutes les heuristiques, compréhension sémantique du contenu.
- Score = `Σ(poids × P(action))`, avec poids négatifs pour not_interested/block/mute/report/**not_dwelled**.
- Liste réelle des actions scorées (cf. §3), dont `not_dwelled` (négatif) et les partages privés DM/copy-link (positifs distincts).
- **Cap de diversité par auteur = décroissance géométrique** (cf. §4bis) : la rafale se cannibalise, c'est dans la formule.
- **Sous-pondération du hors-réseau sauf match de topic** (cf. §4bis) : la cohérence thématique est dans la formule, pas un conseil mou.
- Vidéo pondérée seulement au-delà d'une durée minimale.
- **Les valeurs des poids ne sont PAS dans le repo** (chargées via feature-switches runtime).

**Solide (recoupé par plusieurs sources indépendantes, hors code) :**
- Hiérarchie conversation > bookmark/dwell > like (cohérent avec le code, mais l'ampleur exacte vient d'estimations).
- Pénalité liens externes dans le corps du post (30-50 %, jusqu'à bien plus en pratique pour les non-Premium).
- Demi-vie ~6h, fenêtre des 30-60 min.
- Ton constructif favorisé, outrage réduit.

**Contesté (les sources ne sont PAS d'accord, à tester toi-même) :**
- **Threads vs posts solo longs.** Certaines sources : threads = 2 à 10x l'engagement. D'autres : posts solo longs battent les threads de 40-60 % en impressions. Verdict : ça dépend probablement de la niche et de l'objectif. À A/B tester sur ton compte.
- **Vidéo vs texte.** « Vidéo native ~10x l'engagement » d'un côté ; « le texte bat la vidéo de 30 % » de l'autre. Contradiction franche. À tester.
- **Les poids chiffrés exacts** (cf. §4) : estimations, pas des chiffres xAI.

Méthode reco : tu prends les points « solides » comme acquis, et tu traites les « contestés » comme des hypothèses à valider avec tes propres analytics sur 3-4 semaines (exactement ta logique de boucle SyntheticBrain : claim, prédiction, mesure).

---

## 7. Ce que l'algo Grok change pour TA stratégie

1. **Écris pour un lecteur, pas pour un algo.** Grok lit comme un humain. Clarté, substance, angle. C'est aligné avec ton anti-IA writing : le contenu vide est détecté.
2. **Provoque la conversation à double sens.** Pose une vraie question, prends position, et réponds à ceux qui répondent. C'est le signal #1, et tu le contrôles.
3. **Vise le bookmark.** Frameworks, checklists, data first-party = contenu « à sauvegarder ». Bookmark ≈ dwell ≈ très fort.
4. **Reste dans ton cluster.** Search/IA/GEO, toujours. La dispersion thématique te coûte mécaniquement de la distribution hors réseau.
5. **Ton constructif > outrage.** Tu peux être tranché sans être combatif. L'autorité pédagogique est exactement ce que Grok pousse.
6. **Zéro hashtag, zéro keyword stuffing.** Inutile, voire contre-productif (signal de spam à l'ancienne).
7. **Lien hors du corps**, toujours (cf. playbook §3).

---

## 8. Bonus : être cité par Grok Search (GEO sur X)

Grok ne fait pas que classer le feed, il répond aussi aux questions des users (Grok Search). C'est un moteur de réponse de plus à optimiser, dans ta logique GEO. Ce qui fait gagner une citation Grok :
- Du contenu **frais, bien sourcé, clairement structuré**.
- Une **présence active de la source sur X même** (Grok valorise l'expertise topique et la participation réelle aux conversations).

Autrement dit : ton activité X nourrit ta visibilité dans Grok Search, et inversement. C'est un argument de plus pour traiter X comme un canal sérieux, pas un à-côté. À creuser comme angle de contenu (« comment se faire citer par Grok »), c'est exactement ta doctrine appliquée à un nouveau moteur.

---

## Sources (audit web, juin 2026)

**Source primaire (code lu directement, juin 2026) :**
- [GitHub - xai-org/x-algorithm (repo officiel)](https://github.com/xai-org/x-algorithm)
- Fichiers lus : `home-mixer/scorers/ranking_scorer.rs` (liste des actions + poids via params + diversité auteur + OON), `weighted_scorer.rs`, `phoenix_scorer.rs`, `README.md`.
- [Elon Musk - "Grok will read every post" (post X)](https://x.com/elonmusk/status/1979217645854511402)

**Open-sourcing & contexte :**
- [Open Source For You - Musk open-sources reco + ad ranking](https://www.opensourceforu.com/2026/01/elon-musk-says-x-will-open-source-full-recommendation-and-ad-ranking-code/)
- [WebProNews - Grok-powered algorithm code exposes viral mechanics](https://www.webpronews.com/x-unveils-grok-powered-algorithm-code-exposing-viral-mechanics/)
- [Social Media Today - X shifting to Grok-powered model](https://www.socialmediatoday.com/news/x-formerly-twitter-switching-to-fully-ai-powered-grok-algorithm/803174/)
- [36kr - Transformer takes over sorting](https://eu.36kr.com/en/p/3647512439918212)

**Décryptage architecture :**
- [PostEverywhere - How the X algorithm works (source code)](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works)
- [singhajit - How X's open source reco algorithm works](https://singhajit.com/system-design/x-twitter-for-you-algorithm/)
- [Medium (Ray Zhao) - Inside X's Grok algorithm](https://medium.com/@yuz88650/inside-xs-grok-algorithm-what-happens-when-a-social-network-thinks-like-an-ai-lab-5e09da575a3d)

**Signaux, poids estimés, contradictions :**
- [OpenTweet - 10 X algorithm secrets 2026](https://opentweet.io/blog/x-algorithm-secrets-2026)
- [OpenTweet - What makes posts go viral (real data)](https://opentweet.io/blog/how-twitter-x-algorithm-works-2026)
- [Postory - X algorithm 2026, what xAI open-sourced](https://postory.io/blog/x-algorithm-2026)

**Grok Search / GEO :**
- [Contently - How to optimize for Grok AI search](https://contently.com/2026/04/30/how-to-optimize-for-grok-ai-search/)
- [Hashmeta - Grok Search on X, how to optimize](https://hashmeta.com/blog/grok-search-on-x-how-to-optimize-for-elons-ai-assistant/)
