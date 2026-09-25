#!/usr/bin/env python3
"""Bounded comparisons, distinct from the independent sparse certificate check.
Compares circle formula with a line dynamic program and with old full-graph cuts.
"""
from fractions import Fraction
import importlib.util
import itertools
import json
from math import lcm
from pathlib import Path
import random
from run import certificate, ladder, profile, step
from verify import check


def need(ok,msg):
    if not ok:
        raise ValueError(msg)


def line_minimum(rays,k):
    end=1 << (k+1)
    pins={}
    for n,b in rays:
        while n <= end:
            need(n not in pins or pins[n] == b, 'inconsistent ray assignment')
            pins[n]=b
            n*=2
    scale=lcm(*range(1,k+2))**2
    infinity=10*end*scale
    costs=[0 if pins.get(1,b)==b else infinity for b in (0,1)]
    for n in range(2,end+1):
        w=scale//((n-1).bit_length()**2)
        costs=[min(costs[b],costs[1-b]+w) if pins.get(n,b)==b else infinity for b in (0,1)]
    return Fraction(min(costs),scale)


def main():
    exhaustive=0
    for choices in itertools.product((-1,0,1),repeat=7):
        rays=[(1,0)]+[(n,b) for n,b in zip(range(3,16,2),choices) if b>=0]
        _,value=profile(rays,4)
        need(value==line_minimum(rays,4),'exhaustive line comparison')
        exhaustive+=1
    rng=random.Random(314159)
    randomized=0
    for k in range(3,10):
        for _ in range(32):
            rays=[(1,0)]
            chosen={1:0}
            for _ in range(24):
                n=rng.randrange(2,1 << (k+1))
                odd=n//(n & -n)
                color=chosen.setdefault(odd,rng.randrange(2))
                rays.append((n,color))
            _,value=profile(rays,k)
            need(value==line_minimum(rays,k),'delayed activation line comparison')
            randomized+=1
    old=Path(__file__).resolve().parents[1]/'anchored-cuts'/'experiment.py'
    spec=importlib.util.spec_from_file_location('old_cut_experiment',old)
    full=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(full)
    comparisons=[]
    for p,n in ((3,7),(3,27),(3,97),(5,13),(5,17)):
        for depth in range(4):
            a,ns0,_=ladder(1,p,depth)
            b,ns1,_=ladder(n,p,depth)
            k=max(x.bit_length()-1 for x in ns0+ns1)
            c=certificate(n,p,depth,k)
            need(c['status']=='CAPACITY_LOWER_CERTIFICATE','unexpected test collision')
            h=1 << c['ambient_height_exponent']
            if h>32768:
                continue
            answer=full.cut_certificate(h,n,p)
            sparse=Fraction(*(int(v,16) for v in c['capacity']))
            if answer['status']=='FINITE_SEPARATOR':
                need(sparse<=Fraction(*answer['capacity']),'sparse lower bound exceeds full cut')
            comparisons.append(dict(multiplier=p,source=n,depth=depth,height=h,
                                    sparse=[sparse.numerator,sparse.denominator],
                                    full=answer.get('capacity'),status=answer['status']))
    # An all-time disjointness certificate for the deterministic 27/core ladders.
    _,core,_=ladder(1,3,3)
    _,other,_=ladder(27,3,0)
    need(core == [1,5,13,17,181] and other == [27,41], 'permanent control changed')
    need(41 not in core and core[-1]>41 and 27%3==0,'nonintersection seed check')
    path=[27]
    for _ in range(10000):
        if path[-1]==1:
            break
        path.append(step(path[-1],3))
    need(path[-1]==1,'27 convergence replay exhausted')
    # Full-cycle nonintersection control: the two original sources truly differ for p=5.
    cycles=[[1,3,8,4,2],[13,33,83,208,104,52,26]]
    for cyc in cycles:
        need(all(step(n,5)==t for n,t in zip(cyc,cyc[1:]+cyc[:1])),'5x+1 cycle')
    need(not set(cycles[0]) & set(cycles[1]),'5x+1 cycle overlap')
    uniform_blocks=[]
    for p,n,a,q in ((3,27,1054,665),(5,13,1154,497)):
        need(2**(a*q-1)<p**(q*q)<2**(a*q+1), 'exact irrational-rotation approximation')
        burn=4*(2*q).bit_length()
        depth=burn+q
        c=certificate(n,p,depth,18*q-1)
        check(c)
        h0=max(n,8).bit_length()
        need(q>=h0+8*burn, 'uniform source-height guard')
        count=2*sum(b for h,b in c['births'] if h<=9*q)
        need(count>=q//8, 'rotation-grid lower alternation count')
        block=Fraction(count,36*q)
        need(block>=Fraction(1,576), 'uniform block charge')
        uniform_blocks.append(dict(multiplier=p,source=n,numerator=a,denominator=q,
                                   burn=burn,depth=depth,ambient_exponent=c['ambient_height_exponent'],
                                   alternations_at_block_start=count,
                                   certified_block_lower_bound=[block.numerator,block.denominator]))
    result=dict(status='PASS',exhaustive_ray_line_cases=exhaustive,
                delayed_activation_cases=randomized,full_cut_comparisons=comparisons,
                permanent_27_control=dict(core_nodes=core,other_nodes=other,
                                          convergence_path=path,peak=max(path)),
                five_x_plus_one_cycles=cycles,uniform_blocks=uniform_blocks)
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
