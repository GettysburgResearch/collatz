#!/usr/bin/env python3
"""X-8002: exact near-threshold three- and four-pulse cycle scans.

Every word is represented up to cyclic rotation by putting one pulse at index
zero.  All positive pulse compositions at the minimal total crossing D>0 and
the next three totals are scanned in the declared repetition ranges.  Every
divisibility hit is replayed valuation by valuation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable

EXPERIMENT_ID = "X-8002"
SLACK = 3
FAMILIES = {
    "negative_3_cycle": {
        "base_word": (1, 2),
        "states": (-5, -7),
        "three_pulse_r_max": 50,
        "four_pulse_r_max": 20,
    },
    "negative_11_cycle": {
        "base_word": (1, 1, 1, 2, 1, 1, 4),
        "states": (-17, -25, -37, -55, -41, -61, -91),
        "three_pulse_r_max": 20,
        "four_pulse_r_max": 8,
    },
}


def pulse_compositions(total: int, count: int) -> Iterable[tuple[int, ...]]:
    if count == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - count + 2):
        for tail in pulse_compositions(total - first, count - 1):
            yield (first,) + tail


def exact_replay(word: list[int], start: int) -> bool:
    if start <= 0 or start % 2 == 0:
        return False
    value = start
    for valuation in word:
        numerator = 3 * value + 1
        actual = (numerator & -numerator).bit_length() - 1
        if actual != valuation:
            return False
        value = numerator >> valuation
    return value == start


def encode_int(value: int) -> bytes:
    raw = value.to_bytes(max(1, (value.bit_length() + 7) // 8), "big")
    return len(raw).to_bytes(4, "big") + raw


def scan_count(
    name: str,
    base: tuple[int, ...],
    states: tuple[int, ...],
    pulse_count: int,
    r_max: int,
) -> dict[str, object]:
    k = len(base)
    base_total = sum(base)
    unpulsed_two = 1
    unpulsed_three = 1
    pulse_power = 1
    pulse_total_min = 0
    tested = 0
    hits: list[dict[str, object]] = []
    audit = hashlib.sha256()

    for repeats in range(1, r_max + 1):
        unpulsed_two <<= base_total
        unpulsed_three *= 3**k
        while pulse_power * unpulsed_two <= unpulsed_three:
            pulse_power <<= 1
            pulse_total_min += 1

        length = k * repeats
        for slack in range(SLACK + 1):
            total = pulse_total_min + slack
            if total < pulse_count:
                continue
            compositions = tuple(pulse_compositions(total, pulse_count))
            denominator = (pulse_power << slack) * unpulsed_two - unpulsed_three

            for rotation, negative_state in enumerate(states):
                base_word = (base[rotation:] + base[:rotation]) * repeats
                prefix = [0]
                terms: list[int] = []
                exponent = 0
                for index, valuation in enumerate(base_word):
                    term = 3 ** (length - 1 - index) * (1 << exponent)
                    terms.append(term)
                    prefix.append(prefix[-1] + term)
                    exponent += valuation
                if exponent != base_total * repeats:
                    raise AssertionError("base exponent mismatch")

                from itertools import combinations
                for later_positions in combinations(range(1, length), pulse_count - 1):
                    cuts = (0,) + later_positions + (length,)
                    segment_sums = [terms[0]]
                    for segment in range(1, pulse_count):
                        lo = cuts[segment - 1] + 1
                        hi = cuts[segment] + 1
                        segment_sums.append(prefix[hi] - prefix[lo])
                    lo = cuts[pulse_count - 1] + 1
                    segment_sums.append(prefix[length] - prefix[lo])

                    for pulses in compositions:
                        cumulative = 0
                        numerator = segment_sums[0]
                        for index, pulse in enumerate(pulses, start=1):
                            cumulative += pulse
                            numerator += (1 << cumulative) * segment_sums[index]
                        remainder = numerator % denominator
                        tested += 1
                        for value in (
                            repeats,
                            slack,
                            rotation,
                            *later_positions,
                            *pulses,
                        ):
                            audit.update(int(value).to_bytes(4, "big"))
                        audit.update(encode_int(remainder))

                        if remainder == 0:
                            start = numerator // denominator
                            word = list(base_word)
                            word[0] += pulses[0]
                            for position, pulse in zip(later_positions, pulses[1:]):
                                word[position] += pulse
                            hits.append(
                                {
                                    "repeats": repeats,
                                    "slack": slack,
                                    "rotation": rotation,
                                    "negative_state": negative_state,
                                    "positions": [0, *later_positions],
                                    "pulses": list(pulses),
                                    "start": str(start),
                                    "exact_replay": exact_replay(word, start),
                                    "trivial": start == 1,
                                }
                            )

    return {
        "name": name,
        "pulse_count": pulse_count,
        "r_max": r_max,
        "slack": SLACK,
        "scope": "minimal total pulse crossing D>0 and the next three totals",
        "tested_candidates": tested,
        "hit_count": len(hits),
        "nontrivial_hit_count": sum(not bool(hit["trivial"]) for hit in hits),
        "hits": hits,
        "audit_sha256": audit.hexdigest(),
    }


def canonical_payload() -> dict[str, object]:
    scans: list[dict[str, object]] = []
    for name, raw in FAMILIES.items():
        base = tuple(int(x) for x in raw["base_word"])
        states = tuple(int(x) for x in raw["states"])
        scans.append(scan_count(name, base, states, 3, int(raw["three_pulse_r_max"])))
        scans.append(scan_count(name, base, states, 4, int(raw["four_pulse_r_max"])))
    return {
        "experiment_id": EXPERIMENT_ID,
        "arithmetic": "exact Python integers",
        "scans": scans,
        "totals": {
            "tested_candidates": sum(int(scan["tested_candidates"]) for scan in scans),
            "nontrivial_hits": sum(int(scan["nontrivial_hit_count"]) for scan in scans),
        },
    }


def payload_digest(payload: dict[str, object]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()
    payload = canonical_payload()
    result = dict(payload)
    result["results_sha256"] = payload_digest(payload)
    text = json.dumps(result, sort_keys=True, indent=2) + "\n"
    print(text, end="")
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    if args.check_results:
        frozen = json.loads(args.check_results.read_text(encoding="utf-8"))
        if frozen != result:
            raise SystemExit("frozen result mismatch")
        print("frozen result check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
