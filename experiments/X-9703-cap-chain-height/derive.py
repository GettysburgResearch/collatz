#!/usr/bin/env python3
"""Exact derivation checks for L-9703 and T-9704."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import product
from pathlib import Path

GAMMA = Fraction(161341, 10496)
C0 = Fraction(1024, 41)
DELTA = Fraction(1085579, 256)
LOW_GAMMA = Fraction(191801, 13568)
LOW_C0 = Fraction(1280, 53)


def hash_values(h: "hashlib._Hash", values: tuple[object, ...]) -> None:
    for value in values:
        if isinstance(value, int):
            raw = abs(value).to_bytes(max(1, (abs(value).bit_length() + 7) // 8), "big")
            h.update((b"-" if value < 0 else b"+") + len(raw).to_bytes(4, "big") + raw)
        else:
            raw = repr(value).encode("ascii")
            h.update(len(raw).to_bytes(4, "big") + raw)


def canonical_tile(N: int, q: int, C: int) -> tuple[int, int, int, int, int]:
    rho = (-C * pow(N, -1, q)) % q
    numerator = C + N * rho
    assert numerator % q == 0
    psi = numerator // q
    assert -q < C < N
    assert N > q
    assert 0 <= rho < q
    assert 0 <= psi < N
    return N, q, C, rho, psi


def compose(chain: tuple[tuple[int, int, int, int, int], ...]) -> tuple[int, int, int, int, int]:
    P, Q, F = 1, 1, 0
    for N, q, C, _, _ in chain:
        F = N * F + Q * C
        P *= N
        Q *= q
    R = (-F * pow(P, -1, Q)) % Q
    S = (F + P * R) // Q
    return P, Q, F, R, S


def expanding_audit() -> dict[str, int | str]:
    tiles: list[tuple[int, int, int, int, int]] = []
    for q in (2, 4, 8):
        for N in (3, 5, 7, 9, 11, 13, 15, 17):
            if N <= q:
                continue
            for C in range(-q + 1, N):
                tiles.append(canonical_tile(N, q, C))

    digest = hashlib.sha256()
    checked = 0
    for length in (1, 2):
        for chain in product(tiles, repeat=length):
            P, Q, F, R, S = compose(chain)
            assert 0 <= R < Q
            assert 0 <= S < P
            assert abs(F) < length * P
            for y in (0, 1, 4):
                value = R + Q * y
                for N, q, C, _, _ in chain:
                    numerator = N * value + C
                    assert numerator % q == 0
                    value = numerator // q
                    assert value >= 0
                assert value == S + P * y
            hash_values(digest, (chain, P, Q, F, R, S))
            checked += 1

    return {"tiles": len(tiles), "chains": checked, "digest": digest.hexdigest()}


def artificial_cap_paths() -> dict[str, int | str]:
    digest = hashlib.sha256()
    paths = 0
    steps = 0
    max_ratio = Fraction(0)

    for seed in range(1, 33):
        R = seed
        envelope = Fraction(R + 257)
        for index in range(7):
            Q = 1 << (12 * (1 << index))
            P = 301 * Q + 1 + 2 * ((seed + index) % 7)
            assert P % 2 == 1 and P > 257 * Q

            S = (P * R + Q // 2) // Q
            assert 0 <= S < P
            F = Q * S - P * R
            assert abs(F) < Q <= P < 256 * P

            slope = Fraction(P, Q)
            assert S + 257 < slope * (R + 257)
            envelope *= slope
            assert S + 257 < envelope

            max_ratio = max(max_ratio, Fraction((S + 257).bit_length(), Q.bit_length() - 1))
            hash_values(
                digest,
                (seed, index, Q, P, R, S, F, envelope.numerator, envelope.denominator),
            )
            R = S
            steps += 1
        paths += 1

    return {
        "paths": paths,
        "steps": steps,
        "digest": digest.hexdigest(),
        "max_bitlength_over_radix_bits": f"{max_ratio.numerator}/{max_ratio.denominator}",
    }


def build_payload() -> dict[str, object]:
    assert Fraction(5369, 2) * Fraction(65, 41) - DELTA == GAMMA
    assert Fraction(1792) * Fraction(65, 41) - 2816 == C0
    assert Fraction(5369, 2) * Fraction(84, 53) - DELTA == LOW_GAMMA
    assert Fraction(1792) * Fraction(84, 53) - 2816 == LOW_C0
    assert GAMMA / DELTA == Fraction(161341, 44508739)
    assert Fraction(161341, 44508739) < Fraction(1, 275)

    rows: list[dict[str, int | str]] = []
    for m in range(8, 33):
        B = 1 << m
        upper = GAMMA * B + C0
        lower = LOW_GAMMA * B + LOW_C0
        assert lower > 8
        rows.append(
            {
                "m": m,
                "B": B,
                "upper_log2_lambda": f"{upper.numerator}/{upper.denominator}",
                "lower_log2_lambda": f"{lower.numerator}/{lower.denominator}",
            }
        )

    payload: dict[str, object] = {
        "experiment": "X-9703",
        "status": "EMPIRICAL / EXACT FINITE CHECK",
        "gamma_upper": f"{GAMMA.numerator}/{GAMMA.denominator}",
        "delta": f"{DELTA.numerator}/{DELTA.denominator}",
        "height_ratio": "161341/44508739",
        "stage_rows": rows,
        "expanding_audit": expanding_audit(),
        "cap_paths": artificial_cap_paths(),
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
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n", encoding="utf-8")

    expanding = payload["expanding_audit"]
    caps = payload["cap_paths"]
    assert isinstance(expanding, dict) and isinstance(caps, dict)
    lines = [
        "X-9703 exact cap-chain height checks",
        f"stage coefficient rows: {len(payload['stage_rows'])}",
        f"expanding local tiles: {expanding['tiles']}",
        f"expanding composite chains: {expanding['chains']}",
        f"expanding-offset digest: {expanding['digest']}",
        f"artificial cap paths: {caps['paths']}",
        f"artificial cap steps: {caps['steps']}",
        f"cap-path digest: {caps['digest']}",
        f"asymptotic height ratio: {payload['height_ratio']}",
        f"payload digest: {payload['payload_digest']}",
        "all cap-chain height derivation checks passed",
    ]
    args.summary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
