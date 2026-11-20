#!/usr/bin/env python3
"""Independent literal reconstruction; imports no author arithmetic."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def shortcut(value: int) -> int:
    need(type(value) is int and value > 0, "positive ordinary input")
    if value & 1:
        return (3 * value + 1) // 2
    return value // 2


def odd(value: int) -> tuple[int, int]:
    need(type(value) is int and value > 0 and value & 1 == 1,
         "positive ordinary odd input")
    result, exponent = 3 * value + 1, 0
    while result % 2 == 0:
        result //= 2
        exponent += 1
    return result, exponent


def run() -> dict:
    totals = {"parameters": 0, "known_edges": 0,
              "target_edges": 0, "odd_target_edges": 0,
              "classified_sources": 0}
    fixtures = []
    for m in list(range(1, 25)) + [53, 101]:
        power = 1 << (6 * m)
        need((power - 1) % 9 == 0, "index integrality")
        k = (power - 1) // 9
        n = 16 * k + 1
        known, current = [], n
        while current != 1:
            need(len(known) <= 6 * m + 4, "source did not hit")
            known.append(current)
            current = shortcut(current)
            totals["known_edges"] += 1
        known.extend([1, 2])
        need(len(known) - 2 == 6 * m + 4, "first shortcut depth")
        need(max(known) == (8 * power - 2) // 3, "complete maximum")
        mid, a = odd(n)
        end, b = odd(mid)
        need((a, b, end) == (2, 6 * m + 2, 1), "first odd depth two")

        partner = 2 * n - 1
        for _ in range(4):
            partner = shortcut(partner)
        need(partner == (1 << (6 * m + 1)) - 1, "Mersenne endpoint")

        current = 3 * n
        for j in range(6 * m + 5):
            need(current > max(known), "arbitrary known-clock separation")
            if j >= 4:
                ell = j - 4
                need(current + 1 == 3 ** (ell + 1) *
                     (1 << (6 * m - ell)), "closed target formula")
            current = shortcut(current)
            totals["target_edges"] += 1
        current = 3 * n
        for j in range(6 * m + 3):
            need(current > max(known), "odd-clock separation")
            current, _ = odd(current)
            totals["odd_target_edges"] += 1
        fixtures.append({"m": m, "source_bits": n.bit_length(),
                         "known_max": max(known)})
        totals["parameters"] += 1

    found = []
    for n in range(1, 100000, 16):
        mid, a = odd(n)
        end, b = odd(mid)
        totals["classified_sources"] += 1
        if n > 1 and mid > 1 and end == 1:
            need(a == 2 and b >= 8 and (b - 2) % 6 == 0,
                 "converse exponent")
            m = (b - 2) // 6
            need(9 * n + 7 == 16 * 64 ** m, "converse family")
            found.append(n)
    return {
        "status": "PASS",
        "scope": "independent bounded reconstruction, no author imports",
        "counts": totals,
        "classified_depth_two_sources": found,
        "fixture_sha256": hashlib.sha256(
            json.dumps(fixtures, sort_keys=True).encode()).hexdigest(),
        "limit": "No universal convergence of residual Mersenne targets."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
