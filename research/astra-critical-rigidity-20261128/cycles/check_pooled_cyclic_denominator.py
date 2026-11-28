"""Exact multiple-cell controls on two positive primitive rational cycles."""

import hashlib
import json
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path

from check_near_octave_cycle_denominators import orbit
from check_native_return_curvature import binary_floor, require


def pooled_cycle(p, A, b, tested_cap):
    word = tuple((i+1)*A//p-i*A//p for i in range(p))
    Q, nums, E = orbit(word)
    m_num = min(nums)
    require(m_num >= p*Q and max(nums) < 2*m_num, "actual minimum, width, and full shift range")
    # Exact auxiliary slope A/p removes the full-lap mean. We verify the uniform
    # error directly below and hence do not rely on rounded values of c_*/m.
    cells = [[] for _ in range(b)]
    for s in range(p):
        k, rem = divmod(s*A, p)
        cells[rem*b//p].append((s, k))
    require(all(cells), "every angular cell occupied")

    # V_i^p 2^(-iA), divided by a common constant, captures the maximum
    # error for EVERY base and EVERY chronological displacement through any laps.
    errors = [Fraction(num**p) * Fraction(2)**(p*e-i*A)
              for i, (num,e) in enumerate(zip(nums,E))]
    err_ratio = max(errors) / min(errors)
    drift_denom = 1024
    # 2^(p/1024) >= 1+(ln 2)p/1024 > 1+p/2048.
    require(err_ratio < 1+Fraction(p,2*drift_denom),
            "all-lap log2 drift smaller than 1/1024")

    h = p*p
    n = 3*p+7
    occupancy = Counter()
    all_k = []
    min_gap = p
    min_tuples = None
    max_tuples = 0
    tests = 0
    # J=3m/2 is strictly between X/2 and 2m. Compute floor(log2(V_i/J)+j/b)
    # without transcendental functions by taking bth powers first.
    folded = [binary_floor(Fraction(2*y,3*m_num)**b) for y in nums]
    active_count = [0]*p
    for j, cell in enumerate(cells):
        F = [e+(u+j)//b for e,u in zip(E,folded)]
        tag_rows, value_rows = [], []
        for i in range(p):
            tags, values = [], []
            for s,k in cell:
                laps, phase = divmod(i+s,p)
                c = E[phase]+laps*A-k-F[i]
                require(c in (0,1), "actual dyadic tag in {1,2}")
                tags.append(c)
                values.append(nums[phase]<<c)
            tag_rows.append(tags)
            value_rows.append(values)
        variable = [i for i,row in enumerate(tag_rows) if min(row)<max(row)]
        for i in variable:
            active_count[i] += 1
        if variable:
            gaps = [(t-s)%p or p for s,t in zip(variable,variable[1:]+variable[:1])]
            min_gap = min(min_gap,min(gaps))
            require(3**min(gaps)>h, "actual ternary guard supports order h")
        all_k.append(sum(i%p in variable for i in range(n)))
        # Integer calendar shift, native one-step recurrence incl seam, full Q on forcing.
        for i in range(p):
            i2=(i+1)%p
            increment=F[i2]+(A if i2==0 else 0)-F[i]
            require(increment>=0,"nonnegative true common dyadic winding")
            require(all((v2<<increment)==3*v+Q*(1<<c)
                        for v2,v,c in zip(value_rows[i2],value_rows[i],tag_rows[i])),
                    "unscaled complete denominator in true cell recurrence")
        F_n=F[n%p]+(n//p)*A
        require(1<<(F_n-F[0])>4*h*max(nums), "full-Q cutoff across multiple laps")

        # Explicit repeated-multiplicity comparisons. Encoding uses base h+1 so
        # any legal padded multiset sum is literally coordinatewise with no carry.
        codes=[sum(tag_rows[i%p][s]*(h+1)**i for i in range(n)) for s in range(len(cell))]
        cap=min(tested_cap,h//len(cell))
        choices=list(product(range(cap+1),repeat=len(cell)-1))
        size=len(choices)
        min_tuples=size if min_tuples is None else min(min_tuples,size)
        max_tuples=max(max_tuples,size)
        for reference in (codes,value_rows[0],value_rows[p//3],value_rows[-1]):
            diffs=[entry-reference[-1] for entry in reference[:-1]]
            sums={h*reference[-1]+sum(c*d for c,d in zip(z,diffs)) for z in choices}
            require(len(sums)==size,"multiplicity vectors distinguished after true reference padding")
            tests+=size
    for k in active_count:
        occupancy[k]+=1
    require(max(active_count)<=2 and sum(active_count)>p/2, "native one-step interval occupancy")
    require(sum(all_k)==sum(active_count[i%p] for i in range(n)), "same true time budget pooled")
    return {
        "primitive_odd_period":p,"total_valuation":A,"complete_denominator_bit_length":Q.bit_length(),
        "test_order_h":h,"all_chronological_offsets":p,"occupied_cells":b,
        "cell_size_range":[min(map(len,cells)),max(map(len,cells))],
        "max_uniform_log_drift_upper":f"1/{drift_denom}",
        "actual_active_cell_counts_per_lap":dict(sorted(occupancy.items())),
        "minimum_wrap_guard_gap":min_gap,"coding_edges":n,
        "total_active_coordinates":sum(all_k),"nonreference_multiplicity_cap_tested":tested_cap,
        "padded_vectors_per_cell_range":[min_tuples,max_tuples],
        "padded_vectors_checked_four_views":tests,
    }


if __name__=="__main__":
    base=Path(__file__).parent
    names=("POOLED_CYCLIC_DENOMINATOR.md","POOLED_CYCLIC_DENOMINATOR_RATE.md")
    print(json.dumps({
        "source_sha256":{n:hashlib.sha256((base/n).read_bytes()).hexdigest() for n in names},
        "true_cycle_controls":[pooled_cycle(41,65,13,4),pooled_cycle(306,485,46,2)],
        "scope":"Every native base and full chronological shift checked for the calibrated rational slope. Four-view multiplicity tests are finite choices, not exhaustive full-order multiset enumerations."
    },indent=2,sort_keys=True))
