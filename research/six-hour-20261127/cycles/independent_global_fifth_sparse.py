"""Independent raw-grade repair, rotated source congruence, endpoint and margin checks."""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import comb
import json

def checkword(es,Lset,seen):
    p,a=len(es),sum(es)
    ds=[];t=0
    for j,e in enumerate(es):ds.append(p*t-j*a);t+=e
    shifts=[j for j,z in enumerate(ds) if z==max(ds)]
    for root in shifts:
        e=es[root:]+es[:root]; w=[];z=[];t=0
        for j,ej in enumerate(e):
            w.append((j+1)*a//p-j*a//p);z.append(j*a//p-t);t+=ej
        assert min(z)==0 and all(g>=0 for g in z)
        bits=[min(1,x) for x in z]
        # Independent descent-to-fixed-point by repeatedly relaxing each violated inequality.
        u=bits[:]
        while True:
            change=False
            for j,m in enumerate(w):
                left,right=(j,(j+1)%p) if m==2 else ((j+1)%p,j)
                if u[left]>u[right]:u[left]=u[right];change=True
            if not change:break
        changed=[j for j in range(p) if z[j]!=u[j]]; bad={j for j in range(p) if z[j]>=2 or e[j]>=3}
        assert set(changed)<=bad|{(j-1)%p for j in bad}
        re=[w[j]+u[j]-u[(j+1)%p] for j in range(p)]; assert set(re)<={1,2}
        seen['max_grade']=max(seen['max_grade'],max(z));seen['root_rotations']+=1
        for n in Lset:
            for j in range(p):
                if z[j]!=u[j] or z[(j+n)%p]!=u[(j+n)%p]:continue
                k=sum(e[(j+h)%p] for h in range(n));kk=sum(re[(j+h)%p] for h in range(n));assert k==kk
                mod=2**k;a0=ar=0;raw=proj=fix=0;drift=1+(2*j)%17
                for h in range(n):
                    v=(j+h)%p;g=pow(3,-h-1,mod)
                    raw-=drift*pow(2,a0,mod)*g;proj-=drift*pow(2,ar,mod)*g
                    if z[v]!=u[v]:
                        mh=(j+h)*a//p-j*a//p
                        assert a0==mh+z[j]-z[v] and ar==mh+u[j]-u[v]
                        fix-=drift*(pow(2,a0,mod)-pow(2,ar,mod))*g
                    else: assert a0==ar
                    a0+=e[v];ar+=re[v]
                assert (raw-proj-fix)%mod==0
                seen['rotated_windows']+=1;seen['nonzero_shifts']+=fix%mod!=0;seen['winding_windows']+=n>p

def run():
    seen=Counter(); words=0
    for n in range(3,9):
        for es in product((1,2,3,4),repeat=n):
            if not 3*n<2*sum(es) or not 3*sum(es)<5*n:continue
            if es!=min(es[i:]+es[:i] for i in range(n)):continue
            checkword(es,(3,n+2),seen);words+=1
    # Long rises on ones and a single arbitrarily large descent, with near-critical average.
    n=180;total=285;large=total-n+1;es=[1]*(n-1)+[large]
    checkword(es,(1,7,13,n,2*n),seen);words+=1
    assert seen['max_grade']>=100
    for l in range(1,257):assert comb(2*l+1,l)<=2**(2*l)
    eta=Q(1,10**6);tau=Q(1,2000000);c=Q(1,10**8);gamma=Q(4,3)-Q(1,10000)
    upper=(6*eta/Q(3,2)+gamma*(1-eta)+(5+eta)*21*tau)/(4+eta)
    slack=1-(3+c)*upper
    assert 2*c*(4+eta)<eta and Q(8,3)**15>2000000
    assert upper==Q(2666577000221,8000002000000) and slack==Q(27097267122999779,800000200000000000000)
    return {'words':words,'controls':dict(seen),'consumer_exponent_upper':str(upper),'product_slack':str(slack),'good_start_fraction_lower':str(1-6*c-3*c/tau),'max_unbounded_positive_gap_control':large}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
