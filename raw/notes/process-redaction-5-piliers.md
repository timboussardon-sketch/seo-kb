# Process de rédaction — généralisable tous secteurs

## Le principe central

Je ne pars jamais d'un prompt. Je pars d'un corpus client validé. Tant qu'on n'a pas au moins un texte que le client a lu, corrigé et signé, on ne peut pas produire de contenu qui sonne comme lui. C'est la règle qui change tout.

## Les 5 piliers du process

### 1. Le corpus de référence

Avant toute rédaction, on identifie 2 ou 3 textes que le client a personnellement validés. Ces textes deviennent les "core texts" — la patte, le ton, la structure, le vocabulaire. Tous les contenus suivants s'alignent dessus. Sans ce socle, on produit du contenu générique.

### 2. L'extraction du template structurel

À partir des core texts, on extrait un gabarit Hn réutilisable. Quels H2 reviennent ? Quel ordre ? Quels formats (tableau, étude de cas, FAQ) ? Cette structure devient le moule pour toutes les pages métier. Le client reconnaît sa patte avant même d'avoir lu une phrase.

### 3. La règle "uniquement nos contenus"

Pour chaque nouvelle page, on ne s'autorise que ce qui existe dans le corpus client (dossiers, archives, textes validés). Pas de stats Google, pas de vocabulaire inventé, pas de cas génériques. Si une info n'est pas dans le corpus, on la flag pour validation au lieu de la combler par hallucination. Cette contrainte force la qualité.

### 4. Le pipeline en 8 étapes

Avant de rédiger, on passe par une chaîne fixe : identifier ce que les concurrents ne disent pas (Surprise Gap), ancrer dans le terrain client, lister les inversions expertes, construire l'architecture narrative, puis seulement rédiger. La rédaction n'est jamais l'étape 1 — c'est l'étape 6.

### 5. Les anti-patterns IA

Liste fermée de tournures et de structures à proscrire systématiquement : adverbes creux, "il est important de noter", règle de 3 systématique, conclusions-résumés, bullet points décoratifs, gras sur les premiers mots de paragraphe. Une relecture spécifique pour les détecter et les supprimer.

## Le workflow type pour un nouveau client

D'abord on récupère son corpus existant (textes publiés, dossiers, archives métier). On l'organise dans une arborescence claire. On identifie 1 à 3 textes que le client validera explicitement comme représentatifs de sa patte.

Ensuite on extrait la structure Hn type, le vocabulaire métier validé, les arguments récurrents et les cas clients exploitables.

À partir de là, chaque nouvelle page suit le même cycle court : choix d'un cas client réel dans le corpus, brief Hn calé sur le gabarit, rédaction passant par le pipeline 8 étapes, sauvegarde dans un dossier de référence dédié. Validation client systématique avant de décliner sur les autres pages du même type.

## Ce qui fait la différence

Trois choses concrètement. D'abord la discipline de ne rien inventer — quand on n'a pas l'info, on la flag, on ne la fabrique pas. Ensuite la patte client préservée à chaque itération — on ne dérive jamais loin du gabarit validé. Enfin l'identification systématique d'un angle différenciant par page, basé sur ce que les concurrents évitent de traiter, pas sur ce qu'ils écrivent tous.

Ce process tient pour n'importe quel secteur où le client a une expertise verticale et un corpus exploitable : avocat, consultant, expert-comptable, agence spécialisée, formateur, médecin, architecte. Plus le client a de matière brute (dossiers, archives, mémos internes), plus le résultat est différenciant.

---

## Le pipeline en 8 étapes (détail)

Référence opérationnelle du pilier 4. Skill source : `~/.claude/skills/seo-workflow-article/SKILL.md`.

| Étape | Nom | Output |
|-------|-----|--------|
| 1 | Surprise Gap | 5 angles saturés + 5 infos sous-exploitées classées par gradient d'information |
| 2 | Ancrage local | Signaux E-E-A-T géographiques précis (autorité locale, OPCO, tissu éco) |
| 3 | Données chiffrées | 8-12 stats sourcées (chiffre + source + argument + contexte) |
| 4 | Inversions expertes | 5 croyances fausses + réalité + pourquoi l'erreur persiste + formulation |
| 5 | Architecture narrative | Plan section par section (rappel + contenu + surprise + transition) |
| 6 | Rédaction principale | Prose 2000-2500 mots, pattern Tension → Résolution → Preuve |
| 7 | FAQ micro-intentions | 6-8 questions bas de funnel (non traitées dans le corps) |
| 8 | Compilation finale | Article complet + checklist qualité |

Ordre strict : 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8. Aucune étape ne se saute. La rédaction (étape 6) ne démarre qu'après validation des 5 étapes amont.

**Frameworks mobilisés :**
- Surprise Score (Titans/MIRAS) — étapes 1, 4, 5, 6
- Grounding Score (Triade SERP) — étapes 5, 6, 8
- Anti-AI Writing — étapes 6, 8
- E-E-A-T local — étape 2
