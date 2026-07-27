# Questions & diffs proposes - health

LA SEULE PORTE par laquelle la boucle touche au CODE. Le brain n'edite jamais son skill tout seul :
il ecrit ici un diff propose + la raison, Tim tranche a la revue.

## En attente de decision

### 2026-06-22 — linkedin-journal muette depuis sa creation (relance)
Question deja posee le 2026-06-15, toujours sans reponse. `loops/linkedin-journal` reste muet (0 run, brain cree 2026-06-12, 10 jours). Si aucun trigger n'est cable cette semaine, proposer d'archiver le brain en `loops/_archive/linkedin-journal/` pour ne plus polluer le health check. Tim tranche.

### 2026-06-22 — cadence reelle de loops/seo-quick-win
`manifest.yml` declare `cadence: hebdomadaire`, mais le dernier run est 2026-06-11 (J+11). C'est un skill manuel (`/seo-quick-win` sur un export GSC fourni par Tim). Diff propose : passer la cadence a `a-la-demande` pour refleter l'usage reel, ou planifier un creneau hebdo dans le rituel pour le declencher. Tim tranche.

### 2026-06-15 — cadence pour content-brain/*
Le schema v1 de `content-brain/_template/manifest.yml` n'a pas de champ `cadence` (calque agent-synthetic v2 qui en manque aussi). Resultat : impossible de detecter une boucle muette au niveau d'un brain client (ex. golfiller dernier run J+5). Diff propose : ajouter `cadence: a-la-demande` par defaut dans `_template/manifest.yml`, et au cas par cas dans chaque brain client (golfiller = hebdomadaire ? mensuelle ?). Raison : sans cadence declaree, la routine health n'a pas de baseline pour alerter. Tim tranche.

### 2026-06-15 — trigger linkedin-journal
`loops/linkedin-journal` cadence=quotidienne, 0 run depuis sa creation 2026-06-12. Le brain est instrumente (ledgers vides + manifest + memory) mais aucun cron ni hook ne le declenche. Question : faut-il un workflow GitHub Actions ou un LaunchAgent ? Tim tranche.

### 2026-07-27 — agent-synthetic : phase resolution des predictions (relance escalade)
Proposition posee dans `loops/health/ledgers/mistakes.jsonl` 2026-07-20 : ajouter au run quotidien de `agent-synthetic` une phase qui checke les `resolve_by` echues la veille et met a jour le statut. 7 jours plus tard, les 5 predictions overdue sont toujours la avec retard accru (P-2026-06-01-1 passee de J+20 a J+27). Aucune question equivalente dans `agent-synthetic/memory/questions.md` — la proposition ne remonte pas au bon endroit. Diff propose : (a) porter cette proposition dans `agent-synthetic/memory/questions.md` cette semaine pour que le brain la lise a chaque run ; (b) sans phase resolution, la dette de predictions continuera de croitre et `eval_health` restera ESCALATE indefiniment. Tim tranche : phase resolution ou renoncement a la mesure des predictions ?

### 2026-07-27 — golfiller : trancher les predictions sans data
`content-brain/golfiller` P-golfiller-2026-06-03-1 overdue J+24, dernier export GSC golfiller J+47. 3e semaine consecutive d'alerte. Diff propose : formaliser dans le manifest `content-brain/_template/manifest.yml` une regle "une prediction sans mesure a J+30 apres resolve_by passe automatiquement en `miss` avec constat `data non collectee`". Sinon les predictions non mesurees s'accumulent en dette et polluent `eval_health` sans jamais se resoudre. Tim tranche.

## Tranche (historique)
- (rien pour l'instant)
