#!/usr/bin/env python3
"""Exact finite controls for candidate rigidity, not candidate existence."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def original_step(n):
    return n//2 if n%2==0 else (3*n+1)//2


def paired_step(state):
    x,w,r=state
    require((x+w)%2==1,'paired step without compatibility')
    if x%2:
        return ((3*x+1)//2,w//2,r)
    if r:
        return (x//2,(w+3**(r-1))//2,r-1)
    return (x//2,(3*w+1)//2,0)


def budget(n,a,r):
    f=1
    for j in range(r):
        f*=1+3**j
    b=n*max(1,abs(a))*f
    e=b.bit_length()
    return b,e,9*e+1


def check_prefix(n,a,r,length):
    state=(n,a,r)
    first=None
    for k in range(length):
        x,w,j=state
        if first is None and x==1:
            first=(k,state)
        if (x+w)%2!=1:
            return dict(passed=False,first_failure=k,first_hit=first)
        state=paired_step(state)
    if first is None and state[0]==1:
        first=(length,state)
    return dict(passed=True,terminal=state,first_hit=first)


def known_dual(n):
    xs=[n]
    while xs[-1]!=1:
        require(len(xs)<10000,'selected known control exceeded guard')
        xs.append(original_step(xs[-1]))
    y=Fraction(2)
    for x in reversed(xs[:-1]):
        y=2*y if x%2 else (2*y-1)/3
    a,d=y.numerator,y.denominator
    r=0
    while d%3==0:
        d//=3;r+=1
    require(d==1,'known dual not triadic')
    return a,r,len(xs)-1


def main():
    accepted=[]
    for n in (1,2,3,4,7,27,97):
        a,r,tau=known_dual(n)
        for extra in (0,1,3):
            aa,rr=a*3**extra,r+extra
            b,e,h=budget(n,aa,rr)
            result=check_prefix(n,aa,rr,h)
            require(result['passed'],'known candidate did not pass')
            k,state=result['first_hit']
            require(k==tau and k<=8*e,'early hit bound')
            x,w,j=state
            require(x==1 and w==2*3**j,'exact terminal dual')
            for _ in range(40):
                x,w,j=state
                require((x==1 and w==2*3**j) or (x==2 and w==3**j),'cycle invariant')
                state=paired_step(state)
            accepted.append(dict(n=n,numerator=str(aa),exponent=rr,
                extra_factors=extra,budget=str(b),binary_budget=e,horizon=h,
                first_hit=tau,exact_hit_state=list(result['first_hit'][1])))
    defects=[]
    for r in (0,1,7):
        for length in (0,1,2,5,17,64):
            for sign in (-1,1):
                a=2*3**r+sign*2**length
                result=check_prefix(1,a,r,length+1)
                require(not result['passed'] and result['first_failure']==length,
                        'cycle defect valuation clock')
                defects.append(dict(exponent=r,valuation=length,sign=sign,
                    numerator=str(a),first_failure=result['first_failure']))
    zero=[]
    for n in (1,2,3,7):
        _,_,h=budget(n,0,2)
        result=check_prefix(n,0,2,h)
        require(not result['passed'],'zero candidate accepted')
        zero.append(dict(n=n,exponent=2,horizon=h,first_failure=result['first_failure']))
    n,a,r=3,-4,2
    _,_,old_h=budget(n,a,r)
    altered=a+2**old_h
    _,_,new_h=budget(n,altered,r)
    short=check_prefix(n,altered,r,old_h)
    own=check_prefix(n,altered,r,new_h)
    require(short['passed'] and not own['passed'] and own['first_failure']==old_h,
            'unchanged candidate horizon guard')
    root=Path(__file__).resolve().parent
    print(json.dumps(dict(schema='collatz-exact-candidate-controls/v1',
        scope='Selected exact finite controls for the new rigidity theorem; no universal candidate construction.',
        source_hashes={name:hashlib.sha256((root/name).read_bytes()).hexdigest()
            for name in ['EXACT_CANDIDATE_RIGIDITY.md','lean/TriadicCertificateRigidity.lean']},
        accepted=accepted,cycle_defects=defects,zero_rejections=zero,
        stale_horizon=dict(n=n,exponent=r,original_numerator=str(a),
            altered_numerator=str(altered),old_horizon=old_h,new_horizon=new_h,
            first_failure=own['first_failure']),
        counts=dict(accepted=len(accepted),defects=len(defects),zeros=len(zero),stale=1)),
        indent=2,sort_keys=True))


if __name__=='__main__':
    main()
