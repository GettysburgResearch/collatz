#!/usr/bin/env python3
"""X-9601: exact one-pulse perturbations of the negative 3- and 11-cycles."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

EXPERIMENT_ID = "X-9601"
R_MAX = 20_000
SLACK = 3
FAMILIES = {
    "negative_3_cycle": {
        "base_power_two": 8,
        "base_power_three": 9,
        "odd_steps_per_block": 2,
        "states": (-5, -7),
    },
    "negative_11_cycle": {
        "base_power_two": 2048,
        "base_power_three": 2187,
        "odd_steps_per_block": 7,
        "states": (-17, -25, -37, -55, -41, -61, -91),
    },
}


def replay_formula(
    family: dict[str, object],
    state_index: int,
    repeats: int,
    delta: int,
    start: int,
) -> bool:
    """Reconstruct the rotated word and replay every exact accelerated valuation."""
    if family["odd_steps_per_block"] == 2:
        base_words = ((1, 2), (2, 1))
        word = list(base_words[state_index]) * repeats
    else:
        base = (1, 1, 1, 2, 1, 1, 4)
        word = list(base[state_index:] + base[:state_index]) * repeats
    word[0] += delta

    if start <= 0 or start % 2 == 0:
        return False
    value = start
    for valuation in word:
        numerator = 3 * value + 1
        if numerator % (1 << valuation):
            return False
        if (numerator & -numerator).bit_length() - 1 != valuation:
            return False
        value = numerator >> valuation
    return value == start


def scan_family(name: str, family: dict[str, object]) -> dict[str, object]:
    p = 1
    q = 1
    pulse_power = 1
    delta_min = 0
    hits: list[dict[str, object]] = []
    small_denominator_cases: list[dict[str, object]] = []
    candidate_count = 0
    audit = hashlib.sha256()

    states = tuple(int(x) for x in family["states"])
    coefficients = tuple(-(3 * state + 1) for state in states)
    p_base = int(family["base_power_two"])
    q_base = int(family["base_power_three"])
    odd_steps_per_block = int(family["odd_steps_per_block"])

    for repeats in range(1, R_MAX + 1):
        p *= p_base
        q *= q_base
        while pulse_power * p <= q:
            pulse_power <<= 1
            delta_min += 1

        for slack in range(SLACK + 1):
            pulse = pulse_power << slack
            delta = delta_min + slack
            denominator = pulse * p - q
            pulse_minus_one = pulse - 1
            if denominator <= 0:
                raise AssertionError("pulse did not cross the multiplier threshold")

            for state_index, (state, coefficient) in enumerate(
                zip(states, coefficients)
            ):
                candidate_count += 1
                rhs = coefficient * pulse_minus_one
                if denominator <= rhs:
                    small_denominator_cases.append(
                        {
                            "state": state,
                            "repeats": repeats,
                            "delta": delta,
                            "slack": slack,
                            "denominator": str(denominator),
                            "reduced_rhs": str(rhs),
                        }
                    )
                remainder = rhs % denominator
                if remainder == 0:
                    ratio = rhs // denominator
                    start = state + ratio * 3 ** (
                        odd_steps_per_block * repeats - 1
                    )
                    exact = replay_formula(
                        family, state_index, repeats, delta, start
                    )
                    hits.append(
                        {
                            "state": state,
                            "state_index": state_index,
                            "repeats": repeats,
                            "odd_steps": odd_steps_per_block * repeats,
                            "delta": delta,
                            "slack": slack,
                            "start": str(start),
                            "exact_replay": exact,
                            "trivial": start == 1,
                        }
                    )

                audit.update(repeats.to_bytes(4, "big"))
                audit.update(delta.to_bytes(4, "big"))
                audit.update(state_index.to_bytes(2, "big"))
                encoded = remainder.to_bytes(
                    max(1, (remainder.bit_length() + 7) // 8), "big"
                )
                audit.update(len(encoded).to_bytes(4, "big"))
                audit.update(encoded)

    return {
        "name": name,
        "r_max": R_MAX,
        "slack": SLACK,
        "states": list(states),
        "coefficients": list(coefficients),
        "candidate_count": candidate_count,
        "small_denominator_case_count": len(small_denominator_cases),
        "small_denominator_cases": small_denominator_cases,
        "hit_count": len(hits),
        "nontrivial_hit_count": sum(not bool(hit["trivial"]) for hit in hits),
        "hits": hits,
        "audit_sha256": audit.hexdigest(),
    }


def canonical_payload() -> dict[str, object]:
    families = [scan_family(name, family) for name, family in FAMILIES.items()]
    return {
        "experiment_id": EXPERIMENT_ID,
        "arithmetic": "exact Python integers",
        "r_max": R_MAX,
        "slack": SLACK,
        "families": families,
        "totals": {
            "candidate_count": sum(
                int(item["candidate_count"]) for item in families
            ),
            "nontrivial_hit_count": sum(
                int(item["nontrivial_hit_count"]) for item in families
            ),
        },
    }


def payload_digest(payload: dict[str, object]) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = canonical_payload()
    result = dict(payload)
    result["results_sha256"] = payload_digest(payload)
    print(json.dumps(result, sort_keys=True, indent=2))

    if args.check_results:
        frozen = json.loads(args.check_results.read_text(encoding="utf-8"))
        if frozen != result:
            raise SystemExit("frozen result mismatch")
        print("frozen result check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
