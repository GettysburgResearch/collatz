#!/usr/bin/env python3
"""Independent exact-interface checker for the cartography pulse-chart synthesis.

This is a finite algebraic regression test, not an infinite-orbit proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 expects a positive integer")
    return (n & -n).bit_length() - 1


def accelerated(n: int) -> tuple[int, int]:
    y = 3 * n + 1
    a = v2(y)
    return y >> a, a


def replay_block(n: int, valuations: tuple[int, ...]) -> int:
    for expected in valuations:
        n, actual = accelerated(n)
        if actual != expected:
            raise AssertionError((expected, actual, n))
    return n


def pulse_chart(x: int) -> tuple[int, str, tuple[int, int]] | None:
    if x % 8 == 0:
        return 9 * (x // 8), "A", (1, 2)
    if x % 16 == 7:
        return (9 * x + 1) // 16, "B", (2, 2)
    return None


@dataclass(frozen=True)
class RenewalRow:
    x: int
    r: int
    x_next: int
    p: int
    p_next: int


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x-limit", type=int, default=200_000)
    parser.add_argument("--renewal-limit", type=int, default=2_000_000)
    args = parser.parse_args()

    branch_rows: list[tuple[int, str, int, int, int]] = []
    for x in range(1, args.x_limit + 1):
        step = pulse_chart(x)
        if step is None:
            continue
        x_next, symbol, valuations = step
        n = 42 * x - 5
        n_next = replay_block(n, valuations)
        expected = 42 * x_next - 5
        if n_next != expected:
            raise AssertionError((x, symbol, n_next, expected))
        epsilon = 0 if symbol == "A" else 1
        if (1 << (3 + epsilon)) * x_next != 9 * x + epsilon:
            raise AssertionError("variable-radix recurrence failed")
        branch_rows.append((x, symbol, x_next, n, n_next))

    renewal_rows: list[RenewalRow] = []
    # Start immediately after a B step: such outputs are 4 modulo 9.
    for x0 in range(1, args.renewal_limit + 1):
        if x0 % 9 != 4:
            continue
        x = x0
        r = 0
        while True:
            step = pulse_chart(x)
            if step is None:
                break
            x_next, symbol, _ = step
            if symbol == "A":
                r += 1
                x = x_next
                continue
            # B closes the renewal.
            p = 16 * x0
            p_next = 16 * x_next
            lhs = (1 << (3 * r + 4)) * p_next
            rhs = pow(3, 2 * r + 2) * p + (1 << (3 * r + 4))
            if lhs != rhs:
                raise AssertionError((x0, r, lhs, rhs))
            renewal_rows.append(RenewalRow(x0, r, x_next, p, p_next))
            break

    payload = {
        "branch_cases": len(branch_rows),
        "a_cases": sum(1 for row in branch_rows if row[1] == "A"),
        "b_cases": sum(1 for row in branch_rows if row[1] == "B"),
        "renewal_cases": len(renewal_rows),
        "max_renewal_r": max((row.r for row in renewal_rows), default=-1),
        "first_branch_rows": branch_rows[:12],
        "first_renewal_rows": [row.__dict__ for row in renewal_rows[:12]],
    }
    semantic = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["semantic_sha256"] = hashlib.sha256(semantic).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
