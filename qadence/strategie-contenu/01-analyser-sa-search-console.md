---
type: contenu
format: guide
projet: qadence
cluster: 1
statut: produit
requete_cible: comment analyser sa Search Console
intention: Know → Do
capacite_qadence: Jade (audit GSC 28j) · audit_gsc · analyse_gsc_complete · quick_win
schema: HowTo + Article
created: 2026-06-18
updated: 2026-06-18
regles: GEO (answer-first, pyramide inversée, extractable) · ultra factuel · zéro narratif · zéro pattern « X, pas Y »
sources_vault: [[mots-cles-actionnels]], [[triade-serp]], [[methode-organikk-4-piliers]], [[answer-first-pattern]], [[know-simple-know-do]], [[test-substitution-llm]]
---

# Comment analyser sa Search Console

Analyser sa Search Console se fait en cinq étapes : cadrer la période (28 derniers jours), lire trois rapports dans l'ordre (vue d'ensemble, pages, requêtes), prioriser les requêtes actionnelles, sortir les gains rapides (positions 3 à 15), puis écrire un plan d'action priorisé. Règle constante : chaque chiffre vient de la Search Console réelle, jamais d'une estimation.

## Sur quelle période analyser

Analyse les 28 derniers jours, ou la plage J-32 à J-4. Compare toujours à la période précédente de même durée.

- Les 3 à 4 derniers jours sont incomplets côté Google : les inclure crée une fausse chute en fin de courbe.
- Un chiffre comparé à la période précédente vaut une décision. Un chiffre isolé, non.
- Variation sur 3-4 jours = bruit, aucune action. Baisse régulière sur plusieurs semaines = signal à traiter.

## Quels rapports lire, et dans quel ordre

Trois rapports, du global au détail :

1. **Vue d'ensemble** : clics, impressions, CTR, position moyenne. Tendance générale.
2. **Pages** : quelles URL portent les impressions, lesquelles montent, lesquelles décrochent.
3. **Requêtes** : sur quoi le site sort, et avec quelle intention.

L'ordre est imposé : partir des requêtes d'abord noie l'analyse dans des milliers de lignes sans hiérarchie.

## Comment prioriser les requêtes

Trie par intention business. Le volume n'est plus un critère de choix pertinent : les requêtes informationnelles larges sont traitées par ChatGPT, Perplexity et les AI Overviews sans clic vers le site.

Priorité aux **mots-clés actionnels** : ceux où l'utilisateur attend une action (devis, démo, contact, achat). Test de qualification en deux questions :

1. ChatGPT répond-il déjà correctement à cette requête ?
2. Si oui, fait-il mieux que ta page ?

Deux "oui" = page sans potentiel, on l'abandonne. Un "non" (besoin de ta donnée, ton stock, ton prix, ton intervention) = page à fort potentiel.

Ordre de priorité : décisionnel, puis transactionnel, puis informationnel (souvent à ignorer).

## Comment sortir les gains rapides

Les gains rapides sont les pages déjà en position 3 à 15 dont le CTR est sous le repère attendu. On optimise l'existant avant de créer.

Méthode :

1. Filtrer les pages en position 3 à 15.
2. Exclure les requêtes de marque et la page d'accueil.
3. Trier par impressions décroissantes.
4. Comparer le CTR réel au CTR attendu pour la position.

Repères de CTR attendu :

| Position | CTR attendu |
|---|---|
| 4 | ~7 % |
| 5 | ~5 % |
| 6 à 10 | 2 à 3 % |

CTR réel nettement sous le repère sur une requête actionnelle = gain rapide. Leviers, dans l'ordre : title, meta description, H1, FAQ en haut de page, densification atomique (ajout au passage classé de la preuve ou du chiffre manquant). Aucune nouvelle page tant que les gains rapides sur l'existant ne sont pas épuisés.

## Quoi détecter en plus

Quatre points à passer au crible au-delà des gains rapides :

- **Chutes de position** : page qui glisse sur une requête qui compte. Vérifier l'alignement du contenu avec l'intention actuelle.
- **Déindexation** : pages sans aucune impression, sorties de l'index. Urgence technique.
- **Cannibalisation** : deux pages qui se partagent les impressions sur une même requête. Désigner la page porteuse, faire fusionner ou soutenir l'autre.
- **Impressions sous-exploitées** : forte visibilité, aucun clic. Décalage entre l'attente de la requête et la page.

Règle anti-erreur : ne jamais conclure à un zéro sans vérifier. Zéro clic = soit zéro impression (problème de visibilité), soit vue sans clic (problème de promesse). Décisions opposées.

## Comment finir l'analyse

Sortie obligatoire : un plan d'action priorisé, pas un export. Pour chaque opportunité retenue, noter trois éléments :

- la page concernée,
- le levier exact (title, FAQ, preuve à ajouter),
- le résultat attendu.

Trier par effort contre impact. Attaquer en premier le plus faible effort pour le plus fort impact sur des requêtes qui convertissent. Lire les rapports et calculer les écarts est de la commodité automatisable ; la valeur est dans le choix des pages à traiter et de leur ordre.

## Lancer l'audit automatiquement

Jade, l'agent audit Search Console de Qadence, exécute ces cinq étapes sur les 28 derniers jours de ta propriété : pages en recul, gains rapides triés par intention, cannibalisation, opportunités, rendus en plan d'action. Aucun chiffre inventé : donnée absente = signalée. La décision finale par page reste à toi.

→ **Lancer mon audit Search Console** sur qadence.io/app
