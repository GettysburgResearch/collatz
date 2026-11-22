#!/usr/bin/env python3
"""Exact all-bound literal-tail selector and finite cap-three research replay.

The all-bound proof is QuantitativeInverseSelector.lean. The inverse table is
credited to PR177 a0a0d76f91b4e3846c1b1f0706cad56cb6098317. This executable
never follows an uncertified wanted target and never declares a bounded search
to be a proof of cap-three extinction.
"""

from __future__ import annotations

import argparse
from collections import deque
import hashlib
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def check_word(source: int, word: list[int], endpoint: int) -> None:
    require(source > 0 and source % 2 == 1, "source must be positive odd")
    n = source
    for a in word:
        require(a >= 1, "gaps must be positive")
        numerator = 3 * n + 1
        require(numerator % (1 << a) == 0, "nonintegral odd edge")
        q = numerator // (1 << a)
        require(q > 0 and q % 2 == 1, "gap must be the exact valuation")
        physical = n
        for _ in range(a):
            physical = shortcut(physical)
        require(physical == q, "ordinary clock disagrees with odd edge")
        n = q
    require(n == endpoint, "wrong literal-tail endpoint")


def selected_edge(q: int) -> tuple[int, int]:
    require(q > 0 and q % 2 == 1 and q % 3 != 0, "root must be an odd unit")
    v, r = divmod(q, 18)
    table = {
        1: (4, 96 * v + 5),
        5: (3, 48 * v + 13),
        7: (4, 96 * v + 37),
        11: (3, 48 * v + 29),
        13: (2, 24 * v + 17),
        17: (1, 12 * v + 11),
    }
    a, p = table[r]
    require(1 <= a <= 4 and p > 1 and p % 2 == 1 and p % 3 != 0,
            "selector positivity/unit invariant failed")
    require(3 * p + 1 == (1 << a) * q, "selector edge failed")
    check_word(p, [a], q)
    return a, p


def window_count(n: int) -> int:
    require(n >= 0, "negative interval")
    return (n + 5) // 6 + (n + 1) // 6


def select(q: int, tail: list[int], bound: int) -> dict:
    check_word(q, tail, 1)
    require(q % 3 != 0, "supplied root must be a ternary unit")
    require(bound >= q, "the stated height-window theorem requires N >= q")
    current = q
    inverse_labels: list[int] = []
    vertices = {q}
    budget = window_count(bound)
    while current <= bound:
        a, p = selected_edge(current)
        require(p not in vertices, "nonterminal selected chain repeated a vertex")
        vertices.add(p)
        inverse_labels.append(a)
        current = p
        require(len(inverse_labels) <= budget, "proved finite depth budget violated")
    word = inverse_labels[::-1]
    check_word(current, word, q)
    check_word(current, word + tail, 1)
    require(bound < current and 3 * current < 16 * bound, "height window failed")
    require(sum(word) <= 4 * budget, "prefix clock bound failed")
    return {
        "root": q,
        "bound": bound,
        "predecessor": current,
        "prefix": word,
        "unchanged_tail": tail,
        "inverse_depth": len(word),
        "depth_budget": budget,
        "ordinary_prefix_clock": sum(word),
        "ordinary_clock_budget": 4 * budget,
        "status": "exact supplied-certificate construction",
    }


def cap_three_tree(root: int, vertex_budget: int = 200000) -> dict:
    """Return closure evidence for a fixed root; an unfinished queue is OPEN."""
    require(root > 0 and root % 2 == 1, "root must be positive odd")
    depth = {root: 0}
    todo = deque([root])
    while todo and len(depth) < vertex_budget:
        q = todo.popleft()
        for a in (1, 2, 3):
            numerator = (1 << a) * q - 1
            if numerator % 3 != 0:
                continue
            p = numerator // 3
            if p <= 0 or p % 2 != 1:
                continue
            check_word(p, [a], q)
            if p not in depth:
                depth[p] = depth[q] + 1
                todo.append(p)
    closed = not todo
    acyclic_depth_consistent = closed
    if closed:
        # Separate full-closure pass: check every admissible predecessor,
        # including unit and nonunit leaves, against the resulting vertex set.
        for q in depth:
            for a in (1, 2, 3):
                numerator = (1 << a) * q - 1
                if numerator % 3 == 0 and numerator > 0:
                    p = numerator // 3
                    if p % 2 == 1:
                        require(p in depth, "finite tree omitted a legal predecessor")
                        if depth[p] != depth[q] + 1:
                            acyclic_depth_consistent = False
    encoded = json.dumps(sorted(depth), separators=(",", ":")).encode()
    return {
        "root": root,
        "vertices": len(depth),
        "max_depth": max(depth.values()),
        "maximum_bits": max(depth).bit_length(),
        "vertex_sha256": hashlib.sha256(encoded).hexdigest(),
        "closed": closed,
        "acyclic_depth_consistent": acyclic_depth_consistent,
        "status": "complete finite closure" if closed else "OPEN at execution budget",
    }


def symbolic_terminal_chain(h: int, u: int) -> dict:
    require(h >= 1 and u > 0 and u % 2 == 0 and u % 3 == 2,
            "invalid symbolic terminal-chain parameters")
    chain = [1 + 4**j * 3**(h - j) * u for j in range(h + 1)]
    for j, q in enumerate(chain):
        legal = []
        for a in (1, 2, 3):
            numerator = (1 << a) * q - 1
            if numerator % 3 == 0:
                p = numerator // 3
                check_word(p, [a], q)
                legal.append((a, p))
        expected = [(2, chain[j + 1])] if j < h else []
        require(legal == expected, "symbolic full-tree classification failed")
    require(chain[-1] % 3 == 0, "symbolic terminal leaf is not a multiple of three")
    return {"h": h, "u": u, "root": chain[0], "maximum": chain[-1],
            "vertices": h + 1, "inverse_depth": h,
            "status": "finite replay of written all-parameter chain theorem"}


def certified_symbolic_chain(h: int) -> dict:
    require(h >= 1, "certified family requires positive depth")
    k = 1 + 2 * 3**h
    q = (4**k - 1) // 3
    tail = [2 * k]
    check_word(q, tail, 1)
    require((q - 1) % 3**h == 0, "certified root lacks asserted divisibility")
    u = (q - 1) // 3**h
    result = symbolic_terminal_chain(h, u)
    require(result["root"] == q, "symbolic root and certified root differ")
    result["certified_tail"] = tail
    result["status"] = "finite replay of certified all-depth finite cap-three family"
    return result


def replay() -> dict:
    fixtures = [(1, []), (5, [4]), (37, [4, 1, 1, 2, 3, 4]), (85, [8])]
    selected = [select(q, tail, n)
                for q, tail in fixtures for n in (max(q, 100), 10**6, 1 << 256)]
    for n in range(200):
        actual = sum(k % 2 == 1 and k % 3 != 0 for k in range(1, n + 1))
        require(window_count(n) == actual, "residue count implementation failed")
    trees = [cap_three_tree(q) for q in (5, 31, 37, 101)]
    return {
        "status": "finite execution of an all-bound proved selector; global closure OPEN",
        "selector_source": "PR177 a0a0d76f91b4e3846c1b1f0706cad56cb6098317",
        "selector_fixtures": selected,
        "cap_three_finite_closures": trees,
        "symbolic_chain_fixtures": [symbolic_terminal_chain(h, u)
                                    for h in (1, 2, 7, 64, 128) for u in (2, 8, 20)],
        "certified_chain_fixtures": [certified_symbolic_chain(h) for h in range(1, 6)],
        "scope": "No all-root cap-three extinction or universal low-interval claim.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--source", type=int)
    parser.add_argument("--tail", default="")
    parser.add_argument("--bound", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.replay:
        result = replay()
    else:
        require(args.source is not None and args.bound is not None,
                "supply --source and --bound, or use --replay")
        tail = [int(x) for x in args.tail.split(",") if x]
        result = select(args.source, tail, args.bound)
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
