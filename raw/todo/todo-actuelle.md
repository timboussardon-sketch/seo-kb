# Todo Tim — MAJ 2026-05-02 20:30

> Source : 6 transcripts Claude Code locaux (seo-kb + organikk-next, 7 derniers jours).
> Reconstruite manuellement (slash `/todo` posé mais pas encore exécuté en mode skill).

## ✅ Fait récemment (7 derniers jours)

### 2026-05-01 — Ingest wiki massif (session seo-kb · 14h42)
- 7 concepts créés : `5-types-ancres`, `know-simple-know-do`, `maillage-systeme`, `methode-organikk-4-piliers`, `mots-cles-actionnels`, `pseo-data-driven-models`, `retrieval-collapse`
- 12 entities créées : `chatgpt-search`, `fg-formation`, `franck`, `google-ai-mode`, `jumpto`, `linkedin`, `marrusia-cecile`, `naver`, `perplexity`, `qadence-seo-agent`, `seer-interactive`, `semrush`
- 17 sources datées créées (avril 2026 : algorithme-linkedin, calls Marrusia/Cécile/Franck, scans arxiv 15+25 avril, listicles ChatGPT, opendecoder scoring, organikk process B2B 2026, core update fermes IA, 4 piliers Organikk, pSEO data-driven, ton de voix, drive accompagnement, FG formation, newsletter maillage, scheduled skills cron, posts LinkedIn batch)
- `wiki/index.md` mis à jour

### 2026-05-02 06h46 → 08h00 — Transfert Mac Organikk (session seo-kb)
- Décompression `transfert-mac-organikk.zip`
- Setup projet Organikk côté Mac local

### 2026-05-02 06h58 → 12h24 — Site Organikk : wiki + briefs + corrections (session organikk-next)
- 105 pages déployées sur organikk.co dont 30 fiches wiki + hub (zéro erreur TS)
- `src/app/wiki/page.tsx` + `src/app/wiki/[slug]/page.tsx` créés
- `src/data/wiki.ts` créé
- Briefs : `wiki/briefs/check-indexation-claude.md`, `wiki/briefs/maillage-interne-claude.md`
- Newsletters : `raw/newsletter/newsletter-agent-ia-verifier-indexation-seo.md`, `raw/newsletter/newsletter-maillage-interne-claude.md`
- Mockup `mockups/assets/perf-search-console.svg` (basé stats : 6,87k clics / 192k impressions / CTR 3,6 %)
- Wiki + glossaire déplacés dans le footer (sortis de "Ressources")
- FAQ pages service + méthode reformulées (anti-IA writing)
- Memory projet : `strategie-contenu-pilier-satellite`, `user_foi-chretienne`

### 2026-05-02 08h26 → 10h09 — Reddit GEO : flip de thèse + cleanup vault (session seo-kb)
- `wiki/briefs/reddit-pour-geo-2026.md` modifié — bascule de "lurker-extractor" vers "publication à valeur"
- 2 commits distincts (reddit dédié + reste du vault) + push origin main
- Récup `wiki/articles-publication-ready/reddit-pour-geo-2026-final.md` depuis branche `claude/find-organikk-repo-TvtHs`
- Audit dédoublonnage `~/Documents/seo-kb` vs `~/Downloads/seo-kblast`
- `.obsidian` renommé en `.obsidian.broken` (préparation re-ouverture vault)
- Memory : `canonical_vault_path` (toujours éditer dans `/Users/timothee/Documents/seo-kb/`)

### 2026-05-02 10h09 → 11h51 — Article Reddit GEO publié sur Organikk (session organikk-next)
- Article implémenté sur le site
- Em-dashes purgés du contenu, titres H2 pixel-perfect dégradé bleu, numéros H2 retirés
- Bloc "À retenir" aéré, tableau signal Reddit colorisé 1 ligne sur 2
- Memory : `feedback_blog_h2_gradient`, `feedback_no_em_dashes`

### 2026-05-02 11h57 → 12h28 — Stack d'agents installés (cette session, seo-kb)
- 5 agents créés et posés (non commités) :
  - `.claude/skills/revue-presse-quotidienne/SKILL.md` + `.github/workflows/revue-presse.yml` (cron 7h UTC)
  - `.claude/skills/audit-vault-hygiene/SKILL.md` + `.github/workflows/audit-vault.yml` (cron dim 6h UTC)
  - `.claude/skills/algorithme-recap-hebdo/SKILL.md` + `.github/workflows/algorithme-recap-hebdo.yml` (cron dim 18h UTC)
  - `.claude/commands/todo.md` (slash `/todo`)
  - `.claude/commands/repeats.md` (slash `/repeats`)
- 3 skills legacy archivés dans `raw/notes/scheduled-skills/_archive/`
- Memory projet : `automation_revue_presse_todo`

## 🔄 En cours

- **[démarrée 2026-05-02 ~12h]** Session organikk-next 80d2caef encore ouverte (dernière activité 20h28) — derniers signaux non clôturés : cards bleu foncé / bleu clair (contrast écriture foncé), note constante "pilier + satellites" demandée à 12h11

## 📋 À faire (priorisé)

### Prio 1 — Cette semaine (bloque le reste de la stack)

- [ ] **Push le commit avec les 5 agents** (seo-kb) — 9 fichiers `.claude/` + `.github/workflows/` non commités. Sans push, les workflows GH Actions ne tournent pas.
- [ ] **Ajouter `ANTHROPIC_API_KEY` aux secrets GH** : https://github.com/timboussardon-sketch/seo-kb/settings/secrets/actions — sinon les 3 workflows échoueront au 1er run
- [ ] **Tester les 3 workflows en manuel** via `workflow_dispatch` (Run workflow) avant de laisser le cron tourner seul, dans cet ordre : revue-presse → audit-vault → algorithme-recap-hebdo
- [ ] **Tester `/todo` et `/repeats`** en local dans une session Claude Code dans `seo-kb` pour valider que les slash commands fonctionnent
- [ ] **Réouvrir le vault Obsidian** (le `.obsidian` a été renommé en `.obsidian.broken`) — déclaré "je m'en occupe depuis l'UI Obsidian" dans la session du 2 mai 9h25

### Prio 2 — Semaine suivante

- [ ] **Vérifier le maillage interne de l'article Reddit GEO** sur Organikk (interrogation Tim 11h47 : "tu as suivi les regles de maillage ?")
- [ ] **Valider visuellement les cards bleu foncé / bleu clair** sur le site Organikk (demande 12h23, dernière session organikk-next)
- [ ] **Formaliser la règle "pilier + satellites"** demandée comme note à 12h11 dans organikk-next — elle est en memory projet, mais à coucher en règle dans `~/.claude/CLAUDE.md` ou dans une page wiki si Tim veut l'imposer

### Prio 3 — Backlog

- [ ] **Décider l'auto-fin-de-session todo** (hook SessionEnd ou cron launchd 23h) — différé à ~2026-05-22 selon mémoire projet, à revisiter une fois qu'on a un mois de slash `/todo` manuels en données pour mesurer l'utilité réelle
- [ ] **Ajouter agent archivage** (pas demandé explicitement mais signalé dans la conv 12h28) — purge auto des audits > 30j et revues de presse > 60j si Tim valide
- [ ] **Finaliser le cleanup post-transfert Mac Organikk** (eb4d847c) — la session du 6h46 ouvre un zip mais on ne sait pas si tout a été migré ou si des morceaux traînent dans `~/Desktop/dossier sans titre/tim-claude-transfer/`

---

## 🔥 Prio n°1 aujourd'hui

**Push le commit + ajouter `ANTHROPIC_API_KEY` au secret GH**. Sans ça, les 3 cron qu'on vient de poser ne servent à rien dès demain matin 7h UTC.

## 📌 Point d'attention

Beaucoup de modifs vault non commitées (5 fichiers `.claude/`, 3 workflows, 3 archives, 2 fichiers memory). Le repo seo-kb commence à diverger de ce qui est sur GitHub. Faire un commit propre avant d'attaquer autre chose.

---

*Si une tâche ici a été faite mais n'apparaît pas dans le ✅ Fait, c'est qu'elle n'est pas mentionnée dans une conversation Claude. Annote manuellement avec `✅ done manuellement YYYY-MM-DD` et le prochain `/todo` la conservera.*
