"""Exhaust finite raw suffix permutations and signed cross-bracket estimates."""
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def verify(condition, detail):
    if not condition:
        raise ValueError(detail)


def code(source, depth):
    result = 0
    for j in range(depth):
        if source % 2:
            result |= 1 << j
            source = (3 * source + 1) // 2
        else:
            source //= 2
    return result


def run():
    totals = dict(slope_cylinders=0, joint_word_pairs=0, conditional_suffix_permutations=0,
                  conditional_endpoint_signed_moments=0, exact_prefix_checks=0,
                  actual_numerical_separations=0, selected_slope_residues=0)
    digest = hashlib.sha256()
    for t in range(2, 9):
        size = 1 << t
        parity = [code(x, t) for x in range(size)]
        verify(len(set(parity)) == size, ("full word permutation", t))
        offsets = (-3, -1, 0, 1, 3)
        for L in range(1, t + 1):
            stride = 1 << L
            bases = sorted({pow(3, h, stride) for h in offsets})
            for base in bases:
                totals["slope_cylinders"] += 1
                count = size // stride
                maximal_sums = [0] * count
                for x in range(size):
                    zero_prefix = t if x == 0 else (x & -x).bit_length() - 1
                    release = min(t, L + zero_prefix)
                    tail_length = t - release
                    reference = parity[base * x % size]
                    suffixes = []
                    centered_sum = 0
                    centered_squares = 0
                    for K in range(count):
                        slope = base + stride * K
                        other = parity[(slope * x) % size]
                        verify((other ^ reference) % (1 << release) == 0,
                               ("matched prefix", t, L, x, slope))
                        totals["exact_prefix_checks"] += 1
                        totals["joint_word_pairs"] += 1
                        if K < 1 << tail_length:
                            suffixes.append(other >> release)
                        disagreement = parity[x] ^ other
                        suffix_score = tail_length - 2 * (disagreement >> release).bit_count()
                        centered_sum += suffix_score
                        centered_squares += suffix_score * suffix_score
                        partial, maximum = 0, 0
                        for k in range(L, t):
                            partial += 1 - 2 * ((disagreement >> k) & 1)
                            maximum = max(maximum, abs(partial))
                        maximal_sums[K] += maximum
                    verify(len(set(suffixes)) == len(suffixes) == 1 << tail_length,
                           ("suffix bijection", t, L, x, base))
                    verify(centered_sum == 0 and centered_squares == count * tail_length,
                           ("signed agreement mean/variance", t, L, x, base))
                    totals["conditional_suffix_permutations"] += 1
                    totals["conditional_endpoint_signed_moments"] += 1
                best = min(range(count), key=maximal_sums.__getitem__)
                excess = max(0, maximal_sums[best] - size)
                verify(excess ** 2 <= 4 * size ** 2 * t,
                       ("quenched maximal budget", t, L, base))
                residue = base + stride * best
                high = next(c for c in range(4 ** t + residue, 4 ** t + residue + 3 * size, size)
                            if math.gcd(c, 6) == 1)
                for x in (1, 2, 3, 7, size - 1, 2 * size + 1):
                    a, b = x, high * x
                    verify(code(b, t) == parity[residue * x % size], "selected lift")
                    for _ in range(t + 1):
                        verify(a < b, "positive integer intersection")
                        totals["actual_numerical_separations"] += 1
                        a = (3 * a + 1) // 2 if a % 2 else a // 2
                        b = (3 * b + 1) // 2 if b % 2 else b // 2
                digest.update(f"{t} {L} {base} {residue} {maximal_sums[best]}\n".encode())
                totals["selected_slope_residues"] += 1
    return {"scope": "Exact finite 2-adic cylinders and positive integer paths; asymptotic laws are written proofs.",
            "maximum_word_length": 8, "counts": totals, "selection_table_sha256": digest.hexdigest()}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
