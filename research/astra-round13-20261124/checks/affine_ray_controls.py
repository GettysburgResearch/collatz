"""Independent small affine-ray checks. Requires SymPy."""
from fractions import Fraction
from itertools import accumulate, product
from math import gcd
from sympy import Poly, ZZ, symbols


def run():
    x = symbols('x')
    rays = evaluated = 0
    for p in (2, 3, 4):
        for gaps in product((1, 2, 3), repeat=p):
            for increments in product((0, 1), repeat=p):
                total = sum(increments)
                if total == 0:
                    continue
                A = sum(gaps)
                positions = tuple(accumulate((0, *gaps)))[:-1]
                exponents = tuple(accumulate((0, *increments)))[:-1]
                F = Poly(2**A*x**total - 3**p, x, domain=ZZ)
                H = Poly(sum(2**d*3**(p-1-i)*x**e
                             for i, (d, e) in enumerate(zip(positions, exponents))),
                         x, domain=ZZ)
                G = F.gcd(H)
                V, B = F.exquo(G), H.exquo(G)
                if V.degree() < total // gcd(total, gcd(A, p)):
                    raise ValueError("residual degree bound failed")
                R = abs(int(V.resultant(B)))
                if R <= 0:
                    raise ValueError("residual resultant vanishes")
                for prime in (2, 3):
                    while R % prime == 0:
                        R //= prime
                for k in range(12):
                    t = 2**k
                    v, b = int(V.eval(t)), int(B.eval(t))
                    cancellation = gcd(R, gcd(v, b))
                    original = Fraction(int(H.eval(t)), int(F.eval(t)))
                    if abs(v)//cancellation != original.denominator:
                        raise ValueError("specialized complete denominator mismatch")
                    evaluated += 1
                rays += 1
    return {'affine_rays': rays, 'denominators': evaluated}


if __name__ == '__main__':
    print(run())
