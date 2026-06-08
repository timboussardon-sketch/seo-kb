#!/usr/bin/env python3
"""
eval_health.py — Vue de santé et de dérive de SyntheticBrain (pattern Evaluation & Monitoring).

LECTURE SEULE sur ledgers/. N'écrit QUE dans derived/ (vues calculées, régénérables par design).
Ne touche jamais aux ledgers, à memory/, ni au skill. Idempotent, sûr à relancer.

Ce qu'il répond, à partir de la data déjà loggée :
  - La qualité des éditions dérive-t-elle ? (note_globale, novelty, doctrine_fit, source_diversity)
  - Les claims se fragilisent-ils ? (taux verified, confiance moyenne, sources indépendantes)
  - Les prédictions sont-elles résolues à temps ? (open / en retard / résolues)
  - Statut global : OK / WATCH / ESCALATE (signal seulement, n'impose rien).

Usage : ./eval_health.py            (depuis agent-synthetic/)
Sort  : derived/eval_health.json    (machine, validé par validate.sh)
        derived/eval_health.md      (humain)
"""
import json, os, re
from datetime import date, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
LEDG = os.path.join(HERE, "ledgers")
DERIV = os.path.join(HERE, "derived")

# Seuils conservateurs, documentés ici (pas cachés). À ajuster à la revue hebdo.
RECENT_N = 3          # nb d'éditions récentes pour la moyenne courte
DROP_ESCALATE = 0.6   # chute de note_globale récente vs baseline -> ESCALATE
DROP_WATCH = 0.3      # chute plus douce -> WATCH
CONF_MIN = 0.70       # confiance moyenne récente des claims sous ce seuil -> signal
NOVELTY_MIN = 2.0     # novelty_score récent moyen sous ce seuil -> signal
OVERDUE_ESCALATE = 3  # nb de prédictions en retard au-delà duquel on escalade


def read_jsonl(name):
    """Lit un .jsonl en tolérant les lignes cassées (les saute, ne plante jamais)."""
    path = os.path.join(LEDG, name)
    rows, bad = [], 0
    if not os.path.exists(path):
        return rows, bad, False
    with open(path, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            try:
                rows.append(json.loads(s))
            except Exception:
                bad += 1
    return rows, bad, True


def num(x):
    """Coerce en float si possible (gère '6 claims / 4 sections' -> 6.0), sinon None."""
    if isinstance(x, bool):
        return None
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        m = re.search(r"-?\d+(?:[.,]\d+)?", x)
        if m:
            return float(m.group(0).replace(",", "."))
    return None


def mean(xs):
    xs = [v for v in xs if v is not None]
    return round(sum(xs) / len(xs), 3) if xs else None


def parse_date(s):
    if not isinstance(s, str):
        return None
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d").date()
    except Exception:
        return None


def analyse_runs(runs):
    """Série chronologique de qualité + dérive récent vs baseline."""
    series = []
    for r in runs:
        sq = r.get("score_qualite", {}) if isinstance(r.get("score_qualite"), dict) else {}
        series.append({
            "run": r.get("run"),
            "date": r.get("date"),
            "note_globale": num(r.get("note_globale")),
            "novelty": num(sq.get("novelty_score")),
            "doctrine_fit": num(sq.get("doctrine_fit")),
            "source_diversity": num(sq.get("source_diversity")),
        })
    series.sort(key=lambda x: x["date"] or "")
    scored = [s for s in series if s["note_globale"] is not None]
    recent = scored[-RECENT_N:]
    baseline = scored[:-RECENT_N] if len(scored) > RECENT_N else scored
    drift = None
    rec_note = mean([s["note_globale"] for s in recent])
    base_note = mean([s["note_globale"] for s in baseline])
    if rec_note is not None and base_note is not None:
        drift = round(rec_note - base_note, 3)
    return {
        "n_runs": len(series),
        "n_scored": len(scored),
        "recent_note_globale": rec_note,
        "baseline_note_globale": base_note,
        "drift_note_globale": drift,
        "recent_novelty": mean([s["novelty"] for s in recent]),
        "recent_doctrine_fit": mean([s["doctrine_fit"] for s in recent]),
        "recent_source_diversity": mean([s["source_diversity"] for s in recent]),
        "series": series,
    }


def analyse_claims(claims):
    """Santé des claims : verified, confiance, sources indépendantes, par édition."""
    by_ed = {}
    for c in claims:
        verdict = c.get("verdict") or c.get("status")  # nouveau schéma puis ancien
        ed = c.get("used_in") or c.get("edition") or "?"
        d = by_ed.setdefault(ed, {"ed": ed, "n": 0, "verified": 0,
                                  "conf": [], "indep": []})
        d["n"] += 1
        if verdict == "verified":
            d["verified"] += 1
        d["conf"].append(num(c.get("confidence")))
        d["indep"].append(num(c.get("independent_sources")))
    eds = list(by_ed.values())
    for d in eds:
        d["verified_ratio"] = round(d["verified"] / d["n"], 3) if d["n"] else None
        d["avg_confidence"] = mean(d.pop("conf"))
        d["avg_independent_sources"] = mean(d.pop("indep"))
    eds.sort(key=lambda x: x["ed"])
    recent = eds[-RECENT_N:]
    return {
        "n_claims": len(claims),
        "n_editions": len(eds),
        "recent_avg_confidence": mean([d["avg_confidence"] for d in recent]),
        "recent_verified_ratio": mean([d["verified_ratio"] for d in recent]),
        "by_edition": eds,
    }


def analyse_predictions(preds, ref):
    open_, overdue, resolved = 0, [], 0
    for p in preds:
        status = (p.get("status") or "").lower()
        rb = parse_date(p.get("resolve_by"))
        if status in ("open", "", "pending"):
            open_ += 1
            if rb and rb < ref:
                overdue.append({"id": p.get("id"), "resolve_by": p.get("resolve_by")})
        else:
            resolved += 1
    return {"n": len(preds), "open": open_, "resolved": resolved,
            "overdue": overdue, "n_overdue": len(overdue)}


def schema_report(rows, required, one_of=None):
    """Compte les lignes à qui il manque un champ requis (pattern ch.18 structured output).
    Advisory : ne bloque rien, contrairement à validate.sh. Signale juste la mémoire mal formée."""
    missing, incomplete = {}, 0
    for r in rows:
        if not isinstance(r, dict):
            incomplete += 1
            continue
        gaps = [k for k in required if k not in r or r.get(k) in (None, "", [])]
        if one_of and not any(k in r and r.get(k) not in (None, "") for k in one_of):
            gaps.append("|".join(one_of))
        if gaps:
            incomplete += 1
            for g in gaps:
                missing[g] = missing.get(g, 0) + 1
    return {"n": len(rows), "incomplete": incomplete, "missing_by_field": missing}


def main():
    ref = date.today()
    runs, bad_runs, _ = read_jsonl("runs.jsonl")
    claims, bad_claims, _ = read_jsonl("claims.jsonl")
    preds, bad_preds, _ = read_jsonl("predictions.jsonl")
    bad_total = bad_runs + bad_claims + bad_preds

    R = analyse_runs(runs)
    C = analyse_claims(claims)
    P = analyse_predictions(preds, ref)
    SC = schema_report(claims, ["claim", "sources", "independent_sources", "confidence"],
                       one_of=["verdict", "status"])
    SP = schema_report(preds, ["claim", "resolve_by", "status"])

    signals, level = [], "OK"

    def bump(target):
        nonlocal level
        order = {"OK": 0, "WATCH": 1, "ESCALATE": 2}
        if order[target] > order[level]:
            level = target

    d = R["drift_note_globale"]
    if d is not None and d <= -DROP_ESCALATE:
        signals.append(f"note_globale en chute marquée ({d:+}) sur les {RECENT_N} dernières éditions"); bump("ESCALATE")
    elif d is not None and d <= -DROP_WATCH:
        signals.append(f"note_globale en baisse ({d:+}) sur les {RECENT_N} dernières éditions"); bump("WATCH")
    if R["recent_novelty"] is not None and R["recent_novelty"] < NOVELTY_MIN:
        signals.append(f"novelty_score récent faible ({R['recent_novelty']})"); bump("WATCH")
    if C["recent_avg_confidence"] is not None and C["recent_avg_confidence"] < CONF_MIN:
        signals.append(f"confiance moyenne des claims récente sous le seuil ({C['recent_avg_confidence']})"); bump("WATCH")
    if P["n_overdue"] >= OVERDUE_ESCALATE:
        signals.append(f"{P['n_overdue']} prédictions en retard de résolution"); bump("ESCALATE")
    elif P["n_overdue"] > 0:
        signals.append(f"{P['n_overdue']} prédiction(s) en retard de résolution"); bump("WATCH")
    if bad_total > 0:
        signals.append(f"{bad_total} ligne(s) JSONL illisible(s) dans les ledgers"); bump("WATCH")
    if SC["incomplete"] or SP["incomplete"]:
        signals.append(f"schéma incomplet : {SC['incomplete']}/{SC['n']} claim(s) et "
                       f"{SP['incomplete']}/{SP['n']} prédiction(s) avec un champ requis manquant"); bump("WATCH")
    if not signals:
        signals.append("aucun signal de dérive")

    out = {
        "generated": ref.isoformat(),
        "status": level,
        "signals": signals,
        "thresholds": {"recent_n": RECENT_N, "drop_escalate": DROP_ESCALATE,
                       "drop_watch": DROP_WATCH, "conf_min": CONF_MIN,
                       "novelty_min": NOVELTY_MIN, "overdue_escalate": OVERDUE_ESCALATE},
        "runs": R, "claims": C, "predictions": P,
        "schema": {"claims": SC, "predictions": SP},
        "integrity": {"bad_lines": {"runs": bad_runs, "claims": bad_claims, "predictions": bad_preds}},
    }

    os.makedirs(DERIV, exist_ok=True)
    with open(os.path.join(DERIV, "eval_health.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")

    lines = []
    lines.append("# Santé SyntheticBrain — vue dérivée")
    lines.append("")
    lines.append(f"> Généré le {ref.isoformat()} par `eval_health.py` (lecture seule sur les ledgers). "
                 f"Régénérable, ne fait pas foi : c'est un signal, pas une décision.")
    lines.append("")
    lines.append(f"## Statut : **{level}**")
    for s in signals:
        lines.append(f"- {s}")
    lines.append("")
    lines.append("## Qualité des éditions")
    lines.append(f"- éditions notées : {R['n_scored']} / {R['n_runs']} runs")
    lines.append(f"- note_globale récente ({RECENT_N} dern.) : {R['recent_note_globale']} "
                 f"vs baseline {R['baseline_note_globale']} (dérive {R['drift_note_globale']})")
    lines.append(f"- novelty récent : {R['recent_novelty']} · doctrine_fit : {R['recent_doctrine_fit']} "
                 f"· source_diversity : {R['recent_source_diversity']}")
    lines.append("")
    lines.append("## Claims")
    lines.append(f"- total : {C['n_claims']} sur {C['n_editions']} éditions")
    lines.append(f"- récent : confiance moy {C['recent_avg_confidence']} · taux verified {C['recent_verified_ratio']}")
    lines.append("")
    lines.append("## Prédictions")
    lines.append(f"- {P['open']} ouvertes · {P['resolved']} résolues · {P['n_overdue']} en retard")
    if P["overdue"]:
        for o in P["overdue"]:
            lines.append(f"  - en retard : {o['id']} (échéance {o['resolve_by']})")
    lines.append("")
    lines.append("## Complétude de schéma (advisory, ne bloque pas)")
    lines.append(f"- claims : {SC['incomplete']}/{SC['n']} incomplets"
                 + (f" — manques : {SC['missing_by_field']}" if SC["missing_by_field"] else " — OK"))
    lines.append(f"- prédictions : {SP['incomplete']}/{SP['n']} incomplètes"
                 + (f" — manques : {SP['missing_by_field']}" if SP["missing_by_field"] else " — OK"))
    lines.append("")
    if bad_total:
        lines.append(f"## Intégrité\n- {bad_total} ligne(s) JSONL illisible(s) — lancer `./validate.sh`")
        lines.append("")
    with open(os.path.join(DERIV, "eval_health.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[eval_health] statut={level} | runs notés={R['n_scored']} "
          f"dérive note={R['drift_note_globale']} | prédictions en retard={P['n_overdue']} "
          f"| lignes cassées={bad_total} | schéma incomplet claims={SC['incomplete']}/{SC['n']} "
          f"préds={SP['incomplete']}/{SP['n']}")
    print(f"[eval_health] écrit: derived/eval_health.json + derived/eval_health.md")


if __name__ == "__main__":
    main()
