"""Exact finite controls for GS1 and the reducible functional equation in GS2."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
import json


def require(condition):
    if not condition:
        raise ArithmeticError("finite control failed")


def prefix_monomials(word):
    zeros = ones = 0
    counts = Counter()
    for letter in word:
        if letter == "0":
            counts[(zeros, ones)] += 1
            zeros += 1
        else:
            ones += 1
    return counts


def polynomial_controls():
    checked = 0
    words = ["".join(bits) for length in range(5)
             for bits in product("01", repeat=length)]
    for length in range(3, 7):
        for tail in product("01", repeat=length - 1):
            image = "0" + "".join(tail)
            a, b = image.count("0"), image.count("1")
            if a < 2 or b < 1:
                continue
            inner = prefix_monomials(image)
            for d in range(1, 6):
                for word in words:
                    substituted = "".join(image if x == "0" else "1" * d for x in word)
                    predicted = Counter()
                    for (i, j), multiplicity in prefix_monomials(word).items():
                        for (u, v), coefficient in inner.items():
                            predicted[(u + a*i, v + b*i + d*j)] += coefficient * multiplicity
                    require(predicted == prefix_monomials(substituted))
                    checked += 1
    return checked


def orbit_controls():
    checked = 0
    for source in range(1, 514, 2):
        q, cumulative, power, offset = source, 0, 1, 0
        for n in range(1, 41):
            numerator = 3*q + 1
            step_power = numerator & -numerator
            gap = step_power.bit_length() - 1
            q = numerator // step_power
            offset = 3*offset + power
            cumulative += gap
            power *= step_power
            require(power == 2**cumulative)
            require(3**n * source + offset == power*q)
            checked += 1
    return checked


def scale_controls():
    checked = 0
    for a in range(2, 6):
        for b in range(1, 5):
            for d in range(1, 8):
                for v, w in [(1, 1), (3, 2), (2, 7)]:
                    fast, slow = v, w
                    for n in range(21):
                        require(fast == a**n*v + b*w*sum(a**(n-1-j)*d**j for j in range(n)))
                        require(slow == d**n*w)
                        if d > a:
                            common = gcd(b, d-a)
                            p, q = b // common, (d-a) // common
                            require(p*slow - q*fast == a**n * (p*w - q*v))
                        fast, slow = a*fast + b*slow, d*slow
                        checked += 1
    return checked


def example_controls():
    word = "0"
    for n in range(13):
        require((word.count("0"), word.count("1")) == (2**n, n*2**n))
        slope = Fraction(9, 32)**word.count("0") * Fraction(9, 8)**word.count("1")
        require((slope > 1) == (n >= 11))
        if n < 12:
            word = "".join("0011" if x == "0" else "11" for x in word)
    return 13


if __name__ == "__main__":
    print(json.dumps({"physical_telescope": orbit_controls(),
                      "triangular_polynomial_identity": polynomial_controls(),
                      "coordinate_valuations": scale_controls(),
                      "explicit_jordan_levels": example_controls()}, indent=2))
