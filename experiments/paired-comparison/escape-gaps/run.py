#!/usr/bin/env python3
"""Construct exact gap/affine merger cylinders and retain failed comparison inputs.
Standard library only. Claims EG-001--006 are PROPOSED, not a Collatz proof.
"""
from __future__ import annotations
import argparse
from collections import Counter
from functools import lru_cache
import hashlib
import json
from pathlib import Path


def need(ok, text):
    if not ok:
        raise ValueError(text)


def integer(x, minimum=0):
    need(type(x) is int and x >= minimum, "invalid integer")
    return x


def v2(x):
    integer(x, 1)
    return (x & -x).bit_length()-1


def step(x):
    integer(x, 1)
    return (3*x+1)//2 if x & 1 else x//2


def path(x, word):
    integer(x, 1)
    out=[x]
    for p in word:
        need(p in "01" and (x & 1)==int(p), "nonphysical word")
        x=step(x); out.append(x)
    return out


def symbolic(a, b, word):
    integer(a, 1); integer(b, 1)
    for p in word:
        need(p in "01" and a%2==0 and b%2==int(p), "nonuniform cylinder")
        if p=="1":
            a,b=3*a,3*b+1
        a//=2; b//=2
    return [a,b]


@lru_cache(maxsize=None, typed=True)
def gap(g, variant=0):
    integer(g, 1); integer(variant)
    need(variant in (0,1,2), "unknown gap compiler")
    # Iterative construction avoids Python recursion-depth assumptions.
    stack=[]; h=g
    while h>1:
        if h%2==0:
            stack.append((h, "even", 1)); h//=2
        elif variant<2:
            if h%4==1:
                stack.append((h, "plus", 2)); h=(3*h+1)//4
            else:
                stack.append((h, "minus", 2)); h=(3*h-1)//4
        else:
            j=v2(3*h-1)
            stack.append((h, "long", j+1))
            h=((3*h-1)//2**j+1)//2
    if variant==0:
        length,b,w,z=3,4,"001","100"
    else:
        length,b,w,z=5,5,"10001","01100"
    for old, mode, ell in reversed(stack):
        if mode=="even":
            b*=2; length+=1; w="0"+w; z="0"+z
        else:
            if mode=="plus":
                offset=1; left,right="10","01"
            elif mode=="minus":
                offset=2; left,right="01","10"
            else:
                offset=1; left,right="1"+"0"*(ell-1),"0"*(ell-1)+"1"
            target=offset*pow(2**ell,-1,3)%3
            t=(target-b)*pow(2**length,-1,3)%3
            b=(2**ell*(b+2**length*t)-offset)//3
            length+=ell; w=left+w; z=right+z
    mod=2**length
    ep=symbolic(mod,b,w)
    need(ep==symbolic(mod,b+g,z), "gap endpoint mismatch")
    need(0<b<mod and len(w)==len(z)==length, "gap normalization")
    need(w.count("1")==z.count("1"), "odd-count mismatch")
    if variant<2:
        need(mod<=(8 if variant==0 else 32)*g**7,"polynomial modulus bound")
    if variant==2:
        need((b+g)%2==0, "upper-even variant failure")
    return dict(kind="gap",g=g,variant=variant,modulus=mod,residue=b,
                left=w,right=z,endpoint=ep)


@lru_cache(maxsize=None, typed=True)
def affine(a, b, variant=0):
    integer(a,1); need(type(b) is int,"invalid intercept")
    integer(variant); need(variant in (0,1,2),"unknown compiler")
    A=3**a; c=A-b
    need(c>2**a,"balanced-shadow guard fails")
    cnow=c; evens=0; negative=""
    # This is a resource ceiling, not a mathematical cutoff or a success.
    while evens<a:
        need(len(negative)<100000,"negative-prefix budget exhausted")
        p=cnow%2; negative+=str(p)
        if p:
            cnow=(3*cnow-1)//2
        else:
            cnow//=2; evens+=1
        need(cnow>1,"negative shadow reached fixed point unexpectedly")
    ell=len(negative); tail=gap(cnow-1,variant)
    m=tail["modulus"]
    u=(tail["residue"]+cnow)*pow(3**ell,-1,m)%m
    if u==0:
        u=m
    modulus=2**ell*m; d=2**ell*u-1
    if A*d+b<=0:
        d+=modulus*((-A*d-b)//(A*modulus)+1)
    w=negative+tail["left"]; z="1"*ell+tail["right"]
    ep=symbolic(A*modulus,A*d+b,w)
    need(ep==symbolic(modulus,d,z),"affine endpoint mismatch")
    return dict(kind="affine",a=a,b=b,variant=variant,modulus=modulus,
                residue=d,left=w,right=z,endpoint=ep,negative=negative,
                negative_endpoint=cnow,gap=cnow-1)


def vl_transition(c):
    """Re-derive the parent #125 transition; do not import its implementation."""
    av,bv=v2(3*c-2),v2(3*c-1)
    if av>=3 and av%2==1:
        k=(av-3)//2; b=(3*c-2)//2**av
        d=(3**(k+1)*b+1)//2
        w,z="00"+"01"*k+"00","01"+"10"*k+"11"
    elif bv>=4 and bv%2==0:
        k=(bv-4)//2; b=(3*c-1)//2**bv
        d=(3**(k+2)*b+1)//2
        w,z="100"+"01"*k+"00","110"+"10"*k+"11"
    else:
        return None
    s=v2(d+1); q=3**s*((d+1)//2**s)
    if q%4==3:
        return True,(3*q-1)//4,w+"1"*s+"01",z+"1"*s+"00"
    return False,(q-1)//4,w+"1"*s+"00",z+"1"*s+"01"


def normalized_escape(c):
    s=v2(c)//2; a=s+2; d=c//4**s
    w,z="01"*s,"00"*s
    if d%2==0:
        d=(3*d+2)//4; a-=1; b=(1-3**a)//2
        w+="00"; z+="01"
    else:
        b=2
    need(path(9*c+2,w)[-1]==3**a*d+b and path(c,z)[-1]==d,
         "normalization failure")
    return a,b,d,w,z


def classify(c0, used, budget=256):
    c=c0; orientation=0; words=["",""]
    for count in range(budget):
        tr=vl_transition(c)
        if tr is None:
            break
        merge,d,w,z=tr
        words[orientation]+=w; words[1-orientation]+=z
        if merge:
            return dict(kind="comparison",c=c0,baseline="MERGE",status="MERGE",
                        mechanism="parent",left=words[0],right=words[1],endpoint=d)
        c=d; orientation=1-orientation
    else:
        return dict(kind="comparison",c=c0,baseline="BUDGET",status="BUDGET",
                    terminal=c,left=words[0],right=words[1])
    a,b,d,w,z=normalized_escape(c)
    for variant in range(3):
        key=(a,b,variant); used.add(key); cert=affine(*key)
        if d>=cert["residue"] and (d-cert["residue"])%cert["modulus"]==0:
            words[orientation]+=w+cert["left"]
            words[1-orientation]+=z+cert["right"]
            x=path(9*c0+2,words[0])[-1]; y=path(c0,words[1])[-1]
            need(x==y,"composed certificate mismatch")
            return dict(kind="comparison",c=c0,baseline="OUTSIDE",status="MERGE",
                        mechanism="escape",gate=list(key),left=words[0],right=words[1],
                        endpoint=x,terminal=c)
    return dict(kind="comparison",c=c0,baseline="OUTSIDE",status="OUTSIDE",
                terminal=c,left=words[0],right=words[1])


def crt_lift(modulus, residue, exponent, r):
    """4*C+1 = 3^exponent * 2^(-r) mod 3^(exponent+1)."""
    q=3**(exponent+1)
    target=(3**exponent*pow(2,-r,3)-1)*pow(4,-1,q)%q
    t=(target-residue)*pow(modulus,-1,q)%q
    c=residue+modulus*t
    need((4*c+1)%3**exponent==0,"CRT integrality")
    return c


def original(family, index, variant=0, extra=0):
    if family=="escape":
        s=index; cert=affine(s+2,2,variant)
        mod=4**s*cert["modulus"]; residue=4**s*cert["residue"]
        tail1="01"*s+cert["left"]; tail2="00"*s+cert["right"]
        minimum_r=2
    elif family=="rung":
        j=index; cert=affine(2*j,(9**j-1)//4,variant)
        mod,residue=cert["modulus"],cert["residue"]
        tail1,tail2=cert["left"],cert["right"]
        minimum_r=2*j
    else:
        raise ValueError("unknown original family")
    K=2+len(tail1); r=minimum_r
    while 3**r<2**(r+K):
        r+=1
    r+=extra
    exponent=r-1 if family=="escape" else r-2*index+1
    c=crt_lift(mod,residue,exponent,r)
    u=(4*c+1)//3**exponent
    n=2**r*u-1
    if family=="escape":
        m=(n-1)//2; lower="1"*(r-1)+"00"
    else:
        j=index; m=(n-(4**j-1)//3)//2
        lower="1"+"0"*(2*j-2)+"1"*(r-2*j)+"00"
    w="1"*r+"01"+tail1; z=lower+tail2
    x,y=path(n,w),path(m,z)
    need(x[-1]==y[-1] and 0<m<n and n%3==0,"original-source failure")
    need(min(x[1:])>n and len(w)==len(z)+1,"original no-descent/clock failure")
    if family=="rung" and index%3==2:
        third=(n-(4**index-1)//3-1)//3
        need(0<third<n//3 and path(third,"1"+z)[-1]==x[-1],"one-third lift")
    return dict(kind="original",family=family,index=index,variant=variant,r=r,u=u,
                c=c,n=n,m=m,left=w,right=z,endpoint=x[-1],minimum=min(x[1:]),
                tail_steps=K,no_forward_descent=True)


def common_window(x,y):
    i,j=v2(x),v2(y)
    second_x=i+v2(3*(x//2**i)+1)
    second_y=j+v2(3*(y//2**j)+1)
    ell=min(second_x,second_y)
    if ell<max(i,j)+1 or ell<2:
        return None
    p="0"*i+"1"+"0"*(ell-i-1)
    q="0"*j+"1"+"0"*(ell-j-1)
    return p,q


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full",type=Path,required=True)
    parser.add_argument("--output",type=Path)
    parser.add_argument("--check",type=Path)
    parser.add_argument("--limit",type=int,default=65536)
    args=parser.parse_args(); need(1<=args.limit<=65536,"unsupported grid")
    counts=Counter(); digest=hashlib.sha256(); used=set(); examples=[]; new_samples=[]
    with args.full.open("w",encoding="utf-8",newline="\n") as out:
        def emit(row):
            text=json.dumps(row,sort_keys=True,separators=(",",":"))+"\n"
            out.write(text); digest.update(text.encode()); counts[row["kind"]]+=1
        for g in list(range(1,4097))+[2**127-1,2**128,10**50+17,2**255+12345]:
            for variant in range(3):
                emit(gap(g,variant))
        for a in range(2,65):
            for variant in range(3): used.add((a,2,variant))
        for j in range(1,33):
            for variant in range(3):
                used.add((2*j,(9**j-1)//4,variant))
                used.add((j,(1-3**j)//2,variant))
        # Establish all gate keys needed by the bounded comparison census.
        for c in range(1,args.limit+1):
            a,b,_,_,_=normalized_escape(c)
            for variant in range(3): used.add((a,b,variant))
        for family in ("escape","rung"):
            for index in range(1,17):
                for extra in (0,7):
                    row=original(family,index,0,extra)
                    examples.append({k:row[k] for k in ("family","index","r","n","m","endpoint","minimum")})
                    emit(row)
                    if family=="rung" and index%3==2:counts["one_third_controls"]+=1
        emitted_keys=set(used)
        for key in sorted(emitted_keys): emit(affine(*key))
        for c in range(1,args.limit+1):
            row=classify(c,used)
            counts["baseline_"+row["baseline"]]+=1
            counts["new_"+row["status"]]+=1
            if row.get("mechanism")=="escape":
                counts["additional_mergers"]+=1
                if len(new_samples)<24:new_samples.append(c)
            emit(row)
        # Gate keys introduced only after parent hard returns must be emitted too.
        # Newly encountered post-return types must not silently lack a catalog row.
        need(emitted_keys==used,"gate inventory incomplete after hard returns")
        for x in range(1,129):
            for y in range(x+1,257):
                w=common_window(x,y)
                if w is None:continue
                p,q=w; X,Y=path(x,p)[-1],path(y,q)[-1]
                need(max(X,Y)<y or (x,y)==(1,2),"window maximum rank")
                need(y-x<2 or abs(Y-X)<y-x,"window gap rank")
                counts["window_controls"]+=1
        result=dict(schema="escape-gap-v1",status="PROPOSED",complete_collatz_proof=False,
                    limit=args.limit,counts=dict(sorted(counts.items())),rows_sha256=digest.hexdigest(),
                    additional_samples=new_samples,original_examples=examples[:4]+examples[32:36],
                    parent="081dd4fb8af75b3b237a5eb4cef28b84bb5329be")
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:args.output.write_text(text,encoding="utf-8")
    if args.check:need(args.check.read_text(encoding="utf-8")==text,"canonical mismatch")
    print(text,end="")


if __name__=="__main__":
    main()
