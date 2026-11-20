#!/usr/bin/env python3
"""Finite evidence for CLOCK_HEIGHT.md and PRIME_CIRCULATIONS.md.

The certificates and synthetic clock checks are exact. Actual-orbit
logarithmic inequalities are separately labeled floating-point diagnostics.
No finite computation is claimed to establish the universal theorem.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from random import Random


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def odd_step(n: int) -> tuple[int, int]:
    require(n > 0 and n % 2 == 1, "positive odd input required")
    z = 3 * n + 1
    a = (z & -z).bit_length() - 1
    return z >> a, a


@lru_cache(maxsize=None)
def factor(n: int) -> tuple[tuple[int, int], ...]:
    out: list[tuple[int, int]] = []
    p = 2
    while p * p <= n:
        v = 0
        while n % p == 0:
            n //= p
            v += 1
        if v:
            out.append((p, v))
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append((n, 1))
    return tuple(out)


def rational_rank(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    a = [[Fraction(z) for z in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((j for j in range(r, len(a)) if a[j][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = a[r][c]
        a[r] = [q / z for q in a[r]]
        for j in range(len(a)):
            if j != r and a[j][c]:
                z = a[j][c]
                a[j] = [q - z * u for q, u in zip(a[j], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def circulation_check(sources: list[int], weights: list[int]) -> dict:
    columns = []
    before: Counter[int] = Counter()
    after: Counter[int] = Counter()
    target = []
    exponent = []
    for n, w in zip(sources, weights):
        u, a = odd_step(n)
        target.append(u)
        exponent.append(a)
        col = Counter(dict(factor(u)))
        col.subtract(dict(factor(n)))
        columns.append(col)
        for p, v in factor(n):
            before[p] += w * v
        for p, v in factor(u):
            after[p] += w * v
    require(before == after, "all-prime inventories differ")
    primes = sorted(set().union(*(set(c) for c in columns)))
    rank = rational_rank([[c[p] for c in columns] for p in primes])
    require(rank == len(sources) - 1, "circulation is not a one-dimensional kernel")
    source_product = math.prod(n**w for n, w in zip(sources, weights))
    target_product = math.prod(n**w for n, w in zip(target, weights))
    require(source_product == target_product, "integer products differ")
    total_exponent = sum(a * w for a, w in zip(exponent, weights))
    require(
        math.prod((3 * n + 1)**w for n, w in zip(sources, weights))
        == (1 << total_exponent) * source_product,
        "complete shifted product identity failed",
    )
    require(set(sources) != set(target), "control unexpectedly invariant")
    return {
        "sources": sources,
        "successors": target,
        "division_exponents": exponent,
        "weights": weights,
        "weighted_division_total": total_exponent,
        "common_product": source_product,
        "prime_inventory": dict(sorted(before.items())),
        "valuation_matrix_rank": rank,
        "kernel_dimension": len(sources) - rank,
        "is_invariant_source_set": False,
    }


def threshold_checks(xs: list[Fraction], zs: list[Fraction]) -> int:
    require(len(xs) == len(zs) and len(xs) > 0, "bad abstract sequence")
    require(all(x >= 0 and 0 <= z <= x for x, z in zip(xs, zs)), "bad heights")
    require(all(b - a <= 1 for a, b in zip(xs, xs[1:])), "upward bound failed")
    ts = [3 * i - x for i, x in enumerate(xs)]
    for j in range(len(xs)):
        for i in range(j):
            require(min(zs[i], zs[j]) < ts[j] - ts[i], "clock premise failed")
    hs = {Fraction(1, 4), Fraction(1), Fraction(2), Fraction(4)}
    for z in zs + [2 * x for x in xs]:
        if z > 0:
            hs.update((z, z + Fraction(1, 8)))
    for h in hs:
        count = sum(z >= h for z in zs)
        high = sum(x >= h / 2 for x in xs)
        budget = 5 * high / h
        if h <= 2 * xs[0]:
            budget += 1 + xs[0] / h
        require(count <= budget, f"exact clock tail failed at {h}")
    return len(hs)


def abstract_clock_checks() -> dict:
    rng = Random(20261120)
    count = 0
    sequences = 0
    for n in range(1, 13):
        for _ in range(400):
            xs = [Fraction(rng.randrange(0, 41), 2)]
            for _j in range(1, n):
                xs.append(Fraction(rng.randrange(0, int(2 * xs[-1]) + 3), 2))
            ts = [3 * j - x for j, x in enumerate(xs)]
            zs: list[Fraction] = []
            for j, x in enumerate(xs):
                candidates = [Fraction(k, 2) for k in range(int(2 * x) + 1)]
                admissible = [
                    z for z in candidates
                    if all(min(z, zs[i]) < ts[j] - ts[i] for i in range(j))
                ]
                zs.append(rng.choice(admissible))
            count += threshold_checks(xs, zs)
            sequences += 1
    controls = [
        ([Fraction(0)], [Fraction(0)]),
        ([Fraction(100)] + [Fraction(0)] * 20, [Fraction(100)] + [Fraction(0)] * 20),
        ([Fraction(2)] * 20, [Fraction(2)] * 20),
        ([Fraction(20)] * 64,
         [Fraction(min(16, (j + 1) & -(j + 1))) for j in range(64)]),
    ]
    for xs, zs in controls:
        count += threshold_checks(xs, zs)
    return {
        "arithmetic": "exact rational",
        "seed": 20261120,
        "generated_sequences": sequences,
        "boundary_controls": len(controls),
        "threshold_checks": count,
        "scope": "finite checks of the abstract packing interface, not an all-size proof",
    }


def orbit_checks() -> dict:
    seeds = sorted(set(range(1, 102, 2)) | {121, 6171, 2**15 - 1, 3**20, 5**12})
    edges = pairs = diagnostics = windows = 0
    for source in seeds:
        ns = [source]
        for _ in range(79):
            u, a = odd_step(ns[-1])
            require((u << a) == 3 * ns[-1] + 1, "ordinary edge identity failed")
            require(u <= 2 * ns[-1], "ordinary upward inequality failed")
            ns.append(u)
            edges += 1
        for j in range(len(ns)):
            for i in range(j):
                require(
                    math.gcd(ns[i], ns[j]) * ns[j] < (1 << (3 * (j - i))) * ns[i],
                    "exact exponentiated gcd bound failed",
                )
                pairs += 1
        for end in (1, 2, 5, 10, 20, 40, 80):
            vals = ns[:end]
            xs = [math.log2(n) for n in vals]
            x0 = xs[0]
            total = sum(xs)
            mean = total / end
            e0 = 2 * max(x0 - 1, 0) + x0 * math.log(max(1, x0))
            localized = 2 * end + 5 * sum(math.log(max(1, x)) for x in xs) + e0
            averaged = end * (2 + 5 * math.log1p(mean)) + e0
            inventory: Counter[int] = Counter()
            for n in vals:
                inventory.update(dict(factor(n)))
            for p, v in inventory.items():
                yp = v * math.log2(p)
                require(yp <= localized + 1e-9, "floating local-height diagnostic failed")
                require(localized <= averaged + 1e-9, "floating Jensen diagnostic failed")
                diagnostics += 1
            s = len(inventory)
            maximum = max(xs)
            if s:
                explicit = max(2 * x0, 128 * s * math.log(4 * s))
                require(maximum <= explicit + 1e-9, "floating prefix maximum diagnostic failed")
                if maximum >= 2 * x0:
                    require(maximum <= s * (12 + 14 * math.log1p(maximum)) + 1e-9,
                            "floating implicit peak diagnostic failed")
            windows += 1
    return {
        "sources": seeds,
        "states_per_source": 80,
        "exact_ordinary_edges": edges,
        "exact_exponentiated_gcd_checks": pairs,
        "floating_height_windows": windows,
        "floating_prime_height_diagnostics": diagnostics,
        "scope": "exact identities and separate floating-point sanity checks; no cycle census",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("arithmetic-closure-report.json"))
    args = parser.parse_args()
    five = circulation_check([19, 25, 29, 55, 83], [1, 1, 1, 1, 1])
    seven = circulation_check([5, 7, 25, 55, 65, 83, 95], [2, 2, 1, 3, 1, 3, 1])
    require(five["common_product"] == 62_882_875, "five-state product changed")
    require(seven["weighted_division_total"] == 21, "seven-state exponent changed")
    report = {
        "status": "passed",
        "five_state_extreme_circulation": five,
        "seven_state_nonproper_potential_certificate": seven,
        "abstract_clock": abstract_clock_checks(),
        "actual_orbits": orbit_checks(),
        "evidence_boundary": "Universal theorems rest on written proofs; numerical logs are diagnostics only.",
    }
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "output": str(args.output),
                      "abstract_clock": report["abstract_clock"],
                      "actual_orbits": {k: v for k, v in report["actual_orbits"].items()
                                        if k != "sources"}}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
