#!/usr/bin/env python3
"""Exact finite checks of the ordinary stopping, projected fibers, and rotation-cover counts."""
from collections import Counter
from fractions import Fraction
from math import gcd
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def step(n):
    return (3*n + 1)//2 if n % 2 else n//2


def first_floor(n, floor):
    value, time, odds = n, 0, 0
    while value > floor:
        time += 1
        odds += value % 2
        value = step(value)
        require(time < 1600, "finite control exceeded its checked cutoff")
    return value, time, odds


def first_hit_checks(start, stop, floor, modulus):
    counts, landings = Counter(), Counter()
    max_clock = 0
    for n in range(start, stop):
        y, s, p = first_floor(n, floor)
        require(floor < 2*y <= 2*floor, "landing did not enter by a halving")
        raw = n
        for _ in range(s+p):
            require(raw > floor, "ordinary first hit preceded the claimed time")
            raw = 3*raw+1 if raw % 2 else raw//2
        require(raw == y, "ordinary and shortcut landing sites differ")
        ratio_num, ratio_den = (1 << s)*y, 3**p*n
        require(ratio_num >= ratio_den, "physical slope exceeded true endpoint")
        require(ratio_num*(3*floor)**p <= ratio_den*(3*floor+1)**p,
                "accumulated positive defect exceeded its floor bound")
        landings[y] += 1
        counts[y, s % modulus, p % modulus] += 1
        max_clock = max(max_clock, s)
    total = stop-start
    delta = sum(abs(modulus**2*counts[y,a,b]-mass) for y,mass in landings.items()
                for a in range(modulus) for b in range(modulus))
    tv = Fraction(delta,2*total*modulus**2)
    require(0 <= tv <= 1, "invalid total variation")
    return {"sources":total,"landing_rows":len(landings),"max_shortcut_clock":max_clock,
            "occupied_joint_cells":len(counts),"TV_from_own_uniform_rows":str(tv)}


def projection_checks():
    cases = 0
    for q in range(1,13):
        for a in range(1,20):
            if gcd(q,a) > 1:
                continue
            for m in range(1,21):
                counts = Counter((q*i-a*j) % m for i in range(m) for j in range(m))
                require(len(counts)==m and all(v==m for v in counts.values()),
                        "primitive projection did not have equal fibers")
                cases += 1
    return cases


def near_grid_checks():
    # The last convergent is a rational proxy, bracketed around log_2(3)
    # with its predecessor by exact integer powers.
    pa, qa, pb, qb = 84,53,485,306
    require((1 << pa) < 3**qa and 3**qb < (1 << pb), "wrong logarithm bracket")
    require(abs(pa*qb-pb*qa)==1, "non-neighboring bracket")
    alpha_proxy = Fraction(pb,qb)
    inputs = [(3,2),(8,5),(19,12),(65,41),(84,53)]
    checks = 0
    largest = Fraction(0)
    for a,q in inputs:
        require(max(abs(Fraction(a,q)-v) for v in [Fraction(pa,qa),Fraction(pb,qb)]) <= Fraction(1,q*q),
                "grid perturbation too large for the exact logarithm bracket")
        for m in [1,2,3,5,7]:
            for v in range(m):
                centers = [((alpha_proxy*(v+m*b))/m) % 1 for b in range(q)]
                expected = [(Fraction(a*b,q)+alpha_proxy*v/m) % 1 for b in range(q)]
                for actual, regular in zip(centers, expected):
                    require(min((actual-regular)%1,(regular-actual)%1) <= Fraction(1,q),
                            "vertical slice missed its near-grid location")
                for width in [Fraction(1,m),Fraction(1,2*m),Fraction(1,5*m)]:
                    # The count jumps only at endpoints or translated endpoints.
                    knots = sorted(set(centers + [(x-width)%1 for x in centers] + [Fraction(0)]))
                    tests = knots + [(x+((knots[(i+1)%len(knots)]-x)%1)/2)%1 for i,x in enumerate(knots)]
                    for left in tests:
                        observed = sum((x-left)%1 < width for x in centers)
                        error = abs(observed-q*width)
                        largest=max(largest,error)
                        require(error<=4,"near-grid arc discrepancy exceeded four sites")
                    checks += len(tests)
    return {"tested_arcs":checks,"largest_count_discrepancy":str(largest),
            "logarithm_bracket":[str(Fraction(pa,qa)),str(Fraction(pb,qb))]}


def main():
    floors = [[2048,4096,1024,3],[4096,4608,1024,5],[8192,10240,4096,7]]
    result = {"primitive_projections":projection_checks(),"near_grid":near_grid_checks(),
              "true_first_landings":[dict(interval=[start,stop],floor=floor,modulus=m,
                                          **first_hit_checks(start,stop,floor,m))
                                     for start,stop,floor,m in floors]}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
