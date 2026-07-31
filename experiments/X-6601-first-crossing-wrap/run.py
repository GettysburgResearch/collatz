#!/usr/bin/env python3
"""Exact finite regression for L/T-6601--T-6607.

This is a bounded adversarial audit only. It does not prove any all-length claim.
All decisions use Python integers; no floating point enters.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
from typing import Iterable

sys.set_int_max_str_digits(0)

def min_supercritical_ones(k: int) -> int:
    q = 0
    p3 = 1
    p2 = 1 << k
    while p3 < p2:
        q += 1
        p3 *= 3
    return q

def valid_length(j: int) -> tuple[bool,int,list[int]]:
    lower=[0]+[min_supercritical_ones(k) for k in range(1,j)]
    q=lower[j-1]
    return (pow(3,q)<(1<<j), q, lower)

def generate_words(j: int, q: int, lower: list[int]) -> Iterable[tuple[int,...]]:
    # The final bit is forced even; build the first j-1 bits.
    def rec(pos: int, ones: int, out: list[int]):
        if pos==j-1:
            if ones==q:
                yield tuple(out+[0])
            return
        remaining=(j-1)-pos
        for bit in (0,1):
            new=ones+bit
            k=pos+1
            if new<lower[k] or new>q:
                continue
            if new+(remaining-1)<q:
                continue
            yield from rec(pos+1,new,out+[bit])
    yield from rec(0,0,[])

def mechanical_word(j: int, q: int, lower: list[int]) -> tuple[int,...]:
    counts=lower[:j]
    bits=[counts[k]-counts[k-1] for k in range(1,j)]
    bits.append(0)
    w=tuple(bits)
    assert sum(w)==q and all(b in (0,1) for b in w)
    return w

def affine(word: tuple[int,...]) -> tuple[int,int]:
    A=0
    q=0
    for k,bit in enumerate(word):
        if bit:
            A=3*A+(1<<k)
            q+=1
    return q,A

def odd_positions(word: tuple[int,...]) -> list[int]:
    return [i for i,b in enumerate(word) if b]

def canonical(word: tuple[int,...]) -> tuple[int,int,int,int]:
    j=len(word)
    q,A=affine(word)
    mod=1<<j
    r=(-A*pow(pow(3,q),-1,mod))%mod
    if r==0:
        raise AssertionError("first-crossing residue unexpectedly zero")
    y=(pow(3,q)*r+A)//mod
    # Physical replay and exact parity.
    x=r
    for bit in word:
        if (x&1)!=bit:
            raise AssertionError("parity replay mismatch")
        x=x//2 if bit==0 else (3*x+1)//2
    if x!=y:
        raise AssertionError("endpoint mismatch")
    return r,y,q,A

def v2(n: int) -> int:
    n=abs(n)
    if n==0: raise ValueError("v2(0)")
    return (n & -n).bit_length()-1

def prefix_excess(word: tuple[int,...], lower: list[int]) -> int:
    s=0
    total=0
    for m,b in enumerate(word,1):
        s+=b
        if m<len(word):
            total+=s-lower[m]
    return total

def factors(word: tuple[int,...], L: int) -> list[tuple[int,...]]:
    return [word[i:i+L] for i in range(len(word)-L+1)]

def first_repeat(word: tuple[int,...], L: int):
    seen={}
    for i,z in enumerate(factors(word,L)):
        if z in seen:
            return seen[z],i
        seen[z]=i
    return None

def build(max_j: int) -> dict:
    rows=[]
    total_words=total_wrap=total_nowrap=0
    semantic=hashlib.sha256()
    global_nontrivial_failures=[]
    for j in range(2,max_j+1):
        ok,q,lower=valid_length(j)
        if not ok:
            continue
        w=mechanical_word(j,q,lower)
        rw,yw,qw,Aw=canonical(w)
        D=(1<<j)-pow(3,q)
        dw=rw-yw
        E_num=Aw
        words=wraps=nowraps=0
        min_delta=None
        min_root=None
        first_word=None
        for v in generate_words(j,q,lower):
            words+=1
            total_words+=1
            rv,yv,qv,Av=canonical(v)
            assert qv==q
            delta_v=rv-yv
            if min_delta is None or (delta_v,rv,v)<(min_delta,min_root,first_word):
                min_delta,min_root,first_word=delta_v,rv,v
            if not (j==2 and v==(1,0)) and delta_v<=0:
                global_nontrivial_failures.append(
                    {"j":j,"word":"".join(map(str,v)),"r":rv,"y":yv,"delta":delta_v}
                )
            I=prefix_excess(v,lower)
            dv=odd_positions(v)
            ew=odd_positions(w)
            shifts=[b-a for a,b in zip(dv,ew)]
            if any(h<0 for h in shifts) or sum(shifts)!=I:
                raise AssertionError("swap-distance identity")
            H=sum(a!=b for a,b in zip(v,w))
            if H>2*I:
                raise AssertionError("Hamming/swap bound")
            for L in range(1,j+1):
                pv=len(set(factors(v,L)))
                if pv>L+2+2*I*L:
                    raise AssertionError("factor complexity bound")
            Lstar=(j-2)//(2*(I+1))
            if Lstar>=1 and first_repeat(v,Lstar) is None:
                raise AssertionError("forced repeated factor missing")
            Delta=Aw-Av
            if v==w:
                if Delta!=0 or I!=0:
                    raise AssertionError("mechanical identity")
            else:
                if Delta<=0:
                    raise AssertionError("mechanical numerator not maximal")
                moved=[(d,h) for d,h in zip(dv,shifts) if h>0]
                dstar=min(d for d,h in moved)
                if v2(Delta)!=dstar:
                    raise AssertionError("two-place valuation")
                mod=1<<j
                residue=(Delta*pow(pow(3,q),-1,mod))%mod
                if (rv-rw-residue)%mod:
                    raise AssertionError("canonical displacement")
                s=(-Delta*pow(D,-1,mod))%mod
                if s!=residue or not (1<=s<mod):
                    raise AssertionError("D-inverse displacement")
                wrap=(rw+s)>=mod
                if wrap:
                    wraps+=1; total_wrap+=1
                else:
                    nowraps+=1; total_nowrap+=1
                m=(D*s+Delta)//mod
                if D*s+Delta!=m*mod or m<=0:
                    raise AssertionError("wrap quotient")
                predicted=dw+m-(D if wrap else 0)
                if delta_v!=predicted:
                    raise AssertionError("descent-defect transport")
                if wrap:
                    u=mod-s
                    h=D-m
                    if rv!=rw-u or Delta!=D*u-h*mod:
                        raise AssertionError("wrap coordinates")
                    if delta_v!=dw-h or yv!=yw-u+h:
                        raise AssertionError("physical wrap coordinates")
                    if delta_v<=0 and not (dw<=h<dw+Aw/mod):
                        raise AssertionError("dangerous window")
            semantic.update(
                f"{j}|{''.join(map(str,v))}|{rv}|{yv}|{delta_v}|{I}|{Delta}\n".encode()
            )
        rows.append({
            "j":j,
            "q":q,
            "word_count":words,
            "mechanical_word":"".join(map(str,w)),
            "mechanical_root":rw,
            "mechanical_endpoint":yw,
            "mechanical_delta":dw,
            "mechanical_remainder_numerator":E_num,
            "D":D,
            "wrap_words":wraps,
            "no_wrap_words":nowraps,
            "minimum_delta":min_delta,
            "minimum_delta_root":min_root,
            "minimum_delta_word":"".join(map(str,first_word)),
        })
    if global_nontrivial_failures:
        raise AssertionError(f"empirical Box-2 failures: {global_nontrivial_failures[:3]}")
    payload={
        "experiment_id":"X-6601",
        "status":"EXACT FINITE REGRESSION / NOT A PROOF OF ALL LENGTHS",
        "max_length":max_j,
        "valid_first_crossing_lengths":len(rows),
        "total_first_crossing_words":total_words,
        "total_nonmechanical_wrap_words":total_wrap,
        "total_nonmechanical_no_wrap_words":total_nowrap,
        "nontrivial_canonical_descent_failures":0,
        "trivial_equality":{"j":2,"word":"10","root":1,"endpoint":1},
        "rows":rows,
        "semantic_sha256":semantic.hexdigest(),
    }
    return payload

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--max-length",type=int,default=24)
    ap.add_argument("--output",type=Path)
    ap.add_argument("--check-results",type=Path)
    args=ap.parse_args()
    payload=build(args.max_length)
    text=json.dumps(payload,sort_keys=True,indent=2)+"\n"
    if args.check_results:
        expected=args.check_results.read_text()
        if text!=expected:
            raise SystemExit("result mismatch")
    if args.output:
        args.output.write_text(text)
    else:
        print(text,end="")
if __name__=="__main__":
    main()
