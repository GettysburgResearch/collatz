#!/usr/bin/env python3
"""Numerical regression checks for the fixed-height theorem-development note.

This script does not prove Collatz or the symbolic lemmas.  It checks decimal
constants, entropy-tail numerics on a finite range, and exponent bookkeeping.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


def h2(p: float) -> float:
    if not 0.0 < p < 1.0:
        raise ValueError("p must lie in (0,1)")
    return -(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))


def solve_pstar(target: float) -> float:
    lo, hi = 0.5, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if h2(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def binomial_tail(k: int, threshold: int) -> int:
    return sum(math.comb(k, q) for q in range(threshold, k + 1))


def run(max_k: int) -> dict[str, Any]:
    alpha = math.log(2.0) / math.log(3.0)
    theta = h2(alpha)
    rho = 0.5 * math.log2(3.0)
    pstar = solve_pstar(0.901)
    direct_delta = (1.0 - rho) * (1.0 - 0.901)

    checks: list[dict[str, Any]] = []

    def record(name: str, ok: bool, value: Any) -> None:
        checks.append({"name": name, "ok": bool(ok), "value": value})
        if not ok:
            raise AssertionError(f"{name}: {value}")

    record("alpha_interval", 0.6309297535 < alpha < 0.6309297537, alpha)
    record("theta_interval", 0.9499555271 < theta < 0.9499555273, theta)
    record("rho_interval", 0.7924812503 < rho < 0.7924812505, rho)
    record("pstar_interval", 0.6830805151 < pstar < 0.6830805153, pstar)
    record(
        "pstar_entropy",
        abs(h2(pstar) - 0.901) < 5e-15,
        h2(pstar),
    )
    record(
        "frequency_gap_interval",
        0.0521507615 < pstar - alpha < 0.0521507618,
        pstar - alpha,
    )
    record(
        "direct_killed_pullback_delta_interval",
        0.0205443561 < direct_delta < 0.0205443564,
        direct_delta,
    )
    record("current_no_hit_exponent", 1.0 / 32000.0 == 0.00003125, 1.0 / 32000.0)
    record("direct_exception_gap", 0.099 > 1.0 / 32000.0, 0.099 - 1.0 / 32000.0)

    worst_slack = float("inf")
    worst_k = None
    for k in range(1, max_k + 1):
        threshold = math.ceil(alpha * k)
        tail = binomial_tail(k, threshold)
        log_bound = k * theta * math.log(2.0)
        slack = log_bound - math.log(tail)
        if slack < worst_slack:
            worst_slack = slack
            worst_k = k
        if slack < -2e-11:
            raise AssertionError(
                f"entropy tail regression failed at k={k}: slack={slack}"
            )
    record(
        "finite_entropy_tail_regression",
        True,
        {"max_k": max_k, "worst_k": worst_k, "minimum_log_slack": worst_slack},
    )

    q_samples = [0.80, 0.85, 0.90, 0.95, 0.99]
    collapse = {}
    for q in q_samples:
        if q <= rho:
            continue
        exponent = 1.0 - abs(math.log(rho)) / abs(math.log(q))
        collapse[str(q)] = exponent
        if not exponent < 0.0:
            raise AssertionError(f"expected negative collapse exponent for q={q}")
    record("literal_pullback_exponent_collapse", True, collapse)

    return {
        "status": "pass",
        "scope": "numerical regression only; no Collatz proof",
        "constants": {
            "alpha_log2_over_log3": alpha,
            "binary_entropy_theta": theta,
            "rho_half_log2_3": rho,
            "pstar_h2_equals_0_901": pstar,
            "pstar_minus_alpha": pstar - alpha,
            "direct_beta_0_901_killed_pullback_delta": direct_delta,
            "current_moving_scale_no_hit_exponent": 1.0 / 32000.0,
        },
        "checks": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-k", type=int, default=512)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    result = run(args.max_k)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"

    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")

    if args.check_results:
        expected = args.check_results.read_text(encoding="utf-8")
        if payload != expected:
            raise SystemExit("result differs from frozen report")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
