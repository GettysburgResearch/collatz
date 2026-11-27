"""Finite controls for the independent affine shadow rigidity argument."""
from fractions import Fraction
from itertools import product
from math import gcd
from functools import reduce


def require(condition, message):
    if not condition:
        raise ValueError(message)


def words(length):
    # Each tuple is (complete affine carry, clock denominator).
    level = [(0, 1)]
    for _ in range(length):
        level = [
            (9 * carry + denominator * digit, denominator * clock)
            for carry, denominator in level
            for digit, clock in [(7, 8), (5, 32)]
        ]
    return level


def exact_gcd_checks():
    cases = 0
    for k in range(1, 10):
        macro = words(k)
        for q in range(-180, 181):
            discrepancy = [abs((9**k - n) * q + c) for c, n in macro]
            require(reduce(gcd, discrepancy) == gcd(166, q + 7), (k, q))
            cases += 1
    return cases


def table(forward):
    offsets = [Fraction(i, 4) for i in (-1, 0, 1)] if forward else [
        Fraction(i, 9) for i in (-2, 0, 2)
    ]
    rows = set()
    for h, x, y in product(offsets, (5, 7), (5, 7, 11, 19)):
        a = (y + 23*x - 23*h) / 166
        if forward:
            other_l, other_p = x + 8*h, y - 32*h
        else:
            other_l, other_p = x - 9*h, y + 9*h
        if (0 < a < 1 and other_l in (5, 7) and
                other_p in (5, 7, 11, 19)):
            l = 7*a - x
            rows.add((a, l, l+h))
    return rows


def rational_rows(rows):
    return {
        tuple(Fraction(value, denominator) for value in entries)
        for denominator, *entries in rows
    }


def quotient_checks():
    cases = 0
    for d in range(5, 320):
        if gcd(d, 6) != 1:
            continue
        unit_l = pow(8, -1, d)
        unit_p = pow(32, -1, d)
        for f in (83, 166):
            for start in (0, 1, 7):
                seen = {start % d}
                frontier = list(seen)
                while frontier:
                    z = frontier.pop()
                    for nxt in ((9*z*unit_l) % d, ((9*z+f)*unit_p) % d):
                        if nxt not in seen:
                            seen.add(nxt)
                            frontier.append(nxt)
                modulus = gcd(d, f)
                if modulus == 1:
                    expected = set(range(d))
                elif start % modulus == 0:
                    expected = set(range(0, d, modulus))
                else:
                    expected = {z for z in range(d) if z % modulus}
                require(seen == expected, (d, f, start))
                cases += 1
        for integer_part, carry in product((5, 6), (5, 7)):
            numerator = 9*(integer_part*d + 4) - carry*d
            require(numerator % 8 != 0, (d, integer_part, carry))
    return cases


def main():
    constant = [(83, 60, 5, 5), (83, 61, 12, 12), (83, 63, 26, 26),
                (83, 67, 54, 54)]
    past = table(False)
    future = table(True)
    require(past == rational_rows(constant + [(747, 572, 269, 103),
                                             (747, 724, -161, 5)]), past)
    require(future == rational_rows(constant + [(664, 513, 271, 437)]), future)
    for k in range(1, 65):
        q = 2 * 8**k - 7
        for j in range(k):
            first, r = divmod(3*q+1, 4)
            require(r == 0 and first % 2 == 1, (k, j, q))
            q, r = divmod(3*first+1, 2)
            require(r == 0 and q % 2 == 1 and (q+7) % 83 != 0, (k, j, q))
        require(q == 2 * 9**k - 7, k)
    require({pow(53, j, 83) for j in range(82)} == set(range(1, 83)),
            "incomplete residue orbit")
    local_carries = {(9*z - 8*t)//83
                     for z in (416, 499) for t in (468, 551)}
    require(local_carries == {-8, 0, 1, 9}, local_carries)
    print(f"gcd checks: {exact_gcd_checks()}; past rows: {len(past)}; "
          f"future rows: {len(future)}; finite L paths: 64; residue orbit size: 82; quotient orbits: {quotient_checks()}")


if __name__ == "__main__":
    main()
