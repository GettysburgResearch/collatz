"""Integer Fourier-support and symbolic-divisor checks for symbol dilations."""

from collections import Counter, defaultdict
from functools import cache
from itertools import product
from math import gcd, lcm, prod

from check_transport import divisors, numerator, require, rotate


def polynomial_divmod(f, g):
    """Little-endian integer coefficients, with a monic divisor."""
    require(g[-1] == 1, "monic divisor")
    f = list(f)
    quotient = [0] * max(0, len(f) - len(g) + 1)
    while len(f) >= len(g):
        k = len(f) - len(g)
        lead = f[-1]
        quotient[k] = lead
        for i, coefficient in enumerate(g):
            f[i + k] -= lead * coefficient
        f.pop()
    return tuple(quotient), tuple(f)


@cache
def cyclotomic(d):
    f = (-1,) + (0,) * (d - 1) + (1,)
    for j in range(1, d):
        if d % j == 0:
            f, rem = polynomial_divmod(f, cyclotomic(j))
            require(not any(rem), "cyclotomic division")
    return f


def homogeneous(coeffs, x, y):
    degree = len(coeffs) - 1
    return sum(c * x ** i * y ** (degree - i) for i, c in enumerate(coeffs))


def support(word):
    n, u = len(word), sum(word)
    g = gcd(n, u)
    N, U = n // g, u // g
    cut = next(i for i in range(n) if word[i] and not word[i-1])
    word = rotate(word, cut)
    remaining = u
    levels = defaultdict(list)
    for i, bit in enumerate(word):
        if bit != word[i-1]:
            level = U * i + N * remaining
            sign = 1 if bit else -1
            levels[level].append((i, sign))
        remaining -= bit
    arrays = []
    for corners in levels.values():
        array = [0] * g
        origin = corners[0][0]
        for site, sign in corners:
            require((site - origin) % N == 0, "level lattice")
            slot = (site - origin) // N % g
            require(array[slot] == 0, "slot collision")
            array[slot] = sign
        arrays.append(array)
    degrees = [d for d in range(1, g + 1) if g % d == 0]
    survivors = [d for d in degrees
                 if any(any(polynomial_divmod(row, cyclotomic(d))[1]) for row in arrays)]
    require(1 in survivors, "positive top level")
    return g, N, U, survivors, [d for d in degrees if d not in survivors]


def verify_template(word):
    n = len(word)
    g, N, U, surviving, missing = support(word)
    fundamental = next(h for h in range(1, n + 1) if rotate(word, h) == word)
    require(fundamental == N * lcm(*surviving), "exact stabilizer")
    degree = sum(len(cyclotomic(d)) - 1 for d in surviving)
    for ell in (1, 2, 3):
        dilated = tuple(bit for bit in word for _ in range(ell))
        raw, cancelled, denominator = divisors(dilated)
        x, y = 2 ** (ell * N), 3 ** (ell * U)
        base = prod(homogeneous(cyclotomic(d), x, y) for d in missing)
        residual = prod(homogeneous(cyclotomic(d), x, y) for d in surviving)
        require(raw == base * residual and cancelled % base == 0, "symbolic divisor")
        # Cut at a run boundary for the actual corner polynomial.
        cut = next(i for i in range(n) if word[i] and not word[i-1])
        cut_word = rotate(dilated, cut * ell)
        coef = numerator(cut_word)
        require(coef % base == 0 and residual // gcd(residual, coef // base) == denominator,
                "exact residual denominator")
    return degree, g


def main():
    stats = Counter()
    nontrivial = []
    for n in range(2, 15):
        for word in product(range(2), repeat=n):
            if not 0 < sum(word) or 3 ** sum(word) >= 1 << n:
                continue
            rotations = {rotate(word, h) for h in range(n)}
            if min(rotations) != word:
                continue
            degree, g = verify_template(word)
            stats["all"] += 1
            if len(rotations) == n:
                stats["primitive"] += 1
                if degree < g:
                    stats["primitive with cancellation"] += 1
                    if len(nontrivial) < 8:
                        nontrivial.append(("".join(map(str, word)), degree, g))
    sample = tuple(map(int, "10110100"))
    g, _, _, surviving, missing = support(sample)
    require((g, surviving, missing) == (4, [1, 4], [2]), "three-run example")
    print("positive necklaces of lengths 2 through 14", dict(stats))
    print("first primitive templates with cancellation", nontrivial)
    print("10110100 exact limiting exponent 3/4")


if __name__ == "__main__":
    main()
