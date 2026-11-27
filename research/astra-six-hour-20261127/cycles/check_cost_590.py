"""Exact finite supersets for the fixed-word upper-even cost at the 590 point."""
import json
from fractions import Fraction
from functools import cache


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


@cache
def reflected_hit(source, even_budget):
    point = source
    while point != 1:
        if even_budget < 0 or point > 2**even_budget:
            return False
        if point % 2 == 0:
            point //= 2
            even_budget -= 1
        else:
            point = (3 * point - 1) // 2
    return even_budget == 0


def signed_step(value):
    return (3 * value + 1) / 2 if value.numerator % 2 else value / 2


def prezero(center, depth):
    value = -3 * center
    clock = odds = 0
    while value:
        if value.denominator == 1:
            return None
        value, branch = signed_step(value), value.numerator % 2
        clock += 1
        odds += branch
        require(odds <= depth - 1, "denominator clearing count")
    require(odds == depth - 1, "zero requires full denominator clearing")
    return clock, odds


def power_exponent(value, prime):
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    require(value == 1, "pure prime power")
    return exponent


def candidate_forms():
    base = 590
    cap = Fraction(32, 9)
    forms = set()
    maximum_time = maximum_height = maximum_offset = 0
    for start in range(1, int(base * cap) + 1):
        point = start
        clocks = odds = 0
        while True:
            maximum_time = max(maximum_time, clocks)
            maximum_height = max(maximum_height, point)
            offset = 0
            while base * 2**offset - 1 <= point:
                maximum_offset = max(maximum_offset, offset)
                remaining = 0
                while (base * 2**offset - 1) * 2**remaining <= point:
                    reflected = base * 2**(offset + remaining) - point
                    if 1 <= reflected <= 2**remaining and reflected_hit(reflected, remaining):
                        slope = Fraction(2**(offset + remaining + clocks), 3**odds)
                        center = slope * base - start
                        if slope <= cap and 1 <= center <= 2**(clocks - odds + remaining):
                            forms.add((slope, center, offset))
                    remaining += 1
                offset += 1
            if point == 1:
                break
            odd = point % 2
            point = (3 * point + 1) // 2 if odd else point // 2
            clocks += 1
            odds += odd
            require(clocks <= 115, "finite orbit cutoff")
    return forms, maximum_time, maximum_height, maximum_offset


def all_nine_classes():
    rows = []
    residues = list(range(104, 3**7, 3**5))
    for score in range(1, 5):
        for offset in range(score):
            budget = score - offset - 1
            for odds in range(1, 7):
                modulus = 3**(odds + 1)
                coefficient = 2**(odds + score)
                units = {coefficient * residue % modulus for residue in residues}
                for numerator in range(modulus + 1, 2**budget * modulus + 1):
                    if numerator % modulus not in units:
                        continue
                    center = Fraction(numerator, modulus)
                    b, remaining = center, budget
                    while b != 1 and remaining >= 0 and b <= 2**remaining:
                        if b.numerator % 2:
                            b = (3 * b - 1) / 2
                        else:
                            b /= 2
                            remaining -= 1
                    if b != 1 or remaining != 0 or prezero(center, odds + 1) is None:
                        continue
                    classes = [r for r in residues if (coefficient * r - numerator) % modulus == 0]
                    rows.append(dict(slope=str(Fraction(coefficient, modulus)), center=str(center),
                                     offset=offset, score=score, odds=odds, residues=classes))
    require([(r["slope"], r["center"], r["offset"], r["score"], r["residues"]) for r in rows]
            == [("128/81", "271/81", 0, 4, residues), ("256/243", "623/243", 0, 4, residues)],
            "terminal enumeration on all nine classes")
    return rows


def verify_two_realizations():
    for slope, center, lower_clock, lower_odds, upper_clock, upper_odds in (
        (Fraction(256, 243), Fraction(623, 243), 8, 5, 10, 4),
        (Fraction(128, 81), Fraction(271, 81), 7, 4, 9, 3),
    ):
        for factor, clocks, odds, final_slope, final_constant in (
            (1, lower_clock, lower_odds, 1, -1),
            (3, upper_clock, upper_odds, Fraction(1, 4), 0),
        ):
            coefficient, constant = factor * slope, -factor * center
            count = 0
            for _ in range(clocks):
                branch = constant.numerator % 2
                count += branch
                constant = signed_step(constant)
                coefficient *= Fraction(3**branch, 2)
            require((count, coefficient, constant) == (odds, final_slope, final_constant),
                    "fixed affine realization")


def main():
    forms, max_time, max_height, max_offset = candidate_forms()
    distinct_forms = {(slope, center) for slope, center, _ in forms}
    rows = []
    for slope, center, offset in sorted(forms):
        if slope.denominator == 1:
            continue
        depth = power_exponent(slope.denominator, 3)
        require(center.denominator == 3**depth, "upper depth at a ternary unit")
        cleared = prezero(center, depth)
        if cleared is None:
            continue
        clock, odds = cleared
        exponent = power_exponent(slope.numerator, 2)
        rows.append(dict(slope=str(slope), center=str(center), offset=offset, signed_clock=clock,
                         upper_odds=odds, upper_evens_minus_j=exponent-odds))
    require((len(distinct_forms), max_time, max_height, max_offset) == (26, 115, 638468, 10),
            "complete enlarged finite reduction")
    require(len(rows) == 5, "five prezero rows")
    require([(row["slope"], row["center"], row["upper_evens_minus_j"]) for row in rows
             if row["upper_evens_minus_j"] <= 4]
            == [("256/243", "623/243", 4), ("128/81", "271/81", 4)], "cost frontier")
    verify_two_realizations()
    print(json.dumps(dict(base=590, slope_cap="32/9", starts=2097, largest_clock=max_time,
                          largest_site=max_height, largest_offset=max_offset,
                          candidate_forms=len(distinct_forms), prezero_rows=rows,
                          all_nine_classes_graded_le_six=all_nine_classes()), indent=2))


if __name__ == "__main__":
    main()
