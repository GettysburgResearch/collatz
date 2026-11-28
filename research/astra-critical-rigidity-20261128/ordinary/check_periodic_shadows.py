"""Exact integer replay for rational periodic centers and ordinary source lifts."""

import json
from math import gcd


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n, q=1):
    return (3 * n + q) // 2 if n % 2 else n // 2


def check_row(length, c, t, common, g, h):
    q = 2**length - 3
    require(gcd(c, 2 * q) == 1, "source must be odd with the stated denominator")
    require(common.bit_count() == 1 and 0 < common < 2**length, "incorrect cycle phase")
    j = h + 1 - g
    require(j > 0 and pow(3, j, q) == 1, "the reduced denominator must divide the slope gap")
    a, b = c, 3 * c
    u, v = 0, 0
    for _ in range(t):
        u += a % 2
        v += b % 2
        a, b = step(a, q), step(b, q)
    require((a, b, u, v) == (common, common, g, h), "incorrect rational entry")

    word = []
    state = common
    for _ in range(length):
        word.append(state % 2)
        state = step(state, q)
    require(state == common and sum(word) == 1, "not a one-odd cycle of the stated length")

    lifts = []
    for repeats in (1, 4, 16, 64, 256):
        k = t + length * repeats
        modulus = 1 << k
        residue = c * pow(q, -1, modulus) % modulus
        for source in (residue, residue + modulus):
            aa, bb = source, 3 * source
            a, b = c, 3 * c
            u = v = 0
            for i in range(k):
                require(aa > 0 and bb > 0 and aa != bb, "ordinary states met or became nonpositive")
                require((aa % 2, bb % 2) == (a % 2, b % 2), "parity comparison failed")
                if i >= t:
                    require(aa % 2 == bb % 2 == word[(i - t) % length], "wrong repeated word")
                u += aa % 2
                v += bb % 2
                aa, bb = step(aa), step(bb)
                a, b = step(a, q), step(b, q)
            require(aa != bb and (u, v) == (g + repeats, h + repeats), "incorrect physical endpoint")
        lifts.append({"repeats": repeats, "native_length": k, "combined_grade": u + v})
    return {"period": length, "q": q, "seed_numerator": c, "entry_clock": t,
            "common_numerator": common, "entry_grades": [g, h], "slope_gap": j, "two_lifts_each": lifts}


def finite_noncentering_control():
    a, b = 9, 27
    g = h = 0
    for _ in range(21):
        g += a % 2
        h += b % 2
        a, b = step(a), step(b)
    require((a, b, g, h) == (1, 593, 10, 16), "incorrect noncentering entry")
    d = 3**g * b - 3**(h + 1) * a
    # The word (odd, even) has D=C=1.
    obstruction = d - (3**g - 3**(h + 1))
    for parity in (1, 0, 1, 0):
        require(a != b and a % 2 == b % 2 == parity, "missing two physical copies")
        a, b = step(a), step(b)
    require(obstruction == 34957008 and obstruction % 16 == 0, "nonzero dyadic obstruction mismatch")
    return {"source": 9, "entry_clock": 21, "word": [1, 0], "repeats": 2, "obstruction": obstruction}


def main():
    rows = ((3, -7, 17, 1, 6, 9), (4, 1, 9, 8, 3, 5), (5, -1481, 80, 4, 19, 46),
            (6, 1, 31, 32, 6, 15), (10, 343, 74, 512, 9, 42))
    print(json.dumps({"rows": [check_row(*row) for row in rows],
                      "noncenter": finite_noncentering_control()}, indent=2))


if __name__ == "__main__":
    main()
