#!/usr/bin/env python3
"""Independent bounded reconstruction of the elementary GRH interfaces."""
from __future__ import annotations

import argparse
from collections import deque
import hashlib
import json
from pathlib import Path


def need(ok: bool, why: str) -> None:
    if not ok:
        raise ValueError(why)


def shortcut(n: int) -> int:
    need(type(n) is int and n > 0, 'positive ordinary input')
    return (3*n+1)//2 if n%2 else n//2


def parities(n: int, length: int) -> tuple[int, ...]:
    out=[]
    for _ in range(length):
        out.append(n%2)
        n=shortcut(n)
    return tuple(out)


def connected(modulus: int, affine: bool = True) -> int:
    adjacent=[set() for _ in range(modulus)]
    for x in range(modulus):
        targets=[2*x%modulus]
        if affine:
            targets.append((3*x+1)%modulus)
        for y in targets:
            adjacent[x].add(y)
            adjacent[y].add(x)
    remaining=set(range(modulus))
    count=0
    while remaining:
        queue=deque([remaining.pop()])
        count+=1
        while queue:
            for y in adjacent[queue.popleft()]:
                if y in remaining:
                    remaining.remove(y)
                    queue.append(y)
    return count


def run(source_dir: Path) -> dict:
    counts={'parity_lifts':0,'prescribed_unit_classes':0,
            'certified_sources':0,'blocked_levels':0,'odd_period_quotients':0}
    for length in range(2,10):
        modulus=1<<length
        words=set()
        for residue in range(1,modulus,2):
            base=parities(residue,length)
            words.add(base)
            for lift in range(1,5):
                need(parities(residue+lift*modulus,length)==base,'parity cylinder')
                counts['parity_lifts']+=1
        need(len(words)==modulus//2,'odd-first word bijection')

    for e in range(1,8):
        modulus=3**e
        bound=modulus.bit_length()-1
        good=0
        for residue in range(1,modulus):
            if residue%3==0:
                continue
            n=residue if residue%2 else residue+modulus
            hits=[]
            for a in range(1,bound+1):
                numerator=(n<<a)-1
                if numerator%modulus==0:
                    q=numerator//modulus
                    need(0<q<n,'literal prescribed-level strict decrease')
                    hits.append(a)
            need(len(hits)<=1,'short powers distinct')
            good+=bool(hits)
            counts['prescribed_unit_classes']+=1
        need(good==bound,'exact short class count')
        if e>=3:
            least=3**(e-1)
            need(pow(2,least,modulus)==modulus-1,'minus-one exponent')
            need((1<<least)>modulus,'strict height obstruction')

    valuations=[]
    for E in range(3,9):
        exponent=3**E+1
        numerator=(1<<exponent)-1
        need(numerator%3==0,'certified source integrality')
        n=numerator//3
        need(n>1 and n%2==1 and n%3!=0,'source domain')
        raw=3*n+1
        need(raw==1<<exponent,'full depth-one certificate')
        z=n+1
        valuation=0
        while z%3==0:
            z//=3
            valuation+=1
        need(valuation==E,'independently stripped exact valuation')
        for e in range(3,E+1):
            modulus=3**e
            need(n%modulus==modulus-1,'all prescribed source levels')
            for a in range(1,modulus.bit_length()):
                need(((n<<a)-1)%modulus!=0,'no affordable inverse')
            counts['blocked_levels']+=1
        valuations.append({'E':E,'division_exponent':exponent,'v3_n_plus_1':valuation})
        counts['certified_sources']+=1

    for modulus in range(1,258,2):
        need(connected(modulus)==1,'odd-period affine quotient')
        counts['odd_period_quotients']+=1
    need(connected(7,False)==3,'without additive law three classes remain')

    return {'status':'PASS','counts':counts,'valuation_examples':valuations,
            'scope':'Independent no-import bounded arithmetic for G1 parity cylinders, G2/G3 prescribed-level claims and G5 odd-period rigidity. External GRH prime bounds and Chebotarev theorem not reproved.',
            'author_note_sha256':hashlib.sha256((source_dir/'GRH_INTERFACES.md').read_bytes()).hexdigest(),
            'author_checker_sha256':hashlib.sha256((source_dir/'check_grh_interfaces.py').read_bytes()).hexdigest()}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir',type=Path,required=True)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    raw=json.dumps(run(args.source_dir),indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(raw,encoding='utf-8')
    print(raw,end='')
