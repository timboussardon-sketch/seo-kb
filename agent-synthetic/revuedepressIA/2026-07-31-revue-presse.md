---
title: "Algorithme — édition 2026-07-31"
date: 2026-07-31
type: revue-presse
pilier_info_du_jour: Actualité SEO
piliers_breves: [Business SEO, Recherche agentique, Actualité SEO]
author: SyntheticBrain
status: draft
---

# Algorithme — édition du 31 juillet 2026

## Résumé

- Reddit publie 43 M USD de other revenue au T2 2026, soit +24 % sur un an ; les deux gros contrats de licence de données (Google environ 60 M USD/an, OpenAI environ 70 M USD/an) expirent au premier semestre 2027 et Steve Huffman ne s'engage pas sur leur renouvellement.
- Dans le call, Huffman nomme quatre usages distincts de la data Reddit côté LLM (entraînement, post-entraînement, grounding, index de recherche) et reconnaît que les AI Overviews n'ont pas produit l'effet positif sur le trafic de recherche traditionnel.
- Microsoft publie ses résultats Q4 FY2026 avec une croissance search advertising de +10 % (+9 % à taux constant), portée par un revenu par recherche plus élevé sur Edge et Bing, malgré un effet négatif des partenariats tiers.
- Google Cloud publie la version 0.2 du Open Knowledge Format (OKF) avec cinq signaux de confiance ajoutés (provenance, trust, freshness, lifecycle, attestation), levant l'anti-redite v0.1 posée le 14 juin 2026.
- Brodie Clark repère le 30 juillet des descriptions générées par IA sur les annonces Shopping et Product de Google, extension d'un test déjà mené sur les Search ads en juillet, sans annonce officielle Google.

## Info du jour — Actualité SEO

**Reddit publie 43 M USD de other revenue au T2 2026, quatre usages nommés pour la data côté LLM, deux gros contrats de licence à négocier avant H1 2027**

Reddit a publié ses résultats du T2 2026 le 30 juillet après clôture des marchés US via un 8-K et un call earnings tenu par Steve Huffman et Drew Vollero ([Reddit 8-K StockTitan](https://www.stocktitan.net/sec-filings/RDDT/8-k-reddit-inc-reports-material-event-162e95400070.html), [CNBC](https://www.cnbc.com/2026/07/30/reddit-rddt-q2-2026-earnings-report.html), [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/07/30/reddit-rddt-q2-2026-earnings-call-transcript/)). Le chiffre isolé qui compte pour cette édition, other revenue, atteint 43 M USD, en hausse de 24 % sur un an. Ce poste inclut le chiffre d'affaires de licence de données à des acteurs LLM. La croissance séquentielle ralentit toutefois par rapport au T1 2026 (39 M USD selon la lecture de CNBC), soit environ +10 % trimestre sur trimestre.

Ce chiffre se lit à trois niveaux. Un, le run rate annualisé se situe autour de 172 M USD. Deux, les deux contrats connus publiquement (Google environ 60 M USD/an, OpenAI environ 70 M USD/an) totalisent environ 130 M USD, ce qui laisse une part significative attribuée à d'autres partenaires que Reddit ne détaille pas. Huffman parle d'un « expanding marketplace » sans nommer d'autre client. Trois, ces deux contrats principaux sont décrits comme expirant au premier semestre 2027, et le CEO ne s'engage pas publiquement sur leur renouvellement.

L'angle SEO/GEO est dans les mots exacts de Huffman sur le call, cités par le Motley Fool : la data Reddit sert quatre usages distincts côté LLM, « training, post-training to teach models how to talk, grounding, and as a search index ». C'est la première fois qu'un dirigeant d'un des trois plus gros fournisseurs de data conversationnelle aux LLM énumère aussi précisément les usages qui sortent des mêmes fichiers de licence. Le rattachement à la doctrine est direct : [[concepts/grounding-score]] documente le mécanisme d'ancrage vectoriel des réponses génératives sur une source, [[entities/reddit]] est la source la plus citée par Perplexity et la 2e-3e par ChatGPT et Google AI Mode. Huffman confirme que Reddit alimente les quatre étapes du pipeline de la réponse générative en même temps, pas seulement une couche.

Deuxième signal fort : Huffman reconnaît publiquement que « AI overviews has yet to make a similar level of positive impact » que les liens de recherche traditionnels sur le trafic référent vers Reddit. Le trafic search est décrit comme « choppy in the quarter » et plus volatile en fin de trimestre, avec une visibilité faible côté équipe. Un des plus gros bénéficiaires historiques du trafic organique Google admet donc que l'AI Overview ne remplace pas le clic, ce qui rejoint la lecture de la doctrine [[concepts/tabou-visibilite]] : mesurer la présence dans la réponse générative ne dit rien sur le trafic effectif redirigé, ces deux mesures divergent.

Le reste du T2 confirme la trajectoire : revenu total 805 M USD (+61 % YoY), advertising revenue 762 M USD (+64 %), net income 253 M USD, EPS dilué 1,25 USD (+178 %), DAUq 130,3 M (+18 %), ARPU global 6,18 USD (+36 %), guidance Q3 2026 à 860-870 M USD ([StockTitan release](https://www.stocktitan.net/news/RDDT/reddit-reports-second-quarter-2026-59zmiv75ayor.html)). Reddit affiche donc une croissance publicitaire à deux chiffres alors même que la ligne data licensing ralentit. Pour un consultant qui suit un annonceur ou un site qui dépend de citations Reddit dans les réponses génératives, la question n'est plus de savoir si Reddit sera cité, mais de comprendre à quel prix et sous quelles conditions ce statut restera négocié entre Reddit et chaque moteur d'ici H1 2027.

Trois limites explicites. Premièrement, le 8-K ne mentionne pas nommément Google ou OpenAI et ne détaille pas la ventilation des 43 M USD par client ; l'attribution repose sur la confirmation antérieure des contrats et sur la reprise Wall Street Journal du 22 juillet 2026. Deuxièmement, la ligne other revenue inclut aussi de la data commerciale hors LLM, mais son poids relatif n'est pas publié. Troisièmement, la mesure de trafic référent AI Overviews mentionnée par Huffman est qualitative dans le call, aucun pourcentage n'est communiqué.

**Résolution partielle de deux prédictions ouvertes** : P-2026-07-28-2 (chiffre licence data IA >39 M USD publié le 30 juillet) est **résolue verified** (43 M USD publié). P-2026-07-30-v2-4 (other revenue ≥40 M USD publié 30/07/2026 et pas d'annonce ferme de renouvellement Google pendant le call) est **résolue verified** (43 M USD et Huffman n'a pas confirmé de renouvellement).

**Lien doctrine** : [[entities/reddit]], [[concepts/grounding-score]], [[concepts/data-proprietaire]], [[concepts/tabou-visibilite]], [[concepts/agentic-search]].

---

## Brève 1 — Business SEO

**Microsoft affiche +10 % de search advertising revenue au Q4 FY2026, tiré par le revenu par recherche sur Edge et Bing**

Microsoft a publié ses résultats du Q4 FY2026 le 29 juillet 2026 après clôture ([communiqué Microsoft IR](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast), [CNBC](https://www.cnbc.com/2026/07/29/microsoft-msft-q4-earnings-report-2026.html)). Le chiffre pertinent pour cette édition, search and news advertising revenue hors coûts d'acquisition de trafic, augmente de 10 % sur un an (+9 % à taux de change constant). La croissance est attribuée à un revenu par recherche plus élevé sur Edge et Bing et à un volume de recherche en hausse, avec un effet négatif attribué aux partenariats tiers (le trafic acheté auprès de tiers baisse).

La lecture pour un consultant SEO/GEO est double. D'abord Bing continue de progresser à deux chiffres alors que les référents Google search vers un site comme Reddit sont qualifiés de « choppy » par le CEO Huffman le même jour (voir info du jour). Le trafic Bing organique reste minoritaire côté volume (parts de marché search StatCounter juin 2026 restent autour de 3-4 % Bing hors partenaires vs environ 90 % Google) mais son revenu publicitaire croît deux fois plus vite que la moyenne du marché search publicitaire mondial. Ensuite, la croissance vient explicitement du revenu par recherche et non seulement du volume, ce qui suggère que le mix Copilot / Bing standard, qui inclut des surfaces génératives, monétise mieux par requête. Microsoft ne publie pas le chiffre isolé des annonces sur les surfaces génératives.

Trois limites. Un, la baisse de la contribution des partenariats tiers reste chiffrée uniquement en direction, pas en points. Deux, le chiffre 10 % couvre le trimestre avril-juin 2026, il n'est pas mis en perspective avec la même croissance sur les surfaces génératives seules. Trois, Microsoft ne détaille pas comment le AI Performance report Bing Webmaster Tools (Intents, Topics, Citation Share, Compare) affecte les décisions annonceurs.

**Lien doctrine** : [[concepts/metriques-visibilite-geo]] (dimension revenue-per-search côté annonceur, distincte de la présence citation), [[concepts/tabou-visibilite]] (parler en dollars et en revenue-per-search, pas en « visibilité »).

---

## Brève 2 — Recherche agentique

**Google Cloud publie Open Knowledge Format v0.2 avec cinq signaux de confiance et lève l'anti-redite du 14 juin**

Google Cloud a publié la version 0.2 du Open Knowledge Format (OKF), fresh, couverte par [Open Source For You le 30 juillet 2026](https://www.opensourceforu.com/2026/07/google-introduces-trust-first-update-to-open-knowledge-format/), [Medium Lince Mathew](https://medium.com/@linz07m/google-quietly-shipped-a-new-standard-the-open-knowledge-format-okf-fc7fdafb2b4b), [Flowtivity](https://flowtivity.ai/blog/google-open-knowledge-format/) et [Suganthan Mohanadasan](https://suganthan.com/blog/open-knowledge-format/). L'ajout principal est un ensemble de cinq signaux de confiance destinés à qualifier chaque bundle OKF pour la consommation par un agent LLM : Provenance (sources), Trust (généré ou vérifié), Freshness (via un champ stale_after), Lifecycle (statut de la donnée) et Attestation (via un nouveau concept, Attested Computation).

Le OKF est une spécification ouverte publiée par Google Cloud le 12 juin 2026 (Sam McVeety, Amir Hormati) qui formalise, en dossiers markdown avec frontmatter YAML, le patron « LLM Wiki » décrit par Andrej Karpathy en avril 2025. La v0.1 avait été couverte par cette édition le 14 juin 2026. L'anti-redite explicite posée alors, « ne pas re-traiter OKF sans annonce de connecteur natif autre éditeur, ou v0.2 publiée, ou première mesure d'adoption publique », est levée par la publication de la v0.2 le 30 juillet, ce qui justifie la reprise du sujet.

Ce que change concrètement le v0.2 pour un site éditorial ou une doctrine d'organisation qui alimenterait un agent LLM. Un, l'agent obtient des méta-données objectives (source, fraîcheur, statut) plutôt qu'un score de crédibilité opaque, et peut appliquer ses propres règles de filtrage. Deux, l'ajout de stale_after autorise un consommateur d'agent à écarter une entrée périmée sans avoir à re-fetcher la source, ce qui prolonge la lecture de la doctrine [[concepts/agentic-search]] (l'agent qui agit doit lire vite et de manière fiable). Trois, l'ajout d'Attested Computation ouvre la possibilité qu'un calcul soit signé par une source de confiance ; le mécanisme technique n'est pas encore documenté publiquement dans les reprises.

Deux limites. La v0.2 ne dispose pas encore d'un connecteur natif hors Google Cloud (Microsoft, AWS, Anthropic, Salesforce, ServiceNow, Databricks ne sont pas annoncés). Aucune mesure publique d'adoption OKF, ni pour la v0.1 ni pour la v0.2, n'a été publiée à ce jour. La distinction avec [llms.txt](https://llmstxt.org) reste opérante : OKF sert des dossiers structurés à un agent, llms.txt aiguille un crawler d'indexation vers des pages web.

**Lien doctrine** : [[concepts/agentic-search]], [[concepts/structural-information-geo]], [[concepts/data-proprietaire]] (la doctrine interne d'organisation devient un actif servi directement à des agents, distincte de la publication web).

---

## Brève 3 — Actualité SEO

**Brodie Clark repère des descriptions générées par IA sur les annonces Shopping et Product de Google le 30 juillet**

Le PPC expert Brodie Clark a repéré des descriptions générées par IA affichées à côté des annonces Shopping et Product de Google et l'a publié sur sa page SERP Alert le 30 juillet 2026 ([Search Engine Land](https://searchengineland.com/google-tests-ai-generated-descriptions-in-shopping-ads-484016), [Optimixed](https://www.optimixed.com/google-tests-ai-generated-descriptions-on-shopping-ads/), [Digital Phablet](https://digitalphablet.com/digital-marketing/google-experiments-with-ai-generated-descriptions-for-shopping-ads/)). C'est l'extension d'un test précédent que Google a confirmé pour les annonces Search en juillet, décrit alors comme « a small experiment to see if adding AI-generated context to Search ads helps people make more informed decisions ». Google n'a pas confirmé publiquement l'extension aux Shopping et Product ads.

Deux points opérationnels. Un, l'annonceur perd une part de contrôle éditorial sur la représentation de son produit : le titre, la description marchande et l'image sont toujours contrôlés, mais un texte supplémentaire généré par Google apparaît à côté sans validation annonceur. Deux, la frontière entre l'annonce payante et la réponse générative se rapproche sur la même surface. Un utilisateur voit à la fois une image produit, un prix et un texte reformulé par un moteur, sur un slot qui a été acheté.

Trois limites. C'est un test observé par un tiers, pas un lancement officiel Google. Le format exact (longueur, positionnement, mention d'IA affichée à l'utilisateur) n'est décrit qu'à partir d'une capture d'écran non normative. Aucune mesure d'impact CTR ou CVR n'est disponible. La question opérationnelle pour un consultant qui gère des Shopping campaigns est de surveiller si la description IA apparaît sur ses annonces et de comparer, dès que possible, les métriques avant/après si un test A/B est proposé par Google.

**Lien doctrine** : [[concepts/agentic-search]] (surface d'annonce augmentée d'un texte machine que ni l'annonceur ni l'utilisateur ne pilotent explicitement), [[concepts/tabou-visibilite]] (mesurer CTR et CVR par slot, pas la « visibilité »).

---

Draft SyntheticBrain. Rien n'a été envoyé.
