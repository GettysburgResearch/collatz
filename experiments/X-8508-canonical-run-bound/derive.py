#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HEIGHTS = (
    3760,
    3776,
    4096,
    5504,
    10_000,
    50_000,
    100_000,
    500_000,
    1_140_416,
    2_000_000,
)


def obstruction(r: int, t: int) -> int:
    """665 times (run lower growth - canonical endpoint cap)."""
    return (
        r * (63 * t - 121_080)
        + 504 * r * (r - 1)
        - 665 * (22 * (t + 16 * r) + 559)
    )


def first_failure(t: int) -> tuple[int, int, int]:
    r = 1
    while obstruction(r, t) < 0:
        r += 1
    return r, obstruction(r, t), obstruction(r - 1, t)


def exact_crossing_for_r(r: int) -> tuple[int, int]:
    coefficient = 63 * r - 665 * 22
    constant = (
        -121_080 * r
        + 504 * r * (r - 1)
        - 665 * (22 * 16 * r + 559)
    )
    if coefficient <= 0:
        raise ValueError("no eventual crossing")
    first_integer = (-constant + coefficient - 1) // coefficient
    first_multiple_16 = ((first_integer + 15) // 16) * 16
    return first_integer, first_multiple_16


def audit():
    assert 3**665 > 2**1054

    table = []
    digest = hashlib.sha256()
    for t in HEIGHTS:
        r, positive, previous = first_failure(t)
        row = {
            "height": t,
            "first_forbidden_transition_count": r,
            "first_forbidden_canonical_count": r + 1,
            "obstruction": positive,
            "previous_obstruction": previous,
        }
        table.append(row)
        digest.update(
            f"{t}|{r}|{positive}|{previous}\n".encode()
        )

    first_233, first_233_multiple = exact_crossing_for_r(233)
    first_470, first_470_multiple = exact_crossing_for_r(470)

    assert first_470_multiple == 3760
    assert obstruction(470, 3760) == 124_585
    assert obstruction(469, 3760) == -229_887
    assert first_233_multiple == 1_140_416
    assert obstruction(233, 1_140_416) == 593
    assert obstruction(232, 1_140_416) == -71_724_311

    asymptotic = {
        "uniform_height": 3760,
        "uniform_first_forbidden_transition_count": 470,
        "uniform_first_forbidden_canonical_count": 471,
        "uniform_refund_density": "1/471",
        "eventual_height": 1_140_416,
        "eventual_first_forbidden_transition_count": 233,
        "eventual_first_forbidden_canonical_count": 234,
        "eventual_refund_density": "1/234",
        "r233_exact_integer_crossing": first_233,
        "r233_first_multiple_16": first_233_multiple,
        "r470_exact_integer_crossing": first_470,
        "r470_first_multiple_16": first_470_multiple,
    }

    return {
        "experiment": "X-8508",
        "lower_log_certificate": "3^665 > 2^1054",
        "canonical_cap_bits": "<22*t+559",
        "step_gain_bits": ">(63*t-121080)/665",
        "table": table,
        "asymptotic": asymptotic,
        "table_digest": digest.hexdigest(),
    }


def summary(payload):
    a = payload["asymptotic"]
    lines = [
        "X-8508 canonical-run bound audit",
        f"sample heights:                    {len(payload['table'])}",
        f"uniform height:                    {a['uniform_height']}",
        f"max consecutive canonical lifts:  {a['uniform_first_forbidden_canonical_count'] - 1}",
        f"uniform refunded density:          >= {a['uniform_refund_density']}",
        f"eventual height:                   {a['eventual_height']}",
        f"eventual max canonical lifts:      {a['eventual_first_forbidden_canonical_count'] - 1}",
        f"eventual refunded density:         >= {a['eventual_refund_density']}",
        f"table digest:                      {payload['table_digest']}",
        "",
    ]
    return "\n".join(lines)


def main():
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
