"""Reconstruct and verify an exact primitive high-floor zero-norm cycle."""
from fractions import Fraction
from itertools import accumulate, product
from math import gcd, lcm
import json


def carry(gaps):
    result = position = 0
    for gap in gaps:
        result = 3*result + 2**position
        position += gap
    return result


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def check_templates():
    w = (1, 1, 1, 2, 1, 2, 2, 2)
    d = tuple(accumulate((0, *w)))[:-1]
    count = 0
    for length in range(6):
        for prefix in product((1, 2, 3, 4, 8), repeat=length):
            n, S = 1+length, sum(prefix)
            z, s = 3**n, 2**S
            D = 4096*s**8-z**8
            if D <= 0:
                continue
            P = carry((*prefix, 1))
            f = z*z+4*z*s+8*s*s
            V = (8*s*s-z*z)*(8*s*s+z*z)*(z*z-4*z*s+8*s*s)
            B = z**5-2*s*z**4+4*s*s*z**3+8*s**3*z*z-32*s**4*z+128*s**5
            W = sum(2**di*s**i*z**(7-i) for i, di in enumerate(d))
            C = carry(tuple(t for last in w for t in (*prefix, last)))
            require(D == f*V and C == P*W == P*f*B, 'full evaluated factorization')
            require(7 % gcd(V, B) == 0, 'residual gcd divisibility')
            require(7*(D//gcd(C,D)) > 4*z*z, 'complete denominator bound')
            count += 1
    return count


def run():
    a, b = 485, 306
    n, S = b//2, (a-3)//2
    w = (1, 1, 1, 2, 1, 2, 2, 2)
    z, s = 3**n, 2**S
    seed_d = tuple(accumulate((0, *w)))[:-1]
    W = sum(2**d*s**i*z**(7-i) for i, d in enumerate(seed_d))
    common = z*z + 4*s*z + 8*s*s
    require(W % common == 0 and (z**4+64*s**4) % common == 0, 'common factor')
    A, p = a*4, b*4
    D = 2**A - 3**p
    require(D>0 and gcd(A,p)==4 and 3**p>3*81*D, 'exact floor or clock')
    # Fix the first two entries. Distribute the remaining ones/twos evenly.
    m, total = n-3, S-3
    tail = tuple((i+1)*total//m - i*total//m for i in range(m))
    result = []
    for start in ((1,2), (2,1)):
        prefix = start + tail
        gaps = tuple(h for last in w for h in (*prefix,last))
        require(len(gaps)==p and sum(gaps)==A and set(gaps)=={1,2}, 'gap clocks')
        require(all(gaps != gaps[i:]+gaps[:i] for i in range(1,p) if p%i==0), 'primitivity')
        P = carry((*prefix,1))
        C = carry(gaps)
        require(C==P*W, 'full carry')
        q0 = Fraction(C,D)
        q = low = q0
        for gap in gaps:
            require(q.numerator%2==q.denominator%2==1, 'parity')
            q = (3*q+1)/2**gap
            low = min(low,q)
        require(q==q0 and low>81 and q0.denominator>1, 'ordinary rational closure')
        result.append({'P':P, 'denominator':q0.denominator, 'floor_of_minimum':low//1})
    R = D//gcd(D,W)
    require(abs(result[0]['P']-result[1]['P'])==2*3**(n-2), 'prefix swap')
    require(lcm(*(r['denominator'] for r in result))==R, 'complete denominator lcm')
    return {'arbitrary_prefix_templates_checked':check_templates(), 'a':a,'b':b,'odd_steps':p,'total_clock':A,'prefix_sum':S,
            'exact_uniform_floor':81,'prefixes':[{'initial_gaps':list(s0),
            'minimum_floor':r['floor_of_minimum'],'denominator_bits':r['denominator'].bit_length()}
            for s0,r in zip(((1,2),(2,1)),result)]}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2))
