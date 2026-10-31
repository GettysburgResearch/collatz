#!/usr/bin/env python3
"""Exact finite-state inverse-cone credit certificate and independent replay.

The fixed-point search is synthesis only. Verification checks every modular
state and all three high-digit lifts with integer arithmetic. Neither the
compiler nor its credit proves Collatz termination.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import random

DIGITS=8
MODULUS=3**DIGITS
ALPHABET='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def need(ok: bool, why: object) -> None:
    if not ok:
        raise RuntimeError(str(why))


def synthesize() -> dict:
    units=tuple(c for c in range(MODULUS) if c%3)
    index={c:i for i,c in enumerate(units)}
    options=[]
    for c in units:
        actions=[]
        for a in range(1,7):
            if (2**a*c-1)%3:
                continue
            d=(2**a*c-1)//3
            if d%3==0:
                continue
            successors=tuple(index[(d+2**a*(MODULUS//3)*q)%MODULUS] for q in range(3))
            actions.append((a,successors))
        need(bool(actions),('no action',c))
        options.append(actions)
    values=[0]*len(units)
    for iteration in range(1,10001):
        new=[max(0,min(3*a-7+max(values[j] for j in successors)
                         for a,successors in actions)) for actions in options]
        if new==values:
            break
        values=new
    else:
        raise RuntimeError('synthesis cap reached; no certificate claimed')
    encoded=''.join(ALPHABET[x] for x in values)
    return {'modulus':MODULUS,'digits':DIGITS,'cost_scale':3,'per_step_credit':7,
            'potential':encoded,'unit_order':'increasing residues in [0,modulus) not divisible by 3',
            'synthesis_iterations':iteration,'maximum_potential':max(values)}


def verify(certificate: dict) -> tuple[dict[int,int],dict[int,int]]:
    # This verifier does not call the synthesis recurrence or use its successor table.
    need(certificate['modulus']==6561,'unexpected modulus')
    need(certificate['cost_scale']==3 and certificate['per_step_credit']==7,'unexpected rate')
    units=[r for r in range(6561) if r%3]
    values=[ALPHABET.index(x) for x in certificate['potential']]
    need(len(values)==4374,'wrong certificate length')
    need(min(values)>=0 and max(values)<=18,'potential range')
    credit=dict(zip(units,values))
    policy={}
    for residue in units:
        for a in range(1,7):
            good=True
            for high in range(3):
                c=residue+6561*high
                numerator=2**a*c-1
                if numerator%3:
                    good=False;break
                d=numerator//3
                if d<=0 or d%3==0 or 3*a+credit[d%6561]>7+credit[residue]:
                    good=False;break
            if good:
                policy[residue]=a
                break
        need(residue in policy,('failed universal credit row',residue))
    return credit,policy


def compile_cone(t: int,c: int,policy: dict[int,int]) -> tuple[int,int,tuple[int,...]]:
    need(t>=1 and 0<c<3**t and c%3!=0,('cone domain',t,c))
    constant,coefficient,k=c,3**t,0
    blocks=[]
    for remaining in range(t,0,-1):
        a=policy[constant%6561] if remaining>1 else (1 if constant%3==2 else 2)
        coefficient=coefficient*2**a//3
        constant=(constant*2**a-1)//3
        k+=a;blocks.append(a)
    need(coefficient==2**k and 0<constant<2**k,('normal form',t,c))
    need(3*k<=7*t+17,('amortized compiler bound',t,c,k))
    return k,constant,tuple(blocks)


def trace(n: int,k: int) -> tuple[int,int]:
    odd=0
    for _ in range(k):
        need(n>1,('postterminal step',n,k))
        if n&1:
            odd+=1;n=(3*n+1)//2
        else:n//=2
    return n,odd


@lru_cache(maxsize=None)
def short_plan(depth: int,residue: int,preserve_unit: bool) -> tuple[int,tuple[int,...]]:
    """Exact finite enumeration, separate from the credit policy.

    Uses modulus 3^(depth+1) when preserving the final unit and 3^depth
    otherwise. The budget is the earlier 4*depth upper bound, not a search
    that assumes the improved 3*depth theorem.
    """
    if depth==0:
        return (0,()) if not preserve_unit or residue%3 else (10**6,())
    if residue%3==0:
        return 10**6,()
    modulus=3**(depth+(1 if preserve_unit else 0))
    need(0<=residue<modulus,('plan residue',depth,residue,preserve_unit))
    best=(4*depth+1,())
    for a in range(1,4*depth+1):
        numerator=2**a*residue-1
        if numerator%3:
            continue
        next_residue=(numerator//3)%(modulus//3)
        cost,suffix=short_plan(depth-1,next_residue,preserve_unit)
        if a+cost<best[0]:
            best=(a+cost,(a,)+suffix)
    return best


def validate_short_blocks() -> dict:
    preserving=[short_plan(4,c,True)[0] for c in range(3**5) if c%3]
    need(len(preserving)==162 and max(preserving)==12,'four-step preserving cover')
    terminal=[]
    for t in range(1,5):
        maximum=max(short_plan(t,c,False)[0] for c in range(3**t) if c%3)
        need(maximum<=3*t,('terminal block bound',t,maximum))
        terminal.append(maximum)
    return {'four_step_unit_states':162,'four_step_maximum_cost':12,
            'terminal_maxima_depth_1_to_4':terminal,
            'universal_bound':'k <= 3*t; for t=1 the sharper bound is 2'}


def run(certificate: dict) -> dict:
    potential,policy=verify(certificate)
    checks=0
    for t in range(1,8):
        for c in range(1,3**t):
            if c%3==0:continue
            k,r,blocks=compile_cone(t,c,policy)
            for x in (1,2,7):
                endpoint,odd=trace((x<<k)+r,k)
                need((endpoint,odd)==(3**t*x+c,t),('cone identity',t,c,x))
                checks+=1
    rng=random.Random(20261031)
    large=0
    maximum_bits=0
    for t in (8,16,32,64,128,256):
        candidates=[1,2,3**t-1,3**t-2]
        candidates += [rng.randrange(1,3**t) for _ in range(20)]
        for c in candidates:
            if c%3==0:continue
            k,r,blocks=compile_cone(t,c,policy)
            x=2**257+1
            source=(x<<k)+r
            need(trace(source,k)==(3**t*x+c,t),('large cone',t,c))
            maximum_bits=max(maximum_bits,source.bit_length())
            large+=1
    bad=dict(certificate);bad['potential']='0'*4374
    rejected=False
    try:verify(bad)
    except RuntimeError:rejected=True
    need(rejected,'zero-credit mutation was accepted')
    bounds=[]
    for t in (10,20,50,100,500):
        count=2*3**(t-1)
        k=t
        while math.comb(k,t)<count:k+=1
        # Pure integer replacement of floor(t*log2(3)).
        contracting_limit=(3**t).bit_length()-1
        bounds.append({'ternary_width':t,'necessary_universal_maximum_length':k,
                       'contracting_length_limit':contracting_limit,
                       'contracting_tail_count_upper_bound':math.comb(contracting_limit,t),
                       'unit_tail_count':count})
    encoded=certificate['potential'].encode('ascii')
    return {'status':'PROPOSED all-residue certificate plus EMPIRICAL physical replay; not Collatz termination',
            'modulus':6561,'unit_states_verified':4374,'high_digit_lifts_per_state':3,
            'potential_range':[min(potential.values()),max(potential.values())],
            'potential_sha256':hashlib.sha256(encoded).hexdigest(),
            'synthesis_iterations':certificate['synthesis_iterations'],
            'chosen_action_maximum':max(policy.values()),
            'credit_inequality':'3*a + V((2^a*c-1)/3) <= 7 + V(c)',
            'universal_bound':'k <= floor((7*t+17)/3)',
            'complete_small_cone_replays':checks,'large_cone_replays':large,
            'maximum_replayed_source_bits':maximum_bits,
            'zero_potential_mutation_rejected':rejected,
            'short_blocks':validate_short_blocks(),'counting_lower_bounds':bounds}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--certificate',type=Path)
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    cert=synthesize()
    if a.certificate:
        a.certificate.write_text(json.dumps(cert,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    text=json.dumps(run(cert),sort_keys=True,indent=2)+'\n'
    if a.output:a.output.write_text(text,encoding='utf-8')
    else:print(text,end='')

if __name__=='__main__':main()
