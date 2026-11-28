"""Genuine native rotations, full reduced cycles, and circular recurrence zero runs."""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json

from check_native_return_curvature import require
from check_near_octave_cycle_denominators import factors, orbit, primitive, remainder
from check_nearcritical_denominator_spectrum import finite_case


def inspect_shifts():
    counts = Counter()
    largest_run = 0
    for p in range(2, 10):
        for word in product((1, 2, 3), repeat=p):
            grade = sum(word)
            if (1 << grade) <= 3**p or not primitive(word):
                continue
            q, numerators, prefixes = orbit(word)
            require(q > 0, "reduced positive closure")
            physical = [y << e for y, e in zip(numerators, prefixes)]
            degree = sum(len(f) - 1 for f in factors(p, grade) if any(remainder(physical, f)))
            counts["closed_cycles"] += 1
            counts["proper_degree_cycles"] += degree < p
            for shift in range(1, p):
                differences = [
                    prefixes[(i + shift) % p] + ((i + shift) // p) * grade - prefixes[i]
                    for i in range(p)
                ]
                breaks = [i for i in range(p) if differences[i] != differences[(i + 1) % p]]
                mismatches = [i for i in range(p) if word[i] != word[(i + shift) % p]]
                require(breaks == mismatches and len(breaks) >= 2, "all true break dates identified")
                lengths = [b - a for a, b in zip(breaks, breaks[1:] + [breaks[0] + p])]
                longest = max(lengths)
                require(sum(lengths) == p and longest < degree, "every constant-ratio run below physical degree")
                require(len(mismatches) * (degree - 1) >= p, "native rotation degree bound")
                counts["proper_shifts"] += 1
                counts["equality_run_bounds"] += longest == degree - 1
                counts["equality_product_bounds"] += len(mismatches) * (degree - 1) == p
                largest_run = max(largest_run, longest)
    require(counts["proper_degree_cycles"] and counts["equality_run_bounds"], "nontrivial finite controls")
    return {"counts": dict(counts), "largest_run": largest_run}


def sheet_case(a, odd_factor, P=41, B=65):
    verified = finite_case(a, odd_factor, 0, P, B)
    power = 1 << a
    g = power * odd_factor
    p = g * P
    t = odd_factor * pow(odd_factor, -1, power)
    shift = t * P
    require(0 < shift < p and p // gcd(p, shift) == power, "true native rotation order")
    def mark(i):
        rank = i * B % P
        sheet = i // P
        return int((rank == 1 and sheet % odd_factor == 0) or
                   (rank == 2 and sheet % power < power // 2))
    e = [i * B // P - mark(i) for i in range(p + 1)]
    word = [v - u for u, v in zip(e, e[1:])]
    q, _, _ = orbit(word)
    changed = {i for i in range(p) if mark(i) != mark((i + shift) % p)}
    mismatch = {i for i in range(p) if word[i] != word[(i + shift) % p]}
    require(len(changed) == 2 * odd_factor and all(i * B % P == 2 for i in changed), "sheet endpoint changes")
    require(mismatch == changed | {(i - 1) % p for i in changed}, "actual native rotations through both boundaries")
    require(len(mismatch) == 4 * odd_factor, "exact fixed-budget mismatch count")
    native_degree = verified["true_dimension"]
    require(Fraction(native_degree, p) == Fraction(1, 2 * odd_factor) + Fraction(1, power), "native Fourier rank")
    return {"sheets":g, "odd_factor":odd_factor, "reduced_period":P, "p":p, "rotation":shift,
            "rotation_order":power, "mismatches":len(mismatch), "degree":native_degree,
            "mismatch_times_sha256":sha256(",".join(map(str, sorted(mismatch))).encode()).hexdigest(),
            "complete_denominator_bits":q.bit_length()}


def equality_family(n):
    word = (1,) + (2,) * (n-1) + (3,) + (2,) * (n-1)
    q, numerators, prefixes = orbit(word)
    p = 2*n
    require(q == 4**n + 3**n and numerators[0] == q-2*3**(n-1), "complete equality-family fraction")
    require(max(numerators) == 2*q-3**n and 2*min(numerators) == q+3**n, "both genuine physical extremes")
    mismatch = sum(word[i] != word[(i+n) % p] for i in range(p))
    physical = [y << e for y, e in zip(numerators, prefixes)]
    degree = sum(len(f)-1 for f in factors(p, sum(word)) if any(remainder(physical, f)))
    require(degree == n+1 and mismatch == 2 and mismatch*(degree-1) == p, "sharp rank at actual half turn")
    return {"period":p, "complete_q":q, "true_degree":degree, "mismatches":mismatch}


if __name__ == "__main__":
    root = Path(__file__).parent
    sources = ("OPTIMAL_ROTATION_DENOMINATOR_ORDER.md", "NEARCRITICAL_DENOMINATOR_SPECTRUM.md",
               "ALL_FIXED_ROTATION_DENOMINATORS.md", "MISMATCH_EVENT_HEIGHT.md", "EXACT_ROTATION_RANK_EQUALITY.md")
    cases = [(a, l) for l in (1, 3, 5) for a in (2, 3, 4)]
    print(json.dumps({"source_sha256":{f:sha256((root/f).read_bytes()).hexdigest() for f in sources},
                      "equality_families":[equality_family(n) for n in range(1, 18)],
                      "finite_rank_tests":inspect_shifts(), "finite_sheet_tests":[sheet_case(*row) for row in cases],
                      "scope":"Both native finite checks use positive primitive rational closures. The limiting mismatch-budget order is proved in the manuscript."}, sort_keys=True, indent=2))
