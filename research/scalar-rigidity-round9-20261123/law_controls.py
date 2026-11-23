#!/usr/bin/env python3
"""Exact finite controls for the actual-source discounted-scalar law.

No sampled trajectory is required to reach one. Every actual replay has
a prescribed finite length; scalar values are enclosed using R8-G1.
The infinite distribution and measure-type proofs are written mathematics.
"""

from collections import Counter
from fractions import Fraction
from math import comb
import json


class Checks:
    def __init__(self):
        self.counts = Counter()

    def require(self, condition, category):
        if not condition:
            raise RuntimeError(category)
        self.counts[category] += 1


def odd_step(q):
    if q <= 0 or q % 2 == 0:
        raise ValueError("positive odd source required")
    numerator = 3 * q + 1
    gap = (numerator & -numerator).bit_length() - 1
    return numerator >> gap, gap


def prefix(q, depth):
    gaps = []
    for _ in range(depth):
        q, gap = odd_step(q)
        gaps.append(gap)
    return tuple(gaps), q


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for head in range(1, total - length + 2):
        for tail in compositions(total - head, length - 1):
            yield (head,) + tail


def cylinder(word):
    clock = offset = 0
    for gap in word:
        offset = 3 * offset + 2**clock
        clock += gap
    modulus = 2**(clock + 1)
    residue = ((2**clock - offset) * pow(3**len(word), -1, modulus)) % modulus
    return residue, modulus, offset


def source_count(residue, modulus, limit):
    return 0 if residue > limit else 1 + (limit - residue) // modulus


def scalar_prefix(word):
    return sum((Fraction(g, 3**(i + 1)) for i, g in enumerate(word)), Fraction())


def ramp(value, center):
    return min(Fraction(1), max(Fraction(-1), value - center))


def law_bound(limit, depth):
    number = (limit + 1) // 2
    return (Fraction(1, 3**depth) * (2 + Fraction(limit.bit_length() + depth, 3))
            + Fraction(2 * comb(4 * depth, depth), number)
            + 2 * Fraction(81, 128)**depth)


def run_checks():
    checks = Checks()
    word_tables = {}
    word_count = replay_count = 0
    limits = (1, 2, 3, 16, 31, 64, 127, 1024, 4096)
    for depth in range(1, 6):
        words = []
        total_probability = Fraction()
        for clock in range(depth, 4 * depth + 1):
            clock_words = list(compositions(clock, depth))
            checks.require(len(clock_words) == comb(clock - 1, depth - 1),
                           "positive composition count at exact clock")
            for word in clock_words:
                residue, modulus, offset = cylinder(word)
                checks.require(0 < residue < modulus and residue % 2 == 1,
                               "literal cylinder has a positive odd representative")
                checks.require((3**depth * residue + offset) % modulus == 2**clock,
                               "complete endpoint congruence")
                for lift in (0, 1, 3):
                    q = residue + lift * modulus
                    observed, endpoint = prefix(q, depth)
                    checks.require(observed == word, "cylinder representative literal valuation replay")
                    checks.require(2**clock * endpoint == 3**depth * q + offset,
                                   "complete ordinary affine equation")
                    checks.require(endpoint > 0 and endpoint % 2 == 1,
                                   "literal endpoint positive odd")
                    replay_count += 1
                for limit in limits:
                    number = (limit + 1) // 2
                    count = source_count(residue, modulus, limit)
                    checks.require(abs(Fraction(count, number) - Fraction(1, 2**clock))
                                   <= Fraction(1, number),
                                   "progression probability discrepancy")
                weight = Fraction(1, 2**clock)
                total_probability += weight
                words.append((word, residue, modulus, scalar_prefix(word), weight))
                word_count += 1
        checks.require(len(words) == comb(4 * depth, depth), "all retained word count")
        checks.require(total_probability < 1, "independent retained mass below one")
        checks.require(1 - total_probability <= Fraction(81, 128)**depth,
                       "exact independent tail satisfies Chernoff bound")
        word_tables[depth] = words

    # Independently count literal sources before comparing with word cylinders.
    empirical_rows = []
    actual_prefix_replays = 0
    for limit in (31, 128, 1024, 4096):
        number = (limit + 1) // 2
        for depth in range(1, 6):
            actual_words = Counter()
            enclosures = []
            for q in range(1, limit + 1, 2):
                word, endpoint = prefix(q, depth)
                actual_words[word] += 1
                partial = scalar_prefix(word)
                lower = partial + Fraction(1, 2 * 3**depth)
                upper = partial + Fraction(endpoint.bit_length() + 3, 3**(depth + 1))
                checks.require(endpoint <= 2**depth * q, "ordinary endpoint growth bound")
                checks.require(endpoint.bit_length() <= q.bit_length() + depth,
                               "ordinary endpoint bit length bound")
                checks.require(lower < upper, "unconditional actual scalar enclosure is nonempty")
                checks.require(upper - partial <= Fraction(1, 3**depth)
                               * (1 + Fraction(limit.bit_length() + depth, 3)),
                               "uniform actual scalar tail bound")
                enclosures.append((partial, lower, upper))
                actual_prefix_replays += 1
            retained_empirical = 0
            retained_ideal = Fraction()
            l1 = Fraction()
            for word, residue, modulus, _, weight in word_tables[depth]:
                count = actual_words[word]
                checks.require(count == source_count(residue, modulus, limit),
                               "independent literal source count equals cylinder count")
                retained_empirical += count
                retained_ideal += weight
                l1 += abs(Fraction(count, number) - weight)
            checks.require(l1 <= Fraction(comb(4 * depth, depth), number),
                           "retained word total discrepancy")
            ideal_tail = 1 - retained_ideal
            empirical_tail = 1 - Fraction(retained_empirical, number)
            checks.require(empirical_tail <= ideal_tail + l1,
                           "empirical outside mass bounded without orbit convergence")
            for center in (Fraction(0), Fraction(1, 2), Fraction(1), Fraction(3, 2)):
                empirical_low = sum((ramp(lo, center) for _, lo, _ in enclosures), Fraction()) / number
                empirical_high = sum((ramp(hi, center) for _, _, hi in enclosures), Fraction()) / number
                ideal_partial = sum((weight * ramp(partial, center)
                                     for _, _, _, partial, weight in word_tables[depth]), Fraction())
                # Bounds for the complete independent scalar's expectation:
                # discarded word mass costs at most its mass, and the
                # infinite scalar tail costs E[3^-depth H]=3^-depth.
                ideal_low = ideal_partial - ideal_tail
                ideal_high = ideal_partial + ideal_tail + Fraction(1, 3**depth)
                bound = law_bound(limit, depth)
                checks.require(max(empirical_high - ideal_low, ideal_high - empirical_low) <= bound,
                               "full bounded Lipschitz estimate using certified intervals")
            empirical_rows.append({
                "source_limit": limit,
                "odd_sources": number,
                "prefix_length": depth,
                "retained_actual_sources": retained_empirical,
                "retained_ideal_mass": str(retained_ideal),
            })

    # Independent exact tail sums, without enumerating every word.
    for depth in range(1, 129):
        retained = sum((Fraction(comb(clock - 1, depth - 1), 2**clock)
                        for clock in range(depth, 4 * depth + 1)), Fraction())
        checks.require(0 < 1 - retained <= Fraction(81, 128)**depth,
                       "negative binomial tail formula through depth 128")
        checks.require(comb(4 * depth, depth) <= 2**(4 * depth),
                       "word count growth used in weak convergence")

    # A direct finite model of the no-countable-union implication:
    # all truncated endpoints belong to their changing triadic grid.
    grid_cases = 0
    for word, _, _, partial, _ in word_tables[5]:
        completed = partial + Fraction(1, 3**5)
        checks.require((completed * 3**5).denominator == 1,
                       "terminal-one scalar completion remains triadic")
        grid_cases += 1

    return {
        "status": "PASS",
        "scope": "exact finite cylinder and tail controls; infinite law and measure type are written theorems",
        "finite_gap_words": word_count,
        "cylinder_lift_replays": replay_count,
        "actual_prefix_replays": actual_prefix_replays,
        "maximum_actual_prefix_length": 5,
        "actual_source_limits": [31, 128, 1024, 4096],
        "negative_binomial_tail_depths": [1, 128],
        "triadic_completion_cases": grid_cases,
        "bounded_lipschitz_test_functions": "four monotone clipped affine functions per empirical row",
        "empirical_rows": empirical_rows,
        "exact_checks": sum(checks.counts.values()),
        "checks_by_category": dict(sorted(checks.counts.items())),
        "not_claimed": "random dynamics on a fixed orbit, irrational actual scalar, or Collatz convergence",
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
