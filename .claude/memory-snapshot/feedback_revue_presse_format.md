---
name: Format revue-presse Algorithme = monographique, sans jargon
description: La newsletter "Algorithme" doit être monographique (1 sujet / 1200-1500 mots / voix Tim), pas un template multi-piliers — et accessible aux non-SEO
type: feedback
originSessionId: 9475cb58-11fe-431f-8d55-5491d1024e30
---
Une édition "Algorithme" = **un seul sujet**, prose libre 1200-1500 mots, en voix Tim (apartés entre parenthèses, "je le répète depuis", "et c'est tant mieux", tutoiement dans les digressions). Référence pixel-perfect : les vraies éditions Substack scrapées dans `raw/articles/algorithme-data-claude-perplexity.md` et `raw/articles/algorithme-pourquoi-article-ne-rank-pas.md`.

**À NE PAS reproduire** : le template multi-piliers `## INFO DU JOUR / ## AUSSI SUR LE RADAR / **Les chiffres :** / **Ce que ça change concrètement :** / *(espace réservé)* / **Connecté avec :** [[xxx]]`. Tim a explicitement rejeté ce format en mai 2026 — ton trop neutre, jargon trop dense, voix Tim absente.

**Anti-jargon (règle dure)** : le lecteur cible n'est pas SEO de métier. Acronymes (MCP, OSWorld, AIO, AEO, RAG, E-E-A-T...) doivent être expliqués ou remplacés par périphrase ; concepts techniques doivent être matérialisés par un exemple concret (cf. Tesla autonomie / RE2020 R=7 / atomes A-B-C dans les éditions de mars).

**Why** : Tim a constaté en mai 2026 que les sorties récentes du skill (`raw/revue-de-presse/2026-04-29*.md`, `2026-05-04-*.md`) avaient dérivé vers un rapport de veille multi-sources templaté, jargonneux, avec un placeholder "Ce que j'en pense" qui forçait Tim à rajouter sa voix après coup. Ce n'est pas le produit Algorithme.

**How to apply** : à chaque invocation du skill `revue-presse-quotidienne`, lire d'abord 2 vraies éditions Substack dans `raw/articles/algorithme-*.md` (PAS dans `raw/revue-de-presse/`) avant de rédiger. Si le sujet du jour exige plus de 5 acronymes pour être compris, choisir un autre sujet.
