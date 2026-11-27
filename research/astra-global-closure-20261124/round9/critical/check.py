"""Replay the integer controls for cyclic ordering and two-sided odd paths."""

from fractions import Fraction
from math import gcd
import json


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def shortcut(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def odd_core(x):
    return x // (x & -x)


def forward(x, a):
    value = 3 * x + 1
    require(value % (2 ** (a + 1)) == 2**a, "forward exponent is inexact")
    return value // 2**a


def backward(x, a):
    value = 2**a * x - 1
    require(value % 3 == 0 and value > 0, "illegal inverse edge")
    y = value // 3
    require(y % 2 == 1, "even inverse odd site")
    return y


def grade_data():
    rev = [4, 3, 4, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    carry = 0
    for j, a in enumerate(rev):
        carry = 2**a * carry + 3**j
    require((len(rev), sum(rev), carry) == (16, 26, 49385281), "affine coefficients")
    tests = [0, 1, 2, 3, 17, 10**6 + 1, 3**40]
    for t in tests:
        s = 116582680 + 129140163 * t
        z = 181749759 + 201326592 * t
        require(z > 0 and z % 3 == 0 and z < 2 * s + 1, "smaller multiple")
        require(3**16 * z == 2**26 * s - carry, "incorrect affine row")
        x = s
        for a in rev:
            x = backward(x, a)
        require(x == z, "inverse row mismatch")
        x = z
        odd = 0
        for _ in range(26):
            odd += x % 2
            x = shortcut(x)
        require((odd, x) == (16, s), "shortcut row mismatch")
        if t % 2:
            q = (2 * s + 1) // 3
            require(3 * q == 2 * s + 1 and q % 12 == 1, "minimum parameter residue")
            x = z
            for a in reversed(rev):
                x = forward(x, a)
            require(x == s, "odd terminal mismatch")
    return {"odd_depth": len(rev), "clock": sum(rev), "carry": carry, "sampled_rows": len(tests)}


def folded_order():
    sites = ties = cuts = 0
    for s in range(1, 256, 2):
        grid = []
        for x in range(s, 8 * s, 2):
            k = int(x >= 2 * s) + int(x >= 4 * s)
            z = x * (4 >> k)
            g = 3 * z + (4 >> k)
            grid.append((z, g, odd_core(3 * x + 1)))
        grid.sort()
        require(grid[0][:2] == (4 * s, 12 * s + 4), "wrong first site")
        require(grid[-1][1] < 2 * grid[0][1], "images overlap at wrap")
        low, high = [], []
        for _, g, _ in grid:
            if g >= 16 * s:
                high.append(Fraction(g, 4))
            else:
                low.append(Fraction(g, 2))
        if low and high:
            require(max(high) < min(low), "fold exceeds one cut")
            cuts += 1
        for (z1, g1, y1), (z2, g2, y2) in zip(grid, grid[1:]):
            require(z1 < z2 and g1 <= g2, "quarter-grid order violation")
            if g1 == g2:
                require(y1 == y2, "equal lifts have different odd cores")
                ties += 1
        sites += len(grid)
    return {"odd_minima": 128, "scaled_sites": sites, "ties_with_common_odd_core": ties, "single_cuts": cuts}


def lifted_example():
    exponents = [1, 1, 2, 2, 2]
    sites = [Fraction(value, 13) for value in [283, 431, 653, 493, 373]]
    s = min(sites)
    k = [int(x >= 2 * s) + int(x >= 4 * s) for x in sites]
    p = len(k)
    b = []
    for i, (x, a) in enumerate(zip(sites, exponents)):
        j = (i + 1) % p
        require((3 * x + 1) / 2**a == sites[j], "rational edge mismatch")
        b.append(a + k[j] - k[i])
    require(b == [1, 2, 1, 2, 2], "normalized exponents")
    ranks = sorted(range(p), key=lambda j: sites[j] / 2 ** k[j])
    r = sum(e == 2 for e in b)
    for j in range(p):
        require((ranks[j] + 1) % p == ranks[(j + r) % p], "rank rotation")
    require(gcd(sum(exponents), p) == 1, "primitive ratio")
    return {"actual": exponents, "normalized": b, "bands": k, "range_ratio": str(max(sites) / s)}


def modular_obstruction():
    p, h = 5, 8
    D, u = 2**h - 3**p, 6
    require(pow(u, p, D) == 2 and pow(u, h, D) == 3, "modular parameter")
    coefficients = [4, 1, 2, 2, 2]
    value = sum(c * u ** (p - 1 - i) for i, c in enumerate(coefficients))
    bands = [{4: 0, 2: 1, 1: 2}[coefficients[(i * h) % p]] for i in range(p)]
    normal = [(i + 1) * h // p - i * h // p for i in range(p)]
    actual = [normal[i] + bands[i] - bands[(i + 1) % p] for i in range(p)]
    require(value == 422 * D and actual == [0, 1, 2, 2, 3], "relaxed counterexample")
    return {"denominator": D, "unit": u, "polynomial_value": value, "illegal_exponents": actual}


def local_minimum(L):
    f = [0] + [(3**i).bit_length() - 1 for i in range(1, L + 1)]
    b = [0] + [f[i] + 1 for i in range(1, L + 1)]
    fv = [y - x for x, y in zip(f, f[1:])]
    bv = [y - x for x, y in zip(b, b[1:])]
    m2, m3 = 2 ** (f[-1] + 1), 3**L
    c1 = sum(3 ** (L - 1 - i) * 2 ** f[i] for i in range(L))
    r2 = (2 ** f[-1] - c1) * pow(m3, -1, m2) % m2
    c2 = 0
    for i, a in enumerate(bv):
        c2 = 2**a * c2 + 3**i
    r3 = c2 * pow(2 ** b[-1], -1, m3) % m3
    s = r2 + m2 * ((r3 - r2) * pow(m2, -1, m3) % m3) + m2 * m3
    require(s % 18 == 1, "two-sided CRT minimum residue")
    require(((2 * s + 1) // 3) % 12 == 1, "two-sided minimum parameter")
    require(s % 16 == 11, "initial forward cylinder")
    recentered, original = s, 2 * s + 1
    for _ in range(4):
        recentered = shortcut(recentered)
        original = shortcut(original)
    require(recentered == shortcut(original) == 27 * (s // 16) + 20, "physical minimum meeting")
    for operation, digits in [(forward, fv), (backward, bv)]:
        x = s
        for a in digits:
            x = operation(x, a)
            require(s < x < 2 * s, "two-sided physical window escaped the first octave")
    return {"depth": L, "forward_clock": f[-1], "backward_clock": b[-1], "source_bits": s.bit_length()}


def main():
    result = {
        "protocol": "collatz-round9-critical-1",
        "quarter_grid": folded_order(),
        "actual_progression": grade_data(),
        "nonconstant_lift": lifted_example(),
        "relaxed_modular_counterexample": modular_obstruction(),
        "two_sided_ordinary_minima": [local_minimum(L) for L in [2, 3, 5, 10, 20, 40, 80]],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
