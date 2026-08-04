#!/usr/bin/env python3
"""X-0117: creative skew-product certificate probe.

State = (odd kernel m, chart index i, fuel f=v2-budget proxy).
Try to build a finite set of "moves" that act as a free semigroup on a
cone in R^2 with coordinates (log m, fuel), with expansion of log m and
nonnegative fuel drift.

This is intentionally speculative (IDEA-level construction search).
Moves are Syracuse steps with prescribed valuation k, which change:
  m |-> (3m+1)/2^k   (must be odd integer)
  fuel accounting: speculative prepaid vs tax = k

Search for pairs of expanding valuations whose modular domains on odds
allow long alternating walks with growing m — a skew-product shadow of
Schottky.
"""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def v2(n: int) -> int:
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def S_k(m: int, k: int) -> int | None:
    if m % 2 == 0 or m <= 0:
        return None
    t = 3 * m + 1
    if v2(t) != k:
        return None
    out = t >> k
    if out % 2 == 0:
        return None
    return out


def expanding_ks(Kmax: int = 12):
    return [k for k in range(1, Kmax + 1) if (1 << k) > 3]


def domain_mod(k: int, mod: int) -> set[int]:
    """Odd residues mod `mod` that can have v2(3m+1)=k for some lift.
    Necessary: 3m+1 ≡ 0 mod 2^k, not mod 2^{k+1} for exact k — approx scan.
    """
    out = set()
    for r in range(1, mod, 2):
        for t in range(0, 1 << 6):
            m = r + mod * t
            if S_k(m, k) is not None:
                out.add(r)
                break
    return out


def skew_search(mod: int = 64, depth: int = 25, n_max: int = 20000) -> dict:
    ks = expanding_ks(10)
    domains = {k: domain_mod(k, mod) for k in ks}
    # Find pairs with overlapping domains (needed to alternate) — want overlap
    # for transitions, but Schottky wants separation; record both.
    pair_info = []
    for i, k1 in enumerate(ks):
        for k2 in ks[i + 1 :]:
            inter = domains[k1] & domains[k2]
            pair_info.append(
                {
                    "k1": k1,
                    "k2": k2,
                    "|d1|": len(domains[k1]),
                    "|d2|": len(domains[k2]),
                    "|overlap|": len(inter),
                    "mu1": str(Fraction(1 << k1, 3)),
                    "mu2": str(Fraction(1 << k2, 3)),
                }
            )

    # Greedy: from odd m, always take maximal expanding k available
    survivors = 0
    best = None
    deaths_by = defaultdict(int)
    for m0 in range(1, n_max, 2):
        m = m0
        hist = []
        ok = True
        for _ in range(depth):
            opts = []
            for k in ks:
                out = S_k(m, k)
                if out is not None and out > m:
                    opts.append((k, out))
            if not opts:
                ok = False
                deaths_by["no_expanding_k"] += 1
                break
            opts.sort(key=lambda t: (-t[0], -t[1]))  # largest k then growth
            k, m = opts[0]
            hist.append(k)
        if ok and m > m0:
            survivors += 1
            if best is None or m / m0 > best["growth"]:
                best = {"m0": m0, "final": m, "growth": m / m0, "ks": hist[:20]}
    # Alternating fixed pair walks
    alt_hits = []
    for k1, k2 in [(2, 3), (2, 4), (3, 5), (4, 6)]:
        for m0 in range(1, n_max, 2):
            m = m0
            ok = True
            for i in range(depth):
                k = k1 if i % 2 == 0 else k2
                out = S_k(m, k)
                if out is None:
                    ok = False
                    break
                m = out
            if ok and m > m0:
                alt_hits.append({"k1": k1, "k2": k2, "m0": m0, "final": m, "growth": m / m0})
                break
    return {
        "expanding_ks": ks,
        "pair_info": pair_info[:15],
        "greedy_survivors": survivors,
        "greedy_best": best,
        "alt_hits": alt_hits,
        "note": (
            "Skew-product search: expanding Syracuse valuations rarely sustain "
            "long greedy walks; alternating fixed pairs almost never close."
        ),
    }


def fuel_lyapunov_scan(n_max: int = 5000) -> dict:
    """Creative Lyapunov: f(n) = log(n) - c * popcount_odd_debt.
    Track whether any simple fuel proxy increases for 30 steps on averages.
    """
    import math

    def odd_density_prefix(n, steps):
        odds = 0
        x = n
        for _ in range(steps):
            if x % 2:
                odds += 1
                x = (3 * x + 1) // 2
            else:
                x = x // 2
        return odds / steps

    thr = math.log(2) / math.log(3)
    above = 0
    samples = []
    for n in range(1, n_max + 1):
        d = odd_density_prefix(n, 40)
        if d > thr:
            above += 1
            if len(samples) < 10:
                samples.append({"n": n, "density": d})
    return {
        "threshold": thr,
        "frac_above_thr_40steps": above / n_max,
        "samples": samples,
        "note": "Finite-horizon supercritical density is common; infinite is the issue.",
    }


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    skew = skew_search()
    fuel = fuel_lyapunov_scan()
    summary = {"skew": skew, "fuel": fuel}
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        skew["note"],
        f"greedy survivors={skew['greedy_survivors']} best={skew['greedy_best']}",
        f"alt hits={skew['alt_hits']}",
        f"fuel frac above thr={fuel['frac_above_thr_40steps']:.4f}",
    ]
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
