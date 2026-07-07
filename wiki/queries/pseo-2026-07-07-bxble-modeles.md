# pSEO bxble.com : modèles de pages à créer (2026-07-07)

## Arbitrage Tim (2026-07-07)

Retenus et CONSTRUITS le jour même : M2 (plans de lecture, /plan/, 34 pages), M4 (différences, /difference/, 8 pages), M6 (personnages, /personnage/, 8 pages). Écartés : M1 (verset expliqué), M3 (que dit la Bible sur X), M5 (Spurgeon FR).

Détails d'implémentation : lib/plans-themes.ts (génération depuis les 1 201 péricopes taguées, 12 thèmes éditoriaux, durées bornées par la matière réelle : mariage n'existe qu'en 7 jours), lib/differences.ts + lib/corpus-scan.ts (occurrences comptées sur le corpus au build, garde-fou assertNonEmpty qui casse le build si un radical ne matche rien), lib/personnages.ts (8 figures secondaires, comptes réels du nom). Fait vérifié en construisant : le mot « enfer » n'apparaît pas dans la Segond 1910 (elle écrit « géhenne » et « séjour des morts ») ; la page enfer-et-sejour-des-morts ouvre sur ce fait.

Contexte : bxble.com = chatbot Bible (CTA /chat/) + capture email par lead magnet PDF. Corpus repo : Bible Segond + Martin verset par verset avec embeddings, lexique glosé FR 13 488 mots avec occurrences, 1 201 péricopes, 64 thèmes de versets, graphe intertexte AT→NT, 19 exégèses main, ~890 Ko de Spurgeon traduit FR. Doctrine : le corpus nourrit le bot d'abord, les pages en sont le sous-produit.

Modèles déjà en production (ne pas recréer) : /lexique (13 622), /passage (1 201), /versets (64), /connexion (54), /exegese (19), /questions (29), /pensees (27).

## M1. Verset expliqué : /verset/[reference]

- Variable : la référence (ex. jean-3-16, psaume-23-1, philippiens-4-13).
- Volume cible : 300 à 1 000 pages, bornées aux versets qui cumulent au moins 3 signaux du corpus (thème + intertexte + mots du lexique + péricope). Jamais les 31 000.
- Template : texte Segond ET Martin côte à côte + différences de traduction commentées via le lexique + mots-clés du verset liés vers /lexique + versets liés via embeddings + péricope parente vers /passage + citation Spurgeon si le RAG en trouve une + CTA chat « pose ta question sur ce verset ».
- Requêtes : « jean 3 16 explication », « psaume 23 signification », « philippiens 4 13 que veut dire », « [référence] commentaire ».
- Test substitution LLM : ChatGPT paraphrase le verset mais ne montre ni les deux traductions françaises côte à côte, ni les occurrences réelles des mots, ni le graphe intertexte. La page gagne sur les preuves.
- Anti-cannibalisation : quand une exégèse main existe, la page verset est la fiche courte et pointe vers l'exégèse (canonical distincte, intention distincte : fiche vs étude).
- Compétition : forte sur les 20 versets stars, faible sur la longue traîne des références.

## M2. Plans de lecture : /plan/[theme]-[duree]

- Variable : thème × durée (64 thèmes × 7/21/30 jours), borné aux combinaisons où le corpus fournit assez de péricopes réelles. ~150-200 pages.
- Template : plan jour par jour construit depuis péricopes + versets-thèmes, extrait de chaque passage, PDF téléchargeable contre email (le lead magnet du modèle), CTA chat.
- Requêtes : « plan de lecture bible 30 jours », « lire la bible sur le pardon », « plan lecture biblique débutant », « par où commencer la bible ».
- Test substitution LLM : ChatGPT génère un plan générique ; la page fournit le PDF, les textes intégraux liés, et la progression pensée par péricopes.
- C'est la machine à emails du site. Déjà spécifié dans le skill bxble-directory (modèle Matrix), jamais construit.

## M3. Que dit la Bible sur [thème] : /bible/[theme]

- Variable : les 64 thèmes existants, upgradés de liste brute en page réponse narrative (modèle Narrative du skill bxble-directory).
- Template : réponse directe en tête (answer-first, 150-200 mots ancrés), les versets clés avec les deux traductions, ce que le thème ne dit pas (angle anti-contresens, comme la page Jérémie 29:11), FAQ, CTA chat + PDF du plan M2 correspondant.
- Requêtes : « que dit la bible sur l'argent », « la bible et le divorce », « que dit la bible sur l'anxiété ».
- Test substitution LLM : c'est LE terrain où les IA répondent déjà. La page ne gagne que par la position tranchée, les references précises et le maillage vers les textes. Sans ça, ne pas produire.
- Anti-cannibalisation avec /versets/[theme] : /versets reste la liste, /bible/[theme] devient la réponse ; maillage croisé entre les deux.

## M4. Différence entre [A] et [B] dans la Bible : /difference/[a]-vs-[b]

- Variable : paires de mots du lexique choisies éditorialement. 50 à 100 paires (âme vs esprit, grâce vs miséricorde, péché vs iniquité, crainte vs peur, Sheol vs enfer).
- Template : définition des deux mots depuis le lexique + occurrences chiffrées réelles + versets où les deux apparaissent + nuance Segond/Martin + CTA chat.
- Requêtes : « différence entre âme et esprit bible », « grâce et miséricorde différence », « iniquité définition bible ».
- Test substitution LLM : ChatGPT répond, mais sans les comptes d'occurrences réels ni les versets sourcés en français. Fort potentiel de citation GEO (réponse chiffrée et sourcée).
- Compétition FR : faible.

## M5. Spurgeon en français : /spurgeon/[theme]

- Variable : thème ou verset, croisé avec les ~890 Ko de Spurgeon déjà traduits dans le repo. 40 à 60 pages.
- Template : les passages de Spurgeon sur le thème, sourcés recueil par recueil, reliés aux versets qu'il commente, bio courte, CTA chat.
- Requêtes : « spurgeon citations français », « spurgeon sur la prière », « sermon spurgeon français ».
- Test substitution LLM : les IA citent Spurgeon en anglais ou l'inventent ; le corpus traduit FR est propriétaire. Personne d'autre ne l'a en ligne sous cette forme.
- Volume de recherche modeste, mais zéro concurrence et citabilité GEO maximale (source unique).

## M6. Personnages : /personnage/[nom]

- Variable : personnages bibliques depuis la concordance (occurrences réelles du nom) + péricopes où ils apparaissent. 80 à 150 pages.
- Template : qui il est en 3 phrases, toutes ses apparitions (occurrences chiffrées + liens /passage), sa place dans le graphe intertexte, ce qu'on croit à tort sur lui, CTA chat.
- Requêtes : « qui est melchisédek », « barnabas bible », « qui était la femme de moïse ».
- Test substitution LLM : risque élevé sur les figures majeures (l'IA répond bien) ; ne produire que les personnages secondaires où l'IA est floue et où la concordance donne un avantage réel.

## Matrice de priorisation

| Modèle | Pages | Données dispo | Effort | Impact SEO | Conversion (email/chat) |
|---|---|---|---|---|---|
| M1 Verset expliqué | 300-1000 | totales, déjà en base | moyen | très fort (tête du marché des requêtes Bible FR) | chat |
| M2 Plans de lecture | 150-200 | totales | moyen | moyen | très forte (PDF contre email) |
| M3 Que dit la Bible sur X | 64 | totales | moyen | fort | forte (branche M2) |
| M4 Différence A vs B | 50-100 | totales | faible | moyen | chat |
| M5 Spurgeon FR | 40-60 | totales, propriétaires | faible | modeste | chat, citabilité GEO |
| M6 Personnages | 80-150 | partielles | moyen | moyen | chat |

## Ordre de lancement

1. M1 (le socle de trafic et de maillage : tout le reste s'y accroche).
2. M2 (la capture email, branchée sur M1 et M3).
3. M4 (effort faible, data intégrale, gain GEO rapide).
4. M3 (64 pages, à produire avec position tranchée ou pas du tout).
5. M5 puis M6.

Règles transverses : max 30 % de texte commun entre deux pages d'un même modèle, aucun chiffre inventé (les occurrences viennent du lexique), passage ancré 150-200 mots par page, maillage différencié par page, canonical propre, aucune page sans CTA (chat ou PDF).
