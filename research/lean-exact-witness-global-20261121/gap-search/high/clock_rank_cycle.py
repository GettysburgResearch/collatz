#!/usr/bin/env python3
"""Exact fixed-target cycle excluding unrestricted source-clock overrides.

This is a finite obstruction witness for a proposed union of rewrite rules,
not an experiment claiming universal Collatz coverage. Checks remain active
under python -O. No external packages or stored Collatz results are used.
"""

import json


TARGET = 73
PROGRAMS = (
    (77, 0, (3, 3, 1, 2, 3, 4)),
    (116, 2, (3, 1, 2, 3, 4)),
    (176, 4, (1, 2, 3, 4)),
    (272, 4, (2, 3, 4)),
    (416, 5, (3, 4)),
    (640, 7, (4,)),
    (1024, 10, ()),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def grades(initial, word):
    return ([2 * initial + 1] if initial else []) + [2 * a for a in word]


def rank_drop(child, parent):
    differing = [
        a for a in set(child + parent) if child.count(a) != parent.count(a)
    ]
    if not differing:
        return False
    top = max(differing)
    return child.count(top) < parent.count(top)


def replay(source, initial, word):
    require(source > 0, "nonpositive source")
    require(source % (1 << initial) == 0, "initial division is not integral")
    odd = source // (1 << initial)
    require(odd % 2 == 1, "initial run does not end at an odd source")
    odd_path = [odd]
    for gap in word:
        require(gap > 0, "nonpositive gap")
        numerator = 3 * odd + 1
        require(numerator % (1 << gap) == 0, "nonintegral odd edge")
        odd = numerator // (1 << gap)
        require(odd % 2 == 1, "odd edge does not end at an odd integer")
        odd_path.append(odd)
    require(odd == 1, "complete word does not end at one")

    clock = initial + sum(word)
    trajectory = [source]
    n = source
    for _ in range(clock):
        require(n != 1, "clock is padded after reaching one")
        n = shortcut(n)
        trajectory.append(n)
    require(n == 1, "ordinary replay does not hit one at its stated clock")
    require(0 < TARGET <= 2 * source + 1, "fixed target left the interval")
    return {
        "source": source,
        "initial_even_run": initial,
        "odd_gaps": list(word),
        "odd_path": odd_path,
        "first_hitting_clock": clock,
        "grades": grades(initial, word),
        "ordinary_trajectory": trajectory,
    }


def main():
    rows = [replay(*program) for program in PROGRAMS]
    for parent, child in zip(rows, rows[1:]):
        require(child["source"] > parent["source"], "clock edge did not grow source")
        require(
            child["first_hitting_clock"] + 1 == parent["first_hitting_clock"],
            "clock edge did not decrease its exact clock by one",
        )

    reset_parent, reset_child = rows[-1], rows[0]
    require(
        rank_drop(reset_child["grades"], reset_parent["grades"]),
        "last edge does not strictly decrease the original multiset rank",
    )
    require(reset_child["source"] > TARGET, "reset violates the cofinal source bound")
    require(all(a <= 4 for a in reset_child["odd_gaps"]), "reset exceeds alphabet four")
    require(reset_parent["odd_gaps"] == [], "reset did not preserve the empty suffix")
    print(json.dumps({
        "fixed_target": TARGET,
        "programs": rows,
        "source_clock_edges": 6,
        "cofinal_rank_reset": {
            "parent_source": reset_parent["source"],
            "child_source": reset_child["source"],
            "highest_changed_grade": 21,
            "literal_preserved_suffix": [],
        },
        "conclusion": "The two unrestricted rule families contain a directed cycle.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
