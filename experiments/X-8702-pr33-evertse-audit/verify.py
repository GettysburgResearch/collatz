#!/usr/bin/env python3
"""Independent verifier for X-8702; does not import run.py."""
from __future__ import annotations
import argparse, functools, hashlib, itertools, json, platform, random
from fractions import Fraction
from pathlib import Path

SEED=0x870233
P=(5,30,20,56)
CORE=(9,54,36,24)


def digest(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def valuation(n,p):
    n=abs(n); c=0
    if n==0:return 10**9
    while n%p==0:n//=p;c+=1
    return c


@functools.lru_cache(maxsize=None)
def anchors(kind,t):
    h=2**(11*(t+1)); n=3**(7*(t+1))
    a=h*P[kind]//64; b=(n*P[kind]+CORE[kind])//64
    assert h*P[kind]==64*a and n*P[kind]+CORE[kind]==64*b
    return h,n,a,b


@functools.lru_cache(maxsize=None)
def inverse_pair(t,u):
    _,n,_,_=anchors(0,t); h,_,_,_=anchors(0,u)
    return pow(n,-1,h)


def solve_connector(i,t,j,u):
    _,n,_,b=anchors(i,t); h,_,a,_=anchors(j,u)
    eta=((a-b)*inverse_pair(t,u))%h
    theta=(b+n*eta-a)//h
    assert b+n*eta==a+h*theta and 0<=eta<h and 0<=theta<n
    return P[i]+64*eta,P[j]+64*theta


def reconstruct_connectors(expected):
    rows=[]; connector_cases=local_cases=0
    for m in (12,13):
        base=2**m; d=2**(m-8)
        t=[base+j*d for j in range(257)]+[2*base+2*d]
        positions=(0,127,255) if m==12 else (0,255)
        rng=random.Random(SEED+m)
        triples=rng.sample(list(itertools.product(range(4),repeat=3)),4 if m==12 else 2)
        for pos in positions:
            for i,j,k in triples:
                x0,y0=solve_connector(i,t[pos],j,t[pos+1])
                x1,_=solve_connector(j,t[pos+1],k,t[pos+2])
                connector_cases+=2
                hm=anchors(j,t[pos+1])[0]; hn=anchors(k,t[pos+2])[0]; ns=anchors(i,t[pos])[1]
                assert (y0-x1)%64==0
                c=(y0-x1)//64
                rho=(-c*pow(ns,-1,hn))%hn
                z=(ns*rho+c)//hn
                Z0=x0+64*hm*rho; Z1=x1+64*hn*z
                assert hm*Z1==ns*Z0+CORE[i]
                local_cases+=1
                if len(rows)<12:
                    rows.append({"m":m,"position":pos,"types":[i,j,k],
                        "eta_bits":(x0-P[i]).bit_length(),"correction_bits":rho.bit_length(),
                        "Z0_mod_64":Z0%64})
        A=7*sum(t[j]+1 for j in range(256)); E=11*sum(t[j]+1 for j in range(1,257))
        assert A==Fraction(5369,2)*2**m+1792 and E==Fraction(8459,2)*2**m+2816
        L=2**(m-9)
        for j in range(256):
            assert 11*sum(t[s]+1 for s in range(1,j+1))==11*j*(j+513)*L+11*j
            assert 7*sum(t[s]+1 for s in range(j+1,256))==7*(255-j)*(j+768)*L+7*(255-j)
    assert connector_cases==expected["connector_cases"]
    assert local_cases==expected["local_conjugacy_cases"]
    assert digest(rows)==expected["sample_digest"]


def reconstruct_signed(expected):
    rng=random.Random(SEED); positive=negative=0
    for _ in range(expected["cases"]):
        p=rng.randrange(1,10**8)|1; q=rng.randrange(4*p+1,8*p+100)
        s=rng.randrange(p); y=rng.randint(-10000,10000)
        yn,r=divmod(s+p*y,q)
        assert s+p*y==r+q*yn and 0<=r<q
        if y>=0:
            assert 0<=yn<Fraction(p,q)*(y+1); positive+=1
        else:
            k=-y-1; kn=-yn-1
            assert kn>=0 and q*kn==p*k+(p-s)-(q-r)
            assert kn<Fraction(p,q)*(k+1); negative+=1
    assert positive==expected["nonnegative"] and negative==expected["negative"]


def reconstruct_gates(expected):
    assert 3**53>2**84 and 3**41<2**65
    cap=Fraction(161341,44508739); end=Fraction(6498,346819)
    assert cap<Fraction(1,275) and end<Fraction(1,50)
    assert expected["cap_height_ratio"]==f"{cap.numerator}/{cap.denominator}"
    assert expected["endpoint_product_ratio"]==f"{end.numerator}/{end.denominator}"
    rows=0
    for i,j,k in itertools.product(range(4),repeat=3):
        assert valuation(CORE[i],2)<=3 and valuation(CORE[j],3)<=3 and valuation(P[k],2)<=3
        rows+=1
    assert rows==expected["primitive_rows"] and expected["primitive_gcd_cap"]==216
    intervals=[]; hi=None
    for m in range(12,31):
        E=int(Fraction(8459,2)*2**m+2816); interval=[m,E-3,E+3]
        if hi is not None:assert interval[1]>hi
        hi=interval[2];intervals.append(interval)
    assert intervals==expected["projective_intervals"]
    assert expected["evertse_parameters"]=={"n":257,"c":1,"d":"1/50","S0":[2,3]}


def main():
    ap=argparse.ArgumentParser();ap.add_argument("certificate",type=Path);a=ap.parse_args()
    c=json.loads(a.certificate.read_text())
    reconstruct_connectors(c["actual_connectors"])
    reconstruct_signed(c["signed_quotients"])
    reconstruct_gates(c["arithmetic_gates"])
    x=dict(c);recorded=x.pop("semantic_digest");assert digest(x)==recorded
    print("all independent X-8702 arithmetic checks passed")
    print(json.dumps({"python":platform.python_version(),"platform":platform.platform()},sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
