"""Exact bounded controls for the residue-profile proofs. Python standard library."""
import json
from collections import Counter
from fractions import Fraction
from math import gcd


def check(predicate, label):
    if not predicate:
        raise ValueError(label)


def numeric_checks():
    checks = [
        10**4 < 128 * 3**4,
        193**5 < 256 * 64**5,
        2**2079 < 3**1312,
        (3 * 2**20 + 1)**41 < 2**885,
        Fraction(19, 12) < Fraction(2079, 1312),
        Fraction(65, 41) < Fraction(609, 384),
        2**19 + 3**12 < 2**67,
        2**65 + 3**41 < 2**67,
        42000 * 22 < 2**20,
        33**32 > 2 * 32**32,
        12**4 > 2**5 * 5**4,
        4 * Fraction(33, 32) + 2 * Fraction(12, 5) < Fraction(2999, 1000)**2,
        1 + 5 * Fraction(10, 7) < Fraction(2999, 1000)**2 and 10**2 > 2 * 7**2,
        Fraction(4, 32) + Fraction(67, 100) < 1,
        10**6 + 2 < 2**20 and 200 * (10**6 + 1) < 225640000,
        Fraction(20, 32) + Fraction(67, 200) < 1,
    ]
    for i, passed in enumerate(checks):
        check(passed, ('exact constant', i))
    return len(checks)


def shifted(coeffs, t):
    p = len(coeffs)
    return [coeffs[(r-t) % p] * 2**((t + ((r-t) % p)) // p) for r in range(p)]


def add_monomial(coeffs, exponent, coefficient):
    quotient, remainder = divmod(exponent, len(coeffs))
    coeffs[remainder] += coefficient * 2**quotient


def controls():
    counts = Counter()
    for p in range(2, 13):
        for A in range(p+1, 2*p):
            D = 2**A - 3**p
            if D <= 0 or gcd(p, A) > 1:
                continue
            s = A-p
            for bits in range(1 << (p-1)):
                k = [0] + [(bits >> i) & 1 for i in range(p-1)]
                rs = [(-A*i) % p for i in range(p)]
                ds = [(A*i+r)//p + k[r] for i,r in enumerate(rs)] + [A]
                gaps = [b-a for a,b in zip(ds,ds[1:])]
                predicted = [1+(r<s)+k[(r-s) % p]-k[r] for r in rs]
                check(gaps == predicted, 'literal discrepancy gap')
                counts['profiles'] += 1
                if min(gaps) < 1:
                    continue
                counts['positive_gap_profiles'] += 1
                f = [2**v for v in k]
                diff = [a-b for a,b in zip(shifted(f,s),f)]
                for r, gap in zip(rs,gaps):
                    check(diff[r] == f[r]*(2**(gap-1)-1), 'positive filter')
                C = sum(3**(p-1-i)*2**ds[i] for i in range(p))
                M = gcd(C,D)
                if M > 1:
                    b = pow(p,-1,A)
                    c = (b*p-1)//A
                    x = (pow(2,b,M) * pow(3,-c,M)) % M
                    check(pow(x,p,M)==2%M and pow(x,A,M)==3%M, 'Bezout root')
                    check(sum(v*pow(x,j,M) for j,v in enumerate(f))%M==0, 'full gcd root')
                    counts['nonunit_common_gcd'] += 1
                support = [r for r in range(p) if k[r]]
                if not support:
                    continue
                u = support[0]
                for t in range(1,5):
                    if support != list(range(u,support[-1]+1,t)):
                        continue
                    v = u+t*len(support)
                    G = [a-b for a,b in zip(shifted(f,t),f)]
                    expected = [0]*p
                    for j in range(t):
                        add_monomial(expected,j,1)
                    add_monomial(expected,v,1)
                    add_monomial(expected,u,-1)
                    check(G==expected, 'progression filter')
                    if support[-1]>=s:
                        check(s%t==0 and u<t, 'high progression boundary')
                        if v>=p:
                            check(sum(abs(a) for a in G)<=t+1, 'wrapped height')
                            counts['wrapped_high_progressions'] += 1
                    counts['progression_presentations'] += 1
    # Neither chosen binomial-type comparison polynomial needs to work on all
    # irreducible factors at once. Full-modulus capture survives splitting.
    x, M = 2, 35
    Q1 = lambda z: (z-7)*(z-2)
    Q2 = lambda z: (z-9)*(z-37)
    check((x-7)*(x-9)%M==Q1(x)%M==Q2(x)%M==0, 'composite input')
    check(Q1(7)==Q2(9)==0 and Q1(9)*Q2(7)!=0 and Q1(9)*Q2(7)%M==0,
          'factorwise resultant capture')
    return dict(sorted(counts.items()))


def reduced_clock_controls():
    counts = Counter()
    for A in range(2,17):
        for mask in range(1, 1 << A, 2):
            positions = [i for i in range(A) if mask >> i & 1]
            p = len(positions)
            g = gcd(A,p)
            a, b = A//g, p//g
            D1 = 2**a - 3**b
            if g < 2 or D1 <= 0 or not b < a < 2*b:
                continue
            phase = min(range(p), key=lambda i:b*positions[i]-a*i)
            start = positions[phase]
            ds = sorted((d-start)%A for d in positions)
            data = [divmod(b*d-a*i,b) for i,d in enumerate(ds)]
            counts['positive_denominator_words'] += 1
            f = [0]*b
            for k,r in data:
                check(k >= 0, 'normalized reduced height')
                f[r] += 2**k
            for i,(k,r) in enumerate(data):
                nk,nr = data[(i+1)%p]
                gap = (ds[(i+1)%p]-ds[i])%A
                check(nr==(r-a+b)%b and gap==1+(r<a-b)+nk-k,
                      'visit-specific reduced gap')
            C = sum(3**(p-1-i)*2**d for i,d in enumerate(ds))
            M = gcd(C,D1)
            if M > 1:
                z = pow(b,-1,a)
                x = pow(2,z,M)*pow(3,-((z*b-1)//a),M)%M
                check(pow(x,b,M)==2%M and pow(x,a,M)==3%M, 'principal root')
                check(sum(v*pow(x,r,M) for r,v in enumerate(f))%M==0,
                      'principal projected numerator')
                counts['nonunit_projected_gcd'] += 1
    return dict(sorted(counts.items()))


if __name__=='__main__':
    print(json.dumps({'exact_parameter_checks':numeric_checks(),
                      'bounded_counts':controls(),
                      'noncoprime_counts':reduced_clock_controls()},sort_keys=True))
