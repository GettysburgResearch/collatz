#!/usr/bin/env python3
"""Exact derivation checks for T-9703.

This script checks three finite interfaces only:
  1. the exact PR3 stage-exponent arithmetic and the certified bound
     3^A_m / 2^D_(m+1) < 1/4;
  2. the canonical-cap bound for exhaustive small chains of odd-affine
     Montgomery tiles;
  3. deterministic sample zipper paths whose free quotients exhaust.

The universal infinite conclusion is proved in T-9703, not by this script.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


def hash_values(h: "hashlib._Hash", values: Sequence[object]) -> None:
    """Hash integers in binary so huge values never require decimal rendering."""
    for value in values:
        if isinstance(value, int):
            sign = b"-" if value < 0 else b"+"
            magnitude = abs(value)
            raw = magnitude.to_bytes(max(1, (magnitude.bit_length() + 7) // 8), "big")
            h.update(b"I" + sign + len(raw).to_bytes(8, "big") + raw)
        else:
            raw = repr(value).encode("ascii")
            h.update(b"O" + len(raw).to_bytes(8, "big") + raw)

ALPHA = Fraction(5369, 2)
DELTA = Fraction(1085579, 256)
LOG2_3_UPPER = Fraction(65, 41)
COEFF = Fraction(-22173699, 5248)
CONSTANT = Fraction(1024, 41)


def stage_exponents(m: int) -> tuple[int, int]:
    if m < 8:
        raise ValueError("the corrected stage formulas are frozen for m >= 8")
    B = 1 << m
    A_num = 5369 * B
    D_num = 1085579 * B
    assert A_num % 2 == 0
    assert D_num % 256 == 0
    return A_num // 2 + 1792, D_num // 256 + 2816


def local_tile(N: int, q: int, rho: int, psi: int) -> tuple[int, int, int]:
    """Return (N,q,C) for the canonical tile rho+q*y -> psi+N*y."""
    if N <= 0 or N % 2 == 0:
        raise ValueError("N must be positive and odd")
    if q <= 0 or q & (q - 1):
        raise ValueError("q must be a power of two")
    if not (0 <= rho < q and 0 <= psi < N):
        raise ValueError("canonical digits out of range")
    C = q * psi - N * rho
    check_rho = (-C * pow(N, -1, q)) % q
    check_psi = (C + N * check_rho) // q
    assert (check_rho, check_psi) == (rho, psi)
    return N, q, C


def compose(chain: Sequence[tuple[int, int, int]]) -> tuple[int, int, int]:
    """Return P,Q,F with x_out=(P*x_in+F)/Q."""
    P, Q, F = 1, 1, 0
    for N, q, C in chain:
        F = N * F + Q * C
        P *= N
        Q *= q
    return P, Q, F


def canonical_composite(chain: Sequence[tuple[int, int, int]]) -> tuple[int, int, int, int]:
    P, Q, F = compose(chain)
    R = (-F * pow(P, -1, Q)) % Q
    S_num = F + P * R
    assert S_num % Q == 0
    S = S_num // Q
    return P, Q, R, S


def replay(chain: Sequence[tuple[int, int, int]], x: int) -> int:
    for N, q, C in chain:
        numerator = N * x + C
        assert numerator % q == 0
        x = numerator // q
        assert x >= 0
    return x


def iter_chains(tiles: Sequence[tuple[int, int, int]], length: int) -> Iterable[tuple[tuple[int, int, int], ...]]:
    if length == 0:
        yield ()
        return
    for prefix in iter_chains(tiles, length - 1):
        for tile in tiles:
            yield prefix + (tile,)


def exhaustive_cap_audit() -> dict[str, int | str]:
    tiles: list[tuple[int, int, int]] = []
    for N in (1, 3, 5):
        for q in (2, 4):
            for rho in range(q):
                for psi in range(N):
                    tiles.append(local_tile(N, q, rho, psi))

    h = hashlib.sha256()
    checked = 0
    max_Q_bits = 0
    for length in (1, 2, 3):
        for chain in iter_chains(tiles, length):
            P, Q, R, S = canonical_composite(chain)
            assert 0 <= R < Q
            assert 0 <= S < P
            for y in (0, 1, 2, 7):
                x = R + Q * y
                out = replay(chain, x)
                assert out == S + P * y
            hash_values(h, (chain, P, Q, R, S))
            checked += 1
            max_Q_bits = max(max_Q_bits, Q.bit_length())
    return {
        "local_tiles": len(tiles),
        "chains": checked,
        "max_Q_bits": max_Q_bits,
        "digest": h.hexdigest(),
    }


def sample_quotient_paths() -> dict[str, int | str]:
    """Construct deterministic canonical macro paths with q_(m+1)>4N_m.

    At each step the next correction is defined as the least residue of the
    current output.  The experiment verifies that the free quotient becomes
    zero and thereafter the cap equals the next correction.
    """
    h = hashlib.sha256()
    paths = 0
    stages = 0
    max_positive_quotient_steps = 0

    for seed in range(1, 65):
        q = 1 << (8 + seed % 5)
        R = (17 * seed + 3) % q
        Y = (10 ** (20 + seed % 11)) + seed
        z = R + q * Y
        positive_steps = 0
        exhausted = False

        for step in range(8):
            # q_next squares, while N is deliberately much smaller.
            q_next = q * q
            N = 2 * (q // 8 + seed + step) + 1
            while 4 * N >= q_next:
                N = (N - 1) // 2 | 1
            assert N > 0 and N % 2 == 1 and 4 * N < q_next
            S = (seed * 13 + step * 7) % N
            C = q * S - N * R
            assert (-C * pow(N, -1, q)) % q == R

            current_Y = (z - R) // q
            assert z == R + q * current_Y and current_Y >= 0
            if current_Y > 0:
                positive_steps += 1
            z_next = (N * z + C) // q
            assert z_next == S + N * current_Y

            R_next = z_next % q_next
            Y_next = z_next // q_next
            if current_Y == 0:
                assert z_next == S
                assert Y_next == 0
                assert R_next == S
                exhausted = True

            hash_values(h, (seed, step, q, N, R, S, current_Y, q_next, R_next, Y_next))
            stages += 1
            q, R, Y, z = q_next, R_next, Y_next, z_next

        assert exhausted or Y == 0
        max_positive_quotient_steps = max(max_positive_quotient_steps, positive_steps)
        paths += 1

    return {
        "paths": paths,
        "stages": stages,
        "max_positive_quotient_steps": max_positive_quotient_steps,
        "digest": h.hexdigest(),
    }


def build_payload() -> dict[str, object]:
    assert ALPHA * LOG2_3_UPPER - 2 * DELTA == COEFF
    assert Fraction(1792) * LOG2_3_UPPER - 2816 == CONSTANT
    assert COEFF + CONSTANT < -2

    exponent_rows: list[dict[str, object]] = []
    for m in range(8, 25):
        B = 1 << m
        A, D = stage_exponents(m)
        _, D_next = stage_exponents(m + 1)
        upper = Fraction(A) * LOG2_3_UPPER - D_next
        closed = COEFF * B + CONSTANT
        assert upper == closed
        assert upper < -2
        exponent_rows.append({
            "m": m,
            "B": B,
            "A": A,
            "D": D,
            "D_next": D_next,
            "upper_log2_epsilon": f"{upper.numerator}/{upper.denominator}",
        })

    payload: dict[str, object] = {
        "experiment": "X-9702",
        "status": "EMPIRICAL / EXACT FINITE CHECK",
        "log2_3_upper": "65/41",
        "coefficient": f"{COEFF.numerator}/{COEFF.denominator}",
        "constant": f"{CONSTANT.numerator}/{CONSTANT.denominator}",
        "exponent_rows": exponent_rows,
        "cap_audit": exhaustive_cap_audit(),
        "quotient_paths": sample_quotient_paths(),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload["payload_digest"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()

    payload = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cap = payload["cap_audit"]
    paths = payload["quotient_paths"]
    assert isinstance(cap, dict) and isinstance(paths, dict)
    lines = [
        "X-9702 exact stage-quotient exhaustion checks",
        f"stage exponent rows: {len(payload['exponent_rows'])}",
        f"exhaustive local tiles: {cap['local_tiles']}",
        f"exhaustive composite chains: {cap['chains']}",
        f"composite-cap digest: {cap['digest']}",
        f"deterministic quotient paths: {paths['paths']}",
        f"deterministic quotient stages: {paths['stages']}",
        f"maximum positive-quotient steps: {paths['max_positive_quotient_steps']}",
        f"quotient-path digest: {paths['digest']}",
        f"payload digest: {payload['payload_digest']}",
        "all derivation checks passed",
    ]
    args.summary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
