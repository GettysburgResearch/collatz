#!/usr/bin/env python3
"""Exact finite controls for SOURCE_TRANSFER.md; no escaping orbit is assumed found.

The finite measures below use actual odd predecessors from finitely many
known convergent trajectories, with the potential stopped at their first
visit to 1. They check finite identities, not the infinite entrance-law
construction, sparse-orbit theorem, or asymptotic separation rates.
All checks remain active under python -O.
"""

from collections import Counter
from fractions import Fraction
import json
from math import prod


class CheckFailure(RuntimeError):
    """A named exact control did not hold."""


class Checks:
    def __init__(self):
        self.counts = Counter()

    def require(self, condition, category):
        if not condition:
            raise CheckFailure(category)
        self.counts[category] += 1


def odd_step(n):
    if n <= 0 or n % 2 == 0:
        raise CheckFailure("odd_step domain")
    value = 3 * n + 1
    exponent = (value & -value).bit_length() - 1
    return value >> exponent, exponent


def trajectory_to_one(seed):
    path, seen = [], set()
    n = seed
    while n != 1:
        if n in seen or len(path) >= 2000:
            raise CheckFailure("known finite trajectory did not reach 1")
        path.append(n)
        seen.add(n)
        n, _ = odd_step(n)
    return tuple(path + [1])


def projected(law, modulus):
    result = {}
    for n, mass in law.items():
        residue = n % modulus
        result[residue] = result.get(residue, Fraction(0)) + mass
    return result


def tv(left, right):
    keys = left.keys() | right.keys()
    return sum(abs(left.get(n, 0) - right.get(n, 0)) for n in keys) / 2


def actual_compiler_control(checks, depth=128):
    """Periodic unprimed source: the repeated address keeps 1 fixed."""
    canonical = {1: 2, 4: 6, 7: 4}
    x, y, displacement = 1, 85, 0
    first_values = [y]
    exponent_counts = Counter()
    for k in range(depth + 1):
        checks.require(x == 1, "periodic original root")
        checks.require((y - 1) * 3**k >= 84 * 4**k,
                       "compiler all-depth lower bound at checked depth")
        if k == depth:
            break
        checks.require(y > 0 and y % 2 == 1 and y % 3 == 1,
                       "actual transported ordinary source")
        exponent = canonical[y % 9]
        numerator = (y << exponent) - 1
        checks.require(numerator % 3 == 0, "integer predecessor")
        successor = numerator // 3
        checks.require(successor % 2 == 1 and successor % 3 == 1,
                       "retained parent colour")
        checks.require(odd_step(successor) == (y, exponent),
                       "literal inverse edge and exact valuation")
        checks.require(3 * (successor - 1) >= 4 * (y - 1),
                       "compiler induction step")
        x = ((x << 2) - 1) // 3
        y = successor
        displacement += exponent - 2
        exponent_counts[exponent] += 1
        if len(first_values) < 9:
            first_values.append(y)
    return {
        "scope": "periodic ordinary control; not an escaping counterexample",
        "depth": depth,
        "first_transported_values": first_values,
        "final_value_bits": y.bit_length(),
        "signed_displacement": displacement,
        "canonical_exponent_counts": dict(sorted(exponent_counts.items())),
    }


def finite_layer_cake_control(checks, states, threshold):
    """Exact integral of the finite actual counting function for s=2."""
    ordered = sorted(states)
    left = sum(min(Fraction(1, threshold**2), Fraction(1, n**2))
               for n in ordered)
    cut = threshold
    count = sum(n <= cut for n in ordered)
    right = Fraction(0)
    for endpoint in (n for n in ordered if n > threshold):
        right += count * (Fraction(1, cut**2) - Fraction(1, endpoint**2))
        cut = endpoint
        count += 1
    right += Fraction(count, cut**2)
    checks.require(left == right, "finite exact layer-cake identity")


def finite_source_controls(checks):
    seeds = (7, 31, 47, 97, 871, 837799)
    paths = {seed: trajectory_to_one(seed) for seed in seeds}
    suffixes, potential = {}, {1: Fraction(1)}
    for path in paths.values():
        for index, n in enumerate(path):
            suffix = path[index:]
            checks.require(n > 0 and n % 2 == 1 and n % 3 != 0,
                           "positive odd ternary unit")
            checks.require(n not in suffixes or suffixes[n] == suffix,
                           "same ordinary source has same trajectory")
            suffixes[n] = suffix
        weight = Fraction(1)
        for n in reversed(path[:-1]):
            parent, exponent = odd_step(n)
            checks.require(parent in potential, "potential parent present")
            weight = Fraction(3, 1 << exponent) * weight
            checks.require(n not in potential or potential[n] == weight,
                           "same ordinary source has same potential")
            potential[n] = weight
            checks.require(0 < weight <= Fraction(1, n),
                           "stopped potential ordinary upper bound")
            checks.require(weight == Fraction(3, 1 << exponent) * potential[parent],
                           "stopped potential edge identity")

    # E is a finite union of actually evaluated paths. It is not an
    # escaping component or a claim to enumerate a full inverse basin.
    universe = tuple(sorted(potential))
    weights = {n: potential[n]**2 for n in universe}
    finite_mass = sum(weights.values())
    laws_checked = projections_checked = 0
    for seed in (7, 31, 837799):
        # Exclude the periodic terminal root 1 from every selected ray.
        ray = paths[seed][:-1]
        checks.require(len(set(ray)) == len(ray), "injective finite forward prefix")
        base = {n for n in universe if seed in suffixes[n]}
        a = sum(weights[n] for n in base)
        checks.require(a >= weights[seed] > 0, "retained original-source normalizer")
        for threshold in (1, 3, 10, 100):
            finite_layer_cake_control(checks, ray, threshold)
        lengths = sorted({min(n, len(ray)) for n in (1, 2, 3, 5, 8, 13, 21)})
        for length in lengths:
            prefix = ray[:length]
            empirical = {n: Fraction(1, length) for n in prefix}
            height = max(prefix)
            checks.require(height >= length, "height retains distinct sources")
            for root_index in sorted({length - 1, len(ray) - 1}):
                root = ray[root_index]
                domain = {n for n in universe if root in suffixes[n]}
                mass = sum(weights[n] for n in domain)
                checks.require(base <= domain, "nested actual ancestor sets")
                checks.require(a <= mass <= finite_mass, "exact finite normalizers")
                entrance = {n: weights[n] / mass for n in domain}
                checks.require(sum(entrance.values()) == 1,
                               "finite inverse law is normalized")
                checks.require(all(n in entrance for n in prefix),
                               "forward trial lies in actual ancestor domain")
                overlap = sum(min(empirical[n], entrance.get(n, 0)) for n in prefix)
                checks.require(1 - tv(empirical, entrance) == overlap,
                               "exact ordinary overlap")
                envelope = sum(min(Fraction(1, length), 1 / (a * n**2))
                               for n in prefix)
                checks.require(overlap <= envelope, "same-forward-support envelope")

                # Exponentiating -N KL avoids logarithms or approximate
                # arithmetic. This checks equation (9) and its preliminary
                # pointwise bound, not the infinite sparse-orbit asymptotic.
                product_law = prod(length * entrance[n] for n in prefix)
                product_potential = (length**length
                                     * prod(potential[n]**2 for n in prefix)
                                     / mass**length)
                checks.require(product_law == product_potential,
                               "exponentiated exact relative-entropy identity")
                checks.require(product_law <= length**length
                               / (a**length * prod(n**2 for n in prefix)),
                               "exponentiated relative-entropy lower bound")
                laws_checked += 1

                for modulus in sorted({3, 9, 27, 81, 3**10, height + 1}):
                    projected_empirical = projected(empirical, modulus)
                    projected_entrance = projected(entrance, modulus)
                    capacity = height // modulus + 1
                    scale = Fraction(length, capacity)
                    checks.require(scale < modulus, "retained-quotient scale")
                    residue_counts = Counter(n % modulus for n in prefix)
                    checks.require(all(c <= capacity for c in residue_counts.values()),
                                   "complete ordinary-quotient packing")
                    distance = tv(projected_empirical, projected_entrance)
                    for cutoff in sorted({1, min(3, modulus - 1),
                                          min(10, modulus - 1), modulus - 1}):
                        inverse_tail = sum(p for n, p in entrance.items() if n > cutoff)
                        checks.require(inverse_tail <= 1 / (a * cutoff),
                                       "ordinary integer tail bound")
                        forward_interval = sum(p for n, p in empirical.items()
                                               if n <= cutoff)
                        checks.require(tv(empirical, entrance)
                                       >= 1 - inverse_tail - forward_interval,
                                       "ordinary event lower bound")
                        inverse_residue_mass = sum(p for r, p in projected_entrance.items()
                                                   if 1 <= r <= cutoff)
                        forward_residue_mass = sum(p for r, p in projected_empirical.items()
                                                   if 1 <= r <= cutoff)
                        checks.require(inverse_residue_mass >= 1 - inverse_tail,
                                       "ordinary low sources survive projection")
                        checks.require(forward_residue_mass <= cutoff / scale,
                                       "forward residue-set packing")
                        checks.require(distance >= 1 - 1 / (a * cutoff) - cutoff / scale,
                                       "exact projected separation lower bound")
                        projections_checked += 1
    return {
        "scope": "finite stopped-potential laws on enumerated ordinary ancestors",
        "seeds": list(seeds),
        "distinct_ordinary_sources": len(universe),
        "finite_inverse_laws_checked": laws_checked,
        "projected_cutoff_cases_checked": projections_checked,
        "infinite_escape_or_asymptotic_claim": False,
    }


def run_checks():
    checks = Checks()
    compiler = actual_compiler_control(checks)
    finite_source = finite_source_controls(checks)
    return {
        "status": "PASS",
        "arithmetic": "integers and fractions only; no assertions or floating point",
        "compiler": compiler,
        "finite_source": finite_source,
        "exact_checks": sum(checks.counts.values()),
        "checks_by_category": dict(sorted(checks.counts.items())),
        "not_checked": [
            "existence of an escaping ordinary component",
            "infinite inverse entrance-law construction",
            "whole-orbit sparse counting theorem",
            "asymptotic total-variation and relative-entropy rates",
            "missing sibling-pressure lower or forward collision transfer",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
