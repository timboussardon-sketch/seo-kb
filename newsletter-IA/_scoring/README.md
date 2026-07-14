# _scoring — barème apprenant de la Newsletter IA

Boucle fermée de sélection : on score les news, on publie, on observe ce qui a marché, on recalibre. Réplique la mécanique d'`agent-synthetic` (`source_weights.json`).

## Séparation méthode / données

- **Méthode** (portable, versionnée avec le skill) : `~/.claude/skills/newsletter-ia/references/scoring.md`. La doctrine du barème.
- **Données** (ici, dans le vault) : ce dossier. Ce qui s'apprend édition après édition.

## Fichiers

| Fichier | Rôle |
|---|---|
| `derived/scoring_weights.json` | **Le point de vérité lu au moment de scorer.** Poids d'axes, coefficients de fiabilité, seuils, mapping ★, poids de sources. Réécrit par le script. |
| `ledgers/selections.jsonl` | 1 ligne par candidat scoré par édition (axes, base, coef, rank, bloc, ★, source). Append-only. |
| `ledgers/feedback.jsonl` | 1 ligne par item avec sa perf observée. Alimenté à la main OU par un export (clics, votes sondage, réponses). Source-agnostique. |
| `ledgers/sources.jsonl` | Registre des sources : tier, useful_hits, noise_hits. |
| `calibration.md` | Journal des recalibrations. |
| `recalibrate.py` | Recompte les poids depuis les ledgers, réécrit `derived/` + `sources.jsonl`, journalise. Idempotent. |

## Le feedback (ce qui nourrit l'apprentissage)

Ajouter une ligne dans `feedback.jsonl` par item dont on connaît la perf :

```json
{"edition": "2026-07-14", "item_id": "2026-07-14-ai-mode-1-milliard", "perf": "good", "signal": "clicks", "note": "top clic de l'édition"}
```

`perf` : `hit` / `good` (→ useful) · `ok` (neutre) · `flop` / `wrong` (→ noise, incluant une info qu'on a dû corriger).
`signal` : d'où vient le jugement (`clicks`, `poll`, `reply`, `manual`).

## Recalibrer

```bash
cd ~/Code/seo-kb/newsletter-IA/_scoring && python3 recalibrate.py
```

- **Poids de sources** : actifs dès le 1er feedback. `base_tier + 0.04·useful − 0.1·noise`, borné [0.9, 1.15]. Une source qui délivre monte, une source qui déçoit descend.
- **Calibration d'axe** : gelée tant que < 6 éditions notées (trop de bruit avant). Passé le seuil, chaque poids d'axe glisse selon sa capacité à discriminer les items qui ont marché de ceux qui ont floppé, borné [0.8, 1.3].

## Formule de score (rappel)

`base /80` = somme des 7 axes pondérés · `rank = base × coef_fiabilité × poids_source`.
`base` juge l'entrée en « en bref » · `rank` juge le sujet du jour et l'ordre. ★ = impact seul.
