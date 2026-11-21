#!/usr/bin/env python3
"""Search a complete all-positive-source affine-type rank by residues.

Every source residue, odd AND even, is included.  Thus no unproved
monotonicity of residue weights under halving is needed.
"""
from search_affine_types import search,TYPES
from collections import Counter
import argparse,json,random,time

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--modulus',type=int,default=1440)
    ap.add_argument('--residues',type=int,default=2)
    ap.add_argument('--weights',default='3:128,psi:64')
    ap.add_argument('--steps',type=int,default=300)
    ap.add_argument('--seed',type=int,default=616)
    ap.add_argument('--initial')
    ap.add_argument('--output',required=True)
    args=ap.parse_args();random.seed(args.seed);start=time.monotonic()
    state={q:[int(v)]*args.residues for q,v in (t.split(':') for t in args.weights.split(','))}
    if args.initial:
        old=json.load(open(args.initial))['weights']
        state={q:[v[r%len(v)] for r in range(args.residues)] for q,v in old.items()}
    kinds=list(state)
    cells=[(args.modulus,r if r>1 else args.modulus+1,p) for p in kinds for r in range(1,args.modulus+1)]
    seen={};best=-1;current=-1
    for i in range(args.steps):
        w={q:state[q][:] for q in kinds}
        if i>0:
            q=random.choice(kinds);r=random.randrange(args.residues)
            w[q][r]=max(1,min(16384,round(w[q][r]*random.choice((.5,.625,.75,.8,1.25,4/3,1.6,2)))))
        key=tuple(v for q in kinds for v in w[q])
        if key in seen:continue
        rows=[search(M,r,p,w,rank_modulus=args.residues) for M,r,p in cells]
        score=sum(not row.get('unresolved',False) for row in rows);seen[key]=score
        if score>=current or random.random()<.01:state=w;current=score
        if score>=best:
            improved=score>best;best=score
            result={'step':i,'solved':score,'total':len(cells),'weights':w,
                    'solved_by_kind':dict(Counter(row['kind'] for row in rows if not row.get('unresolved',False))),
                    'unresolved_by_kind':dict(Counter(row['kind'] for row in rows if row.get('unresolved',False))),
                    'seconds':time.monotonic()-start}
            if improved:print(json.dumps(result),flush=True)
            with open(args.output,'w') as f:json.dump({'status':'COMPLETE COVER; REQUIRES INDEPENDENT CHECK' if best==len(cells) else 'SEARCH ONLY; INCOMPLETE',
                'modulus':args.modulus,'rank_modulus':args.residues,'weights':w,
                'types':{q:TYPES[q] for q in kinds},'all_positive_source_residues':True,'summary':result,'rows':rows},f,indent=2)
        if best==len(cells):break

if __name__=='__main__':main()
