#!/usr/bin/env python3
"""Exact bounded checks for the positional ordinal rank and ag frontier.

This is not a Collatz proof. All mathematical all-word conclusions are proved
symbolically in research/ay-swarm-20261030/orders.md. Only Python integers and
the standard library are used. Checks remain active under python -O.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
import itertools
import json
from pathlib import Path
import random
import re


RULES = (
    ("ad", "d"), ("bd", "gd"), ("ae", "ea"), ("af", "eb"),
    ("ag", "fa"), ("be", "fb"), ("bf", "ga"), ("bg", "gb"),
    ("ce", "cb"), ("cf", "caa"), ("cg", "cab"),
)
W_RULES = tuple(rule for rule in RULES if rule[0] != "ag")
ALPHABET = "abcdefg"
PROPER = re.compile(r"c[abefg]*d\Z")
FRONTIER = re.compile(r"c(?:[ab]*ag[efg]*)+d\Z")
THREE_FRONTIER = re.compile(r"c(?:[ab]*ag+)+d\Z")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def rank(word: str) -> tuple[int, int, int, int, int]:
    e = word.count("e") + word.count("f")
    f = sum(word[i:i + 2] in ("cb", "cg") for i in range(len(word) - 1))
    a = word.count("a")
    q = sum(len(word) - i for i, char in enumerate(word) if char == "b")
    prefix_a = 0
    j = 0
    for char in word:
        if char == "a":
            prefix_a += 1
        elif char in "ef":
            j += prefix_a
    return e, f, a, q, j


def difference(before: str, after: str) -> tuple[int, ...]:
    return tuple(y - x for x, y in zip(rank(before), rank(after)))


def expected_delta(lhs: str, prefix: str, suffix: str) -> tuple[int, ...]:
    alpha = prefix.count("a")
    beta = prefix.count("b")
    epsilon = suffix.count("e") + suffix.count("f")
    h = len(suffix)
    delta = int(prefix.endswith("c"))
    table = {
        "ad": (0, 0, -1, -beta, -epsilon),
        "bd": (0, 0, 0, -h - 2, 0),
        "ae": (0, 0, 0, 0, -1),
        "af": (0, 0, -1, h + 1, -epsilon - 1),
        "ag": (1, 0, 0, 0, alpha),
        "be": (0, -delta, 0, -1, 0),
        "bf": (-1, 0, 1, -h - 2, epsilon - alpha),
        "bg": (0, 0, 0, -1, 0),
        "ce": (-1, 1, 0, h + 1, -alpha),
        "cf": (-1, 0, 2, beta, 2 * epsilon - alpha),
        "cg": (0, -1, 1, beta + h + 1, epsilon),
    }
    return table[lhs]


def all_words(alphabet: str, depth: int):
    for length in range(depth + 1):
        for chars in itertools.product(alphabet, repeat=length):
            yield "".join(chars)


def available(word: str, rules=RULES) -> list[tuple[int, str, str]]:
    hits = []
    for lhs, rhs in rules:
        start = 0
        while True:
            index = word.find(lhs, start)
            if index < 0:
                break
            hits.append((index, lhs, rhs))
            start = index + 1
    return hits


def rewrite(word: str, hit: tuple[int, str, str]) -> str:
    index, lhs, rhs = hit
    require(word[index:index + len(lhs)] == lhs, "invalid redex")
    return word[:index] + rhs + word[index + len(lhs):]


@dataclass
class Run:
    word: str
    counts: Counter
    maximum_length: int

    @property
    def steps(self) -> int:
        return sum(self.counts.values())


def normalize(word: str, *, full: bool = False, rightmost: bool = False,
              cap: int = 1_000_000) -> Run:
    rules = RULES if full else W_RULES
    counts: Counter = Counter()
    maximum_length = len(word)
    for _ in range(cap):
        hits = available(word, rules)
        if not hits:
            return Run(word, counts, maximum_length)
        hit = max(hits) if rightmost else min(hits)
        new_word = rewrite(word, hit)
        if hit[1] != "ag":
            require(rank(new_word) < rank(word), "W rank failed")
        else:
            require(rank(new_word)[0] == rank(word)[0] + 1, "ag fuel failed")
        counts[hit[1]] += 1
        word = new_word
        maximum_length = max(maximum_length, len(word))
    raise RuntimeError(f"normalization cap {cap} exceeded")


def encode(n: int) -> str:
    require(n >= 1, "positive input required")
    return "c" + bin(n)[3:].translate(str.maketrans("01", "ab")) + "d"


def value(word: str) -> int:
    require(PROPER.fullmatch(word) is not None, "proper word required")
    n = 1
    for char in word[1:-1]:
        radix, digit = {"a": (2, 0), "b": (2, 1), "e": (3, 0),
                        "f": (3, 1), "g": (3, 2)}[char]
        n = radix * n + digit
    return n


def is_frontier(word: str, *, three: bool = False) -> bool:
    pattern = THREE_FRONTIER if three else FRONTIER
    return word == "cd" or pattern.fullmatch(word) is not None


def budget(start: str, counts: Counter) -> dict[str, int]:
    e, f, a, q, j = rank(start)
    k = counts["ag"]
    d = e + k
    c = f + d
    u = a + 2 * d + c
    v = start.count("b") + u + d + c
    m = len(start) + d + c
    s = q + m * (u + d + c)
    r = j + m * (k + 2 * d + c)
    return {"D": d, "C": c, "U": u, "V": v, "M": m,
            "S": s, "R": r, "bound": u + v + d + c + s + r + k,
            "coarse": 54 * (len(start) + k) ** 2 + 18 * (len(start) + k)}


def check_budget(start: str, run: Run) -> None:
    n = run.counts
    b = budget(start, n)
    require(n["bf"] + n["ce"] + n["cf"] <= b["D"], "D budget")
    require(n["cg"] <= b["C"], "C budget")
    require(n["ad"] + n["af"] <= b["U"], "U budget")
    require(n["bd"] + n["bf"] <= b["V"], "V budget")
    require(n["be"] + n["bg"] <= b["S"], "Q budget")
    require(n["ae"] <= b["R"], "J budget")
    require(run.maximum_length <= b["M"], "length budget")
    require(run.steps <= b["bound"] <= b["coarse"], "total budget")


def frontier_step(word: str) -> Run:
    require(word != "cd" and is_frontier(word), "nonterminal frontier required")
    index = word.index("ag")
    intermediate = word[:index] + "fa" + word[index + 2:]
    run = normalize(intermediate)
    run.counts["ag"] += 1
    run.maximum_length = max(len(word), run.maximum_length)
    require(is_frontier(run.word), "frontier grammar not preserved")
    if is_frontier(word, three=True):
        require(is_frontier(run.word, three=True), "three-symbol frontier failed")
        require(run.counts["bf"] + run.counts["ce"] + run.counts["cf"] == 1,
                "single E consumption failed")
        require(run.counts["cf"] + run.counts["cg"] <= 2,
                "two boundary expansions failed")
        require(len(run.word) <= len(word) + 2, "frontier length bound failed")
        if word.count("g") >= 2:
            require(run.counts["ad"] + run.counts["bd"] == 0,
                    "administrative burst performed dynamics")
            require(value(run.word) == value(word), "administrative value changed")
            require(run.word.count("g") in (word.count("g") - 1, word.count("g")),
                    "administrative g count failed")
            require((run.word.count("g"), run.word.index("g")) <
                    (word.count("g"), word.index("g")),
                    "administrative burst rank failed")
        else:
            require(run.counts["ad"] >= 1, "single-g section had no dynamics")
    check_budget(word, run)
    return run


def frontier_features(word: str) -> dict[str, int | tuple[int, ...]]:
    return {
        "length": len(word),
        "value": value(word),
        "g_count": word.count("g"),
        "binary_count": word.count("a") + word.count("b"),
        "barrier_count": word.count("ag"),
        "g_run_multiset": tuple(sorted((len(x) for x in re.findall("g+", word)),
                                         reverse=True)),
        "binary_block_multiset": tuple(sorted((len(x) for x in re.findall("[ab]+", word)),
                                               reverse=True)),
    }


def run_checks(limit: int, context_depth: int, mixed_depth: int) -> dict:
    contexts = list(all_words(ALPHABET, context_depth))
    contextual_edges = 0
    for prefix in contexts:
        for suffix in contexts:
            for lhs, rhs in RULES:
                before, after = prefix + lhs + suffix, prefix + rhs + suffix
                require(difference(before, after) == expected_delta(lhs, prefix, suffix),
                        f"delta table failed: {before} -> {after}")
                if lhs != "ag":
                    require(rank(after) < rank(before), "context rank failed")
                contextual_edges += 1

    overlap_pairs = 0
    for lhs, _ in RULES:
        for other, _ in RULES:
            require(lhs[1:] != other[:1], "overlapping rules")
            overlap_pairs += 1

    mixed_words = 0
    mixed_max_steps = 0
    for interior in all_words("abefg", mixed_depth):
        start = "c" + interior + "d"
        left = normalize(start)
        right = normalize(start, rightmost=True)
        require(left.word == right.word, "W confluence sample failed")
        require(left.counts == right.counts, "W rule-count invariance failed")
        require(is_frontier(left.word), "normal-form grammar failed")
        check_budget(start, left)
        check_budget(start, right)
        mixed_words += 1
        mixed_max_steps = max(mixed_max_steps, left.steps)

    counterexamples: dict[str, dict] = {}
    total_frontier_edges = 0
    administrative_frontier_edges = 0
    single_g_frontier_edges = 0
    total_rewrites = 0
    max_events = (0, 1)
    max_rewrites = (0, 1)
    max_frontier_length = (0, 1)
    trace_samples = {}
    full_schedule_checks = min(limit, 128)
    for n in range(1, limit + 1):
        start = encode(n)
        initial = normalize(start)
        require(is_frontier(initial.word, three=True), "binary normalization slice failed")
        require(len(initial.word) <= len(start) + 1, "initial frontier expansion failed")
        counts = initial.counts.copy()
        maximum_length = initial.maximum_length
        word = initial.word
        events = 0
        samples = []
        while word != "cd":
            require(events < 100_000, "frontier event cap exceeded")
            nxt = frontier_step(word)
            if word.count("g") >= 2:
                administrative_frontier_edges += 1
            else:
                single_g_frontier_edges += 1
            features_before = frontier_features(word)
            features_after = frontier_features(nxt.word)
            for key, before in features_before.items():
                after = features_after[key]
                if after > before and key not in counterexamples:
                    counterexamples[key] = {
                        "source": n, "event_index": events,
                        "before_word": word, "after_word": nxt.word,
                        "before": before, "after": after,
                    }
            if n in (3, 7, 9, 27, 31, 127) and len(samples) < 12:
                samples.append({"word": word, "value": value(word)})
            counts.update(nxt.counts)
            maximum_length = max(maximum_length, nxt.maximum_length)
            events += 1
            total_frontier_edges += 1
            word = nxt.word
            max_frontier_length = max(max_frontier_length, (len(word), n))
        final_run = Run(word, counts, maximum_length)
        check_budget(start, final_run)
        require(counts["ag"] == events, "event accounting failed")
        if n <= full_schedule_checks:
            left = normalize(start, full=True)
            right = normalize(start, full=True, rightmost=True)
            require(left.word == right.word == word == "cd", "full schedules differ")
            require(left.counts == right.counts == counts,
                    "full schedule-independent counts failed")
        total_rewrites += final_run.steps
        max_events = max(max_events, (events, n))
        max_rewrites = max(max_rewrites, (final_run.steps, n))
        if samples:
            trace_samples[str(n)] = samples

    # Longer arbitrary contexts supplement the exhaustive short-context table.
    rng = random.Random(20261030)
    arbitrary_context_edges = 0
    for _ in range(2000):
        prefix = "".join(rng.choice(ALPHABET) for _ in range(rng.randrange(80)))
        suffix = "".join(rng.choice(ALPHABET) for _ in range(rng.randrange(80)))
        lhs, rhs = rng.choice(RULES)
        require(difference(prefix + lhs + suffix, prefix + rhs + suffix) ==
                expected_delta(lhs, prefix, suffix), "long-context delta failed")
        arbitrary_context_edges += 1

    # All-word finite prefixes, with more than one c/d boundary allowed.
    arbitrary_prefixes = 0
    for _ in range(200):
        start = "".join(rng.choice(ALPHABET) for _ in range(rng.randrange(1, 60)))
        word = start
        counts = Counter()
        maximum_length = len(word)
        for _ in range(400):
            hits = available(word)
            if not hits:
                break
            hit = rng.choice(hits)
            word = rewrite(word, hit)
            counts[hit[1]] += 1
            maximum_length = max(maximum_length, len(word))
            check_budget(start, Run(word, counts, maximum_length))
            arbitrary_prefixes += 1

    require(set(counterexamples) == set(frontier_features("cagd")),
            "some requested simple-order obstruction not found in range")
    return {
        "status": "PASS_BOUNDED_CHECKS_NOT_A_COLLATZ_PROOF",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "parameters": {"positive_source_limit": limit, "context_depth": context_depth,
                       "mixed_interior_depth": mixed_depth, "random_seed": 20261030},
        "contextual_edges": contextual_edges,
        "long_context_edges": arbitrary_context_edges,
        "rule_overlap_pairs_checked": overlap_pairs,
        "proper_mixed_words_normalized_two_ways": mixed_words,
        "maximum_W_steps_for_mixed_samples": mixed_max_steps,
        "arbitrary_word_prefix_budgets_checked": arbitrary_prefixes,
        "positive_sources_terminated_in_bounded_test": limit,
        "full_schedule_rule_count_comparisons": full_schedule_checks,
        "total_frontier_edges": total_frontier_edges,
        "administrative_frontier_edges": administrative_frontier_edges,
        "single_g_frontier_edges": single_g_frontier_edges,
        "total_full_rewrites_on_frontier_paths": total_rewrites,
        "maximum_ag_events": {"count": max_events[0], "source": max_events[1]},
        "maximum_rewrite_steps": {"count": max_rewrites[0], "source": max_rewrites[1]},
        "maximum_frontier_length": {"length": max_frontier_length[0],
                                     "source": max_frontier_length[1]},
        "simple_frontier_rank_counterexamples": counterexamples,
        "initial_trace_samples": trace_samples,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1024)
    parser.add_argument("--context-depth", type=int, default=2)
    parser.add_argument("--mixed-depth", type=int, default=4)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("orders-results.json"))
    args = parser.parse_args()
    require(args.limit >= 128, "limit must include counterexample controls through 128")
    require(args.context_depth >= 0 and args.mixed_depth >= 0, "negative depth")
    result = run_checks(args.limit, args.context_depth, args.mixed_depth)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n",
                           encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ("initial_trace_samples",
                                     "simple_frontier_rank_counterexamples")},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
