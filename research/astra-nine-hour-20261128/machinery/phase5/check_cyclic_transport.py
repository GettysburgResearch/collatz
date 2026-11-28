"""Exact finite controls for stationary marginal transport and the score example."""
from collections import Counter
from fractions import Fraction
from itertools import accumulate
from math import prod
from random import Random


def require(truth, description):
    if not truth:
        raise ArithmeticError(description)


def assignment_cost(starts, ends, period):
    """Minimum cost over bijections of identical-mass individual particles."""
    table = {0: 0}
    for start in starts:
        next_table = {}
        for mask, current in table.items():
            for index, end in enumerate(ends):
                bit = 1 << index
                if mask & bit:
                    continue
                # One full period is compulsory at identical locations.
                distance = (end - start - 1) % period + 1
                updated = mask | bit
                cost = current + distance
                if updated not in next_table or cost < next_table[updated]:
                    next_table[updated] = cost
        table = next_table
    return table[(1 << len(ends)) - 1]


def transport_fixture(window, lower, logarithms):
    modulus = 3**window
    period = 2 * modulus // 3
    lower_period = period // 3
    starts = [logarithms[u] % lower_period + z * lower_period for u in lower for z in range(3)]
    ends = [logarithms[1 + 3 * u] for u in lower for _ in range(3)]
    initial, terminal = Counter(starts), Counter(ends)
    totals = list(accumulate(initial[k] - terminal[k] for k in range(period)))
    offset = max(initial[k] - totals[k] for k in range(period))
    current = [offset + value for value in totals]
    require(totals[-1] == 0, "cyclic balance")
    require(all(current[k] >= initial[k] for k in range(period)), "mandatory starting edge")
    require(any(current[k] == initial[k] for k in range(period)), "missing tight cut")
    expected = assignment_cost(starts, ends, period)
    require(sum(current) == expected, "directed current disagrees with assignment")
    rank_cost = len(starts) + max(
        sum((t - k - 1) % period for t in ends) - sum((s - k) % period for s in starts)
        for k in range(period)
    )
    require(rank_cost == expected, "cut-rank formula")
    for source in starts:
        for stop in ends:
            gap = (stop - source - 1) % period + 1
            root = pow(2, source, modulus)
            lower_residue = (pow(2, stop, modulus) - 1) // 3
            require(((1 << gap) * root - 1) % modulus == 3 * lower_residue,
                    "index transport did not select the true affine child")


def score_fixture():
    barriers = {2**k + delta for k in range(3, 9) for delta in (0, 1)}
    weight = Fraction(1)
    ratio_product = Fraction(1)
    barrier_count = 0
    removed = Fraction(1)
    for score in range(1, 260):
        ordinary_ratio = Fraction(score + 9, score + 15)
        if score in barriers:
            barrier_count += 1
            weight /= 2
            ratio_product *= 2
            removed /= ordinary_ratio
        else:
            correction = Fraction(1, score + 12)
            up, down = Fraction(1, 3) + correction, Fraction(1, 3) - correction
            require(down > Fraction(1, 4) and up + down == Fraction(2, 3), "ellipticity")
            require(down / up == ordinary_ratio, "local product")
            ratio_product *= ordinary_ratio
        untouched = Fraction(prod(range(10, 16)), prod(range(score + 10, score + 16)))
        require(weight == Fraction(1, 2**barrier_count), "Haar invariant weight")
        require(ratio_product == 2**barrier_count * untouched * removed, "telescoping product")


def primitive_character_fixture():
    comparisons = 0
    for window in range(3, 6):
        modulus = 3**window
        period = 2 * modulus // 3
        parent_period = period // 3
        logarithm = {pow(2, k, modulus): k for k in range(period)}
        graph = [logarithm[1 + 3 * pow(2, k, modulus // 3)] for k in range(parent_period)]
        for output_frequency in range(period):
            if output_frequency % 3 == 0:
                continue
            for input_frequency in range(parent_period):
                exponents = Counter(
                    (output_frequency * stop - 3 * input_frequency * k) % period
                    for k, stop in enumerate(graph)
                )
                square = [0] * period
                for r, a in exponents.items():
                    for t, b in exponents.items():
                        square[(r - t) % period] += a * b
                # Phi_(2*3^j)(X) = X^(period/3) - X^(period/6) + 1.
                for i in range(period - 1, parent_period - 1, -1):
                    square[i - parent_period // 2] += square[i]
                    square[i - parent_period] -= square[i]
                expected = 3 * parent_period // 2 if input_frequency % 3 else 0
                require(square[0] == expected and not any(square[1:parent_period]),
                        "actual primitive-character squared magnitude")
                comparisons += 1
    return comparisons


def main():
    rng = Random(1693)
    cases = 0
    for window in range(2, 6):
        modulus = 3**window
        logarithms = {pow(2, k, modulus): k for k in range(2 * modulus // 3)}
        require(len(logarithms) == 2 * modulus // 3, "doubling is not a full unit cycle")
        units = [u for u in range(1, modulus // 3) if u % 3]
        for size in (1, 2, 3):
            for _ in range(12):
                transport_fixture(window, rng.choices(units, k=size), logarithms)
                cases += 1
    require(assignment_cost([0], [0], 6) == 6, "zero-distance positive-gap control")
    score_fixture()
    characters = primitive_character_fixture()
    print(f"physical assignment / current / cut-rank controls {cases}")
    print("positive full-turn control and 259 exact score products passed")
    print(f"exact primitive-character autocorrelation checks {characters}")


if __name__ == "__main__":
    main()
