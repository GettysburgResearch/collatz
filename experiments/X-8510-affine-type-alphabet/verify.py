#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

BETA = (2, 3, 2, 1)
P = (5, 30, 20, 56)


def brute_blocks(t: int, gamma: int, i: int):
    G = 7 * (t + 1) + gamma - BETA[i]
    D = 11 * (t + 17) - i
    A = 3**G
    twoD = 1 << D
    a = (-pow(A, -1, twoD)) % twoD
    h = (A * a + 1) // twoD
    rows = []

    for kappa in range(64):
        y = h + A * kappa
        for j, p in enumerate(P):
            target = pow(3 ** BETA[i], -1, 64) * p % 64
            if y % 64 != target:
                continue
            if y % (1 << j) or (y // (1 << j)) % 2 != 1:
                continue
            R = a + twoD * kappa
            S = y // (1 << j)
            for nu in range(3):
                Rhat = R + (1 << (D + 6)) * nu
                if Rhat % 3:
                    Shat = S + (1 << (6 - j)) * A * nu
                    rows.append((j, nu, Rhat, Shat))

    rows.sort()
    assert len(rows) == 8
    assert len({(row[0], row[1]) for row in rows}) == 8
    return G, D, A, a, tuple(rows)


def independently_reconstruct(payload):
    counters = {key: 0 for key in payload["counters"]}
    digest = hashlib.sha256()

    for t in payload["heights"]:
        for gamma in (1, 2, 3):
            u = pow(pow(3, gamma - 1, 64), -1, 64)
            u_inv = pow(u, -1, 64)
            for i in range(4):
                v = pow(3, 8 - BETA[i], 64)
                v_inv = pow(v, -1, 64)
                G, D, A, _, current = brute_blocks(t, gamma, i)
                assert A * u % 64 == v
                counters["finite_states"] += 1

                for j, nu, _, S in current:
                    _, nextD, _, nexta, following = brute_blocks(
                        t + 16, BETA[i], j
                    )
                    H = 1 << (11 * (t + 33))
                    B = H >> 6
                    g = 3 * (1 << (6 - j))
                    values = []

                    for k in range(4):
                        matches = [
                            row for row in following
                            if row[0] == k and row[2] % 3 == S % 3
                        ]
                        assert len(matches) == 1
                        _, mu, Rnext, _ = matches[0]
                        qnext = (Rnext - nexta) // (1 << nextD)
                        rhs = (Rnext - S) // g
                        rho = rhs * pow(A, -1, H) % H
                        numerator = S + g * A * rho - Rnext
                        assert numerator % (g * H) == 0
                        sigma = numerator // (g * H)
                        assert sigma >= 0
                        values.append((k, mu, qnext, rho, sigma))

                    lam = values[0][3] % B
                    assert all(value[3] % B == lam for value in values)
                    d = tuple((value[3] - lam) // B for value in values)

                    residue3 = values[0][2] % 3
                    assert all(value[2] % 3 == residue3 for value in values)
                    e = tuple((value[2] - residue3) // 3 for value in values)

                    Jvalues = tuple(
                        (
                            192 * value[4]
                            - 3 * A * digit
                            + value[2]
                            - residue3
                        ) // 3
                        for value, digit in zip(values, d)
                    )
                    assert len(set(Jvalues)) == 1
                    J = Jvalues[0]

                    delta = (d[0] - u * P[0]) % 64
                    epsilon = (e[0] - v * P[0]) % 64
                    assert tuple((u * p + delta) % 64 for p in P) == d
                    assert tuple((v * p + epsilon) % 64 for p in P) == e
                    assert epsilon == (A * delta + J) % 64

                    counters["current_blocks"] += 1
                    counters["input_affine_alphabets"] += 1
                    counters["output_affine_alphabets"] += 1
                    counters["slope_compatibilities"] += 1
                    counters["translation_carry_checks"] += 1

                    for k in range(4):
                        assert u_inv * (d[k] - delta) % 64 == P[k]
                        assert v_inv * (e[k] - epsilon) % 64 == P[k]
                        counters["symbol_identity_checks"] += 1
                        counters["continuations"] += 1
                        record = (
                            t, gamma, i, j, nu, k,
                            u, v, delta, epsilon, d[k], e[k], J % 64,
                        )
                        digest.update("|".join(map(str, record)).encode())
                        digest.update(b"\n")

    assert counters == payload["counters"]
    assert digest.hexdigest() == payload["semantic_digest"]
    assert payload["slopes"]["input_by_gamma"] == {
        "1": 1, "2": 43, "3": 57,
    }
    assert payload["slopes"]["output_by_type"] == {
        "0": 25, "1": 51, "2": 25, "3": 11,
    }


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py results/canonical.json")
    payload = json.loads(Path(sys.argv[1]).read_text())
    independently_reconstruct(payload)
    print("X-8510 independent affine-alphabet checks passed")


if __name__ == "__main__":
    main()
