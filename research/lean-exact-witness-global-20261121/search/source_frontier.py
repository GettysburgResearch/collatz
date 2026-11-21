#!/usr/bin/env python3
"""Complete single-query positive-clock matching for fixed affine root cells.

Completeness is for the stated D/E/O/I affine grammar and F3/R3 queries, after
common dyadic normalization. It is not completeness for arbitrary witnesses.
"""
from collections import deque, Counter
import argparse
import importlib.util
import json
from pathlib import Path

import check_source_certificates as dependency

def ordinary_neighbors(node):
    a,b=node
    yield 'D',(2*a,2*b)
    if a%2==0:
        yield ('E',(a//2,b//2)) if b%2==0 else ('O',(3*a//2,(3*b+1)//2))
    if a%3==0 and (2*b-1)%3==0:
        yield 'I',(2*a//3,(2*b-1)//3)



def v2(n):return (n & -n).bit_length()-1


def forward(node):
    a,b=node
    if a%2:raise ValueError('odd-slope frontier has no uniform next step')
    return ('E',(a//2,b//2)) if b%2==0 else ('O',(3*a//2,(3*b+1)//2))


def frontier(node):
    path=[]
    while node[0]%2==0:
        move,node=forward(node)
        path.append([move,list(node)])
    return node,path


def invert_path(start,path):
    nodes=[start]+[tuple(step[1]) for step in path]
    inverse={'O':'I','E':'D'}
    return [[inverse[path[i][0]],list(nodes[i])] for i in range(len(path)-1,-1,-1)]


def backward_layers(root,maxdepth):
    queue=deque([(root,[])])
    while queue:
        node,path=queue.popleft()
        yield node,path
        if len(path)==maxdepth:continue
        for move,nxt in ordinary_neighbors(node):
            if move not in ('D','I') or min(nxt)<=0:continue
            # D and I are the exact two possible ordinary predecessors.
            f,z=forward(nxt)
            if z!=node:raise ValueError('predecessor check')
            queue.append((nxt,path+[[move,list(nxt)]]))


def search(kind,M,r,allow_zero=False):
    starts=((M,r),(3*M,3*r))
    if kind=='R3':starts=starts[::-1]
    sf,sp=frontier(starts[0]);tf,tp=frontier(starts[1])
    height=v2(M);rows=[]
    if sf==tf:
        row=dict(M=M,r=r,p=kind,left=sp,right=tp,endpoint=list(sf),bound=1000000,
                 source_clock_consumed=0,query_kind=None,ordinary_merger=True,
                 origin='ordinary-frontier equality: no conditional query')
        if dependency.queries_and_verify(row):raise ValueError('merger unexpectedly queries')
        rows.append(row)
    for source,back in backward_layers(sf,height if allow_zero else height-1):
        # Common dyadic factors should already have been stripped at the query.
        if source[0]%2==source[1]%2==0:continue
        consumed=height-len(back)
        for querykind in ('F3','R3'):
            if querykind=='F3':
                desired=(3*source[0],3*source[1]);u=source;move='M3'
            else:
                if source[0]%3 or source[1]%3:continue
                desired=(source[0]//3,source[1]//3);u=desired;move='V3'
            df,dp=frontier(desired)
            if df!=tf:continue
            left=sp+back+[[move,list(desired)]]
            right=tp+invert_path(desired,dp)
            row=dict(M=M,r=r,p=kind,left=left,right=right,endpoint=list(desired),bound=1000000,
                source_clock_consumed=consumed,query_kind=querykind,
                query_base_normalized=list(u),query_source_normalized=list(source),
                query_common_halvings=0,source_prefix_clock=consumed,
                origin='complete ordinary-frontier matcher for normalized one-query clock descent')
            queries=dependency.queries_and_verify(row)
            if len(queries)!=1 or queries[0]['kind']!=querykind:raise ValueError('query extraction')
            if consumed!=sum(1 if m in ('E','O') else -1 for m,z in left[:-1]):
                raise ValueError('clock mismatch')
            rows.append(row)
    return rows


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--M',type=int,default=1440)
    ap.add_argument('--out',required=True);ap.add_argument('--allow-zero',action='store_true')
    args=ap.parse_args();rows=[]
    for r in range(1,args.M,2):
        # The r=1 cell starts at its least positive representative. A source
        # terminal exception, if any, is not discharged by this algebraic file.
        for kind in ('F3','R3'):
            rows.extend(search(kind,args.M,r,args.allow_zero))
    grouped={(row['p'],row['r']) for row in rows}
    essential={('R3',r) for r in range(9,args.M,18)}
    summary=dict(candidate_count=len(rows),states_with_candidate=len(grouped),
        by_kind=dict(Counter(p for p,r in grouped)),
        essential_present=sorted(r for p,r in grouped&essential),
        essential_missing=sorted(r for p,r in essential-grouped))
    data=dict(status='EXACT AFFINE SINGLE-QUERY CLOCK CANDIDATES; no universal closure claimed',
              M=args.M,L=144,weights={p:[1]*144 for p in dependency.TYPES},
              allow_zero=args.allow_zero,summary=summary,rows=rows)
    Path(args.out).write_text(json.dumps(data));print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
