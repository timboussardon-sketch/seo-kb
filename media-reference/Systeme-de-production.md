# Média de référence SEO FR — Système de production

But : devenir la référence SEO en France sans que le site soit lu comme un média auto-généré.

Le « feel IA » d'un média ne vient pas du design, il vient du **système de production**. Un flux unique de brèves auto-poussées EST un pipeline IA, quel que soit le thème graphique. La parade : structurer la production en voies dont une partie est non-reproductible par une machine, et verrouiller à chaque sortie une couche que seul l'humain ajoute.

Ce doc articule des briques qui existent déjà (skills `MediaSEO`, `breves-quotidiennes`, `newsletter-ia`, `seo-page-etude-originale`, agent `agent-synthetic`). Il ne les remplace pas, il les met en média.

---

## 1. La règle dure

**La machine ne publie jamais seule.**

Chaque sortie passe une porte où l'humain ajoute la couche que la machine ne peut pas produire. Cette porte n'est pas un contrôle anti-IA-writing (ça, c'est déjà dans les skills). C'est un **ajout de valeur obligatoire**. Sans cet ajout, on ne publie pas, on garde en draft.

C'est la même logique que `MediaSEO` : l'IA apporte des faits solides, l'humain leur donne du sens. On la généralise à tout le média.

---

## 2. Les 3 voies, 3 cadences

Un média auto-généré a une seule texture : des brèves toutes équivalentes qui défilent. Une référence a un **rythme** : du quotidien jetable, de l'hebdo qui prend position, du mensuel qu'on cite pendant un an.

| Voie | Cadence | Brique existante | Ce que la machine fait | Couche non-copiable (la porte) |
|---|---|---|---|---|
| **Le flux** | Quotidien | `MediaSEO` / `breves-quotidiennes` | Veille inversée, tri /70, premier jet factuel sourcé | Une prise par item : « pour qui c'est important et pourquoi », ancrée sur un site FR réel |
| **L'analyse** | Hebdo | `newsletter-ia` (3 blocs) | Structure, rappel des faits, liens entre brèves | Une position datée et signée qu'on peut te contredire dans 6 mois |
| **L'enquête** | ~Mensuel | `seo-page-etude-originale`, `etudes-seo/` | Extraction GSC/logs, calcul, mise en forme | La donnée first-party elle-même (CTR × AI Overviews, logs Fusionn). Aucun LLM ne la génère |

Le flux retient l'audience. L'analyse et l'enquête construisent l'autorité : ce sont elles qu'on cite, qui ramènent les liens éditoriaux et les citations LLM.

---

## 3. La couche non-copiable, voie par voie

### Flux (quotidien)
- La machine produit du factuel pur (mode `MediaSEO` : pas d'interprétation, pas de reco, pas de prédiction).
- **Porte** : pas d'item publié sans une prise de 2 lignes signée. Format « ce que ça change pour un site FR », rattaché à un cas réel (un site, un secteur), pas une généralité.
- Pourquoi c'est non-copiable : un scraper + LLM reproduit le résumé, pas la prise reliée à un site français concret.

### Analyse (hebdo)
- La machine assemble les faits de la semaine et les relie.
- **Porte** : pas d'édition sans une position datée. « Je pense que Google va… », « ce qui est surévalué ici, c'est… ». Une position qu'on pourra te ressortir et qui peut avoir tort.
- Pourquoi c'est non-copiable : la référence, c'est celui qui s'est mouillé et qu'on cite par son nom.

### Enquête (mensuel)
- La machine extrait, calcule, met en forme.
- **Porte** : pas d'étude sans un chiffre first-party. Si la pièce n'a que du desk research, ce n'est pas une étude, c'est une brève longue. On la reclasse.
- Pourquoi c'est non-copiable : c'est ta data propriétaire. C'est le moat.

---

## 4. Ratio cible

Le piège : sur-automatiser le flux et négliger les deux autres voies. Un site qui n'est **que** du flux quotidien sera lu comme un agrégateur IA, même impeccable.

- Volume de production : le flux domine (c'est le quotidien).
- Investissement éditorial et mise en avant : penché vers analyse + enquête.
- Une enquête first-party par mois est le plancher. En dessous, le média n'a pas de moat, juste un flux propre.

La Une reflète ce ratio : un sujet dominant (analyse ou enquête en cours) en tête, le flux en dessous. Jamais 12 cards égales.

---

## 5. La 4e brique à construire : le dashboard vivant

Un « état du SEO FR » maintenu : volatilité SERP, déploiement des AI Overviews en France, part de citations par moteur. De la donnée à jour, pas un article.

Le réflexe « je vais voir où ça en est » crée le retour récurrent qu'aucun article ne crée. C'est ce qui transforme un média qu'on lit en référence qu'on consulte.

Statut : chantier à ouvrir. Source de données candidate : GSC multi-propriétés (export Fusionn), logs Fusionn, suivi manuel AI Overviews FR.

---

## 6. La boucle d'apprentissage

Reprendre le mécanisme `agent-synthetic` (Algorithme) au niveau du média entier, pas par produit isolé :

- **predictions.jsonl** : chaque position datée de l'analyse devient une prédiction avec date de résolution. On vérifie. Un média qui assume ses prédictions passées et dit quand il s'est trompé est par définition non-IA.
- **engagement** : ce qui est lu / cité oriente les voies, sans transformer le flux en course au clic.
- **claims** : chaque affirmation reste une unité vérifiée (≥ 2 sources, primaire d'abord, anti-fraîcheur), comme dans la méthode SyntheticBrain.

Les corrections de Tim deviennent des règles durables dans les skills, jamais des ajustements jetables.

---

## 7. Ce qui trahit le template IA (checklist anti-pattern)

À bannir, côté édito comme côté design :

- [ ] Agrégation sans angle (résumé d'une actu déjà lue ailleurs, sans prise ni data)
- [ ] Grille de cards homogène (hero + 3 colonnes + « voir plus »)
- [ ] Titres formatés (« 5 choses à savoir », « tout ce qu'il faut savoir », « X : ce qui change »)
- [ ] Voix nulle part (pas d'auteur identifiable, jamais de désaccord)
- [ ] Fraîcheur sans profondeur (que des brèves, zéro enquête)
- [ ] Patterns d'écriture IA (liste complète dans le skill `MediaSEO` et `ton-de-voix-tim`)

La Une hiérarchisée (1 sujet dominant + analyse + brèves reliées) est l'inverse du template : elle impose une hiérarchie de rédacteur, pas de CMS. C'est exactement la logique de la `newsletter-ia` 3 blocs portée sur le site.

---

## Liens

- Skill flux strict (journaliste) : `~/.claude/skills/MediaSEO/`
- Skill flux avec angle (réd. en chef) : `~/.claude/skills/breves-quotidiennes/`
- Skill analyse hebdo : `~/.claude/skills/newsletter-ia/`
- Skill enquête first-party : `~/.claude/skills/seo-page-etude-originale/`
- Boucle d'apprentissage : `agent-synthetic/README.md`
- Méthode édition Algorithme : `wiki/methodes/cadrage-boucle-edition-algorithme.md`
