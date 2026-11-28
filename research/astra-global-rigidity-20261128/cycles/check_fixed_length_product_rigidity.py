"""Exact controls for dyadic scale grouping, clipped moments, and a genuine simple-pole shape."""
from fractions import Fraction as F
from math import prod
from check_unrestricted_triple_products import coefficients, require


def signed_coefficients(c, s):
    pos = [v for n,v in zip(c,s) for _ in range(max(0,n))]
    neg = [v for n,v in zip(c,s) for _ in range(max(0,-n))]
    return [(-1)**j*(a-b) for j,(a,b) in enumerate(zip(coefficients(pos), coefficients(neg)))]


def cost_offsets(reverse, stop=None):
    w = F(1); weights = []
    for j,a in enumerate(reverse):
        if j:
            w *= F(3, 2**a)
        weights.append(w if stop is None or j < stop else 0)
    return [sum(weights[:len(reverse)-i]) for i in range(len(reverse)+1)]


def degree_six():
    c = (-1,1,2,-1,0,0,-2,-2,3)
    for a in (8,32,113,257):
        reverse = (2,1,2,2,2,1,a,1)
        costs = reverse[::-1]
        dates = [sum(costs[:i]) for i in range(len(c))]
        require(sum(i*v for i,v in enumerate(c)) == sum(z*v for z,v in zip(dates,c)) == 0, 'alignment')
        s = cost_offsets(reverse); ss = cost_offsets(reverse,6)
        g = signed_coefficients(c,s); gs = signed_coefficients(c,ss)
        u = 2**a
        require(gs[1] == 0 and gs[2] != 0, 'simple clipped moment')
        require(g[1] == -F(2187,512*u), 'small first moment')
        require(g[2] == -F(3*(357149*u+1129221),65536*u), 'second expansion')
        R = F(357149*u,373248)-F(110357653,1097161728)
        approx = (g[2]/g[1]-g[3]/g[2])/4
        require(abs(approx-R)*u < 10**5, 'absolute approximation rate')
        require(R.denominator>1, 'approximation misses the integers')
    return len(c)


def double_moment():
    c = (8,-46,95,-84,27)
    s = cost_offsets([1]*4)
    require(sum(c)==0 and sum(i*v for i,v in enumerate(c))==0, 'moment control aligned')
    moms = [sum(v*x**j for v,x in zip(c,s)) for j in range(1,4)]
    require(moms[:2]==[0,0] and moms[2]!=0, 'genuine double cancellation')
    require(c[-1]%9==0 and c[0]%8==0, 'opposite-end congruences')


def grouped_rational_arc():
    # e_2=2e_1+e_slow. The Laurent polynomial becomes 0 on the extracted ray.
    for n in (81,100,144,256):
        b = int(n**0.5)
        U, V, small = 2**n, 2**(2*n+b), 2**b
        R = F(V, small*U) + F(U**2*small, V)
        require(R == U+1, 'slow coefficient grouping')
        for z in (F(1,7), F(1,2), F(3)):
            x,y = U*z,V*z**2
            require(y/(small*x)+x*x*small/y == x+1, 'weight-preserving arc')


def main():
    degree_six(); double_moment(); grouped_rational_arc()
    print('four aligned B6 simple-pole fixtures, B130 two-moment cancellation, and three-point scale arcs passed')


if __name__ == '__main__':
    main()
