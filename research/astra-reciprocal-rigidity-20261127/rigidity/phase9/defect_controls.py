"""Exact ordinary first-passage, stopped-maximum, and prefix-defect controls."""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
import json


def require(condition, explanation):
    if not condition:
        raise RuntimeError(explanation)


def step(n):
    return n//2 if n % 2 == 0 else (3*n+1)//2


def slope(n):
    return Fraction(3 if n % 2 else 1, 2)


def first_cross(n, threshold):
    seen = set()
    while n < threshold and n not in seen:
        seen.add(n)
        n = step(n)
    require(len(seen) < threshold, "positive finite threshold search")
    return n if n >= threshold else None


def gate_levels(seeds, first_level, last_level):
    levels = {}
    for k in range(first_level, last_level+1):
        threshold = 2**k
        marks = {
            crossing for n in seeds if n < threshold
            if (crossing := first_cross(n, threshold)) is not None
        }
        require(all(threshold <= y < 3*threshold//2 for y in marks), "octave overshoot")
        levels[k] = marks
    return levels


def prefix_values(n, length):
    product = Fraction(1)
    yield product
    for _ in range(length):
        product *= slope(n)
        n = step(n)
        yield product


def horizon(n):
    return max(0, n.bit_length()-4)


@lru_cache(maxsize=8192)
def native_peak(n):
    return max(prefix_values(n, horizon(n)))


def native_controls(max_shell):
    shells = []
    lower_witnesses = 0
    for m in range(5, max_shell+1):
        violations = maximum_defects = 0
        k = m-3
        for n in range(2**m, 2**(m+1)):
            ratio = slope(n)*native_peak(step(n))/native_peak(n)
            require(ratio <= Fraction(9,4), "one-edge overshoot")
            if n % 2 == 0:
                require(ratio <= 1, "even edge incorrectly creates a defect")
            if ratio > 1:
                full = list(prefix_values(n, 1+horizon(step(n))))
                first_record = any(full[t] > max(full[:t]) for t in range(k+1,len(full)))
                require(first_record, "new horizon must create a coefficient record")
                violations += 1
            if ratio == Fraction(9,4):
                maximum_defects += 1
        # Check the exact lower-bound injection into actual maximal-defect sites.
        expected_lifts = set()
        lower = 3*2**(m-1)
        for reversed_word in range(2**(k-1)):
            bits = [(reversed_word >> i) & 1 for i in range(k-1)]
            gain = Fraction(1)
            for bit in bits:
                gain *= Fraction(3 if bit else 1, 2)
                if gain <= 1:
                    break
            else:
                forward = [1, *reversed(bits), 1, 1]
                # Each prescribed next bit refines the current ordinary residue by one power of two.
                source = end = 0
                power_of_three = 1
                for i, bit in enumerate(forward):
                    if end % 2 != bit:
                        source += 2**i
                        end += power_of_three
                    end = step(end)
                    power_of_three *= 3**bit
                lift = lower + (source-lower) % 2**(k+2)
                require(slope(lift)*native_peak(step(lift))/native_peak(lift) == Fraction(9,4),
                        "lower-bound actual residue")
                expected_lifts.add(lift)
        require(0 < len(expected_lifts) <= maximum_defects <= violations, "shell bounds")
        lower_witnesses += len(expected_lifts)
        shells.append([m,violations,maximum_defects,len(expected_lifts)])
    return {"shell_rows_m_violating_maximal_constructed": shells,
            "total_maximal_witnesses": lower_witnesses}


def peak_before_gate(n, marks):
    seen = set()
    product = best = Fraction(1)
    while n not in marks and n not in seen:
        seen.add(n)
        product *= slope(n)
        best = max(best,product)
        n = step(n)
    return best


def stopped_controls():
    seeds = [1,3,7,15,27,31,41,63,97,127,255,447,639,871]
    levels = gate_levels(seeds,1,19)
    safe_start = max(seeds).bit_length()
    counts = [len(levels[k]) for k in range(safe_start,20)]
    require(all(x>=y for x,y in zip(counts,counts[1:])), "finite-seed crossings must coalesce")
    universe = range(1,1025)
    rows = []
    previous = None
    for first in [1,3,5,7,9,11,13,15]:
        marks = frozenset().union(*(levels[k] for k in range(first,20)))
        every = set(universe) | {step(n) for n in universe} | set(marks) | {step(n) for n in marks}
        peaks = {n:peak_before_gate(n,marks) for n in every}
        positive = []
        for n in set(universe) | set(marks):
            ratio = slope(n)*peaks[step(n)]/peaks[n]
            require(ratio<=3, "uniform gate defect")
            if n not in marks:
                require(peaks[n]==max(1,slope(n)*peaks[step(n)]), "Bellman recurrence")
            if ratio>1:
                require(n in marks, "defect at an unmarked source")
                positive.append(n)
        if previous is not None:
            require(all(peaks[n]>=previous[n] for n in universe), "cutoff monotonicity")
        previous = peaks
        rows.append([first,len(marks),len(positive)])
    return {"tested_ordinary_starts_per_cutoff":len(universe),
            "distinct_first_crossings_for_fixed_seeds":counts,
            "cutoff_rows_level_gates_observed_violations":rows}


def merged_mersennes():
    rows = []
    for length in range(5,13):
        start = length+4
        h = next(z for z in range(start,start+2**(length-2)) if pow(3,z,2**length)==2**length-5)
        x = 2**h-1
        y = 3**h-1
        require(horizon(x)==h-4 and horizon(y)>=length, "two actual native horizons")
        end = y
        parity = []
        for _ in range(length):
            parity.append(end%2)
            end = step(end)
        require(parity==[0,1,0,0]+[1]*(length-4), "post-run signed-class word")
        if h<=160:
            n=x
            accumulated=Fraction(1)
            for _ in range(h):
                next_n=step(n)
                require(next_n>n, "initial segment must be increasing")
                accumulated *= slope(n)*native_peak(next_n)/native_peak(n)
                n=next_n
            require(n==y and accumulated>=Fraction(3,16)*Fraction(3,2)**length,
                    "large signed accumulated defect")
        rows.append([length,h])
    return rows


def cycle_charge_control():
    # A rational orbit supplies a nontrivial finite check of the maximum-vertex identity.
    orbit=[Fraction(1,5),Fraction(4,5),Fraction(2,5)]
    for i,x in enumerate(orbit):
        image=x/2 if x.numerator % 2==0 else (3*x+1)/2
        require(image==orbit[(i+1)%len(orbit)], "rational cycle closure")
    z=max(orbit)
    index=orbit.index(z)
    product=total_charge=largest=Fraction(1)
    for i in range(len(orbit)):
        x,y=orbit[(index+i)%len(orbit)],orbit[(index+i+1)%len(orbit)]
        charge=1+1/(x*x)
        product *= (y/x)**2*charge
        total_charge *= charge
        largest=max(largest,product)
    require(largest==product==total_charge, "cycle-maximum cost equality")
    return {"rational_comparison_cycle":[str(x) for x in orbit],
            "unit_free_total_charge":str(total_charge)}


def main():
    print(json.dumps({
        "native":native_controls(12),
        "gates":stopped_controls(),
        "monotone_mersenne_segments_L_h":merged_mersennes(),
        "separate_rational_cycle_test":cycle_charge_control(),
    },sort_keys=True,indent=2))


if __name__=="__main__":
    main()
