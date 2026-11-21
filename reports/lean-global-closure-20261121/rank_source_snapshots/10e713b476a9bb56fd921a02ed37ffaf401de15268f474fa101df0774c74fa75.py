"""Global finite-context synthesis for fixed shortcut-Collatz clocks.

Every LP constraint is an edge of an arbitrary-length binary multiplier
transducer, a legal terminal boundary, or an exact input below 2**q.
Finite-value replay checks only validate implementation; they are not the
proof domain. A feasible floating-point answer is not accepted until every
constraint is reconstructed and checked over fractions.
"""

from collections import Counter
from fractions import Fraction
import argparse
import hashlib
import json
import time
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

SOURCE_SHA256 = hashlib.sha256(open(__file__,'rb').read()).hexdigest()


def T(n):
    return n//2 if n%2 == 0 else (3*n+1)//2


def iterate(n, q):
    p = 0
    for _ in range(q):
        p += n%2
        n = T(n)
    return n, p


def edgevar(context, bit):
    return 2*context+bit


def addbit(context, bit, k):
    return ((context << 1)|bit) & ((1 << (k-1))-1)


def counts(n, k, padded=True):
    c = 0
    answer = Counter()
    while n:
        b = n & 1
        n >>= 1
        answer[edgevar(c,b)] += 1
        c = addbit(c,b,k)
    if padded:
        for _ in range(k-1):
            answer[edgevar(c,0)] += 1
            c = addbit(c,0,k)
    return answer


def final_context(n,k):
    c=0
    while n:
        c=addbit(c,n&1,k)
        n >>= 1
    return c


def initial(r, q, k):
    endpoint, p = iterate(r,q)
    c = 0
    d = Counter()
    for j in range(q):
        b = (r >> j) & 1
        d[edgevar(c,b)] -= 1
        c = addbit(c,b,k)
    # constant multiplier; input context; output context; carry;
    # last high input bit; at least one high input bit processed.
    return (3**p,c,0,endpoint,0,False), d


def advance(s, b, k):
    multiplier,ci,co,carry,_,_ = s
    total = multiplier*b+carry
    out,carry = total & 1,total >> 1
    d = Counter()
    d[edgevar(ci,b)] -= 1
    d[edgevar(co,out)] += 1
    ci = addbit(ci,b,k)
    co = addbit(co,out,k)
    return (multiplier,ci,co,carry,b,True),d


def finish(s, k, padded=True):
    _,ci,co,carry,last,nonempty = s
    if not last or not nonempty:
        return None
    d = Counter()
    while carry:
        out = carry & 1
        carry >>= 1
        d[edgevar(co,out)] += 1
        co = addbit(co,out,k)
    if padded:
        for _ in range(k-1):
            d[edgevar(ci,0)] -= 1
            d[edgevar(co,0)] += 1
            ci = addbit(ci,0,k)
            co = addbit(co,0,k)
    return d,ci,co


def graph(q, k, state_limit, boundary=False):
    states = []
    ids = {}
    roots = []
    for r in range(2**q):
        s,d = initial(r,q,k)
        if s not in ids:
            ids[s] = len(states)
            states.append(s)
        roots.append((ids[s],d))
    edges = []
    for i,s in enumerate(states):
        for b in (0,1):
            t,d = advance(s,b,k)
            if t not in ids:
                ids[t] = len(states)
                states.append(t)
                if len(states)>state_limit:
                    raise RuntimeError(f'state limit {state_limit} exceeded')
            edges.append((i,ids[t],d))
    ends = []
    for i,s in enumerate(states):
        result = finish(s,k,not boundary)
        if result is not None:
            ends.append((i,*result))
    return states,roots,edges,ends


def controls(q,k,boundary=False):
    # Include both short a=0 cases and arbitrary-length transducer examples.
    for n in range(max(3,2**q),max(3,2**q)+4096):
        r = n%(2**q)
        a = n//(2**q)
        s,d = initial(r,q,k)
        d = d.copy()
        while a:
            s,change = advance(s,a&1,k)
            a >>= 1
            d.update(change)
        end,ci,co=finish(s,k,not boundary)
        d.update(end)
        target,_ = iterate(n,q)
        want = counts(target,k,not boundary)
        want.subtract(counts(n,k,not boundary))
        if any(d[i]!=want[i] for i in d.keys()|want.keys()):
            raise AssertionError(('exact transducer mismatch',q,k,n,s,d,want))
        if boundary and (ci!=final_context(n,k) or co!=final_context(target,k)):
            raise AssertionError(('terminal context mismatch',q,k,n))


def solve(q,k,generalized=True,time_limit=60,state_limit=300000,boundary=False):
    begin = time.monotonic()
    states,roots,edges,ends = graph(q,k,state_limit,boundary)
    nw = 2**k
    ns = len(states)
    nb = 2**(k-1) if generalized else 0
    ng = 2**(k-1) if boundary else 0
    gi = nw+ns+nb
    matrix = []
    rhs = []
    # Accumulated actual P(output)-P(input) is bounded above by V(state).
    for i,j,d in edges:
        row = Counter(d)
        row[nw+i] += 1
        row[nw+j] -= 1
        matrix.append(row)
        rhs.append(0)
    for i,d in roots:
        row = Counter(d)
        row[nw+i] -= 1
        matrix.append(row)
        rhs.append(0)
    for i,d,ci,co in ends:
        row = Counter(d)
        row[nw+i] += 1
        if boundary:
            row[gi+co] += 1
            row[gi+ci] -= 1
        matrix.append(row)
        rhs.append(-1)
    # Exact boundary cases n<2**q not represented by a nonempty high word.
    for n in range(3,2**q):
        target,_ = iterate(n,q)
        row = counts(target,k,not boundary)
        row.subtract(counts(n,k,not boundary))
        if boundary:
            row[gi+final_context(target,k)] += 1
            row[gi+final_context(n,k)] -= 1
        matrix.append(row)
        rhs.append(-1)
    if generalized:
        # Every padded word is a closed path at context0. This coboundary
        # condition makes the entire potential nonnegative, despite signed w.
        for c in range(nb):
            for b in (0,1):
                j = addbit(c,b,k)
                row = Counter({edgevar(c,b):-1})
                row[nw+ns+j] += 1
                row[nw+ns+c] -= 1
                matrix.append(row)
                rhs.append(0)
    rows,cols,values = [],[],[]
    for i,row in enumerate(matrix):
        for j,value in row.items():
            if value:
                rows.append(i)
                cols.append(j)
                values.append(value)
    nv = nw+ns+nb+ng
    A = coo_matrix((values,(rows,cols)),shape=(len(matrix),nv)).tocsr()
    bounds = ([(None,None)]*nw if generalized else [(0,None)]*nw)+[(None,None)]*(ns+nb+ng)
    res = linprog([0]*nv,A_ub=A,b_ub=rhs,bounds=bounds,
                  options={'time_limit':time_limit},method='highs')
    report = {'q':q,'k':k,'generalized':generalized,'boundary':boundary,'states':ns,
              'edges':len(edges),'constraints':len(matrix),'variables':nv,
              'status':int(res.status),'message':res.message,
              'seconds':round(time.monotonic()-begin,3)}
    if res.success:
        exact = [Fraction(float(x)).limit_denominator(1000000) for x in res.x]
        valid = all(sum(exact[j]*v for j,v in row.items())<=bound for row,bound in zip(matrix,rhs))
        if not generalized:
            valid = valid and all(x>=0 for x in exact[:nw])
        report.update(exact_constraints_hold=valid,
                      solution=[str(x) for x in exact],
                      weights=[str(x) for x in exact[:nw]])
    return report


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--q',nargs='+',type=int,default=[6,8,10])
    ap.add_argument('--max-k',type=int,default=4)
    ap.add_argument('--time-limit',type=int,default=45)
    ap.add_argument('--state-limit',type=int,default=300000)
    ap.add_argument('--nonnegative',action='store_true')
    ap.add_argument('--boundary',action='store_true')
    ap.add_argument('--output',default='fixed_clock_ranking_report.json')
    args = ap.parse_args()
    if any(q<=0 or q%2 for q in args.q):
        raise ValueError('q must be positive and even')
    runs = []
    for q in args.q:
        for k in range(1,args.max_k+1):
            controls(q,k,args.boundary)
            try:
                row = solve(q,k,not args.nonnegative,args.time_limit,args.state_limit,args.boundary)
            except RuntimeError as exc:
                row = {'q':q,'k':k,'status':'resource_limit','message':str(exc)}
            runs.append(row)
            print(json.dumps({key:value for key,value in row.items() if key!='solution'}),flush=True)
            with open(args.output,'w') as f:
                json.dump({'scope':'global arbitrary-length LP synthesis; no proof claimed from infeasibility or controls',
                           'source_sha256':SOURCE_SHA256,
                           'runs':runs},f,indent=2)
            if row.get('exact_constraints_hold'):
                raise SystemExit(0)
