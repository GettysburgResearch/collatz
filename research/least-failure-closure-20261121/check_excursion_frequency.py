#!/usr/bin/env python3
"""Exact finite controls for EF1's partition, incidence and run clock.

The S-unit theorem and the asymptotic limit are written proofs, not tested
by evaluating their astronomical bound on a finite trajectory.
"""
from hashlib import sha256
import json
from pathlib import Path


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def v2(n):
    need(type(n) is int and n > 0, "positive integer valuation input")
    return (n & -n).bit_length() - 1


def core(m, primes):
    for p in primes:
        while m % p == 0:
            m //= p
    return m


def literal_step(n):
    need(type(n) is int and n > 0 and n % 2, "positive odd source")
    value = (3*n+1)//2
    exponent = 1
    while value % 2 == 0:
        value //= 2
        exponent += 1
    return value, exponent


def simple_history(source, limit):
    states, exponents, seen = [source], [], {source}
    for _ in range(limit):
        target, a = literal_step(states[-1])
        if target in seen:
            break
        states.append(target)
        exponents.append(a)
        seen.add(target)
    return states, exponents


def inspect(states, exponents, primes, core_set):
    need(2 in primes and 3 in primes, "pool must contain 2 and 3")
    need(len(states) == len(exponents)+1, "path clock mismatch")
    need(len(set(states)) == len(states), "simple-prefix hypothesis")
    shifted = [n+1 for n in states]
    cores = [core(m, primes) for m in shifted]
    inside = [q in core_set for q in cores]
    for i, a in enumerate(exponents):
        need(3*states[i]+1 == 2**a*states[i+1], "actual edge identity")
        need(2**a*shifted[i+1] == 3*shifted[i]+2**a-2,
             "shifted edge identity")
        need(2*shifted[i+1] <= 3*shifted[i], "global shifted growth bound")
        if a == 1:
            need(cores[i] == cores[i+1], "valuation one preserves core")
    blocks = []
    i = 0
    while i < len(states):
        if not inside[i]:
            i += 1
            continue
        start = i
        while i+1 < len(states) and inside[i+1] and exponents[i] == 1:
            i += 1
        blocks.append((start, i))
        i += 1
    C = sum(not value for value in inside)
    B = len(blocks)
    need(C+sum(end-start+1 for start, end in blocks) == len(states),
         "complete vertex partition, including last vertex")
    for start, end in blocks:
        length = end-start+1
        sigma = v2(shifted[start])
        need(length <= sigma, "block is too long for its binary valuation")
        # Exact antecedent of log2(m_start) <= h0 + gamma*start.
        need(shifted[start]*2**start <= shifted[0]*3**start,
             "global product inequality")
        need(2**(length+start) <= shifted[0]*3**start,
             "pre-logarithm block-clock certificate")
    ell0 = (shifted[0]-1).bit_length()
    need(len(states) <= 2**B*C + ell0*(2**B-1),
         "conservative integer global clock")
    gaps, path_keys = [], set()
    for (_, end), (start, _) in zip(blocks, blocks[1:]):
        g = start-end-1
        need(g >= 0 and all(not inside[j] for j in range(end+1, start)),
             "gap interior is exactly outside")
        need(any(a >= 2 for a in exponents[end:start]),
             "every inter-block gap has a defect")
        need(exponents[end] >= 2 and exponents[start-1] >= 2,
             "both boundary edges of the gap are defects")
        key = (states[end], start-end)
        need(key not in path_keys, "repeated path occurrence in simple prefix")
        path_keys.add(key)
        gaps.append(g)
    need(sum(gaps) <= C, "outside gap interiors must be disjoint")
    for H in range(9):
        short = sum(g <= H for g in gaps)
        long = len(gaps)-short
        need(long*(H+1) <= C, "long gaps consume outside vertices")
        need(B <= 1+short+C//(H+1), "finite incidence inequality")
    return {"states": len(states), "inside_blocks": B, "outside_visits": C,
            "gaps": gaps, "run_lengths": [b-a+1 for a, b in blocks]}


def main():
    sources = [1, 3, 5, 7, 13, 15, 17, 23, 27, 31, 53, 63, 127, 255,
               511, 871, 6171]
    sources += [2**k-1 for k in (9, 17, 33, 65, 129, 257)]
    sources += [(2**a-1)//3 for a in (8, 32, 128, 512)]
    sources = sorted(set(sources))
    families = [((2, 3), {1}), ((2, 3), {1, 5, 7}),
                ((2, 3, 5), {1, 7, 11}), ((2, 3, 7), {1, 5, 11})]
    checks = total_states = total_blocks = total_gaps = 0
    trace = []
    for source in sources:
        values, gaps = simple_history(source, 512)
        endpoints = sorted({min(t, len(gaps)) for t in
                            (0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                             144, 233, 377, 512)})
        for endpoint in endpoints:
            for primes, Q in families:
                result = inspect(values[:endpoint+1], gaps[:endpoint], primes, Q)
                checks += 1
                total_states += result["states"]
                total_blocks += result["inside_blocks"]
                total_gaps += len(result["gaps"])
                trace.append([str(source), endpoint, list(primes), sorted(Q), result])

    endpoint_control = inspect([17, 13], [2], (2, 3), {1})
    need(endpoint_control["outside_visits"] == 1,
         "the terminal outside vertex is required")
    split_control = inspect([53, 5], [5], (2, 3), {1})
    need(split_control["inside_blocks"] == 2 and v2(54) == 1,
         "internal core-to-core defect must split inside blocks")
    incidence_control = inspect([17, 13, 5], [2, 3], (2, 3), {1})
    need(incidence_control["gaps"] == [1], "outside length versus transition length")
    try:
        inspect([1, 1], [2], (2, 3), {1})
    except ValueError as exc:
        need(str(exc) == "simple-prefix hypothesis", "unexpected cycle rejection")
    else:
        raise ValueError("repeated cycle occurrence accepted as a simple prefix")
    try:
        inspect([3, 5], [1], (2,), {1})
    except ValueError as exc:
        need(str(exc) == "pool must contain 2 and 3", "unexpected pool rejection")
    else:
        raise ValueError("invalid prime pool accepted")
    need(core(4, (2,)) != core(6, (2,)),
         "omitting 3 really invalidates core preservation")
    need(2**35 < 3**23, "exact constant underlying log M_H bound")

    report = {
        "status": "PASS",
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "ordinary_sources": len(sources),
        "prime_core_families": len(families),
        "simple_prefix_partition_checks": checks,
        "vertices_in_those_checks": total_states,
        "inside_blocks": total_blocks,
        "distinct_gaps_within_those_prefixes": total_gaps,
        "H_values_per_prefix": list(range(9)),
        "trace_sha256": sha256(json.dumps(trace, sort_keys=True).encode()).hexdigest(),
        "negative_controls": [
            "17->13 needs the final outside vertex",
            "53->5 needs a split despite both endpoint cores being one",
            "17->13->5 has one outside vertex and two boundary edges",
            "a repeated cycle is not a simple prefix",
            "a pool omitting 3 does not preserve the core on exponent-one edges",
        ],
        "scope": "Finite exact partition, incidence and run-clock controls. "
                 "No external S-unit theorem, astronomical return bound, "
                 "infinite-orbit asymptotic or unrestricted Collatz conclusion "
                 "is computationally verified.",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
