#!/usr/bin/env python3
"""Standalone certificate checker. Imports no producer or repository modules.

Checks exported infinite-domain closed-state certificates, literal modular
edge witnesses, polynomial interpolation and high-floor paths. The producer's
7,176-machine census is NOT independently re-enumerated by this checker.
"""
from __future__ import annotations
import argparse,copy,hashlib,json,math
from fractions import Fraction
from pathlib import Path


def check(ok:bool,msg:str)->None:
    if not ok:raise ValueError(msg)


def integer(x,minimum=0):
    check(type(x) is int and x>=minimum,'integer/type/range');return x


def raw(n:int)->int:
    integer(n,1);return n//2 if n%2==0 else (3*n+1)//2


def word(n:int,b:int)->list[int]:
    integer(n,1);integer(b,2);digits=[]
    while n>0:digits.insert(0,n%b);n//=b
    return digits


def value(m:dict,n:int)->int:
    q=m['initial']
    for d in word(n,m['base']):q=m['transitions'][q][d]
    return m['outputs'][q]


def machine_ok(m:dict):
    b=integer(m['base'],2);s=len(m['outputs'])
    check(len(m['transitions'])==s and s>0,'machine shape')
    check(integer(m['initial'])<s,'initial')
    for row in m['transitions']:
        check(len(row)==b,'row width')
        for q in row:check(integer(q)<s,'transition range')
    for o in m['outputs']:check(type(o) is int,'output type')


def closed(m:dict,r:dict)->int:
    """Validate a closed over-approximation of all canonical arithmetic paths."""
    states=[tuple(a) for a in r['closed_states']];S=set(states)
    check(len(S)==len(states),'duplicate state')
    initial=(-1,-1,0,0,0);check(initial in S,'missing initial')
    b=m['base'];z=integer(r['multiplier'],2);h=integer(r['threshold'],1);c=integer(r['addend']);ns=len(m['outputs']);edges=0
    check(type(r['odd_only']) is bool,'parity flag type')
    check(z in (2,3) and c in (0,1) and h>=1,'relation parameters')
    for node in S:
        check(len(node)==5 and all(type(t) is int for t in node),'state types')
        q,u,carry,par,cap=node
        check(-1<=q<ns and -1<=u<ns and 0<=carry<=z and par in (0,1) and 0<=cap<=h,'state range')
        if q>=0 and u>=0 and carry==c and cap==h and (not r['odd_only'] or par==1):
            check(m['outputs'][q]==m['outputs'][u],'bad accepting state')
        # Enumerate both digits independently; determine the unique low carry.
        for a in range(b):
            for e in range(b):
                low=e+b*carry-z*a
                if not 0<=low<=z or (node==initial and e==0):continue
                q1=-1 if q==-1 and a==0 else m['transitions'][m['initial'] if q==-1 else q][a]
                u1=-1 if u==-1 and e==0 else m['transitions'][m['initial'] if u==-1 else u][e]
                nxt=(q1,u1,low,(b*par+a)&1,min(h,b*cap+a))
                check(nxt in S,'missing transition closure');edges+=1
    check(r['witness'] is None and r['states_seen']==len(S),'closure accounting')
    return edges


def invariant_certificate(m:dict,floor:int,c:dict)->tuple[int,int]:
    machine_ok(m);integer(floor,1)
    if c['status']=='VIOLATION':
        n=integer(c['source'],floor);y=integer(c['image'],1)
        check(raw(n)==y,'false actual edge')
        vals=[value(m,n),value(m,y)]
        check(vals==c['values'] and vals[0]!=vals[1],'false edge labels')
        for rel in c['relations']:
            w=rel['witness']
            if w is None:continue
            k=integer(w['n'],rel['threshold']);v=integer(w['image'],1)
            check(v==rel['multiplier']*k+rel['addend'],'false affine relation')
            check(not rel['odd_only'] or k%2==1,'false parity guard')
            check([value(m,k),value(m,v)]==w['values'] and w['values'][0]!=w['values'][1],'false affine values')
            dd=w['input_digits'];ee=w['output_digits'];check(len(dd)==len(ee)>0,'digits lengths')
            a=b=0
            for d,e in zip(dd,ee):
                check(0<=integer(d)<m['base'] and 0<=integer(e)<m['base'],'digits range')
                a=a*m['base']+d;b=b*m['base']+e
            check((a,b)==(k,v) and ee[0]>0,'digit values')
        return 1,0
    check(c['status']=='INVARIANT_ABOVE_FLOOR' and len(c['relations'])==2,'certificate status')
    a,b=c['relations']
    check((a['multiplier'],a['addend'],a['threshold'],a['odd_only'])==(2,0,(floor+1)//2,False),'even relation domain')
    check((b['multiplier'],b['addend'],b['threshold'],b['odd_only'])==(3,1,floor,True),'odd relation domain')
    return 0,closed(m,a)+closed(m,b)


def poly_model(r:dict)->None:
    m=r['machine'];p=integer(r['prime'],2)
    check(all(p%d for d in range(2,math.isqrt(p)+1)),'not prime')
    states=[tuple(a) for a in r['states']];idx={v:i for i,v in enumerate(states)}
    check(len(idx)==len(states)==len(m['outputs']),'state inventory')
    for v in states:check(all(type(x) is int and 0<=x<p for x in v),'field state')
    kind=r['kind'];check(kind in ('quadratic','coupled','henon','length_binomial'),'polynomial kind');expected_initial=(2%p,) if kind=='quadratic' else ((1,2%p) if kind in ('coupled','henon') else (0,))
    check(states[m['initial']]==expected_initial,'polynomial initial')
    for i,x in enumerate(states):
        if kind=='quadratic':o=x[0]
        elif kind=='coupled':o=(x[0]+2*x[1])%p
        elif kind=='henon':o=x[0]
        else:
            K=r['K'];check(K<p,'binomial denominator guard');o=math.comb(x[0],K)%p if x[0]>=K else 0
        check(m['outputs'][i]==o,'polynomial output')
        for digit,j in enumerate(m['transitions'][i]):
            if kind=='quadratic':nxt=((x[0]**2+digit)%p,)
            elif kind=='coupled':nxt=((x[0]**2+x[1]+digit)%p,(x[0]*x[1]+1)%p)
            elif kind=='henon':nxt=(x[1],(x[0]+x[1]**2+digit)%p)
            else:nxt=((x[0]+1)%p,)
            check(states[j]==nxt,'polynomial transition')


def first_hit_cap(n:int,K:int)->int:
    if n==1:return 0
    j=0
    while j<K:
        n=raw(n);j+=1
        if n==1:return j
    return K


def evaluate_coefficients(a:list,x:int)->Fraction:
    check(all(len(c)==2 and type(c[0]) is int for c in a),'rational coefficient type')
    return sum((Fraction(c[0],integer(c[1],1))*x**i for i,c in enumerate(a)),Fraction(0))


def ideal_identity(r:dict)->int:
    """Independent exact grid identity test, with certified separate degrees.

    Zero on a full (da+1)*(db+1) grid proves the integer polynomial is zero;
    this is not an arbitrary finite sample of the parameter space.
    """
    check(r['family']=='P0(x)=a*x; P1(x)=b*x+1; initial=0; H(x)=x^2','ideal family')
    check(r['sources']==[2,3,5,11] and r['source2_sign']==-1 and r['target']==[[0,1,8]],'ideal schema')
    da=0;db=1
    for n in r['sources']:
        terms=r['multipliers'][str(n)];seen=set()
        for i,j,c in terms:
            integer(i);integer(j);check(type(c) is int and c!=0 and (i,j) not in seen,'ideal monomial');seen.add((i,j))
        da=max(da,max(t[0] for t in terms)+2*max(word(n,2).count(0),word(raw(n),2).count(0)))
        db=max(db,max(t[1] for t in terms)+2*max(word(n,2).count(1),word(raw(n),2).count(1)))
    def output(n,a,b):
        x=0
        for digit in word(n,2):x=a*x if digit==0 else b*x+1
        return x*x
    count=0
    for a in range(da+1):
        for b in range(db+1):
            z=0
            for n in r['sources']:
                h=sum(c*a**i*b**j for i,j,c in r['multipliers'][str(n)])
                e=output(raw(n),a,b)-output(n,a,b)
                if n==2:e=-e
                z+=h*e
            check(z==8*b,'false universal ideal identity');count+=1
    for M in (1,2,4):
        C=sum(abs(c)*M**(i+j) for terms in r['multipliers'].values() for i,j,c in terms)
        check(r['coefficient_bounds'][str(M)]==C,'ideal norm bound')
    return count


def verify(obj:dict)->dict:
    check(obj['schema']=='collatz-polynomial-rigidity-pass5-v1','schema')
    summary={'literal_witnesses':0,'closed_product_edges':0,'polynomial_models':0,'interpolation_values':0,'capped_edges':0,'ladder_raw_steps':0}
    check(len(obj['dfao']['certificates'])==7,'automata certificate inventory')
    for r in obj['dfao']['certificates']:
        a,b=invariant_certificate(r['machine'],r['floor'],r['check']);summary['literal_witnesses']+=a;summary['closed_product_edges']+=b
    check(len(obj['nonlinear']['records'])==33,'nonlinear inventory')
    for r in obj['nonlinear']['records']:
        poly_model(r);a,b=invariant_certificate(r['machine'],r.get('floor',1),r['check'])
        if r['kind']=='henon':
            for d in range(r['base']):check(len({a[d] for a in r['machine']['transitions']})==len(r['states']),'nonreversible finite map')
        summary['polynomial_models']+=1;summary['literal_witnesses']+=a;summary['closed_product_edges']+=b
    r=obj['nonlinear']['bad_prime_control']
    a,b=invariant_certificate(r['machine'],1,r['check']);summary['closed_product_edges']+=b
    check(r['rational_witness']=={'source':2,'image':1,'values':[4,2]},'bad prime witness')
    r=obj['nonlinear']['nilpotent_control'];check(r['ring']=='F2[e]/(e^2)','nilpotent ring')
    check(r['machine']['transitions']==[[0,1],[0,1]] and r['machine']['outputs']==[0,2],'nilpotent table')
    a,b=invariant_certificate(r['machine'],1,r['check']);summary['literal_witnesses']+=a
    check(len(obj['approximation']['rows'])==10,'capped inventory')
    for K,r in enumerate(obj['approximation']['rows'],1):
        M=2**K;check(r['K']==K and r['cap']==M,'capped parameters')
        mx=0
        for n in range(1,2*M):
            mx=max(mx,abs(first_hit_cap(n,K)-first_hit_cap(raw(n),K)));summary['capped_edges']+=1
        check(mx==1 and r['maximum_numerator_defect']==mx,'capped defect')
    for r in obj['approximation']['polynomial_certificates']:
        K=r['K'];M=2**K;table=r['table'];check(len(table)==M+1,'table length')
        for j in range(1,M+1):check(table[j]==first_hit_cap(j,K),'capped table')
        for j in range(M+1):
            for d in (0,1):
                check(evaluate_coefficients(r['transition_coefficients'][d],j)==min(2*j+d,M),'interpolation transition');summary['interpolation_values']+=1
            check(evaluate_coefficients(r['output_coefficients'],j)==Fraction(table[j],K),'interpolation output');summary['interpolation_values']+=1
    summary['ideal_identity_grid_points']=ideal_identity(obj['approximation']['ideal_certificate'])
    check(len(obj['ladders']['cases'])==128,'ladder inventory')
    for r in obj['ladders']['cases']:
        n=r['source'];floor=r['floor'];check(n>=floor and n%3,'ladder start')
        check(len(r['edges'])==32,'ladder depth')
        for old,a,new in r['edges']:
            check(old==n and new%2==1 and new%3 and new>=2*old,'ladder continuation')
            check(3*new+1==(2**a)*old,'ladder affine')
            state=new
            for j in range(a):
                check(state>=floor,'floor breached');state=raw(state);summary['ladder_raw_steps']+=1
            check(state==old and state>=floor,'ladder endpoint');n=new
    return summary


def no_duplicates(pairs):
    d={}
    for k,v in pairs:
        check(k not in d,'duplicate JSON key');d[k]=v
    return d


def mutations(obj:dict)->int:
    tests=[]
    def trial(edit):
        v=copy.deepcopy(obj);edit(v)
        try:verify(v)
        except (ValueError,KeyError,IndexError,TypeError,ZeroDivisionError):return
        raise ValueError('accepted corrupted certificate')
    tests.append(lambda z:z['nonlinear']['records'][0]['check'].__setitem__('source',True))
    tests.append(lambda z:z['nonlinear']['records'][0]['check'].__setitem__('image',99))
    tests.append(lambda z:z['nonlinear']['records'][0]['check'].__setitem__('values',[0,0]))
    tests.append(lambda z:z['nonlinear']['records'][0].__setitem__('prime',4))
    tests.append(lambda z:z['nonlinear']['records'][0]['machine']['transitions'][0].__setitem__(0,0))
    tests.append(lambda z:z['dfao']['certificates'][0]['check']['relations'][0]['closed_states'].pop(0))
    tests.append(lambda z:z['dfao']['certificates'][0]['check']['relations'][0]['closed_states'].pop(-1))
    tests.append(lambda z:z['dfao']['certificates'][0]['check']['relations'][0]['closed_states'].append(z['dfao']['certificates'][0]['check']['relations'][0]['closed_states'][0]))
    tests.append(lambda z:z['approximation']['polynomial_certificates'][0]['table'].__setitem__(1,1))
    tests.append(lambda z:z['approximation']['polynomial_certificates'][0]['output_coefficients'][0].__setitem__(0,99))
    tests.append(lambda z:z['ladders']['cases'][0]['edges'][0].__setitem__(2,1))
    tests.append(lambda z:z['approximation']['ideal_certificate']['multipliers']['11'][0].__setitem__(2,3))
    for t in tests:trial(t)
    try:json.loads('{"x":1,"x":2}',object_pairs_hook=no_duplicates)
    except ValueError:return len(tests)+1
    raise ValueError('duplicate JSON accepted')


def main():
    p=argparse.ArgumentParser();p.add_argument('corpus');p.add_argument('--output',required=True);p.add_argument('--self-test',action='store_true');a=p.parse_args()
    rawdata=Path(a.corpus).read_bytes();obj=json.loads(rawdata,object_pairs_hook=no_duplicates)
    ans=verify(obj);ans['mutations_rejected']=mutations(obj) if a.self_test else 0
    ans['corpus_sha256']=hashlib.sha256(rawdata).hexdigest();ans['producer_census_independently_reenumerated']=False
    out=json.dumps(ans,sort_keys=True,separators=(',',':'))+'\n';Path(a.output).write_text(out,encoding='utf8');print(out,end='')

if __name__=='__main__':main()
