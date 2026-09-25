#!/usr/bin/env python3
"""Independent all-height arithmetic checker plus preserved cut-certificate checker.

Does not import this pass's producer/oracle or any flow solver. Integer event
indices replace the producer's interval sweep. Generic cut verification delegates
to the hash-pinned, solver-free verifier published in the preceding packet.
"""
from __future__ import annotations
from bisect import bisect_right
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import argparse
import copy
import hashlib
import importlib.util
import json

PARENT = Path(__file__).resolve().parents[1]/'dyadic-repair'/'verify.py'
PARENT_SHA = '539b6d637299ccf4b933bc30fd1131d43520b91388a3d95d3246c6103d7f75da'
if hashlib.sha256(PARENT.read_bytes()).hexdigest() != PARENT_SHA:
    raise ValueError('changed parent certificate checker')
spec = importlib.util.spec_from_file_location('preserved_cut_checker', PARENT)
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
C = Counter()


def need(ok, msg):
    if not ok:
        raise ValueError(msg)


def integer(n, minimum=0):
    need(type(n) is int and n >= minimum, 'integer schema')
    return n


def enc(x):
    return [x.numerator, x.denominator]


def frac(pair):
    need(type(pair) is list and len(pair) == 2, 'rational pair')
    need(type(pair[0]) is int and type(pair[1]) is int and pair[1] > 0, 'rational types')
    x = F(*pair); need(enc(x) == pair, 'canonical rational')
    return x


def steps(rows):
    need(type(rows) is list and rows, 'step inventory')
    out = []; end = F(1); D = 0
    for item in rows:
        need(type(item) is list and len(item) == 3, 'step schema')
        a,b = map(frac, item[:2]); c = integer(item[2])
        need(a == end and a < b <= 2 and c in (0,1), 'partition or label')
        for x in (a,b):
            d = x.denominator
            need(d & (d-1) == 0, 'non-dyadic partition')
            D = max(D, d.bit_length()-1)
        out.append((a,b,c)); end=b
    need(end == 2, 'incomplete partition')
    return out,D


def label(rows, x):
    while x >= 2:
        x /= 2
    while x < 1:
        x *= 2
    i = bisect_right([a for a,b,c in rows], x)-1
    return rows[i][2]


def source_label(rows, n):
    return label(rows,F(n,2**(n.bit_length()-1)))


def boundaries(rows,p,scale,offset):
    points = {F(scale),F(2*scale)}
    endpoints = {a for a,b,c in rows}|{F(2)}
    for x in endpoints:
        points.add(x*scale)
        for t in (p.bit_length()-1,p.bit_length()):
            points.add((x*scale*2**t-offset)/p)
    return sorted(x for x in points if scale <= x <= 2*scale)


def expected_shell(rows,p,h,stop=None):
    """Discontinuities mapped to j=(n-1)/2, then integer index intervals."""
    integer(h); scale = 2**h
    stop = 2*scale-1 if stop is None else integer(stop)
    need(scale <= stop < 2*scale, 'partial shell cutoff')
    lo = scale//2; hi = (stop+1)//2
    events = {lo,hi}
    for x in boundaries(rows,p,scale,1):
        z=(x-1)/2
        j=-((-z.numerator)//z.denominator)
        events.add(max(lo,min(hi,j)))
    order=sorted(events); blocks=[]
    for a,b in zip(order,order[1:]):
        if a == b:
            continue
        n=2*a+1; last=2*b-1
        left=source_label(rows,n); right=source_label(rows,(p*n+1)//2)
        if blocks and blocks[-1][1]+2 == n and blocks[-1][2:] == [left,right]:
            blocks[-1][1]=last
        else:
            blocks.append([n,last,left,right])
    bad=[r for r in blocks if r[2] != r[3]]
    return {'h':h,'last_source':stop,'blocks':blocks,
            'defects':sum((b-a)//2+1 for a,b,c,d in bad),'least':bad[0][0] if bad else None}


def verify_shell(row,rows,p,h=None,stop=None):
    h=integer(row['h']) if h is None else h
    expected=expected_shell(rows,p,h,stop)
    need(row == expected,'arithmetic shell partition/count')
    C['shell_certificates']+=1; C['arithmetic_blocks']+=len(expected['blocks'])
    return expected


def verify_model(m):
    need(m['schema']=='least-defect-model-v1','model schema')
    p=integer(m['p'],3); need(p in (3,5),'multiplier')
    rows,D=steps(m['steps']); P=2 if p==3 else 4; start=D+1
    need(type(m['D']) is int and m['D']==D and m['period']==P and m['start']==start,'depth/period/start')
    pts=boundaries(rows,p,1,0)
    ideal=[]; delta=F(0)
    for a,b in zip(pts,pts[1:]):
        x=(a+b)/2; c=label(rows,x); d=label(rows,p*x)
        ideal.append([enc(a),enc(b),c,d])
        if c != d:
            delta+=b-a
    need(m['ideal']==ideal and frac(m['delta'])==delta,'ideal geometry')
    need((delta>0)==(len({c for a,b,c in rows})>1),'finite-step nonconstancy')
    need(len(m['base'])==start+P and len(m['beta'])==P,'base period coverage')
    for h,row in enumerate(m['base']):
        verify_shell(row,rows,p,h)
    for r,pair in enumerate(m['beta']):
        need(frac(pair)==m['base'][start+r]['defects']-delta*2**(start+r-1),'periodic correction')
    C['models']+=1
    return rows


def count(m,h):
    if h<m['start']:
        return m['base'][h]['defects']
    v=frac(m['delta'])*2**(h-1)+frac(m['beta'][(h-m['start'])%m['period']])
    need(v.denominator==1 and v>=0,'tail integrality')
    return v.numerator


def verify_least(m,a):
    candidates=[r['least'] for r in m['base'] if r['least'] is not None]
    if candidates:
        n=min(candidates); expected={'n':n,'shell':n.bit_length()-1,'extra':None}
    elif frac(m['delta'])==0:
        expected={'n':None,'shell':None,'extra':None}
    else:
        h=m['start']+m['period']; rows,_=steps(m['steps'])
        row=verify_shell(a['extra'],rows,m['p'],h)
        need(row['least'] is not None and row['defects']==count(m,h),'late first defect')
        expected={'n':row['least'],'shell':h,'extra':row}
    need(a==expected,'global least defect')
    C['least_certificates']+=1
    return expected['n']


def minimum(m):
    for r in m['base']:
        if r['least'] is not None:
            return r['least']
    if frac(m['delta'])==0:
        return None
    rows,_=steps(m['steps'])
    return expected_shell(rows,m['p'],m['start']+m['period'])['least']


def verify_cutoff(m,c,H=None):
    H=integer(c['H'],1) if H is None else H
    p,start,P=m['p'],m['start'],m['period']; rows,_=steps(m['steps'])
    L=min(H,(2*H-1)//p)
    if L==0:
        need(c=={'H':H,'last_eligible':0,'full_shells':0,'prefix':0,'tail':[0,1],
                 'last_shell':None,'defects':0,'least':None},'empty physical cutoff')
        C['cutoff_certificates']+=1
        return
    a=L.bit_length()-1
    prefix=sum(count(m,h) for h in range(min(start,a)))
    # Independent aggregation: a geometric progression for EACH height residue.
    tail=F(0)
    for r in range(P):
        first=start+r
        if first>=a:
            continue
        num=1+(a-1-first)//P
        tail+=frac(m['delta'])*2**(first-1)*F(2**(P*num)-1,2**P-1)
        tail+=num*frac(m['beta'][r])
    row=verify_shell(c['last_shell'],rows,p,a,L)
    total=F(prefix)+tail+row['defects']; n=minimum(m)
    n=n if n is not None and n<=L else None
    need(total.denominator==1 and (total>0)==(n is not None),'aggregate integrality/witness')
    need(c=={'H':H,'last_eligible':L,'full_shells':a,'prefix':prefix,'tail':enc(tail),
             'last_shell':row,'defects':total.numerator,'least':n},'full physical cutoff')
    C['cutoff_certificates']+=1


def batch(m,d,stop,limit):
    rows,_=steps(m['steps']); selected=[]
    for h in range(d.bit_length()-1,stop.bit_length()):
        row=expected_shell(rows,m['p'],h,min(stop,2**(h+1)-1))
        for a,b,c,e in row['blocks']:
            if c==e:
                continue
            a=max(a,d); a+=int(a%2==0)
            while a<=b and len(selected)<limit:
                selected.append(a); a+=2
    return selected


def verify_completion(c,m):
    V.verify_cut(c)
    need(c['status']=='SEPARATOR','separator required')
    rows=[]
    for a,b,color in c['ranges']:
        left,right=frac(a)+1,frac(b)+1
        if rows and rows[-1][2]==color:
            rows[-1][1]=enc(right)
        else:
            rows.append([enc(left),enc(right),color])
    need(m['steps']==rows and m['p']==c['problem']['p'],'different model from cut')
    verify_model(m)


def verify_refinement(r):
    need(r['schema']=='least-defect-refinement-v1','refinement schema')
    p=integer(r['p'],3); need(p in (3,5),'multiplier')
    N=integer(r['N'],1); cap=integer(r['cap']); limit=integer(r['batch_limit'],1)
    pc=integer(r['precision_cap'],64)
    need(r['selection']=='LEAST_PREFIX_BATCH','unknown policy')
    bits=r['cutoff_bits']; H=None
    if bits is not None:
        H=2**integer(bits,1); need(N<=H,'root outside cutoff')
    have=r['initial_sources'][:]
    need(have==sorted(set(have)) and 1 in have and (p==3 or 3 in have),'initial core/inventory')
    for n in have:
        integer(n,1); need(n%2==1,'initial odd source')
        need(H is None or max(n,(p*n+1)//2)<=H,'initial physical peak')
    need(len(r['records'])<=cap,'round cap')
    def check_problem(c):
        need(c['problem']=={'p':p,'N':N,'odd_sources':have},'original source/edge history')
        need(c['horizon']==(None if H is None else bits-1),'horizon changed')
    def check_answer(m,a):
        if H is None:
            return verify_least(m,a)
        verify_cutoff(m,a,H); return a['least']
    for record in r['records']:
        c,m=record['cut'],record['model']; check_problem(c); verify_completion(c,m)
        need(frac(c['upper'])-frac(c['lower'])<=1,'uncertified optimizer accuracy')
        d=check_answer(m,record['oracle']); need(d is not None,'repair without a defect')
        stop=2*d if H is None else min(2*d,(2*H-1)//p,H)
        need(record['batch_stop']==stop,'batch scope')
        selected=batch(m,d,stop,limit)
        need(record['selected']==selected and selected and selected[0]==d,'not the least defect prefix')
        need(not set(selected)&set(have),'repeated repair')
        for n in selected:
            need(H is None or max(n,(p*n+1)//2)<=H,'repair exits physical cutoff')
        have=sorted(have+selected)
        C['repair_rounds']+=1; C['physical_repair_edges']+=len(selected)
    c=r['final_cut']; check_problem(c)
    if r['status']=='CONVERGENCE':
        V.verify_cut(c); need(c['status']=='PINS_INFEASIBLE','unjustified merger')
        path=r['path']; need(type(path) is list and path and path[0]==N and path[-1]==1,'path endpoints')
        for n,t in zip(path,path[1:]):
            integer(n,1); integer(t,1)
            need(t==((p*n+1)//2 if n%2 else n//2),'literal path')
            need(n%2==0 or n in have,'unretained physical edge')
            need(H is None or max(n,t)<=H,'path leaves cutoff')
        C['path_steps']+=len(path)-1
    elif r['status']=='UNRESOLVED_AT_PRECISION_CAP':
        V.verify_cut(c)
        need(c['status']=='SEPARATOR' and c['tail_terms']>=pc and
             frac(c['upper'])-frac(c['lower'])>1,'false precision cap')
    else:
        m=r['model']; verify_completion(c,m)
        need(frac(c['upper'])-frac(c['lower'])<=1,'final optimizer accuracy')
        d=check_answer(m,r['oracle'])
        if r['status']=='FULL_FINITE_SEPARATOR':
            need(H is not None and d is None and r['oracle']['defects']==0,'incomplete full separator')
            need(c['lower']==c['upper'],'inexact finite optimum')
        else:
            need(r['status']=='UNRESOLVED_AT_ROUND_CAP' and len(r['records'])==cap and d is not None,
                 'false round cap')
    C['refinements']+=1; C[r['status'].lower()]+=1


def grid(D,mask):
    size=2**D; rows=[]
    for i in range(size):
        c=0 if i==0 else (mask>>(i-1))&1
        a,b=F(size+i,size),F(size+i+1,size)
        if rows and rows[-1][2]==c:
            rows[-1][1]=enc(b)
        else:
            rows.append([enc(a),enc(b),c])
    return rows


def arithmetic_inventory(data):
    expected={(p,D,z) for p in (3,5) for D in (1,2,3) for z in range(2**(2**D-1))}
    seen=set()
    for item in data['models']:
        key=tuple(item['grid']); need(key in expected and key not in seen,'grid coverage'); seen.add(key)
        p,D,mask=key; m=item['model']; need(m['p']==p and m['steps']==grid(D,mask),'grid/model mismatch')
        rows=verify_model(m); verify_least(m,item['least'])
        small=[]
        for h in range(10):
            bad=[]
            for n in range(2**h|1,2**(h+1),2):
                if source_label(rows,n)!=source_label(rows,(p*n+1)//2):
                    bad.append(n)
                C['literal_shell_sources']+=1
            need(len(bad)==count(m,h),'literal all-height formula')
            small.append(len(bad))
        need(item['small_counts']==small,'literal small counts')
        hs=[m['start'],m['start']+m['period'],m['start']+7*m['period'],64]
        need(len(item['tail_comparisons'])==len(hs),'recurrence inventory')
        for h,row in zip(hs,item['tail_comparisons']):
            verify_shell(row,rows,p,h); need(row['defects']==count(m,h),'recurrence comparison')
            C['recurrence_checks']+=1
        heights=(1,2,7,8,23,24,127,128,513,2**129)
        need(len(item['cutoffs'])==len(heights),'cutoff inventory')
        for H,c in zip(heights,item['cutoffs']):
            verify_cutoff(m,c,H)
            if H<1024:
                bad=[n for n in range(1,H+1,2) if (p*n+1)//2<=H and
                     source_label(rows,n)!=source_label(rows,(p*n+1)//2)]
                need(c['defects']==len(bad) and c['least']==(bad[0] if bad else None),'literal cutoff')
                C['literal_cutoff_checks']+=1
    need(seen==expected,'omitted grid case')
    configurations=[(p,D,z) for p in (3,5) for D,z in ((1,1),(3,37))]
    need(len(data['huge'])==4,'huge controls')
    for key,row in zip(configurations,data['huge']):
        p,D,z=key; m=row['model']
        need(m['p']==p and m['steps']==grid(D,z),'huge model')
        verify_model(m); verify_cutoff(m,row['cutoff'],2**4096)
        C['symbolic_4096_bit_cutoffs']+=1
    need(data['cycles']==[[5,[1,3,8,4,2,1]],[5,[13,33,83,208,104,52,26,13]]],'cycle inventory')
    for p,path in data['cycles']:
        need(path[0]==path[-1],'cycle closure')
        for n,t in zip(path,path[1:]):
            need(t==((p*n+1)//2 if n%2 else n//2),'control cycle step')
        C['control_cycle_steps']+=len(path)-1


def refinement_inventory(data):
    configurations=[(1,3,0,None),(8,3,0,None),(3,3,32,None),(7,3,64,None),
                    (27,3,160,None),(97,3,96,None),(871,3,16,None),(13,5,32,None),
                    (27,3,160,13),(27,3,96,8),(13,5,96,10)]
    need(len(data['refinements'])==len(configurations),'refinement inventory')
    for r,(N,p,cap,bits) in zip(data['refinements'],configurations):
        need((r['N'],r['p'],r['cap'],r['cutoff_bits'],r['batch_limit'])==(N,p,cap,bits,16),
             'refinement configuration')
        need(r['initial_sources']==([1] if p==3 else [1,3]),'core-only initialization')
        verify_refinement(r)


def corpus(data, section='all'):
    if data['schema']=='least-defect-refinement-v1':
        verify_refinement(data); return
    need(data['schema']=='least-defect-corpus-v1','corpus schema')
    if section in ('all','arithmetic'):
        arithmetic_inventory(data)
    if section in ('all','refinements'):
        refinement_inventory(data)


def self_test(data):
    m=next(x['model'] for x in data['models'] if x['grid']==[3,2,3])
    changes=[('delta',lambda x:x.__setitem__('delta',[0,1])),
             ('beta',lambda x:x['beta'].__setitem__(0,[999,1])),
             ('period',lambda x:x.__setitem__('period',4)),
             ('start',lambda x:x.__setitem__('start',x['start']+1)),
             ('depth',lambda x:x.__setitem__('D',x['D']+1)),
             ('missing-shell',lambda x:x['base'].pop()),
             ('missing-block',lambda x:x['base'][-1]['blocks'].pop()),
             ('even-source',lambda x:x['base'][-1]['blocks'][0].__setitem__(0,2)),
             ('count',lambda x:x['base'][-1].__setitem__('defects',999)),
             ('least',lambda x:x['base'][-1].__setitem__('least',999)),
             ('step-color',lambda x:x['steps'][0].__setitem__(2,True)),
             ('non-dyadic',lambda x:x['steps'][0].__setitem__(1,[4,3])),
             ('ideal-label',lambda x:x['ideal'][0].__setitem__(2,1-x['ideal'][0][2]))]
    def reject(fn,name):
        try:
            fn()
        except (ValueError,KeyError,IndexError,TypeError):
            C['mutations_rejected']+=1
        else:
            raise ValueError('accepted mutation: '+name)
    for name,change in changes:
        bad=copy.deepcopy(m); change(bad)
        reject(lambda:verify_model(bad),name)
    item=next(x for x in data['models'] if x['grid']==[3,2,3])
    for field,value in [('defects',0),('last_eligible',513),('least',None),('tail',[999,1])]:
        bad=copy.deepcopy(item['cutoffs'][-2]); bad[field]=value
        reject(lambda:verify_cutoff(m,bad),field)
    a=copy.deepcopy(item['least']); a['n']+=2
    reject(lambda:verify_least(m,a),'not least')
    r=next(x for x in data['refinements'] if x['N']==3)
    for name,change in [('changed-root',lambda x:x.__setitem__('N',7)),
                        ('missing-least',lambda x:x['records'][0]['selected'].pop(0)),
                        ('batch-stop',lambda x:x['records'][0].__setitem__('batch_stop',999)),
                        ('fake-convergence',lambda x:x['path'].__setitem__(-1,2))]:
        bad=copy.deepcopy(r); change(bad)
        reject(lambda:verify_refinement(bad),name)


def no_duplicates(pairs):
    out={}
    for k,v in pairs:
        need(k not in out,'duplicate JSON key'); out[k]=v
    return out


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file',type=Path); parser.add_argument('--self-test',action='store_true')
    parser.add_argument('--section',choices=('all','arithmetic','refinements'),default='all')
    args=parser.parse_args(); raw=args.file.read_bytes()
    data=json.loads(raw,object_pairs_hook=no_duplicates); corpus(data,args.section)
    counts=dict(C); inherited=dict(V.COUNTS)
    if args.self_test:
        need(data['schema']=='least-defect-corpus-v1','self-test requires full corpus')
        before=C['mutations_rejected']; self_test(data)
        counts['mutations_rejected']=C['mutations_rejected']-before
    print(json.dumps({'status':'PASS','section':args.section,'counts':counts,'preserved_cut_checker':inherited,
                      'corpus_sha256':hashlib.sha256(raw).hexdigest()},sort_keys=True))


if __name__=='__main__':
    main()
