"""Exact bounded controls for physical packing, pair outputs, and collision costs."""

import itertools
import json
from collections import Counter, defaultdict
from fractions import Fraction
from math import log2

from check_native_return_curvature import binary_floor, dates_and_lift, require, two_power


def arithmetic_checks():
    tested = free = packed_rounds = 0
    for mask in range(1 << 11):
        values = [i for i in range(11) if (mask >> i) & 1]
        matching_pairs = defaultdict(list)
        for a, b in itertools.combinations(values, 2):
            matching_pairs[a+b].append((a, b))
        edges = {tuple(sorted(pair1 + pair2)) for pairs in matching_pairs.values()
                 for pair1, pair2 in itertools.combinations(pairs, 2)}
        ap_counts = [len(matching_pairs[2*b]) for b in values]
        require(sum(k*(k-1)//2 for k in ap_counts) <= len(edges),
                "distinct AP pair defects inject into four physical edges")
        if not edges:
            free += 1
            require(max(ap_counts, default=0) <= 1, "weak-Sidon AP cap at every center")
        previous = set()
        for _ in range(3):
            used = set()
            new = set()
            for edge in sorted(edges-previous):
                if used.isdisjoint(edge):
                    used.update(edge)
                    new.add(edge)
            require(all(not used.isdisjoint(e) for e in edges-previous),
                    "the resulting permitted packing is maximal")
            require(not (new & previous), "successive edges are new")
            require(all(sum(v in e for e in previous) <= _ for v in values),
                    "forbidden degree accumulates by at most one per round")
            previous.update(new)
            packed_rounds += 1
        tested += 1
    return {"integer_subsets": tested, "weak_Sidon_subsets": free,
            "maximal_forbidden_edge_rounds": packed_rounds}


def joint_outputs(code, prefix):
    def pair_signature(u, v):
        return tuple(tuple(sorted((a,b))) for a,b in zip(u,v))
    pair_counts = Counter(pair_signature(u,v)
                          for u,v in itertools.combinations_with_replacement(code, 2))
    collisions = sum(x*(x-1)//2 for x in pair_counts.values())
    differences = defaultdict(list)
    for u, v in itertools.permutations(code, 2):
        if u[:prefix] == v[:prefix]:
            differences[tuple(None if a == b else (a,b)
                              for a,b in zip(u[prefix:],v[prefix:]))].append((u,v))
    off_diagonal = sum(len(l)*(len(l)-1) for l in differences.values())
    require(off_diagonal <= 8*collisions, "crossed unordered collision multiplicity")
    preimages = Counter()
    for ordered_pairs in differences.values():
        for (u,v),(a,b) in itertools.permutations(ordered_pairs, 2):
            crossed = tuple(sorted((tuple(sorted((u,b))), tuple(sorted((v,a))))))
            require(crossed[0] != crossed[1] and pair_signature(u,b) == pair_signature(v,a),
                    "nontrivial cross collision, including repeated centers")
            preimages[crossed] += 1
    require(max(preimages.values(), default=0) <= 8, "individual preimage bound")
    return off_diagonal, max(preimages.values(), default=0)


def actual_cells():
    M = 1000000
    R = Fraction(41,10)
    L = Fraction(39*M,10)
    n = 11
    rows = Counter()
    examples = 0
    collision_count = 0
    saw_three = False
    for Y in (M, 1300000, 1600000, 1950000, 2100000, 2500000, 3150000, 3900000, 4080000):
        F = [binary_floor(Fraction(Y * 3**t, L)) for t in range(n+1)]
        if Y % 2 == 0:
            Yodd = Y+1
        else:
            Yodd = Y
        retained = []
        for x in range(Yodd,Y+8000,2):
            nums, E = dates_and_lift(x,1,n+1)
            if min(nums) < M or max(nums) > R*M:
                continue
            tags = tuple(two_power(v-f) for v,f in zip(E,F))
            require(set(tags) <= {1,2,4}, "true three-grade physical bin")
            for t in range(n):
                winding = F[t+1]-F[t]
                if tags[t] == 1:
                    require(winding == 1, "a true smallest tag occurs on a matched departure")
                if winding == 1:
                    pair = tuple(map(int,tags[t:t+2]))
                    require(pair in {(1,2),(1,4),(2,2),(2,4),(4,4)},
                            "legal matched raw tag coordinates")
                    rows[pair] += 1
                    saw_three |= pair[0] == 1
            retained.append((x,tags))
        examples += len(retained)
        # Directly inspect all coordinate-sum collisions. Each final comparison
        # has the full divisor, even when the resulting two source pairs agree.
        sums = defaultdict(list)
        for (x,a),(y,b) in itertools.combinations_with_replacement(retained,2):
            sums[tuple(i+j for i,j in zip(a[:-1],b[:-1]))].append((x,y))
        for pairs in sums.values():
            for (a,b),(c,d) in itertools.combinations(pairs,2):
                integer = two_power(-F[0])*(a+b-c-d)
                require(integer.denominator == 1 and
                        integer.numerator % (1 << (F[-1]-F[0])) == 0,
                        "complete physical dyadic source divisor")
                require(a+b == c+d, "source equality below injective bin range")
                collision_count += 1
    require(examples > 50 and collision_count > 0 and saw_three, f"realized local controls: {examples} sources, {collision_count} collisions, {rows}")
    return {"genuine_ordinary_sources": examples, "native_edges_per_source": n,
            "nontrivial_pair_word_collisions": collision_count,
            "realized_matched_symbols": [{"symbol": list(pair),"instances": count}
                                        for pair,count in sorted(rows.items())]}


def rates():
    g = log2(3)
    s = 1-2*(2-g)
    def theta(R):
        omega = log2(R/4)
        bits = (2-g-omega)*g+omega*log2(5)
        return max(omega*log2(5),3*(s+bits)/5,9*s/16+5*bits/8)/g
    threshold = 4*2**(((g/3-9*s/16)*8/5-(2-g)*g)/(log2(5)-g))
    require(theta(4.1321) < 1/3 < theta(4.1322), "opposite endpoints bracket the crossing")
    return {"limiting_width_four_theta": theta(4),
            "width_four_round_exponent": 4*(1-3*theta(4)),
            "width_threshold_numerical": threshold}


if __name__ == "__main__":
    alphabets = (range(5),range(3),range(2))
    words = list(itertools.product(*alphabets))
    codes = [words, words[::2], [w for w in words if sum(w)%3], words[:14]]
    results = [joint_outputs(code,t) for code in codes for t in range(4)]
    print(json.dumps({"native":actual_cells(), "arithmetic":arithmetic_checks(),
                      "code":{"prefix_tests":len(results),
                              "off_diagonal_coincidences":sum(x for x,_ in results),
                              "largest_individual_preimage":max(y for _,y in results)},
                      "rates":rates()}, sort_keys=True, indent=2))
