"""Exact finite positive-source and cancellation controls for additive clock discrepancies."""

from fractions import Fraction
from math import gcd, isqrt, lcm
import json
from sympy import Matrix


def require(condition, message):
    if not condition:
        raise ValueError(message)


def val2(value):
    value = Fraction(value)
    require(value != 0, "dyadic valuation was requested for zero")
    num = abs(value.numerator)
    den = value.denominator
    return (num & -num).bit_length()-(den & -den).bit_length()


def small_solution(rows, bound):
    matrix = Matrix(rows)
    candidates = []
    for vector in matrix.nullspace():
        common = lcm(*(int(v.q) for v in vector))
        integer = [int(v*common) for v in vector]
        factor = gcd(*integer)
        candidates.append([x//factor for x in integer])
    require(candidates, "no nontrivial kernel")
    if len(candidates) > 1:
        reduced = Matrix(candidates).lll()
        candidates.extend([list(map(int, reduced.row(i))) for i in range(reduced.rows)])
    chosen = min(candidates, key=lambda v: max(map(abs,v)))
    require(0 < max(map(abs,chosen)) <= bound, "explicit small-solution height")
    require(all(sum(a*b for a,b in zip(row,chosen)) == 0 for row in rows), "kernel certificate")
    return chosen


def positive_source(times, odds):
    modulus = 1 << (times[-1]+1)
    residue = sum((1 << t) * pow(3,-u,modulus) for t,u in zip(times,odds))
    x = (-1-residue) % modulus + modulus
    even_times = set(times)
    state = x
    for t in range(times[-1]+1):
        require((state % 2 == 0) == (t in even_times), "actual ordinary parity word")
        if t < times[-1]:
            state = (3*state+1)//2 if state % 2 else state//2
    return x, state


def check(s, deviations):
    M,h = 7*s,4*s
    m=h+1
    require(len(deviations) == M+1 and deviations[0] == 0, "cumulative input")
    defects = [deviations[k]+deviations[j]-deviations[k+j] for k in range(h+1)
               for j in range(M-k+1)]
    L,U = -min(defects),max(defects)
    H,D = 3**(L+U), 2**L*3**U
    B,C = (2*m*H)**3,8*(m*H)**4
    G = 120
    gmin = G+min(b-a for a,b in zip(deviations,deviations[1:h+1]))
    while 8*C*2**gmin > 3**gmin:
        G += 16
        gmin += 16
    u = [j*G+e for j,e in enumerate(deviations)]
    t = [j+entry for j,entry in enumerate(u)]
    p = [Fraction(2**tj,3**uj) for tj,uj in zip(t,u)]
    x, terminal = positive_source(t,u)
    y = -(x+1)
    partial = sum(p[:-1])
    require(y-partial == -p[-1]*(terminal+1) and val2(y-partial) == t[-1], "native exact tail")

    def entry(k,j):
        defect = u[k]+u[j]-u[k+j]
        a = 2**(L+defect)*3**(U-defect)
        require(1 <= a <= H and D*p[k]*p[j] == a*p[k+j], "normalized convolution term")
        return a

    high_rows = [[entry(k,ell-k) for k in range(h+1)] for ell in range(h+1,M)]
    q = small_solution(high_rows,B)
    acoef = [sum(q[k]*entry(k,ell-k) for k in range(ell+1)) for ell in range(h+1)]
    Q = sum(z*v for z,v in zip(q,p))
    P = sum(z*v for z,v in zip(acoef,p))
    first = next(k for k,coeff in enumerate(q) if coeff)
    require(acoef[first] == D*q[first] and all(z == 0 for z in acoef[:first]), "matched first coefficient")
    require(Q*P > 0 and (Q>0) == (q[first]>0), "archimedean sign")
    residual_terms = [D*q[k]*p[k]*p[j] for k in range(h+1) for j in range(M) if k+j>=M]
    require(all(z == 0 or val2(z)>=t[-1] for z in residual_terms), "high convolution rows")
    require(D*Q*partial-P == sum(residual_terms), "finite convolution cancellation")
    form = D*Q*y-P
    I = 3**u[h]*form
    require(I.denominator == 1 and I and val2(I)>=t[-1], "integer form and valuation")
    require(abs(I.numerator) <= 3**u[h]*2*C*(x+2), "archimedean source inequality")
    return {"sources":1,"observed_clocks":M+1,"ordinary_steps":t[-1]+1,
            "homogeneous_rows":len(high_rows),"higher_terms":len(residual_terms),
            "positive_discrepancy":int(U>0),"negative_discrepancy":int(L>0)}


def main():
    counts = {}
    for s in (1,2,3,4):
        M = 7*s
        samples = [[0]*(M+1),
                   [isqrt(2*j*j)//5 for j in range(M+1)],
                   [(j % 2)*((-1)**(j//4)) for j in range(M+1)],
                   [(j*j+3*j)%7-((j+1)%3)+1 for j in range(M+1)]]
        for item in samples:
            data=check(s,item)
            for key,count in data.items():
                counts[key]=counts.get(key,0)+count
    print(json.dumps(counts,sort_keys=True))


if __name__ == "__main__":
    main()
