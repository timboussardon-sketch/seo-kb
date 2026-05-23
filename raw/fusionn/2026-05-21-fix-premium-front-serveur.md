---
type: fix-log
slug: 2026-05-21-fix-premium-front-serveur
title: "Fix Fusionn — modale « choisir un plan » affichée même en premium"
parent: "[[fusionn|Fusionn]]"
date: 2026-05-21
repo: "/Users/timothee/Code/newFusionn"
status: corrigé (déploiement edge functions requis)
---

# Fix — la modale « choisir un plan » s'affichait au lieu des résultats, même en premium

## Symptôme

Au lancement de l'analyse conversationnelle, les résultats n'apparaissaient pas : la modale « choisir un plan » (`SubscriptionChoiceModal`) s'affichait à la place — **y compris pour des comptes premium**.

## Cause racine — désynchronisation front ↔ serveur

Le commit `8f86b76` (« Fix Premium détecté côté front : retire le check Stripe obligatoire ») avait assoupli la détection premium **côté front uniquement** :

- **Front** (`AuthContext.validateSubscription`) : abonnement `active`/`trialing` + `current_period_end` future = premium. Ne vérifie plus `stripe_subscription_id` ni `stripe_customer_id`.
- **Serveur** (edge functions) : exigeait toujours `hasValidPeriod && hasStripeSubscription && hasStripeCustomer`.

Conséquence pour un **premium « manuel »** (réinjecté à la migration, sans Stripe IDs) :

| | Front | Serveur `check-rate-limit` |
|---|---|---|
| Statut perçu | premium | non-premium → limite gratuite (5 analyses) |
| Après 5 analyses | illimité | `allowed: false` |

Le flux conversationnel (`useConversationalAnalysis.startAnalysis`) appelait `checkRateLimit()` **sans garde-fou `isPremium`**, contrairement à la recherche classique (`Compte.handleSubmit`) qui a déjà `if (!isPremium)`. Résultat : `allowed:false` → `onRateLimitExhausted()` → modale « choisir un plan », pas de résultats.

## Correctif — 4 fichiers

1. **`src/hooks/useConversationalAnalysis.ts`** — garde-fou `if (!isPremium)` autour de la vérification du rate limit (aligne le flux conversationnel sur `handleSubmit`).
2. **`supabase/functions/check-rate-limit/index.ts`** — suppression du check Stripe strict : période valide suffit. Cas « expiré » → tier gratuit + log `subscription_expired`.
3. **`supabase/functions/check-semantic-score-limit/index.ts`** — idem + suppression des faux logs « Suspicious premium access attempt » pour les premiums manuels légitimes ; exige désormais une période valide (avant : premium accordé même expiré).
4. **`supabase/functions/check-hn-score-limit/index.ts`** — idem.

## Règle à retenir

La validation d'abonnement doit être **identique front et serveur**. Source de vérité commune : abonnement `active`/`trialing` + `current_period_end > now`, **sans** condition sur les Stripe IDs (les renewals Stripe restent gérés par les webhooks qui matchent sur `stripe_subscription_id`). Toute modif de `AuthContext.validateSubscription` doit être répercutée sur les 3 edge functions `check-*-limit`, et inversement.

## Déploiement

Les edge functions ne prennent effet qu'après redéploiement :

```
supabase functions deploy check-rate-limit
supabase functions deploy check-semantic-score-limit
supabase functions deploy check-hn-score-limit
```
