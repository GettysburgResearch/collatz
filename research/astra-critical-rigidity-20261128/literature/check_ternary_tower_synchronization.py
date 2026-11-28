"""Finite cylinder, physical-equality and landing controls for the tower theorem."""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
import json
from math import comb


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def valuation(value, prime):
    count = 0
    while value % prime == 0:
        value //= prime
        count += 1
    return count


@lru_cache(maxsize=None)
def native_word(residue, width):
    current, slope, carry = residue, 1, 0
    grade = 0
    for date in range(width):
        if current % 2:
            slope *= 3
            carry = 3 * carry + 2**date
            current = (3 * current + 1) // 2
            grade += 1
        else:
            current //= 2
    require(2**width * current == slope * residue + carry, "affine parity word")
    require(0 <= carry <= 3**width - 2**width, "carry maximum")
    return grade, carry


def canonical(residue, width, c, gap=1):
    modulus = 2**width
    factor = 3**gap
    upper = (factor * residue + (1 - factor) * c) % modulus
    first_grade, first_carry = native_word(residue % modulus, width)
    second_grade, second_carry = native_word(upper, width)
    return (first_grade == gap + second_grade and
            first_carry == (1 - factor) * c * 3**second_grade + second_carry)


def tower_residue(n, direction, c, multiplier, width):
    return (c + multiplier * pow(3, direction * n, 2**width)) % 2**width


def cylinder_controls(report):
    for multiplier in (1, 2, 3, 4, 5, 6, 12):
        for c in (-5, 0, 1, 3):
            v = valuation(multiplier, 2)
            depth = v + 3
            for width in range(depth + 1, 12):
                modulus = 2**width
                period = 2**(width-v-2)
                classes = {(c + multiplier) % 2**depth, (c + 3*multiplier) % 2**depth}
                residues = [r for r in range(modulus) if r % 2**depth in classes]
                full_late = sum(not canonical(r, width, c) for r in residues)
                earlier = max(depth, width - 2)
                band = sum(not canonical(r, earlier, c) and canonical(r, width, c)
                           for r in residues)
                require(full_late > 0, "positive surviving capacity branches")
                for direction in (1, -1):
                    sequence = [tower_residue(n, direction, c, multiplier, width)
                                for n in range(period)]
                    require(sorted(sequence) == residues, "complete exponent permutation")
                    start = (3**width + 17) % period
                    length = 2**width + 2**(width - 1) + 9
                    numbers = list(range(start, start + length))
                    for gap in (1, 4):
                        histogram = Counter(native_word(sequence[(n + gap) % period], width)[0]
                                            for n in numbers)
                        for g, count in histogram.items():
                            upper = (length//period + 1) * comb(width, g)
                            require(count <= upper, "single-arm binomial domination")
                    multiplicity = Counter(n % period for n in numbers)
                    actual_band = sum(multiplicity[j] for j,r in enumerate(sequence)
                                      if not canonical(r, earlier, c) and canonical(r, width, c))
                    require(actual_band <= (length//period + 1)*band, "partial-period band")
                    report["complete_periods"] += 1
                    report["residue_visits"] += period
                    report["partial_exponent_visits"] += length


def step(value):
    return (3 * value + 1) / 2 if value.numerator % 2 else value / 2


def landing(value):
    date = 0
    while value.denominator != 1:
        value = step(value)
        date += 1
    return date, int(value)


def physical_controls(report):
    widths = (5, 11, 19, 27)
    for c, multiplier in ((0, 1), (1, 2), (3, 5), (0, 7), (-3, 4)):
        for direction in (1, -1):
            values = [c + multiplier * Fraction(3)**(direction * n) for n in range(122)]
            for width in widths:
                ends = values.copy()
                for _ in range(width):
                    ends = [step(x) for x in ends]
                for n in range(88):
                    for gap in (1, 2, 5, 12, 32):
                        base = n if direction > 0 else n + gap
                        residue = tower_residue(base, direction, c, multiplier, width)
                        balanced = canonical(residue, width, c, gap)
                        equal = ends[n] == ends[n + gap]
                        require(not balanced or equal, "cylinder implies numerical equality")
                        if equal and not balanced:
                            allowed = (multiplier * 3**n <= (abs(c) + 1) * 3**width
                                       if direction > 0 else n + gap <= width + valuation(multiplier, 3))
                            require(allowed, "unbalanced height cutoff")
                            report["unequal_slope_meetings"] += 1
                        if equal and n > width and c >= 0 and direction < 0:
                            common = landing(values[n])
                            require(all(landing(values[i]) == common for i in (n, n + gap)),
                                    "shared landing at paired endpoints")
                            report["verified_common_landings"] += 1
                            if all(ends[n] == ends[i] for i in range(n, n + gap + 1)):
                                require(all(landing(values[i]) == common
                                            for i in range(n, n + gap + 1)),
                                        "whole block landing")
                                report["verified_landing_blocks"] += 1
                        report["actual_endpoint_pairs"] += 1
            if c >= 0 and direction < 0:
                arrivals = [landing(x) for x in values]
                require(all(date >= n for n, (date, _) in enumerate(arrivals)),
                        "first-landing lower bound")
                report["largest_positive_landing_jump"] = max(
                    report["largest_positive_landing_jump"],
                    max(arrivals[i+1][0] - arrivals[i][0] for i in range(len(arrivals)-1)))


def main():
    report = Counter()
    cylinder_controls(report)
    physical_controls(report)
    require(report["unequal_slope_meetings"] > 0, "exercise numerical coincidences")
    require(report["verified_landing_blocks"] > 0, "exercise whole landing blocks")
    print(json.dumps(dict(report), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
