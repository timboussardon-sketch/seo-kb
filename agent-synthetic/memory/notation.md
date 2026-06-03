# Notation des infos — grille de sélection (Brèves + Algorithme)

Définie avec Tim le 2026-06-03. Sert à choisir les meilleures infos, pas seulement des infos « publiables ». Lue avant la sélection, appliquée à chaque candidat, loggée dans `ledgers/breves_scores.jsonl`.

## Portes (binaires — si une échoue, rejet direct, pas de note)

1. **Périmètre** : search / IA / SEO / GEO / AEO / moteurs. Test : « est-ce que ça change la façon dont on est trouvé, lu ou cité dans un moteur ? ».
2. **Sourçable** : au moins une source réelle consultable, et **zéro chiffre, %, date ou citation non sourcé** (anti-hallucination, non négociable).
3. **Fraîcheur** (ajoutée 2026-06-03, retour Tim) : le fait, la donnée ou l'étude date de **moins de ~30 jours**, OU porte un développement neuf daté. Un fait ancien qui a déjà tourné partout (ex. « Google sous 90 % », annoncé début 2026) est **écarté**, même s'il scorerait haut sur le fond. Le déjà-vu, c'est non. Corollaire sur la note : un fait vieux / déjà largement diffusé plafonne **Original ≤ 2**.

## Note de sélection — 4 critères, notés 0-5, **poids égal**, moyenne

| Critère | Ce qu'on note | 5 | 1 |
|---|---|---|---|
| **Solidité** (vérifié + sourcé) | Qualité de la preuve | Source primaire + recoupée par 2 sources indépendantes | Mono-source secondaire / relevé d'agence non confirmé |
| **Envie d'en savoir plus** | Le hook, la tension | On veut lire la suite | Annonce plate, déjà digérée |

**Précisions calibrées (retour Tim 2026-06-03) :**
- *Solidité* : une donnée d'agence **corroborée par ≥2 agences indépendantes concordantes** vaut **4**, pas 3. Le 3 ne vise que la source d'agence **unique / non recoupée**. Ne pas confondre « agrégé » et « fragile ».
- *Envie* : une **bascule de hiérarchie entre moteurs** (part de trafic/marché, qui dépasse qui) est une grosse info structurelle → **Envie 5**. Ne pas sous-noter les faits structurels au profit du spectaculaire.
- *Envie — info trop technique / infra* : une info qui repose sur une **métrique technique ou un détail d'infrastructure** (ratios de crawl, robots.txt, protocoles, parts de crawlers, schéma) plafonne **Envie ≤ 2**, sauf angle business clair et immédiat. Le lecteur est un consultant SEO, pas un ingénieur réseau. (Retour Tim : « trop technique » sur l'asymétrie crawl/referral.)
- *Envie — conseil opérationnel / hygiène* : un « optimisez/complétez X » (remplir ses attributs produit, nettoyer son feed), même avec un multiplicateur chiffré, n'a pas de tension → **Envie ≤ 2**. Ce n'est pas une info, c'est une todo. (Retour Tim : « inintéressant » sur la complétude des données produit.)
- *Original / Fraîcheur* : un fait qui a **déjà tourné partout** ou qui date de **plusieurs semaines** plafonne **Original ≤ 2** et tombe sous la porte Fraîcheur. (Retour Tim : « j'ai déjà vu, c'est vieux » sur Google sous 90 %.)
- *Événement frais ≠ déjà-vu thématique* : un **événement neuf, concret et à enjeu** (un procès, un accord, un lancement) n'est PAS du déjà-vu même si le thème large est connu. Ne pas pénaliser l'Original pour la familiarité du thème quand l'événement lui-même est récent et conséquent. Le déjà-vu ne vise que les **stats/études recyclées**. (Retour Tim : a adoré CNN vs Perplexity que j'avais coupé à tort.)
- *Niche / produit* : une news de **cycle de vie produit ou d'inside-baseball** (un produit fermé, renommé, fusionné) sans conséquence large pour qui veut être trouvé/cité plafonne **Pertinence/Doctrine ≤ 2**. (Retour Tim : « trop niche » sur la fermeture de Project Mariner.)

## Profil de goût de Tim (dérivé des verdicts du 2026-06-03)

**Aime (vise haut sur ces familles) :**
- **Conflits éditeurs/créateurs vs moteurs IA** : procès, licences, copyright, qui contrôle et monétise le contenu, droit de citation. Forte tension + enjeu direct pour ceux qui produisent du contenu. (Ex. adoré : CNN attaque Perplexity.)
- **Bascules de marché / hiérarchie** : qui dépasse qui, part de trafic, fragmentation des moteurs. (Ex. adoré : Gemini dépasse Perplexity.)
- **Données de résultat business** : conversion, revenu, comportement d'achat liés au search/IA. (Ex. 5/5 : le trafic IA convertit mieux que l'organique.)
- **Contre-vérités mesurées** : un signal réputé clé qui s'effondre. (Ex. l'autorité de domaine ne corrèle plus.)
- **Nouveaux business / modèles en SEO-GEO** : opportunités économiques émergentes, nouveaux services, nouvelles façons de monétiser, outils ou marchés naissants ouverts par le search IA. « Quel nouveau métier / revenu ça crée ? »
- **Tendances GEO/SEO sur les réseaux sociaux** : ce qui monte dans la communauté et la voix des praticiens/utilisateurs (LinkedIn, X, Reddit) — débats, retours de terrain, sentiment, méthodes qui émergent, par rapport au discours officiel. Le signal social avant qu'il ne devienne consensus.

**Rejette :**
- **Technique / infra** : ratios de crawl, pay-per-crawl, codes 402, robots.txt, protocoles, parts de crawlers. « Trop technique ».
- **Conseil opérationnel / hygiène** : « complétez vos attributs », « optimisez votre feed ». « Inintéressant ».
- **Niche / produit** : fermeture/renommage d'un produit sans portée large. « Trop niche ».
- **Vieux / déjà-vu** : stat ou étude qui a déjà tourné partout, fait de plusieurs semaines.
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
