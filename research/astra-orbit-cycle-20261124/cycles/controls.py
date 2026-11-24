"""Exact finite controls for the written cycle-rotation exclusions."""
from fractions import Fraction
from itertools import product
from math import gcd

def check(condition, label):
    if not condition:
        raise RuntimeError(label)

def log_interval(n):
    z = Fraction(n - 1, n + 1)
    low = 2 * sum(z**(2*k+1) / (2*k+1) for k in range(128))
    return low, low + 2*z**257 / (257*(1-z*z))

def carry(bits):
    value = 0
    for i, bit in enumerate(bits):
        if bit:
            value = 3*value + 2**i
    return value

def verify():
    l2, u2 = log_interval(2)
    l3, u3 = log_interval(3)
    lo = Fraction(83130157078217,52449289519716)
    hi = Fraction(18340740190704,11571718688839)
    check(lo < l3/u2 < u3/l2 < hi, 'lo < l3/u2 < u3/l2 < hi')
    check(hi.numerator*lo.denominator-lo.numerator*hi.denominator == 1, 'hi.numerator*lo.denominator-lo.numerator*hi.denominator == 1')
    check(min(lo.denominator,hi.denominator) > 10**13, 'min(lo.denominator,hi.denominator) > 10**13')
    check(hi.denominator < 2**44 and l2 > Fraction(1,2), 'hi.denominator < 2**44 and l2 > Fraction(1,2)')
    check(4**512 > 9*2**94*3**512, '4**512 > 9*2**94*3**512')
    print("Exact Farey/log enclosure and middle-range comparison passed")
    triples = 0
    for a in range(17,512):
        for p in range(1,a+1):
            gap = 2**a-3**p
            if gap <= 0: break
            check(gap > 3**(a//2+1), (a,p))
            triples += 1
    print("Positive gaps checked at lengths 17..511:", triples)
    words = positive = integral = 0
    for a in range(1,17):
        for word in product(range(2), repeat=a):
            words += 1
            p = sum(word)
            gap = 2**a-3**p
            if not p or gap<=0: continue
            positive += 1
            c = carry(word)
            if c%gap: continue
            integral += 1
            check(all(word[i] != word[(i+1)%a] for i in range(a)), 'all(word[i] != word[(i+1)%a] for i in range(a))')
    print("Lengths 1..16: words, positive contracting, integral (all alternating):",
          words,positive,integral)

    overlap_checks = 0
    offenders_without_d = []
    for a in range(2,11):
        for bits in product(range(2), repeat=a):
            count = sum(bits)
            den = 2**a - 3**count
            if not count or den <= 0: continue
            d = den//gcd(den,carry(bits))
            for t in range(1,a):
                rot = bits[t:]+bits[:t]
                if bits == rot: continue
                m = a
                while m and bits[m-1]==rot[m-1]: m -= 1
                delta = abs(carry(bits[:m])-carry(rot[:m]))
                q = sum(bits[:m])
                span = (2**(m-q)-1)*(3**q-2**q)
                check(0<delta<=span<3**m, (bits,rot,m))
                check(d*delta%den==0, (bits,rot,d,delta,den))
                if delta%den and not offenders_without_d:
                    offenders_without_d.append((bits,rot,d,delta,den))
                overlap_checks += 1
    check(bool(offenders_without_d), "removing the denominator produced no countercontrol")
    repeated = (1,0,1,0)
    check(repeated[2:]+repeated[:2] == repeated and carry(repeated) == 4**2-3**2,
          "a period multiple has identical states at two different positions")
    print("R1 actual rotated pairs and first failure after dropping d:",overlap_checks,
          offenders_without_d[0])
    tested = primitive = 0
    for a in range(2,6):
        for p in range(1,a):
            n,m = 2**a,3**p
            if n<m: continue
            atoms = [carry(w) for w in product(range(2),repeat=a) if sum(w)==p]
            for r in range(3,7):
                for digits in product(atoms[:min(len(atoms),3)],repeat=r):
                    den = n**r-m**r
                    num = sum(c*n**i*m**(r-1-i) for i,c in enumerate(digits))
                    d = den//gcd(den,num)
                    for shift in range(1,r):
                        shifted = digits[shift:]+digits[:shift]
                        diff = [i for i in range(r) if digits[i]!=shifted[i]]
                        if len(diff)!=2: continue
                        i,j = diff
                        check(digits[i]==shifted[j] and digits[j]==shifted[i], 'digits[i]==shifted[j] and digits[j]==shifted[i]')
                        e = abs(digits[i]-digits[j])
                        g = gcd(r,j-i)
                        k = den//(n**g-m**g)
                        check(k>n**(r-g)>=n*n>e and (d*e)%k==0 and d>1, 'k>n**(r-g)>=n*n>e and (d*e)%k==0 and d>1')
                        tested += 1
                        primitive += all(digits[t:]+digits[:t]!=digits for t in range(1,r))
    print("Transposition cases and primitive cases:",tested,primitive)

if __name__ == "__main__":
    verify()
