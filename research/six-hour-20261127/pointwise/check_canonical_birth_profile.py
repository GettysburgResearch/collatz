"""Exact finite ordinary-source checks for the birth-age / ray profile."""
from collections import Counter
from fractions import Fraction
from math import comb
import json

from check_all_height_audit import accelerated, geometric_terminal_laws, require


def push_measure(raw):
    out = Counter()
    for x, weight in raw.items():
        y,_ = accelerated(x)
        out[y] += weight*Fraction(3*x,3*x+1)
    return out


def subtract(left,right):
    return {x:left.get(x,0)-right.get(x,0) for x in left.keys()|right.keys()}


def finite_original_laws(layers):
    traces = []
    buckets = []
    cap = 17
    classes_checked = 0
    residual_sites = 0
    for depth,law in enumerate(layers):
        q = 3**depth
        traces.append({y:q*law[y%q]/y for y in range(1,2*q,2)})
        if depth == 0:
            buckets.append(traces[0])
            continue
        exact_birth = subtract(traces[-1],push_measure(traces[-2]))
        require(min(exact_birth.values())>=0,"newborn residual positivity")
        residual_sites += len(exact_birth)
        parent_modulus = q//3
        truncated = Counter()
        for a in range(1,2*parent_modulus,2):
            density = parent_modulus*layers[depth-1][a%parent_modulus]
            lam = Fraction(3*a+1,2*q)
            for r in range(cap):
                modulus = 1 << r
                shift = (-lam.numerator*pow(lam.denominator,-1,modulus)) % modulus
                lift = modulus+shift
                x = a+2*parent_modulus*lift
                y,e = accelerated(x)
                require(y < 2*q and lift < 1 << e, "literal canonical newborn")
                state_weight = density*Fraction(3,3*x+1)
                u = (lam+shift)/modulus
                require(state_weight == density/(2*parent_modulus*modulus*(1+u)),
                        "physical and original-law weight")
                truncated[y] += state_weight
                classes_checked += 1
        error = subtract(exact_birth,truncated)
        require(min(error.values())>=0 and sum(error.values())<=Fraction(1,1 << cap),
                "bounded geometric remainder")
        buckets.append(exact_birth)
    comparisons = 0
    for terminal in range(len(layers)):
        cumul = Counter()
        for birth in range(terminal+1):
            aged = buckets[birth]
            for _ in range(terminal-birth):
                aged = push_measure(aged)
            cumul.update(aged)
            comparisons += len(aged)
        require(not any(subtract(cumul,traces[terminal]).values()),"literal age resolution")
    return {"newborn_prefix_lifts":classes_checked,"positive_residual_sites":residual_sites,
            "original_law_age_coordinates":comparisons}


def first_birth(x):
    l = (x-1)//2
    if l == 0:
        return 0
    m = l.bit_length()-1
    native = 0
    count = 0
    while native <= m:
        x,e = accelerated(x)
        native += e
        count += 1
    return count


def capped_source_check():
    seed_count = 0
    entry_tests = 0
    max_m = 12
    octaves = [Counter() for m in range(max_m+1)]
    discrepancies = [Fraction(0) for j in range(1,8)]
    for l in range(1,1 << (max_m+1)):
        x=2*l+1
        j=first_birth(x)
        m=l.bit_length()-1
        octaves[m][j]+=1
        y=x
        for s in range(11):
            require((s>=j)==(y < 2*3**s),"actual least odd representative criterion")
            y,_=accelerated(y)
            entry_tests+=1
        for s in range(1,len(discrepancies)+1):
            if (j<=s)!=(l<1 << (2*s)):
                discrepancies[s-1]+=Fraction(1,x)
        seed_count+=1
    for m,histogram in enumerate(octaves):
        require(histogram==Counter({i+1:comb(m,i) for i in range(m+1)}),"complete birth histogram")
    for j,cost in enumerate(discrepancies,1):
        half_absolute = sum(Fraction((2*j-e)*comb(e-1,j-1),1 << e)
                            for e in range(j,2*j))
        require(cost<=half_absolute and 2*half_absolute**2<=j,"absolute cutoff error")
    return {"ordinary_sources":seed_count,"individual_canonical_tests":entry_tests,
            "exact_birth_histograms":len(octaves),"harmonic_cutoff_bounds":len(discrepancies)}


def finite_harmonicity(layers):
    steps = 0
    for j in range(1,5):
        q = 3**j
        raw = {x:q*layers[j][x%q]/x for x in range(1,2*q,2)}
        for age in range(1,6):
            aged = raw
            for _ in range(age):
                aged=push_measure(aged)
            for horizon in (0,1,2,5):
                def f(x,limit):
                    result=Fraction(1)
                    for _ in range(limit):
                        result*=Fraction(3*x,3*x+1)
                        x,_=accelerated(x)
                    return result
                before=sum(w*f(x,age+horizon) for x,w in raw.items())
                after=sum(w*f(x,horizon) for x,w in aged.items())
                require(before==after,"retained physical path survival")
                steps+=1
    return {"finite_survival_transport_identities":steps}


def main():
    layers=geometric_terminal_laws(6)
    output={}
    for counts in [finite_original_laws(layers),capped_source_check(),finite_harmonicity(layers)]:
        output.update(counts)
    print(json.dumps(output,sort_keys=True,indent=2))


if __name__ == "__main__":
    main()
