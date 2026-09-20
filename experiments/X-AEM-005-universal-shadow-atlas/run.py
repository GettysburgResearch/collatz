#!/usr/bin/env python3
"""Compile exact finite shadow classes and reproducible proposed research evidence."""
import argparse,itertools,json,sys
from pathlib import Path
from collections import Counter
from kernel import (encode,sha,gap,prefix_family,universal_entry,chart_step,T,trace,cert,
                    compile_atlas,indices,resonance,resonance_source,choose,integer,v2)
SCHEMA='collatz-aua-005-v1'
PARENT='7e996feb24cc5d8579d75b39e0b909ffc03b3bcb'
SHIFTS=list(range(-5,12));CAP=18

def bundle():
    atlas={d:compile_atlas(d,CAP) for d in SHIFTS}
    idx=indices(atlas)
    deltas=list(range(1,257))+[2**e-1 for e in [16,32,64,128,256]]+[2**e+1 for e in [16,32,64,128,256]]+[3**100+7]
    gaps=[]
    for d in deltas:
        g=gap(d)
        for t in [0,1,3]:
            y=g['r']+g['modulus']*t
            if trace(y+d,g['F'])[-1]!=trace(y,g['B'])[-1]:raise ValueError('gap replay')
        gaps.append(g)
    prefixes=[]
    for L in range(1,9):
        for w in itertools.product('01',repeat=L):
            w=''.join(w)
            if '1' in w:prefixes.append(prefix_family(w))
    for w in ['110'*50,'11110111000'*12,'1101001101011110001001'*4]:prefixes.append(prefix_family(w,2))
    families=[]
    for d in (1,3):
        minimum=(d+2)//2
        for k in sorted(set([minimum,minimum+1,6,24,36,80,200])):
            for s in [0,1,2,3,4,8,16,32,64,128]:
                for t in [0,1,3]:
                    u=resonance_source(k,d,s,t);row=resonance(k,u,d)
                    if not row or row['kind']!='resonance':raise ValueError('direct CRT guard')
                    if 2**(k+d)>5 and not 2**(k+d)*row['m']<row['n']:raise ValueError('strong compression')
                    strong=9**k>=2**(d+3)*8**k
                    if strong and row['min_forward']<=row['n']:raise ValueError('no descent theorem')
                    row['strong_bound']=strong;families.append(row)
    escapes=[]
    for k in [1,2,6,24,36,80,200]:
        for s in [2,3,4,8,16,32,64,128]:
            for t in [0,1]:
                e=s+3;M=2**(s+6);b0=5*pow(3**s,-1,8)%8
                u=(2**e*b0-1)*pow(3**(2*k-1),-1,M)%M
                eps=1 if k%2 else 2
                u+=M*((eps-u)*pow(M,-1,3)%3)+3*M*t
                row=resonance(k,u,1);v=9**(k-1)*u
                b=(3*v+1)//2**e;C=(3**s*b-1)//4
                if v%16!=5 or C%2!=1 or not row:raise ValueError('strict old-failure extension')
                row['old_H_parameter']=C;escapes.append(row)
    grid=[choose(k,u,idx,CAP) for k in range(1,7) for u in range(1,8192,2)]
    entries=[universal_entry(n) for n in range(2,8193)]
    chart_count=0
    for d in range(6):
        for b in range(-50,51):
            for y in range(1,35):
                x=3**d*y+b
                if x<1:continue
                e,c,z,flip=chart_step(d,b,y);pair=(3**e*z+c,z)
                if flip:pair=pair[::-1]
                if pair!=(T(x),T(y)):raise ValueError('chart mismatch')
                chart_count+=1
    examples=[resonance(1,37,1),resonance(36,5,3)]
    # Gap/rank guard failure and permanent synchronous phase countercontrols.
    controls={'wrong_gap_guard':{'delta':1,'y':1,'F':'100','B':'001'},
              'phase_pair':[2,1],'source_order_bad':{'n':3,'m':3},
              'entry_7':universal_entry(7),'finite_library':{'shifts':SHIFTS,'tail_steps':CAP}}
    full={'atlas':{str(d):obj for d,obj in atlas.items()},'gaps':gaps,'prefixes':prefixes,
          'families':families,'escapes':escapes,'grid':grid,'entries':entries,'controls':controls,'examples':examples}
    payload={'parent':PARENT,'config':{'shifts':SHIFTS,'tail_steps':CAP,'hard_return_stages':8,'grid_k':[1,6],'grid_odd_u_max':8191},
             'atlas':[atlas[d]['summary'] for d in SHIFTS],
             'gap_count':len(gaps),'gap_sha256':sha(gaps),'prefix_count':len(prefixes),'prefix_sha256':sha(prefixes),
             'family_count':len(families),'families_sha256':sha(families),
             'escape_count':len(escapes),'escape_sha256':sha(escapes),
             'strong_family_count':sum(r['strong_bound'] for r in families),
             'grid_counts':dict(Counter(r['status'] for r in grid)),'grid_sha256':sha(grid),
             'entry_counts':dict(Counter(r['type'] for r in entries)),'entry_sha256':sha(entries),
             'chart_checks':chart_count,'controls':controls,'examples':examples}
    return {'schema':SCHEMA,'payload':payload,'sha256':sha(payload)},full

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check',type=Path);ap.add_argument('--write',type=Path)
    ap.add_argument('--full',type=Path);ap.add_argument('--source',type=int);ap.add_argument('--gap',type=int)
    args=ap.parse_args()
    if args.gap is not None:print(json.dumps(gap(args.gap),indent=2));return
    if args.source is not None:
        n=integer(args.source,2);e=v2(n+5)
        if e>=3 and e%3==0:
            a={d:compile_atlas(d,CAP) for d in SHIFTS};out=choose(e//3,(n+5)//2**e,indices(a))
        else:out={'source':n,'entry':universal_entry(n),'status':'ENTRY_ONLY_NOT_SUCCESS'}
        print(json.dumps(out,indent=2));return
    env,full=bundle()
    if args.check and encode(json.loads(args.check.read_text()))!=encode(env):raise ValueError('canonical typed payload differs')
    if args.write:args.write.parent.mkdir(parents=True,exist_ok=True);args.write.write_text(json.dumps(env,indent=2,sort_keys=True)+'\n')
    if args.full:args.full.write_text(json.dumps(full,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'status':'PASS','sha256':env['sha256'],'grid':env['payload']['grid_counts'],
                      'families':env['payload']['family_count'],'rules':sum(v['rules'] for v in env['payload']['atlas']),
                      'points':sum(v['points'] for v in env['payload']['atlas'])},sort_keys=True))
if __name__=='__main__':main()
