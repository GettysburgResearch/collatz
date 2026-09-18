"""Independent finite meeting verifier; imports no Observatory arithmetic kernel.

Usage: python -m observatory.verify collatz-meeting.json
This checks the stated finite equality, not global convergence or completeness.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
from typing import Any


def positive(value: Any) -> int:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{1,2500}", value):
        raise ValueError("An exact integer must be a bounded decimal string.")
    n=int(value)
    if n<=0 or n.bit_length()>8192:
        raise ValueError("Integer outside the positive 8192-bit domain.")
    return n


def index(value: Any, limit=40000) -> int:
    if type(value) is not int or not 0<=value<=limit:
        raise ValueError("Invalid bounded clock/index.")
    return value


def raw_value(seed: int, clock: int) -> int:
    n=seed
    for _ in range(clock):
        if n==1:
            raise ValueError("Witness extends beyond the first visit to 1.")
        n=3*n+1 if n%2 else n//2
        if n.bit_length()>8192:
            raise ValueError("Replay exceeds the independent verifier bit cap.")
    return n


def displayed_anchor(seed: int, mode: str, target: int) -> int | None:
    if mode not in ("raw","shortcut","odd") or mode=="odd" and seed%2==0:
        raise ValueError("Invalid displayed map/domain.")
    n, raw, step=seed,0,0
    while raw<target:
        if n==1:
            raise ValueError("Arrival is beyond stopped support.")
        if n%2==0:
            n//=2;raw+=1
        else:
            n=3*n+1;raw+=1
            if mode=="shortcut":
                n//=2;raw+=1
            elif mode=="odd":
                while n%2==0:
                    n//=2;raw+=1
        step+=1
    return step if raw==target else None


def verify(data: Any) -> dict:
    if not isinstance(data,dict) or data.get("schema")!="collatz-meeting/v1":
        raise ValueError("Expected collatz-meeting/v1.")
    values=[]
    for side in ("left","right"):
        row=data.get(side)
        if not isinstance(row,dict):
            raise ValueError("Missing side record.")
        seed=positive(row.get("seed"));clock=index(row.get("raw"));n=positive(row.get("n"))
        if raw_value(seed,clock)!=n:
            raise ValueError(f"{side} raw replay disagrees.")
        step=displayed_anchor(seed,row.get("map"),clock)
        claimed=row.get("step")
        if claimed is not None:
            index(claimed,10000)
        if claimed!=step:
            raise ValueError(f"{side} displayed clock does not match its raw arrival.")
        if row.get("bits",n.bit_length())!=n.bit_length() or row.get("parity",n%2)!=n%2:
            raise ValueError("Exact bit/parity metadata disagrees.")
        values.append((seed,n))
    if values[0][1]!=values[1][1]:
        raise ValueError("The two replayed states are not equal.")
    request=data.get("request")
    if not isinstance(request,dict) or positive(request.get("seed"))!=values[0][0]:
        raise ValueError("Source recipe is missing or inconsistent.")
    relation=request.get("relation")
    if relation=="flip":
        bit=index(request.get("bit"),8191);partner=values[0][0]^(1<<bit)
    elif relation=="offset":
        delta=request.get("delta")
        if not isinstance(delta,str) or not re.fullmatch(r"[+-]?[0-9]{1,2500}",delta):
            raise ValueError("Invalid exact offset.")
        partner=values[0][0]+int(delta)
    elif relation=="explicit":
        partner=positive(request.get("other"))
    else:
        raise ValueError("Unknown partner relation.")
    if partner!=values[1][0]:
        raise ValueError("Partner relation disagrees with the replayed source.")
    if request.get('map_left')!=data['left']['map'] or request.get('map_right')!=data['right']['map']:
        raise ValueError("Source recipe clocks disagree with the witness clocks.")
    return {"verified":True,"common_state":str(values[0][1]),
            "raw_arrivals":[data['left']['raw'],data['right']['raw']],
            "displayed_arrivals":[data['left']['step'],data['right']['step']],
            "scope":"Independent exact replay of sources, perturbation, finite common value, raw arrivals and represented/hidden displayed anchors. Kernel digests and approximate plot logs are not trusted certificates. No all-time or completeness claim."}


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file',type=Path)
    args=parser.parse_args()
    try:
        if args.file.stat().st_size>200000:
            raise ValueError('Witness exceeds 200 kB.')
        def reject(value):
            raise ValueError('Nonfinite JSON constant: '+value)
        data=json.loads(args.file.read_text(encoding='utf-8'),parse_constant=reject)
        print(json.dumps(verify(data),indent=2))
        return 0
    except (ValueError,OSError,TypeError,KeyError) as exc:
        print(json.dumps({'verified':False,'error':str(exc)}))
        return 1

if __name__=='__main__':
    raise SystemExit(main())
