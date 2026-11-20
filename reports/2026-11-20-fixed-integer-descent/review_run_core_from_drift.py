#!/usr/bin/env python3
"""Separate breadth-first reconstruction of binary-run cores through cap four."""

from collections import deque
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def require(value, message):
    if not value:
        raise ValueError(message)


def count_runs(n):
    text = "0" + format(n, "b")
    return sum(a == "0" and b == "1" for a, b in zip(text, text[1:]))


def hit(upper, shift, cap):
    value = upper
    for j in range(1 << (2 * cap + 1)):
        if count_runs(value - shift) > cap:
            return j
        value *= 3
    raise ValueError("homogeneous bound failed")


def breadth_first_core(cap):
    queue = deque([(0, True, 0)])
    result = set()
    while queue:
        prefix, add_ones, completed_runs = queue.popleft()
        if add_ones:
            h = hit(prefix + 1, 1, cap)
            lengths = range(1, (3**h).bit_length())
        else:
            h = hit(prefix, 0, cap)
            lengths = range(1, 2 * h)
        for length in lengths:
            value = prefix * 2**length + (2**length - 1 if add_ones else 0)
            if add_ones:
                require(value not in result, "duplicate run parse")
                result.add(value)
                new_runs = completed_runs + 1
                if new_runs < cap:
                    queue.append((value, False, new_runs))
            else:
                queue.append((value, True, completed_runs))
    return result


def literal_odd_step(value):
    value = 3 * value + 1
    while value % 2 == 0:
        value //= 2
    return value


def main():
    implementation = ROOT / "experiments/fixed_integer_arithmetic.py"
    spec = importlib.util.spec_from_file_location("arithmetic_to_compare", implementation)
    original = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(original)
    frozen = json.loads((ROOT / "reports/2026-11-20-fixed-integer-descent/arithmetic-run-cores-cap6.json").read_text())
    rows = []
    for cap in range(1, 5):
        sources = breadth_first_core(cap)
        require(sources == set(original.core(cap)), "core generator sets disagree")
        successes = set()
        clocks = []
        steps = 0
        for source in sorted(sources):
            n = source
            seen = set()
            clock = 0
            while n != 1 and count_runs(n) <= cap:
                require(n not in seen, "capped nontrivial cycle")
                seen.add(n)
                n = literal_odd_step(n)
                clock += 1
            if n == 1:
                successes.add(source)
            clocks.append(clock)
            steps += clock
        expected = frozen["core_rows"][cap - 1]
        require(len(sources) == expected["core_sources"], "core count mismatch")
        require(len(successes) == expected["reaches_one_inside_cap"], "success count mismatch")
        require(max(clocks) == expected["max_core_odd_clock"], "clock mismatch")
        require(steps == expected["direct_replayed_odd_steps"], "edge count mismatch")
        rows.append({"cap": cap, "complete_sources": len(sources), "successes": len(successes), "maximum_odd_clock": max(clocks), "literal_odd_edges": steps})
    files = (
        "research/fixed-integer-descent/arithmetic.md",
        "research/fixed-integer-descent/modular_hitting.md",
        "experiments/fixed_integer_arithmetic.py",
    )
    print(json.dumps({
        "status": "PASS",
        "scope": "Independent breadth-first/string-run core reconstruction and literal replay through cap four only; not a second cap-six enumeration.",
        "file_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in files},
        "rows": rows,
    }, indent=2))


if __name__ == "__main__":
    main()
