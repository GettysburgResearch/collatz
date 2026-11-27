"""Exact diagnostics for ALL_SHIFT.md; no decimal logs and no optimiser."""
from fractions import Fraction
from math import gcd


def check(test, name):
    if not test:
        raise ValueError(name)


def check_necklace(bits):
    n = len(bits)
    total = sum(bits)
    D = 2**n - 3**total
    if total == 0 or D <= 0:
        return None
    rotations = [bits[i:]+bits[:i] for i in range(n)]
    if bits != min(rotations) or len(set(rotations)) != n:
        return None
    C = 0
    for j, b in enumerate(bits):
        C = (3*C + 2**j) if b else C
    g = gcd(C, D)
    d = D//g
    start = C//g
    phases = []
    x = start
    for b in bits:
        check(x % 2 == b and gcd(x, d)==1, "reduced parity")
        phases.append(x+d)
        x = (3*x+d)//2 if b else x//2
    check(x == start and len(set(phases))==n, "primitive closure")
    lower = Fraction(19,12)
    base = (min(phases).bit_length()-1)
    for h in range(1,n):
        s = sum(bits[i]!=bits[(i+h)%n] for i in range(n))
        check(s>0 and s%2==0, "mismatch count")
        for i in range(n):
            j=(i+h)%n
            check(phases[j] <= 3**(s//2)*phases[i], "paired ratio")
            R=0
            while bits[(i+R)%n]==bits[(j+R)%n]:
                R+=1
            check((phases[j]-phases[i]) % (2**R)==0, "prefix divisibility")
        H=sum(lower**j for j in range(s+1))
        check(n < H*(1+base+lower*s/2), "conservative all-shift estimate")
    return n-1


def main():
    check(2**19 < 3**12 and 3**41 < 2**65, "log3 enclosure")
    upper=Fraction(65,41)
    for T,b,s0 in [(217000000000,39,40),(2**100,101,132)]:
        check(2*T<=2**b, "dyadic shell")
        H=sum(upper**j for j in range(s0+1))
        W=11+Fraction(143,10)*b+upper*s0/2
        check(H*W<T and W>=Fraction(143,10), "uniform threshold")
        print("excluded mismatch cutoff",s0,"at n >=",T)
    words=shifts=0
    for n in range(2,13):
        for mask in range(1,2**n):
            bits=tuple((mask>>i)&1 for i in range(n))
            hits=check_necklace(bits)
            if hits is not None:
                words+=1
                shifts+=hits
    print("primitive positive rational necklaces",words,"all proper shifts",shifts)


if __name__ == "__main__":
    main()
