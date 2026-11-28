"""Exact controls for finite series boundaries, triple births and cube collisions."""

import json
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, gcd

import sympy as sp


def require(ok, label):
    if not ok:
        raise ArithmeticError(label)


T = sp.symbols("T")


def poly(expr):
    return sp.Poly(expr, T, domain=sp.QQ)


def series_fixture(exponents, data, irreducibles):
    """Verify actual P(E)y=0 and all leftover root multiplicities."""
    P = poly(exponents)
    w, n = P.degree(), len(data)
    require(all(sum(P.nth(j) * data[t + j] for j in range(w + 1)) == 0
                for t in range(n - w)), "actual finite recurrence")
    D = sp.Poly.from_list(list(reversed(P.all_coeffs())), T, domain=sp.QQ)
    Y = sp.Poly.from_list(data[::-1], T, domain=sp.QQ)
    total = D * Y
    U = poly(sum(total.nth(i) * T**i for i in range(w)))
    V = poly(sum(total.nth(n + i) * T**i for i in range(w)))
    require(total == U + poly(T**n) * V, "two integer boundaries")
    G = sp.gcd(D, sp.gcd(U, V))
    remain = D.exquo(G).monic()
    require(remain == poly(irreducibles).monic(), "effective factor")
    checked = []
    for F, multiplicity in remain.factor_list()[1]:
        e = 0
        Ud, Vd = U, V
        while Ud.rem(F).is_zero:
            require(Vd.rem(F).is_zero, "equal boundary order")
            Ud, Vd = Ud.diff(), Vd.diff()
            e += 1
        require(not Vd.rem(F).is_zero and
                (Ud + poly(T**n) * Vd).rem(F).is_zero,
                "original-boundary derivative identity")
        checked.append(dict(root_factor=str(F.as_expr()),
                            effective_multiplicity=multiplicity,
                            differentiated=e))
    return dict(length=n, stencil_degree=w,
                nonzero_coefficients=len(P.terms()), roots=checked)


def calendar(p, h, cut, v, width):
    """Return all one-, two- and three-edge birth checks in an exact phase mesh."""
    # z in [v,cut] may have either tag. Outside that arc the entire row is
    # constant; include all W adjacent unwrapped positions at the seam.
    require(gcd(p, h) == 1 and 2 * h > p, "transitive winding")
    active = []
    forced_two = []
    for r in range(p):
        row = set()
        for j in range(width + 1):
            shift, rr = divmod(r + j, p)
            tags = {1} if rr < v else {2} if rr > cut else {1, 2}
            row.update((c << shift) for c in tags)
        require(row <= {1, 2}, "seam register")
        active.append(len(row) == 2)
        forced_two.append(row == {2})
    def images(r, value):
        rr = (r + h) % p
        div = 2 if r + h < p else 4
        result = set()
        for d in (range(-3, 4) if active[r] else (0,)):
            q, rem = divmod(3 * value + d, div)
            if not rem and (active[rr] or q % (4 if forced_two[rr] else 2) == 0):
                result.add(q)
        return result

    births = traces = 0
    for r in range(p):
        one, two, three = [(r + i * h) % p for i in (1, 2, 3)]
        for h1 in images(r, 0) - {0}:
            births += 1
            require(abs(h1) == 1 and active[r] and active[one], "birth")
            for h2 in images(one, h1):
                require(h2 in {0, h1}, "second height")
                for h3 in images(two, h2):
                    require(h3 == 0 and forced_two[three], "third height")
                    require(100 * max(one, two) < 90 * p, "excluded high arc")
                    traces += 1
    return dict(p=p, h=h, v=v, cut=cut, span=width,
                signed_births=births, complete_traces=traces)


def cube_check(k):
    words = list(product((0, 1), repeat=k))
    # Distinct coordinates share one source law; positivity need not factor.
    cases = 0
    for mask in range(1, 1 << len(words)):
        support = [w for i, w in enumerate(words) if mask >> i & 1]
        n = len(support)
        freq = Counter(tuple(x + y + z for x, y, z in zip(a, b, c))
                       for a, b, c in product(support, repeat=3))
        collision = sum(v * v for v in freq.values())
        require(collision * 64**k >= n**6 * 20**k, "cube symmetrization")
        if n == len(words):
            require(collision * 64**k == n**6 * 20**k, "uniform equality")
        # Every length-three unordered multiset is present, including repetitions.
        if len(freq) == comb(n + 2, 3):
            require(collision <= 6 * n**3, "B3 collision upper bound")
        cases += 1
    return dict(coordinates=k, nonempty_uniform_supports=cases)


if __name__ == "__main__":
    orbit = [1, -1, 2, -2]
    data = [100 + 2 * j + orbit[j % 4] for j in range(106)]
    n = 78
    # Doubling mode absent; repeated factor partially canceled before evaluation.
    roots = [series_fixture((T - 1)**3 * (T + 1)**2 *
                            (T*T + 1)**2 * (T - 2), data,
                            (T - 1)**2 * (T + 1) * (T*T + 1))]
    # The reciprocal boundary roots 2 and 1/2 both survive at multiplicity
    # two in separate exponential-height arrays, each tested before gcd division.
    roots.append(series_fixture((2*T - 1)**3 * (T - 2)**2,
                                [(j + 5) * 2**(n - j) for j in range(n)],
                                (T - 2)**2))
    roots.append(series_fixture((T - 2)**3 * (2*T - 1)**2,
                                [(j + 5) * 2**j for j in range(n)],
                                (2*T - 1)**2))
    # A normalized constant grid would satisfy the sparse torsion stencil,
    # highlighting the independent necessity of the exponential rank shape.
    roots.append(series_fixture((T - 1)*(T - 3), [73] * 66, T-1))
    base = [(306, 179), (665, 389), (15601, 9126)]
    cases = []
    for p, h in base:
        for extra in (Fraction(0), Fraction(1, 100), Fraction(7, 100),
                      Fraction(3, 20)):
            v = p // 100
            cut = v + h + (p * extra.numerator) // extra.denominator
            cases.append(calendar(p, h, cut, v, max(1, p // 1000)))
    print(json.dumps(dict(boundary_polynomials=roots, calendar=cases,
                          cube=[cube_check(i) for i in (1, 2, 3)]), indent=2))
