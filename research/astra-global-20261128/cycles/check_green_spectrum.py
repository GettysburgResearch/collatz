"""Exact controls for the positive Green kernel and marked determinant."""

from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json


def require(claim, message):
    if not claim:
        raise ValueError(message)


def survive(x):
    return 3*x/(3*x+1)


def next_odd(x):
    n = 3*x+1
    return n // (n & -n)


def matrix_determinant(matrix):
    a = [row[:] for row in matrix]
    value = Q(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j,len(a)) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j],a[pivot] = a[pivot],a[j]
            value = -value
        diagonal = a[j][j]
        value *= diagonal
        for i in range(j+1,len(a)):
            if not a[i][j]:
                continue
            factor = a[i][j]/diagonal
            for k in range(j+1,len(a)):
                a[i][k] -= factor*a[j][k]
    return value


def native_basin_check():
    sites = set()
    for start in range(1,160,2):
        if start % 3 == 0:
            continue
        x = start
        while x not in sites:
            sites.add(x)
            x = next_odd(x)
    ordered = sorted(sites)
    index = {x:i for i,x in enumerate(ordered)}
    size = len(ordered)
    w = [survive(Q(x)) for x in ordered]
    t = [1-y for y in w]
    D = [Q(x%3,x*(3*x+1)) for x in ordered]
    successors = [index[next_odd(x)] for x in ordered]
    green = []
    for start in range(size):
        counts = [Q(0)]*size
        multiplier, i = Q(1),start
        while i != index[1]:
            counts[i] = multiplier
            multiplier *= w[i]
            i = successors[i]
        counts[i] = multiplier/(1-w[i])
        require(sum(u*v for u,v in zip(counts,t)) == 1, "forward killing total")
        green.append(counts)
    for i in range(size):
        for j in range(size):
            require(green[i][j]-w[i]*green[successors[i]][j] == int(i==j),
                    "first-step identity on true forward basin")
    # A smaller finite section tests determinant expansion, also with paths
    # exiting the section and with the known cycle retained or removed.
    checks = 0
    for keep in (ordered[:12],ordered[1:14],ordered[::6]):
        for z,u in ((Q(1,2),Q(3,5)),(Q(-1,3),Q(2,3))):
            raw, marked, diagonal_product = [],[],Q(1)
            for x in keep:
                i = index[x]
                row = [Q(j==x)-z*w[i]*int(next_odd(x)==j) for j in keep]
                raw.append(row)
                new_row = row[:]
                new_row[keep.index(x)] += u*D[i]
                marked.append(new_row)
                diagonal_product *= 1+u*D[i]
            predicted = diagonal_product
            if 1 in keep:
                R = 1/(1+u*D[index[1]])
                predicted *= (1-R*Q(3,4)*z)/(1-Q(3,4)*z)
            require(matrix_determinant(marked)/matrix_determinant(raw) == predicted,
                    "physical finite-section Fredholm quotient")
            checks += 1
    return {"distinct_ordinary_unit_sites":size,"green_matrix_entries":size**2,
            "finite_section_determinants":checks,"initial_sources_below":160}


def rational_cycles():
    stats = Counter()
    for p in range(1,6):
        for gaps in product(range(1,5),repeat=p):
            if any(gaps[i:]+gaps[:i] <= gaps for i in range(1,p)):
                continue
            h = sum(gaps)
            if 2**h <= 3**p:
                continue
            c,clock = 0,0
            for gap in gaps:
                c = 3*c+2**clock
                clock += gap
            x = Q(c,2**h-3**p)
            sites = []
            for gap in gaps:
                sites.append(x)
                x = (3*x+1)/2**gap
            require(x == sites[0], "rational orbit closes")
            w = [survive(y) for y in sites]
            t = [1-v for v in w]
            lam = Q(3**p,2**h)
            S = sum(t)
            stationary = [(1/y)/sum(1/z for z in sites) for y in sites]
            rows = []
            for i in range(p):
                row = [Q(0)]*p
                segment = Q(1)
                for k in range(p):
                    j = (i+k)%p
                    row[j] = segment*t[j]/(1-lam)
                    segment *= w[j]
                require(sum(row)==1 and segment==lam, "stochastic positive Green block")
                require(all(row[j]>=lam*t[j]/S for j in range(p)), "uniform minorization")
                rows.append(row)
            for j in range(p):
                require(sum(stationary[i]*rows[i][j] for i in range(p)) == stationary[j],
                        "harmonic-height stationary row")
            V = sum(v*v for v in t)
            square_trace = sum(rows[i][j]*rows[j][i] for i in range(p) for j in range(p))
            d = 1-lam
            require(square_trace == (d*V+lam*S*S)/(d*d), "cyclic signed second trace")
            deficit = V-(square_trace-1)
            require(deficit > 0, "strict variance deficit")
            if S <= Q(1,4):
                require(deficit <= d*d, "upper variance deficit")
                stats["small_loss_trace_upper_checks"] += 1
            for y in range(1,100,2):
                left = right = Q(1)
                for v in sites:
                    left *= v-y
                    right *= v
                require(left != right, "odd-grid cyclic exclusion")
                stats["odd_grid_exclusions"] += 1
            for z in (Q(1),Q(1,4),Q(-2,5)):
                polynomial = Q(1)
                for a in t:
                    polynomial *= z-a
                polynomial = (polynomial-lam*z**p)/(1-lam)
                matrix = [[z*int(i==j)-rows[i][j] for j in range(p)] for i in range(p)]
                require(matrix_determinant(matrix) == polynomial, "cycle characteristic polynomial")
            stats["rational_primitive_positive_cycles"] += 1
            stats["rational_cycle_characteristic_values"] += 3
            stats["rational_stochastic_rows"] += p
    return stats


def resonance_kernel():
    count = 0
    for m in range(2,13):
        for n in range(1,m):
            a,b = Q(m*m-n*n,m*m+n*n),Q(2*m*n,m*m+n*n)
            for t in (Q(1,5),Q(3,4),Q(99,100)):
                for s in (Q(1),Q(2,3),Q(7,8)):
                    # v/(1-sv)^2 at v=t(a-ib), clearing its positive denominator.
                    real, imag = 1-s*t*a,s*t*b
                    numerator_negative_imag = t*(2*a*real*imag+b*(real**2-imag**2))
                    target = t*(1-s*s*t*t)*b
                    require(numerator_negative_imag == target and target>0,
                            "damped common-sign derivative")
                    count += 1
    return count


def reciprocal_shape_constants():
    r, b, low, high = Q(333,500), Q(201,1000), Q(19,100), Q(7,25)
    require(2/Q(3001,1000) > r, "native upward ratio")
    require((1-r)*(1+r**30) < b*(1+r)*(1-r**30), "tail second-moment cap")
    require(high**2+b*(1-high)**2 < low, "large first weight")
    require((1-low)*(1-5*low) > Q(9,1000), "first variance range")
    require(1-6*b+5*b*b+8*high*(high-b)**2 > Q(9,1000), "second variance range")
    return {"geometric_ratio":str(r),"second_moment_cap":str(b),
            "strict_negative_squared_inverse_root_constant":"3/4000"}


def main():
    print(json.dumps({"actual_integer_section":native_basin_check(),
                      "rational_cycle_algebra":rational_cycles(),
                      "exact_resonance_kernel_tests":resonance_kernel(),
                      "reciprocal_shape_constants":reciprocal_shape_constants(),
                      "scope":"Finite checks of the stated kernel, determinant and cycle formulas. The infinite-dimensional bounds are written proofs."},
                     indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
