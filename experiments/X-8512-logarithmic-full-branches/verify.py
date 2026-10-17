#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import sys
from pathlib import Path

BETA = (2, 3, 2, 1)
P = (5, 30, 20, 56)
SOURCE = {
    (1, 0): 5, (1, 1): 2, (1, 2): 1, (1, 3): 0,
    (2, 0): 5, (2, 1): 1, (2, 2): 1, (2, 3): 0,
    (3, 0): 4, (3, 1): 1, (3, 2): 0, (3, 3): 0,
}


def valuation(value: int) -> int:
    if value == 0:
        return 10**9
    count = 0
    while value % 2 == 0:
        value //= 2
        count += 1
    return count


def inverse_log9(unit: int, bits: int) -> int:
    """Independent bit-by-bit inverse of alpha -> 9^alpha."""
    residue = 0
    for bit in range(bits):
        modulus = 1 << (bit + 4)
        candidates = (residue, residue + (1 << bit))
        matching = [
            candidate
            for candidate in candidates
            if pow(9, candidate, modulus) == unit % modulus
        ]
        assert len(matching) == 1
        residue = matching[0]
    assert pow(9, residue, 1 << (bits + 3)) == unit % (1 << (bits + 3))
    return residue


def reconstruct(payload: dict) -> None:
    section_bits = payload["section_bits"]
    expected_table = [
        [31, 29, 15, 5],
        [53, 31, 5, 7],
        [31, 29, 15, 5],
        [29, 23, 13, 7],
    ]
    assert payload["unit_table"] == expected_table
    assert payload["source_marker_table"] == {
        "1": [5, 2, 1, 0],
        "2": [5, 1, 1, 0],
        "3": [4, 1, 0, 0],
    }

    counters = {key: 0 for key in payload["counters"]}
    digest = hashlib.sha256()

    for t in payload["heights"]:
        for gamma in (1, 2, 3):
            for i in range(4):
                G = 7 * (t + 1) + gamma - BETA[i]
                delta = G % 2
                r = (G - delta) // 2
                D = 11 * (t + 17) - i
                marker_bits = max(3 - i, 0)
                if marker_bits:
                    assert (-r - SOURCE[(gamma, i)]) % (1 << marker_bits) == 0
                counters["finite_states"] += 1

                depths = []
                for j in range(4):
                    branch_modulus = 1 << (6 - j)
                    c = (
                        pow(3, -(BETA[i] + 1), branch_modulus)
                        * (P[j] >> j)
                    ) % branch_modulus
                    assert c == expected_table[i][j]
                    assert c % 2 == 1

                    v = D + j - 3
                    depths.append(v + 6 - j)
                    delta_next = (1 + BETA[i] - BETA[j]) % 2
                    next_marker = SOURCE[(BETA[i], j)]
                    next_marker_bits = 3 - j
                    alpha_bits = section_bits + next_marker_bits
                    output_bits = alpha_bits + 3
                    modulus_bits = v + 3 + output_bits
                    modulus = 1 << modulus_bits
                    values = []

                    for z in range(1 << section_bits):
                        u = c + branch_modulus * z
                        exponent = (1 << v) * u
                        numerator = pow(9, exponent, modulus) - 1
                        assert numerator % (1 << (v + 3)) == 0
                        divided = (numerator >> (v + 3)) % (1 << output_bits)
                        normalized = (
                            pow(3, delta_next, 1 << output_bits) * divided
                        ) % (1 << output_bits)
                        assert normalized % 8 == 1
                        alpha_next = inverse_log9(normalized, alpha_bits)
                        assert (
                            alpha_next - next_marker
                        ) % (1 << next_marker_bits) == 0
                        values.append(
                            ((alpha_next - next_marker) >> next_marker_bits)
                            % (1 << section_bits)
                        )

                    counters["branch_balls"] += 1
                    counters["source_marker_checks"] += 1
                    counters["fixed_unit_rows"] += 1
                    assert len(set(values)) == 1 << section_bits
                    counters["finite_section_permutations"] += 1

                    for left, right in itertools.combinations(
                        range(1 << section_bits), 2
                    ):
                        assert valuation(values[left] ^ values[right]) == valuation(left ^ right)
                        counters["isometry_pairs"] += 1

                    record = (
                        t, gamma, i, j, G, D, v, c,
                        delta_next, next_marker, *values,
                    )
                    digest.update("|".join(map(str, record)).encode())
                    digest.update(b"\n")

                assert depths == [D + 3] * 4

    assert counters == payload["counters"]
    assert digest.hexdigest() == payload["semantic_digest"]


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py results/canonical.json")
    payload = json.loads(Path(sys.argv[1]).read_text())
    reconstruct(payload)
    print("X-8512 independent logarithmic-branch checks passed")


if __name__ == "__main__":
    main()
