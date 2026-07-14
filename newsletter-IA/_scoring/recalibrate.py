#!/usr/bin/env python3
"""
Recalibre le barème de sélection de la Newsletter IA à partir du feedback réel.
Réplique la mécanique d'agent-synthetic (source_weights.json) : ledgers append-only
-> poids dérivés bornés, journal dans calibration.md. Ne dépend que de la stdlib.

Lance : python3 recalibrate.py   (depuis _scoring/)
Idempotent : recompte tout depuis les ledgers à chaque run.
"""
import json, os, sys
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
LED = os.path.join(BASE, "ledgers")
DER = os.path.join(BASE, "derived")
WEIGHTS = os.path.join(DER, "scoring_weights.json")
CALIB = os.path.join(BASE, "calibration.md")

USEFUL = {"hit", "good"}
NOISE = {"flop", "wrong"}
AXES = ["nouveaute", "impact_seo", "impact_business", "originalite",
        "surprise", "potentiel_discussion", "durabilite"]


def read_jsonl(path):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def main():
    weights = json.load(open(WEIGHTS))
    sources = read_jsonl(os.path.join(LED, "sources.jsonl"))
    selections = read_jsonl(os.path.join(LED, "selections.jsonl"))
    feedback = read_jsonl(os.path.join(LED, "feedback.jsonl"))

    src_by_id = {s["id"]: s for s in sources}
    sel_by_item = {r["item_id"]: r for r in selections}

    # 1. Recompte hits par source depuis le feedback.
    for s in sources:
        s["useful_hits"] = 0
        s["noise_hits"] = 0
    for fb in feedback:
        sel = sel_by_item.get(fb["item_id"])
        if not sel:
            continue
        src = src_by_id.get(sel.get("source_id"))
        if not src:
            continue
        perf = fb.get("perf")
        if perf in USEFUL:
            src["useful_hits"] += 1
            src["last_useful"] = fb.get("edition") or src.get("last_useful")
        elif perf in NOISE:
            src["noise_hits"] += 1

    # 2. Poids de source = base_tier + 0.04*useful - 0.1*noise, borné.
    tier_base = weights["tier_base"]
    lo, hi = weights["source_factor_bounds"]
    source_weights = {}
    for s in sources:
        base = tier_base.get(s.get("tier", "secondaire"), 1.0)
        w = base + 0.04 * s["useful_hits"] - 0.1 * s["noise_hits"]
        source_weights[s["id"]] = round(clamp(w, lo, hi), 3)

    # 3. Calibration d'axe : gelée tant que < min_editions éditions notées.
    editions = sorted({fb["edition"] for fb in feedback})
    n_ed = len(editions)
    active = n_ed >= weights["axis_calibration_min_editions"]
    if active:
        useful_vals = {a: [] for a in AXES}
        noise_vals = {a: [] for a in AXES}
        for fb in feedback:
            sel = sel_by_item.get(fb["item_id"])
            if not sel:
                continue
            axes = sel.get("axes", {})
            bucket = useful_vals if fb.get("perf") in USEFUL else (
                noise_vals if fb.get("perf") in NOISE else None)
            if bucket is None:
                continue
            for a in AXES:
                if a in axes:
                    bucket[a].append(axes[a])
        for a in AXES:
            u = useful_vals[a]
            nz = noise_vals[a]
            if u and nz:
                discrim = (sum(u) / len(u)) - (sum(nz) / len(nz))
                weights["axis_weights"][a] = round(clamp(1.0 + 0.02 * discrim, 0.8, 1.3), 3)

    # 4. Réécrit les ledgers/dérivés.
    with open(os.path.join(LED, "sources.jsonl"), "w") as f:
        for s in sources:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")

    weights["source_weights"] = source_weights
    weights["editions_with_feedback"] = n_ed
    weights["axis_calibration_active"] = active
    weights["updated"] = date.today().isoformat()
    with open(WEIGHTS, "w") as f:
        json.dump(weights, f, ensure_ascii=False, indent=2)
        f.write("\n")

    # 5. Journalise.
    line = (f"- **{date.today().isoformat()}** — recalibration : "
            f"{n_ed} édition(s) notée(s), {len(feedback)} feedback(s). "
            f"Calibration d'axe {'ACTIVE' if active else 'gelée (< '+str(weights['axis_calibration_min_editions'])+' éditions)'}. "
            f"{len(source_weights)} sources pondérées.\n")
    with open(CALIB, "a") as f:
        f.write(line)

    print(line.strip())
    print(f"source_weights -> {json.dumps(source_weights, ensure_ascii=False)}")


if __name__ == "__main__":
    main()
