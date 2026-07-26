# Algorithme. 2026-07-19

## Résumé

- Duane Forrester (Search Engine Journal, 16 juillet) nomme et cartographie le mécanisme de « fingerprint » qui persiste entre SEO classique et réponses IA, distinct sur Google, Bing et ChatGPT.
- Chez Google et Bing, l'héritage est documenté : le budget SEO et le budget GEO ne se coupent pas en deux, ils partagent le même socle. Chez ChatGPT, la persistance reste opaque à la mesure externe.
- John Mueller précise que les écrans anti-bots (« Are You A Bot ») peuvent faire chuter des pages hors de l'index Google et transférer la canonique à un tiers.
- OpenAI publie une refonte de l'app ChatGPT desktop qui rassemble Chat, Work et Codex dans une interface unique sur macOS et Windows, disponible sur tous les plans.
- Avinash Kaushik demande la renégociation immédiate des honoraires SEO d'agence : 25 à 75 pct de baisse attendue sur les périmètres devenus automatisables par les plateformes.

## Info du jour. GEO / search IA. Ce que votre historique SEO transporte, et où il s'arrête

Pilier de l'édition : **GEO / search IA**.

**Le fait, daté.** Le 16 juillet 2026, Duane Forrester publie sur Search Engine Journal un article intitulé « Do The Answer Engines Keep Your Fingerprint, Or Do They Start Fresh Every Time? » ([SEJ 582124](https://www.searchenginejournal.com/do-the-answer-engines-keep-your-fingerprint-or-do-they-start-fresh-every-time/582124/), reprise d'une note de son Substack *Duane Forrester Decodes*). L'article définit un « fingerprint » de domaine comme la trace persistante que la recherche classique a mesurée : volume et vélocité des liens entrants, distribution des textes d'ancre, profondeur de clic, structure du site, Core Web Vitals, signaux d'auteur, âge du domaine, fraîcheur, couverture schema, discipline canonique. La question posée est simple : cette trace continue-t-elle d'alimenter les réponses des moteurs IA, ou chacun repart-il de zéro ?

**Ce qui est documenté.** La persistance est établie sur deux moteurs.

Sur Google, AI Mode et AI Overviews sont adossés au même socle de qualité et de ranking que les résultats organiques. Le blog développeur Google l'écrit noir sur blanc dans sa doctrine site-reputation-abuse et dans plusieurs annonces AI Mode : l'évaluation par section, l'autorité déclarative, la couverture schema, les signaux de qualité de la page contribuent au même index qui sert Search et les surfaces génératives. C'est ce mécanisme que Profound a mesuré indirectement le 14 juillet quand google.com est apparu numéro 2 des domaines cités par AI Mode via Google Business Profiles et Product Knowledge Panels ([SEL 482463](https://searchengineland.com/ai-mode-cites-google-report-482463), déjà traité 16 juillet).

Sur Bing, la persistance est documentée par l'architecture : le protocole IndexNow (soumission bidirectionnelle des URLs) et le produit Web IQ annoncé le 2 juin 2026 ([blogs.bing.com](https://blogs.bing.com/), déjà traité 6 juin) rendent explicite l'unification entre l'index Bing et les surfaces Copilot. Ce que Bing rankait, Bing le cite.

**Ce qui reste opaque.** Sur ChatGPT, Forrester formule une position argumentée : personne, en dehors d'OpenAI, ne peut affirmer avec certitude si un fingerprint par domaine survit au trajet retrieval → génération. ChatGPT interroge l'index Bing, notamment sur les requêtes commerciales, mais la façon dont le modèle sélectionne, pondère ou oublie les signaux issus de cet index n'est pas publiée. La partie « native model weights » (l'idée qu'un modèle porterait une empreinte par domaine dans ses poids d'entraînement) n'a pas de preuve publique. Forrester la marque comme telle, sans la valider. Cette rigueur descriptive est ce qui rend l'article utile.

**Recoupement adjacent.** Le même 16 juillet, Roger Montti relaye sur SEJ une observation de John Mueller reprise depuis Bluesky : le contenu « spécifique » gagne des citations sur les moteurs IA ([SEJ 582531](https://www.searchenginejournal.com/ai-seo-writing-thats-specific-may-get-cited-more/582531/)). L'article ne repose que sur des posts sociaux et un commentaire Mueller, pas sur une étude. Il éclaire cependant la lecture Forrester : ce que les moteurs IA rétiennent en priorité (contenu au niveau du fait précis, ancré sur une entité) recoupe les signaux que Google mesure déjà pour son ranking. Deux angles convergents, deux natures de preuve à ne pas confondre.

**Angle SEO/GEO.** Pour un consultant SEO/GEO, la conséquence opérationnelle est nette. Le découplage budgétaire fréquent « SEO classique pour Google organique, GEO à part pour les moteurs IA » ne tient pas chez Google ni chez Bing : le même travail (liens autoritaires, couverture schema, qualité par section, discipline canonique) sert les deux surfaces. Il tient partiellement pour la part ChatGPT, où l'index Bing est le socle mais le tri final reste hors mesure externe. La grille budgétaire à faire lire au client se pose alors sur trois lignes : ce qui persiste depuis le SEO classique (fondamentaux qui portent sur Google + Bing + AI Mode + AI Overviews + Copilot), ce qui est spécifique aux surfaces IA (structuration en réponse ancrée, densité d'entités, formats prêts à citer), et ce qui est mesurable en propre (rapports GEO Profound, Peec AI, Semrush AI Visibility Index).

**Lien avec la doctrine du wiki.**

- [[concepts/metriques-visibilite-geo]] : Forrester renforce la thèse selon laquelle la position Google ne suffit pas à mesurer la présence dans les réponses IA. Les métriques `Imp_wc` et `Imp_pos` (part de citations dans une réponse, pondérée par position) restent pertinentes en propre, mais elles se lisent maintenant en regard de l'héritage documenté depuis l'index classique. À enrichir : la dimension « part de citations captée par le moteur lui-même » proposée le 16 juillet (Profound google.com #2) se combine avec la dimension « héritage classique persistant » de Forrester pour former une nouvelle grille.
- [[concepts/structural-information-geo]] : le finding SAGEO Arena (title / meta / headings / schema domine le retrieval) s'aligne exactement sur les signaux que Forrester place dans le fingerprint. C'est la même dépendance vue depuis deux angles : côté benchmark académique (SAGEO), côté architecture éditorialisée (Forrester).
- [[concepts/agentic-search]] : la persistance du fingerprint chez Google + Bing est ce qui rend un agent capable de « faire confiance » à une marque déjà en autorité classique. Chez ChatGPT en mode agent, cette confiance est reconstruite à chaque prompt sur des signaux non entièrement mesurables. Le pilier agent-readiness d'une marque n'est donc pas symétrique entre les moteurs.
- [[concepts/tabou-visibilite]] : le fingerprint est une abstraction utile, mais il n'est pas mesurable en tant que tel. Il se pilote via ses composantes (liens, schema, qualité par section), pas via un tableau de bord unifié. C'est le point où le tabou de la « visibilité » retrouve sa force : refuser une métrique globale illusoire quand les proxys existants font le travail.

**Limites documentaires.**

1. Article Forrester = analyse propriétaire d'un auteur (fondateur de UnboundAnswers.com, ancien Bing / MSN Search). Corroboration primaire sur la partie Google (doc Google Search Central) et Bing (blog Bing + Web IQ), pas sur la partie ChatGPT (opacité assumée par l'auteur lui-même).
2. La dimension « native model weights » (empreinte par domaine dans les poids du modèle) n'a pas de preuve publique. Forrester la mentionne comme hypothèse à ne pas soutenir. À ne pas reprendre comme fait.
3. La position Roger Montti / John Mueller sur « contenu spécifique cité davantage » repose sur des posts sociaux (Bluesky @danabra.mov, @tylergaw.com) et un commentaire Mueller repartagé. Cadre valide, pas donnée mesurée. À traiter comme signal éditorial, pas comme étude.

**Prédictions ouvertes ce run.**

- P-2026-07-19-1 : d'ici le 31 mars 2027, un vendor de mesure GEO (Profound, Peec AI, Semrush AI Visibility Index, Athena Intelligence, Ahrefs Brand Radar) publie une méthodologie séparant explicitement une composante « héritage index classique » et une composante « signaux spécifiques réponses IA » avec chiffres comparés sur ≥ 1 000 domaines.
- P-2026-07-19-2 : d'ici le 31 décembre 2026, John Mueller ou un porte-parole Google confirme publiquement (Search Off the Record, doc Search Central, keynote) que Google-Extended et l'index classique alimentent les surfaces AI Mode / AI Overviews sur les mêmes signaux de qualité (héritage explicite documenté).
- P-2026-07-19-3 : d'ici le 31 mars 2027, OpenAI publie ou confirme la présence d'une signalisation par domaine dans le pipeline ChatGPT (au-delà du seul retrieval Bing), ou une étude tierce le prouve par mesure indirecte reproductible.

---

## Brèves

### Brève 1. Actualité SEO. Les écrans « Are You A Bot » peuvent faire chuter vos pages hors de l'index Google

John Mueller a précisé, dans un épisode récent du podcast Google *Search Off the Record*, ce qui arrive quand un système de sécurité (protection anti-bots type Cloudflare Turnstile, hCaptcha, reCAPTCHA) juge Googlebot suspect et lui sert un écran de vérification à la place du contenu. Matt G. Southern relaye la précision sur Search Engine Journal le 17 juillet ([SEJ 582801](https://www.searchenginejournal.com/are-you-a-bot-screens-can-get-your-pages-dropped-by-google/582801/)).

Le mécanisme est le suivant : Google indexe la page telle que servie. Si l'écran de vérification remplace le vrai contenu, c'est cet écran qui rentre en index. Beaucoup de sites servent le même modèle générique. Google traite alors ces pages comme des doublons, en choisit une comme canonique et déclasse les autres. Si votre page réelle a été précédemment indexée sur une URL similaire à celle d'un tiers, la canonique peut basculer chez ce tiers.

**Angle SEO.** Le point de contrôle : la Search Console (rapport d'indexation, URL Inspection). Un audit des pages qui sont derrière un mur de vérification (checkout, calculateurs, tarification protégée, formulaires complexes) devient une brique standard. Pas de figures publiées dans l'article, pas de nom de service explicitement pointé par Mueller : la précision porte sur le principe, pas sur une action produit.

### Brève 2. Recherche agentique. OpenAI unifie Chat, Work et Codex dans une app ChatGPT desktop

Le 18 juillet 2026, OpenAI publie une refonte de son application desktop ChatGPT. Un sélecteur global permet de basculer entre ChatGPT et Codex. À l'intérieur de ChatGPT, deux modes : Chat pour les échanges rapides, Work pour l'exécution de tâches de bout en bout. Les conversations Chat et Work partagent la vue Recents, avec tri, filtre et épinglage. Les Projets ChatGPT sont accessibles dans l'app. Les conversations Work sont synchronisées cloud entre web, mobile et desktop. La mise à jour est déployée sur macOS et Windows, tous plans confondus, y compris Free ([OpenAI Help Center](https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app), reprise [Neowin](https://www.neowin.net/news/openai-launches-chatgpt-work-and-unveils-unified-desktop-app-with-codex-built-in/) et [Developers Digest](https://www.developersdigest.tech/blog/chatgpt-work-codex-desktop-app)).

**Angle GEO / agent.** Le runtime agent Work (lancé le 9 juillet dans GPT-5.6, déjà traité) devient accessible dans le même contexte visuel que Chat. La distinction disparaît côté utilisateur : entre une question à ChatGPT et une tâche multi-étapes exécutée par l'agent, la porte d'entrée est la même surface. Pour la mesure, cette unification déplace le point d'observation : ce qui compte n'est plus « qui a écrit le prompt Chat » vs « qui a lancé une tâche Work », c'est la nature de la sortie (réponse citée / action exécutée sur un site tiers). À suivre : la publication éventuelle d'un rapport de mesure des sites visités par Work (rien de publié à ce stade).

### Brève 3. Business SEO. Avinash Kaushik demande 25 à 75 pct de baisse sur les honoraires SEO d'agence

Le 17 juillet 2026, Search Engine Journal publie une prise de position d'Avinash Kaushik (chief strategy officer chez Human Made Machine, 16 ans passés chez Google, ex-Intuit et DirecTV) : les annonceurs devraient renégocier maintenant leurs contrats d'agence SEO et attendre entre 25 et 75 pct d'économie sur les périmètres devenus automatisables ([SEJ 581891](https://www.searchenginejournal.com/avinash-kaushik-says-renegotiate-now-seo-fees-25-to-75-lower/581891/)).

L'argument est direct : l'architecture de compte, la structuration audience et mot-clé, la construction de campagne sont désormais gérées à ~ 80 pct par les algorithmes de plateforme, avec un meilleur résultat qu'une équipe humaine. Kaushik propose une grille d'honoraires en trois blocs. Un retenue de base (gouvernance, pilotage, ingénierie de la donnée) à 40 à 50 pct du total. Des honoraires projet pour les travaux nécessitant du jugement humain, à 30 à 40 pct. Un incitatif de résultat sur profit incrémental ou revenu vérifié, à 15 à 25 pct.

**Angle Business SEO.** L'opinion est mono-source et clairement à charge. La grille proposée est cependant utile : elle donne un vocabulaire clair pour reformer un contrat, en séparant la valeur « pilotage stratégique + data engineering + jugement expert » de la valeur « exécution », dont le prix de marché baisse. À creuser : d'autres praticiens (Rand Fishkin, Aleyda Solís, Kevin Indig) publieront-ils une grille comparable dans les 90 jours ? C'est le signal à suivre pour déterminer si Kaushik ouvre un mouvement de fond ou reste isolé.

---

Draft SyntheticBrain. Rien n'a été envoyé.
