"""Exact dyadic reciprocal bounds for distinct positive shortcut orbit states."""

from fractions import Fraction
from math import comb


def ceiling(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def shell_bound(k: int) -> Fraction:
    width = 2**k
    count = width // 2
    high_grade = 0
    for p in range(k, 0, -1):
        low_endpoints = 2 * 3**p + ceiling(Fraction(3, 2) ** p)
        count = min(count, low_endpoints + high_grade + k)
        high_grade += comb(k - 1, p - 1)
    ratio = Fraction(count, width)
    return ratio - ratio**2 / (1 + 2 * ratio)


def scaled_upper(value: Fraction) -> int:
    return ceiling(10**6 * value)


def main() -> None:
    cutoff = 400
    a = Fraction(27, 32)
    b = Fraction(3125, 3456)
    # Start at k=400 in this majorant. The finite sum already includes k=400.
    tail = 5 * (3 * a**80 / (1 - a) + Fraction(3, 5) * b**80 / (1 - b))
    tail += Fraction(2 * (cutoff + 1), 2**cutoff)
    parts = [scaled_upper(shell_bound(k)) for k in range(1, cutoff + 1)]
    tail_upper = scaled_upper(tail)
    totals = {k: sum(parts[max(1, k) - 1 :]) + tail_upper for k in [0, 40, 71]}
    totals[0] += 10**6  # the positive odd integer 1
    for floor, target in [(0, 18_500_000), (40, 6_300_000), (71, 2_800_000)]:
        if totals[floor] >= target:
            raise ArithmeticError(f"reciprocal bound exceeds target at k={floor}")
    print(f"finite_shells={cutoff} geometric_tail_upper_millionths={tail_upper}")
    for k, bound in totals.items():
        print(f"floor=2^{k} reciprocal_sum_upper_millionths={bound}")
    for budget, correction, threshold in [(24, Fraction(512), 74_220), (32, Fraction(4, 3), 33_000)]:
        floor = budget + 10
        lower = Fraction(81, 128) * (1 - Fraction(1, 2) ** (floor - budget))
        mass = 486 * (1 + Fraction(2, 3) ** floor) * (correction / lower) ** 2
        mass *= Fraction(4) ** (budget - 40)
        envelope = scaled_upper(mass)
        if lower * 2 ** (40 - budget) <= correction or envelope > threshold:
            raise ArithmeticError(f"failed physical coverage bound at even budget {budget}")
        print(f"gain_bits=40 even_budget={budget} distortion={correction} mass_upper_millionths={envelope}")


if __name__ == "__main__":
    main()
