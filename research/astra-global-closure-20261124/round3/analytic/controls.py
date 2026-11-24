"""Exact finite controls for the fixed-word divisor argument."""
import itertools
import json
import math
from functools import cache


def accelerated(x):
    n = 3 * x + 1
    power = n & -n
    return power.bit_length() - 1, n // power


@cache
def factors(n):
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        result[n] = 1
    return result


def run(x, length):
    q = [x]
    gaps = []
    for _ in range(length):
        a, y = accelerated(q[-1])
        gaps.append(a)
        q.append(y)
    return q, tuple(gaps)


@cache
def row_products(gaps):
    t = len(gaps) + 1
    products = [1] * t
    for i in range(t - 1):
        clock = carry = 0
        for j in range(i + 1, t):
            carry = 3 * carry + (1 << clock)
            clock += gaps[j - 1]
            products[i] *= carry
            products[j] *= carry
    return tuple(products)


def covered(q, j):
    for prime, v in factors(q[j]).items():
        if v > sum(factors(y).get(prime, 0) for i, y in enumerate(q) if i != j):
            return False
    return True


def check_sources():
    result = {}
    for t in (2, 3, 4, 5, 8):
        bad_sources = 0
        divisor_sources = {}
        for x in range(1, 16001, 2):
            q, gaps = run(x, t - 1)
            prod = row_products(gaps)
            bad = False
            for j in range(t):
                if covered(q, j):
                    bad = True
                    assert prod[j] % q[j] == 0
                    row = (gaps, j, q[j])
                    assert row not in divisor_sources
                    divisor_sources[row] = x
            if t == 3:
                assert bad == (x % q[2] == 0)
                if bad and x > 1:
                    assert q[2] < x and 2 * q[2]**2 - 7 * q[2] <= 9 * x
            if bad and t >= 3:
                assert min(q)**(t - 1) <= (4**(t - 1) * x)**(t - 2)
            bad_sources += bad
        result[t] = {"odd_sources": 8000, "sources_with_a_covered_row": bad_sources,
                     "distinct_word_row_divisor_certificates": len(divisor_sources)}
    return result


def check_terminating_lifts():
    count = 0
    for length in range(1, 5):
        for w in itertools.product((1, 2, 4), repeat=length):
            A = carry = 0
            for a in w:
                carry = 3 * carry + (1 << A)
                A += a
            modulus = 3**(length + 1)
            phi = 2 * 3**length
            for target in (1, 5, 7):
                residue = (1 + 3 * carry * pow(2, -A, modulus)) % modulus
                candidates = [e for e in range(1, phi + 1)
                              if pow(2, e, modulus) * target % modulus == residue]
                assert len(candidates) == 1
                e = candidates[0]
                while True:
                    y = ((1 << e) * target - 1) // 3
                    x, remainder = divmod((1 << A) * y - carry, 3**length)
                    assert remainder == 0
                    if x > 0:
                        states, gaps = run(x, length + 1)
                        assert gaps == w + (e,) and states[-1] == target
                        if min(states[:-1]) > max(row_products(w)):
                            break
                    e += phi
                count += 1
    return count


if __name__ == "__main__":
    print(json.dumps({"source_checks": check_sources(),
                      "fixed_word_target_pairs": check_terminating_lifts()}, indent=2))
