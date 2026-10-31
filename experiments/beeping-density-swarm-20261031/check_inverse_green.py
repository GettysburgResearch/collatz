#!/usr/bin/env python3
"""Exact bounded checks for inverse Green and first-hit transport identities.

No external density theorem, asymptotic limit, or Collatz conclusion is tested.
All acceptance checks remain active under optimized Python.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import json
import math
from pathlib import Path


def require(ok: bool, detail: object) -> None:
    if not ok:
        raise RuntimeError(str(detail))


def odd_step(x: int) -> tuple[int, int]:
    require(x > 0 and x % 2 == 1, ("positive odd input", x))
    z = 3 * x + 1
    a = (z & -z).bit_length() - 1
    return z >> a, a


def transport(f: dict[int, F]) -> dict[int, F]:
    out: defaultdict[int, F] = defaultdict(F)
    for x, mass in f.items():
        t, a = odd_step(x)
        out[t] += F(3, 1 << a) * mass
    return dict(out)


def harmonic(f: dict[int, F]) -> F:
    return sum((mass / x for x, mass in f.items()), F(0))


def defect(f: dict[int, F]) -> F:
    return sum((mass / (x * (3 * x + 1)) for x, mass in f.items()), F(0))


def transport_checks() -> dict:
    starts = [
        {1: F(1)},
        {x: F(1) for x in range(101, 401, 2)},
        {x: F(1, x + 1) for x in range(1, 300, 2)},
    ]
    identities = 0
    rows = []
    for f0 in starts:
        f = dict(f0)
        h0 = harmonic(f)
        paid = F(0)
        occupation: defaultdict[int, F] = defaultdict(F)
        for q in range(21):
            for t, mass in f.items():
                occupation[t] += mass
            g = transport(f)
            loss = defect(f)
            require(harmonic(g) + loss == harmonic(f), ("one-step defect", q))
            paid += loss
            require(harmonic(g) + paid == h0, ("cumulative defect", q))
            f = g
            identities += 2
        for t, mass in occupation.items():
            require(mass <= t * (3 * t + 1) * h0, ("Green target bound", t))
        rows.append({"initial_sources": len(f0), "initial_harmonic_mass": str(h0),
                     "final_harmonic_mass": str(harmonic(f)),
                     "accumulated_exact_loss": str(paid),
                     "distinct_occupation_targets": len(occupation)})
    return {"identities": identities, "rows": rows,
            "fixed_point_control": {"root": 1, "multiplier": "3/4", "full_Green_mass": "4"}}


def word_rows(t: int, max_depth: int, max_total: int):
    """Enumerate all legal inverse words under both explicit finite caps."""
    stack = [(t, (), 0, F(1), True)]
    while stack:
        x, word, total, weight, first_hit = stack.pop()
        yield x, word, total, weight, first_hit
        if len(word) == max_depth:
            continue
        for a in range(1, max_total - total + 1):
            num = (1 << a) * x - 1
            if num % 3:
                continue
            source = num // 3
            require(source > 0 and source % 2, ("integral positive inverse", t, word, a))
            stack.append((source, word + (a,), total + a,
                          weight * F(3, 1 << a), first_hit and source != t))


def word_checks() -> dict:
    words = first_hits = packing_checks = renewal_checks = 0
    max_depth, max_total = 6, 14
    for t in range(1, 52, 2):
        unique = {}
        raw: defaultdict[tuple[int, int], F] = defaultdict(F)
        first: defaultdict[tuple[int, int], F] = defaultdict(F)
        rows = list(word_rows(t, max_depth, max_total))
        for x, word, total, weight, first_hit in rows:
            q = len(word)
            raw[q, total] += weight
            current = x
            product = F(1)
            physical = [x]
            for a in reversed(word):
                nxt, actual_a = odd_step(current)
                require(actual_a == a, ("exact valuation replay", t, word, x))
                product *= F(3 * current, 3 * current + 1)
                current = nxt
                physical.append(current)
            require(current == t and weight / t == product / x, ("path cocycle", t, word))
            require(first_hit == (t not in physical[:-1]), ("first-hit convention", t, word))
            if first_hit:
                require(len(set(physical)) == len(physical), ("simple first-hit path", t, word))
                require(x not in unique, ("cross-depth collision", t, x, word, unique.get(x)))
                unique[x] = word
                first[q, total] += weight
                first_hits += 1
            words += 1
        for q in range(max_depth + 1):
            for a in range(max_total + 1):
                if t == 1:
                    expected = sum((F(3, 4) ** k * first[q-k, a-2*k]
                                    for k in range(q + 1) if a >= 2*k), F(0))
                    require(raw[q, a] == expected, ("exact graded renewal", q, a))
                else:
                    require(raw[q, a] == first[q, a], ("no return in bounded word set", t, q, a))
                renewal_checks += 1
        for Q in range(1, 7):
            selected = [(x, w) for x, word, a, w, hit in rows
                        if hit and len(word) <= Q and a <= 6*Q]
            K, M = F(3, 2) ** Q, t * 2 ** (6*Q)
            require(all(w <= min(K, F(t, x)) and x <= M for x, w in selected),
                    ("common source packing premises", t, Q))
            require(sum((w for x, w in selected), F(0)) <= t * (1 + 5*Q),
                    ("rational packing majorant", t, Q))
            packing_checks += 1
    require(sum((F(5**k, math.factorial(k)) for k in range(10)), F(0)) > 96,
            "finite exponential series certifies log96<5")
    return {"targets": 26, "max_depth": max_depth, "max_total_valuation": max_total,
            "legal_words": words, "first_hit_words": first_hits,
            "graded_renewal_checks": renewal_checks, "packing_checks": packing_checks}


def exact_laws(max_q: int) -> list[tuple[list[int], int]]:
    """Direct inverse transfer; every infinite geometric exponent tail is summed."""
    laws = [([1], 1)]
    for q in range(1, max_q + 1):
        previous, denominator = laws[-1]
        modulus, previous_modulus = 3 ** q, 3 ** (q - 1)
        period = 2 * previous_modulus
        updated = [0] * modulus
        two_power = 1
        for a in range(1, period + 1):
            two_power = 2 * two_power % modulus
            coefficient = 3 * (1 << (period - a))
            for t in range(two_power % 3, modulus, 3):
                parent = ((two_power * t - 1) // 3) % previous_modulus
                updated[t] += coefficient * previous[parent]
        new_denominator = denominator * ((1 << period) - 1)
        require(two_power == 1 and sum(updated) == modulus * new_denominator,
                ("infinite geometric law normalization", q))
        laws.append((updated, new_denominator))
    return laws


def density(laws, q: int, t: int) -> F:
    numerator, denominator = laws[q]
    return F(numerator[t % len(numerator)], denominator)


def reference_checks(laws) -> dict:
    checks, first_checks = 0, 0
    examples = []
    for t in range(1, 502, 2):
        # Finite certificate that these particular targets are not additional cycles.
        current, seen = t, set()
        while current != 1 and current not in seen:
            seen.add(current)
            require(len(seen) < 10000, ("bounded orbit certificate exhausted", t))
            current = odd_step(current)[0]
        require(current == 1, ("unexpected bounded cycle", t))
        kappa = 4 if t == 1 else 1
        cumulative, first_cumulative = F(1), F(1)
        for Q in range(1, len(laws)):
            rho = density(laws, Q, t)
            first = rho - F(3, 4) * density(laws, Q-1, t) if t == 1 else rho
            require(first >= 0, ("first-hit nonnegative", t, Q))
            cumulative += rho
            first_cumulative += first
            upper = t * (1 + 5*Q) + F(9, 8) * F(64, 81) ** Q
            require(first_cumulative <= upper, ("first-hit cumulative bound", t, Q))
            require(cumulative <= kappa * upper, ("raw cumulative bound", t, Q))
            require(cumulative <= kappa * first_cumulative, ("renewal cumulative bound", t, Q))
            checks += 2
            first_checks += 2
        if t in (1, 3, 5, 7, 11, 27):
            examples.append({"target": t, "rho": [str(density(laws, q, t)) for q in range(len(laws))],
                             "cumulative": str(cumulative), "first_hit_cumulative": str(first_cumulative)})
    return {"targets": 251, "max_reference_level": len(laws)-1,
            "cumulative_checks": checks, "renewal_and_nonnegativity_checks": first_checks,
            "examples": examples}


def frontier(t: int, threshold: int, D: int, max_letter: int = 6):
    output = []
    stack = [(t, (), F(1))]
    while stack:
        x, word, weight = stack.pop()
        if x >= threshold or len(word) == D or x % 3 == 0:
            output.append((x, word, weight))
            continue
        for a in range(1, max_letter + 1):
            num = (1 << a)*x-1
            if num % 3 == 0:
                stack.append((num//3, word+(a,), weight*F(3, 1 << a)))
    return output


def prefix_free(words) -> bool:
    words = list(words)
    return len(set(words)) == len(words) and all(
        not (len(a) < len(b) and b[:len(a)] == a)
        for a in words for b in words)


def frontier_checks(laws) -> dict:
    rows, comparisons = [], 0
    for t in (1, 5, 7, 11, 27, 97):
        for D in (1, 2, 3):
            for threshold in (20, 100):
                W = frontier(t, threshold, D)
                require(prefix_free(w for x, w, mass in W), ("frontier premise", t, D, threshold))
                for Q in range(4):
                    lhs = sum((weight * sum((density(laws, q, x) for q in range(Q+1)), F(0))
                               for x, word, weight in W), F(0))
                    rhs = sum((density(laws, q, t) for q in range(D+Q+1)), F(0))
                    require(lhs <= rhs, ("transported prefix-free profile", t, D, Q, threshold))
                    comparisons += 1
                rows.append({"root": t, "D": D, "threshold": threshold, "words": len(W)})
    require(not prefix_free([(), (2,)]), "non-prefix-free guard")
    bad_lhs = (F(1) + F(3, 4)) * (density(laws, 0, 1) + density(laws, 1, 1)) / 2
    bad_rhs = sum((density(laws, q, 1) for q in range(3)), F(0)) / 2
    require(bad_lhs > bad_rhs, ("retained prefix-free failure", bad_lhs, bad_rhs))
    return {"frontiers": len(rows), "exact_profile_comparisons": comparisons, "rows": rows,
            "non_prefix_free_counterexample": {"root": 1, "words": [[], [2]], "Q": 1,
                                               "lhs": str(bad_lhs), "rhs": str(bad_rhs)}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    laws = exact_laws(6)
    report = {"schema": "collatz-inverse-green/v1", "status": "PASS",
              "scope": "exact bounded replay; not proof of asymptotic limits, external inputs, or Collatz",
              "harmonic_transport": transport_checks(), "first_hit_words": word_checks(),
              "exact_reference": reference_checks(laws), "transported_frontiers": frontier_checks(laws),
              "external_density_or_Lean_replayed": False, "full_Collatz_proved": False}
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(json.dumps({"status": "PASS", "output": str(args.output) if args.output else None,
                      "legal_words": report["first_hit_words"]["legal_words"],
                      "reference_targets": report["exact_reference"]["targets"],
                      "frontier_comparisons": report["transported_frontiers"]["exact_profile_comparisons"]}))


if __name__ == "__main__":
    main()
