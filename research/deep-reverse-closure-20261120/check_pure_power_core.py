#!/usr/bin/env python3
"""Finite exact replay of the pure-power first-descent identities."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def strip(n: int, p: int) -> tuple[int, int]:
    need(n > 0 and p >= 2, "invalid stripping input")
    a = 0
    while n % p == 0:
        a += 1
        n //= p
    return a, n


def core(n: int, pool: tuple[int, ...]) -> int:
    for p in pool:
        _, n = strip(n, p)
    return n


def order3(p: int) -> int:
    value = 1
    for r in range(1, p):
        value = 3 * value % p
        if value == 1:
            return r
    raise ValueError("declared prime has no checked order")


def family(e: int) -> tuple[int, int, int]:
    need(e > 0 and e % 4 == 0, "exponent must be positive and divisible by 4")
    n = 3 ** e
    a, u = strip(3*n+1, 2)
    need(a == 2 and u < n, "first ordinary odd step does not strictly descend")
    q = (3*n+5)//8
    need(8*q == 3*n+5, "nonintegral shifted core")
    need(core(u+1, (2,3)) == q, "wrong shifted core")
    return n, u, q


def run() -> dict[str, object]:
    import math
    target_cases = 0
    for r in range(33):
        e = 108*r+80
        need(e == 27*(4*r+3)-1, "not in the required progression")
        family(e)
        target_cases += 1
    pools = ((2,3), (2,3,5), (2,3,5,7,11), (2,3,5,7,11,13,17,19))
    pooled_cases = 0
    maximum_bits = 0
    records = []
    for pool in pools:
        L = math.lcm(*(order3(p) for p in pool if p > 3))
        records.append({"pool": list(pool), "exponent_index_modulus": L})
        for multiplier in (1,2,3):
            k = L*multiplier
            n, u, q = family(4*k)
            need(core(u, pool) == u, "ordinary endpoint retains a pool prime")
            need(core(u+1, pool) == q, "shifted core retains a pool prime")
            need(all(u % p == 1 and q % p == 1 for p in pool if p > 3),
                 "exact outside-pool congruence failed")
            maximum_bits = max(maximum_bits, n.bit_length())
            pooled_cases += 1
    controls = 0
    for e in (0,1,2,3,-4):
        try:
            family(e)
        except ValueError:
            controls += 1
        else:
            raise ValueError("invalid family exponent was accepted")
    n, u, q = family(80)
    need(core(u+1, (2,3)) != q+1, "corrupt core was accepted")
    controls += 1
    return {"status": "PASS", "scope": "finite exact local identities, not a fixed-source future bound",
            "required_progression_cases": target_cases, "finite_pool_cases": pooled_cases,
            "pools": records, "maximum_source_bits": maximum_bits,
            "negative_controls": controls}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
