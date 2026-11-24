"""Exact positive rational controls for the biased-potential arithmetic boundary."""
from fractions import Fraction
from math import gcd


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3*x+1)/2 if x.numerator % 2 else x/2


def cycle(start, expected_word):
    x = start
    values = []
    bits = []
    for _ in expected_word:
        values.append(x)
        bits.append(x.numerator % 2)
        x = step(x)
    require(x == start, "rational cycle did not close")
    require(bits == expected_word, "rational cycle parity mismatch")
    multiplier = Fraction(2**(len(bits)+sum(bits)), 3**len(bits))
    require(multiplier > 1, "cycle does not have increasing tilted terms")
    return values


def main():
    small = cycle(Fraction(19,5), [1,1,1,0,0])
    require(small == [Fraction(x,5) for x in [19,31,49,76,38]], "small cycle values")
    r = Fraction(3**17-2**17, 2**27-3**17)
    require(r == Fraction(129009091,5077565), "large cycle anchor")
    large = cycle(r, [1]*17+[0]*10)
    require(min(large) == r and r > 25, "large cycle minimum")
    require(all(gcd(r.denominator,p)==1 for p in [2,3,7]), "integrality at selected primes")
    require(r.denominator % 5 == 0, "nonintegrality at the omitted prime")
    x = (16*(2**9*r)-19)/27
    require(x == Fraction(39138740731,5077565), "prefix inverse")
    require(all(gcd(x.denominator,p)==1 for p in [2,3,7]), "prefix local integrality")
    values = []
    bits = []
    for _ in range(4):
        values.append(x)
        bits.append(x.numerator % 2)
        x = step(x)
    require(bits == [1,1,1,0] and x == 2**9*r, "prescribed prefix")
    for _ in range(9):
        values.append(x)
        require(x.numerator % 2 == 0, "dyadic return is not even")
        x = step(x)
    require(x == r and min(values) > 25, "prefix floor or cycle entry")
    print("Two exact positive rational cycles; prefix 1110 and nine halvings; selected-prime integrality and geometric divergence")


if __name__ == "__main__":
    main()
