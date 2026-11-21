"""Exact all-length synthesis with position-periodic binary context costs.

This expands fixed_clock_ranking.py by assigning separate local costs at
positions modulo h, and an independent terminal-context correction. A
finite graph coboundary makes the resulting rational potential bounded
below on every positive binary word. Success requires exact reconstruction.
"""

from collections import Counter
from fractions import Fraction
import argparse
import hashlib
import json
import time
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

SOURCE_SHA256=hashlib.sha256(open(__file__,'rb').read()).hexdigest()


def T(n):
    return n//2 if n%2==0 else (3*n+1)//2


def iterate(n,q):
    p=0
    for _ in range(q):
        p+=n%2
        n=T(n)
    return n,p


def addbit(c,b,k):
    return ((c<<1)|b)&((1<<(k-1))-1)


def weight(c,b,j,k,h):
    return (j%h)*(1<<k)+2*c+b


def boundary(c,j,k,h):
    return (j%h)*(1<<(k-1))+c


def features(n,k,h):
    c=j=0
    d=Counter()
    while n:
        b=n&1
        n>>=1
        d[weight(c,b,j,k,h)]+=1
        c=addbit(c,b,k)
        j+=1
    return d,boundary(c,j,k,h)


def initial(r,q,k,h):
    end,p=iterate(r,q)
    ci=0
    d=Counter()
    for j in range(q):
        b=(r>>j)&1
        d[weight(ci,b,j,k,h)]-=1
        ci=addbit(ci,b,k)
    return (3**p,ci,0,end,0,False,0),d


def advance(s,b,q,k,h):
    M,ci,co,carry,_,_,j=s
    total=M*b+carry
    out,carry=total&1,total>>1
    d=Counter()
    d[weight(ci,b,q+j,k,h)]-=1
    d[weight(co,out,j,k,h)]+=1
    ci=addbit(ci,b,k)
    co=addbit(co,out,k)
    return (M,ci,co,carry,b,True,(j+1)%h),d


def finish(s,q,k,h):
    _,ci,co,carry,last,nonempty,j=s
    if not last or not nonempty:
        return None
    d=Counter()
    in_boundary=boundary(ci,q+j,k,h)
    while carry:
        out=carry&1
        carry>>=1
        d[weight(co,out,j,k,h)]+=1
        co=addbit(co,out,k)
        j+=1
    return d,in_boundary,boundary(co,j,k,h)


def graph(q,k,h,state_limit):
    states=[]
    ids={}
    roots=[]
    for r in range(1<<q):
        s,d=initial(r,q,k,h)
        if s not in ids:
            ids[s]=len(states)
            states.append(s)
        roots.append((ids[s],d))
    edges=[]
    for i,s in enumerate(states):
        for b in (0,1):
            t,d=advance(s,b,q,k,h)
            if t not in ids:
                ids[t]=len(states)
                states.append(t)
                if len(states)>state_limit:
                    raise RuntimeError(f'state limit {state_limit} exceeded')
            edges.append((i,ids[t],d))
    ends=[]
    for i,s in enumerate(states):
        f=finish(s,q,k,h)
        if f is not None:
            ends.append((i,*f))
    return states,roots,edges,ends


def controls(q,k,h):
    for n in range(1<<q,(1<<q)+4096):
        s,d=initial(n% (1<<q),q,k,h)
        d=d.copy()
        a=n>>q
        while a:
            s,e=advance(s,a&1,q,k,h)
            d.update(e)
            a>>=1
        e,bi,bo=finish(s,q,k,h)
        d.update(e)
        target,_=iterate(n,q)
        fi,wi=features(n,k,h)
        fo,wo=features(target,k,h)
        fo.subtract(fi)
        if bi!=wi or bo!=wo or any(d[x]!=fo[x] for x in d.keys()|fo.keys()):
            raise AssertionError(('feature transducer mismatch',q,k,h,n))


def solve(q,k,h,seconds,state_limit,reduced=False):
    start=time.monotonic()
    states,roots,edges,ends=graph(q,k,h,state_limit)
    nw=h*(1<<k)
    ns=len(states)
    ng=h*(1<<(k-1))
    nb=0 if reduced else ng
    gi=nw+ns+nb
    nv=gi+ng
    matrix=[]
    rhs=[]
    for i,j,d in edges:
        row=Counter(d)
        row[nw+i]+=1
        row[nw+j]-=1
        matrix.append(row)
        rhs.append(0)
    for i,d in roots:
        row=Counter(d)
        row[nw+i]-=1
        matrix.append(row)
        rhs.append(0)
    for i,d,ci,co in ends:
        row=Counter(d)
        row[nw+i]+=1
        row[gi+co]+=1
        row[gi+ci]-=1
        matrix.append(row)
        rhs.append(-1)
    for n in range(3,1<<q):
        target,_=iterate(n,q)
        row,co=features(target,k,h)
        fi,ci=features(n,k,h)
        row.subtract(fi)
        row[gi+co]+=1
        row[gi+ci]-=1
        matrix.append(row)
        rhs.append(-1)
    # A finite graph coboundary bounds the potential below for all lengths.
    if not reduced:
        for j in range(h):
            for c in range(1<<(k-1)):
                for b in (0,1):
                    row=Counter({weight(c,b,j,k,h):-1})
                    row[nw+ns+boundary(addbit(c,b,k),j+1,k,h)]+=1
                    row[nw+ns+boundary(c,j,k,h)]-=1
                    matrix.append(row)
                    rhs.append(0)
    rows=[]
    cols=[]
    values=[]
    for i,row in enumerate(matrix):
        for j,v in row.items():
            if v:
                rows.append(i)
                cols.append(j)
                values.append(v)
    A=coo_matrix((values,(rows,cols)),shape=(len(matrix),nv)).tocsr()
    bounds=([(0,None)]*nw if reduced else [(None,None)]*nw)+[(None,None)]*(nv-nw)
    res=linprog([0]*nv,A_ub=A,b_ub=rhs,bounds=bounds,
                method='highs',options={'time_limit':seconds})
    report={'q':q,'k':k,'position_period':h,'reduced_gauge':reduced,'states':ns,'edges':len(edges),
            'constraints':len(matrix),'variables':nv,'status':int(res.status),
            'message':res.message,'seconds':round(time.monotonic()-start,3)}
    if res.success:
        exact=[Fraction(float(x)).limit_denominator(1000000) for x in res.x]
        valid=all(sum(exact[j]*v for j,v in row.items())<=bound for row,bound in zip(matrix,rhs))
        if reduced:
            valid=valid and all(x>=0 for x in exact[:nw])
        report.update(exact_constraints_hold=valid,
                      solution=[str(x) for x in exact],
                      weights=[str(x) for x in exact[:nw]],
                      boundary_values=[str(x) for x in exact[gi:]])
    return report


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--q',nargs='+',type=int,default=[6,8])
    p.add_argument('--period',nargs='+',type=int,default=[2,3])
    p.add_argument('--max-k',type=int,default=5)
    p.add_argument('--min-k',type=int,default=1)
    p.add_argument('--time-limit',type=int,default=45)
    p.add_argument('--state-limit',type=int,default=300000)
    p.add_argument('--output',default='periodic_position_ranking_report.json')
    p.add_argument('--reduced',action='store_true')
    a=p.parse_args()
    if any(q<=0 or q%2 for q in a.q):
        raise ValueError('q must be positive and even')
    runs=[]
    for q in a.q:
        for h in a.period:
            for k in range(a.min_k,a.max_k+1):
                controls(q,k,h)
                try:
                    row=solve(q,k,h,a.time_limit,a.state_limit,a.reduced)
                except RuntimeError as exc:
                    row={'q':q,'k':k,'position_period':h,'status':'resource_limit','message':str(exc)}
                runs.append(row)
                print(json.dumps({key:value for key,value in row.items() if key!='solution'}),flush=True)
                with open(a.output,'w') as f:
                    json.dump({'scope':'global all-length synthesis; solver outcomes are research evidence, not proof declarations',
                               'source_sha256':SOURCE_SHA256,'runs':runs},f,indent=2)
                if row.get('exact_constraints_hold'):
                    raise SystemExit(0)
