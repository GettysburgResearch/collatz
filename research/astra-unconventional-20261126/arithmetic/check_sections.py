"""Exact coefficient sections and ordinary affine-shadow controls."""

from collections import Counter
from functools import cache
import json


def branch(exponent):
    denominator = 1 << exponent
    odd = exponent % 2
    residue = ((5 if odd else 1) * (denominator // 2) - 2) // 3
    return denominator, residue, 2 * odd


def require(condition):
    if not condition:
        raise ValueError("Control failed")


def section_control(ceiling, depth):
    branches = {e: branch(e) for e in range(1, ceiling + 1)}

    @cache
    def sections(edge, digits, residue):
        if digits == 0:
            return Counter({(edge, 0, 0): 1})
        mul, offset, _ = branches[edge]
        inner, target = divmod(mul * (residue % 3) + offset, 3)
        shift, suffix = divmod(mul * (residue // 3) + inner, 3 ** (digits - 1))
        result = Counter()
        for parent, (_, _, arrival) in branches.items():
            if arrival != target:
                continue
            for (final, level, remainder), count in sections(parent, digits - 1, suffix).items():
                result[(final, level + edge, (shift << level) + remainder)] += count
        return result

    @cache
    def physical(edge, n, digits):
        if digits == 0:
            return Counter({(edge, n): 1})
        mul, offset, _ = branches[edge]
        parent_index, target = divmod(mul * n + offset, 3)
        result = Counter()
        for parent, (_, _, arrival) in branches.items():
            if arrival == target:
                result.update(physical(parent, parent_index, digits - 1))
        return result

    checks = 0
    largest = 0
    for edge in branches:
        for residue in range(3**depth):
            terms = sections(edge, depth, residue)
            largest = max(largest, sum(terms.values()))
            for _, level, remainder in terms:
                require(depth <= level <= ceiling * depth)
                require(0 <= remainder < 2**level)
            for n in [0, 1, 23, 101]:
                decoded = Counter()
                for (final, level, remainder), count in terms.items():
                    decoded[(final, (n << level) + remainder)] += count
                require(decoded == physical(edge, n * 3**depth + residue, depth))
                checks += 1
    return {"ceiling": ceiling, "depth": depth, "comparisons": checks,
            "largest_leaf_count": largest}


def physical_control():
    largest = 0
    for t in range(50000):
        x = 2*t + 1
        z = 3*x + 1
        exponent = (z & -z).bit_length() - 1
        mul, source, target = branch(exponent)
        v, r = divmod(t, mul)
        require(r == source)
        require((z // mul - 1) // 2 == 3*v + target)
        largest = max(largest, exponent)
    return {"odd_starts": 50000, "largest_exponent": largest}


def shadow_control(length):
    exponents = (3**length).bit_length() - 1
    nb = exponents - length
    na = length - nb
    divisor = 2**exponents
    numerator = 3**length
    carry = 3**na * (4**nb - 3**nb)
    initial = divisor + (-carry * pow(numerator, -1, divisor)) % divisor
    current = initial
    low = initial
    for e in [2]*nb + [1]*na:
        if e == 2:
            require(current % 4 == 1)
            current = (3*current + 1)//4
        else:
            require(current % 2 == 0)
            current = 3*current//2
        low = min(low, current)
    require(divisor*current == numerator*initial+carry)
    return {"word_length": length, "contractions": nb, "expansions": na,
            "input": initial, "minimum": low, "output": current,
            "cleared_carry": carry, "denominator": divisor}


if __name__ == "__main__":
    print(json.dumps({
        "ordinary_coordinates": physical_control(),
        "signed_section_expansions": [section_control(2, 5), section_control(5, 4),
                                      section_control(8, 4)],
        "affine_shadow_words": [shadow_control(n) for n in [12, 24, 48, 96]],
    }, indent=2))
