"""Exact signed and ordinary checks for every sharp whole-valuation family."""

from check_finite_patterns import check, trace
from check_fixed_mersenne import charges

# Valuation, earlier exponent gap, canonical price, odd cofactor residue mod 54.
ROWS = [(28, 12, 1060, 19), (70, 36, 432, 37), (856, 420, 19, 19),
        (926, 448, 30, 49), (1018, 504, 185, 19), (1736, 886, 10, 49),
        (1990, 1038, 245, 19), (3310, 1648, 12, 37), (3592, 1810, 12, 19),
        (8882, 4450, 10, 49), (9172, 4570, 35, 19), (15280, 7614, 7, 37),
        (24346, 12226, 10, 19), (31132, 15676, 30, 19), (34048, 17038, 12, 19)]


def verify(valuation, gap, price, cofactor, costs):
    denominator = 3 ** (gap + 1)
    numerator = 1 - denominator
    grade = 0
    for _ in range(valuation):
        if numerator % 2:
            grade += 1
            if denominator > 1:
                denominator //= 3
                numerator += denominator
            else:
                numerator = 3 * numerator + 1
        numerator //= 2
    check((numerator, denominator, grade) == (1, 1, gap + 2), "signed release profile")
    check(0 < cofactor < 54 and cofactor % 2 == 1 and
          pow(2, valuation - 4, 27) * cofactor % 27 == 1, "full cofactor class")
    check(costs[((10 - gap) // 2) % 81] == price, "pinned ordinary earlier price")
    modulus = 1 << (valuation + 1)
    earlier = ((1 + (1 << valuation)) * pow(3, -gap - 1, modulus)) % modulus
    low, low_grade = trace(earlier - 1, valuation + 1)
    high, high_grade = trace(3**gap * earlier - 1, valuation + 1)
    check(low == high and low_grade == gap + 2 and high_grade == 2,
          "ordinary release and terminal grade")


def main():
    costs = charges()
    for row in ROWS:
        verify(*row, costs)
    print("sharp valuations", len(ROWS), "paid", sum(gap >= price for _, gap, price, _ in ROWS),
          "maximum height saving", max(gap - price for _, gap, price, _ in ROWS))


if __name__ == "__main__":
    main()
