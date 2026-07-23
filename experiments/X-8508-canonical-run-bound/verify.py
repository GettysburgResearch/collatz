#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def raw_left(r: int, t: int) -> int:
    return r * (63 * t - 121_080) + 504 * r * (r - 1)


def raw_right(r: int, t: int) -> int:
    return 665 * (22 * (t + 16 * r) + 559)


def first_bad(t: int) -> tuple[int, int, int]:
    # Independent bounded scan. The author implementation uses a separate
    # obstruction helper and crossing formula.
    for r in range(1, 2000):
        difference = raw_left(r, t) - raw_right(r, t)
        if difference >= 0:
            previous = raw_left(r - 1, t) - raw_right(r - 1, t)
            return r, difference, previous
    raise AssertionError("scan bound too small")


def first_multiple_for_r(r: int) -> int:
    t = 0
    while raw_left(r, t) - raw_right(r, t) < 0:
        t += 16
    return t


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical", type=Path)
    args = parser.parse_args()

    data = json.loads(args.canonical.read_text())
    assert data["experiment"] == "X-8508"
    assert pow(3, 665) > pow(2, 1054)

    checked = 0
    for expected in data["table"]:
        result = first_bad(expected["height"])
        assert result[0] == expected["first_forbidden_transition_count"]
        assert result[0] + 1 == expected["first_forbidden_canonical_count"]
        assert result[1] == expected["obstruction"]
        assert result[2] == expected["previous_obstruction"]
        assert result[1] >= 0 and result[2] < 0
        checked += 1

    a = data["asymptotic"]
    assert first_multiple_for_r(470) == a["uniform_height"]
    assert first_multiple_for_r(233) == a["eventual_height"]
    assert first_bad(a["uniform_height"])[0] == 470
    assert first_bad(a["eventual_height"])[0] == 233

    # Minimal asymptotic transition count under the stated coarse bounds:
    # the coefficient of t is positive first when 63*r > 665*22.
    assert 63 * 232 <= 665 * 22
    assert 63 * 233 > 665 * 22

    print("independent canonical-run verification passed")
    print(f"table rows: {checked}")
    print("uniform: no 471 consecutive canonical lifts from t=3760")
    print("eventual: no 234 consecutive canonical lifts from t=1140416")


if __name__ == "__main__":
    main()
