# études-IA — pages de données citables par les IA

Troisième modèle de sortie du SyntheticBrain, à côté de `revuedepressIA/` (Algorithme) et `breves-IA/` (les brèves). Ici on produit des **pages de données conçues pour être citées par les moteurs génératifs** (AI Overview, Perplexity, ChatGPT Search) : statistiques sourcées, benchmarks chiffrés, études first-party.

## Les trois formats (gradient de moat)
- **Statistiques** (`seo-page-statistiques`) : agrège des chiffres externes vérifiés. Requête-ancre « [sujet] chiffres / statistiques / taux / % + année ».
- **Benchmark** (`seo-page-benchmark`) : comparaison chiffrée, 1 cellule = 1 valeur sourcée. Requête « [A] vs [B] », « benchmark [catégorie] ».
- **Étude originale** (`seo-page-etude-originale`) : data first-party, le format le moins slop et le plus cité. Requête « étude [sujet] », « [sujet] data ».

Plus c'est first-party, meilleur c'est. Cible : une étude originale au centre qui nourrit des pages stats/benchmark satellites.

## Les trois gates (non négociables)
Chaque page passe trois contrôles distincts, idéalement par une passe séparée du rédacteur :
1. **Anti-hallucination** : chaque chiffre est rouvert à sa **source primaire par fetch** (pas une relecture, pas un agrégateur). Un chiffre non fetché = `[À SOURCER]`. La page n'est pas « prête » tant que 100 % des chiffres ne sont pas vérifiés.
2. **Anti-slop** (`test-substitution-llm`) : si un LLM peut écrire la page de mémoire, c'est du slop. Exiger au moins une transformation (exhaustivité inédite, normalisation, croisement original, ou data propriétaire). L'agrégation seule est tolérée comme coup tactique, étiquetée faible moat ; le moat vient de la couche first-party.
3. **Contre-analyse** : aucune page ne publie un chiffre fort sans sa lecture inverse, sourcée (études contraires, biais de méthode, position des acteurs). Une stat seule = tunnel de confirmation, refus de la gate. Conclure nuancé, jamais en absolu.

Détail dans les skills `~/.claude/skills/seo-page-{statistiques,benchmark,etude-originale}/` (sections Vérification + Gate de publication).

## Convention de fichier
`YYYY-MM-DD-stats|benchmark|etude-<slug>.md`, frontmatter avec `skill`, `sources` (nombre), `status` (draft/vérifié/publiable). Bloc Sources obligatoire en fin (intitulé, organisme, date, URL, date de consultation).

## Éditions produites
| Date | Sujet | Format | Statut |
|---|---|---|---|
| 2026-06-18 | Recherche IA et GEO 2026 (zéro-clic, trafic IA) | statistiques | vérifié + contre-analyse + first-party niveau 1 (CTR par position, vault) ; niveau 2 AIO à faire |
| 2026-06-18 | AI Overviews et impact sur le clic 2026 | statistiques | vérifié + contre-analyse + first-party niveau 1 (CTR par position, vault) ; niveau 2 AIO à faire |
| 2026-06-18 | Adoption de l'IA en entreprise France 2026 | statistiques | INSEE vérifié par fetch ; chiffres TPE/PME (Bpifrance/France Num) en attente (403 au contrôle) ; pas de first-party vault sur le sujet |
| 2026-06-18 | CTR par position sur Google 2026 | statistiques | First Page Sage vérifié + first-party vault (CTR par position, falaise pos 2) + contre-analyse |
| 2026-06-18 | RGPD et sanctions CNIL 2025 | statistiques | CNIL vérifié par fetch (259 décisions, 486,8M€) + contre-analyse ; comparaison 2024 et noms en [À SOURCER] |
| 2026-06-18 | Usage grand public de ChatGPT et assistants IA | statistiques | Pew vérifié par fetch (34% adultes US 2025) + contre-analyse ; chiffre 2026 (44%) et données France en [À SOURCER] |
| 2026-06-19 | Zéro-clic par type de requête 2026 : informationnel vs transactionnel | statistiques | Ahrefs vérifié par fetch (−44,6 % CTR pos1 informationnel, −34,5 % imputable aux résumés IA) + Semrush vérifié (expansion AIO de 91,3 % → 57,1 % informationnel en 10 mois) + first-party vault référencé + contre-analyse ; taux 74 %/31 % par intent en [À SOURCER] |

## Boucle d'apprentissage (à brancher)
Comme les brèves et Algorithme, ces études doivent nourrir la mémoire du SyntheticBrain : `predictions.jsonl` (un chiffre publié = une prédiction datée, résolue plus tard sur la data réelle), `calibration.md` (qualité dans le temps), `questions.md` (ex. quel protocole pour remplir les blocs first-party GSC). Wiring proposé à valider en revue hebdo.

## Point ouvert prioritaire
Les deux études du 2026-06-18 plafonnent en « agrégation vérifiée » tant que le **bloc first-party** (mesure sur les 20+ propriétés GSC) n'est pas rempli. C'est le chantier `project_etudes_originales` et le saut vers le format `seo-page-etude-originale`.
