---
type: concept
title: Objection « et la confidentialité / RGPD ? »
aliases: [objection-confidentialite, objection-rgpd, argumentaire-rgpd]
tags: [vente, objections, rgpd, confidentialite, claude, data-proprietaire]
created: 2026-06-10
updated: 2026-06-10
sources: 2
confidence: high
status: stable
---

# Objection « et la confidentialité / RGPD ? »

> L'objection arrive mécaniquement dès qu'on propose d'enregistrer les calls et de traiter la data client ([[data-proprietaire]]). Réponse en deux phrases, puis le détail si le prospect creuse. Vérifié sur les pages officielles Anthropic le 2026-06-10 ([[sources/2026-06-10-anthropic-politique-donnees|détail sourcé ci-dessous]]).

## La réponse courte (à dire en call)

« Sur un forfait Team/Enterprise ou via l'API, Anthropic n'entraîne pas ses modèles sur vos données par défaut et fournit un contrat de sous-traitance (DPA). Le point RGPD à gérer de votre côté, c'est l'information des participants à l'enregistrement et la durée de conservation des transcripts. »

## Le détail si le prospect creuse

1. **Entraînement = question de type de compte, pas d'outil.** Conditions commerciales (API, Team, Enterprise, Bedrock, Vertex) : aucun entraînement par défaut, opt-in explicite requis (Development Partner Program). Comptes consumer (Free/Pro/Max) : depuis septembre 2025, réglage « Help improve Claude » (claude.ai → Settings → Privacy) ; activé = entraînement + rétention 5 ans, désactivé = pas d'entraînement + rétention 30 jours.
2. **RGPD ≠ entraînement.** Trois obligations côté client : informer les participants à l'enregistrement des calls (en amont de tout outil), cadrer Anthropic comme sous-traitant via le DPA (réservé aux comptes commerciaux : un compte Pro/Max perso n'en a pas), minimiser (anonymiser ce qui peut l'être, ne conserver que l'utile).
3. **Le brut reste en local.** Le vault vit sur la machine du client, pas dans un cloud tiers. Seul ce qui sert au traitement en cours transite par l'API.

## Cas d'usage réels

- Call de cadrage Alexia/Adrien (2026-06-10) : l'agence est sur Claude Enterprise, donc conditions commerciales, rien à toggler. Argument donné tel quel à Adrien.
- Guides 0→1 : section confidentialité ajoutée dans le guide agent (chapitre data, §2.4) et le guide skills (avant les workflows).

Sources : politique officielle Anthropic (Updates to Consumer Terms, sept. 2025 ; Data usage, Claude Code Docs ; Privacy Center, « Is my data used for model training? »).

Pages liées : [[moc/moc-vente-objections]] · [[data-proprietaire]] · [[concepts/scam-objection-data-aleatoire]] · [[syntheses/vendre-seo-ia-2026]]
