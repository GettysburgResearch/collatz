"""Independent small integer controls for the reflected-17, positive-root spectrum.

Use one maximal positive pool for all budgets. Match the two genuine itineraries
at their *first* signed 17 and reconstruct each certified success at all phases.
"""
from fractions import Fraction
from functools import cache
import json

PHASES=(17,25,37,55,41,61,91)
PHYSICAL=(0,1,2,3,5,6,7)


def check(test, message):
    if not test:
        raise RuntimeError(str(message))


def step(x, sign):
    u=3*x+sign
    power=0
    while not u%2:
        u//=2
        power+=1
    return u,power


def walk(x, sign, n):
    for _ in range(n):
        x,_=step(x,sign)
    return x


@cache
def signed(m):
    state=m; clocks=0; visited=set(); prefix=[]
    while state!=17 and state not in visited:
        visited.add(state)
        state, e=step(state,-1)
        clocks+=e
        prefix.append(e)
    if state==17:
        return len(prefix),clocks,tuple(prefix)
    return None


def certificate(h,s,w,c,d,E,l):
    modulus=3**h
    r=((-1-w)*pow(2,-d-E,modulus))%modulus
    for phase,(t,h0) in enumerate(zip(PHASES,PHYSICAL)):
        k=max(l,1); R=7*k+phase; H=11*k+h0
        # The first congruence is on N=n/3**s; the second on its free quotient.
        modulus2=1<<(H+1)
        q=((-17*pow(3,-s,modulus2)-r)*pow(modulus,-1,modulus2))%modulus2
        N=r+modulus*q
        while True:
            n=N*3**s
            v=(N<<(d+E))+w
            y=((v+1)*2**h)//3**h-1
            if 0<y<n:break
            N+=modulus*modulus2
        z=(n+17)//modulus2; X=2*3**R*z-t
        check((n+17)%modulus2==0 and (v+1)%modulus==0 and z%3!=0,('CRT',h,s,w,t))
        check(walk(y,1,h)==v and walk(v,1,s)==(n<<d)+c,('positive pieces',h,s,w,t))
        check(walk(y,1,R+s+h)==X==walk(n,1,R),('actual endpoints',h,s,w,t))
    return len(PHASES)


def cone():
    buckets={u:[] for u in PHASES}
    for m in range(1,92,2):
        if m in PHASES:continue
        u=m;seen=set()
        while u not in PHASES and u not in seen:
            seen.add(u); u,_=step(u,-1)
        if u in buckets:buckets[u].append(m)
    from math import prod
    def factors(lst):return prod(Fraction(3*x-1,3*x) for x in lst)
    ratio=[]
    for b in range(1,15):
        small=buckets[PHASES[b%7]]
        lower=(small+list(range(93,93+2*b,2)))[:b]
        ratio.append(factors(lower)/factors([PHASES[j%7] for j in range(b)]))
    check(min(ratio)==Fraction(9730834,9637047) and ratio.index(min(ratio))==6,ratio)
    return {'first_marked':buckets,'worst_product':str(min(ratio))}


def spectrum():
    ranks=[set() for _ in range(7)]; total=[0]*7; crts=0; signatures=set(); cutpoints=set()
    for w in range(1,194,2):
        s=E=0; c=w;seen=set()
        while True:
            if c==1 and 2**(E+1+6)>=3**(s+6):break
            check(c==1 or c not in seen,('cycle in finite pool',c)); seen.add(c)
            c,e=step(c,1); E+=e; s+=1
            ceiling=(3**(s+6)-1)//2**(E+6)
            for d in range(1,ceiling.bit_length()):
                m=(17<<d)-c
                if m<=0:continue
                cutpoints.add(m); path=signed(m)
                if path is None:continue
                b,p,ex=path
                if b%7 or p!=11*(b//7)+d:continue
                l=b//7
                signatures.add((m,d,b,p))
                # Two independent exact forms of the signed normalized carry.
                B=Fraction(17*2048**l,2187**l);clock=0
                for j,e0 in enumerate(ex):
                    B+=Fraction(2**clock,3**(j+1)*2**d); clock+=e0
                check(B==Fraction(m,2**d),('carry form',m,d,ex))
                check(B<=17*(7*l+1)*Fraction(2048,2187)**l,('first arrival tail',m,d,ex))
                for h in range(7):
                    if w*2**h>=17*3**h or (1<<(d+E+h))>=3**(s+h):continue
                    ranks[h].add(s);total[h]+=1
                    crts+=certificate(h,s,w,c,d,E,l)
    return {'success_ranks':[sorted(x) for x in ranks],'all_success_tuples':total,'all_CRT_phase_instances':crts,'distinct_signed_inputs':len(cutpoints),'distinct_matched_grades':len(signatures)}


def main():
    four=[]
    for m in range(1,117,2):
        x=signed(m)
        if x and x[0]>=7:four.append((m,*x[:2]))
    result={'four_extra_delayed_magnitudes':four,'cone':cone(),'spectrum':spectrum()}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':main()
