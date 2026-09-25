#!/usr/bin/env python3
"""Literal checker for pass 2; imports neither experiment nor max-flow code.

Rebuilds finite components by graph traversal (not the generator's union-find),
checks rational capacity construction, antisymmetric flow bounds/conservation,
and a matching Boolean cut. Integer arithmetic only. No assert statements.
"""
from __future__ import annotations
from collections import defaultdict
import copy
from fractions import Fraction
import hashlib
import json
from math import lcm
from pathlib import Path
import sys


def need(ok, msg):
    if not ok:
        raise ValueError(msg)


def map_value(n, multiplier):
    need(n >= 1 and multiplier in (3,5), 'invalid physical input')
    if n & 1:
        return (multiplier*n+1)//2
    return n//2


def partition(h, multiplier):
    neighbors = [[] for _ in range(h+1)]
    for n in range(1,h+1):
        t = map_value(n,multiplier)
        if t <= h:
            neighbors[n].append(t)
            neighbors[t].append(n)
    comp = [0]*(h+1)
    for start in range(1,h+1):
        if comp[start]:
            continue
        comp[start] = start
        stack = [start]
        while stack:
            n = stack.pop()
            for m in neighbors[n]:
                if not comp[m]:
                    comp[m] = start
                    stack.append(m)
    return comp


def check_cut(c):
    h, anchor, multiplier = c['height'],c['anchor'],c['multiplier']
    need(h >= 2 and 1 < anchor <= h,'invalid height/anchor')
    comp = partition(h,multiplier)
    labels = set(comp[1:])
    need(len(labels)==c['quotient_vertices'],'component count')
    if c['status']=='MERGED_WITHIN_CUTOFF':
        need(comp[1]==comp[anchor],'false merge claim')
        return 0
    need(c['status']=='FINITE_SEPARATOR','invalid status')
    need(comp[1]!=comp[anchor],'separation impossible')
    scale = lcm(*(i*i for i in range(1,(h-1).bit_length()+1)))
    need(scale==c['scale'],'wrong capacity scaling')
    caps = defaultdict(int)
    for n in range(1,h):
        a,b = sorted((comp[n],comp[n+1]))
        if a != b:
            caps[a,b] += scale//n.bit_length()**2
    need(len(caps)==c['quotient_edges'],'edge count')
    ones = set(c['ones'])
    need(len(ones)==len(c['ones']) and ones<=labels,'invalid cut labels')
    need(comp[anchor] in ones and comp[1] not in ones,'lost pin')
    value = sum(v for (a,b),v in caps.items() if (a in ones)!=(b in ones))
    need(value==c['scaled_capacity'],'cut value mismatch')
    need(Fraction(value,scale)==Fraction(*c['capacity']),'rational value mismatch')
    balance = defaultdict(int)
    seen = set()
    for a,b,f in c['flow']:
        need((a,b) not in seen,'duplicate flow edge')
        seen.add((a,b))
        need((a,b) in caps and isinstance(f,int),'nonexistent flow edge')
        need(abs(f)<=caps[a,b],'flow capacity violation')
        balance[a] += f
        balance[b] -= f
    for label in labels:
        target = value if label==comp[anchor] else -value if label==comp[1] else 0
        need(balance[label]==target,'flow divergence violation')
    bits = [int(n in ones) for n in comp]
    for n in range(1,h+1):
        t = map_value(n,multiplier)
        if t<=h:
            need(bits[n]==bits[t],'physical edge violation')
    variations = [sum(bits[n]!=bits[n+1] for n in range(1<<k,1<<(k+1)))
                  for k in range(h.bit_length()-1)]
    need(variations==c['shell_variation'],'variation mismatch')
    need(hashlib.sha256(bytes(bits[1:])).hexdigest()==c['coloring_sha256'],'color hash')
    return len(c['flow'])


def check_corridor(c):
    k,r = c['k'],c['r']
    need(1<=r<=k-2,'corridor parameter domain')
    a = 2**(k-r)
    h = 4*3**(r-1)*a
    need(h==c['height'],'corridor height')
    ts = list(range(4*a//3+2,2*a+1))
    seeds = [2**r*t-1 for t in ts]
    need(len(seeds)==c['seeds'] and seeds[0]==c['first_seed'] and seeds[-1]==c['last_seed'],
         'corridor source list')
    seen_exits = set()
    edge_count = 0
    for t,seed in zip(ts,seeds):
        n=seed
        for j in range(r):
            need(n == 3**j * 2**(r-j)*t-1,'affine identity')
            need(2**k<=seed<2**(k+1) and n<=h and n&1,'prefix range/parity')
            if j==r-1:
                need(n not in seen_exits,'exit reused')
                seen_exits.add(n)
            n=map_value(n,3)
            edge_count+=1
        need(n>h,'no final exit')
    need(edge_count==c['literal_edges'],'edge count mismatch')
    need(c['minimum_variation']==len(seeds)-1,'wrong certified lower bound')
    need(c['observed_variation']>=c['minimum_variation'],'reported lower bound failed')
    # Replay the whole selected coloring for the four smaller corridor graphs.
    full_replay = h<=30000
    if full_replay:
        comp=partition(h,3)
        labs=[comp[n] for n in seeds]
        need(len(set(labs))==len(labs) and comp[1] not in labs,'nonindependent roots')
        chosen=set(labs[1::2])
        bits=[int(n in chosen) for n in comp]
        v=sum(bits[n]!=bits[n+1] for n in range(2**k,2**(k+1)))
        need(v==c['observed_variation'],'corridor variation mismatch')
        need(hashlib.sha256(bytes(bits[1:])).hexdigest()==c['coloring_sha256'],'corridor color hash')
    return edge_count, int(full_replay)


def main():
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path('results.json')
    data=json.loads(path.read_text(encoding='utf-8'))
    checked_flows=sum(check_cut(c) for c in data['cut_certificates'])
    corridor_checks=[check_corridor(c) for c in data['corridors']]
    exemplar=next(c for c in data['cut_certificates']
                  if c['status']=='FINITE_SEPARATOR' and c['height']==256 and c['multiplier']==3)
    mutations=[]
    x=copy.deepcopy(exemplar); x['scaled_capacity']+=1; mutations.append((check_cut,x))
    x=copy.deepcopy(exemplar); x['flow'][0][2]+=1; mutations.append((check_cut,x))
    x=copy.deepcopy(exemplar); x['flow'].pop(); mutations.append((check_cut,x))
    x=copy.deepcopy(exemplar); x['flow'].append(x['flow'][0]); mutations.append((check_cut,x))
    x=copy.deepcopy(exemplar); x['ones'].append(1); mutations.append((check_cut,x))
    x=copy.deepcopy(exemplar); x['scale']+=1; mutations.append((check_cut,x))
    x=copy.deepcopy(exemplar); x['status']='MERGED_WITHIN_CUTOFF'; mutations.append((check_cut,x))
    x=copy.deepcopy(data['corridors'][0]); x['first_seed']+=2; mutations.append((check_corridor,x))
    x=copy.deepcopy(data['corridors'][0]); x['height']-=1; mutations.append((check_corridor,x))
    rejected=0
    for checker,c in mutations:
        try:
            checker(c)
        except (ValueError,KeyError,IndexError):
            rejected+=1
        else:
            raise ValueError('semantic mutation was accepted')
    summary=dict(status='PASS', cut_cases=len(data['cut_certificates']),
                 nonzero_flow_edges_checked=checked_flows,
                 corridor_cases=len(corridor_checks),
                 corridor_physical_edges=sum(x[0] for x in corridor_checks),
                 full_corridor_colorings_replayed=sum(x[1] for x in corridor_checks),
                 rejected_semantic_mutations=rejected)
    print(json.dumps(summary,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
