#!/usr/bin/env python3
"""Exact bounded controls for the independent-direction proof, not probability limits."""
from fractions import Fraction
from itertools import product
import json


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def step(x, bit):
    return (3*x+1)//2 if bit else (x+1)//2


def repeat(start, bits):
    seen = {start}
    x = start
    for bit in bits:
        x = step(x, bit)
        if x in seen:
            return True
        seen.add(x)
    return False


def main():
    words = cases = loops = 0
    for length in range(1, 10):
        for bits in product((0, 1), repeat=length):
            words += 1
            up = sum(bits)
            for start in range(1, 2**length+1):
                cases += 1
                x, error, scale = start, 0, 1
                parity = []
                for bit in bits:
                    parity.append(x % 2)
                    error = (3 if bit else 1)*error+scale*(x % 2)
                    scale *= 2
                    x = step(x, bit)
                explicit = sum(2**j * 3**sum(bits[j+1:]) * parity[j]
                               for j in range(length))
                require(error == explicit, "rounding carry expansion")
                require(scale*x == 3**up*start+error, "literal affine identity")
                require(error+scale <= 3**length, "uniform carry bound")
                if x == start:
                    loops += 1
                    require(3**up < 2**length, "strict loop contraction")
                    require(start < 3**length, "loop height barrier")

    coupling = []
    for start in (1, 2, 3):
        for deadline in (2, 3, 4):
            frontier = {start}
            outgoing = set()
            for _ in range(deadline):
                outgoing.update(frontier)
                frontier = {step(x, b) for x in frontier for b in (0, 1)}
            vertices = sorted(outgoing)
            require(len(vertices) <= 18, "spatial enumeration bound")
            spatial_num = 0
            for mask in range(2**len(vertices)):
                choices = {x: (mask >> j) & 1 for j, x in enumerate(vertices)}
                seen, x, closed = {start}, start, False
                for _ in range(deadline):
                    x = step(x, choices[x])
                    if x in seen:
                        closed = True
                        break
                    seen.add(x)
                if closed:
                    spatial_num += 2**mask.bit_count()
            time_num = sum(2**sum(bits)
                           for bits in product((0, 1), repeat=deadline)
                           if repeat(start, bits))
            spatial = Fraction(spatial_num, 3**len(vertices))
            temporal = Fraction(time_num, 3**deadline)
            require(spatial == temporal, "first-repeat spatial/time coupling")
            coupling.append({"start": start, "deadline": deadline,
                             "spatial_vertices": len(vertices),
                             "probability": [spatial.numerator, spatial.denominator]})
    print(json.dumps({"success": True, "word_lengths": [1, 9],
                      "words": words, "word_residue_cases": cases,
                      "closed_cases": loops, "coupling_at_p": [2, 3],
                      "coupling": coupling,
                      "scope": "Exact finite identities and first-repeat probabilities only; no asymptotic probability theorem is inferred from this enumeration."}, sort_keys=True))


if __name__ == "__main__":
    main()
