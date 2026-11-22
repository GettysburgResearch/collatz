"""Exact checks for the head-three negative-cycle obstruction.

The general proofs are in HeadThreeNegativeCycle.lean and
HEAD_THREE_NEGATIVE_CYCLE.md. These checks exercise the explicit complete
source construction and its one complete alphabet-four witness.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HARD_WORD = [3, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 3, 2, 3, 1, 4,
             2, 2, 2, 2, 2, 2, 4, 2, 1, 2, 2, 1, 2, 2, 4, 3,
             2, 1, 2, 3, 1, 2, 1, 4, 1, 3, 1, 2, 3, 4]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def step(n: int) -> int:
    require(n > 0, "ordinary state must be positive")
    return (3 * n + 1) // 2 if n & 1 else n // 2


def negative_step(n: int) -> int:
    require(n > 0, "complement must be positive")
    return (3 * n - 1) // 2 if n & 1 else n // 2


def check_trace(source: int, word: list[int], endpoint: int = 1) -> None:
    n = source
    for a in word:
        require(n > 0 and n & 1 == 1, "nonpositive or even odd-source state")
        require(a > 0, "gap must be positive")
        value = 3 * n + 1
        require(value % (1 << a) == 0, "source gap is not integral")
        n = value >> a
        require(n & 1 == 1, "source gap is not the exact valuation")
    require(n == endpoint, "wrong source endpoint")


def check_no_descent(n: int, horizon: int) -> int:
    current = n
    for _ in range(horizon):
        current = step(current)
        require(current > n, "original target descends inside claimed window")
    return current


def check_pin(b: int, H: int, d: int) -> None:
    require(min(b, H, d) >= 0, "binary pin parameters must be natural")
    require(486 * b + 102 == (1 << H) * d, "wrong binary pin")


def check_cycle() -> dict:
    expected = [136, 68, 34, 17, 25, 37, 55, 82, 41, 61, 91]
    current = 136
    odds = 0
    for j, value in enumerate(expected):
        require(current == value, "wrong cycle state")
        require((1 << j) <= 8 * 3**odds, "wrong cycle prefix multiplier")
        require(current <= 136, "wrong cycle complement bound")
        odds += current & 1
        current = negative_step(current)
    require(current == 136 and odds == 7, "wrong cycle return")
    require(3**7 > 2**11, "cycle must expand its positive high part")
    return {"complement_cycle": expected, "clock": 11, "odd_steps": odds,
            "multiplier_numerator": 2187, "multiplier_denominator": 2048}


def complete_source(k: int) -> dict:
    require(k >= 2, "elementary explicit completion is stated for k >= 2")
    s = (34 * pow(4, (24 - k) % 27, 81)) % 81
    require(1 <= s <= 80, "invalid calibration residue")
    require((pow(4, k + 3, 81) * s) % 81 == 34, "invalid calibration")
    a = 2 + 2 * 3**(k + 1) * s
    numerator = (1 << a) - 4
    denominator = 3**(k + 1)
    require(numerator % denominator == 0, "completion quotient is not integral")
    t = numerator // denominator
    r = 1 + 4**k * t
    require(r >= 103 and (r - 103) % 486 == 0, "source entry is not integral")
    b = (r - 103) // 486
    q = 2048 * b + 429
    n = 8 * q - 1
    H = 2 * k + 2
    require((r - 1) % (1 << H) == 0, "binary pin is not integral")
    require(((r - 1) >> H) & 1 == 1, "binary pin is not exact")
    word = [3, 2, 2, 1, 2] + [2] * k + [a]
    check_trace(q, word)
    check_no_descent(n, 13 + H)
    source_bytes = q.to_bytes((q.bit_length() + 7) // 8, "big")
    return {"k": k, "calibration": s, "terminal_gap": a,
            "source_word": word, "binary_horizon": H,
            "no_descent_through_clock": 13 + H,
            "source_bits": q.bit_length(),
            "source_big_endian_sha256": hashlib.sha256(source_bytes).hexdigest(),
            "complete": True, "alphabet_four": False}


def hard_example() -> dict:
    q = 58849709
    n = 8 * q - 1
    check_trace(q, HARD_WORD)
    require(max(HARD_WORD) == 4, "hard witness is not alphabet four")
    b, H, d = 28735, 11, 6819
    require(q == 2048 * b + 429, "wrong affine source")
    check_pin(b, H, d)
    endpoint = check_no_descent(n, 13 + H)
    return {"source_q": q, "powered_source": 4 * q, "target": n,
            "source_word": HARD_WORD, "source_clock": sum(HARD_WORD),
            "b": b, "H": H, "d": d, "target_endpoint": endpoint,
            "no_descent_through_clock": 24,
            "complete": True, "alphabet_four": True}


def damaged_controls() -> list[str]:
    damaged_word = HARD_WORD.copy()
    damaged_word[0] = 2
    checks = [
        ("binary_pin", lambda: check_pin(28735, 11, 6821)),
        ("exact_gap", lambda: check_trace(58849709, damaged_word)),
        ("source_endpoint", lambda: check_trace(58849709, HARD_WORD, endpoint=3)),
        ("intermediate_carry_as_original_target",
         lambda: check_no_descent(354294 * 28735 + 74222, 1)),
    ]
    rejected = []
    for label, check in checks:
        try:
            check()
        except ValueError:
            rejected.append(label)
        else:
            raise ValueError("damaged control was accepted: " + label)
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-k", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    require(args.max_k >= 2, "max-k must be at least two")
    result = {"status": "PASS", "cycle": check_cycle(),
              "complete_sources": [complete_source(k) for k in range(2, args.max_k + 1)],
              "complete_cap_four_example": hard_example(),
              "damaged_controls_rejected": damaged_controls(),
              "scope": "finite implementation checks; all-parameter proofs are separate"}
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text)


if __name__ == "__main__":
    main()
