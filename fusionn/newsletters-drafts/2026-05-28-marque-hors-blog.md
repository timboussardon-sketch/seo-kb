---
date: 2026-05-28
edition: 2
status: draft v1
sujet: AI Overviews + Reddit, faire exister sa marque hors du blog
sources: [TechCrunch (bloc Expert Advice, 6 mai), Growth Memo (Kevin Indig, 3,7M citations), revue de presse 2026-05-22 et 2026-05-28]
---

# Google cite des inconnus de Reddit. Ta marque, elle, vit toujours dans ton blog.

## La grande idée

Depuis le 6 mai, Google a ajouté un bloc « Expert Advice » qui va piocher ses citations directement dans Reddit, les forums et les posts sociaux, avec un lien vers la conversation d'origine. L'ironie, c'est qu'il appelle « expert » des hobbyistes plutôt que des autorités. Mais peu importe ce qu'on en pense : ce qui compte, c'est que Google est allé chercher la réponse ailleurs que sur les sites officiels.

Et ce n'est pas un cas isolé. Perplexity puise près d'une citation sur deux dans Reddit. ChatGPT, lui, va surtout sur Wikipedia. Kevin Indig a analysé 3,7 millions de citations IA : 91% des sites cités n'apparaissent que sur un seul moteur, et chacun a sa source préférée. Reddit est en train de devenir le carrefour que plusieurs moteurs interrogent en même temps.

Le réflexe, c'est de se dire « je vais soigner mon blog ». Sauf que ton blog, demain, tout le monde en aura un, propre, complet, généré en deux heures. Ce n'est plus là que tu te différencies. Ce qui décide aujourd'hui de ta citation, c'est la preuve conversationnelle : est-ce qu'on parle de ta marque là où les moteurs vont vérifier ? Si personne ne te mentionne sur un forum, dans un fil Reddit, dans des avis, tu n'es pas dans le bloc. Tu peux avoir le meilleur article du marché, tu restes invisible pour cette partie de la SERP.

Je le dis depuis un moment : on ne gagne plus en publiant une page de plus, on gagne en devenant la marque que les gens citent quand ils répondent à quelqu'un d'autre. C'est plus lent, ça ne se génère pas en un clic, et c'est tant mieux (ce qui est facile est facilement copiable). Concrètement, tu arrêtes de tout concentrer sur ton domaine et tu vas créer des traces réelles : répondre pour de vrai dans deux ou trois communautés où sont tes prospects, faire en sorte qu'on cite ton nom dans des fils de discussion, récupérer des avis qui nomment ta boîte. Pas du spam de liens (tu te fais bannir et c'est mérité). De la présence utile, qui laisse une trace que Google et Perplexity iront lire.

## Les mots-clés à attaquer

Sur la mécanique de citation IA, peu de monde traite ça franchement en français aujourd'hui :

- `comment être cité par les ia`
- `google expert advice c'est quoi`
- `présence de marque sur reddit b2b`
- `stratégie reddit pour le seo`
- `aeo forums et communautés`
- `brand mentions et citation ia`

(Ces requêtes sont des cibles éditoriales, à grounder sur Google Suggest avant prod, cf. note interne.)

## Ce qui se dit

- TechCrunch · [Google updates AI search to include expert advice from Reddit and other web forums](https://techcrunch.com/2026/05/06/google-updates-ai-search-to-include-expert-advice-from-reddit-and-other-web-forums/)
- Growth Memo (Kevin Indig) · analyse de 3,7M de citations IA : 91% des sites cités n'apparaissent que sur un seul moteur, Perplexity ≈ Reddit pour près d'1 citation sur 2

[À SOURCER : pull YouTube + Reddit frais sur « AI Overviews Reddit » / « brand mentions AI » via le pipeline, pour 3 vidéos + 3 posts verbatim avant publication.]

---

*[Tester Fusionn](https://fusionn.co)*

---

## Notes internes (à supprimer avant publication)

### Grounding / anti-hallucination
- Bloc Expert Advice + date 6 mai : sourcé TechCrunch (revue de presse 2026-05-28).
- Perplexity ≈ Reddit, ChatGPT ≈ Wikipedia, 91% sur un seul moteur, 3,7M citations : sourcé Growth Memo / Kevin Indig (revue 2026-05-22).
- Mots-clés : cibles éditoriales NON groundées (pas de volume affiché, jamais inventé). À passer dans `scripts/ground-keyword.mjs` (seeds : « citation ia », « reddit seo », « aeo ») avant publi.
- Section « Ce qui se dit » : YouTube/Reddit à puller frais (pipeline) — ne pas réutiliser les liens de l'édition Google I/O.

### Anti-AI writing (vérifié)
- 0 em-dash, 0 mot interdit (crucial, pivotal, landscape…), 0 conclusion-résumé, 0 règle de 3 systématique.
- Apartés présents, 1 référence à une position tenue (« je le dis depuis un moment »), formulations directes (« et c'est tant mieux », « c'est mérité »).
- Aucune mention Fusionn dans le corps (CTA uniquement).

### Doctrine
- Pilier mobilisé : la commodité (le blog parfait que tout le monde aura demain) vs la trace de marque non copiable. Anti-ChatGPT en filigrane.
