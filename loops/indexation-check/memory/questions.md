# Questions & diffs proposes - indexation-check

LA SEULE PORTE par laquelle la boucle touche au CODE. Le brain n'edite jamais son skill tout seul :
il ecrit ici un diff propose + la raison, Tim tranche a la revue.

## En attente de decision

### [2026-07-10] Retirer le check #8 (scraping `site:`) et le remplacer par l'API URL Inspection

**Constat.** Le check #8 du skill est mort. 5 runs consecutifs (15/06, 22/06, 29/06, 06/07, 10/07) le marquent « non testable ». Mesure du 10/07 : `curl` sur `site:organikk.co` renvoie `HTTP 200`, 91 Ko, dont le seul texte visible est « Cliquez ici si, d'ici quelques secondes, vous n'avez pas ete redirige ». Une occurrence de `organikk.co` dans tout le HTML. Aucun blocage recaptcha : Google ne bloque pas, il ne sert simplement plus de SERP sans JS.

Le skill promet une fiabilite de 40 a 60 % sur ce check. La fiabilite reelle observee est de 0 % sur 5 runs.

**Diff propose.**

1. Dans la section « COUCHE B », supprimer le check #8 tel qu'ecrit (scraping `site:` + garde-fous `sleep 4` / detection recaptcha) et le remplacer par un appel a `urlInspection/index:inspect`.
2. Deplacer la section « Variante haute fiabilite - GSC URL Inspection API » du statut d'option a celui de methode par defaut.
3. Ajouter un fallback documente : si aucune connexion GSC n'existe pour le domaine, marquer les pages « statut d'indexation non mesure (pas de connexion GSC) » et ne rien scraper.
4. Ajouter un check derive, disponible des qu'une connexion GSC existe : croiser le sitemap avec `searchAnalytics dimensions=page` pour sortir (a) les pages du sitemap a zero impression, (b) **les pages servies par Google absentes du sitemap**.

**Raison du point 4.** C'est ce croisement, ajoute a la main pendant le run du 10/07, qui a trouve `/manifeste/` : une page en `HTTP 404` que Google sert encore avec 30 impressions sur 28 jours, 2e page du site en impressions. Les 4 audits precedents ne pouvaient pas la voir, puisqu'ils partaient du sitemap et que cette URL n'y figure pas. Un audit qui ne lit que le sitemap est aveugle a exactement la classe de bug la plus couteuse : la page morte que Google continue de servir.

**Cout.** Un endpoint `urlInspection` a cote de `admin-gsc-export` dans `~/Code/newFusionn/supabase/functions/`. La connexion OAuth existe deja (`google_connections`, propriete `https://organikk.co/` verifiee fonctionnelle le 10/07). Estimation ~30 min.

**Gain.** Les 97 pages « indeterminees » du run du 10/07 passent a un statut officiel (`INDEXED`, `CRAWLED_NOT_INDEXED`, `DISCOVERED_NOT_INDEXED`, `URL_IS_UNKNOWN_TO_GOOGLE`). Sans ca, on ne saura jamais si les 38 fiches wiki a zero impression sont indexees ou ignorees, et les deux appellent des actions opposees.

**Limite a garder en tete.** `searchAnalytics` mesure le service en SERP, pas l'appartenance a l'index. Il ne remplace pas `urlInspection`, il le complete. La distinction « non indexee » / « non testable » du skill reste non negociable dans les deux cas.

**Decision attendue de Tim** : oui / non sur le remplacement du check #8, et oui / non sur l'ajout du check de croisement sitemap x GSC.

### [2026-07-10] `manifest.yml` pointe vers un validator qui n'existe pas

`manifest.yml` declare `validator: ../_loop-kit/validate.sh`, ce qui resout en `loops/_loop-kit/validate.sh`. Ce chemin n'existe pas. Le kit reel est a `seo-kb/_loop-kit/validate.sh`, soit `../../_loop-kit/validate.sh` depuis `loops/indexation-check/`.

Le gate a ete passe le 10/07 en appelant le bon chemin a la main (`bash _loop-kit/validate.sh loops/indexation-check` depuis la racine du vault). Resultat `OK`.

**Diff propose** : dans `manifest.yml`, remplacer `validator: ../_loop-kit/validate.sh` par `validator: ../../_loop-kit/validate.sh`.

A verifier : les 5 autres boucles (`health`, `linkedin-journal`, `maillage-interne-gsc`, `seo-cannibalisation`, `seo-quick-win`) portent probablement la meme erreur de chemin.

## Tranche (historique)
- (rien pour l'instant)
