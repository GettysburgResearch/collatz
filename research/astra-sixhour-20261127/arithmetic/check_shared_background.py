"""Exact shared-background factorization, surviving frequencies and half-turn inputs."""
import json
from fractions import Fraction
from itertools import product
from math import gcd

from check_shifts import require


def trim(poly):
    while poly and not poly[-1]:
        poly.pop()
    return poly


def poly_gcd_degree(first, second):
    a, b = [Fraction(t) for t in first], [Fraction(t) for t in second]
    while b:
        while len(a) >= len(b):
            offset, factor = len(a) - len(b), a[-1] / b[-1]
            for i, value in enumerate(b):
                a[offset + i] -= factor * value
            trim(a)
        a, b = b, a
    return len(a) - 1


def odd_carry(word):
    clock = carry = 0
    for letter in word:
        carry = 3 * carry + 2 ** clock
        clock += letter
    return carry, clock


def certificate(background, marks):
    r, k = len(marks), len(background) + 1
    carry, s = odd_carry(background)
    p = 3 ** k
    e = 3 * carry + 2 ** s
    t = sum(marks)
    require(2 <= r and len(set(marks)) >= 2 and all(a >= 1 for a in marks),
            "positive nonconstant markers")
    full = [a for b in marks for a in (*background, b)]
    complete, clock = odd_carry(full)
    d = 2 ** clock - 3 ** (r * k)
    require(d > 0, "positive determinant")
    prefixes = [0]
    for mark in marks:
        prefixes.append(prefixes[-1] + mark)
    h = sum(p ** (r - 1 - j) * 2 ** (s * j + prefixes[j]) for j in range(r))
    require(clock == r * s + t and complete == e * h, "raw factorization")
    require(e * 2 ** k <= 2 ** (s + 1) * p, "internal intercept bound")
    coefficients = [2 ** prefixes[j] for j in reversed(range(r))]
    common = poly_gcd_degree(coefficients, [-2 ** t] + [0] * (r - 1) + [1])
    support = r - common
    require(support >= 2, "nonconstant prefix Fourier support")
    g = gcd(d, complete)
    q = d // g
    nums, state = [], complete // g
    for a in full:
        nums.append(state)
        raw = 3 * state + q
        require(state % 2 == 1 and raw % 2 ** (a + 1) == 2 ** a,
                "wrong physical odd valuation")
        state = raw // 2 ** a
        require(gcd(state, q) == 1, "complete denominator preservation")
    require(state == nums[0], "physical closure")
    result = dict(background_length=k - 1, background_clock=s, marker_total=t,
                  markers=marks, active_frequencies=support, denominator_bits=q.bit_length(),
                  raw_bits=d.bit_length())
    if r == 2 and marks[0] < marks[1]:
        n = 2 ** (s + marks[0])
        u = 2 ** (marks[1] - marks[0]) - 1
        x, y = nums[0], nums[k]
        g0 = gcd(p + n, u)
        require((p + n) * (y - x) == n * u * x, "half-turn identity")
        require(g0 * x % (p + n) == 0 and min(nums) * g0 >= 2 ** k,
                "half-turn numerator divisibility or minimum")
        result["half_turn_gcd_bits"] = g0.bit_length()
    return result


def main():
    count = 0
    for n in range(4):
        for u in product((1, 2, 3), repeat=n):
            for r in (2, 3, 4):
                for marks in product((1, 2, 3), repeat=r):
                    if len(set(marks)) == 1 or 2 ** (r * sum(u) + sum(marks)) <= 3 ** (r * (n+1)):
                        continue
                    certificate(u, list(marks))
                    count += 1
    examples = []
    for n, marks in [(32, [1, 37]), (69, [1, 88]), (20, [1, 2, 672]),
                     (23, [101, 287, 1001, 41]), (18, [1, 7, 1, 7]),
                     (28, [3, 1, 3, 3, 1, 1])]:
        u = tuple(1 + ((i * i + 3*i + 1) % 7 < 6) for i in range(n))
        examples.append(certificate(u, marks))
    # A literal repetition of unequal markers permits polynomial cancellation.
    require(examples[4]["active_frequencies"] == 2, "periodic marker control")
    print(json.dumps(dict(exhaustive_words=count, examples=examples), indent=2))


if __name__ == "__main__":
    main()
