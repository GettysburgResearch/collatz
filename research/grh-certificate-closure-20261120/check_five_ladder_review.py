#!/usr/bin/env python3
"""Independent literal replay for the pinned five-certificate ladder review.

This file imports no author implementation. Finite replay supports, but does
not replace, the universal proof reconstructed in REVIEW_FIVE_LADDER.md.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json


PINNED = {
    "FIVE_CERTIFICATE_LADDER.md": "d66dee00fb9ab089694363d2905f788f3d319c5a79ac3e8d9448efcb5cbb6dba",
    "check_five_certificate_ladder.py": "6f45f58f996d10ae7a01dc3c8f7e3cdcbda95b5508d9249e69594fb87b2b809f",
    "five-ladder-report.json": "4429ebb447ec81300c2086fcea0940d21f57c7abdec8a0b55fb2465980add04c",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def literal_odd(n):
    require(type(n) is int and n > 0 and n % 2 == 1, "ordinary odd input")
    # Take exactly one odd shortcut step, then literal halving steps.
    m = (3*n+1)//2
    clock = 1
    while m % 2 == 0:
        m //= 2
        clock += 1
    return m, clock


def replay(n, expected, first_hit=False):
    clock = 0
    for exponent in expected:
        require(type(exponent) is int and exponent > 0, "integer exponent")
        require(not first_hit or n != 1, "premature first hit")
        n, actual = literal_odd(n)
        require(actual == exponent, "wrong literal exponent")
        clock += actual
    return n, clock


def rewritten(r, b):
    require(r >= 1 and b >= 4, "ladder domain")
    if r == 1:
        return [5, b-3]
    return [4] + [2 for _ in range(r-2)] + [3, b-3]


def inverse_certificate(q, word):
    for exponent in reversed(word):
        numerator = (2**exponent)*q-1
        require(numerator % 3 == 0, "nonintegral source")
        q = numerator//3
        require(q > 0 and q % 2 == 1, "invalid inverse output")
    return q


def source_block(q, r):
    # A small exhaustive selection, independent of the author's lift routine.
    for b in range(4, 6*3**r+6):
        numerator = 4**r*(2**b*q-4)
        if numerator % 3**(r+1):
            continue
        x = 1+numerator//3**(r+1)
        if x % 3:
            require(replay(x, [2]*r+[b])[0] == q, "source block selection")
            return x, b
    raise ValueError("finite lift search exhausted")


def run():
    counts = {"census_odd_inputs": 0, "census_ladder_inputs": 0,
              "paired_shortcut_steps": 0, "all_rank_family_cases": 0,
              "composed_certificates": 0, "finite_density_points": 0,
              "rank_one_residuals": 0, "independent_malformed_controls": 0}
    fixtures = []

    # Exhaustively compare cylinder membership with actual initial valuations.
    # Also replay every source/target block found in this finite interval.
    for x in range(3, 65536, 2):
        counts["census_odd_inputs"] += 1
        q, r = x, 0
        while True:
            next_q, b = literal_odd(q)
            if b != 2 or q == 1:
                break
            q, r = next_q, r+1
        actual = r > 0 and b >= 4
        residues = [s for s in range(1, 9)
                    if x % 2**(2*s+4) == 1+(1 if s % 2 == 0 else 3)*2**(2*s+2)]
        require(actual == bool(residues), "cylinder equivalence")
        if not actual:
            continue
        require(residues == [r], "disjoint cylinder index")
        source, target = [2]*r+[b], rewritten(r, b)
        endpoint, source_clock = replay(x, source)
        image, target_clock = replay(5*x, target)
        require(image == 5*endpoint and source_clock == target_clock == 2*r+b,
                "paired physical endpoints/clocks")
        require(endpoint % 3 and 7*endpoint <= x, "smaller unit endpoint")
        counts["census_ladder_inputs"] += 1
        counts["paired_shortcut_steps"] += source_clock+target_clock

    # Explicit all-rank families: ranks 2 through 8, with three k values each.
    for r in range(1, 8):
        for k in range(1, 4):
            b = 2+2*3**r*k
            numerator = 4**(r+1)*(4**(3**r*k)-1)
            require(numerator % 3**(r+1) == 0, "family integrality")
            x = 1+numerator//3**(r+1)
            word, output = [2]*r+[b], rewritten(r, b)+[4]
            require(x == inverse_certificate(1, word), "independent family formula")
            require(replay(x, word, True) == (1, 2*r+b), "source exact first hit")
            require(replay(5*x, output, True) == (1, 2*r+b+4), "target exact first hit")
            require(len(output) == len(word)+1 and x % 3 == (1+k) % 3,
                    "family rank/unit assertion")
            counts["all_rank_family_cases"] += 1
            fixtures.append((r, k, x.bit_length(), b, len(output)))

    # Compose actual complete first-hit words, not merely grammatical strings.
    for pattern in ([1, 1], [2, 1], [1, 3, 2], [4, 2, 1, 3], [1]*10):
        q, blocks = 1, []
        for r in reversed(pattern):
            q, b = source_block(q, r)
            blocks.insert(0, (r, b))
        source = [a for r, b in blocks for a in [2]*r+[b]]
        target = [a for r, b in blocks for a in rewritten(r, b)]+[4]
        require(replay(q, source, True) == (1, sum(source)), "composed source")
        require(replay(5*q, target, True) == (1, sum(source)+4), "composed target")
        require(len(target) == len(source)+1, "composed exact rank")
        counts["composed_certificates"] += 1
    require(replay(5, [4], True) == (1, 4), "empty source boundary")

    # Exact CRT-period census of the first four cylinders, after removing 3|x.
    R, modulus = 4, 3*2**12
    per_class = [0]*R
    total_units = 0
    for x in range(1, modulus+1):
        if x % 2 == 0 or x % 3 == 0:
            continue
        total_units += 1
        for r in range(1, R+1):
            residue = 1+(1 if r % 2 == 0 else 3)*2**(2*r+2)
            if x % 2**(2*r+4) == residue:
                per_class[r-1] += 1
    require(total_units == modulus//3, "unit base density")
    for r, count in enumerate(per_class, 1):
        require(Fraction(count, total_units) == Fraction(1, 2**(2*r+3)),
                "finite relative density")
    require(sum(Fraction(1, 2**(2*r+3)) for r in range(1, R+1))
            == Fraction(1, 24)*(1-Fraction(1, 4**R)), "geometric density sum")
    counts["finite_density_points"] = modulus

    # Confirm the expressly uncovered rank-one residual, without claiming closure.
    for a in range(2, 35):
        x = (4**a-1)//3
        require(replay(x, [2*a], True)[0] == 1, "rank-one source")
        n = 5*x
        for _ in range(2*a-1):
            n, _ = literal_odd(n)
        require(n == (5*9**(a-1)-1)//4, "rank-one residual identity")
        counts["rank_one_residuals"] += 1

    # Positive signed-offset example using a legal p=3, B=53 template.
    offset = Fraction(-265, 27)
    for _ in range(10):
        require(offset.denominator % 2 == 1, "signed parity domain")
        offset = (3*offset+1)/2 if offset.numerator % 2 else offset/2
    require(offset == 1, "positive offset example")
    for N in (27, 45, 63):
        x = (2**N-53)//27
        require(replay(x, [2, 3, N-5], True)[0] == 1, "offset template source")
        n = 5*x
        for _ in range(10):
            n = (3*n+1)//2 if n % 2 else n//2
        require(n == 5*2**(N-10)+1, "signed offset physical realization")

    for n, word in ((113, [2.0, 8]), (3, [True, 4]), (1, [2]),
                    (113, [2, 7]), (True, [])):
        try:
            require(type(n) is int and n > 0 and n % 2, "input type")
            require(replay(n, word, True)[0] == 1, "nonterminal word")
        except ValueError:
            counts["independent_malformed_controls"] += 1
        else:
            raise ValueError("malformed control accepted")

    return {"status": "PASS", "counts": counts, "pinned_author_files": PINNED,
            "author_imports": False, "grh_used": False,
            "relative_density_limit": "1/24 (universal tail argument in review)",
            "fixture_sha256": hashlib.sha256(repr(fixtures).encode()).hexdigest(),
            "scope": "Independent finite literal replay. FL1-FL4 proof review is separate; neither establishes full forward-five closure or Collatz."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(run(), indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
