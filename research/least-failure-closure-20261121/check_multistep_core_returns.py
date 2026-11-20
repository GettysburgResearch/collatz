#!/usr/bin/env python3
"""Exact finite controls for RU1--RU3; no external theorem is executed."""
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def need(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(n):
    need(type(n) is int and n > 0, "positive ordinary shortcut source")
    return n // 2 if n % 2 == 0 else (3*n+1)//2


def literal_path(n, length):
    need(type(n) is int and n > 0 and n % 2 == 1, "positive odd source")
    values, gaps, clocks = [n], [], 0
    for _ in range(length):
        y = shortcut(values[-1])
        gap = 1
        while y % 2 == 0:
            y = shortcut(y)
            gap += 1
        values.append(y)
        gaps.append(gap)
        clocks += gap
    return values, gaps, clocks


def core(value, primes):
    need(value > 0, "positive shifted value")
    q = value
    for p in primes:
        while q % p == 0:
            q //= p
    return q


def verify_path(values, gaps):
    need(len(values) == len(gaps)+1 and len(gaps) >= 1, "path lengths")
    need(all(type(v) is int and v > 0 and v % 2 for v in values), "positive odd vertices")
    need(all(type(a) is int and a >= 1 for a in gaps), "positive gap exponents")
    A = [0]
    for i, a in enumerate(gaps):
        need(3*values[i]+1 == 2**a*values[i+1], "exact actual division")
        A.append(A[-1]+a)
    r = len(gaps)
    m0, mr = values[0]+1, values[-1]+1
    positives = [3**r*m0]
    positives += [3**(r-1-i)*2**A[i] for i in range(1, r)]
    positives += [2**A[-1]]
    negative = -(2**A[-1])*mr
    rhs = 2*3**(r-1)
    need(sum(positives)+negative == rhs, "complete shifted path identity")

    # Every subsum without the negative summand is positive. Enumerate
    # every subsum containing it, including the singleton negative term.
    sums = [0]
    for term in positives:
        need(term > 0, "strict positivity of all other terms")
        sums += [old+term for old in sums]
    zeros = [mask for mask, total in enumerate(sums) if total+negative == 0]
    if all(a == 1 for a in gaps):
        need(zeros == [1], "all-ones path has exactly its endpoint cancellation")
    else:
        need(not zeros, "unexpected vanishing subsum on a defect path")
    return A, positives, negative, rhs, len(sums), zeros


def main():
    sources = set(range(1, 258, 2))
    sources.update(2**k-1 for k in (9, 12, 17, 24, 33, 65))
    sources.update((2**a-1)//3 for a in (10, 16, 32, 64, 128, 512))
    sources = sorted(sources)
    pools = ((2, 3), (2, 3, 5), (2, 3, 7, 11))
    paths = defect_paths = all_one_paths = literal_clocks = 0
    subset_evaluations = positive_terms = vector_checks = 0
    max_gap = 0
    encodings = {}
    for n in sources:
        full, gaps, clocks = literal_path(n, 8)
        literal_clocks += clocks
        max_gap = max(max_gap, *gaps)
        for r in range(1, 9):
            values, word = full[:r+1], gaps[:r]
            A, positive, negative, rhs, count, zeros = verify_path(values, word)
            paths += 1
            subset_evaluations += count
            positive_terms += len(positive)
            defect_paths += bool(any(a >= 2 for a in word))
            all_one_paths += bool(zeros)
            for P in pools:
                m0, mr = values[0]+1, values[-1]+1
                q, qp = core(m0, P), core(mr, P)
                u, v = m0//q, mr//qp
                vector = (u, *(2**A[i] for i in range(1, r+1)), 2**A[-1]*v)
                coefficients = [Fraction(3*q, 2)]
                coefficients += [Fraction(1, 2*3**i) for i in range(1, r)]
                coefficients += [Fraction(1, 2*3**(r-1)), Fraction(-qp, 2*3**(r-1))]
                need(len(vector) == len(coefficients) == r+2, "correct number of unit variables")
                need(all(core(z, P) == 1 for z in vector), "all variables use only the fixed pool")
                need(all(q % p and qp % p for p in P), "canonical endpoint cores")
                need(sum(c*z for c, z in zip(coefficients, vector)) == 1, "rational S-unit normalization")
                need([Fraction(t, rhs) for t in positive+[negative]] ==
                     [c*z for c, z in zip(coefficients, vector)], "each signed term preserved")
                key = (P, q, qp, r, vector)
                need(key not in encodings or encodings[key] == (n, tuple(word)), "injectivity")
                encodings[key] = (n, tuple(word))
                need(q*vector[0]-1 == n, "recover original ordinary source")
                vector_checks += 1

    infinite_family_controls = []
    for r in range(1, 9):
        for t in range(4):
            n = 2**(r+1)*3**t-1
            values, gaps, _ = literal_path(n, r)
            need(gaps == [1]*r, "infinite-family exact exponent word")
            need(values[-1]+1 == 2*3**(r+t), "infinite-family shifted endpoint")
            need(core(n+1, (2,3)) == core(values[-1]+1, (2,3)) == 1, "both endpoint cores one")
            need(verify_path(values, gaps)[-1] == [1], "essential degeneracy preserved")
            infinite_family_controls.append([r, t])

    # These literal small excursions are controls for endpoint/length
    # conventions, not a search for all exceptions allowed by RU2.
    excursion_controls = []
    for n, length in ((17,2), (47,4), (95,6), (383,8)):
        values, gaps, _ = literal_path(n, length)
        cores = [core(v+1, (2,3)) for v in values]
        for a in range(length):
            if cores[a] != 1:
                continue
            b = a+1
            while b <= length and cores[b] != 1:
                b += 1
            if b <= length and b > a+1:
                need(gaps[a] >= 2, "a valuation-one edge cannot leave the core class")
                need(b-a == (b-a-1)+1, "outside vertices versus transition clock")
                verify_path(values[a:b+1], gaps[a:b])
                excursion_controls.append({"values": values[a:b+1], "outside_length": b-a-1,
                                           "odd_steps": b-a})
    need(any(row["values"] == [17,13,5] for row in excursion_controls), "factor-two control retained")

    malformed = []
    for name, values, gaps in (
        ("even vertex", [2,1], [1]),
        ("zero gap", [1,1], [0]),
        ("wrong endpoint", [17,15], [2]),
        ("nonpositive vertex", [0,1], [1]),
        ("wrong path length", [17,13,5], [2]),
    ):
        try:
            verify_path(values, gaps)
        except ValueError:
            malformed.append(name)
        else:
            raise ValueError("accepted malformed control: "+name)
    for s in (2,3,4):
        d = 1+2
        need((2**35*d*d)**(d**3*(s+1)) == (9*2**35)**(27*(s+1)), "r=1 agrees with SC1")
    report = {
        "status": "PASS: finite exact controls for RU1--RU3",
        "proof_sha256": sha256(Path(__file__).with_name("MULTISTEP_CORE_RETURNS.md").read_bytes()).hexdigest(),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "ordinary_sources": len(sources),
        "prefix_lengths": list(range(1,9)),
        "actual_paths": paths,
        "defect_paths": defect_paths,
        "all_one_paths": all_one_paths,
        "literal_shortcut_edges": literal_clocks,
        "largest_actual_division_exponent": max_gap,
        "negative_containing_subsums_evaluated": subset_evaluations,
        "strictly_positive_terms_checked": positive_terms,
        "fixed_pool_vector_checks": vector_checks,
        "prime_pools": pools,
        "all_one_family_controls": infinite_family_controls,
        "outside_excursion_controls": excursion_controls,
        "malformed_paths_rejected": malformed,
        "scope": [
            "All subsums containing the sole negative term were enumerated on the displayed finite domains.",
            "Subsets of positive terms are handled by explicit positivity checks.",
            "The infinite nondegeneracy classification is proved in the note, not inferred from the samples.",
            "The S-unit theorem and the astronomical count bound are not computationally verified.",
            "No height bound, complete exception enumeration, or full Collatz conclusion is claimed.",
        ],
    }
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
