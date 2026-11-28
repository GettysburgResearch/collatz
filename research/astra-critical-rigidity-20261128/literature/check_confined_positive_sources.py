"""Exact finite controls for physical-band residence and integer source counts."""

from collections import Counter
from fractions import Fraction
from itertools import product
import json


def require(test, label):
    if not test:
        raise ArithmeticError(label)


def valuation_two(x):
    return (x & -x).bit_length()-1


def floor_log_two(x):
    e = x.numerator.bit_length() - x.denominator.bit_length()
    return e - (x < Fraction(2)**e)


def syracuse(x):
    return (3*x+1) >> valuation_two(3*x+1)


def ideal_words(phase, tolerance, n, report):
    real = [phase * 3**i for i in range(n+1)]
    floors = [floor_log_two(y) for y in real]
    fracs = [y / 2**k for y, k in zip(real, floors)]
    optional = [i for i in range(1, n+1) if fracs[i] <= tolerance]
    edges = [(i-1, i) for i in range(2, n+1) if fracs[i] <= tolerance
             and floors[i] - floors[i-1] == 1]
    require(len({i for edge in edges for i in edge}) == 2*len(edges), "disjoint dimers")
    require(all(i in optional for e in edges for i in e), "both endpoints optional")
    legal = []
    free_count = 0
    for selected in product((0,1), repeat=len(optional)):
        bits = dict(zip(optional, selected))
        dates = [floors[i]-bits.get(i,0) for i in range(n+1)]
        internal = all(dates[i] > dates[i-1] for i in range(2,n+1))
        expected = all(bits.get(j,0) <= bits.get(i,0) for i,j in edges)
        require(internal == expected, "native edge constraint")
        if internal:
            free_count += 1
            if dates[0] == 0 and dates[1] > 0:
                legal.append(tuple(dates))
    require(free_count == 2**(len(optional)-2*len(edges))*3**len(edges), "dimer count")
    report["exact_mask_cases"] += 1
    report["constrained_dimers"] += len(edges)
    return legal


def source_class(dates):
    carry = 0
    for position in dates[:-1]:
        carry = 3*carry+2**position
    modulus = 2**(dates[-1]+1)
    residue = ((2**dates[-1]-carry)*pow(3**(len(dates)-1), -1, modulus)) % modulus
    return residue, modulus


def physical_word(x,n):
    dates = [0]
    states = [x]
    for _ in range(n):
        e = valuation_two(3*x+1)
        dates.append(dates[-1]+e)
        x = (3*x+1)>>e
        states.append(x)
    return tuple(dates), states


def population_controls(report):
    for ratio in map(Fraction, ("9/4","5/2","3","7/2","15/4")):
        for n in (3,5,8,12):
            for phase in map(Fraction, ("1","17/16","6/5","3/2","7/4")):
                ideal_words(phase, ratio/2, n, report)
            retreat = Fraction(101,100)
            phase = Fraction(4,3)
            words = ideal_words(phase, ratio/(2*retreat**2), n, report)
            floor = 1024 * 3**n
            z0 = phase*retreat
            lo = int(floor*z0*Fraction(999,1000))
            hi = int(floor*z0*Fraction(1001,1000))
            selected = set()
            for dates in words:
                r, modulus = source_class(dates)
                x = lo + (r-lo)%modulus
                require(x <= hi, "interior ordinary lift")
                require(x not in selected, "disjoint actual source classes")
                selected.add(x)
                obtained, states = physical_word(x,n)
                require(obtained == dates, "actual binary division dates")
                require(all(floor <= y <= ratio*floor for y in states), "real confinement")
                report["actual_interior_word_representatives"] += 1
        # Check whole physical populations independent of the representative construction.
        for floor in (37,93,311,997):
            for n in (2,5,8):
                survivors = []
                for x in range(floor|1, int(ratio*floor)+1, 2):
                    dates, states = physical_word(x,n)
                    report["examined_integer_sources"] += 1
                    if all(floor<=y<=ratio*floor for y in states):
                        r,modulus=source_class(dates)
                        require(x%modulus==r, "located source residue")
                        survivors.append((dates,x))
                report["actual_confined_sources"] += len(survivors)
                for dates in set(w for w,_ in survivors):
                    vals = [x for w,x in survivors if w==dates]
                    require(len(vals)<=1+(int(ratio*floor)-floor)//source_class(dates)[1],
                            "source multiplicity")
                report["exhaustive_populations"] += 1


def arc_controls(report):
    for n in (12,53,107,149,665,1331):
        rotation = []
        for i in range(1,n+1):
            power = 3**i
            winding = power.bit_length()-1
            rotation.append((Fraction(power, 1<<winding),i,winding))
        rotation.sort()
        doubled = rotation + [(2*z,i,w-1) for z,i,w in rotation]
        for width_ratio in map(Fraction, ("13/12","101/100","1001/1000","11001/11000")):
            hi=0
            best=[]
            for lo,(z,_,_) in enumerate(rotation):
                hi=max(hi,lo)
                while hi<lo+n and doubled[hi][0] <= z*width_ratio:
                    hi+=1
                if hi-lo>len(best):
                    best=doubled[lo:hi]
            q=len(best)
            report["exact_rotation_arcs"] += 1
            if q>2 and 2**(q-2)>width_ratio**(2*n):
                ordered=sorted((i,w) for _,i,w in best)
                i0,w0=ordered[0]
                i1,w1=ordered[1]
                require(all((i-i0)*(w1-w0)==(i1-i0)*(w-w0) for i,w in ordered),
                        "lattice collinearity")
                for b in range(1,n//(q-1)+1):
                    power=3**b
                    z=Fraction(power,1<<(power.bit_length()-1))
                    if min(z,2/z)**(q-1) <= width_ratio:
                        break
                else:
                    raise ArithmeticError("missing finite rotation certificate")
                report["certified_collinear_arcs"] += 1
                report["largest_short_clock_witness"] = max(report["largest_short_clock_witness"],b)


def main():
    report=Counter()
    population_controls(report)
    arc_controls(report)
    require(report["certified_collinear_arcs"]>0, "exercise mass above area threshold")
    print(json.dumps(dict(report),sort_keys=True,indent=2))


if __name__=="__main__":
    main()
