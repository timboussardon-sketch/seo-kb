---
title: "Installer le bundle skills complet (S4 J5 vendredi)"
bootcamp: 4
semaine: 4
jour: 5
type: install-procedure
usage: "Bundle Drive S4 J5. ZIP unique téléchargé depuis le Drive, contient tous les skills SEO du bootcamp. Remplace les bundles skill par skill des semaines précédentes."
related:
  - "[[sequencage-semaine-4]]"
  - "[[skills-checklist-bootcamp4]]"
  - "[[skill-indexation-check-cowork]]"
  - "[[observations-whatsapp-bootcamp]]"
---

# Installer le bundle skills complet (vendredi S4 J5)

Salut à tous,

Pour le call de vendredi, j'envoie sur le Drive un **ZIP unique** qui contient tous les skills SEO du bootcamp. Plus de copier-coller skill par skill, plus de "j'ai loupé le bundle de la semaine 2" : tu télécharges un fichier, tu l'extrais dans ton dossier des skills, et tu as tout.

Le ZIP s'appelle `tim-claude-skills-YYYY-MM-DD.zip` (la date du dernier export). Quand je le mets à jour, j'en repousse une nouvelle version sur le Drive avec la nouvelle date dans le nom. Tu sais toujours laquelle est la plus récente.

## Ce que contient le ZIP

Tous les skills travaillés pendant le bootcamp dans un seul dossier :
- Le pack des 9 (S1)
- Tous les hors pack des S2, S3, S4 (`seo-donnees-structurees`, `seo-core-web-vitals`, le workflow mots-clés, `audit-engine-pipeline`, `seo-roadmap-pseo`)
- Les bonus (`seo-product-led-seo`, `seo-peurs-objections`, `seo-modeles-pseo`)

Tu peux choisir de tout prendre, ou ne piocher que ce qui te sert pour ton client. C'est ton dossier, tu fais ce que tu veux. Mais le plus simple est de tout coller : Claude ne déclenche un skill que si tu prononces ses mots de déclenchement, donc avoir 21 skills installés au lieu de 9 ne ralentit rien et ne pollue pas tes conversations.

---

## Installation Mac

### Étape 1 — Télécharger le ZIP

Sur le Drive bootcamp, ouvre le dossier `S4 J5 — Bundle skills complet`. Clique-droit sur `tim-claude-skills-YYYY-MM-DD.zip` → **Télécharger**. Le fichier arrive dans Téléchargements.

### Étape 2 — Décompresser

Double-clic sur le ZIP. Le Finder crée le dossier `tim-claude-skills/` à côté. Ouvre-le, tu y vois tous les skills, un sous-dossier par skill.

### Étape 3 — Ouvrir ton dossier des skills

Dans le Finder, fais **Aller → Aller au dossier** (raccourci `Cmd + Maj + G`). Tape : `~/.claude/skills/` et valide. Le Finder ouvre le dossier.

S'il n'existe pas, le Finder le dit. Crée-le : `Cmd + Maj + G`, tape `~/.claude/`, valide, puis dans le dossier `.claude` clique-droit → Nouveau dossier → nomme-le `skills`.

### Étape 4 — Glisser le contenu

Sélectionne tous les sous-dossiers depuis `tim-claude-skills/` (les dossiers qui commencent par `seo-`, `article-`, `audit-`, `indexation-`, `maillage-`). Glisse-les dans `~/.claude/skills/`.

Si le Finder demande "voulez-vous remplacer ?", clique **Remplacer**. C'est normal : la nouvelle version écrase l'ancienne, c'est exactement ce qu'on veut.

### Étape 5 — Relancer Claude et vérifier

Quitte complètement Claude (Cowork ou Claude Code, peu importe lequel tu utilises). Pas juste recharger l'onglet : sortir et relancer.

Une fois relancé, tape `/skills`. Tu dois voir la liste complète (cf. section "Vérification" plus bas).

---

## Installation Windows

### Étape 1 — Télécharger le ZIP

Sur le Drive bootcamp, ouvre le dossier `S4 J5 — Bundle skills complet`. Clique-droit sur `tim-claude-skills-YYYY-MM-DD.zip` → **Télécharger**. Le fichier arrive dans Téléchargements.

### Étape 2 — Décompresser

Clic-droit sur le ZIP → **Extraire tout**. Garde le dossier de destination par défaut. Windows crée le dossier `tim-claude-skills/` à côté.

### Étape 3 — Ouvrir ton dossier des skills

Ouvre l'Explorateur Windows. Dans la barre d'adresse (en haut), tape : `%USERPROFILE%\.claude\skills\` et valide. L'explorateur ouvre le dossier.

S'il n'existe pas, tape juste `%USERPROFILE%\` dans la barre d'adresse, puis crée à la main le dossier `.claude` puis dedans `skills`.

### Étape 4 — Glisser le contenu

Sélectionne tous les sous-dossiers depuis `tim-claude-skills/` extrait. Glisse-les dans `%USERPROFILE%\.claude\skills\`. Confirme **Remplacer les fichiers** quand Windows demande.

### Étape 5 — Relancer Claude et vérifier

Quitte complètement Claude. Relance. Tape `/skills` pour vérifier la liste.

### ⚠️ Cas spécifique Cowork installé depuis le Microsoft Store

Si tu as installé Cowork depuis le Microsoft Store (et pas via un exécutable classique), il stocke ses skills dans un dossier système sandboxé, pas dans `%USERPROFILE%\.claude\skills\`. Le chemin ressemble à `C:\Users\[ton-nom]\AppData\Local\Packages\[un-truc-cryptique]\LocalState\skills\`.

Test pour savoir si tu es concerné : après avoir mis les skills dans `%USERPROFILE%\.claude\skills\` et relancé, tape `/skills`. Si tu vois la liste complète → tout va bien, ignore cette section. Si tu ne vois rien ou que la liste est incomplète → tu es probablement sur Cowork Microsoft Store, MP immédiatement, on cherche ensemble le bon chemin sur ta machine (cas déjà rencontré en S3).

---

## Vérification après install (toutes plateformes)

Dans Claude (Code ou Cowork), tape `/skills`. Tu dois voir au minimum :

- article-engine-pipeline
- audit-engine-pipeline
- indexation-check
- maillage-interne-gsc
- maillage-systeme
- seo-brief-contenu
- seo-cannibalisation
- seo-cluster-aeo
- seo-clustering-mots-cles
- seo-core-web-vitals
- seo-donnees-structurees
- seo-entites-vectorielles
- seo-modeles-pseo
- seo-mots-cles-decisionnels
- seo-peurs-objections
- seo-product-led-seo
- seo-programmatique-pseo
- seo-quick-win
- seo-recherche-mots-cles
- seo-roadmap-pseo
- seo-workflow-article

Si un skill manque, fais un tour dans `~/.claude/skills/` (Mac) ou `%USERPROFILE%\.claude\skills\` (Windows) et vérifie deux choses sur le sous-dossier manquant :

- Le sous-dossier existe bien (par exemple `~/.claude/skills/seo-roadmap-pseo/`)
- Dedans il y a un fichier qui s'appelle exactement `SKILL.md` (avec un S majuscule, en .md, pas .txt)

Si l'un des deux manque, refais l'étape 4 en glissant uniquement le sous-dossier manquant.

---

## Précautions importantes

- **Tes skills perso à toi (`ton-de-voix-prenom`, skills clients custom) sont gardés.** L'install écrase seulement les skills qui portent le même nom dans le ZIP. Tes skills perso que tu as créés en parallèle (typiquement `ton-de-voix-marie`, `ton-de-voix-romain`) ne sont pas touchés. Vérifie quand même qu'ils sont toujours là après l'install en faisant `/skills`.

- **Si tu as modifié un de mes skills pour ton client** : par exemple tu as adapté `seo-donnees-structurees` à un client WordPress très spécifique. Le ZIP écrase cette adaptation. AVANT d'installer : copie ta version modifiée dans un autre dossier (par exemple `~/.claude/skills-archive/`) pour la garder.

- **L'install ne touche pas tes conversations Claude existantes.** Tu peux réinstaller à tout moment sans casser ton historique ni perdre ton contexte client.

- **Mise à jour future.** Quand je pousse une nouvelle version (nouveaux skills, corrections), je remets un ZIP avec une nouvelle date sur le Drive et je préviens sur WhatsApp. Tu refais les 5 étapes, ça prend 2 minutes.

## En cas de blocage

Trois cas typiques :

1. **`/skills` ne montre pas la nouvelle liste après install** → tu n'as pas relancé Claude complètement. Sortir + relancer, pas juste recharger l'onglet.

2. **Le ZIP refuse de s'extraire** → mauvais téléchargement (Drive incomplet). Re-télécharge depuis le Drive en clic-droit.

3. **Le skill apparaît dans `/skills` mais ne se déclenche pas sur les bons mots-clés** → quitte et relance Claude complètement. C'est instantané au redémarrage.

MP dédié vendredi soir si tu es bloqué. Pas la peine d'attendre lundi pour débloquer un truc qui se règle en 10 minutes.

---

## Note pour Tim (interne)

- **Curation du ZIP avant export.** `~/.claude/skills/` contient des skills internes qui n'ont rien à faire dans le bundle bootcamp : `organikk-blog-article`, `organikk-site`, `kb-semantic-search`, `bxble-directory`, `fusionn-trends-quotidien`. Avant de zipper : copier `~/.claude/skills/` dans un dossier temporaire, supprimer ces 5 sous-dossiers, zipper le dossier nettoyé. Pas pénible (30 secondes) mais à faire systématiquement à chaque export. Sinon les participants chargent 5 skills inutiles qui exposent ta plomberie projets.
- **Procédure de zip propre (à scripter une fois).** Tu peux te poser un mini-script `~/bin/bundle-skills-bootcamp.sh` qui : (a) copie `~/.claude/skills/` dans `/tmp/tim-claude-skills-{date}/`, (b) supprime les 5 sous-dossiers internes, (c) zip le résultat dans `~/Desktop/tim-claude-skills-{date}.zip`. Tu lances le script, tu déposes le ZIP sur le Drive, c'est fini. Si tu veux le script, je l'écris en 2 lignes.
- **Push `seo-roadmap-pseo` au repo GitHub** avant l'export. Il vit dans `~/.claude/skills/` depuis hier mais pas encore commit/push sur le remote. Le ZIP local le prendra de toute façon (il bypasse Git), mais autant garder le remote à jour : `cd ~/.claude/skills && git add seo-roadmap-pseo && git commit -m "Add seo-roadmap-pseo skill" && git push`.
- **Nommage du ZIP.** J'ai mis `tim-claude-skills-YYYY-MM-DD.zip`. La date sert à : (a) que les participants voient quelle version ils ont, (b) que tu puisses dire au call "la dernière version est celle du 29 mai". Format ISO obligatoire (`2026-05-29`), pas `29-05-2026` ni `29 mai 2026`, sinon le tri par nom ne marche pas.
- **Workaround Cowork Microsoft Store.** Toujours pas documenté dans la KB. À chercher AVANT vendredi (poser la question dans le chat ou demander à Lydia/Gregory qui étaient affectés en S3). Si tu as la solution, je l'ajoute dans la section "Cas spécifique" du doc.
- **Cohérence avec [[skills-checklist-bootcamp4]].** Ce doc d'install ne liste que les skills présents dans le ZIP curé. La checklist existante reste valide pour le détail "à quoi sert chacun". Lier les deux dans le message WhatsApp d'envoi vendredi.
- **README dans le ZIP.** Mettre un fichier `README.md` à la racine du ZIP qui dit : "Ce dossier contient les skills SEO du bootcamp Organikk 4 (mai 2026). Pour installer, suivre la procédure dans le doc Drive `install-repo-skills-cowork.md`." Évite que le participant ouvre le ZIP, n'y comprenne rien et abandonne.
- **Normalisation.** Doc sans em-dashes (règle maison). Procédure unique (ZIP depuis Drive) au lieu des 3 méthodes initiales (git clone + 2 variantes Cowork). Plus simple à lire, plus simple à suivre, plus simple à supporter en MP.
