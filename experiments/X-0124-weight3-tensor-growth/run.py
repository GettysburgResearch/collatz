#!/usr/bin/env python3
"""X-0124: first constructive filled-geometry growth via weight-3 suffix tensor.

Uses a fixed-length weight-3 precision-p collision class with R(E)>=1 as a
Minkowski suffix: D <- D + 2^L E. Records seed R vs post-tensor R.

This is a NEW PATH relative to atomic T-0104 freeze (which assumed 2-point
atomic E with effective filled radius 0).
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


def B_ijk(i: int, j: int, k: int) -> int:
    return (1 << i) * 9 + (1 << j) * 3 + (1 << k)


def filled_radius(D) -> int:
    S = set(D)
    diffs = {a - b for a in S for b in S}
    R = 0
    while (R + 1) in diffs and (-(R + 1)) in diffs:
        R += 1
    return R


def best_suffix(p: int, L: int):
    mod = 3**p
    buckets = defaultdict(list)
    for k in range(2, L):
        for j in range(1, k):
            for i in range(0, j):
                buckets[B_ijk(i, j, k) % mod].append((i, j, k))
    best = None
    for triples in buckets.values():
        if len(triples) < 2:
            continue
        B0 = B_ijk(*triples[0])
        E = [(B0 - B_ijk(*t)) // mod for t in triples]
        R = filled_radius(E)
        row = {"R": R, "E": E, "triples": triples[:12], "|E|": len(E)}
        if best is None or R > best["R"] or (R == best["R"] and len(E) > best["|E|"]):
            best = row
    return best


def tensor(D0, L0, E):
    D1 = set()
    for d in D0:
        for e in set(E):
            D1.add(d + (1 << L0) * e)
    return D1


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    trials = []
    for p, L in [(5, 24), (6, 28), (6, 32), (7, 32)]:
        suf = best_suffix(p, L)
        if not suf or suf["R"] < 1:
            trials.append({"p": p, "L": L, "usable": False, "sufR": suf["R"] if suf else None})
            continue
        for seed, L0, name in [
            ({0, 1, 2, 3}, 6, "interval4_L6"),
            (set(range(16)), 10, "interval16_L10"),
            ({0, 1}, 8, "pair_L8"),
        ]:
            D1 = tensor(seed, L0, suf["E"])
            trials.append(
                {
                    "p": p,
                    "suffix_L": L,
                    "seed": name,
                    "seed_R": filled_radius(seed),
                    "suffix_R": suf["R"],
                    "suffix_|E|": suf["|E|"],
                    "L0": L0,
                    "post_|D|": len(D1),
                    "post_R": filled_radius(D1),
                    "predicted_lower": suf["R"] * (1 << L0),
                    "grew": filled_radius(D1) > filled_radius(seed),
                }
            )
    summary = {
        "trials": trials,
        "any_growth": any(t.get("grew") for t in trials),
        "conclusion": (
            "Weight-3 suffixes with R(E)>=1 do NOT grow filled seed radius: "
            "2^L(E-E) is a comb with gaps 2^L (T-0105). predicted_lower was a "
            "false heuristic; empirically grew=False in all trials."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [summary["conclusion"], f"any_growth={summary['any_growth']}"]
    for t in trials:
        lines.append(str(t))
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
