# Pré-audit prospection — Origin 137 (o137.ai)

> Cible : Hugo Beninca, cofondateur et CEO (LinkedIn perso, fichier J1).
> Usage : la partie « Mini-audit » se partage telle quelle (message, PDF ou trame de Loom). La partie « Approche » reste interne.
> Relevé du 2026-07-04. Analyse longue en appui : [[../../../raw/organikk/pré-call/origin137]].
> ⚠️ Avant tout envoi : la page /a-propos affiche « Alexandre Dupont, Fondateur » alors qu'on écrit à Hugo Beninca. Clarifier.

---

## Mini-audit (partageable)

**Ce qu'on a regardé.** Votre site, votre sitemap, votre robots.txt et une dizaine de pages, le 4 juillet 2026. Pas d'accès à votre Search Console, donc aucun chiffre de trafic avancé ici : uniquement ce qui est public et vérifiable.

**Le constat en une phrase : la machine est construite, c'est la conversion qui n'est pas branchée.**

Ce qui est au-dessus de la moyenne (et rare) :

- 137 URLs propres, sitemap mis à jour le 3 juillet, un llms.txt en place et un robots.txt qui accueille explicitement GPTBot, ClaudeBot et PerplexityBot. Presque personne ne fait ça.
- 3 patterns de pages déjà lancés : 9 pages « agence IA » par ville avec du vrai contenu local, 12 pages expertise, 8 pages secteur.

Les 3 trous qui vous coûtent des demandes entrantes :

1. **Vos preuves sont anonymes.** Vos 4 case studies disent « groupe média », « ETI finance », pendant que votre home affiche Sodexo, ENGIE, Thales. Un DSI qui compare atterrit sur des pages qui ne peuvent pas closer. Une seule autorisation client pour passer un case study en nominatif vaut plus que dix pages neuves.
2. **Votre data dort.** Vous revendiquez 47+ agents IA en production. Délais réels de mise en production, coûts constatés, causes d'échec des POC repris : personne en France n'a publié cette étude. C'est exactement le contenu que ChatGPT et Perplexity citent quand un décideur demande « combien coûte un projet IA ». Vous avez le carburant, il n'est pas exploité.
3. **Vos expertises et vos secteurs ne se croisent jamais.** « RAG banque », « agents IA industrie », « computer vision pharma » : ce sont les requêtes d'un acheteur en phase de décision, et aucune page n'y répond alors que vos cas d'usage taggés par secteur fournissent déjà la matière. 25 à 30 pages à faible concurrence, priorisées sur vos cas réels.

**Par quoi commencer.** L'étude d'abord (elle règle le problème de preuve et alimente les citations IA), le croisement expertise × secteur en parallèle dès la semaine 3, l'extension des villes ensuite. À 90 jours, la mesure se fait dans votre Search Console et sur les citations IA, pas au ressenti.

---

## Approche (interne)

**Note de connexion (≤ 300 caractères).**
> Salut Hugo, j'ai regardé o137.ai en creusant les intégrateurs IA : un des rares sites FR avec un vrai llms.txt et des pages villes qui tiennent. Par contre vos case studies anonymes cassent la chaîne. J'ai 3 constats précis si ça t'intéresse. On se connecte ?

**1er message après acceptation.**
> Merci pour le lien Hugo. Ce que je voyais : votre socle SEO est déjà au-dessus de la moyenne (sitemap frais, llms.txt, 9 pages villes correctes), donc je ne vais pas te pitcher du SEO de base. Les 3 trous que j'ai relevés : case studies anonymisées alors que la home affiche Sodexo et Thales, vos 47 agents en production qui ne nourrissent aucune étude publiée, et zéro page sur les croisements type « RAG banque ». Je t'envoie le détail en 1 page ou en Loom de 4 min, comme tu préfères. Au fait, le site vous ramène combien de rendez-vous par mois aujourd'hui ?

**Loom (si demandé).** Partage d'écran sur leurs pages : /agence-ia/lyon (montrer que c'est bien), une case study anonyme (montrer le trou), /cas-usage (montrer la matière du croisement). Dérouler les recos 1-2-3. Finir sur la question GSC.

**Freins probables.** « On gère le contenu en interne » → tant mieux, la machine tourne, on la pointe vers ce qui convertit et ce que les IA citent. « Le SEO on connaît » → c'est visible, et c'est pour ça que le sujet est la preuve et les citations IA, pas le SEO de base. « Pas le temps » → tout est async, Loom + WhatsApp, zéro réunion.
