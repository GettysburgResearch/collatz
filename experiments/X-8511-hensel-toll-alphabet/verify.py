#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

BETA = (2, 3, 2, 1)
P = (5, 30, 20, 56)


def reconstruct(payload):
    counters = {key: 0 for key in payload["counters"]}
    digest = hashlib.sha256()

    for t in payload["heights"]:
        for gamma in (1, 2, 3):
            for i in range(4):
                G = 7 * (t + 1) + gamma - BETA[i]
                D = 11 * (t + 17) - i
                A = 3**G
                M = 1 << D

                # Independent extended-Euclidean inverse construction.
                a = (-pow(A, -1, M)) % M
                numerator = A * a + 1
                assert numerator % M == 0
                h = numerator // M
                assert M * h - A * a == 1

                E = 7 * (t + 17) + BETA[i]
                H = 1 << (11 * (t + 33))
                invA = pow(A, -1, H)
                base = (-invA * h) % H
                slope = (-pow(pow(3, G + E, H), -1, H)) % H

                counters["finite_states"] += 1
                counters["unimodular_matrices"] += 1

                for j, p in enumerate(P):
                    nextG = 7 * (t + 17) + BETA[i] - BETA[j]
                    nextD = 11 * (t + 33) - j
                    nextA = 3**nextG
                    nextM = 1 << nextD
                    nexta = (-pow(nextA, -1, nextM)) % nextM
                    x = (1 << j) * nexta
                    bj = (1 << j) * 3 ** BETA[j]

                    assert (pow(3, E, H) * x + bj) % H == 0
                    assert 0 <= x < H
                    rho = (invA * (x - h)) % H
                    assert rho == (base + slope * bj) % H

                    Y0 = h + A * rho
                    assert (3 ** BETA[i] * Y0) % 64 == p
                    assert (A * rho + h - x) % H == 0
                    tau = (A * rho + h - x) // H
                    assert tau >= 0

                    allowed = tuple(
                        ell
                        for ell in range(3)
                        if (a + M * (rho + H * ell)) % 3
                    )
                    assert len(allowed) == 2

                    counters["target_residues"] += 1
                    counters["affine_toll_rows"] += 1
                    counters["automatic_type_gates"] += 1
                    counters["primitive_two_of_three_gates"] += 1

                    for ell in allowed + tuple(value + 3 for value in allowed):
                        q = rho + H * ell
                        C = a + M * q
                        Y = h + A * q
                        assert M * Y == A * C + 1
                        assert q == h * C - a * Y
                        assert Y % (1 << j) == 0
                        Cp = Y // (1 << j)
                        assert Cp % 3
                        assert (Cp - nexta) % nextM == 0
                        qp = (Cp - nexta) // nextM
                        assert qp == tau + A * ell
                        counters["legal_refund_replays"] += 1
                        counters["intrinsic_inverse_checks"] += 1

                    record = (
                        t, gamma, i, j, G, D, E, bj,
                        base, slope, rho, tau, *allowed,
                    )
                    digest.update("|".join(map(str, record)).encode())
                    digest.update(b"\n")

    assert counters == payload["counters"]
    assert digest.hexdigest() == payload["semantic_digest"]


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py results/canonical.json")
    payload = json.loads(Path(sys.argv[1]).read_text())
    reconstruct(payload)
    print("X-8511 independent Hensel-toll checks passed")


if __name__ == "__main__":
    main()
