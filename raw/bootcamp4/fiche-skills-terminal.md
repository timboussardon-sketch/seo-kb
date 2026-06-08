---
type: source
source_type: transcript
title: "Fiche : faire voir tes skills au Terminal (Claude Code)"
aliases: []
tags: []
created: 2026-06-05
updated: 2026-06-05
sources: 0
confidence: medium
status: draft
---

# Fiche : faire voir tes skills au Terminal (Claude Code)

_Bootcamp SEO #4 · pour Cowork (app de bureau) + Terminal (Claude Code)_

> Fiche pédagogique du [[entities/bootcamp-seo-ia]] ([[offre-bootcamp-seo-ia]]). Le passage au terminal + [[entities/obsidian]] est la brique technique du système ([[concepts/obsidian-as-ide]]).

## Le principe en 2 phrases

Tes skills doivent vivre dans **un seul dossier**. On fait ensuite un raccourci spécial (un « lien symbolique ») pour que le Terminal et Cowork regardent tous les deux ce même dossier. Tu ajoutes un skill une fois, les deux le voient. Tu n'installes jamais rien deux fois.

## Pourquoi tu es bloqué·e

- Le **Terminal** (Claude Code) cherche tes skills dans un dossier précis : `.claude/skills` à la racine de ton profil.
- **Cowork** range les siens ailleurs (son dossier de travail, ou un dossier enfoui dans AppData).
- Les deux ne se parlent pas. Donc le Terminal affiche « aucun skill ».

On va relier les deux. Une seule fois.

---

## 🍏 Si tu es sur Mac

1. Ouvre l'app **Terminal** (Spotlight → tape « Terminal »).
2. Choisis ton dossier maître de skills. Si tes skills sont déjà dans un dossier Cowork, repère son chemin. Sinon on part du classique `~/Documents/Cowork/Skills`.
3. Si un dossier `.claude/skills` existe déjà, on le met de côté (sécurité) :
   ```bash
   mv ~/.claude/skills ~/.claude/skills-ancien 2>/dev/null
   ```
4. On crée le lien (remplace le chemin par celui de ton vrai dossier de skills) :
   ```bash
   ln -s ~/Documents/Cowork/Skills ~/.claude/skills
   ```
5. On vérifie que ça pointe bien :
   ```bash
   ls ~/.claude/skills
   ```
   Tu dois voir la liste de tes dossiers de skills. ✅

---

## 🪟 Si tu es sur Windows

1. Repère d'abord OÙ sont tes skills aujourd'hui (souvent `C:\Users\TonNom\Documents\Cowork\Skills`). Note ce chemin.
2. Affiche les dossiers cachés : dans l'Explorateur, onglet **Affichage → Éléments masqués** (coché). Sinon tu ne verras jamais le dossier `.claude`.
3. Ouvre **PowerShell en administrateur** : menu Démarrer → tape « PowerShell » → clic droit → **Exécuter en tant qu'administrateur**. (L'étape admin est obligatoire pour créer le lien, c'est une seule fois.)
4. Si un dossier `.claude\skills` existe déjà, on le met de côté :
   ```powershell
   Rename-Item "$env:USERPROFILE\.claude\skills" "skills-ancien" -ErrorAction SilentlyContinue
   ```
5. On crée le lien (remplace le chemin après `-Target` par celui de ton vrai dossier de skills) :
   ```powershell
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills" -Target "$env:USERPROFILE\Documents\Cowork\Skills"
   ```
6. On vérifie :
   ```powershell
   dir "$env:USERPROFILE\.claude\skills"
   ```
   Tu dois voir tes dossiers de skills. ✅

> Si PowerShell refuse, active le **Mode développeur** : Paramètres → Confidentialité et sécurité → Pour les développeurs → activer « Mode développeur », puis recommence l'étape 5.

---

## Vérifier que tout marche

1. Ferme et rouvre ton Terminal / Claude Code.
2. Demande simplement : « **Quels skills as-tu à disposition ?** » ou lance un de tes skills.
3. Si Claude les liste et qu'un skill écrit bien dans ton `/wiki` et met à jour ton index, c'est gagné.

## Détail important : le projet doit pointer au bon endroit

Le lien règle l'EMPLACEMENT des skills. Pour qu'un skill agisse dans ton projet (écrire dans `/wiki`, mettre à jour `index.md` et les logs), ton fichier **`CLAUDE.md`** du projet doit indiquer le bon dossier de travail. Si un skill « tourne » mais n'écrit nulle part, c'est le `CLAUDE.md` qu'il faut ajuster, pas le lien.

## La règle à retenir

- Le Terminal lit toujours `.claude/skills`. Toujours.
- Un seul dossier maître de skills. L'autre emplacement n'est qu'un raccourci vers lui.
- Nouvel ajout de skill → tu le poses dans le dossier maître, et c'est tout.

---

## Cas à part : Google Drive (le bug de dossier « vide »)

Si Cowork dit que ton dossier de travail est vide alors que les fichiers sont là, et que ton dossier est dans Google Drive : le problème, c'est que Google Drive en mode **« Stream »** monte un lecteur virtuel (`G:`) que le bac à sable de Cowork ne sait pas lire.

Solution : dans les réglages de Google Drive, passe de **« Diffuser les fichiers »** à **« Reproduire les fichiers » (Mirror)**. Ça crée un vrai dossier local synchronisé au lieu d'un lecteur virtuel. Ou plus simple : garde ton dossier de travail **hors** de Google Drive. (OneDrive marchait parce qu'il utilise un vrai dossier, pas un lecteur monté.)
