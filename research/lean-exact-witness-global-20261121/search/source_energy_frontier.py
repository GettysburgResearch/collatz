#!/usr/bin/env python3
"""Finite exhaustive one-query peak-energy matching on whole affine cells.

The bound is mathematical: a normalized child-source prefix that replaces a
removed parent prefix with smaller ordinary values cannot have any inserted
affine slope larger than the parent's forward-frontier slope peak. Inverse
nodes have slope g*2^h*3^j, so only finitely many such nodes exist.
"""
from collections import deque,Counter
import argparse,importlib.util,json
from pathlib import Path
from check_source_certificates import screen,coverage

import source_frontier as frontier

def bounded_inverse_tree(root,bound):
    todo=deque([(root,[])])
    while todo:
        node,path=todo.popleft()
        if node[0]>bound:continue
        yield node,path
        a,b=node
        candidates=[('D',(2*a,2*b))]
        if a%3==0 and (2*b-1)%3==0:candidates.append(('I',(2*a//3,(2*b-1)//3)))
        for move,nxt in candidates:
            if min(nxt)>0 and nxt[0]<=bound:
                if frontier.forward(nxt)[1]!=node:raise ValueError('inverse identity')
                todo.append((nxt,path+[[move,list(nxt)]]))

def search(kind,M,r):
    starts=((M,r),(3*M,3*r))
    if kind=='R3':starts=starts[::-1]
    sf,sp=frontier.frontier(starts[0]);tf,tp=frontier.frontier(starts[1])
    peak=max([starts[0][0]]+[a for move,(a,b) in sp])
    g=sf[0]
    while g%3==0:g//=3
    depth_bound=(peak//g).bit_length()-1
    records=[];nodes=0;raw_matches=0
    if sf==tf:
        row={'M':M,'r':r,'p':kind,'left':sp,'right':tp,'endpoint':list(sf),'bound':1000000,
             'origin':'ordinary-frontier equality'}
        record=screen({'id':f'{kind}:{r}:direct','row':row})
        if record is None:raise ValueError('direct matcher')
        records.append(record)
    for source,back in bounded_inverse_tree(sf,peak):
        nodes+=1
        if len(back)>depth_bound:raise ValueError('mathematical depth bound')
        if source[0]%2==source[1]%2==0:continue
        for childkind in ('F3','R3'):
            if childkind=='F3':desired=(3*source[0],3*source[1]);move='M3'
            else:
                if source[0]%3 or source[1]%3:continue
                desired=(source[0]//3,source[1]//3);move='V3'
            df,dp=frontier.frontier(desired)
            if df!=tf:continue
            raw_matches+=1
            row={'M':M,'r':r,'p':kind,'left':sp+back+[[move,list(desired)]],
                 'right':tp+frontier.invert_path(desired,dp),'endpoint':list(desired),
                 'bound':1000000,'origin':'complete bounded inverse frontier energy grammar'}
            record=screen({'id':f'{kind}:{r}:{childkind}:{source[0]}:{source[1]}','row':row})
            if record is not None and record.get('multiset_decrease',False):records.append(record)
    return records,{'kind':kind,'r':r,'frontier':list(sf),'slope_peak':peak,'three_free_core':g,
                    'inverse_depth_bound':depth_bound,'inverse_nodes':nodes,'raw_query_matches':raw_matches,
                    'accepted':len(records)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--M',type=int,default=1440);ap.add_argument('--out',required=True)
    ap.add_argument('--essential-only',action='store_true')
    a=ap.parse_args();records=[];stats=[]
    roots=[('R3',r) for r in range(9,a.M,18)] if a.essential_only else [(kind,r) for r in range(1,a.M,2) for kind in ('F3','R3')]
    for i,(kind,r) in enumerate(roots):
        found,s=search(kind,a.M,r);records+=found;stats.append(s)
        if (i+1)%120==0:print(json.dumps({'processed_roots':i+1,'accepted_rules':len(records)}),flush=True)
    represented={tuple(z['root']) for z in records};essential={('R3',r) for r in range(9,a.M,18)}
    max_inserted=max((len(z.get('rank_inserted',[])) for z in records),default=0)
    result={'status':'FINITE EXACT AFFINE ENERGY GRAMMAR; global closure not asserted','M':a.M,
      'root_count':len(roots),'classifications':dict(Counter(z['classification'] for z in records)),
      'states_with_candidate':len(represented),'essential_with_candidate':len(represented&essential),
      'essential_missing_initially':[list(x) for x in sorted(essential-represented)],
      'max_tail_parameter':max((z['tail_parameter'] for z in records),default=0),
      'max_inserted_length':max_inserted,'uniform_energy_base':max(2,max_inserted+1),
      'max_inverse_depth':max(s['inverse_depth_bound'] for s in stats),
      'total_inverse_nodes':sum(s['inverse_nodes'] for s in stats),
      'closure':coverage(records,a.M,'multiset'),'statistics':stats,'records':records}
    Path(a.out).write_text(json.dumps(result,separators=(',',':'))+'\n')
    summary={k:v for k,v in result.items() if k not in ('records','statistics','essential_missing_initially')}
    summary['closure']={k:v for k,v in result['closure'].items() if k not in ('active_states','missing_required')}
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
