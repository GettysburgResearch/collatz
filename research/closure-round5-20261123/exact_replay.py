#!/usr/bin/env python3
"""Exact finite controls for round five; no infinite-orbit inference.

Run from any working directory. Every guard survives python -O. The
infinite entropy and dimension theorems are written proofs, not claims
certified by these bounded computations.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from replay_carry_cycle import run_checks as carry_cycle_checks
from replay_rational import run_checks as rational_checks


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def ordinary_states(n):
    states = [n]
    seen = {n}
    while states[-1] != 1:
        require(len(states) < 10000, "finite ordinary fixture exceeded its cap")
        x = states[-1]
        y = (3 * x + 1) // 2 if x % 2 else x // 2
        require(y not in seen, "unexpected repeat in convergent fixture")
        states.append(y)
        seen.add(y)
    return states


def forward_carry(bits):
    count, carry = 0, 0
    for clock, bit in enumerate(bits):
        carry = 3 * carry + (1 << clock) if bit else carry
        count += bit
    return count, carry


def source_pressure_checks():
    counts = Counter()
    sources = list(range(1, 257)) + [6171, 77031, 837799]
    for source in sources:
        states = ordinary_states(source)
        counts["ordinary_sources"] += 1
        N = len(states) - 1
        bits = tuple(x % 2 for x in states[:-1])
        H = max(states)
        long_m = H.bit_length()
        lengths = set(range(1, min(N, 10) + 1))
        if 1 <= long_m <= N:
            lengths.add(long_m)
        for m in sorted(lengths):
            words = defaultdict(list)
            for j in range(N - m + 1):
                word = bits[j:j + m]
                p, C = forward_carry(word)
                require((1 << m) * states[j + m] == 3 ** p * states[j] + C,
                        "ordinary complete affine identity")
                words[word].append(states[j])
                counts["literal_affine_words"] += 1
            for values in words.values():
                require(len({v % (1 << m) for v in values}) == 1,
                        "same word lost original binary source residue")
                require(len(values) <= H // (1 << m) + 1,
                        "height-cell multiplicity bound")
                counts["source_word_fibres"] += 1
            if (1 << m) > H:
                require(len(words) == N - m + 1, "long-word source injection")
                require(sum(len(v) ** 2 for v in words.values()) == N - m + 1,
                        "exact uniform long-word collision")
                counts["long_word_uniform_laws"] += 1

        # The exact odd-gap words retain the original source endpoint.
        odd_positions = [i for i, x in enumerate(states) if x % 2]
        odd_states = [states[i] for i in odd_positions]
        gaps = [b - a for a, b in zip(odd_positions, odd_positions[1:])]
        M = len(gaps)
        if M == 0:
            continue
        odd_height = max(odd_states)
        for j, gap in enumerate(gaps):
            require((1 << gap) * odd_states[j + 1] == 3 * odd_states[j] + 1,
                    "literal odd edge")
        counts["literal_odd_edges"] += M
        for m in sorted({1, min(M, 4), min(M, 9), min(M, odd_height.bit_length())}):
            fibres = defaultdict(list)
            for endpoint in range(m, M + 1):
                word = tuple(reversed(gaps[endpoint - m:endpoint]))
                A = sum(word)
                prefix = 0
                C = 0
                for i, gap in enumerate(word):
                    prefix += gap
                    C += 3 ** i * (1 << (A - prefix))
                require((1 << A) * odd_states[endpoint] ==
                        3 ** m * odd_states[endpoint - m] + C,
                        "reversed-gap complete endpoint identity")
                modulus = 3 ** m
                require(odd_states[endpoint] % modulus ==
                        C * pow(1 << A, -1, modulus) % modulus,
                        "actual odd-time ternary residue")
                fibres[word].append(odd_states[endpoint - m])
                counts["odd_complete_source_words"] += 1
            for word, values in fibres.items():
                modulus = 1 << sum(word)
                require(len({v % modulus for v in values}) == 1,
                        "equal gap words lost complete binary source congruence")
                if modulus > odd_height:
                    require(len(values) == 1, "good gap word is not unique")
                    counts["good_unique_gap_words"] += 1

        # Exact finite inequality (16), with arbitrary rational centers.
        # This verifies endpoint normalizations, not any ergodic limit.
        for m in sorted({min(M, 5), min(M, 13)}):
            for K in sorted({1, min(m, 3), m}):
                for R in (1, 2, 5):
                    center = Fraction(3, 2)
                    f = [min(g, R) for g in gaps]
                    def deviations(length):
                        return [abs(Fraction(sum(f[j:j + length]), length) - center)
                                for j in range(M - length + 1)]
                    dev_m, dev_K = deviations(m), deviations(K)
                    lhs = sum(dev_m) / len(dev_m)
                    rhs = (Fraction(R * (K - 1), m) +
                           Fraction(M - K + 1, M - m + 1) * sum(dev_K) / len(dev_K))
                    require(lhs <= rhs, "finite truncated growing-window inequality")
                    counts["exact_growing_window_inequalities"] += 1
    return {"scope": "Finite actual prefixes, complete source congruences, exact endpoint averaging; no entropy-limit execution.",
            "counts": dict(sorted(counts.items())),
            "source_range": "1..256, plus 6171, 77031 and 837799; through first ordinary one"}


def main():
    here = Path(__file__).resolve().parent
    source_files = sorted(p for p in here.iterdir()
                          if p.suffix in (".py", ".lean") or p.name in {
                              "TRIADIC_CONSTRUCTION.md", "FIXED_SOURCE_PRESSURE.md",
                              "TERNARY_INFORMATION.md", "CYCLE_EXCLUSION.md"})
    hashes = {p.name: sha256(p.read_bytes()).hexdigest() for p in source_files}
    result = {
        "schema": "collatz-closure-round5-exact/v1",
        "scope": "Exact bounded controls only. Full Collatz, the infinite stationary conclusions and collision upper are not established by execution.",
        "source_sha256": hashes,
        "rational": rational_checks(),
        "source_pressure": source_pressure_checks(),
        "carry_cycle": carry_cycle_checks(),
        "success": True,
    }
    require(hashes == {p.name: sha256(p.read_bytes()).hexdigest() for p in source_files},
            "source bytes changed during replay")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
