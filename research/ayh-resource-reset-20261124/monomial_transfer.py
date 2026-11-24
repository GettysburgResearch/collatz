"""Exact certificate transfer for finite unary string-rewriting systems.

Maps are specified by (nonnegative exponent matrix, positive constants).
A rule is (left word, right word, distinguished-strict flag).
Letter indices and coordinate indices begin at zero. Words compose left to right
as functions, so the rightmost letter acts first. Uses the standard library.
"""

from math import prod


def factor(n):
    if n < 1:
        raise ValueError("Monomial coefficients must be positive integers")
    factors = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def compose(word, maps, multiplicative):
    """Compose monomial maps, or the affine maps with the same linear parts."""
    d = len(maps[0][1])
    matrix = [[int(i == j) for j in range(d)] for i in range(d)]
    const = [1 if multiplicative else 0] * d
    for letter in reversed(word):
        m, c = maps[letter]
        if multiplicative:
            const = [c[i] * prod(val**e for e, val in zip(row, const))
                     for i, row in enumerate(m)]
        else:
            const = [c[i] + sum(e * val for e, val in zip(row, const))
                     for i, row in enumerate(m)]
        matrix = [[sum(e * matrix[k][j] for k, e in enumerate(row))
                   for j in range(d)] for row in m]
    return matrix, const


def orients(maps, rules, multiplicative):
    for left, right, strict in rules:
        mat_l, c_l = compose(left, maps, multiplicative)
        mat_r, c_r = compose(right, maps, multiplicative)
        if any(a < b for row_a, row_b in zip(mat_l, mat_r)
               for a, b in zip(row_a, row_b)):
            return False
        if any(a < b for a, b in zip(c_l, c_r)):
            return False
        if strict and c_l[0] <= c_r[0]:
            return False
    return True


def compile_to_affine(maps, rules):
    """Return the first integer prime-log scale and its same-dimension affine maps."""
    if not maps or not maps[0][1]:
        raise ValueError("A nonempty alphabet and positive dimension are required")
    d = len(maps[0][1])
    for matrix, coefficients in maps:
        if len(matrix) != d or len(coefficients) != d or any(len(row) != d for row in matrix):
            raise ValueError("Matrix and coefficient dimensions must agree")
        if any(type(n) is not int or n < 0 for row in matrix for n in row):
            raise ValueError("Exponents must be nonnegative integers")
        if any(type(n) is not int or n < 1 for n in coefficients):
            raise ValueError("Coefficients must be positive integers")
    rules = list(rules)
    if not orients(maps, rules, True):
        raise ValueError("The supplied monomial interpretation does not orient the rules")
    factors = {n: factor(n) for _, coeff in maps for n in coeff}
    primes = {p for fs in factors.values() for p in fs}
    k = 1
    while True:
        weights = {p: (p**k).bit_length() - 1 for p in primes}
        integer_charge = {n: sum(weights[p] * e for p, e in fs.items())
                          for n, fs in factors.items()}
        affine = [(m, [integer_charge[n] for n in c]) for m, c in maps]
        if orients(affine, rules, False):
            return k, affine
        k *= 2


if __name__ == "__main__":
    nonlinear = [[2, 1], [0, 0]]
    identity = [[1, 0], [0, 1]]
    maps = [(nonlinear, [3, 5]), (nonlinear, [2, 5]),
            (identity, [6, 1]), (identity, [2, 1]), (identity, [3, 1])]
    # The last pair has equal constants by 6=2*3, in two independent contexts.
    rules = [([0], [1], True), ([2], [3, 4], False),
             ([3, 4], [2], False), ([2, 0], [2, 1], True)]
    scale, affine = compile_to_affine(maps, rules)
    if scale != 2 or not orients(affine, rules, False):
        raise RuntimeError("The compiled affine control failed")
    roundtrip = [(m, [2**n for n in shifts]) for m, shifts in affine]
    if not orients(roundtrip, rules, True):
        raise RuntimeError("The monomial round-trip failed")
    try:
        compile_to_affine(maps, [([1], [0], False)])
    except ValueError:
        pass
    else:
        raise AssertionError("A reversed strict coefficient inequality was accepted")
    # Independent exact check of the boundary's effect on a carry defect.
    P = [[1, 1], [0, 1]]
    Q = [[1, 0], [0, 2]]
    C = [[1, 2], [1, 2]]
    D = [[1, 0], [0, 0]]
    J = [[0, 1], [0, 0]]
    letters = {s: (m, [0, 0]) for s, m in zip("abcdefg", [P, P, C, D, Q, Q, Q])}
    equations = "ad:d bd:gd ae:ea af:eb ag:fa be:fb bf:ga bg:gb ce:cb cf:caa cg:cab"
    for n, equation in enumerate(equations.split()):
        left, right = equation.split(":")
        def product(w):
            mats = [letters[ch] for ch in w]
            return compose(range(len(mats)), mats, False)[0]
        a, b = product(left), product(right)
        differences = [[a[i][j] - b[i][j] for j in range(2)] for i in range(2)]
        if min(min(row) for row in differences) < 0 or (2 <= n < 8 and differences != J):
            raise RuntimeError("The full-system matrix control failed on " + equation)
    jcs, _ = compose([0, 1, 0], [(J, [0, 0]), (C, [0, 0])], False)
    jsquared, _ = compose([0, 0], [(J, [0, 0])], False)
    if jcs != J or jsquared != [[0, 0], [0, 0]]:
        raise RuntimeError("The boundary did not reproduce the carry defect")
    print("Exact nonlinear, equality, round-trip, negative and boundary controls passed; scale =", scale)
