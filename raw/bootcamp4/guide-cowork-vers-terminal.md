---
type: source
source_type: transcript
title: "Passer de Cowork à Obsidian + Terminal"
aliases: []
tags: []
created: 2026-06-05
updated: 2026-06-05
sources: 0
confidence: medium
status: draft
---

# Passer de Cowork à Obsidian + Terminal

> Guide de migration du [[entities/bootcamp-seo-ia]] ([[offre-bootcamp-seo-ia]]) : on passe de Claude Cowork à [[entities/obsidian]] + Terminal. La logique `raw/` + `wiki/` vient du pattern LLM Wiki de [[entities/karpathy]] ; tenir le vault dans son IDE, c'est [[concepts/obsidian-as-ide]].

Tu changes juste de fenêtre de discussion. Tes skills arrivent avec le kit que tu télécharges, une commande les place au bon endroit, et le terminal les voit. Tu ne touches pas à Cowork.

Compte 15 minutes. Suis les étapes dans l'ordre.

---

## Étape 1 — Récupère ton dossier de travail

Télécharge ton dossier **seo-kit** depuis ton dashboard bootcamp :
https://organikk.co/dashboard-bootcamp-organikk-private-2026/

Dézippe-le dans **`Documents`**, de façon à obtenir `~/Documents/seo-kit` (Windows : `Documents\seo-kit`).
Vérifie qu'à l'intérieur tu as bien les dossiers `raw/`, `wiki/` et `skills/`.

## Étape 2 — Installe Obsidian (pour lire tes notes)

Télécharge-le gratuitement sur **obsidian.md**.
Ouvre-le → **« Open folder as vault »** → choisis ton dossier `Documents/seo-kit`.

## Étape 3 — Installe Node.js (nécessaire pour le terminal)

Va sur **nodejs.org**, télécharge la version **LTS**, installe-la (tu cliques « Suivant » jusqu'au bout).
C'est ce qui permet d'installer Claude Code à l'étape suivante.

## Étape 4 — Installe Claude Code

Ouvre ton **Terminal** (Mac : Spotlight → « Terminal » · Windows : menu Démarrer → « PowerShell »).
Colle cette ligne, puis Entrée :

```
npm install -g @anthropic-ai/claude-code
```

(Bloqué ? Tu m'envoies un MP.)

## Étape 5 — Mets tes skills au bon endroit

Le terminal lit toujours tes skills dans un dossier précis : `.claude/skills`.
On y copie ceux qui sont dans ton kit. Colle **la ligne qui correspond à ton ordi** :

**Mac :**
```bash
mkdir -p ~/.claude && cp -R ~/Documents/seo-kit/skills ~/.claude/skills
```

**Windows (PowerShell) :**
```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude" | Out-Null
Copy-Item -Recurse -Force "$env:USERPROFILE\Documents\seo-kit\skills" "$env:USERPROFILE\.claude\skills"
```

Le dossier doit impérativement s'appeler **`skills`** et se trouver dans **`.claude`**. C'est fait automatiquement par la commande ci-dessus.

## Étape 6 — Crée le fichier CLAUDE.md (la notice que Claude lira tout seul)

Le plus simple, dans **Obsidian** (déjà ouvert sur ton vault) :
crée une nouvelle note à la **racine** de `seo-kit`, nomme-la **`CLAUDE`** (Obsidian ajoute `.md` tout seul), puis colle ce texte en entier :

```
# Méthode de travail : vault raw/ + wiki/

Tu maintiens une base de connaissance personnelle en markdown (pattern « LLM Wiki » de Karpathy).
Si les dossiers `raw/` et `wiki/` n'existent pas encore, crée-les.

## Les deux dossiers
- `raw/` = mes sources brutes (articles, transcripts de calls, notes, idées). Tu LIS raw/, tu ne le modifies JAMAIS. C'est la source de vérité.
- `wiki/` = les notes distillées. C'est TON domaine : tu écris et tu mets à jour ces pages. Moi je les lis, je ne les écris pas.

## Boucle d'ingest (quand je dépose une source et te dis « ingère-la »)
1. Lis la source dans raw/.
2. Résume-moi les points clés.
3. Crée ou mets à jour la page concernée dans wiki/ (résumé, fiche d'entité, concept).
4. Relie les pages avec des wikilinks [[nom-de-page]].
5. Tiens à jour wiki/index.md (catalogue) et wiki/log.md (journal des ajouts).

## Règles
- raw/ est immuable : tu lis, tu n'écris jamais dedans. Tout ce que tu produis va dans wiki/.
- Chaque fichier commence par un frontmatter (title, type, date, tags).
- Une bonne réponse à une question se classe dans wiki/, elle ne meurt pas dans le chat.

Référence : https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
```

Vérifie que le fichier `CLAUDE.md` est bien à la **racine** de `seo-kit` (pas dans un sous-dossier).

## Étape 7 — Lance et vérifie

Dans le terminal, place-toi dans ton dossier puis lance Claude :

```
cd ~/Documents/seo-kit
claude
```

Une fois Claude lancé, tape :

```
/skills
```

Tu vois ta liste de skills → c'est bon, tu es opérationnel. ✅
(Liste vide ? Reprends l'étape 5, le dossier doit s'appeler exactement `skills` dans `.claude`.)

## Étape 8 — Pour relancer une session plus tard

À chaque nouvelle fenêtre de terminal, tu retapes simplement :

```
cd ~/Documents/seo-kit
claude
```

---

## Comment ça marche ?

Ton dossier a deux parties : `raw/` = tes sources brutes (tu y jettes tout), `wiki/` = les notes propres (c'est Claude qui les écrit).
Tu n'as rien à expliquer à Claude : dès que tu lances `claude` dans `seo-kit`, il lit tout seul le `CLAUDE.md`, le mode d'emploi du dossier, et sait déjà comment maintenir `raw/` et `wiki/`.
