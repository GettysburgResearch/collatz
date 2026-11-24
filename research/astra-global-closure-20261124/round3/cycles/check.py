"""Exact controls for signed rotation products and circular swap distance."""

import argparse
import json
from collections import deque
from math import gcd, prod


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def rotate(word, shift):
    return word[shift:] + word[:shift]


def distances(start):
    """Shortest physical adjacent-swap distance on the entire equal-weight layer."""
    queue = deque([start])
    dist = {start: 0}
    while queue:
        word = queue.popleft()
        for i, bit in enumerate(word):
            j = (i + 1) % len(word)
            if bit == word[j]:
                continue
            other = list(word)
            other[i], other[j] = other[j], other[i]
            other = tuple(other)
            if other not in dist:
                dist[other] = dist[word] + 1
                queue.append(other)
    return dist


def reduced_cycle(word):
    length = len(word)
    gap = 2**length - 3**sum(word)
    carry = 0
    for i, bit in enumerate(word):
        carry = (3 if bit else 1) * carry + bit * 2**i
    common = gcd(carry, gap)
    d, initial = gap // common, carry // common
    states = []
    n = initial
    for bit in word:
        require(n % 2 == bit and gcd(n, d) == 1, "reduced parity")
        states.append(n)
        n = ((3 * n + d) if bit else n) // 2
    require(n == initial and len(set(states)) == length, "primitive closure")
    return d, states


def valuation(n, prime):
    require(n != 0, "valuation at zero")
    exponent = 0
    while n % prime == 0:
        n //= prime
        exponent += 1
    return exponent


def check_rotations(word, d, states):
    length = len(word)
    for shift in range(1, length):
        before, after = [], []
        for n, m in zip(states, rotate(states, shift)):
            if (n - m) % 2:
                odd, even = (n, m) if n % 2 else (m, n)
                before.append(odd - even)
                after.append(3 * odd + d - even)
        common_odd = sum(word) - len(before) // 2
        require(2**length * prod(before) == 3**common_odd * prod(after), "signed product")
        require(sum(valuation(n, 2) for n in after) == length, "dyadic budget")
        require(sum(valuation(n, 3) for n in before)
                - sum(valuation(n, 3) for n in after) == common_odd, "triadic budget")


def check(limit):
    result = {"maximum_length": limit, "primitive_contracting_necklaces": 0,
              "rotation_products": 0, "physical_swap_comparisons": 0}
    for length in range(2, limit + 1):
        for p in range(1, length):
            gap = 2**length - 3**p
            if gap <= 0:
                continue
            u = tuple(((i+1)*p)//length - (i*p)//length for i in range(length))
            g = gcd(p, length)
            shift = pow(p, -1, length) if g == 1 else length // g
            delta = 2 if g == 1 else 0
            seen = {}
            for word, cost in distances(u).items():
                rotations = {rotate(word, n) for n in range(length)}
                if len(rotations) != length:
                    continue
                base = min(rotations)
                if base not in seen:
                    d, states = reduced_cycle(base)
                    check_rotations(base, d, states)
                    seen[base] = d
                    result["primitive_contracting_necklaces"] += 1
                    result["rotation_products"] += length - 1
                d = seen[base]
                flux = [0]
                for actual, target in zip(word, u):
                    flux.append(flux[-1] + actual - target)
                spread = max(flux) - min(flux)
                require(spread**2 <= 2*cost, "transport range")
                mismatch = sum(a != b for a, b in zip(word, rotate(word, shift)))
                bound = 4*cost + delta
                require(0 < mismatch <= bound, "reference shift")
                require((d*p*2**length*3**(1+spread))**bound
                        > 2**length * gap**bound, "full denominator estimate")
                result["physical_swap_comparisons"] += 1
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=13)
    print(json.dumps(check(parser.parse_args().max_length), sort_keys=True))
