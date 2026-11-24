from fractions import Fraction
from itertools import product
import json


def check(condition, context):
    if not condition:
        raise ValueError(context)


def odd_step(x):
    numerator = 3 * x + 1
    gap = (numerator & -numerator).bit_length() - 1
    return gap, numerator >> gap


def word_data(word):
    clock = 0
    carry = 0
    for gap in word:
        carry = 3 * carry + (1 << clock)
        clock += gap
    return clock, carry


def build_logs(k):
    modulus = 3**k
    order = 2 * 3**(k - 1)
    result = {}
    power = 1
    for exponent in range(order):
        check(power not in result, (k, exponent))
        result[power] = exponent
        power = 2 * power % modulus
    check(power == 1 and len(result) == order, (k, power))
    return result


def explicit_controls():
    cases = 0
    canonical = 0
    for n in range(10):
        for m in range(10 - n):
            exponent = 3**(n + m)
            r = exponent + 1
            d = (1 << exponent) + 1
            check(d % (3**(n + m + 1)) == 0, (n, m, "LTE"))
            check(d % (3**(n + m + 2)) != 0, (n, m, "exact LTE"))
            q = (1 << (n + 1)) * (d // 3**(n + 1)) - 1
            h = Fraction(1)
            for gap in (r,) + (1,) * n:
                h = (gap + h) / 3
            expected = Fraction(1, 2) + Fraction(3**m, 3) + Fraction(1, 2 * 3**(n+1))
            check(h == expected, (n, m, "actual scalar"))
            states = []
            for i in range(n+1):
                states.append(q)
                check((q + 1) % 3**(m+i) == 0, (n, m, i, "ternary"))
                check((q + 1) % 3**(m+i+1) != 0, (n, m, i, "ternary exact"))
                gap, nxt = odd_step(q)
                if m >= 1:
                    h_next = 3 * h - gap
                    c = -(-(h - Fraction(1, 2)) // 1) - 1
                    c_next = -(-(h_next - Fraction(1, 2)) // 1) - 1
                    check(c == 3**(i+m-1), (n, m, i, "carry"))
                    check(3 * (h-c) - (h_next-c_next) == 1, (n, m, i, "canonical"))
                    h = h_next
                    canonical += 1
                if i < n:
                    check(gap == 1 and nxt > q, (n, m, i, "increasing"))
                else:
                    check(gap == r and nxt == 1, (n, m, i, "terminal"))
                q = nxt
            check(len(set(states)) == n+1, (n, m, "injective"))
            check(len({q % 3**m for q in states}) == 1, (n, m, "collision"))
            cases += 1
    return cases, canonical


def gluing_controls():
    logs = {k: build_logs(k) for k in range(1, 7)}
    scripts = 0
    reported = 0
    repeated_starts = 0
    for n in range(4):
        for word in product((1, 2, 3, 4), repeat=n):
            scripts += 1
            a, c = word_data(word)
            for m in range(3):
                k = n + m + 1
                modulus = 3**k
                period = 2 * 3**(k-1)
                for u in range(3**m):
                    for t in (1, 5, 7, 11, 13):
                        target = ((1 << a) + 3*c + 3**(n+1)*u) * pow((1 << a)*t, -1, modulus) % modulus
                        first = logs[k][target]
                        # Two different representatives beyond the small-size region.
                        base = first + period * (n + 2)
                        first_q = None
                        for r in (base, base + period):
                            numerator = ((1 << (a + r))*t - (1 << a) - 3*c)
                            q, remainder = divmod(numerator, 3**(n+1))
                            check(remainder == 0 and q > 0 and q % 2 == 1, (word, m, u, t, r, "q"))
                            check(q % 3**m == u, (word, m, u, t, r, "u"))
                            if first_q is None:
                                first_q = q
                            else:
                                check(q > first_q, (word, m, u, t, r, "infinite progression sample"))
                                repeated_starts += 1
                            for expected in word + (r,):
                                actual, q = odd_step(q)
                                check(actual == expected, (word, m, u, t, r, "gap"))
                            check(q == t, (word, m, u, t, r, "target"))
                            reported += 1
    return scripts, reported, repeated_starts


if __name__ == "__main__":
    explicit, canonical = explicit_controls()
    words, cases, pairs = gluing_controls()
    print(json.dumps({
        "explicit_one_run_cases": explicit,
        "actual_canonical_edges_equal_to_one": canonical,
        "distinct_tested_gap_words": words,
        "ordinary_word_residue_target_witnesses": cases,
        "pairs_of_witnesses_in_same_exponent_progression": pairs,
    }, indent=2))
