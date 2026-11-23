"""Candidate generation followed by exact arbitrary-length rank verification.

Concrete inputs generate candidates only. The verifier explores every state
of the exact multiplier transducers with integer costs. It either returns
an actual nondecreasing input, exhausts a search resource, or completes a
global node-potential certificate. No sample pass counts as a proof.
"""

import os
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
os.environ['NUMEXPR_NUM_THREADS']='1'

from collections import Counter, deque
from fractions import Fraction
from math import lcm
import argparse
import hashlib
import json
import random
import time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
import periodic_position_ranking as machine

SOURCE_SHA256=hashlib.sha256(open(__file__,'rb').read()).hexdigest()


def sample_inputs(q,k,size,seed):
    rng=random.Random(seed)
    ns=set(range(3,max(1<<q,128)))
    lengths=[max(2*k,16),32,64,128,256,512]
    for _ in range(size):
        L=rng.choice(lengths)
        ns.add((1<<(L-1))|rng.getrandbits(L-1))
    # Long runs and separated fragments probe beyond fixed bit-length lookup.
    for L in (max(2*k,16),32,64,128,256,512):
        for d in (1,3,5,7,9,17,21,27,31,85):
            if (1<<L)>d:
                ns.add((1<<L)-d)
                ns.add((1<<L)+d)
                ns.add(d*(1<<L)-1)
                ns.add(d*(1<<L)+1)
        for _ in range(32):
            low=rng.getrandbits(k+2)
            high=(1<<(k+1))|rng.getrandbits(k+1)
            ns.add((high<<L)|low)
    return sorted(ns)


def difference(n,q,k,h):
    t,_=machine.iterate(n,q)
    d,co=machine.features(t,k,h)
    fi,ci=machine.features(n,k,h)
    d.subtract(fi)
    nw=h*(1<<k)
    d[nw+co]+=1
    d[nw+ci]-=1
    return d


def candidate(ns,q,k,h,seconds):
    nw=h*(1<<k)
    ng=h*(1<<(k-1))
    nv=nw+ng+1
    rows=[]
    cols=[]
    vals=[]
    constraints=[]
    for i,n in enumerate(ns):
        row=difference(n,q,k,h)
        constraints.append(row)
        for j,v in row.items():
            if v:
                rows.append(i);cols.append(j);vals.append(v)
        rows.append(i);cols.append(nv-1);vals.append(1)
    for j in range(nw):
        rows.append(len(ns));cols.append(j);vals.append(1)
    A=coo_matrix((vals,(rows,cols)),shape=(len(ns)+1,nv)).tocsr()
    # Compact homogeneous normalization: every strict finite candidate can
    # be rescaled into this set. Maximize its common strict margin instead
    # of asking an unbounded LP to certify infeasibility at margin1.
    bounds=[(0,1)]*nw+[(0,0)]+[(-1,1)]*(ng-1)+[(0,1)]
    result=linprog([0]*(nv-1)+[-1],A_ub=A,b_ub=[0]*len(ns)+[1],
                   bounds=bounds,method='highs-ipm',options={'time_limit':seconds,'threads':1,'parallel':False})
    report={'sample_count':len(ns),'variables':nv,'status':int(result.status),
            'message':result.message}
    if not result.success:
        return report,None,None
    report['floating_common_margin']=float(result.x[-1])
    if result.x[-1]<=1e-10:
        report['candidate_result']='no_positive_margin_found'
        return report,None,None
    exact=scores=None
    for common_denominator in (10**6,10**9,10**12,10**15):
        trial=[Fraction(round(float(x)*common_denominator),common_denominator)
               for x in result.x[:-1]]
        trial_scores=[sum(trial[j]*v for j,v in row.items()) for row in constraints]
        if all(x>=0 for x in trial[:nw]) and all(s<0 for s in trial_scores):
            exact,scores=trial,trial_scores
            break
    if exact is None:
        report['exact_reconstruction']='failed'
        return report,None,None
    # Rescale a valid strictly negative rational candidate to the normalized
    # sample guard. Verification later accepts any integer drop of at least1.
    factor=max([Fraction(1)]+[-1/s for s in scores])
    exact=[factor*x for x in exact]
    D=lcm(*(x.denominator for x in exact))
    ints=[int(D*x) for x in exact]
    if not all(sum(ints[j]*v for j,v in row.items())<=-D for row in constraints):
        raise AssertionError('rational candidate normalization failed')
    report.update(exact_reconstruction='passed',scale=str(D),
                  maximum_coefficient_bits=max(abs(x).bit_length() for x in ints))
    return report,ints[:nw],ints[nw:]


def score_delta(d,w):
    return sum(w[i]*v for i,v in d.items())


def exact_verifier(q,k,h,w,g,seconds,state_limit,relax_limit):
    began=time.monotonic()
    short_guards=[]
    for n in range(3,1<<q):
        d=difference(n,q,k,h)
        actual=sum((w+g)[i]*v for i,v in d.items())
        short_guards.append((n,actual))
        if actual>=0:
            return {'outcome':'actual_counterexample','states':0,
                    'relaxations':0,'seconds':round(time.monotonic()-began,3),
                    'input_hex':hex(n),'input_bits':n.bit_length(),
                    'integer_rank_difference':str(actual)},n,None
    states=[]
    ids={}
    best=[]
    words=[]
    lengths=[]
    queued=[]
    queue=deque()
    roots=[]
    edges=[]
    ends={}

    def ensure(s):
        if s not in ids:
            if len(states)>=state_limit:
                raise RuntimeError('state limit')
            ids[s]=len(states)
            states.append(s)
            best.append(None)
            words.append(None)
            lengths.append(None)
            queued.append(False)
            edges.append(None)
        return ids[s]

    def improve(i,value,n,L):
        if best[i] is None or value>best[i]:
            best[i]=value
            words[i]=n
            lengths[i]=L
            if not queued[i]:
                queue.append(i)
                queued[i]=True
            return True
        return False

    relax=0
    try:
        for r in range(1<<q):
            s,d=machine.initial(r,q,k,h)
            i=ensure(s)
            value=score_delta(d,w)
            roots.append((i,value))
            improve(i,value,r,q)
        while queue:
            i=queue.popleft()
            queued[i]=False
            s=states[i]
            f=machine.finish(s,q,k,h)
            if f is not None:
                d,ci,co=f
                tail=score_delta(d,w)+g[co]-g[ci]
                ends[i]=tail
                if best[i]+tail>=0:
                    n=words[i]
                    row=difference(n,q,k,h)
                    actual=sum((w+g)[j]*v for j,v in row.items())
                    if actual!=best[i]+tail or n<=2:
                        raise AssertionError('counterexample reconstruction mismatch')
                    return {'outcome':'actual_counterexample','states':len(states),
                            'relaxations':relax,'seconds':round(time.monotonic()-began,3),
                            'input_hex':hex(n),'input_bits':n.bit_length(),
                            'integer_rank_difference':str(actual)},n,None
            if edges[i] is None:
                out=[]
                for b in (0,1):
                    t,d=machine.advance(s,b,q,k,h)
                    j=ensure(t)
                    out.append((j,score_delta(d,w),b))
                edges[i]=out
            for j,cost,b in edges[i]:
                if improve(j,best[i]+cost,words[i]+(b<<lengths[i]),lengths[i]+1):
                    relax+=1
            if relax>relax_limit:
                raise RuntimeError('relaxation limit')
            if time.monotonic()-began>seconds:
                raise RuntimeError('time limit')
    except RuntimeError as exc:
        return {'outcome':'resource_limit','reason':str(exc),'states':len(states),
                'relaxations':relax,'seconds':round(time.monotonic()-began,3)},None,None

    # Exhaustion is checked as a global finite inequality certificate, not
    # inferred from a finite search horizon.
    if any(value>best[i] for i,value in roots):
        raise AssertionError('root certificate inequality')
    if any(best[i]+cost>best[j] for i,out in enumerate(edges) for j,cost,b in out):
        raise AssertionError('edge certificate inequality')
    if any(best[i]+tail>=0 for i,tail in ends.items()):
        raise AssertionError('terminal certificate inequality')
    if any(x<0 for x in w):
        raise AssertionError('rank lower-bound inequality')
    certificate={'q':q,'k':k,'position_period':h,'integer_weights':[str(x) for x in w],
                 'integer_terminal_corrections':[str(x) for x in g],
                 'states':states,'node_potentials':[str(x) for x in best],
                 'root_guards':roots,'terminal_guards':list(ends.items()),
                 'edges':edges,'short_input_guards':short_guards,'drop':1,
                 'status':'exact finite all-length certificate; Lean formalization still required'}
    return {'outcome':'exact_global_certificate','states':len(states),
            'relaxations':relax,'seconds':round(time.monotonic()-began,3)},None,certificate


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--q',type=int,default=6)
    ap.add_argument('--k',type=int,default=8)
    ap.add_argument('--period',type=int,default=1)
    ap.add_argument('--samples',type=int,default=6000)
    ap.add_argument('--iterations',type=int,default=20)
    ap.add_argument('--lp-seconds',type=int,default=45)
    ap.add_argument('--verify-seconds',type=int,default=120)
    ap.add_argument('--state-limit',type=int,default=1000000)
    ap.add_argument('--relax-limit',type=int,default=3000000)
    ap.add_argument('--output',default='counterexample_rank_synthesis_report.json')
    a=ap.parse_args()
    if a.q<=0 or a.q%2:
        raise ValueError('q must be even and positive')
    machine.controls(a.q,a.k,a.period)
    ns=sample_inputs(a.q,a.k,a.samples,20261121)
    report={'scope':'sample constraints generate candidates only; only exact global exhaustion can certify all lengths',
            'source_sha256':SOURCE_SHA256,'machine_source_sha256':machine.SOURCE_SHA256,
            'q':a.q,'k':a.k,'period':a.period,'iterations':[]}
    for it in range(a.iterations):
        begin=time.monotonic()
        cr,w,g=candidate(ns,a.q,a.k,a.period,a.lp_seconds)
        row={'iteration':it,'candidate':cr}
        certificate=None
        if w is not None:
            vr,n,certificate=exact_verifier(a.q,a.k,a.period,w,g,a.verify_seconds,a.state_limit,a.relax_limit)
            row['global_verifier']=vr
            if n is not None:
                if n in ns:
                    raise AssertionError('candidate fails a sample constraint')
                ns.append(n)
        row['total_seconds']=round(time.monotonic()-begin,3)
        report['iterations'].append(row)
        print(json.dumps(row),flush=True)
        with open(a.output,'w') as f:
            json.dump(report,f,indent=2)
        if certificate is not None:
            with open(a.output+'.certificate.json','w') as f:
                json.dump(certificate,f,indent=2)
            break
        if w is None or vr['outcome']!='actual_counterexample':
            break
