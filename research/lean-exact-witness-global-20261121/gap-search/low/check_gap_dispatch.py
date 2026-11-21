#!/usr/bin/env python3
"""Independent exact audit: no imports from either catalogue generator."""
import argparse
import json
from collections import Counter
from hashlib import sha256
from math import gcd
from pathlib import Path


def need(ok, what):
    if not ok:
        raise ValueError(what)


def step(node, move):
    a,b=node
    if move=='O':
        need(a%2==0 and b%2==1,'odd step guard')
        out=(3*a//2,(3*b+1)//2)
    elif move=='E':
        need(a%2==b%2==0,'even step guard')
        out=(a//2,b//2)
    elif move=='I':
        need(a%3==0 and (2*b-1)%3==0,'inverse step guard')
        out=(2*a//3,(2*b-1)//3)
        need(out[0]%2==0 and out[1]%2==1,'inverse odd parity')
    elif move=='D':out=(2*a,2*b)
    elif move=='M3':out=(3*a,3*b)
    elif move=='V3':
        need(a%3==b%3==0,'division query guard')
        out=(a//3,b//3)
    else:raise ValueError('unknown edge')
    need(min(out)>0,'positivity')
    return out


def complete_prefix(node):
    word=[]
    values=[node]
    while node[0]%2==0:
        if node[1]%2:
            word.append(1)
            node=step(node,'O')
        else:
            need(word,'nonempty child starts even')
            word[-1]+=1
            node=step(node,'E')
        values.append(node)
    return node,word,values


def domains(a,b,M):
    while a%2==b%2==0:a//=2;b//=2
    if a%2==0:
        d=gcd(a,M)
        return [h for h in range(1,M,2) if (h-b)%d==0]
    d=gcd(a,M)
    residues={1%d}
    two=2%d
    while two not in residues:
        residues.add(two)
        two=2*two%d
    return [h for h in range(1,M,2) if any((two*h-b)%d==0 for two in residues)]

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('input',type=Path,help='Frozen low-gap JSON catalogue')
parser.add_argument('--receipt',type=Path,help='Write the deterministic audit receipt')
args=parser.parse_args()
p=args.input
data=json.loads(p.read_text())
rows=data['rows'];polynomials={7:[],15:[]};counts=Counter()
for i,row in enumerate(rows):
    M,r,kind=row['M'],row['r'],row['p']
    need(M==288 and 0<r<M and r%2==1 and kind in ('F3','R3'),'root')
    parent=(M,r) if kind=='F3' else (3*M,3*r)
    desired=(3*M,3*r) if kind=='F3' else (M,r)
    endpoints=[];queries=[]
    for side,start in (('left',parent),('right',desired)):
        node=start
        for move,out in row[side]:
            old=node;node=step(node,move)
            need(tuple(out)==node,('wrong edge',i,move))
            if move in ('M3','V3'):
                base=old if move=='M3' else node
                forward=(side=='left')==(move=='M3')
                qkind='F3' if forward else 'R3'
                queries.append((qkind,base,old if side=='left' else node))
        endpoints.append(node)
    need(endpoints[0]==endpoints[1]==tuple(row['endpoint']),('join',i))
    if row.get('ordinary_merger'):
        need(not queries and not row['dependencies'],'ordinary merger uses query')
        counts['ordinary_mergers']+=1
        continue
    need(len(queries)==1,'one query')
    qkind,base,actual_known=queries[0]
    need(qkind==row['query_kind'] and base==tuple(row['query_base']),'query annotation')
    known=base if qkind=='F3' else tuple(3*x for x in base)
    need(known==actual_known,'query antecedent orientation')
    expected=[[qkind,h] for h in domains(*base,M)]
    need(expected==row['dependencies'],'exact query-domain mismatch')
    pe,old,pvalues=complete_prefix(parent)
    ce,new,cvalues=complete_prefix(known)
    need(pe==ce,'ordinary source endpoints differ')
    need(old==row['source_gap_prefix'] and new==row['child_gap_prefix'],'partial word annotation')
    need(old and row['shared_final_valuation'] is True,'source partial word')
    need(row['finite_entrance_parameters']==[0],'finite entrance scope')
    need(all(a+b>1 for a,b in pvalues+cvalues),'early hit in tail parameter at least one')
    for C in (7,15):
        A=C**old[-1]-(C**new[-1] if new else 0)
        B=sum(C**g for g in old[:-1])-sum(C**g for g in new[:-1])
        need(A>=0 and A+B>0,('all-delta polynomial',i,C,A,B))
        polynomials[C].append((A,B))
    counts['conditional_queries']+=1
    counts['query_'+qkind]+=1
    counts['empty_child_word']+=not new

receipt={
 'status':'PASS: independent exact low-gap row, query, and universal-energy replay',
 'input_sha256':sha256(p.read_bytes()).hexdigest(),
 'audited_rows':len(rows),
 'counts':dict(counts),
 'energy':{str(C):{'checked':len(polynomials[C]),
                   'minimum_coefficient':min(a for a,b in polynomials[C]),
                   'minimum_value_at_delta_zero':min(a+b for a,b in polynomials[C]),
                   'zero_coefficient_rows':sum(a==0 for a,b in polynomials[C])}
           for C in polynomials},
 'proof':'Difference = A*C**delta+B, A>=0 and A+B>0, so all integers delta>=0.',
 'scope':'No global or combined-catalogue coverage inference; parameter zero remains an explicit exception.'}
output=json.dumps(receipt,sort_keys=True,indent=2)+'\n'
if args.receipt:
    args.receipt.write_text(output)
print(output,end='')
