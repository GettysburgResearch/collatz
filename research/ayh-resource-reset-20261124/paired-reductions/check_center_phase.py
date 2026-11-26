"""Exact all-clock lower-phase obstruction at m=0 for the e=6 family."""
import json


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3*n + 1) // 2


def orbit_to_one(n, cap):
    result = []
    for clock in range(cap + 1):
        result.append(n)
        if n == 1:
            return result
        n = shortcut(n)
    raise ValueError("first hit exceeded the prescribed cutoff")


def check():
    j = 11
    z = (2**(j+7)-271)//81
    phases = [2**(j-e)*3**e-1 for e in range(j+1)]
    if z != 3233 or min(phases) <= 2:
        raise ValueError("wrong source or target")
    targeted = set(phases)
    first_hits = []
    for w in range(17, z, 48):
        trace = orbit_to_one(w, 99)
        if not targeted.isdisjoint(trace):
            raise ValueError("smaller ordinary phase meeting")
        first_hits.append(len(trace)-1)
    parent = orbit_to_one(z, 107)
    seen = [(h, phases.index(x)) for h, x in enumerate(parent) if x in targeted]
    if seen != [(7+e, e) for e in range(j+1)]:
        raise ValueError("unexpected parent phase")
    if (len(first_hits), max(first_hits), sum(first_hits)) != (67, 99, 3379):
        raise ValueError("small-source census")
    if shortcut(1) != 2 or shortcut(2) != 1:
        raise ValueError("incorrect terminal cycle")
    # Finite checks of the independent lifting modulus. Its general proof
    # uses the factorization of X^3 - 1 at a ternary unit near one.
    for k in range(32):
        modulus = 3**(k+6)
        residue = pow(2, 162 * 3**k, modulus)
        if (residue-1) % (3**(k+5)) != 0 or residue == 1:
            raise ValueError("ternary lifting order")
    return {"source": z, "triple_first_hit": len(orbit_to_one(3*z,18))-1,
            "source_first_hit": len(parent)-1, "candidate_count": len(first_hits),
            "sum_candidate_first_hit_clocks": sum(first_hits),
            "maximum_candidate_first_hit": max(first_hits),
            "lower_phase_targets": phases, "earlier_candidate_meetings": 0,
            "parent_target_visits": seen, "ternary_precision_controls": 32}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
