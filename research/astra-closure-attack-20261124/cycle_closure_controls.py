"""Exact controls for the complete-denominator transport. Standard library only."""
from fractions import Fraction
from itertools import product
from math import gcd
import json


def require(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def clocks(word):
    multiplier, carry, binary = 1, 0, 1
    for bit in word:
        if bit == "1":
            carry = 3 * carry + binary
            multiplier *= 3
        binary *= 2
    return binary, multiplier, carry


def primitive(word):
    return word not in (word + word)[1:-1]


def verify_pair(left, right):
    P, Q, U = clocks(left)
    R, S, V = clocks(right)
    D = P * R - Q * S
    first = Fraction(S * U + P * V, D)
    second = Fraction(Q * V + R * U, D)
    require(first.denominator == second.denominator, (left, right))
    d = first.denominator
    x, y = first.numerator, second.numerator
    center1, center2 = Fraction(U, P-Q), Fraction(V, R-S)
    c, a = center1.numerator, center1.denominator
    e, b = center2.numerator, center2.denominator
    K, G = a*e-b*c, gcd(P-Q, R-S)
    require(K != 0, (left, right, "equal centers"))
    require(D*b*(a*x-d*c) == d*K*P*(R-S), "start displacement")
    require(D*a*(b*y-d*e) == -d*K*R*(P-Q), "second displacement")
    certificate = D // gcd(D, abs(K)*G)
    require(d % certificate == 0, (left, right, d, certificate))
    require(G != 1 or d == certificate, "nonresonant exactness")
    return d, certificate


def main():
    words = cuts = nontrivial = exact = dependent = 0
    for A in range(2, 13):
        for bits in product("01", repeat=A):
            word = "".join(bits)
            N, M, C = clocks(word)
            if N <= M or not C or not primitive(word):
                continue
            words += 1
            value = Fraction(C, N-M)
            point = value
            for bit in bits:
                require(point.numerator % 2 == int(bit), "literal parity")
                point = (3*point+1)/2 if bit == "1" else point/2
            require(point == value, "literal closure")
            for index in range(1, A):
                left, right = word[:index], word[index:]
                d, certificate = verify_pair(left, right)
                nontrivial += int(certificate > 1)
                exact += int(d == certificate)
                dependent += int(len(left)*right.count("1") == len(right)*left.count("1"))
                cuts += 1
    require(verify_pair("0010", "1111") == (13, 1), "resonant failure")
    for m in range(1, 33):
        left, right = "01"*m, "10"*m
        d, certificate = verify_pair(left, right)
        require(d == certificate == 4**m + 3**m, "sharp half-rate")
    print(json.dumps(dict(positive_primitive_words=words, cuts=cuts,
                          certificates_above_one=nontrivial, exact_certificates=exact,
                          dependent_cuts=dependent, equal_clock_sharp_family=32),
                     indent=2))


if __name__ == "__main__":
    main()
