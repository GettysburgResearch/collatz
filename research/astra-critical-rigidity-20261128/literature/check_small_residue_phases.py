"""Exact controls for the lifting, phase-alias and ordinary-source identities."""

from collections import Counter
from fractions import Fraction
from math import gcd


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def split(value):
    if value == 0:
        raise ValueError("need a nonzero primitive part")
    a = b = 0
    while value % 2 == 0:
        a += 1
        value //= 2
    while value % 3 == 0:
        b += 1
        value //= 3
    return a, b, value


def native(value):
    odd = value.numerator % 2
    return odd, (3 * value + 1) / 2 if odd else value / 2


def residues(stats):
    """The line hypothesis is tested explicitly, without any asymptotic cutoff."""
    for length in range(4, 22):
        for grade in range(1, length + 1):
            determinant = abs(2**length - 3**grade)
            for divisor in (1, 5, 7, 11):
                if determinant % divisor:
                    continue
                q = determinant // divisor
                if q <= 2:
                    continue
                for a in range(-length, length + 1):
                    if a * grade % length:
                        continue
                    b = -a * grade // length
                    multiplier = pow(2, a, q) * pow(3, b, q) % q
                    for u in (-13, -7, -5, -1, 1, 5, 7, 13):
                        v = multiplier * u % q
                        if 2 * v > q:
                            v -= q
                        if not v or gcd(v, 6) != 1 or abs(v) > 29:
                            continue
                        stats["collinear_signed_returns"] += 1
                        for k in range(1, 9):
                            m = (2 * k * a + length) // (2 * length)
                            aa = k * a - m * length
                            bb = k * b + m * grade
                            scaled = Fraction(2) ** aa * Fraction(3) ** bb
                            left = scaled.numerator * u**k
                            right = scaled.denominator * v**k
                            require((left-right) % q == 0, "reduced congruence")
                            if abs(left) + abs(right) >= q:
                                continue
                            require(left == right and aa == bb == 0, "integral lift")
                            require(abs(u) == abs(v), "unsigned primitive lifts")
                            stats["short_power_lifts"] += 1
                            if k == 1:
                                require(u == v and a == m*length, "signed single lift")
                                stats["signed_single_lifts"] += 1
                            if u == -v:
                                stats["necessary_sign_ambiguities"] += 1
                            break


def references(stats):
    for n in [1, 2, 3, 7, 15, 27, 31, 41, 55, 63, 73, 97, 129, 255, 703, 871]:
        states, grades = [n], [0]
        for _ in range(40):
            x = states[-1]
            bit = x % 2
            states.append((3*x + 1)//2 if bit else x//2)
            grades.append(grades[-1]+bit)
        for t in range(2, 41):
            x, g = states[t], grades[t]
            if g == 0 or x == n:
                continue
            D = 2**t - 3**g
            common = gcd(abs(D), abs(x-n))
            q = abs(D) // common
            if q == 1:
                continue
            d = (1 if D > 0 else -1) * (x-n) // common
            z = Fraction(2**t*x - 3**g*n, D)
            first = z
            stats["ordinary_nonreturns"] += 1
            if z < 0:
                stats["negative_closures"] += 1
            for i in range(t + 1):
                require(z.denominator == q, "full phase denominator")
                u, h = z.numerator, grades[i]
                scalar = 2**(t-i) * 3**h * d
                require(u - q*states[i] == scalar, "actual cross-error")
                for v in (1, 2, 3, 5):
                    e2, e3, part = split(v*d)
                    guards = i > e2 and g-h > e3
                    for k in (-2, -1, 0, 1, 2):
                        a = t-i+e2+k*t
                        b = h+e3-k*g
                        if min(a, b) < 0:
                            continue
                        error = part * 2**a * 3**b
                        rr, rem = divmod(v*u-error, q)
                        require(rem == 0, "feasible full-lap reference")
                        if guards:
                            require(k == 0 and rr == v*states[i], "two strict guards")
                            stats["guarded_exact_aliases"] += 1
                        if k:
                            require(rr != v*states[i], "distinct feasible endpoint lap")
                            stats["nonzero_lap_aliases"] += 1
                    for rr in (-7, -1, 0, 1, 2, 3, 5, 11):
                        error = v*u-rr*q
                        if error == 0:
                            continue
                        s2, s3, ep = split(error)
                        a = t-i+e2-s2
                        b = h+e3-s3
                        require((pow(2,a,q)*pow(3,b,q)*part-ep) % q == 0,
                                "stripped physical congruence")
                        if a*g != -b*t or ep != part or a % t:
                            continue
                        k = -a//t
                        require(b == k*g, "signed period vector")
                        exact = Fraction(v*scalar) * Fraction(2**t, 3**g)**k
                        require(exact == error, "reconstructed arbitrary reference")
                        if guards:
                            require(rr == v*states[i], "anchored arbitrary reference")
                        stats["classified_reference_candidates"] += 1
                if i < t:
                    bit, z = native(z)
                    require(bit == states[i] % 2, "signed native parity")
            require(z == first, "closure recurrence")


if __name__ == "__main__":
    counts = Counter()
    residues(counts)
    references(counts)
    for name in (
        "collinear_signed_returns", "short_power_lifts", "signed_single_lifts",
        "necessary_sign_ambiguities", "ordinary_nonreturns", "negative_closures",
        "guarded_exact_aliases", "nonzero_lap_aliases", "classified_reference_candidates",
    ):
        require(counts[name] > 0, name)
        print(f"{name}={counts[name]}")
