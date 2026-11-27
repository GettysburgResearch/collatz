"""Exact signed CDF jumps, branch floor and cycle-lap controls."""

from collections import Counter
from fractions import Fraction as Q
from functools import cache
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valuation(number, prime):
    count = 0
    while number % prime == 0:
        count += 1
        number //= prime
    return count


@cache
def inverse_words(y, depth):
    if depth == 0:
        return [(y, 0)]
    paths = []
    for e in range(1, 9):
        value = 2**e * y - 1
        if value % 3:
            continue
        x = value // 3
        for source, clock in inverse_words(x, depth-1):
            paths.append((source, e+clock))
    return paths


def marked_atoms(y, depth):
    atoms = {}
    for x, clock in inverse_words(y, depth):
        if x % 3 == 0:
            continue
        A = Q(3**depth, 2**clock)
        mark = A * Q(x, y)
        require(0 < mark <= 1, "physical survival mark")
        require(valuation(mark.numerator, 3)-valuation(mark.denominator, 3) == depth,
                "native ternary mark grade")
        require(mark not in atoms, "unique original inverse word at each atom")
        atoms[mark] = A*(x % 3)
        if mark.numerator == 3**depth and mark.denominator.bit_count() == 1:
            require(x == y, "pure-clock jump detects a physical return")
    return atoms


def atom_checks():
    counts = Counter()
    pooled = [set() for _ in range(6)]
    for y in range(1, 100, 2):
        measures = [marked_atoms(y,d) for d in range(6)]
        for d,mass in enumerate(measures):
            pooled[d].update(mass)
            counts["native_atoms"] += len(mass)
        for old, new in zip(measures, measures[1:]):
            require(not old.keys() & new.keys(), "adjacent supports disjoint")
            current = largest = Q(0)
            for b in sorted(old.keys() | new.keys()):
                current += old.get(b, 0)-new.get(b, 0)
                largest = max(largest, abs(current))
            require(2*largest >= max([*old.values(), *new.values()],default=0),
                    "CDF norm pays half the largest jump")
            counts["adjacent_pairs"] += 1
    for old, new in zip(pooled, pooled[1:]):
        require(not old & new, "pooled ternary grade remains exact")
    counts["pooled_adjacent_pairs"] = len(pooled)-1
    return counts


def branch_floor():
    rows = {}
    for y in [1,5,7,11,13,17]:
        choices = [e for e in range(1,7) if (2**e * y) % 9 in (4,7)]
        weights = [Q(3,2**e) for e in choices]
        tail = sum(weights)/(1-Q(1,64)) - max(weights)
        rows[y % 9] = str(tail)
    require(min(map(Q,rows.values())) == Q(17,336), "uniform off-cycle floor")
    return rows


def lap_pairing():
    # Exact rational positive cycles supply many primitive, nonconstant test
    # trajectories. The ordinary parent and atom tests above use only integers.
    counts = Counter()
    for p in range(1, 7):
        for word in product(range(1, 5), repeat=p):
            rotations = [word[j:]+word[:j] for j in range(p)]
            if word != min(rotations) or len(set(rotations)) < p:
                continue
            clock = sum(word)
            if 2**clock <= 3**p:
                continue
            carry = elapsed = 0
            for e in word:
                carry = 3*carry+2**elapsed
                elapsed += e
            start = Q(carry,2**clock-3**p)
            phases, x = [],start
            for e in word:
                phases.append(x)
                x = (3*x+1)/2**e
            require(x == start and len(set(phases)) == p, "least physical lap")
            lam = Q(3**p,2**clock)
            reciprocal = sum(1/x for x in phases)
            paired = Q(0)
            for r in range(p):
                for i,y in enumerate(phases):
                    x = phases[(i-r) % p]
                    partial_survival = Q(1)
                    for t in range(r):
                        z = phases[(i-r+t) % p]
                        partial_survival *= 3*z/(3*z+1)
                    require(partial_survival >= lam, "partial lap survival")
                    paired += 1/(x*y)
                    counts["ordered_pairs"] += 1
            require(paired == reciprocal**2, "all-offset autocorrelation")
            counts["rational_positive_cycles"] += 1
    return counts


def main():
    output = {
        "physical_integer_rows": atom_checks(),
        "off_cycle_ordinary_weight_floor_by_residue": branch_floor(),
        "rational_lap_algebra": lap_pairing(),
        "scope": "Bounded exact controls with inverse gaps capped at eight; written infinite estimates are separate."
    }
    print(json.dumps(output, indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
