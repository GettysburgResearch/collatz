"""Integral shifted paths, literal homogeneous ceilings, and quotient obstruction."""
from fractions import Fraction
from itertools import product
from bisect import bisect_left
import json


def require(truth, message):
    if not truth:
        raise ArithmeticError(message)


def oddpart(x):
    return x // (x & -x)


def native(x):
    v = 3 * x + 1
    a = (v & -v).bit_length() - 1
    return a, v >> a


def raw_h(n, N):
    if 3 * n <= N:
        return 3 * n
    z = 3 * n + 1
    return z if oddpart(z) <= N else z + 2


def homogeneous(z, N):
    return (z & -z) * raw_h(oddpart(z), N)


def realize(word, central, modulus):
    # The inverse of 3 exists modulo the full 2-adic endpoint cylinder.
    E = 0
    B = 0
    P = 1
    for a in word:
        B = 3 * B + (1 << E)
        E += a
        P *= 3
    m = 1 << (E + 1)
    start = ((1 << E) - B) * pow(P, -1, m) % m
    y = start
    for a in word[:central]:
        y = (3 * y + 1) >> a
    if modulus > 1:
        leverage = (m >> sum(word[:central])) * 3**central
        start += m * ((-y * pow(leverage, -1, modulus)) % modulus)
    y = start
    for i, a in enumerate(word):
        if i == central:
            require(y % modulus == 0, "unit-prime central class")
        a_real, y = native(y)
        require(a_real == a, "full chronological cylinder verification")
    return start.bit_length()


def main():
    checked = admissible = lowdef = plusdef = third = 0
    grids = {N:sorted(Fraction(n, 64) * 2**j for n in range(1, N + 1, 2)
                      for j in range(19)) for N in range(1, 128, 2)}
    for x in range(3, 8192, 2):
        a, y = native(x)
        if a not in (1, 2):
            continue
        checked += 1
        for positive in (False, True):
            u = (x + (1 if positive else -1)) // 2
            v = (y + (1 if positive else -1)) // 2
            d = int(a == (2 if positive else 1))
            require((v << a) == 3 * u + d, "integer half native edge")
            require(d == u % 2, "unit-defect parity")
            for N, grid in grids.items():
                if max(oddpart(v), oddpart(u)) <= N and (not d or N < 3 * u):
                    literal = grid[bisect_left(grid, 3 * u)]
                    require(literal == (v << a) == homogeneous(u, N), "literal eligible edge")
                    admissible += 1
                    lowdef += int(not positive and d)
                    plusdef += int(positive and d)
        if x % 3:
            require(y // 3 == ((x - 1) // 2) >> (a - 1), "third delayed half")
            require((y // 3 << a) - 3 * (x // 3) == x % 3 - 1, "integer third digit")
            third += 1
    possible = {}
    for M in range(1, 13):
        triples = [v for v in product(range(-1, 2), range(-2, 2), range(-1, 2))
                   if 1 + 2 * v[1] - 3 * v[0] in (0, M)
                   and 1 + 4 * v[2] - 3 * v[1] in (0, M)]
        possible[str(M)] = triples
        if M >= 4:
            survivors = [v for v in triples if M not in (7, 11) or v[0] % M == 0]
            require(not survivors, "bounded-adjustment obstruction")
    heights = []
    for depth in (3, 9, 27, 81):
        for M in (1, 7, 11):
            heights.append(realize([2] * depth + [1, 2] + [1] * depth, depth, M))
    out = dict(ordinary_binary_edges=checked, literal_shifted_cutoff_edges=admissible,
               minus_unit_edges=lowdef, plus_unit_edges=plusdef, delayed_third_edges=third,
               offset_candidates=possible, finite_positive_window_realizations=len(heights),
               maximum_realizing_start_bits=max(heights))
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
