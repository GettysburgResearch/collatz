"""Exact recurrence partition costs and moving rational-grid rotation controls."""

from bisect import bisect_right
from fractions import Fraction
from math import gcd, prod
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_partition(p, marks, stride):
    require(0 < stride and all(1 <= t <= p for t in marks), "invalid marked interval")
    interior = sorted(set(marks) - {p})
    starts = []
    ends = []
    total_length = pieces = 0
    for residue in range(stride):
        cuts = [0, *interior[residue::stride], p]
        for left, right in zip(cuts, cuts[1:]):
            require(sum(left < event <= right for event in marks) <= stride,
                    "a partition spent too many mismatches")
            starts.append(left)
            ends.append(right)
            pieces += 1
            total_length += right-left
    require(total_length == stride*p and pieces == len(interior)+stride, "window budget")
    require(sorted(starts) == [0]*stride+interior, "incorrect top boundary multiplicity")
    require(sorted(ends) == interior+[p]*stride, "incorrect bottom boundary multiplicity")
    return pieces


def odd_step(x):
    v = 3*x+1
    e = (v & -v).bit_length()-1
    return v >> e, e


def physical_cases():
    comparisons = pieces = 0
    for seed in (27, 31, 97, 703, 871, 6171):
        states = [seed]
        exp = []
        while len(exp) < 60:
            x, e = odd_step(states[-1])
            if x in states:
                break
            states.append(x)
            exp.append(e)
        for p in range(5, min(40, len(exp)), 5):
            for lag in range(1, min(p//2, len(exp)-p)+1):
                marks = [t+1 for t in range(p) if exp[t] != exp[t+lag]]
                for stride in (1, 2, 3, 5, 11):
                    pieces += check_partition(p, marks, stride)
                first_weights = [states[e]+1 for e in marks if e != p]
                require(len(set(first_weights)) == len(first_weights), "repeated marked ordinary state")
                require(prod(first_weights) >= prod(range(2, len(first_weights)+2)), "factorial floor")
                comparisons += 1
    return comparisons, pieces


def rotation_controls():
    templates = near = moved = 0
    floors = (Fraction(0), Fraction(1, 17), Fraction(4, 13), Fraction(5, 9), Fraction(11, 12))
    for q in range(3, 25):
        for numerator in range(1, q):
            if gcd(numerator, q) != 1:
                continue
            for shift in (-1, 0, 1):
                alpha = Fraction(numerator, q) + Fraction(shift, q*q)
                for rho in (Fraction(0), Fraction(2, 7), Fraction(3, 8)):
                    word = [(bisect_right(floors, (rho + t*alpha) % 1)-1) % 3 for t in range(3*q)]
                    bad = [t for t in range(2*q) if word[t] != word[t+q]]
                    require(len(bad) <= 14*len(floors), "boundary packing estimate")
                    for t in bad:
                        grid = (rho + Fraction(t*numerator, q)) % 1
                        require(any(min((grid-f) % 1, (f-grid) % 1) <= Fraction(3, q)
                                    for f in floors), "uncovered moving-grid mismatch")
                    edited = word.copy()
                    errors = list(range(q % 4, 3*q, 7))
                    for i in errors:
                        edited[i] += 5
                    edited_mismatches = sum(edited[t] != edited[t+q] for t in range(2*q))
                    require(edited_mismatches <= len(bad) + 2*len(errors), "Hamming transfer")
                    templates += 1
                    near += len(bad)
                    moved += len(errors)
    return templates, near, moved


def rank(vectors):
    pivots = {}
    for vector in vectors:
        row = list(map(Fraction, vector))
        for i, pivot in sorted(pivots.items()):
            value = row[i]
            row = [x - value*y for x, y in zip(row, pivot)]
        i = next((j for j, x in enumerate(row) if x), None)
        if i is not None:
            pivots[i] = [x / row[i] for x in row]
    return len(pivots)


def endpoint_rank_controls():
    one, two, z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    dependent = [one, (2, 0, 0)]
    independent = [one, two]
    schemes = ((dependent, [two], [1]), (independent, [(1, -1, 0)], [2]),
               (dependent, [two], [2]), (independent, [z], [2]),
               (independent, [z, two, (1, -1, -1)], [2, 2, 2]))
    patterns = set()
    checked = 0
    for roots, carries, weights in schemes:
        states = [roots]
        for carry, weight in zip(carries, weights):
            states.append([tuple(x + m*y for x, y in zip(row, carry))
                           for row, m in zip(states[-1], (1, weight))])
        terminal = states[-1]
        a, b = rank(roots), rank(terminal)
        patterns.add((a, b))
        times = [i*i+4*i for i in range(len(carries)+1)]
        total = rank(roots+carries)
        jump_sum = rank_sum = 0
        for i in range(len(carries)):
            pre, post = roots+carries[:i], terminal+carries[i:]
            P, S = rank(pre), rank(post)
            intersection = P+S-total
            require(rank(pre+states[i]) == P and rank(post+states[i]) == S,
                    "a normalized partial state is missing from a cut span")
            require(intersection >= rank(states[i]), "two partial directions not covered")
            delta = rank(roots+carries[:i+1])-P-(S-rank(terminal+carries[i+1:]))
            jump_sum += times[i+1]*delta
            rank_sum += (times[i+1]-times[i])*(2-intersection)
            checked += 1
        require(jump_sum == (b-2)*times[-1]+rank_sum, "arbitrary-rank calendar boundary sign")
    require(patterns == {(1,1), (1,2), (2,1), (2,2)}, "all four root-rank regimes are required")
    return checked


def main():
    calendars = segments = 0
    for p in range(1, 10):
        for mask in range(1 << p):
            dates = [t+1 for t in range(p) if mask >> t & 1]
            for stride in range(1, 7):
                segments += check_partition(p, dates, stride)
                calendars += 1
    physical, native_segments = physical_cases()
    grids, boundary_hits, corruptions = rotation_controls()
    return {"arbitrary_rank_cuts": endpoint_rank_controls(),
            "arbitrary_open_partitions": calendars, "arbitrary_partition_segments": segments,
            "true_single_orbit_pairs": physical, "true_single_orbit_partition_segments": native_segments,
            "moving_grid_templates": grids, "exact_grid_mismatches": boundary_hits,
            "prescribed_template_corruptions": corruptions}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
