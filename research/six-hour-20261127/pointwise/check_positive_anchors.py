"""Rational and ordinary integer checks for the adaptive positive-anchor results."""
from fractions import Fraction
from itertools import product
import json
from check_extra_budget import PHASES,all_honest_minima,data,need,signed_first_17

CYCLE=[r[0] for r in PHASES]

def odd_step(x,sign=1):
    y=3*x+sign
    e=(y&-y).bit_length()-1
    return y>>e,e

def pool(m):
    states=set()
    for w in range(1,m+1,2):
        x=w
        seen=set()
        while x not in seen:
            seen.add(x)
            x,_=odd_step(x)
        need(x==1,('unexpected positive cycle',w,x))
        states.update(seen)
    return sorted(states)

def cone_screen():
    buckets={t:[] for t in CYCLE}
    for w in range(1,92,2):
        if w in CYCLE:continue
        x=w
        seen=set()
        while x not in CYCLE and x not in seen:
            seen.add(x)
            x,_=odd_step(x,-1)
        if x in CYCLE:buckets[x].append(w)
    need(buckets=={17:[21,23,31,83],25:[45,67],37:[],55:[],41:[],61:[33,49,73],91:[]},'signed entry classes')
    f=lambda x:Fraction(3*x-1,3*x)
    ratios=[]
    for b in range(1,15):
        small=buckets[CYCLE[b%7]]
        values=(small+list(range(93,93+2*b,2)))[:b]
        num=den=Fraction(1)
        for x in values:num*=f(x)
        for i in range(b):den*=f(CYCLE[i%7])
        ratios.append(num/den)
    need(min(ratios)>Fraction(1009,1000) and ratios.index(min(ratios))==6,'product comparison')
    return buckets,min(ratios)

def zero_screen():
    cpool=pool(15)
    need(cpool==[1,3,5,7,9,11,13,15,17,23,35,53],'ordinary cheap pool')
    count=0
    seven=[]
    for D,c in product(range(1,6),cpool):
        if not (1<<D)<c<17*(1<<D):continue
        count+=1
        m=17*(1<<D)-c
        sig=signed_first_17(m)
        if sig is None:continue
        b,e=sig
        if b%7==0:
            seven.append([D,c,b,e])
            need(e-11*(b//7)!=D,(D,c,'compatible signed path'))
    need(seven==[[1,17,0,0],[2,35,7,12]],'first hits of matching odd residue')
    return count,seven

def small_positive_scan(X,R,a,N):
    """Computed values <=N, retaining only the first anchor hit per positive source."""
    best=None
    for w in range(1,(N*a//X)+1,2):
        u=w;E=0
        for q in range(R+1):
            if u==a:
                disp=(X-a)*(1<<E)
                need(disp%3**q==0,('integrality',X,R,a,w,q))
                y=w+disp//3**q
                if y<=N:best=y if best is None else min(best,y)
                break
            u,e=odd_step(u)
            E+=e
    return best

def anchored_full(R,t,n,X,depth,A):
    best=n
    H=((R-CYCLE.index(t))//7)*11+PHASES[CYCLE.index(t)][2]
    for w in range(1,A+17,2):
        u=w;E=0
        for j in range(depth+1):
            if j>0:
                for D in range(u.bit_length()+1):
                    c=u-(A<<D)
                    if D==0:
                        if c!=0:continue
                    else:
                        if not 0<c<17*(1<<D):continue
                        m=17*(1<<D)-c
                        if m%2!=1:continue
                        v=m;clock=0
                        for _ in range(R):
                            v,e=odd_step(v,-1)
                            clock+=e
                        if v!=t or clock!=H+D:continue
                    numerator=(n-A)*(1<<(D+E))
                    need(numerator%3**j==0,('source anchor integrality',w,j))
                    best=min(best,w+numerator//3**j)
            u,e=odd_step(u)
            E+=e
    return best

def main():
    buckets,ratio=cone_screen()
    nc,seven=zero_screen()
    cp=0
    for R in range(1,7):
        for a in range(1,18,2):
            for z in (1,2,5):
                X=a+2*3**R*z
                actual,_=all_honest_minima(X,R,X)
                for N in {X,actual,actual-1,max(1,actual//2)}:
                    got=small_positive_scan(X,R,a,N)
                    need(got==(actual if actual<=N else None),('positive terminal',R,a,z,N,got,actual))
                    cp+=1
    cz=both=0
    for k in (1,2):
        for t,a,h in PHASES:
            R=7*k+a
            H=11*k+h
            for s in range(1,13):
                z=17*pow(2**(H+1),-1,3**s)%3**s
                x,n,delta,_,_=data(R,t,a,h,z)
                need(delta==0 and n%3**s==0 and z%3!=0,'primitive zero anchor')
                actual,_=all_honest_minima(x,R+s,n)
                need(actual==n,('extra zero',R,t,z,s,n,actual))
                cz+=1
            for A in (1,3,5,13,45,49):
                for s in (2,5,8,9):
                    z=(A+17)*pow(2**(H+1),-1,3**s)%3**s or 3**s
                    x,n,_,_,_=data(R,t,a,h,z)
                    actual,_=all_honest_minima(x,R+s,n)
                    got=anchored_full(R,t,n,x,s,A)
                    need(got==actual,('adapted source anchor',R,t,A,s,got,actual))
                    both+=1
    print(json.dumps({'positive_endpoint_capped_minimum_checks':cp,'signed_phase_buckets':buckets,
      'least_raw_rational_product_margin':str(ratio),'zero_anchor_positive_pool':pool(15),
      'zero_anchor_signed_pairs':nc,'pairs_with_matching_odd_residue':seven,
      'unrestricted_exponent_zero_anchor_checks':cz,'positive_source_residue_checks':both},sort_keys=True,indent=2))

if __name__=='__main__':main()
