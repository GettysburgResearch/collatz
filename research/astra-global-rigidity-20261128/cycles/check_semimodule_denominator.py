"""Check the complete-modulus semimodule formula, including nonprimitive clocks."""

from itertools import combinations
from math import gcd


def check(ok, label):
    if not ok:
        raise ValueError(label)


def centers(word):
    n, u = len(word), sum(word)
    g = gcd(n, u)
    N, U = n//g, u//g
    h = pow(U, -1, N)
    k = (1-h*U)//N
    e = f = 0
    heights = []
    for bit in word:
        heights.append((e, f))
        e += U-N*bit
        f = (f+k+h*bit)%g
    check(e == 0 and f == 0, 'cylinder does not close')
    emin, fmin = min(heights)
    ap = [(s-emin, (t-fmin)%g) for s,t in heights]
    keys = {(s%N, (t+h*(s//N))%g) for s,t in ap}
    check(len(keys) == n, 'not a complete Apery system')
    return N,U,g,h,k,ap


def one(word):
    n, u = len(word), sum(word)
    D = 2**n-3**u
    if D <= 1:
        return False
    N,U,g,h,k,ap = centers(word)
    lam = (2**N * pow(3,-U,D))%D
    z = (pow(2,h,D)*pow(3,k,D))%D
    check(pow(z,U,D)*pow(lam,k,D)%D == 2%D, 'two specialization')
    check(pow(z,N,D)*pow(lam,-h,D)%D == 3%D, 'three specialization')
    cap = max(s for s,t in ap)+N+1
    fibers = [set() for _ in range(cap+1)]
    for s,t in ap:
        while s <= cap:
            fibers[s].add(t)
            s,t = s+N, (t-h)%g
    check(len(fibers[-1])==g and len(fibers[-2])==g, 'full tail absent')
    # Each coordinate minimum determines its next edge by a test in the next class.
    for i,(s,t) in enumerate(ap):
        nb = word[i]
        dest = (s+U-nb*N, (t+k+nb*h)%g)
        check(dest == ap[(i+1)%n], 'word reconstruction')
    # Size thresholds descend to ordinary semimodules over the reduced clock.
    for s in range(cap-max(U,N-U)):
        check(len(fibers[s])<=len(fibers[s+U]), 'first count threshold')
        check(len(fibers[s])<=len(fibers[s+N-U]), 'second count threshold')
    apset = set(ap)
    stabilizers = [d for d in range(g) if {(s,(t+d)%g) for s,t in ap} == apset]
    word_periods = [j for j in range(n) if word[j:]+word[:j] == word]
    check(len(stabilizers)==len(word_periods), 'torsion stabilizer')
    vals=[]
    for chart in (0,1):
        zr=(z*pow(lam,chart,D))%D
        prev=set()
        val=0
        for s,row in enumerate(fibers):
            current={(t-chart*s)%g for t in row}
            val += pow(zr,s,D)*(sum(pow(lam,c,D) for c in current-prev)
                                -sum(pow(lam,c,D) for c in prev-current))
            prev=current
        vals.append(val%D)
    c=0
    for i,bit in enumerate(word):
        if bit:
            c=3*c+2**i
    check(gcd(D,*vals)==gcd(D,c), 'complete numerical gcd')
    if g==1:
        check(gcd(D,vals[0])==gcd(D,c), 'single primitive chart')
    return gcd(D,vals[0])>gcd(D,c)


def main():
    count=fail=0
    for n in range(3,12):
        for u in range(1,n):
            if 3**u >= 2**n-1:
                continue
            for inds in combinations(range(n),u):
                word=[int(i in inds) for i in range(n)]
                fail+=one(word)
                count+=1
    extra = [1]*7+[0,1]+[0]*11
    check(one(extra), 'missing explicit single-chart factor-five control')
    count += 1
    fail += 1
    print(f'{count} rooted words checked; {fail} have an extra factor in chart zero alone')


if __name__=='__main__':
    main()
