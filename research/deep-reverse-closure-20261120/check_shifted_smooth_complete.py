#!/usr/bin/env python3
"""Exact finite complement of CS1; it does not prove the external theorem."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def strip(n: int, p: int) -> tuple[int, int]:
    require(isinstance(n, int) and n > 0, "positive integer required")
    require(p in (2, 3), "only declared primes permitted")
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent, n


def odd_step(n: int) -> tuple[int, int]:
    require(isinstance(n, int) and n > 0 and n % 2 == 1,
            "source must be a positive odd integer")
    exponent, endpoint = strip(3 * n + 1, 2)
    return exponent, endpoint


def shifted_core(n: int) -> tuple[int, int, int]:
    require(n > 0 and n % 2 == 1, "source must be positive odd")
    s, rest = strip(n + 1, 2)
    t, q = strip(rest, 3)
    return s, t, q


def boundary_row(k: int) -> dict[str, int]:
    require(isinstance(k, int) and k >= 1, "positive boundary index required")
    b, u = strip(3 ** k - 1, 2)
    source = 2 * 3 ** (k - 1) - 1
    a, actual = odd_step(source)
    require(actual == u and a == b + 1, "boundary normalization failed")
    predicted = 1 if k % 2 else 2 + strip(k, 2)[0]
    require(b == predicted, "boundary valuation formula failed")
    require(2 ** b <= 4 * k, "linear valuation size bound failed")
    s, t, q = shifted_core(u)
    require(3 ** k + 2 ** b - 1 == 2 ** (b + s) * 3 ** t * q,
            "exact boundary equation failed")
    return {"k": k, "b": b, "s": s, "t": t, "q": q,
            "source": source, "endpoint": u}


def verify_preserving_indices(indices: list[int]) -> None:
    actual = [k for k in range(1, 128) if boundary_row(k)["q"] == 1]
    require(indices == actual, "incorrect complete small complement")


def run() -> dict[str, object]:
    rows = [boundary_row(k) for k in range(1, 128)]
    good = [r for r in rows if r["q"] == 1]
    verify_preserving_indices([1, 2, 4])
    require(3 ** 128 > 4800 * 2 ** 14 * 128 ** 15,
            "unbounded cutoff base comparison failed")
    require(129 ** 15 < 3 * 128 ** 15,
            "unbounded cutoff induction comparison failed")
    expected_basin = {1, 3, 5, 15, 23, 35, 53}
    actual_basin: set[int] = set()
    path_count = 0
    edge_count = 0
    # Complete finite cross-checks of all exponent pairs for k < 128.
    # This covers their actual, potentially very large, ordinary values.
    for k in range(1, 128):
        for s in range(1, k + 1):
            t = k - s
            n = 2 ** s * 3 ** t - 1
            start = n
            for j in range(s - 1):
                a, endpoint = odd_step(n)
                require(a == 1, "wrong exponent-one run")
                require(endpoint == 2 ** (s-j-1) * 3 ** (t+j+1)-1,
                        "wrong shifted run formula")
                n = endpoint
                edge_count += 1
            require(n == 2 * 3 ** (k - 1) - 1, "wrong boundary")
            _, endpoint = odd_step(n)
            edge_count += 1
            if k not in (1, 2, 4):
                require(shifted_core(endpoint)[2] > 1,
                        "declared first exit still smooth")
            else:
                actual_basin.add(start)
                value = start
                seen = set()
                while value != 1:
                    require(value not in seen, "unexpected cycle in finite basin")
                    seen.add(value)
                    require(shifted_core(value)[2] == 1,
                            "finite basin leaves class")
                    _, value = odd_step(value)
                    edge_count += 1
                require(len(seen) <= 5, "finite basin hitting bound failed")
            path_count += 1
    require(actual_basin == expected_basin, "wrong finite basin")
    simple_prefixes = 0
    no_known_source_prefixes = 0
    for source in range(1, 1024, 2):
        values = [source]
        seen = {source}
        d = 0
        c = int(shifted_core(source)[2] > 1)
        uses_known_source = False
        for _ in range(128):
            a, endpoint = odd_step(values[-1])
            if endpoint in seen:
                break
            uses_known_source = uses_known_source or values[-1] in (1, 5, 53)
            d += int(a >= 2)
            c += int(shifted_core(endpoint)[2] > 1)
            require(d <= 2*c + 2, "effective simple-prefix count failed")
            simple_prefixes += 1
            if not uses_known_source:
                require(d <= 2*c, "known-source-free prefix count failed")
                no_known_source_prefixes += 1
            values.append(endpoint)
            seen.add(endpoint)
    negative_controls = 0
    for invalid in ([1, 2, 4, 16], [1, 2], [1, 2, 4, 128]):
        try:
            verify_preserving_indices(invalid)
        except ValueError:
            negative_controls += 1
        else:
            raise ValueError("corrupt small complement was accepted")
    for invalid in (0, -1, 2):
        try:
            odd_step(invalid)
        except ValueError:
            negative_controls += 1
        else:
            raise ValueError("invalid ordinary source was accepted")
    for k in (128, 256, 257, 512, 1024, 4096):
        boundary_row(k)
    encoded = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return {
        "status": "PASS",
        "scope": "finite complement, literal run identities and two exact induction comparisons; external logarithm theorem not re-proved",
        "small_boundary_indices": 127,
        "preserving_rows": good,
        "small_rows_sha256": hashlib.sha256(encoded).hexdigest(),
        "run_sources": path_count,
        "literal_odd_edges": edge_count,
        "known_basin": sorted(actual_basin),
        "simple_prefixes": simple_prefixes,
        "known_source_free_prefixes": no_known_source_prefixes,
        "extra_large_valuation_controls": 6,
        "negative_controls": negative_controls,
        "cutoff_base_margin": str(3 ** 128 - 4800 * 2 ** 14 * 128 ** 15),
        "cutoff_ratio_margin": str(3 * 128 ** 15 - 129 ** 15),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.write_text(result, encoding="utf-8")
    else:
        print(result, end="")
