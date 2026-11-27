"""Independent small-instance and exact constant checks for sparse centered grades."""
from collections import defaultdict, Counter
from fractions import Fraction as F
from itertools import product
from math import floor
import json


def need(p, reason):
    if not p:
        raise ArithmeticError(reason)


def numeral(steps):
    v, a = 0, 0
    for x in steps:
        v = 3*v+2**a
        a += x
    return v


def languages(m, first, binary):
    st = [(0, (first,), ())]
    while st:
        i, z, e = st.pop()
        if i == len(m):
            yield z,e
            continue
        largest = (2 if binary else m[i]+z[-1])
        for v in range(1,largest+1):
            new = m[i]+z[-1]-v
            if new>=0:
                st.append((i+1,z+(new,),e+(v,)))


def clipping_controls(binary, c):
    total=deep=nonbinary=forced_resets=0
    checks=0
    maxgrade=maxgap=0
    for t in (F(0),F(1,5),c,F(499,500)):
        alpha=F(31,53)
        phase=[t+i*alpha for i in range(8)]
        site=[w%1 for w in phase]
        m=[1+floor(y)-floor(x) for x,y in zip(phase,phase[1:])]
        for first in range(4):
            groups=defaultdict(list)
            for z,e in languages(m,first,binary):
                clip=tuple(min(v,1) if f<=c else 0 for v,f in zip(z,site))
                forced_resets += any(v>0 and f>c for v,f in zip(z,site))
                fake=tuple(k+u-v for k,u,v in zip(m,clip,clip[1:]))
                need(all(1<=v and (not binary or v<=2) for v in fake),'clipped language')
                key=(z[0],z[-1],tuple((i,v) for i,v in enumerate(z) if v+site[i]>1+c))
                v0=z[0]-clip[0]
                pair=(numeral(e),numeral(fake))
                groups[key].append(pair)
                total +=1
                deep += (max(z)>=2)
                nonbinary += (max(e)>=3)
                maxgrade=max(maxgrade,max(z))
                maxgap=max(maxgap,max(e))
            for (head,tail,record),rows in groups.items():
                h=head-(min(head,1) if site[0]<=c else 0)
                need(len(set(x-2**h*y for x,y in rows))==1,'actual versus clipped translation')
                need(len(set(rows))==len(rows),'clipped path ambiguity')
                hits=Counter(x+y for x,_ in rows for y,_ in rows)
                fake=Counter(x+y for _,x in rows for _,y in rows)
                need(sorted(hits.values())==sorted(fake.values()),'affine pair sum transport')
                checks +=1
    return dict(paths=total,deep_paths=deep,with_gap_at_least_three=nonbinary,
                largest_grade=maxgrade,largest_gap=maxgap,records=checks,
                high_phase_nonzero_resets=forced_resets)


def constants(eta,tau,delta,gamma,mask_bits):
    lo=F(19,12)
    retention=1-2*delta-delta/tau
    separation=eta-delta*(3+eta)-(4+eta)*tau/lo
    C=(5*eta/lo+gamma*(1-eta)+(4+eta)*mask_bits*tau/lo)/(3+eta)
    consumer=1-(3+delta)*C
    need(min(retention,separation,consumer)>0,'nonpositive strict margin')
    return {k:str(v) for k,v in dict(retention=retention,separation=separation,
                                      count_upper=C,period_contradiction=consumer).items()}


def run():
    need(2**19<3**12,'slope lower bound')
    # At c=16/25, use alpha0 < .584963 in c log(5/2)+alpha0 log(12/5).
    need(3**1000000<2**1584963,'slope upper bound')
    need(5**55037*2**529926 < 3**414987,'unrestricted energy 19999/20000')
    return dict(binary=clipping_controls(True,F(49,50)),
        unrestricted=clipping_controls(False,F(16,25)),
        binary_constants=constants(F(1,10000),F(1,80000),F(1,100000),F(999,1000),21),
        any_valuation_constants=constants(F(1,1000000),F(1,4000000),F(1,10**7),F(19999,20000),28))

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
