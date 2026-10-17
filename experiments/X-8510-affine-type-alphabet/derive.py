#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

BETA = (2, 3, 2, 1)
P = (5, 30, 20, 56)
HEIGHTS = (16, 32, 48, 64)


def blocks(t: int, gamma: int, i: int):
    G = 7 * (t + 1) + gamma - BETA[i]
    D = 11 * (t + 17) - i
    A = 3**G
    twoD = 1 << D
    a = (-pow(A, -1, twoD)) % twoD
    h = (A * a + 1) // twoD
    rows = []
    for j in range(4):
        kappa = (
            pow(A, -1, 64)
            * ((pow(3 ** BETA[i], -1, 64) * P[j] - h) % 64)
        ) % 64
        R = a + twoD * kappa
        S = (h + A * kappa) // (1 << j)
        for nu in range(3):
            Rhat = R + (1 << (D + 6)) * nu
            if Rhat % 3:
                Shat = S + (1 << (6 - j)) * A * nu
                rows.append((j, nu, Rhat, Shat))
    assert len(rows) == 8
    return G, D, A, a, rows


def router(t: int, gamma: int, i: int, j: int, nu: int):
    G, D, A, _, current = blocks(t, gamma, i)
    _, _, _, S = next(row for row in current if row[0] == j and row[1] == nu)

    _, nextD, _, nexta, following = blocks(t + 16, BETA[i], j)
    H = 1 << (11 * (t + 33))
    B = H >> 6
    g = 3 * (1 << (6 - j))
    invA = pow(A, -1, H)

    values = []
    for k in range(4):
        matches = [
            row for row in following
            if row[0] == k and row[2] % 3 == S % 3
        ]
        assert len(matches) == 1
        _, mu, Rnext, _ = matches[0]
        qnext = (Rnext - nexta) // (1 << nextD)
        delta = (Rnext - S) // g
        rho = (invA * delta) % H
        sigma = (S + g * A * rho - Rnext) // (g * H)
        assert sigma >= 0
        values.append((k, mu, qnext, rho, sigma))

    lam = values[0][3] % B
    assert all(value[3] % B == lam for value in values)
    d = tuple((value[3] - lam) // B for value in values)

    residues3 = {value[2] % 3 for value in values}
    assert len(residues3) == 1
    r = residues3.pop()
    e = tuple((value[2] - r) // 3 for value in values)

    Kvalues = tuple(
        192 * value[4] - 3 * A * digit + value[2]
        for value, digit in zip(values, d)
    )
    assert len(set(Kvalues)) == 1
    J = (Kvalues[0] - r) // 3
    assert J >= 0
    return A, d, e, J


def audit():
    counters = {
        "finite_states": 0,
        "current_blocks": 0,
        "continuations": 0,
        "input_affine_alphabets": 0,
        "output_affine_alphabets": 0,
        "slope_compatibilities": 0,
        "symbol_identity_checks": 0,
        "translation_carry_checks": 0,
    }
    digest = hashlib.sha256()

    for t in HEIGHTS:
        for gamma in (1, 2, 3):
            u = pow(3, 1 - gamma, 64)
            u_inv = pow(u, -1, 64)
            for i in range(4):
                v = pow(3, 8 - BETA[i], 64)
                v_inv = pow(v, -1, 64)
                G, _, A, _, rows = blocks(t, gamma, i)
                assert G == 7 * (t + 1) + gamma - BETA[i]
                assert A * u % 64 == v
                counters["finite_states"] += 1

                for j, nu, _, _ in rows:
                    A2, d, e, J = router(t, gamma, i, j, nu)
                    assert A2 == A
                    counters["current_blocks"] += 1

                    delta = (d[0] - u * P[0]) % 64
                    epsilon = (e[0] - v * P[0]) % 64
                    assert all(d[k] == (u * P[k] + delta) % 64 for k in range(4))
                    assert all(e[k] == (v * P[k] + epsilon) % 64 for k in range(4))
                    assert epsilon == (A * delta + J) % 64

                    counters["input_affine_alphabets"] += 1
                    counters["output_affine_alphabets"] += 1
                    counters["slope_compatibilities"] += 1
                    counters["translation_carry_checks"] += 1

                    for k in range(4):
                        pin = u_inv * (d[k] - delta) % 64
                        pout = v_inv * (e[k] - epsilon) % 64
                        assert pin == P[k] == pout
                        counters["symbol_identity_checks"] += 1
                        counters["continuations"] += 1
                        record = (
                            t, gamma, i, j, nu, k,
                            u, v, delta, epsilon, d[k], e[k], J % 64,
                        )
                        digest.update("|".join(map(str, record)).encode())
                        digest.update(b"\n")

    return {
        "experiment": "X-8510",
        "heights": list(HEIGHTS),
        "counters": counters,
        "slopes": {
            "input_by_gamma": {
                str(gamma): pow(3, 1 - gamma, 64)
                for gamma in (1, 2, 3)
            },
            "output_by_type": {
                str(i): pow(3, 8 - BETA[i], 64)
                for i in range(4)
            },
        },
        "semantic_digest": digest.hexdigest(),
    }


def summary(payload):
    c = payload["counters"]
    return "\n".join([
        "X-8510 affine type-alphabet audit",
        f"finite states:                    {c['finite_states']}",
        f"current blocks:                   {c['current_blocks']}",
        f"four-way continuations:           {c['continuations']}",
        f"input affine alphabets:           {c['input_affine_alphabets']}",
        f"output affine alphabets:          {c['output_affine_alphabets']}",
        f"slope compatibility checks:       {c['slope_compatibilities']}",
        f"symbol identity checks:           {c['symbol_identity_checks']}",
        f"translation/carry checks:         {c['translation_carry_checks']}",
        f"semantic digest:                  {payload['semantic_digest']}",
        "",
    ])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--summary", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = audit()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.check_results and args.check_results.read_text() != text:
        raise SystemExit("canonical result mismatch")
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
    if args.summary:
        args.summary.write_text(summary(payload))


if __name__ == "__main__":
    main()
