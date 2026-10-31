#!/usr/bin/env python3
"""Separate implementation: literal certificates, raw clocks, full sparse profile.
No producer/project imports. Exact finite tests, not independent peer review.
"""
import argparse, copy, hashlib, json
from fractions import Fraction as Q
from itertools import product

def need(b, text):
    if not b: raise ValueError(text)
def integer(x): return type(x) is int

def pairs(pairs):
    out = {}
    for k,v in pairs:
        need(k not in out, 'duplicate JSON key'); out[k] = v
    return out

def read(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f, object_pairs_hook=pairs)

def digest(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def fraction(x):
    need(type(x) is list and len(x)==2 and all(integer(a)for a in x), 'rational schema')
    need(x[1]>0, 'denominator'); r=Q(*x)
    need([r.numerator,r.denominator]==x, 'noncanonical rational'); return r

def model_check(m):
    need(type(m)is list and len(m)==5,'model schema')
    p,u,v,A,B=m
    need(integer(p) and p in (2,3,5), 'supported prime field')
    d=len(v); need(1<=d<=128 and len(u)==d,'dimension')
    need(all(len(M)==d and all(len(row)==d for row in M)for M in(A,B)),'matrices')
    need(all(integer(a) and 0<=a<p for a in u+v+sum(A,[])+sum(B,[])),'field entry')
    return p,u,v,A,B

def value(m,n):
    p,u,_,A,B=m; row=list(u)
    for b in bin(n)[2:]:
        M=(A,B)[int(b)]
        row=[sum(row[i]*M[i][j]for i in range(len(row)))%p for j in range(len(row))]
    return sum(a*b for a,b in zip(row,m[2]))%p

def rank(columns,p):
    if not columns:return 0
    rows=[list(r)for r in zip(*columns)];h=0
    for c in range(len(columns)):
        k=next((k for k in range(h,len(rows))if rows[k][c]%p),None)
        if k is None:continue
        rows[h],rows[k]=rows[k],rows[h]
        a=pow(rows[h][c]%p,-1,p);rows[h]=[(x*a)%p for x in rows[h]]
        for k in range(len(rows)):
            if k!=h:
                a=rows[k][c]%p;rows[k]=[(x-a*y)%p for x,y in zip(rows[k],rows[h])]
        h+=1
    return h

def certificate_check(c):
    m=model_check(c['model']);p,u,v,A,B=m;d=len(v);r=c['result']
    if r['kind']=='edge':
        n=r['n'];w=r['word'];lane=r['lane']
        need(integer(n) and 1<=n<1<<(4*d+1),'source/bound')
        need(integer(lane) and lane in (0,1),'lane')
        need(all(integer(b)and b in(0,1)for b in w),'word')
        k=(1<<len(w))+sum(b*(1<<i)for i,b in enumerate(w))
        need(n==2*k+lane,'source decoding')
        t=(3*n+1)//2 if n%2 else n//2
        need(value(m,n)!=value(m,t),'not an actual violated edge')
        return 'edge'
    need(r['kind']=='constant','unknown result')
    z=r['certificate'];c0=z['value'];V=z['basis'];W=z['words']
    need(integer(c0)and 0<=c0<p and len(V)==len(W),'constant certificate schema')
    def step(vv,b):
        M=(A,B)[b]
        return [sum(M[i][j]*vv[j]for j in range(d))%p for i in range(d)]+[vv[d]]
    initial=list(v)+[1]
    need(all(len(z)==d+1 and all(integer(a)and 0<=a<p for a in z)for z in V),'span vectors')
    need(rank(V,p)==len(V),'basis rank')
    def inside(z):need(rank(V+[z],p)==len(V),'span not closed/initial absent')
    inside(initial)
    for vv,w in zip(V,W):
        need(all(integer(b)and b in (0,1)for b in w),'generator word')
        expected=initial
        for b in w:expected=step(expected,b)
        need(expected==vv,'basis word does not generate vector')
        for b in (0,1):inside(step(vv,b))
        y=step(vv,1)
        need((sum(a*b for a,b in zip(u,y[:d]))-c0*y[d])%p==0,'constant output fails')
    return 'constant'

def raw_records(x,cap=8192):
    n=x;clock=odd=0;visited=set();out=[]
    while True:
        need(n not in visited and clock<=cap,'raw replay repeat/budget')
        visited.add(n)
        if n%2:out.append((n,odd,clock))
        if n==1:return out,clock
        if n%2:n=(3*n+1)//2;odd+=1
        else:n//=2
        clock+=1

def profile_check(data,rows):
    X=data['source_cap'];need(X==65535,'profile source inventory')
    supplied={};last=0
    for row in rows:
        need(type(row)is list and len(row)==3 and all(integer(a)for a in row),'profile row')
        t,N,D=row;need(t>last and t%2==1 and N>0 and D>0,'profile ordering/sign')
        last=t;supplied[t]=fraction([N,D])
    expected={};clocks=odd_steps=0
    for x in range(1,X+1,2):
        pp,c=raw_records(x);clocks+=c;odd_steps+=len(pp)-1
        for t,q,A in pp:expected[t]=expected.get(t,Q(0))+Q(9**q,4**A)
    need(expected==supplied,'complete first-hit profile mismatch')
    g=data['global_profile']
    need(g['support_size']==len(expected)and g['maximum_support']==max(expected),'profile metadata')
    need(fraction(g['normalized_uniform_error'])==Q(1,2*(X+1)),'tail bound normalization')
    need(g['sha256']==digest(rows),'profile digest')
    need(clocks==data['raw_steps'] and odd_steps==data['odd_steps'],'clock inventory')
    return {'profile_entries':len(expected),'raw_steps':clocks,'odd_steps':odd_steps}

def transport_check(data):
    X=data['source_cap'];need(X==4095,'transport inventory')
    traces=data['traces'];need([a['seed']for a in traces]==[27,31,41,97,703,871],'seed inventory')
    targets={r['target']for tr in traces for r in tr['trace']};bank={t:{}for t in targets}
    for x in range(1,X+1,2):
        pp,_=raw_records(x)
        for t,q,A in pp:
            if t in bank:bank[t][x]=Q(3**q,2**A)
    entries=cohorts=0
    for tr in traces:
        seed=tr['seed'];pp,_=raw_records(seed);rows=tr['trace']
        need(len(pp)==len(rows),'trace length');old={};last=Q(0)
        for (t,q,A),row in zip(pp,rows):
            need([row['target'],row['q'],row['A']]==[t,q,A],'trace physical clock')
            D=Q(3**q,2**A);current={x:v/D for x,v in bank[t].items()}
            need(all(current.get(x)==v for x,v in old.items()),'old source/clock not retained')
            fresh={x:v for x,v in current.items()if x not in old}
            inc=sum((v*v for v in fresh.values()),Q(0));total=sum((v*v for v in current.values()),Q(0))
            need(total==last+inc and total==fraction(row['K']),'transported mass')
            need(len(fresh)==row['incoming'] and inc==fraction(row['increment']),'incoming cohort')
            entries+=1;cohorts+=len(fresh);old=current;last=total
    need(entries==data['ledger_entries']and cohorts==data['cohort_memberships'],'ledger inventory')
    need(fraction(data['cycle_K_at_300'])==Q(16,7)/Q(3,4)**600,'cycle deflation')
    return {'ledger_entries':entries,'cohort_memberships':cohorts}

def cylinder_check(data):
    rows=[];lifts=0
    for k in range(1,7):
        for w in product(range(1,5),repeat=k):
            A=sum(w);mod=2**(A+1);inv=pow(3,-1,mod);r=1
            for a in reversed(w):r=((2**a*r-1)*inv)%mod
            C=sum(3**(k-1-j)*2**sum(w[:j])for j in range(k))
            for h in (0,1,3):
                n=r+h*mod;start=n
                for a in w:
                    n=3*n+1;count=0
                    while n%2==0:n//=2;count+=1
                    need(count==a,'inverse branch replay')
                need(2**A*n==3**k*start+C,'affine replay');lifts+=1
            rows.append([list(w),r,C])
    need(data['word_sha256']==digest(rows)and data['words']==len(rows),'word inventory/hash')
    need(lifts==data['ordinary_lifts'],'lift inventory')
    return {'word_cases':len(rows),'ordinary_lifts':lifts}

def self_tests(samples,rows):
    good_edge=next(c for c in samples if c['result']['kind']=='edge')
    good_const=next(c for c in samples if c['result']['kind']=='constant')
    changes=[]
    for field,val in [('n',0),('n',1),('lane',2),('word',[2])]:
        a=copy.deepcopy(good_edge);a['result'][field]=val;changes.append(a)
    a=copy.deepcopy(good_edge);a['model'][0]=4;changes.append(a)
    a=copy.deepcopy(good_edge);a['model'][1][0]=True;changes.append(a)
    a=copy.deepcopy(good_const);p=a['model'][0];z=a['result']['certificate'];z['value']=(z['value']+1)%p;changes.append(a)
    a=copy.deepcopy(good_const);a['result']['certificate']['basis']=[];a['result']['certificate']['words']=[];changes.append(a)
    rejected=0
    for a in changes:
        try:certificate_check(a)
        except (ValueError,KeyError,IndexError,TypeError):rejected+=1
        else:raise ValueError('accepted mutated certificate')
    # These are direct contract/semantic controls, not resealed full corpora.
    for bad in ['{"a":1,"a":2}','{"schema":1,"schema":2}']:
        try:json.loads(bad,object_pairs_hook=pairs)
        except ValueError:rejected+=1
        else:raise ValueError('duplicate JSON accepted')
    return rejected

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('checks');ap.add_argument('--output',required=True);a=ap.parse_args()
    data=read(a.checks);need(data['schema']=='collatz-pass3-v1','schema');t=data['tracks']
    samples=t['linear']['certificates'];counts={'edge':0,'constant':0}
    for c in samples:counts[certificate_check(c)]+=1
    rows=read(a.checks+'.profile.json')
    result={'schema':'collatz-pass3-verification-v1','certificates':counts,
      'profile':profile_check(t['pressure'],rows),'transport':transport_check(t['transport']),
      'cylinders':cylinder_check(t['cylinders']),'mutations_rejected':self_tests(samples,rows),
      'checks_sha256':hashlib.sha256(open(a.checks,'rb').read()).hexdigest(),
      'profile_sha256':hashlib.sha256(open(a.checks+'.profile.json','rb').read()).hexdigest()}
    with open(a.output,'w',encoding='utf-8')as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
    print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
