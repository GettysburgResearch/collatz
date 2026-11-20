#!/usr/bin/env python3
"""Finite exact controls for FD1--FD3; no S-unit theorem is executed."""
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def need(condition, message):
    if not condition:
        raise ValueError(message)


def valuation(n, p):
    need(type(n) is int and n > 0, "positive valuation argument")
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent


def rational_valuation(x, p):
    return valuation(x.numerator, p)-valuation(x.denominator, p)


def core(n, primes):
    need(type(n) is int and n > 0, "positive core argument")
    for p in primes:
        while n % p == 0:
            n //= p
    return n


def shortcut(n):
    need(type(n) is int and n > 0, "positive ordinary shortcut source")
    return n//2 if n % 2 == 0 else (3*n+1)//2


def next_odd(n):
    need(type(n) is int and n > 0 and n % 2 == 1, "positive odd source")
    y, a = shortcut(n), 1
    while y % 2 == 0:
        y, a = shortcut(y), a+1
    return y, a


def path_to_defect_count(n, count):
    need(type(count) is int and count >= 1, "positive defect count")
    values, gaps, defects = [n], [], 0
    while defects < count:
        y, a = next_odd(values[-1])
        values.append(y)
        gaps.append(a)
        defects += a >= 2
    return values, gaps


def verify_canonical(values, gaps):
    need(len(values) == len(gaps)+1 and len(gaps) >= 1, "actual path lengths")
    need(all(type(n) is int and n > 0 and n % 2 for n in values), "positive odd vertices")
    need(all(type(a) is int and a >= 1 for a in gaps), "positive division exponents")
    need(gaps[0] >= 2 and gaps[-1] >= 2, "canonical first and last defects")
    A = [0]
    for j, a in enumerate(gaps):
        need(3*values[j]+1 == 2**a*values[j+1], "actual ordinary transition")
        A.append(A[-1]+a)
    positions = [i for i, a in enumerate(gaps, 1) if a >= 2]
    r, d = len(gaps), len(positions)
    P0 = 3**r*(values[0]+1)
    E = 2**A[-1]*(values[-1]+1)
    positive = [3**(r-i)*2**A[i] for i in positions]
    negative = [3**(r-i)*2**(A[i-1]+1) for i in positions]
    terms = [P0]
    for q, p in zip(negative, positive):
        terms.extend((-q, p))
    terms.append(-E)
    need(len(terms) == 2*d+2 and sum(terms) == 0, "compressed homogeneous identity")

    # Enumerate every subset, including the empty set and the whole set.
    sums = [0]
    for term in terms:
        sums += [total+term for total in sums]
    zero_masks = [mask for mask, total in enumerate(sums) if total == 0]
    need(zero_masks == [0, (1 << len(terms))-1], "no proper nonempty zero subsum")

    # Check the entire forced-cancellation valuation ladder separately.
    correction_vals = []
    for q, p in zip(negative, positive):
        correction_vals.extend((valuation(q, 2), valuation(p, 2)))
    need(all(a < b for a, b in zip(correction_vals, correction_vals[1:])), "strict correction valuations")
    need(valuation(P0, 2) == valuation(negative[0], 2) == 1, "first forced pair")
    need(valuation(E, 2) > correction_vals[-1], "endpoint is strictly later")
    total = P0
    for j, i in enumerate(positions):
        need(valuation(total, 2) == valuation(negative[j], 2), "negative correction forced")
        total -= negative[j]
        need(total == 3**(r-i)*2**A[i]*values[i], "positive odd defect remainder")
        need(valuation(total, 2) == valuation(positive[j], 2), "positive correction forced")
        total += positive[j]
        need(total == 3**(r-i)*2**A[i]*(values[i]+1), "partial shifted-state identity")
        if j+1 < d:
            run = positions[j+1]-i-1
            need(valuation(values[i]+1, 2) == run+1, "exact intervening one-run")
    need(total == E, "final endpoint cancellation")
    return A, positions, P0, E, positive, negative, len(sums)


def verify_encoding(values, gaps, primes, data):
    A, positions, P0, E, positive, negative, _ = data
    r, d = len(gaps), len(positions)
    q, qp = core(values[0]+1, primes), core(values[-1]+1, primes)
    u, v = (values[0]+1)//q, (values[-1]+1)//qp
    pos = [Fraction(2**(A[i]-1), 3**(i-1)) for i in positions]
    neg = [Fraction(2**A[i-1], 3**(i-1)) for i in positions[1:]]
    terminal = Fraction(2**(A[-1]-1)*v, 3**(r-1))
    vector = (Fraction(u), *pos, *neg, terminal)
    coefficients = (Fraction(3*q, 2), *([1]*d), *([-1]*(d-1)), -qp)
    need(len(vector) == len(coefficients) == 2*d+1, "fixed number of unit variables")
    need(all(core(x.numerator, primes) == core(x.denominator, primes) == 1 for x in vector), "fixed-pool rational units")
    need(sum(c*x for c, x in zip(coefficients, vector)) == 1, "normalized S-unit equation")
    Q1 = negative[0]
    need(Q1 == 2*3**(r-1), "canonical normalization divisor")
    signed_terms = [P0, *positive, *(-x for x in negative[1:]), -E]
    need([Fraction(x, Q1) for x in signed_terms] == [c*x for c, x in zip(coefficients, vector)], "each normalized term preserved")
    need(q*vector[0]-1 == values[0], "recover original ordinary source")
    recovered = [(1-rational_valuation(x, 3), 1+rational_valuation(x, 2)) for x in pos]
    need(recovered == [(i, A[i]) for i in positions], "recover every defect position and cumulative exponent")
    need(recovered[-1][0] == r, "last defect recovers unbounded path length")
    return (primes, q, qp, d, vector)


def verify_extensions(values):
    # Test the exact end-run formulas through the finite limits, plus one
    # forbidden extension on each side; these are not height bounds.
    m, mp = values[0]+1, values[-1]+1
    left, right = valuation(m, 3), valuation(mp, 2)-1
    for length in range(left+1):
        numerator, denominator = 2**length*m, 3**length
        need(numerator % denominator == 0, "integral backwards one-run extension")
        x = numerator//denominator-1
        for _ in range(length):
            x, a = next_odd(x)
            need(a == 1, "actual backwards extension uses only valuation one")
        need(x == values[0], "backwards extension returns to canonical source")
    need((2**(left+1)*m) % 3**(left+1) != 0, "next backwards extension is nonintegral")
    x = values[-1]
    for _ in range(right):
        x, a = next_odd(x)
        need(a == 1, "actual forward extension uses only valuation one")
    need(next_odd(x)[1] >= 2, "next forward extension must be a defect")
    return left, right


def main():
    pools = ((2,3), (2,3,5), (2,3,7,11))
    samples = []
    for source in range(1, 510, 4):
        for d in range(1, 6):
            values, gaps = path_to_defect_count(source, d)
            samples.append((values, gaps, "small-source"))
    long_controls = []
    for L in (1,2,3,8,32,128,512,1024):
        for t in (1,2,3):
            y = 2**L*3**t-1
            numerator = 8*y-1
            need(numerator % 3 == 0, "long-run source integral")
            source = numerator//3
            values, gaps = path_to_defect_count(source, 2)
            need(values[1] == y and gaps[0] == 3, "long-run initial defect")
            need(len(gaps) == L+1 and gaps[1:-1] == [1]*(L-1), "exact arbitrarily long intervening run family")
            samples.append((values, gaps, "long-one-run"))
            long_controls.append({"one_run_length": L-1, "t": t, "odd_steps": len(gaps), "defects": 2})

    subset_evaluations = vector_checks = literal_clock = 0
    max_r = max_a = max_left = max_right = 0
    encodings = {}
    source_count = set()
    for values, gaps, _ in samples:
        data = verify_canonical(values, gaps)
        source_count.add(values[0])
        subset_evaluations += data[-1]
        literal_clock += sum(gaps)
        max_r, max_a = max(max_r, len(gaps)), max(max_a, *gaps)
        for primes in pools:
            key = verify_encoding(values, gaps, primes, data)
            actual = (values[0], tuple(gaps))
            need(key not in encodings or encodings[key] == actual, "distinct canonical paths cannot collide")
            encodings[key] = actual
            vector_checks += 1
        left, right = verify_extensions(values)
        max_left, max_right = max(max_left, left), max(max_right, right)

    # Literal first-return controls demonstrate that both boundary edges
    # are defects; they do not enumerate all allowed S-unit exceptions.
    excursions = []
    for start, limit in ((17,2), (47,4), (95,6), (383,8)):
        values, gaps = [start], []
        for _ in range(limit):
            nxt, gap = next_odd(values[-1])
            values.append(nxt)
            gaps.append(gap)
        cores = [core(x+1, (2,3)) for x in values]
        for a in range(limit):
            if cores[a] != 1 or cores[a+1] == 1:
                continue
            b = a+1
            while b <= limit and cores[b] != 1:
                b += 1
            if b <= limit:
                verify_canonical(values[a:b+1], gaps[a:b])
                excursions.append({"values": values[a:b+1], "defects": sum(x >= 2 for x in gaps[a:b]), "outside_vertices": b-a-1})
    need(any(x["values"] == [17,13,5] for x in excursions), "basic two-defect excursion retained")

    malformed = []
    for name, values, gaps in (
        ("first edge valuation one", [3,5,1], [1,4]),
        ("last edge valuation one", [9,7,11], [2,1]),
        ("wrong ordinary endpoint", [17,15], [2]),
        ("even source", [2,1], [1]),
        ("zero exponent", [1,1], [0]),
        ("empty segment", [1], []),
    ):
        try:
            verify_canonical(values, gaps)
        except ValueError:
            malformed.append(name)
        else:
            raise ValueError("accepted malformed control: "+name)
    for s in (2,3,4):
        variables = 2*1+1
        need((2**35*variables**2)**(variables**3*(s+1)) == (9*2**35)**(27*(s+1)), "d=1 agrees with SC1")

    report = {
        "status": "PASS: finite exact controls for FD1--FD3",
        "proof_sha256": sha256(Path(__file__).with_name("FIXED_DEFECT_CORE_RETURNS.md").read_bytes()).hexdigest(),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "canonical_segments": len(samples),
        "distinct_sample_sources": len(source_count),
        "small_source_range": {"minimum": 1, "maximum": 509, "step": 4},
        "small_domain_defect_counts": list(range(1,6)),
        "all_subsums_evaluated": subset_evaluations,
        "fixed_pool_encoding_checks": vector_checks,
        "prime_pools": pools,
        "literal_shortcut_edges_in_samples": literal_clock,
        "largest_odd_segment_length": max_r,
        "largest_division_exponent": max_a,
        "largest_initial_extension_length": max_left,
        "largest_terminal_extension_length": max_right,
        "long_run_family_controls": long_controls,
        "outside_excursion_controls": excursions,
        "malformed_segments_rejected": malformed,
        "scope": [
            "Every signed subsum was checked on the finite displayed sample domains.",
            "The general nondegeneracy ladder is proved in the note, not inferred from samples.",
            "The S-unit theorem and the astronomical uniform count are external proof input, not executed checks.",
            "The uniform count concerns canonical paths; extension multiplicities are only proved finite.",
            "No source-independent height bound, complete exception list, or full Collatz proof is claimed.",
        ],
    }
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
