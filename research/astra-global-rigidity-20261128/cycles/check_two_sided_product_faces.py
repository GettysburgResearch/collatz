"""Finite, exact controls for TWO_SIDED_PRODUCT_FACES. No symbolic root theorem is assumed."""

from fractions import Fraction
from itertools import combinations_with_replacement


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def valuation2(value):
    value = Fraction(value)
    if not value:
        return 10**9

    def order(x):
        x = abs(x)
        return (x & -x).bit_length() - 1

    return order(value.numerator) - order(value.denominator)


def binomial_half(degree):
    coefficients = [Fraction(1)]
    for j in range(1, degree + 1):
        coefficients.append(coefficients[-1] * (Fraction(1, 2) - j + 1) / j)
    return coefficients


def root_truncations():
    # Ramified graph Z^2 = u v(1+u+v). After taking square roots of both
    # coordinates, the two formal branches contain sqrt(1+u+v).
    count = 0
    for degree in range(1, 11):
        coeffs = binomial_half(degree)
        square = [Fraction(0) for _ in range(2 * degree + 1)]
        for i, left in enumerate(coeffs):
            for j, right in enumerate(coeffs):
                square[i + j] += left * right
        require(square[:degree + 1] == [1, 1] + [0] * (degree - 1),
                (degree, "formal low-degree product"))
        for n in range(9, 32, 2):
            for sign in (1, -1):
                t = Fraction(2) ** (sign * n)
                u, v = 2 * t, t * t
                w1, w2 = Fraction(2) ** ((1 + sign * n) // 2), t
                require(w1 * w1 == u and w2 * w2 == v, (n, sign, "cover"))
                root = w1 * w2 * (1 + t)
                require(root * root == u * v * (1 + u + v), (n, sign, "root"))
                approximation = w1 * w2 * sum(
                    c * (u + v) ** j for j, c in enumerate(coeffs))
                error = root - approximation
                if sign < 0:
                    # The real binomial series alternates from order one onward.
                    require(abs(error) <= w1 * w2 * (u + v) ** (degree + 1),
                            (degree, n, "real truncation"))
                else:
                    # 2-adic denominators of binomial(1/2,j) divide 2^(2j).
                    expected = valuation2(w1 * w2) + (degree + 1) * (n - 1)
                    require(valuation2(error) >= expected, (degree, n, "dyadic truncation"))
                count += 1
    return count


def ordinary_backwards():
    comparisons = 0
    for source in range(3, 304, 2):
        states = [source]
        clocks = []
        for _ in range(5):
            numerator = 3 * states[-1] + 1
            exponent = valuation2(numerator)
            clocks.append(exponent)
            states.append(numerator >> exponent)
        affine = [(Fraction(1), Fraction(0))]
        for exponent in reversed(clocks):
            slope, offset = affine[-1]
            affine.append((2**exponent * slope / 3, (2**exponent * offset - 1) / 3))
        affine.reverse()
        roots = [-offset / slope for slope, offset in affine]
        require(all(x > y for x, y in zip(roots, roots[1:])), (source, "root ordering"))
        require([slope * states[-1] + offset for slope, offset in affine] == states,
                (source, "true terminal"))
        for multiset in combinations_with_replacement(range(6), 3):
            physical = 1
            frozen = Fraction(1)
            for i in multiset:
                physical *= states[i]
                slope, offset = affine[i]
                frozen *= slope * states[-1] + offset
            require(physical == frozen, (source, multiset))
            comparisons += 1
    return comparisons


def faces():
    supports = ({(0, 0), (1, 0), (0, 1)}, {(1, 1), (1, 0), (0, 1)})
    support = {(a + c, b + d) for a, b in supports[0] for c, d in supports[1]}
    cases = 0
    for x in range(-6, 7):
        for y in range(-6, 7):
            if not (x or y):
                continue
            for extremum in (min, max):
                def face(poly):
                    weight = extremum(a * x + b * y for a, b in poly)
                    return {(a, b) for a, b in poly if a * x + b * y == weight}

                require(face(support) == {(a + c, b + d) for a, b in face(supports[0])
                                          for c, d in face(supports[1])}, (x, y))
                if (x, y) == (1, 1):
                    require(len(face(support)) >= 2, "opposite tied faces")
                if (x, y) == (2, 1):
                    require(len(face(support)) == 1, "opposite singleton faces")
                cases += 1
    return cases


if __name__ == "__main__":
    print(ordinary_backwards(), "ordinary three-index affine products;",
          root_truncations(), "exact two-place ramified root tests;",
          faces(), "exposed-face comparisons")
