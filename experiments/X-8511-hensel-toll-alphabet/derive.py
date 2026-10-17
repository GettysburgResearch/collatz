#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

BETA = (2, 3, 2, 1)
P = (5, 30, 20, 56)
HEIGHTS = (16, 32, 48, 64)


def audit():
    counters = {
        "finite_states": 0,
        "unimodular_matrices": 0,
        "target_residues": 0,
        "affine_toll_rows": 0,
        "automatic_type_gates": 0,
        "primitive_two_of_three_gates": 0,
        "legal_refund_replays": 0,
        "intrinsic_inverse_checks": 0,
    }
    digest = hashlib.sha256()

    for t in HEIGHTS:
        for gamma in (1, 2, 3):
            for i in range(4):
                G = 7 * (t + 1) + gamma - BETA[i]
                D = 11 * (t + 17) - i
                A = 3**G
                twoD = 1 << D
                a = (-pow(A, -1, twoD)) % twoD
                h = (A * a + 1) // twoD
                assert twoD * h - A * a == 1

                E = 7 * (t + 17) + BETA[i]
                H = 1 << (11 * (t + 33))
                lam = (-pow(A, -1, H) * h) % H
                unit = (-pow(3, -(G + E), H)) % H

                counters["finite_states"] += 1
                counters["unimodular_matrices"] += 1

                for j in range(4):
                    Gp = E - BETA[j]
                    Dp = 11 * (t + 33) - j
                    Ap = 3**Gp
                    ap = (-pow(Ap, -1, 1 << Dp)) % (1 << Dp)
                    x = (1 << j) * ap
                    bj = (1 << j) * 3 ** BETA[j]

                    assert x == (-bj * pow(3, -E, H)) % H
                    rho = (pow(A, -1, H) * (x - h)) % H
                    assert rho == (lam + unit * bj) % H

                    Y0 = h + A * rho
                    assert (3 ** BETA[i] * Y0) % 64 == P[j]
                    tau = (A * rho + h - x) // H
                    assert tau >= 0

                    allowed = []
                    for ell_mod in range(3):
                        q = rho + H * ell_mod
                        C = a + twoD * q
                        if C % 3:
                            allowed.append(ell_mod)
                    assert len(allowed) == 2

                    counters["target_residues"] += 1
                    counters["affine_toll_rows"] += 1
                    counters["automatic_type_gates"] += 1
                    counters["primitive_two_of_three_gates"] += 1

                    for ell in allowed + [value + 3 for value in allowed]:
                        q = rho + H * ell
                        C = a + twoD * q
                        Y = (A * C + 1) // twoD
                        assert q == h * C - a * Y
                        Cp = Y >> j
                        assert Cp % 3
                        qp = (Cp - ap) // (1 << Dp)
                        assert qp == tau + A * ell
                        counters["legal_refund_replays"] += 1
                        counters["intrinsic_inverse_checks"] += 1

                    record = (
                        t, gamma, i, j, G, D, E, bj,
                        lam, unit, rho, tau, *allowed,
                    )
                    digest.update("|".join(map(str, record)).encode())
                    digest.update(b"\n")

    return {
        "experiment": "X-8511",
        "heights": list(HEIGHTS),
        "counters": counters,
        "semantic_digest": digest.hexdigest(),
    }


def summary(payload):
    c = payload["counters"]
    return "\n".join([
        "X-8511 Hensel quotient and fixed toll-alphabet audit",
        f"finite states:                    {c['finite_states']}",
        f"unimodular matrices:              {c['unimodular_matrices']}",
        f"target residues:                  {c['target_residues']}",
        f"affine toll rows:                 {c['affine_toll_rows']}",
        f"automatic type gates:             {c['automatic_type_gates']}",
        f"two-of-three primitive gates:     {c['primitive_two_of_three_gates']}",
        f"legal refund replays:             {c['legal_refund_replays']}",
        f"intrinsic inverse checks:         {c['intrinsic_inverse_checks']}",
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
