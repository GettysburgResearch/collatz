"""Global finite-transducer synthesis, not a Collatz proof.

Weights multiply binomial(position, degree). Every accepted word is a
canonical binary positive integer. LP feasibility is only a candidate;
exact rational checking and a Lean soundness theorem remain mandatory.
"""
from collections import Counter
from math import comb
from fractions import Fraction
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
import argparse, json, time


def advance(c,b,k):
    return ((c<<1)|b)&((1<<(k-1))-1)


def edge(c,b):
    return 2*c+b


def add_cost(out, context, bit, offset, sign, degree):
    # binom(i+offset,d) = sum_j binom(offset,d-j)*binom(i,j).
    for j in range(degree+1):
        for d in range(j,degree+1):
            if offset>=d-j:
                out[j][edge(context,bit)*(degree+1)+d] += sign*comb(offset,d-j)


def graph(k,degree):
    states=[]; ix={}; initials=[]; distance=[]
    for r in (0,1):
        s=(r,advance(0,r,k),0,2*r,0,0)
        ix[s]=len(states); initials.append(len(states)); states.append(s); distance.append(0)
    edges=[]; ends=[]
    for idx,s in enumerate(states):
        r,ci,co,carry,last,length=s
        for bit in (0,1):
            total=(1+2*r)*bit+carry
            ob,ncarry=total%2,total//2
            target=(r,advance(ci,bit,k),advance(co,ob,k),ncarry,bit,min(2,length+1))
            if target not in ix:
                ix[target]=len(states);states.append(target);distance.append(distance[idx]+1)
            delta=[Counter() for _ in range(degree+1)]
            add_cost(delta,co,ob,0,1,degree)
            add_cost(delta,ci,bit,1,-1,degree)
            edges.append((idx,ix[target],delta))
        # Source n=2a+r must be canonical and >2. a=0 never qualifies.
        if last!=1 or not length or (r==0 and length==1):
            continue
        delta=[Counter() for _ in range(degree+1)]
        offset=0
        while carry:
            ob,carry=carry%2,carry//2
            add_cost(delta,co,ob,offset,1,degree)
            co=advance(co,ob,k);offset+=1
        for j in range(k-1):
            add_cost(delta,co,0,offset+j,1,degree)
            co=advance(co,0,k)
            add_cost(delta,ci,0,1+j,-1,degree)
            ci=advance(ci,0,k)
        ends.append((idx,delta))
    return states,edges,ends,initials,distance


def direct_features(n,k,degree):
    bits=[]
    while n:
        bits.append(n%2);n//=2
    bits += [0]*(k-1)
    result=Counter();context=0
    for pos,b in enumerate(bits):
        for d in range(min(degree,pos)+1):
            result[edge(context,b)*(degree+1)+d] += comb(pos,d)
        context=advance(context,b,k)
    return result


def controls(k,degree):
    """Finite implementation checks; not the all-word proof obligation."""
    states,edges,ends,initials,_=graph(k,degree)
    terminals=dict(ends)
    samples=list(range(3,1024))
    samples += [(1<<p)-1 for p in (20,47,100,257)]
    samples += [(1<<p)+1 for p in (20,47,100,257)]
    for n in samples:
        r=n%2;a=n//2;i=initials[r];pos=0
        value=Counter({edge(0,r)*(degree+1):-1})
        while a:
            bit=a%2;a//=2
            src,dst,delta=edges[2*i+bit]
            if src!=i:raise RuntimeError('edge index mismatch')
            for j,row in enumerate(delta):
                if j<=pos:
                    for idx,c in row.items():value[idx]+=comb(pos,j)*c
            i=dst;pos+=1
        for j,row in enumerate(terminals[i]):
            if j<=pos:
                for idx,c in row.items():value[idx]+=comb(pos,j)*c
        t=n//2 if n%2==0 else (3*n+1)//2
        expected=direct_features(t,k,degree)
        expected.subtract(direct_features(n,k,degree))
        if any(value[z]!=expected[z] for z in value.keys()|expected.keys()):
            raise RuntimeError(('polynomial transducer mismatch',k,degree,n))
    return len(samples)


def solve(k,degree,signed=False,timeout=30):
    start=time.monotonic()
    states,edges,ends,initials,distance=graph(k,degree)
    stride=degree+1;nweights=(1<<k)*stride;ns=len(states)
    nlower=(1<<(k-1))*stride if signed else 0
    nv=nweights+ns*stride+nlower
    H=lambda s,d:nweights+s*stride+d
    L=lambda c,d:nweights+ns*stride+c*stride+d
    rows=[];rhs=[]
    def add_nonpositive_polynomial(poly,shift):
        # It suffices to make every binomial-basis coefficient nonpositive
        # after translating to the minimum reachable scan position.
        for u in range(stride):
            row=Counter()
            for d in range(u,stride):
                if shift>=d-u:
                    for v,c in poly[d].items():row[v]+=comb(shift,d-u)*c
            rows.append(row);rhs.append(0)
    for src,dst,delta in edges:
        poly=[]
        for d in range(stride):
            row=Counter(delta[d]);row[H(dst,d)]+=1;row[H(src,d)]-=1
            if d<degree:row[H(dst,d+1)]+=1
            poly.append(row)
        add_nonpositive_polynomial(poly,distance[src])
    for s,delta in ends:
        poly=[]
        for d in range(stride):
            row=Counter(delta[d]);row[H(s,d)]-=1
            poly.append(row)
        add_nonpositive_polynomial(poly,distance[s])
    for r,s in enumerate(initials):
        rows.append(Counter({H(s,0):1,edge(0,r)*stride:-1}));rhs.append(-1)
    if signed:
        for c in range(1<<(k-1)):
            for b in (0,1):
                nc=advance(c,b,k)
                poly=[]
                for d in range(stride):
                    # w_d + lower_next_d + lower_next_(d+1) - lower_c_d >=0.
                    row=Counter({edge(c,b)*stride+d:-1})
                    row[L(nc,d)]-=1;row[L(c,d)]+=1
                    if d<degree:row[L(nc,d+1)]-=1
                    poly.append(row)
                add_nonpositive_polynomial(poly,c.bit_length())
    rr=[];cc=[];vv=[]
    for r,row in enumerate(rows):
        for c,v in row.items():
            if v:rr.append(r);cc.append(c);vv.append(v)
    mat=coo_matrix((vv,(rr,cc)),shape=(len(rows),nv)).tocsr()
    bounds=([(None,None)]*nweights if signed else [(0,None)]*nweights)+[(None,None)]*(ns*stride+nlower)
    if signed:
        for d in range(stride):bounds[L(0,d)]=(0,0)
    res=linprog([0]*nv,A_ub=mat,b_ub=rhs,bounds=bounds,method='highs',options={'time_limit':timeout})
    report={'k':k,'degree':degree,'signed':signed,'reachable_position_translation':True,'states':ns,'variables':nv,'constraints':len(rows),'status':int(res.status),'message':res.message,'seconds':round(time.monotonic()-start,3)}
    if res.success:
        exact=[Fraction(float(z)).limit_denominator(1000000) for z in res.x]
        okay=all(sum(exact[j]*v for j,v in row.items())<=bound for row,bound in zip(rows,rhs))
        if not signed:okay=okay and all(x>=0 for x in exact[:nweights])
        if signed:okay=okay and all(exact[L(0,d)]==0 for d in range(stride))
        report.update(exact_inequalities=okay,solution=[str(x) for x in exact])
    return report


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--max-k',type=int,default=6);p.add_argument('--degree',type=int,default=1);p.add_argument('--signed',action='store_true');p.add_argument('--controls-only',action='store_true');p.add_argument('--output',default='search.json');args=p.parse_args()
    results=[]
    for k in range(1,args.max_k+1):
        cases=controls(k,args.degree)
        result={'k':k,'degree':args.degree,'control_cases':cases,'scope':'finite implementation controls only'} if args.controls_only else solve(k,args.degree,args.signed)
        result['control_cases']=cases
        results.append(result)
        print(json.dumps({key:value for key,value in result.items() if key!='solution'}),flush=True)
        with open(args.output,'w') as f:json.dump({'scope':'global transducer synthesis; not a proof','results':results},f,indent=2)
        if result.get('status')==0:break
