#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

RUN_LENGTH = 267_629_447_755
RUN_WEIGHT = 236_838_463_643
RUN_LIMIT = 10_000_000
SCALE_DIGITS = 160
SCALE = 10**SCALE_DIGITS

SELECTED_INDICES = (
    0, 1, 2, 3, 11, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24,
    27, 28, 29, 32, 35, 36, 38, 40, 41, 43, 44, 47, 49, 50, 52,
    53, 54, 55, 59, 60, 62, 64, 68, 69, 71, 73, 75, 79, 80, 83,
    89, 92, 93, 94, 96, 97, 100, 101, 102, 105, 108, 109, 120,
    121, 123, 125, 129, 130, 132, 134,
)

INITIAL_LOWER = (
    "1567441266440951895435533."
    "873676569542272619403132162187203755216515895680147289763106"
    "007747255031074577785707334413928560019257048980045859933549"
    "01452271111483139453432898211514707"
)
INITIAL_UPPER = (
    "1567441266440951895435533."
    "873676569542272619403132162187203755216515895680147289763106"
    "007747255031074577785707334413928560019257048980045859933549"
    "01452271111524885234982040317973759"
)

EXPECTED_FLOOR = {
    "kind": "floor",
    "chart_blocks": 8,
    "dyadic_depth": 26,
    "start_symbol": 28_016_158,
    "start_run": 4_760_645,
    "start_offset": 5,
    "start_x": 1_263_100_502_238_270_197_353_429,
    "legal_word": "10111110",
    "failing_symbol": 1,
    "terminal_x": 810_210_927_051_465_104_640_843,
    "failing_residue_mod_8": 3,
}

EXPECTED_CEIL = {
    "kind": "ceil",
    "chart_blocks": 8,
    "dyadic_depth": 25,
    "start_symbol": 38_814_386,
    "start_run": 6_595_534,
    "start_offset": 4,
    "start_x": 1_185_457_427_807_540_176_328_893,
    "legal_word": "11011111",
    "failing_symbol": 0,
    "terminal_x": 1_520_814_155_107_999_553_284_668,
    "failing_residue_mod_16": 12,
}


def prefix_ones(index: int) -> int:
    return index * RUN_WEIGHT // RUN_LENGTH


def run_bit(index: int) -> int:
    return prefix_ones(index + 1) - prefix_ones(index)


def repair_sites(count: int = 136) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    previous = -2
    position = 0
    while len(result) < count:
        left = run_bit(position)
        right = run_bit(position + 1)
        if left != right and position > previous + 1:
            result.append((position, left, right))
            previous = position
        position += 1
    return result


def changed_run_bits() -> dict[int, int]:
    changed: dict[int, int] = {}
    sites = repair_sites()
    for index in SELECTED_INDICES:
        position, left, right = sites[index]
        changed[position] = right
        changed[position + 1] = left
    return changed


def parse_scaled(value: str, upper: bool) -> tuple[int, int]:
    integer_text, fraction_text = value.split(".")
    retained = (fraction_text + "0" * SCALE_DIGITS)[:SCALE_DIGITS]
    scaled = int(retained)
    if upper and any(character != "0" for character in fraction_text[SCALE_DIGITS:]):
        scaled += 1
    return int(integer_text), scaled


def formal_step(
    integer: int, lower: int, upper: int, symbol: int
) -> tuple[int, int, int]:
    denominator = 8 if symbol else 16
    translation = 3 if symbol else 0
    base, remainder = divmod(9 * integer + translation, denominator)
    next_lower = (remainder * SCALE + 9 * lower) // denominator
    next_upper = (remainder * SCALE + 9 * upper + denominator - 1) // denominator
    lower_carry = next_lower // SCALE
    upper_carry = (next_upper - 1) // SCALE
    if lower_carry != upper_carry:
        raise AssertionError("formal interval crosses an integer")
    return (
        base + lower_carry,
        next_lower - lower_carry * SCALE,
        next_upper - lower_carry * SCALE,
    )


def physical_step(value: int, symbol: int) -> int | None:
    if symbol:
        if value % 8 != 5:
            return None
        return (9 * value + 3) // 8
    if value % 16:
        return None
    return 9 * value // 16


def direct_replay(start: int, word: str) -> list[int]:
    states = [start]
    current = start
    for character in word:
        symbol = int(character)
        current = physical_step(current, symbol)
        if current is None:
            raise AssertionError("frozen legal word does not replay")
        states.append(current)
    return states


def scan() -> dict[str, object]:
    changed = changed_run_bits()
    integer, lower = parse_scaled(INITIAL_LOWER, upper=False)
    upper_integer, upper = parse_scaled(INITIAL_UPPER, upper=True)
    if upper_integer != integer:
        raise AssertionError("initial interval crosses an integer")

    active: list[dict[str, int | str]] = []
    maximum = {"floor": 0, "ceil": 0}
    records: dict[str, dict[str, int | str]] = {}
    legal_starts = {"floor": 0, "ceil": 0}
    symbol_index = 0

    for run_index in range(RUN_LIMIT):
        bit = changed.get(run_index, run_bit(run_index))
        macro = (0,) + (1,) * (4 + bit)
        for offset, symbol in enumerate(macro):
            for kind, candidate in (("floor", integer), ("ceil", integer + 1)):
                if physical_step(candidate, symbol) is not None:
                    legal_starts[kind] += 1
                    active.append(
                        {
                            "kind": kind,
                            "start_symbol": symbol_index,
                            "start_run": run_index,
                            "start_offset": offset,
                            "start_x": candidate,
                            "current_x": candidate,
                            "chart_blocks": 0,
                            "dyadic_depth": 0,
                            "word": "",
                        }
                    )

            surviving: list[dict[str, int | str]] = []
            for candidate in active:
                next_value = physical_step(int(candidate["current_x"]), symbol)
                if next_value is None:
                    continue
                candidate["current_x"] = next_value
                candidate["chart_blocks"] = int(candidate["chart_blocks"]) + 1
                candidate["dyadic_depth"] = int(candidate["dyadic_depth"]) + 4 - symbol
                candidate["word"] = str(candidate["word"]) + str(symbol)
                surviving.append(candidate)
                kind = str(candidate["kind"])
                depth = int(candidate["chart_blocks"])
                if depth > maximum[kind]:
                    maximum[kind] = depth
                    records[kind] = dict(candidate)
            active = surviving

            integer, lower, upper = formal_step(integer, lower, upper, symbol)
            symbol_index += 1

    for kind, expected in (("floor", EXPECTED_FLOOR), ("ceil", EXPECTED_CEIL)):
        record = records[kind]
        if record["chart_blocks"] != expected["chart_blocks"]:
            raise AssertionError((kind, record))
        if record["dyadic_depth"] != expected["dyadic_depth"]:
            raise AssertionError((kind, record))
        for key in ("start_symbol", "start_run", "start_offset", "start_x", "word"):
            expected_key = "legal_word" if key == "word" else key
            if record[key] != expected[expected_key]:
                raise AssertionError((kind, key, record[key], expected[expected_key]))

        legal_word = str(record["word"])
        states = direct_replay(int(record["start_x"]), legal_word)
        if states[-1] != expected["terminal_x"]:
            raise AssertionError((kind, states[-1]))
        failing_symbol = int(expected["failing_symbol"])
        if physical_step(states[-1], failing_symbol) is not None:
            raise AssertionError("frozen failure unexpectedly legal")
        record["physical_x_states"] = states
        record["physical_odd_seed"] = 2 * int(record["start_x"]) + 1
        record["failing_symbol"] = failing_symbol
        if failing_symbol:
            record["failing_residue_mod_8"] = states[-1] % 8
        else:
            record["failing_residue_mod_16"] = states[-1] % 16

    return {
        "schema_version": 1,
        "experiment_id": "X-8308",
        "scope": {
            "run_rotations": RUN_LIMIT,
            "chart_rotations": symbol_index,
            "fixed_decimal_scale_digits": SCALE_DIGITS,
            "repair_site_count": len(SELECTED_INDICES),
        },
        "legal_start_counts": legal_starts,
        "maximum_physical_prefix": records,
        "height_interpretation": {
            "known_base_odd_factor_level_J": 1,
            "floor_mixed_coarse_bits_B_plus_60J": int(records["floor"]["dyadic_depth"]) + 60,
            "ceil_mixed_coarse_bits_B_plus_60J": int(records["ceil"]["dyadic_depth"]) + 60,
            "required_bits_A_minus_82": 4_992_586_554_927,
            "conclusion": "the scanned rotations remain far below the mixed-place height gate",
        },
        "interpretation": {
            "proved": [
                "unique outward-enclosed real floor at every scanned chart rotation",
                "complete floor and ceiling physical-prefix census through ten million run rotations",
                "exact replay and first failing residue for both depth-eight records",
            ],
            "not_proved": [
                "a bound beyond the declared rotation range",
                "a full physical cycle",
                "a divergent Collatz seed",
                "the Collatz conjecture or its negation",
            ],
        },
    }


def canonical_bytes(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, sort_keys=True, indent=2) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    data = canonical_bytes(scan())
    if args.write_results:
        args.write_results.parent.mkdir(parents=True, exist_ok=True)
        args.write_results.write_bytes(data)
    if args.check_results and args.check_results.read_bytes() != data:
        raise SystemExit("canonical result mismatch")
    print(data.decode("utf-8"), end="")
    print("SHA256", hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
