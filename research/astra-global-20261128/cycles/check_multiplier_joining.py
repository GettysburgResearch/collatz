"""Finite native affine-line mixtures, residue intersections and parity brackets."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def run(t, n):
    grade = 0
    for _ in range(t):
        grade += n % 2
        n = step(n)
    return n, grade


def parity_word(t, n):
    out = 0
    for i in range(t):
        out += (n % 2) << i
        n = step(n)
    return out


def intersections():
    checks = 0
    for q in (2, 4, 8, 16):
        for a, c in product(range(1, q, 2), repeat=2):
            g = gcd(a - c, q)
            for b, d in product(range(q), repeat=2):
                actual = sum((a*x+b-c*x-d) % q == 0 for x in range(q))
                require(actual == (g if (d-b) % g == 0 else 0), "affine intersection count")
                checks += 1
    return checks


def native_mixtures():
    direct_tests = cells = 0
    for A, a, B, b in ((1, 0, 5, 0), (7, 2, 13, 5), (5, 8, 7, 1)):
        for m in range(8):
            for k in range(1, 6):
                q = 2**k
                line_count, slope_count, direct, predicted = Counter(), Counter(), Counter(), Counter()
                for start in range(2**m):
                    x, xgrade = run(m, A * start + a)
                    y, ygrade = run(m, B * start + b)
                    first_slope = A * 3**xgrade
                    second_slope = B * 3**ygrade
                    slope = second_slope * pow(first_slope, -1, q) % q
                    intercept = (y-slope*x) % q
                    line_count[slope, intercept] += 1
                    slope_count[slope] += 1
                    for u in range(q):
                        n = start + 2**m * u
                        xx, gg = run(m, A*n+a)
                        yy, hh = run(m, B*n+b)
                        require((gg, hh) == (xgrade, ygrade), "fresh tail preserves grades")
                        require((xx, yy) == (x + first_slope*u, y + second_slope*u),
                                "native two-coordinate affine tail")
                        direct[xx % q, yy % q] += 1
                        direct_tests += 1
                for (slope, intercept), multiplicity in line_count.items():
                    for x in range(q):
                        predicted[x, (slope*x+intercept) % q] += multiplicity
                require(predicted == direct, "complete raw native pair law")
                exact = sum(count**2 for count in direct.values())
                energy_upper = sum(n1*n2*gcd(a1-a2, q)
                                   for a1, n1 in slope_count.items()
                                   for a2, n2 in slope_count.items())
                require(exact <= energy_upper, "slope-only collision upper")
                by_coalescence = sum(slope_count.values())**2
                for j in range(1, k+1):
                    coarse = Counter()
                    for slope, count in slope_count.items():
                        coarse[slope % (2**j)] += count
                    by_coalescence += 2**(j-1) * sum(count**2 for count in coarse.values())
                require(by_coalescence == energy_upper, "exact dyadic direction-shell identity")
                words = {parity_word(k, x) for x in range(q)}
                require(len(words) == q, "native word-residue bijection")
                cells += 1
    return direct_tests, cells


def common_triples():
    cases = 0
    for a, c in product(range(1, 8, 2), repeat=2):
        for b, d in product(range(8), repeat=2):
            successful = 0
            for u in range(4):
                x, y = a*u+b, c*u+d
                any_common = False
                for _ in range(3):
                    any_common |= (x-y) % 2 == 0
                    x, y = step(x), step(y)
                successful += any_common
            require(successful >= 2, "native three-date common-parity bound")
            cases += 1
    return cases


def rank(vectors):
    basis = {}
    for row in vectors:
        work = [Fraction(v) for v in row]
        for pivot in sorted(basis):
            if work[pivot]:
                factor = work[pivot]
                work = [x-factor*y for x, y in zip(work, basis[pivot])]
        for pivot, val in enumerate(work):
            if val:
                basis[pivot] = [x/val for x in work]
                break
    return len(basis)


def rank_supports():
    checked = 0
    for size in (2, 3, 4):
        vectors = [(1, *v) for v in product((-1, 1), repeat=size-1)]
        for mask in range(1, 1 << len(vectors)):
            support = [v for i, v in enumerate(vectors) if mask & (1 << i)]
            if any(len({v[i]*v[j] for v in support}) == 1
                   for i in range(size) for j in range(i)):
                continue
            require(size <= 2**(rank(support)-1), "sign-support rank bound")
            checked += 1
    return checked


if __name__ == "__main__":
    tests, cases = native_mixtures()
    print(json.dumps({
        "exact_all_line_intersections": intersections(),
        "native_tail_pairs": tests,
        "native_mixture_and_collision_cases": cases,
        "common_parity_triple_prefix_cases": common_triples(),
        "nondegenerate_sign_supports": rank_supports(),
        "scope": "finite native lines, modular incidences, collision energies, complete parity coding and bracket controls"
    }, indent=2, sort_keys=True))
