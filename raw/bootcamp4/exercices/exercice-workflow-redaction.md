---
title: "Workflow rédaction : rédiger une page incarnée"
bootcamp: 4
type: exercice-workflow
session: 2
cowork: oui
created: 2026-06-09
---

# Workflow rédaction : rédiger une page incarnée

**Pré-requis** : skills article-engine-pipeline et seo-brief-contenu installés. Un brief (Hn) + de la data propriétaire (calls, chiffres).

## Le cas

Passer d'une rédaction générique à une page incarnée, avec Surprise Gap et Grounding. La clé : une seule conversation Claude par projet (le contexte s'accumule), un arrêt à 50% pour relire, un fact-check avant de finir.

## Ce que tu dois faire

**1. Le contexte d'abord**
Donne calls, étude de marché, Reddit, data propriétaire AVANT le brief. Le contexte avant tout.

**2. Lance le pipeline**

```text
Lance article-engine-pipeline sur [requête]. Voici mon brief Hn et ma data.
Décode la requête (RRF), génère la FAQ stratégique, puis rédige
et ARRÊTE-TOI à 50% pour que je relise.
```

**3. Relis à 50%**
Ton, Surprise Gap visible, tics LLM, data injectée. Corrige, puis fais finir.

**4. Fact-check, finalise**
Vérifie les chiffres (Perplexity/Grok), réinjecte les sources, termine.

## Ce que tu dois obtenir — le « screen »

```
ARTICLE — structure produite

[intro : passage ancré 150-200 mots, dans les 300 premiers]
H2 (Surprise Gap) → ce que les autres n'ont pas dit
H2 (data propriétaire) → tes chiffres, tes verbatims
FAQ (5-7 questions, vecteurs distincts)
+ checklist fact-check : chaque chiffre, sa source.
```

## Vérifier que tu as réussi

- [ ] Tu t'es arrêté à 50% et tu as relu.
- [ ] Chaque chiffre est sourcé ou marqué [À SOURCER].
- [ ] Passage ancré 150-200 mots dans les 300 premiers mots.
- [ ] Zéro pattern IA.
- [ ] La voix est la tienne, pas générique.

## Le piège

Tout générer d'un coup sans s'arrêter à 50%. Un article généré en une fois dérive sur le ton et accumule les tics IA. L'arrêt à 50% est non négociable.

## Comment ça marche

Le pipeline décode la requête (RRF), construit une FAQ qui couvre les vecteurs manquants, puis déroule la rédaction en 8 étapes. L'arrêt à 50% te laisse corriger la trajectoire avant qu'il soit trop tard.
