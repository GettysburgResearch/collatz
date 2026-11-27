"""Finite arithmetic for arbitrarily long consecutive paid runs."""
from fractions import Fraction

from descent_macro import certificate, check, source, walk

M, D = 5367, 4096
FAR, INNER = 8897, 2395


def transfer(word, old, new):
    a, p, c = source(word)
    numerator = M*c + (new << a) - 3**p*old
    check(numerator % D == 0, "nonintegral carry")
    return certificate(a, p, numerator//D)[2]


def bridge(t, bias):
    a, p, c = source("P"*t)
    k = M*(c-7*3**p)+(bias << a)+10*3**(8+p)
    return certificate(a+12, 8+p, k)[2]


def main():
    edges = [("L", FAR, FAR)]
    edges.extend(("L"*4+"P"*h, FAR, FAR) for h in (1, 2, 3))
    edges.extend([("L"*4+"P", FAR, INNER), ("P", INNER, INNER), ("PPP", INNER, FAR)])
    for word, before, after in edges:
        print(word, before, after, transfer(word, before, after))
    z = -1-Fraction(3403*M, 3**8)
    v, bits = walk(z, 27)
    check(v == -10 and bits.count("1") == 12, "signed entry into three-cycle")
    v, bits = walk(-10, 3)
    check(v == -10 and bits.count("1") == 2, "signed-cycle induction")
    print("P to interior", bridge(1, INNER))
    print("PPP to free", bridge(3, FAR))
    check(8*M <= 5*(1 << 14), "r>=9 floor")
    for r in range(9):
        a, p, c = source("L"*r+"PP")
        check(4*3**p < 3*(1 << a), "short prefix slope")
        check(4*(3**p*17+c) < (3*17+1)*(1 << a), "short prefix floor")


if __name__ == "__main__":
    main()
