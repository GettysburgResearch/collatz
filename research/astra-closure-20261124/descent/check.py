"""Cross-check finite ternary cylinder unions against forward positive-integer visits."""

from fractions import Fraction
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def words_up_to_clock(limit):
    def extend(word, remaining):
        yield word
        for gap in range(1, remaining + 1):
            yield from extend(word + (gap,), remaining - gap)

    yield from extend((), limit)


def carries(word):
    carry = 0
    total = 0
    for gap in word:
        carry = 3 * carry + (1 << total)
        total += gap
    return 3 ** len(word), 1 << total, carry


def starts_with_any(word, family):
    return any(word[:len(prefix)] == prefix for prefix in family)


def compare(limit, ratio, family):
    modulus = 3 ** limit
    # Above this cutoff the sign of each fixed excess slope dominates its
    # constant carry. Include a full ternary period of positive odd targets.
    last_small = 0
    selected = []
    for word in words_up_to_clock(limit):
        if not starts_with_any(word, family):
            continue
        denom, scale, carry = carries(word)
        excess = scale * ratio.denominator - denom * ratio.numerator
        if excess > 0:
            last_small = max(last_small, carry * ratio.denominator // excess)
        else:
            residue = carry * pow(scale, -1, denom) % denom
            selected.append((residue, denom))

    lower = 2 * (last_small + 2) + 1
    upper = lower + 2 * modulus
    algebraic = {
        q for q in range(lower, upper, 2)
        if any(q % denom == residue for residue, denom in selected)
    }
    physical = set()
    max_start = ratio.numerator * (upper - 1) // ratio.denominator
    for start in range(1, max_start + 1, 2):
        value = start
        word = ()
        clock = 0
        while clock <= limit:
            if lower <= value < upper and start <= ratio * value and starts_with_any(word, family):
                physical.add(value)
            triple = 3 * value + 1
            factor = triple & -triple
            gap = factor.bit_length() - 1
            clock += gap
            word += (gap,)
            value = triple // factor
    require(physical == algebraic, f"physical and ternary targets disagree: {limit}, {ratio}, {family}")
    return len(physical)


def main():
    families = (((1, 1),), ((1, 1), (2,)), ((1, 2), (2, 1), (1, 1, 1)), ((),))
    counts = [
        compare(deadline, ratio, family)
        for deadline, ratio, family in product((5, 7), (Fraction(1), Fraction(3, 2)), families)
    ]
    print(json.dumps({"finite_law_cases": len(counts), "distinct_targets_per_case": counts}))


if __name__ == "__main__":
    main()
