#!/usr/bin/env python3
"""Independent finite arithmetic controls for the round-three proofs.

Exact integers and fractions are used throughout. These finite executions
do not assert an infinite injective orbit, a universal collision decay,
or a successful triadic candidate for an unrestricted source. Every check
remains active under Python -O.
"""

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def chronological_carry(word):
    carry = 0
    for clock, bit in enumerate(word):
        carry = 3 * carry + 2**clock if bit else carry
    return carry


def carry_from_positions(word):
    positions = [i for i, bit in enumerate(word) if bit]
    return sum(3**(len(positions) - 1 - i) * 2**d
               for i, d in enumerate(positions))


def decode_carry(length, ones, carry):
    word = []
    for _ in range(length):
        bit = carry % 2
        ones -= bit
        require(ones >= 0, "invalid carry weight")
        residual = carry - bit * 3**ones
        require(residual >= 0 and residual % 2 == 0,
                "invalid chronological carry")
        carry = residual // 2
        word.append(bit)
    require(ones == 0 and carry == 0, "incomplete carry decoder")
    return tuple(word)


def shortcut(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def replay_word(n, word):
    q = n
    for bit in word:
        require(q % 2 == bit, "word is not legal at unchanged source")
        q = shortcut(q)
    return q


def odd_step(n):
    require(n > 0 and n % 2 == 1, "not a positive ordinary odd state")
    q, gap = 3 * n + 1, 0
    while q % 2 == 0:
        q //= 2
        gap += 1
    return q, gap


def odd_window(n, depth):
    q, gaps, values = n, [], [n]
    for _ in range(depth):
        q, gap = odd_step(q)
        gaps.append(gap)
        values.append(q)
    word = tuple(bit for gap in gaps for bit in (1,) + (0,) * (gap - 1))
    total = sum(gaps)
    partial, carry = 0, 0
    for i, gap in enumerate(gaps):
        carry += 3**(depth - 1 - i) * 2**partial
        partial += gap
    require(carry == chronological_carry(word), "gap/shortcut carry mismatch")
    require(2**total * q == 3**depth * n + carry, "full physical identity failed")
    return {"source": n, "endpoint": q, "gaps": tuple(gaps), "word": word,
            "A": total, "m": depth, "C": carry, "values": values}


def word_controls(max_length=12):
    counts = defaultdict(int)
    omitted_quotient_example = None
    omitted_source_block_example = None
    for length in range(max_length + 1):
        words_by_weight = defaultdict(list)
        for word in product((0, 1), repeat=length):
            ones = sum(word)
            carry = chronological_carry(word)
            require(carry == carry_from_positions(word), "independent carry formula failed")
            require(decode_carry(length, ones, carry) == word, "word was not recovered")
            require(carry < 2**length * 3**ones, "coarse full-carry bound failed")
            counts["complete_words"] += 1
            words_by_weight[ones].append((word, carry))
        for ones, records in words_by_weight.items():
            Q = 3**ones
            for width in (1, 2, 4, 7):
                fibers = defaultdict(list)
                for word, carry in records:
                    fibers[(carry // Q) // width, carry % Q].append(word)
                for fiber in fibers.values():
                    require(len(fiber) <= width, "translated quotient fiber too large")
                    counts["translated_carry_fibers"] += 1
            boxes = {}
            without_quotient = {}
            for word, carry in records:
                modulus = 2**length
                residue = (-carry * pow(3**ones, -1, modulus)) % modulus if length else 0
                endpoints = []
                for source_block in range(1, 5):
                    n = residue + source_block * modulus
                    q = replay_word(n, word)
                    require(modulus * q == Q * n + carry, "supplied affine identity failed")
                    key = (carry // Q, n // modulus, q % Q)
                    require(key not in boxes or boxes[key] == (word, n, q),
                            "actual source-box injection failed")
                    boxes[key] = (word, n, q)
                    counts["ordinary_box_occurrences"] += 1
                    endpoints.append((n, q))
                    weak_key = (n // modulus, q % Q)
                    if weak_key in without_quotient and without_quotient[weak_key][0] != word:
                        if omitted_quotient_example is None:
                            omitted_quotient_example = {
                                "length": length, "ones": ones, "first": without_quotient[weak_key],
                                "second": (word, n, q), "residue": q % Q,
                            }
                    without_quotient[weak_key] = (word, n, q)
                require(endpoints[0][0] != endpoints[1][0]
                        and endpoints[0][1] % Q == endpoints[1][1] % Q,
                        "source-block deletion control did not collide")
                if omitted_source_block_example is None and ones > 0:
                    omitted_source_block_example = {"word": word, "sources_endpoints": endpoints[:2]}
    require(omitted_quotient_example is not None and omitted_source_block_example is not None,
            "missing required damaged-box controls")
    return {"maximum_shortcut_length": max_length, "counts": dict(counts),
            "discarding_carry_quotient_rejected": omitted_quotient_example,
            "discarding_source_quotient_rejected": omitted_source_block_example}


def distinct_orbit(seed):
    values, seen = [], set()
    q = seed
    while q not in seen:
        require(len(values) < 10000, "finite fixture exceeded declared clock cap")
        seen.add(q)
        values.append(q)
        q, _ = odd_step(q)
    require(q == 1, "fixture did not end at the known cycle")
    return values


def collision(records, Q):
    masses = defaultdict(Fraction)
    for row in records:
        masses[row["endpoint"] % Q] += row["weight"]
    return sum((mass**2 for mass in masses.values()), Fraction(0))


def diagonal(records):
    return sum((row["weight"]**2 for row in records), Fraction(0))


def word_squares(records):
    masses = defaultdict(Fraction)
    for row in records:
        masses[row["word"]] += row["weight"]
    return sum((mass**2 for mass in masses.values()), Fraction(0))


def window_controls(orbits):
    counts = defaultdict(int)
    saw_repeated_word = False
    saw_cross_box_collision = False
    for values in orbits:
        N = len(values)
        for m in range(1, min(9, N)):
            records = []
            for j in range(m, N):
                row = odd_window(values[j - m], m)
                require(row["endpoint"] == values[j], "window lost its original occurrence")
                row["weight"] = Fraction(j + 1, N * (j + 2))
                row["k"] = row["C"] // 3**m
                row["ell"] = row["source"] // 2**row["A"]
                kappa = Fraction(1)
                for x in row["values"][:-1]:
                    kappa *= Fraction(3 * x, 3 * x + 1)
                B = max(Fraction(row["source"], x) for x in row["values"])
                require(Fraction(row["C"], 3**m) <= Fraction(m, 3) * B / kappa,
                        "physical carry width estimate failed")
                require(Fraction(row["C"], 2**row["A"]) <= Fraction(3, 2)**m - 1,
                        "complete physical remainder bound failed")
                records.append(row)
                counts["original_windows"] += 1
            Q = 3**m
            quotient_channels = defaultdict(list)
            boxes = defaultdict(list)
            for row in records:
                quotient_channels[row["A"], row["k"]].append(row)
                boxes[row["A"], row["k"], row["ell"]].append(row)
            for group in quotient_channels.values():
                require(collision(group, Q) == word_squares(group), "quotient-channel equality failed")
                require(word_squares(group) >= diagonal(group), "negative repeated-word mass")
                saw_repeated_word |= word_squares(group) > diagonal(group)
                sources_by_word = defaultdict(list)
                for row in group:
                    sources_by_word[row["word"]].append(row["source"])
                for sources in sources_by_word.values():
                    modulus = 2**group[0]["A"]
                    require(len({n % modulus for n in sources}) == 1,
                            "equal words lost source congruence")
                    H = max(sources) - min(sources)
                    require(len(sources) <= 1 + H // modulus, "source interval spacing failed")
                counts["exact_quotient_channels"] += 1
            for group in boxes.values():
                require(collision(group, Q) == diagonal(group), "source box had an off-diagonal")
                counts["exact_source_boxes"] += 1
            for width in (2, 5):
                bands = defaultdict(list)
                for row in records:
                    bands[row["A"], row["k"] // width].append(row)
                for group in bands.values():
                    require(collision(group, Q) <= width * word_squares(group),
                            "weighted translated-fiber upper failed")
                    counts["weighted_interval_groups"] += 1
            sum_box_energies = sum((collision(group, Q) for group in boxes.values()), Fraction(0))
            full_collision = collision(records, Q)
            saw_cross_box_collision |= full_collision > sum_box_energies
            require(full_collision <= len(boxes) * sum_box_energies,
                    "Cauchy aggregation with all cross terms failed")
            counts["full_aggregation_checks"] += 1
    require(saw_repeated_word and saw_cross_box_collision,
            "fixtures did not exercise both retained correlation terms")
    return {"counts": dict(counts), "dropping_repeated_words_rejected": saw_repeated_word,
            "dropping_cross_box_terms_rejected": saw_cross_box_collision,
            "weights": "exact t_j=(j+1)/(N*(j+2))≤1/N; finite test weights, not asserted harmonic-flow samples"}


def floor_log3(n):
    p, e = 1, 0
    while 3 * p <= n:
        p *= 3
        e += 1
    return e


def count_controls(orbits):
    counts = defaultdict(int)
    for K in range(2, 81):
        for m in range(1, K):
            left = sum((Fraction(comb(A - 1, m - 1), 2**A)
                        for A in range(m, K)), Fraction(0))
            right = Fraction(sum(comb(K - 1, j) for j in range(m, K)), 2**(K - 1))
            require(left == right, "negative-binomial exact identity failed")
            counts["exact_binomial_identities"] += 1
    for X in (24, 31, 64, 127, 256, 511, 1024, 2048, 4096):
        K = X.bit_length() - 1
        m = floor_log3(X // 8)
        low_count = 0
        residues = {}
        for n in range(1, X + 1, 2):
            row = odd_window(n, m)
            if row["A"] >= K:
                require(2 * row["endpoint"] < X, "high-clock compression failed")
                counts["ordinary_high_clock_sources"] += 1
            else:
                key = row["gaps"]
                residue = n % 2**(row["A"] + 1)
                require(key not in residues or residues[key] == residue,
                        "exact final-odd cylinder changed residue")
                residues[key] = residue
                low_count += 1
        budget = X * sum((Fraction(comb(A - 1, m - 1), 2**A)
                          for A in range(m, K)), Fraction(0))
        require(low_count <= budget, "complete low-lane source bound failed")
        counts["all_source_low_lane_bounds"] += 1
        for values in orbits:
            high_images = []
            full_count = sum(n <= X for n in values)
            lower_count = sum(2 * n <= X for n in values)
            terminal_unpaid = sum(n <= X for n in values[max(0, len(values) - m):])
            for i, n in enumerate(values[:max(0, len(values) - m)]):
                if n > X:
                    continue
                row = odd_window(n, m)
                require(row["endpoint"] == values[i + m], "fixed odd clock was changed")
                if row["A"] >= K:
                    high_images.append(row["endpoint"])
            require(len(high_images) == len(set(high_images)) <= lower_count,
                    "same-orbit high-lane injection failed")
            require(full_count <= lower_count + budget + terminal_unpaid,
                    "finite segment failed after exact terminal allowance")
            counts["separated_visit_charges_with_terminal_allowance"] += 1
    require(odd_step(1)[0] == odd_step(5)[0] == 1,
            "noninjective basin control did not collide")
    return {"counts": dict(counts), "whole_basin_injectivity_rejected": [1, 5],
            "finite_boundary": "each finite fixture pays its final m source positions; no infinite orbit is fabricated"}


def cycle_conditioning_control():
    words = ((1, 0), (0, 1))
    residues = {str((u, v)): (3 * chronological_carry(u) + 4 * chronological_carry(v)) % 7
                for u in words for v in words}
    require(list(residues.values()) == [0, 4, 3, 0], "known full-D conditioning control failed")
    bound = sum(min(comb(6, j), comb(7, 8 - j)) for j in range(1, 7))
    require(bound == 50, "complete split matching example failed")
    return {"full_denominator": 7, "four_actual_word_residues": residues,
            "matching_bound_at_A13_p8": bound,
            "scope": "known trivial-cycle repetitions; no new positive cycle asserted"}


def main():
    seeds = [1, 3, 7, 27, 97, 871, 6171, 837799, 670617279, 2**31 - 1]
    orbits = [distinct_orbit(n) for n in seeds]
    report = {
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "bounded exact arithmetic controls, never a universal convergence test",
        "word_controls": word_controls(),
        "ordinary_fixtures": [{"source": seed, "distinct_odd_states": len(values), "peak": max(values)}
                              for seed, values in zip(seeds, orbits)],
        "actual_windows": window_controls(orbits),
        "global_count_interfaces": count_controls(orbits),
        "full_cycle_conditioning": cycle_conditioning_control(),
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
