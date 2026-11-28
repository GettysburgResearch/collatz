"""Exact sixfold affine permutations, time-lag balances and clock decompositions."""

from fractions import Fraction
from itertools import permutations, product
from math import gcd
from random import Random
import json


def require(check, detail):
    if not check:
        raise ArithmeticError(detail)


def lift(pi,i):
    q,r=divmod(i,len(pi))
    return pi[r]+q*len(pi)


def inversions(pi):
    n=len(pi)
    out=[]
    for i,v in enumerate(pi):
        j=i+1
        while (j//n)*n+min(pi)<v:
            if lift(pi,j)<v:
                out.append((i,j))
            j+=1
    return out


def cycle_count(pi):
    n=len(pi)
    unseen=set(range(n));count=0
    while unseen:
        x=min(unseen);count+=1
        while x in unseen:
            unseen.remove(x);x=pi[x]%n
    return count


def bubble(pi):
    pi=pi[:];n=len(pi)
    count=0
    while True:
        i=next((r for r in range(n) if lift(pi,r)>lift(pi,r+1)),None)
        if i is None:
            break
        if i==n-1:
            pi[i],pi[0]=pi[0]+n,pi[i]-n
        else:
            pi[i],pi[i+1]=pi[i+1],pi[i]
        count+=1
    require(all(pi[i]==i+pi[0] for i in range(n)),"terminal ordered translation")
    return count,pi[0]


def abstract_controls():
    rng=Random(59021)
    checked=seam=0
    for n in range(3,8):
        for rep in permutations(range(n)):
            if cycle_count(rep)!=1:
                continue
            for _ in range(4):
                pi=[a+n*rng.randint(-2,2) for a in rep]
                inv=inversions(pi)
                k,h=bubble(pi)
                require(k==len(inv) and sum(pi)-n*(n-1)//2==n*h,"independent affine inversion distance")
                g=gcd(h,n)
                require(k>=g-1 and (k-g+1)%2==0,"full permutation cycle-count bound")
                seam+=any(j>=n for _,j in inv)
                checked+=1
    return {"transitive_affine_permutations":checked,"with_seam_inversions":seam}


def reduced_circuit(word):
    A=K=0
    for a in word:
        K=3*K+2**A;A+=a
    D=2**A-3**len(word)
    if D<=0:
        return None
    d=gcd(K,D);q=D//d;start=K//d
    full=[];x=start
    for a in word:
        if x in full:
            return None
        require(x%2==1 and gcd(x,q)==1 and x%3!=0,"reduced odd phase")
        full.append(x); x=3*x+q
        for _ in range(a):
            require(x%2==0,"literal numerator halving")
            full.append(x);x//=2
    require(x==start and len(set(full))==len(full),"exact full rational circuit")
    return full,q


def geometric_control(full,q):
    n=len(full);S=min(full)
    p=sum(x%2 for x in full);A=n-p
    folded=[];exps=[];E=0
    for x in full:
        z=Fraction(x);e=0
        while z>=6*S:
            z/=6;e-=1
        folded.append(z);exps.append(e)
        E=max(E,-e)
    require(len(set(folded))==n,"all full-state rays distinct")
    order=sorted(range(n),key=folded.__getitem__)
    rank={i:r for r,i in enumerate(order)}
    pi=[]
    for i in order:
        j=(i+1)%n
        e=exps[i]+(full[i]%2==0)-exps[j]
        pi.append(rank[j]+n*e)
        require(folded[j]*Fraction(6)**e
                ==3*folded[i]+q*(full[i]%2)*Fraction(6)**exps[i],"actual lifted edge")
    inv=inversions(pi);I,h=bubble(pi)
    require(h==A and I==len(inv) and cycle_count(pi)==1,"physical versus abstract permutation")
    lag=[0]*n
    expected=[]
    # Exhaust all possible scale exponents directly from the physical inequalities.
    for i,x in enumerate(full):
        if x%2==0:
            continue
        for j,y in enumerate(full):
            if i==j:
                continue
            d=0;v=Fraction(x)
            while v>=y:
                v/=6;d-=1
            while v*6<y:
                v*=6;d+=1
            while Fraction(6)**d*(3*x+q)>3*y:
                if Fraction(6)**d*(3*x+q)>3*y+q*(y%2):
                    expected.append((i,j,d))
                    lag[(j-i)%n]+=1
                d-=1
    require(len(expected)==I,"physical crossings with all scales")
    require(all(lag[t]==lag[n-t] for t in range(1,n)),"exact chronological lag reversal")
    g=gcd(A,p)
    require(I>=g-1 and (I-g+1)%2==0,"complete transitive cycle parity")
    if g%2==0:
        require(lag[n//2]%2==1,"mandatory antipodal crossing")

    ordinary_pairs=[]
    for i,x in enumerate(full):
        if x%2==0:
            continue
        for d in range(1,E+2):
            for j,y in enumerate(full):
                if 3*6**d*x<3*y<6**d*(3*x+1):
                    ordinary_pairs.append((i,j,d))
    if q==1:
        require(sorted(expected)==sorted(ordinary_pairs),"unscaled ordinary interval count")
    decomposed=0
    for i,j,d in expected:
        if min(full)<q or d<=0:
            continue
        t=(j-i)%n
        odd=sum(full[(i+k)%n]%2 for k in range(t))
        a=t-odd
        b1,p1=a+d,odd-d
        b2,p2=A-b1,p-p1
        require(min(b1,p1,b2,p2)>0 and 2**b1>3**p1 and 2**b2>3**p2,"strict two-arc clock decomposition")
        require(6**b1>3**t and 6**b1*3**n<6**A*3**t,"lag window with strict endpoints")
        decomposed+=1
    return (I,max((abs(d) for _,_,d in expected),default=0),decomposed,
            int(q!=1 and sorted(expected)!=sorted(ordinary_pairs)))


def rational_controls():
    words=set()
    for p in range(1,6):
        for w in product(range(1,6),repeat=p):
            words.add(min(w[i:]+w[:i] for i in range(p)))
    rng=Random(4419)
    for p in (6,9,12,15,18,21):
        A=(3**p).bit_length()
        for _ in range(20):
            cuts=sorted(rng.sample(range(1,A),p-1))
            edges=tuple(b-a for a,b in zip([0]+cuts,cuts+[A]))
            words.add(min(edges[i:]+edges[:i] for i in range(p)))
    total=nonzero=decomp=diff=0;maxcross=maxscale=0;examples=[]
    for w in sorted(words):
        c=reduced_circuit(w)
        if c is None:
            continue
        full,q=c
        I,D,k,cx=geometric_control(full,q)
        total+=1;nonzero+=I>0;decomp+=k;diff+=cx
        maxcross=max(maxcross,I);maxscale=max(maxscale,D)
        if k and len(examples)<3:
            examples.append({"word":w,"denominator":q,"full_states":len(full),"inversions":I,"strict_arc_splits":k})
    return {"primitive_positive_circuits":total,"with_nonzero_inversions":nonzero,
            "largest_inversion_count":maxcross,"largest_crossed_scale_exponent_magnitude":maxscale,
            "different_if_denominator_assumed_one":diff,"strict_arc_splits_for_applicable_ratio":decomp,
            "examples":examples}


if __name__=="__main__":
    print(json.dumps({"affine_sort":abstract_controls(),"complete_circuits":rational_controls()},indent=2,sort_keys=True))
