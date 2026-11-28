"""Exact controls for generalized Vandermonde inversion and the moving-order budget."""

import hashlib
import json
from fractions import Fraction
from math import comb, factorial, isqrt, prod
from pathlib import Path

from check_high_order_native_residence import determinant
from check_native_return_curvature import require


def vandermonde(values):
    return prod(values[j]-values[i] for i in range(len(values)) for j in range(i+1,len(values)))


def dimension(degrees):
    return Fraction(vandermonde(degrees), vandermonde(range(len(degrees))))


def audit_matrix(degrees, nodes, name):
    d, m = len(nodes), max(degrees)
    require(len(degrees)==d and len(set(nodes))==d, 'distinct positive integer powers and nodes')
    nodes = sorted(nodes)
    delta = min([Fraction(1)] + [b-a for a,b in zip(nodes,nodes[1:])])
    size = max(max(nodes),1/min(nodes))
    require(size**m < 2, 'certified finite aperture near one')
    a = [[v**ell for v in nodes] for ell in degrees]
    full = determinant(a)
    schur_full = full / vandermonde(nodes)
    require(schur_full > 0 and dimension(degrees) / size**(d*m) <= schur_full
            <= dimension(degrees)*size**(d*m), 'full alternant and homogeneous positive envelope')
    tested = 0
    for i in range(d):
        minor_degrees = degrees[:i]+degrees[i+1:]
        dimratio = dimension(minor_degrees)/dimension(degrees)
        q = Fraction(factorial(d-1),prod(abs(degrees[i]-degrees[r]) for r in range(d) if r!=i))
        require(dimratio==q and q<=comb(d-1,i), 'exact Weyl specialization cofactor ratio')
        for j in range(d):
            minor = [[row[c] for c in range(d) if c != j] for r,row in enumerate(a) if r!=i]
            cof = determinant(minor)
            minor_nodes = nodes[:j]+nodes[j+1:]
            schur = cof / vandermonde(minor_nodes)
            require(dimension(minor_degrees)/size**((d-1)*m) <= schur
                    <= dimension(minor_degrees)*size**((d-1)*m), 'cofactor positive envelope')
            inv_abs = abs(cof/full)
            gaps = prod(abs(nodes[j]-u) for c,u in enumerate(nodes) if c!=j)
            require(inv_abs*gaps == schur/schur_full, 'full and minor Vandermonde cancellations')
            require(inv_abs*delta**(d-1) <= size**((2*d-1)*m)*q, 'explicit inverse entry bound')
            tested += 1
    return {'name':name,'dimension':d,'largest_degree':m,'entries_checked':tested}


def budgets(t, beta):
    # Schematic finite instance log M=2^t, T=2^(4t), kappa'=3, alpha=7+3 beta.
    # Integer log inequalities avoid representing M or taking as input an unknown
    # effective constant in an irrationality-measure theorem.
    require(t == isqrt(t)**2 and t>=10**8, 'square sample parameter')
    root = isqrt(t)
    # h=floor(2^t/(128t)) >= 2^t/(256t); m<=20h(t+1)<=2^t.
    require(20*(t+1)<=128*t and 2*t<=t*t, 'aperture and floor budgets')
    L = t**(1+beta)*root
    require(L>t and L**3 < t**(7+3*beta), 'guard exceeds log h, ternary cutoff below gap')
    # n<=2*2^t*t^beta and log(2h+1)<=2t give (1+n/L)log(2h+1)/h
    # <=1+1024*t²*t^beta/L. Lower log K >=2t log2−log(4·100²).
    # Bounds log2>69/100 and log(40000)<11 suffice.
    correction = 1+Fraction(1024*t**(2+beta),L)
    lower = Fraction(138*t,100)-11
    upper = t+correction
    require(lower>upper, 'pigeonhole population exceeds moving Bh-code capacity')
    # d<=2h; normalized 2h kappa' logT/logM <= 2*3*4/128 since log2<1.
    require(Fraction(24,128)<Fraction(1,4), 'main determinant exponent beats 1/M')
    return {'t':t,'log_M_symbolic':'2^t','T_symbolic':'2^(4t)','beta':beta,
            'guard_length':L,'population_minus_capacity_lower':str(lower-upper),
            'example_type':'finite parameter inequalities, without an effective logarithm onset'}


if __name__=='__main__':
    p = Path(__file__).with_name('POLYLOGARITHMIC_NEAR_OCTAVE_RESIDENCE.md')
    ones = [Fraction(1)+Fraction(i-3,1000) for i in range(7)]
    true_return = Fraction(3**53,2**84)
    data={'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
          'exact_inverse_matrices':[
              audit_matrix([3],[Fraction(99,100)],'one surviving signed coefficient'),
              audit_matrix([5,11,17],[true_return**j for j in (-1,0,1)],'actual native homogeneous factors'),
              audit_matrix([11,13,17,19,23,29,31],ones,'mixed side of one and skipped prime exponents'),
              audit_matrix([7,13,23,31],[Fraction(1)+Fraction(i,10**15) for i in range(4)],
                           'nearly coincident distinct roots')],
          'moving_order_budgets':[budgets(10**8,0),budgets(10**8,1),budgets(10**10,2)]}
    print(json.dumps(data,sort_keys=True,indent=2))
