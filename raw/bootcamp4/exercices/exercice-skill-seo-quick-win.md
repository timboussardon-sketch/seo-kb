---
title: "Exercice — seo-quick-win : tes 10 gains rapides"
bootcamp: 4
type: exercice
session: 3
skill: seo-quick-win
cowork: oui
created: 2026-06-09
---

# Exercice — seo-quick-win : tes 10 gains rapides

**Niveau** : débutant · **Pré-requis** : le skill `seo-quick-win` installé, un export GSC de ton client.

## Le cas

Ton client a déjà des pages positionnées dans Google, mais elles ne reçoivent pas les clics qu'elles méritent : bonne position, mauvais taux de clic. On va les repérer et les prioriser, sans créer une seule page nouvelle. C'est le gain le plus rapide du SEO.

## Ce que tu dois faire

**1. Exporte ta Search Console.**
Va sur Google Search Console → **Performances** → onglet **Requêtes**, période **6 mois**, puis bouton **Exporter** → CSV. Refais-le sur l'onglet **Pages**. Tu obtiens deux fichiers.

**2. Lance le skill sur ton export.**
Dans Claude, dépose le CSV et colle :

```text
Lance seo-quick-win sur cet export GSC. Sors-moi le top 10 des quick wins,
triés par impact estimé (delta CTR x impressions), avec pour chaque ligne
une reco de title/meta basée sur la vraie requête.
```

**3. Lis le tableau et garde le top 5.**
Tu n'attaques pas 30 pages. Tu prends les 5 premières par impact et tu réécris leur title/meta cette semaine.

## Ce que tu dois obtenir   ← le « screen »

Un tableau de ce type (exemple sur un site fictif) :

```
QUICK WINS — export GSC (6 mois)

| Page                    | Requête            | Pos | Impr.  | CTR   | CTR attendu | Gain estimé |
|-------------------------|--------------------|-----|--------|-------|-------------|-------------|
| /logiciel-facturation/  | logiciel facture   | 6,2 | 18 400 | 1,1%  | ~6%         | +900 clics  |
| /devis-auto/            | faire un devis     | 4,8 | 9 100  | 2,3%  | ~9%         | +610 clics  |
| /integrations/sage/     | sage facturation   | 7,1 | 6 800  | 0,9%  | ~5%         | +280 clics  |
| ...                     | ...                | ... | ...    | ...   | ...         | ...         |

Top 5 à attaquer cette semaine : réécriture title + meta description.
```

## Vérifier que tu as réussi

- [ ] Tu as un top 5 à 10 trié par impact, pas par volume brut.
- [ ] Chaque ligne pointe une vraie requête de ta GSC, pas une requête inventée.
- [ ] Aucune page en position 1-2 (déjà gagnée) ni au-delà de 20 (trop loin pour un quick win).
- [ ] Chaque ligne a une reco de title/meta concrète.

## Le piège

Confondre « grosses impressions » et « quick win ». Une page à 100 000 impressions en position 30 n'est pas un quick win : elle est trop loin. Le gain est dans l'écart **position 3-12 + CTR faible**. C'est là qu'un meilleur title transforme des impressions déjà acquises en clics, tout de suite.

## Comment ça marche

Le skill croise, requête par requête, la position et le taux de clic de ta GSC. Il repère les pages « à portée » (déjà dans le haut de page mais sous-cliquées) et estime le gain si le CTR rejoignait la moyenne de sa position. Tu ne crées rien : tu débloques ce qui est déjà presque gagné.

## Version WhatsApp

> Exo quick-win : exporte ta GSC (Performances → Requêtes + Pages, 6 mois, CSV). Dépose les 2 fichiers dans Claude et dis « lance seo-quick-win, top 10 trié par impact avec reco title/meta ». Tu gardes le top 5 et tu réécris leurs titles cette semaine. Piège : un quick win c'est position 3-12 + CTR faible, pas juste du gros volume. 💪
