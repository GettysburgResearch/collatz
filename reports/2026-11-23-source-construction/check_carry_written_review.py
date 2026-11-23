#!/usr/bin/env python3
"""Independent exact examples for the carry note's four written arguments."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import argparse
import json


def need(x, why):
    if not x:
        raise ValueError(why)


def odd(x):
    x=F(x)
    need(x.denominator%2==1,'odd rational denominator')
    return x.numerator%2==1


def step(x):
    return (3*x+1)/2 if odd(x) else x/2


def valuation2(x):
    need(x>0,'positive valuation argument')
    return (x&-x).bit_length()-1


def lifting(N,u,L=0):
    R=1
    while 2**R*(u+1)>=3**R:
        R+=1
    x=F(2**R*N); y=F(2**R*(u+1)-3**R,3**R)
    need(R>=2 and F(-1,3)<y<0,'initial crossing interval')
    for j in range(R+1):
        need(x==2**(R-j)*N,'lift original formula')
        need(y==F(2,3)**(R-j)*(u+1)-1,'lift complementary formula')
        if j==1:
            need(0<y<F(1,2),'first positive crossing interval')
        if j>0:
            need(y>0,'positive continuation')
        if j<R:
            need(not odd(x) and odd(y),'literal lifting parities')
            x,y=step(x),step(y)
    need((x,y)==(N,u),'unchanged terminal pair')
    for j in range(L):
        need(odd(x)!=odd(y),'additional chosen prefix')
        x,y=step(x),step(y)
    return R


def complementary_integer(N,L):
    x=N; D=0; b=0
    for j in range(L):
        e=x%2; c=1-e
        D=3**c*D+c*2**j
        b+=c
        x=(3*x+1)//2 if e else x//2
    if L==0:
        return 1
    modulus=2**L
    u=(-D*pow(3**b,-1,modulus))%modulus
    return u or modulus


def true_dual(n):
    path=[n]
    while path[-1]!=1:
        need(len(path)<5000,'selected finite control cap')
        x=path[-1]
        path.append((3*x+1)//2 if x%2 else x//2)
    y=F(2); rev=[y]
    for x in path[-2::-1]:
        y=2*y if x%2 else (2*y-1)/3
        rev.append(y)
    duals=rev[::-1]
    r=0; den=y.denominator
    while den>1 and den%3==0:
        den//=3;r+=1
    need(den==1,'reduced triadic denominator')
    tau=len(path)-1;b=sum(x%2==0 for x in path[:-1])
    for i in range(tau):
        need(odd(path[i])!=odd(duals[i]),'true complementary parity')
        need(step(duals[i])==duals[i+1],'true complementary branch')
    if n>2:
        need(r==b-1,'exact denominator clock')
        o=tau-b
        need(n*3**o<=2**tau,'clock inequality')
        need((n*3**o==2**tau)==(o==0),'clock equality condition')
        need((o==0)==(n==2**tau),'power-of-two boundary')
    if n not in (1,2,4):
        need(y<0,'negative true dual')
        L=tau-3
        need(L>=0 and path[L]==8 and duals[L]==F(-1,9),'last negative pair')
        need(all(t<0 for t in duals[:L+1]),'all earlier duals negative')
        need(duals[L+1]==F(1,3),'true crossing')
        P=[3**r*path[i]*(-duals[i]) for i in range(L+1)]
        need(all(q>0 and q.denominator==1 for q in P),'fixed denominator integer products')
        for i in range(L):
            need(P[i+1]<=F(5,6)*P[i],'negative product contraction')
            if path[i]%2==0:
                need(P[i+1]<F(3,4)*P[i],'negative even contraction')
        need(8*3**r*6**L<=9*n*abs(y.numerator)*5**L,'complete negative clock')
    else:
        need(y=={1:F(2),2:F(1),4:F(1,3)}[n],'three positive true-dual controls')
    return {'n':n,'first_hit':tau,'even_count':b,'reduced_exponent':r,'dual':str(y)}


def reset(R,w):
    initial=w; product=F(1); K=0
    for j in range(R,0,-1):
        need(w>0 and w%2==1 and w%3!=0,'reduced positive odd reset')
        c=w+3**(j-1);k=valuation2(c);v=c>>k
        product*=1+F(3**(j-1),w)
        y=F(w,3**j)
        need(odd(y),'initial odd reset branch')
        y=step(y)
        for _ in range(k-1):
            need(not odd(y),'following reset even branch')
            y=step(y)
        need(y==F(v,3**(j-1)) and odd(y),'full reset endpoint')
        K+=k;w=v
    need(F(2**K*w,initial)==product,'global multiplicative reset telescope')
    return K


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True,type=Path);args=ap.parse_args()
    source_hash=sha256(args.source.read_bytes()).hexdigest()
    sources=(1,2,3,5,7,27,97)
    lift_count=0;continuations=0
    for N in sources:
        for u in range(1,25):
            lifting(N,u);lift_count+=1
        for L in (0,1,2,5,12):
            lifting(N,complementary_integer(N,L),L);continuations+=1
    true=[true_dual(n) for n in (1,2,3,4,6,7,8,16,27,32,97,128)]
    resets=0
    for R in range(1,9):
        for w in range(1,121,2):
            if w%3:
                reset(R,w);resets+=1
    for j in range(1,41):
        need(valuation2(1+3**(j-1))==(1 if (j-1)%2==0 else 2),'unit reset residue')
    need(sha256(args.source.read_bytes()).hexdigest()==source_hash,'source changed during review')
    print(json.dumps({'scope':'Independent finite examples for written lift, true-dual denominator, negative product and reset telescope; no universal construction or Lean review.','reviewed_source_sha256':source_hash,'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'all_target_examples':lift_count,'chosen_continuation_examples':continuations,'true_dual_examples':true,'complete_reset_examples':resets,'unit_reset_levels':40,'success':True},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
