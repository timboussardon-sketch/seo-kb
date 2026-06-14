---
title: "Algorithme — édition du 14 juin 2026"
date: 2026-06-14
pillar: actualite-seo
sources_count: 11
author: SyntheticBrain
---

# Google Search : l'identité de marque et les signalements utilisateurs entrent dans les critères d'éligibilité publicitaire

> Édition du samedi 14 juin 2026. Pilier : **Actualité SEO**.

## Résumé

- Google a publié le 12 juin 2026 une mise à jour de sa Limited Ad Serving Policy qui l'étend à Google Search, avec une montée en charge progressive jusqu'en 2028. La diffusion d'une annonce peut désormais être restreinte sur certaines requêtes en fonction des signalements utilisateurs, de la clarté de l'identité d'annonceur et de l'historique de conformité.
- La sanction Google contre le « back button hijacking » entre en application **demain 15 juin 2026**, après deux mois de période de grâce. Les sites qui empêchent un retour direct à la page précédente s'exposent à une manual action ou à un déclassement automatisé.
- Une mesure relayée le 12 juin par Search Engine Land suggère que Claude n'effectue pas de re-classement de ses propres résultats web et s'appuie largement sur le top 10 de Brave Search ; Claude déclenche une recherche dans 36,6 % des prompts contre environ 90 % pour ChatGPT, ce qui en fait un terrain GEO à part.
- Le toggle d'opt-out AI Overviews et AI Mode dans Google Search Console entre en vigueur opérationnel mardi 17 juin pour les éditeurs UK testeurs. L'interaction avec les Information Agents (déployés globalement aux abonnés Ultra le 12 juin) n'est pas documentée par Google et reste une zone d'incertitude pour qui veut un retrait complet.

## Info du jour — Google Search : la diffusion publicitaire conditionnée à la confiance, jusqu'en 2028

Pilier : **Actualité SEO**.

Google a publié le 12 juin 2026 une mise à jour de sa politique « Limited ad serving » qui en étend la portée à Google Search. La documentation officielle [Updates to Limited ad serving Policy (June 2026)](https://support.google.com/adspolicy/answer/17122370?hl=en) précise que la mise en application s'effectuera de manière progressive et sera complétée d'ici 2028.

Le mécanisme existait déjà sur YouTube et d'autres surfaces publicitaires Google. Il consiste à limiter le volume d'impressions d'un annonceur jugé non qualifié sur les requêtes susceptibles de générer une expérience négative. Trois facteurs entrent dans l'évaluation, tels que listés par Google : les signalements utilisateurs persistants sur le contenu, les produits ou le comportement d'un annonceur, la clarté de l'identité d'annonceur dans l'annonce, et l'appartenance à un secteur identifié comme à haut risque d'abus.

Anu Adegbola, paid media editor de [Search Engine Land](https://searchengineland.com/google-expands-limited-ad-serving-policy-on-search-480137) (12 juin 2026), précise que les recommandations concrètes faites aux annonceurs incluent l'épinglage du domaine en première position des titres responsives, l'usage d'un message spécifique plutôt que générique, et la communication claire des affiliations entre marques. Luis Rijo, dans [PPC Land](https://ppc.land/google-expands-limited-ad-serving-policy-to-google-search-from-june-2026/) (13 juin 2026), ajoute que les annonceurs prioritairement visés par la phase initiale sont « les comptes récents, les annonceurs dont l'identité de marque est ambiguë, et les annonceurs dans les verticales à haut taux d'abus ». Rijo cite également la chronologie YouTube comme repère : l'enforcement initial avait débuté en septembre 2024, avec couverture complète en 2026. Le calendrier Search est donc plus long, étalé sur près de trois ans.

L'extension est confirmée à un troisième niveau par la reprise [Optimixed](https://www.optimixed.com/google-expands-limited-ad-serving-policy-on-search/) du 12 juin 2026, qui n'apporte pas de précision additionnelle mais valide la mise en circulation publique.

Ce qui change concrètement pour l'écosystème search marketing : la qualification d'un annonceur ne se résume plus au Quality Score et à l'enchère. Google introduit un filtre amont qui peut couper la diffusion d'une annonce sur certaines requêtes même si l'annonceur est en règle au sens des Ads Policies classiques. Le critère « signalements utilisateurs » fait entrer dans l'équation un signal comportemental agrégé, équivalent à ce que représente E-E-A-T en référencement naturel mais appliqué à la sélection d'annonces. La parenté est explicite côté principe : la fiche doctrinale [[concepts/e-e-a-t]] décrit la dimension *Trustworthiness* comme « contenu fiable et vérifiable » ; Google transpose ici la même logique à un format publicitaire en intégrant les retours utilisateurs et la lisibilité de l'identité de marque.

Quelques zones d'incertitude restent à observer. Google n'a pas publié de seuil quantitatif sur le nombre de signalements déclenchant une restriction, ni de méthodologie de mesure de la « clarté » d'identité d'annonceur. La page support.google.com mentionne une évaluation continue qui combine attributs de compte, activité utilisateur, maturité du compte, format publicitaire, historique de conformité, secteur et statut de vérification, sans préciser leur pondération. La phase « complète d'ici 2028 » laisse aussi ouverte la question de l'ampleur initiale : combien d'annonceurs concernés en juin 2026, et avec quelle réduction d'impressions ?

Pour les annonceurs grands comptes, l'impact opérationnel est faible à court terme : l'identité de marque est déjà forte, et l'historique de conformité a généralement été construit. Pour les comptes plus récents ou les agences gérant des verticales sensibles (financier, santé, voyage, service client, listées par Rijo), la qualification devient un travail explicite, à intégrer au paramétrage des campagnes : épingler le domaine, expliciter la marque sur la landing page, surveiller les signalements via les feedbacks utilisateurs Ads.

Côté éditeur de site recevant du trafic publicitaire, l'extension n'a pas d'effet direct. Côté annonceur Search, elle ajoute un axe de travail à mesurer dans les six prochains mois.

## Brèves

### Sanction « back button hijacking » : effective demain 15 juin

Pilier : **Actualité SEO**.

La nouvelle politique antispam de Google contre le « back button hijacking » entre en application demain dimanche 15 juin 2026, à l'issue d'une période de grâce de deux mois ouverte par l'annonce du 13 avril. La doctrine officielle figure sur le [Google Search Central Blog](https://developers.google.com/search/blog/2026/04/back-button-hijacking).

Le périmètre couvert : toute pratique qui interfère avec la navigation arrière du navigateur et empêche un utilisateur de revenir directement à la page précédente. Les exemples documentés par Google incluent l'insertion d'états d'historique factices, la redirection vers des pages que l'utilisateur n'avait pas l'intention de visiter, l'affichage de fils de recommandations inattendus lorsque l'utilisateur essaie de quitter, ou l'obligation de cliquer plusieurs fois sur « retour » pour s'échapper d'une page ou d'un site. La classification est explicite : il s'agit d'une violation des malicious practices.

Barry Schwartz, dans [Search Engine Land](https://searchengineland.com/google-search-to-penalize-back-button-hijacking-schemes-474167) (13 avril 2026), rappelle que l'enforcement combine deux mécanismes : action manuelle (manual spam action) ou déclassement algorithmique automatisé. La couverture par [9to5Google](https://9to5google.com/2026/04/13/google-search-back-button-hijacking/) (13 avril 2026) précise que la responsabilité du publisher englobe le code tiers : un script publicitaire, une bibliothèque de recommandation ou un outil d'engagement qui produit le comportement reste imputable au site qui l'intègre.

Le délai a été présenté par Google comme un avertissement explicite. Pour les sites qui utilisent encore des techniques de manipulation de l'historique de navigation (souvent via des partenaires de monetization), demain est la dernière journée d'audit possible avant l'entrée en vigueur. Le risque est binaire : un déclassement, même partiel, sur des pages qui dépendent du trafic organique se traduit par une perte d'impressions immédiate, sans signal en GSC dans les premiers jours.

À surveiller dans les semaines qui suivent : les remontées de manual actions signalées dans les forums (Search Engine Roundtable, Webmaster World) et les premières études de volatilité associées spécifiquement à cette policy plutôt qu'au core update de mai 2026.

### Claude s'appuie sur le top 10 Brave Search : nouvelle donnée Profound

Pilier : **GEO**.

Une nouvelle mesure rendue publique par Jonathan Clark (Moving Traffic Media) à l'issue d'une session [Zero Click by Profound](https://www.tryprofound.com/zeroclick) suggère que Claude ne procède pas à un re-classement de ses propres résultats web, et utilise directement les dix premières positions de Brave Search dans ses réponses. La couverture par Danny Goodwin dans [Search Engine Land](https://searchengineland.com/claude-visibility-brave-search-rankings-480053) (12 juin 2026) reprend les chiffres clés.

Trois mesures sont rapportées :

- Claude déclenche une recherche web dans 36,6 % des prompts, contre environ 90 % pour ChatGPT.
- Le déclenchement est très corrélé à la nature du prompt : signaux de fraîcheur (« best XYZ ») 81 %, signaux de classement 67 %, signaux de localisation 55 %, signaux de comparaison 51 %.
- Les citations de Claude recouvrent celles de ChatGPT à hauteur de 8 % seulement sur un même set de prompts, mais recouvrent les classements Google à 64 %.

La méthodologie précise n'est pas publiée par Profound : la session Zero Click ne précise ni la taille de l'échantillon ni la fenêtre temporelle. Les chiffres doivent donc être lus comme directionnels et non comme une mesure globale stable. L'ordre de grandeur, en revanche, est cohérent avec l'observation déjà documentée que Brave Search est listé comme sous-traitant dans la documentation Claude d'Anthropic.

Conséquence pour le travail GEO : optimiser pour Brave Search devient un levier d'AEO directement actionnable sur Claude, ce qui ouvre une porte distincte des leviers Bing (pour ChatGPT) ou Google (pour AI Overviews et AI Mode). La fiche [[concepts/aeo]] et la fiche [[concepts/metriques-visibilite-geo]] ne couvraient pas jusqu'ici cette dimension « moteur web sous-jacent du LLM » comme axe de mesure de visibilité. Ce signal s'ajoute au registre des dimensions à suivre dans une mesure GEO sérieuse, en plus de Imp_wc et Imp_pos.

Une étude indépendante reproduisant la mesure sur un autre échantillon de prompts permettra de confirmer ou de nuancer l'ordre de grandeur. La prédiction P-2026-06-13-v2-3 (reproduction du 6x authority flip BrightEdge) constitue un précédent méthodologique de référence pour évaluer la solidité de ces mesures de visibilité multi-moteurs.

### Opt-out AI Overviews UK : trois jours avant l'application effective, l'interaction avec les Information Agents reste non documentée

Pilier : **Actualité SEO**.

Le toggle d'opt-out AI Overviews et AI Mode, déployé dans Google Search Console à un sous-ensemble d'éditeurs britanniques le 3 juin 2026 par décision de la Competition and Markets Authority, entre en vigueur opérationnel le 17 juin 2026. Trois jours nous séparent de la date d'application effective.

Deux questions opérationnelles restent ouvertes au 14 juin. D'abord, le scope : la couverture [TechCrunch](https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/) du 3 juin précise que l'opt-out concerne AI Overviews, AI Mode et AI Overviews in Discover, mais exclut l'application Gemini. Un éditeur britannique qui activerait le toggle reste donc exposé à une utilisation de son contenu par les réponses Gemini standalone, ce que le compromis CMA n'adresse pas. Ensuite, et c'est plus directement actionnable pour les SEO : Google n'a publié aucune précision sur le comportement des Information Agents (déployés globalement aux abonnés Ultra le 12 juin) vis-à-vis du toggle. Ces agents surveillent en continu le web et déclenchent des notifications à l'utilisateur ; ils sont distincts des réponses synchrones d'AI Overviews et d'AI Mode. Aucune communication Google publique ne précise si l'opt-out s'applique à la couche événementielle de surveillance ou seulement aux réponses synchrones.

Cette zone grise est l'objet de la prédiction interne P-2026-06-13-v2-2 (Google ne publie pas de précision opérationnelle sur l'interaction opt-out / Information Agents avant fin 2026). Pour les éditeurs UK, la conséquence concrète est qu'activer le toggle le 17 juin n'apporte pas, en l'état des informations publiques, une garantie de retrait complet des surfaces génératives de Google.

La prédiction P-2026-06-09-v2-2, écrite après l'annonce CMA, anticipe un taux d'opt-out effectif sous 10 % des sites éligibles un mois après l'application. Les premières mesures publiques (Datos, Press Gazette, ou un agrégateur indépendant publiant une cohorte d'éditeurs UK) seront le premier signal réel sur l'écart entre l'intention déclarée à 33,2 % dans le sondage Search Engine Land et le comportement observé.

## Sources et recoupements

Info du jour Limited Ad Serving Search :
- Doc Google primaire 12 juin 2026 : https://support.google.com/adspolicy/answer/17122370
- Search Engine Land, Anu Adegbola, 12 juin 2026 : https://searchengineland.com/google-expands-limited-ad-serving-policy-on-search-480137
- PPC Land, Luis Rijo, 13 juin 2026 : https://ppc.land/google-expands-limited-ad-serving-policy-to-google-search-from-june-2026/
- Optimixed, 12 juin 2026 (reprise) : https://www.optimixed.com/google-expands-limited-ad-serving-policy-on-search/

Brève back button hijacking :
- Google Search Central Blog primaire 13 avril 2026 : https://developers.google.com/search/blog/2026/04/back-button-hijacking
- Search Engine Land, Barry Schwartz, 13 avril 2026 : https://searchengineland.com/google-search-to-penalize-back-button-hijacking-schemes-474167
- 9to5Google, 13 avril 2026 : https://9to5google.com/2026/04/13/google-search-back-button-hijacking/

Brève Claude / Brave Search :
- Search Engine Land, Danny Goodwin, 12 juin 2026 : https://searchengineland.com/claude-visibility-brave-search-rankings-480053
- Profound Zero Click (session source primaire) : https://www.tryprofound.com/zeroclick

Brève opt-out AI Overviews UK :
- TechCrunch, 3 juin 2026 : https://techcrunch.com/2026/06/03/publishers-will-be-able-to-opt-out-of-ai-search-thanks-to-new-regulation/
- Search Engine Roundtable et autres reprises (déjà couvertes 0609-v2)
