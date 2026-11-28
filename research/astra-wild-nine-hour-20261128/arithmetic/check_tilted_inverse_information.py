"""Exact controls for ternary minimum-cost statistics and posterior disintegration."""

from collections import defaultdict
from fractions import Fraction
from itertools import product
import json


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def offset(word):
    numerator = 0
    for i, gap in enumerate(word):
        numerator = (numerator << gap) + 3**i
    return numerator * pow(2, -sum(word), 3**len(word)) % 3**len(word), numerator


def residue_laws(theta, depth):
    # Each exponent class has its exact infinite geometric tail attached.
    r = 1-theta
    laws = [{0: Fraction(1)}]
    for n in range(1, depth+1):
        modulus = 3**n
        period = 2*3**(n-1)
        masses = defaultdict(Fraction)
        for gap in range(1, period+1):
            weight = theta * r**(gap-1)/(1-r**period)
            multiplier = pow(2, -gap, modulus)
            for tail, mass in laws[-1].items():
                masses[multiplier*(1+3*tail) % modulus] += weight*mass
        require(sum(masses.values()) == 1, "residue probability")
        laws.append(dict(masses))
    return laws


def minimum_costs(depth, terminal_unit):
    costs = [{0: 0}] if not terminal_unit else [{1: 0, 2: 0}]
    for n in range(1, depth+1):
        modulus = 3**(n+int(terminal_unit))
        current = {}
        for z in range(modulus):
            if z % 3 == 0:
                continue
            options = []
            for gap in range(1, 4*n+1):
                numerator = (z << gap)-1
                if numerator % 3 == 0:
                    tail = (numerator//3) % (modulus//3)
                    if tail in costs[-1]:
                        options.append(gap+costs[-1][tail])
            require(options, "uncovered unit")
            current[z] = min(options)
        costs.append(current)
    return costs


def word_mass(word, theta):
    return theta**len(word)*(1-theta)**(sum(word)-len(word))


def check():
    depth = 5
    costs = minimum_costs(depth, False)
    terminal = minimum_costs(depth, True)
    theta, beta = Fraction(2, 3), Fraction(3, 4)
    laws = {p: residue_laws(p, depth) for p in (theta, beta)}
    counts = defaultdict(int)
    for n in range(1, depth+1):
        modulus = 3**n
        for z, cost in terminal[n].items():
            require(0 <= cost-costs[n][z % modulus] <= 2, "terminal cost correction")
            counts["terminal_unit_comparisons"] += 1
        bucket = defaultdict(list)
        for word in product(range(1, 5), repeat=n):
            z, numerator = offset(word)
            total = sum(word)
            d = total - costs[n][z]
            require(d >= 0, "observed clock below minimum")
            bucket[z, total].append(numerator)
            mass = {p: word_mass(word, p)/laws[p][n][z] for p in laws}
            # Full posterior ratio cancels the unknown cell normalizer across words.
            norm = ((beta/theta)**n *
                    ((1-beta)/(1-theta))**(costs[n][z]-n) * laws[theta][n][z]/laws[beta][n][z])
            require(mass[beta] == norm * ((1-beta)/(1-theta))**d * mass[theta],
                    "conditional exponential-family tilt")
            counts["posterior_tilt_comparisons"] += 1
            for j in range(n+1):
                tail, _ = offset(word[j:])
                pre = word_mass(word[:j], theta)
                projected = laws[theta][n-j][tail]
                prefix_posterior = pre*projected/laws[theta][n][z]
                require(mass[theta] <= prefix_posterior <= 1, "posterior cut bound")
                # The exact posterior expression used in the critical list proof.
                full_density = 3**n*laws[theta][n][z]
                tail_density = 3**(n-j)*projected
                require(prefix_posterior*full_density == 3**j*pre*tail_density,
                        "cut density disintegration")
                counts["prefix_disintegrations"] += 1
        for (z, total), numerators in bucket.items():
            ordered = sorted(numerators)
            require(all(b-a >= modulus and (b-a) % modulus == 0
                        for a, b in zip(ordered, ordered[1:])), "fixed-clock spacing")
            for q in (2, 3, 4):
                require(len(ordered)**q <= q*sum((1+Fraction(B, modulus))**(q-1)
                                                    for B in ordered), "rank-moment bound")
                counts["integer_rank_moment_bounds"] += 1
        for p in laws:
            r = 1-p
            for q in (2, 3, 4):
                moment = sum(m**q for m in laws[p][n].values())
                diagonal = (p**q/(1-r**q))**n
                require(moment >= diagonal, "diagonal moment")
                counts["exact_infinite_gap_moments"] += 1
    print(json.dumps(dict(counts), indent=2, sort_keys=True))


if __name__ == "__main__":
    check()
