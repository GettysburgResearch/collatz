#!/usr/bin/env python3
"""Separate certificate replay; imports no generator or repository module.
Uses whole-word affine numerators, a distinct modular gap pullback, signed
integer templates, and direct-state comparison to reconstruct selector choices.
Same-author implementation diversity is not independent mathematical review.
"""
from __future__ import annotations
import argparse
from collections import Counter
from copy import deepcopy
from functools import lru_cache
import hashlib
import json
from pathlib import Path


def require(ok, message="invalid certificate"):
    if not ok:raise ValueError(message)


def exact(n, lower=None):
    require(type(n) is int,"integer alias")
    if lower is not None:require(n>=lower,"integer range")
    return n


def typed(obj):
    if isinstance(obj,dict):
        require(all(type(k) is str for k in obj),"nontext key")
        for v in obj.values():typed(v)
    elif isinstance(obj,list):
        for v in obj:typed(v)
    else:require(type(obj) in (int,str),"boolean/float/null alias")


def unique(pairs):
    d={}
    for k,v in pairs:
        require(k not in d,"duplicate JSON key");d[k]=v
    return d


def load(line):return json.loads(line,object_pairs_hook=unique)

def T(n):return (3*n+1)//2 if n%2 else n//2

def valuation(n):
    exact(n,1);k=0
    while n%2==0:n//=2;k+=1
    return k


def walk(n,w):
    exact(n,1);require(type(w) is str and len(w)<=100000,"word range")
    smallest=None
    for bit in w:
        require(bit in "01" and str(n%2)==bit,"physical parity")
        n=T(n);smallest=n if smallest is None else min(smallest,n)
    return n,smallest


def polynomial(a,b,w):
    exact(a,1);exact(b,1)
    require(type(w) is str and set(w)<=set("01") and len(w)<=100000,"word")
    p=1;A=0;D=1
    for bit in w:
        if bit=="1":p*=3;A=3*A+D
        D*=2
    require(a%D==0 and (p*b+A)%D==0,"whole source cylinder")
    return [p*a//D,(p*b+A)//D]


@lru_cache(None)
def gap(g,v=0):
    exact(g,1);require(v in (0,1,2))
    reductions=[]
    while g>1:
        if g%2==0:reductions.append((1,0,"0","0"));g//=2
        elif v==2:
            s=valuation(3*g-1);ell=s+1
            reductions.append((ell,1,"1"+"0"*s,"0"*s+"1"))
            g=((3*g-1)//2**s+1)//2
        elif g%4==1:
            reductions.append((2,1,"10","01"));g=(3*g+1)//4
        else:
            reductions.append((2,2,"01","10"));g=(3*g-1)//4
    M,B,w,z=(8,4,"001","100") if v==0 else (32,5,"10001","01100")
    for ell,offset,f,h in reversed(reductions):
        N=M*2**ell
        B=2*B if offset==0 else (2**ell*B-offset)*pow(3,-1,N)%N
        M=N;w=f+w;z=h+z
    return M,B,w,z


@lru_cache(None)
def restricted(a,b,v=0):
    require(a>=1 and 3**a-b>2**a,"restricted guard")
    x=b-3**a;word="";evens=0
    while evens<a:
        require(len(word)<100000,"signed budget")
        p=x%2;word+=str(p);evens+=1-p;x=T(x)
    require(x<-1,"signed endpoint")
    L=len(word);M,B,w,z=gap(-x-1,v)
    u=(B-x)*pow(3**L,-1,M)%M
    if u==0:u=M
    N=2**L*M;d=2**L*u-1
    while 3**a*d+b<=0:d+=N
    return N,d,word+w,"1"*L+z


@lru_cache(None)
def universal(a,b):
    exact(a,0);exact(b)
    if a==0:
        if b==0:return 1,1,"",""
        M,B,w,z=gap(abs(b))
        return (M,B,z,w) if b>0 else (M,B-b,w,z)
    if 3**a-b>2**a:return restricted(a,b)
    s=0
    while 2**s<=2*b:s+=1
    x=b;v=""
    for _ in range(s):v+=str(x%2);x=T(x)
    A=a+v.count("1")
    M,B,w,z=restricted(A,x)
    return 2**s*M,2**s*B,v+w,"0"*s+z


def check_gate(r):
    require(set(r)=={"kind","a","b","modulus","residue","left","right","endpoint"},"gate fields")
    M,B,w,z=universal(r["a"],r["b"])
    require((r["modulus"],r["residue"],r["left"],r["right"])==(M,B,w,z),"gate construction")
    require(M==2**len(w) and len(w)==len(z),"gate clock")
    ep=polynomial(3**r["a"]*M,3**r["a"]*B+r["b"],w)
    require(ep==polynomial(M,B,z)==r["endpoint"],"gate endpoint")


def check_family(r):
    require(set(r)=={"kind","forms","input_modulus","input_residue","modulus","residue","length","words","endpoint"},"family fields")
    forms=r["forms"];M=exact(r["modulus"],1);B=exact(r["residue"],1)
    m=exact(r["input_modulus"],1);r0=exact(r["input_residue"]);L=exact(r["length"],0)
    require(len(forms)>0 and len(forms)==len(r["words"]),"family dimensions")
    require(M==2**L*(m//2**valuation(m)),"family modulus")
    require(M%m==0 and (B-r0)%m==0,"prescribed arithmetic class")
    for form,w in zip(forms,r["words"]):
        require(type(form) is list and len(form)==2,"form")
        a,b=form;exact(a,0);exact(b)
        require(len(w)==L,"family clocks")
        require(polynomial(3**a*M,3**a*B+b,w)==r["endpoint"],"family endpoint")


def check_linear(r):
    forms=r["forms"];require(type(forms) is list and len(forms)>0,"linear dimension")
    cores=[];twos=[]
    for form in forms:
        require(type(form) is list and len(form)==2,"linear form")
        A,b=form;exact(A,1);exact(b);twos.append(valuation(A));d=A
        for prime in (2,3):
            while d%prime==0:d//=prime
        cores.append(d)
    fields={"kind","forms","input_modulus","input_residue","status"}
    exact(r["input_modulus"],1);exact(r["input_residue"])
    if len(set(cores))>1:
        fields.add("six_free_parts")
        require(r["status"]=="IMPOSSIBLE_UNIFORM" and r["six_free_parts"]==cores,"slope obstruction")
    else:
        fields|={"modulus","residue","length","words","endpoint","six_free_part"}
        require(r["status"]=="MERGE" and r["six_free_part"]==cores[0],"linear success")
        M=exact(r["modulus"],1);B=exact(r["residue"],1);L=exact(r["length"],0)
        m=r["input_modulus"]
        require(M==2**L*(m//2**valuation(m)) and M%m==0 and (B-r["input_residue"])%m==0,"linear modulus")
        require(len(r["words"])==len(forms),"linear words")
        for (A,b),s,w in zip(forms,twos,r["words"]):
            require(len(w)==L+s,"rigid clock offset")
            require(polynomial(A*M,A*B+b,w)==r["endpoint"],"linear polynomial merger")
    require(set(r)==fields,"linear fields")


def linear_specs():
    out=[]
    for D in (1,5,7,35):
        for k in range(1,17):
            forms=[[D*2**((i+k)%5)*3**((2*i+k)%5),((i*i+7*k)%67)-33]
                   for i in range(1,2+k%6)]
            out.append([forms,3**(k%3)*2**(k%5),-k])
    for A in range(1,33):
        for B in (1,2,3,5,7):out.append([[[A,-3],[B,5]],12,7])
    out.extend([[[[1,0],[2,0]],1,0],[[[1,0],[5,0]],1,0],[[[5,0],[30,1],[180,-7]],72,3]])
    return out


def check_original(r):
    require(set(r)=={"kind","j","r","c","u","n","companions","main_word","companion_words","endpoint","minimum","family"},"original fields")
    j=exact(r["j"],1);rr=exact(r["r"],2*j);n=exact(r["n"],1);u=exact(r["u"],1);c=exact(r["c"],1)
    f=r["family"];check_family(f)
    require(f["forms"]==[[2*i,(9**i-1)//4] for i in range(j+1)],"ladder forms")
    require(f["input_modulus"]==1 and f["input_residue"]==0,"ladder initial class")
    require((c-f["residue"])%f["modulus"]==0 and c>=f["residue"],"ladder gate")
    require(4*c+1==3**(rr-2*j+1)*u and u%2==1 and n==2**rr*u-1 and n%3==0,"CRT source")
    require(3**rr>=2**(rr+2+f["length"]),"uniform no-descent guard")
    word="1"*rr+"01"+f["words"][-1]
    require(r["main_word"]==word,"main word")
    ep,minimum=walk(n,word)
    require(ep==r["endpoint"] and minimum==r["minimum"] and minimum>n,"no-descent replay")
    require(len(r["companions"])==len(r["companion_words"])==j,"companion count")
    for k,(m,w) in enumerate(zip(r["companions"],r["companion_words"])):
        require(2*m==n-(4**(k+1)-1)//3 and 0<2*m<n,"original source order")
        expected="1"+"0"*(2*k)+"1"*(rr-2*k-2)+"00"+f["words"][j-k-1]
        require(w==expected and len(w)+1==len(word),"companion clocks")
        require(walk(m,w)[0]==ep,"companion merger")


def old_return(c):
    # Determine the same entrance, but obtain endpoint and tail orientation
    # from raw positive trajectories rather than the closed return formula.
    p=valuation(3*c-2);q=valuation(3*c-1)
    if p>=3 and p%2:
        k=(p-3)//2;w="00"+"01"*k+"00";z="01"+"10"*k+"11"
    elif q>=4 and q%2==0:
        k=(q-4)//2;w="100"+"01"*k+"00";z="110"+"10"*k+"11"
    else:return None
    x=walk(9*c+2,w)[0];y=walk(c,z)[0]
    require(y==3*x+2,"VL bridge")
    s=valuation(x+1)
    for _ in range(s+2):
        w+=str(x%2);z+=str(y%2);x=T(x);y=T(y)
    if x==y:return True,x,w,z
    require(y==9*x+2,"VL return")
    return False,x,w,z


def expected_comparison(c0,used,horizon):
    c=c0;orientation=0;words=["",""]
    for _ in range(256):
        tr=old_return(c)
        if tr is None:break
        good,x,w,z=tr;words[orientation]+=w;words[1-orientation]+=z
        if good:return "VL",words,None
        c=x;orientation=1-orientation
    else:return "BUDGET",words,c
    # Normalization by direct positive steps, retaining the specified exponents.
    s=valuation(c)//2;a=s+2;b=2;w="01"*s;z="00"*s
    x=walk(9*c+2,w)[0];y=walk(c,z)[0]
    if y%2==0:
        w+="00";z+="01";x=T(T(x));y=T(T(y));a-=1;b=(1-3**a)//2
    require(x==3**a*y+b,"normalized pair")
    for v in range(3):
        M,R,f,g=restricted(a,b,v)
        if y>=R and (y-R)%M==0:
            words[orientation]+=w+f;words[1-orientation]+=z+g
            return "EG",words,None
    x,y=9*c+2,c;a=2;b=2
    for depth in range(horizon+1):
        used.add((a,b));M,R,f,g=universal(a,b)
        if y>=R and (y-R)%M==0:
            words[orientation]+=f;words[1-orientation]+=g
            return "NEW",words,(depth,a,b,y)
        if depth==horizon:return "OUTSIDE",words,(a,b,y,orientation)
        px,py=x%2,y%2
        words[orientation]+=str(px);words[1-orientation]+=str(py)
        # Infer the next exponent from the actual two parities. Obtain the
        # intercept by subtraction, not the source grammar's case formula.
        delta=a+px-py;X,Y=T(x),T(y)
        if delta<0:
            x,y=Y,X;a=-delta;orientation=1-orientation
        else:x,y=X,Y;a=delta
        b=x-3**a*y
    raise ValueError("unreachable")


def check_comparison(r,used,horizon):
    c=exact(r["c"],1);tag,words,extra=expected_comparison(c,used,horizon)
    require(r["mechanism"]==tag and r["words"]==words,"selector reconstruction")
    require(r["baseline"]==("MERGE" if tag in ("VL","EG") else "BUDGET" if tag=="BUDGET" else "OUTSIDE"),"baseline")
    fields={"kind","c","mechanism","baseline","status","words"}
    if tag in ("VL","EG","NEW"):
        fields.add("endpoint");require(r["status"]=="MERGE","success tag")
        require(walk(9*c+2,words[0])[0]==walk(c,words[1])[0]==r["endpoint"],"merger replay")
        if tag=="NEW":
            fields|={"depth","gate","parameter"};depth,a,b,y=extra
            require((r["depth"],r["gate"],r["parameter"])==(depth,[a,b],y),"new gate choice")
    elif tag=="OUTSIDE":
        fields.add("chart");require(r["status"]=="OUTSIDE" and r["chart"]==list(extra),"outside frontier")
        a,b,y,o=extra;states=[walk(9*c+2,words[0])[0],walk(c,words[1])[0]]
        require(states[o]==3**a*y+b and states[1-o]==y,"frontier orientation")
    else:
        fields.add("terminal");require(r["status"]=="BUDGET" and r["terminal"]==extra,"budget")
    require(set(r)==fields,"comparison fields")


def check_row(r,used,horizon=12):
    typed(r);require(type(r) is dict and "kind" in r,"row")
    if r["kind"]=="gate":check_gate(r)
    elif r["kind"]=="family":check_family(r)
    elif r["kind"]=="original":check_original(r)
    elif r["kind"]=="linear":check_linear(r)
    elif r["kind"]=="core":
        require(set(r)=={"kind","n","word"},"core fields")
        require(walk(r["n"],r["word"])[0]==1,"core endpoint")
        x=r["n"]
        for bit in r["word"]:
            require(x!=1,"core first arrival");x=T(x)
    elif r["kind"]=="comparison":check_comparison(r,used,horizon)
    else:raise ValueError("unknown kind")


def family_specs():
    out=[]
    for j in range(1,17):out.append(([[2*i,(9**i-1)//4] for i in range(j+1)],1,0))
    for size in (2,3,4,8,16,32,64,128,256):
        for m,r in ((1,0),(8,3),(72,3),(30,-7)):out.append(([[0,i] for i in range(size)],m,r))
    for k in range(1,41):
        out.append(([[(k*i+3)%7,((i*i+3*k)%43)-21] for i in range(1,2+k%8)],3**(k%4)*2**(k%6),-k))
    out.append(([[0,0],[0,0]],15,2));return out


def encoded(x):return json.dumps(x,sort_keys=True,separators=(",",":"))


def self_test(samples):
    mutations=[]
    for kind,key,value in [
        ("gate","residue",0),("gate","modulus",3),("gate","a",-1),
        ("gate","left",""),("gate","endpoint",[0,0]),
        ("family","input_modulus",3),("family","length",-1),
        ("family","modulus",3),("family","endpoint",[1,1]),
        ("original","n",1),("original","minimum",0),("original","u",2),
        ("original","r",0),("original","endpoint",1),
        ("core","word",""),("comparison","endpoint",0),
        ("outside","chart",[0,0,1,0]),("new","depth",-1),
        ("linear","six_free_part",0),("linear","length",-1),
        ("impossible","six_free_parts",[1,1])]:
        row=deepcopy(samples[kind]);row[key]=value;mutations.append(row)
    for kind,key in [("gate","a"),("family","length"),("original","j"),("comparison","c")]:
        for alias in (True,1.0):
            row=deepcopy(samples[kind]);row[key]=alias;mutations.append(row)
    for row in mutations:
        try:check_row(row,set())
        except (ValueError,KeyError,TypeError,ZeroDivisionError):pass
        else:raise ValueError("accepted mutation")
    for text in ('{"x":1,"x":2}', '{"kind":"gate","a":NaN}', '{"kind":"gate","a":null}'):
        try:typed(load(text))
        except ValueError:pass
        else:raise ValueError("accepted JSON control")
    # The phase-mismatch countercontrol must remain unresolved synchronously.
    x,y=1,2
    for _ in range(100):require(x!=y,"phase control");x,y=T(x),T(y)
    return len(mutations)+3


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("full",type=Path);p.add_argument("--summary",required=True,type=Path)
    p.add_argument("--self-test",action="store_true")
    args=p.parse_args();summary=load(args.summary.read_text())
    require(summary["schema"]=="ufs-v1" and summary["complete_collatz_proof"] is False,"summary scope")
    require(set(summary)=={"schema","status","complete_collatz_proof","parent","parallel","limit","horizon","counts","rows_sha256","additional_samples"},"summary fields")
    require(summary["status"]=="PROPOSED" and summary["parent"]=="f5e7ec9a23fa691d71a5a9f518cbff5529a5ea00" and summary["parallel"]=="edd48df6e9c678fa4a65b4ed8f41421dfc92518b","summary provenance")
    require(1<=exact(summary["limit"],1)<=65536 and exact(summary["horizon"],0)==12,"summary range")
    require(type(summary["counts"]) is dict and all(type(k) is str and type(v) is int and v>=0 for k,v in summary["counts"].items()),"typed counts")
    require(type(summary["additional_samples"]) is list and all(type(v) is int and v>=1 for v in summary["additional_samples"]),"typed samples")
    require(type(summary["rows_sha256"]) is str and len(summary["rows_sha256"])==64,"typed digest")
    counts=Counter();digest=hashlib.sha256();used=set();keys=set();cs=[];orig=[];families=[];linears=[];cores=set();samples={};new_samples=[]
    with args.full.open("rb") as f:
        for line in f:
            digest.update(line);r=load(line);check_row(r,used,summary["horizon"])
            kind=r["kind"];counts[kind]+=1
            if kind=="gate":
                key=(r["a"],r["b"]);require(key not in keys,"duplicate gate");keys.add(key)
            if kind=="family":families.append([r["forms"],r["input_modulus"],r["input_residue"]])
            if kind=="linear":
                linears.append([r["forms"],r["input_modulus"],r["input_residue"]])
                counts["linear_"+r["status"]]+=1
                if r["status"]=="IMPOSSIBLE_UNIFORM":samples.setdefault("impossible",r)
            if kind=="original":orig.append((r["j"],r["r"]))
            if kind=="core":require(r["n"] not in cores,"duplicate core");cores.add(r["n"])
            if kind=="comparison":
                cs.append(r["c"]);counts["comparison_"+r["mechanism"]]+=1
                if r["mechanism"]=="NEW" and len(new_samples)<12:new_samples.append(r["c"])
                if r["mechanism"]=="NEW":samples.setdefault("new",r)
                if r["mechanism"]=="OUTSIDE":samples.setdefault("outside",r)
            if kind not in samples:
                if kind=="linear" and r["status"]!="MERGE":continue
                if kind=="gate" and r["a"]==0 and r["b"]==0:continue
                if kind=="core" and r["n"]==1:continue
                if kind=="comparison" and r["status"]!="MERGE":continue
                samples[kind]=r
    require(cs==list(range(1,summary["limit"]+1)),"complete comparison range")
    base={(a,b) for a in range(13) for b in range(-128,129)}
    base|={(0,10**60+7),(1,10**60+9),(32,3**32+100),(64,-10**60),(128,3**128),(32,3**32-2**32)}
    require(keys==base|used,"gate inventory")
    require(encoded(families)==encoded(family_specs()),"family input inventory")
    require(encoded(linears)==encoded(linear_specs()),"linear input inventory")
    require([j for j,rr in orig]==[j for j in range(1,17) for _ in range(2)],"original inventory")
    for i in range(0,len(orig),2):require(orig[i+1][1]==orig[i][1]+5,"original second height")
    targets=set()
    for a in range(7):
        A=3**a
        for b in range(-32,33):
            for z in (1,2):
                if A*z+b>0:targets.add(A*z+b)
                if (z-b)%A==0 and z-b>0:targets.add((z-b)//A)
    require(cores==targets,"core catalogue completeness")
    require(dict(sorted(counts.items()))==summary["counts"],"count mismatch")
    require(new_samples==summary["additional_samples"],"sample mismatch")
    require(digest.hexdigest()==summary["rows_sha256"],"corpus digest")
    controls=self_test(samples) if args.self_test else 0
    print(encoded(dict(status="PASS",rows=sum(counts[k] for k in ("gate","family","linear","original","core","comparison")),
                       counts=dict(sorted(counts.items())),controls_rejected=controls,rows_sha256=digest.hexdigest())))


if __name__=="__main__":main()
