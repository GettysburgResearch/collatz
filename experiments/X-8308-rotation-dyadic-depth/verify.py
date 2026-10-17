#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

RUN_DENOMINATOR = 267_629_447_755
RUN_NUMERATOR = 236_838_463_643
LIMIT = 10_000_000
DECIMALS = 160
UNIT = 10**DECIMALS

CHOSEN = {
    0, 1, 2, 3, 11, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24,
    27, 28, 29, 32, 35, 36, 38, 40, 41, 43, 44, 47, 49, 50, 52,
    53, 54, 55, 59, 60, 62, 64, 68, 69, 71, 73, 75, 79, 80, 83,
    89, 92, 93, 94, 96, 97, 100, 101, 102, 105, 108, 109, 120,
    121, 123, 125, 129, 130, 132, 134,
}

LOWER = (
    "1567441266440951895435533."
    "873676569542272619403132162187203755216515895680147289763106"
    "007747255031074577785707334413928560019257048980045859933549"
    "01452271111483139453432898211514707"
)
UPPER = (
    "1567441266440951895435533."
    "873676569542272619403132162187203755216515895680147289763106"
    "007747255031074577785707334413928560019257048980045859933549"
    "01452271111524885234982040317973759"
)


def bit(position: int) -> int:
    return (
        (position + 1) * RUN_NUMERATOR // RUN_DENOMINATOR
        - position * RUN_NUMERATOR // RUN_DENOMINATOR
    )


def repair_map() -> dict[int, int]:
    sites: list[tuple[int, int, int]] = []
    position = 0
    last = -2
    while len(sites) < 136:
        left, right = bit(position), bit(position + 1)
        if left != right and position > last + 1:
            sites.append((position, left, right))
            last = position
        position += 1
    answer: dict[int, int] = {}
    for index, (position, left, right) in enumerate(sites):
        if index in CHOSEN:
            answer[position] = right
            answer[position + 1] = left
    return answer


def scaled_fraction(text: str, upper: bool) -> tuple[int, int]:
    whole, digits = text.split(".")
    kept = (digits + "0" * DECIMALS)[:DECIMALS]
    value = int(kept)
    if upper and any(character != "0" for character in digits[DECIMALS:]):
        value += 1
    return int(whole), value


def next_interval(
    whole: int, lower: int, upper: int, symbol: int
) -> tuple[int, int, int]:
    divisor = 8 if symbol else 16
    additive = 3 if symbol else 0
    quotient, remainder = divmod(9 * whole + additive, divisor)
    raw_lower = (remainder * UNIT + 9 * lower) // divisor
    raw_upper = (remainder * UNIT + 9 * upper + divisor - 1) // divisor
    carry_a = raw_lower // UNIT
    carry_b = (raw_upper - 1) // UNIT
    assert carry_a == carry_b
    return (
        quotient + carry_a,
        raw_lower - carry_a * UNIT,
        raw_upper - carry_a * UNIT,
    )


def apply(value: int, symbol: int) -> int | None:
    if symbol == 0:
        return 9 * value // 16 if value % 16 == 0 else None
    return (9 * value + 3) // 8 if value % 8 == 5 else None


def census() -> tuple[dict[str, int], dict[str, dict[str, int | str]], int]:
    changed = repair_map()
    whole, low = scaled_fraction(LOWER, False)
    upper_whole, high = scaled_fraction(UPPER, True)
    assert upper_whole == whole

    starts = {"floor": 0, "ceil": 0}
    best_depth = {"floor": 0, "ceil": 0}
    best: dict[str, dict[str, int | str]] = {}
    active: list[list[int | str]] = []
    global_symbol = 0

    for run in range(LIMIT):
        run_value = changed.get(run, bit(run))
        for offset, symbol in enumerate((0,) + (1,) * (4 + run_value)):
            for label, start in (("floor", whole), ("ceil", whole + 1)):
                if apply(start, symbol) is not None:
                    starts[label] += 1
                    active.append([label, global_symbol, run, offset, start, start, 0, 0, ""])

            kept: list[list[int | str]] = []
            for item in active:
                result = apply(int(item[5]), symbol)
                if result is None:
                    continue
                item[5] = result
                item[6] = int(item[6]) + 1
                item[7] = int(item[7]) + 4 - symbol
                item[8] = str(item[8]) + str(symbol)
                kept.append(item)
                label = str(item[0])
                if int(item[6]) > best_depth[label]:
                    best_depth[label] = int(item[6])
                    best[label] = {
                        "kind": label,
                        "start_symbol": int(item[1]),
                        "start_run": int(item[2]),
                        "start_offset": int(item[3]),
                        "start_x": int(item[4]),
                        "current_x": int(item[5]),
                        "chart_blocks": int(item[6]),
                        "dyadic_depth": int(item[7]),
                        "word": str(item[8]),
                    }
            active = kept
            whole, low, high = next_interval(whole, low, high, symbol)
            global_symbol += 1

    return starts, best, global_symbol


def replay(word: str, start: int) -> list[int]:
    states = [start]
    value = start
    for character in word:
        value = apply(value, int(character))
        assert value is not None
        states.append(value)
    return states


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/canonical.json")
    frozen = json.loads(path.read_text(encoding="utf-8"))
    starts, best, rotations = census()

    assert rotations == frozen["scope"]["chart_rotations"] == 58_849_491
    assert starts == frozen["legal_start_counts"]

    for label in ("floor", "ceil"):
        expected = frozen["maximum_physical_prefix"][label]
        for key in (
            "kind", "start_symbol", "start_run", "start_offset", "start_x",
            "current_x", "chart_blocks", "dyadic_depth", "word",
        ):
            assert best[label][key] == expected[key], (label, key)
        states = replay(str(expected["word"]), int(expected["start_x"]))
        assert states == expected["physical_x_states"]
        assert 2 * int(expected["start_x"]) + 1 == expected["physical_odd_seed"]
        assert apply(states[-1], int(expected["failing_symbol"])) is None

    assert frozen["maximum_physical_prefix"]["floor"]["dyadic_depth"] == 26
    assert frozen["maximum_physical_prefix"]["ceil"]["dyadic_depth"] == 25
    assert frozen["height_interpretation"]["floor_mixed_coarse_bits_B_plus_60J"] == 86
    assert frozen["height_interpretation"]["ceil_mixed_coarse_bits_B_plus_60J"] == 85

    print("X-8308 independent ten-million-rotation census passed")


if __name__ == "__main__":
    main()
