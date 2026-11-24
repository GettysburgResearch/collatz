"""Exact finite controls for the moving-center telescope and tile construction."""
from fractions import Fraction
from math import gcd
from itertools import accumulate, product


def require(condition):
    if not condition:
        raise ValueError("finite control failed")


def affine(word):
    carry = odd = 0
    for t, bit in enumerate(word):
        if bit:
            carry = 3 * carry + 2**t
            odd += 1
    return odd, carry


def center(word):
    odd, carry = affine(word)
    return Fraction(carry, 2**len(word) - 3**odd)


def trace(source, word):
    states = [Fraction(source)]
    for bit in word:
        n = states[-1]
        require(n.denominator % 2 == 1 and n.numerator % 2 == bit)
        states.append((3 * n + 1) / 2 if bit else n / 2)
    return states


def check_segment(windows, source):
    word = sum(windows, ())
    states = trace(source, word)
    cuts = [0, *accumulate(map(len, windows))]
    weights = [2**cut * 3**sum(word[cut:]) for cut in cuts]
    ns = [states[cut] for cut in cuts]
    cs = list(map(center, windows))
    require(all(ns[i] != cs[i] for i in range(len(cs))))
    require(weights[-1] * (ns[-1] - cs[-1]) - weights[0] * (ns[0] - cs[0])
            == sum(weights[i] * (cs[i-1] - cs[i]) for i in range(1, len(cs))))
    return len(windows)


def tiles():
    A, p = 65, 41
    base = tuple((j+1)*p//A - j*p//A for j in range(A))
    options = []
    for offset in range(0, A-7, 8):
        tile = base[offset:offset+8]
        i = next(j for j in range(7) if tile[j] != tile[j+1])
        swapped = tile[:i] + (tile[i+1], tile[i]) + tile[i+2:]
        options.append((tile, swapped))
    D = 2**A - 3**p
    nonintegral = 0
    for choices in product(range(2), repeat=len(options)):
        word = sum((pair[choice] for pair, choice in zip(options, choices)), ()) + base[64:]
        source = center(word)
        path = trace(source, word)
        require(source > 0 and path[-1] == source and len(set(path[:-1])) == A)
        nonintegral += source.denominator != 1
        twin = options[0][1-choices[0]] + word[8:]
        require(gcd(affine(word)[1] - affine(twin)[1], D) == 1)
        for s in range(A):
            rotated = word[s:] + word[:s]
            require(all(abs(A*x - j*p) <= 18*A for j, x in enumerate(accumulate(rotated), 1)))
    require(nonintegral >= 2**(len(options)-1))
    return 2**len(options), nonintegral


if __name__ == "__main__":
    windows = [(1, 1, 0), (0, 0, 0), (1, 0, 1)]
    word = sum(windows, ())
    p, c = affine(word)
    modulus = 2**len(word)
    lifted_source = (-c * pow(3**p, -1, modulus)) % modulus + 10**7 * modulus
    check_segment(windows, lifted_source)
    check_segment([(0,)*25], 2**25)
    count, nonintegral = tiles()
    print(f"2 exact segments; {count} primitive rational itineraries; {nonintegral} nonintegral")
