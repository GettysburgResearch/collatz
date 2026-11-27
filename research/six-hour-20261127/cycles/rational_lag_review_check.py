"""Signed, multi-step physical source fibres and negative-lag amplification controls."""
from collections import Counter
from itertools import product
from math import gcd
import json
from review_physical_odd_transfer import odd_period

def order(z,d):
    if d==1:return 1
    cur=z%d;n=1
    while cur!=1:
        cur=cur*z%d;n+=1
    return n

def main():
    counts=Counter()
    for p in range(3,9):
        for word in product((1,2,3),repeat=p):
            cy=odd_period(word)
            if cy is None:continue
            xs,d=cy;A=sum(word)
            E=[0]
            for e in word:E.append(E[-1]+e)
            j=max(range(p),key=lambda i:p*E[i]-i*A)
            w=word[j:]+word[:j];N=[int(d*xs[(i+j)%p]) for i in range(p)]
            g=gcd(A,p);q=p//g;a=A//g
            if q<2:continue
            z=[];prefix=0
            for i,e in enumerate(w):
                z.append(i*a//q-prefix);prefix+=e
            if not 0<=min(z)<=max(z)<=2:continue
            H=max(1,max(z));ell=[2**(H-y) for y in z]
            K=[y*n for y,n in zip(ell,N)]
            m=[(i+1)*a//q-i*a//q for i in range(p)]
            r=[i*a%q for i in range(p)]
            assert all(K[(i+1)%p]*2**m[i]==3*K[i]+d*ell[i] for i in range(p))
            counts['cycles']+=1;counts['denominator_exceeds_period']+=d>p
            for h in (1,-1,2,-2,p+1,1-p):
                t=h*a%q
                if t==0:continue
                rho=(pow(3,h,d)*pow(2,-(h*a//q),d))%d
                c=[(r_i+t)//q for r_i in r]
                G=[2**c[i]*K[(i+h)%p]-K[i] for i in range(p)]
                delta=[2**c[i]*ell[(i+h)%p]-ell[i] for i in range(p)]
                assert all((G[i]-(rho-1)*K[i])%d==0 for i in range(p))
                for i in range(p):
                    b=5;M=B=0
                    for o in range(b):
                        u=(i+o)%p;B=3*B+(1<<M)*delta[u];M+=m[u]
                    J0,a0=divmod(G[i],d);Jb,ab=divmod(G[(i+b)%p],d)
                    assert (1<<M)*G[(i+b)%p]==3**b*G[i]+d*B
                    assert (J0+pow(3**b,-1,1<<M)*B+a0*pow(d,-1,1<<M))%(1<<M)==0
                    assert (Jb-pow(1<<M,-1,3**b)*B+ab*pow(d,-1,3**b))%3**b==0
                    counts['signed_two_clock_windows']+=1
                    counts['negative_floor_controls']+=J0<0 or Jb<0
    for d in (1,5,7,11,13,17,19,25,29,35,49,65):
        for q in (59,131,257):
            a=q+q//2+1
            for h in range(-2*q,2*q+1):
                t=h*a%q
                if not t:continue
                rho=pow(3,h,d)*pow(2,-(h*a//q),d)%d
                n=order(rho,d)
                if n*t>=q:continue
                assert n*(h*a//q)==n*h*a//q
                assert (pow(3,n*h,d)*pow(2,-(n*h*a//q),d)-1)%d==0
                assert n*t==n*h*a%q
                counts['compatible_amplifications']+=1
                counts['negative_nontrivial_amplifications']+=h<0 and n>1
    print(json.dumps(dict(counts),indent=2,sort_keys=True))
if __name__=='__main__':main()
