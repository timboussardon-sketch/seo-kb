---
description: Compile chaque jour la substance des conversations Claude Code (24h, seo-kb + organikk-next) dans raw/journal/YYYY-MM-DD.md — décisions, idées, pivots, questions ouvertes
---

Tu compiles le **journal de bord conversationnel** de Tim pour une journée donnée. À la différence de `/todo` (qui capture les actions) et `/repeats` (qui détecte les rabâchages 30j), tu captures **la substance** : ce qui s'est dit, décidé, exploré, pivoté.

## OBJECTIF

Écrire `raw/journal/YYYY-MM-DD.md` (overwrite si refait pour la même date) avec un compte-rendu structuré des sessions Claude Code des dernières 24h. Cible d'usage : alimenter la mémoire long terme de "l'employé IA" (cf. `wiki/agents/ia-employe.md`) pour qu'il ait une vue d'ensemble de ce qui se passe semaine après semaine.

## ÉTAPE 1 — DÉTERMINER LA FENÊTRE

Date du jour : `date +%Y-%m-%d`. Fenêtre : **dernières 24h** (J-1 à J-0, soit ~24h glissantes par défaut).

Si l'utilisateur passe un argument `$ARGUMENTS` au format `YYYY-MM-DD`, utilise cette date comme jour cible et lis les transcripts modifiés ce jour-là (00:00 à 23:59 UTC).

## ÉTAPE 2 — RÉCUPÉRER LES TRANSCRIPTS

Sources :
- `~/.claude/projects/-Users-timothee-Documents-seo-kb/*.jsonl`
- `~/.claude/projects/-Users-timothee-Documents-organikk-next/*.jsonl`

```bash
find ~/.claude/projects/-Users-timothee-Documents-seo-kb/ ~/.claude/projects/-Users-timothee-Documents-organikk-next/ -name "*.jsonl" -mtime -1 2>/dev/null
```

Si 0 fichier modifié dans la fenêtre, écris dans le fichier de sortie : "Pas de session Claude Code aujourd'hui." et termine.

## ÉTAPE 3 — PARSING DES JSONL

Pour chaque JSONL pertinent :
- Si > 5000 lignes, lis seulement les 2000 dernières.
- Si une session est encore active (mtime < 5 min), ignore les 50 dernières lignes par sécurité.
- Évite de relire un fichier déjà parsé.

Chaque ligne est un objet JSON. Extraire :
- Messages **user** (ce que Tim a demandé / dit)
- Messages **assistant text** (les réponses substantielles, pas les annonces de tool calls)
- Tool calls **Write** / **Edit** : noter `file_path` (artefacts produits)
- Tool calls **Bash** avec `git commit` : noter le message de commit

Ne pas re-citer les contenus longs in extenso. Synthétiser.

## ÉTAPE 4 — EXTRACTION PAR CATÉGORIE

Tu produis 6 sections. Pour chacune, **n'invente jamais** : si rien n'est extractible, écris "Rien d'identifié sur cette fenêtre."

### 4.1 🎯 Sujets traités
Quels chantiers ont été abordés aujourd'hui ? Regroupe par projet/thème (ex: "IA employé", "article cluster X", "audit client Y", "refacto Organikk landing").
Format : `- **[Sujet]** — 1 phrase de contexte (cwd : seo-kb / organikk-next)`

### 4.2 💡 Idées & hypothèses émises
Toute nouvelle idée formulée par Tim ou validée dans la conversation : pistes éditoriales, hypothèses stratégiques, intuitions sur un client, réflexions doctrinales.
Format : `- [Idée en 1 phrase] (origine : Tim / claude / conjoint)`
Tag `(à creuser)` si formulée comme exploration sans décision.

### 4.3 ✅ Décisions prises
Choix tranchés dans la session : "on part sur X", "on abandonne Y", "le brief sera structuré comme Z". Distingue des idées : une décision a un avant/après.
Format : `- **[Décision]** — pourquoi : [raison brève si extractible]`

### 4.4 🔄 Pivots & changements de cap
Moments où Tim (ou la conversation) a changé d'avis sur un sujet. Important pour tracer l'évolution de la doctrine.
Format : `- Sur **[sujet]** : avant on disait X, maintenant on dit Y. Raison : [si extractible]`

### 4.5 ❓ Questions ouvertes
Questions soulevées mais non résolues, choix différés, points qui demandent une recherche ultérieure.
Format : `- [Question] — laissée ouverte pour [raison / quand y revenir]`

### 4.6 📦 Artefacts produits
Fichiers créés ou modifiés via Write/Edit + commits git du jour.
Format :
- **Créés** : `path/to/file.md` — 1 phrase sur le contenu
- **Modifiés** : `path/to/file.md` — 1 phrase sur le changement
- **Commits** : `<hash court>` — message

## ÉTAPE 5 — RÉDACTION DU FICHIER

Écris dans `raw/journal/YYYY-MM-DD.md` (crée le dossier `raw/journal/` s'il n'existe pas) :

```markdown
---
type: journal
title: Journal — YYYY-MM-DD
date: YYYY-MM-DD
tags: [journal, ia-employe, conversations]
status: auto-generated
sessions: N
---

# Journal — YYYY-MM-DD

> Compilé automatiquement depuis les transcripts Claude Code (seo-kb + organikk-next) sur 24h.
> N sessions analysées.

## 🎯 Sujets traités

- **[Sujet 1]** — contexte. (seo-kb)
- **[Sujet 2]** — contexte. (organikk-next)

## 💡 Idées & hypothèses émises

- [Idée 1] (origine : Tim)
- [Idée 2] (origine : claude, à creuser)

## ✅ Décisions prises

- **[Décision 1]** — pourquoi : [raison].
- **[Décision 2]** — pourquoi : [raison].

## 🔄 Pivots & changements de cap

- Sur **[sujet]** : avant on disait X, maintenant on dit Y. Raison : […].

## ❓ Questions ouvertes

- [Question] — à reprendre quand [signal].

## 📦 Artefacts produits

**Créés**
- `path/to/file.md` — 1 phrase
- `path/to/other.md` — 1 phrase

**Modifiés**
- `path/to/file.md` — 1 phrase

**Commits**
- `abc1234` — message commit
- `def5678` — message commit

---

## Liens vers la doctrine
<!-- Si un sujet du jour touche un concept stable, mets un wikilink -->
- [[ia-employe]]

---

*Auto-généré via `/recap-jour`. Pour ajouter du contexte humain, édite à la main — le prochain run préservera tes annotations.*
```

## ÉTAPE 6 — FUSION SI LE FICHIER EXISTE DÉJÀ

Si `raw/journal/YYYY-MM-DD.md` existe (déjà tourné aujourd'hui, ou édité à la main) :
- Lis le fichier existant.
- **Préserve les annotations manuelles de Tim** : tout commentaire qui n'a pas l'air auto-généré, toute note ajoutée sous une section, toute ligne marquée `(manuel)`.
- Réécris avec la nouvelle extraction, en ajoutant les annotations préservées sous chaque section avec un tag `(manuel)`.

## ÉTAPE 7 — RÉPONSE FINALE

Termine au format :

```
Journal du YYYY-MM-DD écrit : raw/journal/YYYY-MM-DD.md

📊 Snapshot :
- N sessions Claude Code parsées (seo-kb : X / organikk-next : Y)
- N sujets, N idées, N décisions, N pivots, N questions ouvertes
- N artefacts produits

🔥 Fait marquant du jour : [le truc le plus important — décision majeure, pivot, ou idée qui mérite d'être creusée]
📌 À reprendre demain : [question ouverte ou chantier non terminé le plus saillant]
```

## CONTRAINTES

- **Langue** : français.
- **Voix** : factuelle, dense, style Tim (cf. `raw/notes/tim-my-voice.md`). Pas de "il convient de", pas de meta-commentaires sur la qualité de la session.
- **Pas d'invention** : si tu n'es pas sûr qu'une décision a été prise, tag `(à valider)`. Si une idée est formulée comme question, classe-la en 4.5, pas en 4.2.
- **Densité** : un journal du jour bien fait fait 200-500 lignes max. Si tu débordes, c'est que tu cites trop. Synthétise.
- **Distinction idée vs décision** : critère = y a-t-il un avant/après actionnable ? Oui = décision, non = idée.
- **Voix passive proscrite** : "Tim a décidé" plutôt que "il a été décidé".
- **Dates absolues** : convertis "demain", "la semaine prochaine" en YYYY-MM-DD.
- **Pas de contenu sensible** : si une session contient des infos client confidentielles (nom + chiffres), résume sans citer (`un client a partagé ses chiffres trafic`, pas `Acme Corp a perdu 30% en avril`).

## NOTES TECHNIQUES

- Si plusieurs sessions tournent en parallèle (plusieurs JSONL actifs), traite-les séparément puis fusionne par sujet à l'étape 4.
- Le `cwd` d'une session se trouve dans le premier message JSONL (champ `cwd` ou `workingDirectory`).
- Si tu identifies une décision qui contredit une note de `wiki/` ou `raw/ia-employe/`, signale-le explicitement dans la section 4.4 (Pivots).
- Pour traçabilité long terme : ne jamais supprimer un journal existant, même s'il est faux. Marque-le `status: corrected` et écris la version juste avec un nouveau timestamp.
