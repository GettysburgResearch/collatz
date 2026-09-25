#!/usr/bin/env python3
"""Standalone verifier: no authoring module, graph solver, or max-flow import.

Reconstructs the dyadic subdivision by rational interval recursion, physical
relations by graph traversal, and verifies an exact feasible flow against a cut.
All failures use explicit exceptions and remain active under Python -O/-OO.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from bisect import bisect_right
import argparse
import copy
import json
import hashlib

COUNTS=defaultdict(int)


def need(ok,msg):
    if not ok:
        raise ValueError(msg)


def integer(n,minimum=0):
    need(type(n) is int and n>=minimum,'integer schema')
    return n


def q(pair):
    need(type(pair) is list and len(pair)==2,'rational schema')
    need(type(pair[0]) is int,'rational numerator'); integer(pair[1],1)
    out=Fraction(*pair)
    need([out.numerator,out.denominator]==pair,'noncanonical rational')
    return out


def oddpart(n):
    integer(n,1)
    while n%2==0:
        n//=2
    return n


def T(n,p):
    return (p*n+1)//2 if n%2 else n//2


def ph(n):
    return Fraction(n,2**(n.bit_length()-1))-1


def endpoint(a):
    return oddpart((1+a).numerator)


def components(nodes,relations,pins):
    adjacent={n:set() for n in nodes}
    for a,b in relations:
        adjacent[a].add(b); adjacent[b].add(a)
    for color in (0,1):
        same=[oddpart(n) for n,c in pins if c==color]
        for a,b in zip(same,same[1:]):
            adjacent[a].add(b); adjacent[b].add(a)
    result={}
    for start in sorted(nodes):
        if start in result:
            continue
        stack=[start]; reached={start}
        while stack:
            a=stack.pop()
            for b in adjacent[a]:
                if b not in reached:
                    reached.add(b); stack.append(b)
        root=min(reached)
        result.update({n:root for n in reached})
    return result


def reconstruct(problem,horizon,L):
    p=problem['p']; integer(p,3); need(p in (3,5),'multiplier')
    N=integer(problem['N'],1)
    sources=problem['odd_sources']
    need(type(sources) is list and sources==sorted(set(sources)),'source inventory')
    for a in sources:
        integer(a,1); need(a%2==1,'odd source')
    pins=problem.get('pins',[[1,0],[N,1]])
    need(type(pins) is list,'pins schema')
    for item in pins:
        need(type(item) is list and len(item)==2,'pin pair')
        integer(item[0],1); integer(item[1]); need(item[1] in (0,1),'pin color')
    need([1,0] in pins and [N,1] in pins,'original pins')
    relations=[(a,oddpart(p*a+1)) for a in sources]
    marked={oddpart(n) for n,c in pins}|{x for e in relations for x in e}|{1}
    positions=sorted({ph(n) for n in marked if n!=1})
    K=max(n.bit_length()-1 for n in marked)
    if horizon is not None:
        integer(horizon); need(horizon>=K and L==horizon+1,'finite horizon')
    else:
        need(L>=K+2,'tail depth')
    weights=[Fraction(1,j*j) for j in range(1,L+1)]
    tails=[Fraction(0)]*(L+1)
    for d in range(L-1,-1,-1):
        tails[d]=tails[d+1]+weights[d]
    raw=set(); pieces=[]; leaves=[]
    stack=[(Fraction(0),Fraction(1),0,positions)]
    while stack:
        a,b,d,inside=stack.pop()
        u,v=endpoint(a),endpoint(b)
        raw.update((u,v))
        if inside:
            pieces.append((u,v,weights[d],weights[d]))
            mid=(a+b)/2
            stack.append((mid,b,d+1,[z for z in inside if mid<z<b]))
            stack.append((a,mid,d+1,[z for z in inside if a<z<mid]))
        else:
            if horizon is None:
                lo,hi=tails[d]+Fraction(1,L+1),tails[d]+Fraction(1,L)
            else:
                lo=hi=tails[d]
            pieces.append((u,v,lo,hi)); leaves.append((a,b,u,v))
    classes=components(raw,relations,pins)
    caps=defaultdict(lambda:[Fraction(0),Fraction(0)])
    for u,v,lo,hi in pieces:
        a,b=sorted((classes[u],classes[v]))
        if a!=b:
            caps[a,b][0]+=lo; caps[a,b][1]+=hi
    return raw,classes,dict(caps),sorted(leaves),K,marked


def verify_cut(c):
    need(c['schema']=='dyadic-repair-cut-v1','cut schema')
    L=integer(c['tail_terms'],1)
    raw,classes,caps,leaves,K,marked=reconstruct(c['problem'],c['horizon'],L)
    need(integer(c['max_phase_depth'])==K,'maximum phase depth')
    zero,one=classes[1],classes[oddpart(c['problem']['N'])]
    if zero==one:
        need(c['status']=='PINS_INFEASIBLE','missed pin collision')
        COUNTS['pin_infeasibilities']+=1
        return
    need(c['status']=='SEPARATOR','incorrect infeasibility')
    need(c['classes']==[[n,classes[n]] for n in sorted(raw)],'physical component classes')
    need(c['source_vertex']==one and c['sink_vertex']==zero,'network pins')
    colors={}
    for item in c['colors']:
        need(type(item) is list and len(item)==2,'color schema')
        a,b=item; integer(a,1); integer(b); need(b in (0,1) and a not in colors,'colors')
        colors[a]=b
    need(set(colors)==set(classes.values()),'color coverage')
    need(colors[zero]==0 and colors[one]==1,'wrong pin values')
    expected_ranges=[[[a.numerator,a.denominator],[b.numerator,b.denominator],colors[classes[u]]] for a,b,u,v in leaves]
    need(c['ranges']==expected_ranges,'subtree completion')
    expected_stats={'marked_phases':len(marked),'raw_vertices':len(raw),'quotient_vertices':len(colors),'terminal_intervals':len(leaves),'compressed_edges':len(caps)}
    need(c['stats']==expected_stats,'inventory statistics')
    seen=set(); balance=defaultdict(Fraction); cutlo=Fraction(0); cuthi=Fraction(0)
    for item in c['edges']:
        need(type(item) is list and len(item)==5,'flow edge schema')
        a,b=item[:2]; integer(a,1); integer(b,1)
        need(a<b and (a,b) in caps and (a,b) not in seen,'edge inventory')
        seen.add((a,b)); lo,hi,f=map(q,item[2:])
        need([lo,hi]==caps[a,b],'subtree capacity')
        need(abs(f)<=lo,'flow capacity exceeded')
        balance[a]+=f; balance[b]-=f
        if colors[a]!=colors[b]:
            cutlo+=lo; cuthi+=hi
        COUNTS['flow_edges']+=1
    need(seen==set(caps),'missing edge')
    lower,upper=q(c['lower']),q(c['upper'])
    need(lower==cutlo and upper==cuthi and lower<=upper,'cut value')
    for a in colors:
        expected=lower if a==one else -lower if a==zero else Fraction(0)
        need(balance[a]==expected,'flow conservation/optimality')
    COUNTS['cut_certificates']+=1
    COUNTS['dyadic_terminal_intervals']+=len(leaves)


def evaluator(c):
    ranges=c['ranges']; starts=[q(r[0]) for r in ranges]
    def value(n):
        return ranges[bisect_right(starts,ph(n))-1][2]
    return value


def verify_edge(c,e,root_fair=False):
    p=c['problem']['p']; n=integer(e['n'],1); target=integer(e['target'],1)
    need(n%2 and target==T(n,p),'nonphysical repair')
    need(n not in c['problem']['odd_sources'],'already retained repair')
    value=evaluator(c); observed=[value(n),value(target)]
    need(e['colors']==observed,'false repair colors')
    if e['kind']=='ROOT_FAIR_EDGE':
        need(root_fair,'fair edge outside its policy')
        have=set(c['problem']['odd_sources']); a=oddpart(c['problem']['N']); seen=set()
        while a in have and a!=1 and a not in seen:
            seen.add(a); a=oddpart(p*a+1)
        need(a==n and a not in have,'reset or changed root frontier')
    else:
        need(e['kind'] in ('MARKED_ODD_EDGE','ROTATION_INTERVAL'),'unknown defect type')
        need(observed[0]!=observed[1],'satisfied edge labeled a defect')
    K=c['max_phase_depth']; extra=(2*p+1).bit_length()
    need(n < 2**(K+extra+1),'defect exceeds proved size bound')
    if e['kind']=='MARKED_ODD_EDGE':
        need(n in {a for a,b in c['classes']},'unmarked source')
    if e['kind']=='ROTATION_INTERVAL':
        a,b=map(q,e['interval']); h=integer(e['shell'])
        need(h==K+extra and 1<=a<b<=2,'rotation interval')
        need(a*2**h<n and Fraction(n)+Fraction(1,p)<b*2**h,'interval margin')
    COUNTS['physical_repair_edges']+=1
    COUNTS[e['kind'].lower()]+=1


def verify_refinement(r):
    need(r['schema']=='dyadic-repair-refinement-v1','refinement schema')
    N=integer(r['N'],1); p=integer(r['p'],3); need(p in (3,5),'multiplier')
    cap=integer(r['round_cap']); policy=r['policy']; need(policy in ('root-fair','cuts-only'),'policy')
    sources=r['initial_sources'][:]
    need(sources==sorted(set(sources)),'initial inventory')
    need(1 in sources and (p==3 or 3 in sources),'known core cycle missing')
    records=r['records']; need(len(records)<=cap,'cap exceeded')
    for i,item in enumerate(records):
        c=item['cut']; verify_cut(c)
        need(c['problem']=={'p':p,'N':N,'odd_sources':sources},'original source/retained edges changed')
        fair=policy=='root-fair' and i%2==1
        need((item['edge']['kind']=='ROOT_FAIR_EDGE')==fair,'repair scheduling')
        verify_edge(c,item['edge'],fair)
        sources=sorted(sources+[item['edge']['n']])
    need(r['final_sources']==sources,'final relation inventory')
    if r['status']=='UNRESOLVED_AT_RESOURCE_CAP':
        need(len(records)==cap,'premature resource report')
        verify_cut(r['last_cut'])
        need(r['last_cut']['status']=='SEPARATOR' and r['last_cut']['problem']=={'p':p,'N':N,'odd_sources':sources},'incorrect final cut')
    else:
        path=r['path']; need(type(path) is list and path and path[0]==N,'original path')
        for a,b in zip(path,path[1:]):
            integer(a,1); integer(b,1)
            need(b==T(a,p) and (a%2==0 or a in sources),'physical path or source coverage')
        if r['status']=='CONVERGENCE':
            need(path[-1]==1,'convergence endpoint')
        else:
            need(r['status']=='VERIFIED_OTHER_CYCLE','unknown outcome')
            start=integer(r['cycle_start']); need(start<len(path)-1 and path[start]==path[-1],'cycle closure')
            need(1 not in path[start:-1],'core cycle mislabeled')
        COUNTS['physical_path_steps']+=len(path)-1
    COUNTS['refinements']+=1
    COUNTS[r['status'].lower()]+=1


def verify_file(data):
    schema=data['schema']
    if schema=='dyadic-repair-cut-v1':
        verify_cut(data)
    elif schema=='dyadic-repair-refinement-v1':
        verify_refinement(data)
    elif schema=='dyadic-repair-corpus-v1':
        for c in data['cuts']:
            verify_cut(c)
        for r in data['refinements']:
            verify_refinement(r)
    else:
        raise ValueError('unknown file schema')


def self_test(c):
    """Semantic mutations are run directly, not rejected just by a file hash."""
    need(c['status']=='SEPARATOR','self test needs a feasible cut')
    changes=[
        ('lower-value',lambda x:x.__setitem__('lower',[0,1])),
        ('upper-value',lambda x:x.__setitem__('upper',[0,1])),
        ('missing-edge',lambda x:x['edges'].pop()),
        ('flow',lambda x:x['edges'][0].__setitem__(4,[999999999,1])),
        ('capacity',lambda x:x['edges'][0].__setitem__(2,[0,1])),
        ('class',lambda x:x['classes'][0].__setitem__(1,999999)),
        ('color',lambda x:x['colors'][0].__setitem__(1,1-x['colors'][0][1])),
        ('completion',lambda x:x['ranges'][0].__setitem__(2,1-x['ranges'][0][2])),
        ('boolean-source',lambda x:x['problem'].__setitem__('N',True)),
        ('even-relation',lambda x:x['problem']['odd_sources'].append(2)),
        ('false-merged',lambda x:x.__setitem__('status','PINS_INFEASIBLE')),
        ('false-depth',lambda x:x.__setitem__('max_phase_depth',x['max_phase_depth']+1)),
    ]
    for name,change in changes:
        bad=copy.deepcopy(c); change(bad)
        try:
            verify_cut(bad)
        except (ValueError,KeyError,IndexError,TypeError):
            COUNTS['mutations_rejected']+=1
        else:
            raise ValueError('mutation accepted: '+name)


def verify_models(data,models,raw_bytes):
    need(models['schema']=='dyadic-repair-tests-v1','model schema')
    need(models['corpus_sha256']==hashlib.sha256(raw_bytes).hexdigest(),'model/corpus digest')
    expected={(p,K,bits) for p in (3,5) for K in (1,2,3) for bits in range(1,2**(2**K-1))}
    seen=set()
    for row in models['step_function_oracles']:
        p,K,bits=row['p'],row['K'],row['bits']; key=(p,K,bits)
        need(key in expected and key not in seen,'step-function inventory'); seen.add(key)
        e=row['edge']; n=integer(e['n'],1); target=integer(e['target'],1)
        need(n%2 and target==T(n,p),'grid oracle physical edge')
        def color(m):
            index=(m*2**K)//2**(m.bit_length()-1)-2**K
            return 0 if index==0 else (bits >> (index-1))&1
        need(color(n)!=color(target) and e['colors']==[color(n),color(target)],'grid oracle contrast')
        h=K+(2*p+1).bit_length()
        need(e['kind']=='ROTATION_INTERVAL' and e['shell']==h and 2**h<=n<2**(h+1),'grid oracle scale')
        a,b=map(q,e['interval'])
        need(1<=a<b<=2 and a*2**h<n and Fraction(n)+Fraction(1,p)<b*2**h,'grid oracle margin')
    need(seen==expected,'missing step function')
    COUNTS['exhaustive_oracle_checks']+=len(seen)
    need([r['K'] for r in models['dyadic_lookahead']]==list(range(2,9)),'lookahead inventory')
    for row in models['dyadic_lookahead']:
        K=row['K']; tail=sum((Fraction(1,j*j) for j in range(3,K+2)),Fraction(0))
        need(q(row['minimum'])==min(4*tail,Fraction(1,2)+2*tail),'lookahead minimum')
        need(q(row['pin_only'])==2*tail and row['b3']==int(K>=6),'lookahead coupling')
    COUNTS['lookahead_checks']+=7
    seen=set(); assignments=0; feasible=0
    index=0
    for p in (3,5):
        for K in (1,2,3,4):
            H=2**(K+1)
            candidates=list(range(1,(2*H-1)//p+1,2))
            for seed in range(16 if K<4 else 4):
                N=3+2*(seed%((H-2)//2))
                retained=[a for j,a in enumerate(candidates) if (17*seed+29*j+j*j)%7<3]
                c=data['cuts'][index]; row=models['dense_comparisons'][index]; index+=1
                need(c['problem']=={'p':p,'N':N,'odd_sources':retained} and c['horizon']==K,'dense problem inventory')
                need((row['p'],row['K'],row['seed'])==(p,K,seed),'dense model identity')
                need(row['minimum']==(c['lower'] if c['status']=='SEPARATOR' else None),'dense reported minimum')
                rays=set(range(1,H,2))
                classes=components(rays,[(a,oddpart(p*a+1)) for a in retained],[[1,0],[N,1]])
                assignments+=2**(len(rays)-2)
                if classes[1]!=classes[N]:
                    feasible+=2**(len(set(classes.values()))-2)
    need(len(models['dense_comparisons'])==index==104 and len(data['cuts'])==114,'cut corpus coverage')
    need(models['counts']['dense_assignments']==assignments and models['counts']['dense_feasible_assignments']==feasible,'enumeration totals')
    COUNTS['dense_inventory_checks']+=index
    extra=models['adaptive_rotation_controls']
    retained=[r for r in data['refinements'] if r['records']]
    need(len(extra)==len(retained),'adaptive oracle inventory')
    for row,r in zip(extra,retained):
        c=r['records'][-1]['cut']; e=row['edge']; value=evaluator(c)
        need(row['p']==r['p'] and row['N']==r['N'] and row['K']==c['max_phase_depth'],'adaptive oracle original source')
        n=integer(e['n'],1); t=integer(e['target'],1)
        need(n%2 and t==T(n,r['p']) and n not in c['problem']['odd_sources'],'adaptive oracle edge')
        need(value(n)!=value(t) and e['colors']==[value(n),value(t)],'adaptive oracle contrast')
        h=row['K']+(2*r['p']+1).bit_length(); a,b=map(q,e['interval'])
        need(e['kind']=='ROTATION_INTERVAL' and e['shell']==h and 2**h<=n<2**(h+1),'adaptive oracle scale')
        need(a*2**h<n and Fraction(n)+Fraction(1,r['p'])<b*2**h,'adaptive oracle margin')
    COUNTS['additional_rotation_controls']+=len(extra)


def no_duplicates(pairs):
    out={}
    for key,value in pairs:
        need(key not in out,'duplicate JSON key')
        out[key]=value
    return out


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file',type=Path)
    parser.add_argument('--self-test',action='store_true')
    parser.add_argument('--models',type=Path)
    args=parser.parse_args()
    data=json.loads(args.file.read_text(),object_pairs_hook=no_duplicates)
    verify_file(data)
    if args.models:
        models=json.loads(args.models.read_text(),object_pairs_hook=no_duplicates)
        verify_models(data,models,args.file.read_bytes())
    verified_counts=dict(COUNTS)
    if args.self_test:
        if data['schema']=='dyadic-repair-corpus-v1':
            sample=next(c for c in data['cuts'] if c['status']=='SEPARATOR')
        elif data['schema']=='dyadic-repair-refinement-v1':
            sample=data['records'][0]['cut']
        else:
            sample=data
        self_test(sample)
        verified_counts['mutations_rejected']=COUNTS['mutations_rejected']
    print(json.dumps({'status':'PASS','counts':verified_counts},sort_keys=True))

if __name__=='__main__':
    main()
