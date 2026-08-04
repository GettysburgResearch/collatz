#!/usr/bin/env python3
"""X-0120: weight-three high-precision collision suffix hunt (C-0103 residual).

Fixed length L, weight 3: ones at i<j<k < L.
B = 2^i*9 + 2^j*3 + 2^k.
Collision precision p: equal B mod 3^p.
Measure filled radius R(E) of normalized offsets.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


def B_ijk(i: int, j: int, k: int) -> int:
    return (1 << i) * 9 + (1 << j) * 3 + (1 << k)


def filled_radius(D: list[int]) -> int:
    S = set(D)
    diffs = {a - b for a in S for b in S}
    R = 0
    while (R + 1) in diffs and (-(R + 1)) in diffs:
        R += 1
    return R


def hunt(p: int, L: int) -> dict:
    mod = 3**p
    buckets: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for k in range(2, L):
        for j in range(1, k):
            for i in range(0, j):
                buckets[B_ijk(i, j, k) % mod].append((i, j, k))
    rich = {c: t for c, t in buckets.items() if len(t) >= 2}
    best = None
    maxR = 0
    has01 = False
    for c, triples in rich.items():
        B0 = B_ijk(*triples[0])
        E = [(B0 - B_ijk(i, j, k)) // mod for i, j, k in triples]
        R = filled_radius(E)
        if 0 in E and -1 in E:
            has01 = True
        if R > maxR or (R == maxR and best and len(E) > best["|E|"]) or best is None:
            maxR = R
            best = {"|E|": len(E), "R": R, "span": max(E) - min(E), "sample": triples[:6], "E_sample": E[:8]}
    return {
        "p": p,
        "L": L,
        "rich": len(rich),
        "maxR": maxR,
        "has01": has01,
        "best": best,
    }


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    # L^3 cost: keep moderate
    specs = [
        (2, 16),
        (3, 18),
        (4, 20),
        (5, 22),
        (6, 24),
        (6, 28),
        (7, 28),
    ]
    rows = [hunt(p, L) for p, L in specs]
    summary = {
        "rows": rows,
        "any_R_ge_1": any(r["maxR"] >= 1 for r in rows),
        "any_R_ge_2": any(r["maxR"] >= 2 for r in rows),
        "high_p_ge_6_maxR": max((r["maxR"] for r in rows if r["p"] >= 6), default=None),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"any R>=1: {summary['any_R_ge_1']}  R>=2: {summary['any_R_ge_2']}  high_p>=6 maxR={summary['high_p_ge_6_maxR']}",
    ]
    for r in rows:
        lines.append(
            f"p={r['p']} L={r['L']} rich={r['rich']} maxR={r['maxR']} has01={r['has01']} best={r['best']}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
