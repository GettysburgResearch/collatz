"""Exact finite checks for the affine and stopping interfaces in local_first_landing.md."""

from collections import Counter
from fractions import Fraction
from itertools import combinations


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def shortcut(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def oddstep(x):
    n = 3 * x + 1
    return n // (n & -n)


def native(r, k):
    x = r
    q = 0
    for _ in range(k):
        q += x % 2
        x = shortcut(x)
    return q, x


def words(total, depth):
    for cuts in combinations(range(1, total), depth - 1):
        breaks = (0, *cuts, total)
        yield tuple(y - x for x, y in zip(breaks, breaks[1:]))


def offset_code(word):
    """Return 2^s B_b using the integer recurrence in inverse word order."""
    offset = 0
    for i, gap in enumerate(word):
        offset = (offset << gap) + 3**i
    return offset


def actual_inverse(w, word):
    chain = [w]
    for e in word:
        numerator = (chain[-1] << e) - 1
        require(numerator % 3 == 0, "nonintegral prefix at a full congruence")
        x = numerator // 3
        require(x > 0 and x % 2 == 1 and oddstep(x) == chain[-1], "invalid odd edge")
        chain.append(x)
    return chain


def first_landing(x, threshold, max_steps):
    for i in range(max_steps + 1):
        if x % 2 and x <= threshold:
            return x, i
        x = shortcut(x)
    raise AssertionError("first landing exceeded physical word clock")


def bridge(a, threshold):
    """Test ternary class 2 modulo 3, using a finite-scale boost."""
    e = 1
    while (1 << e) * a < 36 * threshold or ((a << e) - 1) % 9 != 6:
        e += 1
    return ((a << e) - 1) // 3, e


def run():
    c = Counter()
    seen_by_source = {}
    lifted_nonunit = 0
    for threshold in (1, 9, 27):
        for a in range(1, threshold + 1, 2):
            if a % 3 == 0:
                continue
            w, first_e = bridge(a, threshold)
            for k in range(6):
                for r in range(1 << k):
                    q, t = native(r, k)
                    for b in range(1, 5):
                        modulus = 3 ** (b + q)
                        for s in range(max(b, 2 * b - 2), 2 * b + 3):
                            power = 1 << s
                            # The complete fine residue after multiplying by 2^s.
                            residue = (power * w - 3**b * t) % modulus
                            for word in words(s, b):
                                code = offset_code(word)
                                c["words_compared"] += 1
                                if code % modulus != residue:
                                    continue
                                chain = actual_inverse(w, word)
                                z = chain[-1]
                                require(power * w - code == 3**b * z, "full affine row")
                                require((z - t) % (3**q) == 0, "fine native cofactor")
                                x = r + (1 << k) * ((z - t) // (3**q))
                                if x <= r or min(chain) <= threshold or x <= threshold * (1 << k):
                                    continue
                                require(x % (1 << k) == r, "native suffix")
                                require(native(x, k) == (q, z), "native exact replay")
                                W = Fraction((1 << k) * power * w, 3 ** (q + b))
                                delta = Fraction((1 << k) * t, 3**q) - r
                                require(x == W * (1 - Fraction(code, power * w)) - delta,
                                        "source and affine correction")
                                require(0 <= delta < 1 << k and x < W, "height correction sign")
                                require(first_landing(x, threshold, k + s + first_e)
                                        == (a, k + s + first_e), "wrong first physical landing")
                                key = (threshold, k, r, x)
                                require(key not in seen_by_source, "duplicate first clock or target")
                                seen_by_source[key] = (a, b, s)
                                c["actual_landings"] += 1
                                c["all_even_native"] += q == 0
                                c["periodic_landings"] += a == 1
                                c["nonunit_terminal"] += z % 3 == 0
    # The small-threshold embedding preserves the subsequent odd orbit,
    # keeps all images distinct across the unchanged and lifted branches,
    # and increases the first valuation by exactly two.
    for Q in range(20, 301):
        image = set()
        for n in range(Q // 4 + 1, Q + 1):
            if n % 2 == 0:
                continue
            y = 4 * n + 1 if n % 3 == 0 else n
            require(y % 3 != 0 and y not in image and y <= 4 * Q + 1, "unit embedding")
            image.add(y)
            if y != n:
                require(oddstep(y) == oddstep(n) and 3 * y + 1 == 4 * (3 * n + 1),
                        "successor or reserve loss")
                lifted_nonunit += 1
    require(min(c["all_even_native"], c["periodic_landings"], c["nonunit_terminal"]) > 0,
            "missing boundary group in finite control")
    c["unit_embeddings"] = lifted_nonunit
    return dict(sorted(c.items()))


if __name__ == "__main__":
    print(run())
