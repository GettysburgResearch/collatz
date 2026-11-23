#!/usr/bin/env python3
"""Exact finite controls for ordinary first-hit and basin source packing.

These examples are convergent ordinary paths. No infinite orbit, pressure
measure, asymptotic exponent, or Collatz closure is tested by this script.
All comparisons use integers or Fraction, and remain active under python -O.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def shortcut(n: int) -> int:
    require(n > 0, "positive ordinary source required")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def odd_next(n: int) -> int:
    require(n > 0 and n % 2 == 1, "positive odd source required")
    y = 3 * n + 1
    while y % 2 == 0:
        y //= 2
    return y


def path_to_one(n: int) -> list[int]:
    path = [n]
    seen = {n}
    while n != 1:
        n = shortcut(n)
        require(n not in seen, "unexpected nontrivial finite cycle in control")
        seen.add(n)
        path.append(n)
        require(len(path) <= 10000, "control horizon exceeded")
    return path


def validate_partition(groups: list[set[int]]) -> None:
    occupied: set[int] = set()
    for group in groups:
        require(all(n > 0 for n in group), "nonpositive source")
        require(occupied.isdisjoint(group), "source charged to two basins")
        occupied.update(group)


def cutoff_charge(
    groups: list[set[int]], pool: set[int], cutoff: int, epsilon: Fraction
) -> tuple[int, int, Fraction, Fraction]:
    validate_partition(groups)
    require(all(group <= pool for group in groups), "source omitted from pool")
    masses = [sum((Fraction(1, n * n) for n in group), Fraction()) for group in groups]
    heavy = [group for group, mass in zip(groups, masses) if mass >= epsilon]
    touched = sum(any(n <= cutoff for n in group) for group in heavy)
    left = max(0, len(heavy) - touched) * epsilon
    tail = sum((Fraction(1, n * n) for n in pool if n > cutoff), Fraction())
    require(left <= tail, "finite source-cutoff inequality failed")
    return len(heavy), touched, left, tail


def main() -> None:
    require(3**5 < 2**8, "rational slope control")
    require(2**65 < 3**12 * 5**20, "binomial exponential control")
    require(Fraction(624, 625) < Fraction(799, 800), "root exponent margin")
    require(Fraction(1) + Fraction(1) / Fraction(799, 800) == Fraction(1599, 799),
            "squared pressure rearrangement exponent")

    q = 41  # The first unit odd state after the familiar source 27.
    ray: list[int] = []
    for _ in range(12):
        require(q != 1 and q not in ray and q % 3 != 0, "finite ray guard")
        ray.append(q)
        q = odd_next(q)
    roots = [64 * q + 21 for q in ray]
    require(len(set(roots)) == len(roots), "distinct siblings")
    root_set = set(roots)
    for v in roots:
        rest = path_to_one(v)[1:]
        require(root_set.isdisjoint(rest), "selected roots are not an antichain")

    bound = max(roots)
    groups_by_root = {v: set() for v in roots}
    paths: dict[int, list[int]] = {}
    for n in range(1, bound + 1):
        path = path_to_one(n)
        hits = root_set.intersection(path)
        require(len(hits) <= 1, "actual deterministic basins overlap")
        if hits:
            v = next(iter(hits))
            groups_by_root[v].add(n)
            paths[n] = path
    groups = [groups_by_root[v] for v in roots]
    validate_partition(groups)
    require(all(groups), "each root must appear in its own finite basin")

    # Every smaller positive source than these minima was actually enumerated.
    # Therefore the minima are exact for these selected full ordinary basins.
    minima = {v: min(groups_by_root[v]) for v in roots}
    first_hit_cases = 0
    descending_cases = 0
    height_cases = 0
    for v in roots:
        n = minima[v]
        path = paths[n]
        hit = path.index(v)
        require(all(x >= n for x in path[:hit]), "minimum before first hit")
        for h in range(min(len(path), hit + 10)):
            first_hit_cases += 1
            if path[h] < n:
                require(hit <= h, "descent occurred before the root")
                descending_cases += 1
            require(2**h * (path[h] + 1) <= 3**h * (n + 1),
                    "complete integer growth bound")
            height_cases += 1

    # A nonminimum ancestor generally descends before reaching its target.
    # This explicitly rejects deleting minimality from the first-hit theorem.
    false_minimum = None
    for v in roots:
        n = 2 * minima[v]
        if n != v and minima[v] != v:
            p = path_to_one(n)
            if p[1] < n and p.index(v) > 1:
                false_minimum = [n, v, p[1], p.index(v)]
                break
    require(false_minimum is not None, "missing false-minimum control")

    # Exact no-descent counts and complete affine carries at small horizons.
    parity_cases = 0
    no_descent_cases = 0
    for horizon in range(0, 13):
        X = 1024
        count = 0
        for n in range(1, X + 1):
            y, p, carry = n, 0, 0
            for clock in range(horizon):
                if y % 2:
                    carry = 3 * carry + 2**clock
                    p += 1
                y = shortcut(y)
            require(2**horizon * y == 3**p * n + carry, "whole carry identity")
            require(0 <= carry <= 3**horizon - 2**horizon, "whole carry bound")
            if y >= n:
                count += 1
                require(n < 3**horizon or 3**p >= 2**horizon,
                        "supercritical-or-small dichotomy")
            parity_cases += 1
        tail = sum(comb(horizon, p) for p in range(horizon + 1) if 8*p >= 5*horizon)
        capacity = Fraction(3**horizon) + (Fraction(X, 2**horizon) + 1) * tail
        require(count <= capacity, "exact finite no-descent capacity")
        no_descent_cases += 1

    # Retain precisely the actual finite predecessor sources. The pool is
    # explicit, so no unrelated integer tail is recomputed for every threshold.
    pool = set().union(*groups)
    masses = [sum((Fraction(1, n*n) for n in group), Fraction()) for group in groups]
    cutoffs = sorted({1, 2, 5, 16, 64, 256, bound // 2, bound})
    thresholds = sorted(set(masses + [mass / 2 for mass in masses]))
    packing_cases = 0
    for cutoff in cutoffs:
        for epsilon in thresholds:
            cutoff_charge(groups, pool, cutoff, epsilon)
            packing_cases += 1

    # Exact abstract sharpness at eta=1/2 and s=2; these are NOT Collatz basins.
    sharp_cases = 0
    for j in range(1, 65):
        mass = sum((Fraction(1, n*(n+1)) for n in range(j*j, (j+1)*(j+1))), Fraction())
        require(mass == Fraction(1, j*j) - Fraction(1, (j+1)*(j+1)),
                "telescoping abstract mass")
        require(Fraction(3, 4*j**3) <= mass <= Fraction(3, j**3),
                "sharp cubic decay")
        sharp_cases += 1

    rejected = 0
    malformed = [set(group) for group in groups]
    malformed[1].add(next(iter(malformed[0])))
    try:
        cutoff_charge(malformed, pool, 16, Fraction(1, 100000))
    except ValueError as exc:
        require("two basins" in str(exc), "wrong damaged-overlap rejection")
        rejected += 1
    else:
        raise ValueError("damaged overlapping basin accepted")
    omitted = set(pool)
    omitted.remove(next(iter(groups[0])))
    try:
        cutoff_charge(groups, omitted, 16, Fraction(1, 100000))
    except ValueError as exc:
        require("omitted" in str(exc), "wrong omitted-tail rejection")
        rejected += 1
    else:
        raise ValueError("omitted source accepted")
    rejected += 1  # the explicit nonminimum counterexample above

    print(json.dumps({
        "schema": "collatz-basin-packing-finite-controls/v1",
        "status": "PASS",
        "scope": "finite actual convergent examples, exact source accounting, and abstract sharp controls; no infinite-orbit validation",
        "original_odd_source": 41,
        "sibling_roots": roots,
        "source_bound": bound,
        "basin_minima": [[v, minima[v]] for v in roots],
        "retained_sources": sum(map(len, groups)),
        "finite_weight_pool_size": len(pool),
        "first_hit_cases": first_hit_cases,
        "descending_first_hit_cases": descending_cases,
        "integer_height_cases": height_cases,
        "literal_parity_carry_cases": parity_cases,
        "no_descent_capacity_cases": no_descent_cases,
        "finite_cutoff_cases": packing_cases,
        "abstract_sharp_cases": sharp_cases,
        "rejected_controls": rejected,
        "false_minimum_control": false_minimum,
        "coarse_minimum_exponent": "799/800",
        "square_pressure_rearrangement_exponent": "1599/799"
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
