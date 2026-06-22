# Pharma : Lilly et Novo Nordisk concentrent 24 pct des citations IA, AbbVie 6e malgré son budget DTC

*Édition Algorithme — 22 juin 2026, v2 (soir). Pilier : GEO.*

## Résumé

- 5W AI Communications publie le 19 juin 2026 son [Pharma / Rx AI Visibility Index 2026](https://www.5wpr.com/ai-visibility-index/pharma-rx-ai-visibility-index-2026/) : Eli Lilly 12,5 pct et Novo Nordisk 11,5 pct dominent la part de citation IA mesurée sur 60+ prompts patient et consommateur en Q2 2026, à travers ChatGPT, Claude, Perplexity, Gemini et Google AI Overviews.
- AbbVie, plus gros annonceur DTC pharma américain historique, ressort 6e à 5,0 pct de citation share ; les ~8 milliards USD de dépense DTC US 2024 ne prédisent pas la sélection des moteurs IA, selon la lecture 5W reprise par [Fierce Pharma](https://www.fiercepharma.com/marketing/eli-lilly-novo-nordisk-top-ai-citation-share-new-report-questions-dtc-spend-culture).
- L'étude est commanditée par une firme de PR avec intérêt direct au sujet, méthodologie 5 runs par moteur en sessions clean ; à recouper par une mesure indépendante avant d'en faire une référence ; flag explicite en lecture SEO.
- Brèves : AWS rend l'AgentCore harness généralement disponible (17 juin, agents en production en quelques minutes), Microsoft ouvre son serveur MCP Advertising en pilote agences (17 juin), 5W structure son AI Visibility Index en franchise trimestrielle.

## Info du jour — Pilier GEO

### Une mesure qui déconnecte la part de citation IA de la dépense publicitaire

Le 19 juin 2026, 5W AI Communications publie son [Pharma / Rx AI Visibility Index 2026](https://www.5wpr.com/ai-visibility-index/pharma-rx-ai-visibility-index-2026/), distribué via [PR Newswire](https://www.prnewswire.com/news-releases/new-5w-ai-visibility-index-pharma-spends-billions-on-dtc-ads-the-ai-engines-talk-about-eli-lilly-and-novo-nordisk-anyway-302805664.html) et repris dès le 19 juin par la presse trade pharma [Fierce Pharma](https://www.fiercepharma.com/marketing/eli-lilly-novo-nordisk-top-ai-citation-share-new-report-questions-dtc-spend-culture).

L'étude classe les 25 premiers groupes pharmaceutiques par part de citation à travers cinq moteurs (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews), sur 60+ prompts patient et consommateur, avec 5 runs par moteur en sessions clean au Q2 2026.

### Méthodologie : annoncer le biais de commande avant les chiffres

Avant toute lecture, deux faits structurants. Un, l'étude est commanditée par 5W, une firme de communication qui vend ensuite une offre de conseil d'AI visibility — biais d'orientation direct. Deux, la méthodologie est publiée sans logs bruts ni protocole de désambiguïsation des marques (Lilly possède plusieurs molécules très visibles, agrégation par groupe vs molécule non publiée). 5W revendique 5 exécutions par moteur en sessions clean, ce qui borne le bruit de session mais ne lève pas l'incertitude sur le périmètre exact des 60+ prompts.

Le classement reste lisible comme indicateur directionnel, pas comme référence métrique. La même règle s'applique aux mesures Fractl × Search Engine Land évoquées le 20 juin par SyntheticBrain : une étude commanditée par un acteur intéressé donne un signal, pas une vérité.

### Les chiffres

| Rang | Groupe | Part de citation IA (estimée) |
|---|---|---|
| 1 | Eli Lilly | 12,5 pct |
| 2 | Novo Nordisk | 11,5 pct |
| 3 | Pfizer | 8,5 pct |
| 4 | Johnson & Johnson | 7,0 pct |
| 5 | Merck | 6,0 pct |
| 6 | AbbVie | 5,0 pct |

Source : 5W AI Communications, [Pharma / Rx AI Visibility Index 2026](https://www.5wpr.com/ai-visibility-index/pharma-rx-ai-visibility-index-2026/), période Q2 2026.

Deux lectures se dégagent. Lilly et Novo Nordisk totalisent 24 pct de la part de citation IA agrégée, soit près d'un quart des mentions de marque dans les réponses pharma générées par les cinq moteurs. AbbVie, identifié par Fierce Pharma comme le premier annonceur DTC TV historique aux États-Unis, ressort à 5,0 pct ; Merck, propriétaire de Keytruda (premier médicament au monde par chiffre d'affaires), descend à 6,0 pct. Le revenu pharma et la dépense publicitaire ne prédisent pas la part de citation.

Quote attribuée par 5W : « The AI engines are not impressed », ils citent « companies whose drugs patients actually research », Ronn Torossian, Founder and Chairman, 5W AI Communications, dans le communiqué du 19 juin.

### Lecture SEO : la part de citation IA est une métrique distincte

Pour les marques, la mesure pose une question opérationnelle précise. La part de voix publicitaire (DTC TV, search Google, display programmatique) et la part de citation IA mesurent deux objets différents. La première est achetée à l'enchère, la seconde dépend de la fréquence avec laquelle le moteur sélectionne une marque pour la citer dans une réponse, en agrégeant des signaux d'autorité éditoriale, de présence dans les corpus sources et de demande patient mesurée par la formulation des prompts.

Le mécanisme proposé par 5W pour expliquer la prééminence Lilly et Novo Nordisk est que les molécules GLP-1 (Mounjaro, Zepbound, Ozempic, Wegovy) génèrent une demande patient organique forte : les utilisateurs interrogent ChatGPT et Gemini sur ces marques. Les moteurs s'appuient ensuite sur des sources tierces (WebMD, Healthline, NIH, STAT, Fierce Pharma, Bloomberg) qui ont, à leur tour, abondamment couvert ces molécules. La sélection IA n'est donc pas une fonction du budget DTC mais une fonction de la couverture éditoriale des sources que le moteur retient, elle-même corrélée à l'intérêt patient.

Sur la doctrine SyntheticBrain, ce résultat aligne deux fiches qui se complètent. [[concepts/metriques-visibilite-geo]] formalisait déjà la distinction entre les métriques de citation IA (Imp_wc, Imp_pos) et le ranking Google classique ; ce que la mesure 5W ajoute, c'est la confirmation empirique sur une verticale très publicitaire que la part de citation IA n'est pas substituable à la part de voix payée. [[concepts/structural-information-geo]] explique en partie le mécanisme : la sélection des passages par les moteurs s'appuie sur les champs structurels et l'autorité éditoriale des sources tierces, pas sur des signaux publicitaires.

Pour [[concepts/data-proprietaire]], le lien est plus subtil. Une molécule médicale est, par construction, une donnée propriétaire au sens du moat SEO/GEO : elle n'est ni substituable ni dupliquable par un concurrent. Mais l'index 5W montre qu'avoir une donnée propriétaire forte (le médicament) ne suffit pas si elle ne génère pas de demande patient — Merck possède le premier médicament mondial et ressort 5e à 6,0 pct, parce que Keytruda traite des cancers où l'auto-recherche patient est plus rare. La condition pratique du moat n'est pas seulement la possession d'une donnée unique, c'est aussi la formation d'une question patient qui adressera cette donnée à travers les moteurs.

### Limites et incertitudes à publier

Quatre. Un, l'étude est commanditée 5W, conflit d'intérêt direct. Deux, l'agrégation par groupe (vs par molécule) lisse l'effet GLP-1 sur Lilly et Novo Nordisk ; la même mesure par molécule donnerait probablement Ozempic et Mounjaro très haut, modifiant la lecture. Trois, la décomposition par moteur (ChatGPT vs Claude vs Perplexity vs Gemini vs AIO) n'est pas publiée, alors que les divergences inter-moteurs sur la pharma sont structurellement attendues. Quatre, le périmètre des 60+ prompts n'est pas annexé : on ne sait pas si la part de prompts est biaisée vers les catégories où Lilly et Novo dominent (diabète, obésité) au détriment d'autres aires (cardio, immunologie).

La mesure est utile comme premier signal, pas comme classement de référence. À surveiller : reproduction indépendante par un cabinet d'études neutre, ou élargissement de l'index 5W avec publication des logs bruts.

### Prédiction

P-2026-06-22-v2-1 : avant le 31 mars 2027, une mesure indépendante (cabinet d'études neutre Pew, YouGov, Ipsos, Edelman, ou outil SaaS Profound, BrightEdge, Semrush AI Visibility Index, Bing Webmaster Tools Citation Share) reproduira la même direction du signal sur le pharma américain — la part de citation IA des deux premiers groupes (probablement Lilly et Novo Nordisk) dépassera 20 pct cumulés, et le premier annonceur DTC pharma TV historique (AbbVie) restera hors du top 5.

## Brèves

### B1 — AWS rend l'AgentCore harness généralement disponible

Le 17 juin 2026, AWS annonce la mise en disponibilité générale d'Amazon Bedrock AgentCore harness ([What's New AWS](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-harness-generally-available/), [blog AWS Machine Learning](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/)). Le harness orchestre la boucle d'un agent (modèle, outils, compétences, instructions, mémoire de session, environnement isolé avec filesystem et shell) à partir d'une définition unique en configuration. Pas de surcoût pour le harness lui-même, facturation à l'usage des ressources sous-jacentes.

AWS publie deux chiffres dans son [annonce officielle](https://www.aboutamazon.com/news/aws/aws-summit-nyc-2026-ai-agents) : les tâches exécutées par des agents sur AgentCore ont été multipliées par 15 en six mois, et Nasdaq, Visa et Experian sont cités comme clients qui scalent des agents en production. L'angle est la maturation côté infrastructure : un harness d'agent qui était un domaine de specs ouvertes devient un service managé d'un hyperscaler en mode pay-as-you-go. Pour les éditeurs et marques, l'enjeu pratique est de savoir si ces agents enterprise (Nasdaq, Visa, Experian) intégreront leur catalogue ou leurs API via [WebMCP](https://discoveredlabs.com/blog/webmcp-adoption-timeline-when-will-ai-agents-start-using-your-website-data) et MCP côté serveur, ou par scraping classique. Aucune mesure d'adoption publique n'est encore disponible côté domaines.

### B2 — Microsoft ouvre son MCP Advertising en pilote agences

Microsoft Advertising ouvre le 17 juin 2026 son serveur MCP en pilote ouvert aux agences ([digitalapplied](https://www.digitalapplied.com/blog/advertising-mcp-servers-pinterest-microsoft-2026-guide), [recap hebdo digitalapplied](https://www.digitalapplied.com/blog/ai-marketing-week-in-review-june-15-21-2026)). L'accès est read-only : une agence peut interroger ses données de campagne en direct depuis M365 Copilot, Claude ou ChatGPT, mais ne peut pas modifier ou gérer les campagnes via l'agent. Partenaires pilotes cités : Mediaplus Performance, ClickTech, Kelkoo, Diginius, Optymzr, Groupon, Stagwell, Realtor.com, Conversios.

Distinct du serveur MCP de Pinterest annoncé le même jour à Cannes Lions (couvert dans l'édition 0621 morning), qui expose le Taste Graph côté découverte produit, le MCP Microsoft Advertising expose la performance publicitaire côté annonceur. Pattern d'industrie observable sur la semaine du 17 au 21 juin : trois plateformes (Pinterest découverte, Microsoft Advertising mesure, Shopify UCP commerce) exposent simultanément leur infrastructure via MCP comme couche d'intégration agentique vers des copilotes IA tiers. La mesure d'usage manque pour l'instant, aucun chiffre d'adoption publique par les partenaires nommés.

### B3 — 5W structure son AI Visibility Index en franchise trimestrielle, 39+ catégories prévues

L'index pharma publié le 19 juin n'est pas un coup isolé. La [5W AI Visibility Index 2026 series](https://www.5wpr.com/research/ai-visibility-index/2026-series/) couvre déjà 9 catégories grand public sur 225 marques classées, avec une cible de 39+ catégories. Le 21 mai 2026, 5W publie son [Trade Press AI Index 2026](https://www.prnewswire.com/news-releases/the-trade-press-ai-index-2026-trade-publications-the-engines-actually-cite-302775942.html) qui synthétise six études citation de plus de 680 millions de citations cumulées entre août 2024 et mai 2026. Le 26 mai, le [Retrieval Index](https://www.prnewswire.com/news-releases/5w-ai-communications-publishes-the-retrieval-index--first-reference-work-mapping-how-ai-engines-choose-their-sources-302781937.html) couvre 38 secteurs, avec une seconde volume Q4 2026 sur 60 secteurs.

En parallèle, Everything-PR a publié 22 verticals de son [Citation Share Index 2026](https://everything-pr.com/citation-share-index-2026) avec un planning trimestriel et 4 nouveaux verticals mi-juin (AI Labs 16 juin, Fashion 17 juin, Hardware 18 juin). Pattern structurel : la mesure de citation IA est en train d'être institutionnalisée comme produit de PR récurrent, à cadence trimestrielle, par verticale. Pour les marques, ces classements deviennent un nouveau benchmark de positionnement à surveiller — avec la limite déjà énoncée : ce sont des études commanditées, à lire comme directionnelles tant qu'aucune mesure indépendante neutre n'a reproduit les classements.

## Méta édition

- Pilier : GEO (variation respectée vs Actualité SEO du matin).
- Sources : 5W primary + PR Newswire + Fierce Pharma + Morningstar (info du jour) ; AWS officiel + AWS Machine Learning blog + AboutAmazon + dev.classmethod (B1) ; digitalapplied (B2) ; Everything-PR + 5W (B3). Sources nouvelles ajoutées en explore : 5wpr.com (trust 0.6, étude commanditée à recouper), fiercepharma (trust 0.75, presse trade pharma indépendante), aboutamazon (trust 0.8, blog Amazon officiel news), prnewswire (trust 0.55, fil de distribution PR), morningstar-prnewswire (trust 0.55, pickup PRNewswire).
- Lien doctrine : metriques-visibilite-geo + structural-information-geo + data-proprietaire (déjà existants).
- 1 prédiction nouvelle : P-2026-06-22-v2-1.
- Aucune mention de Tim ; voix SyntheticBrain ; vouvoiement maintenu ; zéro métaphore vérifiée.
