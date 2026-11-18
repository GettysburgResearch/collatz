"""Reconstruct the source bank from affine congruences and replay raw steps."""
import argparse
import json
from fractions import Fraction
from pathlib import Path


def affine_sources(limit):
    yield 1
    # A prefix represents T^k(n) = (m*n+c)/h. During extension solve
    # this affine congruence at precision 2h without using the producer's
    # recursive forward state or lifting a stored source.
    stack = [(0, 1, 1, 0)]
    while stack:
        cost, h, m, c = stack.pop()
        for bit in (0, 1):
            new_cost = cost + 2 - bit
            if new_cost > limit or (h == 1 and bit == 0):
                continue
            modulus = 2 * h
            residue = ((h * bit - c) * pow(m, -1, modulus)) % modulus
            yield modulus + residue
            if bit:
                stack.append((new_cost, modulus, 3 * m, 3 * c + h))
            else:
                stack.append((new_cost, modulus, m, c))


def raw_cost(source):
    n = source
    cost = 0
    for _ in range(source.bit_length() - 1):
        if n % 2:
            n = (3 * n + 1) // 2
            cost += 1
        else:
            n //= 2
            cost += 2
    return cost


def check(receipt):
    budget, bits = receipt["budget"], receipt["fraction_bits"]
    rows = receipt["rows"]
    clocks = {r["clock"] for r in rows}
    if len(clocks) != len(rows) or min(clocks) < 1 or min(budget, bits) < 1:
        raise ValueError("invalid receipt parameters")
    # Exact cost-level counts obtained as coefficients of z / (1-z-z^2).
    counts = [0, 1]
    while len(counts) <= budget + 2:
        counts.append(counts[-1] + counts[-2])
    count = 1 + sum(counts[:budget + 1])
    if count != receipt["source_count"]:
        raise ValueError("wrong source cardinality")
    for small in range(1, min(12, budget) + 1):
        direct = [x for x in range(1, 2 ** (small + 1), 2)
                  if raw_cost(x) <= small]
        if sorted(affine_sources(small)) != direct:
            raise ValueError("small exhaustive source comparison failed")
    scale = 1 << bits
    numerators = {q: scale * 3 ** (4 * q) for q in clocks}
    sums = dict.fromkeys(clocks, 0)
    maximum = max(clocks)
    visited = 0
    for source in affine_sources(budget):
        visited += 1
        state = source
        steps = 0
        q = 0
        while q < maximum:
            state = (3 * state + 1) // 2
            steps += 1
            while state % 2 == 0:
                state //= 2
                steps += 1
            q += 1
            if q in numerators:
                sums[q] += numerators[q] // (state ** 2 << (4 * steps))
    if visited != count:
        raise ArithmeticError("wrong number of replayed paths")
    # The full Fibonacci generating function is 4/11 at z=1/4.
    remaining_cost = Fraction(4, 11) - sum(
        Fraction(counts[d], 4 ** d) for d in range(1, budget + 1))
    for row in rows:
        q = row["clock"]
        minimum_k = max(q + 1, (budget + 3) // 2)
        other_lifts = min(Fraction(3 ** q, 2 * 5 ** q),
                          Fraction(9 ** q, 7 ** q * 2 ** minimum_k))
        tail = other_lifts + Fraction(9, 4) ** q * remaining_cost
        error = count + (scale * tail.numerator + tail.denominator - 1) // tail.denominator
        if (row["lower_units"], row["upper_units"]) != (sums[q], sums[q] + error):
            raise ValueError(f"certificate mismatch at clock {q}")
    return visited


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path)
    args = parser.parse_args()
    source_count = check(json.loads(args.receipt.read_text()))
    print(f"Verified {source_count} source paths")
