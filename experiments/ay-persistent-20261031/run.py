#!/usr/bin/env python3
"""Exact finite-core and sparse-source certificate producer (standard library).

No Collatz convergence assumption is used. An unfinished computation is an
error, never a positive certificate. See the accompanying PROOF.md.
"""
from __future__ import annotations
import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import hashlib
import json
from pathlib import Path


def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)


def odd_step(n: int) -> int:
    z = 3 * n + 1
    return z // (z & -z)


def height(u: int, cap: int) -> int:
    steps = 0
    while u.bit_count() < cap:
        u *= 3
        steps += 1
        require(steps <= (1 << (cap - 1)) - 1, "homogeneous bound failed")
    return steps


def core_sources(cap: int):
    def visit(u: int, remaining: int):
        yield u
        if remaining:
            for gap in range(1, 2 * height(u, cap) + 1):
                yield from visit((u << gap) + 1, remaining - 1)
    yield from visit(1, cap - 1)


def integer_set_hash(values) -> str:
    digest = hashlib.sha256()
    for value in sorted(values):
        digest.update(f"{value}\n".encode("ascii"))
    return digest.hexdigest()


def core_row(cap: int) -> dict:
    memo = {1: ("ONE", 0)}
    successful = set()
    digest = hashlib.sha256()
    histogram = Counter()
    count = largest = longest = 0
    witness = 1
    for source in core_sources(cap):
        count += 1
        largest = max(largest, source)
        n = source
        path = []
        seen = set()
        while n.bit_count() <= cap and n not in memo:
            if n in seen:
                raise ValueError(f"cycle in cap {cap}: {n}")
            seen.add(n)
            path.append(n)
            n = odd_step(n)
        kind, clock = memo.get(n, ("EXIT", 0))
        for n in reversed(path):
            clock += 1
            memo[n] = kind, clock
        kind, clock = memo[source]
        if kind == "ONE":
            successful.add(source)
        if clock > longest:
            longest, witness = clock, source
        histogram[clock] += 1
        digest.update(f"{source},{kind},{clock}\n".encode("ascii"))
    return {
        "cap": cap, "core_size": count, "one": len(successful),
        "exit": count - len(successful), "maximum_delay": longest,
        "witness": witness, "max_core_value": largest,
        "max_bitlength": largest.bit_length(),
        "core_sha256": digest.hexdigest(),
        "basin_sha256": integer_set_hash(successful),
        "largest_basin_value": max(successful),
        "histogram": {str(k): histogram[k] for k in sorted(histogram)},
    }


def modular_bounds(bits: int = 20) -> dict:
    modulus = 1 << bits
    cycles = []
    visited = set()
    for root in (1, 5):
        n = root
        weights = []
        while n not in visited:
            visited.add(n)
            weights.append(n.bit_count())
            n = 3 * n % modulus
        require(n == root and len(weights) == modulus // 4, "bad unit cycle")
        cycles.append(weights)
    require(len(visited) == modulus // 2, "incomplete unit inventory")
    bounds = {}
    for cap in range(2, 11):
        maximum = 0
        for weights in cycles:
            first = next(i for i, w in enumerate(weights) if w >= cap)
            run = 0
            for offset in range(1, len(weights) + 1):
                w = weights[(first + offset) % len(weights)]
                run = run + 1 if w < cap else 0
                maximum = max(maximum, run)
        bounds[str(cap)] = maximum
    return {"modulus_bits": bits, "unit_count": len(visited), "bounds": bounds}


def first_descent(n: int) -> tuple[int, int, int]:
    # The root is a symbolic lift of the 1 -> 2 -> 1 cycle, not a physical
    # trajectory out of the killed state 1. It strictly lowers every 1+4u, u>0.
    if n == 1:
        return 2, 1, 1
    x, clock, odds = n, 0, 0
    while x >= n:
        z = 3 * x + 1
        valuation = (z & -z).bit_length() - 1
        odds += 1
        if (z >> valuation) < n:
            used = (z // n).bit_length()
            require(1 <= used <= valuation, "bad partial-halving clock")
            return clock + used, odds, z >> used
        clock += valuation
        x = z >> valuation
        if clock > 20000:
            raise ValueError(f"unfinished source {n}")
    raise RuntimeError("unreachable")


def sparse_rows(max_weight: int = 8) -> dict:
    level = [1]
    rows = []
    all_digest = hashlib.sha256()
    widths = Counter()
    for weight in range(1, max_weight + 1):
        next_level = []
        digest = hashlib.sha256()
        longest, witness = 0, 1
        for n in level:
            k, odds, endpoint = first_descent(n)
            widths[max(n.bit_length(), k)] += 1
            require(3 ** odds < 2 ** k, "noncontracting certificate")
            require(endpoint < n or n == endpoint == 1, "bad original-source order")
            if k > longest:
                longest, witness = k, n
            row = f"{n},{k},{odds},{endpoint}\n".encode("ascii")
            digest.update(row)
            all_digest.update(row)
            if weight < max_weight:
                next_level.extend(n + (1 << d) for d in range(n.bit_length(), k))
        largest = max(level)
        rows.append({"weight": weight, "nodes": len(level),
                     "maximum_clock": longest, "witness": witness,
                     "max_value": largest, "max_bits": largest.bit_length(),
                     "sha256": digest.hexdigest()})
        level = next_level
    width = max(widths)
    mass = sum(count << (width - b) for b, count in widths.items())
    return {"weight_cap": max_weight, "nodes": sum(r["nodes"] for r in rows),
            "clock_bound": max(r["maximum_clock"] for r in rows),
            "domain_width": width, "odd_density_numerator": 2 * mass,
            "density_denominator_exponent": width,
            "sha256": all_digest.hexdigest(), "levels": rows}


def compile_descent(n: int):
    """Return (clock, endpoint) on the certified cylinder union, else None.

    Odd inputs use at most eight low-set-bit prefixes; high bits are not
    enumerated. This is a total guarded selector, not a universal one.
    """
    require(type(n) is int and n >= 1, "positive integer required")
    if n == 1:
        return None
    if n % 2 == 0:
        return 1, n // 2
    prefix = 1
    for depth in range(1, 9):
        k, odds, endpoint = first_descent(prefix)
        require(k <= 552, "prefix outside verified clock bound")
        width = max(prefix.bit_length(), k)
        if n & ((1 << width) - 1) == prefix:
            answer = 3 ** odds * ((n - prefix) >> k) + endpoint
            require(answer < n, "failed original-source comparison")
            return k, answer
        if depth == 8:
            return None
        remainder = n - prefix
        bit = remainder & -remainder
        require(bit.bit_length() - 1 < k, "invalid tree continuation")
        prefix += bit
    raise RuntimeError("unreachable")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("task", choices=("core", "sparse"))
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(args.workers >= 1, "workers must be positive")
    if args.task == "core":
        if args.workers == 1:
            rows = [core_row(s) for s in range(2, 11)]
        else:
            with ProcessPoolExecutor(max_workers=args.workers) as pool:
                rows = list(pool.map(core_row, range(2, 11)))
        output = {"schema": 1, "modular": modular_bounds(), "caps": rows}
    else:
        output = {"schema": 1, "sparse": sparse_rows()}
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"task": args.task, "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
