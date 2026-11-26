"""Exact finite checks for the two scaled swaps and rational rotation controls.

Decimal evaluations are diagnostic controls for the written regulator identities.
The displayed exact properties and the analytic arguments are independent checks.
"""

from decimal import Decimal as D, localcontext
from fractions import Fraction
from math import gcd, prod


def require(condition):
    if not condition:
        raise ArithmeticError("unit-control mismatch")


def edge(x):
    n = 3 * x + 1
    d = n & -n
    return d, n // d


def check_swaps():
    paths = ((25, 19, 29, 11), (55, 83, 125), (7, 11), (143, 215, 323, 485, 91))
    for grouped in (paths[:2], paths[2:]):
        require(prod(path[0] for path in grouped) == prod(path[-1] for path in grouped))
        require(prod(edge(x)[0] for path in grouped for x in path[:-1]) == 2**8)
        for path in grouped:
            for x, y in zip(path, path[1:]):
                require(edge(x)[1] == y)
    return 10


def check_rotation(a, m):
    require(gcd(a, m) == 1)
    den = 2**a - 3**m
    require(0 < den < 3**m)
    terms = [3 ** (m - 1 - j) * 2 ** (a * j // m) for j in range(m)]
    numerators = [sum(terms)]
    inverse = pow(a, -1, m)
    for r in range(m - 1):
        j = ((m - 1 - r) * inverse) % m
        jump = terms[j]
        require(2 * jump >= 3 ** (m - 1))
        numerators.append(numerators[-1] + jump)
    for r, x in enumerate(numerators):
        next_r = (r + a) % m
        clock = (r + a) // m
        require(2**clock * numerators[next_r] == 3 * x + den)
        require(x % 2 == 1 and den % 2 == 1)
    gap = min(b - a for a, b in zip(numerators, numerators[1:]))
    return m, Fraction(gap, den)


def rogers(t, c):
    """Real Rogers L on t < 1 (reflection reduces the Taylor argument)."""
    if t < 0:
        return -rogers(t / (t - 1), c)
    if t > D("0.5"):
        return c - rogers(1 - t, c)
    if t == 0:
        return D(0)
    power = t
    s = D(0)
    j = 1
    while power > D("1e-64"):
        s += power / (j * j)
        power *= t
        j += 1
    return s + t.ln() * (1 - t).ln() / 2


def check_decimal(x, c):
    d, y = edge(x)
    q = D(3) / d
    unit = lambda z: (D(3 * z).sqrt() + D(3 * z + 1).sqrt())
    u = unit(x)
    w = unit(y)
    xx, yy = u**-2, w**-2
    t, v = q.sqrt() * u / w, q.sqrt() / (u * w)
    s = v / q
    b = (1 - v) / (1 - t)
    err = D("1e-48")
    require(abs(b + 1 / b - (2 + D(36 * x) / (d + 3))) < err)
    L = lambda z: rogers(z, c)
    require(abs(L(yy) + L(-xx) - L(-xx * yy) + L(-s) + L(v)) < err)
    require(abs(L(t) + L(v) + L(-q / v) + L(-q / t) - L(-q)) < err)
    correction = (L(xx**2) + L(s**2)) / 2 - L(-xx * yy)
    require(correction > 0 and abs(L(s) - L(v) - L(yy) + L(xx) - correction) < err)



def check_stress(clock, c):
    d = 2**clock
    y = 10_000_001
    while (d*y-1) % 3:
        y += 2
    x = (d*y-1)//3
    require(edge(x) == (d, y))
    q = D(3)/d
    xx = (D(3*x).sqrt() + D(3*x+1).sqrt())**-2
    yy = (D(3*y).sqrt() + D(3*y+1).sqrt())**-2

    def centered(t):
        return rogers(t, c)-c if t <= 1 else c-rogers(1/t, c)

    basis = []
    total = D(0)
    for i, u in enumerate((-24, -16)):
        for r, v in enumerate((8, 16)):
            sign = (-1)**(i+r)
            k, j = (u+v)//2, (v-u)//2
            args = [q**k * xx**(eta*j) * yy**(eps*j)
                    for eta in (-1, 1) for eps in (-1, 1)]
            basis.extend((abs(t.ln()), sign*eta, u, v) for t, eta in zip(args, (-1,-1,1,1)))
            total += D(sign)/(v-u)*(sum(map(centered, args)) - centered(q**u) - centered(q**v))
    total *= -1 if q > 1 else 1
    require(0 < total < 500*max(xx, yy)**2)
    ordered = sorted(basis)
    require(ordered[0][0] < ordered[1][0] and ordered[0][3] == ordered[1][3] == 8)
    require(ordered[0][1] == -ordered[1][1])
    return total


def cubic_even_root(x, bits):
    root = 0
    for j in range(1, bits):
        if (root**3-3*root-12*x-2) % (2**(j+1)):
            root += 2**j
    require((root**3-3*root-12*x-2) % (2**bits) == 0)
    return root


def dickson(k, t, modulus=None):
    a, b = 2, t
    for _ in range(k):
        a, b = b, t*b-a
        if modulus:
            a, b = a % modulus, b % modulus
    return a


def check_cubic_fields():
    bits = 64
    count = 0
    for x in range(1, 1000, 2):
        if x % 3 == 0:
            continue
        d, _ = edge(x)
        t = cubic_even_root(x, bits)
        require((t-2) % 8 == 4)
        require((t+2) % (8*d) == 4*d)
        lead = x*(3*x+1)
        require(gcd(lead, gcd(9*(3*x+1), 27*x)) == 1)
        count += 1
    initial = cubic_even_root(1, bits)
    exponents = (1, 5, 7, 11, 13, 17, 19)
    for e in exponents:
        trace = dickson(e, 14)
        x, rem = divmod(trace-2, 12)
        require(rem == 0 and x % 2 and x % 3)
        require(cubic_even_root(x, bits) == dickson(e, initial, 2**bits))
    return count, len(exponents)

def main():
    swaps = check_swaps()
    cubic_count, shared_count = check_cubic_fields()
    rotations = [check_rotation(a, m) for a, m in ((8, 5), (65, 41), (485, 306))]
    with localcontext() as context:
        context.prec = 68
        # L(1)=2L(1/2), and Li2(1/2) has an absolutely convergent Taylor series.
        c = 2 * rogers(D("0.5"), D(0))
        probes = (*range(1, 200, 2), 341, 5461)
        for x in probes:
            check_decimal(x, c)
        context.prec = 92
        stresses = [check_stress(clock, c) for clock in range(1, 15)]
    print(f"exact_physical_swap_edges={swaps}")
    print(f"exact_dyadic_cubic_sources={cubic_count}; shared_pell_field_exponents={shared_count}; bits=64")
    print("exact_balanced_rational_periods=" + ",".join(str(m) for m, _ in rotations))
    print("sorted_gap_floors=" + ",".join(str(gap.numerator // gap.denominator) for _, gap in rotations))
    print(f"decimal_rogers_and_trace_edges={len(probes)}; tolerance=1e-48")
    print(f"decimal_positive_invariant_edges={len(stresses)}; clocks=1..14; "
          f"smallest_positive_order={min(stresses).adjusted()}")


if __name__ == "__main__":
    main()
