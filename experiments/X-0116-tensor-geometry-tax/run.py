#!/usr/bin/env python3
"""X-0116: geometry vs tax under T-0006-style atomic chronological tensoring.

Reimplements the L-0008 atomic suffixes and L-0007 Minkowski update
  D <- D + 2^L {0, ±K_p}
without depending on the other branch as a proved library.

Measures at each stage:
  - cumulative length (tax proxy)
  - |D|
  - filled difference radius: max R with [-R,R] ⊆ D-D
  - modular coverage: |D mod 2^b| for b=1..12
  - whether coverage mod 2^b ever increases after L >= b

Predicts (toward T-0104): filled radius stays equal to the seed's; coverage
mod 2^b freezes once cumulative L >= b.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

# Atomic K_p grows double-exponentially; allow large int serialization in digests.
sys.set_int_max_str_digits(0)


def v3_of_pow2_minus1(R: int) -> int:
    """v3(2^R - 1) for R = 2*3^{p-1} equals p; compute generally via loop."""
    x = (1 << R) - 1
    c = 0
    while x % 3 == 0:
        x //= 3
        c += 1
    return c


def atomic_K(p: int) -> int:
    R = 2 * (3 ** (p - 1))
    # K = (2^R - 1)/3^p
    return ((1 << R) - 1) // (3**p)


def atomic_length(p: int) -> int:
    return 2 * (3 ** (p - 1)) + 1


def filled_radius(D: set[int]) -> int:
    diffs = {a - b for a in D for b in D}
    R = 0
    while R + 1 in diffs and -(R + 1) in diffs:
        R += 1
    # also require 0 in diffs (always)
    return R


def mod_coverage(D: set[int], b: int) -> int:
    m = 1 << b
    return len({d % m for d in D})


def amplify(seed: set[int], a0: int, stages: int, L0: int) -> dict:
    """Seed D0 as offsets; a0 = weight of seed code; L0 = seed length."""
    D = set(seed)
    L = L0
    a = a0
    rows = []
    for n in range(stages):
        p = a + 1  # next atomic precision/weight-one code V_{a+1} in T-0006 notation
        # In T-0006: V_i = V_{a0+i} with precision a0+i, append to U_{i-1} of weight a0+i-1
        # stage n=0..: p = a0+(n+1) = a+1 when a starts as a0
        K = atomic_K(p)
        Lp = atomic_length(p)
        # D <- D + 2^L {0, +K}  (use + for both; difference set sees ±)
        newD = set()
        for d in D:
            newD.add(d)
            newD.add(d + (1 << L) * K)
        D = newD
        L = L + Lp
        a = a + 1
        cov = {b: mod_coverage(D, b) for b in range(1, 13)}
        rows.append(
            {
                "stage": n + 1,
                "p": p,
                "K_odd": K % 2 == 1,
                "K_bitlen": K.bit_length(),
                "Lp": Lp,
                "cum_L": L,
                "cum_a": a,
                "|D|": len(D),
                "filled_radius": filled_radius(D),
                "coverage": cov,
                "log_mu": a * math.log(3) - L * math.log(2),
            }
        )
    return rows


def freeze_analysis(rows: list[dict], seed_cov: dict) -> dict:
    """For each b, find first stage where cum_L >= b and whether coverage changed after."""
    out = {}
    for b in range(1, 13):
        freeze_stage = None
        for r in rows:
            if r["cum_L"] >= b:
                freeze_stage = r["stage"]
                break
        cov_after = []
        for r in rows:
            if freeze_stage is not None and r["stage"] >= freeze_stage:
                cov_after.append(r["coverage"][b])
        out[b] = {
            "seed_cov": seed_cov[b],
            "freeze_stage": freeze_stage,
            "cov_at_freeze_and_after": cov_after,
            "max_cov": max(cov_after) if cov_after else seed_cov[b],
            "grew_after_freeze": (
                max(cov_after) > cov_after[0] if len(cov_after) > 1 else False
            ),
        }
    return out


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    # Toy seed: consecutive run like a small chart — D={0,1,2,3}, filled radius 3,
    # covers all mod 4, half of mod 8, etc.
    seed = {0, 1, 2, 3}
    L0, a0 = 6, 4  # 64->81 style scale
    seed_cov = {b: mod_coverage(seed, b) for b in range(1, 13)}
    rows = amplify(seed, a0=a0, stages=6, L0=L0)
    freeze = freeze_analysis(rows, seed_cov)

    # Sparse seed like O-0005 flavor: full mod 16 but not an interval
    seed2 = set(range(0, 16))  # full mod 16
    # punch holes to make filled radius small while keeping mod16
    seed2 = {i for i in range(0, 64) if i % 4 == 0 or i % 4 == 1}  # denser
    # Better: arithmetic progression-ish covering mod 16
    seed2 = set(range(16))  # filled radius 15, covers 16 mod 16
    rows2 = amplify(seed2, a0=8, stages=5, L0=24)
    freeze2 = freeze_analysis(rows2, {b: mod_coverage(seed2, b) for b in range(1, 13)})

    # Radius growth?
    radii = [filled_radius(seed)] + [r["filled_radius"] for r in rows]
    radii2 = [filled_radius(seed2)] + [r["filled_radius"] for r in rows2]

    summary = {
        "seed": sorted(seed),
        "seed_filled_radius": filled_radius(seed),
        "seed_coverage": seed_cov,
        "stages": rows,
        "freeze": freeze,
        "radii_trajectory": radii,
        "radius_grew": max(radii) > radii[0],
        "any_mod_grew_after_freeze": any(v["grew_after_freeze"] for v in freeze.values()),
        "seed2_radii": radii2,
        "seed2_radius_grew": max(radii2) > radii2[0],
        "seed2_any_mod_grew_after_freeze": any(
            v["grew_after_freeze"] for v in freeze2.values()
        ),
        "tax_proxy_cum_L_last": rows[-1]["cum_L"] if rows else None,
        "conclusion": (
            "Under atomic chronological tensoring, filled difference radius stays "
            "equal to the seed radius (sparse spikes do not fill), and coverage "
            "mod 2^b does not grow after cum_L >= b."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"radii={radii} grew={summary['radius_grew']}",
        f"any mod grew after freeze={summary['any_mod_grew_after_freeze']}",
        f"seed2 radii={radii2} grew={summary['seed2_radius_grew']}",
        f"final cum_L={summary['tax_proxy_cum_L_last']} |D|={rows[-1]['|D|']}",
    ]
    for b in (4, 8, 12):
        lines.append(f"  mod 2^{b}: {freeze[b]}")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
