#!/usr/bin/env python3
"""Synchronise la doctrine de l'agent qadence (table `skills` Supabase) avec la
source de vérité Obsidian (~/.claude/skills/*/SKILL.md).

À lancer après chaque modification d'un SKILL.md (ou après `./kb rebuild`) :
    python3 qadence/sync-skills.py            # applique
    python3 qadence/sync-skills.py --dry-run  # montre les écarts sans écrire

Créds : ~/.config/seo-kb/qadence-skills.env (SUPABASE_URL + SUPABASE_SERVICE_ROLE).
"""
import os, re, sys, json, urllib.request, urllib.parse

SK = os.path.expanduser("~/.claude/skills")
CFG = os.path.expanduser("~/.config/seo-kb/qadence-skills.env")

# slug DB (table skills) -> dossier source ~/.claude/skills
# Inclut les 20 skills SEO, la voix, et les ALIAS propriétaires que load_skill expose.
MAP = {
    # SEO (verbatim)
    "brief_contenu": "seo-brief-contenu", "cannibalisation": "seo-cannibalisation",
    "cluster_aeo": "seo-cluster-aeo", "clustering_mots_cles": "seo-clustering-mots-cles",
    "core_web_vitals": "seo-core-web-vitals", "donnees_structurees": "seo-donnees-structurees",
    "entites_vectorielles": "seo-entites-vectorielles", "geo_audit": "seo-geo-audit",
    "maillage_interne_gsc": "maillage-interne-gsc", "maillage_systeme": "maillage-systeme",
    "modeles_pseo": "seo-modeles-pseo", "mots_cles_decisionnels": "seo-mots-cles-decisionnels",
    "peurs_objections": "seo-peurs-objections", "preparation_semantique": "seo-preparation-semantique",
    "product_led_seo": "seo-product-led-seo", "programmatique_pseo": "seo-programmatique-pseo",
    "quick_win": "seo-quick-win", "recherche_mots_cles": "seo-recherche-mots-cles",
    "roadmap_pseo": "seo-roadmap-pseo", "workflow_article": "seo-workflow-article",
    # Voix transverse
    "ton_de_voix_tim": "ton-de-voix-tim",
    # Alias propriétaires exposés par load_skill -> pointent sur la doctrine réelle
    "maillage_interne": "maillage-interne-gsc",
    "objections_clients": "seo-peurs-objections",
    "score_geo": "seo-geo-audit",
    "score_semantique": "seo-entites-vectorielles",
    "content_gaps": "seo-cluster-aeo",
    "strategie_seo": "seo-roadmap-pseo",
}

def load_cfg():
    cfg = {}
    with open(CFG) as f:
        for line in f:
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1); cfg[k] = v
    return cfg["SUPABASE_URL"], cfg["SUPABASE_SERVICE_ROLE"]

def body_of(txt):
    m = re.match(r"^---\n.*?\n---\n?(.*)$", txt, re.S)
    return (m.group(1) if m else txt).strip()

def main():
    dry = "--dry-run" in sys.argv
    url, key = load_cfg()
    H = {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json"}

    # état actuel
    req = urllib.request.Request(f"{url}/rest/v1/skills?select=name,prompt", headers=H)
    current = {s["name"]: (s.get("prompt") or "") for s in json.load(urllib.request.urlopen(req))}

    changed = unchanged = missing = 0
    for slug, folder in sorted(MAP.items()):
        path = os.path.join(SK, folder, "SKILL.md")
        if not os.path.exists(path):
            print(f"  ❌ source absente : {slug} ({folder})"); missing += 1; continue
        new = body_of(open(path).read())
        if slug not in current:
            print(f"  ⚠️  slug absent en base : {slug}"); missing += 1; continue
        if current[slug].strip() == new.strip():
            unchanged += 1; continue
        print(f"  {'~' if dry else '✓'} {slug:26} ← {folder}  ({len(current[slug])} → {len(new)} car.)")
        changed += 1
        if not dry:
            data = json.dumps({"prompt": new}).encode()
            r = urllib.request.Request(
                f"{url}/rest/v1/skills?name=eq.{urllib.parse.quote(slug)}",
                data=data, headers={**H, "Prefer": "return=minimal"}, method="PATCH")
            urllib.request.urlopen(r)

    print(f"\n{'[dry-run] ' if dry else ''}à jour: {unchanged} · modifiés: {changed} · problèmes: {missing}")

if __name__ == "__main__":
    main()
