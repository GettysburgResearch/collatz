#!/usr/bin/env python3
"""Exact finite ordinary-source controls for the adaptive Green comparison."""
from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from math import isqrt

B = Fraction(1) + Fraction(1, 26) + Fraction(1, 12 * 13**2)
MASS_CONSTANT = 1 + Fraction(7, 12) / (1 - B / 3) ** 2


def edge(x):
    n = 3 * x + 1
    e = (n & -n).bit_length() - 1
    return e, n >> e


def boost(r):
    d = max(13, r)
    return 1 + Fraction(1, 2*d) + Fraction(1, 12*d*d)


def residue(x, modulus):
    r = x % modulus
    return r if r % 2 else r + modulus


def digest_integers(values):
    h = hashlib.sha256()
    for n in values:
        data = n.to_bytes(max(1, (n.bit_length() + 7) // 8), 'big')
        h.update(len(data).to_bytes(8, 'big'))
        h.update(data)
    return h.hexdigest()


def cohort_controls(V):
    mass = [Fraction(0) for _ in range(3)]
    rows = defaultdict(Fraction)
    count = Counter()
    ages = Counter()
    data = []
    for v in range(1, V + 1, 2):
        x, A, j, three, psize = v, 0, 0, 1, 2
        a = Fraction(1)
        while True:
            r = residue(x, three)
            m = v % psize
            relift = x - (v // psize) * 2 * three
            assert m > 0 and relift == r
            principal = m
            for _ in range(j):
                _, principal = edge(principal)
            assert principal == r
            before = (v - 1)//2 >= 2**A
            assert before == (r != x)
            if not before:
                break
            rows[j] += Fraction(1, r)
            count[j] += 1
            a *= boost(r)
            e, x = edge(x)
            A += e
            j += 1
            three *= 3
            psize <<= e
        ages[j] += 1
        for p in range(1, 4):
            mass[p-1] += a**p
        data.extend((v, j, a.numerator, a.denominator))
    p1_upper = V * MASS_CONSTANT
    assert mass[0] <= p1_upper
    for p in (2, 3):
        cp = Fraction(7*p, 12) * B**(p-1)
        assert mass[p-1] <= V*(1+cp/(1-B**p/3)**2)
    for j, val in rows.items():
        assert val <= Fraction(V*(j+1), 3**j)
    return {
        "V": V,
        "odd_sources": (V+1)//2,
        "ages": sorted(ages.items()),
        "moment_per_V_floored_millionths": [m*10**6//V for m in mass],
        "p1_proved_constant": str(MASS_CONSTANT),
        "prebirth_row_counts": sorted(count.items()),
        "row_bound_ratios_floored_millionths": [
            [j, (r * 3**j * 10**6) // (V * (j+1))] for j,r in sorted(rows.items())
        ],
        "individual_source_fraction_sha256": digest_integers(data),
    }


def sqrt_lower(x, bits=48):
    return isqrt((x.numerator << (2*bits))//x.denominator)


def path_controls(V):
    paths, incidences, phase_returns, high_edges = 0, 0, 0, 0
    visits = Counter()
    sum_lower = Counter()
    sum_rounded_lower = Counter()
    max_gain = defaultdict(Fraction)
    best_state = 1
    for v in range(1, V+1, 2):
        paths += 1
        seen = set()
        x, three, two, j, A = v, 1, 1, 0, 0
        raw, norm_sq = Fraction(1), Fraction(1, v**3)
        old_phase = {}
        while x not in seen:
            seen.add(x)
            best_state = max(best_state, x)
            incidences += 1
            r = residue(x, three)
            ratio = Fraction(three, two*x)
            assert norm_sq == ratio**3 * raw**2
            phase = (j % 2, A % 2)
            round_sq = norm_sq / (3**phase[0] * 2**phase[1])
            assert round_sq == Fraction(3**(3*j//2), 2**((3*A+1)//2))**2 * raw**2 / x**3
            if phase in old_phase:
                assert round_sq > old_phase[phase]
                phase_returns += 1
            if x >= 13:
                old_phase[phase] = round_sq
            else:
                old_phase.clear()
            visits[x] += 1
            sum_lower[x] += sqrt_lower(norm_sq)
            sum_rounded_lower[x] += sqrt_lower(round_sq)
            max_gain[x] = max(max_gain[x], ratio)
            b = boost(r)
            factor_sq = b**2 * Fraction(3*x, 3*x+1)**3
            if x >= 13:
                assert factor_sq > 1
                high_edges += 1
            else:
                old_phase.clear()
            raw *= b
            norm_sq *= factor_sq
            e, x = edge(x)
            three *= 3
            two <<= e
            j += 1
            A += e
    scale = 2**48
    ratios = []
    for x, n in visits.items():
        q = max_gain[x]
        # Each enclosed irrational sum lies in [L/scale, (L+n)/scale].
        assert (sum_lower[x]+n)**2 >= q**3 * scale**2
        assert sum_rounded_lower[x] <= sum_lower[x]
        assert 6*(sum_rounded_lower[x]+n)**2 >= sum_lower[x]**2
        ratios.append((Fraction((sum_lower[x]+n)**2, scale**2)/q, x))
    largest_ratio, example = max(ratios)
    return {
        "source_cutoff":V, "paths":paths, "distinct_targets":len(visits),
        "first_arrival_incidences":incidences, "positive_high_edge_tests":high_edges,
        "strict_same_parity_return_tests":phase_returns, "largest_target":best_state,
        "largest_enclosed_u_squared_over_finite_q_ceiling_millionths":
            -((-10**6*largest_ratio)//1),
        "largest_ratio_target":example,
        "target_moments_sha256":digest_integers(
            z for x in sorted(visits) for z in (x,visits[x],sum_lower[x],
                                                sum_rounded_lower[x],max_gain[x].numerator,
                                                max_gain[x].denominator)),
    }


if __name__ == "__main__":
    out = {
        "arithmetic":"integer and Fraction throughout, square roots enclosed on denominator 2^48",
        "cohorts":[cohort_controls(V) for V in (127, 1023, 4095, 16383)],
        "finite_first_arrivals":path_controls(2047),
    }
    print(json.dumps(out, sort_keys=True, indent=2))
