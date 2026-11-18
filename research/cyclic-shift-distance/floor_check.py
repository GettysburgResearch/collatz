"""Exact Farey, distance and ordinary descent checks for the uniform floors."""

from fractions import Fraction


def log_interval(integer, terms=100):
    # ln x = 2 atanh((x-1)/(x+1)); majorize the omitted positive tail geometrically.
    z = Fraction(integer - 1, integer + 1)
    low = 2 * sum(z ** (2 * j + 1) / (2 * j + 1) for j in range(terms))
    error = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return low, low + error


def verify_farey(cap, left, right, upper, log2, log3):
    a, b = left
    c, d = right
    assert b * c - a * d == 1 and b + d > cap
    min_gap = b * log2[0] - a * log3[1]
    assert min_gap > 0 and d * log2[1] < c * log3[0]
    assert a / (3 * min_gap) < upper


def verify_first_cutoff(distance, exponent):
    # (1) is impossible on [2^j,2^(j+1)) for this and all larger j.
    assert 3**200 < 2**317 and 3**12 > 2**19
    assert 2**exponent > (
        Fraction(12, 7) * (2 + 16 * (exponent + 1) + distance)
        * Fraction(317, 200) ** (distance + 1)
    )


def verify_refinement(distance, minimum_cap, known_descent, period_cap, refined_cap):
    assert 2 * period_cap < 3 * known_descent  # lambda <= L/(3m) < 1/2
    cap = 1 + 2 * minimum_cap * 3 ** (distance // 2)
    z = (cap - 1).bit_length()
    period_bound = Fraction(12, 7) * (z + 1) * (Fraction(317, 200) ** (distance + 1) - 1)
    assert period_bound < refined_cap
    return z


def local_descent(limit):
    max_steps = 0
    for source in range(2, limit):
        x = source
        steps = 0
        while x >= source:
            x = (3 * x + 1 if x % 2 else x) // 2
            steps += 1
        max_steps = max(max_steps, steps)
    return max_steps


def main():
    log2, log3 = log_interval(2), log_interval(3)
    verify_first_cutoff(10, 17)
    verify_farey(2**17, (79335, 125743), (31867, 50508), 2**33, log2, log3)
    z_local = verify_refinement(10, 2**33, 4_000_000, 2**17, 12_000)
    verify_farey(12_000, (6956, 11025), (665, 1054), 4_000_000, log2, log3)
    verify_first_cutoff(42, 39)
    verify_farey(
        2**39, (137528045312, 217976794617), (340526703945, 539722056247),
        2**76, log2, log3,
    )
    z_external = verify_refinement(42, 2**76, 2**68, 2**39, 90_000_000_000)
    verify_farey(
        90_000_000_000, (6586818670, 10439860591), (65470613321, 103768467013),
        2**68, log2, log3,
    )
    print(f"Certified Farey and distance bounds, Z <= {z_local} and {z_external}.")
    max_steps = local_descent(4_000_000)
    print(f"Verified first descent for 2 <= n < 4,000,000. Maximum shortcut steps: {max_steps}.")
    print("The stronger floor uses Barina's external convergence computation below 2^68.")


if __name__ == "__main__":
    main()
