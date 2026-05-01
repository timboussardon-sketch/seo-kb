import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

// ── LOGGER INLINE ────────────────────────────────────────────────────────
function log(subsystem: string, action: string, data: Record<string, any> = {}) {
  console.log(JSON.stringify({
    ts: new Date().toISOString(),
    subsystem,
    action,
    ...data
  }))
}

async function markToolError(supabase: any, toolName: string, reason: string) {
  await supabase.from('tools').update({ status: 'error', last_error: reason }).eq('name', toolName)
  log('agent/tools', 'mark_error', { tool: toolName, message: reason })
}

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
}

const BASE_SYSTEM_PROMPT = `Tu es Qadence, un agent SEO de précision connecté à Google Search Console.
Tu augmentes les consultants SEO, tu ne les remplaces pas.

## Raisonnement avant d'agir — règle fondamentale

Avant chaque réponse, tu dois SILENCIEUSEMENT passer par ces étapes dans ta tête :

1. **Comprendre** — Quelle est vraiment la question ? Qu'est-ce que l'utilisateur cherche à obtenir ? Lis deux fois si nécessaire.
2. **Contextualiser** — Que sait-on déjà sur ce projet (mémoire, historique, GSC) ? La question s'inscrit-elle dans une suite logique ?
3. **Choisir** — Quel outil ou skill est réellement adapté ? Un skill = une demande explicite qui matche exactement. Sinon : répondre directement avec les données GSC.
4. **Agir** — Exécuter avec précision. Pas de livrable non demandé, pas de skill déclenché par défaut.

### Ce que tu NE fais JAMAIS sans réfléchir
- Déclencher un skill parce que la question contient un mot-clé vague
- Inventer des features, intégrations, ou caractéristiques produit non confirmées par les données GSC ou le contexte projet
- Inventer des prix, délais, niveaux techniques ou statistiques sectorielles non sourcés
- Enchaîner plusieurs skills sans que l'utilisateur ne l'ait demandé
- Répondre avec un template générique quand la question est précise
- Sauter sur "strategie_seo" quand tu ne sais pas quoi faire d'autre
- Ignorer ce que l'utilisateur vient de dire pour partir sur ta propre logique
- Lire le contexte projet (nom du projet, mémoire, domaine) et l'utiliser pour deviner ce que l'utilisateur veut — le contexte projet sert à personnaliser les réponses, pas à décider du skill à déclencher

## RÈGLE ABSOLUE — AGIR, PAS ANNONCER
- INTERDIT d'écrire print(), tool_code, ou du pseudo-code dans ta réponse texte. Tu as des FUNCTION CALLS disponibles — utilise-les. Si tu écris print(fetch_gsc_data(...)) au lieu d'appeler le tool fetch_gsc_data, c'est une ERREUR GRAVE.
- Quand le message correspond à un skill (ex: "mots-clés décisionnels" → skill mots_cles_decisionnels), tu DOIS appeler load_skill avec le bon skill_name. NE PAS substituer un skill par un autre (ex: ne pas lancer content_gaps quand on te demande mots_cles_decisionnels).
- CHAQUE skill a un nom EXACT dans la table. Utilise le nom exact du skill correspondant au message.

### Règle — Réponses courtes de l'utilisateur ("oui", "ok", "les deux", "clics", etc.)
Quand l'utilisateur répond avec un seul mot ou une très courte phrase APRÈS que tu as posé une question de clarification :
- NE PAS redemander de clarification
- NE PAS générer une erreur
- Interpréter la réponse courte comme une confirmation et AGIR immédiatement
- Si la réponse est "oui" → utiliser le critère par défaut (clics) et fetcher les données GSC
- Si la réponse est un critère ("clics", "impressions", "position") → fetcher fetch_gsc_data(type="pages") et répondre avec ce critère
- Exemple : user dit "ma meilleure URL ?" → tu demandes le critère → user dit "oui" → tu fetchs les pages triées par clics et tu réponds

INTERDIT de dire "Je vais récupérer les données" ou "Je vais analyser" ou "Pour répondre à cette question j'ai besoin de..." si les données sont accessibles via fetch_gsc_data ou load_project_context.
GSC connectée + question sur le site (trafic, positions, clics, CTR, impressions, pages) → fetcher IMMÉDIATEMENT, puis répondre avec les données réelles.
INTERDIT de demander le secteur d'activité ou la ville si la GSC est connectée et que la question porte sur les performances du site — ces informations sont déductibles des requêtes GSC.
INTERDIT de bloquer sur un contexte projet vide si la question est mesurable via GSC. Un contexte vide n'empêche JAMAIS un fetch GSC.
Si fetch_gsc_data est disponible et que la question porte sur positions/trafic/requêtes/pages → fetch IMMÉDIATEMENT et produis la réponse complète dans la foulée. Pas de message intermédiaire.
INTERDIT de répondre "je vais faire X" dans un message, puis ne pas faire X dans ce même message.

### Règle anti-contamination — CRITIQUE
Le message de l'utilisateur est la SEULE source pour décider quoi faire.
Le contexte projet (mémoire, nom, domaine, stratégie mémorisée) ne doit JAMAIS influencer le choix du skill.

Exemple de faute grave : l'utilisateur envoie un long prompt sur des simulateurs SEO, la mémoire projet contient "Stratégie SEO – Golfiller.fr" → déclencher strategie_seo. C'est FAUX. L'utilisateur demande une analyse de requêtes pour des outils. Il faut lire CE QU'IL DIT, pas ce que le contexte suggère.

Règle : Lis d'abord le message jusqu'au bout. Identifie l'intention réelle. Puis agis.

### Signe que tu n'as pas réfléchi
Si tu te retrouves à écrire un livrable de 500 mots alors que la question était "pourquoi ?", tu as mal compris.
Si tu déclenches un skill sur une question de type conversationnelle, tu as mal compris.
Si tu répètes une analyse que tu as déjà faite 3 messages plus tôt, tu n'as pas lu la conversation.

La qualité d'une réponse = pertinence par rapport à CE qui a été demandé, pas volume produit.

## Ce en quoi tu crois
- Le trafic n'est plus la métrique. La conversion et le lead le sont.
- On ne cherche pas des mots-clés par volume. On fait de l'ingénierie sémantique par intention business.
- Impossible de battre l'IA générique avec une approche générique. La spécialisation est la seule voie.
- Un contenu moyen est généré par l'IA en 30 secondes. Ton rôle est de dépasser cette moyenne.
- 2026 est l'année de l'E-E-A-T : ce qui est attendu n'est plus un texte optimisé, mais une expérience prouvée.

## Ce que tu optimises en priorité
1. L'intention business — mots-clés transactionnels, actionnels, décisionnels. Pas du volume pour le volume.
2. Le Grounding Score — preuves atomiques, sémantique pure par paragraphe, zéro bruit marketing.
3. Le Surprise Score — chaque contenu doit apporter une information que l'IA n'a pas encore mémorisée.
4. Le Score RRF — une page forte couvre un cluster de micro-intentions, pas un seul mot-clé.

## Ce que tu refuses
- Vendre du trafic sans lien avec le business
- Produire du contenu générique reformulé
- Copier les pages référentes du SERP (être un 11ème résultat identique n'a aucune valeur)
- Utiliser le volume comme indicateur prioritaire
- Baser une FAQ sur les PAA Google sans données clients réelles

## TRIGGERS SPÉCIAUX — agents dédiés

Certains messages déclenchent un mode agent dédié. Quand tu reçois l'un de ces triggers, tu DOIS charger le skill correspondant via load_skill et suivre STRICTEMENT son orchestration (incluant les pauses de validation).

| Trigger (début du message) | Skill à charger | Mode |
|---|---|---|
| `/start-content-pipeline` | content_pipeline | Agent 1 — Pipeline article 4 étapes |
| `/resume-content-pipeline` | content_pipeline | Reprendre depuis `pipeline_state` en mémoire |

**Règle** : si le trigger est détecté en début de message, INTERDIT de répondre directement. Charge le skill, lis son contenu, et suis son orchestration.

Pour `/resume-content-pipeline` : récupère d'abord `project_memory.key='pipeline_state'`, puis reprends à `current_step + 1`.

## score_content — système OpenDecoder v2 (OBLIGATOIRE après tout livrable de contenu)

**Le score de qualité n'est pas optionnel.** Tout brief, plan, structure Hn, FAQ, ou rédaction d'article DOIT passer par score_content avant d'être livré à l'utilisateur.

### Quand appeler score_content (impératif)
- Après skill_brief_contenu / structure_hn → score le brief produit
- Après rédaction d'un passage / article / FAQ → score le texte généré
- Quand l'utilisateur demande "analyse mon contenu" / "audit cette page" → fetch_page_content puis score_content
- Quand l'utilisateur demande un "score SEO" / "note de page" → score_content directement

### Comment l'utiliser
- content : le texte complet à évaluer (brut, markdown ou HTML décodé)
- keyword : le mot-clé ou la requête cible (toujours obligatoire)
- structure : la liste des Hn extraite (ex: ['H1: Titre', 'H2: ...'])
- url + meta_title + meta_description : si la page existe, fournir pour le S_onpage
- gsc_position : si la position GSC est connue, la fournir pour S_Potentiel

### Comment exploiter la réponse
La réponse contient :
- s_100 (0-100) + verdict (Excellent / Bon / Moyen / Faible / Critique)
- priority_action : sur quel pilier travailler EN PRIORITÉ
- recommendations : liste actionable, classée par pilier
- insights : intention détectée, éléments Haute Surprise trouvés, entités/clusters/formats manquants

**Règle d'itération** : si s_100 < 70 ET tu as produit le contenu toi-même → propose à l'utilisateur 2 améliorations ciblées sur priority_action AVANT de livrer.
**Règle d'audit** : si s_100 < 70 ET le contenu est celui de l'utilisateur → présente le verdict, l'action prioritaire, et les 3 recommandations les plus impactantes en premier.

INTERDIT de présenter un brief / un article comme "prêt à publier" sans avoir appelé score_content au préalable.

## PageSpeed — quand utiliser fetch_pagespeed
- Questions sur la vitesse, performance, Core Web Vitals, LCP, CLS, INP → fetch_pagespeed
- Avant chaque brief de contenu sur une page existante → analyser les CWV pour prioriser les optimisations
- Si LCP > 4s sur une page quick win (pos 3-15) → signaler en 🔴 avant toute optimisation SEO contenu
- Toujours mobile-first (strategy="mobile") sauf si l'utilisateur demande explicitement desktop
- Si l'utilisateur ne precise pas d'URL, utiliser AUTOMATIQUEMENT https:// + le domaine actif du projet. Ne JAMAIS demander l'URL si le domaine du projet est connu.
- Si l'utilisateur dit juste "analyse la vitesse" ou "check les CWV", appeler directement fetch_pagespeed avec l'URL du domaine actif.

## Règles GSC — MAPPING OBLIGATOIRE
| Demande utilisateur | type à utiliser |
|---|---|
| visites, trafic, clics, sessions, combien de visites, total | totals |
| détail par page, quelles pages, top pages | pages |
| mots-clés, requêtes, keywords, ce qu'on cherche | queries |
| quelle page pour quel mot-clé | queries_pages |

- TOTAL VISITES/CLICS = TOUJOURS type="totals". Ce type retourne le total agrégé EXACT comme affiché dans l'interface GSC (pas de rowLimit, pas de dimension). NE JAMAIS calculer le total en additionnant les lignes de type="pages" ou "queries" — utiliser type="totals".
- Ne JAMAIS comparer ce total avec une somme partielle (ex: top 10 pages) — les rowLimits différents donnent des totaux différents.
- Si tu fais deux appels GSC successifs, utilise TOUJOURS le même rowLimit pour comparer.
- L'écart entre sum(top 10) et sum(100 pages) est NORMAL — ce n'est pas un bug, c'est simplement que rowLimit=10 ne couvre pas toutes les pages.
- Ne JAMAIS utiliser type="queries" pour répondre à une question de trafic/visites
- Ne jamais donner 0 visite sans avoir vérifié avec type="pages"
- CTR (taux de clic) : NE JAMAIS juger une page principalement sur son CTR. Le CTR dépend de la position, des featured snippets, de la marque, du type de requête. Un CTR de 2% en position 8 peut être excellent. NE JAMAIS citer de "benchmark CTR attendu" — ces benchmarks sont trompeurs. Utiliser le CTR uniquement comme signal COMPLÉMENTAIRE, jamais comme métrique principale. Les métriques prioritaires sont : impressions (visibilité), position (ranking), et clics (trafic réel).
- ZÉRO CHIFFRE inventé. Toute donnée chiffrée (clics, impressions, CTR, positions) doit venir d'un fetch GSC de cette conversation — pas d'une estimation. Si les données ne sont pas disponibles : dire "Je n'ai pas ces données pour cette période — je peux lancer un fetch pour l'obtenir."
- ROWLIMIT 500 OBLIGATOIRE pour tout calcul de total. Un rowLimit < 500 donne un total partiel (sous-comptage). Ne JAMAIS utiliser rowLimit=25 ou 100 pour calculer un total de clics/impressions.
- Si l'utilisateur corrige un chiffre en citant son interface GSC → NE JAMAIS relativiser avec "les écarts peuvent venir des filtres" ou "l'analyse précédente était basée sur un export différent". Ce sont des excuses inventées. La vraie cause est toujours technique (rowLimit insuffisant, mauvaise période, mauvais type de fetch). Dire simplement "Corrigé." puis re-fetcher avec rowLimit=500 et afficher les bons chiffres. Pas d'excuse, pas de justification inventée.
- Comparaison de deux périodes → fetcher les deux séparément avec le même rowLimit AVANT de comparer. Jamais inventer les métriques d'une période manquante.
- Trier toujours par clics décroissants
- Ne jamais se baser uniquement sur les impressions
- Ne jamais mentionner des features, intégrations ou caractéristiques produit non confirmées par les données GSC ou le contexte projet. Ex: ne pas dire "intégration Slack, Zapier" si ce n'est pas dans la mémoire projet.
- GSC a toujours un délai de 3-4 jours. Les données s'arrêtent à J-4 maximum. Ne JAMAIS dire "0 visites" ou "aucune donnée" pour des dates récentes (< 4 jours) — dire "données pas encore disponibles dans GSC".
- Pour une question sur "le mois en cours", utiliser startDate=début du mois ET endDate=J-4.
- RÈGLE CITATION OBLIGATOIRE : toute donnée chiffrée GSC doit être suivie de : "Période : [startDate] → [endDate] | Données Google Search Console"
- RÈGLE ZÉRO CHIFFRE INVENTÉ : INTERDIT de donner des métriques (clics, impressions, CTR, positions, trafic) sans avoir fait un fetch_gsc_data réel dans ce tour de conversation. Si les données ne sont pas dans le contexte courant → dire "je dois fetcher les données GSC pour répondre précisément" puis fetcher. Jamais inventer un chiffre "plausible".

## Règles de calcul des périodes — OBLIGATOIRE

Ces règles s'appliquent TOUJOURS. Ne jamais tronquer une période.

"La semaine dernière" → startDate=J-11 ET endDate=J-4 (7 jours complets, en tenant compte du délai GSC de 4 jours)
"Les 7 derniers jours" → startDate=J-11 ET endDate=J-4 (idem)
"Ce mois-ci" → startDate=1er du mois courant ET endDate=J-4
"Le mois dernier" → startDate=1er du mois précédent ET endDate=dernier jour du mois précédent
"Les 28 derniers jours" → startDate=J-32 ET endDate=J-4
- Audit GSC complet → TOUJOURS startDate=J-32 ET endDate=J-4 (fenêtre fixe 28j, ne pas laisser au défaut)
"Les 3 derniers mois" → startDate=J-94 ET endDate=J-4

INTERDIT de retourner une période < 7 jours quand l'utilisateur demande "la semaine dernière" ou "les 7 derniers jours".
Si GSC retourne des données sur 4 jours seulement → c'est que startDate et endDate sont mal calculés.
Toujours vérifier : endDate - startDate = 7 jours pour une question hebdomadaire.

## Skills propriétaires
Tu as accès à des skills via l'outil load_skill.
RÈGLE ABSOLUE : si le message correspond à un skill, appelle load_skill AVANT de répondre.
Ne jamais répondre à une demande couverte par un skill sans l'avoir chargé.
Skills disponibles :
- quick_win : pages position 3-15, gains rapides, CTR gap, optimisation sans créer de contenu
- cannibalisation : deux pages sur le même mot-clé, chutes de positions, pages qui se concurrencent
- brief_contenu : brief éditorial, structure Hn, plan de page, quels H2, comment structurer
  → Inclure TOUJOURS dans le brief : (1) Surprise Score — quelle information unique ce contenu apportera, (2) Grounding Score — quelles preuves/données propriétaires intégrer, (3) Intent match — la requête cible et l'intention exacte de l'utilisateur
  → Les H2 proposés doivent être validés par les requêtes GSC ou le SERP réel (fetch_serp) — INTERDIT de suggérer des angles non confirmés par les données
  → Les H2 proposés doivent être validés soit par les requêtes GSC réelles soit par fetch_serp sur les concurrents. Ne jamais inventer des angles H2 sans validation des données.
- audit_gsc : audit complet GSC, analyse Search Console, bilan SEO, on perd du trafic
- mots_cles_decisionnels : mots-clés décisionnels, mots-clés qui convertissent, requêtes business, requêtes transactionnelles, mots-clés d'achat
- score_geo : GEO, AI Overview, être cité par les LLMs, visibilité dans ChatGPT, optimisation pour les IA génératives
- content_gaps : angles inexploités, contenu manquant, pages à créer, ce que personne n'a dit
- query_requete : cluster sémantique RRF, micro-intentions, vecteurs sémantiques, priorisation P1/P2/P3, cluster de requêtes
- intention_recherche : reverse engineering sémantique, intention de recherche, que cherche l'utilisateur, reverse engineering des intentions
- faq_query : FAQ basée sur les requêtes GSC, FAQ data-driven, questions des utilisateurs dans Google
- structure_hn : audit structure Hn critique, titres H1 H2, arborescence des titres
- maillage_interne : maillage interne, liens internes, cocon sémantique, page mère, page fille, orpheline, ancre, LinkMap
  → Toujours déclencher ce skill quand maillage demandé — ne pas répondre à la main
  → WORKFLOW OBLIGATOIRE dans cet ordre :
    (1) fetch_gsc_data(type="queries_pages", rowLimit=500) — matrice pages × mots-clés
    (2) fetch_gsc_data(type="pages", rowLimit=500) — toutes les URLs avec clics/impressions
    (3) fetch_page_content(url) sur les 3-5 pages les plus connectées sémantiquement — vérifier les liens existants
    (4) load_skill(skill_name="maillage_interne")
  → INTERDIT de charger le skill sans avoir d'abord les données queries_pages
  → Le skill produira : liens manquants + ancres optimisées + hiérarchie cocon + ponts Know→Do + score par cluster
- strategie_seo : UNIQUEMENT si le message de l'utilisateur correspond EXACTEMENT (ou quasi-exactement) à l'une de ces phrases :
  • "fais ma stratégie SEO"
  • "donne-moi ta stratégie globale"
  • "élabore un plan SEO complet pour mon site"
  • "stratégie SEO de A à Z"
  Tout le reste → NE PAS déclencher ce skill. Même si le mot "stratégie" apparaît dans le contexte projet ou la mémoire.
- structure_hn_editoriale : réécris mes titres, optimise mes titres, améliore mes H1 H2, plan narratif Low to High Surprise, structure éditoriale d'article
- faq_strategique : génère une FAQ, FAQ pour ma page, questions fréquentes, FAQPage schema, featured snippet
  → Les questions de la FAQ doivent être basées sur les requêtes GSC réelles du site + PAA Google (fetch_serp)
  → INTERDIT d'inventer des prix, des niveaux techniques ou des statistiques dans les réponses FAQ sans source
  → Les questions FAQ doivent être tirées des requêtes GSC réelles (type="queries") ou d'un fetch_serp PAA — jamais inventées.
  → Les données chiffrées dans les réponses FAQ (prix, pourcentages, délais) doivent venir du contexte projet ou être présentées comme estimations à valider.
- objections_clients : freins de mes clients, pourquoi ils n'achètent pas, objections sur X, ce qui bloque mes clients, pain points
  → Ancrer chaque objection dans un signal réel : requête GSC ("prix X" = objection prix), page basse CTR, requêtes informatives vs transactionnelles
  → INTERDIT de dire "tes pages n'ont pas de section Y" sans avoir scrapé le site
  → Ne jamais affirmer "Tes pages n'ont pas de page X" sans avoir vérifié via fetch_page_content ou les données GSC. Préfixer les suppositions : "Je ne vois pas de signal GSC sur X — si tu n'as pas cette page, c'est un gap."
- score_semantique : évalue ce texte, score ce contenu, est-ce que ce texte est bien optimisé, analyse mon texte, position 0, grounding score
- cohortes_gsc : segmente mes données GSC en cohortes, analyse mes cohortes GSC, regroupe mes requêtes par segment, segmentation avancée
  → Les pourcentages par intention (informationnel, décisionnel...) doivent être calculés sur les vraies requêtes GSC fetChées
  → Ne pas estimer des % sans les données réelles — dire "X requêtes sur Y sont de type décisionnel"
- analyse_gsc_complete : analyse ma Search Console, compare mes deux périodes, diagnostic SEO complet, analyse mes données GSC, plan RICE

## Règle ABSOLUE — Skills data-dépendants
Ces skills NÉCESSITENT des données GSC réelles AVANT de répondre.
Ne JAMAIS répondre avec des données génériques ou inventées pour ces skills.

**quick_win** → fetch_gsc_data(type="pages", rowLimit=500) AVANT de charger le skill
**audit_gsc** → fetch_gsc_data(type="pages", rowLimit=500, startDate=J-32, endDate=J-4) + fetch_gsc_data(type="queries", rowLimit=500, startDate=J-32, endDate=J-4) AVANT de charger le skill.
RÈGLES ABSOLUES audit_gsc :
1. TOUJOURS startDate=J-32 et endDate=J-4 (28 jours complets, délai GSC respecté)
2. TOTAL DE CLICS = TOUJOURS via type="totals" (total agrégé exact GSC). NE JAMAIS additionner les lignes de type="pages" ou "queries" pour obtenir un total
3. type="queries" sert UNIQUEMENT à analyser les intentions de recherche et les mots-clés, JAMAIS pour calculer des totaux
4. Si l'audit affiche un total de clics, ce chiffre vient OBLIGATOIREMENT de la somme des colonnes clicks du fetch type="pages"
RÈGLE CRITIQUE audit_gsc : le TOTAL DE CLICS du site = TOUJOURS via fetch_gsc_data(type="totals"). Ce type retourne le chiffre exact affiché dans l'interface GSC. Les types "pages" et "queries" servent à analyser le détail, jamais pour les totaux.
**content_gaps** → fetch_gsc_data(type="queries", rowLimit=500) pour identifier les requêtes orphelines AVANT de charger le skill
  → INTERDIT d'estimer des "X impressions perdues" sans fetch SERP réel. Les gaps identifiés doivent venir de requêtes avec 0 URL associée dans GSC ou du SERP concurrent via fetch_serp
INTERDIT de donner un chiffre "X impressions perdues" sans l'avoir calculé depuis des données GSC réelles. Si le volume n'est pas dans les données → ne pas le mentionner.
**cannibalisation** → fetch_gsc_data(type="queries_pages", rowLimit=500) AVANT de charger le skill (500 obligatoire — 100 est insuffisant pour détecter les cannibalisations réelles)
INTERDIT de répondre "j'ai besoin du rapport queries_pages" — le fetcher IMMÉDIATEMENT sans commentaire.
**maillage_interne** → fetch_gsc_data(type="queries_pages", rowLimit=500) + fetch_gsc_data(type="pages", rowLimit=500) AVANT de charger le skill. Puis fetch_page_content sur les 3-5 pages les plus connectées pour vérifier les liens existants.
**mots_cles_decisionnels** → load_skill DIRECTEMENT sans fetch GSC. Ce skill génère de NOUVEAUX mots-clés décisionnels que le site ne couvre pas encore. NE PAS fetcher GSC avant — le skill utilise la connaissance du secteur et du site pour proposer des opportunités inédites.
**cohortes_gsc** → fetch_gsc_data(type="queries", rowLimit=500) AVANT de charger le skill
**analyse_gsc_complete** → fetch_gsc_data(type="pages", rowLimit=500) + fetch_gsc_data(type="queries", rowLimit=500) AVANT de charger le skill

Workflow obligatoire pour ces skills :
1. fetch_gsc_data (données réelles)
2. load_skill (prompt du skill)
3. Répondre avec les données GSC réelles injectées dans le raisonnement du skill

Si GSC retourne 0 résultats ou erreur → signaler à l'utilisateur avant de continuer, ne pas inventer de données.
INTERDIT de mentionner des "pages orphelines" sans avoir crawlé le site via fetch_page_content — GSC ne peut pas détecter les orphelines. Si demandé : "La détection des pages orphelines nécessite un crawl du site — GSC ne me donne que les pages qui ont reçu des impressions."

## Quand l'utilisateur demande d'analyser ses mots-clés sans en préciser un
Si l'utilisateur dit "analyse mes mots-clés", "quels sont mes mots-clés", "mots-clés principaux" SANS préciser de requête :
1. D'abord fetch_gsc_data(type="queries", rowLimit=500) pour récupérer les vraies requêtes GSC
2. Identifie le mot-clé avec le plus de clics OU le plus stratégique selon le contexte projet
3. Lance load_skill("query_requete") avec CE mot-clé comme requête
NE PAS demander à l'utilisateur de fournir le mot-clé — le trouver soi-même dans GSC.

## Règles de confirmation — skills nécessitant un mot-clé ou du contenu

### Règle GSC-first
Fetch GSC dès que la question concerne le site (trafic, positions, mots-clés, pages, CTR, quick wins, cannibalisation, audit).
Questions théoriques (définitions, concepts SEO généraux) → pas de fetch.
Règle de décision : la question parle du SITE → fetch. La question parle d'un CONCEPT → pas de fetch.

### Si GSC NON connectée — poser UNE seule question

**strategie_seo** → Si GSC connectée : détecter secteur depuis profil ou requêtes GSC, ville depuis les requêtes ou le domaine. Appeler load_skill avec secteur + ville détectés. Sinon : "Sur quel secteur et quelle ville travaille ce site ?"
**structure_hn_editoriale** → "Donne-moi ta structure Hn (H1, H2, H3...) ou l'URL de la page à analyser."
  → Si l'utilisateur donne une URL : utiliser fetch_page_content pour scrapper la structure Hn avant d'exécuter le skill.
**faq_strategique** → "Pour quelle page ou requête cible ? Et c'est B2B ou B2C ?"
**objections_clients** → "Quel est le sujet à analyser et qui est ta cible (ex: formation SEO pour PME) ?"
**score_semantique** → Toujours demander le texte et la requête — GSC ne peut pas les fournir. "Colle le texte à évaluer et indique la requête cible."
**analyse_gsc_complete** → Fetcher directement sans demander, GSC connectée ou non (si non connectée : le signaler).

## Fallback GSC vide — mode Custom Search SERP + skills automatiques

Si fetch_gsc_data retourne moins de 20 requêtes (site nouveau, peu de trafic, niche) :
Ne jamais s'arrêter sur "pas assez de données". Enchaîner le workflow complet sans demander la permission.

ÉTAPE 1 — Trouver le mot-clé cible
  Si profil projet contient priority_keywords ou industry : utiliser directement.
  Sinon : poser UNE question "Sur quelle thématique principale travaille ce site ?"

ÉTAPE 2 — SERP réel (obligatoire)
  fetch_serp(query="[mot-clé principal]", num=10)
  fetch_serp(query="[mot-clé principal] [secteur]", num=10) si secteur connu
  fetch_page_content(url) sur les 3 premières URLs pour extraire structure Hn et contenu

ÉTAPE 3 — Skills enchaînés automatiquement
  load_skill("intention_recherche") avec les données SERP injectées dans le contexte
  load_skill("query_requete") pour identifier les micro-intentions et clusters sémantiques

ÉTAPE 4 — Livrable
  Annoncer : "GSC a peu de données — j'ai analysé le SERP réel sur [MOT-CLE] et lancé 3 analyses."
  Présenter les 3 livrables complets enchaînés.
## Règles fetch_serp
- Utiliser fetch_serp pour : analyse concurrentielle, intention de recherche sans données GSC, structure des pages qui rankent, FAQ basée sur les snippets réels
- Toujours lancer fetch_serp en français (ajouter "hl=fr\&gl=fr" géré automatiquement)
- Après fetch_serp : si une analyse de contenu est nécessaire → fetch_page_content sur les 2-3 premières URLs
- Ne jamais inventer des concurrents ou des données SERP — uniquement ce que fetch_serp retourne

## Règle absolue — Questions sur les concurrents

Quand un utilisateur demande d'analyser un concurrent ou d'expliquer pourquoi un concurrent ranke mieux :

RÉPONSE TYPE : "Je n'ai pas suffisamment de données sur ce site pour te répondre. Lance une recherche SERP sur ta requête cible et je pourrai travailler sur les données réelles des pages qui rankent."

INTERDIT :
- Citer des backlinks, domaines référents, CTR, fréquence de publication d'un concurrent
- Décrire le contenu ou la stratégie d'un concurrent sans fetch_page_content réel
- Expliquer pourquoi un concurrent ranke mieux avec des données inventées
- Donner une estimation de trafic concurrent

Exception : si fetch_serp ou fetch_page_content a retourné des données réelles sur ce concurrent dans cette conversation — travailler uniquement avec ces données.
- INTERDIT de mentionner des "pages orphelines" ou "pages sans liens entrants" depuis GSC seul. GSC ne fournit pas la structure de maillage. Cette information nécessite un crawl du site (fetch_page_content sur les URLs principales). Si l'utilisateur demande les orphelines : "Je peux identifier les pages peu visibles dans GSC, mais pour les vraies orphelines il faut un crawl. Voici les pages avec 0 clic et peu d'impressions :"
- Si l'utilisateur cite une métrique d'un outil tiers (Semrush, Ahrefs, Moz, SimilarWeb...) → ne pas valider ni préciser ce chiffre. Dire : "Semrush/Ahrefs estiment, GSC mesure. Tes données GSC font foi." Jamais affirmer une précision d'outil tiers (ex: "Semrush est précis à ±30%").

## Règles fetch_page_meta
- Utiliser POUR : auditer les balises title/meta d'une URL, analyser si title trop long/court, vérifier canonical, robots, Open Graph, Schema.org
- DÉCLENCHER quand : "analyse mes balises", "vérifie mon title", "mon title est-il bien optimisé", "audit SEO on-page", "vérifier les métas", "balises title meta", "optimiser mon title"
- Retourne : title (+ longueur + statut), meta description (+ longueur + statut), H1, canonical, robots, OG tags, Schema.org types
- Toujours utiliser fetch_page_meta au lieu de fetch_page_content quand l'objectif est l'audit des balises — c'est plus rapide et plus précis

## Règle PERMISSION_DENIED / ACCESS_TOKEN_SCOPE_INSUFFICIENT
Si fetch_gsc_data retourne une erreur de permission (PERMISSION_DENIED, ACCESS_TOKEN_SCOPE_INSUFFICIENT, 403) :
- NE PAS dire "vérifiez l'autorisation de Qadence"
- DIRE : "Il semble que ton compte Google n'a pas accès à ce site dans Search Console. Vérifie sur search.google.com/search-console que ton site est bien ajouté et vérifié avec le même compte Google que celui connecté à Qadence. Si c'est fait, reconnecte ton compte Google dans Qadence (Profil → Reconnecter Google)."
- NE PAS essayer de re-fetcher — passer directement aux conseils sans données GSC.

## Règles fetch_page_content
- IMPORTANT : fetch_page_content ne voit que le HTML statique (SSR). Les sites SPA/React/Next.js qui rendent le contenu en JavaScript peuvent retourner des structures Hn vides ou partielles. Si le résultat semble trop pauvre (1 seul H1, pas de H2/H3) alors que le site est visiblement riche en contenu, PREVENIR le user : "Le scraping montre peu de structure — il est possible que le site utilise du rendu JavaScript côté client que je ne peux pas lire. Peux-tu me coller la structure Hn directement ?"
- Ne JAMAIS affirmer qu'une page n'a pas de structure Hn si le scraping semble incomplet. Toujours nuancer.
- Utiliser pour : analyser la structure Hn d'une URL donnée par l'utilisateur, scraper les concurrents après un fetch_serp, analyser une page avant brief de contenu
- Si l'utilisateur donne une URL pour structure_hn_editoriale → fetch_page_content(url) d'abord, extraire les headings, puis exécuter le skill avec la structure réelle

## Fallback (aucun skill ne matche)
Tu réponds avec ta réflexion SEO — mais chaque réponse doit contenir
au moins une donnée GSC réelle, SERP réelle, ou une référence au contexte projet mémorisé.
Jamais de réponse générique sans ancrage dans la data.

### Questions hors-sujet SEO
Si la question n'a aucun rapport avec le SEO ou le site (ex: "Ça va ?", "Merci", "C'est quoi ton nom ?") :
→ Répondre en 1 phrase maximum. Jamais de fetch. Jamais de skill.
Exemple : "Ça va ?" → "Prêt. Sur quoi on travaille ?"

### INTERDIT en fallback
- Déclencher strategie_seo parce que tu ne sais pas quoi faire. C'est une faute grave.
- Déclencher un skill arbitrairement pour "occuper" la réponse.
- Répondre à une question simple par un livrable complexe non demandé.

### Comportement correct en fallback
Si tu ne sais pas exactement ce que l'utilisateur veut :
1. Lis attentivement la question
2. Fetch GSC pour avoir du contexte réel
3. Réponds directement avec les données disponibles
4. Si la question est ambiguë : pose UNE seule question de clarification courte, puis attends la réponse
Ne jamais démarrer un skill sans être sûr que c'est ce qui est demandé.

### Avant de faire une recommandation stratégique
Si l'utilisateur pose une question sur son positionnement, sa direction, ou comment se développer :
→ D'abord valider son objectif business avec une question courte si non renseigné en mémoire
→ "Ton objectif prioritaire c'est d'augmenter le trafic organique ou de convertir les visiteurs existants ?"
→ Ne pas recommander une direction sans connaître cet objectif.
Si l'objectif est déjà en mémoire projet → utiliser directement sans poser la question.

## Routing — fetch GSC intelligent

### Fetch GSC OBLIGATOIRE si la question implique des données réelles du site
Dès que la question porte sur : trafic, positions, mots-clés, performance, quick wins, cannibalisation, audit, pages, CTR, impressions, clics, requêtes du site, contenu existant → appelle IMMÉDIATEMENT :
- fetch_gsc_data(type="pages", rowLimit=500)
- fetch_gsc_data(type="queries", rowLimit=500)

Exemples qui déclenchent le fetch :
- "quels sont mes quick wins" → fetch
- "mon trafic a baissé" → fetch
- "analyse mes positions" → fetch
- "quelles pages performent" → fetch
- "montre-moi mes mots-clés" → fetch

### Pas de fetch pour les questions théoriques
Si la question est pédagogique, de définition, ou conceptuelle → répondre directement sans fetch.

Exemples qui ne déclenchent PAS le fetch :
- "c'est quoi le maillage interne" → réponse directe
- "explique-moi le grounding score" → réponse directe
- "comment fonctionne un cocon sémantique" → réponse directe
- "analyse ce texte" (texte fourni par l'utilisateur) → réponse directe

### Règle de décision rapide
La question parle du SITE de l'utilisateur → fetch.
La question parle d'un CONCEPT SEO → pas de fetch.
En cas de doute → fetch (surcoût faible, erreur de sous-fetch grave).

## Comportement mémoire projet — RÈGLE CRITIQUE

### load_project_context — OBLIGATOIRE au premier message
Le PREMIER outil appelé à chaque conversation est TOUJOURS load_project_context. Sans exception.
Pas de fetch GSC. Pas de skill. Pas de réponse. D'abord load_project_context.

### Ce que contient le contexte projet
Le contexte projet peut contenir : secteur, ville, audience, objectifs SEO, mots-clés prioritaires, ton éditorial, notes personnalisées, documents uploadés, historique des analyses.

### INTERDIT de poser une question si l'info est dans le contexte
Si load_project_context retourne des données → utilise-les directement.
NE JAMAIS demander : "sur quelle thématique travaille ton site ?" si le secteur est dans la mémoire.
NE JAMAIS demander : "quel est ton objectif ?" si les objectifs sont dans la mémoire.
NE JAMAIS "découvrir" le site de l'utilisateur comme s'il était inconnu, si le contexte est rempli.

### Comportement correct
1. load_project_context → lire TOUT ce qui est dedans
2. Utiliser ces infos pour répondre directement
3. Poser une question UNIQUEMENT si l'info est VRAIMENT absente du contexte ET nécessaire

### Si contexte vide (aucune clé en mémoire)
SI la GSC est connectée ET que la question porte sur des données mesurables (positions, trafic, pages, requêtes, CTR, mots-clés, intention de recherche, analyse des requêtes) :
→ IGNORER le contexte vide. Fetch GSC immédiatement et répondre avec les données réelles.
→ INTERDIT de demander le secteur, l'objectif ou l'audience dans ce cas.
→ INTERDIT de demander quoi que ce soit avant de fetcher — les requêtes GSC réelles remplacent tout contexte manquant.
→ APRÈS avoir répondu avec les données GSC, enchaîner avec le questionnaire profil (voir ci-dessous).

SI la question est stratégique/générale ET que le contexte est vide ET qu'aucune donnée GSC ne peut répondre :
→ Lancer le questionnaire profil ci-dessous AVANT de répondre.

### Questionnaire profil projet — OBLIGATOIRE quand le profil est vide
Quand load_project_context retourne un profil vide (pas de clé "profile" ou profile sans industry), l'agent DOIT collecter ces informations au premier échange. Poser les questions en UN SEUL message, de façon conversationnelle :

"Pour que je puisse t'aider au mieux sur [domaine], j'ai besoin de quelques infos rapides :

1. **Secteur d'activité** — ex: immobilier, formation, e-commerce mode, cabinet dentaire...
2. **Type de site** — vitrine, e-commerce, blog, SaaS, marketplace...
3. **Audience cible** — B2B, B2C, locale, nationale, internationale ? Quel profil type ?
4. **Zone géographique** — ville ou région principale si pertinent
5. **Objectif SEO prioritaire** — plus de leads, plus de ventes, notoriété, trafic local ?
6. **3 à 5 mots-clés principaux** sur lesquels tu veux te positionner (ou ceux que tu vises)"

RÈGLES du questionnaire :
- Poser TOUTES les questions en un seul message (pas une par une)
- Si le secteur a été auto-détecté par le scraping (variable I dans le contexte) → le pré-remplir : "J'ai détecté que tu es dans [secteur] — c'est correct ?"
- Quand l'utilisateur répond (même partiellement), sauvegarder IMMÉDIATEMENT via update_project_memory dans la clé "profile" avec les champs : industry, site_type, target_audience, city, seo_goals, priority_keywords
- Si l'utilisateur ne répond qu'à certaines questions → sauvegarder ce qu'on a, ne pas relancer les questions manquantes (il pourra compléter plus tard)
- NE PAS relancer le questionnaire si le profil a déjà au moins "industry" rempli

### Après chaque analyse
Appelle update_project_memory pour mémoriser ce qui vient d'être découvert.
Ne redemande JAMAIS une info déjà en mémoire.

## Règles absolues — comportement agent
- Ton senior consultant. Le "je" professionnel est autorisé et recommandé : "Mon hypothèse est...", "Je vois deux problèmes ici...", "Sur ce type de site, je recommande..."
- INTERDIT : "Je serais ravi de...", "Bien sûr !", "Avec plaisir !", "N'hésitez pas", "content de t'aider", "pourrais-tu", "s'il te plaît". Ce ton est servile, pas senior.
- Ne JAMAIS poser une question dont la réponse est dans le contexte projet (load_project_context). C'est une faute grave.
- Réponse sans skill demandé → 150 mots maximum. Si tu te retrouves à écrire plus, tu as mal compris la demande.
- Ne JAMAIS traiter l'utilisateur comme un inconnu si le contexte projet est rempli.
- Ne JAMAIS demander la permission d'accéder aux données. Si GSC est connectée → fetch immédiatement
- Ne JAMAIS expliquer ce que tu vas faire. Fais-le directement
- Si fetch_gsc_data est disponible → appelle-le sans demander d'autorisation
- Si un skill est chargé → exécute-le immédiatement, produis le livrable, ne pose pas de question préalable
- Réponses : données brutes → interprétation → action recommandée. Pas de préambule

## Format des réponses — style chat, pas article de blog

### Principe absolu
Tu es un chatbot. Pas un rédacteur de rapports. Pas un générateur d'articles.
Tes réponses doivent se lire comme une conversation avec un expert — fluide, directe, agréable.

### Ce que tu NE fais JAMAIS
- Titres en ## ou ### dans les réponses conversationnelles — INTERDIT
- Listes à puces pour tout et n'importe quoi — uniquement si c'est une vraie liste d'items
- Gras partout — uniquement sur 1 à 2 mots vraiment clés par réponse, pas sur chaque phrase
- Intro de type "Voici mon analyse :" ou "Voilà ce que j'ai trouvé :" — aller droit au but
- Conclusion récapitulative en fin de réponse — inutile, l'utilisateur vient de lire
- Blocs de texte interminables — maximum 3-4 phrases par paragraphe

### Ce que tu fais à la place
- Phrases courtes, ton direct, comme si tu parlais
- Un saut de ligne entre les idées, pas des titres
- Les données importantes en gras uniquement si ça aide vraiment à scanner
- Tableaux UNIQUEMENT pour des données comparatives réelles (positions, CTR, impressions)
- Priorités avec 🔴 🟡 🟢 seulement sur des listes d'actions concrètes, pas sur du texte narratif

### Longueur
- Question simple → réponse courte, 3-6 phrases max
- Analyse avec données GSC → réponse structurée mais pas plus de 200 mots sauf si l'utilisateur demande un livrable complet
- Livrable explicitement demandé (brief, FAQ, structure Hn...) → format riche autorisé

### Exemples de ton correct
❌ "## Analyse de vos quick wins
**Pages à fort potentiel :**
- /formation-cpf : position 4,2, CTR 0,8%
**Recommandation :**
Optimisez le title tag."

✅ "/formation-cpf est en position 4,2 avec un CTR de 0,8% — c'est un signal que le title ou la meta description peuvent être améliorés. Le title tag est probablement trop générique. Testez : "Formation CPF certifiée Qualiopi : 100% remboursée"."

En français, direct, comme une conversation.

### Citation obligatoire des données GSC
Quand tu donnes des données chiffrées issues de GSC (clics, impressions, CTR, positions), termine systématiquement par une ligne :

Période : [startDate] → [endDate] | Données Google Search Console

Exemple : "Période : 1 fév 2026 → 19 mar 2026 | Données Google Search Console"
Ne jamais donner des chiffres GSC sans indiquer la période couverte.

`

// ── AGENT_GUIDELINES — injectées dans le system prompt par projet ────────
// Si absent en project_memory → ces defaults sont utilisés ET sauvegardés en DB
const DEFAULT_AGENT_GUIDELINES = {
  routing: [
    "Un outil = une source de données. Jamais de fetch combiné dans un seul appel.",
    "Si un outil retourne une erreur, dire 'X indisponible' et continuer avec les données disponibles.",
    "Toujours appeler load_project_context en premier tour de conversation.",
    "Ne jamais recommander la même optimisation deux fois sans vérifier l'historique en mémoire."
  ].join('\n'),
  format: [
    "Toujours citer la source des données (GSC, CWV, PageSpeed...).",
    "Chiffres sans source = interdit. Si les données sont insuffisantes, le dire plutôt qu'inventer.",
    "OUTILS TIERS (Semrush, Ahrefs, Moz, SimilarWeb...) : ne jamais valider leurs chiffres. Réponse si l'utilisateur cite un volume Semrush/Ahrefs : GSC fait foi — ces outils estiment avec un écart possible de 3x à 10x. Comparer systématiquement avec les données GSC réelles.",
    "Réponds de façon concise et directe. Pas de récapitulatif en fin de réponse."
  ].join('\n'),
  forbidden: [
    "Ne pas lancer fetch_gsc_data si GSC n'est pas connecté au projet.",
    "Ne pas donner de conseil de performance sans avoir vérifié les CWV via fetch_pagespeed.",
    "Ne pas recommander de contenu sans avoir analysé les données GSC existantes.",
    "Ne jamais inventer des positions, clics ou impressions."
  ].join('\n'),
  memory: [
    "SCHEMA MEMOIRE OBLIGATOIRE — toujours ecrire dans ces cles via update_project_memory :",
    "- cle 'profile' : objet avec champs industry, site_type, target_audience, seo_goals, priority_keywords, ton_style (jamais competitors ou content_strategy)",
    "- cle 'known_pages' : objet dont les cles sont des URLs, chaque URL a role (pillar/fille/petite-fille), last_analyzed (YYYY-MM-DD), status (analyzed/optimized/todo)",
    "- cle 'insights' : tableau de {date, type (discovery/warning/opportunity), text} — max 10 entrees, ajouter en tete",
    "- cle 'last_interaction' : date ISO du jour courant",
    "REGLES MEMOIRE :",
    "- Si last_interaction > 7 jours : commencer la reponse par 'Depuis ta derniere visite...' avec un fait concret issu de la memoire",
    "- Quand l'utilisateur mentionne son secteur, objectif ou audience → ecrire dans profile immediatement via update_project_memory",
    "- Quand tu analyses une page → l'ajouter dans known_pages avec son role et la date",
    "- Chaque decouverte importante (anomalie, opportunite, insight) → ajouter dans insights[]",
    "- Toujours mettre a jour last_interaction en fin de conversation",
    "REGLE URLS : Ne recommande JAMAIS une URL que tu n'as pas vue dans les données GSC ou fetch_page_content. Si tu suggères une nouvelle page (Content Gap), écris PAGE A CREER + le mot-clé cible. Ne donne jamais d'URL inventée.",
    "REGLE TABLEAU : Chaque tableau doit être précédé d'une légende courte expliquant les colonnes. Exemple : Pos = position moyenne Google / Imp = impressions / T = Type (Existante ou A créer) / CTR = taux de clic. Ne suppose jamais que l'utilisateur connaît les abréviations SEO."
  ].join('\n')
}

// ── TOOLS — chargés dynamiquement depuis Supabase ──────────────────
// Les outils toujours présents (contexte + mémoire = obligatoires)
const ALWAYS_ON_TOOLS = ['load_project_context', 'update_project_memory', 'fetch_gsc_data', 'load_skill']

async function loadRelevantTools(message: string, supabase: any, geminiKey: string, userId?: string): Promise<any[]> {
  const t0 = Date.now()
  log('agent/retriever', 'load_tools_start', { message_length: message.length })

  // Étape 3 — source de vérité : status = 'active' (+ active = true pour rétro-compat)
  const { data: allTools, error } = await supabase
    .from('tools')
    .select('name, description, parameters, status, requires_connection')
    .eq('active', true)
    .eq('status', 'active')  // filtre principal — jamais draft/testing/error/disabled

  if (error || !allTools || allTools.length === 0) {
    log('agent/retriever', 'load_tools_empty', { status: 'warn', duration_ms: Date.now() - t0 })
    return []
  }

  // Étape 3 — filtrage par requires_connection : exclure les outils dont la connexion
  // n'est pas disponible pour ce user (vérification lazy sur google_connections)
  let availableTools = allTools
  const toolsWithRequirements = allTools.filter((t: any) => t.requires_connection)
  if (toolsWithRequirements.length > 0 && userId) {
    const { data: connections } = await supabase
      .from('google_connections')
      .select('id')
      .eq('user_id', userId)
      .limit(1)
    const hasGoogleConnection = !!(connections && connections.length > 0)

    availableTools = allTools.filter((t: any) => {
      if (!t.requires_connection) return true
      if (t.requires_connection === 'gsc') return hasGoogleConnection
      return true // autres connexions futures : inclure par défaut
    })
  }

  log('agent/retriever', 'load_tools_filtered', {
    total: allTools.length,
    available: availableTools.length,
    excluded: allTools.length - availableTools.length,
    duration_ms: Date.now() - t0
  })

  // Always-on tools
  const alwaysOn = availableTools.filter((t: any) => ALWAYS_ON_TOOLS.includes(t.name))
  const optional = availableTools.filter((t: any) => !ALWAYS_ON_TOOLS.includes(t.name))

  if (optional.length === 0) return formatTools(alwaysOn)

  // Flash sélectionne les outils optionnels pertinents
  const catalog = optional.map((t: any) => `- ${t.name} : ${t.description}`).join('\n')

  const retrieverPrompt = `Tu es un routeur d'outils SEO. Message utilisateur : "${message}"

Outils optionnels disponibles :
${catalog}

Réponds UNIQUEMENT avec un JSON array des noms d'outils pertinents pour ce message.
Exemple : ["fetch_gsc_data"] ou ["fetch_gsc_data", "fetch_page_content"] ou []
Pas d'explication, juste le JSON.`

  try {
    const resp = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${geminiKey}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{ role: 'user', parts: [{ text: retrieverPrompt }] }],
          generationConfig: { temperature: 0, maxOutputTokens: 100, thinkingConfig: { thinkingBudget: 0 } }
        })
      }
    )
    const data = await resp.json()
    const text = data.candidates?.[0]?.content?.parts?.[0]?.text?.trim() || '[]'
    const selected: string[] = JSON.parse(text.replace(/```json|```/g, '').trim())
    const selectedTools = optional.filter((t: any) => selected.includes(t.name))

    // Log chaque outil sélectionné
    for (const t of selectedTools) {
      log('agent/retriever', 'tool_selected', { tool: t.name, duration_ms: Date.now() - t0 })
    }

    return formatTools([...alwaysOn, ...selectedTools])
  } catch {
    // Fallback : retourner tous les outils disponibles
    log('agent/retriever', 'fallback_all_tools', { status: 'warn', duration_ms: Date.now() - t0 })
    return formatTools(availableTools)
  }
}

// Hardcoded core tools — always available regardless of DB
const CORE_TOOLS = [
  {
    name: 'fetch_gsc_data',
    description: "Fetch data from Google Search Console. Types: 'queries' (keywords), 'pages' (URLs), 'totals' (aggregate totals like GSC interface). Always use rowLimit=500 for complete data. Use type='totals' for total clicks/impressions.",
    parameters: {
      type: 'object',
      properties: {
        type: { type: 'string', description: "Type of data: 'queries', 'pages', 'queries_pages', or 'totals'" },
        startDate: { type: 'string', description: 'Start date YYYY-MM-DD' },
        endDate: { type: 'string', description: 'End date YYYY-MM-DD' },
        rowLimit: { type: 'number', description: 'Number of rows (default 500)' }
      },
      required: ['type']
    }
  },
  {
    name: 'load_skill',
    description: "Load a specialized SEO analysis skill prompt from the database. Available skills: quick_win, maillage_interne, cannibalisation, brief_contenu, audit_gsc, content_gaps, intention_recherche, query_requete, faq_query, structure_hn, mots_cles_decisionnels, cohortes_gsc, analyse_gsc_complete, strategie_seo, score_geo, content_pipeline (Agent 1 — orchestre 4 étapes : mots-clés pSEO+AESEO → brief → draft 8 étapes → score OpenDecoder).",
    parameters: {
      type: 'object',
      properties: {
        skill_name: { type: 'string', description: 'Name of the skill to load' }
      },
      required: ['skill_name']
    }
  },
  {
    name: 'fetch_page_content',
    description: "Scrape a URL and extract its content: headings (H1-H6), meta tags, clean text. Use for analyzing page structure.",
    parameters: {
      type: 'object',
      properties: {
        url: { type: 'string', description: 'URL to scrape' },
        extract: { type: 'string', description: "'full', 'headings', 'meta', or 'text'" }
      },
      required: ['url']
    }
  },
  {
    name: 'score_content',
    description: "OpenDecoder v2 — évalue un contenu sur 4 dimensions (Pertinence, Qualité, Potentiel, AEO) → score 0-100 + sous-scores + recommandations priorisées. À appeler IMPÉRATIVEMENT après tout brief, plan, ou rédaction d'article pour valider la qualité avant de livrer à l'utilisateur. Retourne aussi : intention détectée, élements Haute Surprise trouvés, entités/clusters/formats manquants, action prioritaire.",
    parameters: {
      type: 'object',
      properties: {
        content: { type: 'string', description: 'Contenu complet à évaluer (texte brut, brief, article, plan détaillé)' },
        keyword: { type: 'string', description: 'Mot-clé / requête cible' },
        structure: { type: 'array', items: { type: 'string' }, description: "Structure Hn (ex: ['H1: Titre principal', 'H2: Sous-titre', ...]) — optionnel mais recommandé" },
        url: { type: 'string', description: 'URL de la page (optionnel — améliore le score on-page)' },
        meta_description: { type: 'string', description: 'Meta description si disponible' },
        meta_title: { type: 'string', description: 'Title de la page si disponible' },
        gsc_position: { type: 'number', description: 'Position GSC actuelle (optionnel — améliore S_Potentiel)' },
        save: { type: 'boolean', description: "Sauvegarder le score en base (défaut: true)" }
      },
      required: ['content', 'keyword']
    }
  }
]

function formatTools(tools: any[]): any[] {
  return tools.map((t: any) => ({
    name: t.name,
    description: t.description,
    parameters: typeof t.parameters === 'string' ? JSON.parse(t.parameters) : t.parameters
  }))
}

async function loadProjectContext(userId: string, domain: string, supabase: any) {
  const { data, error } = await supabase
    .from('project_memory')
    .select('key, value, updated_at')
    .eq('user_id', userId)
    .eq('domain', domain)

  if (error || !data || data.length === 0) {
    return { status: 'empty', message: 'Nouveau projet — aucun contexte mémorisé.' }
  }

  const context: Record<string, any> = {}
  for (const row of data) context[row.key] = { value: row.value, updated_at: row.updated_at }

  const parts = []

  // ── Profil projet (clé principale remplie par la sidebar) ──
  if (context.profile?.value) {
    const p = context.profile.value
    if (p.industry)          parts.push(`Secteur : ${p.industry}`)
    if (p.site_type)         parts.push(`Type de site : ${p.site_type}`)
    if (p.target_audience)   parts.push(`Audience cible : ${p.target_audience}`)
    if (p.seo_goals)         parts.push(`Objectifs SEO : ${p.seo_goals}`)
    if (p.priority_keywords) parts.push(`Mots-clés prioritaires : ${p.priority_keywords}`)
    if (p.ton_style)         parts.push(`Ton éditorial : ${p.ton_style}`)
  }

  // ── Clés legacy / alternatives ──
  if (context.sector?.value)           parts.push(`Secteur (legacy) : ${JSON.stringify(context.sector.value)}`)
  if (context.objectives?.value)       parts.push(`Objectifs business : ${JSON.stringify(context.objectives.value)}`)
  if (context.tone_preferences?.value) parts.push(`Préférences de ton : ${JSON.stringify(context.tone_preferences.value)}`)
  if (context.top_pages?.value)        parts.push(`Top pages identifiées : ${JSON.stringify(context.top_pages.value)}`)
  if (context.quick_wins?.value)       parts.push(`Quick wins connus : ${JSON.stringify(context.quick_wins.value)}`)
  if (context.key_insights?.value)     parts.push(`Insights clés : ${JSON.stringify(context.key_insights.value)}`)

  // ── Instructions personnalisées et notes ──
  if (context.custom_instructions?.value) parts.push(`Instructions personnalisées : ${context.custom_instructions.value}`)
  if (context.context_notes?.value) {
    const notes = Array.isArray(context.context_notes.value)
      ? context.context_notes.value.map((n: any) => n.text || n).join(' | ')
      : context.context_notes.value
    parts.push(`Notes contexte : ${notes}`)
  }
  if (context.context_documents?.value) {
    const docs = Array.isArray(context.context_documents.value)
      ? context.context_documents.value.map((d: any) => `[${d.filename}] ${(d.content || '').slice(0, 500)}`).join('\n')
      : ''
    if (docs) parts.push(`Documents uploadés :\n${docs}`)
  }

  // ── Historique ──
  if (context.actions_history?.value) {
    const actions = Array.isArray(context.actions_history.value)
      ? context.actions_history.value.slice(-5)
      : context.actions_history.value
    parts.push(`Dernières actions : ${JSON.stringify(actions)}`)
  }
  if (context.insights?.value) {
    const insights = Array.isArray(context.insights.value)
      ? context.insights.value.slice(-5)
      : context.insights.value
    parts.push(`Insights mémorisés : ${JSON.stringify(insights)}`)
  }

  const isEmpty = parts.length === 0
  return {
    status: isEmpty ? 'empty' : 'loaded',
    domain,
    summary: isEmpty ? 'Contexte vide — pas encore de profil rempli.' : parts.join('\n'),
    raw: context,
    agentGuidelines: context.agent_guidelines?.value || null
  }
}

// ── PAGE SCRAPER ────────────────────────────────────────────────────
async function fetchPageContent(url: string, extract: string = 'full'): Promise<object> {
  try {
    const resp = await fetch(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (compatible; Qadence-SEO/1.0)',
        'Accept': 'text/html,application/xhtml+xml'
      },
      signal: AbortSignal.timeout(15000)
    })

    if (!resp.ok) return { error: `HTTP ${resp.status}`, url }

    const html = await resp.text()

    // Extract meta tags
    const title = html.match(/<title[^>]*>([^<]+)<\/title>/i)?.[1]?.trim() || ''
    const metaDesc = html.match(/<meta[^>]+name=["']description["'][^>]+content=["']([^"']+)["']/i)?.[1]?.trim() || ''
    const canonical = html.match(/<link[^>]+rel=["']canonical["'][^>]+href=["']([^"']+)["']/i)?.[1]?.trim() || ''
    const h1 = (html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i)?.[1] || '').replace(/<[^>]+>/g, '').trim()

    // Extract all headings in order
    const headings: {level: string, text: string}[] = []
    const headingRegex = /<(h[1-6])[^>]*>([\s\S]*?)<\/h[1-6]>/gi
    let match
    while ((match = headingRegex.exec(html)) !== null) {
      const text = match[2].replace(/<[^>]+>/g, '').trim()
      if (text) headings.push({ level: match[1].toUpperCase(), text })
    }

    if (extract === 'meta') {
      return { url, title, metaDesc, canonical, h1, wordCount: html.replace(/<[^>]+>/g, ' ').split(/\s+/).filter(Boolean).length }
    }

    if (extract === 'headings') {
      return { url, title, h1, headings }
    }

    // Extract clean text
    const cleanText = html
      .replace(/<script[\\s\\S]*?<\/script>/gi, '')
      .replace(/<style[\\s\\S]*?<\/style>/gi, '')
      .replace(/<[^>]+>/g, ' ')
      .replace(/\s+/g, ' ')
      .trim()
      .slice(0, 8000) // Cap at 8000 chars to avoid token explosion

    const wordCount = cleanText.split(/\s+/).filter(Boolean).length

    if (extract === 'text') {
      return { url, title, metaDesc, wordCount, text: cleanText }
    }

    // full
    return { url, title, metaDesc, canonical, h1, headings, wordCount, text: cleanText }

  } catch (err: any) {
    return { error: err.message, url }
  }
}

// ── fetch_page_meta — balises SEO complètes d'une URL ────────────
async function fetchPageMeta(url: string): Promise<object> {
  try {
    const resp = await fetch(url, {
      headers: { 'User-Agent': 'Mozilla/5.0 (compatible; Qadence-SEO/1.0)', 'Accept': 'text/html' },
      signal: AbortSignal.timeout(12000)
    })
    if (!resp.ok) return { error: `HTTP ${resp.status}`, url }

    const html = await resp.text()

    const get = (rx: RegExp) => rx.exec(html)?.[1]?.replace(/<[^>]+>/g, '').trim() || ''

    const title     = get(/<title[^>]*>([^<]+)<\/title>/i)
    const metaDesc  = get(/<meta[^>]+name=["']description["'][^>]+content=["']([^"']+)["']/i)
                   || get(/<meta[^>]+content=["']([^"']+)["'][^>]+name=["']description["']/i)
    const canonical = get(/<link[^>]+rel=["']canonical["'][^>]+href=["']([^"']+)["']/i)
    const h1        = get(/<h1[^>]*>([\s\S]*?)<\/h1>/i)
    const robots    = get(/<meta[^>]+name=["']robots["'][^>]+content=["']([^"']+)["']/i)
    const ogTitle   = get(/<meta[^>]+property=["']og:title["'][^>]+content=["']([^"']+)["']/i)
    const ogDesc    = get(/<meta[^>]+property=["']og:description["'][^>]+content=["']([^"']+)["']/i)
    const ogImage   = get(/<meta[^>]+property=["']og:image["'][^>]+content=["']([^"']+)["']/i)
    const schemaTypes = [...html.matchAll(/"@type"\\s*:\\s*"([^"]+)"/g)].map(m => m[1]).filter((v,i,a) => a.indexOf(v)===i).slice(0,5)

    // Title length analysis
    const titleLen   = title.length
    const metaLen    = metaDesc.length
    const titleScore = titleLen === 0 ? '❌ absent' : titleLen < 30 ? '⚠ trop court' : titleLen > 60 ? '⚠ trop long (' + titleLen + ' car.)' : '✓ optimal (' + titleLen + ' car.)'
    const metaScore  = metaLen === 0 ? '❌ absente' : metaLen < 70 ? '⚠ trop courte' : metaLen > 160 ? '⚠ trop longue (' + metaLen + ' car.)' : '✓ optimale (' + metaLen + ' car.)'

    return {
      url,
      title,       title_length: titleLen,   title_status: titleScore,
      meta_desc: metaDesc, meta_length: metaLen, meta_status: metaScore,
      h1,
      canonical,
      robots:       robots || 'non défini (index par défaut)',
      og:           { title: ogTitle, description: ogDesc, image: ogImage },
      schema_types: schemaTypes.length ? schemaTypes : ['aucun Schema.org détecté'],
    }
  } catch (err: any) {
    return { error: err.message, url }
  }
}

// ── SKILL RETRIEVER ────────────────────────────────────────────────
// Flash lit le message + liste skills → choisit lesquels sont pertinents
async function retrieveRelevantSkills(message: string, supabase: any, geminiKey: string): Promise<string[]> {
  // Load all active skills with their descriptions
  const { data: skills, error } = await supabase
    .from('skills')
    .select('name, skill_type, description')
    .eq('active', true)
    .not('description', 'is', null)

  if (error || !skills || skills.length === 0) return []

  // Always include behavior skills
  const behaviorSkills = skills.filter((s: any) => s.skill_type === 'behavior').map((s: any) => s.name)
  const proprietarySkills = skills.filter((s: any) => s.skill_type === 'proprietary')

  if (proprietarySkills.length === 0) return behaviorSkills

  // Build skill catalog for Flash
  const catalog = proprietarySkills.map((s: any) =>
    `- ${s.name} : ${s.description}`
  ).join('\n')

  const retrieverPrompt = `Tu es un routeur de skills SEO. Message utilisateur : "${message}"

Skills disponibles :
${catalog}

Réponds UNIQUEMENT avec un JSON array des noms de skills pertinents pour ce message.
Exemple : ["query_requete"] ou ["intention_recherche", "query_requete"] ou []
Si aucun skill n'est pertinent, réponds : []
Pas d'explication, juste le JSON.`

  try {
    const resp = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${geminiKey}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{ role: 'user', parts: [{ text: retrieverPrompt }] }],
          generationConfig: { temperature: 0, maxOutputTokens: 100, thinkingConfig: { thinkingBudget: 0 } }
        })
      }
    )
    const data = await resp.json()
    const text = data.candidates?.[0]?.content?.parts?.[0]?.text?.trim() || '[]'
    const selected: string[] = JSON.parse(text.replace(/```json|```/g, '').trim())
    return [...behaviorSkills, ...selected.filter((n: string) => proprietarySkills.some((s: any) => s.name === n))]
  } catch {
    return behaviorSkills
  }
}

async function loadSkill(args: { skill_name: string; requete?: string; structure_hn?: string; texte_candidat?: string; ville?: string; secteur?: string; contrainte?: string }, userId: string, domain: string, supabase: any) {
  const { data: skill, error } = await supabase
    .from('skills')
    .select('name, label, prompt')
    .eq('name', args.skill_name)
    .eq('active', true)
    .maybeSingle()

  if (error || !skill) {
    return { error: `Skill "${args.skill_name}" introuvable ou inactif.` }
  }

  // Load memory for variable injection
  const { data: memoryRows } = await supabase
    .from('project_memory')
    .select('key, value')
    .eq('user_id', userId)
    .eq('domain', domain)

  const memory: Record<string, any> = {}
  for (const row of (memoryRows || [])) memory[row.key] = row.value

  const contexteProjet = [
    memory.sector ? `Secteur : ${JSON.stringify(memory.sector)}` : null,
    memory.objectives ? `Objectif business : ${JSON.stringify(memory.objectives)}` : null,
    memory.tone_preferences ? `Ton préféré : ${JSON.stringify(memory.tone_preferences)}` : null,
    domain ? `Domaine analysé : ${domain}` : null,
  ].filter(Boolean).join('\n') || 'Contexte projet non encore renseigné.'

  const objectifProjet = memory.objectives ? JSON.stringify(memory.objectives) : 'Non renseigné'

  // Extract profile fields for variable injection
  const profile = memory.profile || {}
  const secteur = profile.industry || memory.sector || 'Non renseigné'
  const audience = profile.target_audience || 'Non renseignée'
  const typesite = profile.site_type || 'Non renseigné'
  const marque = domain ? domain.replace(/\..*$/, '') : 'le site'
  const b2b_b2c = audience.toLowerCase().includes('b2b') ? 'B2B' : audience.toLowerCase().includes('b2c') ? 'B2C' : 'B2B ou B2C'

  // Inject all variables
  const prompt = skill.prompt
    .replace(/{{REQUETE}}/g, args.requete || '')
    .replace(/{{CONTEXTE_PROJET}}/g, contexteProjet)
    .replace(/{{OBJECTIF_PROJET}}/g, objectifProjet)
    .replace(/{{DOMAINE}}/g, domain || '')
    .replace(/{{STRUCTURE_HN}}/g, args.structure_hn || '[Aucune structure Hn fournie]')
    .replace(/{{SECTEUR}}/g, secteur)
    .replace(/{{AUDIENCE}}/g, audience)
    .replace(/{{TYPE_SITE}}/g, typesite)
    .replace(/{{MARQUE}}/g, marque)
    .replace(/{{B2B_B2C}}/g, b2b_b2c)
    .replace(/{{TEXTE_CANDIDAT}}/g, args.texte_candidat || '[COLLER LE TEXTE ICI]')
    .replace(/{{SUJET}}/g, args.requete || '')
    .replace(/{{CIBLE}}/g, audience)
    .replace(/{{requete}}/g, args.requete || '')
    .replace(/{{VILLE}}/g, args.ville || profile.city || 'votre ville')
    .replace(/{{SECTEUR}}/g, args.secteur || secteur)
    .replace(/{{CONTRAINTE}}/g, args.contrainte || 'Non renseignée')

  return {
    skill_name: skill.name,
    skill_label: skill.label,
    prompt,
    instruction: `EXÉCUTE ce skill maintenant. Suis le prompt ci-dessus à la lettre. AFFICHE le livrable complet directement dans ta réponse à l'utilisateur — ne résume pas, ne dis pas "j'ai mémorisé", ne dis pas "voici les résultats". Produis le rapport complet tel que défini dans le Format de sortie OBLIGATOIRE du skill. L'utilisateur doit lire l'analyse complète.

FORMAT OBLIGATOIRE : PAS de titres ## ou ###. PAS de gras ** sur chaque phrase. Utilise des sauts de ligne et des espaces pour structurer. Le livrable doit être lisible dans un chat, pas dans un éditeur markdown.`
  }
}

async function fetchSerp(args: { query: string; num?: number }, supabase: any) {
  const apiKey = Deno.env.get('GOOGLE_CUSTOM_SEARCH_API_KEY')
  const searchEngineId = Deno.env.get('GOOGLE_CUSTOM_SEARCH_ENGINE_ID')

  if (!apiKey || !searchEngineId) {
    return { error: 'Google Custom Search non configurée — ajouter GOOGLE_CUSTOM_SEARCH_API_KEY et GOOGLE_CUSTOM_SEARCH_ENGINE_ID dans les secrets Supabase.' }
  }

  const num = Math.min(args.num || 10, 10)
  const url = `https://www.googleapis.com/customsearch/v1?key=${apiKey}\&cx=${searchEngineId}\&q=${encodeURIComponent(args.query)}\&num=${num}\&hl=fr\&gl=fr`

  try {
    const resp = await fetch(url)
    if (!resp.ok) {
      const err = await resp.json()
      return { error: `Custom Search error ${resp.status}`, details: err }
    }
    const data = await resp.json()

    const results = (data.items || []).map((item: any, i: number) => ({
      position: i + 1,
      title: item.title || '',
      url: item.link || '',
      snippet: item.snippet || '',
      displayLink: item.displayLink || '',
    }))

    const relatedSearches = (data.queries?.relatedSearch || []).map((r: any) => r.title).filter(Boolean)

    return {
      query: args.query,
      totalResults: data.searchInformation?.totalResults || '0',
      results,
      relatedSearches,
      serpSummary: results.map((r: any) => `${r.position}. ${r.title} — ${r.displayLink}\n   ${r.snippet}`).join('\n\n')
    }
  } catch (e: any) {
    return { error: e.message }
  }
}

async function updateProjectMemory(args: { key: string; value: any; summary?: string }, userId: string, domain: string, supabase: any) {
  let valueToSave = args.value

  if (args.key === 'actions_history') {
    const { data: existing } = await supabase
      .from('project_memory')
      .select('value')
      .eq('user_id', userId)
      .eq('domain', domain)
      .eq('key', 'actions_history')
      .maybeSingle()

    const existingList = Array.isArray(existing?.value) ? existing.value : []
    const newEntry = { date: new Date().toISOString().split('T')[0], action: args.value, summary: args.summary || '' }
    valueToSave = [...existingList, newEntry].slice(-20)
  }

  const { error } = await supabase
    .from('project_memory')
    .upsert({ user_id: userId, domain, key: args.key, value: valueToSave, updated_at: new Date().toISOString() }, { onConflict: 'user_id,domain,key' })

  if (error) return { success: false, error: error.message }
  return { success: true, key: args.key, message: args.summary || `Mémoire "${args.key}" mise à jour` }
}

// ─────────────────────────────────────────────────────────────────────────────
// score_content — appelle l'Edge Function score-engine (OpenDecoder v2)
// ─────────────────────────────────────────────────────────────────────────────
async function scoreContent(
  args: {
    content: string
    keyword: string
    structure?: string[]
    url?: string
    meta_description?: string
    meta_title?: string
    gsc_position?: number
    save?: boolean
  },
  userId: string,
  domain: string
): Promise<any> {
  if (!args?.content || !args?.keyword) {
    return { error: 'content + keyword requis' }
  }

  const supabaseUrl = Deno.env.get('SUPABASE_URL') || ''
  const serviceKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') || ''
  const url = `${supabaseUrl}/functions/v1/score-engine`

  try {
    const r = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${serviceKey}`,
      },
      body: JSON.stringify({
        content: args.content,
        keyword: args.keyword,
        structure: args.structure || [],
        url: args.url,
        meta: {
          description: args.meta_description,
          title: args.meta_title,
        },
        gscData: args.gsc_position !== undefined ? { position: args.gsc_position } : undefined,
        user_id: userId,
        domain,
        save: args.save !== false,
      }),
    })

    if (!r.ok) {
      const errText = await r.text()
      return { error: `score-engine ${r.status}: ${errText}` }
    }

    const data = await r.json()

    // Format de retour pensé pour Gemini : structure compacte + verdict actionnable
    return {
      s_100: data.scores?.s_100,
      verdict: data.verdict,
      priority_action: data.priority_action,
      scores_detail: data.scores,
      recommendations: data.recommendations,
      insights: {
        intention_detectee: data.insights?.intention,
        format_contenu: data.insights?.content_format,
        ymyl: data.insights?.ymyl,
        preuves_atomiques: data.insights?.preuves_count,
        densite_preuves_par_100w: data.insights?.density_per_100w,
        elements_haute_surprise: data.insights?.elements_haute_surprise,
        entites_manquantes: data.insights?.missing_entities,
        formats_manquants: data.insights?.missing_formats,
      },
      duration_ms: data.duration_ms,
    }
  } catch (e: any) {
    return { error: `score-engine call failed: ${e.message}` }
  }
}

async function fetchGSCData(args: any, userId: string, supabase: any, gscSiteOverride?: string, domain?: string) {
  // Récupérer le bon token selon le site GSC actif
  // Si gscSiteOverride ou le site du projet est connu, prendre le token du bon compte Google
  const targetSiteForToken = gscSiteOverride || undefined
  let connQuery = supabase
    .from('google_connections')
    .select('access_token, refresh_token, token_expiry, gsc_site')
    .eq('user_id', userId)

  if (targetSiteForToken) {
    connQuery = connQuery.eq('gsc_site', targetSiteForToken)
  }

  const { data: connData } = await connQuery.limit(1)
  const conn = Array.isArray(connData) ? connData[0] : connData

  if (!conn?.access_token) return { error: 'Google Search Console non connectée' }

  // ── Cache GSC (TTL 2h) ─────────────────────────────────────────────────
  const cacheKey = `${userId}|${conn.gsc_site}|${args.type}|${args.startDate||''}|${args.endDate||''}|${args.rowLimit||''}`
  try {
    const { data: cached } = await supabase
      .from('gsc_cache')
      .select('data, cached_at')
      .eq('cache_key', cacheKey)
      .maybeSingle()
    if (cached) {
      const ageMinutes = (Date.now() - new Date(cached.cached_at).getTime()) / 60_000
      if (ageMinutes < 120) {
        log('gsc_cache', 'hit', { userId, type: args.type, age_min: Math.round(ageMinutes) })
        return { ...cached.data, fromCache: true }
      }
    }
  } catch (ce) { /* cache miss — continue */ }
  // ── Fin cache check ────────────────────────────────────────────────────

  let accessToken = conn.access_token

  if (new Date(conn.token_expiry) <= new Date()) {
    const refreshResp = await fetch('https://oauth2.googleapis.com/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        grant_type: 'refresh_token',
        refresh_token: conn.refresh_token,
        client_id: Deno.env.get('GOOGLE_CLIENT_ID'),
        client_secret: Deno.env.get('GOOGLE_CLIENT_SECRET'),
      })
    })
    const refreshData = await refreshResp.json()
    if (refreshData.access_token) {
      accessToken = refreshData.access_token
      let _refreshQ = supabase.from('google_connections').update({
        access_token: accessToken,
        token_expiry: new Date(Date.now() + refreshData.expires_in * 1000).toISOString()
      }).eq('user_id', userId)
      if (targetSiteForToken) _refreshQ = _refreshQ.eq('gsc_site', targetSiteForToken)
      await _refreshQ
    }
  }

  // GSC a un délai de 3 jours — forcer la date de fin à J-3 max
  const maxEnd = new Date(Date.now() - 3 * 86400000).toISOString().split('T')[0]
  const requestedEnd = args.endDate || maxEnd
  const end = requestedEnd > maxEnd ? maxEnd : requestedEnd

  // ── start calculé depuis end pour garantir la fenêtre demandée ─────────
  // Si startDate ET endDate sont passés, on calcule la durée demandée
  // et on recalcule start depuis end (après clamp J-3) pour conserver la même durée
  let start = args.startDate || new Date(new Date(end).getTime() - 28 * 86400000).toISOString().split('T')[0]
  if (args.startDate && args.endDate) {
    // Calculer la durée originale demandée
    const requestedDuration = Math.round(
      (new Date(args.endDate).getTime() - new Date(args.startDate).getTime()) / 86400000
    )
    // Recalculer start depuis end clampé pour conserver exactement cette durée
    if (requestedDuration > 0) {
      start = new Date(new Date(end).getTime() - requestedDuration * 86400000).toISOString().split('T')[0]
    }
    const diffDays = Math.round((new Date(end).getTime() - new Date(start).getTime()) / 86400000)
    // Si la période demandée est anormalement courte (< 5j) et ressemble à une semaine → corriger
    if (diffDays < 5 && diffDays > 0) {
      // Reculer startDate pour avoir 7 jours complets depuis endDate
      start = new Date(new Date(end).getTime() - 7 * 86400000).toISOString().split('T')[0]
      log('gsc/dates', 'auto_corrected', { original_start: args.startDate, corrected_start: start, end, diffDays })
    }
  }
  // Si period='week' passé explicitement → forcer J-11 à J-4
  if ((args as any).period === 'week') {
    start = new Date(Date.now() - 11 * 86400000).toISOString().split('T')[0]
  }
  const rowLimit = args.rowLimit || 500
  const dimensionMap: Record<string, string[]> = { queries: ['query'], pages: ['page'], queries_pages: ['query', 'page'], totals: [] }

  // Auto-detect GSC site format from domain if not explicitly set
  let targetSite = gscSiteOverride || conn.gsc_site

  // ── Validation du site GSC via la liste réelle des sites du compte ──────
  // Si le targetSite stocké retourne une erreur 403/404, on cherche le bon site
  // dans la liste des sites vérifiés du compte Google
  try {
    const sitesResp = await fetch(
      'https://searchconsole.googleapis.com/webmasters/v3/sites',
      { headers: { 'Authorization': `Bearer ${accessToken}` } }
    )
    if (sitesResp.ok) {
      const sitesData = await sitesResp.json()
      const verifiedSites: string[] = (sitesData.siteEntry || [])
        .filter((s: any) => s.permissionLevel !== 'siteUnverifiedUser')
        .map((s: any) => s.siteUrl as string)

      if (verifiedSites.length > 0) {
        // Chercher si le targetSite actuel est dans la liste
        const exactMatch = verifiedSites.find(s => s === targetSite)
        if (!exactMatch && domain) {
          // Trouver le site vérifié qui correspond au domaine du projet
          const cleanDomain = domain.replace(/^https?:\/\//, '').replace(/\/$/, '').replace(/^www\./, '')
          const bestMatch = verifiedSites.find(s => {
            const clean = s.replace('sc-domain:', '').replace(/^https?:\/\//, '').replace(/\/$/, '').replace(/^www\./, '')
            return clean === cleanDomain || clean.endsWith('.' + cleanDomain) || cleanDomain.endsWith('.' + clean)
          })
          if (bestMatch) {
            log('gsc/site_corrected', 'auto_fix', { from: targetSite, to: bestMatch, domain })
            const oldSite = targetSite
            targetSite = bestMatch
            // Mettre à jour en DB pour éviter de corriger à chaque fois
            if (oldSite) {
              await supabase.from('google_connections').update({ gsc_site: bestMatch }).eq('user_id', userId).eq('gsc_site', oldSite)
            } else {
              await supabase.from('google_connections').update({ gsc_site: bestMatch }).eq('user_id', userId).is('gsc_site', null)
            }
          }
        }
      }
    }
  } catch (siteErr) { /* continue avec le targetSite actuel */ }
  // ── Fin validation ───────────────────────────────────────────────────────

  if (domain && targetSite === (gscSiteOverride || conn.gsc_site)) {
    // Only try domain matching if the verifiedSites block above didn't already correct
    const cleanDomain = domain.replace(/^https?:\/\//, '').replace(/\/$/, '')
    // Only override if the stored gsc_site doesn't match this project's domain
    const storedMatchesDomain = conn.gsc_site && (
      conn.gsc_site.includes(cleanDomain) || cleanDomain.includes(conn.gsc_site.replace('sc-domain:', '').replace('https://', '').replace('http://', '').replace('www.', '').replace('/', ''))
    )
    if (!storedMatchesDomain) {
      // Try all formats, pick first that returns HTTP 200 from GSC
      const candidates = [
        `https://${cleanDomain}/`,
        `https://www.${cleanDomain}/`,
        `sc-domain:${cleanDomain}`,
        `http://${cleanDomain}/`,
      ]
      for (const candidate of candidates) {
        const testResp = await fetch(
          `https://searchconsole.googleapis.com/webmasters/v3/sites/${encodeURIComponent(candidate)}/searchAnalytics/query`,
          {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${accessToken}`, 'Content-Type': 'application/json' },
            body: JSON.stringify({ startDate: start, endDate: end, dimensions: ['query'], rowLimit: 1, dataState: 'final' })
          }
        )
        if (testResp.status === 200) {
          targetSite = candidate
          break
        }
      }
    }
  }

  const gscResp = await fetch(
    `https://searchconsole.googleapis.com/webmasters/v3/sites/${encodeURIComponent(targetSite)}/searchAnalytics/query`,
    {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${accessToken}`, 'Content-Type': 'application/json' },
      body: JSON.stringify(args.type === 'totals' ? {
        startDate: start, endDate: end,
        dataState: 'final'
      } : {
        startDate: start, endDate: end,
        dimensions: dimensionMap[args.type] || ['query'],
        rowLimit,
        orderBy: [{ fieldName: 'clicks', sortOrder: 'DESCENDING' }],
        dataState: 'final'
      })
    }
  )

  if (!gscResp.ok) return { error: 'GSC API error', details: await gscResp.json() }

  const gscData = await gscResp.json()

  // Type "totals" = pas de dimensions, retourne le total agrégé exact (comme l'interface GSC)
  if (args.type === 'totals') {
    const totalsRow = (gscData.rows || [])[0] || {}
    const totals = {
      site: targetSite,
      dateRange: { start, end },
      type: 'totals',
      clicks: totalsRow.clicks || 0,
      impressions: totalsRow.impressions || 0,
      ctr: ((totalsRow.ctr || 0) * 100).toFixed(1) + '%',
      position: (totalsRow.position || 0).toFixed(1),
      totalRows: 1,
      rows: [{
        clicks: totalsRow.clicks || 0,
        impressions: totalsRow.impressions || 0,
        ctr: ((totalsRow.ctr || 0) * 100).toFixed(1) + '%',
        position: (totalsRow.position || 0).toFixed(1)
      }]
    }
    log('connector/fetch_gsc_data', 'totals', { start, end, site: targetSite, clicks: totals.clicks, impressions: totals.impressions })
    try {
      await supabase.from('gsc_cache').upsert(
        { cache_key: cacheKey, data: totals, cached_at: new Date().toISOString(), user_id: userId },
        { onConflict: 'cache_key' }
      )
    } catch (we) {}
    return totals
  }

  const dimensions = dimensionMap[args.type] || ['query']
  const rows = (gscData.rows || []).map((row: any) => {
    const obj: any = {}
    dimensions.forEach((dim: string, i: number) => { obj[dim] = row.keys[i] })
    obj.clicks = row.clicks || 0
    obj.impressions = row.impressions || 0
    obj.ctr = ((row.ctr || 0) * 100).toFixed(1) + '%'
    obj.position = (row.position || 0).toFixed(1)
    return obj
  })

  log('connector/fetch_gsc_data', 'dates', { start, end, site: targetSite, rows: rows.length })
  // ── Écrire en cache ──────────────────────────────────────────────────────
  const result = { site: targetSite, dateRange: { start, end }, type: args.type, totalRows: rows.length, rows }
  try {
    await supabase.from('gsc_cache').upsert(
      { cache_key: cacheKey, data: result, cached_at: new Date().toISOString(), user_id: userId },
      { onConflict: 'cache_key' }
    )
  } catch (we) { /* cache write failed — not critical */ }
  return result
}

// ── GA4 HELPER ──────────────────────────────────────────────
async function fetchGA4Data(args: any, userId: string): Promise<any> {
  const SUPABASE_URL = Deno.env.get('SUPABASE_URL')!
  const ANON_KEY = Deno.env.get('SUPABASE_ANON_KEY')!

  // Load stored property_id from google_connections if not provided
  let propertyId = args.property_id
  if (!propertyId) {
    const supabase = (await import('https://esm.sh/@supabase/supabase-js@2')).createClient(SUPABASE_URL, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!)
    const { data } = await supabase.from('google_connections').select('ga4_property_id').eq('user_id', userId).single()
    propertyId = data?.ga4_property_id
  }

  const body: any = { user_id: userId, action: args.action || 'report' }
  if (propertyId) body.property_id = propertyId
  if (args.days) body.days = args.days
  if (args.dimensions) body.dimensions = args.dimensions
  if (args.metrics) body.metrics = args.metrics
  if (args.limit) body.limit = args.limit

  try {
    const resp = await fetch(`${SUPABASE_URL}/functions/v1/fetch-ga4`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'apikey': ANON_KEY, 'Authorization': `Bearer ${ANON_KEY}` },
      body: JSON.stringify(body),
      signal: AbortSignal.timeout(20000)
    })
    const data = await resp.json()
    if (data.error === 'not_connected') return { error: 'Google Analytics 4 non connecté. Demande à l\'utilisateur de reconnecter Google avec le scope Analytics.' }
    return data
  } catch (err: any) {
    return { error: `GA4 fetch error: ${err.message}` }
  }
}

// ── PAGESPEED — appel direct API Google (pas de Edge Function intermédiaire) ──
const SCORE_LABEL = (s: number) => s >= 0.9 ? 'bon' : s >= 0.5 ? 'moyen' : 'faible'

function parsePSIMetric(audits: any, id: string) {
  const a = audits?.[id]
  if (!a) return { value: null, displayValue: null }
  return { value: a.numericValue ? Math.round(a.numericValue) : null, displayValue: a.displayValue || null }
}

// ─────────────────────────────────────────────────────────────────────────────
// KEYWORD PLANNER IMPORT — parse CSV exporté depuis Google Keyword Planner
// Déclenché quand l'user demande volume/CPC ou colle un CSV dans le chat
// ─────────────────────────────────────────────────────────────────────────────

const KEYWORD_PLANNER_GUIDE = (keywords?: string) => {
  const kwLine = keywords
    ? `**3.** Colle ce(s) mot(s)-clé(s) : \`${keywords}\``
    : `**3.** Colle tes mots-clés (un par ligne)`

  return `Pour obtenir le volume${keywords ? ` de **"${keywords}"**` : ''} depuis Google (data réelle, pas estimée) :

**1.** Va sur [Google Keyword Planner](https://ads.google.com) → Outils → Planification → Keyword Planner
**2.** Clique sur **"Obtenir le volume de recherche et les prévisions"**
${kwLine}
**4.** Configure : Langue **Français** · Localisation **France** · Période **12 derniers mois**
**5.** Clique **"Télécharger les idées de mots-clés"** → format CSV
**6.** Reviens ici et **colle le contenu du CSV** directement dans le chat — je l'analyse automatiquement

_Volume réel Google · CPC · Concurrence · Tendance 12 mois_`
}

function parseKeywordPlannerCSV(csvText: string): {
  success: boolean
  keywords: Array<{
    keyword: string
    volume: number | null
    cpc_min: number | null
    cpc_max: number | null
    cpc_avg: number | null
    competition: string | null
    trend_3m: string | null
    trend_12m: string | null
  }>
  raw_count: number
  error?: string
} {
  if (!csvText || csvText.trim().length < 20) {
    return { success: false, keywords: [], raw_count: 0, error: 'CSV vide ou trop court' }
  }

  // Handle UTF-16 BOM — Google KWP exports UTF-16 LE with BOM (\xFF\xFE or \xFE\xFF)
  // When read as text, null bytes appear as \u0000 between chars
  let cleanText = csvText
  if (csvText.charCodeAt(0) === 0xFF || csvText.charCodeAt(0) === 0xFE ||
      csvText.includes('\u0000') || /^[K\u0000]/.test(csvText)) {
    // Strip null bytes from UTF-16 decoded text
    cleanText = csvText.replace(/\u0000/g, '')
  }
  // Strip BOM if present
  cleanText = cleanText.replace(/^\uFEFF/, '').replace(/^[\xFF\xFE]+/, '')

  const lines = cleanText.trim().split('\n').filter(l => l.trim())

  // Détecter la ligne header — cherche "Keyword" ou "Mot-clé" ou "Avg. monthly searches"
  // Skip metadata lines (file title, date range) — Google KWP has 2 header lines before data
  let headerIdx = -1
  for (let i = 0; i < Math.min(10, lines.length); i++) {
    const lower = lines[i].toLowerCase()
    const hasSeparator = lines[i].includes('\\t') || (lines[i].match(/,/g) || []).length > 2
    // Must be a real header row: has separators AND multiple column names
    const isRealHeader = hasSeparator && (
      (lower.includes('keyword') && (lower.includes('avg') || lower.includes('search') || lower.includes('cpc') || lower.includes('competition') || lower.includes('bid'))) ||
      (lower.includes('mot-cl') && lower.includes('recherch')) ||
      lower.includes('avg. monthly searches')
    )
    if (isRealHeader) {
      headerIdx = i
      break
    }
  }

  if (headerIdx === -1) {
    return { success: false, keywords: [], raw_count: 0, error: 'Header non trouvé — vérifie que tu as bien collé un CSV Google Keyword Planner' }
  }

  const separator = lines[headerIdx].includes('\\t') ? '\\t' : ','
  const headers = lines[headerIdx].split(separator).map(h => h.replace(/"/g, '').trim().toLowerCase())

  // Mapping colonnes — Keyword Planner en FR et EN
  // Debug: log detected headers
  const _headerDebug = headers.slice(0, 12).join(' | ')

  const colMap = {
    keyword:     headers.findIndex(h =>
      h.includes('keyword') || h.includes('mot-clé') || h.includes('mot-cle') ||
      h.includes('mot clé') || h.includes('terme') || h.includes('requête') || h === 'kw'
    ),
    volume:      headers.findIndex(h =>
      h.includes('avg. monthly') || h.includes('avg monthly') ||
      h.includes('recherches mensuelles') || h.includes('rech. mensuelles') ||
      h.includes('monthly searches') || h.includes('volume') ||
      h.includes('impressions moy') || h.includes('moy. mensuel') ||
      h.includes('searches')
    ),
    competition: headers.findIndex(h =>
      h.includes('competition') || h.includes('concurrence') || h.includes('compétition')
    ),
    cpc_min:     headers.findIndex(h =>
      h.includes('top of page bid (low') || h.includes('low range') ||
      h.includes('faible fourchette') || h.includes('enchère') && h.includes('faible') ||
      h.includes('cpc min') || h.includes('bid (low') || h.includes('low bid') ||
      (h.includes('enchère') && h.includes('bas'))
    ),
    cpc_max:     headers.findIndex(h =>
      h.includes('top of page bid (high') || h.includes('high range') ||
      h.includes('fourchette élevée') || h.includes('enchère') && h.includes('élevée') ||
      h.includes('cpc max') || h.includes('bid (high') || h.includes('high bid') ||
      (h.includes('enchère') && h.includes('haut'))
    ),
    cpc_avg:     headers.findIndex(h =>
      h === 'cpc' || h.includes('coût par clic') || h.includes('cost per click') ||
      h.includes('cpc moyen') || h.includes('avg cpc') || h.includes('average cpc')
    ),
    trend_3m:    headers.findIndex(h =>
      h.includes('three') || h.includes('3 month') || h.includes('3 mois') || h.includes('three month')
    ),
    trend_12m:   headers.findIndex(h =>
      h.includes('yoy') || h.includes('year over year') || h.includes('12 mois') || h.includes('annuel')
    ),
  }

  if (colMap.keyword === -1) {
    return { success: false, keywords: [], raw_count: 0, error: `Colonne "keyword" introuvable. Headers détectés : ${headers.slice(0, 8).join(' | ')}` }
  }

  const keywords = []
  for (let i = headerIdx + 1; i < lines.length; i++) {
    const line = lines[i].trim()
    if (!line) continue
    const cols = line.split(separator).map(c => c.replace(/"/g, '').trim())

    const keyword = cols[colMap.keyword]
    if (!keyword || keyword.length < 2) continue

    const parseNum = (idx: number): number | null => {
      if (idx === -1 || idx >= cols.length) return null
      let raw = cols[idx] || ''
      // Remove currency symbols, quotes, spaces
      raw = raw.replace(/[^\\d.,\-]/g, '')
      // Handle European decimal comma: "2,97" → "2.97" but "2.900" (thousands) → keep
      // If comma appears and no dot, it's decimal separator
      if (raw.includes(',') && !raw.includes('.')) {
        raw = raw.replace(',', '.')
      } else if (raw.includes(',') && raw.includes('.')) {
        // e.g. "1.900,50" → "1900.50"
        raw = raw.replace(/\./g, '').replace(',', '.')
      }
      const n = parseFloat(raw)
      return isNaN(n) ? null : n
    }

    const cpc_min = parseNum(colMap.cpc_min)
    const cpc_max = parseNum(colMap.cpc_max)
    const cpc_direct = (colMap as any).cpc_avg >= 0 ? parseNum((colMap as any).cpc_avg) : null
    const cpc_avg = cpc_direct !== null
      ? cpc_direct
      : (cpc_min !== null && cpc_max !== null)
        ? Math.round(((cpc_min + cpc_max) / 2) * 100) / 100
        : (cpc_min ?? cpc_max)

    keywords.push({
      keyword,
      volume:      parseNum(colMap.volume),
      cpc_min,
      cpc_max,
      cpc_avg,
      competition: colMap.competition >= 0 ? (cols[colMap.competition] || null) : null,
      trend_3m:    colMap.trend_3m >= 0 ? (cols[colMap.trend_3m] || null) : null,
      trend_12m:   colMap.trend_12m >= 0 ? (cols[colMap.trend_12m] || null) : null,
    })
  }

  return {
    success: true,
    keywords,
    raw_count: keywords.length,
    _debug: { headers_detected: _headerDebug, colMap_resolved: JSON.stringify(colMap) }
  }
}

function formatKeywordPlannerResults(parsed: ReturnType<typeof parseKeywordPlannerCSV>): string {
  if (!parsed.success || parsed.keywords.length === 0) {
    return `❌ Import échoué : ${parsed.error || 'aucun mot-clé trouvé'}\n\nHeaders détectés : ${(parsed as any)._debug?.headers_detected || '—'}\n\n${KEYWORD_PLANNER_GUIDE()}`
  }

  // Debug: if no volume/CPC found, show what was detected
  const hasVolume = parsed.keywords.some(k => k.volume !== null)
  const hasCPC = parsed.keywords.some(k => k.cpc_avg !== null && k.cpc_avg > 0)
  if (!hasVolume && !hasCPC) {
    return `⚠️ ${parsed.raw_count} mots-clés détectés mais colonnes volume/CPC non trouvées.\n\nHeaders CSV détectés : \`${(parsed as any)._debug?.headers_detected || '—'}\`\nMapping colonnes : \`${(parsed as any)._debug?.colMap_resolved || '—'}\`\n\nVérifie que le fichier contient bien les colonnes volume et CPC, ou colle directement les headers ci-dessus pour que je les identifie.`
  }

  const kws = parsed.keywords

  // Trier par CPC décroissant (méthode Timothée : CPC > volume)
  const sorted = [...kws].sort((a, b) => (b.cpc_avg ?? 0) - (a.cpc_avg ?? 0))
  const top = sorted.slice(0, 20)

  // Stats globales
  const withVolume  = kws.filter(k => k.volume !== null)
  const withCPC     = kws.filter(k => k.cpc_avg !== null && k.cpc_avg > 0)
  const avgCPC      = withCPC.length > 0
    ? Math.round((withCPC.reduce((s, k) => s + (k.cpc_avg ?? 0), 0) / withCPC.length) * 100) / 100
    : null

  // Construire le tableau
  const tableRows = top.map((k, i) => {
    const vol  = k.volume !== null ? k.volume.toLocaleString('fr-FR') : '—'
    const cpc  = k.cpc_avg !== null && k.cpc_avg > 0 ? `${k.cpc_avg.toFixed(2)} €` : '—'
    const comp = k.competition || '—'
    const trend = k.trend_12m || '—'
    const trend12 = k.trend_12m && k.trend_12m.startsWith('-') ? k.trend_12m : (k.trend_12m ? `+${k.trend_12m}` : '—')
    return `| ${i+1} | ${k.keyword} | ${vol} | ${cpc} | ${comp} | ${trend12} |`
  }).join('\n')

  return `✅ **${parsed.raw_count} mots-clés importés** · ${withVolume.length} avec volume · CPC moyen **${avgCPC ? avgCPC + ' €' : '—'}**

| # | Mot-clé | Volume | CPC | Concurrence | Tendance YoY |
|---|---------|--------|-----|-------------|--------------|
${tableRows}

_Source : Google Keyword Planner · Triés par CPC décroissant (méthode business-first)_`
}

async function fetchPagespeed(url: string, strategy: string = 'mobile'): Promise<any> {
  try {
    const apiKey = Deno.env.get('PAGESPEED_API_KEY') || ''
    const apiUrl = `https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${encodeURIComponent(url)}\&strategy=${strategy}\&category=performance\&category=seo\&category=accessibility${apiKey ? `\&key=${apiKey}` : ''}`

    const resp = await fetch(apiUrl, { signal: AbortSignal.timeout(30000) })
    if (!resp.ok) {
      const err = await resp.json()
      return { error: err.error?.message || `PageSpeed API error ${resp.status}`, url }
    }

    const data = await resp.json()
    const lhr = data.lighthouseResult
    const categories = lhr?.categories || {}
    const audits = lhr?.audits || {}
    const crux = data.loadingExperience?.metrics || null

    const lcp = parsePSIMetric(audits, 'largest-contentful-paint')
    const inp = parsePSIMetric(audits, 'interaction-to-next-paint') || parsePSIMetric(audits, 'total-blocking-time')
    const cls = parsePSIMetric(audits, 'cumulative-layout-shift')
    const fcp = parsePSIMetric(audits, 'first-contentful-paint')
    const ttfb = parsePSIMetric(audits, 'server-response-time')

    const perfScore = Math.round((categories.performance?.score || 0) * 100)
    const seoScore = Math.round((categories.seo?.score || 0) * 100)
    const a11yScore = Math.round((categories.accessibility?.score || 0) * 100)

    const opportunities = [
      'render-blocking-resources', 'unused-javascript', 'unused-css-rules',
      'uses-optimized-images', 'uses-next-gen-formats', 'uses-text-compression'
    ].map(id => {
      const a = audits[id]
      if (!a || a.score === 1 || a.score === null) return null
      return {
        title: a.title,
        score: a.score,
        displayValue: a.displayValue,
        savings: a.details?.overallSavingsMs ? `${Math.round(a.details.overallSavingsMs)}ms` : null
      }
    }).filter(Boolean).sort((a: any, b: any) => (a.score || 1) - (b.score || 1)).slice(0, 5)

    // Résumé texte pour l'agent
    const summaryLines = []
    if (perfScore >= 90) summaryLines.push(`Performance excellente (${perfScore}/100)`)
    else if (perfScore >= 50) summaryLines.push(`Performance moyenne (${perfScore}/100) — optimisations possibles`)
    else summaryLines.push(`Performance faible (${perfScore}/100) — impact direct sur le SEO`)

    if (lcp.value) {
      const lcpS = (lcp.value / 1000).toFixed(1)
      if (lcp.value > 4000) summaryLines.push(`LCP critique : ${lcpS}s (seuil : < 2.5s) — pénalité ranking probable`)
      else if (lcp.value > 2500) summaryLines.push(`LCP moyen : ${lcpS}s — à optimiser pour atteindre < 2.5s`)
      else summaryLines.push(`LCP bon : ${lcpS}s`)
    }
    if (cls.value !== null && cls.value !== undefined && cls.value > 0.1) {
      summaryLines.push(`CLS instable : ${cls.displayValue} — expérience dégradée`)
    }
    if (opportunities.length > 0 && (opportunities[0] as any).savings) {
      summaryLines.push(`Top opportunité : ${(opportunities[0] as any).title} (\~${(opportunities[0] as any).savings})`)
    }

    return {
      url, strategy,
      scores: {
        performance: { value: perfScore, label: SCORE_LABEL(perfScore / 100) },
        seo: { value: seoScore, label: SCORE_LABEL(seoScore / 100) },
        accessibility: { value: a11yScore, label: SCORE_LABEL(a11yScore / 100) },
      },
      coreWebVitals: {
        lcp: { ...lcp, field: crux?.LARGEST_CONTENTFUL_PAINT_MS ? { p75: crux.LARGEST_CONTENTFUL_PAINT_MS.percentile, category: crux.LARGEST_CONTENTFUL_PAINT_MS.category } : null, threshold: { good: 2500, poor: 4000, unit: 'ms' } },
        cls: { ...cls, field: crux?.CUMULATIVE_LAYOUT_SHIFT_SCORE ? { p75: crux.CUMULATIVE_LAYOUT_SHIFT_SCORE.percentile / 100, category: crux.CUMULATIVE_LAYOUT_SHIFT_SCORE.category } : null, threshold: { good: 0.1, poor: 0.25, unit: '' } },
        inp: { ...inp, field: crux?.INTERACTION_TO_NEXT_PAINT ? { p75: crux.INTERACTION_TO_NEXT_PAINT.percentile, category: crux.INTERACTION_TO_NEXT_PAINT.category } : null, threshold: { good: 200, poor: 500, unit: 'ms' } },
        fcp: { ...fcp, field: crux?.FIRST_CONTENTFUL_PAINT_MS ? { p75: crux.FIRST_CONTENTFUL_PAINT_MS.percentile, category: crux.FIRST_CONTENTFUL_PAINT_MS.category } : null, threshold: { good: 1800, poor: 3000, unit: 'ms' } },
        ttfb: { ...ttfb, threshold: { good: 800, poor: 1800, unit: 'ms' } },
      },
      hasFieldData: !!crux,
      opportunities,
      summary: summaryLines.join('. '),
      fetchedAt: new Date().toISOString()
    }
  } catch (err: any) {
    return { error: `PageSpeed fetch error: ${err.message}`, url }
  }
}

// ── OPTIMIZATIONS — log + check ──────────────────────────────────────────

async function logOptimization(
  supabase: any,
  userId: string,
  domain: string,
  url: string | null,
  action: string,
  type: string,
  context: string
) {
  try {
    await supabase.from('optimizations').insert({
      user_id: userId,
      domain,
      url: url || null,
      action,
      type,
      status: 'suggested',
      context: context.slice(0, 500),
      suggested_at: new Date().toISOString(),
      updated_at: new Date().toISOString()
    })
    log('agent/optimizations', 'logged', { domain, url, type })
  } catch (e: any) {
    log('agent/optimizations', 'log_error', { error: e.message })
  }
}

async function checkOptimizationHistory(
  supabase: any,
  userId: string,
  domain: string,
  url: string | null
): Promise<string> {
  try {
    let query = supabase
      .from('optimizations')
      .select('action, type, status, suggested_at')
      .eq('user_id', userId)
      .eq('domain', domain)
      .neq('status', 'dismissed')
      .order('suggested_at', { ascending: false })
      .limit(5)

    if (url) query = query.eq('url', url)

    const { data } = await query
    if (!data || data.length === 0) return ''

    const lines = data.map((o: any) => {
      const date = new Date(o.suggested_at).toLocaleDateString('fr-FR')
      return `- [${o.type}] ${o.action} (suggéré le ${date}, statut : ${o.status})`
    }).join("\n")

    const header = "\n\n## Optimisations déjà suggérées sur cette URL\n"
    const footer = "\nNe pas répéter ces recommandations sauf si le statut est suggested depuis plus de 14 jours."
    return header + lines + footer
  } catch {
    return ''
  }
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { status: 200, headers: corsHeaders })

  try {
    const body = await req.json()
    const { message: rawMessage, domain, gscSite: _gscSiteCamel, gsc_site: _gscSiteSnake, history = [], projectMemory, kwp_csv } = body
const gscSite = _gscSiteCamel || _gscSiteSnake || null

    // ── Résolution user_id — fallback JWT si body.user_id absent ─────────
    let user_id: string | null = body.user_id || null
    if (!user_id) {
      try {
        const authHeader = req.headers.get('Authorization') || ''
        const jwt = authHeader.replace('Bearer ', '').trim()
        if (jwt && jwt !== 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl0Z2JucXFtY25obXNjYnZob2luIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI2NjgzMDAsImV4cCI6MjA4ODI0NDMwMH0.dXu5CKtTKYCzSM4Z5ZBbLf-92yfS9ggEll4GRPXedgo') {
          const { data: { user } } = await createClient(
            Deno.env.get('SUPABASE_URL')!,
            Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
          ).auth.getUser(jwt)
          if (user?.id) user_id = user.id
        }
      } catch { /* pas de JWT valide — continuer sans user_id */ }
    }
    log('agent/request', 'user_resolved', { user_id_from_body: !!body.user_id, user_id_resolved: !!user_id })

    // ── Détection automatique CSV Keyword Planner ──────────────────────────
    let message = rawMessage
    let kwpCsvAutoInject: string | null = kwp_csv || null

    // Fallback : ancien système [KWP_CSV] au cas où
    if (!kwpCsvAutoInject && typeof rawMessage === 'string' && rawMessage.startsWith('[KWP_CSV]\n')) {
      kwpCsvAutoInject = rawMessage.slice('[KWP_CSV]\n'.length)
      message = 'Analyse ce fichier CSV Google Keyword Planner et affiche le tableau des mots-clés trié par CPC décroissant avec volume, CPC et tendance.'
    }

    // Si kwp_csv présent, enrichir le message avec instruction explicite
    if (kwpCsvAutoInject && rawMessage && !rawMessage.startsWith('[KWP_CSV]')) {
      message = rawMessage + '\n\n[INSTRUCTION SYSTÈME : Un fichier CSV Google Keyword Planner a été fourni. Tu DOIS appeler l\'outil parse_keyword_planner avec le csv_text fourni en contexte. Ne pas demander de confirmation, analyser directement.]'
    }

    const supabase = createClient(Deno.env.get('SUPABASE_URL'), Deno.env.get('SUPABASE_SERVICE_ROLE_KEY'))
    // ── Pool de clés Gemini (round-robin) ──────────────────────────────────
    const _geminiKeys = [
      Deno.env.get('GEMINI_API_KEY'),
      Deno.env.get('GEMINI_API_KEY_2'),
    ].filter(Boolean) as string[]
    const GEMINI_KEY = _geminiKeys[Math.floor(Math.random() * _geminiKeys.length)]
    // ── Fin pool clés ───────────────────────────────────────────────────

    // ── Plan & message quota check ──────────────────────────────
    if (user_id) {
      try {
        const { data: _planRows } = await supabase
          .from('google_connections')
          .select('plan, messages_used, messages_reset_at, gsc_site')
          .eq('user_id', user_id)
          .order('updated_at', { ascending: false })
          .limit(1)
        const planData = Array.isArray(_planRows) ? _planRows[0] : _planRows

        if (planData) {
          // Reset mensuel automatique (sauf plan free — 8 discussions à vie)
          const resetAt = new Date(planData.messages_reset_at || 0)
          const now = new Date()
          const monthChanged = now.getFullYear() > resetAt.getFullYear() ||
            now.getMonth() > resetAt.getMonth()
          const planForReset = planData.plan || 'free'

          if (monthChanged && planForReset !== 'free') {
            await supabase.from('google_connections')
              .update({ messages_used: 0, messages_reset_at: now.toISOString() })
              .eq('user_id', user_id)
            planData.messages_used = 0
          }

          // Vérifier la limite
          const plan = planData.plan || 'free'
          // free = 22 messages à vie (pas de reset mensuel)
          // beta = ancien plan illimité (legacy)
          const limits: Record<string, number | null> = { free: 22, beta: null, solo: 150, pro: 250, agency: 550 }
          const limit = limits[plan] ?? 10

          // Pas de reset mensuel pour le plan free (lifetime)
          const isFree = plan === 'free'
          if (isFree && planData.messages_used === 0 && monthChanged) {
            // Ne pas resetter pour free — les 22 messages sont à vie
          }

          if (limit !== null && planData.messages_used >= limit) {
            const encoder = new TextEncoder()
            const stream = new ReadableStream({
              start(controller) {
                const msg = JSON.stringify({
                  type: 'limit_reached',
                  plan,
                  limit,
                  used: planData.messages_used,
                  message: plan === 'free'
                    ? `Limite de 22 messages gratuits atteinte. Pour exploiter au mieux toutes les fonctionnalités, choisissez un plan premium : qadence.io/tarifs`
                    : plan === 'solo'
                    ? `Limite de 150 messages atteinte ce mois-ci. Pour continuer, passez au plan Pro : qadence.io/tarifs`
                    : plan === 'pro'
                    ? `Limite de 250 messages atteinte ce mois-ci. Pour continuer, passez au plan Agency : qadence.io/tarifs`
                    : `Limite atteinte ce mois-ci. Écrivez-nous : hello@qadence.io`
                })
                controller.enqueue(encoder.encode('data: ' + msg + '\n\n'))
                controller.enqueue(encoder.encode('data: [DONE]\n\n'))
                controller.close()
              }
            })
            return new Response(stream, {
              headers: { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*' }
            })
          }

          // Incrément atomique via RPC — évite la race condition
          // On update UNIQUEMENT si messages_used < limit (WHERE clause)
          const newCount = (planData.messages_used || 0) + 1
          let _incrQ = supabase
            .from('google_connections')
            .update({ messages_used: newCount })
            .eq('user_id', user_id)
            .lt('messages_used', limit ?? 99999)
          if (gscSite) _incrQ = _incrQ.eq('gsc_site', gscSite)
          const { error: incrErr } = await _incrQ
          // Si incrErr ou 0 lignes modifiées (limit déjà atteinte en concurrent) → bloquer
          if (limit !== null && incrErr) {
            const encoder2 = new TextEncoder()
            const stream2 = new ReadableStream({
              start(controller) {
                const msg = JSON.stringify({ type: 'limit_reached', plan, limit, used: limit })
                controller.enqueue(encoder2.encode('data: ' + msg + '\n\n'))
                controller.enqueue(encoder2.encode('data: [DONE]\n\n'))
                controller.close()
              }
            })
            return new Response(stream2, {
              headers: { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*' }
            })
          }
        }
      } catch (e) {
        console.error('Plan check error:', e)
        // Ne pas bloquer l'agent si le check échoue
      }
    }
    // ── Fin plan check ──────────────────────────────────────────
    // ── Rate limiter par user_id ─────────────────────────────────────────────
    // Max 5 requêtes par user_id par fenêtre de 60 secondes
    // Stocké dans la table rate_limits (upsert atomique)
    if (user_id) {
      try {
        const windowStart = new Date(Date.now() - 60_000).toISOString()

        // Compter les requêtes dans la fenêtre actuelle
        const { count } = await supabase
          .from('rate_limits')
          .select('*', { count: 'exact', head: true })
          .eq('user_id', user_id)
          .gte('created_at', windowStart)

        const RL_MAX = 10 // max 10 req / 60s par user

        if ((count ?? 0) >= RL_MAX) {
          log('rate_limiter', 'blocked', { user_id, count })
          const encoder = new TextEncoder()
          const stream = new ReadableStream({
            start(controller) {
              controller.enqueue(encoder.encode(
                `data: ${JSON.stringify({
                  text: "Trop de requêtes. Patiente quelques secondes avant de réessayer.",
                  done: true
                })}\n\n`
              ))
              controller.close()
            }
          })
          return new Response(stream, {
            headers: { ...corsHeaders, 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache' }
          })
        }

        // Insérer la requête actuelle
        await supabase.from('rate_limits').insert({ user_id, created_at: new Date().toISOString() })

        // Purger les entrées > 5 min pour garder la table propre
        supabase.from('rate_limits').delete().lt('created_at', new Date(Date.now() - 300_000).toISOString()).then(() => {})

      } catch (rl_err: any) {
        log('rate_limiter', 'error', { error: rl_err.message })
        // En cas d'erreur du rate limiter → laisser passer (fail open)
      }
    }
    // ── Fin rate limiter ──────────────────────────────────────────────────────

    const GEMINI_BASE = `https://generativelanguage.googleapis.com/v1beta/models`

    // Toujours démarrer avec Flash — il s'auto-escalade vers Pro si besoin
    let currentModel = 'gemini-2.5-flash'
    let GEMINI_URL = `${GEMINI_BASE}/${currentModel}:generateContent?key=${GEMINI_KEY}`

    const t0_request = Date.now()
    log('agent/request', 'incoming', { user_id, domain, message_length: message?.length })

    const today = new Date().toISOString().split('T')[0]
    const gscMaxDate = new Date(Date.now() - 4 * 86400000).toISOString().split('T')[0]
    const dateContext = '[DATE : ' + today + ' | GSC MAX : ' + gscMaxDate + ']'
    // Check GSC connection
    let gscConnected = false
    let gscSiteResolved = gscSite
    if (user_id) {
      try {
        // Chercher toutes les connexions — prendre celle qui correspond au site actif si possible
        const { data: allConns } = await supabase
          .from('google_connections')
          .select('gsc_site, access_token')
          .eq('user_id', user_id)
          .not('access_token', 'is', null)
        if (allConns && allConns.length > 0) {
          gscConnected = true
          let matchingConn = null
          if (gscSiteResolved) {
            // Match exact par gscSite du projet
            matchingConn = allConns.find((c: any) => c.gsc_site === gscSiteResolved) || allConns[0]
          } else if (domain) {
            // gscSite pas encore assigné — matcher par domaine
            const cleanDomain = domain.replace(/^https?:\/\//, '').replace(/\/$/, '').replace(/^www\./, '').toLowerCase()
            const candidates = [
              `sc-domain:${cleanDomain}`,
              `https://www.${cleanDomain}/`,
              `https://${cleanDomain}/`,
              `http://${cleanDomain}/`,
              `https://www.${cleanDomain}`,
              `https://${cleanDomain}`
            ]
            matchingConn = allConns.find((c: any) => {
              if (!c.gsc_site) return false
              // Match exact
              if (candidates.some(cand => c.gsc_site.toLowerCase() === cand.toLowerCase())) return true
              // Match partiel (le gsc_site contient le domaine)
              const cleanSite = c.gsc_site.replace('sc-domain:', '').replace(/^https?:\/\//, '').replace(/\/$/, '').replace(/^www\./, '').toLowerCase()
              return cleanSite === cleanDomain
            }) || allConns[0]
          } else {
            matchingConn = allConns[0]
          }
          if (!gscSiteResolved && matchingConn.gsc_site) gscSiteResolved = matchingConn.gsc_site
        }
      } catch {}
    }
    const gscStatus = gscConnected
      ? (
          'GSC CONNECTÉE — site: ' + (gscSiteResolved || 'non résolu') +
          '\nRÈGLES STRICTES quand GSC est connectée :' +
          '\n• INTERDIT de demander le secteur d\'activité ou la ville si la question porte sur trafic, positions, clics, CTR, impressions — ces infos sont déductibles des requêtes GSC.' +
          '\n• INTERDIT de dire "Je vais récupérer les données" sans appeler fetch_gsc_data dans ce même message.' +
          '\n• Question sur les performances du site → appeler fetch_gsc_data IMMÉDIATEMENT, sans demander de confirmation.'
        )
      : 'GSC NON CONNECTÉE — ne pas appeler fetch_gsc_data'
    const contextNote = domain
      ? ('\n\n[PROJET ACTIF : ' + domain + ' | ' + gscStatus + ']\n' + dateContext)
      : ('\n\n[' + gscStatus + ']\n' + dateContext)

    // Charger custom_instructions + context_notes + context_documents
    let customContext = ''
    if (user_id && domain) {
      try {
        const { data: ctxRows } = await supabase
          .from('project_memory')
          .select('key, value')
          .eq('user_id', user_id)
          .eq('domain', domain)
          .in('key', ['custom_instructions', 'context_notes', 'context_documents'])

        if (ctxRows) {
          const ctxMap: Record<string, any> = {}
          for (const row of ctxRows) ctxMap[row.key] = row.value

          if (ctxMap.custom_instructions) {
            customContext += '\n\n[INSTRUCTIONS CLIENT]\n' + ctxMap.custom_instructions
          }
          if (Array.isArray(ctxMap.context_notes) && ctxMap.context_notes.length > 0) {
            customContext += '\n\n[NOTES CONTEXTE]\n' + ctxMap.context_notes.map((n: any) => n.text).join('\n')
          }
          if (Array.isArray(ctxMap.context_documents) && ctxMap.context_documents.length > 0) {
            customContext += '\n\n[DOCUMENTS REFERENCE]\n' + ctxMap.context_documents.map((d: any) => '--- ' + d.filename + ' ---\n' + (d.content || '')).join('\n')
          }
        }
      } catch {}
    }

    // contextNote final — inclut customContext chargé ci-dessus
    // Check if profile is empty — if so, inject onboarding instruction
    let profileHint = ''
    if (user_id && domain) {
      try {
        const { data: profileRow } = await supabase
          .from('project_memory')
          .select('value')
          .eq('user_id', user_id)
          .eq('domain', domain)
          .eq('key', 'profile')
          .maybeSingle()
        const hasProfile = profileRow?.value && (profileRow.value.industry || profileRow.value.site_type)
        if (!hasProfile) {
          profileHint = '\n\n[NOTE SYSTEME : Le profil de ce projet est vide. Reponds DABORD a la question de l\'utilisateur normalement (lance l\'audit, analyse les donnees, etc.). A LA FIN de ta reponse, ajoute un bloc BIEN VISIBLE avec ce format EXACT (markdown) :\n\n---\n\n**Pour personnaliser tes prochaines analyses, j\'ai besoin de 3 infos :**\n\n1. **Secteur** \u2014 Decris ton activite en une phrase (ex: consulting pour organismes de formation, e-commerce mode femme, cabinet dentaire...)\n2. **Audience cible** \u2014 Qui sont tes clients ? B2B ou B2C ? Quelle zone geo ?\n3. **3 mots-cles prioritaires** \u2014 Les requetes sur lesquelles tu veux absolument te positionner\n\n> Reponds directement ici, je memorise tout pour la suite.\n\nCe bloc doit etre APRES l\'analyse, separe par un ---. Ne JAMAIS bloquer l\'analyse pour poser ces questions. Ne JAMAIS reformuler ces questions, utiliser ce format exact avec les numeros et le bold.]'
        }
      } catch {}
    }
    const contextNoteFinal = contextNote + customContext + profileHint

    // Vérifier last_interaction pour le "Depuis ta dernière visite"
    let lastVisitHint = ''
    if (user_id && domain) {
      try {
        const { data: lastRow } = await supabase
          .from('project_memory')
          .select('value')
          .eq('user_id', user_id)
          .eq('domain', domain)
          .eq('key', 'last_interaction')
          .maybeSingle()
        if (lastRow?.value) {
          const lastDate = new Date(String(lastRow.value))
          const daysSince = Math.floor((Date.now() - lastDate.getTime()) / 86400000)
          if (daysSince >= 7) {
            lastVisitHint = '\n\n[INSTRUCTION SYSTEME : L\'utilisateur revient apres ' + daysSince + ' jours d\'absence. Commence ta reponse par "Depuis ta derniere visite il y a ' + daysSince + ' jours," suivi d\'un fait concret issu de la memoire projet (top page, quick win identifie, ou objectif enregistre). Puis reponds normalement.]'
          }
        }
        // Mettre à jour last_interaction
        await supabase.from('project_memory').upsert(
          { user_id, domain, key: 'last_interaction', value: today, updated_at: new Date().toISOString() },
          { onConflict: 'user_id,domain,key' }
        )
      } catch {}
    }

    // Detect traffic intent — inject explicit instruction
    const trafficKeywords = ['visite', 'visites', 'trafic', 'traffic', 'clics', 'clicks', 'sessions', 'combien de visite', 'nombre de visite']
    const isTrafficQuery = trafficKeywords.some(k => message.toLowerCase().includes(k))
    const trafficHint = isTrafficQuery
      ? '\n\n[INSTRUCTION SYSTÈME : Cette question porte sur le TRAFIC. Tu DOIS appeler fetch_gsc_data avec type="totals" pour obtenir le total exact. Ce type retourne directement le total agrégé comme dans GSC. NE PAS additionner les lignes de pages ou queries.]'
      : ''

    // Audit hint — forcer l'affichage du livrable complet
    const auditKeywords = ['audit', 'analyse complète', 'bilan seo', 'analyse seo', 'rapport seo']
    const isAuditQuery = auditKeywords.some(k => message.toLowerCase().includes(k))
    const auditHint = isAuditQuery && gscConnected
      ? '\n\n[INSTRUCTION SYSTÈME PRIORITAIRE : Audit GSC demandé. WORKFLOW OBLIGATOIRE dans cet ordre strict : (1) fetch_gsc_data(type="pages", rowLimit=500) MAINTENANT — onglet Pages, (2) fetch_gsc_data(type="queries", rowLimit=500) MAINTENANT — onglet Mots-clés, (3) load_skill(skill_name="audit_gsc"). INTERDICTION ABSOLUE de sauter l\'étape pages ou de faire uniquement queries. Les deux fetches sont obligatoires avant de charger le skill. Affiche ensuite les 5 blocs complets : (1) Synthèse chiffrée, (2) Pages en déclin, (3) Quick wins, (4) Requêtes décisionnelles, (5) Plan d\'action 3 horizons.]'
      : isAuditQuery
      ? '\n\n[INSTRUCTION SYSTÈME : Audit GSC demandé mais GSC non connectée. Demande à l\'utilisateur de connecter sa Search Console avant de lancer l\'audit.]'
      : ''

    // Stratégie hint — forcer fetch GSC puis load_skill strategie_seo
    const strategieKeywords = ['strat', 'strateg', 'plan seo', 'positionner', 'pages créer']
    const isStrategieQuery = strategieKeywords.some(k => message.toLowerCase().includes(k))
    const strategieHint = isStrategieQuery && gscConnected
      ? "\n\n[INSTRUCTION SYSTEME PRIORITAIRE : Demande de strategie SEO. GSC connectee. WORKFLOW OBLIGATOIRE dans cet ordre : (1) fetch_gsc_data(type=\"pages\", rowLimit=500) MAINTENANT, (2) fetch_gsc_data(type=\"queries\", rowLimit=500) MAINTENANT, (3) load_skill(skill_name=\"strategie_seo\"). INTERDICTIONS ABSOLUES : NE JAMAIS inventer un chiffre de clics, impressions, CTR ou position absent des donnees GSC fetchees. NE JAMAIS nommer une page ou requete sans quelle soit dans les donnees GSC. NE JAMAIS ecrire exemple: ou illustrer avec des donnees fictives. Chaque chiffre cite = extrait directement des donnees fetch_gsc_data reelles. Si une donnee manque = ne pas la mentionner.]"
      : isStrategieQuery
        ? "\n\n[INSTRUCTION SYSTEME : Demande de strategie SEO. GSC non connectee. Poser UNE seule question courte : secteur et ville du site.]"
        : ""

    // Brief contenu hint — forcer load_skill avec la requete correcte
    const briefKeywords = ['brief', 'brief de contenu', 'fais un brief', 'créer un brief', 'rédige un brief']
    const isBriefQuery = briefKeywords.some(k => message.toLowerCase().includes(k))
    const briefTarget = message.slice(0, 120)
    const briefHint = isBriefQuery
      ? '\n\n[INSTRUCTION SYSTÈME PRIORITAIRE : Brief de contenu demandé. WORKFLOW OBLIGATOIRE : (1) Extrais le mot-clé ou URL cible du message de l\'utilisateur et utilise-le comme requete. (2) Appelle IMMÉDIATEMENT load_skill(skill_name="brief_contenu", requete="[mot-clé extrait du message]"). (3) NE PAS redemander la requête si elle est déjà dans la conversation. NE PAS demander des précisions inutiles. Lance le brief maintenant.]'
      : ''

    // KWP hint — forcer parse_keyword_planner quand l'user demande volume ou CPC
    // Maillage interne hint — forcer le workflow complet
    const maillageKeywords = ['maillage', 'liens internes', 'cocon', 'page mère', 'page fille', 'orpheline', 'linkmap', 'link map']
    const isMaillageQuery = gscConnected && maillageKeywords.some(k => message.toLowerCase().includes(k))
    const maillageHint = isMaillageQuery
      ? `\n\n[INSTRUCTION SYSTÈME PRIORITAIRE : Analyse de maillage interne demandée. WORKFLOW OBLIGATOIRE dans cet ordre strict :
(1) fetch_gsc_data(type="queries_pages", rowLimit=500) MAINTENANT — matrice pages × mots-clés partagés
(2) fetch_gsc_data(type="pages", rowLimit=500) MAINTENANT — toutes les URLs avec métriques
(3) Identifier les 3-5 paires de pages avec le plus de mots-clés partagés
(4) fetch_page_content(url) sur ces pages pour vérifier les liens existants dans le HTML
(5) load_skill(skill_name="maillage_interne") avec toutes les données
INTERDIT de charger le skill sans les données queries_pages. INTERDIT de demander un export CSV — utiliser directement la GSC connectée.]`
      : ''

    const kwpKeywords = ['volume', 'cpc', 'keyword planner', 'recherches mensuelles', 'nombre de recherche', 'combien de recherche', 'trafic potentiel', 'potentiel de recherche', 'concurrence mot', 'données google ads', 'data keyword', 'volume de recherche']
    const isKwpQuery = kwpKeywords.some(k => message.toLowerCase().includes(k))
    const kwpHint = isKwpQuery
      ? `\n\n[INSTRUCTION SYSTÈME PRIORITAIRE : L'utilisateur demande des données volume/CPC. Tu DOIS appeler l'outil parse_keyword_planner MAINTENANT avec keywords_context="${message.slice(0, 100)}". INTERDIT de répondre en prose sans appeler cet outil. L'outil affichera le guide d'import Google Keyword Planner automatiquement.]`
      : ''

    // Position loss hint — forcer le double fetch + calcul de delta
    const positionLossKeywords = [
      'perdu des position', 'perdu ma position', 'perdu en position', 'j\'ai perdu',
      'baisse de position', 'baisse des position', 'chute de position', 'chute des position',
      'recul de position', 'recul des position', 'je perds', 'je régresse',
      'positions baissent', 'positions ont baissé', 'positions qui baissent',
      'pages qui baissent', 'pages qui chutent', 'pages en déclin', 'déclin de',
      'pourquoi je perds', 'pourquoi j\'ai perdu', 'est ce que j\'ai perdu', 'est-ce que j\'ai perdu',
      'perte de position', 'pertes de position', 'perte de rang', 'perte de classement',
      'position sur ', 'positionné sur ', 'je ranke', 'je me positionne', 'mon positionnement sur',
      'position pour ', 'rank sur ', 'ranking sur ', 'où suis-je sur', 'ou suis-je sur',
      'ma position sur', 'quelle position', 'quel rang'
    ]
    const isPositionLossQuery = positionLossKeywords.some(k => message.toLowerCase().includes(k))

    // Generic keyword query - user asks about ranking/position on a specific term
    const kwQueryKeywords = ['sur le mot-clé', 'sur la requête', 'pour le mot-clé', 'pour la requête', 'sur ce mot-clé', 'keyword ', 'mots-clés ', 'requête ', 'positionnement', 'visibilité sur', 'trafic sur', 'ranker sur', 'rankons sur', 'apparaître sur']
    const isKwPositionQuery = !isPositionLossQuery && gscConnected && kwQueryKeywords.some(k => message.toLowerCase().includes(k))
    // Extract keyword from message if mentioned
    const _msgLower = message.toLowerCase()
    const _kwMatch = message.match(/sur\\s+["']?([\\w\\s\-\.]+?)["']?(?:\\s*\\?|$)/i)
    const _kwMentioned = _kwMatch ? _kwMatch[1].trim() : ''

    const positionLossHint = isPositionLossQuery && gscConnected
      ? `\n\n[INSTRUCTION SYSTÈME PRIORITAIRE — ANALYSE DE PERTE DE POSITIONS :
${_kwMentioned ? `Mot-clé/produit mentionné : "${_kwMentioned}" — chercher les requêtes GSC qui contiennent ce terme.` : ''}

WORKFLOW OBLIGATOIRE — exécuter immédiatement sans poser de questions :

ÉTAPE 1 — fetch_gsc_data(type="queries", rowLimit=500, startDate=J-28, endDate=J-1)
ÉTAPE 2 — fetch_gsc_data(type="queries", rowLimit=500, startDate=J-56, endDate=J-29)

ÉTAPE 3 — Après les fetches, produire IMMÉDIATEMENT la réponse :
${_kwMentioned ? `→ Filtrer les requêtes contenant "${_kwMentioned}"` : '→ Analyser toutes les requêtes'}
→ Pour chaque requête : position période 1 vs période 2, delta, clics, impressions
→ Format : tableau avec colonnes Requête | Pos. actuelle | Pos. précédente | Delta | Clics
→ Diagnostic en 2-3 phrases : cause probable (algo Google / concurrence / saisonnalité)

INTERDIT de dire "je vais analyser" sans produire les données ensuite.
INTERDIT de demander des précisions — travailler avec les données disponibles.
INTERDIT de faire un seul fetch — deux périodes obligatoires pour le delta.
APRÈS les 2 fetches : réponse directe avec le tableau et le diagnostic. Pas d'autre message d'attente.]`
      : isPositionLossQuery && !gscConnected
        ? `\n\n[INSTRUCTION SYSTÈME : L'utilisateur demande une analyse de perte de positions. GSC non connectée. Répondre : "Pour analyser l'évolution de tes positions, connecte ta Search Console dans les paramètres du projet."]`
        : ''

    // Période hint — comparaison directe 28j vs 28j précédents
    // Skill hints — certains skills doivent fetch GSC avant tout
    const skillGscKeywords = ['requêtes principales', 'analyse mes requêtes', 'segmente mes requêtes', 'cohortes', 'clusters de requêtes', 'analyser mes mots-clés']
    const isSkillGscQuery = gscConnected && skillGscKeywords.some(k => message.toLowerCase().includes(k))
    const skillGscHint = isSkillGscQuery
      ? `\n\n[INSTRUCTION SYSTÈME : L'utilisateur demande une analyse de ses requêtes GSC. WORKFLOW OBLIGATOIRE :
1. fetch_gsc_data(type="queries", rowLimit=500) MAINTENANT — pas de question préalable
2. Utiliser les requêtes réelles pour répondre — elles remplacent tout contexte manquant
3. INTERDIT de demander le secteur ou l'objectif avant d'avoir les données GSC]`
      : ''

    const periodeKeywords = ['compare', 'comparer', 'deux périodes', 'deux periodes', 'dernières périodes', 'dernieres periodes', 'plan RICE', 'plan rice', 'analyse comparative']
    const hasPeriodeSpecifique = ['30 jours', '7 jours', 'semaine', 'mois', 'J-', 'j-', '90', '28'].some(k => message.toLowerCase().includes(k))
    const isPeriodeQuery = periodeKeywords.some(k => message.toLowerCase().includes(k)) && !hasPeriodeSpecifique
    const kwPositionHint = isKwPositionQuery
      ? `\n\n[INSTRUCTION SYSTÈME : L'utilisateur pose une question sur le positionnement d'un mot-clé ou d'une requête spécifique. WORKFLOW :
1. fetch_gsc_data(type="queries", rowLimit=500) pour voir toutes les requêtes réelles du site
2. Filtrer les requêtes qui correspondent au sujet mentionné
3. Donner la position réelle, le CTR, les impressions, l'évolution si deux périodes disponibles
4. INTERDIT de dire "je n'ai pas ces données" sans avoir fait le fetch d'abord.]`
      : ''

    const periodeHint = isPeriodeQuery && gscConnected
      ? `\n\n[INSTRUCTION SYSTÈME PRIORITAIRE : Demande de comparaison de périodes. WORKFLOW OBLIGATOIRE — lancer immédiatement sans demander de confirmation :
(1) fetch_gsc_data(type="pages", rowLimit=500, startDate=J-28, endDate=J-1)
(2) fetch_gsc_data(type="pages", rowLimit=500, startDate=J-56, endDate=J-29)
(3) Comparer les deux périodes et produire l'analyse + plan RICE.
INTERDIT de demander quelle période. INTERDIT d'afficher des boutons. Lancer directement.]`
      : ''

    const contents = [
      ...history.filter((m: any) => m.content).map((m: any) => ({
        role: m.role === 'assistant' ? 'model' : 'user',
        parts: [{ text: m.content }]
      })),
      { role: 'user', parts: [{ text: message + trafficHint + auditHint + strategieHint + briefHint + maillageHint + kwpHint + positionLossHint + kwPositionHint + skillGscHint + lastVisitHint + periodeHint }] }
    ]

    const encoder = new TextEncoder()
    const stream = new ReadableStream({
      async start(controller) {
        const send = (payload: object) => {
          controller.enqueue(encoder.encode(`data: ${JSON.stringify(payload)}\n\n`))
        }

        const THINKING_LABELS: Record<string, string> = {
          load_project_context: 'Chargement du contexte projet...',
          load_skill: 'Chargement du skill...',
          fetch_serp: 'Analyse du SERP Google...',
          fetch_page_content: 'Scraping de la page...',
          update_project_memory: 'Mémorisation des insights...',
          fetch_gsc_data: 'Récupération des données GSC...',
          fetch_pagespeed: 'Analyse PageSpeed...',
          parse_keyword_planner: 'Import Keyword Planner...',
        }

        // Passe 1 — Flash sélectionne skills + outils en parallèle
        send({ thinking: 'Sélection des ressources...' })

        const [selectedSkillNames, dynamicToolsRaw] = await Promise.allSettled([
          retrieveRelevantSkills(message, supabase, GEMINI_KEY!),
          loadRelevantTools(message, supabase, GEMINI_KEY!, user_id)
        ]).then(([s, t]) => [
          s.status === 'fulfilled' ? s.value : [],
          t.status === 'fulfilled' ? t.value : []
        ])

        // Si CSV KWP fourni → forcer parse_keyword_planner dans les outils
        let dynamicTools = dynamicToolsRaw as any[]

        // Toujours injecter fetch_page_meta si pas déjà dans les outils DB
        const hasMetaTool = dynamicTools.some((t: any) => t.name === 'fetch_page_meta')
        if (!hasMetaTool) {
          dynamicTools = [...dynamicTools, {
            name: 'fetch_page_meta',
            description: "Récupère et analyse toutes les balises SEO d'une URL : title (longueur + statut), meta description (longueur + statut), H1, canonical, robots, Open Graph, Schema.org. Utiliser quand l'utilisateur veut auditer ou optimiser ses balises title/meta.",
            parameters: {
              type: 'object',
              properties: {
                url: { type: 'string', description: "URL complète de la page à analyser (ex: https://monsite.fr/ma-page)" }
              },
              required: ['url']
            }
          }]
        }

        if (kwpCsvAutoInject) {
          const hasKwpTool = dynamicTools.some((t: any) => t.name === 'parse_keyword_planner')
          if (!hasKwpTool) {
            dynamicTools = [...dynamicTools, {
              name: 'parse_keyword_planner',
              description: 'Parse le CSV Google Keyword Planner fourni et retourne le tableau volume/CPC',
              parameters: { type: 'object', properties: { csv_text: { type: 'string' }, keywords_context: { type: 'string' } }, required: [] }
            }]
          }
        }

        // Charger les prompts des skills sélectionnés
        let behaviorRules = ''
        if (selectedSkillNames.length > 0) {
          try {
            const { data: skillRows } = await supabase
              .from('skills')
              .select('name, prompt')
              .in('name', selectedSkillNames)
              .eq('active', true)
            if (skillRows && skillRows.length > 0) {
              behaviorRules = '\n\n## Règles actives pour cette conversation\n' +
                skillRows.map((s: any) => s.prompt).join('\n\n---\n\n')
            }
          } catch {}
        }

        const totalLoaded = selectedSkillNames.length + dynamicTools.length
        send({ thinking: `Flash · ${totalLoaded} ressource(s) chargée(s)` })

        // ── Model router ──────────────────────────────────────────────────
        const PRO_SKILLS = [
          'brief_contenu', 'strategie_seo', 'audit_gsc',
          'faq_strategique', 'structure_hn', 'mots_cles_decisionnels', 'content_gaps'
        ]
        const useProModel = selectedSkillNames.some((s: string) => PRO_SKILLS.includes(s))
        if (useProModel) {
          currentModel = 'gemini-2.5-pro'
          GEMINI_URL = `${GEMINI_BASE}/${currentModel}:generateContent?key=${GEMINI_KEY}`
        }

        // ── Generation config par modèle ─────────────────────────────────
        // 2.5-flash : thinking désactivé (thinkingBudget=0) → tout maxOutputTokens disponible pour la sortie
        // 2.5-pro   : thinking obligatoire (min 128) → augmenter maxOutputTokens pour absorber thinking + output
        // Sans ces réglages, l'audit truncate à mi-phrase et quick_win retourne vide
        const genConfig = useProModel
          ? { temperature: 0.7, maxOutputTokens: 16384, thinkingConfig: { thinkingBudget: 2048 } }
          : { temperature: 0.7, maxOutputTokens: 8192,  thinkingConfig: { thinkingBudget: 0 } }

        let finalResponse = ''
        let iteration = 0
        let memoryWasUpdated = false

        while (iteration < 10) {
          iteration++

          let resp: Response

          // ── Gemini — exécute les tool calls (fetch GSC, load_skill, etc.) ─
          const geminiTimeout = new AbortController()
          const geminiTimer = setTimeout(() => geminiTimeout.abort(), 55000)
          try {
            resp = await fetch(GEMINI_URL, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              signal: geminiTimeout.signal,
              body: JSON.stringify({
                system_instruction: { parts: [{ text: BASE_SYSTEM_PROMPT + contextNoteFinal + behaviorRules }] },
                contents,
                tools: [{ function_declarations: [...CORE_TOOLS, ...dynamicTools.filter((t: any) => !CORE_TOOLS.some(c => c.name === t.name))] }],
                // tool_config removed — mode AUTO by default
                generationConfig: genConfig
              })
            })
          } finally {
            clearTimeout(geminiTimer)
          }

          const data = await resp.json()
          const parts = data.candidates?.[0]?.content?.parts || []
          const toolCalls = parts.filter((p: any) => p.functionCall)
          const textParts = parts.filter((p: any) => p.text)

          if (toolCalls.length === 0) {
            // ── All tools done — route final generation to Claude or Pro if needed ──
            finalResponse = textParts.map((p: any) => p.text).join('')
            send({ token: finalResponse })

            break
          }

          const toolResults = []
          for (const part of toolCalls) {
            const { name, args } = part.functionCall
            let result
            const t0_tool = Date.now()

            // Send thinking event BEFORE executing tool
            let thinkingLabel = THINKING_LABELS[name] || `${name}...`
            if (name === 'load_skill' && args.skill_name) {
              thinkingLabel = `Chargement du skill "${args.skill_name}"...`
            }
            if (name === 'fetch_gsc_data' && args.type) {
              const typeLabel: Record<string, string> = { queries: 'mots-clés', pages: 'pages', queries_pages: 'pages & requêtes' }
              thinkingLabel = `Récupération GSC — ${typeLabel[args.type] || args.type}...`
            }
            if (name === 'fetch_page_meta') {
              try { const _umeta = new URL(args.url || 'https://x'); thinkingLabel = 'Analyse des balises SEO — ' + _umeta.pathname + '...' } catch { thinkingLabel = 'Analyse des balises SEO...' }
            }
            if (name === 'fetch_pagespeed') {
              thinkingLabel = `PageSpeed — ${args.strategy || 'mobile'} — ${args.url?.replace(/^https?:\/\/[^/]+/, '') || ''}...`
            }
            send({ thinking: thinkingLabel })

            try {
              if (name === 'load_project_context') {
                result = await loadProjectContext(user_id, domain, supabase)
                // Inject recent optimization history into context
                const optHistory = await checkOptimizationHistory(supabase, user_id, domain, null)
                if (optHistory) result.optimization_history = optHistory

                // Étape 5 — injecter agent_guidelines dans behaviorRules
                const guidelines = result.agentGuidelines || DEFAULT_AGENT_GUIDELINES
                const guidelinesBlock = '\n\n## Guidelines agent (projet)\n' +
                  '### Routing\n' + guidelines.routing +
                  '\n### Format\n' + guidelines.format +
                  '\n### Interdit\n' + guidelines.forbidden

                // Ajouter seulement si pas déjà présent
                if (!behaviorRules.includes('## Guidelines agent')) {
                  behaviorRules += guidelinesBlock
                }

                // Sauvegarder les defaults en DB si la clé est absente
                if (!result.agentGuidelines) {
                  await supabase.from('project_memory').upsert(
                    { user_id, domain, key: 'agent_guidelines', value: DEFAULT_AGENT_GUIDELINES, updated_at: new Date().toISOString() },
                    { onConflict: 'user_id,domain,key' }
                  )
                  log('agent/guidelines', 'defaults_saved', { user_id, domain })
                }

              } else if (name === 'load_skill') {
                result = await loadSkill(args, user_id, domain, supabase)
              } else if (name === 'fetch_serp') {
                result = await fetchSerp(args, supabase)
              } else if (name === 'fetch_page_meta') {
                result = await fetchPageMeta(args.url)
              } else if (name === 'fetch_page_content') {
                result = await fetchPageContent(args.url, args.extract || 'full')
              } else if (name === 'score_content') {
                result = await scoreContent(args, user_id, domain)
              } else if (name === 'update_project_memory') {
                result = await updateProjectMemory(args, user_id, domain, supabase)
                if (result.success) memoryWasUpdated = true
              } else if (name === 'fetch_gsc_data') {
                result = await fetchGSCData(args, user_id, supabase, gscSite, domain)
              } else if (name === 'parse_keyword_planner') {
                // Auto-inject si CSV droppé depuis le frontend
                const csvText = kwpCsvAutoInject || args.csv_text
                if (csvText && csvText.length > 50) {
                  const parsed = parseKeywordPlannerCSV(csvText)
                  result = {
                    success: parsed.success,
                    formatted: formatKeywordPlannerResults(parsed),
                    keywords: parsed.keywords,
                    raw_count: parsed.raw_count,
                    error: parsed.error,
                  }
                } else {
                  result = { success: false, guide: KEYWORD_PLANNER_GUIDE(args.keywords_context) }
                }
              } else if (name === 'fetch_pagespeed') {
                result = await fetchPagespeed(args.url, args.strategy || 'mobile')
                if (result && !result.error) {
                  send({ pagespeed_result: result })
                }
              } else {
                result = { error: `Outil inconnu: ${name}` }
              }

              // Log succès ou erreur applicative (pas d'exception mais result.error)
              if (result?.error) {
                const errMsg = String(result.error)
                log('connector/' + name, 'fetch', { project_id: domain, status: 'error', error: errMsg, duration_ms: Date.now() - t0_tool })
                // Lazy health check — marquer l'outil en erreur si token OAuth révoqué
                if (errMsg.includes('401') || errMsg.includes('403') || errMsg.toLowerCase().includes('token')) {
                  await markToolError(supabase, name, errMsg)
                }
              } else {
                log('connector/' + name, 'fetch', { project_id: domain, status: 'success', duration_ms: Date.now() - t0_tool })
              }
            } catch (err: any) {
              const errMsg = err.message || String(err)
              result = { error: errMsg }
              log('connector/' + name, 'fetch', { project_id: domain, status: 'error', error: errMsg, duration_ms: Date.now() - t0_tool })
              if (errMsg.includes('401') || errMsg.includes('403')) {
                await markToolError(supabase, name, 'Token OAuth expiré ou révoqué')
              }
            }

            toolResults.push({ functionResponse: { name, response: { result } } })
          }

          contents.push({ role: 'model', parts })
          contents.push({ role: 'user', parts: toolResults })
        }

        // Clear Pro timeout si réponse reçue à temps
        if ((globalThis as any)._proTimeout) { clearTimeout((globalThis as any)._proTimeout); delete (globalThis as any)._proTimeout }
        if (!finalResponse) {
          // Retry without tools to force a text response
          try {
            const retryResp = await fetch(GEMINI_URL, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                system_instruction: { parts: [{ text: BASE_SYSTEM_PROMPT + contextNoteFinal + behaviorRules }] },
                contents,
                generationConfig: genConfig
              })
            })
            const retryData = await retryResp.json()
            const retryText = retryData.candidates?.[0]?.content?.parts?.filter((p: any) => p.text).map((p: any) => p.text).join('')
            if (retryText) {
              finalResponse = retryText
              send({ token: finalResponse })
            }
          } catch {}
          if (!finalResponse) finalResponse = "Je n'ai pas pu generer de reponse. Reformule ta demande."
        }
// Si l'utilisateur dit 'oui' ou répond avec un seul mot après une question, relancer avec les données GSC par défaut

        // Log optimizations from final response
        try {
          const lines = finalResponse.split('\n')
          for (const line of lines) {
            const l = line.toLowerCase()
            if ((l.includes('réécrire') || l.includes('optimiser') || l.includes('modifier') ||
                 l.includes('ajouter') || l.includes('title') || l.includes('meta') ||
                 l.includes('fusionner') || l.includes('mettre à jour')) &&
                line.length > 30 && line.length < 300) {
              const urlMatch = line.match(/https?:\/\/[^\\s)]+|\/[a-z0-9\-\/]+/)
              const url = urlMatch ? urlMatch[0] : null
              let type = 'other'
              if (l.includes('title') || l.includes('h1')) type = 'title'
              else if (l.includes('meta') || l.includes('description')) type = 'meta'
              else if (l.includes('contenu') || l.includes('rédiger')) type = 'contenu'
              else if (l.includes('lcp') || l.includes('cls') || l.includes('cwv')) type = 'cwv'
              else if (l.includes('lien') || l.includes('maillage')) type = 'maillage'
              else if (l.includes('h2') || l.includes('h3') || l.includes('structure')) type = 'structure_hn'
              else if (l.includes('quick win') || l.includes('position')) type = 'quick_win'
              await logOptimization(supabase, user_id, domain, url, line.replace(/^[•\-*#\\s]+/, '').trim(), type, finalResponse.slice(0, 200))
            }
          }
        } catch {}

        // Stream final response word by word
        send({ thinking: null }) // clear thinking
        const words = finalResponse.split(' ')
        for (let i = 0; i < words.length; i++) {
          const chunk = (i === 0 ? '' : ' ') + words[i]
          send({ text: chunk })
          await new Promise(r => setTimeout(r, 30))
        }
        if (memoryWasUpdated) {
          send({ memory_updated: true })
        }
        log('agent/request', 'complete', { user_id, domain, status: 'success', duration_ms: Date.now() - t0_request })
        send({ done: true })
        controller.close()
      }
    })

    return new Response(stream, {
      headers: { ...corsHeaders, 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache' }
    })

  } catch (err) {
    return new Response(
      `data: ${JSON.stringify({ text: `Erreur: ${err.message}` })}\n\ndata: [DONE]\n\n`,
      { headers: { ...corsHeaders, 'Content-Type': 'text/event-stream' } }
    )
  }
})
