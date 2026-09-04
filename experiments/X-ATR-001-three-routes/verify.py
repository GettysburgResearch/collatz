#!/usr/bin/env python3
"""Separately implemented strict replay; never imports run.py.

The checker uses literal forward steps and a reverse-tree traversal, rather than
run.py's first-return/fan formulas. Both implementations have the same authoring
session: this is implementation separation, NOT independent mathematical review.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Rat
import hashlib
import json
from pathlib import Path

EXPECTED_SCOPE={"forward_limit_inclusive":12289,"fan_target_limit_inclusive":49153,
 "deep_h_max":32,"deep_k_max":24,"density_h_max":32,"tile_count":32,
 "tile_search_shortcut_cap":128,"parametric_h_max":32,"two_parameter_a_max":8,"two_parameter_h_max":16,
 "schur_targets":[10,13,19,22,28,37],"schur_depths":[0,2,4,8],
 "certificate_claim":"finite exact checks plus explicitly stated symbolic inequalities; not global coverage"}


def need(condition: bool, message: str) -> None:
    if not condition:raise ValueError(message)


def val3(x: int) -> int:
    need(x!=0,"zero valuation")
    x=abs(x);d=0
    while x%3==0:x//=3;d+=1
    return d


def hh(n: int) -> bool:return n>=4 and n%3==1


def nxt(n: int) -> int:return n//2 if n%2==0 else (3*n+1)//2


def rnk(n: int) -> int:
    z=2*n+1;u=z
    while u%3==0:u//=3
    return z*u


def qweight(n: int) -> Rat:
    z=2*n+1;h=val3(z);u=z//3**h;k=val3(2**(h+1)*u-1)
    return max(Rat(1),Rat(3**(h+k),4**h))


def walk(n: int) -> tuple[int,str]:
    need(hh(n),"walk source outside H")
    x=n;bits=""
    for _ in range(2*n.bit_length()+4):
        bits+=str(x%2);x=nxt(x)
        if x==1 or hh(x):return x,bits
    raise ValueError("first-return runtime violation")


def predecessors(y: int) -> list[int]:
    work=[2*y];found=set();iterations=0
    while work:
        x=work.pop();iterations+=1
        need(iterations<=4*(2*y+1).bit_length()+10,"reverse easy tree did not close")
        if x==1 or x%3==0:continue
        if hh(x):found.add(x);continue
        need(x%3==2,"unexpected reverse class")
        work.append(2*x)
        z=(2*x-1)//3
        if z>1:work.append(z)
    return sorted(found)


def trace(n: int,bits: str) -> int:
    for b in bits:
        need(b in "01" and n%2==int(b),"nonphysical parity word")
        n=nxt(n)
    return n


def aff(bits: str) -> tuple[int,int,int]:
    ones=[i for i,b in enumerate(bits) if b=="1"]
    q=len(ones)
    A=sum(2**i*3**(q-1-t) for t,i in enumerate(ones))
    return q,A,len(bits)


def canon(bits: str) -> int:
    q,A,j=aff(bits)
    return (-A*pow(3**q,-1,2**j))%2**j


def ratlist(x: Rat) -> list[int]:return [x.numerator,x.denominator]


def firstdrop(n: int) -> tuple[str,int] | None:
    x=n;bits=""
    for _ in range(128):
        bits+=str(x%2);x=nxt(x)
        if (x==1 or hh(x)) and rnk(x)<rnk(n):return bits,x
    return None


def tile_record(n: int,bits: str) -> dict:
    y=trace(n,bits);q,A,j=aff(bits)
    h0,h1=val3(2*n+1),val3(2*y+1)
    H=max(h0+1,h1+1-q)
    need(h0>=1 and h1>=1 and rnk(y)<rnk(n),"rank tile invalid")
    need(2*A+2**j>3**q,"missing positive z-coordinate offset")
    return {"source":n,"word":bits,"endpoint":y,"h_source":h0,"h_endpoint":h1,
       "modulus":2**j*3**H,"base_rank_ratio":[rnk(y),rnk(n)]}


def check(document: dict) -> None:
    need(set(document)=={"payload","sha256"},"report envelope")
    p=document["payload"]
    need(p["scope"]==EXPECTED_SCOPE,"scope mismatch / inflated theorem coverage")
    encoded=json.dumps(p,sort_keys=True,separators=(",",":")).encode()
    need(hashlib.sha256(encoded).hexdigest()==document["sha256"],"payload digest")
    need(Rat(1,20)+Rat(64,147)<Rat(1,2),"kernel rational majorant")
    need(Rat(27,605)<Rat(1,20),"bulk rational majorant")
    need(243<256 and Rat(2,3)+Rat(6561,131072)<Rat(3,4),"parametric inequality")
    stats=Counter(); largest=Rat(); safe=Rat()
    for y in range(4,49154,3):
        xs=predecessors(y)
        need(all(walk(x)[0]==y for x in xs),"inverse return mismatch")
        kv=sum((Rat(1,rnk(x)) for x in xs),Rat())*rnk(y)
        need(kv<=qweight(y)/2,"kernel inequality")
        stats["fan_targets"]+=1;stats["fan_edges"]+=len(xs)
        largest=max(largest,kv)
        if qweight(y)==1:
            stats["nonresonant_fan_targets"]+=1;safe=max(safe,kv)
        if kv>1:stats["pointwise_weight_expansion_targets"]+=1
    need(p["kernel_ratio_max"]==ratlist(largest),"kernel maximum")
    need(p["nonresonant_ratio_max"]==ratlist(safe),"safe maximum")
    deep=set()
    for h in range(1,33):
        for u in range(1,32,2):
            if u%3 and (3**h*u-1)//2>=4:deep.add((3**h*u-1)//2)
        for k in range(1,25):
            m=3**k
            u=pow(2**(h+1),-1,m)
            if u%2==0:u+=m
            if (3**h*u-1)//2<4:u+=2*m
            deep.add((3**h*u-1)//2)
    for y in sorted(deep):
        kv=sum((Rat(1,rnk(x)) for x in predecessors(y)),Rat())
        need(kv<=qweight(y)/rnk(y)/2,"deep kernel")
    stats["deep_arithmetic_targets"]=len(deep)

    er=et=dropmax=(0,0);unresolved=[];expected_tiles=[]
    fixed=unfixed=0
    for n in range(4,12290,3):
        y,bits0=walk(n)
        need(n in predecessors(y) if y!=1 else n==4,"forward/inverse coverage")
        need(len(bits0)<=rnk(n).bit_length()+1,"return clock")
        stats["forward_sources"]+=1
        if y==1 or qweight(y)==1:stats["one_return_absorption_or_halving"]+=1
        elif rnk(y)<rnk(n):stats["resonant_but_rank_decreasing"]+=1
        else:stats["one_return_rank_nondecrease"]+=1
        x=n;r=t=0
        while hh(x) and qweight(x)==1:
            x,bits=walk(x);r+=1;t+=len(bits)
            need(r<=rnk(n).bit_length(),"entrance return bound")
        need(t<=rnk(n).bit_length()*(rnk(n).bit_length()+1),"entrance physical clock")
        if r>er[0]:er=(r,n)
        if t>et[0]:et=(t,n)
        x=n;prod=Rat(1);u=(2*n+1)//3**val3(2*n+1)
        for r in range(1,33):
            x,_=walk(x)
            if x==1 or x<n:break
            prod*=qweight(x)
            need(Rat(2**r)<=u*prod,"no-descent source pressure")
            stats["no_descent_pressure_prefixes"]+=1
        found=firstdrop(n)
        if found is None:unresolved.append(n)
        else:
            bits,z=found
            if len(bits)>dropmax[0]:dropmax=(len(bits),n)
            if y!=1 and rnk(y)>=rnk(n) and len(expected_tiles)<32:
                expected_tiles.append(tile_record(n,bits))
        x=n;bits=""
        for j in range(1,33):
            bits+=str(x%2);x=nxt(x)
            if hh(x):
                q,A,_=aff(bits);Z=2*A+2**j;h=val3(Z)
                if h<q:
                    need(h==val3(2*x+1),"first fixed jet")
                    W=2**(h+1)*Z-3**h*2**j
                    if W and val3(W)<q:
                        k=val3(W)-h
                        actual=val3(2**(h+1)*((2*x+1)//3**h)-1)
                        need(k==actual,"second fixed jet");fixed+=1
                    else:unfixed+=1
                else:unfixed+=1
            if x==1:break
    stats["fixed_endpoint_jet_pairs"]=fixed;stats["unfrozen_endpoint_jet_pairs"]=unfixed
    need(p["statistics"]==dict(sorted(stats.items())),"statistics / exhaustive coverage")
    need(p["entry_max_returns_and_source"]==list(er),"entry maximum")
    need(p["entry_max_shortcut_steps_and_source"]==list(et),"entry clock maximum")
    need(p["rank_drop_pilot"]=={"max_steps_and_source":list(dropmax),
        "unresolved_at_cap":unresolved,"scope":"finite source interval only"},"rank-drop pilot")
    need(p["tiles"]==expected_tiles and len(p["tiles"])==32,"tile inventory or modulus")
    for t in p["tiles"]:
        n=t["source"];M=t["modulus"];bits=t["word"];y=t["endpoint"]
        for lift in (1,3,19):
            a=n+M*lift;b=trace(a,bits)
            need(val3(2*a+1)==t["h_source"] and val3(2*b+1)==t["h_endpoint"],"tile jets")
            need(rnk(b)*rnk(n)<=rnk(y)*rnk(a),"upward tile monotonicity")
    need(p["rank_spike"]=={"source":13,"endpoint":10,"ranks":[27,147]},"rank counterexample")
    need(walk(13)[0]==10 and rnk(13)==27 and rnk(10)==147,"rank counterexample replay")
    params=[]
    for h in range(2,33):
        bits="10010"+"10"*(2*h);j=len(bits);r=canon(bits);m=3**(h+1)
        s=(3**h-1)//2;n=r+2**j*((s-r)*pow(2**j,-1,m)%m)
        if n<=1:n+=2**j*m
        y=trace(n,bits);first,_=walk(n)
        need(val3(2*n+1)==h and val3(2*y+1)==1,"parametric jets")
        need(4*rnk(y)<3*rnk(n),"parametric rank decrease")
        need(Rat(rnk(first),rnk(n))>Rat(3**(h+1),16),"unbounded initial spike")
        params.append({"h":h,"source":n,"endpoint":y,"first_return":first,
          "final_rank_ratio":ratlist(Rat(rnk(y),rnk(n)))})
    need(p["parametric_samples"]==params,"parametric sample inventory")
    two_parameter=[]
    need(Rat(2,3)+Rat(27,512)<Rat(3,4) and 27<32,"two-parameter constants")
    for a in range(1,9):
        for h in range(2,17):
            bits="1"*a+"0"+"10"*(2*(h+a)+3)
            j=len(bits);r=canon(bits);m=3**(h+1)
            n=r+2**j*((((3**h-1)//2-r)*pow(2**j,-1,m))%m)
            if n<=1:n+=2**j*m
            y=trace(n,bits);first,_=walk(n)
            t=n+1;dyadic=0
            while t%2==0:t//=2;dyadic+=1
            need(dyadic==a and val3(2*n+1)==h,"two-parameter source jets")
            need(val3(2*y+1)==1 and 4*rnk(y)<3*rnk(n),"two-parameter decrease")
            need(Rat(rnk(first),rnk(n))>Rat(3**(h+a),4**(a+1)),"two-parameter spike")
            if a>=2:need(first>n,"genuine initial numerical growth")
            two_parameter.append([a,h,n,y,first])
    family_digest=hashlib.sha256(json.dumps(two_parameter,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    need(p["two_parameter_family"]=={"cases":len(two_parameter),"sha256":family_digest},"two-parameter inventory")
    rows=[];low=Rat()
    for h in range(1,33):
        k=1
        while 3**(h+k)<=4**h:k+=1
        rows.append([h,k]);low+=Rat(1,3**(h+k))
    need(p["density"]=={"cutoffs":rows,"lower":ratlist(low),
        "upper":ratlist(low+Rat(1,3**33))},"density enclosure")
    failures=[]
    for n,a in ((31,1),(121,4)):
        x=n;prod=Rat(1);tr=[n]
        for r in range(1,129):
            x,_=walk(x);tr.append(x);need(x!=1,"countertest clock")
            prod*=qweight(x);norm=prod/Rat(3,2)**r
            if norm>rnk(n)**a:
                failures.append({"source":n,"power":a,"returns":r,"trace":tr,
                   "normalized_charge":ratlist(norm),"rank_power":rnk(n)**a});break
        else:raise ValueError("missing budget counterexample")
    need(p["budget_countertests"]==failures,"budget countertests")
    schur=[]
    for target in EXPECTED_SCOPE["schur_targets"]:
        need(qweight(target)>1,"Schur target is not resonant")
        direct=predecessors(target)
        safe_row=sum((Rat(1,rnk(x)) for x in direct if qweight(x)==1),Rat())
        for L in EXPECTED_SCOPE["schur_depths"]:
            resolved={x for x in direct if qweight(x)>1}
            frontier={x for x in direct if qweight(x)==1}
            for depth in range(L):
                following=set()
                for x in frontier:
                    for z in predecessors(x):
                        if qweight(z)>1:
                            need(z not in resolved,"duplicate return source");resolved.add(z)
                        else:following.add(z)
                frontier=following
            lower=sum((Rat(1,rnk(x)) for x in resolved),Rat())
            schur.append({"target":target,"safe_interiors":L,
                "resolved_resonant_sources":len(resolved),
                "lower_mass":ratlist(lower),"upper_mass":ratlist(lower+safe_row/2**L)})
    need(p["schur_intervals"]==schur,"Schur tail enclosures")
    need(set(p)=={"scope","statistics","kernel_ratio_max","nonresonant_ratio_max",
      "entry_max_returns_and_source","entry_max_shortcut_steps_and_source","rank_drop_pilot",
      "rank_spike","density","tiles","parametric_samples","budget_countertests","schur_intervals","two_parameter_family"},"payload keys")


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("certificate",type=Path)
    ns=ap.parse_args();doc=json.loads(ns.certificate.read_text());check(doc)
    print("PASS: independent implementation replay; "+doc["sha256"])

if __name__=="__main__":main()
