"""Exact finite certificates for the cubic-descent four-power theorem.

Uses only Python integers and fractions.  The cone check is a finite part
of the argument, not an implementation of the Subspace Theorem or a
search for arbitrary Collatz cycles.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from math import gcd, lcm


C = F(485, 306)
GAMMA = C - 1
UNIT, *GAINS = [tuple(F(i == j) for i in range(4)) for j in range(4)]


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, x):
    return tuple(v * x for v in a)


def sub(a, b):
    return add(a, scale(b, -1))


def total(rows):
    out = (F(0),) * 4
    for row in rows:
        out = add(out, row)
    return out


def integral(row):
    denominator = lcm(*(x.denominator for x in row))
    result = tuple(int(x * denominator) for x in row)
    common = 0
    for x in result:
        common = gcd(common, abs(x))
    return tuple(x // (common or 1) for x in result)


def cross(x, y):
    return (x[1] * y[2] - x[2] * y[1],
            x[2] * y[0] - x[0] * y[2],
            x[0] * y[1] - x[1] * y[0])


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


@lru_cache(maxsize=8192)
def vertex(rows):
    """An exact feasible vertex, or None, for a bounded closed polytope.

    Rows mean r[0] + sum(r[i+1] * x[i]) >= 0.  All callers retain
    the bounded domain constructed by domain_and_tests.  Every nonempty
    bounded polytope, including a lower-dimensional one, has a vertex.
    """
    for a, b, c in combinations(rows, 3):
        u = cross(b[1:], c[1:])
        v = cross(c[1:], a[1:])
        w = cross(a[1:], b[1:])
        den = dot(a[1:], u)
        if not den:
            continue
        nums = tuple(-a[0] * i - b[0] * j - c[0] * k
                     for i, j, k in zip(u, v, w))
        if den < 0:
            den = -den
            nums = tuple(-x for x in nums)
        if all(den * r[0] + dot(r[1:], nums) >= 0 for r in rows):
            return nums, den
    return None


def value_numerator(row, point):
    nums, den = point
    return den * row[0] + dot(row[1:], nums)


def domain_and_tests(floors, descent=3):
    """A floor 2 means an actual square; floor 3 allows any exponent >=3.

    The variable for a floor-three factor is its total homogeneous gain
    divided by three.  Such a factor is never a comparison coordinate.
    """
    heights = [UNIT]
    costs = []
    for e, gain in zip(floors, GAINS):
        costs.append(sub(heights[-1], scale(gain, (e - C) / GAMMA)))
        heights.append(add(heights[-1], scale(gain, e)))
    floor = 1 - descent + descent * (descent - 1) * C / GAMMA
    domain = GAINS + costs + [sub(heights[-1], scale(UNIT, floor))]
    drop = scale(sub(heights[-1], UNIT), F(1, descent))
    p_cost = add(drop, scale(UNIT, 1 - (descent - 1) * C / GAMMA))

    tests = []
    for i in range(3):
        if floors[i] != 2:
            continue
        for j in range(i + 1, 3):
            if floors[j] != 2:
                continue
            for k in (1, 2):
                savings = [scale(GAINS[i], k), GAINS[j],
                           scale(heights[i + 1], 1 / C)]
                charge = add(scale(costs[i], k), costs[j])
                margins = [sub(saving, charge) for saving in savings]
                if k == 2:
                    margins += [sub(saving, GAINS[i]) for saving in savings]
                margins.append(sub(scale(GAINS[j], 2 / GAMMA), costs[i]))
                tests.append(((i, j, k), tuple(map(integral, margins))))

        for k in (1, 2):
            savings = [scale(GAINS[i], k), drop,
                       scale(heights[i + 1], 1 / C)]
            charge = add(scale(costs[i], k), p_cost)
            margins = [sub(saving, charge) for saving in savings]
            if k == 2:
                margins += [sub(saving, GAINS[i]) for saving in savings]
            divisor = scale(add(scale(UNIT, C / GAMMA), drop), descent - 1)
            margins.append(sub(divisor, costs[i]))
            tests.append(((i, "descent", k), tuple(map(integral, margins))))
    return tuple(map(integral, domain)), tuple(tests)


def uncovered_point(rows, tests):
    """Search the complement of the union of strict comparison regions.

    At a feasible vertex choose a comparison for which every margin is
    positive.  Its failure is the union of the closed halfspaces -m >=0.
    Recurse on all of them.  Empty leaves are certified by exact vertex
    enumeration.  An uncovered vertex is returned as a counterexample.
    """
    nodes = 0

    def visit(constraints, candidates):
        nonlocal nodes
        nodes += 1
        point = vertex(constraints)
        if point is None:
            return None
        scores = [(min(value_numerator(r, point) for r in margins), idx)
                  for idx, (_, margins) in enumerate(candidates)]
        best, index = max(scores, default=(0, 0))
        if best <= 0:
            return point
        _, margins = candidates[index]
        remaining = candidates[:index] + candidates[index + 1:]
        for margin in margins:
            negative = tuple(-x for x in margin)
            result = visit(constraints + (negative,), remaining)
            if result is not None:
                return result
        return None

    return visit(rows, tests), nodes


def check_scalar_bounds():
    require(3**306 < 2**485, "outward logarithm bound")
    amplitude = 1 + 2 * GAMMA / (2 - C)
    amplitude3 = 1 + 3 * GAMMA / (3 - C)
    floor = 6 * C / GAMMA - 2
    require(amplitude3**3 < floor, "three nonsquare rises cannot reach cube")
    require(amplitude * amplitude3 < floor, "two rises must both be squares")
    excess = amplitude**2 - floor
    first_gain = (floor / amplitude - 1) / 2
    first_cost = 1 - (2 - C) * first_gain / GAMMA
    descent_cost = (amplitude**2 - 1) / 3 + 1 - 2 * C / GAMMA
    internal_height = (1 - excess * (1 + GAMMA / 2)) / C
    require(0 < excess < F(1, 3), "small total extra descending deficit")
    require(internal_height > F(1, 3), "positive intermediate height")
    require(first_gain > internal_height, "first leading-term error")
    require((floor - 1) / 3 > internal_height, "cube leading-term error")
    require(internal_height - first_cost - descent_cost > F(1, 5),
            "strict two-rise Subspace-Theorem margin")
    require(2 * C / GAMMA > first_cost, "two-rise divisibility contradiction")
    return {"extra_drop_upper": str(excess),
            "comparison_margin_lower": str(internal_height-first_cost-descent_cost)}


def numerator(word):
    a, b, c = 1, 1, 0
    for parity in word:
        c = (3 if parity else 1) * c + (b if parity else 0)
        a *= 3 if parity else 1
        b *= 2
    return a, b, c


def replay_arithmetic():
    count = 0
    for width in range(1, 7):
        for word in product((0, 1), repeat=width):
            a, b, c = numerator(word)
            for e in (2, 3, 4):
                full = word * e
                aa, bb, cc = numerator(full)
                residue = (-cc * pow(aa, -1, bb)) % bb
                x = residue + bb
                z = x
                for parity in full:
                    require(z % 2 == parity, "physical parity replay")
                    z = (3 * z + 1) // 2 if parity else z // 2
                before = (b - a) * x - c
                after = (b - a) * z - c
                require(b**e * after == a**e * before, "endpoint brackets")
                require(before % b**e == 0, "starting divisibility")
                require(after % a**e == 0, "ending divisibility")
                m = abs(before) // b**e
                require(m > 0, "chosen source avoids a root fixed point")
                geometric = sum(a**(e-1-i) * b**i for i in range(e))
                require(abs(z-x) == m * geometric, "geometric displacement")
                require((z > x) == (a > b), "direction of repeated block")
                count += 1
    return count


def main():
    print("scalar bounds:", check_scalar_bounds())
    total_nodes = 0
    for floors in product((2, 3), repeat=3):
        rows, tests = domain_and_tests(floors)
        if floors == (3, 3, 3):
            require(vertex(rows) is None, "all nonsquares domain is empty")
            print(floors, "empty height domain")
            continue
        counterexample, nodes = uncovered_point(rows, tests)
        require(counterexample is None, f"uncovered cubic-descent cone {floors}")
        total_nodes += nodes
        print(floors, "covered; exact recursion nodes:", nodes)

    rows, tests = domain_and_tests((2, 2, 2), descent=2)
    point = ((5, 5, 10), 10)  # g = (1/2, 1/2, 1), an abstract cone point.
    require(all(value_numerator(r, point) >= 0 for r in rows),
            "square-descent negative control is feasible")
    require(all(any(value_numerator(r, point) <= 0 for r in margins)
                for _, margins in tests),
            "square-descent point must escape every comparison")
    # Mutation control: with every comparison removed, the actual cubic
    # domain is nonempty and the covering checker must return a witness.
    cube_rows, _ = domain_and_tests((2, 2, 2))
    witness, _ = uncovered_point(cube_rows, ())
    require(witness is not None, "empty-comparison mutation was rejected")
    print("negative controls: square-descent witness retained; missing comparisons rejected")
    print("ordinary powered-block arithmetic replays:", replay_arithmetic())
    print("PASS: seven cubic-descent cones; total recursion nodes:", total_nodes)


if __name__ == "__main__":
    main()
