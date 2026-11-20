#!/usr/bin/env python3
"""Exact finite replays for DIRECTED_DEPTH_TWO.md; no Collatz conjecture oracle."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def step(n: int) -> int:
    require(type(n) is int and n > 0, "positive integer input required")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def odd_step(n: int) -> tuple[int, int]:
    require(type(n) is int and n > 0 and n % 2 == 1, "positive odd input required")
    y = 3 * n + 1
    a = (y & -y).bit_length() - 1
    return y >> a, a


def witness(m: int) -> dict[str, int]:
    require(type(m) is int and m >= 1, "positive integer m required")
    b = 64 ** m
    require((b - 1) % 9 == 0, "index integrality")
    return {
        "m": m,
        "source": (16 * b - 7) // 9,
        "one_sided_target": (32 * b - 23) // 9,
        "known_orbit_maximum": (8 * b - 2) // 3,
        "separated_target_clock": 6 * m + 4,
        "odd_target_clock": 6 * m + 2,
    }


def verify(row: dict[str, int]) -> dict[str, int]:
    require(set(row) == set(witness(1)), "witness field set")
    require(all(type(v) is int for v in row.values()), "integer witness fields")
    m = row["m"]
    expected = witness(m)
    require(row == expected, "witness differs from exact construction")
    b, n, z = 64 ** m, row["source"], row["one_sided_target"]
    h, deadline = row["known_orbit_maximum"], row["separated_target_clock"]
    require(n % 16 == 1 and z == 2 * n - 1, "one-sided source class")
    u, a = odd_step(n)
    one, a2 = odd_step(u)
    require((a, a2, one) == (2, 6 * m + 2, 1), "two-odd-event certificate")
    require(n > 1 and u > 1, "first hitting depth")

    known = []
    value = n
    for clock in range(deadline + 1):
        known.append(value)
        if clock < deadline:
            require(value != 1, "earlier known hitting time")
        else:
            require(value == 1, "known exact hitting time")
        value = step(value)
    known.extend([1, 2])
    require(max(known) == h, "known complete orbit maximum")
    known_set = set(known)

    value = z
    for _ in range(4):
        value = step(value)
    require(value == 2 ** (6 * m + 1) - 1, "Mersenne reduction")

    value = 3 * n
    target_count = 0
    expected_initial = [(16 * b - 7) // 3, 8 * b - 3, 12 * b - 4, 6 * b - 2]
    for clock in range(deadline + 1):
        if clock < 4:
            require(value == expected_initial[clock], "initial target formula")
        else:
            ell = clock - 4
            require(value == 3 ** (ell + 1) * 2 ** (6 * m - ell) - 1, "target prefix formula")
        require(value >= 3 * b - 1 > h, "complete-known-orbit separation")
        require(value not in known_set, "independently clocked separation")
        target_count += 1
        value = step(value)

    value = 3 * n
    odd_count = 0
    for clock in range(6 * m + 3):
        require(value > 1, "early odd target hit")
        if clock == 1:
            require(value == 8 * b - 3, "first odd target")
        elif 2 <= clock < 6 * m + 2:
            ell = clock - 2
            require(value == 3 ** (ell + 1) * 2 ** (6 * m - ell) - 1, "odd target prefix")
        elif clock == 6 * m + 2:
            require(value == (3 ** (6 * m + 1) - 1) // 2, "last odd target")
        new, division = odd_step(value)
        if clock == 0:
            require(division == 1, "first tripled division")
        elif clock == 1:
            require(division == 3, "second tripled division")
        elif 2 <= clock < 6 * m + 1:
            require(division == 1, "valuation-one target run")
        elif clock == 6 * m + 1:
            require(division == 2, "target exit division")
        odd_count += 1
        value = new
    return {"known_states": len(known), "target_states": target_count, "odd_target_states": odd_count,
            "source_bits": n.bit_length(), "m": m}


def run() -> dict[str, object]:
    parameters = list(range(1, 97)) + [127, 255, 1024]
    counts = [verify(witness(m)) for m in parameters]
    classified = []
    classified_inputs = 0
    for n in range(1, 1_000_000, 16):
        classified_inputs += 1
        u, a = odd_step(n)
        last, b = odd_step(u)
        if n > 1 and u > 1 and last == 1:
            require(a == 2 and b % 6 == 2 and b >= 8, "classification exponent")
            m = (b - 2) // 6
            require(witness(m)["source"] == n, "classification converse")
            classified.append({"n": n, "m": m})

    mutations = 0
    for key in ["source", "one_sided_target", "known_orbit_maximum", "separated_target_clock", "odd_target_clock"]:
        row = witness(2)
        row[key] += 1
        try:
            verify(row)
        except ValueError:
            mutations += 1
        else:
            raise ValueError("accepted altered witness: " + key)
    for invalid in [0, -1, True, 1.0]:
        try:
            witness(invalid)
        except ValueError:
            mutations += 1
        else:
            raise ValueError("accepted invalid parameter")
    return {
        "status": "PASS",
        "claim_status": "finite exact replay; universal statements require the written proofs",
        "source_pr": 146,
        "source_head": "6863d298187af8b2619efbf78cc4b0aa8e627393",
        "parameter_count": len(parameters),
        "parameters": parameters,
        "largest_source_bits": max(r["source_bits"] for r in counts),
        "known_states": sum(r["known_states"] for r in counts),
        "target_states": sum(r["target_states"] for r in counts),
        "odd_target_states": sum(r["odd_target_states"] for r in counts),
        "classified_inputs": classified_inputs,
        "classification_examples": classified,
        "rejected_mutations_and_domains": mutations,
        "boundary": "No claim that every residual Mersenne target converges; no full Collatz proof.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
