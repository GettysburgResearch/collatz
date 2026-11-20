#!/usr/bin/env python3
"""Independent quotient-kernel reconstruction for FC1/FC3/FC6."""
from fractions import Fraction
from math import gcd
import json


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def quotient_matrix(r):
    q = 2**r
    rows = []
    for a in range(q):
        children = []
        for n in (a, a+q):
            children.append((n//2 if n % 2 == 0 else (3*n+1)//2) % q)
        need(len(set(children)) == 2, 'two lifts should remain distinct')
        rows.append(children)
    column = [0]*q
    for children in rows:
        for b in children:
            column[b] += 1
    need(column == [2]*q, 'quotient kernel not doubly stochastic')
    for a in range(q):
        weights = [0]*q
        weights[a] = 1
        for _ in range(r):
            out = [0]*q
            for b, w in enumerate(weights):
                for c in rows[b]:
                    out[c] += w
            weights = out
        need(weights == [1]*q, 'r-step quotient kernel not exactly uniform')
    # Non-Boolean rational labels, separate from the author's Boolean census.
    tested = 0
    for salt in range(1, 9):
        p = [Fraction((a*a+salt*a+3*salt) % (2*salt+7)-salt, salt+1) for a in range(q)]
        osc = sum(abs(x-y) for x in p for y in p)/q**2
        edge = sum(abs(p[a]-p[b]) for a in range(q) for b in rows[a])/(2*q)
        need(osc <= r*edge, 'FC1 failed for rational metric labels')
        tested += 1
    return {'r':r,'matrix_states':q,'all_initial_rows_checked':q,'rational_labels':tested}


def commutator(q):
    inv2 = pow(2,-1,q)
    for x in range(q):
        path = [(3*x+1)%q,x,x*inv2%q,(3*x*inv2+1)%q,(3*x+2)%q]
        need((2*path[2])%q == path[1], 'first dilation')
        need((3*path[2]+1)%q == path[3], 'affine edge')
        need((2*path[3])%q == path[4], 'second dilation')
    return True


def tent_identities(r):
    m = r//2
    weights = [min(j+1,r-j) for j in range(r)]
    variation = weights[0]**2+weights[-1]**2+sum((a-b)**2 for a,b in zip(weights,weights[1:]))
    variance = sum(w*w for w in weights)
    need(variation == r, 'tent shift norm')
    need(3*variance == m*(m+1)*(2*m+1), 'tent variance')
    need(12*variance >= r**3, 'tent cubic bound')


def main():
    rows = [quotient_matrix(r) for r in range(1,8)]
    qs = [q for q in range(5,301) if gcd(q,6)==1]
    for q in qs:
        commutator(q)
    for r in range(2,1002,2):
        tent_identities(r)
    print(json.dumps({'status':'PASS','quotient_matrix_audits':rows,
                      'coprime_commutator_moduli':len(qs),'tent_identity_lengths':500,
                      'external_predecessor_bound_replayed':False,
                      'scope':'Independent finite algebra checks; not a Collatz proof.'},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
