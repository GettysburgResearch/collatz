#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

BETA = (2, 3, 2, 1)
P = (5, 30, 20, 56)
SAMPLES = (
    (48, 1, 0),
    (48, 3, 3),
    (80, 2, 1),
    (3760, 1, 1),
    (3760, 3, 3),
    (3776, 1, 1),
)


def valuation_two(value: int) -> int:
    return (value & -value).bit_length() - 1


def enumerate_blocks(t: int, gamma: int, i: int):
    G = 7 * (t + 1) + gamma - BETA[i]
    D = 11 * (t + 17) - i
    A = 3**G
    modulus = 1 << D
    source = (-pow(A, -1, modulus)) % modulus
    first_output = (A * source + 1) // modulus

    rows = []
    # Brute force q modulo 192. This independently resolves the six binary
    # output bits and the ternary primitive-core gate without importing the
    # author's kappa/nu formulas.
    for q in range(192):
        C = source + modulus * q
        if math.gcd(C, 6) != 1:
            continue
        Y = first_output + A * q
        residue = (pow(3, BETA[i], 64) * (Y % 64)) % 64
        if residue not in P:
            continue
        j = P.index(residue)
        if valuation_two(Y) != j:
            continue
        Cnext = Y >> j
        assert math.gcd(Cnext, 6) == 1
        rows.append((j, q // 64, C, Cnext))
    assert len(rows) == 8
    return G, D, A, rows


def verify_samples():
    counts = {
        "sample_states": 0,
        "enumerated_blocks": 0,
        "continuations": 0,
        "exact_replays": 0,
    }
    digest = hashlib.sha256()

    for t, gamma, i in SAMPLES:
        G, D, A, blocks = enumerate_blocks(t, gamma, i)
        counts["sample_states"] += 1
        counts["enumerated_blocks"] += len(blocks)

        next_cache = {
            j: enumerate_blocks(t + 16, BETA[i], j)
            for j in range(4)
        }
        Qcurrent = 3 * (1 << (D + 6))

        for j, nu, R, S in blocks:
            _, Dnext, _, next_rows = next_cache[j]
            Qnext = 3 * (1 << (Dnext + 6))
            Pcoeff = 3 * (1 << (6 - j)) * A
            common = math.gcd(Pcoeff, Qnext)
            reduced_coefficient = Pcoeff // common
            reduced_modulus = Qnext // common
            assert common == 3 * (1 << (6 - j))
            assert reduced_coefficient == A
            assert reduced_modulus == 1 << (11 * (t + 33))

            rhos = []
            for k in range(4):
                matches = [
                    row for row in next_rows
                    if row[0] == k
                    and row[2] % 3 == S % 3
                    and (row[2] - S) % common == 0
                ]
                assert len(matches) == 1
                _, mu, Rnext, _ = matches[0]
                delta = (Rnext - S) // common
                rho = (pow(A, -1, reduced_modulus) * delta) % reduced_modulus
                sigma = (S + Pcoeff * rho - Rnext) // Qnext
                assert sigma >= 0
                rhos.append(rho)

                for ell in (0, 1, 3):
                    m = rho + reduced_modulus * ell
                    C = R + Qcurrent * m
                    Cnext = S + Pcoeff * m
                    mnext = sigma + A * ell
                    assert Cnext == Rnext + Qnext * mnext
                    assert A * C + 1 == (1 << (D + j)) * Cnext
                    counts["exact_replays"] += 1

                record = (
                    t, gamma, i, j, nu, k, mu,
                    rho, sigma, reduced_modulus, A,
                )
                text = "|".join(
                    str(value) if pos < 7 else hex(value)
                    for pos, value in enumerate(record)
                )
                digest.update(text.encode())
                digest.update(b"\n")
                counts["continuations"] += 1

            assert len(set(rhos)) == 4

    return counts, digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical", type=Path)
    args = parser.parse_args()

    canonical = json.loads(args.canonical.read_text())
    assert canonical["transition_digest"] == (
        "66c03b99bb494255cc8d56f1e226c3f850f9548a60a0e3d3a036abac449cc724"
    )
    assert canonical["counters"]["continuations"] == 1536
    assert canonical["counters"]["exact_replays"] == 4608
    assert canonical["threshold"]["strict_refund_height"] == 3760
    assert canonical["threshold"]["doubling_refund_height"] == 3776

    assert 3**665 > 2**1054
    assert 3 ** (7 * 3744 + 5) <= 2 * (1 << (11 * (3744 + 33)))
    assert 3 ** (7 * 3760 + 5) > 2 * (1 << (11 * (3760 + 33)))
    assert 3 ** (7 * 3760 + 5) <= 4 * (1 << (11 * (3760 + 33)))
    assert 3 ** (7 * 3776 + 5) > 4 * (1 << (11 * (3776 + 33)))

    counts, digest = verify_samples()
    print("independent top-boundary verification passed")
    print(json.dumps(counts, sort_keys=True))
    print(f"independent digest: {digest}")


if __name__ == "__main__":
    main()
