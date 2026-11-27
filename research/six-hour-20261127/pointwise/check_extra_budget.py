"""Exact ordinary extra-budget controls, independent of the baseline author's program."""
from collections import Counter
from fractions import Fraction
import json

PHASES=((17,0,0),(25,1,1),(37,2,2),(55,3,3),(41,4,5),(61,5,6),(91,6,7))
LAMBDA=Fraction(2048,2187)

def need(ok, msg):
    if not ok:
        raise ArithmeticError(msg)

def data(R,t,a,h,z):
    k,delta=divmod(R-a,7)
    H=11*k+h
    p=R-delta
    V=2**(H+1)*3**delta*z
    return 2*3**R*z-t,V-17,delta,p,H

def signed_first_17(m):
    u=m
    q=d=0
    seen=set()
    while u!=17 and u not in seen:
        seen.add(u)
        v=3*u-1
        e=(v&-v).bit_length()-1
        u=v>>e
        q+=1
        d+=e
    return (q,d) if u==17 else None

def all_honest_minima(target,R,bound,mark=None):
    """BFS, retaining counts of histories that do or do not pass the prescribed mark.

    A candidate y<=bound reaching a current vertex v in <=h more odd steps needs
    v+1 <= (3/2)^h*(bound+1); use this inclusive pruning before every push.
    An optional (inverse depth, value) marks passage through the principal root.
    """
    states=Counter({(target,mark is None or mark==(0,target)):1})
    minima=Counter()
    best=bound+1
    for i in range(R+1):
        for (u,saw),cnt in states.items():
            if u<best:
                best=u
                minima=Counter()
            if u==best:
                minima[saw]+=cnt
        if i==R:break
        h=R-i-1
        cap=(min(best,bound)+1)*3**h//2**h-1
        future=Counter()
        for (u,saw),cnt in states.items():
            if u%3==0:continue
            numerator=u*2
            while numerator<=3*cap+1:
                if numerator%3==1:
                    v=(numerator-1)//3
                    future[v,saw or mark is None or mark==(i+1,v)]+=cnt
                numerator*=2
        states=future
    need(best<=bound,(target,R,'no witness within the input bound'))
    return best,minima

def main():
    finite={m:signed_first_17(m) for m in range(1,78,2)}
    signed={m:v for m,v in finite.items() if v is not None}
    expected={17:(0,0),21:(3,5),23:(1,2),25:(6,10),31:(2,4),33:(7,12),37:(5,9),41:(3,6),45:(8,14),49:(6,11),55:(4,8),61:(2,5),67:(7,13),73:(5,10)}
    need(signed==expected,'signed table')
    c3=c1=0
    for R in range(7,30):
        for t,a,h in PHASES:
            for z in (1,2,3,5,7,11):
                x,n,delta,p,H=data(R,t,a,h,z)
                V=n+17
                for s in (0,1,2,3):
                    m,counts=all_honest_minima(x,R+s,n,(p,n))
                    local,_=all_honest_minima(n,delta+s,n)
                    need(m==local and counts[False]==0,(R,t,z,s,m,local,counts))
                    c3+=1
                    if s==1:
                        u={0:V-17,1:4*V//3-23,3:32*V//27-21,6:1024*V//729-25}.get(delta)
                        closed=(2*u-1)//3 if u is not None and u%3==2 else n
                        need(m==closed,('first extra',R,t,z,m,closed))
                        c1+=1
    sharp,passage=all_honest_minima(61219,11,57327,(7,57327))
    need(sharp==45295 and not passage[True],'fourth-step sharpness')
    allone=0
    for k in (1,2):
        for t,a,h in PHASES:
            R=7*k+a
            H=11*k+h
            for s in range(1,13):
                z=16*pow(2**(H+1),-1,3**s)%3**s
                x,n,_,_,_=data(R,t,a,h,z)
                exact=(2**s*(n+1))//3**s-1
                m,_=all_honest_minima(x,R+s,exact)
                need(m==exact,(k,t,s,z,m,exact))
                allone+=1
    need(182*1407*LAMBDA**200<1,'window at s=0')
    need(Fraction(1456,1407)*Fraction(3,2)*LAMBDA**7<1,'window s-increment')
    need(Fraction(1408,1401)*LAMBDA<1,'window b-increment')
    print(json.dumps({'signed_odd_inputs_through_77':39,'signed_first_17':len(signed),
        'composition_and_passage_checks':c3,'extra_one_closed_form_checks':c1,
        'extra_one_to_twelve_sharp_family_checks':allone,'fourth_extra_exact_minimum':sharp,
        'fourth_extra_winner_passes_principal':bool(passage[True]),'window_rational_checks':3},sort_keys=True,indent=2))

if __name__=='__main__':main()
