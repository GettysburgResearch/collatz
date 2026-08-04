#!/usr/bin/env python3
"""X-0119: fixed-length weight-two high-precision collision suffix hunt.

Fix length L and weight 2. Words = ones at i<j < L.
Collision code of precision p means B congruent mod 3^p (p >= 2).
Offsets E = (B0 - B)/3^p; measure filled radius R(E).
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


def B_ij(i: int, j: int) -> int:
    return (1 << i) * 3 + (1 << j)


def filled_radius(D: list[int]) -> int:
    S = set(D)
    diffs = {a - b for a in S for b in S}
    R = 0
    while (R + 1) in diffs and (-(R + 1)) in diffs:
        R += 1
    return R


def hunt(p: int, L: int) -> dict:
    mod = 3**p
    buckets: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for j in range(1, L):
        for i in range(0, j):
            buckets[B_ij(i, j) % mod].append((i, j))
    rich = {c: pairs for c, pairs in buckets.items() if len(pairs) >= 2}
    best = None
    top = []
    for c, pairs in rich.items():
        i0, j0 = pairs[0]
        B0 = B_ij(i0, j0)
        E = [(B0 - B_ij(i, j)) // mod for i, j in pairs]
        # verify exact congruence
        assert all(B_ij(i, j) % mod == B0 % mod for i, j in pairs)
        R = filled_radius(E)
        row = {
            "|E|": len(E),
            "R": R,
            "span": max(E) - min(E),
            "sample": pairs[:8],
            "E_sample": E[:8],
        }
        top.append(row)
        if best is None or R > best["R"] or (R == best["R"] and len(E) > best["|E|"]):
            best = row
    top.sort(key=lambda r: (-r["R"], -r["|E|"]))
    return {
        "p": p,
        "L": L,
        "rich": len(rich),
        "maxR": best["R"] if best else 0,
        "best": best,
        "top": top[:6],
    }


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    rows = []
    for p, L in [(2, 18), (2, 24), (3, 24), (3, 30), (4, 30), (4, 36), (5, 36), (5, 42)]:
        rows.append(hunt(p, L))
    summary = {
        "rows": rows,
        "any_R_ge_1": any(r["maxR"] >= 1 for r in rows),
        "any_R_ge_2": any(r["maxR"] >= 2 for r in rows),
        "maxR_overall": max(r["maxR"] for r in rows),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"any R>=1: {summary['any_R_ge_1']}  any R>=2: {summary['any_R_ge_2']}  maxR={summary['maxR_overall']}",
    ]
    for r in rows:
        lines.append(
            f"p={r['p']} L={r['L']} rich={r['rich']} maxR={r['maxR']} bestR={r['best']}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
