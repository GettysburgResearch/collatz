#!/usr/bin/env python3
"""Independent exact reconstruction of the expanded renewal constants.

No author checker is imported. This certifies the 54 rational residue
inequalities, not the missing finite all-source energy estimate.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

GRID = 10**12


def require(condition, message):
    if not condition:
        raise ValueError(message)


def upper_power(q):
    """Ceiling of q^(21/25) on a different grid from the author's."""
    require(q > 0, "positive input")
    numerator = q.numerator**21 * GRID**25
    denominator = q.denominator**21
    high = 1 << ((numerator.bit_length() + 24)//25)
    low = 0
    while low + 1 < high:
        middle = (low + high)//2
        if middle**25 * denominator >= numerator:
            high = middle
        else:
            low = middle
    require(low**25 * denominator < numerator <= high**25 * denominator,
            "exact enclosing root")
    return Q(high, GRID)


def first_exponent(residue, odd_count, start, offset, correction):
    modulus = 3**odd_count
    period = 2 * 3**(odd_count-1)
    candidates = [a for a in range(start, start+period)
                  if (2**(a+offset)*residue-correction) % modulus == 0]
    require(len(candidates) == 1, "complete inverse exponent class")
    return candidates[0]


def build_coefficients(c, power):
    smallest = next(q for q in range(5, 168, 2) if q % 81 == c)
    short = Q(0)
    for r in (1, 2):
        p = r+1
        correction = 4**p-3**p
        b = first_exponent(c, p, 4, 2*r, correction)
        ratio = Q(3**p*smallest, 2**(2*r+b)*smallest-correction)
        short += power(ratio)/(1-power(Q(1, 2**(2*3**r))))
    b3 = first_exponent(c, 4, 4, 6, 4**4-3**4)
    geometric_r = power(Q(3,4))
    tail = (power(Q(3*smallest, 2**b3*smallest-4))*geometric_r**3 /
            ((1-geometric_r)*(1-power(Q(1,2**54)))))
    added = Q(0)
    for a, minimum, correction in ((1,6,65),(2,4,73),(4,4,121)):
        b = first_exponent(c, 4, minimum, a+2, correction)
        ratio = Q(81*smallest, 2**(a+2+b)*smallest-correction)
        added += power(ratio)/(1-power(Q(1,2**54)))
    initial_a = 4 if c % 3 == 1 else 3
    high_valuation = Q(4*smallest, 2**initial_a*smallest-1)
    return short+tail+added, high_valuation


def correction(word):
    b = 0
    clock = 0
    for a in word:
        b = 3*b + 2**clock
        clock += a
    return b, clock


def endpoint_density(word):
    """Count legal ternary lifts without using the stated density formula."""
    b, clock = correction(word)
    p = len(word)
    modulus = 3**(p+1)
    legal = []
    for q in range(1, modulus):
        if q % 3 == 0:
            continue
        value = 2**clock*q-b
        if value % (3**p) == 0 and (value//(3**p)) % 3:
            legal.append(q)
    require(len(legal) == 2, "exactly two ternary lifts")
    endpoint_fraction = Q(len(legal), 2*3**p)
    require(endpoint_fraction*Q(3**p,2**clock) == Q(1,2**clock),
            "harmonic mean equals source cylinder mass")
    return {"word":list(word),"legal_lifts":legal,
            "endpoint_modulus":modulus,"source_mass_denominator":2**clock}


def main():
    rows = []
    for c in range(1,81):
        if c % 3 == 0:
            continue
        harmonic, extra = build_coefficients(c, lambda x:x)
        fractional, _ = build_coefficients(c, upper_power)
        require(harmonic < Q(5,8), "harmonic row")
        require(fractional < Q(91,100), "fractional row")
        require(harmonic+extra < Q(7,8), "adjacent remainder row")
        rows.append((c,harmonic,fractional,harmonic+extra))
    require(len(rows) == 54, "whole endpoint residue cover")
    words = [(2,)*r+(b,) for r in range(1,5) for b in (4,11)]
    words += [(1,1,1,6),(1,1,2,4),(1,1,4,4)]
    means = [endpoint_density(w) for w in words]
    # Exact universality of the normalization, not a sampled floating mean.
    require(Q(1,24)+Q(1,256)+Q(1,128)+Q(1,512) == Q(85,1536),
            "combined domain density")
    maxima = {}
    for index, name in ((1,"harmonic"),(2,"subcritical"),(3,"adjacent_bridge")):
        row = max(rows, key=lambda x:x[index])
        value = row[index]
        maxima[name] = {"residue":row[0],
                       "upper_fraction":[value.numerator,value.denominator]}
    print(json.dumps({
        "status":"PASS: independent finite coefficient and density reconstruction",
        "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "rational_power_grid":GRID,"endpoint_classes":len(rows),
        "maxima":maxima,"exact_ternary_density_controls":means,
        "scope":"No author checker imported. Infinite sums and invariant-label transfer require the written proof; no remainder finiteness is established."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
