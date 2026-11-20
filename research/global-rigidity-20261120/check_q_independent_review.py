#!/usr/bin/env python3
"""Independent finite Q-section audit, without importing the author's transducer.

The canonical state is recovered from the two actual affine slope powers,
with the old orientation used only to resolve an equal-slope tie.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def check(value: bool, label: str) -> None:
    if not value:
        raise RuntimeError(label)


def shortcut(n: int) -> int:
    return n // 2 if not n % 2 else (3 * n + 1) // 2


def odd_part(n: int) -> int:
    check(n > 0, "positive odd-part input")
    return n // (n & -n)


def canonical(x_form: tuple[int, int], y_form: tuple[int, int], denominator: int, old_swap: bool) -> tuple[int, int, bool]:
    ax, bx = x_form
    ay, by = y_form
    swap = ay < ax if ay != ax else old_swap
    base, other = (y_form, x_form) if swap else (x_form, y_form)
    check(other[0] % base[0] == 0, "integral affine slope ratio")
    ratio, exponent = other[0] // base[0], 0
    while ratio > 1 and ratio % 3 == 0:
        ratio //= 3
        exponent += 1
    check(ratio == 1, "affine slopes are powers of three apart")
    constant = other[1] - 3**exponent * base[1]
    check(constant % denominator == 0, "canonical defect integrality")
    return exponent, constant // denominator, swap


def trace(a: int, horizon: int) -> list[dict]:
    x, y = a, 3 * a - 1
    x_form, y_form = (1, 0), (3, -1)
    denominator, swap = 1, False
    result = []
    for h in range(horizon + 1):
        s, d, swap = canonical(x_form, y_form, denominator, swap)
        check(x * denominator == x_form[0] * a + x_form[1], "literal X agrees with affine form")
        check(y * denominator == y_form[0] * a + y_form[1], "literal Y agrees with affine form")
        base, other = (y, x) if swap else (x, y)
        check(other == 3**s * base + d, "recovered physical canonical state")
        result.append({"x": x, "y": y, "s": s, "d": d, "swap": swap, "base_form": y_form if swap else x_form, "bit": base % 2})
        if h < horizon:
            px, py = x % 2, y % 2
            x_form = (3**px * x_form[0], 3**px * x_form[1] + px * denominator)
            y_form = (3**py * y_form[0], 3**py * y_form[1] + py * denominator)
            x, y = shortcut(x), shortcut(y)
            denominator *= 2
    return result


def expected_signed(h: int) -> tuple[int, int, bool]:
    if h < 8:
        return (*((1, -1), (2, -1), (1, -2), (1, -4), (1, -7), (0, -4), (0, -6), (0, -9))[h], False)
    r, phase = divmod(h - 8, 3)
    return r + 1, (5, 7, 10)[phase] * 3 ** (r + 1) - 1, True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    signed = trace(-2, 150)
    for h, state in enumerate(signed):
        check((state["s"], state["d"], state["swap"]) == expected_signed(h), "signed state law")
    code = "".join(str(state["bit"]) for state in signed[:-1])
    check(code == ("0" + "1" * 7 + "110" * 48)[:150], "signed parity code")

    family_cases = family_edges = strengthened_cases = 0
    for h_limit in range(3, 97):
        for t in (1, 2, 3, 4, 5, 6, 7, 11, 32, 257):
            n = (1 << h_limit) * t
            a, floor = n - 2, 2 * n - 5
            actual = trace(a, h_limit)
            xs, ys = [], []
            for h, state in enumerate(actual):
                x_expected = n - 2 if not h else 3 ** (h - 1) * (1 << (h_limit - h)) * t - 1
                y_expected = 3 ** (1 + (2 * h + 1) // 3) * (1 << (h_limit - h)) * t - (7, 10, 5)[h % 3]
                check((state["x"], state["y"]) == (x_expected, y_expected), "all-horizon literal formulas")
                check(state["y"] > floor, "raw bad-arm floor")
                check((state["s"], state["d"], state["swap"]) == expected_signed(h), "positive cylinder signed state")
                if h:
                    check(state["y"] != 3 * state["x"] - 1 and state["x"] != 3 * state["y"] - 1, "both numerical Q orientations")
                    check((state["s"], state["d"]) not in ((1, -1), (0, 0)), "canonical nontermination inside finite horizon")
                xs.append(state["x"])
                ys.append(state["y"])
            check(set(xs).isdisjoint(ys), "independent-clock meeting exclusion")
            endpoint_condition = t % 2 == (1 if h_limit % 3 == 1 else 0)
            if endpoint_condition:
                check(ys[-1] % 2 == 1 and all(odd_part(y) > floor for y in ys), "parity-qualified odd-part floor")
                strengthened_cases += 1
            family_cases += 1
            family_edges += 2 * h_limit

    # Necessary restriction: a raw endpoint floor is not an odd-part floor.
    boundary = trace(6, 3)
    check(boundary[-1]["y"] == 20 and odd_part(20) == 5 and 5 < 11 < 20, "unqualified odd-part strengthening must fail")

    returns = [
        ("10", 1, 3, 1, False),
        ("010", 2, 3, 2, False),
        ("01100", 6, 9, 10, False),
        ("001100", 12, 9, 20, False),
        ("110001", 11, 9, 29, True),
        ("01111011011101110", 121310, 177147, 469334, True),
        ("0111101101110111010", 121310, 531441, 1539074, True),
    ]
    return_cases = 0
    for word, residue, slope, constant, swap in returns:
        modulus = 1 << len(word)
        for lift in (0, 1, 7, 29, 1001):
            a = residue + modulus * lift
            actual = trace(a, len(word))
            check("".join(str(state["bit"]) for state in actual[:-1]) == word, "literal canonical return code")
            last = actual[-1]
            check((last["s"], last["d"], last["swap"]) == (1, -1, swap), "return section and orientation")
            check(last["base_form"] == (slope, constant), "recovered affine return map")
            return_cases += 1

    for u in range(100):
        a, b = 121310 + 131072 * u, 163957 + 177147 * u
        last = trace(a, 17)[-1]
        check(last["swap"] and last["y"] == b and a < b < 2 * a - 1, "expansion still violates bad-arm floor")
        a, b = 121310 + 1048576 * u, 122968 + 1062882 * u
        last = trace(a, 19)[-1]
        check(last["swap"] and last["y"] == b and a % 2 == b % 2 == 0 and a < b < 2 * a - 1, "even expansion still violates floor")

    isolated = trace(4, 12)
    check(isolated[10]["x"] == isolated[10]["y"] == 1, "isolated ordinary meeting")
    check((isolated[10]["s"], isolated[10]["d"]) == (1, -2), "meeting is not symbolic absorption")
    check(all((state["s"], state["d"]) != (1, -1) for state in isolated[1:]), "no canonical return at isolated source")
    check(isolated[0]["x"] == isolated[8]["y"] and isolated[9]["x"] == isolated[9]["y"], "independent and synchronous meeting clocks differ")

    report = {
        "status": "PASS",
        "method": "literal physical iteration and affine-slope reconstruction; author's state-transition code not imported",
        "scope": "finite independent interface audit; no global guard-success claim",
        "horizon_min": 3,
        "horizon_max": 96,
        "all_horizon_cases": family_cases,
        "all_horizon_literal_edges": family_edges,
        "parity_qualified_oddpart_cases": strengthened_cases,
        "signed_states_checked": len(signed),
        "return_word_cases": return_cases,
        "orientation_expansion_controls": 200,
        "endpoint_parity_counterexample": {"H": 3, "t": 1, "a": 6, "floor": 11, "Y_H": 20, "oddpart_Y_H": 5},
        "isolated_a4_control": {"independent_meeting": [0, 8], "first_synchronous_meeting": 9, "specified_one_meeting": 10, "state_at_clock_10": [1, -2]},
    }
    rendered = json.dumps(report, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
