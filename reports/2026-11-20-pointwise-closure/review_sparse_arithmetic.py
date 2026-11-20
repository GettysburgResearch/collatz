"""Independent small arithmetic reconstruction for the sparse-spectrum review."""

import itertools
import json
import random


def U(n):
    z = 3 * n + 1
    exponent = 0
    while z % 2 == 0:
        z //= 2
        exponent += 1
    return z, exponent


def bit_positions(n):
    answer = []
    j = 0
    while n:
        if n % 2:
            answer.append(j)
        n //= 2
        j += 1
    return answer


def demand(x, msg):
    if not x:
        raise RuntimeError(msg)


solutions = set()
pair_checks = 0
for h in range(1, 201):
    scale = 3**h
    for u in [1] + [2**j + 1 for j in range(1, 81)]:
        v = scale * u
        # Independent two-bit detection: v-1 is a positive power of two.
        p = v - 1
        if p > 0 and p & (p - 1) == 0:
            solutions.add((u, v, h))
        pair_checks += 1
demand(solutions == {(1, 3, 1), (1, 9, 2), (3, 9, 1)}, "E2 sample")

rng = random.Random(20261120)
cuts = 0
identities = 0
for r in range(2, 9):
    for _ in range(80):
        positions = [0] + sorted(rng.sample(range(1, 301), r - 1))
        n = sum(2**j for j in positions)
        for left, D in zip(positions, positions[1:]):
            d = D - left
            J = (d - 1) // 2
            u, v = divmod(n, 2**D)
            actual, shadow, A = n, v, 0
            for j in range(J + 1):
                demand(A < D, "cut capacity")
                demand(2**A * shadow <= 4**j * v < 2**D, "scaled lower bound")
                demand(actual == 2**(D - A) * 3**j * u + shadow, "cut identity")
                demand(len(bit_positions(actual)) == len(bit_positions(3**j * u)) + len(bit_positions(shadow)), "disjoint blocks")
                if r <= 3 and len(bit_positions(actual)) <= r:
                    demand(j in ({0} if r == 2 else {0, 1, 2}), "small spectrum")
                identities += 1
                if j < J:
                    actual, actual_exp = U(actual)
                    shadow, shadow_exp = U(shadow)
                    demand(actual_exp == shadow_exp, "valuation handoff")
                    A += shadow_exp
            cuts += 1

occupancy = 0
reserved = 0
for n in list(range(1, 1000, 2)) + [2**q + 1 for q in (80, 160, 320)]:
    path, used = [], set()
    x = n
    while x not in used and len(path) < 400:
        path.append(x)
        used.add(x)
        x = U(x)[0]
    for S, K in ((2, 1), (3, 3)):
        for L in range(1, 21):
            i = 0
            short = 0
            windows = []
            while i < len(path):
                positions = bit_positions(path[i])
                if len(positions) <= S:
                    gaps = [b - a for a, b in zip(positions, positions[1:])]
                    if gaps and max(gaps) > 2 * L:
                        end = min(i + L, len(path))
                        count = sum(len(bit_positions(v)) <= S for v in path[i:end])
                        demand(count <= K, "reserved-window spectrum")
                        windows.append((i, end))
                        reserved += 1
                        i = end
                        continue
                    short += 1
                i += 1
            demand(short <= sum((2 * L)**j for j in range(S)), "short-gap count")
            demand(len(windows) <= (len(path) + L - 1) // L, "window packing")
            observed = sum(len(bit_positions(v)) <= S for v in path)
            demand(observed <= short + K * len(windows), "coverage partition")
            occupancy += 1

print(json.dumps({
    "status": "PASS", "two_bit_pairs": pair_checks,
    "random_sparse_cuts_popcount_2_through_8": cuts,
    "cut_identity_states": identities,
    "greedy_occupancy_decompositions": occupancy,
    "reserved_windows_checked": reserved,
    "scope": "Independent bounded arithmetic only; S-unit theorem and universal proofs reviewed separately."
}, indent=2, sort_keys=True))
