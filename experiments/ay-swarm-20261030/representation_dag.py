#!/usr/bin/env python3
"""Exact finite mixed-radix fibres; no Collatz stopping-time oracle is used.

This is a current-integer representation compiler, not a termination proof.
All checks use explicit exceptions and run under optimized Python as well.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path

DIGITS = {"a": (2, 0), "b": (2, 1), "e": (3, 0), "f": (3, 1), "g": (3, 2)}
BY_BASE = {2: "ab", 3: "efg"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def value(word):
    require(word.startswith("c") and word.endswith("d"), "wrong boundary")
    n = 1
    for symbol in word[1:-1]:
        base, digit = DIGITS[symbol]
        n = base * n + digit
    return n


def parents(n):
    require(type(n) is int and n >= 1, "positive integer required")
    if n == 1:
        return ()
    return tuple((n // base, BY_BASE[base][n % base])
                 for base in (2, 3) if n // base >= 1)


def quotient_nodes(n):
    """Reachable division quotients, stopping exactly at the leading 1."""
    require(type(n) is int and n >= 1, "positive integer required")
    seen, todo = {n}, [n]
    while todo:
        q = todo.pop()
        for p, _ in parents(q):
            if p not in seen:
                seen.add(p)
                todo.append(p)
    return sorted(seen)


def fibre_count(n):
    table = {}
    for q in quotient_nodes(n):
        table[q] = 1 if q == 1 else sum(table[p] for p, _ in parents(q))
    return table[n]


@lru_cache(maxsize=None)
def all_words(n):
    if n == 1:
        return ("cd",)
    return tuple(w[:-1] + digit + "d" for p, digit in parents(n)
                 for w in all_words(p))


def affine_minimum(n, maps, seed=0):
    """Minimum of a scalar monotone affine fold over EVERY representation.

    A digit s sends x to maps[s][0]*x + maps[s][1], in reading order.
    This is not a componentwise minimum of correlated matrix coordinates.
    Return exact optimum and one concrete minimizing representation.
    """
    require(type(seed) is int and seed >= 0, "nonnegative integer seed required")
    require(set(maps) == set(DIGITS), "all five digit maps required")
    for a, b in maps.values():
        require(type(a) is int and type(b) is int and a >= 0 and b >= 0,
                "nonnegative integer affine maps required")
    table = {}
    for q in quotient_nodes(n):
        if q == 1:
            table[q] = (seed, "cd")
            continue
        candidates = []
        for p, digit in parents(q):
            a, b = maps[digit]
            score, word = table[p]
            candidates.append((a * score + b, word[:-1] + digit + "d"))
        table[q] = min(candidates)
    return table[n]


def fold(word, maps, seed=0):
    result = seed
    for digit in word[1:-1]:
        a, b = maps[digit]
        result = a * result + b
    return result


def exhaustive_forward_fibres(limit):
    """Independent literal prefix construction, not the quotient recurrence."""
    result = {n: [] for n in range(1, limit + 1)}
    todo = [(1, "c")]
    while todo:
        n, word = todo.pop()
        result[n].append(word + "d")
        for digit, (base, remainder) in DIGITS.items():
            m = base * n + remainder
            if m <= limit:
                todo.append((m, word + digit))
    return result


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def odd_step(n):
    require(n % 2 == 1, "odd argument required")
    m = 3 * n + 1
    return m // (m & -m)


def additive_search(limit=511, max_weight=3):
    """Finite falsification of scalar all-representation additive envelopes.

    A positive finding would only be finite evidence. Ties are resolved by
    the explicit pair (popcount, v2(n+1)); no trajectory data are a feature.
    """
    sources = list(range(3, limit + 1, 2))
    maximum = max(sources + [odd_step(n) for n in sources])
    p = [parents(n) for n in range(1, maximum + 1)]
    symbols = tuple(DIGITS)
    best = None
    histogram = Counter()
    survivors = []
    for weights in itertools.product(range(max_weight + 1), repeat=5):
        if not any(weights):
            continue
        weight = dict(zip(symbols, weights))
        score = [0] * (maximum + 1)
        for n in range(2, maximum + 1):
            score[n] = min(score[parent] + weight[digit] for parent, digit in p[n - 1])
        def rank(n):
            return (score[n], n.bit_count(), ((n + 1) & -(n + 1)).bit_length() - 1)
        failures = [n for n in sources if rank(odd_step(n)) >= rank(n)]
        first = failures[0] if failures else None
        histogram[str(first)] += 1
        record = {"weights": weight, "failures": len(failures), "first_failure": first,
                  "first_input_rank": list(rank(first)) if first else None,
                  "first_output": odd_step(first) if first else None,
                  "first_output_rank": list(rank(odd_step(first))) if first else None}
        key = (len(failures), -(first or (limit + 1)), weights)
        if best is None or key < best[0]:
            best = (key, record)
        if not failures:
            survivors.append(record)
    return {"status": "EMPIRICAL bounded parameter falsification only",
            "source_limit": limit, "weight_range": [0, max_weight],
            "candidates": (max_weight + 1) ** 5 - 1,
            "best": best[1], "first_failure_histogram": dict(sorted(histogram.items())),
            "finite_survivors": survivors}


def run_checks():
    literal = exhaustive_forward_fibres(1024)
    count_checks = 0
    map_cases = [
        {s: (1, i + 1) for i, s in enumerate(DIGITS)},
        {s: (base, digit) for s, (base, digit) in DIGITS.items()},
        {s: ((i % 3), (4 - i) ** 2) for i, s in enumerate(DIGITS)},
    ]
    minimum_checks = 0
    for n, words in literal.items():
        require(all(value(w) == n for w in words), "forward value mismatch")
        require(len(words) == len(set(words)) == fibre_count(n), "fibre count mismatch")
        require(set(words) == set(all_words(n)), "complete fibre mismatch")
        count_checks += 1
        if n <= 128:
            for maps in map_cases:
                exact = min(fold(w, maps) for w in words)
                actual, witness = affine_minimum(n, maps)
                require(actual == exact == fold(witness, maps), "minimum mismatch")
                require(witness in words, "minimum witness missing")
                minimum_checks += 1
    huge = []
    for bits in [64, 256, 1024, 4096]:
        n = (1 << bits) - 1
        nodes = quotient_nodes(n)
        count = fibre_count(n)
        # No floating-point logarithm is used to check this loose node bound.
        log3 = 0
        power = 1
        while power <= n:
            power *= 3
            log3 += 1
        require(len(nodes) <= n.bit_length() * log3, "quotient node bound failed")
        huge.append({"input_bits": bits, "quotient_nodes": len(nodes),
                     "representation_count_bits": count.bit_length(),
                     "representation_count_sha256": hashlib.sha256(str(count).encode()).hexdigest()})
    # Coordinate minima from different words cannot be spliced into a matrix vector.
    vectors = [(0, 10), (10, 0)]
    fake = tuple(min(v[i] for v in vectors) for i in range(2))
    require(fake not in vectors and sum(fake) < min(map(sum, vectors)), "correlation control failed")
    return {"schema": "ay-representation-dag/v1", "status": "exact bounded checks",
            "complete_fibres": count_checks, "literal_words": sum(map(len, literal.values())),
            "affine_minimum_checks": minimum_checks,
            "large_inputs": huge, "correlation_negative_control": {"vectors": vectors, "invalid_coordinate_minimum": fake},
            "search": additive_search()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run_checks()
    body = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(body, encoding="utf-8")
    else:
        print(body, end="")


if __name__ == "__main__":
    main()
