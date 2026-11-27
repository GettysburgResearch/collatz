"""Signed-gap entropy rates and finite higher-difference obstructions."""
from fractions import Fraction as F
from itertools import product
from math import gcd
import json


def require(x,m):
    if not x:raise ArithmeticError(m)


def low(x):return x&-x


def diff(x):return tuple(v-u for u,v in zip(x,x[1:]))


def geometry():
    # Every tested convex doubled sequence spells an exact instance of the
    # interval bound for ALL offsets; the slope widths are summed directly.
    tests=0
    for P in range(2,15):
        g0=2*P+3
        g=[g0+(i*(g0-1))//P for i in range(P)]
        require(all(b>a for a,b in zip(g,g[1:])) and g[-1]<2*g0,'convex source')
        L=[sum(g)]
        for x in g:L.append(L[-1]+x)
        require(L[-1]==2*L[0],'octave normalization')
        A=lambda r:L[r%P]<<(r//P)
        for t in range(1,P):
            gaps=[A(r+t)-A(r) for r in range(P)]
            require(all(b-a>=t for a,b in zip(gaps,gaps[1:])),'injective')
            require(all(0<v<=4*t*g0 and g0*P<=L[0] for v in gaps),'bit scale')
            tests+=len(gaps)
    return tests


def rate_constants():
    M=F(5116201,10**6)
    require(M-1<F(33,8),'BLS coarse bound')
    # (33/8)h_2(1/17)<log3, by exact integer exponentiation.
    require(17**(17*33)*2**33 < 16**(16*33)*3**(17*8),'published M subpower')
    # 2h_2(5/32)<log3 with h_2(e)=H(e)+e log2.
    require(32**64*2**10 < 5**10*27**54*3**32,'conditional M subpower')
    # Exact numerical cutoffs inherited in the established all-lag branches.
    require(F(109,100)/F(128,25)-F(7,10)*(F(1,4)+F(7,530)+F(26,1000))-F(9,1000)>0,'full BLS')
    require(36**36*2**10<35**35*3**12,'small macroscopic arm')
    require(2264**216*47**6*2**73<2209**216*3**72,'long macroscopic arm')
    return dict(published_subpower_offset='1/17',conditional_subpower_offset='5/32',
                published_all_lags='1/1000',conditional_all_lags='1/36')


def example():
    starts=(83,94,107,121)
    a=starts
    rows=[];curv=[]
    for j,m in enumerate((1,2,1,2,1,0)):
        require(all(low(v)<=2 and gcd(v,3)==1 for v in a),'genuine eligible labels')
        require(min(diff(a))>0 and min(diff(diff(a)))>0,'strict first two differences')
        curv.append(diff(diff(diff(a)))[0]);rows.append(a)
        if not m:break
        new=tuple((3*x+low(x))>>m for x in a)
        require(all((v<<m)==3*x+low(x) for x,v in zip(a,new)),'true mechanical image')
        for x,v in zip(a,new):
            odd=x//low(x)
            require((3*odd+1)//low(3*odd+1)==v//low(v),'physical odd trajectory')
        a=new
    require(all(rows[j][1:]==rows[j+2][:-1] for j in range(4)),'one common orbit')
    require(min(curv)<0<max(curv),'third sign reversal')
    return curv


if __name__=='__main__':
    print(json.dumps({'rates':rate_constants(),'exact_interval_samples':geometry(),
                      'one_orbit_third_differences':example()},sort_keys=True,indent=2))
