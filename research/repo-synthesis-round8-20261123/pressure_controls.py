#!/usr/bin/env python3
"""Exact finite controls for scalar phases and pressure clocks.

The infinite families and escaping pressure input remain written proofs.
All checks stay active under python -O. No floating point is used.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd
import json


class Checks:
    def __init__(self):
        self.counts = Counter()

    def require(self, condition, category):
        if not condition:
            raise RuntimeError(category)
        self.counts[category] += 1


def odd_step(q):
    if q == 0 or q % 2 == 0:
        raise ValueError("nonzero odd ordinary source required")
    value = 3 * q + 1
    magnitude = abs(value)
    gap = (magnitude & -magnitude).bit_length() - 1
    return value // 2**gap, gap


def ordinary_certificate(q):
    if q <= 0 or q % 2 == 0:
        raise ValueError("positive odd ordinary source required")
    states, gaps = [q], []
    while states[-1] != 1:
        if len(gaps) >= 2000:
            raise RuntimeError("finite ordinary certificate replay cap")
        successor, gap = odd_step(states[-1])
        states.append(successor)
        gaps.append(gap)
    return states, gaps


def phase_orbits(d):
    if d < 1 or gcd(d, 3) != 1:
        raise ValueError("positive denominator coprime to three required")
    if d == 1:
        return [(0,)]
    seen, result = set(), []
    for start in range(1, d):
        if gcd(start, d) != 1 or start in seen:
            continue
        orbit, value = [], start
        while value not in seen:
            seen.add(value)
            orbit.append(value)
            value = 3 * value % d
        if value != start:
            raise RuntimeError("tripling permutation failed to close")
        result.append(tuple(orbit))
    return result


def minimum_lift(residue, denominator):
    fraction = Fraction(residue, denominator)
    return fraction + (fraction <= Fraction(1, 2))


def profile(d, orbit, checks):
    lifts = [minimum_lift(a, d) for a in orbit]
    charges = [3 * value - lifts[(i + 1) % len(lifts)]
               for i, value in enumerate(lifts)]
    for value, charge in zip(lifts, charges):
        checks.require(Fraction(1, 2) < value <= Fraction(3, 2),
                       "strict minimum-lift endpoints")
        checks.require(charge.denominator == 1 and 1 <= charge <= 3,
                       "integer canonical phase charges")
    total = sum(lifts, Fraction())
    checks.require(2 * total == sum(charges),
                   "complete periodic charge telescoping")
    checks.require((2 * total).denominator == 1,
                   "exact rational block-factor exponent")
    return {"length": len(orbit), "total": total,
            "mean": total / len(orbit), "twice_total": int(2 * total)}


def phase_passes(data, floor):
    """Exact R8-P1 comparison for a supplied verified odd floor Q."""
    q = floor + 2
    return ((3 * q + 1)**data["length"]
            < q**data["length"] * 2**data["twice_total"])


def multiplicative_order(denominator):
    if denominator < 2 or gcd(3, denominator) != 1:
        raise ValueError("unit modulus required")
    value, order = 3 % denominator, 1
    while value != 1:
        value = 3 * value % denominator
        order += 1
        if order > denominator:
            raise RuntimeError("finite order bound failed")
    return order


def valuation(value, prime):
    if value <= 0:
        raise ValueError("positive valuation argument required")
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def clock_upper(j):
    partial = Fraction(2, 3) * sum(
        (Fraction((3**i).bit_length() - 1, 3**i)
         for i in range(1, j + 1)), Fraction())
    return partial + Fraction(8 * (2 * j + 3), 30 * 3**j)


def run_checks():
    checks = Checks()
    finite_floor = []
    for q in range(1, 32, 2):
        states, gaps = ordinary_certificate(q)
        for a, b, gap in zip(states, states[1:], gaps):
            checks.require(a > 0 and b > 0 and a % 2 == b % 2 == 1,
                           "positive ordinary finite-floor domain")
            checks.require(2**gap * b == 3 * a + 1,
                           "complete ordinary finite-floor transition")
        checks.require(states[-1] == 1,
                       "all odd sources through 31 explicitly reach one")
        finite_floor.append({"source": q, "odd_steps": len(gaps),
                             "binary_clock": sum(gaps),
                             "maximum_odd_state": max(states)})
    checks.require(10**4 < 3**4 * 2**7,
                   "unconditional seven-eighths phase threshold")
    checks.require(100**5 < 33**5 * 2**8,
                   "verified-floor four-fifths phase threshold")

    table_expected = {
        11: (2, Fraction(4, 5)), 26: (4, Fraction(5, 6)),
        35: (2, Fraction(5, 6)), 46: (2, Fraction(19, 22)),
        52: (4, Fraction(5, 6)), 85: (4, Fraction(13, 16)),
        109: (4, Fraction(23, 27)),
    }
    finite_denominators = []
    for d, (expected_count, expected_mean) in table_expected.items():
        orbits = phase_orbits(d)
        profiles = [profile(d, orbit, checks) for orbit in orbits]
        checks.require(len(orbits) == expected_count,
                       "complete finite-table tripling orbit count")
        checks.require(min(data["mean"] for data in profiles) == expected_mean,
                       "complete finite-table minimum mean")
        checks.require(sum(map(len, orbits)) ==
                       sum(gcd(a, d) == 1 for a in range(1, d)),
                       "every reduced numerator in finite table covered")
        for data in profiles:
            checks.require(phase_passes(data, 31),
                           "exact finite-floor contraction for every listed phase")
        finite_denominators.append({"denominator": d, "orbits": len(orbits),
                                   "minimum_mean": str(expected_mean)})

    two_power_rows = []
    for k in range(13):
        d = 2**k
        orbits = phase_orbits(d)
        profiles = [profile(d, orbit, checks) for orbit in orbits]
        means = sorted(data["mean"] for data in profiles)
        if k == 0:
            expected = [Fraction(1)]
        elif k == 1:
            expected = [Fraction(3, 2)]
        elif k == 2:
            expected = [Fraction(1)]
        elif k == 3:
            expected = [Fraction(3, 4), Fraction(5, 4)]
        else:
            expected = [1 - Fraction(2, d), 1 + Fraction(2, d)]
        checks.require(means == expected, "complete two-power phase mean formula")
        for orbit, data in zip(orbits, profiles):
            if k >= 3:
                checks.require(data["length"] == d // 4,
                               "exact order for every two-power coset")
            if k >= 4:
                residues = {a % 8 for a in orbit}
                checks.require(residues in ({1, 3}, {5, 7}),
                               "complete two-power residue coset")
                checks.require(sum(2 * a < d for a in orbit) * 2 == len(orbit),
                               "half of each two-power coset below one half")
                checks.require(set((a + d // 2) % d for a in orbit) == set(orbit),
                               "half-period translation preserves complete coset")
            if not (k == 3 and data["mean"] == Fraction(3, 4)):
                checks.require(phase_passes(data, 1),
                               "all claimed two-power phases contract")
            else:
                checks.require(set(orbit) == {5, 7} and not phase_passes(data, 31),
                               "unresolved denominator-eight phase retained")
        two_power_rows.append({"exponent": k, "denominator": d,
                               "means": list(map(str, means))})
    checks.require(Fraction(2) * Fraction(5, 6)**4 == Fraction(625, 648),
                   "exact worst two-power block factor")

    for prime, first_negative_exponent in ((5, 2), (7, 3), (17, 8)):
        for k in range(1, 7):
            d = prime**k
            exponent = first_negative_exponent * prime**(k - 1)
            checks.require(pow(3, exponent, d) == d - 1,
                           "explicit prime-power negative-one lift")
            checks.require(pow(3, exponent, 2 * d) == 2 * d - 1,
                           "explicit doubled negative-one lift")
            if prime == 7:
                checks.require(pow(3, exponent, 4 * d) == 4 * d - 1,
                               "explicit quadrupled seven-power lift")

    prime_power_rows = []
    for prime, largest_k in ((5, 4), (7, 4), (11, 4), (13, 3), (17, 3)):
        t = multiplicative_order(prime)
        w = valuation(3**t - 1, prime)
        base_d = prime**w
        base_info = {}
        for orbit in phase_orbits(base_d):
            data = profile(base_d, orbit, checks)
            for a in orbit:
                base_info[a] = (set(orbit), data)
        for k in range(w + 1, largest_k + 1):
            d, multiple = prime**k, prime**(k - w)
            checks.require(multiplicative_order(d) == t * multiple,
                           "odd-prime-power binomial order formula")
            profiles = []
            for orbit in phase_orbits(d):
                data = profile(d, orbit, checks)
                profiles.append(data)
                base_orbit, base_data = base_info[orbit[0] % base_d]
                fibers = defaultdict(set)
                for a in orbit:
                    fibers[a % base_d].add(a)
                checks.require(set(fibers) == base_orbit,
                               "full reduction onto one base orbit")
                for a, fiber in fibers.items():
                    checks.require(fiber == {a + j * base_d for j in range(multiple)},
                                   "every ordinary residue fiber retained")
                checks.require(data["mean"] ==
                               1 + (base_data["mean"] - 1) / multiple,
                               "exact odd-prime-power fiber mean identity")
                checks.require(data["mean"] > Fraction(9, 10),
                               "strict odd-prime-power phase lower mean")
                checks.require(phase_passes(data, 1),
                               "every tested high odd-prime-power phase contracts")
            prime_power_rows.append({"prime": prime, "base_order": t,
                                     "base_valuation": w, "exponent": k,
                                     "orbits": len(profiles),
                                     "minimum_mean": str(min(
                                         data["mean"] for data in profiles))})
    unresolved_121 = [profile(121, orbit, checks) for orbit in phase_orbits(121)]
    checks.require(min(data["mean"] for data in unresolved_121) == Fraction(3, 5),
                   "exceptional eleven-square low phase retained")

    # This is a negative ordinary control, not a positive counterexample.
    checks.require(odd_step(-5) == (-7, 1) and odd_step(-7) == (-5, 2),
                   "literal negative denominator-eight cycle")
    checks.require(3 * Fraction(5, 8) - 1 == Fraction(7, 8) and
                   3 * Fraction(7, 8) - 2 == Fraction(5, 8),
                   "exact negative-cycle scalar phases")

    clock_expectations = {
        1: Fraction(2, 3), 2: Fraction(88, 135), 3: Fraction(256, 405),
        4: Fraction(764, 1215), 5: Fraction(2282, 3645),
        6: Fraction(152, 243), 20: Fraction(32706613742, 52301766015),
    }
    checks.require(3**5 < 2**8 and 3**2 > 2**3,
                   "exact logarithmic rational comparisons")
    checks.require([(3**j).bit_length() - 1 for j in range(1, 7)] ==
                   [1, 3, 4, 6, 7, 9], "first six exact pressure clock floors")
    for j, expected in clock_expectations.items():
        checks.require(clock_upper(j) == expected,
                       "exact finite pressure clock upper bound")
    checks.require(clock_upper(40) < Fraction(625344347433389, 10**15),
                   "forty-term exact pressure decimal enclosure")
    lower_40 = Fraction(2, 3) * sum(
        (Fraction((3**j).bit_length() - 1, 3**j) for j in range(1, 41)), Fraction())
    checks.require(lower_40 > Fraction(5, 8),
                   "pressure ceiling does not exclude five eighths")

    return {
        "status": "PASS",
        "scope": "exact finite ordinary certificates, complete listed modular domains, and rational pressure clock bounds",
        "exact_checks": sum(checks.counts.values()),
        "checks_by_category": dict(sorted(checks.counts.items())),
        "verified_ordinary_floor": 31,
        "finite_floor_certificates": finite_floor,
        "excluded_finite_denominators": finite_denominators,
        "two_power_rows": two_power_rows,
        "odd_prime_power_rows": prime_power_rows,
        "pressure_clock_upper_bounds": {str(j): str(value)
                                         for j, value in clock_expectations.items()},
        "forty_term_upper_bound": str(clock_upper(40)),
        "unproved": "arithmetic rigidity of the actual scalar for every positive ordinary source, including surviving low phases and irrational values",
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
