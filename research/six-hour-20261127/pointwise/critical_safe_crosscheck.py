"""Independent exhaustive checks of physical affine rows and nonuniform block composition."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import comb
import json

def require(value,message):
    if not value: raise ValueError(message)

def orbit(x,s):
    y=x;h=0;word=[];aff=0
    for _ in range(s):
        v=3*y+1;e=(v&-v).bit_length()-1
        aff=3*aff+(1<<h);h+=e;y=v>>e;word.append(e)
    require((1<<h)*y==3**s*x+aff,"affine identity")
    return y,h,tuple(word),aff

def word_rows(count):
    for m in range(5,14):
      starts=range(2**m+1,2**(m+1),2);N=2**(m-1)
      for s in range(1,min(6,m//2)+1):
        data=[(x,*orbit(x,s)) for x in starts];words=Counter((h,w) for x,y,h,w,A in data)
        retained=F(0)
        for h in range(s,m):
            inrow=[(w,n) for (v,w),n in words.items() if v==h]
            require(len(inrow)==comb(h-1,s-1),"missing full word")
            require(all(n==N//2**h for w,n in inrow),"incorrect uniform multiplicity")
            retained+=F(comb(h-1,s-1),2**h)
            count["complete_words"]+=len(inrow)
        overflow=sum(h>=m for x,y,h,w,A in data)
        require(F(overflow,N)==1-retained,"finite complementary overflow")
        count["overflow_octaves"]+=1
        for (h,w),n in words.items():
            if h==m and F(n,N)!=F(1,2**h):count["detect_excess_one_bit"]+=1
        for K in [1,2,4]:
            byrow=defaultdict(list);high=0
            for x,y,h,w,A in data:
                if h>=m:continue
                if A>K*2**h:high+=1;continue
                require(A>=3**(s-1) and (A-2**h*y)%3**s==0,"row interval/congruence")
                f=F(3**s*x,2**h*y)
                require(f/x==F(3**s,2**h*y) and f>=F(1,2),"corrected mass")
                byrow[y,h].append((x,A))
            require(F(high,N)<=F(s,3*K),"geometric high affinity")
            for (y,h),row in byrow.items():
                B=F(K*2**h,3**s)
                require(len(set(A for x,A in row))==len(row),"affine source collision")
                require(len(row)<=int(B)+1,"positive endpoint frequency")
                require(len(row)*F(3**s,2**h)<=4*K,"4K row")
                if len(row)>B:count["detect_dropped_progression_endpoint"]+=1
                if y<3**s:count["retained_rows_below_ternary_period"]+=1
                count["tested_rows"]+=1
            count["markov_truncations"]+=1
    # Verifies the exact independent geometric input to E(F_s)=s/3 without a numerical tail approximation.
    for emax in range(1,32):
        finite=sum(F(1,4**j) for j in range(1,emax+1))
        require(finite+F(1,3*4**emax)==F(1,3),"geometric multiplier")
    # The local good-block definition includes H<=m-1, forcing every actual reachable y>=3^s.
    # Outside those retained windows the arithmetic row still holds on the same low-affine criterion.
    for y in range(1,32,2):
      for s in range(2,6):
       if y>=3**s:continue
       inv={y}
       for _ in range(s):
        inv={(2**e*z-1)//3 for z in inv for e in range(1,8) if (2**e*z-1)%3==0}
       rows=defaultdict(list)
       for x in inv:
        end,h,w,A=orbit(x,s);require(end==y,"inverse word physical path")
        for K in [1,4]:
         if A<=K*2**h:rows[h,K].append(x)
       for (h,K),xs in rows.items():
        require(len(xs)*3**s<=4*K*2**h,"independent small endpoint row")
        count["general_rows_below_ternary_period"]+=1

def block_composition(count):
    for m in range(7,13):
      N=2**(m-1);source=list(range(2**m+1,2**(m+1),2))
      for s,t in [(1,2),(2,1),(2,3),(3,2)]:
        pairs=[(x,orbit(x,s)[0]) for x in source]
        endpoint_counts=Counter(orbit(z,t)[0] for x,z in pairs)
        per_octave=defaultdict(list)
        for y,n in endpoint_counts.items():per_octave[y.bit_length()-1].append((n,y))
        A={max(group)[1] for group in per_octave.values()}
        # Adversarial target: maximize actual endpoint multiplicity separately in each octave.
        rest=lambda z: orbit(z,t)[0] in A
        observed=sum(orbit(x,s+t)[0] in A for x in source)
        require(observed==sum(rest(z) for x,z in pairs),"set-valued backward composition")
        incoming=Counter(z.bit_length()-1 for x,z in pairs);fake=F(0)
        for j,n in incoming.items():
            low=2**j;all_odd=range(low+(low%2==0),2*low,2);st=sum(rest(v) for v in all_odd)
            fake+=F(n*st,len(all_odd))
        if fake!=observed:count["detect_uniform_intermediate_restart"]+=1
        count["two_block_adversarial_targets"]+=1

def debt(count):
    for x in range(3,4000,2):
        y=x;E=0;ds=[0]
        for j in range(1,41):
            if y==1:break
            y,e,_,_=orbit(y,1);E+=e
            require(2**E*y*3**j<=x*10**j,"physical debt telescope")
            ds.append(7*j-4*E)
        i=ds.index(min(ds))
        require(all(v>=ds[i] for v in ds[i:]),"finite debt minimum")
        count["finite_minimum_tails"]+=1
    count["actual_bad_sources_assumed"]=0
if __name__=='__main__':
    c=Counter();word_rows(c);block_composition(c);debt(c);print(json.dumps(dict(c),indent=2,sort_keys=True))
