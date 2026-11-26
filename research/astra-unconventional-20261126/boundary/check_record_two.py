"""Check exact J=2 conjugation, cylinder arithmetic, and pressure roots."""
from fractions import Fraction
from itertools import product
from math import log


def odd_step(n):
    numerator = 3 * n + 1
    e = (numerator & -numerator).bit_length() - 1
    return e, numerator >> e


def explicit_macro(t):
    if t % 2 == 0:
        return "A", 3 * (t // 2)
    if t % 8 == 7:
        return "B", 9 * (t // 8) + 8
    return None


def physical_macro(t):
    e, q = odd_step(6 * t - 1)
    if e == 1:
        return "A", (q + 1) // 6
    if e == 2:
        e, q = odd_step(q)
        if e == 1:
            return "B", (q + 1) // 6
    return None


def cylinder(script):
    """Return m,s,c for forward map (3**m * x+c) / 2**s."""
    m, s, c = 0, 0, 0
    for block in script:
        if block == "A":
            c = 3 * c
            m, s = m + 1, s + 1
        else:
            c = 9 * c + (1 << s)
            m, s = m + 2, s + 3
    return m, s, c


def check_cylinder(script):
    m, s, c = cylinder(script)
    q, d = 3**m, 1 << s
    residue = (-c * pow(q, -1, d)) % d
    start = d + residue
    x = start
    for desired in script:
        branch, x = explicit_macro(x)
        assert branch == desired
    assert d * x == q * start + c
    assert x % q == c * pow(d, -1, q) % q
    real = -Fraction(c, q - d)
    assert -1 <= real <= 0
    return m, s, c


def root(f, a, b):
    assert f(a) > 0 and f(b) < 0
    for _ in range(80):
        y = (a + b) / 2
        if f(y) > 0:
            a = y
        else:
            b = y
    return (a + b) / 2


if __name__ == "__main__":
    for t in range(1, 100001):
        assert physical_macro(t) == explicit_macro(t)
    print("100000 positive ordinary sources matched")
    count = 0
    for depth in range(1, 16):
        maps = {check_cylinder(word) for word in product("AB", repeat=depth)}
        assert len(maps) == 2**depth
        count += len(maps)
    print(f"{count} cylinders matched through depth 15")
    e = root(lambda h: 2**(-h) + 8**(-h) - 1, 0, 1)
    d = root(lambda h: 3**(-h) + 9**(-h) - 1, 0, 1)
    D = root(lambda h: (2/3)*2**(1-h) + (8/9)*8**(1-h) - 1, 1, 2)
    print(f"dyadic e={e:.9f}, ternary d={d:.9f}, e+d={e+d:.9f}")
    print(f"real-dyadic graph D={D:.9f}, triple D+d={D+d:.9f}")
