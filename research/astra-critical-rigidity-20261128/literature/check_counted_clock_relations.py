"""Check rectangular local products, primitive heights and chronological gcds."""

from fractions import Fraction
from math import gcd, lcm, prod
import json


def require(condition):
    if not condition:
        raise ArithmeticError("counted clock relation control failed")


def height(x):
    return max(abs(x.numerator), x.denominator)


def valuation(x, p):
    n, d = abs(x.numerator), x.denominator
    if not n:
        raise ValueError("valuation at zero")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def absolute_value(x, place):
    if x == 0:
        return Fraction(0)
    if not place:
        return abs(x)
    return Fraction(place) ** (-valuation(x, place))


def projective_height(values):
    den = lcm(*(x.denominator for x in values))
    nums = [int(x * den) for x in values]
    content = gcd(*nums)
    rough = content
    for p in (2, 3):
        while rough % p == 0:
            rough //= p
    return max(abs(x) for x in nums) // content, rough


def order_three(q):
    j, x = 1, 3 % q
    while x != 1:
        j += 1
        x = 3 * x % q
    return j


def rectangle(t, g, q, shear, i_max, j_max, counts):
    U = Fraction(2**t, 3**g)
    V = U**shear * 3**order_three(q)
    Z = [U**i * V**j for i in range(i_max + 1)
         for j in range(j_max + 1)]
    require(len(set(Z)) == len(Z))
    X = [z - 1 for z in Z]
    k = len(X) - 1
    cap = height(U)**i_max * height(V)**j_max
    HX, rough = projective_height(X)
    require(2**(t-1) <= HX <= 2*cap and rough % q == 0)
    pivot = min(range(len(Z)), key=lambda i: Z[i])
    Y = [z - Z[pivot] for z in Z]
    HY, yrough = projective_height(Y)
    require(HX <= HY <= 2*HX and rough == yrough)
    numerators, sx, sy = Fraction(1), Fraction(1), Fraction(1)
    reciprocal_min = Fraction(1)
    pivots = []
    for place in (0, 2, 3):
        norms = [absolute_value(z, place) for z in Z]
        s = min(range(len(Z)), key=lambda i: norms[i])
        pivots.append(s)
        wx = max(absolute_value(x, place) for x in X)
        wy = max(absolute_value(y, place) for y in Y)
        if place:
            require(wx == wy)
        sx *= wx
        sy *= wy
        reciprocal_min /= norms[s]
        for i, z in enumerate(Z):
            if i == s:
                continue
            val = absolute_value(z-Z[s], place)
            require(0 < val <= wy)
            require(val <= (1 if place else 2)*norms[i])
            numerators *= val
    require(reciprocal_min == cap)
    require(sx == HX*rough and sy == HY*rough)
    require(numerators <= 2**k * cap)
    require(numerators*q**k*HY**k <= sy**k*2**k*cap)
    counts["rectangles"] += 1
    counts["pair_difference_forms"] += 3*k
    counts["distinct_place_pivots"] += len(set(pivots)) >= 2
    counts["negative_secondary_exponents"] += shear < 0
    counts["nontrivial_projective_content"] += rough > 1


def chronological_tests(counts):
    for n in (1, 2, 3, 5, 7, 27, 703, 6171):
        qs, grades = [], []
        x, g = n, 0
        for t in range(1, 81):
            bit = x % 2
            g += bit
            x = ((1+2*bit)*x+bit)//2
            delta = abs((1 << t)-3**g)
            q = delta//gcd(delta, x-n)
            qs.append(q)
            grades.append(g)
        for i in range(3, 48, 4):
            for shift in (1, 3, 7):
                selected = [i, i+shift, i+2*shift, i+3*shift]
                D = lcm(*(qs[j] for j in selected))
                divisors = [j for j, q in enumerate(qs)
                            if D % q == 0 and q*q >= 1 << (j+1)]
                if len(divisors) < 2:
                    continue
                l = lcm(*(qs[j] for j in divisors))
                all_q = prod(qs[j] for j in divisors)
                overlaps = 1
                for a, h in enumerate(divisors):
                    for j in divisors[:a]:
                        d = gcd(qs[j], qs[h])
                        require(abs((1 << (h-j))-3**(grades[h]-grades[j])) % d == 0)
                        overlaps *= d
                require(D % l == 0 and l*overlaps >= all_q)
                counts["shared_divisor_packs"] += 1
                counts["eligible_members"] += len(divisors)


def main():
    counts = dict.fromkeys(("rectangles", "pair_difference_forms",
                           "distinct_place_pivots", "negative_secondary_exponents",
                           "nontrivial_projective_content", "shared_divisor_packs",
                           "eligible_members", "full_size_margin_parameters"), 0)
    for t, g, q in ((3, 1, 5), (4, 1, 13), (4, 2, 7), (5, 3, 5),
                    (6, 2, 5), (7, 3, 101)):
        require((2**t-3**g) % q == 0)
        for shear in (-2, -1, 0, 1):
            for i, j in ((2, 1), (3, 2), (5, 2)):
                rectangle(t, g, q, shear, i, j, counts)
    for B in range(1, 129):
        k = (64*B+1)*17-1
        for t in (16, 17, 40, 100):
            # Twice the claimed logarithmic excess, using 176Bt for A.
            require(2*k + 4*176*B*t + 4 <= k*t)
            counts["full_size_margin_parameters"] += 1
    chronological_tests(counts)
    print(json.dumps(counts, sort_keys=True))


if __name__ == "__main__":
    main()

