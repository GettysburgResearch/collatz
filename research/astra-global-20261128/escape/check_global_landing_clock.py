#!/usr/bin/env python3
"""Bounded exact controls for native time, the scale walk and balanced addresses."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def bounded_landing(value, floor, budget):
    for clock in range(budget + 1):
        if value % 2 and value <= floor:
            return value, clock
        value = (3 * value + 1) // 2 if value % 2 else value // 2
    return None


def shifted(outcome):
    if outcome is None:
        return None
    label, clock = outcome
    return label, clock + 1


def check_native_splits():
    windows = 0
    sources = 0
    for floor in (1, 4, 17, 31):
        for left_half in (floor + 1, 2 * floor + 3, 173):
            for budget in (1, 4, 11, 37, 90):
                candidates = range(2 * left_half, 4 * left_half)
                original = Counter(bounded_landing(x, floor, budget) for x in candidates)
                branches = Counter()
                for m in range(left_half, 2 * left_half):
                    branches[shifted(bounded_landing(m, floor, budget - 1))] += 1
                    branches[shifted(bounded_landing(3 * m + 2, floor, budget - 1))] += 1
                require(original == branches, "native even and odd image split")
                windows += 1
                sources += len(candidates)
    return windows, sources


def modulo_three_scale(value):
    while value >= 3:
        value /= 3
    while value < 1:
        value *= 3
    return value


def check_scale_walk():
    words = crossing_tests = crossings = phase_tests = 0
    levels = (Fraction(4, 3), Fraction(3, 2), Fraction(2), Fraction(3), Fraction(5))
    for length in range(1, 11):
        for bits in product((0, 1), repeat=length):
            levels_seen = [Fraction(1)]
            for bit in bits:
                levels_seen.append(levels_seen[-1] * 2 / 3 ** bit)
            end = levels_seen[-1]
            words += 1
            for target in levels:
                forward = all(v < target for v in levels_seen[:-1]) and end >= target
                overshoot = end / target
                reverse = 1 <= overshoot < 2 and all(
                    end / v > overshoot for v in reversed(levels_seen[:-1]))
                require(forward == reverse, "strict reversed first-crossing criterion")
                crossing_tests += 1
                if not forward:
                    continue
                crossings += 1
                residual_separation = Fraction(91) / end
                for extra, landing in ((0, Fraction(1)), (3, Fraction(3, 7)),
                                       (9, Fraction(5, 8))):
                    original = Fraction(2 ** (length + extra), 91) * landing
                    reduced = Fraction(2 ** extra) * landing / residual_separation
                    require(original == reduced * 3 ** sum(bits), "exact phase cocycle")
                    require(modulo_three_scale(original) == modulo_three_scale(reduced),
                            "wrapped clock phase")
                    phase_tests += 1
    return words, crossing_tests, crossings, phase_tests


def check_balanced_addresses():
    exit_tests = 0
    for depth in (4, 12, 31, 60):
        total = numerator = 0
        letters = []
        for index in range(1, depth + 2):
            next_total = 0
            while 8 * 2 ** next_total < 9 * 3 ** index:
                next_total += 1
            exponent = next_total - total
            letters.append(exponent)
            numerator = 2 ** exponent * numerator + 3 ** (index - 1)
            total = next_total
            slope = Fraction(3 ** index, 2 ** total)
            require(Fraction(4, 9) <= slope <= Fraction(8, 9), "balanced slope")
        modulus = 3 ** (depth + 1)
        residue = numerator * pow(2 ** total, -1, modulus) % modulus
        exits = []
        slope = Fraction(1)
        for index, exponent in enumerate(letters[:depth]):
            if index:
                eligible = [f for f in range(3, 15) if f != exponent
                            and (2 ** f * residue - 1) % 3 == 0
                            and (2 ** f * residue - 1) % 9 != 0]
                require(bool(eligible), "eligible unit side branch")
                new_slope = slope * Fraction(3, 2 ** eligible[0])
                require(Fraction(4, 9) * Fraction(3, 2 ** 14) <= new_slope < Fraction(19, 20),
                        "positive capped side-branch weight")
                exits.append(tuple(letters[:index]) + (eligible[0],))
                exit_tests += 1
            dividend = 2 ** exponent * residue - 1
            require(dividend % 3 == 0, "address reconstruction")
            modulus //= 3
            residue = (dividend // 3) % modulus
            slope *= Fraction(3, 2 ** exponent)
        for short, long in zip(exits, exits[1:]):
            require(short != long[:len(short)], "prefix-free exits")
    return exit_tests


def check_octave_discrepancies():
    observed = {}
    for dilation in (Fraction(2), Fraction(3), Fraction(4), Fraction(5), Fraction(17, 9)):
        ratio = modulo_three_scale(dilation)
        cuts = sorted({Fraction(1), Fraction(2), Fraction(3), ratio,
                       min(2 * ratio, Fraction(3)), max(Fraction(1), 2 * ratio / 3)})
        difference = Fraction(0)
        for left, right in zip(cuts, cuts[1:]):
            middle = (left + right) / 2
            first = int(1 <= middle < 2)
            other = sum((Fraction(3 ** k, 1) / ratio for k in (0, 1)
                         if 1 <= 3 ** k * middle / ratio < 2), Fraction(0))
            difference += (right - left) * abs(first - other) / 2
        formula = 1 - max(2 / ratio - 1, 0) - max(2 * ratio / 3 - 1, 0)
        require(difference == formula, "wrapped octave integral")
        observed[str(dilation)] = str(difference)
    return observed


def main():
    windows, sources = check_native_splits()
    words, tests, crossings, phases = check_scale_walk()
    print(json.dumps({
        "scope": "bounded exact identities; analytic transport and orbit fates are outside the check",
        "native_count_windows": windows,
        "native_count_sources": sources,
        "scale_walk_words": words,
        "forward_reverse_tests": tests,
        "first_crossings": crossings,
        "phase_checks": phases,
        "balanced_side_exits": check_balanced_addresses(),
        "full_octave_tv": check_octave_discrepancies(),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
