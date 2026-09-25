#!/usr/bin/env python3
"""Standalone completion/cut/flow checker. Imports no generator or flow solver.

Rebuilds the compressed graph by rational interval bisection, not a binary trie.
Replays every active-set round and exhaustively checks its finite-height oracle.
Certificates give upper and lower witnesses. No extrapolation to all odd edges.
"""
from __future__ import annotations
import argparse
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def need(test, message):
    if not test:
        raise ValueError(message)


def integer(n, minimum=0):
    need(type(n) is int and n >= minimum, 'invalid integer')
    return n


def core(n):
    integer(n,1)
    while n % 2 == 0:
        n //= 2
    return n


def image(n,p):
    return (p*n+1)//2 if n % 2 else n//2


def rat(row):
    need(type(row) is list and len(row)==2 and all(type(s) is str for s in row),'rational schema')
    a,b=map(int,row)
    need(b>0 and row==[str(a),str(b)],'rational encoding')
    value=Q(a,b)
    need(value.numerator==a and value.denominator==b,'noncanonical rational')
    return value


def number(row):
    need(type(row) is list and len(row)==3,'symbolic schema')
    need(type(row[0]) is int,'coefficient type')
    return row[0],rat(row[1:])


def plus(x,y):
    return x[0]+y[0],x[1]+y[1]


def minus(x,y):
    return x[0]-y[0],x[1]-y[1]


ZERO=(0,Q(0))


def enclosure(j):
    integer(j,1)
    need(j<=2048,'enclosure resource cap')
    h=s=Q(0)
    for i in range(j):
        h+=Q(1,i+1)
        s+=h/Q((i+1)*2**i)
    return s,s+Q(1,2**(j-1))


def nonnegative(x,low,high):
    if x==ZERO:
        return True
    return x[0]*(low if x[0]>=0 else high)+x[1]>=0


def rebuild(row):
    p=integer(row['multiplier'])
    need(p in (3,5),'unsupported map')
    source=integer(row['source'],2)
    k=row['horizon']
    if k is not None:
        integer(k)
    selected=row['odd_edges']
    need(type(selected) is list and selected==sorted(set(selected)),'noncanonical odd edges')
    for n in selected:
        integer(n,1)
        need(n%2==1,'even edge in odd list')
    need(1 in selected and (p!=5 or 3 in selected),'core edges missing')
    if k is not None:
        limit=2**(k+1)
        need(source<=limit and all(max(n,image(n,p))<=limit for n in selected),'physical cutoff exceeded')
    marks={Q(1),Q(2)}
    for n in [source]+selected+[image(n,p) for n in selected]:
        r=core(n)
        marks.add(Q(r,2**(r.bit_length()-1)))
    points=sorted(marks)
    depth=max((x.denominator.bit_length()-1 for x in points),default=0)
    h=[Q(0)]
    for i in range(1,max(depth,0 if k is None else k+1)+1):
        h.append(h[-1]+Q(1,i*i))
    vertices={1}
    raw=defaultdict(lambda:ZERO)
    leaves=[]
    todo=[(Q(1),Q(2),0)]
    while todo:
        a,b,d=todo.pop()
        left,right=core(a.numerator),core(b.numerator)
        vertices.update((left,right))
        inner=bisect_left(points,b)>bisect_right(points,a)
        if inner:
            cap=(0,Q(1,(d+1)**2))
            mid=(a+b)/2
            todo.extend(((a,mid,d+1),(mid,b,d+1)))
        else:
            cap=(1,-h[d]) if k is None else (0,h[k+1]-h[d])
            leaves.append((a,b,left,right))
        if left!=right and cap!=ZERO:
            key=tuple(sorted((left,right)))
            raw[key]=plus(raw[key],cap)
    # Equality components by independent graph traversal rather than union-find.
    adjacency={v:set() for v in vertices}
    for n in selected:
        t=core(image(n,p))
        need(n in vertices and t in vertices,'lost physical mark')
        adjacency[n].add(t)
        adjacency[t].add(n)
    labels={}
    for start in sorted(vertices):
        if start in labels:
            continue
        group={start};todo=[start]
        while todo:
            for v in adjacency[todo.pop()]:
                if v not in group:
                    group.add(v);todo.append(v)
        for v in group:
            labels[v]=min(group)
    graph=defaultdict(lambda:ZERO)
    for (u,v),cap in raw.items():
        u,v=labels[u],labels[v]
        if u!=v:
            key=tuple(sorted((u,v)))
            graph[key]=plus(graph[key],cap)
    for key,value in (('compressed_vertices',len(vertices)),('compressed_edges',len(raw)),
                      ('quotient_vertices',len(set(labels.values())))):
        need(type(row[key]) is int and row[key]==value,'incorrect structural count')
    leaves.sort()
    return p,source,k,selected,vertices,labels,graph,leaves


def verify(row):
    common={'schema','multiplier','source','horizon','odd_edges','compressed_vertices',
            'compressed_edges','quotient_vertices','status'}
    need(type(row) is dict and row.get('schema')=='dyadic-completion-v1','certificate schema')
    status=row['status']
    extra={'path'} if status=='CONVERGENCE' else {'value','ones','flow','zeta_terms','zeta_interval'}
    need(set(row)==common|extra,'unknown or missing certificate fields')
    p,source,k,selected,vertices,labels,graph,leaves=rebuild(row)
    if status=='CONVERGENCE':
        need(labels[core(source)]==labels[1],'pins not connected')
        path=row['path']
        need(type(path) is list and path and path[0]==source and path[-1]==1,'path endpoints')
        need(len(set(path))==len(path),'path repeats')
        for n in path:
            integer(n,1)
            if k is not None:
                need(n<=2**(k+1),'path escapes horizon')
        for n,t in zip(path,path[1:]):
            need(t==image(n,p) and (n%2==0 or n in selected),'illegal path')
        return dict(status=status,flow_edges=0,physical_edges=len(path)-1),None
    need(status=='OPTIMAL_COMPLETION','unknown status')
    low,high=enclosure(row['zeta_terms'])
    need(type(row['zeta_interval']) is list and len(row['zeta_interval'])==2,'enclosure schema')
    need((rat(row['zeta_interval'][0]),rat(row['zeta_interval'][1]))==(low,high),'enclosure mismatch')
    ones=row['ones']
    need(type(ones) is list and ones==sorted(set(ones)) and all(type(x) is int for x in ones),'cut side schema')
    ones=set(ones)
    need(ones<=set(labels.values()),'unknown component')
    need(labels[1] not in ones and labels[core(source)] in ones,'incorrect pins')
    value=number(row['value'])
    need(nonnegative(value,low,high),'negative objective')
    cut=ZERO
    for (u,v),cap in graph.items():
        need(nonnegative(cap,low,high),'negative capacity')
        if (u in ones)!=(v in ones):
            cut=plus(cut,cap)
    need(value==cut,'primal value mismatch')
    flows=row['flow']
    need(type(flows) is list,'flow list required')
    balance=defaultdict(lambda:ZERO)
    seen=[]
    for entry in flows:
        need(type(entry) is list and len(entry)==3,'flow entry schema')
        u,v=entry[:2]
        integer(u,1);integer(v,1)
        edge=(u,v)
        need(u<v and edge in graph,'unknown oriented flow edge')
        f=number(entry[2])
        need(f!=ZERO,'zero flow must be omitted')
        need(nonnegative(minus(graph[edge],f),low,high) and nonnegative(plus(graph[edge],f),low,high),'flow capacity exceeded')
        seen.append(edge)
        balance[u]=plus(balance[u],f)
        balance[v]=minus(balance[v],f)
    need(seen==sorted(set(seen)),'duplicate/unordered flow')
    for v in set(labels.values()):
        expected=value if v==labels[core(source)] else (minus(ZERO,value) if v==labels[1] else ZERO)
        need(balance[v]==expected,'flow conservation failure')
    stops=[a for a,_,_,_ in leaves]
    def color(n):
        r=core(n)
        if r in vertices:
            return int(labels[r] in ones)
        u=Q(r,2**(r.bit_length()-1))
        i=bisect_right(stops,u)-1
        a,b,left,_=leaves[i]
        need(a<u<b,'extension interval inconsistency')
        return int(labels[left] in ones)
    need(color(source)==1 and color(1)==0,'extension pins')
    for n in selected:
        need(color(n)==color(image(n,p)),'extension violates retained odd edge')
    return dict(status=status,flow_edges=len(flows),physical_edges=len(selected)),color


def verify_refinement(row):
    need(set(row)=={'source','multiplier','horizon','status','history','certificate'},'refinement schema')
    p=row['multiplier'];source=row['source'];k=row['horizon']
    integer(k);need(k<=16,'finite-oracle verifier resource cap')
    all_edges=[n for n in range(1,2**(k+1)+1,2) if image(n,p)<=2**(k+1)]
    expected={1} if p==3 else {1,3}
    previous=ZERO
    calls=flow_edges=0
    last_status=None
    for i,stage in enumerate(row['history']):
        calls+=1
        cert=stage['certificate']
        need(cert['source']==source and cert['multiplier']==p and cert['horizon']==k,'round changes problem')
        need(cert['odd_edges']==sorted(expected),'round constraint set mismatch')
        result,color=verify(cert)
        flow_edges+=result['flow_edges']
        need(stage['round']==i and type(stage['round']) is int and stage['retained']==len(expected),'round counters')
        if result['status']=='CONVERGENCE':
            need(set(stage)=={'round','retained','status','certificate'} and stage['status']=='CONVERGENCE','convergence round schema')
            last_status='CONVERGENCE'
            need(i==len(row['history'])-1,'continued after convergence')
        else:
            need(set(stage)=={'round','retained','status','value','violations','certificate'},'optimal round schema')
            need(stage['status']=='OPTIMAL_RELAXATION' and stage['value']==cert['value'],'round value mismatch')
            value=number(cert['value'])
            need(value[0]==0 and value[1]>=previous[1],'nonmonotone finite optimum')
            previous=value
            defects=[n for n in all_edges if color(n)!=color(image(n,p))]
            need(type(stage['violations']) is int and stage['violations']==len(defects),'defect census mismatch')
            last_status='FULL_FINITE_OPTIMUM' if not defects else 'UNRESOLVED_AT_ROUND_CAP'
            expected.update(defects)
    need(row['history'] and row['certificate']==row['history'][-1]['certificate'],'final certificate mismatch')
    need(row['status']==last_status,'incorrect refinement termination label')
    return calls,flow_edges


def mutation_tests(data):
    good=next(r for r in data['certificates'] if r['status']=='OPTIMAL_COMPLETION' and r['horizon'] is None and r['flow'])
    tests=[]
    def add(change):
        x=deepcopy(good);change(x);tests.append(x)
    add(lambda x:x.update(source=True))
    add(lambda x:x.update(multiplier=7))
    add(lambda x:x.update(horizon=-1))
    add(lambda x:x['odd_edges'].append(x['odd_edges'][-1]))
    add(lambda x:x['odd_edges'].remove(1))
    add(lambda x:x.update(ones=[]))
    add(lambda x:x.update(value=[x['value'][0]+1,*x['value'][1:]]))
    add(lambda x:x['zeta_interval'][0].__setitem__(0,'0'))
    add(lambda x:x.update(compressed_vertices=x['compressed_vertices']+1))
    add(lambda x:x['flow'].append(deepcopy(x['flow'][0])))
    add(lambda x:x['flow'][0][2].__setitem__(0,x['flow'][0][2][0]+1))
    add(lambda x:x.update(unproved_global_invariance=True))
    add(lambda x:x['ones'].append(10**20+1))
    add(lambda x:x.update(zeta_terms=0))
    add(lambda x:x.update(horizon=0))
    for x in tests:
        try:
            verify(x)
        except (ValueError,KeyError,TypeError):
            continue
        raise ValueError('mutation accepted')
    c=deepcopy(next(r for r in data['certificates'] if r['status']=='CONVERGENCE'))
    c['path'][1]+=1
    try:
        verify(c)
    except ValueError:
        pass
    else:
        raise ValueError('bad merger accepted')
    r=deepcopy(data['refinements'][0]);r['history'][0]['violations']+=1
    try:
        verify_refinement(r)
    except ValueError:
        pass
    else:
        raise ValueError('bad finite oracle accepted')
    return len(tests)+2


def strict_object(pairs):
    result={}
    for key,value in pairs:
        need(key not in result,'duplicate JSON key')
        result[key]=value
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    raw=args.input.read_bytes()
    data=json.loads(raw,object_pairs_hook=strict_object)
    need(set(data)=={'schema','certificates','refinements'} and data['schema']=='dyadic-completion-corpus-v1','corpus schema')
    totals=dict(certificates=0,flow_edges=0,physical_edges=0,refinement_rounds=0,refinement_flow_edges=0)
    for row in data['certificates']:
        result,_=verify(row)
        totals['certificates']+=1
        totals['flow_edges']+=result['flow_edges']
        totals['physical_edges']+=result['physical_edges']
    for row in data['refinements']:
        a,b=verify_refinement(row)
        totals['refinement_rounds']+=a
        totals['refinement_flow_edges']+=b
    totals['mutations_rejected']=mutation_tests(data) if args.self_test else 0
    totals.update(status='PASS',sha256=sha256(raw).hexdigest())
    print(json.dumps(totals,sort_keys=True))


if __name__=='__main__':
    main()
