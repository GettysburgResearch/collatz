#!/usr/bin/env python3
"""Bounded exact checks of the six-run guarded eleven-rule AYH system.

The all-source clock comes from the separate finite-core theorem/certificate.
This program checks the rewriting interface and actual guarded schedules;
it does not establish unrestricted Collatz or an unrestricted string order.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
import itertools
import json
from pathlib import Path


RULES = (
    ("ad", "d"), ("bd", "gd"),
    ("ae", "ea"), ("af", "eb"), ("ag", "fa"),
    ("be", "fb"), ("bf", "ga"), ("bg", "gb"),
    ("ce", "cb"), ("cf", "caa"), ("cg", "cab"),
)
AFFINE = {"a": (2, 0), "b": (2, 1), "e": (3, 0),
          "f": (3, 1), "g": (3, 2)}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def decode(word):
    require(word.startswith("c") and word.endswith("d")
            and all(letter in AFFINE for letter in word[1:-1]), "improper word")
    value = 1
    administrative = 0
    for letter in word[1:-1]:
        multiplier, addend = AFFINE[letter]
        if multiplier == 3:
            administrative += value.bit_length()
        value = multiplier * value + addend
    return value, administrative


def runs(n):
    return bin(n)[2:].count("01") + int(n > 0)


def valuation(n):
    require(n > 0, "positive valuation input required")
    return (n & -n).bit_length() - 1


def oddpart(n):
    return n >> valuation(n)


def odd_step(n):
    require(n > 0 and n & 1, "positive odd input required")
    return oddpart(3 * n + 1)


@lru_cache(maxsize=None)
def clock(n):
    """First hit of 1 or >6 runs, including time zero; reject past 107."""
    require(n > 0 and n & 1, "clock input must be positive odd")
    for events in range(108):
        if n == 1 or runs(n) > 6:
            return events
        n = odd_step(n)
    raise ValueError("six-run first-hit clock exceeded certified 107")


def active(word):
    n, _ = decode(word)
    return n != 1 and runs(oddpart(n)) <= 6


def rank(word):
    n, administrative = decode(word)
    return clock(oddpart(n)), valuation(n), administrative


def applications(word):
    for position in range(len(word) - 1):
        for left, right in RULES:
            if word.startswith(left, position):
                yield left, position, word[:position] + right + word[position + len(left):]


def check_step(word, left, position, result):
    require(active(word), "source is outside the allowed guard")
    require(word.startswith(left, position), "source rule occurrence missing")
    before, h_before = decode(word)
    after, h_after = decode(result)
    if left == "ad":
        require(before % 2 == 0 and after == before // 2, "even dynamic value mismatch")
        require(h_after == h_before, "even dynamic changed H")
        require(clock(oddpart(after)) == clock(oddpart(before)), "halving changed q")
        require(valuation(after) == valuation(before) - 1, "halving valuation mismatch")
    elif left == "bd":
        require(before > 1 and before % 2 == 1 and after == (3 * before + 1) // 2,
                "odd dynamic value mismatch")
        require(h_after - h_before == before.bit_length() - 1,
                "odd dynamic H creation mismatch")
        require(clock(oddpart(after)) == clock(before) - 1, "odd event did not reduce q")
    else:
        require(left in {lhs for lhs, _ in RULES[2:]}, "unrecognized administrative rule")
        require(after == before and h_after == h_before - 1,
                "administrative value/H mismatch")
    require(rank(result) < rank(word), "ordinal-coordinate rank did not strictly decrease")


def binary_word(n):
    require(n >= 1, "positive word input required")
    return "c" + "".join("b" if bit == "1" else "a" for bit in bin(n)[3:]) + "d"


def budget(word):
    n, h = decode(word)
    return h + 108 * (n.bit_length() - 1) + 5885


def trace(word, schedule):
    initial = word
    allowance = budget(word)
    steps = 0
    odd_events = 0
    while active(word):
        choices = list(applications(word))
        require(choices, "active proper word has no rule")
        index = 0 if schedule == "left" else len(choices) - 1 if schedule == "right" else steps % len(choices)
        left, position, result = choices[index]
        check_step(word, left, position, result)
        odd_events += left == "bd"
        steps += 1
        require(steps <= allowance, "literal rewrite budget exceeded")
        word = result
    require(odd_events <= 107, "odd-event budget exceeded")
    terminal, _ = decode(word)
    require(terminal == 1 or runs(oddpart(terminal)) > 6, "unexpected terminal state")
    require(odd_events == clock(oddpart(decode(initial)[0])), "schedule changed first-hit odd clock")
    return steps, odd_events, terminal


def reject(operation):
    try:
        operation()
    except ValueError:
        return
    raise ValueError("negative control accepted")


def run():
    require(107 * 106 // 2 + 2 * 107 == 5885, "budget constant changed")
    require(clock(74475) == 107, "sharp certified odd-clock witness changed")
    counts = {left + "->" + right: 0 for left, right in RULES}
    right_of = dict(RULES)
    words = 0
    scheduled_words = []
    for length in range(7):
        for body in itertools.product(AFFINE, repeat=length):
            word = "c" + "".join(body) + "d"
            words += 1
            if length <= 3:
                scheduled_words.append(word)
            if not active(word):
                continue
            for left, position, result in applications(word):
                check_step(word, left, position, result)
                counts[left + "->" + right_of[left]] += 1
    require(all(counts.values()), "not every actual rule was checked")

    scheduled_words += [binary_word(n) for n in
                        (1, 2, 3, 7, 27, 31, 129, 879, 74475,
                         (1 << 16) - 1, (1 << 64) - 1)]
    schedule_edges = 0
    schedule_count = 0
    maximum_schedule_length = 0
    maximum_schedule_odd_events = 0
    for word in scheduled_words:
        terminals = []
        for schedule in ("left", "right", "rotating"):
            edges, odd_events, terminal = trace(word, schedule)
            schedule_count += 1
            schedule_edges += edges
            maximum_schedule_length = max(maximum_schedule_length, edges)
            maximum_schedule_odd_events = max(maximum_schedule_odd_events, odd_events)
            terminals.append(oddpart(terminal))
        require(len(set(terminals)) == 1, "scheduling changed odd terminal value")

    stress_edges = 0
    stress_rows = []
    for bits in (64, 257, 1024, 4096):
        n = (1 << bits) - 1
        initial_clock = clock(n)
        require(runs(n) == 1 and initial_clock <= 21, "long one-run outside-core bound failed")
        while n != 1 and runs(n) <= 6:
            word = binary_word(n)
            left, position, result = next(a for a in applications(word) if a[0] == "bd")
            check_step(word, left, position, result)
            n = oddpart(decode(result)[0])
            stress_edges += 1
        stress_rows.append({"initial_bits": bits, "odd_events": initial_clock,
                            "terminal_one_runs": runs(n)})

    # The guard is mathematically essential, even for the first dynamic step.
    outside = binary_word(5461)  # 1010101010101: seven one-runs.
    change = next(a for a in applications(outside) if a[0] == "bd")
    require(not active(outside) and rank(outside) == (0, 0, 0)
            and rank(change[2]) == (0, 13, 12), "unguarded-rank counterexample changed")
    reject(lambda: check_step(outside, *change))
    reject(lambda: check_step("cafd", "af", 1, "cead"))
    reject(lambda: decode("abgd"))
    reject(lambda: decode("cdbd"))
    # Merely counting ternary letters cannot replace the bitlength sum H.
    require(decode("caed")[1] - decode("cead")[1] == 1
            and sum(c in "efg" for c in "caed") == sum(c in "efg" for c in "cead"),
            "administrative-weight control changed")

    return {
        "schema": "collatz-six-run-guarded-ayh-v1",
        "scope": "all eleven rules on proper words, stopped at 1 or run-cap exit",
        "not_claimed": "unrestricted AYH termination or a context-compatible reduction order",
        "complete_word_corpus_max_body_length": 6,
        "complete_word_corpus_size": words,
        "checked_rule_occurrences": counts,
        "literal_guarded_schedules": schedule_count,
        "literal_rewrite_edges": schedule_edges,
        "largest_observed_schedule_length": maximum_schedule_length,
        "largest_observed_schedule_odd_events": maximum_schedule_odd_events,
        "large_one_run_stress": stress_rows,
        "large_source_dynamic_checks": stress_edges,
        "rejected_controls": 4,
        "guard_failure_control": {"source": 5461, "before": [0, 0, 0], "after": [0, 13, 12]},
        "bound": "H + 108*(bitlength(N)-1) + 5885",
        "evidence_limit": "finite interface replay; all-source scope requires the written core and rank proofs",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    report = run()
    if args.compare:
        require(report == json.loads(args.compare.read_text(encoding="utf-8")), "frozen replay differs")
    content = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as handle:
            handle.write(content)
    print(content, end="")


if __name__ == "__main__":
    main()
