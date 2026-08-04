#!/usr/bin/env python3
"""Independent exact checker for X-9703."""
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
            raw = abs(value).to_bytes(max(1, (abs(value).bit_length() + 7) // 8), "big")
            h.update((b"-" if value < 0 else b"+") + len(raw).to_bytes(4, "big") + raw)
        else:
            raw = repr(value).encode("ascii")
            h.update(len(raw).to_bytes(4, "big") + raw)


def parse_fraction(text: str) -> Fraction:
    numerator, denominator = text.split("/", 1)
    return Fraction(int(numerator), int(denominator))


def independent_offset_audit() -> tuple[int, str]:
    # Different bases and radices from derive.py.  Composition is performed
    # directly, without using its canonical helper.
    tiles: list[tuple[int, int, int]] = []
    for q in (2, 8):
        for N in (5, 9, 13, 17, 21):
            if N <= q:
                continue
            for C in range(-q + 1, N, 2):
                rho = (-C * pow(N, -1, q)) % q
                psi = (C + N * rho) // q
                assert 0 <= psi < N
                tiles.append((N, q, C))

    digest = hashlib.sha256()
    checked = 0
    for length in (1, 2, 3):
        for index, chain in enumerate(product(tiles, repeat=length)):
            if length == 3 and index % 97:
                continue
            P, Q, F = 1, 1, 0
            for N, q, C in chain:
                F = N * F + Q * C
                P *= N
                Q *= q
            assert abs(F) < length * P
            R = (-F * pow(P, -1, Q)) % Q
            S = (F + P * R) // Q
            assert 0 <= R < Q and 0 <= S < P
            hash_values(digest, (chain, P, Q, F, R, S))
            checked += 1
    return checked, digest.hexdigest()


def independent_cap_paths() -> tuple[int, int, str]:
    digest = hashlib.sha256()
    paths = 0
    steps = 0

    for seed in range(2, 29):
        R = seed * seed
        envelope = Fraction(R + 257)
        for index in range(6):
            Q = 1 << (10 * (1 << index))
            P = (263 + 2 * ((seed + 3 * index) % 11)) * Q + 1
            assert P % 2 == 1 and P > 257 * Q
            S = (P * R) // Q
            F = Q * S - P * R
            assert abs(F) < Q < P
            slope = Fraction(P, Q)
            assert S + 257 < slope * (R + 257)
            envelope *= slope
            assert S + 257 < envelope
            hash_values(digest, (seed, index, Q, P, R, S, F))
            R = S
            steps += 1
        paths += 1

    return paths, steps, digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path, required=True)
    args = parser.parse_args()

    payload = json.loads(args.check_results.read_text(encoding="utf-8"))
    claimed_digest = payload.pop("payload_digest")
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert hashlib.sha256(canonical).hexdigest() == claimed_digest
    payload["payload_digest"] = claimed_digest

    gamma = parse_fraction(payload["gamma_upper"])
    delta = parse_fraction(payload["delta"])
    ratio = parse_fraction(payload["height_ratio"])
    assert gamma == Fraction(161341, 10496)
    assert delta == Fraction(1085579, 256)
    assert ratio == gamma / delta < Fraction(1, 275)

    for row in payload["stage_rows"]:
        B = 1 << int(row["m"])
        assert parse_fraction(row["upper_log2_lambda"]) == gamma * B + Fraction(1024, 41)
        assert parse_fraction(row["lower_log2_lambda"]) == (
            Fraction(191801, 13568) * B + Fraction(1280, 53)
        ) > 8

    chains, expanding_digest = independent_offset_audit()
    paths, steps, cap_digest = independent_cap_paths()

    print(f"independent expanding chains: {chains}")
    print(f"independent expanding digest: {expanding_digest}")
    print(f"independent cap paths: {paths}")
    print(f"independent cap steps: {steps}")
    print(f"independent cap digest: {cap_digest}")
    print(f"committed payload digest: {claimed_digest}")
    print("all independent cap-chain height checks passed")


if __name__ == "__main__":
    main()
