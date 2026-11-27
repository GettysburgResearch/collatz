"""Exact small orbits and large factored certificates for independent parity clocks."""
from fractions import Fraction
from math import gcd,prod
import json


def require(q,msg):
    if not q:
        raise ArithmeticError(msg)

def raw(bits):
    c=0
    for t,a in enumerate(bits):
        c=3*c+(1<<t) if a else c
    return c

def mechanical(n,b,primes):
    temp=[((t+1)*b)//n-(t*b)//n for t in range(n)]
    phases=[t for t in range(1,n) if temp[t-1:t+1]==[1,0]]
    phases.sort(key=lambda t:(t*b)%n)
    return temp,[t-1 for t in phases[:len(primes)]]

def run(n,b,primes,literal=True):
    template,markers=mechanical(n,b,primes)
    require(len(markers)==len(primes) and gcd(n,b)==1,'mechanical slots')
    a,base=1<<n,3**b
    ns=prod(primes)
    coeffs=[(1<<t)*3**sum(template[t+1:]) for t in markers]
    c0=raw(template)
    require(a>base,'positive')
    x=Fraction(c0,a-base)
    # Repeating impulse period ell, phase j=0 in a cell.
    for di,ell in zip(coeffs,primes):
        x+=Fraction(di*base**(ell-1),a**ell-base**ell)
    full=(a-base)*prod((a**ell-base**ell)//(a-base) for ell in primes)
    mean=ns*c0+sum((ns//ell)*d for ell,d in zip(primes,coeffs))
    require(x.denominator==full//gcd(a-base,mean),'exact complete denominator')
    if not literal:
        return dict(period=n*ns,odd_count=b*ns,clock_gcd=gcd(n*ns,b*ns),
                    full_q_bits=x.denominator.bit_length(),
                    divisor_bits=full.bit_length(),cell_primes=primes)
    y=x
    bits=[]
    lo=hi=None
    for j in range(ns):
        cell=template.copy()
        mask=[j%ell==0 for ell in primes]
        for use,t in zip(mask,markers):
            if use:
                cell[t:t+2]=[0,1]
        cc=c0+sum(d for d,use in zip(coeffs,mask) if use)
        require(cc==raw(cell),'superposition')
        end=(base*y+cc)/a
        for bit in cell:
            require(y.numerator%2==bit,'native rational parity')
            if bit:
                lo=y if lo is None else min(lo,y)
                hi=y if hi is None else max(hi,y)
            y=(3*y+1)/2 if bit else y/2
        require(y==end,'physical cell terminal')
        bits.extend(cell)
    require(y==x,'physical closure')
    alpha=Fraction(b,n)
    if Fraction(len(primes),n)<min(1-alpha,2*alpha-1):
        require(all(bits[j] or bits[(j+1)%len(bits)] for j in range(len(bits))),
                'every actual odd division is one or two')
    for ell in primes:
        shift=len(bits)//ell
        require(any(bits[j]!=bits[(j+shift)%len(bits)] for j in range(len(bits))),
                'least period')
    require(Fraction(raw(bits),(1<<len(bits))-3**sum(bits))==x,'literal complete denominator')
    require(hi>2*lo,'strictly crosses one octave')
    return dict(period=len(bits),odd_count=sum(bits),cycle_denominator_bits=x.denominator.bit_length(),
                odd_ratio_millionth_floor=(hi.numerator*lo.denominator*10**6)//(hi.denominator*lo.numerator),
                smallest_odd_floor=lo.numerator//lo.denominator,primes=primes)

if __name__=='__main__':
    # Positive upper convergents to log_2(3), plus a small positive template.
    literal=[run(8,5,[5,7]),run(65,41,[5]),
             run(65,41,[5,7]),run(65,41,[5,7,11])]
    compact=[run(485,306,[5,7,11,13],False),
             run(24727,15601,[5,7,11,13,17],False)]
    print(json.dumps(dict(physical_cycles=literal,compact_denominator_certificates=compact),
                     indent=2,sort_keys=True))
