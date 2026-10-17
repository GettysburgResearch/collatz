#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

M = 2**19
N = 9**6
DELTA = N - M
ROWS = (
    ("AAAAAB", 360448, 365367),
    ("AAAABA", 471040, 477468),
    ("AAABAA", 267776, 271431),
    ("AABAAA", 366784, 371790),
    ("ABAAAA", 19416, 19683),
    ("BAAAAA", 349523, 354294),
)


def pair_data():
    inverse = pow(DELTA, -1, M)
    pairs = []
    matrix = []

    for i, (_word_i, domain_i, output_i) in enumerate(ROWS):
        row = []
        for j, (_word_j, domain_j, _output_j) in enumerate(ROWS):
            rho = ((domain_j - output_i) * inverse) % M
            sigma = (N * rho + output_i - domain_j) // M
            assert N * rho + output_i - domain_j == M * sigma
            assert sigma > rho

            for lift in (0, 1, 17):
                quotient = rho + M * lift
                successor = sigma + N * lift
                h = M * quotient + domain_i
                h_next = N * quotient + output_i
                assert h_next == M * successor + domain_j
                assert successor > quotient

            row.append(sigma - rho)
            pairs.append(
                {
                    "source": i,
                    "target": j,
                    "rho": rho,
                    "sigma": sigma,
                    "sigma_minus_rho": sigma - rho,
                }
            )
        matrix.append(row)

    return pairs, matrix


def quotient_minima(depth: int):
    # A type sequence i_0,...,i_L gives
    # q_L=(N^L q_0+C)/M^L. Solve the unique q_0 residue modulo M^L.
    states = [(0, index) for index in range(6)]
    modulus = 1
    power_n = 1
    records = []

    for transitions in range(1, depth + 1):
        next_states = []
        for correction, source in states:
            output = ROWS[source][2]
            for target in range(6):
                domain = ROWS[target][1]
                next_correction = (
                    N * correction + (output - domain) * modulus
                )
                next_states.append((next_correction, target))

        modulus *= M
        power_n *= N
        states = next_states
        inverse = pow(power_n, -1, modulus)
        minimum = min(
            (-correction * inverse) % modulus
            for correction, _target in states
        )
        records.append(
            {
                "transitions": transitions,
                "type_sequences": len(states),
                "minimum_initial_quotient": minimum,
                "minimum_bits": minimum.bit_length(),
            }
        )

    return records


def payload():
    pairs, matrix = pair_data()
    return {
        "schema_version": 1,
        "experiment_id": "X-8404",
        "status": "EMPIRICAL / EXACT FINITE INTERFACE AUDIT",
        "radix": M,
        "multiplier": N,
        "refund": DELTA,
        "branches": [
            {
                "index": index,
                "word": word,
                "domain_digit": domain,
                "output_digit": output,
            }
            for index, (word, domain, output) in enumerate(ROWS)
        ],
        "ordered_pair_count": len(pairs),
        "minimum_rho": min(row["rho"] for row in pairs),
        "maximum_rho": max(row["rho"] for row in pairs),
        "minimum_sigma": min(row["sigma"] for row in pairs),
        "maximum_sigma": max(row["sigma"] for row in pairs),
        "minimum_strict_growth": min(
            row["sigma_minus_rho"] for row in pairs
        ),
        "maximum_strict_growth": max(
            row["sigma_minus_rho"] for row in pairs
        ),
        "growth_matrix": matrix,
        "quotient_minima": quotient_minima(7),
        "interpretation": {
            "proved_by_finite_replay": [
                "all 36 exact ordered-pair quotient residues and successors",
                "strict quotient growth for every ordered pair and three lift values",
                "the complete least initial quotient through seven transitions",
            ],
            "not_proved": [
                "a forever-defined finite quotient state",
                "a divergent Collatz seed",
                "a positive cycle",
                "the Collatz conjecture or its negation",
            ],
        },
    }


def semantic_digest(obj):
    encoded = json.dumps(
        obj, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    obj = payload()
    obj["payload_sha256"] = semantic_digest(obj)
    print(json.dumps(obj, sort_keys=True, indent=2))

    if args.check_results:
        frozen = json.loads(args.check_results.read_text(encoding="utf-8"))
        assert frozen == obj
        print("frozen result check passed")


if __name__ == "__main__":
    main()
