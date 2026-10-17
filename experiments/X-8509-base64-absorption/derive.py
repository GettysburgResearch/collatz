#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

BETA = (2, 3, 2, 1)
P = (5, 30, 20, 56)
HEIGHTS = (32, 48)


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


def audit():
    counters = {
        "finite_states": 0,
        "current_blocks": 0,
        "continuations": 0,
        "common_prefix_sets": 0,
        "distinct_input_digits": 0,
        "common_ternary_residues": 0,
        "distinct_output_digits": 0,
        "common_carries": 0,
        "carry_bounds": 0,
        "base64_replays": 0,
    }
    digest = hashlib.sha256()

    for t in HEIGHTS:
        H = 1 << (11 * (t + 33))
        B = H >> 6
        for gamma in (1, 2, 3):
            for i in range(4):
                G, D, A, _, current = blocks(t, gamma, i)
                counters["finite_states"] += 1
                for j, nu, R, S in current:
                    counters["current_blocks"] += 1
                    nextG, nextD, nextA, nexta, following = blocks(
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
                        _, mu, Rnext, _ = matches[0]
                        qnext = (Rnext - nexta) // (1 << nextD)
                        delta = (Rnext - S) // g
                        rho = (pow(A, -1, H) * delta) % H
                        sigma = (S + g * A * rho - Rnext) // (g * H)
                        assert sigma >= 0
                        values.append((k, mu, Rnext, qnext, rho, sigma))

                    lam = values[0][4] % B
                    assert all(value[4] % B == lam for value in values)
                    counters["common_prefix_sets"] += 1

                    d = [(value[4] - lam) // B for value in values]
                    assert all(0 <= digit < 64 for digit in d)
                    assert len(set(d)) == 4
                    counters["distinct_input_digits"] += 1

                    residues3 = {value[3] % 3 for value in values}
                    assert len(residues3) == 1
                    r = residues3.pop()
                    counters["common_ternary_residues"] += 1

                    e = [(value[3] - r) // 3 for value in values]
                    assert all(0 <= digit < 64 for digit in e)
                    assert len(set(e)) == 4
                    counters["distinct_output_digits"] += 1

                    Kvalues = [
                        192 * value[5] - 3 * A * digit + value[3]
                        for value, digit in zip(values, d)
                    ]
                    assert len(set(Kvalues)) == 1
                    K = Kvalues[0]
                    assert K % 3 == r
                    J = (K - r) // 3
                    assert J >= 0 and 3 * J < 4 * A
                    counters["common_carries"] += 1
                    counters["carry_bounds"] += 1

                    for index, value in enumerate(values):
                        k, mu, Rnext, qnext, rho, sigma = value
                        assert e[index] == (A * d[index] + J) % 64
                        for ell in (0, 1, 2):
                            z = d[index] + 64 * ell
                            mnext = sigma + A * ell
                            total = A * z + J
                            assert total == 64 * mnext + e[index]
                            assert mnext == total // 64
                            assert e[index] == total % 64
                            counters["base64_replays"] += 1

                        record = (
                            t, gamma, i, j, nu, k, mu,
                            lam, d[index], e[index], J, A,
                        )
                        encoded = "|".join(
                            str(x) if pos < 7 else hex(x)
                            for pos, x in enumerate(record)
                        )
                        digest.update(encoded.encode())
                        digest.update(b"\n")
                        counters["continuations"] += 1

    assert 3**665 > 2**1054
    q = lambda t: (63 * t - 353_166) // 665
    threshold = {
        "first_preservation_multiple_16": 5616,
        "first_factor4_multiple_16": 5632,
        "q_5600": q(5600),
        "q_5616": q(5616),
        "q_5632": q(5632),
        "factor4_margin": 63 * 5632 - 353_165 - 2 * 665,
        "canonical_uniform_limit": 471,
        "canonical_eventual_limit": 234,
    }
    assert threshold["q_5600"] < 0
    assert threshold["q_5616"] == 0
    assert threshold["q_5632"] == 2
    assert threshold["factor4_margin"] == 321

    return {
        "experiment": "X-8509",
        "heights": list(HEIGHTS),
        "counters": counters,
        "absorption": threshold,
        "semantic_digest": digest.hexdigest(),
    }


def summary(payload):
    c = payload["counters"]
    a = payload["absorption"]
    return "\n".join(
        [
            "X-8509 base-64 top-cell and absorption audit",
            f"finite states:                    {c['finite_states']}",
            f"current blocks:                   {c['current_blocks']}",
            f"four-way continuations:           {c['continuations']}",
            f"common long prefixes:             {c['common_prefix_sets']}",
            f"distinct input digit sets:        {c['distinct_input_digits']}",
            f"distinct output digit sets:       {c['distinct_output_digits']}",
            f"common carry identities:          {c['common_carries']}",
            f"base-64 exact replays:             {c['base64_replays']}",
            f"noncanonical preservation height: {a['first_preservation_multiple_16']}",
            f"factor-4 absorption height:        {a['first_factor4_multiple_16']}",
            f"semantic digest:                  {payload['semantic_digest']}",
            "",
        ]
    )


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
