#!/usr/bin/env python3
"""Replay two finite AYH witnesses; arithmetic is separate from SRS clocks."""
from __future__ import annotations

import json

RULES = [
    ("ad", "d"), ("bd", "gd"),
    ("ae", "ea"), ("af", "eb"), ("ag", "fa"),
    ("be", "fb"), ("bf", "ga"), ("bg", "gb"),
    ("ce", "cb"), ("cf", "caa"), ("cg", "cab"),
]

CERTIFICATES = [
    ("cbabbd", "ceababbd", [4,3,2,1,0,5,4,3,2,1,0,5,4,3,2,1,0,5,4,3,2,1,0,6,5,4,3,2,1]),
    ("cabaabd", "cabaaaabd", [5,4,3,2,1,0,5,4,3,2,1,0,5,4,3,2,1,0,6,5,4,3,2,1,0,6,5,4,3,2,1,0]),
]


def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)


def value(word: str) -> int:
    require(word.startswith("c") and word.endswith("d"), "not a proper word")
    number = 1
    for digit in word[1:-1]:
        if digit in "ab":
            number = 2 * number + "ab".index(digit)
        else:
            require(digit in "efg", "unrecognized digit")
            number = 3 * number + "efg".index(digit)
    return number


def is_subsequence(left: str, right: str) -> bool:
    index = 0
    for letter in right:
        if index < len(left) and left[index] == letter:
            index += 1
    return index == len(left)


def replay(source: str, target: str, positions: list[int]) -> dict:
    word = source
    counts = [0] * len(RULES)
    ordinary = [value(word)]
    rows = []
    for clock, position in enumerate(positions):
        matches = [(i, lhs, rhs) for i, (lhs, rhs) in enumerate(RULES)
                   if word[position:position + len(lhs)] == lhs]
        require(len(matches) == 1, f"ambiguous/invalid step {clock}")
        index, lhs, rhs = matches[0]
        child = word[:position] + rhs + word[position + len(lhs):]
        before, after = value(word), value(child)
        if index in (0, 1):
            require(after == (before // 2 if before % 2 == 0 else (3 * before + 1) // 2),
                    f"invalid physical edge at {clock}")
            ordinary.append(after)
        else:
            require(after == before, f"administrative rule changed value at {clock}")
        reverse_position = len(word) - position - len(lhs)
        reverse = word[::-1]
        require(reverse[reverse_position:reverse_position + len(lhs)] == lhs[::-1],
                "reversed redex mismatch")
        require(reverse[:reverse_position] + rhs[::-1] + reverse[reverse_position + len(lhs):]
                == child[::-1], "reversed rewrite mismatch")
        counts[index] += 1
        rows.append({"clock": clock, "position": position, "rule": index,
                     "before": word, "after": child})
        word = child
    require(word == target, "wrong endpoint")
    require(all(counts), "some rule was not used")
    require(is_subsequence(source, target), "embedding failed")
    return {"source": source, "target": target, "raw_rewrites": len(rows),
            "shortcut_path": ordinary, "rule_counts": counts, "trace": rows}


def main() -> None:
    reports = [replay(*certificate) for certificate in CERTIFICATES]
    require(reports[1]["source"] == "cab" + "aa" + "bd", "source sandwich changed")
    require(reports[1]["target"] == "cab" + "aaaa" + "bd", "target sandwich changed")
    print(json.dumps({"status": "passed", "scope": "two literal finite witnesses; not Collatz",
                      "certificates": reports}, indent=2))


if __name__ == "__main__":
    main()
