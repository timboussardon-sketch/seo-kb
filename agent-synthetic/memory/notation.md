# Notation des infos — grille de sélection (Brèves + Algorithme)

Définie avec Tim le 2026-06-03. Sert à choisir les meilleures infos, pas seulement des infos « publiables ». Lue avant la sélection, appliquée à chaque candidat, loggée dans `ledgers/breves_scores.jsonl`.

## Portes (binaires — si une échoue, rejet direct, pas de note)

1. **Périmètre** : search / IA / SEO / GEO / AEO / moteurs. Test : « est-ce que ça change la façon dont on est trouvé, lu ou cité dans un moteur ? ».
2. **Sourçable** : au moins une source réelle consultable, et **zéro chiffre, %, date ou citation non sourcé** (anti-hallucination, non négociable).

## Note de sélection — 4 critères, notés 0-5, **poids égal**, moyenne

| Critère | Ce qu'on note | 5 | 1 |
|---|---|---|---|
| **Solidité** (vérifié + sourcé) | Qualité de la preuve | Source primaire + recoupée par 2 sources indépendantes | Mono-source secondaire / relevé d'agence non confirmé |
| **Envie d'en savoir plus** | Le hook, la tension | On veut lire la suite | Annonce plate, déjà digérée |

**Précisions calibrées (retour Tim 2026-06-03) :**
- *Solidité* : une donnée d'agence **corroborée par ≥2 agences indépendantes concordantes** vaut **4**, pas 3. Le 3 ne vise que la source d'agence **unique / non recoupée**. Ne pas confondre « agrégé » et « fragile ».
- *Envie* : une **bascule de hiérarchie entre moteurs** (part de trafic/marché, qui dépasse qui) est une grosse info structurelle → **Envie 5**. Ne pas sous-noter les faits structurels au profit du spectaculaire.
| **Original** | Fait ou nuance neuf | Personne ne l'a dit comme ça | Repris partout depuis 3 jours |
| **Doctrine / orienté SEO-IA** | Lien aux 4 piliers + cœur search | Change comment on est trouvé/cité, colle à la doctrine | Périphérique, lien décoratif |

## Bonus

- **+0,5** si l'info **casse un consensus établi** (angle contrarien, contredit une croyance répandue). Jamais une pénalité pour une bonne info consensuelle. Moyenne capée à 5.

## Seuil

- **Retenu si moyenne (bonus inclus) ≥ 4,5/5.**
- En dessous → écarté. Si moins de 10 brèves atteignent 4,5, **élargir la veille** (étape 2 du skill), jamais descendre le seuil.
- Variante possible plus tard : marquer « top » à ≥ 5,0.

## Boucle de calibration

- Chaque candidat (gardé ou écarté) est loggé dans `ledgers/breves_scores.jsonl` : 4 notes + bonus + moyenne + verdict + raison.
- Quand Tim annote une édition (`top` / `garde` / `coupe`), comparer ses verdicts à mes notes, repérer les écarts systématiques (ex. je sur-note l'« original », je sous-note le « hook »), et ajuster mon échelle. Consigner l'ajustement ici et dans `calibration.md`.
- Les poids sont égaux par défaut ; ils ne changeront qu'avec des données de calibration suffisantes, jamais au feeling.
