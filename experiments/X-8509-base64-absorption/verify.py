#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

BETA = (2, 3, 2, 1)
P = (5, 30, 20, 56)
SAMPLES = (
    (64, 1, 0, 0),
    (64, 2, 1, 3),
    (80, 3, 2, 1),
    (96, 1, 3, 2),
)


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


def brute_blocks(t: int, gamma: int, i: int):
    G = 7 * (t + 1) + gamma - BETA[i]
    D = 11 * (t + 17) - i
    A = 3**G
    modulus = 1 << D
    a = (-pow(A, -1, modulus)) % modulus
    h = (A * a + 1) // modulus
    rows = []
    for q in range(192):
        C = a + modulus * q
        if math.gcd(C, 6) != 1:
            continue
        Y = h + A * q
        residue = (pow(3, BETA[i], 64) * (Y % 64)) % 64
        if residue not in P:
            continue
        j = P.index(residue)
        if v2(Y) != j:
            continue
        rows.append((j, q, C, Y >> j))
    assert len(rows) == 8
    return G, D, A, a, rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical", type=Path)
    args = parser.parse_args()

    data = json.loads(args.canonical.read_text())
    assert data["experiment"] == "X-8509"
    assert data["semantic_digest"] == (
        "b05a53257b8309fcd9da40d389ed87daa8ffdeb208b5c3837b726668ac002b91"
    )
    assert data["counters"]["continuations"] == 768
    assert data["counters"]["base64_replays"] == 2304

    states = blocks_checked = continuations = replays = 0
    for t, gamma, i, selected_j in SAMPLES:
        G, D, A, _, current = brute_blocks(t, gamma, i)
        H = 1 << (11 * (t + 33))
        B = H >> 6
        states += 1
        for j, qcurrent, R, S in [row for row in current if row[0] == selected_j]:
            blocks_checked += 1
            _, Dnext, _, anext, following = brute_blocks(
                t + 16, BETA[i], j
            )
            g = 3 * (1 << (6 - j))
            values = []
            for k in range(4):
                matches = [
                    row for row in following
                    if row[0] == k and row[2] % 3 == S % 3
                ]
                assert len(matches) == 1
                _, qnext, Rnext, _ = matches[0]
                delta = (Rnext - S) // g
                rho = (pow(A, -1, H) * delta) % H
                sigma = (S + g * A * rho - Rnext) // (g * H)
                values.append((k, qnext, rho, sigma))

            common = values[0][2] % B
            assert all(row[2] % B == common for row in values)
            digits = [(row[2] - common) // B for row in values]
            assert len(set(digits)) == 4

            residues = {row[1] % 3 for row in values}
            assert len(residues) == 1
            residue3 = residues.pop()
            outputs = [(row[1] - residue3) // 3 for row in values]
            assert len(set(outputs)) == 4

            carries = [
                (192 * row[3] - 3 * A * digit + row[1] - residue3) // 3
                for row, digit in zip(values, digits)
            ]
            assert len(set(carries)) == 1
            J = carries[0]
            assert 0 <= 3 * J < 4 * A

            for row, digit, output in zip(values, digits, outputs):
                assert output == (A * digit + J) % 64
                for ell in (0, 2):
                    z = digit + 64 * ell
                    mnext = row[3] + A * ell
                    assert A * z + J == 64 * mnext + output
                    replays += 1
                continuations += 1

    assert pow(3, 665) > pow(2, 1054)
    for t, factor, expected in (
        (5600, 1, False),
        (5616, 1, True),
        (5616, 2, False),
        (5632, 4, True),
    ):
        left = pow(3, 7 * t + 5)
        right = factor * (1 << (11 * (t + 49)))
        assert (left > right) is expected

    print("independent base-64 absorption verification passed")
    print(
        json.dumps(
            {
                "sample_states": states,
                "sample_blocks": blocks_checked,
                "continuations": continuations,
                "exact_replays": replays,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
