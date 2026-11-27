"""Exact finite ternary fibres and independent pointwise direct-vs-mixed chart diagnostics."""
from collections import defaultdict
from itertools import product
from math import pi,sin,cos,sqrt
from pathlib import Path
import cmath,json,random
from independent_fifth_setup import rows


def gcd_controls():
    words=prefixes=observations=0
    for a in range(1,8):
        ws=list(product((1,2),repeat=max(0,a-1)))
        if a>5:ws=ws[::5]
        for w in ws:
            c=[3**(a-1)]
            for m in w:c.append(c[-1]//3*2**m)
            N=5*3**(a-1);past=[() for _ in range(N)]
            for i,ci in enumerate(c):
                table=defaultdict(lambda:defaultdict(int))
                for k in range(N):
                    entry=ci*k%N
                    table[past[k]][entry]+=1
                    past[k]+=entry,
                for old,hits in table.items():
                    if i:
                        assert len(hits)==3 and all((3*j-2**w[i-1]*old[-1])%N==0 for j in hits)
                        assert len(set(hits.values()))==1
                    else:assert len(hits)==5
                prefixes+=1;observations+=len(table)
            words+=1
    return words,prefixes,observations


def law_controls():
    (n,L,K,cp,rp),masks,cs,edges=rows(); rng=random.Random(924718683)
    def normalized(z1,z2):
        n=abs(z1)**2+abs(z2)**2; w=2*z1.conjugate()*z2/n
        return w,(abs(z1)**2-abs(z2)**2)/n,n
    def poly(ci,S,w,z):
        phases=[cmath.exp(2j*pi*k*S) for k in range(-K,K+1)];p=[w**s if s>=0 else w.conjugate()**(-s) for s in range(-L,L+1)];zp=[z**l for l in range(L+1)]
        return sum(c*phases[k+K]*p[s+L]*zp[j] for (k,s,j),c in cs[ci].items())/(1<<cp)
    err=imag=0.;rel=-1.;checks=0
    for old,new,m,R in edges:
        ratio=R/(1<<rp)
        for i in range(3):
            r,b,psi=rng.random(),rng.random()*2*pi,rng.random()*2*pi
            w0=sin(b)*cmath.exp(1j*(psi-2*pi*r));z0=cos(b)
            A=sqrt((1+z0)/2)
            C=w0/(2*A)
            direct=0j
            for j in range(3):
                u=((3*r)%1+j)/3;p=C*cmath.exp(2j*pi*u)
                A2,C2=((A+p,p) if m==1 else (A,A+p));wb,z,g=normalized(A2,C2)
                direct+=g**2.5*poly(new,2**m*u,wb,z)/(3*ratio)
            direct-=poly(old,(3*r)%1,w0,z0)
            base=0j
            for (k,s,j),coef in cs[old].items():
                az=sin(b)**abs(s)*cmath.exp(1j*s*psi)
                base-=coef*cmath.exp(2j*pi*(3*k-s)*r)*az*(cos(b)**j)/(1<<cp)
            for j in range(3):
                w=sin(b)*cmath.exp(1j*(psi+2*pi*j/3));z=cos(b);ss=1 if m==2 else -1
                g=(3+2*w.real+ss*z)/2; wn=(w.real+1+ss*z+1j*w.imag)/g;zn=(z-ss*(1+2*w.real))/(2*g)
                base+=g**2.5*poly(new,2**m*r+2**m*j/3,wn,zn)/(3*ratio)
            err=max(err,abs(direct-base));imag=max(imag,abs(direct.imag));rel=max(rel,direct.real/poly(old,(3*r)%1,w0,z0).real);checks+=1
    assert err<1e-10 and imag<1e-12 and rel<1/6000
    return checks,err,imag,rel

if __name__=='__main__':
    w,p,o=gcd_controls();c,e,i,r=law_controls();print(json.dumps({'finite_mechanical_words':w,'prefixes':p,'exact_conditional_fibres':o,'direct_complex_column_vs_three_branch_Fourier_points':c,'max_pointwise_formula_discrepancy_float':e,'max_imaginary_residual_float':i,'max_normalized_one_sided_pointwise_residual_float':r,'random_float_is_diagnostic_only':True},sort_keys=True,indent=2))
