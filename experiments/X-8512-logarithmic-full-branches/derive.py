#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

BETA = (2, 3, 2, 1)
P = (5, 30, 20, 56)
HEIGHTS = (16, 32)
SECTION_BITS = 7
SOURCE_MARKERS = {
    (1, 0): 5, (1, 1): 2, (1, 2): 1, (1, 3): 0,
    (2, 0): 5, (2, 1): 1, (2, 2): 1, (2, 3): 0,
    (3, 0): 4, (3, 1): 1, (3, 2): 0, (3, 3): 0,
}


def v2(value: int) -> int:
    if value == 0:
        return 10**9
    return (value & -value).bit_length() - 1


def log9_mod(unit: int, bits: int) -> int:
    """Return alpha mod 2^bits from 9^alpha == unit mod 2^(bits+3)."""
    alpha = 0
    for n in range(bits):
        modulus = 1 << (n + 4)
        if pow(9, alpha, modulus) != unit % modulus:
            alpha += 1 << n
        assert pow(9, alpha, modulus) == unit % modulus
    return alpha


def fixed_unit(i: int, j: int) -> int:
    modulus = 1 << (6 - j)
    return (
        pow(3, -(BETA[i] + 1), modulus)
        * (P[j] >> j)
    ) % modulus


def branch_values(t: int, gamma: int, i: int, j: int) -> dict:
    G = 7 * (t + 1) + gamma - BETA[i]
    D = 11 * (t + 17) - i
    delta = G & 1
    r = (G - delta) // 2
    valuation = D + j - 3
    c = fixed_unit(i, j)
    delta_next = (1 + BETA[i] - BETA[j]) & 1
    marker_bits = 3 - j
    alpha_bits = SECTION_BITS + marker_bits
    output_bits = alpha_bits + 3

    modulus = 1 << (valuation + 3 + output_bits)
    base = pow(9, 1 << valuation, modulus)
    next_marker = SOURCE_MARKERS[(BETA[i], j)]
    values = []

    for z in range(1 << SECTION_BITS):
        unit = c + (1 << (6 - j)) * z
        divided = (
            (pow(base, unit, modulus) - 1) >> (valuation + 3)
        ) % (1 << output_bits)
        normalized = (
            pow(3, delta_next, 1 << output_bits) * divided
        ) % (1 << output_bits)
        assert normalized % 8 == 1
        alpha_next = log9_mod(normalized, alpha_bits)
        assert (alpha_next - next_marker) % (1 << marker_bits) == 0
        z_next = (
            (alpha_next - next_marker) >> marker_bits
        ) % (1 << SECTION_BITS)
        values.append(z_next)

    return {
        "G": G,
        "D": D,
        "delta": delta,
        "r": r,
        "valuation": valuation,
        "unit": c,
        "delta_next": delta_next,
        "next_marker": next_marker,
        "values": values,
    }


def audit() -> dict:
    unit_table = [
        [fixed_unit(i, j) for j in range(4)]
        for i in range(4)
    ]
    assert unit_table == [
        [31, 29, 15, 5],
        [53, 31, 5, 7],
        [31, 29, 15, 5],
        [29, 23, 13, 7],
    ]

    counters = {
        "finite_states": 0,
        "branch_balls": 0,
        "source_marker_checks": 0,
        "fixed_unit_rows": 0,
        "finite_section_permutations": 0,
        "isometry_pairs": 0,
    }
    digest = hashlib.sha256()

    for t in HEIGHTS:
        for gamma in (1, 2, 3):
            for i in range(4):
                G = 7 * (t + 1) + gamma - BETA[i]
                delta = G & 1
                r = (G - delta) // 2
                marker_bits = max(3 - i, 0)
                if marker_bits:
                    assert (
                        -r - SOURCE_MARKERS[(gamma, i)]
                    ) % (1 << marker_bits) == 0
                counters["finite_states"] += 1

                common_depths = []
                for j in range(4):
                    row = branch_values(t, gamma, i, j)
                    assert row["valuation"] + 6 - j == row["D"] + 3
                    common_depths.append(row["D"] + 3)
                    assert row["unit"] & 1

                    counters["branch_balls"] += 1
                    counters["source_marker_checks"] += 1
                    counters["fixed_unit_rows"] += 1

                    values = row["values"]
                    assert len(set(values)) == 1 << SECTION_BITS
                    counters["finite_section_permutations"] += 1

                    for left, right in itertools.combinations(
                        range(1 << SECTION_BITS), 2
                    ):
                        assert v2(values[left] ^ values[right]) == v2(left ^ right)
                        counters["isometry_pairs"] += 1

                    record = (
                        t, gamma, i, j,
                        row["G"], row["D"], row["valuation"],
                        row["unit"], row["delta_next"], row["next_marker"],
                        *values,
                    )
                    digest.update("|".join(map(str, record)).encode())
                    digest.update(b"\n")

                assert len(set(common_depths)) == 1

    return {
        "experiment": "X-8512",
        "heights": list(HEIGHTS),
        "section_bits": SECTION_BITS,
        "unit_table": unit_table,
        "source_marker_table": {
            str(gamma): [SOURCE_MARKERS[(gamma, i)] for i in range(4)]
            for gamma in (1, 2, 3)
        },
        "counters": counters,
        "semantic_digest": digest.hexdigest(),
    }


def summary(payload: dict) -> str:
    c = payload["counters"]
    return "\n".join([
        "X-8512 logarithmic full-branch isometry audit",
        f"finite states:                    {c['finite_states']}",
        f"branch balls:                     {c['branch_balls']}",
        f"source marker checks:             {c['source_marker_checks']}",
        f"fixed unit rows:                  {c['fixed_unit_rows']}",
        f"finite section permutations:      {c['finite_section_permutations']}",
        f"isometry pairs:                   {c['isometry_pairs']}",
        f"semantic digest:                  {payload['semantic_digest']}",
        "",
    ])


def main() -> None:
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
