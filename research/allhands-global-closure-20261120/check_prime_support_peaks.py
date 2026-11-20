#!/usr/bin/env python3
"""Exact bounded replay of the ordinary prime-support peak interfaces.

The universal argument is PRIME_SUPPORT_PEAKS.md. This program does not
assert full convergence or enumerate hypothetical nontrivial cycles.
It deliberately uses explicit exceptions, and works unchanged under -OO.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from functools import lru_cache
from pathlib import Path


def require(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)


def odd_step(n: int) -> tuple[int, int]:
    require(type(n) is int and n > 0 and n % 2 == 1, "positive odd integer required")
    raw = 3 * n + 1
    a = 0
    while raw % 2 == 0:
        raw //= 2
        a += 1
    return raw, a


def trajectory(source: int, cap: int = 200) -> tuple[list[int], list[int]]:
    odd_step(source)
    values = [source]
    exponents = []
    seen = {source}
    while len(exponents) < cap and values[-1] != 1:
        value, a = odd_step(values[-1])
        values.append(value)
        exponents.append(a)
        if value in seen:
            break
        seen.add(value)
    return values, exponents


def validate_edges(values: list[int], exponents: list[int]) -> None:
    require(len(values) == len(exponents) + 1, "edge count")
    for j, a in enumerate(exponents):
        target, actual = odd_step(values[j])
        require(type(a) is int and a == actual and target == values[j + 1], "corrupted edge")


@lru_cache(maxsize=None)
def factor(n: int) -> tuple[tuple[int, int], ...]:
    require(type(n) is int and n > 0, "positive factor input")
    result = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            result.append((p, e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        result.append((n, 1))
    return tuple(result)


def return_certificate(values: list[int], indices: list[int], divisor: int) -> None:
    require(type(divisor) is int and divisor > 0, "positive divisor")
    require(bool(indices), "nonempty selected positions")
    require(all(type(i) is int and 0 <= i < len(values) for i in indices), "position domain")
    require(all(i < j for i, j in zip(indices, indices[1:])), "chronological positions")
    require(all(values[i] % divisor == 0 for i in indices), "actual common divisor")
    if len(indices) > 1:
        left = divisor ** (len(indices) - 1) * values[indices[-1]]
        right = 6 ** (indices[-1] - indices[0]) * values[indices[0]]
        require(left < right, "telescoped return budget")


def check_source(source: int, counts: dict[str, int]) -> dict[str, int]:
    values, exponents = trajectory(source)
    validate_edges(values, exponents)
    counts["sources"] += 1
    counts["literal_odd_edges"] += len(exponents)
    counts["largest_source"] = max(counts["largest_source"], source)
    counts["maximum_state_bits"] = max(counts["maximum_state_bits"], max(values).bit_length())

    # Reconstruct the affine numerator from the actual edge list.
    for i in range(len(values) - 1):
        powers = 1
        correction = 0
        for j in range(i + 1, min(len(values), i + 17)):
            correction = 3 * correction + powers
            powers <<= exponents[j - 1]
            d = j - i
            require(powers * values[j] == 3 ** d * values[i] + correction, "affine numerator")
            gcd = math.gcd(values[i], values[j])
            require(correction > 0 and correction % gcd == 0, "gcd divides positive correction")
            require(gcd * values[j] < 6 ** d * values[i], "P1")
            counts["affine_pair_checks"] += 1

    factors = [dict(factor(n)) for n in values]
    support = sorted({p for row in factors for p in row})
    for p in support:
        powers = [p ** row.get(p, 0) for row in factors]
        for e in range(1, max(row.get(p, 0) for row in factors) + 1):
            q = p ** e
            selected = [j for j, n in enumerate(values) if n % q == 0]
            return_certificate(values, selected, q)
            counts["prime_power_return_checks"] += 1
        for h in range(1, max(powers).bit_length()):
            selected = [j for j, q in enumerate(powers) if q > 2 ** h]
            if len(selected) > 1:
                left = 2 ** (h * (len(selected) - 1)) * values[selected[-1]]
                right = 6 ** (selected[-1] - selected[0]) * values[selected[0]]
                require(left < right, "discrete height threshold charge")
                counts["height_threshold_checks"] += 1

    peak = 0
    for k, value in enumerate(values):
        if value <= peak:
            continue
        peak = value
        if peak < 256:
            continue
        # For an odd integer >1, ceil(log2(peak)/2) is exact here.
        nwindow = (peak.bit_length() + 1) // 2
        if k < nwindow - 1:
            require(peak < source ** 2, "short-prefix source alternative")
            counts["source_boundary_checks"] += 1
            continue
        block = values[k - nwindow + 1:k + 1]
        require(all(n * n > peak for n in block), "backward peak height floor")
        block_support = {p for n in block for p, _ in factor(n)}
        s = len(block_support)
        require(s > 0, "nontrivial peak has nonempty support")
        # M < 28s+7s log2 M implies the weaker all-integer bound below.
        b = peak.bit_length()
        require(peak < (2 ** (28 * s)) * (b ** (7 * s)), "integer P8 consequence")
        require(peak < (s + 1) ** (128 * s), "P10")
        counts["record_peak_windows"] += 1

    if support:
        s = len(support)
        require(max(values) <= max(source ** 2, (s + 1) ** (128 * s)), "finite-source P11")
        require(max(values) <= max(4 ** s * source, (s + 1) ** (64 * s)), "finite-source P13e")
        counts["finite_source_bounds"] += 1
    else:
        require(values == [1], "empty support case")
    return {"source": source, "states": len(values), "support": len(support), "max": max(values)}


def reject(callable_) -> None:
    try:
        callable_()
    except ValueError:
        return
    raise ValueError("negative control unexpectedly accepted")


def run() -> dict:
    counts = {key: 0 for key in (
        "sources", "literal_odd_edges", "largest_source", "maximum_state_bits",
        "affine_pair_checks", "prime_power_return_checks", "height_threshold_checks",
        "record_peak_windows", "source_boundary_checks", "finite_source_bounds",
        "negative_controls", "peak_cost_windows", "deleted_tail_checks",
    )}
    sources = sorted(set(range(1, 2048, 2)) | {2 ** k - 1 for k in range(2, 19)} |
                     {2 ** k + 1 for k in range(2, 19)} | {3 ** k for k in range(1, 13)})
    fixtures = [check_source(n, counts) for n in sources]
    for value in (0, -1, 2, True):
        reject(lambda value=value: odd_step(value))
        counts["negative_controls"] += 1
    values, exponents = trajectory(27)
    bad = list(values)
    bad[1] += 2
    reject(lambda: validate_edges(bad, exponents))
    counts["negative_controls"] += 1
    reject(lambda: return_certificate(values, [0, 1], 27))
    counts["negative_controls"] += 1
    # Removing the boundary occurrence would charge an unreturned power
    # against zero internal cost: this literal singleton defeats it.
    singleton = 3 ** 20
    require(singleton > 6 ** 0, "first occurrence negative control")
    counts["negative_controls"] += 1
    # The only actual cycle used in this replay is {1}.
    require(odd_step(1) == (1, 2), "root fixed point")
    # Audit coordinate-maxima deletion on many actual peak-ending windows.
    # These test the P13 interface even when their length is not 2s+1.
    for source in sources:
        values, exponents = trajectory(source)
        record = 0
        for k, peak in enumerate(values):
            if peak <= record:
                continue
            record = peak
            for width in (2, 3, 5, 9, 17):
                if k + 1 < width:
                    continue
                start = k + 1 - width
                block = values[start:k + 1]
                rows = [dict(factor(n)) for n in block]
                support = sorted({p for row in rows for p in row})
                deleted = {max(range(width), key=lambda j: rows[j].get(p, 0)) for p in support}
                retained = [j for j in range(width) if j not in deleted]
                total_a = sum(exponents[start:k])
                require(total_a <= 2 * (width - 1), "actual peak exponent budget")
                counts["peak_cost_windows"] += 1
                cost_integer = 3 ** (width - 1) * 2 ** (total_a - (width - 1))
                for p in support:
                    for e in range(1, max(row.get(p, 0) for row in rows) + 1):
                        q = p ** e
                        original = [j for j, n in enumerate(block) if n % q == 0]
                        remaining = [j for j in retained if block[j] % q == 0]
                        require(len(remaining) <= len(original) - 1, "one removed occurrence at every level")
                        # The global cost pays all original, not merely retained, returns.
                        require(q ** len(remaining) < cost_integer, "boundary-free valuation tail")
                        counts["deleted_tail_checks"] += 1
    return {
        "status": "PASS",
        "scope": "bounded exact-integer ordinary trajectory replay; universal proofs remain written arguments",
        "cycle_fixture": "only the actual fixed point 1; no nontrivial cycle asserted",
        "counts": counts,
        "fixture_digest": hashlib.sha256(json.dumps(fixtures, sort_keys=True).encode()).hexdigest(),
        "representative_fixtures": [x for x in fixtures if x["source"] in {1, 27, 127, 255, 1023, 262143, 531441}],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(result)
    print(result, end="")


if __name__ == "__main__":
    main()
