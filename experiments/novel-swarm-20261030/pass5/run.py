#!/usr/bin/env python3
"""Exact finite-state checks for polynomial-digit Collatz rigidity.

No Collatz-convergence assumption. A finite automaton is checked on ALL
positive sources through a complete arithmetic product graph. Modular
invariance of a rational polynomial machine is NOT exact invariance over Q.
"""
from __future__ import annotations
import argparse
from collections import deque
from fractions import Fraction
from itertools import product
import json, math, hashlib
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def T(n: int) -> int:
    need(type(n) is int and n > 0, 'positive integer source required')
    return (3*n+1)//2 if n&1 else n//2


def digits(n: int, base: int) -> list[int]:
    need(type(n) is int and n >= 0 and type(base) is int and base >= 2, 'bad digits')
    if not n:
        return [0]
    a=[]
    while n:
        n,r=divmod(n,base); a.append(r)
    return a[::-1]


def evaluation(machine: dict, n: int) -> int:
    q=machine['initial']
    for d in digits(n,machine['base']):
        q=machine['transitions'][q][d]
    return machine['outputs'][q]


def validate_machine(m: dict) -> None:
    b=m['base']; ts=m['transitions']; out=m['outputs']; q=m['initial']
    need(type(b) is int and b>=2,'bad base')
    need(len(ts)==len(out)>0 and type(q) is int and 0<=q<len(ts),'bad states')
    need(all(len(row)==b and all(type(x) is int and 0<=x<len(ts) for x in row) for row in ts),'bad transition')
    need(all(type(x) is int for x in out),'integer output labels required')


def padded_step(m: dict, q: int, digit: int) -> int:
    """-1 means canonical representation has not started; ignore padding zeros."""
    return -1 if q==-1 and digit==0 else m['transitions'][m['initial'] if q==-1 else q][digit]


def relation(m: dict, multiplier: int, addend: int, threshold: int,
             odd_only: bool, retain: bool=False) -> dict:
    """Decide f(multiplier*n+addend)=f(n) for n>=threshold (odd if requested).

    Read both words MSB first, with backwards carries. Input may be padded
    on the left. The output must start nonzero. State cap=min(prefix,threshold)
    enforces the source threshold. Queue exhaustion is a complete finite check.
    """
    validate_machine(m)
    need(multiplier in (2,3) and addend in (0,1) and threshold>=1,'bad relation')
    b=m['base']; init=(-1,-1,0,0,0)
    nodes=[init]; prev=[None]; seen={init:0}; queue=deque([0]); witness=None
    while queue:
        i=queue.popleft(); q,r,upper,par,cap=nodes[i]
        if q!=-1 and r!=-1 and upper==addend and cap==threshold and (not odd_only or par==1):
            if m['outputs'][q]!=m['outputs'][r]:
                ds=[]; es=[]; j=i
                while prev[j] is not None:
                    j0,d,e=prev[j]; ds.append(d); es.append(e); j=j0
                ds.reverse(); es.reverse()
                n=0; y=0
                for d,e in zip(ds,es): n=b*n+d; y=b*y+e
                need(y==multiplier*n+addend,'carry reconstruction')
                need(n>=threshold and (not odd_only or n&1),'source domain')
                witness={'n':n,'image':y,'input_digits':ds,'output_digits':es,
                         'values':[evaluation(m,n),evaluation(m,y)]}
                break
        for d in range(b):
            for lower in range(multiplier+1):
                e=multiplier*d+lower-b*upper
                if not 0<=e<b or (i==0 and e==0):
                    continue
                nxt=(padded_step(m,q,d),padded_step(m,r,e),lower,
                     (b*par+d)%2,min(threshold,b*cap+d))
                if nxt not in seen:
                    seen[nxt]=len(nodes); nodes.append(nxt); prev.append((i,d,e)); queue.append(len(nodes)-1)
    ans={'multiplier':multiplier,'addend':addend,'threshold':threshold,'odd_only':odd_only,
         'states_seen':len(nodes),'witness':witness}
    if retain and witness is None:
        ans['closed_states']=[list(x) for x in nodes]
    return ans


def invariant_check(m: dict, floor: int, retain: bool=False) -> dict:
    need(type(floor) is int and floor>=1,'bad floor')
    d=relation(m,2,0,(floor+1)//2,False,retain)
    if d['witness'] is not None:
        s=d['witness']['image']; ans={'status':'VIOLATION','source':s,'image':T(s),'relations':[d]}
    else:
        o=relation(m,3,1,floor,True,retain)
        if o['witness'] is None:
            return {'status':'INVARIANT_ABOVE_FLOOR','relations':[d,o]}
        n=o['witness']['n']; z=T(n)
        s=n if evaluation(m,n)!=evaluation(m,z) else 3*n+1
        ans={'status':'VIOLATION','source':s,'image':T(s),'relations':[d,o]}
    need(ans['source']>=floor and evaluation(m,ans['source'])!=evaluation(m,ans['image']),'actual edge')
    ans['values']=[evaluation(m,ans['source']),evaluation(m,ans['image'])]
    return ans


def compare(a: dict,b: dict) -> dict:
    """Exact equivalence on canonical positive words, not finite sampling."""
    need(a['base']==b['base'],'base mismatch')
    base=a['base']; seen=set(); queue=deque()
    for d in range(1,base):
        q=a['transitions'][a['initial']][d]; r=b['transitions'][b['initial']][d]
        if (q,r) not in seen: seen.add((q,r)); queue.append((q,r,d))
    while queue:
        q,r,n=queue.popleft()
        if a['outputs'][q]!=b['outputs'][r]: return {'equal':False,'source':n,'states':len(seen)}
        for d in range(base):
            pair=(a['transitions'][q][d],b['transitions'][r][d])
            if pair not in seen: seen.add(pair); queue.append((*pair,base*n+d))
    return {'equal':True,'states':len(seen)}


def oddpart(n: int)->int:
    while n and n%2==0:n//=2
    return n


def power_two(b:int)->bool:
    return b>0 and b&(b-1)==0


def finite_pattern(base:int, table:list[int], constant:int)->dict:
    cap=len(table)
    ts=[[min(cap,base*q+d) for d in range(base)] for q in range(cap+1)]
    return {'base':base,'initial':0,'transitions':ts,'outputs':table+[constant]}


def canonical_model(m:dict,floor:int)->dict:
    """The classification's explicit candidate, then checked by compare()."""
    k=(floor+1)//2; b=m['base']
    probe=next(n for n in range(floor,floor+6) if n%2 and n%3)
    c=evaluation(m,probe)
    small=[0]+[evaluation(m,n) for n in range(1,k)]
    if not power_two(b):return finite_pattern(b,small,c)
    roots=[n for n in range(1,floor,2) if n%3==0]
    labels={}
    for n in roots:
        v=n
        while v<k:v*=2
        labels[n]=evaluation(m,v)
    return ray_model(b,floor,c,labels,{n:small[n] for n in range(1,k)})


def ray_model(base:int,floor:int,constant:int,labels:dict[int,int],small:dict[int,int])->dict:
    need(power_two(base),'ray constructor is for power-of-two bases')
    k=(floor+1)//2; top=max([k,*labels],default=k)
    roots=sorted(labels); tail={m:top+1+j for j,m in enumerate(roots)}; dead=top+1+len(roots)
    ts=[]; out=[]
    for n in range(top+1):
        row=[]
        for d in (0,1):
            z=2*n+d
            if z<=top: row.append(z)
            elif d==0 and oddpart(n) in labels:row.append(tail[oddpart(n)])
            else:row.append(dead)
        ts.append(row)
        out.append(small.get(n,constant) if n<k else labels.get(oddpart(n),constant))
    for root in roots:ts.append([tail[root],dead]);out.append(labels[root])
    ts.append([dead,dead]);out.append(constant)
    width=base.bit_length()-1; grouped=[]
    for q in range(len(ts)):
        row=[]
        for d in range(base):
            s=q
            for j in range(width-1,-1,-1):s=ts[s][(d>>j)&1]
            row.append(s)
        grouped.append(row)
    return {'base':base,'initial':0,'transitions':grouped,'outputs':out}


def dfao_track()->dict:
    summary=[]; certificates=[]
    for base,states in [(2,2),(3,2),(4,2),(2,3)]:
        counts={str(f):{'invariant':0,'violated':0} for f in (1,4,8)}
        total=0; product_states=0
        for flat in product(range(states),repeat=base*states):
            ts=[list(flat[i*base:(i+1)*base]) for i in range(states)]
            for out in product((0,1),repeat=states):
                machine={'base':base,'initial':0,'transitions':ts,'outputs':list(out)}; total+=1
                for floor in (1,4,8):
                    check=invariant_check(machine,floor)
                    if check['status']=='VIOLATION':counts[str(floor)]['violated']+=1
                    else:
                        counts[str(floor)]['invariant']+=1
                        cmp=compare(machine,canonical_model(machine,floor))
                        need(cmp['equal'],'classification counterexample')
                        product_states+=cmp['states']
        summary.append({'base':base,'states':states,'machines':total,'floors':counts,'equivalence_states':product_states})
    for base in (2,4,8):
        floor=32
        m=ray_model(base,floor,0,{3:1,9:2,15:3,21:4,27:5},{1:7,2:8,5:9})
        cert=invariant_check(m,floor,True)
        need(cert['status']=='INVARIANT_ABOVE_FLOOR','sharp ray control')
        certificates.append({'name':f'sharp_rays_base_{base}','floor':floor,'machine':m,'check':cert})
    for base in (3,5,10):
        floor=17;m=finite_pattern(base,[0,9,8,7,6,5,4,3,2],1)
        cert=invariant_check(m,floor,True)
        need(cert['status']=='INVARIANT_ABOVE_FLOOR','small support control')
        certificates.append({'name':f'small_support_base_{base}','floor':floor,'machine':m,'check':cert})
    # A truncated ray in a multiplicatively independent base is not tail invariant.
    m=finite_pattern(3,[int(oddpart(n)==3) for n in range(82)],0)
    cert=invariant_check(m,8)
    need(cert['status']=='VIOLATION','base-3 truncated ray')
    certificates.append({'name':'base3_truncated_ray','floor':8,'machine':m,'check':cert})
    return {'summary':summary,'certificates':certificates}


def polynomial_machine(base:int,prime:int,initial:tuple,step,output)->dict:
    vals=[initial];ix={initial:0};ts=[];out=[]
    for state in vals:
        row=[]
        for d in range(base):
            nxt=tuple(x%prime for x in step(state,d))
            if nxt not in ix:ix[nxt]=len(vals);vals.append(nxt)
            row.append(ix[nxt])
        ts.append(row);out.append(output(state)%prime)
    return {'base':base,'initial':0,'transitions':ts,'outputs':out},[list(v) for v in vals]


def nonlinear_track()->dict:
    records=[]
    for base in (2,3,5,10):
        for p in (3,5,7):
            kinds=[('quadratic',lambda x,d:(x[0]*x[0]+d,),lambda x:x[0],(2%p,)),
                   ('coupled',lambda x,d:(x[0]*x[0]+x[1]+d,x[0]*x[1]+1),lambda x:x[0]+2*x[1],(1,2%p))]
            for kind,step,out,init in kinds:
                m,states=polynomial_machine(base,p,init,step,out)
                chk=invariant_check(m,1)
                records.append({'kind':kind,'base':base,'prime':p,'states':states,'machine':m,'check':chk})
    # A one-dimensional degree-K polynomial in the digit count stays zero
    # until length K. Carries expose a huge actual source without a source scan.
    for base,K,p in [(2,64,67),(2,512,521),(3,128,131)]:
        def output(x,K=K,p=p):
            return math.prod((x[0]-j)%p for j in range(K))*pow(math.factorial(K),-1,p)%p
        m,states=polynomial_machine(base,p,(0,),lambda x,d:(x[0]+1,),output)
        chk=invariant_check(m,1)
        need(chk['status']=='VIOLATION','delayed nonlinear witness')
        records.append({'kind':'length_binomial','base':base,'K':K,'prime':p,'states':states,'machine':m,'check':chk})
    # Polynomial automorphisms remain permutations after finite reduction.
    for base in (2,3):
        for p in (3,5,7):
            m,states=polynomial_machine(base,p,(1,2%p),lambda x,d:(x[1],x[0]+x[1]**2+d),lambda x:x[0])
            for d in range(base):need(len({row[d] for row in m['transitions']})==len(states),'reversible finite map')
            chk=invariant_check(m,32)
            need(chk['status']=='VIOLATION','reversible tail witness')
            records.append({'kind':'henon','base':base,'prime':p,'floor':32,'states':states,'machine':m,'check':chk})
    # A bad specialization can erase a genuine defect: retain this control.
    m,states=polynomial_machine(2,2,(0,),lambda x,d:(2*x[0]+d,),lambda x:2*x[0])
    bad=invariant_check(m,1,True)
    need(bad['status']=='INVARIANT_ABOVE_FLOOR','bad-prime control')
    return {'records':records,'bad_prime_control':{'prime':2,'machine':m,'states':states,'check':bad,
            'rational_witness':{'source':2,'image':1,'values':[4,2]}},
            'nilpotent_control':{'ring':'F2[e]/(e^2)','machine':{'base':2,'initial':0,'transitions':[[0,1],[0,1]],'outputs':[0,2]},
                                 'check':invariant_check({'base':2,'initial':0,'transitions':[[0,1],[0,1]],'outputs':[0,2]},1)}}


def mul_poly(a:list[Fraction],b:list[Fraction])->list[Fraction]:
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def interpolate(values:list[Fraction])->list[Fraction]:
    """Newton interpolation on 0,...,M; exact rational power coefficients."""
    a=values[:]; diffs=[]
    while a:
        diffs.append(a[0]);a=[a[i+1]-a[i] for i in range(len(a)-1)]
    ans=[Fraction(0)]*len(values);basis=[Fraction(1)]
    for k,v in enumerate(diffs):
        for j,c in enumerate(basis):ans[j]+=v*c
        basis=[x/Fraction(k+1) for x in mul_poly(basis,[Fraction(-k),Fraction(1)])]
    return ans


def horner(poly:list[Fraction],x:int)->Fraction:
    v=Fraction(0)
    for c in reversed(poly):v=v*x+c
    return v


def capped(n:int,K:int)->int:
    for j in range(K):
        if n==1:return j
        n=T(n)
    return K


def ideal_certificate()->dict:
    """Universal integer-polynomial identity, using coefficient arithmetic."""
    def add(*polys):
        z={}
        for poly in polys:
            for k,v in poly.items():z[k]=z.get(k,0)+v
        return {k:v for k,v in z.items() if v}
    def scale(p,c):return {k:c*v for k,v in p.items() if c*v}
    def mul(p,q):
        z={}
        for (i,j),v in p.items():
            for (k,l),w in q.items():z[i+k,j+l]=z.get((i+k,j+l),0)+v*w
        return {k:v for k,v in z.items() if v}
    def pw(p,n):
        z={(0,0):1}
        for _ in range(n):z=mul(z,p)
        return z
    one={(0,0):1};a={(1,0):1};b={(0,1):1};b2=pw(b,2)
    def output(n):
        x={}
        for d in digits(n,2):x=mul(a,x) if d==0 else add(mul(b,x),one)
        return pw(x,2)
    sources=[2,3,5,11]
    defects={n:add(output(T(n)),scale(output(n),-1)) for n in sources}
    # The identity below uses e2=f(2)-f(1), opposite the raw T defect.
    e2=scale(defects[2],-1)
    D=add(mul(add(pw(a,2),a,one),add(mul(add(pw(a,3),one),b),scale(one,2))),
          scale(mul(b,add(mul(add(a,one),b2),scale(b,2),scale(one,2))),-1))
    E=add(pw(a,4),pw(a,2),one,scale(b2,-1));L=add(D,scale(add(b2,scale(one,2)),2))
    multipliers={2:add(scale(mul(add(b2,scale(one,2)),E),2),mul(b2,L)),
                 3:scale(L,-1),5:scale(add(b2,scale(one,2)),-2),11:scale(one,2)}
    total=add(*[mul(multipliers[n],e2 if n==2 else defects[n]) for n in sources])
    need(total==scale(b,8),'universal ideal identity')
    pack=lambda p:[[i,j,c] for (i,j),c in sorted(p.items())]
    norms={str(M):sum(abs(c)*M**(i+j) for p in multipliers.values() for (i,j),c in p.items()) for M in (1,2,4)}
    return {'family':'P0(x)=a*x; P1(x)=b*x+1; initial=0; H(x)=x^2',
            'sources':sources,'source2_sign':-1,'target':[[0,1,8]],
            'multipliers':{str(n):pack(multipliers[n]) for n in sources},'coefficient_bounds':norms}


def approximation_track()->dict:
    rows=[]; tables=[]
    for K in range(1,11):
        M=2**K; table=[K]+[capped(n,K) for n in range(1,M)]+[K]
        # Above M the value is exactly K. Both n and T(n)>=M when n>=2M,
        # so all possible defects are captured by this exact finite range.
        f=lambda n:table[min(n,M)]
        defects=[abs(f(n)-f(T(n))) for n in range(1,2*M)]
        need(max(defects)==1 and f(1)==0 and f(M)==K,'capped-clock global defect')
        rows.append({'K':K,'cap':M,'finite_edge_checks':2*M-1,'maximum_numerator_defect':max(defects),
                     'witness':1,'range':[0,K]})
        if K<=5:
            pols=[interpolate([Fraction(min(2*j+d,M)) for j in range(M+1)]) for d in (0,1)]
            h=interpolate([Fraction(t,K) for t in table])
            for j in range(M+1):
                for d in (0,1):need(horner(pols[d],j)==min(2*j+d,M),'transition interpolation')
                need(horner(h,j)==Fraction(table[j],K),'output interpolation')
            tables.append({'K':K,'table':table,'transition_coefficients':[[[x.numerator,x.denominator] for x in a] for a in pols],
                           'output_coefficients':[[x.numerator,x.denominator] for x in h]})
    return {'rows':rows,'polynomial_certificates':tables,'ideal_certificate':ideal_certificate()}


def high_ladder_track()->dict:
    cases=[]
    for floor in (1,8,31,128):
        for n in range(floor,floor+48):
            if n%3==0:continue
            x=n;edges=[]
            for _ in range(32):
                choices=(3,5,7) if x%3==2 else (4,6,8)
                a=next(a for a in choices if ((2**a*x-1)//3)%3)
                y=(2**a*x-1)//3
                need(y>=2*x and y%2==1 and y%3,'high inverse source')
                z=y;low=z
                for __ in range(a):z=T(z);low=min(low,z)
                need(z==x and low>=floor,'high inverse replay')
                edges.append([x,a,y]);x=y
            cases.append({'floor':floor,'source':n,'edges':edges})
    return {'cases':cases}


def main()->None:
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--serial',action='store_true');a=p.parse_args()
    tracks=[dfao_track,nonlinear_track,approximation_track,high_ladder_track]
    if a.serial:res=[f() for f in tracks]
    else:
        with ProcessPoolExecutor(max_workers=4) as pool:res=[r.result() for r in [pool.submit(f) for f in tracks]]
    obj={'schema':'collatz-polynomial-rigidity-pass5-v1','dfao':res[0],'nonlinear':res[1],'approximation':res[2],'ladders':res[3]}
    data=json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n';Path(a.output).write_text(data,encoding='utf8')
    summary={'sha256':hashlib.sha256(data.encode()).hexdigest(),'bytes':len(data.encode()),
             'automata':sum(r['machines'] for r in res[0]['summary']),
             'infinite_domain_checks':3*sum(r['machines'] for r in res[0]['summary']),
             'nonlinear_models':len(res[1]['records']),
             'ladder_edges':sum(len(r['edges']) for r in res[3]['cases']),
             'delayed_witnesses':[{'base':r['base'],'K':r['K'],'source':r['check']['source'],
                 'states_seen':sum(v['states_seen'] for v in r['check']['relations'])} for r in res[1]['records'] if r['kind']=='length_binomial']}
    print(json.dumps(summary,sort_keys=True))

if __name__=='__main__':main()
