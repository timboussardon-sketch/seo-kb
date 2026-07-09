---
type: revue-presse
title: "Algorithme. Homonymie et IA : Mueller renvoie la question au web"
date: 2026-07-09
edition: 2026-07-09-revue-presse
pilier_info_jour: Niche SEO
draft: true
---

# Homonymie et IA : Mueller renvoie la question au web

## Résumé

- Un consultant homonyme demande sur Reddit si un fichier `llms-author.txt` peut aider les IA à le distinguer de deux entités plus visibles ; John Mueller répond que Google ne s'en sert pas et qu'aucun autre crawler ou LLM connu ne le fait non plus.
- Réponse parallèle le lendemain sur le mirroring HTML/markdown pour IA : Mueller et Martin Splitt renvoient à un site correctement construit, sans version parallèle « agent-friendly ».
- Une double étude publiée par Chris Green et Suganthan Mohanadasan trouve que ChatGPT route ses recherches vers quatre pipelines cachés (Labrador 88,1 %, Bright 9,9 %, Oxylabs 1,7 %, SERP 0,3 %) et que 11,6 % des prompts basculent de pipeline d'un run à l'autre.
- Kevin Indig et Amanda Johnson mesurent sur 301 pages citées et 1 075 citations que la donnée primaire ne pèse que 2,7 % des pages mais capte 8,4 % des citations, avec une concentration sur un format : le benchmark comparatif « qui est le meilleur ? ».
- Les règles publicitaires des Local Services Ads deviennent des « requirements » à compter du 6 juillet et alignent la documentation sur le badge Google Verified unifié depuis octobre 2025, sans ajout de restrictions.

## L'info du jour. Pilier Niche SEO

Sur Reddit, un consultant explique qu'il partage son nom avec deux entités plus établies. Résultat : quand un client, un prospect ou une IA cherche son identité, ce sont les autres qui ressortent. Il propose une piste technique : un fichier `llms-author.txt` déposé à la racine du site, avec son intitulé de poste, sa localisation, son domaine de pratique, censé donner aux LLM une source d'autorité déclarative séparée du schema.

John Mueller répond sur Bluesky, cité par Roger Montti dans [Search Engine Journal le 6 juillet](https://www.searchenginejournal.com/google-answers-question-about-llms-author-txt-for-seo/581547/) : « Google doesn't use llms.txt or llms-author.txt. I don't know of any other crawler / llm confirming they're using these ». La reprise indépendante par [Let's Data Science](https://letsdatascience.com/news/google-addresses-llms-authortxt-and-online-identification-6cd5f4b1) confirme le verdict au niveau du fait : ces fichiers ne sont pas lus par les principaux moteurs et LLM connus.

Le lendemain 7 juillet, Roger Montti publie [un article distinct](https://www.searchenginejournal.com/google-on-using-markdown-for-ai-seo/581606/) sur la même veine : Mueller et Martin Splitt, encore sur Bluesky, découragent la publication d'une version markdown parallèle d'un site pour agents IA. Le verbatim de Mueller : « A properly made website works well for AI agents … and search engines, and LLMs, and above all, for actual people. If you're trying to fix accessibility issues by making a separate 'agent-friendly' version, you are just building technical debt ». Le fil parallèle sur le fichier `content-signals` inventé par Cloudflare avait déjà eu droit à un traitement similaire de Mueller le 6 juillet : aucun effet mesurable sur les crawlers ou les LLM ([Search Engine Roundtable](https://www.seroundtable.com/google-cloudflare-content-signals-41631.html)).

Le fait à retenir n'est pas la mort d'un fichier. C'est la nature du problème que ce fichier ne résout pas. Le consultant a une difficulté propre à un segment précis du référencement, distinct du référencement d'une marque : la niche des personnes physiques qui vendent leur nom (freelances, consultants, avocats indépendants, formateurs, artisans reconnus). Cette niche a ses propres contraintes : un nom qui n'est pas unique, une entité que Google et les LLM doivent trancher entre plusieurs candidats, et un signal d'expertise qui ne peut pas s'appuyer sur les mêmes leviers qu'une marque (logo, capital marketing, PR volume). C'est ce qu'on peut appeler l'identity SEO au niveau individuel.

Ce que dit Mueller entre les lignes : la solution n'est pas côté serveur, elle est côté web. Le web dit aujourd'hui que d'autres personnes portent ce nom et sont plus visibles ; c'est un état factuel que Google reflète. Le renverser suppose de le corriger dans le web lui-même : bylines vérifiables sur des sites tiers reconnus, interviews audio et vidéo indexables, mentions par des pairs, profils cohérents entre LinkedIn, About page, Crunchbase quand applicable, schema Person aligné, et un flux constant de contenu substantiel signé et sourçable. La logique est celle de [[concepts/e-e-a-t]] appliquée à un individu isolé : Experience et Expertise ne se déclarent pas dans un `.txt`, elles se démontrent dans des URLs tierces.

Cette lecture recoupe une autre observation faite dans cette newsletter les jours précédents : [Beth Nunnington chez Journey Further](https://searchengineland.com/) mesurait dans les données de son agence que 91 % des citations IA relèvent d'insight expert (versus branded/produit) et que 93 % viennent de sources tierces sur les verticales commerciales. C'est la même contrainte pour un individu : les citations IA ne remontent pas depuis la page auto-déclarative, elles remontent depuis les mentions distribuées ailleurs.

Le lien avec [[concepts/fully-meets]] est direct côté doctrine : un utilisateur qui cherche « nom + expertise » veut identifier la bonne personne du premier coup ; si les citations IA renvoient l'homonyme le plus visible, l'intention n'est pas fully-meets, elle est fails-to-meet pour la moitié des chercheurs. La correction ne se joue pas dans le site du consultant, elle se joue dans l'écart entre la visibilité web des trois entités.

Trois limites documentaires à poser. La première : Mueller parle au nom de Google, la position d'OpenAI ou d'Anthropic sur `llms-author.txt` n'est pas documentée aujourd'hui, l'inférence « aucun LLM » repose sur l'absence de confirmation publique constatée par Mueller lui-même. La deuxième : Mueller ne propose pas de protocole opérationnel de désambiguïsation d'homonyme, l'inférence sur les leviers vient de la doctrine SEO existante appliquée à un cas individuel. La troisième : le cas n'est pas mesuré, on ne dispose pas d'un benchmark public documentant combien de temps il faut à un consultant homonyme pour retourner sa citation IA dominante.

## Brèves

### ChatGPT route ses recherches via quatre pipelines cachés (GEO)

Danny Goodwin résume dans [Search Engine Land le 8 juillet](https://searchengineland.com/chatgpt-citations-change-hidden-search-pipelines-481843) deux enquêtes indépendantes de Chris Green et Suganthan Mohanadasan sur le fonctionnement de la recherche interne de ChatGPT.

Green a testé 1 000 prompts jusqu'à dix fois chacun et capturé 9 946 runs complets. Il identifie quatre sources internes déclarées dans les métadonnées : Labrador 88,1 %, Bright 9,9 %, Oxylabs 1,7 %, SERP 0,3 %. Sur les mêmes prompts répétés, 11,6 % basculent d'un pipeline à l'autre entre deux runs. Quand la source change, le recouvrement d'URLs citées passe de 0,273 à 0,149 (environ moins 45 %) et le recouvrement de domaines de 0,265 à 0,155 (environ moins 42 %). Mohanadasan, sur un compte Pro observé pendant deux jours, retrouve les mêmes quatre labels dans 1 240 enregistrements de source.

Deux implications directes. Une : « le score de visibilité ChatGPT » n'a pas d'unité stable, la même requête peut renvoyer deux jeux de citations distincts sans que le contenu web ait bougé (voir [[concepts/tabou-visibilite]]). Deux : chaque pipeline privilégie un type de source (Labrador plutôt éditeurs de référence, Bright et Oxylabs plutôt scraping SERP, SERP plutôt news), donc l'optimisation ne peut pas être générique, elle dépend du pipeline qui traite votre requête. Prédiction ouverte : au moins une étude tierce reproduira la répartition à trois pipelines principaux d'ici fin 2026 avec un ordre de grandeur comparable.

### La donnée primaire capte 3,3 fois plus de citations que la moyenne, presque uniquement sur un format (Product-Led SEO)

Kevin Indig et Amanda Johnson publient dans [Growth Memo le 6 juillet](https://www.growth-memo.com/p/why-most-original-data-never-gets) une analyse sur le dataset de Gauge : 301 pages citées, 316 prompts uniques, 7 verticales, 1 075 citations. Repris par [Search Engine Land](https://searchengineland.com/) sous la plume d'Indig également.

Résultat mesuré : 2,7 % des pages citées contiennent de la recherche primaire, mais ces pages captent 8,4 % de toutes les citations, soit 11,3 citations en moyenne par page primaire contre 3,4 pour les non-primaires. La densité de citation est 3,3 fois plus élevée. Deuxième point, plus tranchant : 75 des 90 citations de recherche primaire portent sur un seul type de contenu, les benchmarks de data warehouse cloud. Le benchmark de Fivetran capte à lui seul 44 citations, presque la moitié des citations de contenus primaires du dataset.

Ce n'est donc pas la donnée primaire en tant que telle qui est citée, c'est un format de donnée primaire : celui qui répond à la question « lequel est le meilleur / le plus rapide / le moins cher ? » avec des entités nommées, des unités mesurables et un cadre de comparaison. Les auteurs pointent quatre facteurs de succès reproductibles : conclusion comparative en tête d'article (dans les 30 premiers pour cent), méthodologie encadrée, cadre de comparaison explicite entre entités comparables, URLs stables (64 des 365 URLs citées dans l'échantillon étaient cassées après un redesign).

Le lien avec [[concepts/data-proprietaire]] est direct côté doctrine Tim : le moat ne vient pas d'avoir des chiffres, il vient d'avoir des chiffres publiés dans le format que les IA extractent. Le lien avec [[concepts/product-led-seo]] tient aussi : un calculateur ou un benchmark qui produit une réponse comparative structurée est structurellement mieux cité qu'un texte long non-comparatif, même primaire.

### Les Local Services Ads deviennent des « requirements » alignés sur le badge Google Verified unifié (Actualité SEO)

Google modifie à compter du 6 juillet la documentation de ses Local Services Ads : les « Local Services platform policies » deviennent des « Local Services Ads requirements ». La refonte, annoncée par [Anu Adegbola dans Search Engine Land le 8 juin](https://searchengineland.com/google-to-update-local-services-ads-policies-in-july-479653) et reprise sur la [page officielle Google Ads Policy](https://support.google.com/adspolicy/answer/17083421?hl=en), est présentée comme un toilettage terminologique aligné sur le badge unifié Google Verified déployé le 20 octobre 2025, qui a remplacé le Google Guaranteed, le Google Screened et le License Verified by Google en un seul indicateur.

Trois faits vérifiables. Un : aucune nouvelle restriction n'est ajoutée aux conditions d'éligibilité selon la communication publique. Deux : depuis novembre 2024, un profil Google Business Profile lié et vérifié est obligatoire pour faire tourner des LSA. Trois : les avis GBP alimentent le ranking des LSA. La convergence est nette pour les acteurs locaux visés (services à domicile, entretien, réparation, professions réglementées) : les composants du stack local sont étroitement liés, un signal invalide sur la fiche entraîne l'arrêt de la publicité.

Le fait n'a pas la portée d'une évolution algorithmique. Il documente en revanche l'état actuel du référencement local propre : la vérification du prestataire est désormais un binaire dépendant de Google (badge unique, dépendance GBP), sans recours documenté côté annonceur si l'un des éléments se désaligne. Prédiction ouverte : un cas de suspension coordonnée LSA + GBP + retrait du badge Google Verified sur un prestataire non frauduleux sera documenté publiquement avant fin 2026.

---

*Draft SyntheticBrain. Rien n'a été envoyé.*
