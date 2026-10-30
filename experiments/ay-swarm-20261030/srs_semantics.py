#!/usr/bin/env python3
"""Exact checks for the AYH scheduling, housekeeping, and envelope packet.

No numerical assertion below is an all-integer termination proof.  The universal
statements have proofs in research/ay-swarm-20261030/srs-semantics.md.
The checks deliberately use explicit exceptions, so -O retains every check.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import product
import json
from pathlib import Path


RULES = (
    ("ad", "d"), ("bd", "gd"), ("ae", "ea"), ("af", "eb"),
    ("ag", "fa"), ("be", "fb"), ("bf", "ga"), ("bg", "gb"),
    ("ce", "cb"), ("cf", "caa"), ("cg", "cab"),
)
DIGITS = {"a": (2, 0), "b": (2, 1), "e": (3, 0),
          "f": (3, 1), "g": (3, 2)}
TER = frozenset("efg")

# The complete affine interpretations in AYH, Example 4.3.  The third
# homogeneous coordinate is constant 1.  String composition is left to right
# as matrix multiplication, unlike the arithmetic value evaluation.
CERT = {
    "a": ((1, 1, 0), (1, 0, 0), (0, 0, 1)),
    "b": ((1, 3, 1), (3, 4, 1), (0, 0, 1)),
    "c": ((1, 5, 0), (0, 0, 0), (0, 0, 1)),
    "d": ((1, 0, 1), (1, 0, 1), (0, 0, 1)),
    "e": ((7, 2, 2), (2, 5, 1), (0, 0, 1)),
    "f": ((2, 1, 1), (1, 1, 0), (0, 0, 1)),
    "g": ((2, 2, 0), (2, 4, 2), (0, 0, 1)),
}
IDENTITY = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def value(word):
    require(word.startswith("c") and word.endswith("d"), "bad boundary")
    n = 1
    for ch in word[1:-1]:
        base, digit = DIGITS[ch]
        n = base * n + digit
    return n


def housekeeping(word):
    n, result = 1, 0
    for ch in word[1:-1]:
        base, digit = DIGITS[ch]
        if ch in TER:
            result += n.bit_length()
        n = base * n + digit
    return result


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def binary_word(n):
    require(n >= 1, "positive source required")
    return "c" + bin(n)[3:].translate(str.maketrans("01", "ab")) + "d"


def redexes(word, auxiliary_only=False):
    result = []
    for pos in range(len(word) - 1):
        for rule, (lhs, rhs) in enumerate(RULES):
            if auxiliary_only and rule < 2:
                continue
            if word[pos:pos + 2] == lhs:
                result.append((pos, rule, word[:pos] + rhs + word[pos + 2:]))
    return result


def normalize(word, strategy, auxiliary_only=False, ceiling=100000):
    counts, arithmetic = Counter(), []
    for step in range(ceiling + 1):
        choices = redexes(word, auxiliary_only)
        if not choices:
            return word, counts, arithmetic
        require(step < ceiling, "normalization test exceeded its finite ceiling")
        choice = choices[0] if strategy == "left" else choices[-1]
        if strategy == "alternate":
            choice = choices[0] if step % 2 else choices[-1]
        _, rule, target = choice
        if rule < 2:
            arithmetic.append(value(word))
        counts[rule] += 1
        word = target
    raise RuntimeError("unreachable")


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def interpretation(word):
    result = IDENTITY
    for ch in word:
        result = matmul(result, CERT[ch])
    return result


def certificate_rank(word):
    return interpretation(word)[0][2]


@lru_cache(None)
def representations(n):
    require(n >= 1, "positive fibre required")
    if n == 1:
        return ("",)
    result = []
    for base, alphabet in ((2, "ab"), (3, "efg")):
        quotient, digit = divmod(n, base)
        if quotient:
            result.extend(w + alphabet[digit] for w in representations(quotient))
    return tuple(result)


def envelope(n, penalty=0):
    candidates = ((certificate_rank("c" + w + "d")
                   + penalty * housekeeping("c" + w + "d"), "c" + w + "d")
                  for w in representations(n))
    return min(candidates)


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def check_all():
    local_edges = 0
    for length in range(6):
        for letters in product(DIGITS, repeat=length):
            word = "c" + "".join(letters) + "d"
            n, h = value(word), housekeeping(word)
            for _, rule, target in redexes(word):
                local_edges += 1
                if rule >= 2:
                    require(value(target) == n, "auxiliary value changed")
                    require(housekeeping(target) == h - 1, "X unit drop failed")
                else:
                    require(value(target) == shortcut(n), "dynamic semantics failed")
                    delta = 0 if rule == 0 else n.bit_length() - 1
                    require(housekeeping(target) == h + delta, "dynamic H update failed")

    aux_sources, aux_steps = 0, 0
    for length in range(5):
        for letters in product(DIGITS, repeat=length):
            word = "c" + "".join(letters) + "d"
            target, counts, _ = normalize(word, "left", auxiliary_only=True)
            require(target == binary_word(value(word)), "wrong X normal form")
            require(sum(counts.values()) == housekeeping(word), "wrong exact X cost")
            aux_sources += 1
            aux_steps += sum(counts.values())

    schedule_sources, schedule_rewrites = 0, 0
    for n in range(1, 513):
        word = binary_word(n)
        reference = None
        for strategy in ("left", "right", "alternate"):
            target, counts, orbit = normalize(word, strategy)
            require(target == "cd", "bounded source did not reach 1")
            weight = sum(1 if x % 2 == 0 else x.bit_length() for x in orbit)
            require(sum(counts.values()) == weight, "weighted orbit cost mismatch")
            signature = (sorted(counts.items()), orbit)
            if reference is None:
                reference = signature
            require(signature == reference, "schedule-dependent labelled counts")
            schedule_rewrites += sum(counts.values())
        schedule_sources += 1

    mixed_schedule_sources = 0
    for length in range(4):
        for letters in product(DIGITS, repeat=length):
            word = "c" + "".join(letters) + "d"
            signatures = []
            for strategy in ("left", "right"):
                target, counts, orbit = normalize(word, strategy)
                require(target == "cd", "mixed bounded source did not reach 1")
                expected = housekeeping(word) + sum(
                    1 if x % 2 == 0 else x.bit_length() for x in orbit)
                require(sum(counts.values()) == expected, "mixed cost mismatch")
                signatures.append((sorted(counts.items()), orbit))
            require(signatures[0] == signatures[1], "mixed Parikh mismatch")
            mixed_schedule_sources += 1

    orientations = []
    for index, (lhs, rhs) in enumerate(RULES):
        left, right = interpretation(lhs), interpretation(rhs)
        weak = all(left[i][j] >= right[i][j] for i in range(2) for j in range(3))
        strict = weak and left[0][2] > right[0][2]
        orientations.append({"rule": lhs + "->" + rhs, "strict": strict})
        require(strict == (index != 3), "published certificate reconstruction failed")

    fibre_cases = []
    for n in (3, 5, 7, 8, 11, 13, 22):
        rank, word = envelope(n)
        fibre_cases.append({"n": n, "representations": len(representations(n)),
                            "minimum": rank, "witness": word})
    family = []
    for k in range(1, 13):
        n = 3 * 2 ** k + 1
        m = shortcut(n)
        witness = "c" + "a" * k + "fd"
        source_rank = certificate_rank(witness)
        rn, wn = envelope(n)
        rm, wm = envelope(m)
        require(rn == source_rank, "family minimum mismatch")
        require(rm >= source_rank + fibonacci(k), "Fibonacci gap failed")
        family.append({"k": k, "n": n, "target": m, "source_rank": rn,
                       "target_rank": rm, "gap": rm-rn,
                       "fibonacci_bound": fibonacci(k),
                       "source_witness": wn, "target_witness": wm})

    # A finite check of the stronger all-target lower-bound statement.
    band_targets = 0
    for k in range(1, 7):
        source = certificate_rank("c" + "a" * k + "fd")
        for m in range(2 ** (k + 2) + 1, 2 ** (k + 3) + 1):
            rank, _ = envelope(m)
            require(rank >= source + fibonacci(k), "dyadic-band lower bound failed")
            band_targets += 1

    return {
        "status": "bounded exact checks passed; universal proofs are in the note",
        "source": {"paper": "https://arxiv.org/html/2105.14697v3",
                   "certificate": "Example 4.3, deletion of af->eb",
                   "upstream_commit": "8a4dfda60f97a6d33ff0a24fdfa7a172d4bec340"},
        "housekeeping_local_edges": local_edges,
        "housekeeping_sources": aux_sources,
        "housekeeping_rewrites": aux_steps,
        "schedule_sources": schedule_sources,
        "schedule_rewrites_across_three_strategies": schedule_rewrites,
        "mixed_schedule_sources": mixed_schedule_sources,
        "certificate_orientations": orientations,
        "complete_small_fibres": fibre_cases,
        "infinite_obstruction_family_bounded_replay": family,
        "dyadic_band_targets": band_targets,
        "limitations": ["No universal Collatz termination claim.",
                        "No claim about all possible matrix certificates or orders.",
                        "All minima in this output enumerate the complete finite fibre."]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(check_all(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
