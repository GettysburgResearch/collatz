#!/usr/bin/env python3
"""Independent verifier for the X-8703 height-renewal certificate.

This module deliberately does not import build.py.  It reconstructs every word,
residue, affine endpoint, count, digest, and representative certificate from
the recurrence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


SCHEMA = "X-8703-centered-height-renewal-v1"
EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()


class VerificationError(RuntimeError):
    """Raised on the first certificate mismatch."""


def check(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def packed(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def sha(value: Any) -> str:
    return hashlib.sha256(packed(value)).hexdigest()


def ceiling(numerator: int, denominator: int) -> int:
    check(denominator > 0, "nonpositive interval denominator")
    quotient, remainder = divmod(numerator, denominator)
    return quotient + bool(remainder)


def control_word(number: int, length: int) -> tuple[int, ...]:
    return tuple(int(character) for character in f"{number:0{length}b}")


def fraction_relation(left: tuple[str, int, int], right: tuple[str, int, int]) -> int:
    cross = left[1] * right[2] - right[1] * left[2]
    if cross < 0:
        return -1
    if cross > 0:
        return 1
    return 0


def tied_extreme(
    candidates: tuple[tuple[str, int, int], ...], want_maximum: bool
) -> tuple[tuple[str, int, int], ...]:
    check(len(candidates) > 0, "missing endpoint candidates")
    extreme = candidates[0]
    tied = [extreme]
    for candidate in candidates[1:]:
        relation = fraction_relation(candidate, extreme)
        better = relation > 0 if want_maximum else relation < 0
        if better:
            extreme = candidate
            tied = [candidate]
        elif relation == 0:
            tied.append(candidate)
    return tuple(tied)


def independently_derive_record(
    height: int,
    t: int,
    number: int,
    pow64: list[int],
    pow81: list[int],
    inverse_powers: list[int],
) -> dict[str, Any]:
    """Use the closed modular sum and direct recurrence replay."""
    word = control_word(number, t + 1)
    differences = [word[i] - word[i + 1] for i in range(t)]

    D = [0]
    for j in range(1, t + 1):
        # This is the defining sum, updated only after the earlier value has
        # independently been established.
        D.append(81 * D[-1] + pow64[j - 1] * differences[j - 1])

    modulus = pow64[t]
    modular_sum = sum(
        differences[i] * pow64[i] * inverse_powers[i + 1] for i in range(t)
    )
    r = (-modular_sum) % modulus
    check(
        (pow81[t] * r + D[t]) % modulus == 0,
        f"terminal residue failed at t={t}, word={number}",
    )

    # Replaying from r gives c_j.  Replaying from r+64^t gives an independent
    # check of every affine slope.
    replay_zero = [r]
    replay_one = [r + modulus]
    for j in range(t):
        numerator_zero = 81 * replay_zero[-1] + differences[j]
        numerator_one = 81 * replay_one[-1] + differences[j]
        check(
            numerator_zero % 64 == 0 and numerator_one % 64 == 0,
            f"direct replay is nonintegral at t={t}, word={number}, j={j}",
        )
        replay_zero.append(numerator_zero // 64)
        replay_one.append(numerator_one // 64)

    c_values = []
    slopes = []
    for j in range(t + 1):
        formula_numerator = pow81[j] * r + D[j]
        check(
            formula_numerator % pow64[j] == 0,
            f"closed c_j is nonintegral at t={t}, word={number}, j={j}",
        )
        formula_c = formula_numerator // pow64[j]
        formula_slope = pow81[j] * pow64[t - j]
        check(replay_zero[j] == formula_c, "closed and replayed c_j disagree")
        check(
            replay_one[j] - replay_zero[j] == formula_slope,
            "closed and replayed affine slopes disagree",
        )
        c_values.append(formula_c)
        slopes.append(formula_slope)

    lower = (
        ("band_lower", height - 64 * r, 64 * modulus),
        ("crossing_lower", height - c_values[t], pow81[t]),
    )
    upper = tuple(
        (f"pre_crossing_{j}", height - c_values[j], slopes[j]) for j in range(t)
    ) + (("crossing_upper", 64 * height - c_values[t], pow81[t]),)
    active_lower = tied_extreme(lower, True)
    active_upper = tied_extreme(upper, False)
    start = ceiling(active_lower[0][1], active_lower[0][2])
    stop = ceiling(active_upper[0][1], active_upper[0][2])

    return {
        "t": t,
        "word": "".join(str(bit) for bit in word),
        "differences": differences,
        "D": D,
        "r": r,
        "c": c_values,
        "slopes": slopes,
        "bounds": {
            "lower": [list(candidate) for candidate in lower],
            "upper": [list(candidate) for candidate in upper],
            "active_lower": [list(candidate) for candidate in active_lower],
            "active_upper": [list(candidate) for candidate in active_upper],
        },
        "integer_Q": {
            "start_inclusive": start,
            "stop_exclusive": stop,
            "count": max(0, stop - start),
        },
    }


def projection(record: dict[str, Any]) -> list[Any]:
    t = record["t"]
    return [
        t,
        record["word"],
        record["D"][t],
        record["r"],
        record["c"][t],
        record["bounds"]["active_lower"],
        record["bounds"]["active_upper"],
        record["integer_Q"]["start_inclusive"],
        record["integer_Q"]["stop_exclusive"],
    ]


def values_at(record: dict[str, Any], q: int) -> list[int]:
    return [
        constant + coefficient * q
        for constant, coefficient in zip(record["c"], record["slopes"])
    ]


def violations(height: int, values: list[int], t: int) -> list[str]:
    answer: list[str] = []
    if 64 * values[0] < height:
        answer.append("band_lower")
    for j in range(t):
        if not values[j] < height:
            answer.append(f"pre_crossing_{j}")
    if not values[t] >= height:
        answer.append("crossing_lower")
    if not values[t] < 64 * height:
        answer.append("crossing_upper")
    return answer


def crossing_time(height: int, values: list[int]) -> int | None:
    return next((j for j, value in enumerate(values) if value >= height), None)


def independently_certify_boundary(
    height: int, record: dict[str, Any]
) -> dict[str, Any]:
    start = record["integer_Q"]["start_inclusive"]
    stop = record["integer_Q"]["stop_exclusive"]
    check(start < stop, "representative interval is empty")
    probes = [
        ("below_start", start - 1, False),
        ("at_start", start, True),
        ("before_stop", stop - 1, True),
        ("at_stop", stop, False),
    ]
    output = []
    for position, q, expected in probes:
        values = values_at(record, q)
        failed = violations(height, values, record["t"])
        inside = len(failed) == 0
        check(inside == expected, f"boundary classification failed at {position}")
        if inside:
            check(
                crossing_time(height, values) == record["t"],
                "interior endpoint does not have the declared first crossing",
            )
        output.append(
            {
                "position": position,
                "Q": q,
                "inside": inside,
                "failed_inequalities": failed,
                "B": values,
                "first_crossing": crossing_time(height, values),
            }
        )
    return {"chart": record, "boundary_replay": output}


def plain_counter(counter: Counter[str]) -> dict[str, int]:
    return {key: counter[key] for key in sorted(counter)}


def independent_enumeration(
    height: int, max_steps: int
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    check(height >= 1, "height must be positive")
    check(1 <= max_steps <= 18, "max_steps outside 1..18")
    pow64 = [64**j for j in range(max_steps + 1)]
    pow81 = [81**j for j in range(max_steps + 1)]
    whole = hashlib.sha256()
    kept_whole = hashlib.sha256()
    depths = []
    representatives = []
    grand_words = grand_kept = grand_seeds = 0

    for t in range(1, max_steps + 1):
        inverse = pow(81, -1, pow64[t])
        inverse_powers = [1]
        for _ in range(t):
            inverse_powers.append(
                (inverse_powers[-1] * inverse) % pow64[t]
            )
        at_depth = hashlib.sha256()
        kept_at_depth = hashlib.sha256()
        kept = seed_count = 0
        least_width: int | None = None
        greatest_width = 0
        first = last = widest = None
        lower_counts: Counter[str] = Counter()
        upper_counts: Counter[str] = Counter()
        chart_signs: Counter[str] = Counter()
        seed_signs: Counter[str] = Counter()
        words = 1 << (t + 1)

        for number in range(words):
            record = independently_derive_record(
                height, t, number, pow64, pow81, inverse_powers
            )
            row = packed(projection(record)) + b"\n"
            whole.update(row)
            at_depth.update(row)
            width = record["integer_Q"]["count"]
            if width <= 0:
                continue
            kept += 1
            seed_count += width
            kept_whole.update(row)
            kept_at_depth.update(row)
            sign = record["word"][0]
            chart_signs[sign] += 1
            seed_signs[sign] += width
            lower_counts[
                "+".join(bound[0] for bound in record["bounds"]["active_lower"])
            ] += 1
            upper_counts[
                "+".join(bound[0] for bound in record["bounds"]["active_upper"])
            ] += 1
            if first is None:
                first = record
            last = record
            if widest is None or width > greatest_width:
                widest = record
            least_width = width if least_width is None else min(least_width, width)
            greatest_width = max(greatest_width, width)

        check(words == 2 ** (t + 1), "word enumeration is incomplete")
        grand_words += words
        grand_kept += kept
        grand_seeds += seed_count
        depths.append(
            {
                "t": t,
                "words": words,
                "retained_charts": kept,
                "represented_seed_states": seed_count,
                "interval_width_min": least_width,
                "interval_width_max": greatest_width if kept else None,
                "active_lower_counts": plain_counter(lower_counts),
                "active_upper_counts": plain_counter(upper_counts),
                "retained_charts_by_e0": plain_counter(chart_signs),
                "represented_seed_states_by_e0": plain_counter(seed_signs),
                "all_chart_digest": at_depth.hexdigest(),
                "retained_chart_digest": kept_at_depth.hexdigest(),
            }
        )
        if kept:
            check(
                first is not None and last is not None and widest is not None,
                "missing independently selected representative",
            )
            representatives.append(
                {
                    "t": t,
                    "first_lexicographic": independently_certify_boundary(
                        height, first
                    ),
                    "last_lexicographic": independently_certify_boundary(
                        height, last
                    ),
                    "widest_first_tie": independently_certify_boundary(
                        height, widest
                    ),
                }
            )

    check(
        grand_words == 2 ** (max_steps + 2) - 4,
        "closed total-word count failed",
    )
    return (
        {
            "total_words": grand_words,
            "retained_charts": grand_kept,
            "represented_seed_states": grand_seeds,
            "all_chart_digest": whole.hexdigest(),
            "retained_chart_digest": kept_whole.hexdigest(),
            "depths": depths,
        },
        representatives,
    )


def bound_constants() -> dict[str, Any]:
    difference = 81**18 - 64**19
    threshold_numerator = 64 * 81**17
    check(difference > 0, "multiplicative growth does not clear the height band")
    threshold = ceiling(threshold_numerator, difference)
    margin = 11 * difference - threshold_numerator
    check(threshold == 11, "the exact large-height threshold is not 11")
    check(margin > 0, "the H=11 threshold margin is not positive")

    # Expanding D_j by the binary controls makes every coefficient except that
    # of e_0 nonpositive.  Their sum is exactly -81^(j-1).
    for j in range(1, 19):
        negative_sum = -sum(
            17 * 81 ** (j - 1 - i) * 64 ** (i - 1)
            for i in range(1, j)
        ) - 64 ** (j - 1)
        check(
            negative_sum == -(81 ** (j - 1)),
            f"control-error minimum identity failed at j={j}",
        )

    # The three positive branch differences are 17Q, 17Q+4, 17Q+13;
    # on the first branch positivity forces Q>=1.
    check(min(17, 4, 13) == 4, "positive branch increment bound failed")
    return {
        "steps": 18,
        "control_error_lower": -(81**17),
        "branchwise_positive_step_minimum": 4,
        "large_height_threshold": threshold,
        "ratio_test": {
            "81_power_18": 81**18,
            "64_power_19": 64**19,
            "difference": difference,
            "threshold_numerator": threshold_numerator,
            "threshold_margin_at_11": margin,
        },
        "conclusion": (
            "A positive legal path starting in H/64 <= B_0 < H either fails "
            "before renewal or crosses B >= H by step 18."
        ),
    }


def exact_power_of_64(height: int) -> int | None:
    exponent = 0
    remaining = height
    while remaining > 1 and remaining % 64 == 0:
        remaining //= 64
        exponent += 1
    return exponent if remaining == 1 else None


def recorded_command(height: int, max_steps: int) -> str:
    exponent = exact_power_of_64(height)
    argument = (
        f"--height-power {exponent}"
        if exponent is not None
        else f"--height {height}"
    )
    return (
        "python3 -B experiments/X-8703-centered-height-renewal/build.py "
        f"{argument} --max-steps {max_steps} "
        "--output experiments/X-8703-centered-height-renewal/results/canonical.json"
    )


def reconstruct_semantic(height: int, max_steps: int) -> dict[str, Any]:
    enumeration, representatives = independent_enumeration(height, max_steps)
    exponent = exact_power_of_64(height)
    return {
        "schema": SCHEMA,
        "experiment_id": "X-8703",
        "agent": "gpt56-sol-02",
        "issue": 40,
        "classification": {
            "enumeration": "EMPIRICAL exact finite computation",
            "identities": "elementary identities proved in L-8702",
            "universal_bound": "elementary lemma proposed in L-8702",
            "counterexample": "none claimed",
        },
        "parameters": {
            "height": height,
            "height_expression": (
                f"64^{exponent}" if exponent is not None else str(height)
            ),
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
        "elementary_18_step_bound": bound_constants(),
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
            "empty_retained_digest": EMPTY_SHA256,
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


def verify_certificate_data(certificate: dict[str, Any]) -> dict[str, Any]:
    check(
        set(certificate)
        == {"semantic", "semantic_digest", "provenance", "artifact_digest"},
        "unexpected top-level certificate fields",
    )
    semantic = certificate["semantic"]
    check(isinstance(semantic, dict), "semantic payload is not an object")
    check(sha(semantic) == certificate["semantic_digest"], "semantic digest mismatch")
    artifact_input = {
        "semantic": semantic,
        "semantic_digest": certificate["semantic_digest"],
        "provenance": certificate["provenance"],
    }
    check(
        sha(artifact_input) == certificate["artifact_digest"],
        "artifact digest mismatch",
    )
    check(semantic.get("schema") == SCHEMA, "wrong schema")
    parameters = semantic.get("parameters", {})
    height = parameters.get("height")
    max_steps = parameters.get("max_steps")
    check(type(height) is int and height >= 1, "invalid height parameter")
    check(
        type(max_steps) is int and 1 <= max_steps <= 18,
        "invalid max_steps parameter",
    )

    provenance = certificate["provenance"]
    check(isinstance(provenance, dict), "provenance is not an object")
    check(
        provenance.get("command") == recorded_command(height, max_steps),
        "recorded command does not match parameters",
    )
    check(provenance.get("random_seed") is None, "unexpected random seed")
    environment = provenance.get("environment")
    check(
        isinstance(environment, dict)
        and set(environment) == {"python", "implementation", "platform", "machine"}
        and all(isinstance(value, str) and value for value in environment.values()),
        "malformed environment record",
    )

    expected = reconstruct_semantic(height, max_steps)
    check(semantic == expected, "independent semantic reconstruction mismatch")
    return {
        "height": height,
        "max_steps": max_steps,
        "total_words": expected["enumeration"]["total_words"],
        "retained_charts": expected["enumeration"]["retained_charts"],
        "represented_seed_states": expected["enumeration"][
            "represented_seed_states"
        ],
        "semantic_digest": certificate["semantic_digest"],
        "artifact_digest": certificate["artifact_digest"],
    }


def verify_path(path: Path) -> dict[str, Any]:
    try:
        certificate = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise VerificationError(f"cannot read certificate: {error}") from error
    return verify_certificate_data(certificate)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    arguments = parser.parse_args()
    try:
        summary = verify_path(arguments.certificate)
    except VerificationError as error:
        print(f"verification failed: {error}")
        return 1
    print("all independent X-8703 certificate checks passed")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
