#!/usr/bin/env python3
"""Independent finite witness reconstruction; no imports from run.py or repo.

H-grid labels are classified at ALL future depths from complete literal core
paths. Root-mine successful families are verified; its unsuccessful/optimality
labels are NOT independently re-searched by this program.
"""
from __future__ import annotations
import argparse
from collections import Counter
import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def check(c,message='invalid certificate'):
    if not c: raise ValueError(message)

def nat(x,lo=0):
    check(type(x) is int and x>=lo,'not an exact permitted integer')

def typed_tree(x, key=None):
    if type(x) is bool:
        check(key=='all_prefix_coefficients_above_one','boolean numeric alias')
    elif type(x) is float:
        raise ValueError('floating-point alias')
    elif type(x) is dict:
        for k,v in x.items():typed_tree(v,k)
    elif type(x) is list:
        for v in x:typed_tree(v,key)

def object_no_duplicates(items):
    ans={}
    for k,v in items:
        check(k not in ans,'duplicate JSON key');ans[k]=v
    return ans

def T(x):return x//2 if x%2==0 else (3*x+1)//2

def path(x):
    nat(x,1);states=[x];odds=[0];word=[]
    for _ in range(10000):
        if states[-1]==1:return states,odds,''.join(word)
        p=states[-1]%2;word.append(str(p));odds.append(odds[-1]+p)
        states.append(T(states[-1]))
    raise ValueError('unresolved finite path budget')

def replay(x,w):
    nat(x,1);check(type(w) is str and set(w)<=set('01'))
    states=[x]
    for c in w:
        check(x%2==int(c),'bad physical parity');x=T(x);states.append(x)
    return x,states

def affine(a,b,w):
    # Independently propagate a WHOLE progression a*h+b. Both coefficients
    # must permit the indicated division; no sampled parity acceptance.
    for c in w:
        check(a%2==0 and b%2==int(c),'nonuniform progression')
        if c=='1': a,b=3*a,3*b+1
        a//=2;b//=2
    return a,b

def factor(a):
    nat(a,1);p=q=0
    while not a%2:a//=2;p+=1
    while not a%3:a//=3;q+=1
    return p,q,a

def verify_H(row):
    check(type(row) is list and len(row)==7)
    c,s,p,t,q,d,kind=row
    for n in row[:5]:nat(n)
    check(c>=1 and type(d) is int)
    xs,qs,w=path(9*c+2);ys,ps,z=path(c)
    check([s,p,t,q]==[len(w),qs[-1],len(z),ps[-1]],'wrong stopping data')
    check(d==4+2*p-s-2*q+t,'wrong reported defect')
    upto=max(s,t)
    while len(xs)<=upto:
        qs.append(qs[-1]+xs[-1]%2);xs.append(T(xs[-1]))
    while len(ys)<=upto:
        ps.append(ps[-1]+ys[-1]%2);ys.append(T(ys[-1]))
    first=next((j for j in range(upto+1) if xs[j]==ys[j]),None)
    if first is None:
        check((s-t)%2!=0,'missing phase proof')
        expected='phase'
    else:
        expected='uniform' if ps[first]-qs[first]==2 else 'isolated'
        if expected=='uniform':
            F=''.join(str(x%2) for x in xs[:first]);G=''.join(str(y%2) for y in ys[:first])
            M=1<<first
            check(affine(9*M,9*c+2,F)==affine(M,c,G),'whole H cylinder fails')
    check(kind==expected,'incorrect all-depth classification')

def verify_family(row):
    fs=row['forms'];t=row['point'];nat(t)
    check(type(fs) is list and len(fs)>=2)
    values=[];paths=[];facts=[]
    for f in fs:
        check(type(f) is list and len(f)==2);a,b=f;nat(a,1);check(type(b) is int)
        n=a*t+b;values.append(n);paths.append(path(n));facts.append(factor(a))
    check(row['values']==values and row['stopping_words']==[x[2] for x in paths])
    charges=[u+2*v+2*q[-1]-len(w) for (u,v,_),(_,q,w) in zip(facts,paths)]
    check(row['weighted_charges']==charges)
    if len({f[2] for f in facts})>1:
        status='incompatible_slope_cores'
    elif len({(len(p[2])-f[0])%2 for p,f in zip(paths,facts)})>1:
        status='phase_blocked_at_forced_clocks'
    else:
        words=row['words'];check(len(words)==len(fs))
        offsets=[];derivatives=[]
        for (a,b),n,w,f in zip(fs,values,words,facts):
            check(replay(n,w)[0]==1,'not at common core endpoint')
            offsets.append(len(w)-f[0])
            derivatives.append(Fraction(a*3**w.count('1'),1<<len(w)))
        check(len(set(offsets))==1,'wrong forced clocks')
        status='uniform_at_point' if len(set(derivatives))==1 else 'isolated_at_forced_clocks'
        if status=='uniform_at_point':
            base,M=row['progression'];nat(M,1);check(base==t and M==1<<offsets[0])
            eps=[affine(a*M,a*t+b,w) for (a,b),w in zip(fs,words)]
            check(len(set(eps))==1,'family endpoint slopes differ')
    check(row['status']==status,'incorrect pointwise germ status')

def verify_lift(row):
    n,m=row['n'],row['m'];nat(n,2);nat(m,1);check(m<n)
    w,z=row['words'];E,states=replay(n,w);check(replay(m,z)[0]==E==row['endpoint'])
    L,J=len(w),len(z);q,p=w.count('1'),z.count('1')
    A=(1<<L)*3**max(p-q,0);B=(1<<J)*3**max(q-p,0)
    check(row['steps']==[A,B],'nonprimitive lattice step')
    check(affine(A,n,w)==affine(B,m,z)==(3**max(q,p),E),'lift identity')
    check(row['endpoint_step']==3**max(q,p))
    last=None if A>=B else (n-m-1)//(B-A)
    check(row['order_last_parameter']==last,'wrong order domain')
    q0=0;pred=True
    for i,c in enumerate(w,1):
        q0+=int(c)
        pred=pred and 3**q0>1<<i
    check(type(row['all_prefix_coefficients_above_one']) is bool)
    check(row['all_prefix_coefficients_above_one']==pred,'coefficient claim')
    if pred:check(min(states[1:])>n,'predescent point control')

def verify_escape(row,seed):
    t=row['t'];nat(t)
    n=303+(1<<10)*3**28*t;m=27+(1<<51)*t
    C=128+16*3**31*t
    check([row['n'],row['m'],row['C']]==[n,m,C])
    w,z=seed['words'];E,states=replay(n,w)
    check(replay(m,z)[0]==E==row['endpoint']==1154+16*3**33*t)
    check(min(states[1:])==row['minimum']>n)
    check(10*m<n and n%3==0 and n%16==15 and n%32==15)
    check(C%16==0 and (3*C-2)%4==2 and (3*C-1)%2==1)
    check((n+5)%8==4,'burst exclusion')

def verify_drift(row):
    n,m,s,q,mu,times=row;nat(n,3);check(n%2 and m==(n-1)//2)
    xs,qs,_=path(n);ys,ps,z=path(m)
    check([s,q]==[len(z),ps[-1]])
    actual_mu=max([2*v-i for i,v in enumerate(ps)]+[2*q-s+1])
    check(mu==actual_mu,'incorrect anchor balance budget')
    actual=[]
    for a in range(1,len(xs)):
        if xs[a]<n:break
        actual.append([a,qs[a],xs[a]])
    check(times==actual,'missing prefix observations')
    for a,odds,x in times:
        # Finite floor hypothesis; exact rational 1/7 inequality.
        check(7*(2*odds-a)>a,'charge lower bound')
        check((3*n+1)**odds >= (1<<a)*n**odds,'finite floor product bound')
        for b in [0,1,s//2,s,s+1,s+10]:
            y=m;p=0
            for _ in range(b):p+=y%2;y=T(y)
            check(2*p-b<=mu,'global companion budget')
            check(7*(2*(odds-p)+(b-a)+mu)>a,'projective mismatch')

def reject(f,row,alter):
    bad=copy.deepcopy(row);alter(bad)
    try:f(bad)
    except (ValueError,KeyError,TypeError,IndexError):return 1
    raise ValueError('corrupt semantic control accepted')

def self_test(obj):
    count=0
    h=obj['H_grid'][127]
    for i,value in [(0,True),(1,h[1]+1),(2,h[2]+1),(3,h[3]+2),(4,h[4]+1),(5,h[5]+2),(6,'uniform')]:
        count+=reject(verify_H,h,lambda r,i=i,v=value:r.__setitem__(i,v))
    f=next(r for r in obj['families'] if r['status']=='uniform_at_point')
    for mutate in [lambda r:r['values'].__setitem__(0,r['values'][0]+1),
                   lambda r:r['weighted_charges'].__setitem__(0,r['weighted_charges'][0]+1),
                   lambda r:r['words'].__setitem__(0,r['words'][0]+'0'),
                   lambda r:r['progression'].__setitem__(1,2*r['progression'][1]),
                   lambda r:r.__setitem__('status','isolated_at_forced_clocks')]:
        count+=reject(verify_family,f,mutate)
    l=obj['seed']
    for mutate in [lambda r:r.__setitem__('m',r['m']+1),
                   lambda r:r.__setitem__('n',True),
                   lambda r:r.__setitem__('endpoint',r['endpoint']+1),
                   lambda r:r['steps'].__setitem__(0,2*r['steps'][0]),
                   lambda r:r['steps'].__setitem__(1,r['steps'][1]+1),
                   lambda r:r.__setitem__('order_last_parameter',0),
                   lambda r:r.__setitem__('all_prefix_coefficients_above_one',False)]:
        count+=reject(verify_lift,l,mutate)
    count+=reject(verify_drift,obj['drift'][12],lambda r:r.__setitem__(4,r[4]+1))
    count+=reject(verify_drift,obj['drift'][12],lambda r:r[5].append([100,50,999]))
    count+=reject(verify_lift,obj['control_lifts'][0],lambda r:r.__setitem__('order_last_parameter',None))
    try:json.loads('{"x":1,"x":2}',object_pairs_hook=object_no_duplicates)
    except ValueError:count+=1
    else:raise ValueError('duplicate accepted')
    return count

def verify(obj):
    typed_tree(obj)
    check(obj['schema']=='PSS-1')
    check(len(obj['H_grid'])==65536)
    for c,row in enumerate(obj['H_grid'],1):check(row[0]==c);verify_H(row)
    # Exact requested family inventory is authenticated separately from validity.
    forms=[[[9,2],[1,0]],[[8,-5],[4,-1],[3,-5]],[[1,1],[1,2],[1,3],[1,4]],
           [[5,1],[30,-3],[90,7]],[[1,1],[5,1]],[[2,1],[1,2]],[[12,-1],[18,-5],[27,2]]]
    inventory=[(f,t) for f in forms for t in range(1,65) if min(a*t+b for a,b in f)>0]
    inventory += [([[1,1],[1,1<<k]],0) for k in range(1,33)]
    check([(r['forms'],r['point']) for r in obj['families']]==inventory)
    for row in obj['families']:verify_family(row)
    verify_lift(obj['seed']);check(obj['seed']['n']==303 and obj['seed']['m']==27)
    for row in obj['control_lifts']:verify_lift(row)
    check([r['t'] for r in obj['escape']]==[0,1,2,3,7,31,255,2**64,2**128,2**256])
    for row in obj['escape']:verify_escape(row,obj['seed'])
    check(len(obj['root_mine'])==4095)
    for n,row in enumerate(obj['root_mine'],2):
        check(row['source']==n)
        check(row['status'] in ['infinite_family','finite_parameter_segment','no_hit_before_coefficient_crossing'])
        if row['status']!='no_hit_before_coefficient_crossing':
            c=row['certificate'];check(c['n']==n);verify_lift(c)
            check(c['all_prefix_coefficients_above_one'])
            check((c['order_last_parameter'] is None)==(row['status']=='infinite_family'))
    check([r[0] for r in obj['drift']]==list(range(3,2050,2)))
    for row in obj['drift']:verify_drift(row)
    return dict(schema='PSS-1',
                sha256=hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
                H_grid=len(obj['H_grid']),H_counts=dict(sorted(Counter(r[6] for r in obj['H_grid']).items())),
                H_ternary_counts=dict(sorted(Counter(r[6] for r in obj['H_grid'] if r[0]%3==2).items())),
                families=len(obj['families']),family_counts=dict(sorted(Counter(r['status'] for r in obj['families']).items())),
                root_mine=len(obj['root_mine']),root_counts=dict(sorted(Counter(r['status'] for r in obj['root_mine']).items())),
                escape_examples=len(obj['escape']),drift_sources=len(obj['drift']),
                drift_observations=sum(len(r[5])*6 for r in obj['drift']),
                scope='finite exact corpus, not universal convergence or independent review')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('full',type=Path)
    p.add_argument('--summary',type=Path);p.add_argument('--self-test',action='store_true');a=p.parse_args()
    obj=json.loads(a.full.read_text(),object_pairs_hook=object_no_duplicates);s=verify(obj)
    if a.summary:
        reference=json.loads(a.summary.read_text(),object_pairs_hook=object_no_duplicates)
        check(json.dumps(s,sort_keys=True)==json.dumps(reference,sort_keys=True),'summary mismatch')
    if a.self_test:s['semantic_controls_rejected']=self_test(obj)
    s['status']='PASS';print(json.dumps(s,sort_keys=True))
if __name__=='__main__':main()
