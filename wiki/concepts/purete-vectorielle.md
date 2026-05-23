---
type: concept
title: Pureté vectorielle (une page = une intention)
aliases: [purete-vectorielle, purete-semantique, vector-purity, une-page-une-intention]
tags: [doctrine-tim, geo, embedding, intention, redaction, grounding-score, faq, terme-signature]
created: 2026-05-16
updated: 2026-05-16
sources: 3
confidence: high
status: stable
---

# Pureté vectorielle

**Terme signature de Tim.** Renommé depuis "pureté sémantique", formulation sortie en live au bootcamp 4 session 2 en réponse à Jamel sur la FAQ. Une page ne traite qu'une seule intention pour que son vecteur reste aligné avec la requête cible.

## La règle

> Une page = un mot-clé, mais surtout **une page = une pureté vectorielle**.

Sur "agence SEO" tu ne donnes pas un outil d'audit technique + un cas client BTP + dix sujets connexes sur la même page. Tu noies l'intention. Sur "faut-il acheter des backlinks en SEO" tu ne déballes pas toutes les techniques de ranking, tu restes sur les backlinks.

## Pourquoi ça marche (mécanique embedding)

Une page est encodée en un vecteur. Si elle mélange trois intentions, son vecteur devient le barycentre de trois zones de l'espace sémantique : il s'éloigne de chacune des trois requêtes au lieu d'en viser une seule. Résultat direct : le [[concepts/grounding-score]] (similarité cosinus requête ↔ passage) baisse sur toutes les requêtes à la fois. Une page pure pointe droit sur sa cible, une page diluée ne gagne nulle part.

Corollaire mesuré en GEO : plus le contenu s'étale hors intention, moins il est cité par les moteurs génératifs. La longueur sans pureté est un handicap, pas un signal d'autorité.

## Le rôle de la FAQ

La pureté du corps ne t'interdit pas les ouvertures connexes : elles vont en FAQ. Sur une page backlinks, une question FAQ "backlinks vs contenu" est légitime parce qu'elle capte une micro-intention adjacente sans tirer le vecteur du corps hors de sa cible. Le corps reste pur, la FAQ absorbe la périphérie.

## Exemples concrets (verbatim bootcamp)

- **"agence SEO"** : la page répond à "comment choisir la bonne agence", pas "voici aussi notre outil d'audit + nos cas clients tous secteurs".
- **Page Zinédine Zidane** : tu peux mentionner l'équipe de France, tu ne déroules pas tous les clubs ni tous les joueurs. L'entité centrale reste Zidane.

## Articulation avec les autres concepts

- **[[concepts/grounding-score]]** : la pureté vectorielle est la condition d'entrée pour un Grounding Score haut. Page diluée = cosinus plat partout.
- **[[concepts/surprise-gap]]** : une page pure peut concentrer son information manquante sur une seule cible au lieu de l'éparpiller.
- **[[concepts/passage-ranking]]** : un corps pur produit des passages de 150-200 mots tous alignés sur la même requête, donc extractibles.
- **[[concepts/answer-first-pattern]]** : answer-first + pureté = la réponse arrive vite ET ne dévie pas ensuite.
- **[[concepts/aeo]]** (Know-Simple / Know / Do) : une intention par page = un format par page. Mélanger les intentions casse aussi le mapping format ↔ intention.

## Limites

- Concept de discipline éditoriale, pas de seuil chiffré : "pure" reste un jugement de praticien.
- Sorti en transcript bootcamp, pas encore confronté à une source tierce ni à un test A/B dans cette KB.
- Le découpage "une intention" suppose un travail d'intention amont propre (cf. brief) : mal défini en amont, la pureté ne se mesure pas.

## Pages liées

[[concepts/grounding-score]] · [[concepts/surprise-gap]] · [[concepts/passage-ranking]] · [[concepts/answer-first-pattern]] · [[concepts/aeo]] · [[concepts/anti-ai-writing]] · [[raw/bootcamp4/session-2-redaction-transcript]] · [[raw/bootcamp4/session-2-redaction-debrief]] · [[raw/bootcamp4/session-2-redaction-resume-participants]]
