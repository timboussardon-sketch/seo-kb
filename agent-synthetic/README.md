# SyntheticBrain — mémoire de l'agent `/agent-synthetic`

Cerveau d'apprentissage de la newsletter **Algorithme**. Ce dossier est la **mémoire** de l'agent. Le skill `/agent-synthetic` (dans `~/.claude/skills/agent-synthetic/`) la lit au début de chaque édition et la réécrit à la fin. C'est ce qui fait que l'agent apprend d'une newsletter à la suivante.

Cadrage complet : `../wiki/methodes/cadrage-boucle-edition-algorithme.md`.

## Principe

L'agent enveloppe le skill socle `revue-presse-quotidienne`. Il ne le remplace pas. Il ajoute autour :
- un **briefing** qui lit cette mémoire,
- une **veille agentique** qui découvre de nouvelles sources,
- un **recoupement** entre sources,
- un **fact-check à verdict**,
- une **titraille intelligente** (jamais racoleuse),
- une phase d'**apprentissage** qui réécrit cette mémoire et pose des questions.

La self-amélioration est simple et auditable : l'agent réécrit des **notes** (les fichiers ci-dessous), jamais son propre prompt. Tout est versionné git, donc réversible.

## Les fichiers

| Fichier | Rôle |
|---|---|
| `directives.md` | Consignes pour la prochaine édition, écrites par l'agent à la fin de la précédente |
| `source_registry.jsonl` | Toutes les sources connues : confiance, dernière contribution utile, statut (explore/exploit/retiré) |
| `source_weights.json` | Poids courants par source, dérivés du registre |
| `wording_rules.md` | Style maison accumulé. La règle n°1 : hook intelligent, jamais racoleur |
| `headlines.jsonl` | Titres testés et leur performance |
| `predictions.jsonl` | Prédictions datées avec leur date de résolution et leur statut |
| `said_index.jsonl` | Thèmes déjà traités, pour l'anti-redite profond |
| `engagement.jsonl` | Opens et clics par édition et par section (alimenté plus tard) |
| `calibration.md` | Score de l'agent dans le temps sur les 4 critères de qualité |
| `questions.md` | Les « comment faire mieux » de l'agent : à tester, ou à trancher par Tim |

## Cible de qualité (une grande édition)

1. Recoupement solide (vérifié, croisé, zéro bruit)
2. Angle inédit / surprise
3. Lien avec la doctrine (`wiki/concepts/`, via `./kb search`)
4. Hook intelligent qui prouve qu'on a creusé, jamais racoleur

## Autonomie et garde-fous

- **Sources** : auto-ajout au-dessus d'un seuil de confiance (source corroborée), retrait du bruit, tout journalisé. En dessous du seuil, validation à la revue hebdo.
- **Skills** : l'agent ne modifie jamais un skill tout seul. Il propose un diff dans `questions.md`, Tim valide à la revue hebdo.
- **Questions** : groupées à la revue hebdo du vendredi (urgent seulement si bloquant).
- Tout est commité en git. Autonome sur la data, jamais sur le code, jamais invisible ni irréversible.
