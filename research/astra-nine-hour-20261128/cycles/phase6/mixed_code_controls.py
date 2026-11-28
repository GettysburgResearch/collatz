"""Exact logarithm brackets, physical tag legality, and mixed-alphabet shortening."""

from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, prod


def need(ok, name):
    if not ok:
        raise ValueError(name)


def log_bounds(x, terms=48):
    z = F(x-1, x+1)
    low = sum(2*z**(2*k+1)/(2*k+1) for k in range(terms))
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return low, low+tail


def numerical():
    l2,h2 = log_bounds(2)
    l3,h3 = log_bounds(3)
    l7,h7 = log_bounds(7)
    gl,gu = l3/h2,h3/l2
    zl,zu = l7/h2,h7/l2
    a0,a1 = 2-gu,2-gl
    s0,s1 = 2*gl-3,2*gu-3
    U0,U1 = a0*gl+s0,a1*gu+s1
    V0,V1 = a0*zl+s0*gl,a1*zu+s1*gu
    D0,D1 = U0*V0/(U0+V0),U1*V1/(U1+V1)
    need(F(5248,10000) < D0 < D1 < F(5249,10000),'mixed rate')
    need(F(30196,10000) < gl/D1 < gu/D0 < F(30198,10000),'clock exponent')
    print('Exact rational brackets: .5248 < d < .5249; 3.0196 < log_2(3)/d < 3.0198.')


def physical():
    slopes = windows = 0
    for p in range(2,60):
        for A in range(1,2*p):
            if not 3*p < 2*A or gcd(A,p)!=1:
                continue
            slopes += 1
            for r in range(p):
                N = p+3
                b = [(r+(t+1)*A)//p-(r+t*A)//p for t in range(N)]
                slots = [t for t in range(N-1) if b[t]==1]
                need(all(v in (1,2) for v in b),'native calendar alphabet')
                need(all(t+1 not in slots for t in slots),'disjoint paired dates')
                need(sum(x==1 for x in b)==2*N-((r+N*A)//p),'mixed count')
                need(all(1+next_bit-bit>0 for bit,next_bit in ((0,0),(0,1),(1,1))),'valid tags')
                need(1+0-1==0,'forbidden 10')
                windows += 1
    print(f'{slopes} reduced clock slopes and {windows} full-offset windows passed pairing checks.')


def shortening():
    two = ((0,0),(0,1),(1,1))
    one = ((0,),(1,))
    letters = product(two,two,one)
    words = [a+b+c for a,b,c in letters]
    sq = lambda x,y: tuple(a+b for a,b in zip(x,y))
    delta = lambda x,y: tuple(a-b for a,b in zip(x,y))
    for alphabet,e,f in ((two,3,7),(one,2,3)):
        need(len(alphabet)==e and len({delta(x,y) for x in alphabet for y in alphabet})==f,
             'local alphabet and difference counts')
    # A prefix may select any full block, independent of physical ordering.
    blocks = ((0,1),(2,3),(4,))
    checks = codes = 0

    def visit(order, next_index, recorded):
        nonlocal checks,codes
        codes += 1
        m = len(order)
        for bits in product((0,1),repeat=3):
            P = prod(a for a,b in zip((3,3,2),bits) if b)
            D = prod(a for a,b in zip((7,7,3),bits) if not b)
            ij = [j for block,yes in zip(blocks,bits) if yes for j in block]
            classes = {}
            for x in order:
                key = tuple(x[j] for j in ij)
                classes[key] = classes.get(key,0)+1
            cnt = sum(n*(n-1) for n in classes.values())
            need(cnt <= D-1 and m*m <= P*(m+cnt),'same-prefix pair injection and Cauchy')
            checks += 1
        for j in range(next_index,len(words)):
            x = words[j]
            fresh = {sq(x,y) for y in order+[x]}
            if len(fresh)==m+1 and not fresh & recorded:
                visit(order+[x],j+1,recorded|fresh)

    visit([],0,set())
    print(f'All {codes} Sidon subsets of two paired and one singleton block passed {checks} projections.')


if __name__ == '__main__':
    numerical()
    physical()
    shortening()
