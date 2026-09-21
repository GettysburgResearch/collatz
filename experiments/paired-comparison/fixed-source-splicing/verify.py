#!/usr/bin/env python3
"""Standalone literal/affine verifier; imports no generator or repository code.
Baseline OUTSIDE labels are authenticated, NOT independently reclassified.
"""
import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path

BASELINE = '1779b90595779a44067c7b68c6283340d67ed1b474791dd7df329d1cd63d0a44'
PARENT = '0fb8e0a5da81c4c9138e39152e4389587291a0c2'


def check(ok, message):
    if not ok:
        raise ValueError(message)


def typed(obj):
    if type(obj) is dict:
        check(all(type(k) is str for k in obj), 'non-string key')
        for value in obj.values():
            typed(value)
    elif type(obj) is list:
        for value in obj:
            typed(value)
    else:
        check(type(obj) in (int, str), 'noncanonical type')


def unique(pairs):
    out = {}
    for k, v in pairs:
        check(k not in out, 'duplicate key')
        out[k] = v
    return out


def parse(text):
    obj = json.loads(text, object_pairs_hook=unique)
    typed(obj)
    return obj


def dump(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))


def forward(x, length):
    check(type(x) is int and x > 0, 'source positivity')
    word = ''; values = []
    for _ in range(length):
        bit = x & 1; word += str(bit)
        x = (x+bit*(2*x+1))//2
        values.append(x)
    return x, word, values


def word_check(x, word):
    check(type(word) is str and set(word) <= {'0', '1'}, 'word alphabet')
    end, actual, values = forward(x, len(word))
    check(actual == word, 'not actual parities')
    return end, values


def affine(A, B, word):
    # Keep the FULL numerator/denominator, rather than halving coefficients.
    check(A > 0 and B > 0, 'affine positivity')
    p, c, d = 1, 0, 1; prefixes = []
    for bit in word:
        check(bit in '01', 'affine alphabet')
        check((p*A) % (2*d) == 0, 'affine slope parity')
        check((p*B+c) % (2*d) == int(bit)*d, 'affine intercept parity')
        if bit == '1':
            p *= 3; c = 3*c+d
        d *= 2
        check((p*A) % d == (p*B+c) % d == 0, 'full denominator')
        prefixes.append([p*A//d, (p*B+c)//d])
    return [p*A//d, (p*B+c)//d], prefixes


def check_certificate(n, item):
    typed(item)
    check(set(item) == {'status','method','m','words','endpoint','minimum','strict'}, 'certificate fields')
    check(item['status'] == 'MERGE' and 0 < item['m'] < n, 'original-root order')
    check(type(item['words']) is list and len(item['words']) == 2, 'two words')
    y, values = word_check(n, item['words'][0])
    z, _ = word_check(item['m'], item['words'][1])
    check(values and y == z == item['endpoint'], 'meeting')
    check(item['minimum'] == min(values), 'all-state minimum')
    check(item['strict'] == int(min(values) > n), 'strictness')


def first_run(n):
    r = 0; z = n+1
    while z % 2 == 0:
        z //= 2; r += 1
    return r, z


def make(n, m, a, b, method):
    y, w, values = forward(n, a); z, v, _ = forward(m, b)
    check(y == z, 'independent selector did not merge')
    return dict(status='MERGE',method=method,m=m,words=[w,v],endpoint=y,
                minimum=min(values),strict=int(min(values)>n))


def selection(n):
    r, u = first_run(n)
    check(r >= 2 and 3**r*u % 4 == 3, 'selector hard entrance')
    initial, _, _ = forward(n, r+2)
    check((initial-2) % 9 == 0, 'H entrance')
    C = (initial-2)//9; d = C; e = 0
    while d % 2 == 0:
        d //= 2; e += 1
    if e % 2:
        y, _, _ = forward(n, r+e+3)
        check(y % 3 == 2, 'valuation inverse residue')
        m = (2*y-1)//3
        if m < n:
            return make(n,m,r+e+3,1,'VALUATION')
    if r in (2,3):
        z, _, _ = forward(n,r+1); s, _ = first_run(z)
        terminal, _, _ = forward(z,s)
        if terminal % 4 == 0:
            return make(n,3*C,r+s+3,s+1,'RESTART')
    z, _, _ = forward(n,r+1); s, _ = first_run(z)
    terminal, _, _ = forward(z,s)
    if terminal % 4 == 2:
        endpoint, _, _ = forward(z,s+2)
        check((endpoint-2)%9==0,'second H entrance')
        d=(endpoint-2)//9; e=0
        check(d>0,'positive second parameter')
        while d%2==0:
            d//=2; e+=1
        if e%2:
            a=r+s+e+4
            y, _, _ = forward(n,a); m, rem=divmod(2*y-1,3)
            check(rem==0,'second odd predecessor')
            if m<n:
                return make(n,m,a,1,'SECOND_VALUATION')
    for j in range(1,65):
        y, _, _ = forward(n,j)
        if y <= n:
            return dict(status='OUTSIDE',stop='DESCENT_OR_RETURN',clock=j,state=y)
        m, rem = divmod(2*y-1,3)
        if rem == 0 and 0 < m < n:
            return make(n,m,j,1,'BAND')
    return dict(status='OUTSIDE',stop='HORIZON',clock=64,state=y)


def check_source(row):
    typed(row)
    check(set(row) == {'kind','n','baseline','result'}, 'source fields')
    n = row['n']; check(2 <= n <= 65536, 'source range')
    base, result = row['baseline'], row['result']
    if base['status'] == 'MERGE':
        check_certificate(n,base)
        check(dump(result) == dump(base), 'parent certificate changed')
        r,u = first_run(n)
        if base['method'] == 'UFS':
            check(r>=2 and 3**r*u%4==3 and base['m']==(n-1)//2, 'UFS original source')
            check(base['words'][0].startswith('1'*r+'01') and
                  base['words'][1].startswith('1'*(r-1)+'00'), 'UFS initial clocks')
        else:
            if n%2==0: expected=make(n,n//2,1,0,'EVEN')
            elif n%4==1: expected=make(n,(3*n+1)//4,2,0,'MOD4')
            else:
                check(3**r*u%4==1,'good first exit')
                expected=make(n,(n-1)//2,r+2,r+1,'GOOD_EXIT')
            check(dump(base)==dump(expected),'elementary baseline')
    else:
        r,u = first_run(n)
        check(base==dict(status='OUTSIDE',C=(3**(r-1)*u-1)//4), 'baseline outside schema')
        check(dump(result)==dump(selection(n)), 'new selector outcome')
        if result['status']=='MERGE':
            check_certificate(n,result)


def check_family(row):
    typed(row)
    check(set(row)=={'kind','args','forms','words','endpoint','strict','divisible3'},'family fields')
    kind=row['kind']; args=row['args']; forms=row['forms']; words=row['words']
    check(len(forms)==len(words)==2 and all(len(f)==2 for f in forms),'family shape')
    end,prefixes=affine(*forms[0],words[0]); other,_=affine(*forms[1],words[1])
    check(end==other==row['endpoint'],'whole affine endpoint')
    if kind=='TEMPLATE':
        k,=args; check(0<=k<=80,'template k')
        expected=[[9*2**(2*k+2),9*2**(2*k+1)+2],[2*3**(k+1),3**(k+1)]]
        check(forms==expected and words==['01'*k+'00','1'],'template identity')
        check(row['strict']==row['divisible3']==0,'template tags')
        return
    check(forms[1][0]<forms[0][0] and forms[1][1]<forms[0][1],'whole original-root order')
    if kind in ('SHORT_RUN','UNBOUNDED'):
        r,k,u,U=args
        Q=2**(2*k+4)
        check(U==3*Q and u>0 and u%2==1,'CRT modulus')
        check((3**(r-1)*u-1)%Q==Q//2,'exact valuation')
        nA,nB=forms[0]; mA,mB=forms[1]
        check([nA,nB]==[2**r*U,2**r*u-1],'original family')
        check(2**(2*k+3)*mA==3**(r+k)*U and
              2**(2*k+3)*mB==3**(k+1)*(3**(r-1)*u-1),'companion family')
        check(words==['1'*r+'01'*(k+1)+'00','1'],'valuation clocks')
        check(nA%3==nB%3==0 and row['divisible3']==1,'CRT 3 condition')
        # Canonical positive tail: the preceding CRT member is invalid or not smaller.
        check(u<=U or nB-nA<=mB-mA,'unnecessary positive tail shift')
        if kind=='SHORT_RUN':
            check(2<=r<=5 and 0<=k<=64 and row['strict']==0,'short stratum inventory')
        else:
            check(5<=r<=80 and row['strict']==1,'unbounded inventory')
            check(3**(r+k)<2**(r+2*k+3),'lambda below one')
            check(k==0 or 3**(r+k-1)>=2**(r+2*k+1),'least k')
    else:
        check(kind=='RESTART_FAMILY','family kind')
        r,s,u,U=args
        check(r in (2,3) and 1<=s<=80 and U==2**(s+3) and 0<u<U,'restart inventory')
        check((3**r*u+1)%(2**(s+1))==0,'restart division')
        v=(3**r*u+1)//2**(s+1)
        check(v%2==1 and 3**s*v%4==1,'actual second good exit')
        check(forms==[[2**r*U,2**r*u-1],[3**r*U//4,3*(3**(r-1)*u-1)//4]],'restart forms')
        check(words==['1'*r+'0'+'1'*s+'00','1'*(s-1)+'01'],'restart clocks')
        check(row['strict']==row['divisible3']==0,'restart tags')
    if row['strict']:
        check(all(a>=forms[0][0] and b>forms[0][1] for a,b in prefixes),'all-time whole-family floor')


def self_test(samples):
    bad=[]
    for key,value in [('endpoint',[0,0]),('words',['0','1']),('strict',1),('divisible3',1)]:
        row=copy.deepcopy(samples['TEMPLATE']); row[key]=value; bad.append(('family',row))
    for index in (0,1):
        for coord in (0,1):
            row=copy.deepcopy(samples['UNBOUNDED']); row['forms'][index][coord]+=1; bad.append(('family',row))
    for key,value in [('endpoint',0),('m',1311),('minimum',0),('strict',0),('words',['1','1']),('method','BASE')]:
        row=copy.deepcopy(samples['SOURCE']); row['result'][key]=value; bad.append(('source',row))
    for value in (True,1311.0,'1311'):
        row=copy.deepcopy(samples['SOURCE']); row['n']=value; bad.append(('source',row))
    for category,row in bad:
        try:
            (check_family if category=='family' else check_source)(row)
        except (ValueError,TypeError):
            pass
        else:
            raise ValueError('mutation accepted: '+dump(row))
    for text in ('{"a":1,"a":2}', '{"a":true}', '{"a":1.0}', '{"a":null}'):
        try: parse(text)
        except ValueError: pass
        else: raise ValueError('JSON control accepted')
    pairs=0
    for n in range(2,257):
        actual={forward(m,1)[0]:m for m in range(1,n) if forward(m,1)[0]>=n}
        predicted={y:(2*y-1)//3 for y in range(n,2*n+1) if y%3==2 and 2*y-1<3*n}
        check(actual==predicted,'complete one-step inverse menu')
        pairs+=n+1
    # A true identity need NOT be an admissible smaller-original-source witness.
    y,w,_=forward(191,10); z,v,_=forward(273,1)
    check(y==z==410 and 273>191,'root-order countercontrol')
    check(selection(27)==dict(status='OUTSIDE',stop='DESCENT_OR_RETURN',clock=59,state=23),'pointwise unresolved control')
    return dict(rejected_controls=len(bad)+4,annulus_pairs=pairs,additional_countercontrols=2)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('full',type=Path); parser.add_argument('--summary',type=Path,required=True)
    parser.add_argument('--self-test',action='store_true'); args=parser.parse_args()
    summary=parse(args.summary.read_text()); counts=Counter(); digest=hashlib.sha256(); basehash=hashlib.sha256()
    expected=[('TEMPLATE',[k]) for k in range(81)]
    expected += [('SHORT_RUN',[r,k]) for r in range(2,6) for k in range(65)]
    expected += [('UNBOUNDED',[r]) for r in range(5,81)]
    expected += [('RESTART_FAMILY',[r,s]) for r in (2,3) for s in range(1,81)]
    position=0; samples={}
    with args.full.open('rb') as stream:
        for raw in stream:
            row=parse(raw); check(raw==(dump(row)+'\n').encode(),'canonical line bytes')
            digest.update(raw); counts['rows']+=1; counts['kind_'+row['kind']]+=1
            if position<len(expected):
                kind,ident=expected[position]
                check(row['kind']==kind and row['args'][:len(ident)]==ident,'family coverage/order')
                check_family(row); samples.setdefault(kind,row)
            else:
                check(row['kind']=='SOURCE' and row['n']==position-len(expected)+2,'source coverage/order')
                check_source(row); n=row['n']; base=row['baseline']; result=row['result']
                basehash.update((dump([n,base])+'\n').encode())
                counts['baseline_'+base['status']]+=1; counts['final_'+result['status']]+=1
                if base['status']!='MERGE' and result['status']=='MERGE':
                    counts['added_'+result['method']]+=1; counts['added_strict']+=result['strict']
                if result['status']=='OUTSIDE': counts['outside_'+result['stop']]+=1
                if n==1311: samples['SOURCE']=row
            position+=1
    check(position==len(expected)+65535,'complete finite inventory')
    check(basehash.hexdigest()==BASELINE==summary['baseline_sha256'],'authenticated parent outcomes')
    wanted=dict(schema=1,source_range=[2,65536],scan_horizon=64,counts=dict(sorted(counts.items())),
                sha256=digest.hexdigest(),baseline_sha256=BASELINE,parent_blob=PARENT)
    check(dump(summary)==dump(wanted),'full summary')
    report=dict(status='PASS',rows=position,sha256=digest.hexdigest(),
                parent_outside_scope='authenticated, not independently reclassified')
    if args.self_test: report.update(self_test(samples))
    print(dump(report))


if __name__=='__main__':
    main()
