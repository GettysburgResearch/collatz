#!/usr/bin/env python3
"""Independent replay checker for X-9702.

This file does not import derive.py.  It recomputes the frozen exponent identity,
uses direct finite-state enumeration to verify composite domains/caps, checks the
committed digests, and rebuilds a separate family of quotient-exhaustion paths.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import product
from pathlib import Path


def hash_values(h: "hashlib._Hash", values: tuple[object, ...]) -> None:
    for value in values:
        if isinstance(value, int):
            sign = b"-" if value < 0 else b"+"
            magnitude = abs(value)
            raw = magnitude.to_bytes(max(1, (magnitude.bit_length() + 7) // 8), "big")
            h.update(b"I" + sign + len(raw).to_bytes(8, "big") + raw)
        else:
            raw = repr(value).encode("ascii")
            h.update(b"O" + len(raw).to_bytes(8, "big") + raw)


def parse_fraction(text: str) -> Fraction:
    a, b = text.split("/", 1)
    return Fraction(int(a), int(b))


def direct_replay(chain: tuple[tuple[int, int, int], ...], x: int) -> int | None:
    for N, q, C in chain:
        numerator = N * x + C
        if numerator % q:
            return None
        x = numerator // q
        if x < 0:
            return None
    return x


def independent_composite_audit() -> tuple[int, str]:
    # Different parameter set and direct residue enumeration, rather than the
    # recursive canonical formula used by derive.py.
    tiles: list[tuple[int, int, int]] = []
    for N in (1, 3):
        for q in (2, 4, 8):
            for rho in range(q):
                for psi in range(N):
                    tiles.append((N, q, q * psi - N * rho))

    checked = 0
    h = hashlib.sha256()
    for length in (1, 2, 3):
        for chain in product(tiles, repeat=length):
            Q = 1
            P = 1
            for N, q, _ in chain:
                Q *= q
                P *= N

            accepted: list[tuple[int, int]] = []
            for x in range(Q):
                out = direct_replay(chain, x)
                if out is not None:
                    accepted.append((x, out))
            assert len(accepted) == 1
            R, S = accepted[0]
            assert 0 <= R < Q
            assert 0 <= S < P
            for y in (0, 1, 3, 9):
                out = direct_replay(chain, R + Q * y)
                assert out == S + P * y
            hash_values(h, (chain, R, S, P, Q))
            checked += 1
    return checked, h.hexdigest()


def independent_quotient_paths() -> tuple[int, int, str]:
    h = hashlib.sha256()
    paths = 0
    zero_tail_steps = 0

    for seed in range(3, 52, 2):
        q = 1 << (7 + seed % 4)
        R = seed % q
        z = R + q * (1 << (80 + seed))
        seen_zero = False

        for step in range(10):
            q_next = q * q
            N = 2 * (seed + step + 1) + 1
            assert 4 * N < q_next
            S = (seed + 5 * step) % N
            C = q * S - N * R
            assert (N * R + C) // q == S

            Y = (z - R) // q
            assert Y >= 0 and z == R + q * Y
            z_next = (N * z + C) // q
            assert z_next == S + N * Y
            R_next = z_next % q_next
            Y_next = z_next // q_next

            # Exact ratio inequality, cross-multiplied without logarithms.
            assert z_next * q < N * (q + z)
            assert 4 * N < q_next

            if seen_zero:
                assert Y == 0 and z == R
                assert z_next == S == R_next
                assert Y_next == 0
                zero_tail_steps += 1
            elif Y_next == 0:
                seen_zero = True

            hash_values(h, (seed, step, q, N, R, S, Y, q_next, R_next, Y_next))
            q, R, z = q_next, R_next, z_next

        assert seen_zero
        paths += 1

    return paths, zero_tail_steps, h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path, required=True)
    args = parser.parse_args()
    payload = json.loads(args.check_results.read_text(encoding="utf-8"))

    assert payload["experiment"] == "X-9702"
    assert parse_fraction(payload["log2_3_upper"]) == Fraction(65, 41)
    assert parse_fraction(payload["coefficient"]) == Fraction(-22173699, 5248)
    assert parse_fraction(payload["constant"]) == Fraction(1024, 41)

    # Rebuild every exponent row directly.
    for row in payload["exponent_rows"]:
        m = int(row["m"])
        B = 1 << m
        A = 5369 * B // 2 + 1792
        D = 1085579 * B // 256 + 2816
        D_next = 1085579 * (2 * B) // 256 + 2816
        upper = Fraction(65 * A, 41) - D_next
        assert B == row["B"] and A == row["A"] and D == row["D"] and D_next == row["D_next"]
        assert upper == parse_fraction(row["upper_log2_epsilon"])
        assert upper < -2

    # Verify the payload digest before the independent computations.
    claimed_digest = payload.pop("payload_digest")
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert hashlib.sha256(canonical).hexdigest() == claimed_digest
    payload["payload_digest"] = claimed_digest

    chains, independent_cap_digest = independent_composite_audit()
    paths, zero_tail_steps, independent_path_digest = independent_quotient_paths()

    print(f"independent composite chains: {chains}")
    print(f"independent composite digest: {independent_cap_digest}")
    print(f"independent quotient paths: {paths}")
    print(f"verified zero-tail steps: {zero_tail_steps}")
    print(f"independent quotient digest: {independent_path_digest}")
    print(f"committed payload digest: {claimed_digest}")
    print("all independent stage-quotient checks passed")


if __name__ == "__main__":
    main()
