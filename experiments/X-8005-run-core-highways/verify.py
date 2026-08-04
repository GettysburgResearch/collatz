#!/usr/bin/env python3
from __future__ import annotations
import json, sys

def val2(n):
    if n==0: raise ValueError
    c=0
    while n%2==0:
        n//=2; c+=1
    return c

def raw_step(z):
    r=z%16
    if r in (0,8):
        return 9*z//8,0
    if r==1:
        return (9*z+7)//16,1
    return None,None

def macro_direct(z):
    r=0
    while z%8==0:
        z=9*z//8; r+=1
    if z%16!=1: return None
    return r,(9*z+7)//16

def check(path):
    data=json.load(open(path,encoding='utf-8'))
    assert data['experiment_id']=='X-8005'
    local=macro=two=0
    for z in range(1,100001):
        z1,b=raw_step(z)
        if z1 is not None:
            local+=1
            assert 6*z1-5>0
        q=macro_direct(z)
        if q is not None:
            macro+=1
            r,zp=q
            u=z//(2**(3*r))
            assert 16*zp==9**(r+1)*u+7
            q2=macro_direct(zp)
            if q2 is not None:
                s,_=q2
                up=zp//(2**(3*s))
                assert up%144==(1 if s%2==0 else 89)
                two+=1
    assert data['local_checks']>=local
    assert data['macro_checks']>=macro
    assert data['two_macro_mod144_checks']>=two

    for row in data['reset_family']['sample_rows']:
        m=row['m']; d=m//3
        assert m%6==0
        z=(2**(m+4)-7)//9
        z1,b=raw_step(z); assert b==1 and z1==2**m
        cur=z1
        for _ in range(d):
            cur,b=raw_step(cur); assert b==0
        assert cur==9**d
        k=(3+val2(d))//4
        for _ in range(k):
            cur,b=raw_step(cur); assert b==1
        assert k==row['consecutive_B_after_power']
        assert ('A' if cur%8==0 else 'exit')==row['post_B_domain']
        n=0; w=z
        while n<10000:
            w2,b=raw_step(w)
            if w2 is None: break
            w=w2; n+=1
        assert n==row['actual_depth']

    for ss,item in data['u_equals_1_first_hensel_hits'].items():
        s=int(ss); r=item['r']; target=4+3*s
        mod=1<<(target+3)
        x=(pow(9,r+1,mod)+7)%mod
        assert val2(x)==target

    wanted={int(k):v['r'] for k,v in data['u_equals_1_first_hensel_hits'].items()}
    seen={}; mod=1<<25
    for rr in range(0,max(wanted.values())+1,2):
        x=(pow(9,rr+1,mod)+7)%mod
        vv=25 if x==0 else val2(x)
        if vv>=4 and (vv-4)%3==0:
            ss=(vv-4)//3
            if ss in wanted and ss not in seen: seen[ss]=rr
    assert seen==wanted
    print('all independent X-8005 checks passed')

if __name__=='__main__':
    check(sys.argv[1])
