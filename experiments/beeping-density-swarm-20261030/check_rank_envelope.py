#!/usr/bin/env python3
"""Independent bounded replay of rank_envelope.py; proof scope is in the report."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

from rank_envelope import (
    absorbed, ceil_div, contact_return, critical_real_envelope, envelope, gamma,
    inverse_contact_fan, is_contact, phi, shortcut,
)


def require(ok: bool, label: str) -> None:
    if not ok:
        raise RuntimeError(label)


def reference_gamma(n: int) -> int:
    if n == 1:
        return 0
    def raw(d: int) -> int:
        d = abs(d)
        u = d
        while u % 3 == 0:
            u //= 3
        return d * u
    answer = raw(n)
    x = n
    # Deliberately continue past the proved evaluator horizon.
    for k in range(1, 2 * n.bit_length() + 5):
        x = x // 2 if x % 2 == 0 else (3 * x + 1) // 2
        if x != n:
            answer = min(answer, 4 ** k * raw(x - n))
    return answer


def reference_phi(n: int) -> int:
    if n == 1:
        return 0
    # Fixed, source-only tail bound below one.  This is intentionally different
    # from the adaptive maximizer cutoff in the implementation under test.
    j, three, four = 0, 1, 1
    while three * (n + 1) ** 2 >= four:
        j, three, four = j + 1, three * 3, four * 4
    states = [n]
    for _ in range(j):
        states.append(absorbed(states[-1]))
    result = 0
    for x in reversed(states):
        result = max(gamma(x), ceil_div(result, 3))
    return result


def contact_horizon(n: int) -> int:
    if n == 1:
        return 0
    limit, three, four = 0, 1, 1
    while four * (phi(n) - 1) <= three * (n + 1) ** 2:
        limit, three, four = limit + 1, three * 3, four * 4
    x = n
    for j in range(limit + 1):
        if x == 1 or phi(x) == gamma(x):
            return j
        x = absorbed(x)
    raise RuntimeError(f"contact theorem failed at source {n}, limit {limit}")


def run(bound: int) -> dict:
    increases, decreases, equalities, contacts = [], 0, 0, 0
    max_horizon = (0, 1)
    max_contact = (0, 1)
    sublevel_counts = {m: 0 for m in (16, 64, 256, 1024)}
    for n in range(2, bound + 1):
        g, p = gamma(n), phi(n)
        q = phi(absorbed(n))
        require(n <= g <= p <= (n + 1) ** 2, f"size bound at {n}")
        require(p == max(g, ceil_div(q, 3)), f"Bellman identity at {n}")
        require(q <= 3 * p, f"one-step bound at {n}")
        if n <= 1000:
            require(g == reference_gamma(n), f"Gamma independent replay at {n}")
            require(p == reference_phi(n), f"Phi independent replay at {n}")
        if q > p:
            if len(increases) < 10:
                increases.append({"n": n, "next": absorbed(n), "phi": p, "next_phi": q})
        elif q < p:
            decreases += 1
        else:
            equalities += 1
        contacts += p == g
        max_horizon = max(max_horizon, (envelope(n)[2], n))
        max_contact = max(max_contact, (contact_horizon(n), n))
        for m in sublevel_counts:
            sublevel_counts[m] += p <= m

    powers = []
    for h in [*range(1, 21), 24, 32, 48, 64, 96, 128]:
        n = 3 ** h
        p = phi(n)
        next_n = shortcut(n)
        require(gamma(n) == n, f"known power-three identity H={h}")
        require(p > n, f"powers of three are not contact states H={h}")
        require(phi(next_n) <= 3 * p, f"power-three envelope H={h}")
        powers.append({
            "h": h, "n": str(n), "gamma": str(n), "phi": str(p),
            "phi_over_gamma": str(Fraction(p, n)),
            "next_gamma": str(gamma(next_n)), "next_phi": str(phi(next_n)),
            "next_phi_over_phi": str(Fraction(phi(next_n), p)),
            "maximizing_time": envelope(n)[1],
            "evaluated_horizon": envelope(n)[2],
        })

    critical = []
    for n in [2, 3, 5, 9, 27, 81, 243, 729, 1023, 4095, 1932103]:
        a, b, horizon = critical_real_envelope(n)
        c, d, _ = critical_real_envelope(absorbed(n))
        value, next_value = Fraction(a, b), Fraction(c, d)
        require(value == max(Fraction(gamma(n)), Fraction(4, 9) * next_value),
                f"critical Bellman identity {n}")
        require(next_value <= Fraction(9, 4) * value, f"critical growth {n}")
        critical.append({"n": n, "value": str(value), "horizon": horizon,
                         "next_value": str(next_value)})

    six_power_savings = []
    for h in range(1, 129):
        n, ceiling = 6 ** h, 12 ** h
        value = phi(n)
        require(value <= ceiling, f"nontrivial rank savings at 6**{h}")
        if h <= 10 or h in (16, 32, 64, 96, 128):
            six_power_savings.append({"h": h, "n": str(n), "phi": str(value),
                                      "upper_bound": str(ceiling)})

    fans = {}
    contact_pairs = 0
    for n in range(2, min(bound, 1000) + 1):
        if not is_contact(n):
            continue
        y, clock = contact_return(n)
        if y == 1:
            continue
        if y not in fans:
            fan = inverse_contact_fan(y)
            for row in fan["sources"]:
                x = row["n"]
                for j in range(row["clock"]):
                    require(j == 0 or not is_contact(x),
                            f"inverse fan skipped an earlier contact at {x}")
                    x = absorbed(x)
                require(x == y, f"inverse fan physical endpoint mismatch at {y}")
                require(row["clock"] <= fan["depth_bound"], f"inverse fan depth at {y}")
            fans[y] = fan
        lookup = {row["n"]: row["clock"] for row in fans[y]["sources"]}
        require(lookup.get(n) == clock, f"missing inverse contact source {n} to {y}")
        contact_pairs += 1
    contact_counterexamples = []
    for n, expected_y, expected_clock in [(11, 26, 2), (19, 44, 2)]:
        y, clock = contact_return(n)
        require((y, clock) == (expected_y, expected_clock), f"contact counterexample {n}")
        require(phi(y) > phi(n), f"contact increase missing at {n}")
        fan = inverse_contact_fan(y)
        row_ratio = phi(y) * sum((Fraction(1, phi(row["n"]))
                                 for row in fan["sources"]), Fraction())
        contact_counterexamples.append({"n": n, "endpoint": y, "clock": clock,
                                        "phi_before": phi(n), "phi_after": phi(y),
                                        "full_inverse_fan": fan,
                                        "inverse_power_one_row_ratio": str(row_ratio)})

    # The finite sample is not used to infer the universal theorems.
    return {
        "status": "PASS",
        "source_range": [2, bound],
        "independent_reference_range": [2, min(bound, 1000)],
        "checks": ["properness bounds", "integer Bellman identity",
                   "global factor-three inequality", "independent Gamma and Phi evaluators",
                   "finite contact traversal", "selected exact critical real envelopes"],
        "phi_decreases": decreases, "phi_equalities": equalities,
        "phi_increases": (bound - 1) - decreases - equalities,
        "contact_states": contacts,
        "first_increases": increases,
        "max_evaluated_horizon": {"steps": max_horizon[0], "n": max_horizon[1]},
        "max_contact_horizon": {"steps": max_contact[0], "n": max_contact[1]},
        "finite_sublevel_counts": sublevel_counts,
        "powers_of_three": powers,
        "critical_real_samples": critical,
        "six_power_savings_checked_range": [1, 128],
        "six_power_savings": six_power_savings,
        "contact_inverse_replay": {
            "forward_source_range": [2, min(bound, 1000)],
            "nonkilled_contact_pairs": contact_pairs,
            "distinct_endpoint_fans": len(fans),
            "leaf_paths_replayed": sum(len(f["sources"]) for f in fans.values()),
        },
        "contact_return_counterexamples": contact_counterexamples,
        "unresolved": "No strict contraction for all sources or for induced contact/unsafe returns.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bound", type=int, default=10000)
    parser.add_argument("--out", type=Path, default=Path(__file__).with_name("rank_envelope_results.json"))
    args = parser.parse_args()
    if args.bound < 2:
        raise SystemExit("bound must be at least two")
    report = run(args.bound)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items()
                      if k not in {"powers_of_three", "critical_real_samples", "six_power_savings",
                                   "contact_return_counterexamples"}}, indent=2))
