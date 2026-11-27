"""Physical finite controls for the least-source threshold and reselection."""

from fractions import Fraction
from math import log, sqrt


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def orbit(n, count):
    odd = 0
    for _ in range(count):
        odd += n % 2
        n = step(n)
    return n, odd


def canonical(u):
    h, w = 0, (4 * u + 1) // 9
    require(9 * w == 4 * u + 1 and w % 2 == 1, "invalid parent")
    while w % 3 == 0:
        h, w = h + 1, w // 3
    return h, 8 * 2**h * w - 1


def first_hit(n, expected):
    for clock in range(expected):
        require(n != 1, f"earlier hit at {clock}")
        n = step(n)
    require(n == 1, "claimed endpoint was not one")


def main():
    jump_ratio = Fraction(20970919, 122875)
    expected_hits = (6, 23, 64, 108, 114, 120, 107, 319, 306, 228)
    require(jump_ratio < 171, "jump bound")
    require(6 * 64**10 > 1550 * 21 * 27**10, "infinite-family induction base")
    for j, expected in enumerate(expected_hits):
        first_hit(9 * 2 ** (6 * j + 1) + 2, expected)
    for u in range(2, 50001, 9):
        h, b = canonical(u)
        require(orbit(b, h + 5)[0] == 9 * u + 2, "canonical representative")
    for j in range(50):
        parent = 2 ** (6 * j + 1)
        h, b = canonical(parent)
        child_endpoint = 9 * 27**j + 1
        require(orbit(9 * parent + 2, 6 * j + 1)[0] == child_endpoint, "terminal")
        require((2 * j + 1) % 3**h == 0, "valuation lower")
        require((2 * j + 1) % 3 ** (h + 1) != 0, "valuation upper")
        if j >= 10:
            require(171 * child_endpoint < b, "diagnostic for the infinite inequality")
    for d in range(3, 120):
        mersenne = 2**d - 1
        smaller = 2 ** (d - 1) - 1
        target = 9 * 2 ** (d - 3) - 1
        require(orbit(smaller, 2)[0] == target, "adjacent boundary")
        if d % 2:
            parent = (3 ** (d - 1) - 1) // 4
            require(canonical(parent) == (d - 3, mersenne), "ternary-power parent")
        else:
            common = (3**d - 1) // 4
            require(orbit(mersenne, d + 2)[0] == common, "even Mersenne left")
            require(orbit(smaller, d + 1)[0] == common, "even Mersenne right")
    for d in range(20):
        for a in range(1, 18):
            ref, grade = orbit(9 * d + 2, a)
            for v in (1, 2, 17, 98):
                n = 9 * (2**a * v + d) + 2
                require(orbit(n, a)[0] == ref + 9 * 3**grade * v, "dyadic physical endpoint")
    print("J =", jump_ratio)
    print("power-of-two family finite first hits =", *expected_hits)
    print("translate exponent =", round(log(2 / sqrt(3)) * log(3) / log(1.5), 8))
    print("canonical, dyadic and Mersenne physical endpoint controls passed")


if __name__ == "__main__":
    main()
