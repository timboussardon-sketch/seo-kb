---
type: revue-presse
title: Algorithme, édition 17 juillet 2026 (local après-midi)
date: 2026-07-17
edition: 2026-07-17-v2
pilier: GEO
status: draft
sources: 11
confidence: medium-high
tags: [revue-presse, algorithme, geo, seo, mesure, chatgpt, arxiv, indexation]
---

# 45 études GEO passées en revue : aucune technique n'a d'effet causal démontré sur le fait d'être retrouvé

## En bref

- Une revue critique de 45 études GEO publiée le 15 juillet conclut qu'aucune technique passée en revue ne montre d'effet causal stable, longitudinal et inter-plateformes sur la découvrabilité organique.
- Les gains du papier fondateur du GEO restent valides dans leur cadre expérimental, mais ils sont conditionnés au fait que la source soit déjà présente dans un contexte fixe. Ils n'établissent donc ni la découvrabilité ni un effet durable sur le trafic.
- Un second preprint, publié le 16 juillet, mesure que la pertinence statique d'un document ne prédit pas son utilité réelle dans une recherche multi-étapes : corrélation de Spearman de -0,026 sur 23 322 observations, soit une indépendance statistique de fait.
- Sur le terrain, deux comptes ChatGPT testés le même mois ne voient pas les mêmes sources de retrieval. Un canal nommé `bing` apparaît chez un compte et jamais chez un autre, à 0 occurrence sur 595 résultats.
- Trois brèves Actualité SEO et IA complètent l'édition : Mueller relie « crawled not indexed » à la qualité du site et non à la technique, Google chiffre à deux semaines le délai de réévaluation d'une canonicalisation, la génération d'images entre dans les AI Overviews.

---

## L'info du jour. Trois publications de la semaine convergent : la mesure GEO n'est pas reproductible (pilier GEO)

Trois documents parus entre le 14 et le 16 juillet 2026 portent sur des objets différents et arrivent au même endroit. Deux sont des preprints arXiv, le troisième est un test réseau conduit par un praticien. Aucun des trois ne dit que le GEO ne sert à rien. Ils disent que ce que le marché mesure aujourd'hui sous le nom de GEO n'est pas ce que le marché croit mesurer.

**Premier document, la revue de 45 études.** Olivier Martinez a soumis le 15 juillet 2026 une revue critique intitulée [Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)](https://arxiv.org/abs/2607.14035), en catégorie Information Retrieval. Le corpus retenu compte 45 études sur une fenêtre de publication de novembre 2023 à juillet 2026.

La thèse centrale est que le GEO n'est pas une tâche de classement unique. C'est un enchaînement stochastique et partiellement observable qui va de l'activation de la recherche au comportement de l'utilisateur, en passant par le crawl, l'indexation, le retrieval, le reranking, l'allocation de contexte, la citation, la proéminence et l'absorption factuelle. Chaque étape a ses propres conditions, et une technique qui agit sur l'une n'agit pas mécaniquement sur les autres.

Trois conclusions sont citables directement depuis le résumé.

- Sur le papier fondateur du GEO, celui dont le marché cite les gains depuis deux ans : « The foundational paper's widely cited gains are valid within its experimental setting but conditional on a source already being present in a fixed context; they establish neither organic discoverability nor durable traffic effects. »
- Sur ce qui marche : « topical relevance and context position are the most reproducible levers », et à l'inverse « generic heuristics transfer poorly », la compétition peut éroder les gains individuels, et surtout « citation-oriented rewrites can impair retrieval ».
- Sur l'état de la preuve : « Within this corpus, the evidence is narrow: already-retrieved content can causally alter its citation or use, but no reviewed technique shows a stable, longitudinal, cross-platform causal effect on organic discoverability or downstream behavior. »

Le résumé ajoute un point qui prend tout son sens plus bas : « Commercial audits further reveal low source overlap, substantial run-to-run variability, and persistent fidelity gaps. »

La lecture honnête est celle-ci. Le GEO sait agir sur un contenu **déjà retrouvé** par le moteur, pour modifier la façon dont il est cité ou utilisé. Il ne sait pas prouver qu'il fait entrer un contenu dans l'ensemble retrouvé. Ce sont deux problèmes distincts, et une partie du marché vend le second en s'appuyant sur les mesures du premier.

**Deuxième document, la pertinence statique ne prédit pas l'utilité réelle.** Debayan Mukhopadhyay, Utshab Kumar Ghosh et Shubham Chatterjee ont soumis le 16 juillet 2026 [Bridge Evidence: Static Retrieval Utility Does Not Predict Causal Utility in Multi-Step Agentic Search](https://arxiv.org/abs/2607.15253). Le protocole est contrefactuel : des agents ReAct traitent 1 000 questions de développement du jeu HotpotQA, puis chaque document consulté est supprimé et les étapes suivantes sont rejouées. On mesure ce qui se casse quand le document disparaît, ce qui donne un score d'utilité causale (CTU) comparé au score d'utilité statique classique (SRU).

Les chiffres, tous vérifiés sur la page primaire.

- La corrélation de Spearman entre utilité causale et utilité statique est de **-0,026** sur 23 322 observations de documents. Autrement dit, les deux grandeurs sont indépendantes.
- **Environ un tiers** des documents réellement utiles à la trajectoire de l'agent paraissent inutiles quand on les note en statique.
- Les documents-pont, ceux qui ne répondent pas à la question mais permettent l'étape suivante, représentent **27,2 pct** du corpus avec des proxys BM25 et cross-encoder.
- Les entités discriminantes réapparaissent dans la requête suivante **4,02 fois plus souvent** que les entités non pertinentes (6,1 pct contre 1,5 pct), sur 227 139 observations d'entités.

La conclusion des auteurs est nette : « Static relevance and causal usefulness are different quantities in agentic retrieval, and optimizing the first does not deliver the second. »

**Troisième document, deux comptes ne voient pas le même moteur.** Suganthan Mohanadasan a publié le 14 juillet 2026 la deuxième partie de son analyse du trafic réseau de ChatGPT, [How ChatGPT picks sources, part 2](https://suganthan.com/blog/how-chatgpt-picks-sources-part-2/). En inspectant le champ `result_source`, il identifie un canal de retrieval qu'il n'avait jamais vu : `bing`.

Le point important n'est pas l'existence du canal, c'est sa distribution. Sur un recensement de ses 30 dernières conversations, soit 595 résultats, il compte `bright` 558 fois, `labrador` 21 fois, `serp` 16 fois, et `bing` exactement 0 fois. Il l'écrit lui-même : « The rollout isn't even being served to my account. » Le canal est réservé à certaines cohortes. David Konitzny, lui, le reproduit sur plusieurs prompts, ce que confirme la reprise de [Search Engine Roundtable du 16 juillet](https://www.seroundtable.com/recap-07-16-2026-41698.html). Trois comptes sont comparés dans le test : un compte gratuit en Italie, un compte Plus aux Émirats, un compte en Allemagne.

Deux précisions que l'auteur donne sur son propre travail méritent d'être reprises, parce qu'elles sont rares dans ce domaine. Le champ `ranking_score` existe dans le pipeline mais « came back null in both my tests ». Et il se corrige publiquement sur sa théorie précédente des tiers de licence : « I over-reached. Real licensing, wrong tier theory. » Les captures de référence datent des 23 et 24 juin 2026, avec un nouveau test le 4 juillet 2026.

**Pourquoi les trois se répondent.** Le survey annonce en toutes lettres que les audits commerciaux révèlent « substantial run-to-run variability ». Suganthan en donne la version observable : la variabilité n'est pas seulement d'un test à l'autre, elle est d'un compte à l'autre, sur le même moteur, à la même période. Le papier sur les documents-pont explique pourquoi une mesure de citation ne suffit pas à décrire ce qui se passe : un tiers de ce qui sert réellement à l'agent ne ressemble pas à ce qu'on note comme pertinent, et n'apparaît nulle part dans une réponse finale.

**Ce que ça change concrètement pour un site.**

Premièrement, un audit GEO conduit depuis un seul compte ne mesure pas un moteur, il mesure un compte. Tant qu'un rapport ne documente pas le compte utilisé, son tier, sa zone géographique et la date de capture, ses résultats ne sont comparables ni à ceux du mois précédent, ni à ceux d'un client voisin. Ce n'est pas un détail de méthode, c'est la condition pour que le chiffre veuille dire quelque chose.

Deuxièmement, la distinction entre « être retrouvé » et « être cité » devient opérationnelle. Une action qui améliore la citation d'un contenu déjà retrouvé est mesurable et documentée. Une action censée faire entrer un contenu dans l'ensemble retrouvé ne dispose, à ce jour, d'aucune preuve causale stable dans la littérature. Un plan GEO qui promet la seconde en s'appuyant sur les chiffres de la première fait une promesse que les 45 études ne portent pas.

Troisièmement, et c'est le point le plus contre-intuitif, réécrire pour la citation peut dégrader le retrieval. Le survey l'écrit, et ça recoupe une mesure que la doctrine porte depuis avril.

**Connexions doctrine.**

La fiche [[concepts/structural-information-geo]] repose sur le benchmark SAGEO Arena, qui mesurait sur 170 000 documents que l'optimisation du seul body text **dégrade** le retrieval (Hit Rate -4,54, et jusqu'à -22,35 sur les réécritures longues de type AutoGEO), alors que l'optimisation des champs structurels le fait progresser (+22 pct de Hit Rate, +35 pct avec ajout de statistiques). La phrase « citation-oriented rewrites can impair retrieval » du survey est une corroboration indépendante de ce finding, arrivée par un autre chemin et sur un autre corpus. Un concept posé en avril tient trois mois plus tard face à une revue de 45 études.

La fiche [[concepts/metriques-visibilite-geo]] listait déjà dans ses limites qu'aucun outil grand public ne calcule ces métriques sur son propre site, et que les métriques 2024-2025 pouvaient évoluer. Elle gagne une limite supplémentaire, plus dure : la mesure doit être **répétée, multi-comptes et datée** pour valoir quelque chose. C'est exactement ce que propose le survey, un protocole reproductible fondé sur des mesures répétées, des paraphrases, des contrôles, une validation humaine et la prise en compte de l'interférence multi-acteurs.

La fiche [[concepts/methode-organikk-4-piliers]] mérite un ajustement à discuter en revue hebdo. Le pilier 4 (AEO) porte aujourd'hui un KPI unique, le taux de citation dans les réponses génératives. Le survey défend un vecteur de visibilité qui sépare quatre grandeurs distinctes : découvrabilité, citation, absorption factuelle, résultat économique. Un taux de citation seul agrège quatre choses qui ne bougent pas ensemble.

**Limites documentaires, à publier en clair.**

- Les deux papiers sont des **preprints non relus par les pairs**. Sur [2607.14035](https://arxiv.org/abs/2607.14035), l'affiliation de l'auteur n'est pas renseignée sur la page arXiv, et il s'agit d'un auteur unique sans double codage annoncé. Il reconnaît lui-même que sa recherche initiale n'a pas conservé le décompte de résultats par base ni un registre d'exclusion complet, et que l'hétérogénéité des tâches empêche d'agréger les gains en pourcentage.
- [2607.15253](https://arxiv.org/abs/2607.15253) tourne sur HotpotQA, un banc de test académique, et pas sur un moteur commercial en production. Transposer ses résultats à ChatGPT ou à AI Mode est une inférence, pas un résultat. Les affiliations des trois auteurs ne sont pas listées sur la page.
- Les chiffres de distribution de Suganthan viennent d'**un seul compte**, il le dit explicitement. La reproduction par David Konitzny est rapportée par Suganthan puis par Search Engine Roundtable, elle ne repose pas sur un protocole partagé et documenté entre les deux testeurs.
- Aucune des trois publications n'a été reprise, à la date de rédaction, par un vendor de mesure GEO qui accepterait d'appliquer le protocole proposé à son propre produit.

**Deux prédictions vérifiables.**

- P-2026-07-17-v2-1 : un vendor de mesure de visibilité IA (Profound, Semrush, Ahrefs, Similarweb, Otterly, Brandi ou équivalent) publie avant le 31 mars 2027 une méthodologie qui documente explicitement le compte de mesure, son tier et sa zone géographique, et qui rapporte une variabilité inter-comptes chiffrée. Résolution positive : documentation publique et datée. Résolution négative : aucun vendor ne publie ces trois éléments d'ici l'échéance.
- P-2026-07-17-v2-2 : le canal de retrieval `bing` dans ChatGPT sort du stade de cohorte et devient observable par défaut sur des comptes de tiers et de zones différents, documenté par au moins deux testeurs indépendants, avant le 31 décembre 2026.

**Lecture opérationnelle** (à considérer comme une lecture, pas comme une consigne définitive).

- Consultants et responsables acquisition : datez et documentez le compte de vos relevés GEO. Un rapport sans compte, tier, géo et date de capture n'est pas comparable dans le temps, et vous ne pourrez pas défendre son évolution devant un client.
- Éditeurs : la priorité mesurable reste la pertinence thématique et la position dans le contexte, les deux leviers que le survey qualifie de plus reproductibles. Les heuristiques générales, elles, se transfèrent mal d'un moteur à l'autre.
- Équipes contenu : avant de réécrire une page « pour être citée », vérifiez que vous ne dégradez pas ce qui la fait retrouver. Le survey et le benchmark SAGEO pointent le même risque depuis deux corpus différents.
- Direction : la question à poser à un prestataire GEO n'est pas « combien de citations ». C'est « est-ce que vous agissez sur du contenu déjà retrouvé, ou est-ce que vous prétendez le faire entrer dans la sélection, et sur quelle preuve ».

---

## Brèves

### B1. Mueller relie « crawled not indexed » à la qualité du site, pas à un problème technique (Actualité SEO)

John Mueller et Martin Splitt ont consacré un épisode du podcast [Search Off the Record](https://developers.google.com/search/podcasts/search-off-the-record) au rapport d'indexation des pages de la Search Console. Barry Schwartz en a rendu compte le 16 juillet sur [Search Engine Roundtable](https://www.seroundtable.com/google-crawled-not-indexed-quality-ai-content-41701.html).

Le point de fond : quand les systèmes de Google détectent un problème de qualité sur un site, ils réduisent le nombre de pages crawlées et indexées, et ces pages ressortent dans le rapport en « discovered not indexed » ou « crawled not indexed ». Mueller ne vise pas le contenu généré par IA en tant que tel. Il vise le contenu générique, sans originalité, que n'importe qui aurait pu écrire, et qui dégrade la qualité perçue du site entier.

Verdict opérationnel : un volume anormal de « crawled currently not indexed » n'est pas une anomalie à corriger URL par URL. C'est un verdict de qualité sur le site, et Mueller invite explicitement à prendre du recul sur la qualité globale plutôt qu'à chercher le correctif technique. Directement opposable à un projet qui veut multiplier les pages générées sans données propres.

Réserve de sourçage : la page Search Engine Roundtable a renvoyé un code 403 à la vérification directe depuis cet environnement. Les verbatims qui circulent sur cet épisode sont attribués à la transcription faite par Search Engine Roundtable, ils n'ont pas été recoupés sur le transcript primaire du podcast. La substance, elle, est corroborée par plusieurs reprises indépendantes.

### B2. Google chiffre à deux semaines le délai de réévaluation d'une canonicalisation (Actualité SEO)

Le [changelog officiel Google Search Central](https://developers.google.com/search/updates) porte une entrée datée du 10 juillet 2026 : « Updated the canonicalization troubleshooting guide with clarifications on re-evaluation time », avec pour raison affichée « To provide better expectations about how long it takes for canonicalization changes to take effect ».

Le chiffre ne figure pas dans le changelog, il figure dans le guide lui-même. La page [Canonicalization troubleshooting](https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting) indique désormais : « Even after fixing content issues, Google might hold pages in a duplicate cluster for up to two weeks. » Et elle pose la condition qui compte : « Pages will generally split out faster if the difference between the new content and the other clustered pages is clear and significant. »

Deux usages concrets. D'abord un délai opposable : après un dédoublonnage, deux semaines sans mouvement relèvent du fonctionnement normal, pas de l'échec. Ensuite une consigne : la sortie du cluster dépend d'une différence claire et significative entre le nouveau contenu et le reste du groupe. Un ensemble de pages programmatiques qui ne fait varier que la variable d'entrée ne remplit pas cette condition et restera groupé.

### B3. La génération d'images entre dans les AI Overviews (IA)

Barry Schwartz a documenté le 14 juillet 2026 sur [Search Engine Land](https://searchengineland.com/google-ai-overviews-now-lets-you-create-image-482163) que Google fait descendre la génération d'images depuis AI Mode vers les AI Overviews, avec son modèle Nano Banana. Citation de Google reprise dans l'article : « To help bring those unique ideas to life, we're bringing image generation directly into AI Overviews in Search ».

Le déploiement est annoncé « over the coming weeks in English », dans toutes les régions qui supportent déjà la création d'images dans AI Mode. L'article ne détaille pas la liste de ces régions et ne dit pas si la France en fait partie. Aucune date de généralisation n'est donnée.

Lecture pour les sites à composante visuelle : Google Images reste un canal d'acquisition résiduel mais réel pour l'e-commerce, la recette, la décoration ou l'immobilier. Si la surface de réponse fabrique l'image à la demande, une image générique indexée perd sa fonction de porte d'entrée. Ce qu'une image générée ne produit pas reste mesurable : la photo du produit réel, du chantier réel, de l'équipe réelle. Aucune donnée publique ne chiffre encore l'effet sur le trafic Google Images, et il est trop tôt pour en produire une.

---

Draft SyntheticBrain, 17 juillet 2026 (local après-midi). Rien n'a été envoyé.
