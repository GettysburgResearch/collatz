#!/usr/bin/env python3
"""Exact small regression for the two-macro normalization, not termination."""
from itertools import product
import json

M = 2**38
K = 3**24
D = K - M
CONSTANTS = (610948284866, 613397164994)
SOURCES = (210578993150, 341135408638)
DELTA = CONSTANTS[1] - CONSTANTS[0]
A_STAR = 1714077182
C = 5285712575


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def main():
    require(DELTA == 2**9 * 3**14, "offset factorization")
    require(D * A_STAR + CONSTANTS[0] == DELTA * C, "first normalized offset")
    require(D * A_STAR + CONSTANTS[1] == DELTA * (C + 1), "second normalized offset")
    require(0 < C < C + 1 < M, "ceiling digit interval")
    require(0 < C < C + 1 < D, "real shadow lies within a unit interval")
    for digit in (0, 1):
        require(0 < SOURCES[digit] < 2 * M, "safe residue positivity")
        require((K * SOURCES[digit] + CONSTANTS[digit]) % (2 * M) == 0,
                "safe endpoint parity congruence")
        require(SOURCES[digit] % 512 == A_STAR % 512 == 510,
                "common binary residue")
        require(A_STAR % (3**14) == CONSTANTS[digit] * pow(M, -1, 3**14) % (3**14),
                "common ternary endpoint residue")

    word_count, step_count = 0, 0
    for length in range(1, 7):
        modulus = M**length
        for word in product((0, 1), repeat=length):
            affine = sum(K ** (length - 1 - j) * M**j * (C + digit)
                         for j, digit in enumerate(word))
            b = (-affine * pow(K**length, -1, modulus)) % modulus
            require(b > 0, "positive primitive normalized source")
            for digit in word:
                numerator = K * b + C + digit
                require(numerator % M == 0, "normalized exact step")
                next_b = numerator // M
                require(next_b > b, "positive normalized expansion")
                require(next_b == (K * b + M - 1) // M, "ceiling-map equality")
                require(M * next_b - K * b == C + digit, "restricted remainder")
                a, next_a = A_STAR + DELTA * b, A_STAR + DELTA * next_b
                require(a >= SOURCES[digit] and (a - SOURCES[digit]) % (2 * M) == 0,
                        "recovered actual safe cylinder")
                require(M * next_a == K * a + CONSTANTS[digit], "original macro")
                require((a - A_STAR) // DELTA == b, "normalization round trip")
                b = next_b
                step_count += 1
            word_count += 1
    report = {
        "status": "exact normalization checks passed; all-source termination remains unproved",
        "K": K, "M": M, "D": D, "delta": DELTA, "a_star": A_STAR,
        "normalized_digits": [C, C + 1],
        "finite_words": word_count, "actual_macro_steps": step_count,
        "scope": "Every binary word through length 6; no large source census and no infinite-path inference",
    }
    output = json.dumps(report, sort_keys=True, indent=2) + "\n"
    print(output, end="")


if __name__ == "__main__":
    main()
