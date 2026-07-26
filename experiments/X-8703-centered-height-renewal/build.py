#!/usr/bin/env python3
"""Build the exact centered height-renewal atlas certificate.

The full atlas has 2^20 - 4 word charts at the canonical parameters.  This
builder streams deterministic digests and stores only aggregate statistics and
selected boundary certificates; it never retains the full atlas in memory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


EXPERIMENT_ID = "X-8703"
AGENT = "gpt56-sol-02"
ISSUE = 40
SCHEMA = "X-8703-centered-height-renewal-v1"
DEFAULT_HEIGHT_POWER = 18
DEFAULT_MAX_STEPS = 18


class AtlasError(RuntimeError):
    """Raised when an exact arithmetic invariant fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AtlasError(message)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def object_digest(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def ceil_div(numerator: int, denominator: int) -> int:
    """Return ceil(numerator / denominator), including for negative inputs."""
    require(denominator > 0, "ceil_div requires a positive denominator")
    return -((-numerator) // denominator)


def bits_of(index: int, length: int) -> tuple[int, ...]:
    return tuple((index >> (length - 1 - position)) & 1 for position in range(length))


def compare_fractions(left: tuple[str, int, int], right: tuple[str, int, int]) -> int:
    """Compare labelled fractions (label, numerator, positive denominator)."""
    difference = left[1] * right[2] - right[1] * left[2]
    return (difference > 0) - (difference < 0)


def extreme_candidates(
    candidates: Iterable[tuple[str, int, int]], maximum: bool
) -> tuple[tuple[str, int, int], ...]:
    candidates = tuple(candidates)
    require(bool(candidates), "an interval endpoint needs at least one candidate")
    best = candidates[0]
    ties = [best]
    for candidate in candidates[1:]:
        comparison = compare_fractions(candidate, best)
        improves = comparison > 0 if maximum else comparison < 0
        if improves:
            best = candidate
            ties = [candidate]
        elif comparison == 0:
            ties.append(candidate)
    return tuple(ties)


def derive_word_record(
    height: int,
    depth: int,
    word_index: int,
    powers_64: list[int] | None = None,
    powers_81: list[int] | None = None,
    inverse_81_depth: int | None = None,
) -> dict[str, Any]:
    """Derive one exact affine chart and its half-open integer Q interval."""
    require(height >= 1, "height must be positive")
    require(depth >= 1, "depth must be positive")
    require(0 <= word_index < (1 << (depth + 1)), "word index out of range")

    if powers_64 is None:
        powers_64 = [64**j for j in range(depth + 1)]
    if powers_81 is None:
        powers_81 = [81**j for j in range(depth + 1)]
    modulus = powers_64[depth]
    if inverse_81_depth is None:
        inverse_81_depth = pow(powers_81[depth], -1, modulus)

    bits = bits_of(word_index, depth + 1)
    differences: list[int] = []
    D_values = [0]
    D = 0
    for j in range(depth):
        difference = bits[j] - bits[j + 1]
        differences.append(difference)
        D = 81 * D + powers_64[j] * difference
        D_values.append(D)

    r = (-inverse_81_depth * D_values[depth]) % modulus
    c_values: list[int] = []
    slopes: list[int] = []
    for j in range(depth + 1):
        numerator = powers_81[j] * r + D_values[j]
        require(
            numerator % powers_64[j] == 0,
            f"nonintegral c_{j} at depth {depth}, word {word_index}",
        )
        c_values.append(numerator // powers_64[j])
        slopes.append(powers_81[j] * powers_64[depth - j])

    lower_candidates = (
        ("band_lower", height - 64 * r, 64 * modulus),
        ("crossing_lower", height - c_values[depth], powers_81[depth]),
    )
    upper_candidates = tuple(
        (
            f"pre_crossing_{j}",
            height - c_values[j],
            slopes[j],
        )
        for j in range(depth)
    ) + (
        (
            "crossing_upper",
            64 * height - c_values[depth],
            powers_81[depth],
        ),
    )
    active_lower = extreme_candidates(lower_candidates, maximum=True)
    active_upper = extreme_candidates(upper_candidates, maximum=False)
    q_start = ceil_div(active_lower[0][1], active_lower[0][2])
    q_stop = ceil_div(active_upper[0][1], active_upper[0][2])

    return {
        "t": depth,
        "word": f"{word_index:0{depth + 1}b}",
        "differences": differences,
        "D": D_values,
        "r": r,
        "c": c_values,
        "slopes": slopes,
        "bounds": {
            "lower": [list(candidate) for candidate in lower_candidates],
            "upper": [list(candidate) for candidate in upper_candidates],
            "active_lower": [list(candidate) for candidate in active_lower],
            "active_upper": [list(candidate) for candidate in active_upper],
        },
        "integer_Q": {
            "start_inclusive": q_start,
            "stop_exclusive": q_stop,
            "count": max(0, q_stop - q_start),
        },
    }


def digest_projection(record: dict[str, Any]) -> list[Any]:
    """Compact, documented projection committed by the streaming atlas digest."""
    depth = record["t"]
    return [
        depth,
        record["word"],
        record["D"][depth],
        record["r"],
        record["c"][depth],
        record["bounds"]["active_lower"],
        record["bounds"]["active_upper"],
        record["integer_Q"]["start_inclusive"],
        record["integer_Q"]["stop_exclusive"],
    ]


def replay_values(record: dict[str, Any], q_value: int) -> list[int]:
    return [
        c_j + slope_j * q_value
        for c_j, slope_j in zip(record["c"], record["slopes"])
    ]


def failed_inequalities(
    height: int, values: list[int], depth: int
) -> list[str]:
    failures: list[str] = []
    if 64 * values[0] < height:
        failures.append("band_lower")
    for j in range(depth):
        if values[j] >= height:
            failures.append(f"pre_crossing_{j}")
    if values[depth] < height:
        failures.append("crossing_lower")
    if values[depth] >= 64 * height:
        failures.append("crossing_upper")
    return failures


def first_crossing(height: int, values: list[int]) -> int | None:
    for j, value in enumerate(values):
        if value >= height:
            return j
    return None


def boundary_certificate(height: int, record: dict[str, Any]) -> dict[str, Any]:
    interval = record["integer_Q"]
    start = interval["start_inclusive"]
    stop = interval["stop_exclusive"]
    require(start < stop, "cannot certify an empty interval")

    probes = (
        ("below_start", start - 1, False),
        ("at_start", start, True),
        ("before_stop", stop - 1, True),
        ("at_stop", stop, False),
    )
    replay = []
    for label, q_value, expected_inside in probes:
        values = replay_values(record, q_value)
        failures = failed_inequalities(height, values, record["t"])
        inside = not failures
        require(
            inside == expected_inside,
            f"bad boundary probe {label} for t={record['t']} word={record['word']}",
        )
        if inside:
            require(
                first_crossing(height, values) == record["t"],
                "an interior probe has the wrong first crossing",
            )
        replay.append(
            {
                "position": label,
                "Q": q_value,
                "inside": inside,
                "failed_inequalities": failures,
                "B": values,
                "first_crossing": first_crossing(height, values),
            }
        )
    return {"chart": record, "boundary_replay": replay}


def elementary_bound_data() -> dict[str, Any]:
    """Constants used by the elementary, non-computational 18-step proof."""
    denominator = 81**18 - 64**19
    numerator = 64 * 81**17
    require(denominator > 0, "81^18 must exceed 64^19")
    threshold = ceil_div(numerator, denominator)
    require(threshold == 11, "unexpected large-height threshold")
    require(
        11 * denominator - numerator
        == 1_551_116_294_402_118_154_433_498_457_982_123,
        "unexpected exact threshold margin",
    )
    return {
        "steps": 18,
        "control_error_lower": -(81**17),
        "branchwise_positive_step_minimum": 4,
        "large_height_threshold": threshold,
        "ratio_test": {
            "81_power_18": 81**18,
            "64_power_19": 64**19,
            "difference": denominator,
            "threshold_numerator": numerator,
            "threshold_margin_at_11": 11 * denominator - numerator,
        },
        "conclusion": (
            "A positive legal path starting in H/64 <= B_0 < H either fails "
            "before renewal or crosses B >= H by step 18."
        ),
    }


def _counter_dict(counter: Counter[str]) -> dict[str, int]:
    return {key: counter[key] for key in sorted(counter)}


def enumerate_atlas(height: int, max_steps: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Stream the whole atlas and return aggregates plus selected certificates."""
    require(height >= 1, "height must be positive")
    require(1 <= max_steps <= 18, "max_steps must lie in 1..18")

    powers_64 = [64**j for j in range(max_steps + 1)]
    powers_81 = [81**j for j in range(max_steps + 1)]
    all_hasher = hashlib.sha256()
    retained_hasher = hashlib.sha256()
    depth_rows: list[dict[str, Any]] = []
    representative_rows: list[dict[str, Any]] = []
    total_words = 0
    total_retained = 0
    total_seed_states = 0

    for depth in range(1, max_steps + 1):
        modulus = powers_64[depth]
        inverse = pow(powers_81[depth], -1, modulus)
        depth_hasher = hashlib.sha256()
        depth_retained_hasher = hashlib.sha256()
        retained = 0
        seed_states = 0
        width_min: int | None = None
        width_max = 0
        first_record: dict[str, Any] | None = None
        last_record: dict[str, Any] | None = None
        widest_record: dict[str, Any] | None = None
        active_lower: Counter[str] = Counter()
        active_upper: Counter[str] = Counter()
        charts_by_initial_digit: Counter[str] = Counter()
        seeds_by_initial_digit: Counter[str] = Counter()

        word_count = 1 << (depth + 1)
        for word_index in range(word_count):
            record = derive_word_record(
                height,
                depth,
                word_index,
                powers_64,
                powers_81,
                inverse,
            )
            encoded = canonical_bytes(digest_projection(record)) + b"\n"
            all_hasher.update(encoded)
            depth_hasher.update(encoded)

            width = record["integer_Q"]["count"]
            if width == 0:
                continue
            retained += 1
            seed_states += width
            retained_hasher.update(encoded)
            depth_retained_hasher.update(encoded)
            initial_digit = record["word"][0]
            charts_by_initial_digit[initial_digit] += 1
            seeds_by_initial_digit[initial_digit] += width
            lower_key = "+".join(
                item[0] for item in record["bounds"]["active_lower"]
            )
            upper_key = "+".join(
                item[0] for item in record["bounds"]["active_upper"]
            )
            active_lower[lower_key] += 1
            active_upper[upper_key] += 1
            if first_record is None:
                first_record = record
            last_record = record
            if widest_record is None or width > width_max:
                widest_record = record
            width_min = width if width_min is None else min(width_min, width)
            width_max = max(width_max, width)

        total_words += word_count
        total_retained += retained
        total_seed_states += seed_states
        depth_rows.append(
            {
                "t": depth,
                "words": word_count,
                "retained_charts": retained,
                "represented_seed_states": seed_states,
                "interval_width_min": width_min,
                "interval_width_max": width_max if retained else None,
                "active_lower_counts": _counter_dict(active_lower),
                "active_upper_counts": _counter_dict(active_upper),
                "retained_charts_by_e0": _counter_dict(charts_by_initial_digit),
                "represented_seed_states_by_e0": _counter_dict(
                    seeds_by_initial_digit
                ),
                "all_chart_digest": depth_hasher.hexdigest(),
                "retained_chart_digest": depth_retained_hasher.hexdigest(),
            }
        )
        if retained:
            require(
                first_record is not None
                and last_record is not None
                and widest_record is not None,
                "missing representative",
            )
            representative_rows.append(
                {
                    "t": depth,
                    "first_lexicographic": boundary_certificate(height, first_record),
                    "last_lexicographic": boundary_certificate(height, last_record),
                    "widest_first_tie": boundary_certificate(height, widest_record),
                }
            )

    enumeration = {
        "total_words": total_words,
        "retained_charts": total_retained,
        "represented_seed_states": total_seed_states,
        "all_chart_digest": all_hasher.hexdigest(),
        "retained_chart_digest": retained_hasher.hexdigest(),
        "depths": depth_rows,
    }
    return enumeration, representative_rows


def height_power_if_exact(height: int) -> int | None:
    power = 0
    value = height
    while value > 1 and value % 64 == 0:
        value //= 64
        power += 1
    return power if value == 1 else None


def canonical_command(height: int, max_steps: int) -> str:
    power = height_power_if_exact(height)
    height_argument = (
        f"--height-power {power}" if power is not None else f"--height {height}"
    )
    return (
        "python3 -B experiments/X-8703-centered-height-renewal/build.py "
        f"{height_argument} --max-steps {max_steps} "
        "--output experiments/X-8703-centered-height-renewal/results/canonical.json"
    )


def semantic_certificate(height: int, max_steps: int) -> dict[str, Any]:
    enumeration, representatives = enumerate_atlas(height, max_steps)
    power = height_power_if_exact(height)
    return {
        "schema": SCHEMA,
        "experiment_id": EXPERIMENT_ID,
        "agent": AGENT,
        "issue": ISSUE,
        "classification": {
            "enumeration": "EMPIRICAL exact finite computation",
            "identities": "elementary identities proved in L-8702",
            "universal_bound": "elementary lemma proposed in L-8702",
            "counterexample": "none claimed",
        },
        "parameters": {
            "height": height,
            "height_expression": f"64^{power}" if power is not None else str(height),
            "max_steps": max_steps,
            "depth_range": [1, max_steps],
            "word_encoding": (
                "lexicographic binary e_0...e_t, e_0 most significant"
            ),
            "Q_interval": "[start_inclusive, stop_exclusive) over integers",
        },
        "recurrence": {
            "equation": "64*B_(n+1)=81*B_n+e_n-e_(n+1)",
            "D_j": (
                "sum_(i=0)^(j-1) 81^(j-1-i)*64^i*(e_i-e_(i+1))"
            ),
            "residue": "r=[-81^(-t)*D_t] mod 64^t in [0,64^t)",
            "affine_chart": (
                "B_j=c_j+81^j*64^(t-j)*Q; "
                "c_j=(81^j*r+D_j)/64^j"
            ),
            "first_crossing": (
                "H/64<=B_0<H; B_j<H for 0<=j<t; H<=B_t<64H"
            ),
        },
        "elementary_18_step_bound": elementary_bound_data(),
        "enumeration": enumeration,
        "representatives": representatives,
        "digest_protocol": {
            "hash": "sha256",
            "serialization": (
                "UTF-8/ASCII JSON, sorted keys, separators comma/colon, then LF"
            ),
            "order": "increasing t, then increasing binary word value",
            "projection": [
                "t",
                "word",
                "D_t",
                "r",
                "c_t",
                "all tied active lower bounds [label,numerator,denominator]",
                "all tied active upper bounds [label,numerator,denominator]",
                "Q start inclusive",
                "Q stop exclusive",
            ],
            "empty_retained_digest": hashlib.sha256(b"").hexdigest(),
        },
        "limitations": [
            (
                "The atlas partitions only positive ordinary states whose exact "
                "forced tail remains legal through a first height crossing."
            ),
            (
                "States that hit a forbidden low residue before crossing are "
                "not represented by a retained chart."
            ),
            (
                "The canonical counts concern only H=64^18 and t=1..18; the "
                "scripts accept other finite heights but make no infinite-path "
                "claim."
            ),
            (
                "No retained finite chart is an all-time ordinary survivor or "
                "a Collatz counterexample."
            ),
        ],
    }


def build_certificate(height: int, max_steps: int) -> dict[str, Any]:
    semantic = semantic_certificate(height, max_steps)
    semantic_digest = object_digest(semantic)
    provenance = {
        "command": canonical_command(height, max_steps),
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "machine": platform.machine(),
        },
        "random_seed": None,
    }
    without_artifact_digest = {
        "semantic": semantic,
        "semantic_digest": semantic_digest,
        "provenance": provenance,
    }
    return {
        **without_artifact_digest,
        "artifact_digest": object_digest(without_artifact_digest),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    height_group = parser.add_mutually_exclusive_group()
    height_group.add_argument("--height", type=int)
    height_group.add_argument("--height-power", type=int, default=DEFAULT_HEIGHT_POWER)
    parser.add_argument("--max-steps", type=int, default=DEFAULT_MAX_STEPS)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if (
        args.output is not None
        and args.check_results is not None
        and args.output.resolve() == args.check_results.resolve()
    ):
        print(
            "--output and --check-results must name different files",
            file=sys.stderr,
        )
        return 2
    if args.height is not None:
        height = args.height
    else:
        require(args.height_power is not None, "missing height")
        require(args.height_power >= 0, "height power must be nonnegative")
        height = 64**args.height_power

    certificate = build_certificate(height, args.max_steps)
    text = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    if args.check_results is not None:
        expected = json.loads(args.check_results.read_text(encoding="utf-8"))
        if certificate != expected:
            print("frozen result mismatch", file=sys.stderr)
            return 1

    summary = certificate["semantic"]["enumeration"]
    print(
        json.dumps(
            {
                "artifact_digest": certificate["artifact_digest"],
                "height": height,
                "max_steps": args.max_steps,
                "represented_seed_states": summary["represented_seed_states"],
                "retained_charts": summary["retained_charts"],
                "semantic_digest": certificate["semantic_digest"],
                "total_words": summary["total_words"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
