"""Exact word rotation, ordered rational controls, and both Farey parents."""

from fractions import Fraction
from itertools import combinations
from math import gcd, lcm, prod

from check_every_sublap import states


def require(ok, what):
    if not ok:
        raise AssertionError(what)


def carry(a):
    c, m = 0, 0
    for h in a:
        c = 3*c + (1 << m)
        m += h
    return c, m


def run():
    parents = ordered = crosses = characters = 0
    for p in range(2, 9):
        for A in range((3**p).bit_length(), 2*p + 1):
            for cuts in combinations(range(1,A), p-1):
                stops = (0,) + cuts + (A,)
                a = tuple(y-x for x,y in zip(stops, stops[1:]))
                if any(a > a[i:] + a[:i] for i in range(1,p)):
                    continue
                xs = states(a)
                if len(set(xs)) != p or min(xs) <= 1:
                    continue
                for t in range(1,p):
                    base = t*A // p
                    for n in {base, base+1}:
                        D = abs((1 << n) - 3**t)
                        words = [(a+a)[i:i+t] for i in range(p)]
                        c, m = zip(*(carry(w) for w in words))
                        ratio = [Fraction(2)**(m[i]-n)*xs[(i+t)%p]/xs[i]
                                 for i in range(p)]
                        require(prod(ratio) == Fraction(2)**(t*A-p*n), 'clock index')
                        for i in range(p):
                            j = (i+1)%p
                            require((c[j] << a[i]) == 3*c[i]+(1 << m[i])-3**t,
                                    'exact carry rotation')
                            if m[i]<n and m[j]<=n:
                                q=D//gcd(D,c[i]); r=D//gcd(D,c[j])
                                require(gcd(D,(1 << (n-m[i]))-1) % (D//lcm(q,r)) == 0,
                                        'saturated pair divisor')
                                characters += 1
                        if p*n-t*A==1 or p*n-t*A==-1:
                            parents += 1
                        if p*n<=t*A:
                            continue
                        if max(ratio)<1:
                            i=xs.index(min(xs)); j=(i+1)%p
                            require(a[i]==1 and m[i]<n and m[j]<=n, 'two minimum arcs')
                            ordered += 1
                        else:
                            require(any(ratio[i]>1>ratio[(i+1)%p] for i in range(p)),
                                    'mixed signs and exact crossing')
                            crosses += 1
    require(min(parents,ordered,crosses,characters)>0, 'nonempty controls')
    print(f'{parents} determinant-one parents, {ordered} ordered upper clocks, '
          f'{crosses} mixed upper clocks, {characters} exact adjacent carry divisors')


if __name__ == '__main__':
    run()
