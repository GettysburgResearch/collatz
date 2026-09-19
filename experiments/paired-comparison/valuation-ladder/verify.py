#!/usr/bin/env python3
"""Separate forward-state verifier; imports no generator or repository modules."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path


def need(ok, msg):
    if not ok:
        raise ValueError(msg)


def T(n):
    need(type(n) is int and n > 0, "nonpositive/noninteger state")
    return n//2 if n % 2 == 0 else (3*n+1)//2


def val(n):
    need(type(n) is int and n > 0, "invalid valuation")
    s=0
    while n % 2 == 0:
        n //= 2
        s += 1
    return s


def move(pair, times):
    words=["", ""]
    a,b=pair
    for _ in range(times):
        words[0] += str(a % 2)
        words[1] += str(b % 2)
        a,b=T(a),T(b)
    return (a,b),words


def stage(c, old=False):
    need(type(c) is int and c > 0, "invalid comparison parameter")
    original=(9*c+2,c)
    if old:
        r=val(c+2)-1
        if r < 3:
            return None
        pair,words=move(original,r+3)
    else:
        # A different construction: iterate actual Q states, rather than
        # substituting a valuation bridge's closed endpoint formula.
        if c % 4 == 2:
            pair,_=move(original,2)
            length=2
        elif c % 8 == 3:
            pair,_=move(original,3)
            length=3
        else:
            return None
        d=pair[1]
        need(pair[0] == 3*d-1, "Q seed failure")
        while d % 4 == 1:
            need(d > 1, "unexpected fixed Q parameter")
            pair,_=move(pair,2)
            d=pair[1]
            length += 2
            need(pair[0] == 3*d-1, "Q repeat failure")
        if d % 4 != 3:
            return None
        pair,_=move(pair,2)
        length += 2
        need(pair[1] == 3*pair[0]+2, "affine exit failure")
        while pair[0] % 2:
            pair,_=move(pair,1)
            length += 1
            need(pair[1] == 3*pair[0]+2, "odd exit failure")
        pair,_=move(pair,2)
        length += 2
        pair2,words=move(original,length)
        need(pair2 == pair, "stage replay mismatch")
    if pair[0] == pair[1]:
        return "MERGE",pair[0],len(words[0]),*words
    need(pair[1] == 9*pair[0]+2, "not a hard return")
    return "RETURN",pair[0],len(words[0]),*words


def expected(c, old=False, budget=256):
    root,total,orientation=c,0,0
    words=["",""]
    stages=[]
    for _ in range(budget):
        out=stage(c,old)
        if out is None:
            return dict(c=root,status="OUTSIDE",terminal=c,clock=total,
                        orientation=orientation,stages=stages,words=words)
        status,d,clock,w,v=out
        words[orientation] += w
        words[1-orientation] += v
        total += clock
        stages.append(dict(c=c,status=status,d=d,clock=clock))
        if status == "MERGE":
            return dict(c=root,status="MERGE",endpoint=d,clock=total,
                        stages=stages,words=words)
        c,orientation=d,1-orientation
    return dict(c=root,status="BUDGET",terminal=c,clock=total,
                orientation=orientation,stages=stages,words=words)


def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":"))


def check_row(row,c):
    want={"old":expected(c,True),"new":expected(c)}
    need(canonical(row) == canonical(want),"typed row mismatch")


def unique(pairs):
    d={}
    for k,v in pairs:
        need(k not in d,"duplicate JSON key")
        d[k]=v
    return d


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("full",type=Path)
    p.add_argument("--summary",type=Path,required=True)
    p.add_argument("--self-test",action="store_true")
    args=p.parse_args()
    digest=hashlib.sha256()
    counts={mode:dict(admitted=0,MERGE=0,OUTSIDE=0,BUDGET=0) for mode in ["old","new"]}
    count=0
    with args.full.open(encoding="utf-8") as f:
        for count,line in enumerate(f,1):
            row=json.loads(line,object_pairs_hook=unique)
            check_row(row,count)
            digest.update((canonical(row)+"\n").encode())
            for mode in counts:
                counts[mode][row[mode]["status"]] += 1
                counts[mode]["admitted"] += stage(count,mode == "old") is not None
    summary=json.loads(args.summary.read_text(encoding="utf-8"),object_pairs_hook=unique)
    need(type(summary["limit"]) is int and summary["limit"] == count,"missing/extra rows")
    need(canonical(summary["counts"]) == canonical(counts),"count mismatch")
    need(summary["rows_sha256"] == digest.hexdigest(),"full digest mismatch")
    rejected=0
    if args.self_test:
        good={"old":expected(59,True),"new":expected(59)}
        mutations=[]
        for path,value in [(("new","clock"),8),(("new","endpoint"),39),
                           (("new","c"),True),(("new","words"),["0000000","1101100"]),
                           (("new","status"),"OUTSIDE"),(("old","c"),59.0)]:
            bad=copy.deepcopy(good)
            bad[path[0]][path[1]]=value
            mutations.append(bad)
        for bad in mutations:
            try:
                check_row(bad,59)
            except ValueError:
                rejected += 1
            else:
                raise ValueError("forged witness accepted")
        try:
            json.loads('{"x":1,"x":2}',object_pairs_hook=unique)
        except ValueError:
            rejected += 1
        else:
            raise ValueError("duplicate key accepted")
    print(json.dumps(dict(rows=count,counts=counts,rows_sha256=digest.hexdigest(),
                          rejected_controls=rejected,status="PASS"),sort_keys=True))


if __name__ == "__main__":
    main()
