#!/usr/bin/env python3
"""Separate forward-state/numerator verifier; imports no generator or repo module.
This verifies the supplied finite corpus, not mathematical peer-review status.
"""
from __future__ import annotations
import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path


def check(ok,msg):
    if not ok:raise ValueError(msg)


def nat(n,minimum=0):
    check(type(n) is int and n>=minimum,"integer type/range")
    return n


def parse(text):
    def pairs(items):
        out={}
        for k,v in items:
            check(k not in out,"duplicate JSON key")
            out[k]=v
        return out
    def bad(_):raise ValueError("noninteger JSON number")
    return json.loads(text,object_pairs_hook=pairs,parse_float=bad,parse_constant=bad)


def val(n):
    nat(n,1); k=0
    while n%2==0:n//=2;k+=1
    return k


def forward(n,word):
    nat(n,1); check(type(word) is str,"word type")
    low=None
    for p in word:
        check(p in "01" and (n%2)==int(p),"physical parity")
        n=(3*n+1)//2 if n%2 else n//2
        low=n if low is None else min(low,n)
    return n,low


def one(n):
    return (3*n+1)//2 if n%2 else n//2


def cylinder(M,R,word):
    nat(M,1);nat(R,1)
    check(M%2**len(word)==0,"uniform-word modulus")
    endpoint,_=forward(R,word)
    A=0; q=0
    for i,p in enumerate(word):
        if p=="1":A=3*A+2**i;q+=1
    check(3**q*R+A==2**len(word)*endpoint,"affine numerator")
    return [3**q*M//2**len(word),endpoint]


def gap_row(r):
    g=nat(r["g"],1); variant=nat(r["variant"])
    check(variant in (0,1,2),"gap variant")
    M,R=nat(r["modulus"],1),nat(r["residue"],1)
    p,q=r["left"],r["right"]
    check(type(p) is str and type(q) is str and len(p)==len(q),"gap clocks")
    check(M==2**len(p) and R<M,"canonical dyadic class")
    check(p.count("1")==q.count("1"),"equal odd count")
    check(all(type(x) is int for x in r["endpoint"]),"typed endpoint")
    check(cylinder(M,R,p)==cylinder(M,R+g,q)==r["endpoint"],"gap merger")
    if variant<2:check(M<=(8 if variant==0 else 32)*g**7,"polynomial modulus bound")
    if variant==2:check((R+g)%2==0,"upper-even guarantee")


def affine_row(r):
    a=nat(r["a"],1);check(type(r["b"]) is int,"intercept type")
    b=r["b"];variant=nat(r["variant"])
    check(variant in (0,1,2),"affine variant")
    c=3**a-b;check(c>2**a,"shadow hypothesis")
    w=r["negative"];check(type(w) is str and w,"negative word")
    z=-c; evens=0
    for p in w:
        check(evens<a,"continued past a-th even")
        check(p in "01" and z%2==int(p),"negative physical path")
        if z%2:z=(3*z+1)//2
        else:z//=2;evens+=1
        check(z<-1,"negative fixed-point exclusion")
    check(evens==a and z==-nat(r["negative_endpoint"],2),"balanced terminal")
    check(nat(r["gap"],1)==-z-1,"balanced gap")
    p,q=r["left"],r["right"]
    check(type(p) is str and type(q) is str and p.startswith(w)
          and q.startswith("1"*len(w)) and len(p)==len(q),"shadow prefix/clocks")
    M,R=nat(r["modulus"],1),nat(r["residue"],1)
    check(M==2**len(p),"affine full modulus")
    check((R+1)%2**len(w)==0,"odd-spine divisibility")
    check(all(type(x) is int for x in r["endpoint"]),"typed affine endpoint")
    check(cylinder(3**a*M,3**a*R+b,p)==cylinder(M,R,q)==r["endpoint"],
          "affine whole-cylinder merger")


def baseline(c0):
    c=c0; words=["",""]; orientation=0
    for _ in range(256):
        alpha,beta=val(3*c-2),val(3*c-1)
        if alpha>=3 and alpha%2:
            length=alpha+1
        elif beta>=4 and beta%2==0:
            length=beta+1
        else:return "OUTSIDE",c,words
        x,y=9*c+2,c; w,z="",""
        for _ in range(length):
            w+=str(x%2);z+=str(y%2);x,y=one(x),one(y)
        check(y==3*x+2,"independent parent bridge")
        while x%2:
            check(y%2==1,"paired odd phase")
            w+="1";z+="1";x,y=one(x),one(y)
        for _ in range(2):
            w+=str(x%2);z+=str(y%2);x,y=one(x),one(y)
        words[orientation]+=w;words[1-orientation]+=z
        if x==y:return "MERGE",x,words
        check(y==9*x+2,"independent parent return")
        c=x;orientation=1-orientation
    return "BUDGET",c,words


def normalization(c):
    x,y=9*c+2,c; a=2; p,q="",""
    while y%4==0:
        for _ in range(2):
            p+=str(x%2);q+=str(y%2);x,y=one(x),one(y)
        a+=1
    if y%2==0:
        for _ in range(2):
            p+=str(x%2);q+=str(y%2);x,y=one(x),one(y)
        a-=1
    b=x-3**a*y
    check(3**a-b>2**a,"normalized type not covered by hypothesis")
    return a,b,y,p,q


def comparison_row(r,gates):
    c=nat(r["c"],1)
    status,terminal,words=baseline(c)
    check(r["baseline"]==status,"parent outcome")
    if status=="MERGE":
        check(r["status"]=="MERGE" and r["mechanism"]=="parent"
              and [r["left"],r["right"]]==words and nat(r["endpoint"],1)==terminal,
              "parent certificate preservation")
        return
    if status=="BUDGET":
        check(r["status"]=="BUDGET" and r["terminal"]==terminal
              and [r["left"],r["right"]]==words,"budget preservation")
        return
    check(nat(r["terminal"],1)==terminal,"outside terminal")
    a,b,d,p,q=normalization(terminal); hit=None
    for variant in range(3):
        key=(a,b,variant);check(key in gates,"missing gate inventory")
        cert=gates[key]
        if d>=cert["residue"] and (d-cert["residue"])%cert["modulus"]==0:
            hit=key;break
    if hit is None:
        check(r["status"]=="OUTSIDE" and [r["left"],r["right"]]==words,
              "outside row dropped or misclassified")
        return
    check(r["status"]=="MERGE" and r["mechanism"]=="escape"
          and r["gate"]==list(hit) and all(type(i) is int for i in r["gate"]),
          "extension gate metadata")
    X=forward(9*c+2,words[0])[0];Y=forward(c,words[1])[0]
    orientation=0 if X==9*terminal+2 and Y==terminal else 1
    check(orientation==0 or (Y==9*terminal+2 and X==terminal),"return orientation")
    cert=gates[hit];words[orientation]+=p+cert["left"];words[1-orientation]+=q+cert["right"]
    check([r["left"],r["right"]]==words,"composed words")
    check(len(words[0])==len(words[1]),"comparison clocks")
    check(forward(9*c+2,words[0])[0]==forward(c,words[1])[0]==nat(r["endpoint"],1),
          "whole original comparison replay")


def original_row(row,gates):
    r=nat(row["r"],2);u=nat(row["u"],1);c=nat(row["c"],1)
    n,m=nat(row["n"],1),nat(row["m"],1)
    j=nat(row["index"],1);variant=nat(row["variant"])
    check(u%2==1 and n==2**r*u-1 and n%3==0 and 0<m<n,"immutable original source")
    if row["family"]=="escape":
        key=(j+2,2,variant);cert=gates[key]
        M,R=4**j*cert["modulus"],4**j*cert["residue"]
        p="01"*j+cert["left"];q="00"*j+cert["right"]
        check(m==(n-1)//2,"half companion")
        lower="1"*(r-1)+"00";exponent=r-1;min_r=2
    elif row["family"]=="rung":
        check(r>=2*j,"rung existence")
        key=(2*j,(9**j-1)//4,variant);cert=gates[key]
        M,R=cert["modulus"],cert["residue"]
        p,q=cert["left"],cert["right"]
        check(m==(n-(4**j-1)//3)//2,"ladder companion")
        lower="1"+"0"*(2*j-2)+"1"*(r-2*j)+"00"
        exponent=r-2*j+1;min_r=2*j
    else:raise ValueError("unknown original family")
    K=nat(row["tail_steps"],1)
    check(K==2+len(p) and 3**r>=2**(r+K),"uniform no-descent bound")
    while 3**min_r<2**(min_r+K):min_r+=1
    check(r in (min_r,min_r+7),"declared original corpus parameter")
    check(4*c+1==3**exponent*u and (c-R)%M==0 and c>=R,"CRT/cylinder entrance")
    check(c<R+M*3**(exponent+1),"canonical positive CRT representative")
    check(row["left"]=="1"*r+"01"+p and row["right"]==lower+q,"original words")
    X,minimum=forward(n,row["left"]);Y,_=forward(m,row["right"])
    check(X==Y==nat(row["endpoint"],1) and len(row["left"])==len(row["right"])+1,
          "original meeting/clocks")
    check(row["no_forward_descent"] is True and nat(row["minimum"],1)==minimum>n,
          "all-state no-forward-descent")
    if row["family"]=="rung" and j%3==2:
        third=(n-(4**j-1)//3-1)//3
        check(0<third<n//3 and forward(third,"1"+row["right"])[0]==X,"one-third certificate")


def window_count():
    info={}
    for n in range(1,257):
        x=n;t=0;odds=[]
        while len(odds)<2:
            if x%2:odds.append(t)
            x=one(x);t+=1
        info[n]=odds
    count=0
    for x in range(1,129):
        for y in range(x+1,257):
            ell=min(info[x][1],info[y][1])
            if ell<2 or ell<max(info[x][0],info[y][0])+1:continue
            X,Y=x,y
            for _ in range(ell):X,Y=one(X),one(Y)
            check(max(X,Y)<y or (x,y)==(1,2),"window maximum contraction")
            check(y-x<2 or abs(Y-X)<y-x,"window gap contraction")
            count+=1
    return count


def mutation_tests(samples,gates):
    tests=[]
    def add(kind,key,value):
        r=deepcopy(samples[kind]);r[key]=value;tests.append((kind,r))
    g=samples["gap"];a=samples["affine"];o=samples["original"];c=samples["comparison"]
    add("gap","g",g["g"]+1);add("gap","g",True)
    add("gap","modulus",2*g["modulus"]);add("gap","residue",g["residue"]+1)
    add("gap","left","1"+g["left"][1:]);add("gap","endpoint",[1.0,g["endpoint"][1]])
    add("affine","a",True);add("affine","b",a["b"]+1)
    add("affine","negative","");add("affine","negative_endpoint",a["negative_endpoint"]+1)
    add("affine","residue",a["residue"]+1);add("affine","variant",99)
    add("original","m",o["m"]+1);add("original","r",o["r"]+1)
    add("original","minimum",o["n"]);add("original","no_forward_descent",False)
    add("original","left",o["left"][:-1]);add("comparison","status","OUTSIDE")
    add("comparison","endpoint",c["endpoint"]+1);add("comparison","terminal",c["terminal"]+1)
    funcs={"gap":gap_row,"affine":affine_row,"original":lambda r:original_row(r,gates),
           "comparison":lambda r:comparison_row(r,gates)}
    rejected=0
    for kind,row in tests:
        try:funcs[kind](parse(json.dumps(row)))
        except (ValueError,KeyError,TypeError):rejected+=1
        else:raise ValueError("semantic corruption accepted: "+kind)
    for text in ('{"x":1,"x":2}','{"x":NaN}','{"x":1.0}'):
        try:parse(text)
        except ValueError:rejected+=1
        else:raise ValueError("JSON corruption accepted")
    return rejected


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("full",type=Path);p.add_argument("--summary",type=Path,required=True)
    p.add_argument("--self-test",action="store_true");args=p.parse_args()
    summary=parse(args.summary.read_text(encoding="utf-8"));limit=nat(summary["limit"],1)
    check(limit<=65536 and summary["schema"]=="escape-gap-v1"
          and summary["status"]=="PROPOSED" and summary["complete_collatz_proof"] is False,
          "summary scope")
    counts=Counter();digest=hashlib.sha256();gates={};gaps=set();originals=[];comparisons=[];samples={}
    with args.full.open("rb") as f:
        for data in f:
            digest.update(data);r=parse(data.decode());kind=r["kind"];counts[kind]+=1
            if kind=="gap":
                gap_row(r);key=(r["g"],r["variant"])
                check(key not in gaps,"duplicate gap input");gaps.add(key);samples.setdefault(kind,r)
            elif kind=="affine":
                affine_row(r);key=(r["a"],r["b"],r["variant"])
                check(key not in gates,"duplicate gate");gates[key]=r;samples.setdefault(kind,r)
            elif kind=="original":originals.append(r);samples.setdefault(kind,r)
            elif kind=="comparison":comparisons.append(r)
            else:raise ValueError("unknown corpus kind")
    expected_gaps={(g,v) for g in list(range(1,4097))+[2**127-1,2**128,10**50+17,2**255+12345]
                   for v in range(3)}
    check(gaps==expected_gaps,"complete gap corpus")
    check(len(originals)==64,"original corpus size")
    original_keys=set()
    for r in originals:
        original_row(r,gates);key=(r["family"],r["index"],r["r"])
        if r["family"]=="rung" and r["index"]%3==2:counts["one_third_controls"]+=1
        check(key not in original_keys,"duplicate original row");original_keys.add(key)
    check(Counter((r["family"],r["index"]) for r in originals)
          ==Counter({(f,j):2 for f in ("escape","rung") for j in range(1,17)}),"original parameter grid")
    check(len(comparisons)==limit,"comparison corpus length")
    extra=[]
    for expected,r in enumerate(comparisons,1):
        check(type(r["c"]) is int and r["c"]==expected,"complete ordered input grid")
        comparison_row(r,gates)
        counts["baseline_"+r["baseline"]]+=1;counts["new_"+r["status"]]+=1
        if r.get("mechanism")=="escape":
            counts["additional_mergers"]+=1;extra.append(r["c"]);samples.setdefault("comparison",r)
    counts["window_controls"]=window_count()
    check(dict(counts)==summary["counts"],"typed aggregate counts")
    check(all(type(x) is int for x in summary["counts"].values()),"aggregate integer types")
    check(extra[:24]==summary["additional_samples"],"addition sample")
    check(digest.hexdigest()==summary["rows_sha256"],"full corpus digest")
    check(summary["parent"]=="081dd4fb8af75b3b237a5eb4cef28b84bb5329be","source pin")
    expected_examples=[{k:r[k] for k in ("family","index","r","n","m","endpoint","minimum")}
                       for r in originals[:4]+originals[32:36]]
    check(json.dumps(summary["original_examples"],sort_keys=True)==json.dumps(expected_examples,sort_keys=True),
          "typed example summary")
    rejected=mutation_tests(samples,gates) if args.self_test and "comparison" in samples else 0
    print(json.dumps(dict(result="PASS",rows=sum(counts[k] for k in ("gap","affine","original","comparison")),
                         symbolic_gap_cylinders=len(gaps),symbolic_affine_cylinders=len(gates),
                         original_certificates=len(originals),additional_mergers=len(extra),
                         rejected_mutations=rejected,rows_sha256=digest.hexdigest()),sort_keys=True))


if __name__=="__main__":main()
