---
title: Implémenter le starter kit SEO sous Claude Cowork
bootcamp: 4
jour: J5 (semaine 4)
created: 2026-05-26
public: oui (doc à distribuer aux participants)
---

# Installer ton système SEO IA sous Claude Cowork

Tu reçois le starter kit : mes 9 skills, ma doctrine SEO, mon kit d'accompagnement client, et l'infra d'automatisation. Ce doc te dit comment l'installer chez toi et le faire tourner sous Claude Cowork en moins d'une heure.

Pas de code à écrire. Tu clones, tu remplis 3 fichiers, tu lances.

---

## Avant de commencer, ce qu'il te faut

- [ ] Un abonnement Claude (Pro 20€/mois minimum, Max si tu veux du volume)
- [ ] Claude Desktop installé (claude.ai/download) avec le mode Cowork activé
- [ ] Git installé (pour cloner le repo). Si tu ne sais pas : `git --version` dans ton terminal. Si ça répond, c'est bon.
- [ ] 1 heure devant toi, au calme

Si tu n'as jamais touché un terminal : pas de panique, il y a 4 commandes en tout dans ce doc, copier-coller.

---

## Étape 1 — Récupérer le starter kit

Deux options selon ton niveau.

### Option A, Git (recommandé, tu auras les mises à jour)

```bash
cd ~/Documents
git clone [URL-DU-REPO-STARTER] seo-kit
cd seo-kit
```

### Option B, ZIP (si Git te bloque)

Télécharge le ZIP depuis le Drive bootcamp, dézippe-le dans `~/Documents/seo-kit`.

---

## Étape 2 — Comprendre ce qu'il y a dedans

```
📂 seo-kit/
  ├── .claude/
  │   ├── skills/              → Les 9 skills SEO (le cœur)
  │   ├── commands/            → Slash commands (todo, recap-jour)
  │   ├── scripts/             → Scripts d'indexation du vault
  │   ├── bin/                 → Runners d'automatisation
  │   └── launchd/             → Exemples de crons (macOS)
  ├── AGENTS.md                → L'OS du vault : comment tout s'articule
  ├── wiki/
  │   ├── concepts/            → La doctrine SEO (entités, passage ranking…)
  │   ├── syntheses/           → Les synthèses méthodo
  │   └── entities/            → Les concepts tech (BERT, MIRAS, SGE…)
  └── raw/notes/
      ├── drive-accompagnement/→ Kit d'onboarding client clé en main
      └── contenu-seo/         → Doctrine de production de contenu
```

Le fichier à lire en premier : **`AGENTS.md`**. C'est le mode d'emploi de tout le système.

---

## Étape 3 — Installer les skills

Les skills doivent vivre dans `~/.claude/skills/` (ton dossier Claude global), pas seulement dans le repo. Une commande pour tout copier :

```bash
mkdir -p ~/.claude/skills
cp -R ~/Documents/seo-kit/.claude/skills/* ~/.claude/skills/
```

Vérification : ouvre Claude Code ou Cowork, tape `/`, tu dois voir les skills (seo-preparation-semantique, seo-quick-win, maillage-systeme…) dans la liste.

---

## Étape 4 — Remplir tes 3 fichiers contexte

C'est l'étape qui fait 80 % de la différence. Sans elle, Claude produit du générique. Crée un dossier `contexte/` dans ton workspace et remplis ces 3 fichiers (templates fournis dans `raw/notes/drive-accompagnement/02_Systeme_IA/fichiers-contexte-template.md`).

### `about-me.md`
Ton identité pro : ce que tu fais, pour qui, ton positionnement, tes liens.

### `my-voice.md`
Ton ton de voix : tes principes, ce que tu fais systématiquement, ce que tu ne fais JAMAIS, tes formats. **C'est ce fichier que les skills de rédaction et de revue de presse vont charger.** Prends 1h pour le remplir avec 3 à 5 de tes textes signature comme ancrage.

### `my-rules.md`
Tes règles de travail : sourcing, rédaction, SEO, ta vision, tes priorités.

> Ces 3 fichiers, c'est ce qui transforme "un Claude générique" en "ton employé SEO". Ne les bâcle pas.

---

## Étape 5 — Pointer Cowork sur ton dossier

1. Ouvre Claude Desktop
2. Active le mode Cowork
3. Sélectionne ton dossier de travail (`~/Documents/seo-kit` ou ton repo client)
4. Vérifie que Claude lit bien tes fichiers : demande-lui « résume-moi mon fichier my-voice »

S'il te répond avec TON contenu, c'est bon. S'il invente, c'est qu'il ne lit pas le bon dossier.

---

## Étape 6 — Premier test (un vrai livrable en 5 minutes)

Lance un skill sur une vraie requête de ton métier :

```
/seo-preparation-semantique "ta requête business"
```

Tu dois obtenir : entités sémantiques pondérées, lexique, micro-intentions, score sur 100, correctifs. Si ça tourne, ton système est opérationnel.

Autres premiers tests utiles :
- `/seo-quick-win` (avec un export GSC) → tes pages position 4-12 à corriger
- `/maillage-systeme` → ton plan de maillage interne

---

## Étape 7 — Automatiser (optionnel mais puissant)

Pour qu'un skill tourne tout seul (ex. la revue de presse chaque matin) :

1. Tape `/schedule` dans Claude Code
2. Crée une routine : cron `0 7 * * 1-5`, ton repo, prompt `/revue-presse-bootcamp`
3. Active

La routine tourne sur l'infra Anthropic, machine fermée. Tu démarres ta journée avec le livrable déjà prêt.

---

## Si tu bloques

- **Les skills n'apparaissent pas** → vérifie qu'ils sont bien dans `~/.claude/skills/` (étape 3), pas seulement dans le repo.
- **Claude n'a pas ta voix** → vérifie que Cowork pointe sur le bon dossier (étape 5) et que `my-voice.md` est rempli.
- **Tu es sur Windows** → les chemins `~/` deviennent `C:\Users\toi\`, les commandes `cp -R` deviennent `xcopy`. MP sur le WhatsApp bootcamp, on t'aide.
- **Reste bloqué** → WhatsApp Tim, ne perds pas 2h seul là-dessus.

---

## Ce que tu NE reçois PAS dans ce kit (et pourquoi)

Pour des raisons de confidentialité, le kit ne contient pas mes données clients, mes calls de découverte, ni mes propositions commerciales. Tu reçois la **méthode** (skills, doctrine, templates, automatisation), pas mes données privées. C'est la méthode qui se reproduit chez tes clients, pas mes données.

---

*Doc d'implémentation Cowork, Bootcamp 4. À distribuer aux participants via le Drive. Timothée Boussardon, mai 2026.*
