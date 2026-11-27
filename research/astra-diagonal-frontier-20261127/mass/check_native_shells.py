"""Replay native source, normalized endpoint and exchange identities on finite rows."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def path(source: int, horizon: int) -> tuple[list[int], int]:
    state = source
    bits = []
    for _ in range(horizon):
        bits.append(state % 2)
        state = (3 * state + 1) // 2 if state % 2 else state // 2
    return bits, state


def passes(bits: list[int]) -> bool:
    debt = 0
    for bit in bits:
        debt += 7 * bit - 4
        if debt < 0:
            return False
    return True


def inverse_residue(bits: list[int]) -> int:
    value = 0
    modulus = 1 << len(bits)
    for bit in reversed(bits):
        value = (2 * value - bit) % modulus
        if bit:
            value = value * pow(3, -1, modulus) % modulus
    return value or modulus


def check_row(horizon: int) -> dict:
    size = 1 << horizon
    accepted = []
    swap_checks = 0
    by_shell = {}
    for source in range(1, size, 2):
        bits, endpoint = path(source, horizon)
        if not passes(bits):
            continue
        accepted.append(source)
        odd_count = sum(bits)
        check(inverse_residue(bits) == source, "native residue inversion failed")
        previous_odds, carry = 0, 0
        for i, bit in enumerate(bits):
            if bit:
                previous_odds += 1
                carry += (1 << i) * 3 ** (odd_count - previous_odds)
        check(size * endpoint == 3**odd_count * source + carry, "native affine identity failed")
        for start in range(0, horizon - 3, 4):
            if bits[start : start + 4] != [1, 1, 1, 0]:
                continue
            other_bits = bits.copy()
            other_bits[start : start + 4] = [1, 1, 0, 1]
            other_source = inverse_residue(other_bits)
            replay, other_endpoint = path(other_source, horizon)
            check(passes(replay) and replay == other_bits, "exchange lost the native gate")
            before = sum(bits[:start])
            mod = 3 ** (before + 3)
            phase_num = (1 << (start + 2)) * pow(size, -1, mod) % mod
            difference = (Fraction(other_endpoint - endpoint, 3**odd_count)
                          - Fraction(phase_num, mod))
            check(difference.denominator == 1, "ternary endpoint exchange phase failed")
            swap_checks += 1
        age = horizon - source.bit_length()
        if age > 4:
            continue
        row = by_shell.setdefault(age, {"sources": 0, "survive_seven": 0})
        row["sources"] += 1
        row["survive_seven"] += int(passes(path(source, horizon + 7)[0]))
    return {"horizon": horizon, "accepted": len(accepted),
            "exchange_checks": swap_checks, "selected_shell_counts": by_shell}


def main() -> None:
    rows = [check_row(k) for k in (7, 11, 14, 17)]
    output = {
        "scope": "Exact finite source and congruence checks; shell counts are diagnostic, not an asymptotic test.",
        "rows": rows,
    }
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="also save the deterministic JSON here")
    options = parser.parse_args()
    rendered = json.dumps(output, indent=2) + "\n"
    if options.output is not None:
        options.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
