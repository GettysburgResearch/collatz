#!/usr/bin/env python3
"""Independent checker for X-8501.

This file intentionally does not import derive.py.  It uses direct finite-chain
composition and a separately written decoder reconstruction.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

CORE = ((5, 0, 2), (30, 1, 3), (20, 2, 2), (56, 3, 1))
P = tuple(row[0] for row in CORE)
B = tuple((1 << row[1]) * (3 ** row[2]) for row in CORE)


def digest_without_field(payload: dict[str, Any]) -> str:
    clean = dict(payload)
    expected = clean.pop("payload_digest")
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":")).encode()
    actual = hashlib.sha256(raw).hexdigest()
    assert actual == expected
    return actual


def odd(t: int) -> int:
    return 3 ** (7 * (t + 1))


def radix(t: int) -> int:
    return 1 << (11 * (t + 17))


@lru_cache(maxsize=None)
def direct_connector(t: int, i: int, j: int) -> tuple[int, int]:
    n = odd(t)
    q = radix(t)
    left = (n * P[i] + B[i]) // 64
    right = q * P[j] // 64
    residue = ((right - left) * pow(n, -1, q)) % q
    out = (left + n * residue - right) // q
    assert left + n * residue == right + q * out
    assert 0 <= residue < q and 0 <= out < n
    return residue, out


@lru_cache(maxsize=None)
def inverse_pair(t: int) -> tuple[int, int]:
    n, q = odd(t), radix(t)
    inv = pow(n, -1, q)
    carry = (n * inv - 1) // q
    assert n * inv - q * carry == 1
    return inv, carry


def reconstruct_normal(t: int, i: int, j: int) -> tuple[int, int, int]:
    n, q = odd(t), radix(t)
    inv, carry = inverse_pair(t)
    omega = (P[i] + B[i] * inv) // 64
    assert 64 * omega == P[i] + B[i] * inv
    six = (P[j] * inv - P[i] * carry) % 64
    value = -omega + (q // 64) * six
    if value < 0:
        value += q
    eta, theta = direct_connector(t, i, j)
    assert value == eta
    assert (n * six - B[i] * carry - P[j]) % 64 == 0
    eps = int(-omega + (q // 64) * six < 0)
    theta2 = (n * six - B[i] * carry - P[j]) // 64 + eps * n
    assert theta2 == theta
    return six, eta, theta


def check_carry_step(t: int) -> None:
    n, q = odd(t), radix(t)
    inv, carry = inverse_pair(t)
    del inv
    n2, q2 = odd(t + 16), radix(t + 16)
    inv2, carry2 = inverse_pair(t + 16)

    u = 1 << 176
    s = 3 ** 112
    reduced = (pow(u, -1, n) * carry) % n
    h = (1 + u * q * reduced) // n
    digit = (-h * pow(u * q, -1, s)) % s
    predicted = reduced + n * digit
    assert predicted == carry2
    assert (1 + q2 * predicted) // n2 == inv2


def direct_stage_exponents(width: int, base: int) -> tuple[int, int, int]:
    odds = sum(7 * (base + 16 * j + 1) for j in range(width))
    current = sum(11 * (base + 16 * j + 1) for j in range(1, width + 1))
    next_base = base + 16 * width
    nxt = sum(11 * (next_base + 16 * j + 1) for j in range(1, width + 1))
    return odds, current, nxt


def check_decoder(t: int, i: int, j: int, k: int, lift: int) -> tuple[int, int]:
    eta, theta = direct_connector(t, i, j)
    del eta
    eta2, _ = direct_connector(t + 16, j, k)
    n = odd(t)
    q2 = radix(t + 16)
    residue = ((eta2 - theta) * pow(n, -1, q2)) % q2
    z = residue + lift * q2
    z2 = (n * z + theta - eta2) // q2
    assert n * z + theta == eta2 + q2 * z2

    _, _, _ = reconstruct_normal(t + 16, j, 0)
    inv_next, carry_next = inverse_pair(t + 16)
    omega_next = (P[j] + B[j] * inv_next) // 64
    low = n * z + theta + omega_next
    assert low % (q2 // 64) == 0
    six = (low // (q2 // 64)) % 64
    matches = []
    for candidate in range(4):
        code = (P[candidate] * inv_next - P[j] * carry_next) % 64
        if code == six:
            matches.append(candidate)
    assert matches == [k]
    return z, z2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path, required=True)
    args = parser.parse_args()
    payload = json.loads(args.check_results.read_text(encoding="utf-8"))
    assert payload["experiment"] == "X-8501"
    digest = digest_without_field(payload)

    # Check the exact source cutoff independently.
    assert 2 ** 1287 > 3 ** 812
    assert 2 ** 1298 < 3 ** 819
    assert 13573 * 13573 - 13457 * 117 * 117 == 13456
    assert 118 * 118 < 13925

    # Recompute every committed refund row from direct sums.
    for row in payload["refund_rows"]:
        width = row["width"]
        base = row["least_multiple_16_base"]
        a, e, en = direct_stage_exponents(width, base)
        assert (a, e, en) == (
            row["odd_exponent"],
            row["current_binary_exponent"],
            row["next_binary_exponent"],
        )
        assert 84 * a - 53 * en == row["53_scaled_margin"] > 0
        if base:
            aa, _, ee = direct_stage_exponents(width, base - 16)
            assert 84 * aa <= 53 * ee

    normal_cases = 0
    for t in (48, 3744):
        check_carry_step(t)
        for i in range(4):
            for j in range(4):
                reconstruct_normal(t, i, j)
                normal_cases += 1

    decode_cases = 0
    for t in (3744,):
        n, q2 = odd(t), radix(t + 16)
        # Exact rational lower surrogate: N/Q > 2.
        assert 84 * 7 * (t + 1) - 53 * 11 * (t + 33) > 53
        assert n > 2 * q2
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for lift in (0, 2):
                        z, z2 = check_decoder(t, i, j, k, lift)
                        if z:
                            assert z2 >= 2 * z
                        decode_cases += 1

    phase_checks = 0
    for period in range(1, 59):
        for phase in range(period):
            for block in range(4, 9):
                index = period * block + phase
                lhs = index * (index - 1) // 2
                rhs = (period * period * block * (block - 1) // 2
                       + block * period * (period + 2 * phase - 1) // 2
                       + phase * (phase - 1) // 2)
                assert lhs == rhs
                phase_checks += 1

    # Directly rederive the local cylinder-depth law on a different horizon.
    depth_checks = 0
    t0 = 3760
    for length in range(1, 17):
        direct = sum(11 * (t0 + 16 * n + 33) for n in range(length))
        closed = 88 * length * length + (11 * t0 + 275) * length
        assert direct == closed
        assert 4 ** length <= 2 ** (2 * length)
        depth_checks += 1

    print("X-8501 independent checker")
    print(f"committed payload digest: {digest}")
    print(f"independent normal-form cases: {normal_cases}")
    print(f"independent decoder cases: {decode_cases}")
    print(f"independent phase-identity cases: {phase_checks}")
    print(f"independent cylinder-depth rows: {depth_checks}")
    print("all independent linear-refund checks passed")


if __name__ == "__main__":
    main()
