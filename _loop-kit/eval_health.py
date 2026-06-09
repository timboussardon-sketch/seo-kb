#!/usr/bin/env python3
"""
eval_health.py (Loop Kit) - vue de sante d'un brain. LECTURE SEULE sur ledgers/, ecrit SEULEMENT derived/.
Idempotent. Usage : ./eval_health.py [chemin_du_brain]   (defaut : dossier courant).
Signale OK / WATCH / ESCALATE a partir de la data deja loggee (n'impose rien).
"""
import json, os, sys
from datetime import date

DIR = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
LEDG = os.path.join(DIR, "ledgers")
DERIV = os.path.join(DIR, "derived")
OVERDUE_ESCALATE = 3  # nb de predictions en retard au-dela duquel on escalade

def read_jsonl(name):
    p = os.path.join(LEDG, name)
    rows = []
    if not os.path.exists(p):
        return rows
    with open(p, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    return rows

today = date.today().isoformat()
runs = read_jsonl("runs.jsonl")
claims = read_jsonl("claims.jsonl")
preds = read_jsonl("predictions.jsonl")

def is_resolved(p):
    return bool(p.get("resolved") or p.get("verdict") or p.get("resolved_at") or p.get("status") in ("resolved","closed","hit","partial","miss"))

open_p = [p for p in preds if not is_resolved(p)]
overdue = [p for p in open_p if str(p.get("resolve_by", "")) and str(p.get("resolve_by")) < today]
resolved = [p for p in preds if is_resolved(p)]
verified_tracked = [c for c in claims if "verified" in c]
verified = [c for c in claims if c.get("verified") is True]

status = "OK"
reasons = []
if len(overdue) >= OVERDUE_ESCALATE:
    status = "ESCALATE"; reasons.append(f"{len(overdue)} predictions en retard")
elif overdue:
    status = "WATCH"; reasons.append(f"{len(overdue)} prediction(s) en retard")
if verified_tracked and len(verified) / len(verified_tracked) < 0.6:
    status = "ESCALATE" if status == "ESCALATE" else "WATCH"
    reasons.append("moins de 60% des claims verifies")

out = {
    "brain": os.path.basename(DIR),
    "generated": today,
    "runs": len(runs),
    "claims_total": len(claims),
    "claims_verified": len(verified),
    "predictions_open": len(open_p),
    "predictions_overdue": len(overdue),
    "predictions_resolved": len(resolved),
    "status": status,
    "reasons": reasons,
}
os.makedirs(DERIV, exist_ok=True)
with open(os.path.join(DERIV, "eval_health.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
with open(os.path.join(DERIV, "eval_health.md"), "w", encoding="utf-8") as f:
    f.write(f"# Sante boucle - {out['brain']} ({today})\n\n")
    f.write(f"**Statut : {status}**" + (f" - {'; '.join(reasons)}" if reasons else "") + "\n\n")
    f.write(f"- Runs loggés : {out['runs']}\n")
    f.write(f"- Claims : {out['claims_total']} (verifies : {out['claims_verified']})\n")
    f.write(f"- Predictions : {out['predictions_open']} ouvertes, {out['predictions_overdue']} en retard, {out['predictions_resolved']} resolues\n")
print(f"{status}  (runs={out['runs']} preds_open={out['predictions_open']} overdue={out['predictions_overdue']})")
