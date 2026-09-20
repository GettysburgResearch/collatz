#!/usr/bin/env python3
"""Independent finite witness verifier. No generator/repository imports.
It checks whole cylinders and actual original arms, not OUTSIDE semantics or an all-n theorem.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path


def require(ok, message):
    if not ok: raise ValueError(message)


def integer(x,minimum=None):
    require(type(x) is int and (minimum is None or x>=minimum),'integer field')
    return x


def word(w):
    require(type(w) is str and set(w)<={'0','1'},'word syntax')
    return w


def orbit(x,w):
    for bit in word(w):
        require(x%2==int(bit),'literal parity')
        x=(3*x+1)//2 if x%2 else x//2
    return x


def affine(P,Q,w):
    for bit in word(w):
        require(P%2==0 and Q%2==int(bit),'uniform affine parity')
        P,Q=(3*P//2,(3*Q+1)//2) if bit=='1' else (P//2,Q//2)
    return [P,Q]


def two_words(row):
    require(type(row.get('words')) is list and len(row['words'])==2,'two words')
    return [word(x) for x in row['words']]


def endpoint_pair(row,result):
    E=row.get('endpoint');require(type(E) is list and len(E)==2,'affine endpoint')
    for x in E:integer(x,1)
    require(E==result,'affine endpoint equality')


def check(row):
    require(type(row) is dict,'row object')
    kind=row.get('kind')
    if kind=='gap':
        g=integer(row['g'],1);M=integer(row['M'],2);B=integer(row['B'],1);w,z=two_words(row)
        require(row['mode'] in ('long','old','long_alt'),'mode')
        require(0<B<M and M==2**len(w) and len(w)==len(z),'gap cylinder')
        require(w.count('1')==z.count('1'),'balanced odd counts')
        E=affine(M,B,w);require(E==affine(M,B+g,z),'gap equality');endpoint_pair(row,E)
        if row['mode']=='long':require(g==1 or M**4<=16**4*(g-1)**9,'rational bound consequence')
    elif kind=='shadow':
        a=integer(row['a'],1);b=integer(row['b']);k=integer(row['k'],0);seed=integer(row['seed'],1)
        require(seed in (1,3),'seed')
        L=integer(row['L'],1);h=integer(row['h'],2);d=integer(row['d'],1);P=integer(row['period'],2)
        W,Z=two_words(row);pre=row['prefixes'];require(type(pre) is list and len(pre)==2,'prefixes')
        w,z=[word(x) for x in pre];e=k+(2 if seed==3 else 0);c=3**a*seed*2**k-b
        require(c>2**(a+e) and 3**a*d+b>0,'positive/negative guards')
        require(len(w)==len(z)==L and w.count('0')==a+e and w[-1]=='0','first even stopping')
        require(orbit(-c,w)==-h and orbit(-seed*2**k,z)==-1,'signed prefixes')
        require(L>=k+(3 if seed==3 else 0),'preperiod length')
        expected='0'*k+'100'+'1'*(L-k-3) if seed==3 else '0'*k+'1'*(L-k)
        require(z==expected and z.count('1')-w.count('1')==a,'lower seed/balance')
        require((d+seed*2**k)%2**L==0 and d%2**(k+1)==2**k,'exact source/valuation')
        require(W.startswith(w) and Z.startswith(z) and len(W)==len(Z) and P==2**len(W),'full words')
        E=affine(3**a*P,3**a*d+b,W);require(E==affine(P,d,Z),'shadow cylinder');endpoint_pair(row,E)
    elif kind=='comparison':
        C=integer(row['C'],1);require(row['status'] in ('MERGE','OUTSIDE','BUDGET'),'status')
        if row['status']!='MERGE':return
        w,z=two_words(row);endpoint=integer(row['endpoint'],1)
        require(len(w)==len(z),'comparison clocks')
        require(orbit(9*C+2,w)==orbit(C,z)==endpoint,'original comparison merger')
        P=2**len(w)
        require(affine(9*P,9*C+2,w)==affine(P,C,z),'whole comparison cylinder')
    elif kind=='lift':
        k=integer(row['k'],0);r=integer(row['r'],2);u=integer(row['u'],1)
        n=integer(row['n'],1);m=integer(row['m'],1);C=integer(row['C'],1)
        require(u%2==1 and n==2**r*u-1 and m==(n-3)//4 and 4*m<n and n%3==0,'original roots')
        require(4*C+1==3**(r-1)*u and C%2**(k+1)==2**k,'H entrance')
        w,z=two_words(row);endpoint=integer(row['endpoint'],1)
        require(len(w)==len(z)+2 and orbit(n,w)==orbit(m,z)==endpoint,'lift clocks/endpoint')
        x=n;low=None
        for bit in w:
            require(x%2==int(bit),'lift parity')
            x=(3*x+1)//2 if x%2 else x//2
            low=x if low is None else min(low,x)
        require(low==integer(row['minimum'],1) and low>n,'entire no-descent arm')
    elif kind=='meeting_type':
        C=integer(row['C'],1);w,z=two_words(row);y=integer(row['endpoint'],1)
        require(len(w)==len(z) and orbit(9*C+2,w)==orbit(C,z)==y,'meeting')
        x,v=9*C+2,C
        for p,q in zip(w,z):
            require(x!=v,'not the first meeting')
            x=(3*x+1)//2 if x%2 else x//2;v=(3*v+1)//2 if v%2 else v//2
        expected='ROBUST' if z.count('1')-w.count('1')==2 else 'ISOLATED_ONLY'
        require(row['type']==expected,'permanent coefficient classification')
    elif kind=='neighborhood':
        C=integer(row['isolated_C'],1);P=integer(row['prefix_length'],1)
        B=integer(row['B'],1);M=integer(row['M'],2);w,z=two_words(row)
        require(B>C and (B-C)%2**P==0 and (B-C)%M!=0,'nearby but excluding base point')
        require(M==2**len(w) and len(w)==len(z) and P<len(w),'neighborhood length')
        require(orbit(9*C+2,w[:P])==orbit(C,z[:P]),'common point prefix')
        require(z[:P].count('1')-w[:P].count('1')!=2,'base point isolated')
        E=affine(9*M,9*B+2,w);require(E==affine(M,B,z),'neighborhood merger');endpoint_pair(row,E)
    elif kind=='dense_gate':
        C=integer(row['C'],1);P=integer(row['P'],0);B=integer(row['B'],1);M=integer(row['M'],2);w,z=two_words(row)
        require(B>C and (B-C)%2**P==0 and M%2**P==0,'prescribed cell')
        require(M==2**len(w) and len(w)==len(z) and len(w)>=P,'dense gate lengths')
        orbit(9*C+2,w[:P]);orbit(C,z[:P])
        E=affine(9*M,9*B+2,w);require(E==affine(M,B,z),'dense gate equality');endpoint_pair(row,E)
    else:raise ValueError('unknown kind')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('corpus',type=Path);ap.add_argument('--summary',type=Path,required=True)
    args=ap.parse_args();summary=json.loads(args.summary.read_text(encoding='utf-8'));raw=args.corpus.read_bytes()
    require(hashlib.sha256(raw).hexdigest()==summary['rows_sha256'],'corpus digest')
    counts={};sources=set();mergers=0;controls={}
    for line in raw.splitlines():
        row=json.loads(line);check(row);kind=row['kind'];counts[kind]=counts.get(kind,0)+1
        if kind=='comparison':
            require(row['C'] not in sources,'duplicate source');sources.add(row['C'])
            mergers+=row['status']=='MERGE'
        if kind!='comparison' or row['status']=='MERGE':controls.setdefault(kind,row)
    require(counts==summary['kinds'] and sources==set(range(1,summary['limit']+1)),'corpus coverage')
    require(mergers==summary['counts']['MERGE'],'merger census')
    mutations=[]
    for kind,fields in {'gap':['g','M','B'],'shadow':['a','b','k','seed','L','h','d','period'],
                        'comparison':['C','endpoint'],'lift':['n','m','C','r','minimum'],
                        'meeting_type':['C','endpoint'],'neighborhood':['isolated_C','B','M'],
                        'dense_gate':['B','M']}.items():
        for field in fields:
            r=copy.deepcopy(controls[kind]);r[field]+=1;mutations.append(r)
    for kind in controls:
        r=copy.deepcopy(controls[kind]);r['words'][0]=('1' if r['words'][0][0]=='0' else '0')+r['words'][0][1:];mutations.append(r)
    for kind in ('gap','shadow','comparison','lift'):
        r=copy.deepcopy(controls[kind]);field={'gap':'g','shadow':'a','comparison':'C','lift':'n'}[kind];r[field]=True;mutations.append(r)
    for row in mutations:
        try:check(row)
        except (ValueError,KeyError):pass
        else:raise ValueError('semantic mutation accepted')
    print(json.dumps({'kinds':counts,'mergers':mergers,'semantic_mutations_rejected':len(mutations),
                     'scope':'whole-cylinder and literal-witness verification; OUTSIDE labels not independently classified'},sort_keys=True))

if __name__=='__main__':main()
