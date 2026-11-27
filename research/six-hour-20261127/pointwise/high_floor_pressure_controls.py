"""Finite true-orbit controls for the all-power principal pressure result."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb
import json

def check(ok, tag):
    if not ok: raise ArithmeticError(tag)

def odd_step(x):
    z=3*x+1;e=(z&-z).bit_length()-1
    return e,z>>e

def native():
    rows=Counter()
    for n in range(1,8):
        for w in product((1,2,3,4),repeat=n):
            A=B=0
            for e in w:
                B=3*B+(1<<A);A+=e
            m=((1<<A)-B)*pow(3**n,-1,1<<(A+1))%(1<<(A+1))
            x=m; states=[m]; clock=0; G=Q(0); correction=Q(1)
            for i,e in enumerate(w):
                G+=Q(1<<clock,3**(i+1));correction*=Q(3*x+1,3*x)
                actual,x=odd_step(x);clock+=actual
                check(actual==e,'native principal source')
                states.append(x)
            check(G/m==correction-1 and x<2*3**n,'source tilt and terminal floor')
            Z=Q(1<<A,m)
            check(Z==Q(3**n,x)*correction,'centered payoff')
            for H in (1,8,16,99):
                if min(states)<=H:
                    check(Z*H>=1<<n,'small-site cost')
                    rows['excluded_physical_floors']+=1
            for z in (Q(0),Q(1,8),Q(1),Q(5)):
                payoff=Q(1<<A,1)/(m+z*G)
                check(payoff*2*max(1,z)>=1,'all-power lower floor')
                if z:
                    check(payoff<=3**n*max(1,1/z),'positive tilt upper')
                rows['exact_tilt_word_rows']+=1
    return dict(rows)

def gate():
    states={0:1}
    gamma4=Q(7,8)**4*Q(7,6)**3
    for n in range(1,81):
        D=7*n//4; cumulative=0; new={}
        for A in range(1,D+1):
            cumulative+=states.get(A-1,0)
            new[A]=cumulative
        states=new
        mass=sum(Q(a,1<<k) for k,a in states.items())
        check(mass**4<=gamma4**n,'native gate exponential upper')
        check(mass>=Q(comb(D-1,n-1),n*(1<<D)),'rotation lower')
    return dict(rational_depths=80)

def octaves():
    output=[]
    for n in (6,9,12,15):
        counts=Counter()
        low=None
        for v in range((1<<n)+1,1<<(n+1),2):
            x=v;minimum=x;A=0
            for _ in range(n):
                e,x=odd_step(x);A+=e;minimum=min(minimum,x)
            if minimum>3 and A>=3*n//2 and v<(1<<(A+1)):
                counts['genuine_source_rows']+=1
                low=min(minimum,low) if low is not None else minimum
                check(Q(1<<A,v)>=Q(1<<(3*n//2),1<<(n+1)),'finite octave payoff')
        output.append(dict(odd_depth=n,initial_bits=n,sampled=1<<(n-1),
                           kept=counts['genuine_source_rows'],least_observed_floor=low))
    return output

if __name__=='__main__':
    print(json.dumps(dict(native=native(),gate=gate(),ordinary_octaves=octaves()),indent=2,sort_keys=True))
