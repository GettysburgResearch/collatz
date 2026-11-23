#!/usr/bin/env python3
"""Exact finite controls for the first-hit basin-minimum split.

The sources are ordinary, explicitly convergent integers.  No source is
assumed to escape, and this checker does not test an infinite-family or
real-exponent theorem by a finite census.  Assertions are not used.
"""

from __future__ import annotations

from math import comb
from pathlib import Path
import hashlib
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def shortcut(n: int) -> int:
    require(type(n) is int and n > 0, "positive ordinary source required")
    return (3 * n + 1) // 2 if n % 2 else n // 2


def complete_path(n: int) -> list[int]:
    """The finite controls must actually reach one; no conclusion on timeout."""
    path = [n]
    for _ in range(10000):
        if path[-1] == 1:
            return path
        path.append(shortcut(path[-1]))
    raise ValueError("a finite control did not finish within its declared resource guard")


def odd_successor(n: int) -> int:
    require(n > 0 and n % 2 == 1, "odd source required")
    n = 3 * n + 1
    while n % 2 == 0:
        n //= 2
    return n


def sibling(n: int) -> int:
    return 64 * n + 21


def validate_roots(roots: list[int], paths: dict[int, list[int]]) -> None:
    require(len(set(roots)) == len(roots), "repeated root")
    root_set = set(roots)
    for root in roots:
        path = paths[root]
        require(path[0] == root and path[-1] == 1, "incomplete root trajectory")
        require(all(shortcut(a) == b for a, b in zip(path, path[1:])),
                "root trajectory is not literal")
        require(not (set(path[1:]) & root_set), "roots have comparable full basins")


def affine_check(n: int, H: int, endpoint: int, p: int, carry: int) -> None:
    require((1 << H) * endpoint == 3 ** p * n + carry,
            "complete affine carry identity failed")
    require(0 <= carry <= 3 ** H - 2 ** H < 3 ** H,
            "complete carry bound failed")


def first_hit_check(m: int, root: int, H: int, first_hit: int,
                    path: list[int], basin_minimum: int) -> None:
    require(m == basin_minimum, "candidate is not the basin minimum")
    require(path[0] == m and root in path and path.index(root) == first_hit,
            "root hitting witness missing or wrong")
    require(all(z >= m for z in path[:first_hit]),
            "a pre-hit source is below the claimed minimum")
    x = m
    for _ in range(H):
        x = shortcut(x)
    if x < m:
        require(first_hit <= H, "strict descent preceded the minimum's root hit")
        require((1 << H) * (root + 1) <= 3 ** H * (m + 1),
                "cleared first-hit growth bound failed")


def main() -> None:
    q = 65
    ray = [q]
    while ray[-1] != 1:
        ray.append(odd_successor(ray[-1]))
    require(len(set(ray)) == len(ray), "the finite ordinary ray repeats before one")
    roots = []
    labels = {}
    for j, q in enumerate(ray):
        v = q
        for b in (1, 2):
            v = sibling(v)
            require(v == 64 ** b * q + (64 ** b - 1) // 3,
                    "complete sibling affine formula failed")
            require(odd_successor(v) == odd_successor(q), "sibling successor changed")
            roots.append(v)
            labels[v] = {"ray_index": j, "sibling_depth": b, "base": q,
                         "odd_successor": odd_successor(q)}
    root_paths = {root: complete_path(root) for root in roots}
    validate_roots(roots, root_paths)
    root_set = set(roots)

    # Every smaller positive source is explicitly resolved through one,
    # so a first observed root occurrence is its exact full-basin minimum.
    Xmax = 4096
    horizons = [0, 1, 2, 3, 4, 6, 8, 12, 16, 20]
    cutoffs = [1, 2, 3, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    minima = {}
    minimum_paths = {}
    first_hits = {}
    nondescent = {H: [] for H in horizons}
    carry_checks = 0
    maximum_clock = 0
    small_carry_controls = 0
    first_source_hits = 0
    for n in range(1, Xmax + 1):
        path = complete_path(n)
        maximum_clock = max(maximum_clock, len(path) - 1)
        hits = [(i, v) for i, v in enumerate(path) if v in root_set]
        require(len(hits) <= 1, "a positive source visited two incomparable roots")
        if hits:
            first_source_hits += 1
            tau, root = hits[0]
            if root not in minima:
                minima[root] = n
                minimum_paths[root] = path
                first_hits[root] = tau
        x, p, carry = n, 0, 0
        for H in range(max(horizons) + 1):
            if H in nondescent:
                affine_check(n, H, x, p, carry)
                carry_checks += 1
                if x >= n:
                    nondescent[H].append(n)
                    if 3 ** p < 2 ** H:
                        require(n < 3 ** H, "small-carry cutoff lost an ordinary source")
                        small_carry_controls += 1
                    else:
                        require(8 * p >= 5 * H, "large odd-count cutoff failed")
            bit = x % 2
            if bit:
                carry = 3 * carry + (1 << H)
                p += 1
            x = shortcut(x)

    require(all(m % 2 for m in minima.values()), "a full-basin minimum was even")
    require(len(set(minima.values())) == len(minima), "disjoint basins shared a minimum")
    require(85 in minima and minima[85] == 75,
            "expected nonunit full-basin minimum changed")
    rows = []
    strict_minimum_controls = 0
    for X in cutoffs:
        low = {v: m for v, m in minima.items() if m <= X}
        for H in horizons:
            N = sum(n <= X for n in nondescent[H])
            roots_below = [v for v in roots if (1 << H) * v <= 3 ** H * (X + 1)]
            late = early = 0
            for v, m in low.items():
                path = minimum_paths[v]
                tau = first_hits[v]
                first_hit_check(m, v, H, tau, path, m)
                z = m
                for _ in range(H):
                    z = shortcut(z)
                if z >= m:
                    late += 1
                    require(m in nondescent[H], "actual minimum lost from no-descent set")
                else:
                    early += 1
                    strict_minimum_controls += 1
                    require(v in roots_below, "actual hit root lost from bounded root set")
            require(len(low) == late + early and late <= N and early <= len(roots_below),
                    "first-hit partition or its injections failed")
            require(len(low) <= N + len(roots_below), "BM4 failed")
            threshold = (5 * H + 7) // 8
            B = sum(comb(H, p) for p in range(threshold, H + 1))
            require((1 << H) * N <= (1 << H) * 3 ** H + (X + (1 << H)) * B,
                    "rational-cleared BM7 failed")
            rows.append({"X": X, "H": H, "exact_low_minima": len(low),
                         "actual_nondescent_sources": N, "small_roots": len(roots_below),
                         "minimum_nondescent_part": late, "minimum_early_hit_part": early})

    # Test the whole parity-cylinder enumeration, not an iid surrogate.
    cylinders = 0
    for H in range(11):
        residues = set()
        for bits in range(1 << H):
            carry = p = 0
            word = [(bits >> i) & 1 for i in range(H)]
            for k, bit in enumerate(word):
                if bit:
                    carry = 3 * carry + (1 << k)
                    p += 1
            modulus = 1 << H
            residue = (-carry * pow(3 ** p, -1, modulus)) % modulus
            source = residue if residue else modulus
            z = source
            for bit in word:
                require(z % 2 == bit, "canonical cylinder did not realize its whole word")
                z = shortcut(z)
            affine_check(source, H, z, p, carry)
            residues.add(residue)
            cylinders += 1
        require(len(residues) == 1 << H, "whole words collided in one parity cylinder")

    binomial_rows = []
    require(3 ** 5 < 2 ** 8, "rational odd-frequency cutoff changed")
    require(2 ** 65 < 3 ** 12 * 5 ** 20, "exact entropy base comparison failed")
    for H in range(65):
        B = sum(comb(H, p) for p in range((5 * H + 7) // 8, H + 1))
        require(B ** 8 * 3 ** (3 * H) * 5 ** (5 * H) <= 2 ** (24 * H),
                "weighted binomial bound failed after clearing eighth powers")
        require(B ** 32 <= 2 ** (31 * H), "BM8 failed after clearing 32nd powers")
        binomial_rows.append({"H": H, "tail_count": B})

    # Three independently meaningful omitted-hypothesis / mutation controls.
    rejected = []
    comparable = [sibling(65), odd_successor(sibling(65))]
    try:
        validate_roots(comparable, {v: complete_path(v) for v in comparable})
    except ValueError:
        rejected.append("a root and its actual odd successor are comparable")
    else:
        raise ValueError("comparable roots were accepted")

    nonminimum = complete_path(150)
    require(85 in nonminimum and shortcut(150) < 150 and nonminimum.index(85) > 1,
            "omitted-minimum counterexample did not realize its claimed behavior")
    try:
        first_hit_check(150, 85, 1, nonminimum.index(85), nonminimum, minima[85])
    except ValueError:
        rejected.append("150 hits 85 but is not its basin minimum; descent precedes its root hit")
    else:
        raise ValueError("a nonminimum was accepted as the minimum")

    try:
        first_hit_check(2, 85, 1, 0, complete_path(2), 2)
    except ValueError:
        rejected.append("2 descends but has no hit of the specified root85")
    else:
        raise ValueError("missing basin membership was accepted")

    try:
        affine_check(75, 1, shortcut(75), 1, 2)  # The true complete carry is 1.
    except ValueError:
        rejected.append("tampered complete affine carry")
    else:
        raise ValueError("damaged carry was accepted")

    base = Path(__file__).resolve().parent
    result = {
        "status": "PASS",
        "scope": "Exact finite ordinary controls for BM4, BM6--BM9. No escaping source or infinite-family theorem is assumed or inferred.",
        "finite_ordinary_ray": ray,
        "source_limit": Xmax,
        "maximum_observed_first_hit_one_clock": maximum_clock,
        "sources_hitting_a_selected_root": first_source_hits,
        "counts": {"incomparable_roots": len(roots), "exact_minima_at_or_below_limit": len(minima),
                   "split_cases": len(rows), "strict_minimum_first_hit_checks": strict_minimum_controls,
                   "complete_affine_carries": carry_checks,
                   "subcritical_nondescent_small_source_cases": small_carry_controls,
                   "exact_parity_cylinders": cylinders, "binomial_horizons": len(binomial_rows),
                   "rejected_controls": len(rejected)},
        "roots": [{"root": v, **labels[v], "minimum_if_at_most_limit": minima.get(v),
                   "minimum_first_hit_clock": first_hits.get(v), "complete_root_path": root_paths[v]}
                  for v in roots],
        "first_hit_split": rows,
        "binomial_controls": binomial_rows,
        "rejected_controls": rejected,
        "source_sha256": {name: hashlib.sha256((base / name).read_bytes()).hexdigest()
                          for name in ("check_basin_minima.py", "SPARSE_BASIN_MINIMA.md")},
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
