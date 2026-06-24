---
type: query
title: "Mots-clés que les IA ne peuvent pas manger (matière newsletter)"
aliases: [mots-cles-que-l-ia-ne-mange-pas, kw-non-cannibalisables, newsletter-ia-ne-mange-pas]
tags: [newsletter, geo, aeo, mots-cles-actionnels, product-led, data-proprietaire, ai-overview, cannibalisation]
created: 2026-06-24
updated: 2026-06-24
sources: 6
confidence: high
status: draft
---

# Mots-clés que les IA ne peuvent pas manger

Note de matière pour une édition de newsletter. Tout ce que le vault dit sur le sujet, recoupé et sourcé. Voix de travail, pas encore la voix d'édition.

## Le point de départ : ta propre phrase

L'expression vient de toi, en clair, dans le call Leexi du 21 mai 2026 :

> "Il faut qu'on trouve tous les mots-clés que ChatGPT ne peut pas vous manger. Parce que demain, si tu tapes « meilleur logiciel de prise de notes », il va te lister les logiciels, mais est-ce que tu fais un clic derrière ? Pas forcément. (...) Tous les mots-clés informationnels qui vont être mangés par les IA, on ne récupérera aucun clic." [[sources/leexi-call-2026-05-21]]

C'est la thèse centrale. Un mot-clé est "mangé" quand le moteur génératif répond à la place du site, dans son interface, sans renvoyer de clic. La question n'est pas d'être visible, c'est de savoir si la requête laisse encore une raison de cliquer. [[concepts/tabou-visibilite]]

## Le mécanisme : ce que l'IA mange, ce qu'elle laisse

L'IA répond bien aux requêtes où l'utilisateur veut **lire** ("qu'est-ce que X", "top 10 des Y"). Elle ne répond pas à la place du site quand l'utilisateur veut **faire** : calculer, simuler, comparer sur ses propres chiffres, décider, demander un devis, tester un outil. [[concepts/mots-cles-actionnels]]

D'où le terme signature : le **mot-clé actionnel**, à la fois décisionnel et transactionnel. L'utilisateur attend une action à la fin (contact, démo, téléchargement, devis, achat), pas juste une information. Ce sont les requêtes qui survivent à l'IA parce que la réponse n'est pas un paragraphe, c'est un geste. [[concepts/mots-cles-actionnels]]

## La donnée qui tranche : la prévalence des AI Overviews dépend du type d'intention

C'est le chiffre qui rend la newsletter solide, et il est contre-intuitif. L'étude Seer Interactive (24 avril 2026, 53 marques, 5,47 millions de requêtes) mesure la fréquence d'apparition de l'AI Overview par type de requête :

| Type de requête | Prévalence AI Overview |
|---|---|
| Informationnelle | 36 % |
| Commerciale | 8 % |
| Transactionnelle | 5 % |
| Comparaison ("meilleur X", "X vs Y") | 95,4 % |
| Question ("comment faire X") | 85,9 % |

Source : [[concepts/metriques-visibilite-geo]] via l'édition [[revues-presse/2026-06-16]]. Lecture directe : une requête transactionnelle a 5 % de chances de croiser un AIO, une requête de comparaison en a 95 %. Le terrain transactionnel est presque vierge d'IA. Le terrain de la comparaison générique est saturé.

Deuxième couche de la même étude : sur les requêtes **sans** AI Overview, le CTR organique monte (de 2,93 % à 3,97 % en douze mois). Ce segment ne disparaît pas, il se concentre sur les gens qui ont déjà décidé de cliquer. Les mots-clés que l'IA ne mange pas valent donc mécaniquement plus cher au clic. [[revues-presse/2026-06-16]]

## Le piège à désamorcer : "comparatif" n'est pas un bloc homogène

Tension à traiter franchement dans l'édition, sinon un lecteur attentif la verra. Toi tu recommandes les pages de bascule ("passer de Fathom à Leexi", "passer de Whisper à Leexi") [[sources/leexi-call-2026-05-21]]. Or Seer dit que les requêtes de comparaison sont mangées à 95 %. Et l'étude Averi (8 juin 2026, 12 mois de GSC) montre une page "AirOps alternatives" à 0,02 % de CTR, 77 967 impressions pour 17 clics. [[revues-presse/2026-06-08]]

La résolution n'est pas que "le comparatif est mort". Elle est qu'il y a deux objets différents derrière le même mot :

- **Le comparatif éditorial generique** ("meilleur logiciel de X", "X alternatives" en listicle) : un LLM produit 80 % de la page tout seul, il connaît les acteurs et génère la liste dans l'AIO. Page substituable, donc mangée. C'est exactement le cas Averi.
- **La page de bascule décisionnelle** ("passer de X à Y") portée par de la data propriétaire (preuves clients réelles, captures, chiffres internes) et un point de conversion (récupérer un email) : l'intention est d'agir, pas de lire un classement. Ce n'est pas le même mot-clé même si le mot "comparatif" traîne autour.

Le test qui sépare les deux est le test de substitution. [[concepts/test-substitution-llm]]

## Les deux filtres pour décider d'attaquer un mot-clé ou pas

**Test de substitution LLM (filtre 80 %).** Pour chaque idée de page, demander à un LLM de produire la réponse. S'il produit 80 % de la page, ne pas la créer : elle n'a aucun avantage défensif. [[concepts/test-substitution-llm]]

**Test ChatGPT en 2 questions.** Q1 : est-ce que ChatGPT peut répondre à cette requête ? Q2 : si oui, peut-il faire mieux que toi ? Oui aux deux : la page est morte avant d'exister. Sinon : opportunité, surtout si l'intention est une action. [[concepts/mots-cles-actionnels]]

Les deux disent la même chose sous deux angles : un mot-clé survit à l'IA quand sa réponse exige quelque chose que le modèle n'a pas, soit une donnée propriétaire, soit un outil qui s'exécute.

## Où ils se trouvent : pas dans Semrush, dans ta data

Les mots-clés actionnels ne sont pas dans les outils SEO classiques, parce que tout le monde y a accès et qu'un LLM peut les ressortir aussi. Ils sont dans ta data propriétaire : calls clients, tickets SAV, chat support, avis G2/Trustpilot, champ "raison du deal perdu" du CRM, commentaires LinkedIn, GSC croisée avec les deals closed. [[concepts/data-proprietaire]] [[concepts/mots-cles-actionnels]]

Ta formulation dans le call : "La data propriétaire que tu as, toi, moi je ne l'ai pas. On se battra sur les mêmes mots-clés, sauf les mots-clés propriétaires que tu as, toi." [[sources/leexi-call-2026-05-21]] C'est le moat. Un nouvel entrant copie ton outil en dix minutes sur Claude Code, il ne copie pas dix ans de calls clients.

## Le format qui défend pour de bon : la page est l'outil

L'extrême du test de substitution, c'est le Product-Led SEO : la page embarque le composant fonctionnel (calculateur, simulateur, configurateur, comparateur sur données réelles). L'AI Overview peut résumer un texte, il ne peut pas exécuter ton calculateur dans la SERP. [[concepts/product-led-seo]]

Et l'outil ne sert pas qu'à défendre le mot-clé. Il récupère un email et il envoie à Google un signal d'engagement (l'utilisateur uploade, joue avec l'outil). [[sources/leexi-call-2026-05-21]] La requête "outil gratuit de X" force d'ailleurs ChatGPT à renvoyer vers une vraie page outil, là où "meilleur logiciel de X" ne renvoie qu'une liste.

## Le cadrage business à garder en tête

Sur 100 personnes qui cherchent, 90 veulent comprendre, 10 sont prêtes à agir. [[raw/bootcamp4/exercices/exercice-skill-seo-mots-cles-decisionnels]] Le travail consiste à isoler les 10, et à transformer une partie des 90 en emails via un outil ou une page-problématique. Chaque page a un intérêt mesurable (un email, un lead), pas un score de visibilité. [[concepts/tabou-visibilite]]

Ordre d'attaque des mots-clés : décisionnel d'abord (meilleur, comparatif de bascule, avis), actionnel (la page attend un geste), transactionnel (achat), informationnel en dernier. [[raw/bootcamp4/session-3-audit-resume-participants]]

## Angles d'édition possibles

- Angle "le chiffre qui retourne l'intuition" : 5 % d'AIO sur le transactionnel contre 95 % sur la comparaison. Ouvrir là-dessus, dérouler le reste.
- Angle "le test que tu peux faire en 30 secondes" : le test ChatGPT 2 questions, appliqué en direct sur trois mots-clés du lecteur.
- Angle "pourquoi ta page comparatif est à 0,02 % de CTR" : partir du cas Averi, expliquer substituable vs défendable.
- Angle "la seule liste de mots-clés que personne ne peut te copier" : la data propriétaire comme moat.

## Sources mobilisées

```
[[sources/leexi-call-2026-05-21]] — la phrase fondatrice + cadrage email/outil/data propriétaire (verbatim Tim)
[[concepts/mots-cles-actionnels]] — terme signature, test ChatGPT 2 questions, où trouver les kw
[[concepts/test-substitution-llm]] — filtre 80 %, cas Victoria Garden (5 validées / 2 rejetées)
[[concepts/product-led-seo]] — la page EST l'outil, défense la plus solide face aux LLM
[[concepts/data-proprietaire]] — le moat, 5 types de data propriétaire
[[concepts/tabou-visibilite]] — bannir "visibilité", vendre des leads
[[revues-presse/2026-06-16]] — étude Seer : prévalence AIO par type d'intention (le tableau)
[[revues-presse/2026-06-08]] — étude Averi : cas page "alternatives" à 0,02 % de CTR
```

## Gaps identifiés

- Pas de chiffre first-party à toi sur la prévalence AIO par intention (tout vient de Seer/Averi, panels externes). Un relevé maison sur une propriété GSC réelle rendrait l'édition imparable. À croiser avec [[project_etudes_originales]] (étude CTR x AI Overviews GSC déjà prévue).
- Le seuil 80 % du test de substitution est qualitatif, jamais mesuré. L'édition peut l'assumer comme heuristique, pas comme métrique.
- Manque un exemple chiffré de page-outil qui a tenu (CTR maintenu) pour équilibrer le cas Averi négatif. Golfiller pourrait servir si data dispo. [[project_golfiller]]

## Queries dérivées

- "Quels mots-clés de bascule (passer de X à Y) survivent réellement à l'AIO selon la GSC ?"
- "Liste des formats de page qui passent le test de substitution, classés par coût de production"
- "Comment mesurer en GSC la part de mes impressions qui partent sur des requêtes mangées par l'AIO"
