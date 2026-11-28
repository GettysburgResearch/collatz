"""Exact affine-center and native-denominator controls for moving sparse sums."""

from fractions import Fraction
from itertools import product
from math import gcd, lcm


def need(condition, message):
    if not condition:
        raise ArithmeticError(message)


def affine(w):
    a, b = Fraction(1), Fraction(0)
    for bit in w:
        a = a * (1+2*bit) / 2
        b = (b * (1+2*bit) + bit) / 2
    return a, b


def center(w):
    a, b = affine(w)
    return b/(1-a)


def outside_six(d):
    for p in [2, 3]:
        while d % p == 0:
            d //= p
    return d


def check_pieces(pieces):
    w = sum((a*k+b for a,k,b in pieces), ())
    u, n = sum(w), len(w)
    if 2**n <= 3**u:
        return None
    s = [center(a) for a, _, _ in pieces]
    x = center(w)
    kappa, U, ell, h = [], [], 0, 0
    for i, (a, k, b) in enumerate(pieces):
        ab, bb = affine(b)
        kappa.append(ab*s[i]+bb-s[(i+1)%len(s)])
        ell += k*len(a)+len(b)
        h += k*sum(a)+sum(b)
        U.append(Fraction(2**ell, 3**h))
    X = U[-1]
    V = kappa[-1]+sum((z*t for z,t in zip(kappa[:-1],U[:-1])),Fraction(0))
    need((X-1)*(x-s[0]-kappa[-1]) == V, 'cyclic center telescope')
    primitive = all(w[i:]+w[:i] != w for i in range(1,n))
    if primitive and len(pieces[0][0]) < n:
        need(any(kappa), 'primitive loop forced by vanishing centered jumps')
    H = lcm(*(r.denominator for r in kappa))
    D = 2**n-3**u
    dV = D//gcd(D,(H*V).numerator)
    need(outside_six((H*V/(X-1)).denominator) == dV, 'exact outside-six denominator')
    q = x.denominator
    b = (s[0]+kappa[-1]).denominator
    need((H*b*dV)%q==0 and (H*b*q)%dV==0, 'two-sided exact denominator comparison')
    return (primitive, any(z<0 for z in kappa), dV!=q, V==0)


def main():
    motifs = [(0,), (1,), (1,0), (1,1,0), (0,0,1)]
    connectors = [(), (0,), (1,0)]
    total = [0]*5
    for a,b,c in product(motifs, repeat=3):
        for k,l in product([1,3], [1,2]):
            for z in connectors:
                r = check_pieces([(a,k,z),(b,l,()),(c,2,(0,))])
                if r is not None:
                    total[0] += 1
                    for j, flag in enumerate(r, start=1):
                        total[j] += int(flag)
    need(all(total), 'each calibration label must be represented')
    # Distinct primitive half-windows of the same type can cancel the entire
    # nonprincipal cyclotomic determinant, despite a nonzero center difference.
    A = tuple(int(i in [0,1,6,8,9,10,11,12]) for i in range(13))
    B = tuple(int(i in [0,1,2,4,5,8,10,11]) for i in range(13))
    cA = int(affine(A)[1]*2**13)
    cB = int(affine(B)[1]*2**13)
    full = int(affine(A+B)[1]*2**26)
    Q = 2**13+3**8
    need((cA,cB)==(73213,14201) and cA-cB==4*Q, 'equal-type half difference')
    need(full==3**8*cA+2**13*cB and full%Q==0, 'nonprincipal full cancellation')
    need(all((A+B)[i:]+(A+B)[:i]!=A+B for i in range(1,26)), 'primitive half pair')
    need(sum(A)==sum(B)==8 and 2**26>3**16, 'positive half types')
    need(gcd(2**26-3**16,full)==Q, 'sharp remaining principal factor in the control')
    print(f'{total[0]} positive three-template displays; {total[1]} primitive, {total[2]} signed jump, '
          f'{total[3]} unequal compared denominators, {total[4]} zero centered sum.')
    print(f'Primitive (26,16) half pair has C_A={cA}, C_B={cB}, full C={full}, '
          f'full nonprincipal cancellation {Q}, reduced q={center(A+B).denominator}.')


if __name__ == '__main__':
    main()
