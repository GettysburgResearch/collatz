"""Count consecutive critical Collatz parity blocks by exact ordinary lifting.

Use --histogram through modest lengths to inspect every shell modulo 2^L.
A histogram costs O(A_L^2) operations and O(2^L) memory. Without it the
program keeps an explicit stack and counts just the requested shells.
"""

import argparse
import json
from collections import Counter


def thresholds(length):
    powers = [1]
    lower = []
    for t in range(length + 1):
        while powers[-1] < 1 << t:
            powers.append(3 * powers[-1])
        lower.append(len(powers) - 1)
    return powers, lower


def critical_pairs(length):
    powers, lower = thresholds(length)
    target = lower[-1]
    stack = [(0, 0, 0, 0)]
    while stack:
        t, count, residue, endpoint = stack.pop()
        if t == length:
            yield residue, endpoint
            continue
        for parity in (0, 1):
            next_count = count + parity
            next_t = t + 1
            if not lower[next_t] <= next_count <= target:
                continue
            if next_count + length - next_t < target:
                continue
            lift = (endpoint & 1) ^ parity
            lifted = endpoint + lift * powers[count]
            new_endpoint = (3 * lifted + 1 if parity else lifted) // 2
            stack.append((next_t, next_count, residue + (lift << t), new_endpoint))


def critical_endpoint(value, lower):
    count = 0
    for t in range(1, len(lower)):
        odd = value & 1
        count += odd
        if count < lower[t] or count > lower[-1]:
            return None
        value = (3 * value + 1 if odd else value) // 2
    return value if count == lower[-1] else None


def observe(length, shells, histogram=False, check=False):
    modulus = 1 << length
    mask = modulus - 1
    powers, lower = thresholds(length)
    multiplier = powers[-1]
    counts = [0] * len(shells)
    total = 0
    residues = set()
    endpoint_counts = Counter()
    for residue, endpoint in critical_pairs(length):
        total += 1
        for i, shell in enumerate(shells):
            if critical_endpoint(endpoint + shell * multiplier, lower) is not None:
                counts[i] += 1
        if histogram or check:
            residues.add(residue)
            endpoint_counts[endpoint & mask] += 1
    result = {"length": length, "weight": lower[-1], "first_count": total,
              "both": dict(zip(shells, counts))}
    if check:
        direct = {x for x in range(modulus) if critical_endpoint(x, lower) is not None}
        if direct != residues:
            raise AssertionError("lifted parity residues disagree with ordinary enumeration")
        for shell, count in zip(shells, counts):
            actual = 0
            for x in direct:
                y = critical_endpoint(x + shell * modulus, lower)
                if y is None:
                    raise AssertionError("first-block discrepancy after source lift")
                actual += critical_endpoint(y, lower) is not None
            if actual != count:
                raise AssertionError("second-block discrepancy")
    if histogram:
        # Index by the shift (3^q j) mod 2^L to avoid one modular inverse per pair.
        by_shift = [0] * modulus
        for endpoint, multiplicity in endpoint_counts.items():
            for residue in residues:
                by_shift[(residue - endpoint) & mask] += multiplicity
        if sum(by_shift) != total**2:
            raise AssertionError("shell correlation sum mismatch")
        if any(by_shift[(j * multiplier) & mask] != n for j, n in zip(shells, counts)):
            raise AssertionError("correlation histogram disagrees with ordinary tests")
        maximum = max(by_shift)
        inverse = pow(multiplier, -1, modulus)
        first_max = min((i * inverse) & mask for i, n in enumerate(by_shift) if n == maximum)
        result.update({"max_both": maximum, "first_max_shell": first_max,
                       "sum_squares_both": sum(n*n for n in by_shift)})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-length", type=int, default=6)
    parser.add_argument("--max-length", type=int, default=16)
    parser.add_argument("--shells", type=int, nargs="+", default=[0, 1])
    parser.add_argument("--histogram", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.min_length < 1 or args.min_length > args.max_length or min(args.shells) < 0:
        parser.error("use positive lengths in increasing order and nonnegative shells")
    for length in range(args.min_length, args.max_length + 1):
        print(json.dumps(observe(length, args.shells, args.histogram, args.check), sort_keys=True),
              flush=True)


if __name__ == "__main__":
    main()
