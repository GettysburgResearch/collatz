"""Exact controls for moving clusters and integer separation of odd phases."""
from collections import Counter
from hashlib import sha256
from itertools import product
from math import gcd, isqrt
import json


def require(ok, description):
    if not ok:
        raise ArithmeticError(description)


def states(gaps):
    """Replay all accelerated rational phases over one odd denominator."""
    p = len(gaps)
    A = sum(gaps)
    D = 2 ** A - 3 ** p
    require(D > 0, "positive determinant required")
    C = 0
    E = 0
    for e in gaps:
        C = 3 * C + (1 << E)
        E += e
    g = gcd(C, D)
    d = D // g
    nums = [C // g]
    for e in gaps:
        temp = 3 * nums[-1] + d
        require(temp % (1 << e) == 0 and (temp >> e) % 2 == 1, "clock error")
        nums.append(temp >> e)
    require(nums[-1] == nums[0], "cycle replay")
    return nums[:-1], d, D


def check_shadow(gaps, counts):
    p = len(gaps)
    A = sum(gaps)
    nums, d, _ = states(gaps)
    if len(set(nums)) != p:
        return
    counts["primitive_words"] += 1
    least_index = nums.index(min(nums))
    nums *= 3
    gaps *= 3
    dates = [0]
    for e in gaps:
        dates.append(dates[-1] + e)
    for v in range(1, p):
        B = [dates[i + v] - dates[i] for i in range(p)]
        for u, freq in Counter(B).items():
            m = p - freq
            require(m > 0, "primitive cycle has a defect")
            counts["windows"] += 1
            for i, b in enumerate(B):
                if b != u:
                    continue
                counts["good_starts"] += 1
                H = 1
                while B[(i + H) % p] == u:
                    H += 1
                k = H - 1
                e = dates[i + k] - dates[i]
                diff = nums[i] - nums[i + v]
                z, rem = divmod(diff, 1 << (e + 1))
                require(rem == 0 and z, "initial difference parameter")
                require(nums[i + k] - nums[i + v + k] == 2 * 3 ** k * z,
                        "terminal difference parameter")
                for j in range(k + 1):
                    remaining = dates[i + k] - dates[i + j]
                    require(nums[i + j] - nums[i + j + v] == (2 << remaining) * 3 ** j * z,
                            "joint dyadic and ternary divisibility")
                t = (i - least_index) % p
                L = (A + p - 1) // p
                require(max(nums[i], nums[i + v]) * 3 ** p <=
                        min(nums[i], nums[i + v]) * (1 << (L * m + A)),
                        "two-sided good-start ratio")
                require((1 << (H + t)) * 3 ** p <=
                        (nums[least_index] + d) * 3 ** t * (1 << (L * m + A)),
                        "minimum-rooted run bound")


def check_cluster(p, A, all_windows):
    k = isqrt(p)
    positions = list(range(p // 2, p // 2 + k))
    gaps = [1] * p
    for i in positions:
        gaps[i] = 2 + ((i * i * 17 + (i >> 2)) % 7 < 3)
    gaps[0] += A - sum(gaps)
    require(gaps[0] - 1 > sum(gaps[i] - 1 for i in positions), "isolated largest jump")
    nums, d, D = states(gaps)
    require(len(set(nums)) == p and gcd(p, A) == 1, "primitive coprime clocks")
    dates = [0]
    for e in gaps * 2:
        dates.append(dates[-1] + e)
    support = [i for i in range(p) if gaps[i] != 1]
    require(support == [0, *positions], "one giant and one microcluster")
    widths = [max(xs) - min(xs) for xs in (
        [dates[i] for i in positions], [dates[i + 1] for i in positions], positions)]
    require(max(widths) <= 3 * k, "rectangle widths")
    minimum = None
    if all_windows:
        for v in range(1, p):
            frequencies = Counter(dates[i + v] - dates[i] for i in range(p))
            best = p - max(frequencies.values())
            require(2 * best >= k, "every lag has many exceptions")
            minimum = best if minimum is None else min(best, minimum)
    return {
        "odd_period": p,
        "native_clock": A,
        "microcluster_size": k,
        "largest_patch_width": max(widths),
        "global_minimum_defect_count": minimum,
        "whole_determinant_bits": D.bit_length(),
        "reduced_denominator_bits": d.bit_length(),
        "denominator_sha256": sha256(d.to_bytes((d.bit_length() + 7) // 8, "big")).hexdigest(),
    }


def main():
    counts = Counter()
    for p in range(2, 7):
        for word in product((1, 2, 3), repeat=p):
            if 2 ** sum(word) > 3 ** p:
                check_shadow(list(word), counts)
    fixture = [check_cluster(p, a, small) for p, a, small in
               [(41, 65, True), (306, 485, True), (15601, 24727, False)]]
    print(json.dumps({"integer_checks": dict(sorted(counts.items())),
                      "arbitrary_patch_words": fixture}, indent=2))


if __name__ == "__main__":
    main()
