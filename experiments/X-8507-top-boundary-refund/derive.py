#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

BETA = (2, 3, 2, 1)
P = (5, 30, 20, 56)
HEIGHTS = (32, 64, 3760, 3776)


def block_data(t: int, gamma: int, i: int):
    G = 7 * (t + 1) + gamma - BETA[i]
    D = 11 * (t + 17) - i
    A = 3**G
    modulus = 1 << D
    a = (-pow(A, -1, modulus)) % modulus
    h = (A * a + 1) // modulus

    blocks = []
    inv_a64 = pow(A, -1, 64)
    inv_sig64 = pow(3 ** BETA[i], -1, 64)
    for j in range(4):
        kappa = (inv_a64 * ((inv_sig64 * P[j] - h) % 64)) % 64
        R = a + modulus * kappa
        S = (h + A * kappa) // (1 << j)
        assert S & 1 and S % 3
        step = 1 << (D + 6)
        allowed = []
        for nu in range(3):
            Rhat = R + step * nu
            if Rhat % 3:
                Shat = S + (1 << (6 - j)) * A * nu
                assert (A * Rhat + 1) == (1 << (D + j)) * Shat
                allowed.append((j, nu, Rhat, Shat))
        assert len(allowed) == 2
        blocks.extend(allowed)
    return G, D, A, blocks


def all_blocks(t: int):
    return {
        (gamma, i): block_data(t, gamma, i)
        for gamma in (1, 2, 3)
        for i in range(4)
    }


def transition_table(t: int, current, following):
    H = 1 << (11 * (t + 33))
    table = {}
    for (gamma, i), (G, D, A, blocks) in current.items():
        inv_a = pow(A, -1, H)
        state_rows = {}
        for j, nu, R, S in blocks:
            next_blocks = following[(BETA[i], j)][3]
            choices = []
            g = 3 * (1 << (6 - j))
            Qnext = g * H
            for k in range(4):
                matches = [
                    row for row in next_blocks
                    if row[0] == k and row[2] % 3 == S % 3
                ]
                assert len(matches) == 1
                _, mu, Rnext, Snext = matches[0]
                assert (Rnext - S) % g == 0
                delta = (Rnext - S) // g
                rho = (inv_a * delta) % H
                sigma_num = S + g * A * rho - Rnext
                assert sigma_num % Qnext == 0
                sigma = sigma_num // Qnext
                assert sigma >= 0
                choices.append((k, mu, rho, sigma, Rnext, Snext))
            assert len({row[2] for row in choices}) == 4
            state_rows[(j, nu)] = (R, S, choices)
        table[(gamma, i)] = state_rows
    return table


def audit():
    counters = {
        "finite_states": 0,
        "current_blocks": 0,
        "continuations": 0,
        "unique_ternary_matches": 0,
        "type_independent_modulus": 0,
        "distinct_rho_sets": 0,
        "nonnegative_sigma": 0,
        "exact_replays": 0,
    }
    rows = []

    for t in HEIGHTS:
        current = all_blocks(t)
        following = all_blocks(t + 16)
        table = transition_table(t, current, following)
        H = 1 << (11 * (t + 33))
        counters["finite_states"] += len(table)

        for (gamma, i), state_rows in table.items():
            G, D, A, _ = current[(gamma, i)]
            Qcurrent = 3 * (1 << (D + 6))
            counters["current_blocks"] += len(state_rows)
            for (j, nu), (R, S, choices) in state_rows.items():
                counters["distinct_rho_sets"] += 1
                Pcoeff = 3 * (1 << (6 - j)) * A
                Dnext = following[(BETA[i], j)][1]
                Qnext = 3 * (1 << (Dnext + 6))
                assert Qnext == 3 * (1 << (6 - j)) * H
                for k, mu, rho, sigma, Rnext, _ in choices:
                    counters["continuations"] += 1
                    counters["unique_ternary_matches"] += 1
                    counters["type_independent_modulus"] += 1
                    counters["nonnegative_sigma"] += 1
                    assert 0 <= rho < H
                    for ell in (0, 1, 2):
                        m = rho + H * ell
                        C = R + Qcurrent * m
                        Cnext = S + Pcoeff * m
                        mnext = sigma + A * ell
                        assert Cnext == Rnext + Qnext * mnext
                        assert (A * C + 1) == (1 << (D + j)) * Cnext
                        counters["exact_replays"] += 1
                    rows.append(
                        (t, gamma, i, j, nu, k, mu, rho, sigma, H, A)
                    )

    digest = hashlib.sha256()
    for row in sorted(rows, key=lambda item: item[:7]):
        encoded = "|".join(
            str(value) if index < 7 else hex(value)
            for index, value in enumerate(row)
        )
        digest.update(encoded.encode())
        digest.update(b"\n")

    assert 3**665 > 2**1054
    threshold = {
        "lower_log_certificate": "3^665 > 2^1054",
        "strict_refund_height": 3760,
        "strict_margin": 63 * 3760 - 236790,
        "doubling_refund_height": 3776,
        "doubling_margin": 63 * 3776 - 237455,
        "previous_multiple_strict_fails_exactly": not (
            3 ** (7 * 3744 + 5) > 2 * (1 << (11 * (3744 + 33)))
        ),
        "strict_threshold_holds_exactly": (
            3 ** (7 * 3760 + 5) > 2 * (1 << (11 * (3760 + 33)))
        ),
        "previous_multiple_doubling_fails_exactly": not (
            3 ** (7 * 3760 + 5) > 4 * (1 << (11 * (3760 + 33)))
        ),
        "doubling_threshold_holds_exactly": (
            3 ** (7 * 3776 + 5) > 4 * (1 << (11 * (3776 + 33)))
        ),
    }
    assert threshold["strict_margin"] == 90
    assert threshold["doubling_margin"] == 433
    assert all(value for key, value in threshold.items() if key.endswith("exactly"))

    return {
        "experiment": "X-8507",
        "heights": list(HEIGHTS),
        "counters": counters,
        "threshold": threshold,
        "transition_digest": digest.hexdigest(),
    }


def summary(payload):
    c = payload["counters"]
    t = payload["threshold"]
    return "\n".join(
        [
            "X-8507 top-boundary quotient audit",
            f"finite states:                    {c['finite_states']}",
            f"current eight-block states:       {c['current_blocks']}",
            f"four-way continuations:           {c['continuations']}",
            f"unique ternary matches:           {c['unique_ternary_matches']}",
            f"type-independent modulus checks:  {c['type_independent_modulus']}",
            f"distinct four-residue sets:       {c['distinct_rho_sets']}",
            f"nonnegative carries:              {c['nonnegative_sigma']}",
            f"exact quotient replays:           {c['exact_replays']}",
            f"strict refund height:             {t['strict_refund_height']}",
            f"doubling refund height:           {t['doubling_refund_height']}",
            f"transition digest:                {payload['transition_digest']}",
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
    if args.check_results:
        expected = args.check_results.read_text()
        if expected != text:
            raise SystemExit("canonical result mismatch")
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
    if args.summary:
        args.summary.write_text(summary(payload))


if __name__ == "__main__":
    main()
