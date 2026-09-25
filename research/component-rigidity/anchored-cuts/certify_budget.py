#!/usr/bin/env python3
"""Produce a literal convergence path OR a separator-energy lower certificate.

Uncapped mathematical procedure terminates by FC-006 (not by Collatz).
Default resource cap is explicit; it can return UNRESOLVED_AT_RESOURCE_CAP.
Use --max-height 0 only to request the uncapped procedure.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
from experiment import cut_certificate, require, step
from verify_certificates import check_cut


def certify(anchor: int, budget: Fraction, multiplier: int = 3,
            max_height: int = 65536) -> dict:
    require(anchor>=1 and budget>=0, 'positive anchor and nonnegative budget required')
    require(max_height==0 or max_height>=2, 'invalid resource cap')
    if anchor==1:
        return dict(status='CONVERGENCE',anchor=1,multiplier=multiplier,path=[1],height=1)
    height=1 << max(1,(anchor-1).bit_length())
    inspected=[]
    while max_height==0 or height<=max_height:
        c=cut_certificate(height,anchor,multiplier)
        check_cut(c)
        inspected.append(height)
        if c['status']=='MERGED_WITHIN_CUTOFF':
            n=anchor
            path=[n]
            seen={n}
            while n!=1:
                n=step(n,multiplier)
                require(n<=height, 'purported finite core component exited')
                require(n==1 or n not in seen, 'purported core link entered another cycle')
                path.append(n)
                seen.add(n)
            return dict(status='CONVERGENCE',anchor=anchor,multiplier=multiplier,
                        budget=[budget.numerator,budget.denominator],height=height,
                        inspected_heights=inspected,path=path)
        if Fraction(*c['capacity'])>budget:
            return dict(status='ENERGY_BUDGET_EXCLUDED',anchor=anchor,multiplier=multiplier,
                        budget=[budget.numerator,budget.denominator],height=height,
                        inspected_heights=inspected,certificate=c)
        height*=2
    return dict(status='UNRESOLVED_AT_RESOURCE_CAP',anchor=anchor,multiplier=multiplier,
                budget=[budget.numerator,budget.denominator],max_height=max_height,
                inspected_heights=inspected)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('anchor',type=int)
    p.add_argument('--budget',type=Fraction,required=True)
    p.add_argument('--multiplier',type=int,choices=(3,5),default=3)
    p.add_argument('--max-height',type=int,default=65536)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    result=certify(a.anchor,a.budget,a.multiplier,a.max_height)
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('certificate','path')},indent=2))

if __name__=='__main__':
    main()
