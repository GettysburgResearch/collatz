"""Finite arithmetic controls for the weighted parity and rational-fit arguments."""
from collections import Counter
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(value):
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2


def matrix_rank(rows):
    pivots = {}
    for row in rows:
        current = list(map(Fraction, row))
        for col, previous in sorted(pivots.items()):
            if current[col]:
                scalar = current[col]
                current = [v - scalar * p for v, p in zip(current, previous)]
        first = next((i for i, entry in enumerate(current) if entry), None)
        if first is not None:
            scalar = current[first]
            pivots[first] = [v / scalar for v in current]
    return len(pivots)


def weighted_prefix_checks():
    clocks = 0
    for start in range(1, 513):
        value = start
        place = Fraction(1)
        evens = 0
        partial = Fraction(0)
        product = Fraction(start)
        for i in range(32):
            bit = value % 2
            partial += bit * 3 ** evens * place
            product *= 1 + Fraction(bit, 3 * value)
            evens += 1 - bit
            place *= Fraction(2, 3)
            value = step(value)
            end = place * 3 ** evens * value
            require(3 * start + partial == 3 * end == 3 * product, "finite telescope")
            require(end.numerator % (2 ** (i + 1)) == 0, "dyadic valuation")
            clocks += 1
    return clocks


def fitting_controls():
    values = [27]
    for _ in range(40):
        values.append(step(values[-1]))
    require(len(set(values)) == len(values), "distinct physical observations")
    counts = Counter(x % 2 for x in values[:-1])
    results = []
    for degree in range(5):
        data = []
        for current, following in zip(values, values[1:]):
            terms = [current ** j for j in range(degree + 1)]
            data.append(terms + [-following * t for t in terms])
        rank = matrix_rank(data)
        require(min(counts.values()) > degree + 1, "root bound hypothesis")
        require(rank == 2 * (degree + 1), "nonzero fit unexpectedly survived")
        results.append(rank)
    require(all(step(x) == 3 - x for x in (1, 2)), "periodic rational interpolant")
    return {"source": 27, "observations": 40, "even": counts[0], "odd": counts[1],
            "full_fitting_matrix_ranks_degrees_0_to_4": results}


def block_carry_checks():
    result = {}
    for word in ("110111", "111110"):
        carry = 0
        odds = 0
        for i, letter in enumerate(word):
            if letter == "1":
                carry = 3 * carry + 2 ** i
                odds += 1
        lifts = 0
        for source in range(1, 1025):
            value = source
            actual = []
            for _ in word:
                actual.append(str(value % 2))
                value = step(value)
            if "".join(actual) == word:
                require(2 ** len(word) * value == 3 ** odds * source + carry, "block carry")
                lifts += 1
        require(lifts == 16 and 3 ** odds > 2 ** len(word), "expanding physical cylinder")
        result[word] = {"carry": carry, "positive_lifts_through_1024": lifts}
    return result


if __name__ == "__main__":
    print(json.dumps({"prefix_clocks": weighted_prefix_checks(),
                      "rational_fits": fitting_controls(),
                      "automatic_block_coefficients": block_carry_checks()}, sort_keys=True))
