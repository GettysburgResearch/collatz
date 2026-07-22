#!/usr/bin/env python3
"""Independent replay for X-8502; imports no author module."""
from __future__ import annotations

import argparse
import hashlib
import json
from functools import lru_cache
from pathlib import Path

P = (5, 30, 20, 56)
TOLL = (9, 54, 36, 24)


def odd_power(t: int) -> int:
    return pow(3, 7 * (t + 1))


def binary_power(t: int) -> int:
    return pow(2, 11 * (t + 17))


@lru_cache(maxsize=None)
def bezout(t: int) -> tuple[int, int]:
    n, m = odd_power(t), binary_power(t)
    r = pow(n, -1, m)
    c, rem = divmod(n * r - 1, m)
    assert rem == 0
    return r, c


def source_word(t: int, i: int, q: int) -> int:
    r, _ = bezout(t)
    return -TOLL[i] * r + binary_power(t) * (TOLL[i] + q)


def target_word(t: int, i: int, q: int) -> int:
    n, m = odd_power(t), binary_power(t)
    r, c = bezout(t)
    del r
    source = source_word(t, i, q)
    numerator = n * source + TOLL[i]
    assert numerator % m == 0
    target = numerator // m
    assert target == TOLL[i] * (n - c) + n * q
    return target


def direct_next(t: int, i: int, q: int) -> tuple[int, int] | None:
    target = target_word(t, i, q)
    try:
        j = P.index(target % 64)
    except ValueError:
        return None
    r2, _ = bezout(t + 16)
    base2 = -TOLL[j] * r2 + binary_power(t + 16) * TOLL[j]
    difference = target - base2
    modulus = binary_power(t + 16)
    if difference % modulus:
        return None
    return j, difference // modulus


def digest_without_field(payload: dict[str, object]) -> str:
    clone = dict(payload)
    expected = clone.pop("payload_digest")
    raw = json.dumps(clone, sort_keys=True, separators=(",", ":")).encode()
    actual = hashlib.sha256(raw).hexdigest()
    assert actual == expected
    return actual


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path, required=True)
    args = parser.parse_args()

    payload = json.loads(args.check_results.read_text(encoding="utf-8"))
    assert payload["experiment"] == "X-8502"
    digest = digest_without_field(payload)

    assert 3 ** 5 < 2 ** 8
    assert 3 ** 106 < 2 ** 170
    assert 2 ** 175 > 3 ** 106

    identity = 0
    pair_cases = 0
    legal = 0
    growth = 0

    for t in (80, 3744, 3792):
        n, m = odd_power(t), binary_power(t)
        for i in range(4):
            for q in (0, 3, 256, 511):
                source = source_word(t, i, q)
                target = target_word(t, i, q)
                assert m * target == n * source + TOLL[i]
                assert source % 64 == P[i]
                identity += 1

            for j in range(4):
                r2, _ = bezout(t + 16)
                base2 = -TOLL[j] * r2 + binary_power(t + 16) * TOLL[j]
                constant = TOLL[i] * (n - bezout(t)[1])
                modulus = binary_power(t + 16)
                residue = ((base2 - constant) * pow(n, -1, modulus)) % modulus
                cap = (constant + n * residue - base2) // modulus
                assert direct_next(t, i, residue) == (j, cap)
                assert target_word(t, i, residue) % 64 == P[j]
                pair_cases += 1

                for lift in (1, 3):
                    q = residue + modulus * lift
                    result = direct_next(t, i, q)
                    assert result == (j, cap + n * lift)
                    legal += 1
                    if t >= 3744 and q >= 256:
                        assert result[1] >= 2 * q
                        growth += 1

    print("X-8502 independent checker")
    print(f"committed payload digest: {digest}")
    print(f"independent complement identities: {identity}")
    print(f"independent canonical pair cases: {pair_cases}")
    print(f"independent legal lifts: {legal}")
    print(f"independent growth cases: {growth}")
    print("all independent complement-quotient checks passed")


if __name__ == "__main__":
    main()
