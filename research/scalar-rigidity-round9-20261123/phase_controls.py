#!/usr/bin/env python3
"""Exact finite controls for complete denominator rigidity.

The infinite structural claims are proved in PHASE_RIGIDITY.md. The
actual scalar is enclosed from literal finite ordinary prefixes, never
identified with a negative rational periodic limit. All checks survive -O.
"""

from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import gcd
import json


class Checks:
    def __init__(self):
        self.counts = Counter()

    def require(self, condition, category):
        if not condition:
            raise RuntimeError(category)
        self.counts[category] += 1


@lru_cache(None)
def factor(n):
    if n < 1:
        raise ValueError("positive factorization argument required")
    factors = []
    p = 2
    while p * p <= n:
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        if k:
            factors.append((p, k))
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


def valuation(n, p):
    if n == 0:
        raise ValueError("finite valuation argument required")
    n, answer = abs(n), 0
    while n % p == 0:
        answer += 1
        n //= p
    return answer


@lru_cache(None)
def order(d):
    if d < 1 or gcd(3, d) != 1:
        raise ValueError("positive unit modulus required")
    if d == 1:
        return 1
    phi = d
    for p, _ in factor(d):
        phi = phi // p * (p - 1)
    result = phi
    for p, _ in factor(phi):
        while result % p == 0 and pow(3, result // p, d) == 1:
            result //= p
    return result


def orbit_from(a, d):
    if d < 2 or gcd(a, d) != 1 or gcd(d, 3) != 1:
        raise ValueError("reduced unit phase required")
    result, value = [], a % d
    for _ in range(order(d)):
        result.append(value)
        value = 3 * value % d
    if value != a % d or len(set(result)) != len(result):
        raise RuntimeError("exact orbit length failed")
    return tuple(result)


def orbits(d):
    seen, result = set(), []
    for a in range(1, d):
        if gcd(a, d) == 1 and a not in seen:
            current = orbit_from(a, d)
            seen.update(current)
            result.append(current)
    return result


def lift(a, d):
    f = F(a, d)
    return f + (f <= F(1, 2))


def means(d, orbit):
    return (sum((lift(a, d) for a in orbit), F()) / len(orbit),
            F(sum(orbit), d * len(orbit)))


def phase_passes(d, orbit, floor):
    total = sum((lift(a, d) for a in orbit), F())
    exponent = 2 * total
    if exponent.denominator != 1:
        raise RuntimeError("phase block exponent is not integral")
    q = floor + 2
    return ((3 * q + 1)**len(orbit)
            < q**len(orbit) * 2**int(exponent))


def support_caps(d):
    powers = dict(factor(d))
    primes = [p for p in powers if p != 2]
    if 3 in primes:
        raise ValueError("residual denominator divisible by three")
    caps, data = {}, {}
    ell_two = max((valuation(order(p), 2) for p in primes), default=0)
    caps[2] = ell_two + 3
    for p in primes:
        t = order(p)
        w = valuation(3**t - 1, p)
        ell = max((valuation(order(q), p) for q in primes if q != p), default=0)
        caps[p] = w + ell
        data[p] = (t, w, ell)
    return caps, data, ell_two


def odd_step(q):
    if q <= 0 or q % 2 == 0:
        raise ValueError("positive odd ordinary source required")
    value = 3 * q + 1
    gap = valuation(value, 2)
    return value // 2**gap, gap


def affine_word(word):
    coefficient, constant, clock = 1, 0, 0
    for gap in word:
        constant = 3 * constant + 2**clock
        coefficient *= 3
        clock += gap
    return coefficient, constant, clock


def scalar_word(word):
    numerator = sum((gap * 3**(len(word) - 1 - i)
                     for i, gap in enumerate(word)), 0)
    return F(numerator, 3**len(word) - 1)


def cylinder(word, repeats, checks):
    coefficient, constant, clock = affine_word(word)
    denominator = coefficient - 2**clock
    checks.require(denominator > 0 and denominator % 2 == constant % 2 == 1,
                   "negative rational shadow has complete odd denominator")
    total_word = word * repeats
    total_clock = clock * repeats
    modulus = 2**(total_clock + 1)
    source = (-constant * pow(denominator, -1, modulus)) % modulus
    checks.require(0 < source < modulus and source % 2 == 1,
                   "literal positive ordinary cylinder source")
    q, partial, actual_clock = source, F(), 0
    for i, prescribed in enumerate(total_word):
        successor, gap = odd_step(q)
        checks.require(gap == prescribed and successor > 0,
                       "every prescribed cylinder valuation is actual")
        checks.require(2**gap * successor == 3 * q + 1,
                       "complete ordinary cylinder edge")
        partial += F(gap, 3**(i + 1))
        actual_clock += gap
        checks.require(2**actual_clock < 3**(i + 1),
                       "every literal finite cylinder pressure clock")
        q = successor
    length = len(total_word)
    target = scalar_word(word)
    checks.require(partial + target / 3**length == target,
                   "exact periodic scalar candidate tail identity")
    checks.require(q.bit_length() <= 4 * length + 1,
                   "ordinary endpoint height funds scalar enclosure")
    lower = partial + F(1, 2 * 3**length)
    upper = partial + F(q.bit_length() + 3, 3**(length + 1))
    error = F(4 * length + 4, 3**(length + 1))
    checks.require(target - error <= lower <= upper <= target + error,
                   "entire actual scalar enclosure approaches fixed low phase")
    return {"word_length": len(word), "repeats": repeats,
            "source": str(source), "prefix_steps": length,
            "endpoint_bits": q.bit_length(), "target": str(target),
            "certified_error": str(error)}


def run_checks():
    checks = Checks()
    fiber_rows = []
    for d, base in [(175, 35), (637, 91), (1375, 275), (15125, 3025),
                    (176, 88), (2912, 728), (2240, 560), (3872, 968)]:
        multiple = d // base
        checks.require(d % base == 0 and
                       set(dict(factor(d))) == set(dict(factor(base))),
                       "full composite fiber domain")
        checks.require(order(d) == multiple * order(base),
                       "complete order ratio funds every fiber")
        minimum = F(2)
        for current in orbits(d):
            base_orbit = orbit_from(current[0] % base, base)
            fibers = defaultdict(set)
            for a in current:
                fibers[a % base].add(a)
            checks.require(set(fibers) == set(base_orbit),
                           "full projected composite coset")
            for a, fiber in fibers.items():
                checks.require(fiber == {a + base * j for j in range(multiple)},
                               "every mixed-modulus residue lift retained")
            mu, _ = means(d, current)
            base_mu, base_nu = means(base, base_orbit)
            expected = (1 + (base_mu - 1) / multiple if multiple % 2
                        else 1 + (base_nu - F(1, 2)) / multiple)
            checks.require(mu == expected,
                           "exact odd-or-even complete fiber mean")
            checks.require(mu > 1 - F(1, 2 * multiple),
                           "strict complete fiber lower mean")
            if multiple >= 4:
                checks.require(phase_passes(d, current, 1),
                               "complete composite denominator fiber contraction")
            minimum = min(minimum, mu)
        fiber_rows.append({"d": d, "base": base, "fiber": multiple,
                           "minimum_mean": str(minimum)})
    checks.require(order(275) == order(55),
                   "cross-prime order obstruction is retained")

    cap_violations = cap_phases = binary_boundary_phases = 0
    for d in range(2, 1537):
        if d % 3 == 0:
            continue
        powers = dict(factor(d))
        caps, data, ell_two = support_caps(d)
        for p, (_, w, ell) in data.items():
            k = powers[p]
            checks.require(valuation(order(d // p**k), p) == ell,
                           "cross-order valuation depends only on prime support")
            if k > w + ell:
                checks.require(order(d) == p * order(d // p),
                               "violated odd support cap produces full prime fiber")
        if not any(k > caps[p] for p, k in powers.items()):
            continue
        cap_violations += 1
        for current in orbits(d):
            mu, _ = means(d, current)
            checks.require(mu >= F(4, 5) and phase_passes(d, current, 31),
                           "every complete phase at a violated support cap contracts")
            cap_phases += 1
            if powers.get(2, 0) == 4 and ell_two == 0:
                checks.require(mu >= F(13, 16),
                               "binary sixteen-times-odd boundary lower mean")
                binary_boundary_phases += 1
    for d, expected in [(5 * 11, 96800), (7 * 13, 1456)]:
        caps, _, _ = support_caps(d)
        bound = 2**caps[2]
        for p, _ in factor(d):
            bound *= p**caps[p]
        checks.require(bound == expected, "exact fixed-support denominator bound")

    doubling_cosets = 0
    for d in range(3, 385):
        if d % 3 == 0:
            continue
        for current in orbits(d):
            mu, nu = means(d, current)
            target = d if d % 2 else d // 2
            transformed = orbit_from((2 * current[0]) % d, d) if d % 2 else \
                orbit_from(current[0] % target, target)
            _, next_nu = means(target, transformed)
            checks.require(mu == 1 + next_nu - nu,
                           "exact doubling or projection defect identity")
            doubling_cosets += 1
    for j in range(2, 9):
        d = 3**j - 2
        checks.require(pow(3, j, d) == 2 % d,
                       "explicit complete doubling-in-tripling family")
        for current in orbits(d):
            mu, _ = means(d, current)
            checks.require(mu == 1 and phase_passes(d, current, 1),
                           "every phase in the complete three-power-minus-two family")
    checks.require(order(23) == 11 and pow(3, 7, 23) == 2,
                   "doubling family beyond negative-one pairing")

    low_rows, cylinders = [], []
    for n in range(2, 15):
        target = F(1, 2) + F(1, 3**n - 1)
        d = target.denominator
        word = [1] * (n - 1) + [2]
        current = orbit_from(target.numerator, d)
        mu, _ = means(d, current)
        checks.require(len(current) == n and mu == F(n + 1, 2 * n),
                       "complete first low-family phase and mean")
        checks.require(scalar_word(word) == target,
                       "first low-family complete scalar word")
        clocks = 0
        for i, gap in enumerate(word):
            clocks += gap
            checks.require(2**clocks < 3**(i + 1),
                           "first low-family complete pressure prefix clocks")
        if n <= 8:
            for repeat in range(1, 7):
                cylinders.append(cylinder(word, repeat, checks))
        low_rows.append({"family": "one terminal two", "n": n,
                         "denominator": d, "mean": str(mu), "target": str(target)})

    for n in range(6, 13):
        d = 2 * (3**n - 1)
        target = F(3**n, d)
        word = [1] * n + [2] * (n - 1) + [3]
        current = orbit_from(target.numerator, d)
        mu, _ = means(d, current)
        checks.require(len(current) == 2 * n and mu == F(3, 4) + F(1, 4 * n),
                       "sharp binary low-family exact phase")
        checks.require(scalar_word(word) == target,
                       "sharp binary low-family complete scalar word")
        checks.require(3**(2 * n) > 2**(3 * n + 1),
                       "sharp low phase survives every finite-floor test")
        checks.require(target < F(5, 8),
                       "sharp low starting scalar below pressure ceiling")
        if n % 2 == 0:
            caps, _, ell_two = support_caps(d)
            checks.require(valuation(d, 2) == ell_two + 3 == caps[2],
                           "binary support cap is attained by low phases")
        if n <= 10:
            for repeat in range(1, 5):
                cylinders.append(cylinder(word, repeat, checks))
        low_rows.append({"family": "sharp binary support", "n": n,
                         "denominator": d, "mean": str(mu), "target": str(target)})

    gate_checks = 0
    for n in range(2, 11):
        denominator = 3**n - 2**(n + 1)
        constant = 3**n - 2**n
        target = F(1, 2) + F(1, 3**n - 1)
        word = [1] * (n - 1) + [2]
        for source in range(1, 256, 2):
            difference_v = valuation(denominator * source + constant, 2)
            q, candidate, clock = source, target, 0
            while True:
                successor, gap = odd_step(q)
                canonical = word[clock % n]
                next_candidate = 3 * candidate - gap
                if gap != canonical:
                    break
                q, candidate, clock = successor, next_candidate, clock + 1
                if clock > difference_v + 1:
                    raise RuntimeError("first departure not found within exact valuation")
            checks.require((gap < canonical) == (difference_v % (n + 1) == n),
                           "exact ordinary first-departure valuation gate")
            if gap > canonical:
                checks.require(next_candidate < F(1, 2),
                               "wrong first-departure gate rejects exact scalar candidate")
            gate_checks += 1

    analytic_primes = []
    for p in [1013, 2003, 2027, 4007, 5003]:
        checks.require(factor(p) == ((p, 1),), "analytic control uses a prime modulus")
        t = order(p)
        harmonic = sum((F(1, j) for j in range(1, (p - 1) // 2 + 1)), F())
        checks.require(25 * p * harmonic**2 < 4 * t**2,
                       "exact rational prime-only Gauss threshold")
        minimum = F(2)
        for current in orbits(p):
            mu, _ = means(p, current)
            checks.require(mu > F(4, 5) and phase_passes(p, current, 31),
                           "all complete cosets at checked analytic prime")
            minimum = min(minimum, mu)
        analytic_primes.append({"prime": p, "order": t, "minimum_mean": str(minimum)})

    return {"status": "PASS", "exact_checks": sum(checks.counts.values()),
            "checks_by_category": dict(sorted(checks.counts.items())),
            "composite_fiber_cases": fiber_rows,
            "support_cap_modulus_limit": 1536,
            "violated_cap_denominators": cap_violations,
            "complete_phases_at_violated_caps": cap_phases,
            "binary_boundary_phases": binary_boundary_phases,
            "doubling_identity_cosets": doubling_cosets,
            "ordinary_first_departure_gates": gate_checks,
            "low_phase_families": low_rows,
            "ordinary_cylinders": cylinders,
            "analytic_prime_controls": analytic_primes,
            "scope": "finite exact controls for the written complete-denominator proofs; actual scalars enclosed from ordinary finite prefixes",
            "unproved": "all-time carry control and arithmetic rigidity of one fixed positive ordinary source"}


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
