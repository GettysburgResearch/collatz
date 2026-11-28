"""Exact finite controls for the centred low-boundary amplitude."""
from fractions import Fraction

THREE_QUARTERS = Fraction(3, 4)


def odd_part(value):
    return value // (value & -value)


def odd_step(value):
    lifted = 3 * value + 1
    odd = odd_part(lifted)
    return odd, (lifted // odd).bit_length() - 1


def first_hit(value, budget):
    site = odd_part(value)
    divisions = (value // site).bit_length() - 1
    for depth in range(budget + 1):
        if site == 1:
            return depth, Fraction(2) ** (divisions - 2 * depth) / value
        site, gap = odd_step(site)
        divisions += gap
    return None


def in_positive_range(candidate):
    if candidate <= 0 or candidate > 1:
        return False
    level_zero = candidate
    while level_zero.numerator % 3 == 0:
        level_zero /= THREE_QUARTERS
    if level_zero > 1 or level_zero.denominator % 3 == 0:
        return False
    denominator = odd_part(level_zero.denominator)
    if odd_part(level_zero.numerator) != 1:
        return False
    threshold = Fraction(1)
    budget = 0
    while threshold >= level_zero:
        threshold *= Fraction(5, 6)
        budget += 1
    result = first_hit(denominator, budget)
    return result is not None and result[1] == level_zero


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def control():
    units = [value for value in range(1, 501, 2) if value % 3]
    for value in units:
        result = first_hit(value, 400)
        require(result is not None, f"finite first hit at {value}")
        depth, amplitude = result
        require(odd_part(amplitude.denominator) == value, "odd denominator")
        require(amplitude <= Fraction(5, 6) ** depth, "finite contraction")
        for rank in range(5):
            require(in_positive_range(THREE_QUARTERS**rank * amplitude),
                    "positive rational membership")
    for value in [Fraction(5, 16), Fraction(1, 3), Fraction(3, 2), Fraction(0)]:
        require(not in_positive_range(value), "rational nonmember")
    # At a fixed positive rank, realize many symbolic infinite-exponent limits
    # by actual integer inverse routes with their true odd gap lengths.
    for root in [1, 5, 7, 13, 85]:
        amplitude = first_hit(root, 400)[1]
        for rank in range(1, 5):
            for exponent in [25, 50, 80]:
                odd = root
                for index in range(rank):
                    start = exponent if index == 0 else 3
                    gap = next(e for e in range(start, start + 6)
                               if ((1 << e) * odd) % 9 in (4, 7))
                    odd = ((1 << gap) * odd - 1) // 3
                value = first_hit(odd, 400)[1]
                actual = odd
                for _ in range(rank):
                    actual, _ = odd_step(actual)
                require(actual == root, "literal route to original root")
                target = THREE_QUARTERS**rank * amplitude
                require(0 < value - target < Fraction(4 * rank, 1 << exponent),
                        "finite approximation to the rank point")
    print(f"PASS {len(units)} odd units, five rank tests per unit, "
          "four rational exclusions, sixty explicit rank-point approaches")


if __name__ == "__main__":
    control()
