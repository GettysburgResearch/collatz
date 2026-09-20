#!/usr/bin/env python3
"""Universal finite-family synchronization and a bounded successive-type selector.
PROPOSED; not a complete Collatz proof. Standard library only.
The gap, restricted affine, VL and normalization primitives are retained from
PR127 f5e7ec9a23fa691d71a5a9f518cbff5529a5ea00, with their hypotheses intact.
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


def actual(n, length):
    integer(n,1); integer(length)
    word=[]
    for _ in range(length):
        word.append(str(n%2)); n=step(n)
    return n,"".join(word)


@lru_cache(maxsize=None, typed=True)
def universal(a, b):
    """One synchronous whole-cylinder gate for every a>=0, integer b."""
    integer(a); need(type(b) is int,"invalid intercept")
    if a==0:
        if b==0:
            result=dict(modulus=1,residue=1,left="",right="")
        else:
            f=gap(abs(b))
            result=dict(modulus=f["modulus"],residue=f["residue"]+max(-b,0),
                        left=f["right"] if b>0 else f["left"],
                        right=f["left"] if b>0 else f["right"])
    else:
        length=0; word=""; A=a; B=b
        if 3**a-b<=2**a:
            need(b>0,"preconditioning sign")
            length=(2*b).bit_length(); B,word=actual(b,length)
            A=a+word.count("1")
        need(3**A-B>2**A,"preconditioning failed")
        f=affine(A,B)
        result=dict(modulus=2**length*f["modulus"],residue=2**length*f["residue"],
                    left=word+f["left"],right="0"*length+f["right"])
    mod,d=result["modulus"],result["residue"]
    ep=symbolic(3**a*mod,3**a*d+b,result["left"])
    need(ep==symbolic(mod,d,result["right"]),"universal endpoint")
    need(mod==2**len(result["left"]) and len(result["left"])==len(result["right"]),
         "universal clock")
    return dict(kind="gate",a=a,b=b,endpoint=ep,**result)


def synchronize(forms, modulus=1, residue=0):
    """Merge a finite family (3**a*x+b), preserving x=residue mod modulus."""
    need(type(forms) is list and len(forms)>0,"empty/invalid family")
    integer(modulus,1); need(type(residue) is int,"invalid residue")
    for form in forms:
        need(type(form) in (list,tuple) and len(form)==2,"invalid form")
        integer(form[0]); need(type(form[1]) is int,"invalid intercept")
    k=v2(modulus); odd=modulus//2**k; mod=2**k; d=residue%mod
    lower=max(1,max((-b)//(3**a)+1 for a,b in forms))
    if d<lower:d+=mod*((lower-d+mod-1)//mod)
    ends=[]; words=[]; powers=[]; length=k
    for a,b in forms:
        e,w=actual(3**a*d+b,k)
        ends.append(e); words.append(w); powers.append(a+w.count("1"))
    for j in range(1,len(forms)):
        hi,lo=(0,j) if powers[0]>=powers[j] else (j,0)
        a=powers[hi]-powers[lo]; b=ends[hi]-3**a*ends[lo]
        f=universal(a,b); m=f["modulus"]; target=f["residue"]
        t=(target-ends[lo])*pow(3**powers[lo],-1,m)%m
        deficit=target-(ends[lo]+3**powers[lo]*t)
        if deficit>0:t+=m*((deficit+3**powers[lo]*m-1)//(3**powers[lo]*m))
        ell=len(f["left"])
        for i in range(len(forms)):
            e,w=actual(ends[i]+3**powers[i]*t,ell)
            ends[i]=e; words[i]+=w; powers[i]+=w.count("1")
        d+=mod*t; mod*=m; length+=ell
        need(len(set(ends[:j+1]))==len(set(powers[:j+1]))==1,"lost common endpoint")
    t=(residue-d)*pow(mod,-1,odd)%odd if odd>1 else 0
    for i in range(len(forms)):ends[i]+=3**powers[i]*t
    d+=mod*t; mod*=odd
    ep=[odd*3**powers[0],ends[0]]
    for i,(a,b) in enumerate(forms):
        need(symbolic(3**a*mod,3**a*d+b,words[i])==ep,"family cylinder")
    need(d%modulus==residue%modulus and mod%modulus==0,"lost prescribed class")
    return dict(kind="family",forms=[list(f) for f in forms],input_modulus=modulus,
                input_residue=residue,modulus=mod,residue=d,length=length,
                words=words,endpoint=ep)


def strip_slope(A):
    integer(A,1);s=v2(A);D=A//2**s;a=0
    while D%3==0:D//=3;a+=1
    return D,s,a


def linear_synchronize(forms, modulus=1, residue=0):
    """Complete feasibility classification for arbitrary positive integer slopes.
    Matching 6-free parts is equivalent to a uniform asynchronous affine merger.
    """
    need(type(forms) is list and len(forms)>0,"invalid linear family")
    integer(modulus,1);need(type(residue) is int,"invalid class")
    parts=[]
    for form in forms:
        need(type(form) in (list,tuple) and len(form)==2,"linear form")
        A,b=form;integer(A,1);need(type(b) is int,"linear intercept")
        parts.append(strip_slope(A))
    base=dict(kind="linear",forms=[list(f) for f in forms],input_modulus=modulus,input_residue=residue)
    if len({d for d,s,a in parts})>1:
        return dict(**base,status="IMPOSSIBLE_UNIFORM",six_free_parts=[d for d,s,a in parts])
    D=parts[0][0];k=v2(modulus);odd=modulus//2**k;mod=2**k;d=residue%mod
    lower=max(1,max((-b)//A+1 for A,b in forms))
    if d<lower:d+=mod*((lower-d+mod-1)//mod)
    words=[];ends=[];powers=[];length=k
    for (A,b),(_,s,a) in zip(forms,parts):
        e,w=actual(A*d+b,k+s);words.append(w);ends.append(e);powers.append(a+w.count("1"))
    for j in range(1,len(forms)):
        hi,lo=(0,j) if powers[0]>=powers[j] else (j,0)
        a=powers[hi]-powers[lo];b=ends[hi]-3**a*ends[lo]
        f=universal(a,b);m=f["modulus"];R=f["residue"];coef=D*3**powers[lo]
        t=(R-ends[lo])*pow(coef,-1,m)%m
        if ends[lo]+coef*t<R:t+=m*((R-ends[lo]-coef*t+coef*m-1)//(coef*m))
        ell=len(f["left"])
        for i in range(len(forms)):
            e,w=actual(ends[i]+D*3**powers[i]*t,ell)
            ends[i]=e;words[i]+=w;powers[i]+=w.count("1")
        d+=mod*t;mod*=m;length+=ell
        need(len(set(ends[:j+1]))==len(set(powers[:j+1]))==1,"linear merging")
    t=(residue-d)*pow(mod,-1,odd)%odd if odd>1 else 0
    for i in range(len(forms)):ends[i]+=D*3**powers[i]*t
    d+=mod*t;mod*=odd;ep=[odd*D*3**powers[0],ends[0]]
    for i,(A,b) in enumerate(forms):
        need(polynomial_linear(A*mod,A*d+b,words[i])==ep,"linear endpoint")
        need(len(words[i])==length+parts[i][1],"linear clock difference")
    need((d-residue)%modulus==0 and mod%modulus==0,"linear class")
    return dict(**base,status="MERGE",modulus=mod,residue=d,length=length,
                words=words,endpoint=ep,six_free_part=D)


def polynomial_linear(a,b,word):
    # symbolic() already supports arbitrary positive affine slopes.
    return symbolic(a,b,word)


def linear_specs():
    out=[]
    for D in (1,5,7,35):
        for k in range(1,17):
            forms=[(D*2**((i+k)%5)*3**((2*i+k)%5),((i*i+7*k)%67)-33)
                   for i in range(1,2+k%6)]
            out.append((forms,3**(k%3)*2**(k%5),-k))
    for A in range(1,33):
        for B in (1,2,3,5,7):out.append(([(A,-3),(B,5)],12,7))
    out.extend([([(1,0),(2,0)],1,0), ([(1,0),(5,0)],1,0),
                ([(5,0),(30,1),(180,-7)],72,3)])
    return out


def chart_step(a,b,y,orientation):
    """Credited complete grammar from PR128/AUA-002, not new here."""
    if b%2==0:
        if y%2:return a,(3*b+1-3**a)//2,(3*y+1)//2,orientation
        return a,b//2,y//2,orientation
    if y%2==0:return a+1,(3*b+1)//2,y//2,orientation
    if a:return a-1,(b-3**(a-1))//2,(3*y+1)//2,orientation
    return 1,(1-3*b)//2,(y+b)//2,1-orientation


def classify(c0, used, horizon=12, budget=256):
    c=c0; orientation=0; words=["",""]
    for count in range(budget):
        tr=vl_transition(c)
        if tr is None:break
        merge,d,w,z=tr
        words[orientation]+=w; words[1-orientation]+=z
        if merge:
            return dict(kind="comparison",c=c0,mechanism="VL",baseline="MERGE",
                        status="MERGE",words=words,endpoint=d)
        c=d; orientation=1-orientation
    else:
        return dict(kind="comparison",c=c0,mechanism="BUDGET",baseline="BUDGET",
                    status="BUDGET",words=words,terminal=c)
    a,b,y,w,z=normalized_escape(c)
    for variant in range(3):
        f=affine(a,b,variant)
        if y>=f["residue"] and (y-f["residue"])%f["modulus"]==0:
            words[orientation]+=w+f["left"]; words[1-orientation]+=z+f["right"]
            e=path(c0,words[1])[-1]
            return dict(kind="comparison",c=c0,mechanism="EG",baseline="MERGE",
                        status="MERGE",words=words,endpoint=e)
    a,b,y=2,2,c
    for depth in range(horizon+1):
        used.add((a,b)); f=universal(a,b)
        if y>=f["residue"] and (y-f["residue"])%f["modulus"]==0:
            words[orientation]+=f["left"]; words[1-orientation]+=f["right"]
            e=path(c0,words[1])[-1]
            need(e==path(9*c0+2,words[0])[-1],"composed merger")
            return dict(kind="comparison",c=c0,mechanism="NEW",baseline="OUTSIDE",
                        status="MERGE",words=words,endpoint=e,depth=depth,
                        gate=[a,b],parameter=y)
        if depth==horizon:
            return dict(kind="comparison",c=c0,mechanism="OUTSIDE",baseline="OUTSIDE",
                        status="OUTSIDE",words=words,chart=[a,b,y,orientation])
        x=3**a*y+b
        words[orientation]+=str(x%2); words[1-orientation]+=str(y%2)
        a,b,y,orientation=chart_step(a,b,y,orientation)
    raise ValueError("unreachable selector state")


def original(j, extra=0):
    integer(j,1); integer(extra)
    f=synchronize([(2*i,(9**i-1)//4) for i in range(j+1)])
    K=2+f["length"]; r=2*j
    while 3**r<2**(r+K):r+=1
    r+=extra; exponent=r-2*j+1; q=3**(exponent+1)
    target=(3**exponent*pow(2,-r,3)-1)*pow(4,-1,q)%q
    c=f["residue"]+f["modulus"]*((target-f["residue"])*pow(f["modulus"],-1,q)%q)
    u=(4*c+1)//3**exponent; n=2**r*u-1
    mainword="1"*r+"01"+f["words"][j]; trajectory=path(n,mainword)
    ms=[]; ws=[]
    for k in range(j):
        m=(n-(4**(k+1)-1)//3)//2
        w="1"+"0"*(2*k)+"1"*(r-2*k-2)+"00"+f["words"][j-k-1]
        need(0<2*m<n and path(m,w)[-1]==trajectory[-1],"original companion")
        ms.append(m);ws.append(w)
    need(n%3==0 and min(trajectory[1:])>n,"original no-descent")
    return dict(kind="original",j=j,r=r,c=c,u=u,n=n,companions=ms,
                main_word=mainword,companion_words=ws,endpoint=trajectory[-1],
                minimum=min(trajectory[1:]),family=f)


def core_partners(a,b):
    A=3**a
    values={A+b,2*A+b}
    for z in (1,2):
        if (z-b)%A==0:values.add((z-b)//A)
    return sorted(x for x in values if x>0)


def core_catalogue():
    forms=[(a,b) for a in range(7) for b in range(-32,33)]
    targets=sorted(set(x for a,b in forms for x in core_partners(a,b)))
    for n in targets:
        x=n; w=""
        while x!=1:
            need(len(w)<10000,"core witness budget")
            w+=str(x%2);x=step(x)
        yield dict(kind="core",n=n,word=w)


def dumps(obj):return json.dumps(obj,sort_keys=True,separators=(",",":"))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full",required=True,type=Path)
    parser.add_argument("--output",type=Path)
    parser.add_argument("--check",type=Path)
    parser.add_argument("--limit",type=int,default=65536)
    args=parser.parse_args();need(1<=args.limit<=65536,"unsupported limit")
    counts=Counter();digest=hashlib.sha256();used=set();samples=[];families=[]
    # These grids are explicit finite tests; unbounded statements use the proof.
    for j in range(1,17):families.append(synchronize([(2*i,(9**i-1)//4) for i in range(j+1)]))
    for size in (2,3,4,8,16,32,64,128,256):
        for m,r in ((1,0),(8,3),(72,3),(30,-7)):
            families.append(synchronize([(0,i) for i in range(size)],m,r))
    for k in range(1,41):
        forms=[((k*i+3)%7,((i*i+3*k)%43)-21) for i in range(1,2+k%8)]
        families.append(synchronize(forms,3**(k%4)*2**(k%6),-k))
    families.append(synchronize([(0,0),(0,0)],15,2))
    with args.full.open("w",encoding="utf-8",newline="\n") as out:
        def emit(row):
            text=dumps(row)+"\n";out.write(text);digest.update(text.encode());counts[row["kind"]]+=1
        for a in range(13):
            for b in range(-128,129):used.add((a,b))
        for a,b in [(0,10**60+7),(1,10**60+9),(32,3**32+100),
                    (64,-10**60),(128,3**128),(32,3**32-2**32)]:used.add((a,b))
        rows=[]
        for c in range(1,args.limit+1):rows.append(classify(c,used))
        for a,b in sorted(used):emit(universal(a,b))
        for f in families:emit(f)
        for forms,m,r in linear_specs():
            row=linear_synchronize(forms,m,r);emit(row);counts["linear_"+row["status"]]+=1
        for j in range(1,17):
            for extra in (0,5):emit(original(j,extra))
        for row in core_catalogue():emit(row)
        for row in rows:
            emit(row);counts["comparison_"+row["mechanism"]]+=1
            if row["mechanism"]=="NEW" and len(samples)<12:samples.append(row["c"])
        result=dict(schema="ufs-v1",status="PROPOSED",complete_collatz_proof=False,
                    parent="f5e7ec9a23fa691d71a5a9f518cbff5529a5ea00",
                    parallel="edd48df6e9c678fa4a65b4ed8f41421dfc92518b",
                    limit=args.limit,horizon=12,counts=dict(sorted(counts.items())),
                    rows_sha256=digest.hexdigest(),additional_samples=samples)
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:args.output.write_text(text,encoding="utf-8")
    if args.check:need(args.check.read_text(encoding="utf-8")==text,"canonical mismatch")
    print(text,end="")


if __name__=="__main__":main()
