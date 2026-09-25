#!/usr/bin/env python3
"""Bounded tests against exhaustive ordinary-ray assignments, not new theorems.

Imports the producer to test it. The certificate verifier is separately written.
No random sampling, floats, removable assertions, or external packages.
"""
from __future__ import annotations
from fractions import Fraction as Q
import hashlib
import importlib.util
import itertools
import json
from math import lcm
from pathlib import Path
import run


def need(ok,message):
    if not ok:
        raise ValueError(message)


def brute(source,p,selected,k,infinite):
    h=2**(k+1)
    odds=list(range(1,h,2))
    if run.odd(source)==1:
        return None,0,0
    free=[n for n in odds if n not in (1,run.odd(source))]
    optimum=None
    admissible=0
    denominator=lcm(*(j*j for j in range(1,k+2)))
    weights=[0]+[denominator//(n.bit_length()**2) for n in range(1,h)]
    for mask in range(2**len(free)):
        side={run.odd(source)}|{n for j,n in enumerate(free) if (mask>>j)&1}
        if any((n in side)!=(run.odd(run.step(n,p)) in side) for n in selected):
            continue
        admissible+=1
        b=[0]+[int(run.odd(n) in side) for n in range(1,h+1)]
        cost=Q(sum(weights[n] for n in range(1,h) if b[n]!=b[n+1]),denominator)
        value=run.Z(0,cost)
        if infinite:
            v=sum(b[n]!=b[n+1] for n in range(2**k,2**(k+1)))
            value=run.Z(v,cost-v*sum((Q(1,j*j) for j in range(1,k+2)),Q(0)))
        if optimum is None or value<optimum:
            optimum=value
    return optimum,2**len(free),admissible


def value(cert):
    a,b,c=cert['value']
    return run.Z(a,Q(int(b),int(c)))


def main():
    tests=assignments=admissible=fresh=positive_repairs=0
    rows=[]
    for p,k in ((3,2),(3,3),(5,3)):
        universe=run.full_edges(p,k)
        compulsory={1} if p==3 else {1,3}
        optional=[n for n in universe if n not in compulsory]
        for mask in range(2**len(optional)):
            edges=sorted(compulsory|{n for j,n in enumerate(optional) if (mask>>j)&1})
            for source in range(3,2**(k+1),2):
                for infinite in (False,True):
                    model=run.Model(source,p,edges,None if infinite else k)
                    cert=model.solve()
                    expected,total,allowed=brute(source,p,edges,k,infinite)
                    tests+=1;assignments+=total;admissible+=allowed
                    need((expected is None)==(cert['status']=='CONVERGENCE'),'exhaustive feasibility mismatch')
                    if expected is not None:
                        need(value(cert)==expected,'exhaustive optimum mismatch')
                    if not infinite or expected is None:
                        continue
                    for edge in universe:
                        if edge in edges:
                            continue
                        endpoints={edge,run.odd(run.step(edge,p))}
                        unused=endpoints-model.marks
                        if not unused:
                            continue
                        extended=run.Model(source,p,sorted(edges+[edge])).solve()
                        need(extended['status']=='OPTIMAL_COMPLETION','fresh edge unexpectedly merges pins')
                        difference=value(extended)-value(cert)
                        bounds=[run.Z(2,-2*sum((Q(1,j*j) for j in range(1,n.bit_length())),Q(0))) for n in unused]
                        bound=min(bounds)
                        need(difference.sign()>=0 and not bound<difference,'fresh repair inequality failed')
                        fresh+=1
                        positive_repairs+=int(difference.sign()>0)
    # An actual 3x+1 example makes the fresh-ray repair bound exact and
    # strictly separates all-halving completion from the earlier pin-only relaxation.
    before=run.Model(27,3,[1,5]).solve()
    model=run.Model(27,3,[1,5,27]);after=model.solve()
    old=run.Z(2,-Q(205,72));new=run.Z(4,-Q(5197,900));repair=run.Z(2,-Q(5269,1800))
    need(value(before)==old and value(after)==new and new-old==repair,'sharp repair fixture')
    shell=[sum(model.color(n)!=model.color(n+1) for n in range(2**k,2**(k+1))) for k in range(9)]
    need(shell==[0,0,0,0,2,4,4,4,4],'unexpected sharp-fixture extension')
    for n in list(range(1,4097))+[2**511+27,2**511+41,2**512-1]:
        need(model.color(n)==model.color(2*n),'dyadic extension failure')
    # Finite full-graph comparison against the preserved integer-capacity solver.
    parent=Path(__file__).resolve().parents[1]/'anchored-cuts'/'experiment.py'
    spec=importlib.util.spec_from_file_location('prior_integer_cut_reference',parent)
    prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
    full=0
    for p,source in ((3,27),(3,97),(5,13)):
        for k in range(max(5,source.bit_length()-1),10):
            current=run.Model(source,p,run.full_edges(p,k),k).solve()
            reference=prior.cut_certificate(2**(k+1),source,p)
            need((current['status']=='CONVERGENCE')==(reference['status']=='MERGED_WITHIN_CUTOFF'),'full graph feasibility mismatch')
            if current['status']!='CONVERGENCE':
                need(value(current)==run.Z(0,Q(*reference['capacity'])),'full graph value mismatch')
            full+=1
    # Infinite completion is the finite-depth problem plus its exact terminal-perimeter penalty.
    tail_tests=0
    for p,source,depth in ((3,27,0),(3,27,4),(5,13,4)):
        m=run.Model(source,p,run.selected_ladders(source,p,depth))
        cert=m.solve();d=m.depth
        if d<=12:
            counts=[sum(m.color(n)!=m.color(n+1) for n in range(2**k,2**(k+1))) for k in range(d+1)]
            head=sum((Q(v,(k+1)**2) for k,v in enumerate(counts)),Q(0))
            expected=run.Z(counts[-1],head-counts[-1]*sum((Q(1,j*j) for j in range(1,d+2)),Q(0)))
            need(expected==value(cert),'infinite boundary penalty mismatch')
            tail_tests+=1
    phase_tests=0
    for k in range(3,65):
        model=run.Model(7,3,[1,7],k);cert=model.solve()
        harmonic=sum((Q(1,j*j) for j in range(1,k+2)),Q(0))
        expected=min(run.Z(0,2*harmonic-2),run.Z(0,4*harmonic-Q(47,9)))
        need(value(cert)==expected,'phase-envelope fixture')
        need(model.color(3)==int(k>=29),'phase-transition source label')
        phase_tests+=1
    terminal=run.Model(7,3,[1,7]);ct=terminal.solve()
    need(value(ct)==run.Z(2,-Q(2)) and terminal.color(3)==1,'infinite phase branch')
    result=dict(status='PASS',phase_transition_checks=phase_tests,phase_transition_first_horizon=29,exhaustive_problems=tests,enumerated_assignments=assignments,
                admissible_assignments=admissible,fresh_repair_cases=fresh,
                strictly_positive_repairs=positive_repairs,full_graph_comparisons=full,
                terminal_penalty_checks=tail_tests,sharp_fixture=dict(before=old.pack(),after=new.pack(),increment=repair.pack(),shell_variation=shell),
                dyadic_extension_checks=4099,
                prior_source_sha256=hashlib.sha256(parent.read_bytes()).hexdigest())
    print(json.dumps(result,sort_keys=True,separators=(',',':')))


if __name__=='__main__':
    main()
