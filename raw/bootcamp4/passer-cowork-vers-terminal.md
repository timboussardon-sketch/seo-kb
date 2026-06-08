---
title: "Passer de Cowork à Obsidian + terminal"
bootcamp: 4
type: doc-participant
public: oui
usage: "Fiche unique A→Z pour migrer de Claude Cowork vers Obsidian (vault) + terminal (Claude Code). Méthode Karpathy raw/ + wiki/. Mêmes skills, même dossier ~/.claude/skills/."
related:
  - "[[install-repo-skills-cowork]]"
  - "[[IMPLEMENTATION-COWORK]]"
  - "[[karpathy-llm-wiki]]"
---

# Passer de Cowork à Obsidian + terminal

> Fiche participant du [[entities/bootcamp-seo-ia]] ([[offre-bootcamp-seo-ia]]) : migration A→Z vers [[entities/obsidian]] + terminal, méthode raw/ + wiki/ de [[entities/karpathy]]. Travailler le vault directement dans son éditeur, c'est [[concepts/obsidian-as-ide]].

Tes skills sont déjà installés (même dossier que Cowork). Tu ne réinstalles rien : tu changes juste de fenêtre. Voici les 5 étapes : 

## Ce que tu dois faire

**1. Récupère le dossier de travail.**
Télécharge ton dossier `seo-kit` depuis ton dashboard bootcamp : https://organikk.co/dashboard-bootcamp-organikk-private-2026/ . Dézippe-le dans `~/Documents/seo-kit`.

**2. Installe Obsidian (pour VOIR tes notes).**
Télécharge-le gratuitement sur **obsidian.md**. Ouvre-le → « Open folder as vault » → choisis `~/Documents/seo-kit`.

**3. Crée le fichier `CLAUDE.md` (la notice que Claude lira tout seul).**
Le plus simple : ouvre le **Terminal** et colle ce bloc en entier, puis Entrée. Il crée le fichier au bon endroit, tout seul :

```bash
cat > ~/Documents/seo-kit/CLAUDE.md << 'EOF'
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
EOF
```

(Windows : ouvre le dossier `seo-kit`, clic droit → Nouveau → Document texte, renomme-le `CLAUDE.md`, ouvre-le et colle le contenu ci-dessus **sans** la première ligne `cat ...` ni la dernière ligne `EOF`.)

**4. Installe Claude Code (pour PILOTER Claude).**
Dans ton terminal, colle :
`npm install -g @anthropic-ai/claude-code`
(Bloqué ? Tu m'envoies un MP.)

**5. Lance.**
Ouvre le **Terminal**. Quand il s'ouvre, tu es dans ton dossier personnel, pas dans `seo-kit`. Il faut d'abord y entrer. Tape ces deux lignes, une par une, en validant avec Entrée à chaque fois :

```bash
cd ~/Documents/seo-kit
claude
```

La première ligne (`cd ~/Documents/seo-kit`) te place dans le bon dossier. La seconde (`claude`) lance Claude. Une fois dedans, tape `/skills` : tu vois ta liste de skills, c'est bon, tu es opérationnel.

**À retenir : à chaque fois que tu ouvres une nouvelle fenêtre de terminal pour travailler, tu retapes `cd ~/Documents/seo-kit` puis `claude`.** C'est le réflexe de départ, deux lignes, à chaque session.


Comment ça marche ?

Ton dossier a deux parties : **`raw/`** = tes sources brutes (tu y jettes tout), **`wiki/`** = les notes propres (c'est Claude qui les écrit).

Tu n'as rien à expliquer à Claude : dès que tu lances `claude` dans `seo-kit`, il lit tout seul le mode d'emploi du dossier et sait déjà comment maintenir `raw/` et `wiki/`.

Comment ça marche : tu déposes un doc dans le terminal, tu dis à Claude « ajoute-le à l'endroit X ». Il la range et la résume dans `wiki/`, et tu vois tout apparaître en direct dans Obsidian.

*Cette logique `raw/` + `wiki/` est déjà intégrée dans ton `seo-kit`, rien à installer. Si tu veux comprendre l'idée derrière (lecture optionnelle) : pattern « LLM Wiki » d'Andrej Karpathy, https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f*



---

## Version WhatsApp

> On passe à Obsidian + terminal. Tes skills sont déjà prêts, tu ne réinstalles rien.
> 1. Récupère ton dossier `seo-kit` sur ton dashboard (organikk.co/dashboard-bootcamp-organikk-private-2026), dézippe dans `~/Documents/seo-kit`.
> 2. Installe Obsidian (obsidian.md) → « Open folder as vault » → ce dossier.
> 3. Colle dans le Terminal la commande donnée dans la fiche (elle crée le `CLAUDE.md` tout seul).
> 4. Terminal : `npm install -g @anthropic-ai/claude-code` (bloqué ? MP).
> 5. Ouvre le Terminal et tape ces deux lignes (Entrée après chaque) : `cd ~/Documents/seo-kit` puis `claude`. Ensuite `/skills` pour vérifier. Le `cd ~/Documents/seo-kit` est à retaper à chaque nouvelle fenêtre de terminal.
> Ensuite : tu jettes tes sources dans `raw/`, Claude les range dans `wiki/`. Tu déposes chaque jour, sinon ça sert à rien. 💪
