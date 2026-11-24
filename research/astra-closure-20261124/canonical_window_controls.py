"""Exact finite controls for ordinary canonical windows and extremal digit runs."""
from fractions import Fraction
import json
from math import log, log2, sqrt


def require(statement, message):
    if not statement:
        raise ValueError(message)


def edge(q):
    t = 3 * q + 1
    power = t & -t
    return power.bit_length() - 1, t // power


def controls():
    scalars = {1: Fraction(1)}
    edges = windows = tested_prefixes = run_checks = scalar_checks = 0
    for source in range(1, 2048, 2):
        path = [source]
        gaps = []
        while path[-1] != 1:
            require(len(path) <= 10000, "exhausted oracle budget")
            a, r = edge(path[-1])
            gaps.append(a)
            path.append(r)
        require(len(set(path)) == len(path), "repeated preterminal state")
        for i in reversed(range(len(gaps))):
            scalars[path[i]] = (gaps[i] + scalars[path[i + 1]]) / 3
        phases, carries = [], []
        for q in path:
            h = scalars[q]
            centered = h - Fraction(1, 2)
            c = (centered.numerator - 1) // centered.denominator
            carries.append(c)
            phases.append(h - c)
            require(2**c <= q, "normalized height floor")
            residue = centered % 1
            require(min(residue, 1-residue) >= Fraction(1, 3**q.bit_length()),
                    "scalar too close to a centered ternary endpoint")
            scalar_checks += 1
        digits = []
        for i, a in enumerate(gaps):
            b = 3*phases[i] - phases[i+1]
            require(b in (1, 2, 3), "digit not ternary")
            require(a+carries[i+1] == b+3*carries[i], "wrong carry")
            digits.append(int(b))
        for j, digit in enumerate(digits):
            if digit not in (1, 3):
                continue
            t = j
            while t < len(digits) and digits[t] == digit:
                t += 1
            require(2**(t-j+carries[j]) <= path[j], "extremal run bound")
            run_checks += 1
        edges += len(gaps)
        for n in sorted({len(gaps), len(gaps)//2}):
            maximum = max(path[:n+1])
            m = 0
            while 3**m <= maximum:
                m += 1
            for length in (m, m+1):
                if length > n:
                    continue
                starts = range(n-length+1)
                paid = {i for i, c in enumerate(carries[:n+1]) if c}
                clean = [i for i in starts if not any(v in paid for v in range(i, i+length+1))]
                cw = {tuple(digits[i:i+length]) for i in clean}
                all_words = {tuple(digits[i:i+length]) for i in starts}
                require(len(cw) == len(clean), "clean collision below full modulus")
                require(len(starts) <= len(all_words)+(length+1)*len(paid),
                        "finite canonical-window bound")
                windows += len(starts)
                tested_prefixes += 1
    u = log2(3)-1
    z = (-(1-u) + sqrt((1-u)**2+4*(2-u)*u)) / (2*(2-u))
    entropy = log(1+z+z*z)-u*log(z)
    require(3**1000 * 8**1138 > 21**1138, "exact coarse entropy exponent")
    return {"odd_sources": 1024, "ordinary_edges_with_multiplicity": edges,
            "tested_prefix_length_pairs": tested_prefixes, "sampled_windows": windows,
            "extreme_runs_including_suffixes": run_checks, "phase_distances": scalar_checks,
            "optimized_exponent_approximation": round(log(3)/entropy, 12),
            "exact_coarse_exponent_above_1138_over_1000": True}


if __name__ == "__main__":
    print(json.dumps(controls(), indent=2, sort_keys=True))
