---
name: "source-command-repeats"
description: "Détecte les décisions/sujets/positions que Tim rabâche dans ses sessions Codex (30 derniers jours) et propose une formalisation"
---

# source-command-repeats

Use this skill when the user asks to run the migrated source command `repeats`.

## Command Template

Tu détectes les **patterns cognitifs récurrents** de Tim dans ses conversations Codex locales. Objectif : identifier ce qu'il rabâche pour le **formaliser** (concept wiki, entité, règle AGENTS.md, ou skill) — au lieu de le re-expliquer à chaque session.

## OBJECTIF

Réduire la charge cognitive en transformant les arguments / positions / décisions répétés en **artefacts persistants** dans le vault.

## ENTRÉE

Transcripts JSONL Codex de Tim sur les 30 derniers jours :
- `~/.Codex/projects/-Users-timothee-Documents-seo-kb/*.jsonl`
- `~/.Codex/projects/-Users-timothee-Documents-organikk-next/*.jsonl`

## ÉTAPE 1 — RÉCUPÉRATION DES TRANSCRIPTS

Date du jour : `date +%Y-%m-%d`. Fenêtre : 30 derniers jours.

```bash
find ~/.Codex/projects/-Users-timothee-Documents-seo-kb/ ~/.Codex/projects/-Users-timothee-Documents-organikk-next/ -name "*.jsonl" -mtime -30 -type f
```

Liste les fichiers, taille, mtime. Si > 20 fichiers, prends les 20 plus récents.

## ÉTAPE 2 — EXTRACTION DES MESSAGES TIM

Pour chaque JSONL, extrais uniquement les **messages user** (entrées de Tim, pas les réponses assistant). Chaque ligne JSONL est un objet ; les messages user ont `"type": "user"` ou `"role": "user"` (le format peut varier selon la version Codex — sois flexible).

Exclus :
- Les messages courts (< 30 caractères) : "ok", "merci", "go"
- Les messages qui sont juste des outputs de tool (pas du texte Tim)
- Les system reminders et messages techniques

Pour gérer les fichiers volumineux, lis chaque JSONL avec Read. Si > 5000 lignes, focus sur les 2000 dernières.

## ÉTAPE 3 — DÉTECTION DES PATTERNS RÉCURRENTS

Tu cherches des **patterns cognitifs**, pas juste des mots-clés. 6 catégories à scanner :

### A) Positions doctrinales répétées
Phrases qui expriment une opinion forte, qui reviennent dans plusieurs sessions sous des formes proches.
**Exemple** : Tim dit dans 3 sessions différentes que "le netlinking est mort" / "les backlinks ne valent plus rien" / "Google a downgradé les backlinks". → Pattern doctrinal.

### B) Arguments réutilisés (verbatim ou paraphrase)
Phrases-types qu'il sort souvent : "le vrai sujet c'est…", "ça confirme ce que je dis depuis…", "ne pas avoir peur de l'avenir mais le préparer".
Si une formule apparaît 3+ fois → candidate à intégrer dans `raw/notes/tim-my-voice.md`.

### C) Refus / corrections récurrents
Tim corrige Codex sur le même point dans plusieurs sessions.
**Exemple** : "non pas comme ça, je veux X" — si X revient 3 fois → règle AGENTS.md à fixer.

### D) Concepts cités sans page wiki
Termes techniques que Tim mentionne récurremment mais qui n'existent pas encore dans `wiki/concepts/` ou `wiki/entities/`.
**Exemple** : Tim parle souvent de "Surprise Score" mais aucun `wiki/concepts/surprise-score.md`.

### E) Process répétés
Suite d'étapes que Tim demande systématiquement dans le même ordre.
**Exemple** : "extrait les chiffres → cite la source → ajoute un aparté → résume en 1 ligne". → Candidat à un skill.

### F) Décisions stratégiques répétées
Choix business / orientation produit qui reviennent (ex: "on va sur l'AEO pas le SEO classique", "Organikk se positionne sur les outils, pas l'audit").

## ÉTAPE 4 — SCORING

Pour chaque pattern détecté, attribue :
- **Occurrences** : N fois sur 30 jours
- **Catégorie** : A/B/C/D/E/F
- **Status existant** : déjà formalisé dans le vault ? (cherche le slug correspondant dans `wiki/concepts/`, `wiki/entities/`, `raw/notes/tim-my-voice.md`, racines `AGENTS.md` du projet et `~/.Codex/AGENTS.md`)
- **Type de formalisation suggérée** :
  - A → `wiki/concepts/<slug>.md` (page concept doctrinal)
  - B → ajout dans `raw/notes/tim-my-voice.md`
  - C → règle dans `AGENTS.md` (projet ou global)
  - D → `wiki/concepts/<slug>.md` ou `wiki/entities/<slug>.md`
  - E → nouveau skill dans `.Codex/skills/<nom>/SKILL.md` ou `~/.Codex/skills/`
  - F → `wiki/decisions/<slug>.md` (créer le dossier si absent) ou ajout à `wiki/syntheses/tim-profil-doctrine.md`

**Filtre** : ne garde que les patterns avec **3+ occurrences**. En dessous, c'est du bruit.

## ÉTAPE 5 — RÉDACTION DU RAPPORT

Output : `wiki/syntheses/decisions-repetees.md` (overwrite — l'historique est dans git).

```markdown
---
type: synthese
title: Décisions et patterns répétés — MAJ YYYY-MM-DD
date: YYYY-MM-DD
window: 30 derniers jours
tags: [synthese, meta, decisions-repetees, formalisation]
status: report
---

# Décisions et patterns répétés — MAJ YYYY-MM-DD

> Ce que tu rabâches dans tes sessions Codex. Candidats à formaliser pour ne plus avoir à le re-expliquer.
> Source : N transcripts Codex (seo-kb + organikk-next, fenêtre 30j)

## 🎯 À formaliser en priorité (top 5)

### 1. [Pattern court 1 phrase]
- **Catégorie** : A — Position doctrinale
- **Occurrences** : N fois (sessions du YYYY-MM-DD au YYYY-MM-DD)
- **Verbatims** :
  > "extrait court 1" *(YYYY-MM-DD, projet seo-kb)*
  > "extrait court 2" *(YYYY-MM-DD, projet organikk-next)*
  > "extrait court 3" *(YYYY-MM-DD, projet seo-kb)*
- **Status** : non formalisé — pas de `wiki/concepts/<slug>.md` correspondant
- **Action suggérée** : créer `wiki/concepts/<slug>.md` avec le pattern doctrinal extrait

### 2. [Pattern 2]
…

(jusqu'à 5)

## 📋 Autres patterns détectés (3-5 occurrences)

### [Pattern]
- **Catégorie** : [B/C/D/E/F]
- **Occurrences** : N
- **Verbatim type** : "..."
- **Action suggérée** : [type de formalisation]

(liste les autres, format compressé)

## ✅ Patterns déjà formalisés (récents)

Patterns qui apparaissent souvent ET qui ont déjà un artefact dans le vault. Pas d'action, juste un tracking de cohérence.

- [Pattern] → déjà dans `wiki/concepts/<slug>.md`
- [Pattern] → déjà dans `raw/notes/tim-my-voice.md`

## 🚨 Contradictions détectées

Si Tim a dit X dans une session et l'inverse dans une autre, signale-le ici. Ce sont les zones où sa pensée évolue et qui méritent d'être tranchées.

- [YYYY-MM-DD] "position A" *vs* [YYYY-MM-DD] "position contraire" — contexte : [thème commun]

(si rien : "Pas de contradiction notable.")

---

## Synthèse

- **N patterns détectés** au total (3+ occurrences)
- **K à formaliser en priorité** (catégorie A/D/E)
- **Top action recommandée** : [phrase actionnable]

---

*Rapport régénéré à la demande via `/repeats`. L'historique est dans `git log wiki/syntheses/decisions-repetees.md`.*
```

## ÉTAPE 6 — RÉPONSE FINALE

Termine ta réponse par :

```
Décisions répétées : N patterns détectés sur 30 jours, K à formaliser en priorité.

🎯 Top action : [phrase actionnable la plus urgente]
🔥 Pattern n°1 : [titre court] — N occurrences
🚨 Contradiction critique : [si détectée, sinon "aucune"]
```

## CONTRAINTES

- **Voix Tim** : factuel, direct, pas de "il convient", pas de superlatifs.
- **Pas d'invention** : si tu ne trouves pas 3 occurrences, n'invente pas un pattern.
- **Verbatims courts** : 1-2 phrases max par citation, sinon ça noie le rapport.
- **Anonymisation** : si un nom de client apparaît dans un verbatim, remplace par `[client]`.
- **Privacy** : ne cite jamais des credentials, des chemins de secrets, des mots de passe qui apparaitraient dans les transcripts.
- **Performance** : si plus de 50 patterns détectés, garde les top 20 par occurrences.
