#!/usr/bin/env python3
"""Garde-fou crédits Netlify.

Compte les déploiements du cycle de facturation en cours sur tous les sites
de l'équipe et compare au budget. À lancer AVANT tout push sur un repo
auto-déployé (organikk-next, fusionn, bxble).

Budget : l'enveloppe Pro a été épuisée le 2026-06-11 avec ~165 déploiements
sur 12 jours. Cadre fixé avec Tim : 120 builds max par cycle, alerte à 70 %.

Sortie : OK / ATTENTION / STOP + détail par site. Code retour 1 si STOP.
"""
import json
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone

BUDGET_CYCLE = 120
WARN_RATIO = 0.7

def token() -> str:
    cfg = json.load(open(f"{__import__('os').path.expanduser('~')}/Library/Preferences/netlify/config.json"))
    return next(iter(cfg["users"].values()))["auth"]["token"]

def api(path: str, tok: str):
    req = urllib.request.Request(f"https://api.netlify.com/api/v1{path}", headers={"Authorization": f"Bearer {tok}"})
    return json.load(urllib.request.urlopen(req))

def main() -> int:
    tok = token()
    bw = api("/accounts/tim-boussardon/bandwidth", tok)
    start = bw["period_start_date"][:10]
    # Recharge de crédits : la baseline repart de la date du top up si plus récente.
    import os
    base_file = os.path.expanduser("~/.config/seo-kb/netlify-budget-baseline")
    if os.path.exists(base_file):
        override = open(base_file).read().strip()[:10]
        if override > start:
            start = override
    sites = [s for s in api("/sites?per_page=100", tok) if s.get("build_settings", {}).get("repo_url")]
    total = 0
    lines = []
    for s in sites:
        if s.get("build_settings", {}).get("stop_builds"):
            continue
        deploys = api(f"/sites/{s['id']}/deploys?per_page=100", tok)
        n = sum(1 for d in deploys if (d.get("created_at") or "") >= start)
        total += n
        if n:
            lines.append(f"  {s['name']:<14} {n:>3} builds")
    pct = total / BUDGET_CYCLE
    print(f"Cycle depuis le {start} · {total}/{BUDGET_CYCLE} builds ({pct:.0%} du budget)")
    print("\n".join(lines))
    if pct >= 1:
        print("STOP : budget du cycle épuisé. Ne pas pousser, prévenir Tim.")
        return 1
    if pct >= WARN_RATIO:
        print(f"ATTENTION : {pct:.0%} du budget consommé. Batcher strictement, prévenir Tim avant tout push non urgent.")
        return 0
    print("OK : marge disponible.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
