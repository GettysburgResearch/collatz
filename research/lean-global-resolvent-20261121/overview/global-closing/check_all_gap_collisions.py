#!/usr/bin/env python3
"""Exact finite controls for ACTUAL_ALL_GAP_COLLISIONS.md.

These checks test identities, finite inequalities, boundary conventions and
deliberately false variants. They do not verify asymptotic statements, an
escaping orbit, the source-qualified stationary extraction, or Collatz.
Only Python integers and fractions are used in the checks.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
import json


def require(condition, message):
    """Keep every mathematical check active under python -O."""
    if not condition:
        raise AssertionError(message)


def valuation(n, prime):
    require(n != 0, 'Exact check failed (original source line 19)')
    n = abs(n)
    result = 0
    while n % prime == 0:
        n //= prime
        result += 1
    return result


def step(q):
    a = valuation(3 * q + 1, 2)
    return (3 * q + 1) // 2**a, a


def distinct_prefix(p, cap):
    states, exponents, seen = [], [], set()
    q = p
    while len(states) < cap and q not in seen:
        seen.add(q)
        states.append(q)
        q, a = step(q)
        exponents.append(a)
    return states, exponents[: len(states) - 1]


def words(exponents, m):
    return Counter(tuple(exponents[i:i + m])
                   for i in range(len(exponents) - m + 1))


def entropy_product(counts):
    """exp(M H(P)), as an exact rational for counts totaling M."""
    total = sum(counts.values())
    denominator = 1
    for count in counts.values():
        denominator *= count**count
    return Fraction(total**total, denominator)


def word_affine(word):
    total, carry = 0, 0
    for a in word:
        carry = 3 * carry + 2**total
        total += a
    return total, carry


def realized_word(p, d):
    result = []
    q = p
    for _ in range(d):
        q, a = step(q)
        result.append(a)
    return tuple(result), q


checks = Counter()
fixtures = []
reduced_example = None
for source in (5, 7, 41, 703, 871, 9257):
    states, exponents = distinct_prefix(source, 64)
    fixtures.append({"source": source, "distinct_states": len(states),
                     "maximum_state": max(states)})
    require(len(set(states)) == len(states), 'Exact check failed (original source line 82)')
    require(all(q > 0 and q % 2 and q % 3 for q in states), 'Exact check failed (original source line 83)')

    # Use all actual gaps, including the largest gap and all starting states.
    for i in range(len(states)):
        total, carry = 0, 0
        for j in range(i + 1, len(states)):
            carry = 3 * carry + 2**total
            total += exponents[j - 1]
            d = j - i
            p, q = states[i], states[j]
            require(2**total * q == 3**d * p + carry, 'Exact check failed (original source line 93)')
            denominator = 2**total - 3**d
            divisor = gcd(carry, abs(denominator))
            b, c = denominator // divisor, carry // divisor
            require(gcd(divisor, 6) == 1 and gcd(abs(b), 6) == 1, 'Exact check failed (original source line 97)')
            require((p - q) % divisor == 0, 'Exact check failed (original source line 98)')
            numerator = b * p - c
            require(numerator == 2**total * ((p - q) // divisor), 'Exact check failed (original source line 100)')
            require(valuation(numerator, 2) == total + valuation(p - q, 2), 'Exact check failed (original source line 101)')
            require(valuation(numerator, 3) == valuation(p - q, 3), 'Exact check failed (original source line 102)')
            if divisor > 1 and reduced_example is None:
                reduced_example = {"source_index": i, "end_index": j,
                                   "p": p, "q": q, "A": total,
                                   "C": carry, "D": denominator,
                                   "gcd": divisor}
            for m in range(valuation(p - q, 3) + 1):
                modulus = 2**(total + 1) * 3**m
                require(numerator % modulus == 0, 'Exact check failed (original source line 110)')
                require(modulus <= (p + 1) * max(c, abs(b)), 'Exact check failed (original source line 111)')
                checks["reduced_anchor_joint_divisibility"] += 1
            checks["all_gap_affine_and_valuation_identity"] += 1

    for N in sorted({len(states), min(8, len(states)), min(17, len(states))}):
        if N < 3:
            continue
        qs, es = states[:N], exponents[:N - 1]
        for m in range(1, N):
            wm = words(es, m)
            M = N - m
            require(sum(wm.values()) == M, 'Exact check failed (original source line 122)')
            pm = entropy_product(wm)
            for k in range(1, m + 1):
                wk = words(es, k)
                pk = entropy_product(wk)
                blocks = (m + k - 1) // k
                # (N-m)H_m <= ceil(m/k)(N-k)H_k.
                require(pm <= pk**blocks, 'Exact check failed (original source line 129)')
                checks["exact_sliding_block_entropy"] += 1

            Q = 3**m
            endpoints = qs[m:]
            residues = Counter(q % Q for q in endpoints)
            for w in wm:
                A, C = word_affine(w)
                residue = C * pow(2**A, -1, Q) % Q
                require(all(qs[j] % Q == residue for j in range(m, N)
                           if tuple(es[j - m:j]) == w), 'Exact check failed (original source line 138)')
                checks["backward_window_endpoint_residue"] += 1
            for X in sorted({1, Q - 1, min(Q - 1, max(qs)),
                             min(Q - 1, sorted(qs)[N // 2])}):
                retained = [j for j in range(m, N) if qs[j] <= X]
                selected_words = [tuple(es[j - m:j]) for j in retained]
                require(len(set(selected_words)) == len(selected_words), 'Exact check failed (original source line 145)')
                K = len(retained)
                # K log K <= (N-m)H_m; 0^0 is interpreted as one.
                require((K**K if K else 1) <= pm, 'Exact check failed (original source line 148)')
                checks["exact_height_occupation_entropy"] += 1

            word_energy = sum(c * c for c in wm.values())
            endpoint_energy = sum(c * c for c in residues.values())
            require(endpoint_energy >= word_energy, 'Exact check failed (original source line 153)')
            # Col(P) >= exp(-H(P)), using integer powers only.
            require(Fraction(word_energy, M * M)**M >= 1 / pm, 'Exact check failed (original source line 155)')
            full_residues = Counter(q % Q for q in qs)
            require(sum(c * c for c in full_residues.values()) >= endpoint_energy, 'Exact check failed (original source line 157)')
            checks["collision_entropy_lower_bound"] += 1

        for m in range(1, 7):
            Q = 3**m
            full_energy = sum(c * c for c in Counter(q % Q for q in qs).values())
            lag_counts = [sum((qs[i + d] - qs[i]) % Q == 0
                              for i in range(N - d))
                          for d in range(1, N)]
            require(full_energy == N + 2 * sum(lag_counts), 'Exact check failed (original source line 166)')
            for L in sorted({0, 1, N // 2, N - 1}):
                short_energy = N + 2 * sum(lag_counts[:L])
                require(short_energy <= N * (2 * L + 1), 'Exact check failed (original source line 169)')
                require(full_energy - short_energy == 2 * sum(lag_counts[L:]), 'Exact check failed (original source line 170)')
                checks["all_gap_decomposition_and_short_gap_bound"] += 1

# Check the complete exact-valuation cylinder and return CRT class on an
# exhaustive finite family of words. This is not an asymptotic experiment.
for d in range(1, 5):
    for w in product(range(1, 5), repeat=d):
        A, C = word_affine(w)
        D = 2**A - 3**d
        two_modulus = 2**(A + 1)
        a = ((2**A - C) * pow(3**d, -1, two_modulus)) % two_modulus
        require(a % 2 == 1, 'Exact check failed (original source line 181)')
        for m in range(1, 5):
            Q = 3**m
            r = C * pow(D, -1, Q) % Q
            t = ((r - a) * pow(two_modulus, -1, Q)) % Q
            p = a + two_modulus * t
            require(p > 0 and p % 3, 'Exact check failed (original source line 187)')
            actual_word, endpoint = realized_word(p, d)
            require(actual_word == w, 'Exact check failed (original source line 189)')
            require((endpoint - p) % Q == 0, 'Exact check failed (original source line 190)')
            actual_word2, endpoint2 = realized_word(p + two_modulus * Q, d)
            require(actual_word2 == w, 'Exact check failed (original source line 192)')
            require((endpoint2 - p - two_modulus * Q) % Q == 0, 'Exact check failed (original source line 193)')
            # Losing the last parity bit does not retain the exact word.
            wrong_word, _ = realized_word(p + 2**A, d)
            require(wrong_word != w, 'Exact check failed (original source line 196)')
            checks["exact_word_and_return_crt"] += 1

negative_controls = {}
# Without the finite-window boundary factor, subadditivity does not give the
# proposed inequality even for one finite seven-letter word.
synthetic = [1, 1, 1, 2, 1, 1, 1]
single, triple = words(synthetic, 1), words(synthetic, 3)
single_p, triple_p = entropy_product(single), entropy_product(triple)
require(triple_p**7 > single_p**15, 'Exact check failed (original source line 205)')  # H_3 > 3 H_1.
negative_controls["omitting_window_boundary_factor"] = "rejected exactly"

# Replacing 2^A-3^d by the plus sign destroys joint divisibility.
p, q, A, C, d = 27, 41, 1, 1, 1
require(((2**A + 3**d) * p - C) % 2**(A + 1) != 0, 'Exact check failed (original source line 210)')
negative_controls["wrong_anchor_denominator_sign"] = "rejected exactly"

require(reduced_example is not None, 'Exact check failed (original source line 213)')
example = reduced_example
g = example["gcd"]
lhs = (example["D"] // g) * example["p"] - example["C"] // g
require(lhs != 2**example["A"] * (example["p"] - example["q"]), 'Exact check failed (original source line 217)')
negative_controls["forgetting_gcd_on_reduced_rhs"] = "rejected exactly"

# Prefix-only carry 1 does not replace the complete carry 5 for 27 -> 31.
require((31 - pow(2**3, -1, 3**2)) % 3**2 != 0, 'Exact check failed (original source line 221)')
negative_controls["discarding_complete_carry"] = "rejected exactly"

report = {
    "status": "passed",
    "arithmetic": "exact Python integers and fractions; no floating-point entropy",
    "scope": "finite identities, finite inequalities and negative controls only",
    "not_verified": ["an infinite escaping orbit", "stationary extraction inputs",
                     "asymptotic entropy occupation", "critical collision upper bound",
                     "Collatz conjecture"],
    "fixtures": fixtures,
    "checks": dict(sorted(checks.items())),
    "reduced_anchor_example": reduced_example,
    "negative_controls": negative_controls,
}
print(json.dumps(report, indent=2))
