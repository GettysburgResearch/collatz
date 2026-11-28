"""Exact finite replays for normalized signed lines and their rational shadows."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, groupby
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3*x+1)//2 if x%2 else x//2


def rational_step(z):
    return (3*z+1)/2 if z.numerator%2 else z/2


def valuation_two(n):
    require(n != 0, "valuation of zero")
    return (abs(n) & -abs(n)).bit_length()-1


def line(d, A, B):
    return 3**max(d, 0)*A - 3**max(-d, 0)*B


def line_next(d, delta, a, b):
    dn = d+b-a
    c = max(dn, 0)+a-max(d, 0)
    require(c in (0, 1), "bad normalized multiplier")
    raw = 3**c*delta + 3**max(dn, 0)*a - 3**max(-dn, 0)*b
    require(raw%2 == 0, "incompatible paired letters")
    return dn, raw//2


def inspect_prefix(A, B, d, letters, counts):
    records = []
    lam = Fraction(abs(line(d, A, B)), 3**abs(d))
    require(lam <= 1, "control must have unit-scale entry")
    grade = 0
    output = [(d, line(d, A, B))]
    for a, b in letters:
        require((A%2, B%2) == (a, b), "wrong physical bits")
        delta = line(d, A, B)
        require(delta != 0 and A != B, "collapsed input")
        require(d == 0 or delta%3 != 0, "nonunit positive slope")
        records.append((d, delta, A, B, a, b, lam))
        dn, next_delta = line_next(d, delta, a, b)
        A, B = step(A), step(B)
        require(next_delta == line(dn, A, B), "signed line recurrence")
        require(next_delta != 0 and A != B, "collapsed endpoint")
        next_lam = Fraction(abs(next_delta), 3**abs(dn))
        if a or b:
            require(max(1, next_lam) <= 2*max(1, lam), "archimedean active bound")
        else:
            require(next_lam*2 == lam, "common even scaling")
        counts["native_steps"] += 1
        counts["negative_level_dates"] += d < 0
        counts["balanced_dates"] += d == 0
        grade += a+b
        d, lam = dn, next_lam
        output.append((d, next_delta))

    for threshold in (0, 1, 2, 3, 5, 8, 12):
        observed = sum((1 << threshold)*r[-1] >= 1 for r in records)
        require(observed <= (threshold+4)*(grade+1), "archimedean occupation bound")
        counts["occupation_threshold_checks"] += 1

    for common, group in groupby(records, key=lambda r: r[4] == r[5]):
        group = list(group)
        if not common:
            continue
        d, delta, A, B, _, _, _ = group[0]
        require(all(row[0] == d for row in group), "varying level within a common run")
        if d == 0:
            require(len(group) <= valuation_two(delta), "balanced countdown")
            continue
        j = abs(d)
        H = 3**j-1
        v = valuation_two(H)
        require(v == (1 if j%2 else 2+valuation_two(j)), "two-adic lifting formula")
        retained = len(group)-v
        if retained <= 0:
            continue
        z = Fraction(delta if d>0 else -delta, H)
        q = z.denominator
        require(q%2 == 1 and H%q == 0 and z.numerator%3 != 0, "bad rational center")
        counts["retained_scalar_runs"] += 1
        for row in group[:retained]:
            level, offset, _, _, a, b, size = row
            require(z == Fraction(offset if level>0 else -offset, H), "incorrect current center")
            require((z.numerator%2, z.denominator) == (a, q), "wrong scalar letter or denominator")
            require(a == b and abs(z) == size*Fraction(3**j, H), "shadow size identity")
            counts["retained_scalar_dates"] += 1
            counts["negative_scalar_dates"] += z < 0
            counts["noninteger_scalar_dates"] += q > 1
            z = rational_step(z)
    return output


def ordinary_prefixes(counts):
    for s in range(1, 1024, 2):
        lo, hi = step(s), step(3*s)
        A, B = lo, hi
        letters = []
        for _ in range(80):
            if step(A) == step(B):
                break
            letters.append((A%2, B%2))
            A, B = step(A), step(B)
        inspect_prefix(lo, hi, 1, letters, counts)
        counts["ordinary_sources"] += 1


def offset(dates):
    value = 0
    for date in dates:
        value = 3*value+(1 << date)
    return value


def erase_cycles(vertices, edges, counts):
    stack = [vertices[0]]
    positions = {stack[0]: 0}
    path = []
    length = odd = 0
    for vertex, edge in zip(vertices[1:], edges):
        if vertex not in positions:
            path.append(edge)
            positions[vertex] = len(stack)
            stack.append(vertex)
            continue
        pos = positions[vertex]
        ls = path[pos:]+[edge]
        circle = stack[pos:]
        require(len(circle) == len(set(circle)) == len(ls), "not a vertex-simple cycle")
        state = vertex
        for expected, (a, b) in zip(circle, ls):
            require(state == expected, "deleted walk did not splice")
            state = line_next(*state, a, b)
        require(state == vertex, "cycle did not close")
        p = sum(a for a, _ in ls)
        require(p > 0 and p == sum(b for _, b in ls), "simple cycle grade")
        length += len(ls)
        odd += p
        for old in stack[pos+1:]:
            del positions[old]
        del stack[pos+1:]
        del path[pos:]
        counts["simple_components"] += 1
        counts["nonbase_simple_components"] += vertex != vertices[0]
    require(stack == [vertices[0]] and not path, "open residue after cycle deletion")
    require(length == len(edges) and odd == sum(a for a, _ in edges), "decomposition lost mass")


def inspect_closed_word(edges, counts):
    L = len(edges)
    U = [i for i, (a, _) in enumerate(edges) if a]
    V = [i for i, (_, b) in enumerate(edges) if b]
    p = len(U)
    D = 2**L-3**p
    C = offset(U)
    require(len(V) == p and C-offset(V) == D, "ordered equation failed")
    A = (-C*pow(3**p, -1, 2**L)) % 2**L
    if A < 2:
        A += 2**L
    vertices = inspect_prefix(A, A-1, 0, edges, counts)
    require(vertices[0] == vertices[-1] == (0, 1), "not an adjacent closed walk")
    erase_cycles(vertices, edges, counts)
    counts["static_adjacent_pairs"] += 1
    counts["negative_center_pairs"] += D < 0


def adjacent_words(counts):
    for L in range(1, 21):
        for p in range(1, min(5, L)+1):
            D = 2**L-3**p
            table = {}
            for positions in combinations(range(L), p):
                C = offset(positions)
                require(C not in table, "equal offsets with different words")
                table[C] = frozenset(positions)
            for C, U in table.items():
                V = table.get(C-D)
                if V is None:
                    continue
                inspect_closed_word([(int(i in U), int(i in V)) for i in range(L)], counts)
    # The existing signed adjacent-return control has negative rational centers.
    labels = {"U": (0, 1), "D": (1, 0), "E": (0, 0), "O": (1, 1)}
    signed = [labels[k] for k in "UUDOODE"+10*"ODU"+"E"]
    inspect_closed_word(signed, counts)



def main():
    counts = Counter()
    ordinary_prefixes(counts)
    adjacent_words(counts)
    for key in ("negative_level_dates", "negative_scalar_dates", "noninteger_scalar_dates",
                "negative_center_pairs", "nonbase_simple_components"):
        require(counts[key] > 0, f"missing concrete control for {key}")
    print(json.dumps(dict(counts), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
