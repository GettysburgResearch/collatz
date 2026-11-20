#!/usr/bin/env python3
"""Independent rule-by-rule and scheduling replay of the run-cap AYH order."""

from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path
import random


ROOT = Path(__file__).resolve().parents[2]
RULES = (("ad", "d"), ("bd", "gd"), ("ae", "ea"), ("af", "eb"),
         ("ag", "fa"), ("be", "fb"), ("bf", "ga"), ("bg", "gb"),
         ("ce", "cb"), ("cf", "caa"), ("cg", "cab"))
DIGITS = {"a": (2, 0), "b": (2, 1), "e": (3, 0), "f": (3, 1), "g": (3, 2)}


def require(value, message):
    if not value:
        raise ValueError(message)


def runs(n):
    bits = "0" + bin(n)[2:]
    return sum(left == "0" and right == "1" for left, right in zip(bits, bits[1:]))


def decode(word):
    require(word.startswith("c") and word.endswith("d"), "improper boundaries")
    value, potential = 1, 0
    for letter in word[1:-1]:
        base, digit = DIGITS[letter]
        if base == 3:
            potential += len(bin(value)) - 2
        value = base * value + digit
    return value, potential


def odd_part(n):
    valuation = 0
    while n % 2 == 0:
        n //= 2
        valuation += 1
    return n, valuation


@lru_cache(None)
def clock(odd):
    value = odd
    for elapsed in range(108):
        if value == 1 or runs(value) > 6:
            return elapsed
        value, _ = odd_part(3 * value + 1)
    raise ValueError("107-event run-cap certificate failed on a replayed source")


def state(word):
    value, potential = decode(word)
    odd, valuation = odd_part(value)
    return value, potential, (clock(odd), valuation, potential)


def guarded(value):
    odd, _ = odd_part(value)
    return value > 1 and runs(odd) <= 6


def successors(word):
    for number, (left, right) in enumerate(RULES):
        position = word.find(left)
        while position >= 0:
            yield position, number, word[:position] + right + word[position + len(left):]
            position = word.find(left, position + 1)


def binary_word(n):
    return "c" + "".join("b" if bit == "1" else "a" for bit in bin(n)[3:]) + "d"


def ternary_word(n):
    digits = []
    while n:
        n, digit = divmod(n, 3)
        digits.append(digit)
    digits.reverse()
    return "c" + ("a" if digits[0] == 2 else "") + "".join("efg"[d] for d in digits[1:]) + "d"


def main():
    word_count = guarded_edges = 0
    rule_counts = [0] * len(RULES)
    for length in range(8):
        for letters in product(DIGITS, repeat=length):
            word = "c" + "".join(letters) + "d"
            value, potential, rank = state(word)
            word_count += 1
            for _, number, successor in successors(word):
                other, other_potential, other_rank = state(successor)
                rule_counts[number] += 1
                if number >= 2:
                    require(other == value and other_potential == potential - 1, "administrative rule defect")
                elif number == 0:
                    require(value % 2 == 0 and 2 * other == value and other_potential == potential, "even dynamic rule defect")
                else:
                    require(value % 2 == 1 and 2 * other == 3 * value + 1, "odd dynamic value defect")
                    require(other_potential - potential == value.bit_length() - 1, "odd dynamic potential defect")
                if guarded(value):
                    require(other_rank < rank, "guarded ordinal rank did not decrease")
                    guarded_edges += 1

    rng = random.Random(20261120)
    sequences = sequence_steps = maximum_steps = 0
    for n in range(1, 513):
        for initial in (binary_word(n), ternary_word(n)):
            require(decode(initial)[0] == n, "alternative representation mismatch")
            for policy in ("leftmost", "rightmost", "random"):
                word = initial
                source, h0 = decode(word)
                budget = h0 + 108 * (source.bit_length() - 1) + 5885
                steps = odds = evens = administrative = created = 0
                while guarded(decode(word)[0]):
                    choices = list(successors(word))
                    require(choices, "nonterminal proper word has no rule")
                    if policy == "leftmost":
                        chosen = min(choices, key=lambda row: (row[0], row[1]))
                    elif policy == "rightmost":
                        chosen = max(choices, key=lambda row: (row[0], -row[1]))
                    else:
                        chosen = rng.choice(choices)
                    _, rule, other = chosen
                    before, h_before, rank_before = state(word)
                    _, h_after, rank_after = state(other)
                    require(rank_after < rank_before, "scheduled rank failure")
                    if rule >= 2:
                        administrative += 1
                    elif rule == 0:
                        evens += 1
                    else:
                        odds += 1
                        created += h_after - h_before
                    word = other
                    steps += 1
                    require(steps <= budget, "literal scheduling budget exceeded")
                final_value, final_h = decode(word)
                b0 = source.bit_length()
                require(odds <= 107, "odd clock exceeded")
                require(odds + evens <= b0 - 1 + 2 * odds, "dynamic budget failure")
                require(created <= odds * (b0 - 1) + odds * (odds - 1) // 2, "creation budget failure")
                require(administrative == h0 + created - final_h, "administrative conservation failure")
                require(final_value == 1 or not guarded(final_value), "incorrect stopping guard")
                sequences += 1
                sequence_steps += steps
                maximum_steps = max(maximum_steps, steps)

    unguarded = binary_word(5461)
    bad_successor = next(other for _, number, other in successors(unguarded) if number == 1)
    require(not guarded(5461), "negative control unexpectedly guarded")
    require(state(bad_successor)[2] > state(unguarded)[2], "unguarded rank-growth control failed")
    files = ("research/fixed-integer-descent/rewriting.md", "experiments/fixed_integer_rewriting.py")
    report = {
        "status": "PASS",
        "scope": "Separate rule table, binary-string runs, literal odd clock, and three rewrite schedulers; does not repeat the cap-six finite core proof.",
        "file_sha256": {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for path in files},
        "proper_words_through_inner_length": 7,
        "proper_words": word_count,
        "all_rule_occurrences": sum(rule_counts),
        "guarded_rank_edges": guarded_edges,
        "rule_occurrences": {left + " -> " + right: count for (left, right), count in zip(RULES, rule_counts)},
        "odd_clock_values_replayed": clock.cache_info().currsize,
        "scheduled_sequences": sequences,
        "scheduled_rewrite_steps": sequence_steps,
        "maximum_scheduled_length": maximum_steps,
        "unguarded_control": {"source": 5461, "destination": decode(bad_successor)[0], "before_rank": list(state(unguarded)[2]), "after_rank": list(state(bad_successor)[2])},
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
