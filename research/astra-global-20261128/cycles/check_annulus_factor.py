"""Exact controls for moving-octave occupancy, block tests and parity coding."""

from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json


def require(value, message):
    if not value:
        raise AssertionError(message)


def floor_clock(length):
    p, three_power = 0, 1
    while three_power * 3 <= 2**length:
        p += 1
        three_power *= 3
    return p


def word_circle(word):
    h, p = len(word), sum(word)
    den = 2**h - 3**p
    total = 0
    for j, b in enumerate(word):
        total = 3**b * total + b * 2**j
    x = Q(total, den)
    out = []
    for b in word:
        out.append(x)
        require(x.numerator % 2 == b, "native parity")
        x = (3**b*x+b)/2
    require(x == out[0] and len(set(out)) == len(out), "primitive closure")
    return out


def octave_count(sites):
    return max(sum(v <= w < 2*v for w in sites) for v in sites)


def cycle_tests():
    counts = Counter()
    for h in range(2, 13):
        for word in product((0, 1), repeat=h):
            p = sum(word)
            if not p or not 2**h > 3**p or 2*2**h >= 3*3**p:
                continue
            rotations = [word[j:] + word[:j] for j in range(h)]
            if word != min(rotations) or len(set(rotations)) != h:
                continue
            sites = word_circle(word)
            odd = [x for x, b in zip(sites, word) if b]
            cents = [Q(1)]
            for d in range(1, h):
                l = floor_clock(d)
                center = []
                for j, x in enumerate(sites):
                    y = sites[(j+d)%h]
                    count = sum(rotations[j][:d])
                    hit = l <= count <= l+1
                    if Q(1, 2) < y / x < 2:
                        require(hit, "same octave fixes one of two counts")
                        counts["near_ratio_pairs"] += 1
                    center.append(hit)
                cents.append(Q(sum(center), h))
            delta = Q(octave_count(sites), h)
            for n in range(1, h+1):
                bound = (Q(n) + 2*sum((n-d)*cents[d] for d in range(1, n)))/n**2
                require(delta**2 <= bound, "finite height concentration test")
                counts["finite_block_bounds"] += 1
            S = sum(1/x for x in odd)
            K = p*sum(1/x**2 for x in odd)/S**2
            delta_odd = Q(octave_count(odd), p)
            require(delta_odd*K >= Q(1, 8), "reciprocal concentration")
            if min(sites) >= 1:
                lam = Q(3**p, 2**h)
                selectors = [x.numerator * pow(x.denominator, -1, 3) % 3 for x in odd]
                a = sum(r/(x*(3*x+1)) for r, x in zip(selectors, odd))
                J = p*lam*a/(1-lam)**2
                require(Q(9,4)*lam*K <= J <= Q(32,3)*K, "physical critical cost")
                require(J*delta >= Q(9,64)*lam, "octave cost")
                counts["physical_cost_comparisons"] += 1
            counts["primitive_rational_cycles"] += 1
    return counts


def coding_test():
    for d in range(1, 13):
        names = set()
        for start in range(2**d):
            x, name = start, 0
            for j in range(d):
                b = x % 2
                name += b * 2**j
                x = (3**b*x+b)//2
            names.add(name)
        require(len(names) == 2**d, "all shortcut parity residues")
    return 2**13-2


def switching_test():
    count = Counter()
    for odd, h in ((5, 8), (12, 19), (17, 27)):
        base = [((j+1)*odd)//h - (j*odd)//h for j in range(h)]
        pairs = [i for i in range(h) if base[i] == 0 and base[(i+1)%h] == 1]
        distinct = set()
        for choices in product((0,1), repeat=len(pairs)):
            word = base.copy()
            for i, bit in zip(pairs, choices):
                if bit:
                    word[i], word[(i+1)%h] = word[(i+1)%h], word[i]
            distinct.add(tuple(word))
            prefix = [0]
            for a, b in zip(word, base):
                prefix.append(prefix[-1]+a-b)
            require(prefix[-1] == 0 and max(prefix)-min(prefix) <= 2,
                    "switches preserve bounded discrepancy on every block")
        require(len(distinct) == 2**len(pairs), "independent switch entropy")
        count["reference_periods"] += 1
        count["distinct_perturbed_words"] += len(distinct)
    return count


def log_bracket(n):
    z = Q(n-1, n+1)
    terms = 90
    low = 2*sum(z**(2*i+1)/(2*i+1) for i in range(terms))
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return low, low+tail


def first_clock_ray():
    p, h, floor = 137528045312, 217976794617, 2**71
    lo2, _ = log_bracket(2)
    _, hi3 = log_bracket(3)
    gap_low = h*lo2-p*hi3
    delta = 3*floor*gap_low/(2*h)
    require(delta > Q(73,5000) and delta**2 > Q(1,4700), "first ray occupancy")
    require(2*p*(1+Q(1,3*floor))/(floor*gap_low) < 130, "first ray cost ceiling")
    require((138*delta**2-delta)/137 > Q(1,10000), "finite translate obstruction")
    n = 2**36
    require(n <= h and Q(1,4700)-Q(1,n)-Q(8,2**18) >
            Q(1,10000)+Q(4000000,n), "two million exceptional block lengths")
    return {"odd_clock_ray": str(p), "shortcut_clock_ray": str(h),
            "strict_single_cycle_cost_ceiling": 130,
            "certified_anomalous_lengths": 2000000, "tested_length_ceiling": n}


def full_parent_packet():
    # Use a critical finite prototype from an actual ordinary integer, then
    # realize simultaneous dyadic/ternary cylinders at much larger heights.
    L, radius = 8, 3
    prototype = 27
    modulus = 2**(2*L)*3**L
    residue = prototype % modulus
    floor = 2**44
    start0 = floor + ((residue-floor) % modulus)
    starts = [start0+j*modulus for j in range(24)]
    visited = set()
    counts = Counter()
    for start in starts:
        x, reference = start, prototype
        for date in range(L+1):
            require(x not in visited, "disjoint ordinary packet")
            visited.add(x)
            require((x-reference) % 2**(2*L-date) == 0 and
                    (x-reference) % 3**L == 0, "two simultaneous coordinates")
            frontier = [(x, reference)]
            for depth in range(radius):
                following = []
                for y, z in frontier:
                    require((y % 2, y % 3) == (z % 2, z % 3),
                            "full parent and child branch labels")
                    b = y % 2
                    following.extend([((3**b*y+b)//2,(3**b*z+b)//2),
                                      (2*y,2*z)])
                    if y % 3 == 2:
                        following.append(((2*y-1)//3,(2*z-1)//3))
                    counts["labelled_neighbors"] += 1
                frontier = following
            b = x % 2
            x, reference = (3**b*x+b)//2, (3**b*reference+b)//2
    counts["actual_packet_vertices"] = len(visited)
    counts["disjoint_segments"] = len(starts)
    counts["local_radius"] = radius
    return counts


print(json.dumps({
    "positive_native_rational_circles": cycle_tests(),
    "first_clock_ray": first_clock_ray(),
    "complete_parity_residue_tests": coding_test(),
    "bounded_discrepancy_control": switching_test(),
    "full_parent_packet": full_parent_packet(),
    "scope": "Finite exact controls, with positive rational cycles and distinct ordinary shortcut starts."
}, indent=2, sort_keys=True))
