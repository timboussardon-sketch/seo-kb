---
name: "source-command-todo"
description: "Reconstruit raw/todo/todo-actuelle.md à partir des transcripts Codex locaux (seo-kb + organikk-next, 7 derniers jours)"
---

# source-command-todo

Use this skill when the user asks to run the migrated source command `todo`.

## Command Template

Tu reconstruis la todo de Tim (Timothée Boussardon, consultant SEO/IA) à partir de ses **transcripts Codex locaux**.

## OBJECTIF

Mettre à jour le fichier unique `raw/todo/todo-actuelle.md` (overwrite, pas d'archivage par date) avec un snapshot frais qui distingue :
- ✅ **Fait récemment** (7 derniers jours)
- 🔄 **En cours**
- 📋 **À faire** (priorisé)

## ÉTAPE 1 — RÉCUPÉRER LES TRANSCRIPTS

Les transcripts JSONL Codex sont dans :
- `~/.Codex/projects/-Users-timothee-Documents-seo-kb/*.jsonl`
- `~/.Codex/projects/-Users-timothee-Documents-organikk-next/*.jsonl`

Date du jour : exécute `date +%Y-%m-%d` pour l'obtenir.
Fenêtre : 7 derniers jours (J-7 à J-0).

Liste les fichiers JSONL de ces 2 dossiers et trie par mtime décroissante :

```bash
ls -lt ~/.Codex/projects/-Users-timothee-Documents-seo-kb/*.jsonl ~/.Codex/projects/-Users-timothee-Documents-organikk-next/*.jsonl 2>/dev/null
```

Garde seulement ceux modifiés dans les 7 derniers jours :

```bash
find ~/.Codex/projects/-Users-timothee-Documents-seo-kb/ ~/.Codex/projects/-Users-timothee-Documents-organikk-next/ -name "*.jsonl" -mtime -7 2>/dev/null
```

## ÉTAPE 2 — PARSER CHAQUE TRANSCRIPT

Pour chaque JSONL pertinent, lis-le (Read avec offset/limit si gros — les fichiers peuvent être volumineux). Chaque ligne est un objet JSON (entrée user, message assistant, tool_use, tool_result).

**Extrais 3 catégories d'événements :**

### A) ✅ FAIT (actions complétées)
Signaux dans les messages :
- Tool calls `Write` / `Edit` réussis → fichier créé/modifié
- Tool calls `Bash` avec `git commit` réussis
- Messages assistant qui annoncent une livraison concrète : "j'ai créé X", "j'ai publié Y", "fichier sauvegardé dans..."
- Phrases user qui valident une livraison : "parfait", "ok merci", "tu valides", "ça marche"

Format : `[YYYY-MM-DD] Action concrète (source : seo-kb | organikk-next)`

### B) 🔄 EN COURS
Signaux :
- Sessions ouvertes mais pas explicitement clôturées (dernière entrée user ou assistant sans validation)
- Phrases Tim type : "je vais faire", "je dois finir", "on continue demain", "je reprends ça plus tard"
- Travaux multi-étapes où certaines tâches sont marquées completed mais d'autres pending dans TaskCreate de la session
- Plans validés mais pas encore implémentés

Format : `[démarrée le YYYY-MM-DD] Action en cours — où ça en est`

### C) 📋 À FAIRE (priorisé)
Signaux :
- Tim dit explicitement : "à faire", "TODO", "il faudra", "je dois", "prochaine étape", "rappelle-moi de"
- Fins de session avec "next steps" listés mais non exécutés
- Décisions différées : "on verra plus tard", "pour l'instant on laisse"
- TaskCreate avec status `pending` non clôturées

Format : `- [ ] Action prio N (raison de la prio si déductible)`

**Priorisation des À FAIRE** :
- Prio 1 = mentionnée dans la session la plus récente OU avec deadline proche OU bloque autre chose
- Prio 2 = mentionnée dans plusieurs sessions
- Prio 3 = mentionnée une seule fois, ancienne

## ÉTAPE 3 — FUSION AVEC L'EXISTANT

Lis `raw/todo/todo-actuelle.md` s'il existe.

Logique de fusion :
- **À FAIRE non datés ou plus anciens que la fenêtre 7j mais toujours présents dans le fichier existant** → conserver tels quels (Tim ne les a pas faits, ils restent valides)
- **À FAIRE de l'existant qui apparaissent maintenant dans FAIT** → les déplacer en FAIT (avec la date où ils ont été faits)
- **Annotations manuelles de Tim dans le fichier** (ex: "✅ done manuellement", commentaires) → préserver

Si le fichier n'existe pas, repars de zéro.

## ÉTAPE 4 — RÉDIGER LE FICHIER

Format final, à écrire dans `raw/todo/todo-actuelle.md` (overwrite) :

```markdown
# Todo Tim — MAJ YYYY-MM-DD HH:MM

> Source : transcripts Codex locaux (seo-kb + organikk-next, 7 derniers jours)
> Reconstruit via slash command `/todo`

## ✅ Fait récemment (7 derniers jours)

- [YYYY-MM-DD] Action complétée (source : seo-kb)
- [YYYY-MM-DD] Action complétée (source : organikk-next)
…

## 🔄 En cours

- [démarrée le YYYY-MM-DD] Action en cours — état actuel
…

## 📋 À faire (priorisé)

### Prio 1 (cette semaine)
- [ ] Action prio 1 (raison)
- [ ] Action prio 1 (raison)

### Prio 2 (semaine suivante)
- [ ] Action prio 2

### Prio 3 (backlog)
- [ ] Action prio 3

---

*Si une tâche ici a été faite mais n'apparaît pas dans le ✅ Fait, c'est qu'elle n'est pas mentionnée dans une conversation Codex. Annote manuellement avec `✅ done manuellement YYYY-MM-DD` et le prochain `/todo` la conservera.*
```

## ÉTAPE 5 — RÉPONSE FINALE

Termine ta réponse au format :

```
Todo mise à jour : raw/todo/todo-actuelle.md

📊 Snapshot :
- ✅ N actions faites sur 7 jours
- 🔄 N actions en cours
- 📋 N actions à faire (X prio 1 / Y prio 2 / Z backlog)

🔥 Prio n°1 aujourd'hui : [action la plus urgente]
📌 Point d'attention : [thème récurrent ou projet qui stagne, si détecté]
```

## CONTRAINTES

- **Langue** : français uniquement
- **Ton** : direct, factuel, style Tim (cf. `raw/notes/tim-my-voice.md`). Phrases courtes, zéro bullshit.
- **Pas d'invention** : ne déduis JAMAIS une tâche qui n'est pas explicitement dans les transcripts. Si tu déduis (ex: "brief produit hier → rédaction à prévoir"), précise `(déduit)`.
- **Pas de remplissage** : si une section est vide, écris "Rien d'identifié sur cette fenêtre" plutôt qu'inventer.
- **Dates absolues** : convertis "demain", "la semaine prochaine" en YYYY-MM-DD à partir de la date du jour.
- **Ne propose pas de tâches récurrentes génériques** ("revue de presse", "post LinkedIn") sauf si elles sont explicitement mentionnées dans les transcripts comme dues.

## NOTES TECHNIQUES

- Les JSONL peuvent être très gros. Si > 5000 lignes, lis seulement les 2000 dernières lignes (offset négatif via `wc -l` puis Read avec offset calculé).
- Si une session est encore active (le JSONL est en cours d'écriture), ignore les 50 dernières lignes par sécurité.
- Pour identifier le `cwd` d'une session, regarde le premier message JSONL : il contient souvent un champ `cwd` ou `workingDirectory`.
- Évite de re-lire un même fichier 2 fois.
