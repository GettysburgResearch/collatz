"""Exact compatibility controls for TAIL_CAPTURE_BRIDGE.md; not global coverage."""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def shortcut(n: int) -> int:
    require(n > 0, "nonpositive shortcut input")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def actual_path(n: int, clocks: int) -> list[int]:
    values = [n]
    for _ in range(clocks):
        values.append(shortcut(values[-1]))
    return values


def complete_states(root: int, gaps: list[int]) -> list[int]:
    states = [root]
    for gap in gaps:
        require(root > 0 and root % 2 == 1 and gap > 0, "bad odd gap")
        numerator = 3 * root + 1
        require(numerator % (2**gap) == 0, "nonintegral odd edge")
        root = numerator // (2**gap)
        require(root % 2 == 1, "gap is not the exact valuation")
        states.append(root)
    require(root == 1, "certificate does not end at one")
    return states


def grade(e: int, gaps: list[int]) -> Counter[int]:
    return Counter(([2 * e + 1] if e else []) + [2 * a for a in gaps])


def changed_grade(old: Counter[int], new: Counter[int]) -> int:
    changed = [g for g in old.keys() | new.keys() if old[g] != new[g]]
    require(bool(changed), "grades coincide")
    highest = max(changed)
    require(new[highest] < old[highest], "grade did not decrease")
    return highest


small_tail = [1, 1, 2, 3, 4]
complete_states(37, [4] + small_tail)
complete_states(9, [2] + small_tail)
small_target = actual_path(75, 4)
require(small_target[-1] == 128 and 113 < 128 <= 145, "small capture")
require(changed_grade(grade(0, [4] + small_tail),
                      grade(3, [2] + small_tail)) == 8, "small grade")

tail = [1, 2, 2, 1, 4, 1, 1, 1, 4, 4, 2, 1, 1, 1,
        1, 1, 1, 2, 4, 3, 3, 3, 1, 2, 3, 4]
old_word, new_word = [4] + tail, [2] * 4 + tail
old_states = complete_states(31973, old_word)
new_states = complete_states(18945, new_word)
require(old_states[1:] == new_states[4:], "literal tails differ")
require(changed_grade(grade(2, old_word), grade(3, new_word)) == 8,
        "full certificate grade")
old_source, new_source = 4 * 31973, 8 * 18945
require(new_source > old_source, "replacement height")
max_removed = 2
literal_sources = [2 * old_states[0]]
for gap, endpoint in zip(old_word, old_states[1:]):
    max_removed = max(max_removed, gap)
    literal_sources.append(2 ** (max_removed - 1) * endpoint)
envelope = max(literal_sources)
require(envelope == 71944, "literal-cut maximum")
target = 255783
require(2 * envelope + 1 < target <= 2 * old_source + 1
        < 2 * new_source + 1, "whole-interval fixture")
require((3 * target + 1) % 4 == 2, "first target gap is not one")
lower_target = actual_path(31967, 4)
require(31967 < 31973 and lower_target[-1] == 161837, "lower target path")
require(2 * envelope + 1 < lower_target[-1] <= 2 * new_source + 1,
        "lower target capture")

family_controls = []
for e, depths in [(2, [4, 5, 16, 128]), (3, [6, 7, 16, 128])]:
    for h in depths:
        for v in [2, 74]:
            q = 1 + 3**h * v
            b = 1 + 4**h * v
            states = [1 + 4**j * 3**(h-j) * v for j in range(h+1)]
            require(all(x > 0 and x % 2 == 1 for x in states), "odd chain")
            require(all(3 * states[j+1] + 1 == 4 * states[j]
                        for j in range(h)), "chain edge")
            r = (16 * q - 1) // 3
            require(3 * r + 1 == 16 * q, "gap-four source")
            require(8 * b > 2**e * r, "family interval inclusion")
            require(changed_grade(grade(e, [4]), grade(3, [2] * h)) == 8,
                    "family grade")
            family_controls.append({"e": e, "h": h, "v": v,
                                    "source_gain": 8 * b - 2**e * r})

print(json.dumps({
    "schema": "collatz-tail-capture-controls/v1",
    "scope": "Exact finite compatibility controls; arbitrary families have written proofs.",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "success": True,
    "small_target_path": small_target,
    "old_odd_states": old_states,
    "new_odd_states": new_states,
    "old_source": old_source,
    "new_source": new_source,
    "old_clock": 2 + sum(old_word),
    "new_clock": 3 + sum(new_word),
    "highest_changed_grade": 8,
    "literal_cut_maximum": envelope,
    "literal_cut_ceiling": 2 * envelope + 1,
    "replacement_ceiling": 2 * new_source + 1,
    "whole_interval_target": target,
    "lower_target_path": lower_target,
    "family_controls": family_controls
}, indent=2) + "\n", end="")
