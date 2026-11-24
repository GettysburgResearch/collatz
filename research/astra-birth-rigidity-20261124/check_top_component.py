"""Exact controls for the top cyclotomic component, using only the standard library."""
from collections import Counter
from fractions import Fraction
from functools import cache
from math import gcd
import json


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def trim(coefficients):
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients


def primitive_part(polynomial):
    polynomial = trim(polynomial)
    if not polynomial:
        return []
    content = gcd(*polynomial)
    if polynomial[-1] < 0:
        content = -content
    return [value // content for value in polynomial]


def polynomial_gcd(left, right):
    left, right = primitive_part(left[:]), primitive_part(right[:])
    while right:
        while len(left) >= len(right):
            offset = len(left) - len(right)
            top = left[-1]
            left = [right[-1] * value for value in left]
            for i, value in enumerate(right):
                left[offset+i] -= top * value
            left = primitive_part(left)
        left, right = right, left
    return left


def monic_quotient(numerator, denominator):
    remainder = numerator[:]
    quotient = [0] * (len(numerator) - len(denominator) + 1)
    for shift in reversed(range(len(quotient))):
        coefficient = remainder[shift + len(denominator) - 1]
        quotient[shift] = coefficient
        for i, value in enumerate(denominator):
            remainder[shift+i] -= coefficient * value
    require(not any(remainder), "inexact cyclotomic division")
    return quotient


@cache
def cyclotomic(index):
    polynomial = [-1] + [0] * (index-1) + [1]
    for divisor in range(1, index):
        if index % divisor == 0:
            polynomial = monic_quotient(polynomial, cyclotomic(divisor))
    return polynomial


def prime_divisors(value):
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def normalized_word(marks, length):
    return [int(clock in marks) for clock in range(length)]


def least_period(word):
    return next(k for k in range(1, len(word)+1) if
                len(word) % k == 0 and word == word[:k] * (len(word)//k))


def components(word):
    positions = [i for i, bit in enumerate(word) if bit]
    length, count = len(word), len(positions)
    clock_gcd = gcd(length, count)
    a, b = length//clock_gcd, count//clock_gcd
    phi = cyclotomic(clock_gcd)
    degree = len(phi)-1
    top_factor = [0] * (b*degree+1)
    for i, coefficient in enumerate(phi):
        top_factor[b*i] = coefficient * 2**(a*(degree-i))
    carry_polynomial = [2**pos for pos in reversed(positions)]
    carry = sum(value * 3**i for i, value in enumerate(carry_polynomial))
    difference = 2**length - 3**count
    return (polynomial_gcd(carry_polynomial, top_factor), top_factor, carry, difference)


def replay(word, carry, difference):
    start = Fraction(carry, difference)
    require(start > 0 and gcd(start.denominator, 6) == 1, "bad physical start")
    current = start
    for bit in word:
        require(current.numerator % 2 == bit, "parity mismatch")
        current = (3*current+1)/2 if bit else current/2
        require(current.denominator == start.denominator, "denominator changed")
    require(current == start, "failed rational closure")
    return start


def mixed_word(g):
    prime_r, prime_s = prime_divisors(g)[:2]
    marks = set()
    for j in range(g):
        marks.update([5*j + int(j % (g//prime_r) == 1),
                      5*j+2 + int(j % (g//prime_s) == 1), 5*j+4])
    return normalized_word(marks, 5*g)


def main():
    counts = Counter()
    for length in range(2, 15):
        for mask in range(1, 1 << length, 2):
            count = mask.bit_count()
            if 2**length <= 3**count:
                continue
            word = [(mask >> clock) & 1 for clock in range(length)]
            shared, _, carry, difference = components(word)
            replay(word, carry, difference)
            counts["positive_normalized_words"] += 1
            g = gcd(length, count)
            if g == 1 or (len(prime_divisors(g)) == 1 and (g != 4 or count//g % 2)):
                repeated = least_period(word) < length
                require((len(shared) > 1) == repeated, (word, shared))
                counts["equivalence_checks"] += 1
                counts["repeated_cases"] += int(repeated)
    examples = {}
    for g in [6, 10, 12, 15, 18, 20, 21, 24, 30, 35, 45, 60]:
        word = mixed_word(g)
        shared, top, carry, difference = components(word)
        start = replay(word, carry, difference)
        require(least_period(word) == len(word) and shared == top and start.denominator > 1, g)
        numerical_top = sum(value * 3**i for i, value in enumerate(top))
        require(carry % numerical_top == 0 and difference % numerical_top == 0, g)
        examples[g] = str(start)
    word = normalized_word({0,1,2,4,6,8,10,11,13,15,17,18,20,22,23,25}, 28)
    shared, _, carry, difference = components(word)
    start = replay(word, carry, difference)
    require(least_period(word) == 28 and shared == [128,0,-16,0,1], "quartic witness")
    print(json.dumps(dict(bounded=dict(counts), mixed_rational_sources=examples,
                          quartic=dict(A=28, p=16, C=carry, D=difference,
                                       gcd=gcd(carry,difference), start=str(start),
                                       common_quartic_ascending=shared)), indent=2))


if __name__ == "__main__":
    main()
