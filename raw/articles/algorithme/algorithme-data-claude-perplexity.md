\# DATA avec Claude \+ Perplexity \- by Timothée \- Algorithme

\*\*URL:\*\* https://algorithme.substack.com/p/data-avec-claude-perplexity

\*\*Description:\*\* (data propriétaire \+ fact checking avec CLAUDE et Perplexity)

\*\*Stats:\*\* 1202 words | 27 links | 9 images

\#\# Headings (H1)

\- DATA avec Claude \+ Perplexity

\#\# Sub-subheadings (H3)

\- (data propriétaire \+ fact checking avec CLAUDE et Perplexity)

\- Tout à fait prêt. Qu'avez-vous pour moi ?

\#\# Content

DATA avec Claude \+ Perplexity \- by Timothée \- Algorithme Algorithme S'abonner Se connecter DATA avec Claude \+ Perplexity (data propriétaire \+ fact checking avec CLAUDE et Perplexity) Timothée mars 11, 2026 6 6 Partager L’IA a déjà (presque) tout lu. Tous les articles, tous les contenus génériques de votre thématique. Republier ce qui existe déjà, c’est ce qu’on appelle du Low Surprise . Le modèle LLM le lit, ne le mémorise pas, et l’oublie. Il faut le surprendre avec une information unique, nouvelle, qui peut changer la perception du lecteur. Ça ne vient pas de moi, mais de Google. Et il est formel là-dessus. Page 42 de ses Quality Rater Guidelines, il qualifie un contenu “sans effort” quand il reprend mécaniquement des informations existantes et n’apporte n’apporte aucun gain d’information. Note la plus basse. Cette information vient d’ailleurs détruire tous ceux qui s’amusent à créer du contenu IA sans contexte, sans data, sans expertise. Je le répète depuis un petit moment mais ça veut dire concrètement qu’aujourd’hui, pour être cité, il faut apporter de la data propriétaire . Ok mais comment on collecte cette data ? Un chiffre issu de votre terrain, un résultat client, une observation unique. Pas juste balancer une dinguerie, mais apporter un information gain . En sachant ça, on se rend compte que les critères de ranking d’un contenu viennent de prendre un tournant majeur. Analyse GEO sur https://organikk.co/outils/analyse-geo Ajouter une étape de Fact Checking à vos contenus Un contenu qui cite des données correctes, c’est la norme, rien d’exceptionnel aux yeux de Google. À contrario, citer une data fausse ou obsolète, et la note de votre contenu est dégradée. Il devient donc obligatoire de fact-checker ces contenus. Oui ça sonne moins sexy que générer un article SEO en un clic, mais ce qu’on veut c’est pas du sexy, c’est de la performance. 1\. Process pour récolter de la data On pourrait penser que c’est réservé aux grosses boîtes, mais que nenni. Les artisans, avocats, TPE, tout le monde est désormais concerné. Pour mieux comprendre, voici ce que fait l’IA : L’IA génère d’abord un brouillon. Ensuite, elle ne vérifie pas votre article en entier — elle l’atomise. Elle découpe chaque affirmation en fait isolé. Avec un exemple : “La Tesla Model S a une autonomie de 600 km et coûte 90 000 €.” L’IA vérifie trois atomes séparément. Atome A : le modèle. Atome B : l’autonomie. Atome C : le prix. Si vous écrivez “la Tesla est une voiture chère avec une bonne autonomie” , vous ne serez pas cités. Et c’est une super nouvelle. Cela veut dire que si je crée le même site que vous demain, sur la même thématique, si je n’ai pas d’expertise, alors je serai toujours derrière. 2\. Comment récolter et stocker ? Data \= meilleur contexte 1\. Données internes (vos projets dans Claude) : tarifs, équipements, services, procédures d’arrivée, offres promo. Ce sont les données qui viennent de vous, et donc les plus risquées à halluciner, parce que si je me trompe, ça crée une fausse promesse commerciale directement sur votre site. Ne pas scraper le web à ce stade. 2\. Données externes (sources web) : météo, événements locaux, distances, données touristiques. Ce sont des données que je vais chercher sur des sources tierces (climate-data.org, .gouv, etc.) et qui sont plus faciles à sourcer et à vérifier. Aujourd’hui de nombreuses API permettent de récolter de la bonne data. On stockera ensuite l’ensemble dans un NotebookLM ou projet Claude. Ces données pourront être réutilisées lors de la création de votre article ou pour ajouter de la data à un article existant. Deux manières de procéder : Ajouter de la data dans le contexte Ajouter de la data lors de la rédaction d’un article Dans les deux cas, il va falloir fact-checker. Quand l’IA rédige du contenu pour vous, toutes les affirmations n’ont pas le même niveau de fiabilité. Voici le tri à faire systématiquement avant de publier. La règle d’or : ce qui vous appartient ne peut être validé que par vous. Ce qui appartient à de la data scrapée par un LLM doit être validé par une source tierce. Ne mélangez pas les deux. → Prompt fact-checking (à passer sur Perplexity) Votre article est prêt, vous allez fact-checker vos articles avec ce prompt : PROMPT : Tu es un fact-checker senior spécialisé en contenus web et SEO. Ta mission : vérifier la fiabilité d’un texte (article, post, script vidéo, page de vente). Analyse le texte ci-dessous et : Isole toutes les affirmations factuelles vérifiables (chiffres, dates, classements, citations d’études, données marché, réglementations, noms d’institutions, etc.). Pour chaque affirmation, indique : a) La citation exacte (copiée du texte) b) Ton verdict : Exact / Approximatif à reformuler / Faux ou non sourçable c) Une courte justification (1-3 phrases) d) Une version corrigée/sécurisée de la phrase, si nécessaire e) Une ou deux sources externes fiables (titre \+ domaine, pas besoin d’URL complète) Contrainte méthodo importante : si tu n’es pas sûr à ≥ 80 %, classe l’info en “Approximatif / à reformuler” ou “Non vérifiable” et propose une version prudente. Ne devine pas de chiffres précis : préfère les ordres de grandeur (”environ”, “entre X et Y”, “de l’ordre de”). Format de sortie attendu (obligatoire) : Section 1 – Liste des affirmations factuelles \[Citation exacte\] Verdict : … Justification : … Reformulation proposée : … Pistes de sources : … Section 2 – Risques majeurs de désinformation Liste les 3-5 points qui posent le plus gros risque (chiffres douteux, causalités abusives, généralisation non prouvée…). Section 3 – Recommandations SEO / crédibilité Comment reformuler ou sourcer pour maximiser E-E-A-T (précision, sources primaires, datation, prudence sur les stats). Texte à fact-checker : \[COLLER ICI TON TEXTE SEO À VÉRIFIER\] Et ensuite, corrigez en fonction des résultats obtenus. Évidemment, ce que j vous donne dans cette newsletter c’est vraiment ce que j’applique au quotidien. J’ai repensé tout mon process de rédaction pour être au plus proche de ce qui est attendu par les LLMs. Ce sont 9 étapes qui s’exécutent les unes après les autres pour venir améliorer l’existant. Réservé aux plus motivés. 1/ Je construis la stratégie SEO des boites B2B et produis tous les contenus pendant 3 mois : pré-audit 3/ On construit ton propre système SEO IA avec CLAUDE : prendre un call 3/ Trouver vos meilleurs mots-clés pour Chatgpt, Youtube etc : Fusionn.io ⇢ Tu as apprécié cette édition de revue de presse et le format te plaît ? Like 💙 la newsletter pour que je puisse rédiger sur des sujets similaires. 6 6 Partager Discussion à propos de ce post Commentaires Restacks Lucas Flandre 6d Liké par Timothée Top Répondre Partager 1 réponse de Timothée Helene Landron 4d Liké par Timothée Bonjour Timothée, je t'ai écrit à propos de la facturation de fusionn pourrais-tu me répondre ? Répondre Partager 1 réponse de Timothée 4 commentaires supplémentaires... meilleur Dernier Discussions Aucun post Tout à fait prêt. Qu'avez-vous pour moi ? S'abonner © 2026 Timothée Boussardon · Confidentialité ∙ Conditions ∙ Avis de collecte Lancez votre Substack Obtenir l’app Substack est le foyer de la grande culture This site requires JavaScript to run correctly. Please turn on JavaScript or unblock scripts

\#\# Links (27)

\- https://algorithme.substack.com/

\- https://algorithme.substack.com/

\- https://substack.com/@timotheebssrdn

\- https://substack.com/@timotheebssrdn

\- https://substackcdn.com/image/fetch/$s\_\!K2cp\!,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6566675-5d5f-40f4-ad89-25e4f94f9dde\_1530x880.png

\- https://substackcdn.com/image/fetch/$s\_\!CoNi\!,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9aa52ed0-4417-49be-8968-8f98666ce18a\_1304x942.png

\- https://substackcdn.com/image/fetch/$s\_\!zNLB\!,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F47589ded-74ec-425a-8922-1914a39d5d67\_1580x536.png

\- https://organikk.co/services

\- https://cal.com/tim-boussardon-yzrrb1/30min

\- https://fusionn.io/

\- https://substackcdn.com/image/fetch/$s\_\!KK4W\!,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba615140-533e-4fa3-b15c-54ce1fc74edf\_1174x324.png

\- https://substack.com/profile/194566903-lucas-flandre?utm\_source=comment

\- https://substack.com/profile/194566903-lucas-flandre?utm\_source=substack-feed-item

\- https://algorithme.substack.com/p/data-avec-claude-perplexity/comment/226488648

\- https://algorithme.substack.com/p/data-avec-claude-perplexity/comment/226488648

\- https://substack.com/profile/9378917-helene-landron?utm\_source=comment

\- https://substack.com/profile/9378917-helene-landron?utm\_source=substack-feed-item

\- https://algorithme.substack.com/p/data-avec-claude-perplexity/comment/227118031

\- https://algorithme.substack.com/p/data-avec-claude-perplexity/comment/227118031

\- https://algorithme.substack.com/p/data-avec-claude-perplexity/comments

\- https://substack.com/privacy

\- https://substack.com/tos

\- https://substack.com/ccpa\#personal-data-collected

\- https://substack.com/signup?utm\_source=substack\&amp;utm\_medium=web\&amp;utm\_content=footer

\- https://substack.com/app/app-store-redirect?utm\_campaign=app-marketing\&amp;utm\_content=web-footer-button

\- https://substack.com/

\- https://enable-javascript.com/

\#\# Images (9)

\- \!\[Algorithme\](https://substackcdn.com/image/fetch/$s\_\!kNkO\!,w\_40,h\_40,c\_fill,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ca38a98-563a-4baf-833b-9e7c925a53a1\_1280x1280.png)

\- \!\[Avatar de Timothée\](https://substackcdn.com/image/fetch/$s\_\!ErKX\!,w\_36,h\_36,c\_fill,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2758228-4f3e-4e67-b051-4be77ee2948c\_970x970.png)

\- \!\[Image\](https://substackcdn.com/image/fetch/$s\_\!K2cp\!,w\_1456,c\_limit,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6566675-5d5f-40f4-ad89-25e4f94f9dde\_1530x880.png)

\- \!\[Image\](https://substackcdn.com/image/fetch/$s\_\!CoNi\!,w\_1456,c\_limit,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9aa52ed0-4417-49be-8968-8f98666ce18a\_1304x942.png)

\- \!\[Image\](https://substackcdn.com/image/fetch/$s\_\!zNLB\!,w\_1456,c\_limit,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F47589ded-74ec-425a-8922-1914a39d5d67\_1580x536.png)

\- \!\[Image\](https://substackcdn.com/image/fetch/$s\_\!KK4W\!,w\_1456,c\_limit,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba615140-533e-4fa3-b15c-54ce1fc74edf\_1174x324.png)

\- \!\[Avatar de User\](https://substackcdn.com/image/fetch/$s\_\!TnFC\!,w\_32,h\_32,c\_fill,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

\- \!\[Avatar de Lucas Flandre\](https://substackcdn.com/image/fetch/$s\_\!CawT\!,w\_32,h\_32,c\_fill,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81959247-667f-428e-a87f-d212c5d6f486\_1024x1024.png)

\- \!\[Avatar de Helene Landron\](https://substackcdn.com/image/fetch/$s\_\!Tfxb\!,w\_32,h\_32,c\_fill,f\_auto,q\_auto:good,fl\_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Forange.png)

\---

