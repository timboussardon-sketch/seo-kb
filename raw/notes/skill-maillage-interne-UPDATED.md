# Skill : Maillage Interne — LinkMap AI

## Philosophie (méthode Boussardon)

Le maillage interne est la puissance SEO. Pas de backlinks achetés, mais un cocon sémantique solide construit autour de mots-clés business.

Principes :
- Page mère = au moins 10 citations depuis pages filles/petites-filles
- Le maillage part de la stratégie de mots-clés — le cocon est la conséquence
- Priorité : transactionnel > décisionnel > informationnel
- On ne lie pas parce que les pages parlent de la même chose — on lie pour faire avancer l'utilisateur dans sa tâche (Task-Based Linking)
- Le maillage sémantique (même thème) et le maillage intentionnel (Know → Do) coexistent

---

## WORKFLOW OBLIGATOIRE — exécuter dans cet ordre exact

### Étape 1 — Matrice de proximité (données GSC)

Tu as DÉJÀ les données de fetch_gsc_data(type="queries_pages") dans le contexte. Utilise-les.

1. Construire la matrice : pour chaque page, lister ses mots-clés GSC
2. Identifier les PAIRES de pages qui partagent des mots-clés communs
3. Scorer chaque paire : nombre de mots-clés partagés × impressions combinées = score de proximité
4. Les paires avec le score le plus élevé SANS lien entre elles = opportunités prioritaires

### Étape 2 — Classification des pages par intention

Classifier chaque page du top 50 (par clics) :

| Type | Signal GSC | Exemples |
|------|-----------|----------|
| Know | Requêtes "comment", "pourquoi", "qu'est-ce que", "guide" | Blog, guide, définition |
| Do | Requêtes transactionnelles, prix, devis, réservation | Page produit, service, outil |
| Know+Do | Requêtes comparatives, "meilleur", "vs", "avis" | Comparatif, landing page |

### Étape 3 — Détecter les liens manquants

Pour les 5 paires de pages avec le score de proximité le plus élevé :
- Vérifier via fetch_page_content si un lien <a href="..."> existe entre les deux pages
- Si pas de lien → LIEN MANQUANT = suggestion prioritaire
- L'ancre recommandée = le mot-clé partagé avec le plus d'impressions

### Étape 4 — Construire la hiérarchie cocon

Grouper les pages par cluster (mots-clés partagés) :
- Page mère = celle avec le plus de clics sur le head term du cluster
- Pages filles = pages qui rankent sur des variantes longue traîne
- Pages petites-filles = pages ultra-nichées liées au même cluster

Règles de maillage du cocon :
- Pages mères liées entre elles (maillage horizontal niveau 0)
- Chaque page fille cite sa page mère + 1-2 pages sœurs
- Chaque petite-fille cite sa page fille + sa page mère (lien profond)
- Ancres = requête exacte ou variante proche (jamais "cliquez ici" ou "en savoir plus")

### Étape 5 — Détecter les ponts Know → Do manquants

Chaque page Know DOIT avoir au moins 1 lien vers une page Do thématiquement reliée.
Lister les pages Know sans lien vers un Do = opportunités de conversion manquées.

---

## FORMAT DE SORTIE OBLIGATOIRE

### Bloc 1 — Liens manquants haute priorité

Pour chaque lien manquant (max 10) :

```
🔴 [Page source] → [Page destination]
   Type : sémantique | intentionnel (Know→Do)
   Ancre suggérée : "[mot-clé partagé]"
   Raison : X mots-clés partagés, Y impressions combinées
   Où insérer : dans la section [H2 le plus pertinent de la page source]
```

### Bloc 2 — Pages sous-maillées

Pages avec impressions élevées mais peu/pas de connexions détectées vers d'autres pages du site.
Ce sont les pages orphelines fonctionnelles (GSC les voit mais aucune autre page ne les renforce).

### Bloc 3 — Hiérarchie cocon

```
Page Mère : /[url] (head term, X clics)
├── /[url-fille-1] (fille) — requête : "..."
│   └── /[url-petite-fille] (petite-fille) — requête : "..."
├── /[url-fille-2] (fille) — requête : "..."
└── /[url-fille-3] (fille) — requête : "..."
```

### Bloc 4 — Ponts Know → Do manquants

| Page Know (source) | Page Do (destination) | Ancre recommandée | Priorité |
|--------------------|-----------------------|-------------------|----------|
| /guide-... | /service-... | "..." | HAUTE |

### Bloc 5 — Score de maillage par cluster

| Cluster | Pages | Liens existants | Liens manquants | Score /10 |
|---------|-------|-----------------|-----------------|-----------|
| [thème] | X | Y | Z | W |

Score = (liens existants / liens théoriques nécessaires) × 10

---

## Points de vigilance

- Ne pas automatiser à 100% : le maillage part de la stratégie. Les suggestions sont des insights, pas des ordres
- Cannibalisation : si 2 pages répondent à la même intention, signaler AVANT de mailler — consolider d'abord
- Ancres variées : ne pas répéter la même ancre exacte partout
- Prioriser les pages business : une landing transactionnelle > un blog informatif
- Si fetch_page_content retourne une structure vide (site JS/SPA) : le signaler et baser les suggestions uniquement sur la proximité GSC

## Rappels méthode

"Le maillage interne, c'est la puissance. Et ça part de tes mots-clés."
"Une page mère doit avoir au moins 10 citations."
"La Search Console a toutes les données — elle est juste mal visualisée."
"On ne lie pas des pages parce qu'elles parlent de la même chose — on les lie pour faire avancer l'utilisateur dans sa tâche."
