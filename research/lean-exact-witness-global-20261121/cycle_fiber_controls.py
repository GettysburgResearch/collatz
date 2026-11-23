"""Exact controls for CYCLE_EXCLUSION_CONTINUATION.md.

This replays specified rational cycles; it is not a cycle census.
All checks remain active under Python -O.
"""

from fractions import Fraction
from math import gcd
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def cycle(word):
    require(word and set(word) <= {"0", "1"}, "nonempty binary word required")
    bits = tuple(int(b) for b in word)
    positions = [i for i, b in enumerate(bits) if b]
    p = len(positions)
    c = sum(2**d * 3 ** (p - 1 - j) for j, d in enumerate(positions))
    denominator = 2 ** len(bits) - 3**p
    require(denominator != 0, "zero return denominator")
    root = Fraction(c, denominator)
    q = root
    states = []
    for bit in bits:
        require(q.denominator % 2 == 1, "even rational denominator")
        require(q.numerator % 2 == bit, "prescribed parity is not actual")
        states.append(q)
        q = (3 * q + 1) / 2 if bit else q / 2
    require(q == root, "cycle failed to close")
    require(len(set(states)) == len(bits), "control word is not primitive")
    return {
        "word": word,
        "A": len(bits),
        "p": p,
        "D": denominator,
        "C": c,
        "root": root,
        "states": tuple(states),
        "minimum": min(states),
    }


def json_cycle(item):
    return {
        key: [str(q) for q in value] if key == "states"
        else str(value) if isinstance(value, Fraction)
        else value
        for key, value in item.items()
    }


def carry_check(item, steps=32):
    bits = tuple(int(b) for b in item["word"])
    a = len(bits)
    carries = list(bits)
    quotients = list(item["states"])
    first_zero = None
    for t in range(steps + 1):
        for i, bit in enumerate(bits):
            allowed = {-1, 0, 1, 2} if bit else {-1, 0}
            require(carries[i] in allowed, "uniform carry alphabet violated")
            require(
                2 * quotients[(i + 1) % a] - 3**bit * quotients[i] == carries[i],
                "carry lost the full rational linear system",
            )
        if not any(carries) and first_zero is None:
            first_zero = t
        if t == steps:
            break
        digits = [c % 2 for c in carries]
        require(
            all(q.numerator % 2 == b for q, b in zip(quotients, digits)),
            "carry parity differs from rational binary digit",
        )
        numerators = [
            carries[i] + 3**bits[i] * digits[i] - 2 * digits[(i + 1) % a]
            for i in range(a)
        ]
        require(all(n % 2 == 0 for n in numerators), "nonintegral carry update")
        carries = [n // 2 for n in numerators]
        quotients = [(q - b) / 2 for q, b in zip(quotients, digits)]
    if any(q.denominator != 1 for q in item["states"]):
        require(first_zero is None, "nonintegral rational cycle reached zero carry")
    return {"word": item["word"], "steps": steps, "first_zero": first_zero}


def complementary_control(word, expected_root, expected_dual_root):
    x = cycle(word)
    y = cycle("".join("1" if b == "0" else "0" for b in word))
    require(x["root"] == expected_root, "wrong original root")
    require(y["root"] == expected_dual_root, "wrong complementary root")
    moment = sum((2 * a - 1) * (2 * b - 1) for a, b in zip(x["states"], y["states"]))
    require(moment == 3 * x["A"], "coupled moment identity failed")
    for i, bit in enumerate(map(int, word)):
        j = (i + 1) % x["A"]
        require(
            4 * x["states"][j] * y["states"][j]
            == 3 * x["states"][i] * y["states"][i]
            + bit * y["states"][i] + (1 - bit) * x["states"][i],
            "coupled edge identity failed",
        )
    return {
        "original": json_cycle(x),
        "complement": json_cycle(y),
        "coupled_moment": str(moment / x["A"]),
        "carry_checks": [carry_check(x), carry_check(y)],
    }


def main():
    min_x = cycle("1101111111100000")
    min_y = cycle("1111101001011100")
    require((min_x["A"], min_x["p"], min_x["D"]) == (16, 10, 6487), "minimum parameters")
    require((min_y["A"], min_y["p"], min_y["D"]) == (16, 10, 6487), "second minimum parameters")
    require((min_x["C"], min_y["C"]) == (83245, 109193), "minimum numerators")
    require(min_x["minimum"] == min_x["root"] > 12, "first root is not a minimum above 12")
    require(min_y["minimum"] == min_y["root"] > 12, "second root is not a minimum above 12")
    require(min_y["root"] - min_x["root"] == 4, "minimum root separation")
    require(min_x["C"] % 6487 == min_y["C"] % 6487 == 5401, "minimum common residue")

    cross_x = cycle("011111111100011101000")
    cross_y = cycle("111111111101000000011")
    require((cross_x["A"], cross_x["p"], cross_x["D"]) == (21, 13, 502829), "crossing parameters")
    require((cross_y["A"], cross_y["p"], cross_y["D"]) == (21, 13, 502829), "second crossing parameters")
    require((cross_x["C"], cross_y["C"]) == (3703718, 4206547), "crossing numerators")
    require(cross_y["root"] - cross_x["root"] == 1, "initial crossing separation")
    require(cross_x["minimum"] == Fraction(1851859, 502829) > 3, "first crossing minimum")
    require(cross_y["minimum"] == Fraction(1590227, 502829) > 3, "second crossing minimum")
    require(cross_x["C"] % 502829 == cross_y["C"] % 502829 == 183915, "crossing common residue")
    require(gcd(183915, 502829) == 1, "crossing residue is not a unit")
    require(cross_x["word"][:15].count("1") == cross_y["word"][:15].count("1") == 11, "unequal prefix counts")
    require(cross_x["states"][15] == Fraction(25946461, 502829), "first crossing endpoint")
    require(cross_y["states"][15] == Fraction(25443632, 502829), "second crossing endpoint")
    require(cross_y["states"][15] - cross_x["states"][15] == -1, "common-count order did not reverse")

    controls = {
        "scope": "Specified exact rational controls only; no all-word fiber bound or integer-cycle exclusion",
        "minimum_collision": [json_cycle(min_x), json_cycle(min_y)],
        "common_count_crossing": [json_cycle(cross_x), json_cycle(cross_y)],
        "crossing_clock": 15,
        "crossing_odd_count": 11,
        "complementary_controls": [
            complementary_control("10", Fraction(1), Fraction(2)),
            complementary_control("110", Fraction(-5), Fraction(4, 5)),
            complementary_control("11100", Fraction(19, 5), Fraction(40, 23)),
        ],
        "fiber_carry_checks": [carry_check(c) for c in (min_x, min_y, cross_x, cross_y)],
    }
    print(json.dumps(controls, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
