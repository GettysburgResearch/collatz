"""Compute critical first-exit gate mass, with independent small-cutoff checks."""
from collections import defaultdict
from fractions import Fraction
import json


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def memoized(cutoff):
    # At state x store (gate, principal slope to gate), with zero for a cycle.
    rows = {}
    for start in range(1, cutoff):
        path, seen = [], set()
        state = start
        while state < cutoff and state not in rows and state not in seen:
            seen.add(state)
            path.append(state)
            state = step(state)
        if state >= cutoff:
            gate, slope = state, Fraction(1)
        else:
            gate, slope = rows.get(state, (0, Fraction(0)))
        for node in reversed(path):
            slope *= Fraction(3 if node % 2 else 1, 2)
            rows[node] = gate, slope
    vector = defaultdict(Fraction)
    for gate, slope in rows.values():
        if gate:
            vector[gate] += slope / gate
    return vector


def by_first_hit_product(cutoff):
    vector = defaultdict(Fraction)
    for start in range(1, cutoff):
        state, weight, seen = start, Fraction(1, start), set()
        while state < cutoff and state not in seen:
            seen.add(state)
            if state % 2:
                weight *= Fraction(3 * state, 3 * state + 1)
            state = step(state)
        if state >= cutoff:
            vector[state] += weight
    return vector


def checks():
    records = []
    for cutoff in (2, 5, 10, 30, 100, 300, 1000):
        vector = memoized(cutoff)
        if vector != by_first_hit_product(cutoff):
            raise ArithmeticError(f"First-hit product disagrees at {cutoff}")
        direct_gates = {step(x) for x in range(1, cutoff) if step(x) >= cutoff}
        if set(vector) != direct_gates:
            raise ArithmeticError(f"Incorrect gate support at {cutoff}")
        harmonic = sum((Fraction(1, x) for x in range(1, cutoff)), Fraction(0))
        total = sum(vector.values(), Fraction(0)) / harmonic
        if not 0 <= total <= 1:
            raise ArithmeticError(f"Invalid normalized mass at {cutoff}")
        records.append({
            "cutoff": cutoff,
            "gates": len(vector),
            "total_floor_times_10_pow_12": (10**12 * total).__floor__(),
            "largest_floor_times_10_pow_12": (
                10**12 * max(vector.values(), default=Fraction(0)) / harmonic
            ).__floor__(),
        })
    return {"source_weight": "1/x normalized by H_(X-1)", "exact_two_implementations": records}


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2))
