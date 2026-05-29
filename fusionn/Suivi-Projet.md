# Suivi projet — Fusionn

Document de suivi de l'état du projet Fusionn. Pour le détail chronologique des sessions, voir [[Historique]].

Repo actif : `~/Code/newFusionn`. Dernière mise à jour : 2026-05-26.

---

## État au 2026-05-26

**Diagnostic global et plan d'action 90 jours : voir [[Diagnostic-plan-action-2026-05-26]].**

MRR 696 € · ARR 8 352 € · MAU 8 % · acquisition à l'arrêt (0 inscrit sur 7j). Trois fuites distinctes identifiées : top-funnel + activation (46 % s'inscrivent sans chercher) + rétention (23 % testent une fois et partent). Priorité immédiate : casser la fuite d'activation avant tout (email J+1, tour produit forcé, décongelation Brief synthèse).

Côté UI/UX, livraisons de cette session :
- Nouvel onglet **Brief synthèse** en tête de la nav Stratégie (modèle Organikk repris pour la structure de contenu, DA Fusionn pour la mise en page).
- Refonte **Stratégie pSEO** : header sobre, KPI strip, timeline 3 phases avec narrative parsé par phase, accordéons playbooks lisibles, tables zebra.
- Suppression FAB "Tout télécharger" en bas à droite.
- Accents FR forcés dans 6 edge functions Gemini (`generate-brief`, `generate-hn-structure`, `generate-vecteurs`, `generate-micro-intentions`, `generate-faq`, `generate-objections`).
- Bouton "Copier le brief" passé en bleu Google. Bouton "Exporter Google Docs" temporairement retiré côté UI (edge function `export-to-gdocs` déployée mais renvoie 2xx-error à déboguer).
- Création compte manuel `contact@ameline-calendrier.fr` + edge function `admin-recover-user` pour automatiser le geste à l'avenir.
- Accroche écran d'accueil : "Tim, sur quel mot-clé veux-tu travailler ?" (remplace "analysons-nous ?").

---

## État au 2026-05-22

**En prod (`fusionn.co`)**
- Balise de vérification Google Search Console à jour.
- Analytics datafa.st pointant sur le bon domaine.
- Build `main` réparé : la prod était gelée depuis le 2026-05-21 à cause d'un build cassé, c'est résolu.

**Prêt mais pas encore en prod**
- Feature « Onglets YouTube et Reddit » : tout le code est sur la branche `feat/youtube-reddit-tabs`, le backend est entièrement déployé (Edge Functions + tables). Il reste à tester en conditions réelles dans l'app, puis à merger dans `main`.

---

## Livré cette session (2026-05-22)

### 1. Search Console + analytics

- Balise `google-site-verification` remplacée dans `index.html` (ancienne valeur obsolète).
- Script datafa.st : `data-domain` corrigé de `foccus.io` vers `fusionn.co`.
- Commits `502ea50` puis `dfc4580` sur `main`, en ligne.
- À vérifier côté Tim : le `data-website-id` datafa.st pointe peut-être encore vers une propriété foccus.io.

### 2. Réparation du build `main`

- Le build de `main` échouait depuis le commit `c55f31b` : `useConversationalAnalysis.ts` importait `getSelectedGscProperty` sans que la fonction soit exportée sur `main` (elle n'existait que sur la branche `feat/gsc-usage-ab`).
- Conséquence : chaque déploiement Netlify échouait, prod gelée sur la version du 2026-05-21 13:53.
- Corrigé par `dfc4580` : ajout du helper sur `main`.

### 3. Feature : onglets Mots-clés YouTube et Reddit

Deux nouveaux onglets dans le workspace (nouvelle section de nav « Découvrir »), générés automatiquement à chaque recherche.

- **YouTube** : Edge Function `generate-youtube-keywords` qui appelle YouTube Data API v3 (`search.list` + `videos.list`) pour les vraies vidéos qui rankent, puis Gemini pour clusteriser les mots-clés. Validé en test réel : 42 mots-clés, vraies vues.
- **Reddit** : le navigateur de l'utilisateur récupère les posts Reddit (l'API JSON publique bloque les IP datacenter des Edge Functions, pas les IP résidentielles), puis l'Edge Function `generate-reddit-keywords` fait le clustering Gemini. Aucun compte ni app Reddit nécessaire.
- **Anti-hallucination** : Gemini ne produit aucun chiffre. Il référence vidéos et posts par id, le serveur joint la donnée réelle (vues, upvotes, commentaires). Conforme à la doctrine.
- 2 tables `search_youtube_keywords_results` / `search_reddit_keywords_results`, migration `20260522120000` appliquée. Cache 30 jours.
- Export CSV et rechargement d'historique inclus.
- Branche `feat/youtube-reddit-tabs`, commits `ee62892` → `3b182a0`.

---

## Infra et accès (référence)

- **Hébergement** : `fusionn.co` sur **Netlify** (site `fusionn2`, id `a50cfaba-84fb-403f-a12f-d9479406d032`), auto-deploy depuis la branche `main`. Pas AWS.
- **Supabase** : projet `fwhfnzbtlddzfxbsejyf` (région eu-west-1).
- **Secrets Edge Functions** posés : `GEMINI_API_KEY`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `YOUTUBE_API_KEY`.
- **Google Cloud** : projet `309434449968`. YouTube Data API v3 activée.
- **Branches** : `main` (prod), `feat/youtube-reddit-tabs` (feature en attente de merge), `feat/gsc-usage-ab` (feature GSC non mergée).
- **Modèle IA** : `gemini-3-pro-preview` pour toutes les fonctions de génération (choix de Tim, pas de bascule vers Flash).

---

## Points d'attention

- **Reste à faire** : tester la feature YouTube/Reddit dans l'app, puis merger `feat/youtube-reddit-tabs` dans `main`.
- **CORS Reddit** : le fetch Reddit côté navigateur n'a pas pu être vérifié hors app. À confirmer au premier test réel. Plan B si échec : un proxy.
- **Quota YouTube** : 10 000 unités/jour, une recherche coûte ~101 unités, soit environ 100 recherches distinctes par jour tous utilisateurs confondus. Le cache amortit. Demander une augmentation à Google si ça contraint.
- **Branche `feat/gsc-usage-ab` non mergée** : contient la feature GSC (front + Edge Functions + migration) et le retry Gemini sur les 12 autres fonctions. À livrer un jour, en déployant front ET backend ensemble.
- **`_shared/gemini.ts`** : le helper de retry n'existe pas sur `main`. Les fonctions YouTube/Reddit appellent Gemini en direct avec un retry inline.
