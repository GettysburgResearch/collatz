#!/usr/bin/env python3
"""Deterministic model comparisons and retained finite experiments.

Imports the authoring code for generation, but dense comparison enumerates
Boolean assignments directly and never calls another flow solver. Run the
separate verify.py against the emitted corpus for independent reconstruction.
"""
from fractions import Fraction as Q
from math import lcm
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import run


def check(ok,message):
    if not ok:
        raise ValueError(message)


def dense(problem,K):
    H=1 << (K+1); rays=list(range(1,H,2))
    def op(n):
        while n%2==0:
            n//=2
        return n
    fixed={}
    for n,color in problem.get('pins',[[1,0],[problem['N'],1]]):
        n=op(n)
        if n in fixed and fixed[n]!=color:
            return None,0,0
        fixed[n]=color
    free=[n for n in rays if n not in fixed]
    scale=lcm(*range(1,K+2))**2
    energy_edges=[(op(n),op(n+1),scale//n.bit_length()**2) for n in range(1,H)]
    relations=[(n,op(problem['p']*n+1)) for n in problem['odd_sources']]
    best=None; feasible=0
    for bits in range(1 << len(free)):
        b=fixed|{n:(bits >> i)&1 for i,n in enumerate(free)}
        if any(b[a]!=b[z] for a,z in relations):
            continue
        feasible+=1
        value=sum(w for a,z,w in energy_edges if b[a]!=b[z])
        best=value if best is None else min(best,value)
    return (None if best is None else Q(best,scale)),1 << len(free),feasible


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus',type=Path,required=True)
    parser.add_argument('--summary',type=Path,required=True)
    args=parser.parse_args()
    cuts=[]; totals=Counter(); dense_rows=[]
    for p in (3,5):
        for K in (1,2,3,4):
            H=1 << (K+1)
            sources=list(range(1,(2*H-1)//p+1,2))
            samples=16 if K<4 else 4
            for seed in range(samples):
                N=3+2*(seed % ((H-2)//2))
                retained=[a for j,a in enumerate(sources) if (17*seed+29*j+j*j)%7<3]
                problem={'p':p,'N':N,'odd_sources':retained}
                cert=run.solve(problem,horizon=K)
                expected,trials,feasible=dense(problem,K)
                if expected is None:
                    check(cert['status']=='PINS_INFEASIBLE','dense infeasibility mismatch')
                else:
                    check(cert['status']=='SEPARATOR' and Q(*cert['lower'])==expected==Q(*cert['upper']),'dense cut mismatch')
                cuts.append(cert)
                totals['dense_problems']+=1; totals['dense_assignments']+=trials; totals['dense_feasible_assignments']+=feasible
                dense_rows.append({'p':p,'K':K,'seed':seed,'minimum':None if expected is None else run.enc(expected)})
    toy={'p':3,'N':5,'odd_sources':[],'pins':[[1,0],[5,1],[7,1]]}
    transition=[]
    for K in range(2,9):
        cert=run.solve(toy,horizon=K); cuts.append(cert)
        tail=sum((Q(1,j*j) for j in range(3,K+2)),Q(0))
        expected=min(4*tail,Q(1,2)+2*tail)
        check(Q(*cert['lower'])==expected,'dyadic lookahead example')
        labels=dict(cert['colors']); classes=dict(cert['classes'])
        check(labels[classes[3]]==int(K>=6),'lookahead switch')
        transition.append({'K':K,'b3':labels[classes[3]],'minimum':run.enc(expected),'pin_only':run.enc(2*tail)})
    infinite_toy=run.solve(toy); cuts.append(infinite_toy)
    check(dict(infinite_toy['colors'])[dict(infinite_toy['classes'])[3]]==1,'infinite lookahead')
    oracle_rows=[]
    for p in (3,5):
        for K in (1,2,3):
            cells=1 << K
            for bits in range(1,1 << (cells-1)):
                labels=[0]+[(bits >> j)&1 for j in range(cells-1)]
                c={'status':'SEPARATOR','problem':{'p':p},'max_phase_depth':K,
                    'ranges':[[run.enc(Q(j,cells)),run.enc(Q(j+1,cells)),labels[j]] for j in range(cells)]}
                e=run.defect(c,prefer_marked=False)
                def direct(n):
                    h=n.bit_length()-1
                    index=((n << K) >> h)-cells
                    return labels[index]
                check(e['n']%2 and e['target']==run.step(e['n'],p),'oracle physical edge')
                check(direct(e['n'])!=direct(e['target']),'oracle direct-grid contrast')
                check(e['n']<1 << (K+(2*p+1).bit_length()+1),'oracle size bound')
                oracle_rows.append({'p':p,'K':K,'bits':bits,'edge':e})
    totals['exhaustive_step_function_oracles']=len(oracle_rows)
    big=(1 << 512)+12345
    large=run.solve({'p':3,'N':big,'odd_sources':[]},horizon=520)
    check(large['stats']['raw_vertices']<=514,'sparse 512-bit tree size')
    cuts.append(large)
    large_inf=run.solve({'p':3,'N':big,'odd_sources':[big]},tail_terms=64)
    cuts.append(large_inf)
    settings=[(3,1,0,0,'root-fair'),(3,8,0,0,'root-fair'),(5,26,24,0,'root-fair'),(3,3,16,0,'root-fair'),(3,5,16,0,'root-fair'),(3,7,32,0,'root-fair'),
              (3,9,32,0,'root-fair'),(3,27,96,3,'root-fair'),(3,27,64,3,'cuts-only'),
              (3,97,96,0,'root-fair'),(3,871,48,0,'root-fair'),
              (5,13,24,0,'root-fair'),(5,17,24,0,'root-fair'),(5,13,16,0,'cuts-only')]
    refinements=[run.refine(N,p,cap,depth,policy=policy) for p,N,cap,depth,policy in settings]
    for r in refinements:
        totals[r['status'].lower()]+=1; totals['repair_rounds']+=len(r['records'])
    scoped_rotations=[]
    for r in refinements:
        if r['records']:
            c=r['records'][-1]['cut']
            e=run.defect(c,prefer_marked=False)
            scoped_rotations.append({'p':r['p'],'N':r['N'],'edge':e,'K':c['max_phase_depth']})
    corpus={'schema':'dyadic-repair-corpus-v1','cuts':cuts,'refinements':refinements}
    text=json.dumps(corpus,sort_keys=True,separators=(',',':'))+'\n'
    args.corpus.write_text(text)
    summary={'schema':'dyadic-repair-tests-v1','counts':dict(totals),
             'corpus_sha256':hashlib.sha256(text.encode()).hexdigest(),
             'dense_comparisons':dense_rows,'dyadic_lookahead':transition,
             'step_function_oracles':oracle_rows,'adaptive_rotation_controls':scoped_rotations,
             'large_case':{'source_bits':big.bit_length(),'symbolic_height_exponent':521,'stats':large['stats'],'infinite_case_stats':large_inf['stats']},
             'refinements':[{'p':r['p'],'N':r['N'],'policy':r['policy'],'cap':r['round_cap'],'outcome':r['status'],'repairs':len(r['records']),'path_steps':len(r['path'])-1 if 'path' in r else None,'max_phase_depth':max((z['cut']['max_phase_depth'] for z in r['records']),default=0)} for r in refinements]}
    args.summary.write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':'PASS','counts':dict(totals),'corpus_sha256':summary['corpus_sha256'],'large_case':summary['large_case']},sort_keys=True))

if __name__=='__main__':
    main()
