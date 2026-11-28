"""Finite checks for the dyadic native tube, prime dilation and rank rectangles."""
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement, product
import json
from math import gcd

from check_rational_six_sum import clock_word, floor_log2, native_cycle


def require(condition, description):
    if not condition:
        raise ValueError(description)


def pow2(exponent):
    return Fraction(1 << max(0, exponent), 1 << max(0, -exponent))


def multiply(left, right):
    out = Counter()
    for i, a in left.items():
        for j, b in right.items():
            out[i + j] += a * b
    return {i: a for i, a in out.items() if a}


def frobenius():
    tests = exact = nonzero = repetitions = 0
    for offsets in combinations_with_replacement(range(8), 4):
        i, j, k, l = offsets
        poly = Counter((i, l))
        poly.subtract((j, k))
        poly = {i: a for i, a in poly.items() if a}
        if not poly:
            continue
        power = {0: 1}
        for _ in range(11):
            power = multiply(power, poly)
        dilated = {11 * i: a for i, a in poly.items()}
        require(all((power.get(i, 0) - dilated.get(i, 0)) % 11 == 0
                    for i in set(power) | set(dilated)), "integer dilation")
        if len(poly) == 3:
            repetitions += 1
        for modulus in (3, 5, 7, 19):
            for stride in (-3, -1, 2):
                t = -11
                def tag(date):
                    return 1 + (date * date % modulus < (modulus + 1) // 2)

                # U is in Z[1/2] at negative dates. D includes the matching
                # dyadic factor, so this checks weighted shifts at both signs.
                def normalized(polynomial, date):
                    return sum(a * pow2(-date - stride * i) *
                               pow2(date + stride * i) * tag(date + stride * i)
                               for i, a in polynomial.items())

                lhs = normalized(power, t)
                rhs = normalized(dilated, t)
                require(lhs.denominator == rhs.denominator == 1 and
                        (lhs - rhs) % 11 == 0 and abs(rhs) <= 8,
                        "weighted finite alphabet dilation")
                if all(normalized(poly, t + stride * j) == 0
                       for j in range(10 * max(poly) + 1)):
                    require(lhs == rhs == 0, "exact local annihilation")
                    exact += 1
                if rhs:
                    nonzero += 1
                tests += 1
    require(exact and nonzero and repetitions, "vacuity controls")
    return dict(weighted_congruences=tests, exact_local_zero_cases=exact,
                nonzero_dilations=nonzero, doubled_inner_stencils=repetitions)


def rational_grid():
    rows = []
    for B, P, sheets, seed in ((485, 306, 2, 1), (485, 306, 3, 2)):
        E, q, y = native_cycle(clock_word(P, B, sheets, seed))
        p, A, minimum = len(y), E[-1], min(y)
        tau = pow(B, -1, P)
        carry, residue = divmod(tau * B, P)
        require(residue == 1 and gcd(A, p) == sheets and max(y) < 3 * minimum,
                "actual physical rational fixture")
        def exponent(t):
            lap, position = divmod(t, p)
            return lap * A + E[position]
        def floor(t):
            return exponent(t) + floor_log2(4 * y[t % p], 7 * minimum)
        def data(t, j):
            right = t + j * tau
            tag = pow2(exponent(right) - floor(t) - carry * j)
            return tag, tag * y[right % p]
        checked = signed = 0
        # This is a genuine multi-sheet, q-scaled positive rational grid.
        # The moving-p outlier bound itself concerns ordinary integer cycles.
        for t in range(-p, p, 7):
            for j in (0, 1, 2, 3, 11, 22, 33):
                tag, value = data(t, j)
                next_tag, next_value = data(t + 1, j)
                signed_time = ((j * tau + p // 2) % p) - p // 2
                require((t + j * tau - t - signed_time) % p == 0,
                        "signed physical return")
                right = t + signed_time
                lhs = P * (exponent(t + j * tau) - exponent(t) - carry * j) - j
                rhs = P * (exponent(right) - exponent(t)) - B * signed_time
                require(lhs == rhs, "de-meaned signed time equality")
                require(tag in (1, 2) and next_tag in (1, 2) and
                        value.denominator == 1 and next_value.denominator == 1 and
                        pow2(floor(t + 1) - floor(t)) * next_value ==
                        3 * value + q * tag, "true scaled native affine law")
                checked += 1
                signed += signed_time < 0
        require(signed > 0, "negative representative exercised")
        rows.append(dict(p=p, P=P, sheets=sheets, full_q_bits=q.bit_length(),
                         checked=checked, negative_representatives=signed))
    return rows


def rectangles():
    checks = 0
    for denominator in (41, 103):
        z = Fraction(denominator + 1, denominator)
        for d, b, f in product(range(1, 8), repeat=3):
            if b < d:
                continue
            def stencil(x):
                return x**b * (x**f - 1) - (x**d - 1)
            left = stencil(z**11) - stencil(z) * sum(z**(h * d) for h in range(11))
            lower = (z**f - 1) * (z**(10 * b) - 1)
            require(left >= lower > 0, "two-scale strict curvature")
            checks += 1
    # Precisely enumerate rank rectangles and the repeated-inner-point cases.
    populations = []
    for E in (0, 1, 3, 16, 47):
        side = 28
        expected = set()
        for i in range(side):
            for d in range(1, side):
                for b in range(d, side):
                    if d * b <= E and i + d + b < side:
                        expected.add((i, i + d, i + b, i + b + d))
        direct = {q for q in combinations_with_replacement(range(side), 4)
                  if q[0] < q[1] <= q[2] < q[3] and q[1] - q[0] == q[3] - q[2]
                  and (q[1] - q[0]) * (q[2] - q[0]) <= E}
        require(expected == direct, "precise nested and repeated counting")
        populations.append(dict(E=E, three_or_four=len(direct),
                                repeated=sum(q[1] == q[2] for q in direct)))
    return dict(positive_rational_base_inequalities=checks, populations=populations)


def genuine_ordinary():
    bands = edges = 0
    for x in range(101, 10001, 2):
        y = [x]
        exps = [0]
        for _ in range(7):
            n = 3 * y[-1] + 1
            a = (n & -n).bit_length() - 1
            y.append(n >> a)
            exps.append(exps[-1] + a)
        lo, hi = min(y), max(y)
        if 2 * hi > 7 * lo or len(set(y)) != len(y):
            continue
        # Band cutoff 7/2, midpoint L=15m/8. Real ordinary orbit, q=1.
        shifts = [a + floor_log2(8 * value, 15 * lo) for value, a in zip(y, exps)]
        tags = [pow2(a - f) for a, f in zip(exps, shifts)]
        require(all(c in (1, 2) for c in tags), "binary tags on actual ordinary segment")
        for t in range(7):
            require(pow2(shifts[t + 1] - shifts[t]) * tags[t + 1] * y[t + 1] ==
                    3 * tags[t] * y[t] + tags[t], "actual ordinary normalized edge")
            edges += 1
        bands += 1
    require(bands > 0, "real ordinary examples")
    return dict(confined_distinct_segments=bands, ordinary_edges=edges,
                native_steps_per_segment=7)


if __name__ == "__main__":
    print(json.dumps(dict(frobenius=frobenius(), rational_chart=rational_grid(),
                          rank_rectangles=rectangles(), ordinary=genuine_ordinary()),
                     indent=2, sort_keys=True))
