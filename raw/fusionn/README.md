---
type: project-source
slug: fusionn
title: "Fusionn — outil SEO conversationnel (React + Supabase Edge)"
source_repo: "/Users/timothee/Code/newFusionn"
runtime: "React (Vite) + Supabase Edge Functions (Deno)"
date_added: 2026-05-21
language: typescript
---

# Fusionn — dossier raw

Notes techniques sur **Fusionn**, l'outil SEO conversationnel de Tim : à partir d'un mot-clé, il génère mots-clés sémantiques, FAQ, micro-intentions, structure Hn, brief, vecteurs, etc. Repo actif : `/Users/timothee/Code/newFusionn` (à ne pas confondre avec la vieille copie Bolt dans `Downloads/`). Voir aussi [[qadence-seo-agent]], l'autre agent SEO.

Ce dossier capture les **décisions et correctifs techniques structurants** — pas le code, qui vit dans le repo.

## Sous-docs

- [[2026-05-21-fix-premium-front-serveur]] — la modale « choisir un plan » s'affichait à la place des résultats, **même en premium**. Désynchronisation front ↔ serveur sur la détection d'abonnement.

## Architecture premium (résumé)

Deux endroits calculent le statut premium, et ils **doivent rester identiques** :

- **Front** — `src/contexts/AuthContext.tsx` → `validateSubscription()` produit `isPremium`.
- **Serveur** — les edge functions `check-rate-limit`, `check-semantic-score-limit`, `check-hn-score-limit` recalculent le premium côté serveur.

Règle d'or : abonnement `active`/`trialing` + `current_period_end` dans le futur = premium. Les `stripe_subscription_id` / `stripe_customer_id` **ne sont plus exigés** (clients Premium manuels issus de la migration, cf. `PREMIUM_INJECTION.md` du repo). Toute modif d'un côté se répercute sur l'autre — sinon bug. Détail dans [[2026-05-21-fix-premium-front-serveur]].
