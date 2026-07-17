# Prestation — Catherine

- Slug : catherine
- Domaine : consultante marketing (SEO/GEO), Canada
- Type : accompagnement 1:1 consultant (système Claude + Obsidian, calqué Alexia)
- Statut : démarrage (call découverte 2026-06-11, proposition 1 500 € HT ; espace client ouvert 2026-07-03 ; questionnaire répondu 2026-07-16)
- Offre : setup + workflows hebdo, mois 1 calls hebdo puis async

## Où on en est
Étape courante : parcours Alexia (accompagnement 1:1 consultante), pas la roadmap SEO classique. Questionnaire répondu 12/12 le 2026-07-16 ; dashboard ouvert sur Programme + Ressources (déployé 2026-07-17).
Prochaine action : **bloqué sur Catherine** — elle doit remplir ses 3 docs de contexte (liens ci-dessous). Sans eux, pas de `contexte-catherine`, donc pas de kit, donc onglet Installation fermé. Côté Tim : partager les 3 docs en édition avec elle, puis envoyer le message d'explication.

## Dette technique bloquante (identifiée 2026-07-17)
Le générateur de kit est **mono-client bien au-delà de ce qu'annonce l'Annexe A §A.9** (qui ne mentionne que `ZIP_DST` et `OUT`). En réalité :
- `build-dataset.py` porte Alexia dans `OUT`, `ZIP_DST`, `NATIVE_SKILLS` (`contexte-alexia`), le README (URL du repo GitHub), `INSTALL_PROMPT`, les textes de `WORKFLOWS` et `VOIX_RE.sub("voix-alexia")`.
- `build-vault.py` accepte bien un slug, mais exige une **baseline** (un `vault-seo-organikk.zip` déjà présent sur le dashboard du client, que Catherine n'a pas) et réinjecte `contexte-alexia` en dur (lignes ~115-116).
- Un repo GitHub `catherine-seo-kit` reste à créer (le README du kit pointe vers l'URL de clone).
Conséquence : rendre le kit multi-client est un chantier à part, à faire **avant** que Catherine ne rende ses docs, sinon on est bloqué à ce moment-là.

## Accès et data
- Drive : « Catherine — Accompagnement SEO (Organikk) » → https://drive.google.com/drive/folders/1LnOAq51lHkm7uwkYHJF3sOEmjD6SKsuh
- 3 docs de contexte (créés vierges le 2026-07-17, **à partager en édition avec elle**) :
  - about-me → https://docs.google.com/document/d/11M10CqwRY9zBuDrko-swhQ2_ICw4NieBx33UwaHTifg/edit
  - my-rules → https://docs.google.com/document/d/1VVr1ugtRC6cGp5z93HSu_O-lbrLlij44ga8SAfRH0P8/edit
  - my-voice → https://docs.google.com/document/d/1k1TriWJNQdEBY-cpyGvgGgtuFcJq-TwHutUhkjJTjug/edit
- GSC : Catherine répond « Oui » à la question 12, elle accepte de partager ses accès. Reste à récupérer l'accès concret.
- Data propriétaire reçue : transcript call découverte + résumé/proposition (raw/organikk/clients/catherine/) + réponses au questionnaire (ci-dessous)
- Outillage connu : Claude en outil principal depuis 3-4 mois (avant : ChatGPT entraîné avec projets et GPT personnalisés), Search Console, Google Analytics, SEMrush en version gratuite (le payant est coupé), Ubersuggest, PageSpeed Insights, Answer the Public, Site Checker, Yoast, RankMath, Geoptie Rank Tracker (testé en gratuit pour le GEO)

## Réponses au questionnaire — 2026-07-16
Verbatim, tel qu'elle l'a saisi dans l'espace client (`client_selections`, doc_key `catherine-accompagnement`).

**Ce qu'il faut retenir pour le cadrage**
- Sa définition de la réussite (q9) : automatiser ses process pour que sa méthode soit plus claire et plus stable. C'est le critère sur lequel elle jugera l'accompagnement.
- Son plus gros point de friction (q6, q11) : le manque de structure. Elle teste beaucoup et se promène entre les outils sans arriver à un portrait clair, et elle hésite particulièrement sur quoi utiliser côté GEO.
- Les rapports clients (q4) lui prennent 30 minutes à 1 heure chacun : elle les produit avec Claude en lui important des données d'autres outils, le résultat la satisfait mais rien n'est automatisé.
- Elle a déjà testé Claude Cowork et l'a trouvé lent, en attribuant la lenteur à son ordinateur qu'elle changera d'ici 2-3 mois.
- Client cité (q10) : Ôtruche Marketing, une agence démarrée récemment, site sous Wix — elle trouve que Wix complexifie le processus.

| # | Question | Réponse |
|---|---|---|
| q1 | Parcours SEO | « J'ai commancé il y a 8 ans, pour le site de mon employeur. En fait, je ne savais même pas que ça s'appelait du SEO au début! C'était un site très basique et j'ai commencé à l'améliorer pour que certaines pages ressortent plus rapidement dans les résultats de recherches. Je me suis lancée à mon compte il y a 4 ans comme rédactrice web et c'est là que j'ai vraiment dcouvert le SEO. Je l'offre depuis ce temps: au début plus sous forme d'optimisation de contenu, mais maintenant de façon plus globale en stratégie. » |
| q2 | Outils utilisés | « J'utilise la Search Console, Google Analytics, SEMrush (avant version payante, maintenant juste la base gratuite), Ubbersuggest (mais je trouve que ses données diffèrent beaucoup des autres outils), PageSpeed Insight, Answer the public (particulièrement pour les FAQ ou trouver des idées de contenus), Site checker (parfois), Claude, ChatGPT, Yoast, RankMath, etc. J'ai testé Geoptie Rank Tracker dernièrement pour avoir un meilleur aperçu GEO, et j'ai bien apprécié la version gratuite. » |
| q3 | Usage de l'IA | « J'ai commencé par utilisé ChatGPT que j'ai beaucoup entraîné. J'ai créé des projets et des GTP personnalisés, mais depuis 3-4 mois, je suis passée presque essentiellement sur Claude. J'ai parti mes projets et je teste beaucoup avec Claude. J'ai essayé Claude Cowork aussi, mais je le trouve assez lent (ce doit être à cause de mon ordinateur qui est à changé d'ici 2-3 mois). » |
| q4 | Production des rapports clients | « Je les produis essentiellement avec Claude. Je lui importe des données qui viennent d'autres outils pour lui fournir plus de matière et il réussit à me faire des rapports assez complets et bien montés. Ceci dit, ce n'est pas automatisé, j'y passe donc quand même un bon 30 minutes à une heure par rapport. » |
| q5 | Note (échelle) | 5 |
| q6 | Ce qu'elle veut améliorer | « Avoir un processus clair et plus automatisé. Je teste encore beaucoup et je me promène entre les outils pour réussir à avoir un portrait clair. J'hésite beaucoup du côté de GEO à savoir quoi utiliser. » |
| q7 | Son process de démarrage client | « Une fois son objectif connu, je commence par faire un audit de son site et de sa présence web en général. Ensuite, je lui demande des accès pour son site web, sa Search Console, son Google Analytics et sa page Google my Business. » |
| q8 | (choix) | « Les deux! » |
| q9 | Critère de réussite | « Je vais considérer cet accompagnement comme réussi si j'automatise mes processus pour que ma méthide soit plus claire et plus stable. » |
| q10 | Client de référence | « Une agence qu'on vient de partir récemment : Ôtruche Marketing. Le site est sur Wix, donc pour moi, je trouve que ça complexifie le processus. » |
| q11 | Principal frein | « Le manque de structure. » |
| q12 | Partage des accès GSC | « Oui. » |

## Journal des étapes faites
| Date | Étape (roadmap) | Ce qui a été fait | Output | Skill |
|---|---|---|---|---|
| 2026-07-03 | 1 | Dashboard client créé (gabarit Alexia) : seul l'onglet Questionnaire est ouvert, le reste verrouillé. Réponses persistées en ligne (Supabase `client_selections`, doc_key `catherine-accompagnement`) + localStorage ; `admin.html` pour lire ses réponses. **Déployé sur organikk.co** (push validé par Tim, vérifié live : 200 + X-Robots-Tag noindex) | organikk.co/catherine-accompagnement/ | roadmap-prestation |
| 2026-07-16 | 1 | Catherine a répondu aux 12 questions du questionnaire (12/12). Réponses récupérées depuis Supabase et recopiées verbatim dans cette fiche. | Section « Réponses au questionnaire » ci-dessus | roadmap-prestation |
| 2026-07-17 | 2 (Annexe A, partiel) | **3 docs de contexte créés** (gabarits vierges extraits des docs d'Alexia, ses réponses retirées — y compris les URL de ses clients dans le test de cohérence) + Drive « Catherine — Accompagnement SEO (Organikk) ». **Dashboard : onglets Programme et Ressources ouverts** (contenu tiré de la proposition du 11/06 ; séquence 4 semaines corrigée par Tim : setup Claude / workflow / suivi et automatisation / tests et déploiement). **Onglet Questionnaire : bloc « Ce que j'ai compris »** (gate 2b) affiché à 12/12, avec bouton WhatsApp de correction. Installation laissé verrouillé (kit non générable). Déployé + vérifié live (200 + X-Robots-Tag noindex) | organikk.co/catherine-accompagnement/ + [Drive](https://drive.google.com/drive/folders/1LnOAq51lHkm7uwkYHJF3sOEmjD6SKsuh) | roadmap-prestation |

## Spécificités client
- Canada : tarif énoncé 1 500 € HT, conversion CAD + taxes à trancher avant facturation.
- Douleur n°1 : les rapports clients (outils compliqués, reprise à la main) ; douleur n°2 : par où commencer sur un nouveau client (éparpillement SEO/GEO).
- Ses process marketing hors SEO tournent bien : ne pas y toucher.
- Cas qui marche : nettoyage de conduits de ventilation (leads) — la méthode existe, elle n'est pas encodée.
- Questionnaire adapté en conséquence (rapports clients + par où commencer, pas de pré-rempli).
