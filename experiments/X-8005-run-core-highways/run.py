#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

EXP='X-8005'

def v2(n:int)->int:
    if n==0: raise ValueError
    return (n & -n).bit_length()-1

def step(z:int):
    if z>0 and z%8==0:
        return 9*z//8,0
    if z>0 and z%16==1:
        return (9*z+7)//16,1
    return None,None

def replay(z:int, cap:int=100000):
    word=[]
    for _ in range(cap):
        z2,b=step(z)
        if z2 is None: break
        word.append(b); z=z2
    return z,word

def macro(z:int):
    r=0
    while z%8==0:
        z=9*z//8; r+=1
    if z%16!=1: return None
    return r,(9*z+7)//16


def cylinder_a(r:int,s:int):
    M=1<<(4+3*s)
    L=16*M
    b=1 if s%2==0 else 9
    return ((M*b-7)*pow(pow(9,r+1,L),-1,L))%L

def reset_seed(m:int)->int:
    assert m%6==0 and m>=6
    return ((1<<(m+4))-7)//9

def expected_b_tail(d:int)->int:
    return (3+v2(d))//4

def post_power_b(z:int,k:int)->int:
    for _ in range(k):
        assert z%16==1
        z=(9*z+7)//16
    return z

def canonical_payload():
    local=0; macros=0; congr=0
    digest=hashlib.sha256()
    for z in range(1,500_001):
        z2,b=step(z)
        if z2 is not None:
            local+=1
            n=6*z-5; n2=6*z2-5
            assert n>0 and n2>0 and (n&1) and (n2&1)
            digest.update(z.to_bytes((z.bit_length()+7)//8 or 1,'big'))
            digest.update(bytes([b]))
        mm=macro(z)
        if mm is not None:
            r,zp=mm; macros+=1
            u=z>>(3*r)
            assert u&1
            assert (pow(9,r,16)*u)%16==1
            assert 16*zp==pow(9,r+1)*u+7
            mm2=macro(zp)
            if mm2 is not None:
                s,_=mm2
                up=zp>>(3*s)
                assert 16*(1<<(3*s))*up==pow(9,r+1)*u+7
                assert up%144==(1 if s%2==0 else 89)
                aa=cylinder_a(r,s)
                L=1<<(8+3*s)
                assert u>=aa and (u-aa)%L==0
                kk=(u-aa)//L
                M=1<<(4+3*s)
                cc=(pow(9,r+1)*aa+7)//M
                assert up==cc+16*pow(9,r+1)*kk
                congr+=1

    reset_rows=[]; max_depth=(-1,None); reset_digest=hashlib.sha256()
    for m in range(6,1201,6):
        d=m//3
        z=reset_seed(m)
        assert z%16==1
        z1,b=step(z); assert b==1 and z1==(1<<m)
        cur=z1
        for _ in range(d):
            cur,b=step(cur); assert b==0
        assert cur==pow(9,d)
        k=expected_b_tail(d)
        assert v2(pow(9,d)-1)==3+v2(d)
        cur2=post_power_b(cur,k)
        assert cur2%16!=1
        _,word=replay(z,20000)
        depth=len(word)
        if depth>max_depth[0]: max_depth=(depth,m)
        reset_digest.update(m.to_bytes(2,'big'))
        reset_digest.update(depth.to_bytes(2,'big'))
        reset_digest.update(hashlib.sha256(bytes(word)).digest())
        if m in (6,18,96,600,1200):
            s=v2(d); odd=d>>s
            resume_A=(cur2%8==0)
            predicted=(s%4==1 and odd%8==3)
            assert resume_A==predicted
            reset_rows.append({
                'm':m,'d':d,'seed_bits':z.bit_length(),
                'certified_prefix':1+d+k,'actual_depth':depth,
                'consecutive_B_after_power':k,
                'post_B_domain':('A' if cur2%8==0 else 'exit'),
                'v2_d':s,'odd_d_mod8':odd%8,
            })

    first={}; limit=1_000_000
    for r in range(0,limit+1,2):
        x=(pow(9,r+1,1<<25)+7)%(1<<25)
        vv=25 if x==0 else v2(x)
        if vv>=4 and (vv-4)%3==0:
            s=(vv-4)//3
            if 0<=s<=6 and str(s) not in first:
                first[str(s)]={'r':r,'valuation':vv}
                if len(first)==7: break
    assert len(first)==7

    pure_power_hits=[]; reset_hits=[]; tested=0
    for e in range(1,1001,2):
        num=pow(9,e)+7
        if num%16: continue
        w=num//16; vv=v2(w)
        if vv%3: continue
        core=w>>vv
        preB=pow(9,vv//3)*core
        if preB%16!=1: continue
        nxt=(9*preB+7)//16
        tested+=1
        if nxt&(nxt-1)==0 and (nxt.bit_length()-1)%3==0:
            pure_power_hits.append(e)
        val=9*nxt+7
        if val>0 and val&(val-1)==0:
            reset_hits.append(e)

    return {
        'experiment_id':EXP,
        'arithmetic':'exact Python integers',
        'local_checks':local,
        'macro_checks':macros,
        'two_macro_mod144_checks':congr,
        'local_digest':digest.hexdigest(),
        'reset_family':{
            'm_min':6,'m_max':1200,'step':6,'count':200,
            'max_actual_depth':max_depth[0],'first_m_at_max':max_depth[1],
            'semantic_digest':reset_digest.hexdigest(),'sample_rows':reset_rows,
        },
        'u_equals_1_first_hensel_hits':first,
        'bounded_exact_reset_search':{
            'odd_exponent_max':1000,'eligible_cases':tested,
            'pure_power_hits':pure_power_hits,'second_reset_hits':reset_hits,
        }
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check-results',type=Path)
    args=parser.parse_args()
    payload=canonical_payload()
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    out=dict(payload); out['results_sha256']=hashlib.sha256(raw).hexdigest()
    print(json.dumps(out,sort_keys=True,indent=2))
    if args.check_results:
        frozen=json.loads(args.check_results.read_text(encoding='utf-8'))
        if frozen!=out:
            raise SystemExit('frozen result mismatch')
        print('frozen result check passed')
if __name__=='__main__': main()
