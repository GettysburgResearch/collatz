"""Integer replay of the true upper even-count reduction. No size cap on a gap."""
from fractions import Fraction
from math import gcd
import json


def trajectory(x, clocks):
    odds = 0
    for _ in range(clocks):
        bit = x.numerator % 2
        x = (x * (1 + 2 * bit) + bit) / 2
        odds += bit
    return x, odds


def ordinary(x, clocks):
    v, p = trajectory(Fraction(x), clocks)
    assert v.denominator == 1
    return int(v), p


def residue(c, h):
    return (c.numerator * pow(c.denominator, -1, 2**h)) % 2**h


def simple(a, h, cap=Fraction(32, 81)):
    center = -Fraction(3 + 2**a, 27)
    out, q = trajectory(center, h)
    x0 = residue(center, h)
    y0, p = ordinary(x0, h)
    assert p == q
    assert y0 == out + Fraction(3**q, 2**h) * (x0 - center)
    # On this exact shape x-center < cap*N.
    assert Fraction(3**q, 2**h) * cap + max(out, 0) / 2048 < Fraction(3, 8)
    return dict(a=a, h=h, q=q, x0=x0, y0=y0, signed=str(out))


def main():
    assert pow(2, 162, 81) == 1
    assert all(pow(2, a, 81) != 1 for a in range(1, 54))
    upper = [next(b for b in range(54)
                  if (9 + 3*2**a + 2**b - 2**16) % 81 == 0)
             for a in range(1, 10)]
    assert upper == [30, 44, 36, 20, 6, 32, 48, 26, 0]
    rows = [simple(a, h) for a, h in [(1, 2), (2, 10), (3, 13),
                                      (4, 5), (6, 7), (8, 9)]]
    for row in rows:
        assert row["h"] <= upper[row["a"]-1]

    long = -Fraction(1, 9)
    assert trajectory(long, 10) == (1, 6)
    assert Fraction(81, 1024) * (9*Fraction(32, 81)+Fraction(1, 2048))+Fraction(1, 2048) < Fraction(3, 8)
    for a, signed_output in [(5, -1), (7, -7)]:
        center = -Fraction(3 + 2**a, 27)
        assert trajectory(center, 4) == (signed_output, 3)
    assert trajectory(Fraction(-29), 8) == (-1, 2)

    center = -Fraction(515, 27)
    h = 18
    x0 = residue(center, h)
    y0 = (19683*x0+31371)//16384
    assert 16384*y0 == 19683*x0+31371 and y0 % 3 == 0
    assert 3*19683*16 == 3*(19683*2**18//16384)
    assert ordinary(y0, 4)[0] == ordinary(x0, 18)[0]
    assert ordinary(y0, 4)[1] == 3
    assert 3**ordinary(x0, 18)[1] == (3**3)*(19683*2**18//16384)//16
    assert Fraction(19683, 16384)*Fraction(32,81)+Fraction(31371, 16384*2048) < Fraction(3,4)
    triple = dict(h=h,x0=x0,y0=y0,common=ordinary(y0,4)[0],
                  source_odds=ordinary(x0,18)[1],visitor_odds=3)

    return {"upper_minimum_by_even_offset": {"3":[3,4], "4":[4,5,6]},
            "upper_second_at_most":15,"score_two_last_residues_mod54":upper,
            "direct_rows":rows, "triple":triple}


if __name__ == "__main__":
    print(json.dumps(main(),sort_keys=True,indent=2))
