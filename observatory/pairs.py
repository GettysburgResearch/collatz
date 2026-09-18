"""Exact paired trajectories, column carries, and bounded falsification studies.

Pure arithmetic; no GUI or server. A raw arrival is never silently relabeled as
an accelerated step. A failed finite-horizon predicate is not an all-time claim.
"""
from __future__ import annotations

from collections import Counter
import re
from typing import Any

try:
    from .core import (Budget, Cancelled, TimedOut, bounded_int, parse_integer,
                       normalize_request, orbit, transition, valuation2, plot_log2)
except ImportError:
    from core import (Budget, Cancelled, TimedOut, bounded_int, parse_integer,
                      normalize_request, orbit, transition, valuation2, plot_log2)

RAW_LIMIT = 20000
RAW_DIGITS = 750000


def fields(request: dict, allowed: set[str]) -> None:
    extra = set(request) - allowed - {"kind"}
    if extra:
        raise ValueError("Unknown request fields: " + ", ".join(sorted(extra)))


def signed_integer(value: Any) -> int:
    if not isinstance(value, str) or not re.fullmatch(r"[+-]?[0-9]{1,2500}", value):
        raise ValueError("delta must be an exact signed decimal string.")
    n = int(value)
    if abs(n).bit_length() > 8192:
        raise ValueError("delta exceeds 8192 bits.")
    return n


def partner(seed: int, config: dict) -> int:
    relation = config["relation"]
    if relation == "flip":
        n = seed ^ (1 << config["bit"])
    elif relation == "offset":
        n = seed + int(config["delta"])
    else:
        n = int(config["other"])
    if n <= 0 or n.bit_length() > config["max_bits"]:
        raise ValueError("The partner must be positive and within max_bits; a flip may produce zero.")
    return n


def pair_config(request: dict) -> dict:
    fields(request, {"seed", "relation", "other", "delta", "bit", "map_left", "map_right", "steps", "max_bits", "raw_limit"})
    seed = parse_integer(request.get("seed", "27"))
    relation = request.get("relation", "offset")
    if relation not in ("flip", "offset", "explicit"):
        raise ValueError("relation must be flip, offset, or explicit.")
    relation_field = {"flip": "bit", "offset": "delta", "explicit": "other"}[relation]
    if ({"bit", "delta", "other"} - {relation_field}) & set(request):
        raise ValueError("Supply only the parameter for the selected relation.")
    config = {"kind": "pair", "seed": str(seed), "relation": relation,
              "max_bits": bounded_int(request.get("max_bits", 8192), "max_bits", 8, 8192),
              "steps": bounded_int(request.get("steps", 2000), "steps", 1, 10000),
              "raw_limit": bounded_int(request.get("raw_limit", 10000), "raw_limit", 1, RAW_LIMIT)}
    if relation == "flip":
        config["bit"] = bounded_int(request.get("bit", 2), "bit", 0, 8191)
    elif relation == "offset":
        config["delta"] = str(signed_integer(request.get("delta", "1")))
    else:
        config["other"] = str(parse_integer(request.get("other", "28")))
    other = partner(seed, config)
    for side, n in (("left", seed), ("right", other)):
        base = normalize_request({"kind": "orbit", "seed": str(n),
                                  "map": request.get("map_" + side, "shortcut"),
                                  "steps": config["steps"], "max_bits": config["max_bits"]})
        config["map_" + side] = base["map"]
    return config


def raw_support(trace: dict, budget: Budget, limit: int) -> dict:
    """Materialize a bounded raw prefix of precisely the computed displayed support."""
    anchors = {row["raw"]: row["i"] for row in trace["rows"]}
    target = trace["raw_steps"]
    n, rows, digits = int(trace["seed"]), [], 0
    reason = None
    for t in range(min(target, limit) + 1):
        budget.check()
        text = str(n)
        rows.append({"raw": t, "step": anchors.get(t), "n": text,
                     "log2": plot_log2(n), "bits": n.bit_length(), "parity": n & 1})
        digits += len(text)
        if t == target:
            break
        if digits >= RAW_DIGITS:
            reason = "raw_storage_limit"
            break
        n = 3 * n + 1 if n & 1 else n // 2
    if rows[-1]["raw"] < target and reason is None:
        reason = "raw_step_limit"
    return {"rows": rows, "computed_until": rows[-1]["raw"], "target_until": target,
            "complete": rows[-1]["raw"] == target, "reason": reason,
            "scope": "Raw prefix of the computed trace, including hidden accelerated states. Null step means not represented in that displayed clock."}


def shared_states(left: list[dict], right: list[dict], raw: bool = False) -> list[dict]:
    """First arrivals of distinct common exact states; no drawing coordinates used."""
    first_right = {}
    for row in right:
        first_right.setdefault(row["n"], row)
    shared, seen = [], set()
    for a in left:
        if a["n"] in first_right and a["n"] not in seen:
            b = first_right[a["n"]]
            seen.add(a["n"])
            shared.append({"n": a["n"],
                           "left": {"raw": a["raw"], "step": a.get("step") if raw else a["i"]},
                           "right": {"raw": b["raw"], "step": b.get("step") if raw else b["i"]}})
    return sorted(shared, key=lambda x: (max(x["left"]["raw"], x["right"]["raw"]),
                                        x["left"]["raw"] + x["right"]["raw"], x["left"]["raw"]))


def pair(config: dict, budget: Budget) -> dict:
    seed = int(config["seed"])
    other = partner(seed, config)
    traces = []
    for side, n in (("left", seed), ("right", other)):
        budget.progress({"unit": "pair", "side": side, "completed": len(traces), "total": 2})
        traces.append(orbit({"seed": str(n), "map": config["map_" + side],
                             "steps": config["steps"], "max_bits": config["max_bits"]}, budget))
    left, right = traces
    raw_left = raw_support(left, budget, config["raw_limit"])
    raw_right = raw_support(right, budget, config["raw_limit"])
    return {"left": left, "right": right, "raw_left": raw_left, "raw_right": raw_right,
            "shared_displayed": shared_states(left["rows"], right["rows"]),
            "shared_raw": shared_states(raw_left["rows"], raw_right["rows"], raw=True),
            "partner": str(other), "source_xor": str(seed ^ other),
            "meeting_order": "Increasing max(raw arrival A, raw arrival B), then total arrivals, then A. Not simultaneous time.",
            "scope": "Exact intersections of the stated finite supports, stopped at 1. Missing intersections are not nonmerging claims."}


def carry_summary(n: int, budget: Budget | None = None) -> dict:
    """The +1 is an injected carry at column zero; propagated carries start after it."""
    if not n & 1:
        return {"operation": "halve", "input": str(n), "output": str(n // 2),
                "v2": None, "max_run": 0, "carry_count": 0}
    carry, count, run, longest = 1, 0, 0, 0
    for bit in range(n.bit_length() + 2):
        if budget and bit % 128 == 0:
            budget.check()
        total = ((n >> bit) & 1) + (((n << 1) >> bit) & 1) + carry
        carry = total // 2
        count += carry
        run = run + 1 if carry else 0
        longest = max(longest, run)
    return {"operation": "add", "input": str(n), "output": str(3 * n + 1),
            "v2": valuation2(3 * n + 1), "max_run": longest, "carry_count": count}


def carry_columns(n: int, offset: int, width: int, budget: Budget) -> dict:
    summary = carry_summary(n, budget)
    columns = []
    if not n & 1:
        for bit in range(offset, offset + width):
            columns.append({"bit": bit, "n": (n >> bit) & 1, "shift": (n >> (bit + 1)) & 1,
                            "carry_in": None, "carry_out": None, "output": (n >> (bit + 1)) & 1})
        return {**summary, "columns": columns}
    carry = 1
    for bit in range(offset + width):
        if bit % 128 == 0:
            budget.check()
        a, b = (n >> bit) & 1, ((n << 1) >> bit) & 1
        total = a + b + carry
        if bit >= offset:
            columns.append({"bit": bit, "n": a, "shift": b, "carry_in": carry,
                            "carry_out": total // 2, "output": total & 1})
        carry = total // 2
    return {**summary, "columns": columns}


def carry_config(request: dict) -> dict:
    fields(request, {"left", "right", "offset", "width"})
    return {"kind": "carry", "left": str(parse_integer(request.get("left", "27"))),
            "right": str(parse_integer(request.get("right", "31"))),
            "offset": bounded_int(request.get("offset", 0), "offset", 0, 8191),
            "width": bounded_int(request.get("width", 32), "width", 1, 256)}


def carries(config: dict, budget: Budget) -> dict:
    a = carry_columns(int(config["left"]), config["offset"], config["width"], budget)
    b = carry_columns(int(config["right"]), config["offset"], config["width"], budget)
    comparable = a["operation"] == b["operation"] == "add"
    differences = [{"bit": x["bit"], "input": x["n"] != y["n"], "output": x["output"] != y["output"],
                    "carry": x["carry_out"] != y["carry_out"] if comparable else None}
                   for x, y in zip(a["columns"], b["columns"])]
    return {"left": a, "right": b, "differences": differences, "comparable_carries": comparable,
            "offset": config["offset"], "width": config["width"],
            "scope": "Literal bit columns at common powers of two. Odd: n + (n << 1) + 1. Even: halving, no fictional addition carries. Input +1 is injected at column 0."}


def study_config(request: dict) -> dict:
    fields(request, {"seed", "stride", "count", "relation", "delta", "bit", "horizon", "max_bits", "motif", "value", "target"})
    seed = parse_integer(request.get("seed", "1"))
    stride = parse_integer(request.get("stride", "2"))
    count = bounded_int(request.get("count", 64), "count", 1, 128)
    horizon = bounded_int(request.get("horizon", 200), "horizon", 1, 4000)
    if count * horizon * 2 > 300000:
        raise ValueError("2 × count × horizon must not exceed 300,000 raw steps.")
    bits = bounded_int(request.get("max_bits", 1024), "max_bits", 8, 2048)
    if (seed + (count - 1) * stride).bit_length() > bits:
        raise ValueError("A family source exceeds max_bits.")
    relation = request.get("relation", "offset")
    if relation not in ("flip", "offset"):
        raise ValueError("Study relation must be flip or offset.")
    if relation == "flip" and "delta" in request or relation == "offset" and "bit" in request:
        raise ValueError("Supply only the selected relation parameter.")
    config = {"kind": "study", "seed": str(seed), "stride": str(stride), "count": count,
              "horizon": horizon, "max_bits": bits, "relation": relation}
    if relation == "flip":
        config["bit"] = bounded_int(request.get("bit", 2), "bit", 0, bits - 1)
    else:
        config["delta"] = str(signed_integer(request.get("delta", "2")))
    motif, value = request.get("motif", "carry_run"), request.get("value", "3")
    if motif not in ("carry_run", "valuation", "parity_prefix"):
        raise ValueError("motif must be carry_run, valuation, or parity_prefix.")
    if motif == "parity_prefix":
        if not isinstance(value, str) or not re.fullmatch(r"[01]{1,32}", value):
            raise ValueError("A parity motif is a 1–32 bit shortcut prefix.")
    elif not isinstance(value, str) or not re.fullmatch(r"[0-9]{1,4}", value) or not 1 <= int(value) <= bits:
        raise ValueError("A carry/valuation threshold must be an exact integer string in [1, max_bits].")
    target = request.get("target", "merge")
    if target not in ("merge", "left_descends"):
        raise ValueError("target must be merge or left_descends.")
    return {**config, "motif": motif, "value": value, "target": target}


def motif_test(n: int, config: dict, budget: Budget) -> tuple[bool | None, dict]:
    motif, value = config["motif"], config["value"]
    if motif == "carry_run":
        info = carry_summary(n, budget)
        return bool(n & 1 and info["max_run"] >= int(value)), info
    if motif == "valuation":
        v = valuation2(3 * n + 1) if n & 1 else None
        return v is not None and v >= int(value), {"v2_3n_plus_1": v, "odd_branch": bool(n & 1)}
    start = n
    emitted = []
    for _ in value:
        budget.check()
        emitted.append(str(n & 1))
        nxt, _, peak = transition(n, "shortcut")
        if peak.bit_length() > config["max_bits"]:
            return None, {"prefix": "".join(emitted), "status": "feature_bit_limit"}
        n = nxt
    prefix = "".join(emitted)
    return prefix == value, {"prefix": prefix, "source": str(start),
                             "scope": "Fixed shortcut prefix, including continuation through the trivial cycle. Descriptive, not a prospective prediction."}


def study(config: dict, budget: Budget) -> dict:
    seed, stride = int(config["seed"]), int(config["stride"])
    members, interruption = [], None
    try:
        for j in range(config["count"]):
            budget.check()
            n = seed + j * stride
            item = {"index": j, "seed": str(n), "partner": None, "selected": None,
                    "target_holds": None, "outcome": "unfinished"}
            try:
                other = partner(n, config)
            except ValueError as exc:
                members.append({**item, "outcome": "invalid_partner", "reason": str(exc)})
                continue
            item["partner"] = str(other)
            selected, feature = motif_test(n, config, budget)
            item.update(selected=selected, feature=feature)
            base = {"map": "raw", "steps": config["horizon"], "max_bits": config["max_bits"]}
            a = orbit({**base, "seed": str(n)}, budget)
            b = orbit({**base, "seed": str(other)}, budget)
            common = shared_states(a["rows"], b["rows"])
            complete_a = a["status"] in ("reached_one", "cycle", "step_limit")
            complete_b = b["status"] in ("reached_one", "cycle", "step_limit")
            if config["target"] == "merge":
                holds = True if common else False if complete_a and complete_b else None
                witness = common[0] if common else None
            else:
                holds = True if a["first_descent"] is not None else False if complete_a else None
                witness = a["rows"][a["first_descent"]] if holds else None
            outcome = ("unfinished" if holds is None or selected is None else
                       "support" if selected and holds else "counterexample" if selected else
                       "control_pass" if holds else "control_fail")
            item.update(target_holds=holds, outcome=outcome, witness=witness,
                        left_status=a["status"], right_status=b["status"],
                        left_until=a["raw_steps"], right_until=b["raw_steps"],
                        left_terminal=a["terminal"], right_terminal=b["terminal"])
            members.append(item)
            budget.progress({"unit": "paired sources", "completed": j + 1, "total": config["count"]})
    except (Cancelled, TimedOut) as exc:
        interruption = "cancelled" if isinstance(exc, Cancelled) else "timed_out"
    completed = len(members)
    for j in range(completed, config["count"]):
        members.append({"index": j, "seed": str(seed + j * stride), "partner": None,
                        "selected": None, "target_holds": None, "outcome": "unfinished", "reason": "not_computed"})
    return {"members": members, "counts": dict(Counter(x["outcome"] for x in members)),
            "count": config["count"], "completed": completed, "interruption": interruption,
            "hypothesis": {"if": {"motif": config["motif"], "value": config["value"]},
                           "then": config["target"], "raw_horizon": config["horizon"]},
            "scope": "Exhaustive bounded progression, paired perturbations. Counterexamples falsify only the stated finite-horizon implication. All controls/invalid/unfinished sources remain in the denominator. Shared tails mean members are NOT independent samples; no predictive accuracy or causal significance is claimed."}
