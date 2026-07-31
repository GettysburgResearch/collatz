#!/usr/bin/env python3
"""Independent exact reconstruction for X-6601.

Imports no author-side module. The finite horizon is read from the artifact.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
sys.set_int_max_str_digits(0)

def ceil_alpha_count(k):
    q=0
    while 3**q < 2**k:
        q+=1
    return q

def lengths(n):
    for j in range(2,n+1):
        lows=[0]+[ceil_alpha_count(k) for k in range(1,j)]
        q=lows[-1]
        if 3**q < 2**j:
            yield j,q,lows

def words(j,q,lows):
    stack=[(0,0,())]
    while stack:
        pos,o,prefix=stack.pop()
        if pos==j-1:
            if o==q:
                yield prefix+(0,)
            continue
        rem=j-1-pos
        # push 1 then 0 so traversal is 0,1 after pop
        for b in (1,0):
            z=o+b
            k=pos+1
            if z<lows[k] or z>q or z+rem-1<q:
                continue
            stack.append((pos+1,z,prefix+(b,)))

def mech(j,q,lows):
    out=tuple([lows[k]-lows[k-1] for k in range(1,j)]+[0])
    assert sum(out)==q and set(out)<=set((0,1))
    return out

def aff(w):
    positions=[i for i,b in enumerate(w) if b]
    q=len(positions)
    A=sum(3**(q-i-1)*2**d for i,d in enumerate(positions))
    return positions,A

def root_endpoint(w):
    pos,A=aff(w); q=len(pos); j=len(w); M=2**j
    r=(-A*pow(3**q,-1,M))%M
    assert r
    y=(3**q*r+A)//M
    z=r
    got=[]
    for b in w:
        got.append(z%2)
        z=(z//2) if z%2==0 else ((3*z+1)//2)
    assert tuple(got)==w and z==y
    return pos,A,r,y

def ord2(n):
    n=abs(n); assert n
    c=0
    while n%2==0:
        c+=1; n//=2
    return c

def excess(w,lows):
    s=t=0
    for k,b in enumerate(w,1):
        s+=b
        if k<len(w): t+=s-lows[k]
    return t

def facs(w,L):
    return [w[k:k+L] for k in range(len(w)-L+1)]

def rebuild(maxj):
    table=[]
    count=wraps_total=nowraps_total=0
    digest=hashlib.sha256()
    failures=[]
    for j,q,lows in lengths(maxj):
        w=mech(j,q,lows)
        ep,Aw,rw,yw=root_endpoint(w)
        den=2**j-3**q
        d0=rw-yw
        wc=wr=nw=0
        champion=None
        for v in words(j,q,lows):
            wc+=1; count+=1
            dp,Av,rv,yv=root_endpoint(v)
            d=rv-yv
            key=(d,rv,v)
            champion=key if champion is None or key<champion else champion
            if not (j==2 and v==(1,0)) and d<=0:
                failures.append((j,v,rv,yv,d))
            I=excess(v,lows)
            shifts=[b-a for a,b in zip(dp,ep)]
            assert min(shifts)>=0 and sum(shifts)==I
            assert sum(a!=b for a,b in zip(v,w))<=2*I
            for L in range(1,j+1):
                assert len(set(facs(v,L)))<=L+2+2*I*L
            Ls=(j-2)//(2*(I+1))
            if Ls:
                fs=facs(v,Ls)
                assert len(set(fs))<len(fs)
            DA=Aw-Av
            if v==w:
                assert DA==I==0
            else:
                assert DA>0
                dstar=min(d for d,h in zip(dp,shifts) if h)
                assert ord2(DA)==dstar
                M=2**j
                res=DA*pow(3**q,-1,M)%M
                assert (rv-rw)%M==res
                s=(-DA*pow(den,-1,M))%M
                assert s==res and s
                wrapped=rw+s>=M
                wr+=wrapped; nw+=not wrapped
                wraps_total+=wrapped; nowraps_total+=not wrapped
                m=(den*s+DA)//M
                assert den*s+DA==m*M and m>0
                assert d==d0+m-(den if wrapped else 0)
                if wrapped:
                    u=M-s; h=den-m
                    assert rv==rw-u
                    assert DA==den*u-h*M
                    assert d==d0-h
                    assert yv==yw-u+h
                    if d<=0:
                        assert d0<=h<d0+Aw/M
            digest.update(f"{j}|{''.join(map(str,v))}|{rv}|{yv}|{d}|{I}|{DA}\n".encode())
        assert champion is not None
        table.append({
            "j":j,"q":q,"word_count":wc,
            "mechanical_word":"".join(map(str,w)),
            "mechanical_root":rw,"mechanical_endpoint":yw,
            "mechanical_delta":d0,
            "mechanical_remainder_numerator":Aw,
            "D":den,"wrap_words":wr,"no_wrap_words":nw,
            "minimum_delta":champion[0],
            "minimum_delta_root":champion[1],
            "minimum_delta_word":"".join(map(str,champion[2])),
        })
    assert not failures
    return {
        "experiment_id":"X-6601",
        "status":"EXACT FINITE REGRESSION / NOT A PROOF OF ALL LENGTHS",
        "max_length":maxj,
        "valid_first_crossing_lengths":len(table),
        "total_first_crossing_words":count,
        "total_nonmechanical_wrap_words":wraps_total,
        "total_nonmechanical_no_wrap_words":nowraps_total,
        "nontrivial_canonical_descent_failures":0,
        "trivial_equality":{"j":2,"word":"10","root":1,"endpoint":1},
        "rows":table,
        "semantic_sha256":digest.hexdigest(),
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("artifact",type=Path)
    a=ap.parse_args()
    frozen=json.loads(a.artifact.read_text())
    rebuilt=rebuild(int(frozen["max_length"]))
    if rebuilt!=frozen:
        raise SystemExit("independent reconstruction mismatch")
    print(json.dumps({
        "verified":True,
        "max_length":rebuilt["max_length"],
        "words":rebuilt["total_first_crossing_words"],
        "semantic_sha256":rebuilt["semantic_sha256"],
    },sort_keys=True))
if __name__=="__main__":
    main()
