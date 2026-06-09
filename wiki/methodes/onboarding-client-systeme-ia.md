---
type: methode
title: "Onboarding client — système IA complet (repo dédié + pack vivant)"
aliases: [onboarding-client-systeme-ia, systeme-client-livrable, playbook-client-ia]
tags: [client, livrable, organikk, systeme-ia, pack, submodule, procedure]
created: 2026-06-09
updated: 2026-06-09
sources: 1
confidence: high
status: stable
---

# Onboarding client — système IA complet

Playbook reproductible pour livrer à un client un **système IA complet** (pas juste des livrables) tout en protégeant le moat. Premier cas : **Leexi** (2026-06-09). À rejouer à chaque nouveau client.

Évolution de [[queries/transfert-vault-client]], qui ne faisait qu'un snapshot figé. Ici le client reste sur la **dernière version** de la doctrine et des skills.

## Le principe en une phrase

On donne au client la méthode et les skills (c'est ce qu'il achète), jamais la data des autres clients, le commercial, ni la voix perso de Tim. [[concepts/data-proprietaire|La data propriétaire]] du client devient sa voix ; le pack apporte la doctrine [[syntheses/4-piliers-organikk|4 piliers]].

## Les 3 repos

| Repo | Pour qui | Contenu |
|---|---|---|
| `seo-kb` | Tim, privé à vie | doctrine source, tous les clients, commercial, voix perso. **Jamais partagé.** |
| `<client>-seo` | le client (transfert ownership GitHub au handover) | `data/` (sa data immuable), `brain/` (mémoire + voix), `production/` (pages), `AGENTS.md` + `STRATEGIE.md` adaptés, submodule `pack/` |
| `organikk-seo-pack` | tous les clients | doctrine + skills génériciss, **vivant** (synchronisé) |

Le flux vivant : Tim édite `seo-kb` → `./build-pack.sh` → `git push` du pack → chaque client `git submodule update --remote`.

## Procédure pas à pas

### 1. Dossier client privé dans seo-kb
- Créer `raw/organikk/clients/<slug>/` avec une fiche maître `<slug>.md` (contexte, contacts, état SEO, angle, périmètre, points ouverts) et rapatrier les transcripts du client.
- Cette fiche reste **privée** (ma stratégie sur eux, prix, ce que je pense). Elle ne part jamais dans le repo client.

### 2. Repo client transférable
- `mkdir <client>-seo` avec `data/{calls,emails,...}`, `brain/{memoire,voix-<client>,ledgers}`, `production/{modeles,pages,briefs}`, `git init`.
- `AGENTS.md` : la méthode adaptée au client (data propriétaire → modèles de pages → capture e-mail → boucle d'apprentissage), SANS la doctrine 4 piliers verbatim ni la voix perso.
- `STRATEGIE.md` : les 4 piliers (Surprise/Grounding/pSEO/AEO + data propriétaire) réécrits avec les exemples du client, tirés du vrai seo-kb.
- Déposer la data du client dans `data/` (elle lui appartient, sa place est là aussi).

### 3. Pack vivant (une seule fois, puis réutilisé)
- `organikk-seo-pack` contient `doctrine/` (régénéré depuis seo-kb par `build-pack.sh`, exclut clients tiers / commercial / voix perso) et `skills/` (skills génériciss à la main).
- Brancher dans le repo client : `git submodule add <url-pack> pack` puis `git submodule update --init --remote`.
- Câbler les skills invocables : `ln -s ../pack/skills .claude/skills` (committé).

### 4. La voix : paramétrée, jamais celle de Tim
- Reconstruire `brain/voix-<client>/` depuis les calls du client (`data/calls/`). Tant qu'il n'y a que le call de découverte (vente Tim↔client), c'est un **v0 voix de marque** partiel ; la voix client réelle attend leurs calls de démo.
- Les skills lisent `$VOIX_DIR` (= `brain/voix-<client>/`). Ne JAMAIS porter `tim-my-voice` ni `style-timothee`.

### 5. Genericisation des skills (au portage dans le pack)
- Retirer : chemins `/Users/timothee/...`, références aux autres clients, exemples sectoriels d'un autre client, lignes commerciales (prix, pitch), corpus de voix perso.
- Repointer les sauvegardes vers `production/` du repo client.
- Garder la méthode intacte (c'est la valeur). État du portage dans `organikk-seo-pack/skills/README.md`.

### 6. Espace client (organikk-next)
- Dashboard/questionnaire HTML en DA Leexi (gabarit standard, cf. [[queries/transfert-vault-client]] et la note dashboard DA Leexi), dans `public/<slug>/`, noindex.
- Formulaires : insert anon Supabase, **pas de select anon** si confidentiel, lecture admin via clé runtime (jamais commitée). Ne pas compter sur Netlify Forms (détection off sur export statique = POST 404 silencieux).

### 7. Handover
- Transférer l'ownership GitHub du repo `<client>-seo`.
- Donner au compte client l'accès collaborateur au pack privé `organikk-seo-pack` (sinon `submodule update` échoue).

## Garde-fous (ce qui ne part jamais)

- La data des autres clients.
- Le commercial : prix, discours de vente, pipeline de prospection.
- La voix perso de Tim (`tim-my-voice`, `style-timothee`).

`build-pack.sh` applique ces exclusions et alerte si une référence de voix perso fuite.

## Pages liées

[[queries/transfert-vault-client]] · [[syntheses/4-piliers-organikk]] · [[concepts/data-proprietaire]] · [[concepts/anti-ai-writing]] · [[methodes/ranker-verticale-niche-sans-backlink]]
