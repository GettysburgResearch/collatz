#!/usr/bin/env python3
"""X-9603: exact two-support pulse scan on the negative 3-cycle."""
from __future__ import annotations

import argparse
import hashlib
import json
from math import gcd
from pathlib import Path

R_MAX = 400
SLACK = 3


def setup(
    repeats: int, rotation: int
) -> tuple[list[int], int, list[int], int, int]:
    word = ([1, 2] if rotation == 0 else [2, 1]) * repeats
    state = -5 if rotation == 0 else -7
    odd_steps = 2 * repeats
    states = [state]
    prefix = 0
    weights: list[int] = []
    for position, valuation in enumerate(word):
        numerator = 3 * states[-1] + 1
        assert numerator % (1 << valuation) == 0
        states.append(numerator >> valuation)
        prefix += valuation
        weights.append(
            (-states[-1])
            * 3 ** (odd_steps - 1 - position)
            * (1 << prefix)
        )
    assert states[-1] == state

    minimum_pulse = 0
    while (1 << (prefix + minimum_pulse)) <= 3**odd_steps:
        minimum_pulse += 1
    return word, state, weights, prefix, minimum_pulse


def replay(
    base_word: list[int],
    second_position: int,
    first_pulse: int,
    second_pulse: int,
    start: int,
) -> bool:
    word = list(base_word)
    word[0] += first_pulse
    word[second_position] += second_pulse
    if start <= 0 or start % 2 == 0:
        return False
    value = start
    for valuation in word:
        numerator = 3 * value + 1
        if (numerator & -numerator).bit_length() - 1 != valuation:
            return False
        value = numerator >> valuation
    return value == start


def canonical_payload() -> dict[str, object]:
    hits: list[dict[str, object]] = []
    candidate_count = 0
    gcd_admissible_count = 0
    audit = hashlib.sha256()

    for repeats in range(1, R_MAX + 1):
        for rotation in (0, 1):
            word, state, weights, base_exponent, minimum_pulse = setup(
                repeats, rotation
            )
            odd_steps = 2 * repeats
            first_weight = weights[0]

            for extra in range(SLACK + 1):
                total_pulse = minimum_pulse + extra
                if total_pulse < 2:
                    continue
                denominator = (
                    (1 << (base_exponent + total_pulse)) - 3**odd_steps
                )
                two_to_total = 1 << total_pulse

                for second_position in range(1, odd_steps):
                    second_weight = weights[second_position]
                    coefficient = (first_weight - second_weight) % denominator
                    rhs = (
                        first_weight
                        - (second_weight % denominator)
                        * (two_to_total % denominator)
                    ) % denominator
                    common = gcd(coefficient, denominator)

                    if rhs % common:
                        candidate_count += total_pulse - 1
                        continue

                    gcd_admissible_count += 1
                    two_to_first = 2
                    for first_pulse in range(1, total_pulse):
                        candidate_count += 1
                        if (
                            two_to_first * coefficient - rhs
                        ) % denominator == 0:
                            second_pulse = total_pulse - first_pulse
                            correction = (
                                first_weight * ((1 << first_pulse) - 1)
                                + (1 << first_pulse)
                                * second_weight
                                * ((1 << second_pulse) - 1)
                            )
                            assert correction % denominator == 0
                            start = state + correction // denominator
                            exact = replay(
                                word,
                                second_position,
                                first_pulse,
                                second_pulse,
                                start,
                            )
                            hits.append(
                                {
                                    "repeats": repeats,
                                    "rotation": rotation,
                                    "second_position": second_position,
                                    "first_pulse": first_pulse,
                                    "second_pulse": second_pulse,
                                    "start": str(start),
                                    "exact_replay": exact,
                                    "trivial": start == 1,
                                }
                            )
                        two_to_first = (2 * two_to_first) % denominator

                    audit.update(repeats.to_bytes(4, "big"))
                    audit.update(bytes([rotation, extra]))
                    audit.update(second_position.to_bytes(4, "big"))
                    encoded = common.to_bytes(
                        max(1, (common.bit_length() + 7) // 8), "big"
                    )
                    audit.update(len(encoded).to_bytes(4, "big"))
                    audit.update(encoded)

    return {
        "experiment_id": "X-9603",
        "arithmetic": "exact Python integers",
        "family": (
            "negative 3-cycle repeated word with exactly two pulse supports"
        ),
        "r_max": R_MAX,
        "total_pulse_slack": SLACK,
        "candidate_count": candidate_count,
        "gcd_admissible_position_count": gcd_admissible_count,
        "hits": hits,
        "nontrivial_hit_count": sum(
            not bool(hit["trivial"]) and bool(hit["exact_replay"])
            for hit in hits
        ),
        "semantic_audit_sha256": audit.hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = canonical_payload()
    payload["results_sha256"] = hashlib.sha256(
        json.dumps(
            payload, sort_keys=True, separators=(",", ":")
        ).encode()
    ).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))

    if args.check_results:
        frozen = json.loads(args.check_results.read_text(encoding="utf-8"))
        if frozen != payload:
            raise SystemExit("frozen result mismatch")
        print("frozen result check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
