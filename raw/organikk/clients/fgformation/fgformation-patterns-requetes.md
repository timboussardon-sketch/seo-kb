---
client: FG Formation
type: Reverse engineering des modèles de requêtes (corpus pSEO) — skills seo-programmatique-pseo + seo-modeles-pseo
source: [[fgformation-personas-problematiques]] · [[fgformation-modeles-pseo]] · [[fgformation-mots-cles]]
date: 2026-07-14
relié: [[fgformation]]
---

# Modèles de requêtes — reverse engineering du corpus FG Formation

> **En résumé.** On sort ici la grille des **patterns de requêtes** qui structurent le sujet Qualiopi / NDA / CPF sur Google, Wikipédia, Reddit, YouTube, les forums, les FAQ et les bases de connaissances. Chaque pattern est un moule : une structure de requête que des humains tapent réellement, réutilisable pour produire du contenu à l'échelle. L'objectif n'est pas la page isolée, c'est le **corpus** : le bot (Google et les LLM) a besoin de couvrir tout l'espace d'entités autour de FG Formation (indicateurs, financements, statuts, professions, secteurs, situations). Les pages en sont le sous-produit. On distingue les patterns qui **nourrissent le corpus** (définition, liste, chronologie, statistiques) de ceux qui **convertissent** (coût, choix, cas d'usage décisionnel). Deux arbres partout : formateur indépendant / organisme de formation. Aucun volume inventé, chiffres en `[À SOURCER]`.

---

## 1. D'où viennent ces patterns (méthode)

Un pattern de requête n'est pas inventé, il est observé. Le reverse engineering se fait à deux niveaux distincts, qu'on confond souvent.

**Niveau 1 — la charnière interrogative (ce que l'humain tape).** C'est la surface : « c'est quoi », « comment », « combien », « faut-il », « qui », « pourquoi ». Elle donne l'intention brute.

**Niveau 2 — le moule structurel implicite (comment la plateforme organise la réponse).** C'est le vrai gisement. Chaque plateforme a industrialisé, sur des millions de pages, une poignée d'architectures de contenu répétables. Ce sont ces gabarits qu'on lit à rebours, parce qu'ils sont déjà validés par le clic et cités par les LLM. Voici les moules par source.

- **Google** (autocomplete, People Also Ask, recherches associées). Charnières explicites : « c'est quoi », « comment », « combien », « faut-il », « quelle différence entre ». Moules implicites : le **PAA en escalier** (une question en ouvre trois autres — chaque bloc PAA est un plan de FAQ tout fait), le **featured snippet** (paragraphe-réponse de 40-60 mots, liste numérotée ou tableau, que Google extrait littéralement), les **recherches associées** en bas de page qui exposent les variables voisines (métier, statut, dispositif) — c'est-à-dire les colonnes de nos moteurs pSEO.
- **Wikipédia**. Charnière : « qu'est-ce que ». Moules implicites, les plus cités par les LLM : l'**infobox** (fiche-entité normée : nom, type, autorité de tutelle, date de création, cadre légal), la section **« Historique »** (chronologie datée), **« Cadre juridique / réglementation »**, **« Liste de »**, le **tableau récapitulatif**, et **« Voir aussi »** (le maillage d'entités voisines). Ces sept moules sont le squelette d'une page d'autorité.
- **Reddit** (r/AutoEntrepreneur, r/entrepreneur, r/smallbusiness, groupes formateurs FB/LinkedIn). Charnières : « quelqu'un a déjà fait… ? », « ça vaut le coup ? ». Moules implicites lisibles dans les **formats de titres** : `[Serious]` (question sérieuse), `PSA:` (mise en garde partagée), `Is X worth it?` (validation d'investissement), `Anyone else…?` (recherche de pairs), `Rant:` (frustration = objection brute), le **weekly/help thread** (dépannage récurrent). Chaque format = un registre de page (avis, mise en garde, ROI, objection).
- **YouTube**. Charnière : « comment ». Moules implicites dans les **titres qui performent** : `X en Y minutes` (format court time-boxed), `X vs Y` (comparaison filmée), `J'ai testé X pendant N jours` (retour d'expérience), `À regarder avant de faire X` (mise en garde), `X expliqué simplement`, `X pour débutants`, `Arrête de faire X`. Ces gabarits se transposent tels quels en H1 d'article + vidéo intégrée (stratégie signaux du client).
- **Forums métier** (formateurs pro, création d'entreprise, Digiforma community). Moule implicite : le **titre de thread = erreur précise + contexte daté** (`NDA refusé motif 4.2, que faire ?`, `[Résolu] EDOF bloqué depuis 3 semaines`). Le tag `[Résolu]` signale une page-solution complète à répliquer. Registre : dépannage à ROI conversion élevé.
- **FAQ et bases de connaissances** (France Compétences, DREETS, Digiforma, Qualiopi.gouv). Moules implicites : la **question atomique oui/non** en accordéon, la **définition de sigle** normée, le **glossaire** entier. Le registre le plus facile à industrialiser et le plus cité en réponse directe par les moteurs génératifs.
- **Sites d'autorité / éditeurs SaaS du secteur** (guides Digiforma, Walter Learning, blogs OF). Moules implicites : le **guide pilier** (`Guide complet de X`, `X : tout ce qu'il faut savoir`, `X 101`), le **roundup** (`Les N meilleurs / les N erreurs / les N étapes`), la **page pilier + cluster FAQ**. C'est le format qui capte le maillage et pose l'autorité de tête de cluster.

Le filtre reste celui de la doctrine : on ne retient un pattern que si un humain, seul, taperait vraiment cette requête. Les labels SEO artificiels (« prix comparatif solution qualiopi ») sont exclus. Un moule structurel (infobox, roundup, PAA en escalier) n'est pas une requête : c'est le **gabarit de la page** qui répond à la requête — on l'utilise pour structurer, jamais comme H1.

---

## 2. Les patterns par intention

Pour chaque pattern : la structure, pourquoi il existe (l'intention derrière), le type de contenu qu'il permet de produire, et des exemples appliqués à FG. Les variables entre crochets `[...]` sont alimentées par la matière réelle du vault (métiers de formateur, secteurs, professions réglementées, statuts, financements, indicateurs Qualiopi).

### A. Définition / lexique — intention *définition* (source : Wikipédia, FAQ, bases de connaissances)

**Structure :** `qu'est-ce que [entité]` · `[sigle] c'est quoi` · `[sigle] définition` · `[sigle] signification`

**Pourquoi il existe :** le sujet est saturé de sigles opaques (NDA, EDOF, RNCP, RS, BPF, OPCO, DREETS, Qualiopi). Le débutant total (persona P3) ne peut rien décider tant qu'il n'a pas le vocabulaire. C'est la porte d'entrée du corpus : ces pages posent les entités que le reste du site va relier.

**Contenu produit :** fiche courte, réponse en une phrase dès l'ouverture, définition + à quoi ça sert + qui est concerné + lien vers la page d'action. Format idéal pour être cité par les LLM.

**Exemples FG :**
1. `qu'est-ce qu'un NDA formateur`
2. `EDOF c'est quoi`
3. `différence entre RNCP et RS`
4. `BPF bilan pédagogique et financier définition`
5. `qu'est-ce qu'un audit de surveillance Qualiopi`

### B. Liste / énumération — intention *liste* (source : Wikipédia, bases de connaissances)

**Structure :** `liste des [éléments]` · `[nombre] [éléments] de [sujet]` · `quels sont les [éléments]`

**Pourquoi il existe :** l'internaute veut l'inventaire exhaustif avant de se lancer, pas un article qui tourne autour. Qualiopi se prête parfaitement à ce moule car le référentiel est une liste normée (7 critères, 32 indicateurs, pièces à fournir).

**Contenu produit :** page-inventaire structurée, un bloc par élément, tableau récapitulatif en tête. Excellent pour le corpus : couvre mécaniquement tout l'espace d'un sous-sujet.

**Exemples FG :**
6. `liste des 32 indicateurs Qualiopi`
7. `quels sont les 7 critères Qualiopi`
8. `liste des pièces à fournir pour un dossier NDA`
9. `quels financements pour une formation professionnelle` (CPF, OPCO, FIPU, France Travail…)
10. `documents à préparer pour un audit Qualiopi`

### C. Chronologie / historique / échéances — intention *chronologie* (source : Wikipédia, institutionnel)

**Structure :** `historique de [sujet]` · `[obligation] depuis quand` · `échéances [sujet] [année]` · `ce qui change pour [sujet] en [année]`

**Pourquoi il existe :** la réglementation formation bouge (Qualiopi obligatoire depuis 2022, évolutions du référentiel, décisions déontologiques comme la CNB fin 2023 pour les avocats). L'internaute veut savoir où on en est **maintenant** et ce qui l'attend.

**Contenu produit :** frise ou tableau daté, section « ce qui change cette année ». Fort signal de fraîcheur pour le SEO et les LLM.

**Exemples FG :**
11. `Qualiopi obligatoire depuis quelle année`
12. `ce qui change pour les organismes de formation en 2026`
13. `évolutions du référentiel Qualiopi`

### D. Statistiques / chiffres — intention *statistiques* (source : Wikipédia, études, institutionnel)

**Structure :** `chiffres [sujet]` · `taux de [métrique] [sujet]` · `combien de [population]` · `statistiques [sujet] [année]`

**Pourquoi il existe :** un chiffre attire le lien et la citation. Les journalistes, les blogueurs et les LLM reprennent les pages qui donnent une donnée sourcée. C'est un aimant à autorité pour le corpus.

**Contenu produit :** page-donnée, un chiffre par bloc, source + organisme + année obligatoires. Ne jamais inventer : `[À SOURCER]`.

**Exemples FG :**
14. `taux de refus des dossiers NDA` `[À SOURCER]`
15. `combien d'organismes de formation certifiés Qualiopi en France` `[À SOURCER]`
16. `délai moyen d'instruction d'un dossier NDA` `[À SOURCER]`

> Attention doctrine : ce pattern est puissant mais interdit sans donnée réelle. Croiser avec une étude first-party FG (ex. taux de réussite de ses accompagnements) transforme la page en donnée propriétaire non copiable.

### E. Tutoriel / procédure — intention *tutoriel* (source : YouTube, bases de connaissances)

**Structure :** `comment [action]` · `comment [action] étape par étape` · `[action] : mode d'emploi` · `comment [action] sans [obstacle]`

**Pourquoi il existe :** l'internaute passe à l'exécution et veut être guidé. C'est le registre YouTube par excellence, à coupler avec la vidéo (stratégie signaux du client).

**Contenu produit :** guide numéroté, chaque étape atomique, encart offre d'accompagnement en bas. Se décline en vidéo intégrée à l'article.

**Exemples FG :**
17. `comment obtenir la certification Qualiopi`
18. `comment déposer son NDA de formateur`
19. `comment rendre sa formation éligible au CPF`
20. `comment préparer son audit de surveillance sans stress`
21. `comment créer un organisme de formation` (par où commencer)

### F. Comparaison — intention *comparaison* (source : Google PAA, forums)

**Structure :** `[option A] ou [option B]` · `[A] vs [B]` · `différence entre [A] et [B]` · `[A] ou [B] : lequel choisir`

**Pourquoi il existe :** l'internaute hésite entre deux voies concrètes et cherche un arbitrage. Le PAA regorge de ces paires. Intention plus mûre que la définition.

**Contenu produit :** tableau comparatif honnête + verdict argumenté + CTA. Attention : jamais de comparaison de marques concurrentes (règle FG).

**Exemples FG :**
22. `RNCP en nom propre ou adossement à un certificateur`
23. `Qualiopi en nom propre, partenariat université ou portage`
24. `auto-entrepreneur ou société pour un formateur`
25. `NDA seul ou Qualiopi : par quoi commencer`

### G. Choix / meilleure option — intention *choix décisionnel* (source : Google, Reddit)

**Structure :** `quel [service] choisir pour [situation]` · `quel [service] quand on est [profil]` · `meilleur [service] pour [besoin]`

**Pourquoi il existe :** l'internaute a décidé de déléguer, il choisit un prestataire. Forte proximité conversion. C'est le cœur des Spokes décisionnels déjà scorés dans [[fgformation-modeles-pseo]].

**Contenu produit :** page-choix avec critères de décision + verdict + preuve + CTA devis/RDV.

**Exemples FG :**
26. `quel accompagnement Qualiopi choisir quand on est formateur seul`
27. `quel accompagnement pour sécuriser son audit de surveillance`

### H. Avis / retour d'expérience — intention *avis* (source : Reddit, forums)

**Structure :** `[sujet] avis` · `[sujet] retour d'expérience` · `[sujet] arnaque ?` · `quelqu'un a déjà fait [action]`

**Pourquoi il existe :** avant de payer, l'internaute cherche la preuve sociale et veut désamorcer la peur de l'arnaque. Récurrent dans les calls : le clé en main fait peur autant qu'il attire. Registre Reddit typique.

**Contenu produit :** page qui traite l'objection frontalement (cas clients, ce qui distingue un vrai accompagnement d'un certificat acheté). Angle FG : *accompagnement qui rend autonome, pas sous-traitance de la conformité*.

**Exemples FG :**
28. `accompagnement Qualiopi clé en main arnaque`
29. `les offres Qualiopi clé en main tiennent-elles à l'audit de surveillance`
30. `retour d'expérience passage Qualiopi formateur indépendant`

### I. Coût / prix — intention *prix* (source : Google, Reddit)

**Structure :** `combien coûte [service]` · `prix [service]` · `tarif [service] pour [profil]` · `[service] pas cher / petit budget`

**Pourquoi il existe :** le budget est un préalable à toute décision. Le reste à charge bloque plus que le coût total (verbatim calls). Intention nette de devis.

**Contenu produit :** page tarif avec fourchette `[À SOURCER]`, ce qui fait varier le prix, simulateur possible, CTA devis.

**Exemples FG :**
31. `combien coûte un accompagnement Qualiopi pour un formateur indépendant`
32. `prix accompagnement Qualiopi pour un organisme de formation`
33. `Qualiopi petit budget quand on démarre`

### J. Obligation oui/non — intention *analyse / vérification* (source : FAQ, Google PAA)

**Structure :** `faut-il [condition] pour [objectif]` · `[sujet] obligatoire pour [profil]` · `est-ce qu'il faut [action]`

**Pourquoi il existe :** l'internaute lève un doute réglementaire avant d'agir. Registre FAQ pur, très cité par les LLM car réponse binaire claire. **Le meilleur moule industrialisable par profession** (l'obligation déontologique varie).

**Contenu produit :** réponse oui/non tranchée dès l'ouverture, puis nuance et lien vers l'action.

**Exemples FG :**
34. `faut-il être Qualiopi pour facturer une entreprise en direct`
35. `Qualiopi obligatoire pour former des avocats` (décision CNB)
36. `faut-il un NDA pour dispenser une formation`
37. `Qualiopi est-il obligatoire pour le CPF`

### K. Éligibilité / diagnostic — intention *analyse personnalisée* (source : Google, outils)

**Structure :** `suis-je concerné par [obligation]` · `[sujet] est-ce fait pour moi` · `est-ce que je peux [action] quand [situation]`

**Pourquoi il existe :** l'internaute veut savoir si **son** cas entre dans le cadre. Point d'entrée idéal pour un outil (le quiz lead magnet « Qualiopi est-il fait pour moi ? »).

**Contenu produit :** page auto-évaluation ou quiz interactif segmentant vers le bon arbre. Fort potentiel de capture d'email (Product-Led).

**Exemples FG :**
38. `Qualiopi est-il fait pour moi`
39. `dois-je passer Qualiopi si je forme seulement des particuliers`
40. `holistique / bien-être : ma formation est-elle finançable` (réponse : non, à dire cash)

### L. Résolution de problème / dépannage — intention *déblocage urgent* (source : forums, Reddit)

**Structure :** `[problème] que faire` · `[action] refusé` · `pourquoi mon [dossier] a été rejeté` · `erreur [X] : comment corriger`

**Pourquoi il existe :** situation subie, souvent urgente, avec deadline. Le plus fort ROI conversion car l'internaute est en douleur active. SERP souvent vierges. Registre forum/Reddit « help ».

**Contenu produit :** landing diagnostic (causes du blocage + solution + offre de déblocage), CTA immédiat.

**Exemples FG :**
41. `mon NDA a été refusé que faire`
42. `dossier CPF refusé pour du 100% e-learning`
43. `j'ai perdu ma certification Qualiopi comment la récupérer`
44. `mon organisme de portage CPF a fait faillite que faire`

### M. Cas d'usage par segment — intention *identification / cas d'usage* (source : Google longue traîne)

**Structure :** `[sujet] pour [profil / secteur / statut]` · `[sujet] quand on est [métier]`

**Pourquoi il existe :** l'internaute se reconnaît dans **sa** situation précise, pas dans la page générale. C'est le principe validé (analogie hôtel Bordeaux) : une page par micro-intention. **Le plus gros moteur pSEO** : chaque variable = une page, SERP quasi vierges.

**Contenu produit :** landing dédiée à un segment, avec ses exemples et son vocabulaire propre, maillée vers la business page de son arbre.

**Exemples FG :**
45. `accompagnement Qualiopi pour formateur en [métier]` (vente, cybersécurité, coiffure, FLE, HSE, massage bien-être, management…)
46. `Qualiopi pour le centre de formation interne d'une entreprise [secteur]` (industrie, automobile, santé, BTP, IT…)
47. `Qualiopi pour un cabinet d'avocats qui forme ses pairs`
48. `Qualiopi pour un éditeur de logiciel qui forme ses clients` (cœur de « qualiopi pour PME », persona P10)

### N. Transition « passer de X à Y » — intention *changement de situation* (source : forums)

**Structure :** `passer de [état A] à [état B]` · `transférer [objet] de [A] vers [B]` · `de [statut A] à [statut B]`

**Pourquoi il existe :** l'internaute change d'état (statut juridique, mode de facturation) et craint de perdre quelque chose au passage. Intention mûre, souvent avec deadline.

**Contenu produit :** guide de transition + accompagnement sécurisé + CTA.

**Exemples FG :**
49. `passer en direct avec les entreprises sans passer par un organisme de formation`
50. `transférer son NDA d'auto-entrepreneur vers une société`
51. `passer de la sous-traitance à sa propre clientèle quand on est formateur`

### O. ROI / rentabilité — intention *validation de l'investissement* (source : Reddit, forums)

**Structure :** `[investissement] est-ce rentable` · `[sujet] vaut-il le coup` · `à partir de combien de [unité] c'est rentable`

**Pourquoi il existe :** objection classique avant l'achat, et parfois après (« la certif ne m'a pas fait travailler plus », verbatim call). L'internaute veut chiffrer le retour.

**Contenu produit :** page ROI avec cas chiffrés `[À SOURCER]`, seuil de rentabilité, angle « faut-il garder / passer Qualiopi ».

**Exemples FG :**
52. `Qualiopi est-ce rentable quand on est formateur indépendant`
53. `à partir de combien de clients Qualiopi devient rentable`
54. `faut-il garder Qualiopi si je n'ai aucune vente`

### P. Modèles & templates téléchargeables — intention *outil / ressource* (source : Google, bases de connaissances)

**Structure :** `modèle de [document]` · `exemple de [document]` · `[document] à télécharger` · `template [document]`

**Pourquoi il existe :** l'internaute veut un livrable prêt à l'emploi. Aimant à lead magnet : on donne le modèle contre un email, on accompagne pour le remplir.

**Contenu produit :** page ressource + document téléchargeable + offre de relecture / accompagnement.

**Exemples FG :**
55. `modèle de contrat de formation`
56. `exemple de programme de formation conforme Qualiopi`
57. `modèle de dossier NDA`

### Q. Checklist / procédure ordonnée — intention *procédure / préparation* (source : bases de connaissances, YouTube)

**Structure :** `checklist [objectif]` · `étapes pour [objectif]` · `dans quel ordre faire [démarches]`

**Pourquoi il existe :** l'internaute veut ne rien oublier et connaître l'ordre des démarches (confusion fréquente : SIRET → NDA → Qualiopi, on croit qu'il faut Qualiopi avant le SIRET).

**Contenu produit :** checklist actionnable + encart accompagnement.

**Exemples FG :**
58. `dans quel ordre faire SIRET, NDA et Qualiopi`
59. `checklist avant un audit Qualiopi`
60. `étapes pour devenir organisme de formation`

### R. Autorité / entité-acteur — intention *qui fait quoi* (source : Wikipédia infobox, Google « qui »)

**Structure :** `qui délivre [certification]` · `qui est [organisme]` · `qui peut [action réglementée]` · `qui contrôle [dispositif]`

**Pourquoi il existe :** le sujet est peuplé d'acteurs opaques dont l'internaute ne sait pas qui fait quoi (France Compétences, le COFRAC, les organismes certificateurs accrédités, la DREETS, la Caisse des Dépôts pour le CPF). Savoir qui délivre, qui contrôle, qui finance conditionne toute la suite. C'est le moule infobox de Wikipédia, très cité par les LLM car il pose les relations entre entités.

**Contenu produit :** fiche-entité normée (rôle, périmètre, ce qu'il délivre ou contrôle, comment on le contacte), maillée vers les autres acteurs. Nourrit fortement le corpus et le graphe d'entités que Google et les moteurs génératifs lisent.

**Exemples FG :**
61. `qui délivre la certification Qualiopi`
62. `qui sont les organismes certificateurs Qualiopi accrédités`
63. `qui peut auditer un organisme de formation`
64. `qui contrôle l'utilisation du CPF`

### S. Causalité / explication — intention *pourquoi* (source : Google « pourquoi », forums)

**Structure :** `pourquoi [obligation / phénomène]` · `pourquoi [échec fréquent]` · `pourquoi [écart constaté]`

**Pourquoi il existe :** l'internaute ne veut pas seulement quoi faire, il veut comprendre la logique — soit pour se rassurer, soit parce qu'il subit un effet qu'il ne s'explique pas (dossier qui traîne, prix qui varient du simple au triple). Registre explicatif que Google traite volontiers en featured snippet.

**Contenu produit :** page-explication answer-first (la cause en une phrase, puis le mécanisme), reliée à la page d'action correspondante.

**Exemples FG :**
65. `pourquoi Qualiopi est obligatoire`
66. `pourquoi mon dossier NDA prend autant de temps`
67. `pourquoi les prix d'un accompagnement Qualiopi varient autant`
68. `pourquoi un dossier CPF en e-learning est refusé`

### T. Mythe / idée reçue — intention *lever un doute contradictoire* (source : Reddit, forums, YouTube « la vérité sur »)

**Structure :** `[sujet] ne sert à rien` · `[affirmation fausse] vrai ou faux` · `la vérité sur [sujet]` · `[sujet] c'est une arnaque`

**Pourquoi il existe :** le secteur charrie des croyances fausses qui bloquent la décision (« Qualiopi ne sert qu'à cocher une case », « le CPF c'est fini », « il faut Qualiopi avant le SIRET »). L'internaute cherche à trancher une info contradictoire entendue ailleurs. Registre Reddit `Rant` / YouTube « la vérité sur ». Proche du pattern H (avis) mais centré sur une **croyance précise à démonter**, pas sur la réputation d'un prestataire.

**Contenu produit :** page qui énonce le mythe puis le corrige factuellement (moule « idée reçue → réalité »), angle FG honnête (ce que Qualiopi apporte vraiment, ce qu'il n'apporte pas). Fort pour désamorcer l'objection avant le CTA.

**Exemples FG :**
69. `Qualiopi ne sert à rien vrai ou faux`
70. `faut-il vraiment Qualiopi pour être payé`
71. `le CPF est-il vraiment mort pour les formateurs`

### U. Erreur à éviter / piège — intention *sécuriser avant d'agir* (source : YouTube « à regarder avant », roundups d'autorité)

**Structure :** `erreurs à éviter [action]` · `pièges [sujet]` · `ce qu'il ne faut pas faire pour [objectif]` · `à savoir avant de [action]`

**Pourquoi il existe :** l'internaute est sur le point d'agir et veut éviter le faux pas coûteux (motif de refus classique, non-conformité qui saute à l'audit de surveillance). Moule roundup (`Les N erreurs`) très partagé et très maillé. Distinct du tutoriel E (qui dit comment faire) : ici on dit **ce qui fait échouer**.

**Contenu produit :** page-liste des pièges, un bloc par erreur (le piège + pourquoi il coûte cher + comment l'éviter), encart accompagnement. Excellent aimant à liens.

**Exemples FG :**
72. `erreurs à éviter pour un audit Qualiopi`
73. `pièges du dossier NDA`
74. `ce qu'il ne faut pas faire pour rester conforme à l'audit de surveillance`

### V. Négation / contournement — intention *atteindre l'objectif sans l'obstacle* (source : Google « sans », forums)

**Structure :** `[objectif] sans [obstacle]` · `[action] sans [prérequis supposé]` · `se passer de [contrainte]`

**Pourquoi il existe :** l'internaute veut le résultat mais cherche à éviter une contrainte qu'il croit obligatoire, ou vérifie si un raccourci existe. Intention décisionnelle très nette, souvent avec une réponse tranchée à donner cash (parfois « non, c'est impossible » — ce qui construit la confiance). Le modificateur `sans` isole des SERP vierges et des micro-intentions précises.

**Contenu produit :** page qui répond franchement (oui c'est possible sous conditions / non c'est un mythe), puis oriente vers la vraie solution et le CTA. Angle FG : dire la vérité même quand elle ferme une porte.

**Exemples FG :**
75. `former des entreprises sans être Qualiopi`
76. `faire financer une formation sans Qualiopi`
77. `dispenser une formation sans NDA`
78. `rendre une formation éligible CPF sans certification RNCP`

---

## 3. Les patterns industrialisables (les moteurs)

Un pattern est industrialisable quand sa structure accepte une **variable alimentée par une base de données réelle**, produisant N pages dont le contenu change réellement (pas seulement le H1). Les variables ci-dessous sortent toutes de la matière FG (calls, référentiel Qualiopi, réglementation), donc chaque page est ancrée et non copiable.

| Moteur (pattern × variable) | Source de la variable | Pages possibles | Intention dominante | Rôle |
|---|---|---|---|---|
| **M — Cas d'usage : `accompagnement Qualiopi pour formateur en [métier]`** | métiers vus en call (vente, cybersécurité, coiffure, FLE, HSE, massage, management, automobile, arts graphiques, sport, RSE, coaching…) | ~25-30 | Identification / cas d'usage | Conversion, arbre A |
| **M — Cas d'usage : `Qualiopi pour le centre de formation interne d'une entreprise [secteur]`** | secteurs (industrie, automobile, santé, BTP, transport, IT…) | ~10-15 | Cas d'usage | Conversion, arbre B |
| **M — Cas d'usage : `Qualiopi pour [structure réglementée]`** | association, ordre, société savante, syndicat, fédération | ~5 | Cas d'usage | Conversion, arbre B |
| **J — Obligation : `Qualiopi / formation obligatoire pour former des [profession]`** | professions réglementées (avocats, notaires, experts-comptables, médecins, experts fonciers…) | ~6-8 | Analyse / vérification | Corpus + autorité |
| **A — Lexique : `[sigle] c'est quoi` / `différence entre [A] et [B]`** | sigles et paires du domaine (NDA, EDOF, RNCP, RS, BPF, OPCO, DREETS) | ~10-15 | Définition | Corpus (pose les entités) |
| **B — Liste : `liste / rôle de l'indicateur [n] Qualiopi`** | 32 indicateurs du référentiel | ~10-32 | Liste / analyse | Corpus (autorité référentiel) |
| **I — Coût : `combien coûte [service Qualiopi] pour [profil]`** | profils × services (formateur, OF, PME × Qualiopi, NDA, audit blanc) | ~6-10 | Prix | Conversion |
| **M — Financement : `rendre une formation [domaine] finançable [dispositif]`** | domaines (IA, cybersécurité, management…) × dispositifs (CPF, OPCO, FIPU, France Travail) | ~8-12 | Cas d'usage / analyse | Corpus + conversion |
| **N — Transition : `refaire son NDA en passant en [statut]`** | statuts (SARL, EURL, SASU) | ~3 | Changement de situation | Conversion |
| **R — Acteur : `qui délivre / contrôle [dispositif]`** | acteurs (France Compétences, certificateurs, COFRAC, DREETS, Caisse des Dépôts) | ~6-8 | Autorité / entité | Corpus (graphe d'entités) |
| **U — Erreur : `erreurs à éviter pour [action]`** | actions (audit initial, audit de surveillance, dossier NDA, dossier CPF, création OF) | ~5-8 | Sécurisation | Corpus + conversion (aimant à liens) |
| **V — Contournement : `[objectif] sans [obstacle]`** | objectifs × obstacles (financer / former / CPF × Qualiopi, NDA, RNCP) | ~6-9 | Décisionnel | Conversion (SERP vierges) |

Priorité d'industrialisation : les moteurs **M cas d'usage** (métier / secteur) d'abord, car ce sont eux qui atteignent la cible ~100 pages avec la conversion la plus directe et des SERP vierges. Les moteurs **A lexique**, **B indicateurs** et **J obligation** se lancent en parallèle car ils construisent l'autorité de corpus qui fait remonter tout le reste (et alimentent les citations LLM).

---

## 4. Tableau de synthèse — tous les patterns

Potentiel SEO : Faible / Moyen / Fort. Scalabilité : nombre de pages générables avec les variables réelles FG. « — » = pattern unitaire (peu ou pas de variable).

| Pattern | Structure de requête | Intention | Potentiel SEO | Scalabilité (pages) |
|---|---|---|---|---|
| A. Définition / lexique | `qu'est-ce que [entité]`, `[sigle] c'est quoi` | Définition | Moyen | ~10-15 |
| B. Liste / énumération | `liste des [éléments]`, `quels sont les [éléments]` | Liste | Fort | ~10-32 (indicateurs) |
| C. Chronologie / échéances | `[obligation] depuis quand`, `ce qui change en [année]` | Chronologie | Moyen | ~3-5 |
| D. Statistiques | `chiffres [sujet]`, `taux de [métrique]` | Statistiques | Fort (si data) | ~5-8 |
| E. Tutoriel / procédure | `comment [action] étape par étape` | Tutoriel | Fort | ~10-15 |
| F. Comparaison | `[A] ou [B]`, `différence entre [A] et [B]` | Comparaison | Moyen | ~8-12 |
| G. Choix / meilleure option | `quel [service] choisir pour [situation]` | Choix décisionnel | Moyen | ~4-6 |
| H. Avis / retour d'expérience | `[sujet] avis`, `[sujet] arnaque ?` | Avis | Moyen | ~4-6 |
| I. Coût / prix | `combien coûte [service] pour [profil]` | Prix | Fort | ~6-10 |
| J. Obligation oui/non | `faut-il [X] pour [Y]`, `[sujet] obligatoire pour [profil]` | Analyse / vérification | Fort | ~8-12 |
| K. Éligibilité / diagnostic | `[sujet] est-ce fait pour moi`, `suis-je concerné` | Analyse personnalisée | Moyen | ~5-8 (+ quiz) |
| L. Résolution de problème | `[problème] que faire`, `[action] refusé` | Déblocage urgent | Fort | ~8-12 |
| M. Cas d'usage par segment | `[sujet] pour [métier / secteur / statut]` | Identification / cas d'usage | Fort | ~50-60 (le moteur) |
| N. Transition « passer de X à Y » | `passer de [A] à [B]`, `transférer [objet]` | Changement de situation | Fort | ~5-8 |
| O. ROI / rentabilité | `[investissement] est-ce rentable` | Validation investissement | Moyen | ~4-6 |
| P. Modèles / templates | `modèle de [document]`, `exemple de [document]` | Outil / ressource | Moyen | ~5-8 |
| Q. Checklist / procédure ordonnée | `checklist [objectif]`, `dans quel ordre [démarches]` | Procédure | Moyen | ~5-8 |
| R. Autorité / entité-acteur | `qui délivre [X]`, `qui contrôle [X]` | Qui fait quoi | Moyen | ~6-8 |
| S. Causalité / explication | `pourquoi [obligation / échec]` | Pourquoi | Moyen | ~4-6 |
| T. Mythe / idée reçue | `[sujet] ne sert à rien`, `la vérité sur [X]` | Lever un doute | Moyen | ~4-6 |
| U. Erreur à éviter / piège | `erreurs à éviter [action]`, `pièges [sujet]` | Sécurisation | Fort | ~5-8 |
| V. Négation / contournement | `[objectif] sans [obstacle]` | Décisionnel | Fort | ~6-9 |

Total brut de pages générables si tous les moteurs tournent : ~185-265. La cible réaliste (celle de Tim) reste ~100 pages en gardant les patterns au meilleur ratio autorité × conversion, en assumant que toutes ne performeront pas (logique hôtel Bordeaux).

---

## 5. Lecture corpus / GEO

Tous les patterns ne jouent pas le même rôle. Deux familles :

- **Patterns de corpus** (définition A, liste B, chronologie C, statistiques D, obligation J, indicateurs B) : ils posent les entités et couvrent l'espace du sujet. C'est ce que le bot lit pour comprendre que FG Formation fait autorité sur Qualiopi. Ils captent peu de leads directs mais font remonter tout le reste et nourrissent les citations dans ChatGPT et Google AI. Ce sont eux qui remplissent le corpus.
- **Patterns de conversion** (cas d'usage M, coût I, choix G, résolution de problème L, transition N) : ils captent le prospect mûr avec CTA devis/RDV. Ce sont les Spokes déjà scorés dans [[fgformation-modeles-pseo]].

La bonne séquence respecte la doctrine « corpus avant pages » : on lance en parallèle un socle de corpus (lexique + indicateurs + obligations par profession) qui établit l'autorité, et le moteur de cas d'usage par métier/secteur qui convertit. Les pages de conversion rankent mieux quand le corpus autour est dense.

## Prochaines étapes

1. Alimenter chaque moteur du §3 avec sa **base de variables réelle** (liste des métiers vus en call, secteurs, professions, sigles, 32 indicateurs) → passage en `seo-programmatique-pseo` pour figer template + source de données.
2. Prioriser dans la GSC FG les patterns déjà en page 2-3 (croiser avec [[fgformation-gsc-quickwins]]).
3. Sourcer les chiffres du pattern D (statistiques) via une étude first-party FG avant toute publication (jamais de chiffre inventé).
4. Brancher le pattern K (éligibilité) sur le quiz lead magnet « Qualiopi est-il fait pour moi ? ».

## Journal

- **2026-07-14** : reverse engineering des modèles de requêtes pour nourrir le corpus. 17 patterns classés par intention, ~60 exemples appliqués, 9 moteurs industrialisables adossés aux variables réelles des calls, tableau de synthèse (structure / intention / potentiel SEO / scalabilité). Distinction corpus vs conversion. Prochain : figer les bases de variables par moteur en `seo-programmatique-pseo`.
- **2026-07-14 (enrichissement)** : passage au reverse engineering de niveau 2. §1 réécrit pour distinguer la **charnière interrogative explicite** (ce que l'humain tape) du **moule structurel implicite** (l'architecture de contenu que la plateforme impose : PAA en escalier, infobox et « Voir aussi » Wikipédia, formats de titres Reddit `[Serious]`/`PSA`/`worth it`, gabarits YouTube `X en Y min`/`vs`/`à regarder avant`, titre-erreur des forums, guide pilier + roundup des sites d'autorité). 5 patterns génériques ajoutés : R (autorité/acteur « qui »), S (causalité « pourquoi »), T (mythe/idée reçue), U (erreur à éviter/piège), V (négation/contournement « sans »). 18 exemples FG supplémentaires (61→78), 3 moteurs industrialisables de plus (R acteurs, U erreurs, V contournement), total brut réévalué ~185-265 pages. Prochain inchangé : figer les bases de variables en `seo-programmatique-pseo`.
