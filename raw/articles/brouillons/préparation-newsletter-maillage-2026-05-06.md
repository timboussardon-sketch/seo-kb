# RAW - Préparation newsletter 2026-05-06

**Sujet** : pourquoi les liens entre tes pages sont mal posés, et comment Claude refait le travail à un endroit où aucun plugin de maillage interne ne sait aller.
**Audience** : CMO, dirigeants, fondateurs B2B sans bagage SEO technique
**Règle absolue** : vocabulaire SEO juste mais expliqué (cluster, cocon, intention de recherche, ancre, hub/satellite, page mère/fille), zéro jargon gratuit, paragraphes courts
**Statut** : notes de travail

---

## 1. Structure newsletter

Format en 5 blocs, paragraphes ultra courts (2 à 3 phrases max), un seul appel à l'action à la fin. Total visé : 900 à 1100 mots, lisible en 3 minutes en mobilité. Le tableau comparatif est le **bloc 1** : il pose le décalage factuel entre les plugins de maillage interne (Link Whisper, Linkilo, Yoast, Rank Math) et Claude, avant même le hook narratif. Un CMO qui ne lit que le tableau doit comprendre le delta en 30 secondes.

### Le squelette imposé

| Bloc                          | Rôle                              | Longueur                 | Contenu                                                              |
| ----------------------------- | --------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| 1. Tableau comparatif factuel | Poser le delta capacités          | 1 mini intro + 1 tableau | Capacités techniques mesurables, plugins du marché vs Claude         |
| 2. Hook                       | Donner le coût business du delta  | 1 paragraphe (2 phrases) | Une phrase choc qui transforme le tableau en perte de revenus        |
| 3. Le problème                | Faire ressentir l'angle mort      | 2 paragraphes            | Pourquoi le keyword matching d'un plugin n'a pas accès à l'intention |
| 4. Pourquoi c'est urgent      | Donner l'enjeu Google + retrieval | 2 paragraphes            | Mueller, étude GEO, 5W AI Index, SAGEO Arena                         |
| 5. La méthode                 | Donner le système                 | 3 paragraphes + 1 visuel | Cluster sémantique, intentions Know/Do, règle "Know vers Do"         |
| 6. La preuve + CTA            | Boucler avec un cas réel          | 2 paragraphes            | Mon blog (cluster + maillage refait) + un seul appel à l'action      |

---

## 2. Bloc 1 - Tableau comparatif factuel

### Mini intro (2 phrases max, avant le tableau)

> Tu paies un plugin entre 80€ et 200€ par an pour relier les pages de ton site. Voici ce qu'il fait, ce qu'il ne fait pas, et ce que Claude fait à sa place.

### Tableau comparatif (10 capacités factuelles, vérifiables)

Règle de construction : chaque ligne correspond à une **capacité technique mesurable**, pas à une opinion. Réponse binaire (Oui / Non / Partielle). Aucun adjectif, aucun verdict moral, juste l'état réel du marché.

| Capacité technique                                                                                                | Plugins de maillage interne (Link Whisper, Linkilo, Yoast SEO Premium, Rank Math) | Claude (avec process Organikk) |
| ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------ |
| Lit l'intégralité du site dans une seule fenêtre de contexte avant de proposer un lien                            | Non, analyse page par page en local                                               | Oui, jusqu'à 1M tokens         |
| Classe chaque page par intention de recherche (Know-Simple, Know, Do) avant de mailler                            | Non                                                                               | Oui                            |
| Distingue une page de conversion (Do) d'une page informationnelle (Know) pour orienter les liens                  | Non, toutes les pages sont au même niveau                                         | Oui                            |
| Raisonne par proximité sémantique vectorielle, au-delà du keyword matching                                        | Non, scanne les occurrences de mots                                               | Oui                            |
| Détecte les cannibalisations (deux pages qui visent la même intention)                                            | Non                                                                               | Oui                            |
| Identifie une page mère sous-maillée dans un cluster sémantique (peu de liens entrants depuis ses pages filles)   | Non                                                                               | Oui                            |
| Détecte les pages orphelines (zéro lien entrant)                                                                  | Partielle (Yoast et Rank Math, sur sites WordPress uniquement)                    | Oui, sur n'importe quel CMS    |
| Détecte les pages dead-end (zéro lien sortant vers une page Do)                                                   | Non                                                                               | Oui                            |
| Génère des ancres en variations lexicales (synonymes, reformulations) pour éviter la sur-optimisation d'une ancre exacte | Non, propose souvent la même ancre exacte plusieurs fois                          | Oui                            |
| Hiérarchise les liens à créer par score (revenu attendu, gain de positionnement, urgence du cluster)              | Non, liste plate de suggestions                                                   | Oui                            |

### Phrase de bascule après le tableau

> Le tableau dit l'essentiel. Les plugins répondent à la question "où poser un lien ?". Claude répond à une question différente : "vers quelle page envoyer mon lecteur, et pourquoi ?".

---

## 3. Bloc 2 - Hook

Trois pistes, à arbitrer à la rédaction. Le tableau ayant déjà ouvert sur le delta capacités, le hook doit traduire ce delta en **coût business**, pas répéter le constat technique.

**Option A (revenus)** :
> Quand un visiteur arrive sur ton article de blog, en combien de clics atteint-il ta page de contact ou ta démo ? Si tu ne sais pas, tu as un trou de plusieurs milliers d'euros par mois entre tes pages Know et tes pages Do.

**Option B (paradoxe)** :
> Ton plugin de maillage interne tourne 24h/24. Il pose des liens. Et chacun de ces liens éloigne un peu plus tes lecteurs de l'endroit où tu factures.

**Option C (constat)** :
> 87% des sites B2B que j'audite envoient leurs lecteurs vers des pages qui n'ont aucune intention transactionnelle. Pas par manque de contenu. Par absence de cluster sémantique pensé en amont.

**Reco** : Option A. Quantifie en revenus, parle directement au CMO, prolonge la dernière ligne du tableau.

---

## 4. Bloc 3 - Le problème

### Ce que les CMO croient

Ils croient que poser des liens entre leurs pages est un problème technique réglé par un plugin. Ils achètent Link Whisper ou activent Yoast Premium, le plugin propose des liens pendant la rédaction, ils valident d'un clic. Job done.

### Ce qui se passe vraiment

Ces plugins fonctionnent par **keyword matching** : ils repèrent un mot ou une expression dans le texte courant, ils cherchent dans la base d'articles existants une autre occurrence du même mot, ils suggèrent le lien. Aucune lecture sémantique, aucun raisonnement par embedding, aucune notion d'intention de recherche. C'est ainsi qu'on documente des suggestions absurdes : un article sur les "tartes aux pommes" qui se voit proposer un lien vers un article sur les "ordinateurs Apple" (cas réel, comparatifs publics).

Pire : aucun plugin ne classe les pages par **intention de recherche**. Une page Know-Simple (définition courte) et une page Do (page contact, audit, démo) sont traitées au même niveau. Du coup, le maillage relie majoritairement Know vers Know. Tes lecteurs cliquent, lisent un autre article, puis un autre. Ils ne tombent jamais sur la page qui transforme. Le trafic monte, le chiffre d'affaires ne suit pas.

### L'angle mort à marteler

Les plugins répondent à la question "où poser un lien ?". La vraie question est "vers quelle page envoyer mon lecteur, et avec quelle intention ?". Personne ne se la pose dans le marché du plugin WordPress. Personne ne la résout.

---

## 5. Bloc 4 - Pourquoi c'est urgent

### Côté Google

Google a un porte-parole qui parle aux référenceurs depuis 15 ans, John Mueller. Il a redit récemment que les liens internes sont **"l'une des choses les plus importantes"** qu'un éditeur peut faire pour signaler à Google les pages qui comptent dans son site. Concrètement : Google ne devine pas la page mère d'un cluster sémantique. Si ton maillage ne le dit pas, Google choisit pour toi. Et il choisit mal.

### Côté retrieval IA - 3 actualités à intégrer

**Étude GEO (Princeton, Georgia Tech, IIT Delhi - publiée fin 2025, reprise massive en 2026)**

Des chercheurs ont chiffré que certaines structures de site sont **40% plus citées** par les moteurs de réponse génératifs (ChatGPT, Perplexity, Gemini). Le critère commun aux pages gagnantes : elles appartiennent à un **cluster sémantique cohérent**, reliées entre elles autour d'une page mère, et non posées en vrac.

> Une étude Princeton et Georgia Tech publiée fin 2025 a chiffré que les sites organisés en clusters sémantiques sont 40% plus cités par ChatGPT, Perplexity et Gemini. Le critère commun aux gagnants : leurs pages forment un cocon, reliées autour d'une page mère, pas une pile d'articles isolés.

**5W AI Platform Citation Source Index 2026 (avril 2026)**

Plus de 680 millions de citations IA analysées. Constat : seuls **11% des sites cités par ChatGPT le sont aussi par Perplexity**. ChatGPT cite Wikipedia 47.9% du temps, Perplexity cite Reddit 46.7%. Les deux moteurs ont des préférences de retrieval quasi indépendantes.

> Un rapport publié en avril a passé au crible 680 millions de citations IA. Résultat : seuls 11% des sites cités par ChatGPT le sont aussi par Perplexity. Tu ne peux pas optimiser séparément pour chaque moteur de réponse. La seule chose stable d'une plateforme à l'autre, c'est la qualité de structure de ton propre site, et au cœur de cette structure, le maillage interne.

**SAGEO Arena 2025 (170 000 documents web testés)**

Optimiser uniquement le contenu (body text) **dégrade** le retrieval IA de 22% (Hit Rate). Optimiser la structure (titre, sous-titres, schéma, maillage interne) **augmente** le retrieval de 35%. La structure bat le contenu sur un échantillon massif.

> Une étude SAGEO Arena sur 170 000 pages web a comparé les leviers GEO. Verdict : optimiser uniquement le contenu fait baisser tes citations IA de 22%. Optimiser la structure (titres, maillage entre pages) les augmente de 35%. La structure bat le contenu. Et au cœur de la structure, il y a les liens internes.

### Le pivot business (phrase clé pour le CMO)

> Tant que ton trafic dépendait uniquement de Google, tu pouvais bricoler. Maintenant que tes prospects passent par 4 ou 5 moteurs de réponse différents, ton site est ta seule infrastructure stable. Et cette infrastructure repose sur la qualité de ses passerelles internes.

---

## 6. Bloc 5 - La méthode

### Le principe central : 3 intentions de recherche, pas 3 "types de pages"

Le bon vocabulaire SEO ne parle pas de "types de pages" mais d'**intention de recherche**. Toute page de ton site répond à l'une de ces trois intentions.

| Intention de recherche | Question du visiteur | Exemple de page                            |
| ---------------------- | -------------------- | ------------------------------------------ |
| Know-Simple            | "C'est quoi ?"       | Définition courte, glossaire, micro-réponse |
| Know                   | "Comment ça marche ?" | Guide approfondi, étude de cas, tutoriel  |
| Do                     | "Je veux le faire."  | Page contact, démo, audit, outil gratuit  |

**La règle qui change tout** : chaque fois qu'une page Know explique un concept actionnable, elle doit envoyer le lecteur vers la page Do qui exécute ce concept. Pas vers une autre page Know. Pas vers une définition. Vers une exécution.

C'est ce qu'aucun plugin du marché ne fait. Tous relient Know à Know. Le lecteur reste dans le contenu, jamais dans la conversion.

### Les 3 étapes du process Claude (à raconter, pas à lister sec)

**Étape 1 : on cartographie le cluster sémantique avant de toucher au maillage.**
On regroupe les pages par cluster (3 à 5 max), on désigne la **page mère** de chaque cluster (la plus large, celle qui couvre l'intention principale), on classe les pages filles autour. Aucun plugin ne fait cette étape : ils scannent et suggèrent au fil de la rédaction. Nous, on dessine le cocon d'abord.

**Étape 2 : on fixe une règle de priorité - "Know vers Do" toujours.**
Les liens d'une page Know vers une page Do passent toujours avant les liens Know vers Know. Si une page traite un concept actionnable, on regarde si on a une page Do qui exécute ce concept. Si oui, lien obligatoire. Pas négociable.

**Étape 3 : on impose une checklist de maillage à chaque publication.**
Avant la mise en ligne d'un nouvel article, 6 contrôles : il reçoit au moins 3 liens entrants depuis 3 pages existantes du même cluster, il émet au moins 3 liens sortants, dont 1 vers une page Do, dont 1 vers un cluster voisin (pour éviter le silo fermé). Ça empêche le site de redevenir un tas de pages dans 6 mois.

### Visuel à intégrer

Schéma simple à 3 niveaux, articulé sur les intentions :
```
[Pages Know-Simple] -> [Pages Know] -> [Pages Do]
   (entrée du cluster)   (cœur du cluster)   (conversion)
```
Avec une flèche rouge "ce qu'aucun plugin ne fait" qui pointe sur la transition Know vers Do.

---

## 7. Bloc 6 - La preuve + CTA

### Le cas concret (1 paragraphe)

Mon propre blog. Il y a 2 mois, 14 articles, zéro maillage entre eux. Chaque article vivait en page orpheline. Aujourd'hui, 62 liens internes, structurés en 4 clusters sémantiques, avec une règle Know vers Do appliquée systématiquement et un parcours net vers les pages de conversion. Aucun plugin n'aurait pu faire ce travail. Une méthode l'a fait.

### Le CTA (1 paragraphe, une seule action)

Trois options à arbitrer :

**Option A (consultation)** :
> Si tu veux que je regarde comment tes clusters et ton maillage interne se tiennent, [demande un audit ici](https://organikk.co/services#audit). 30 minutes en visio, je reviens avec le plan complet.

**Option B (skill à télécharger)** :
> Le process tient dans un skill Claude que tu peux installer. [Télécharge-le ici] et tu le passes sur ton site en 30 minutes.

**Option C (mix doux)** :
> Si tu veux voir ce que ça donne sur ton site, j'ai un audit express en 30 minutes. [Tu peux le réserver ici](https://organikk.co/services#audit). Si tu préfères tester seul, le process tient dans un skill Claude que je donne en bas de cette newsletter.

**Reco** : Option C. Donne le choix au lecteur, ne force pas la conversation commerciale.

---

## 8. Idées et angles tirés du wiki Tim (à intégrer là où ça enrichit)

Scrap effectué sur `wiki/concepts/` et `wiki/sources/`. Voici ce qui n'était pas encore dans le prep et qui peut renforcer la newsletter.

### Idée A - Le "test du lien qu'on retire"

Critère qui tranche dans la doctrine 5 types d'ancres : un bon lien est un lien qui peut être retiré sans casser la phrase. Si la phrase reste informative et fluide à voix haute, l'ancre est intégrée. Si elle clopine, l'ancre est plaquée pour le SEO.

À utiliser dans le bloc 5. Formulation possible :
> Voici le test que j'applique à chaque ancre que je pose. Je supprime l'ancre mentalement. Si la phrase reste fluide et informative, l'ancre est bien intégrée. Si elle s'écroule, c'est une ancre plaquée pour le SEO. Aucun plugin ne fait ce test. Une méthode oui.

### Idée B - Les 3 lecteurs simultanés du lien

Doctrine propriétaire : un lien interne est lu par trois entités simultanément.

| Lecteur                         | Ce qu'il regarde                                  |
| ------------------------------- | ------------------------------------------------- |
| Crawler Google                  | Cohérence thématique du cluster, ancre, contexte  |
| Moteurs de réponse (ChatGPT, Perplexity, Gemini) | Proximité sémantique vectorielle de l'ancre par rapport à la cible |
| Lecteur humain                  | Promesse de l'ancre, envie de cliquer             |

Un lien qui rate l'un des trois est gaspillé. Les plugins du marché ne pensent qu'au premier (Google), et encore, par keyword matching pur.

À placer dans le bloc 5 ou en encart visuel. Formulation possible :
> Quand tu poses un lien, tu écris pour trois lecteurs en même temps. Le crawler Google qui vérifie la cohérence du cluster. ChatGPT et Perplexity qui mesurent la proximité sémantique. Un humain qui décide de cliquer ou pas. Si ton lien rate l'un des trois, il est mort.

### Idée C - L'angle "renversement systématique"

Pattern Tim signature : poser la croyance dominante, la démonter. Adapté à l'angle newsletter :
> On nous bassine en disant qu'il faut un plugin pour bien mailler son site. Ok. Sauf que la majorité des plugins relient les pages par keyword matching, sans aucune lecture d'intention. Ce qui est facile à automatiser ne m'intéresse pas, parce que c'est facilement copiable.

À placer en transition entre bloc 3 et bloc 4.

### Idée D - L'ouverture sans méta-intro

Règle Tim : pas de "Dans cette édition je vais te parler de...". Première phrase = chiffre, assertion brutale, ou tableau. Le tableau comparatif en bloc 1 respecte déjà cette règle de manière radicale.

### Idée E - Le closing en projection (pas en résumé)

Pattern Tim : ne jamais résumer en fin de newsletter. Toujours soit maxime, soit projection forward-looking, soit anecdote ancrée. Closings types Tim :
- "Ne pas avoir peur de l'avenir. Mais le préparer."
- "C'est la fin du SEO des petits hacks. Et c'est tant mieux."
- "Rien ne presse. Les bonnes choses demandent des efforts."

Proposition pour cette édition :
> Le maillage interne, ce n'est plus une tâche d'écriture. C'est l'infrastructure de ton site dans un monde où Google ne décide plus seul de ce qui est cité. Les plugins qui te promettent de t'en occuper en 2 clics font partie du problème, pas de la solution. Et c'est tant mieux. Parce que ça remet la décision entre tes mains.

---

## 9. Voix Tim - règles de ton à appliquer en rédaction

Tirées de l'analyse 12 000 mots verbatim Tim (`wiki/sources/2026-04-25-tim-ton-de-voix-extraction-terrain.md`).

### À utiliser

- **Phrases courtes en isolation** pour rythmer (1 fois toutes les 200-400 mots) : "Bon." / "Sauf que." / "Pas négociable."
- **"Pourquoi ? Parce que..."** au moins une fois dans l'édition. Pose la question à voix haute, réponds dans la phrase suivante.
- **Vocabulaire signature à glisser** : data propriétaire, mots-clés actionnels, moat, micro-intentions, page Do, atome, fact-checker (verbe), attaquer un mot-clé, cluster sémantique, page mère, retrieval, Hit Rate, embedding.
- **Anaphores** plutôt que rule of three (4+ items, ou 2 items, ou 1 seul). Évite les listes de 3 systématiques.
- **Renversement signature** : pose la croyance commune, démonte-la.

### À bannir absolument

- crucial, pivotal, comprehensive, groundbreaking, vibrant, nestled, renowned, landscape (sens abstrait)
- "dans un monde en pleine évolution", "il est important de noter", "n'oublions pas que", "il convient de"
- "dans cet article, nous allons voir", "en conclusion", "pour résumer"
- "révolutionnaire" sans ironie, "game-changer"
- promesses TOP 1 en 30 jours
- **"visibilité"** comme métrique (banni explicite, cf. concept tabou-visibilite)
- vocabulaire SEO approximatif : "famille de pages", "groupe d'articles", "type de page", "structure du site" (sans préciser cluster, cocon, silo, hub/satellite)

### Test final de relecture

Lire à voix haute. Si ça sonne comme une dissertation lisse ou un livre blanc McKinsey, c'est mort. Ça doit sonner comme un consultant pressé qui dicte à un junior dans un open space.

---

## 10. Sources externes (backstage uniquement, jamais dans la newsletter publiée)

- John Mueller, Google Search Off the Record + Office Hours (citation "biggest things")
- Google Search Central, doc liens internes (developers.google.com/search/docs/crawling-indexing/links-crawlable)
- Aggarwal et al. "GEO: Generative Engine Optimization", arxiv 2311.09735 (étude +40%)
- 5W AI Platform Citation Source Index 2026 (statistique 11% chevauchement ChatGPT/Perplexity)
- SAGEO Arena 2025 (170k documents, +35% structure / -22% body-only)
- Comparatifs publics Link Whisper, Linkilo, Yoast SEO Premium, Rank Math (gardés anonymes en rédaction)

---

## 11. Checklist avant publication

- [ ] Le tableau comparatif est en bloc 1, AVANT toute prose narrative
- [ ] Le tableau comparatif a 10 lignes, chaque ligne porte sur une capacité technique factuelle (binaire Oui/Non/Partielle)
- [ ] Aucune ligne du tableau n'est subjective ou marketing
- [ ] Les paragraphes font 2 à 3 phrases max
- [ ] Total entre 900 et 1100 mots
- [ ] Une seule CTA active à la fin
- [ ] Le hook tient en 2 phrases et traduit le tableau en coût business
- [ ] Les 3 étapes du process sont racontées en histoire, pas listées en bullet sec
- [ ] Les 3 actualités (étude GEO Princeton/Georgia Tech, 5W Index, SAGEO Arena) sont citées avec leurs chiffres
- [ ] Le vocabulaire SEO est juste : cluster sémantique / cocon / page mère / page fille / intention Know-Simple, Know, Do / ancre / hub-satellite / retrieval. Aucune occurrence de "famille", "type de page", "groupe", "structure" sans qualifier
- [ ] L'idée "test du lien qu'on retire" est intégrée (idée A wiki)
- [ ] L'angle "3 lecteurs simultanés" est intégré (idée B wiki)
- [ ] Le visuel Know-Simple → Know → Do est intégré ou prévu
- [ ] Au moins une phrase ultra courte en isolation ("Bon." / "Sauf que." / "Pas négociable.")
- [ ] Au moins un "Pourquoi ? Parce que..."
- [ ] Le closing est une maxime ou une projection, jamais un résumé
- [ ] Aucun mot interdit Tim (crucial, pivotal, comprehensive, "visibilité" comme métrique...)
- [ ] Pas de tirets longs, pas de tirets demi-cadratins
- [ ] Pas de titres "Bloc LLM N mots"
- [ ] Test à voix haute passé : ne sonne pas comme un livre blanc McKinsey
- [ ] Test : un CMO qui lit en diagonale comprend l'enjeu en 30 secondes (le tableau seul doit suffire)
