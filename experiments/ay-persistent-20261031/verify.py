#!/usr/bin/env python3
"""Standalone reconstruction. Imports neither run.py nor any repository module."""
from __future__ import annotations
import argparse
from collections import Counter, deque
import hashlib
import json
from pathlib import Path


def check(condition: bool, message: str = "certificate rejected") -> None:
    if not condition:
        raise ValueError(message)


def same(actual, claimed) -> None:
    check(type(actual) is type(claimed), "type mismatch")
    if isinstance(actual, dict):
        check(actual.keys() == claimed.keys(), "key mismatch")
        for key in actual:
            same(actual[key], claimed[key])
    elif isinstance(actual, list):
        check(len(actual) == len(claimed), "length mismatch")
        for a, b in zip(actual, claimed):
            same(a, b)
    else:
        check(actual == claimed, f"value mismatch: {actual!r} != {claimed!r}")


def unique_object(pairs):
    obj = {}
    for key, value in pairs:
        check(key not in obj, "duplicate JSON key")
        obj[key] = value
    return obj


def load(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=unique_object)


def odd_image(n: int) -> int:
    value = n + n + n + 1
    while value % 2 == 0:
        value //= 2
    return value


def sha_values(values) -> str:
    h = hashlib.sha256()
    for n in sorted(values):
        h.update((str(n) + "\n").encode("ascii"))
    return h.hexdigest()


def reconstruct_modular() -> dict:
    modulus = 1 << 20
    limits = {}
    # Directly examine EVERY odd residue, rather than trusting a cycle census.
    for cap in range(2, 11):
        maximum = 0
        for residue in range(1, modulus, 2):
            value, delay = residue, 0
            while value.bit_count() < cap:
                value = (value * 3) & (modulus - 1)
                delay += 1
                check(delay <= (1 << (cap - 1)) - 1, "homogeneous guard")
            maximum = max(maximum, delay)
        limits[str(cap)] = maximum
    return {"modulus_bits": 20, "unit_count": modulus // 2, "bounds": limits}


def inverse_basin(cap: int, maximum_size: int) -> set[int]:
    pending = deque([1])
    found = {1}
    while pending:
        target = pending.popleft()
        if target % 3 == 0:
            continue
        exponent = 2 if target % 3 == 1 else 1
        numerator = (target << exponent) - 1
        while True:
            check(numerator % 3 == 0, "inverse integrality")
            source = numerator // 3
            if source.bit_count() > cap:
                break
            if source not in found:
                found.add(source)
                pending.append(source)
                check(len(found) <= maximum_size, "basin exceeds certificate")
            numerator = 4 * numerator + 3
    return found


def verify_core(claimed: dict) -> dict:
    cap = claimed["cap"]
    check(type(cap) is int and 2 <= cap <= 10)
    stack = [(1, 1)]
    histogram = Counter()
    digest = hashlib.sha256()
    successful = set()
    count = longest = largest = 0
    witness = 1
    while stack:
        source, ones = stack.pop()
        count += 1
        largest = max(largest, source)
        if ones < cap:
            multiplier, gap_height = source, 0
            while bin(multiplier).count("1") < cap:
                multiplier *= 3
                gap_height += 1
                check(gap_height <= (1 << (cap - 1)) - 1)
            for gap in range(2 * gap_height, 0, -1):
                stack.append((source * (2 ** gap) + 1, ones + 1))
        value, clock = source, 0
        while value != 1 and value.bit_count() <= cap:
            check(clock < claimed["maximum_delay"], "unfinished capped source")
            value = odd_image(value)
            clock += 1
        kind = "ONE" if value == 1 else "EXIT"
        if kind == "ONE":
            successful.add(source)
        if clock > longest:
            longest, witness = clock, source
        histogram[clock] += 1
        digest.update(f"{source},{kind},{clock}\n".encode("ascii"))
    backwards = inverse_basin(cap, len(successful))
    check(backwards == successful, "forward/inverse basin mismatch")
    result = {"cap": cap, "core_size": count, "one": len(successful),
              "exit": count - len(successful), "maximum_delay": longest,
              "witness": witness, "max_core_value": largest,
              "max_bitlength": largest.bit_length(),
              "core_sha256": digest.hexdigest(),
              "basin_sha256": sha_values(successful),
              "largest_basin_value": max(successful),
              "histogram": {str(k): histogram[k] for k in sorted(histogram)}}
    same(result, claimed)
    return {"cap": cap, "sources": count, "inverse_basin": len(backwards)}


def verify_sparse(claimed: dict) -> dict:
    check(claimed["weight_cap"] == 8)
    level = [1]
    rows = []
    complete = hashlib.sha256()
    literal_steps = 0
    intervals = []
    for weight in range(1, 9):
        next_level = []
        digest = hashlib.sha256()
        longest, witness = 0, 1
        for n in level:
            x, k, odds, coefficient, additive = n, 0, 0, 1, 0
            while True:
                parity = x % 2
                if parity:
                    x = (3 * x + 1) // 2
                    additive = 3 * additive + (1 << k)
                    coefficient *= 3
                    odds += 1
                else:
                    x //= 2
                k += 1
                if x < n or (n == 1 and k == 2):
                    break
                check(k < claimed["clock_bound"], "unfinished sparse node")
            check(coefficient == 3 ** odds and coefficient < 1 << k)
            check(coefficient * n + additive == (1 << k) * x, "affine identity")
            check(x < n or n == x == 1, "original-source order")
            literal_steps += k
            width = max(n.bit_length(), k)
            reversed_bits = int(format(n, f"0{width}b")[::-1], 2)
            intervals.append((width, reversed_bits))
            if k > longest:
                longest, witness = k, n
            row = f"{n},{k},{odds},{x}\n".encode("ascii")
            digest.update(row)
            complete.update(row)
            if weight < 8:
                # Enumerate possible positions of the NEXT set bit. Larger
                # positions are covered symbolically by the affine lift.
                position = len(bin(n)) - 2
                while position < k:
                    next_level.append(n | (1 << position))
                    position += 1
        largest = max(level)
        rows.append({"weight": weight, "nodes": len(level),
                     "maximum_clock": longest, "witness": witness,
                     "max_value": largest, "max_bits": largest.bit_length(),
                     "sha256": digest.hexdigest()})
        level = next_level
    domain_width = max(w for w, _ in intervals)
    normalized = sorted((r << (domain_width - w), (r + 1) << (domain_width - w))
                        for w, r in intervals)
    previous_end = -1
    mass = 0
    for left, right in normalized:
        check(previous_end <= left, "overlapping residue cylinders")
        mass += right - left
        previous_end = right
    result = {"weight_cap": 8, "nodes": sum(r["nodes"] for r in rows),
              "clock_bound": max(r["maximum_clock"] for r in rows),
              "domain_width": domain_width, "odd_density_numerator": 2 * mass,
              "density_denominator_exponent": domain_width,
              "sha256": complete.hexdigest(), "levels": rows}
    same(result, claimed)
    return {"nodes": result["nodes"], "literal_shortcut_steps": literal_steps}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("task", choices=("core", "sparse"))
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    data = load(args.path)
    check(type(data["schema"]) is int and data["schema"] == 1)
    if args.task == "core":
        same(reconstruct_modular(), data["modular"])
        check([r["cap"] for r in data["caps"]] == list(range(2, 11)))
        result = [verify_core(row) for row in data["caps"]]
    else:
        result = verify_sparse(data["sparse"])
    print(json.dumps({"verified": args.task, "inventory": result}, sort_keys=True))


if __name__ == "__main__":
    main()
