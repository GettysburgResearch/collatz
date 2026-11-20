#!/usr/bin/env python3
"""Independent ordinary-integer replays from a physical credit potential.

This reads the full little-endian int32 table checked by verify_physical.cpp.
It follows E/O decisions directly, then runs the ordinary shortcut map on
three concrete prefixes. The all-lift inequalities, not these examples,
supply the universal certificate.
"""
from __future__ import annotations

import argparse
from array import array
import hashlib
import json
from pathlib import Path
import sys


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


class Potential:
    def __init__(self, path: Path, depth: int, p: int, q: int):
        self.modulus, self.p, self.q = 3**depth, p, q
        self.count = 2 * self.modulus // 3
        need(path.stat().st_size == 4 * self.count, "wrong table length")
        self.values = array("i")
        need(self.values.itemsize == 4, "int32 array required")
        with path.open("rb") as stream:
            self.values.fromfile(stream, self.count)
        if sys.byteorder != "little":
            self.values.byteswap()
        need(min(self.values) >= 0, "negative credit")
        self.maximum = max(self.values)

    def at(self, unit: int) -> int:
        residue = unit % self.modulus
        need(residue % 3 != 0, "nonunit lookup")
        return self.values[2 * (residue // 3) + residue % 3 - 1]

    def inverse_gap(self, target: int) -> tuple[int, int]:
        before = target
        original_credit = self.at(target)
        even_count = 0
        while True:
            residue = target % self.modulus
            credit = self.at(target)
            if residue % 9 in (2, 8):
                worst = max(self.at((2 * (residue + j * self.modulus) - 1) // 3)
                            for j in range(3))
                if credit >= self.q - self.p + worst:
                    source = (2 * target - 1) // 3
                    exponent = even_count + 1
                    need(3 * source + 1 == (1 << exponent) * before,
                         "collapsed ordinary inverse identity failed")
                    need(source > 0 and source % 2 == 1 and source % 3,
                         "inverse gap did not produce an odd positive unit")
                    need(self.q * exponent + self.at(source) <= self.p + original_credit,
                         "collapsed credit failed on actual integer")
                    return source, exponent
            need(credit >= self.q + self.at(2 * target), "no certified physical action")
            target *= 2
            even_count += 1
            need(even_count <= original_credit // self.q, "even run exhausted its credit")

    def compile(self, depth: int, tail: int) -> tuple[int, int]:
        need(depth >= 1 and 0 < tail < 3**depth and tail % 3 != 0,
             "invalid ternary suffix")
        initial_credit = self.at(tail)
        source, total = tail, 0
        for _ in range(depth - 1):
            source, exponent = self.inverse_gap(source)
            total += exponent
        terminal = 1 if source % 3 == 2 else 2
        need(self.q * terminal - self.at(source) <= self.q,
             "terminal refund failed on actual integer")
        source = ((1 << terminal) * source - 1) // 3
        total += terminal
        need(0 < source < 1 << total, "compiled binary suffix out of range")
        need(self.q * total <= self.p * depth + initial_credit + self.q - self.p,
             "source-sensitive compiler bound failed")
        return source, total


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("potential", type=Path)
    parser.add_argument("depth", type=int)
    parser.add_argument("p", type=int)
    parser.add_argument("q", type=int)
    args = parser.parse_args()
    potential = Potential(args.potential, args.depth, args.p, args.q)
    cases = [(d, c) for d in range(1, 7) for c in range(1, 3**d) if c % 3]
    cases += [(d, c) for d in (40, 100, 1000)
              for c in (1, 2, 3**d - 1, 3**d - 2)]
    replays = 0
    for d, c in cases:
        suffix, clock = potential.compile(d, c)
        for prefix in (0, 1, 37):
            state = (prefix << clock) + suffix
            odd_count = 0
            for _ in range(clock):
                odd_count += state % 2
                state = (3 * state + 1) // 2 if state % 2 else state // 2
            need(state == 3**d * prefix + c, "ordinary forward endpoint mismatch")
            need(odd_count == d, "ordinary forward odd-count mismatch")
            replays += 1
    digest = hashlib.sha256()
    with args.potential.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    print(json.dumps({
        "status": "PASS",
        "table_sha256": digest.hexdigest(),
        "certificate_depth": args.depth,
        "p": args.p,
        "q": args.q,
        "max_credit": potential.maximum,
        "global_additive_numerator": potential.maximum + args.q - args.p,
        "distinct_suffixes": len(cases),
        "ordinary_forward_replays": replays,
        "prefixes": [0, 1, 37],
        "largest_ternary_depth": 1000,
        "scope": "Bounded ordinary replays; universal scope comes from all-lift inequalities.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
