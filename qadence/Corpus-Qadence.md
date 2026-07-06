# Corpus Qadence

Note de doctrine, 6 juillet 2026. Validée en session avec Claude après analyse de bxble et de Fusionn.

## La règle

Je ne crée pas de pages SEO. Je construis les corpus dont l'agent a besoin pour répondre juste, l'agent les lit au moment de répondre, et j'expose ces corpus en pages publiques.

Le SEO est le sous-produit du carburant du produit.

C'est la logique que j'ai déjà appliquée sur bxble sans la formuler. Le bot avait besoin de trouver des versets : j'ai construit la concordance (31 170 versets balayés), elle est devenue les pages Versets par thème. Le bot avait besoin du sens grec et hébreu : j'ai construit le lexique Strong's (13 622 mots), il est devenu les pages Lexique. Le bot avait besoin de relier les passages : les connexions curées sont devenues les pages Connexion.

Fusionn suit la même logique. La page « Liste des mots-clés pour [X] » repose sur un grounding réel (867 requêtes Google Suggest pour consultant SEO, fichier JSON par mot-clé). Le corps de la page, ce sont des tableaux scorés. La prose ne porte rien.

## Pourquoi ça tient

Une page issue d'un corpus est dense par construction. Un rédacteur ou une IA qui « écrit une page » produit du corpus moyen, donc de la commodité, donc rien de payant ni de citable.

Le coût de la page est déjà payé : le corpus était nécessaire au produit.

Le corpus est stable. Une page qui repose sur une donnée périssable meurt avec sa donnée.

Sans data propriétaire, on retombe dans le corpus moyen de Claude. Je le répète depuis le début : la data propriétaire est la matière première, tout le reste est copiable.

## Ce que j'ai rejeté (et pourquoi)

- Guides how-to en prose : du corpus moyen, aucune data, aucune défense.
- Relevés « qui les IA citent sur [sujet] » : coût d'API par formulation et par moteur, et la donnée bouge en quelques semaines. Au mieux une étude ponctuelle datée, jamais un modèle industrialisé.
- Glossaire GEO : tout le monde en a un, l'agent n'en a pas besoin (la doctrine couvre déjà les concepts).
- Archétypes de pages en pages dédiées : personne ne tape « modèle de page comparatif ». Le dataset reste, il nourrit les autres corpus en interne, sans pages.

## Les 5 corpus retenus

| # | Corpus | Ce que l'agent en fait | Pages publiques | Requêtes captées | Taille |
|---|---|---|---|---|---|
| 1 | Lexique des modificateurs d'intention | Classe chaque requête GSC de l'utilisateur par signal (« gratuit », « vs », « avis », « pour [profil] »…) | 1 fiche par modificateur + index | longue traîne par modificateur, « requête transactionnelle » | ~140 fiches, corpus fini |
| 2 | Dictionnaire des métriques GSC | Explique et interprète la donnée sans se tromper (position moyenne pondérée, pièges d'interprétation) | 1 fiche par métrique/rapport | « position moyenne search console », « impressions vs clics » | ~60-80 fiches, fini |
| 3 | Bibliothèque de diagnostics | Le raisonnement de botbeat : symptôme, causes possibles, vérifications, actions | 1 fiche par symptôme | « chute de trafic google », « page pas indexée pourquoi » | ~80-120 fiches, fini |
| 4 | Corpus-sujet | Le paysage d'un sujet avant de conseiller dessus : requêtes réelles (Suggest/PAA), entités des pages qui rankent, structure de SERP | 1 page par sujet | « mots-clés [sujet] », plans de pages | illimité, construit en flux |
| 5 | Benchmarks GSC agrégés | Recommande sur de l'observé : CTR réel par position, effets mesurés des actions sur les sites connectés | 10-15 pages de chiffres | « CTR moyen par position 2026 » | différé, dépend du volume de sites connectés |

Les corpus 1 à 3 sont finis, gratuits, et sortent de ma doctrine et de mes skills sans une seule API.

Le corpus 4 se construit en flux : quand un utilisateur travaille un sujet, l'agent construit le corpus pour lui répondre, on le met en cache, il devient une page. Le travail client paie la page (même mécanique que la concordance bxble).

Le corpus 5 est le seul actif que personne ne peut copier. Anonymisation dès la réception et DPA, comme sur les dashboards clients. On pose le schéma d'agrégation maintenant, on publie quand le volume de sites connectés donne des chiffres solides.

## Le maillage vient tout seul

Une fiche diagnostic pointe une métrique du dictionnaire. Une page sujet classe ses requêtes avec le lexique. Un benchmark chiffre un diagnostic. Cinq corpus, un seul graphe interne (c'est le même effet que Versets vers Lexique sur bxble).

Chaque page se termine par le même renvoi : l'agent fait ça sur ton site, avec ta Search Console.

## Ordre de construction

1. Lexique des modificateurs, côté agent d'abord : dataset + branchement dans la table skills, on vérifie que ses classifications de requêtes s'améliorent. Les pages publiques viennent après validation.
2. Dictionnaire des métriques GSC.
3. Bibliothèque de diagnostics.
4. Corpus-sujet, dès que le pipeline en flux est branché sur l'agent.
5. Schéma d'agrégation des benchmarks posé tôt, publication plus tard.

Maquette de la fiche lexique validée en session (page « gratuit », mise en page une colonne, fiche d'identité, 2 tableaux, erreurs, position signée). La v1 était trop chargée et écrite comme une IA, la v2 corrige.

Liens : [[Journal]], [[Strategie-contenu]], [[Playbook-growth]]
