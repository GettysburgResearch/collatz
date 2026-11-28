#!/usr/bin/env python3
"""Exact bounded replay of the sharp halving-label construction.

The infinite density and summability statements are proved in Markdown;
these finite integer checks do not replace those proofs.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def ceil_log2(n: int) -> int:
    require(n > 0, "The integer logarithm needs positive input")
    return (n - 1).bit_length()


def block_length(k: int) -> int:
    a = ceil_log2(k + 1)
    return a + ceil_log2(a + 1)


def label(n: int) -> int:
    require(n > 0, "Only positive integers have this label")
    bits = bin(n)[2:]
    parity, offset, k = 0, 0, 1
    while offset + block_length(k) <= len(bits):
        end = offset + block_length(k)
        parity ^= int(all(bit == "1" for bit in bits[offset:end]))
        offset, k = end, k + 1
    return parity


def main() -> None:
    maximum_shell = 17
    upper = 1 << (maximum_shell + 1)
    values = [0] + [label(n) for n in range(1, upper + 1)]
    for n in range(1, upper // 2 + 1):
        require(values[2 * n] == values[n], f"Halving at {n}")
    for n in range(1, upper // 2):
        d0 = int(values[2 * n] != values[2 * n + 1])
        d1 = int(values[2 * n + 1] != values[2 * n + 2])
        old = int(values[n] != values[n + 1])
        born = int(values[n] == values[n + 1] != values[2 * n + 1])
        require(d0 + d1 == old + 2 * born, f"Creation identity at {n}")

    ends, cumulative = {}, 0
    for k in range(1, 30):
        ell = block_length(k)
        cumulative += ell
        ends[cumulative] = (k, ell)
        require(cumulative <= 2 * (1 << ell), f"J_k p_k bound at {k}")
    rows = []
    previous = None
    for j in range(maximum_shell + 1):
        lower, stop = 1 << j, 1 << (j + 1)
        total = sum(values[n] != values[n + 1] for n in range(lower, stop))
        even = sum(values[n] != values[n + 1]
                   for n in range(lower + lower % 2, stop, 2))
        completed = ends.get(j + 1)
        if completed is None:
            require(even == 0, f"No block completion at shell {j}")
        elif completed[0] >= 2:
            require(even == (1 << (j - completed[1])),
                    f"Exact completion count at shell {j}")
        if previous is not None:
            require(total <= previous + 2 * even, f"Shell recurrence at {j}")
        require((j + 1) * total <= 16 * (1 << j), f"Finite rate bound at {j}")
        rows.append({
            "shell": j, "start": lower, "stop_exclusive": stop,
            "boundary_count": total, "even_boundary_count": even,
            "ones": sum(values[lower:stop]),
        })
        previous = total
    result = {
        "schema": "collatz-binary-boundary-finite/v1",
        "success": True,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "maximum_integer_evaluated": upper,
        "halving_checks": upper // 2,
        "creation_identity_checks": upper // 2 - 1,
        "rows": rows,
        "scope": "Exact finite counts and algebra only; natural density one-half and weighted-boundary divergence remain written infinite proofs. This label is not Collatz invariant.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
