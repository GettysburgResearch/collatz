#!/usr/bin/env python3
"""Adaptive exact-cell frontier for one-query strict-clock induction.

Only unresolved cells are binary split.  Query dependencies activate coarse
F3/R3 cells as needed.  A finite work checkpoint is not an impossibility result.
"""
import argparse
from collections import deque,Counter
import importlib.util
import json
from pathlib import Path
import time

import source_frontier as front


def dependencies(row,base):
    if row.get('ordinary_merger'):return []
    form=row['query_base_normalized']
    return [(row['query_kind'],r) for r in front.dependency.oddpart_residues(*form,base)]


def early_hit(row):
    if row.get('ordinary_merger'):return False
    # The only possible exceptional nonnegative parameter is zero, since every
    # affine form has a positive slope and intercept.
    source_value=row['r']*(3 if row['p']=='R3' else 1)
    ordinary=row['left'][:-1]
    return source_value==1 or any(z[1]==1 for move,z in ordinary)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--budget',type=int,default=10000)
    ap.add_argument('--out',required=True);ap.add_argument('--resume')
    args=ap.parse_args();base=1440
    if args.resume:
        old=json.loads(Path(args.resume).read_text())
        active={tuple(x) for x in old['active_coarse_states']}
        queue=deque(tuple(x) for x in old['unresolved_frontier'])
        leaves=old['resolved_leaves'];processed=old['processed'];splits=old['binary_splits']
    else:
        active={('R3',r) for r in range(9,base,18)}
        queue=deque((p,base,r) for p,r in sorted(active))
        leaves=[];processed=0;splits=0
    start=time.monotonic();stop=processed+args.budget
    while queue and processed<stop:
        kind,M,r=queue.popleft();processed+=1
        rows=front.search(kind,M,r)
        if rows:
            choices=[]
            for row in rows:
                deps=dependencies(row,base)
                choices.append((sum(d not in active for d in deps),len(deps),
                                -row['source_clock_consumed'],len(row['left'])+len(row['right']),row,deps))
            choices.sort(key=lambda x:x[:4]);_,_,_,_,row,deps=choices[0]
            row['dependencies_coarse']=[list(d) for d in deps]
            row['parameter_zero_early_hit']=early_hit(row)
            leaves.append(row)
            for dep in deps:
                if dep not in active:
                    active.add(dep);queue.append((dep[0],base,dep[1]))
        else:
            splits+=1
            queue.append((kind,2*M,r));queue.append((kind,2*M,r+M))
        if processed%10000==0:
            print(json.dumps(dict(processed=processed,leaves=len(leaves),unresolved=len(queue),
                active=len(active),max_bits=max(front.v2(m) for _,m,_ in queue) if queue else 0,
                seconds=round(time.monotonic()-start,3))),flush=True)
    summary=dict(processed=processed,resolved_leaves=len(leaves),unresolved_cells=len(queue),
        activated_coarse_states=len(active),binary_splits=splits,
        resolved_by_bits=dict(Counter(front.v2(row['M']) for row in leaves)),
        unresolved_by_bits=dict(Counter(front.v2(M) for p,M,r in queue)),
        parameter_zero_early_hit_leaves=sum(row['parameter_zero_early_hit'] for row in leaves),
        seconds=time.monotonic()-start)
    data=dict(status='FINITE EXACT UNRESOLVED FRONTIER; full source-clock induction NOT discharged' if queue
        else 'FINITE COMBINATORIAL COVER; early-hit checks and Lean replay STILL REQUIRED',
        base_modulus=base,processed=processed,binary_splits=splits,summary=summary,
        active_coarse_states=[list(x) for x in sorted(active)],resolved_leaves=leaves,
        unresolved_frontier=[list(x) for x in queue])
    Path(args.out).write_text(json.dumps(data));print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
