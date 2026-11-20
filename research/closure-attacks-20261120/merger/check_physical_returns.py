#!/usr/bin/env python3
"""Check exact affine five-pair return and its valuation rank; no orbit census."""

from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(pair, bit):
    a, b = pair
    require(a % 2 == 0 and b % 2 == bit, ("illegal affine parity", pair, bit))
    if bit:
        return 3 * a // 2, (3 * b + 1) // 2
    return a // 2, b // 2


def affine_word(word):
    c = q = 0
    for index, bit in enumerate(map(int, word)):
        if bit:
            c = 3 * c + 2 ** index
            q += 1
    return q, c


def valuation_two(n):
    require(n > 0, ("nonpositive valuation input", n))
    return (n & -n).bit_length() - 1


def main():
    words = ("101111111111111000010", "100100111111111011101")
    starts = ((12582912, 5712553), (62914560, 28562765))
    x, y = starts
    differences = []
    for clock, (left, right) in enumerate(zip(*words), 1):
        x, y = step(x, int(left)), step(y, int(right))
        difference = y[0] - 5 * x[0], y[1] - 5 * x[1]
        reverse_difference = x[0] - 5 * y[0], x[1] - 5 * y[1]
        require(reverse_difference[0] * reverse_difference[1] >= 0
                and reverse_difference[1] != 0,
                ("possible reversed same-clock return", clock, reverse_difference))
        differences.append(difference)
        if clock < 21:
            require(difference != (0, 0), ("early affine return", clock))
            require(difference[0] * difference[1] >= 0 and difference[1] != 0,
                    ("possible positive numerical return", clock, difference))
    require(x == (86093442, 39085825), ("left endpoint", x))
    require(y == (430467210, 195429125), ("right endpoint", y))
    require(differences[18] == (0, 1), ("clock-19 carry", differences[18]))
    require(differences[20] == (0, 0), ("final return", differences[20]))
    require(all(a % 2 == 0 and b % 2 == 1 and a % 3 == 0 and b % 3 != 0
                for a, b in (starts[0], x)), "odd unit domain")
    require(x[0] > starts[0][0] and x[1] > starts[0][1], "nonexpanding control")
    q1, c1 = affine_word(words[0])
    q2, c2 = affine_word(words[1])
    require(q1 == q2 == 15 and c1 == 24340829 and c2 == 5 * c1,
            ("return constants", q1, c1, q2, c2))
    a, b, c = 3 ** 15, 2 ** 21, c1
    d = a - b
    require(d == 12251755 > 0, "expanding slope")
    # Identity D*R(X)+C = A/B*(D*X+C), checked coefficient by coefficient.
    lhs = Fraction(d * a, b), Fraction(d * c, b) + c
    rhs = Fraction(a * d, b), Fraction(a * c, b)
    require(lhs == rhs, "valuation conjugacy")
    # Construct arbitrarily long prescribed runs via the exact residue at
    # depth k, and replay modest depths to check the rank implementation.
    ranks = []
    for depth in range(1, 13):
        modulus = 2 ** (21 * depth)
        z = (-c * pow(d, -1, modulus)) % modulus
        if z == 0:
            z += modulus
        initial = z
        rank = valuation_two(d * z + c)
        require(rank >= 21 * depth, ("run construction", depth, rank))
        for _ in range(depth):
            require((a * z + c) % b == 0, ("run integrality", depth, z))
            require(z % b == 1518249, ("physical return residue", depth, z))
            next_z = (a * z + c) // b
            require(next_z > z > 0, ("positive expansion", z, next_z))
            next_rank = valuation_two(d * next_z + c)
            require(next_rank == rank - 21, ("rank drop", rank, next_rank))
            z, rank = next_z, next_rank
        ranks.append({"prescribed_returns": depth, "initial_bits": initial.bit_length()})
    product = Fraction(1, 4) * Fraction(11, 7) ** 2
    for numerator, denominator in ((17, 11), (26, 17), (83, 55), (98, 65), (125, 83)):
        product *= Fraction(numerator, denominator)
    require(product == 5, ("semigroup product", product))
    print(json.dumps({
        "status": "PASS",
        "scope": "all-lift affine return, first-return sign checks, exact rank identity",
        "first_same_clock_return": 21,
        "odd_count_each_arm": 15,
        "source_progression": "5712553+12582912*u, u>=0",
        "returned_progression": "39085825+86093442*u, u>=0",
        "result": "first same-clock ratio-five return increases the odd unit parameter; both orientations checked",
        "rank": "v2(12251755*z+24340829), decreases by 21 on each repeated word",
        "finite_rank_controls": ranks,
        "semigroup_product": str(product),
        "unproved": "total success, arbitrary return-word switching, and general M5 mergers",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
