#!/usr/bin/env python3
"""Exact global-rule checker and ordinary mixed-base normalization experiment.

This does not search residue cells.  Rule inequalities are checked coefficient
by coefficient, so they cover arbitrary nonnegative interpretation inputs.
The accompanying Lean module proves arbitrary-word termination and ordinary
transport.  Concrete traces below expose a failed candidate closing step.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


# Composition is left to right as functions: the rightmost symbol acts first.
# Homogeneous third coordinate records the affine constant.
MATRICES = {
    "f": ((1, 1, 0), (1, 0, 0), (0, 0, 1)),
    "t": ((1, 3, 1), (3, 4, 1), (0, 0, 1)),
    "0": ((7, 2, 2), (2, 5, 1), (0, 0, 1)),
    "1": ((2, 1, 1), (1, 1, 0), (0, 0, 1)),
    "2": ((2, 2, 0), (2, 4, 2), (0, 0, 1)),
    "L": ((1, 5, 0), (0, 0, 0), (0, 0, 1)),
    "R": ((1, 0, 1), (1, 0, 1), (0, 0, 1)),
}
RULES = (
    ("fR", "R"), ("tR", "2R"),
    ("f0", "0f"), ("f2", "1f"), ("t0", "1t"),
    ("t1", "2f"), ("t2", "2t"),
    ("L0", "Lt"), ("L1", "Lff"), ("L2", "Lft"),
)
NORMAL_PATTERN = re.compile(r"L(?:[ft]*f1[012]*)+R\Z")
IDENTITY = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def multiply(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def interpretation(word):
    result = IDENTITY
    for digit in word:
        result = multiply(result, MATRICES[digit])
    return result


def rank(word):
    return interpretation(word)[0][2]


def value(word):
    require(word.startswith("L") and word.endswith("R"), "noncanonical word")
    n = 1
    for digit in word[1:-1]:
        if digit in "ft":
            n = 2*n + (digit == "t")
        else:
            require(digit in "012", "invalid digit")
            n = 3*n + int(digit)
    return n


def shortcut(n):
    return n//2 if n % 2 == 0 else (3*n+1)//2


def rule_certificate():
    result = []
    for left, right in RULES:
        a, b = interpretation(left), interpretation(right)
        diff = tuple(tuple(a[i][j]-b[i][j] for j in range(3)) for i in range(2))
        require(all(x >= 0 for row in diff for x in row), (left, right, diff))
        require(diff[0][2] > 0, (left, right, "missing strict first constant"))
        result.append({"left": left, "right": right, "difference": diff})
    # Every left context preserves a strict first-coordinate drop.
    require(all(m[0][0] >= 1 for m in MATRICES.values()), "context monotonicity")
    return result


def redexes(word):
    return [(i, left, right) for left, right in RULES
            for i in range(len(word)-len(left)+1) if word.startswith(left, i)]


def normal_form(word, keep_trace=True):
    start = value(word)
    old_rank = rank(word)
    clock = 0
    trace = [{"word": word, "value": start, "rank": old_rank, "clock": 0}]
    while choices := redexes(word):
        i, left, right = min(choices)
        child = word[:i] + right + word[i+len(left):]
        child_rank = rank(child)
        require(child_rank < old_rank, "rank did not strictly decrease")
        old_value, new_value = value(word), value(child)
        if left in ("fR", "tR"):
            require(new_value == shortcut(old_value), "invalid ordinary dynamic step")
            clock += 1
        else:
            require(new_value == old_value, "auxiliary step changed the value")
        word, old_rank = child, child_rank
        if keep_trace:
            trace.append({"word": word, "value": new_value, "rank": old_rank,
                          "clock": clock, "rule": f"{left}->{right}"})
    require(word == "LR" or NORMAL_PATTERN.fullmatch(word), "grammar classification failed")
    return {"word": word, "value": value(word), "rank": rank(word),
            "ordinary_clock": clock, "trace": trace if keep_trace else []}


def blocked_return(word):
    require(not redexes(word) and word != "LR", "expected nonterminal normal form")
    i = word.rfind("f1")
    require(i >= 0 and all(d in "012" for d in word[i+2:-1]), "missing final obstruction")
    restored = word[:i] + "0t" + word[i+2:]
    require(value(restored) == value(word), "missing rule was not value preserving")
    return {"start_word": word, "start_value": value(word), "start_rank": rank(word),
            "restored_word": restored, "restored_rank": rank(restored),
            "end": normal_form(restored)}


def erased_partner(word):
    i = word.rfind("f1")
    require(i >= 0, "no f1 to erase")
    child = word[:i+1] + word[i+2:]
    require(0 < value(child) < value(word), "candidate did not shrink ordinary value")
    require(rank(child) < rank(word), "candidate did not shrink common rank")
    return {"word": child, "value": value(child), "rank": rank(child)}


def exact_report():
    rules = rule_certificate()
    examples = [blocked_return(w) for w in ("Lf1R", "Lff1R", "Ltf1R", "Lf11R", "Lf12R")]
    first = examples[0]
    require((first["end"]["word"], first["end"]["value"], first["end"]["rank"],
             first["end"]["ordinary_clock"]) == ("Lff1R", 13, 40, 4),
            "the 7 to 13 first obstruction changed")
    for item in examples:
        item["erased_partner"] = erased_partner(item["start_word"])
    return {
        "schema": "collatz-mixed-normal-form/v1",
        "scope": "global affine rule certificates and exact ordinary traces; no universal merger cover",
        "rules": rules,
        "normal_form_grammar": "LR or L([ft]*f1[012]*)+R",
        "examples": examples,
        "first_unsupported_step": "every nonterminal normal form has a blocked-erasure partner in its ordinary component",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = exact_report()
    content = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(content)
    print(json.dumps({"global_rule_checks": len(report["rules"]),
                      "exact_normal_form_returns": len(report["examples"]),
                      "first_obstruction": {"source": 7, "endpoint": 13,
                                            "ordinary_clock": 4, "ranks": [26, 40]},
                      "global_cover": "OPEN"}, sort_keys=True))


if __name__ == "__main__":
    main()
