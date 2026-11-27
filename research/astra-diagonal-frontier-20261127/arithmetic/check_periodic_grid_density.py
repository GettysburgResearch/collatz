"""Enumerate exact finite digit chains and pooled calendar fibers."""
from collections import Counter
from itertools import product
import json
from check_plateau_components import graph, require


def advance(x, b):
    return (3*x+(1 << b)-1) >> b


def image(z, calendar):
    for b in calendar:
        z = advance(z, b)
    return z


def main():
    calendars = sources = chain_tests = 0
    for h in range(1, 7):
        for word in product((1, 2), repeat=h):
            mod = 1 << sum(word)
            digit_words = set()
            histogram = Counter()
            for v in range(mod):
                z = v
                digits = []
                for b in word:
                    y = advance(z, b)
                    digits.append((y << b)-3*z)
                    z = y
                digit_words.add(tuple(digits))
                gap = image(v+1, word)-z
                require(gap>=0, "monotone image")
                histogram[gap] += 1
            require(len(digit_words)==mod, "uniform independent digits: actual full bijection")
            slots = {1:1}
            for b in word:
                out = Counter()
                D = 1 << b
                for g, multiplicity in slots.items():
                    lower, rem = divmod(3*g, D)
                    out[lower] += (D-rem)*multiplicity
                    if rem:
                        out[lower+1] += rem*multiplicity
                    require(sum((3*g-d+D-1)//D for d in range(D))==3*g,
                            "exact conditional martingale mean")
                    chain_tests += 1
                slots = out
            require(slots==histogram, "rounding gap transition matches all literal adjacent pairs")
            require(sum(g*k for g,k in slots.items())==3**h, "telescoped full-period mean")
            calendars += 1
            sources += mod

    pool_checks = all_periodic = cells = 0
    for N in range(3, 704, 2):
        comps = graph(N)
        th = next(iter(comps.values()))
        zs = []
        for key in comps:
            for v, _ in key:
                z = v
                while 2*z<=N:
                    z *= 2
                zs.append(z)
        zs.sort()
        Q = len(zs)
        drift = Q*th
        require(drift.denominator==1 and len(set(zs))==Q, "pooled primitive orbits")
        A = drift.numerator
        for h in (2, 4, 6):
            groups = []
            for r, z in enumerate(zs):
                w = tuple((r+(j+1)*A)//Q-(r+j*A)//Q for j in range(h))
                output = image(z, w)
                require(output==zs[(r+h*A)%Q], "pooled uniform lifted translation at every rank")
                if not groups or groups[-1][0]!=w:
                    groups.append([w, z, z, 0])
                groups[-1][2] = z
                groups[-1][3] += 1
            require(len(groups)<=2*h+2, "contiguous calendar cells")
            cover = 0
            for w, lo, hi, count in groups:
                full = len({image(t,w) for t in range(lo,hi+1)})
                jumps = sum(image(t+1,w)>image(t,w) for t in range(lo,hi))
                require(count<=full==1+jumps, "integer interval bounds every periodic subfamily")
                cover += hi-lo+1
                cells += 1
            require(cover <= (N+1)//2, "disjoint physical cell hulls")
            pool_checks += 1
            all_periodic += Q
    return {"independent_calendars":calendars, "exhaustive_dyadic_sources":sources,
            "conditional_gap_transitions":chain_tests, "pooled_calendar_checks":pool_checks,
            "periodic_start_checks":all_periodic, "contiguous_spatial_cells":cells}


if __name__ == "__main__":
    print(json.dumps(main(), sort_keys=True, indent=2))
