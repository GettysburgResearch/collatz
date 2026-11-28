#!/usr/bin/env python3
"""Exact bounded checks of affine-word decoding, independent forward matrices."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def forward_matrix(word):
    a, b = Fraction(1), Fraction(0)
    for bit in word:
        slope = Fraction(3 if bit else 1, 2)
        a, b = slope * a, slope * b + Fraction(bit, 2)
    return a, b


def decode_code(t, a, c):
    original = t, a, c
    word = []
    for _ in range(t):
        bit = c % 2
        word.append(bit)
        if bit:
            # Natural subtraction in the Lean raw candidate is truncated.
            a //= 3
            c = max(0, c - a) // 2
        else:
            c //= 2
    fa, fb = forward_matrix(word)
    length, scale, offset = original
    if fa * 2**length == scale and fb * 2**length == offset:
        return tuple(word)
    return None


def decode_matrix(a, b):
    if a <= 0 or b < 0:
        return None
    denominator = a.denominator
    if denominator & (denominator - 1):
        return None
    t = denominator.bit_length() - 1
    c = b * denominator
    if c.denominator != 1:
        return None
    return decode_code(t, a.numerator, c.numerator)


def main():
    words = 0
    matrices = set()
    for t in range(15):
        for w in product((0, 1), repeat=t):
            a, b = forward_matrix(w)
            require(decode_matrix(a, b) == w, "Forward matrix failed round trip")
            require((a, b) not in matrices, "Two words give the same affine matrix")
            matrices.add((a, b))
            words += 1

    # Exhaust every code in complete coefficient boxes through depth five.
    # Acceptance is compared with literal enumeration, not a second decoder.
    boxes = accepted = 0
    for t in range(6):
        actual = {}
        for w in product((0, 1), repeat=t):
            a, b = forward_matrix(w)
            actual[int(a * 2**t), int(b * 2**t)] = w
        for a in range(3**t + 1):
            for c in range(3**t - 2**t + 1):
                found = decode_code(t, a, c)
                require(found == actual.get((a, c)), "Complete coefficient-box mismatch")
                boxes += 1
                accepted += found is not None

    malformed = [
        (Fraction(0), Fraction(0)),
        (Fraction(-1, 2), Fraction(1)),
        (Fraction(1, 3), Fraction(0)),
        (Fraction(1, 2), Fraction(-1)),
        (Fraction(1, 2), Fraction(1, 3)),
        (Fraction(2), Fraction(0)),
        (Fraction(1), Fraction(1)),
    ]
    for a, b in malformed:
        require(decode_matrix(a, b) is None, "Malformed matrix was accepted")

    root = Path(__file__).resolve().parent
    print(json.dumps({
        "scope": "bounded exact affine-code controls, not Collatz reachability",
        "independent_forward_words": words,
        "unique_matrices": len(matrices),
        "complete_coefficient_box_cases": boxes,
        "accepted_box_codes": accepted,
        "malformed_matrices": len(malformed),
        "sha256": {name: hashlib.sha256((root/name).read_bytes()).hexdigest()
                   for name in ("AffineWordDecoder.lean", "check_affine_decoder.py")},
    }, sort_keys=True))


if __name__ == "__main__":
    main()
