# pSEO bxble.com vague 2 : modèles corpus (2026-07-07, soir)

Contexte : vague 1 livrée le jour même (plans 34 pages, différences 8, personnages 36 avec maillage par versets partagés, Bible cliquable en popup sur tous les contenus). Cette recherche identifie la vague suivante, en excluant l'existant (lexique, passage, versets, connexions, exégèses, questions, pensées, plans, différences, personnages) et les modèles écartés par Tim (verset expliqué, « que dit la Bible sur X », Spurgeon FR).

Sondes corpus du jour : « ne crains point » = 26 occurrences réelles dans la Segond, « ne craignez point » = 9, « ne vous effrayez pas » = 3 (le mythe des « 365 ne crains pas » est démontable avec nos comptes) ; lieux abondants (Babylone 267 versets, Sion 167, Samarie 115, Béthel 66, Jéricho 59) ; 1 201 péricopes avec texte_court rempli sur 66 livres (zéro vide).

## N1. Listes bibliques : /liste/[slug]

- Variable : les listes finies que tout le monde cherche. ~25 pages éditoriales : les 12 apôtres, les 10 commandements, les 10 plaies d'Égypte, les 7 paroles de Jésus en croix, les 9 fruits de l'Esprit, les 8 béatitudes, les 12 tribus, les juges d'Israël, les rois d'Israël et de Juda, les 7 Églises de l'Apocalypse, les miracles de Jésus, les paraboles (liste), les femmes de la généalogie de Jésus, les noms de Dieu…
- Template : réponse d'abord (la liste complète, numérotée, avec la référence de chaque élément), puis chaque élément avec son verset cliquable (VerseRef déjà en prod), une note sur les variantes entre passages (les 10 commandements d'Exode 20 et de Deutéronome 5 diffèrent : angle honnêteté), CTA chat.
- Requêtes : « liste des 12 apôtres », « les 10 commandements dans l'ordre », « fruits de l'esprit liste », « 7 paroles de jésus sur la croix », « liste des paraboles de jésus ».
- Test substitution LLM : ChatGPT répond, mais sans les versets sources cliquables ni les variantes entre récits. Position featured snippet et citation IA : c'est le format le plus extractible qui existe.
- Compétition : moyenne (sites bibliques génériques), aucune avec versets sourcés interactifs.

## N2. Combien de fois dans la Bible : /combien/[slug]

- Variable : expressions et mots comptés sur le corpus. ~25 pages : « ne crains pas » (le mythe des 365), amour, prière, pardon, alléluia, amen, grâce, enfer (0, déjà démontré sur /difference), joie, argent…
- Template : la réponse chiffrée en H1-lead (compte exact Segond, méthode dite en une ligne), répartition AT/NT, premier et dernier verset, les occurrences marquantes citées, et le démontage du chiffre qui circule quand il en circule un.
- Requêtes : « combien de fois ne crains pas dans la bible », « 365 fois ne crains rien vrai ou faux », « combien de fois amour dans la bible », « combien de fois amen dans la bible ».
- Test substitution LLM : c'est LE modèle incopiable. Les IA répètent le chiffre légendaire (365) ; personne d'autre ne compte sur un corpus réel. Chaque page est un fact-check citable, exactement la doctrine « directories Data IA » (nourrir l'IA de ce qui lui manque).
- Compétition : quasi nulle en FR avec méthode transparente.
- Note honnêteté : afficher « compté sur la Segond 1910, les totaux varient selon les traductions » (comme sur /difference).

## N3. Résumés par livre : /resume/[livre]

- Variable : les 66 livres. Données : les 1 201 texte_court des péricopes = un résumé par chapitre DÉJÀ rédigé dans le repo, plus difficulte et lecture_minutes.
- Template : « Résumé du livre de [X] chapitre par chapitre » : intro éditoriale courte (auteur présumé, époque, fil du livre, en assumant les incertitudes), puis la liste chapitre par chapitre (texte_court + minutes), temps de lecture total calculé, maillage vers le plan de lecture du thème dominant et les personnages du livre.
- Requêtes : « résumé livre de job », « genèse résumé par chapitre », « livre de ruth résumé », « résumé apocalypse chapitre par chapitre ».
- Test substitution LLM : ChatGPT résume, mais sans structure chapitre par chapitre navigable ni minutes réelles ; fort trafic étudiants/curieux/catéchèse.
- Effort : le plus faible de la vague (le corps des pages existe déjà dans pericopes.json), 66 intros éditoriales à écrire.

## N4. Lieux bibliques : /lieu/[slug]

- Variable : ~20 lieux à forte requête : Jéricho, Babylone, Béthel, Nazareth, Bethléhem, Capernaüm, Sodome, Ninive, Golgotha, Gethsémané, Sion, Samarie, le Jourdain, le Sinaï, l'Éden…
- Template : le moteur personnages réutilisé tel quel : accroche, récit (ce qui s'y est passé, dans l'ordre du canon), comptes réels d'occurrences, « le débat que la Bible ne tranche pas » quand il existe (localisation de l'Éden…), passages clés, en une phrase.
- Maillage croisé automatique avec les personnages : Rahab↔Jéricho, Naomi↔Bethléhem, Zachée et Bartimée↔Jéricho, le moteur de co-occurrence fonctionne déjà entre tout nom scanné.
- Requêtes : « jéricho dans la bible », « où se trouve babylone aujourd'hui », « pourquoi sodome a été détruite », « golgotha signification ».
- Test substitution LLM : risque moyen (l'IA raconte bien) ; l'avantage reste les comptes, les versets cliquables et le maillage.

## N5. Prières de la Bible : /prieres/[slug]

- Variable : ~15 prières nommées : la prière de Jabets (1 Chroniques 4:10, grosse requête héritée du livre de Wilkinson), d'Anne, de Salomon à la dédicace, de Daniel, de Jonas, de Néhémie, le Notre Père, la prière sacerdotale de Jean 17, Gethsémané, le Magnificat…
- Template : le texte complet de la prière (corpus), le contexte en récit court, ce que la prière demande réellement (vs l'usage qu'on en fait : angle anti-contresens validé sur Jérémie 29:11), comment prier avec, CTA chat.
- Requêtes : « prière de jabets », « prière de salomon », « magnificat texte », « prière sacerdotale jean 17 ».
- Test substitution LLM : moyen ; l'angle anti-contresens (Jabets n'est pas une formule de prospérité) fait la différence.

## N6. Paraboles expliquées : /parabole/[slug]

- Variable : ~35 paraboles. Requêtes énormes (« parabole du semeur explication », « fils prodigue signification »).
- Test substitution LLM : le plus risqué de la vague, l'IA explique bien les paraboles célèbres. À ne produire qu'avec l'angle exégèse (contexte, à qui Jésus parle, le détail que tout le monde rate) et en dernier.

## Matrice

| Modèle | Pages | Données | Effort | Impact SEO | Citabilité IA |
|---|---|---|---|---|---|
| N2 Combien de fois | ~25 | comptes corpus, incopiables | faible | moyen | maximale (fact-check chiffré) |
| N1 Listes bibliques | ~25 | corpus complet | faible-moyen | fort (snippets) | forte |
| N3 Résumés par livre | 66 | texte_court déjà rédigé | faible | fort (requêtes scolaires) | moyenne |
| N4 Lieux | ~20 | moteur personnages réutilisé | moyen | moyen | moyenne |
| N5 Prières | ~15 | corpus + éditorial | moyen | moyen | moyenne |
| N6 Paraboles | ~35 | corpus + gros éditorial | fort | fort mais disputé | faible |

## Ordre recommandé

1. N2 Combien de fois (l'actif le plus différenciant : personne d'autre ne compte).
2. N1 Listes bibliques (l'AEO le plus direct).
3. N3 Résumés par livre (le corps des pages existe déjà dans pericopes.json).
4. N4 Lieux (le moteur existe, le maillage personnages↔lieux vient tout seul).
5. N5 puis N6.

Règles transverses inchangées : max 30 % de texte commun par modèle, comptes calculés au build avec garde-fou assertNonEmpty, citations verbatim contrôlées contre le corpus, intertitres spécifiques par page, pas de trait latéral, versets cliquables via VerseRef.
