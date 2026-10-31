#!/usr/bin/env python3
"""Semantic integration checks and explicit negative controls.

This file imports the producer's selector for integration tests. The separate
verify.py does not import it. All checks remain active under Python -O.
"""
from __future__ import annotations
from functools import lru_cache
import itertools
import json
import random
from run import compile_descent
from verify import same, unique_object

RULES = (("ad", "d"), ("bd", "gd"), ("ae", "ea"), ("af", "eb"),
         ("ag", "fa"), ("be", "fb"), ("bf", "ga"), ("bg", "gb"),
         ("ce", "cb"), ("cf", "caa"), ("cg", "cab"))


def check(ok: bool, message: str = "semantic control failed") -> None:
    if not ok:
        raise ValueError(message)


def T(n: int) -> int:
    check(n > 1, "physical step out of killed 1")
    return (3 * n + 1) // 2 if n % 2 else n // 2


def U(n: int) -> int:
    n = 3 * n + 1
    return n // (n & -n)


def v2(n: int) -> int:
    return (n & -n).bit_length() - 1


def value_and_H(word: str) -> tuple[int, int]:
    check(word[0] == "c" and word[-1] == "d")
    value, admin = 1, 0
    for letter in word[1:-1]:
        if letter in "efg":
            admin += value.bit_length()
            value = 3 * value + "efg".index(letter)
        else:
            check(letter in "ab")
            value = 2 * value + (letter == "b")
    return value, admin


@lru_cache(maxsize=None)
def q10(n: int) -> int:
    steps = 0
    while n != 1 and n.bit_count() <= 10:
        check(steps < 79, "capped rank not total")
        n = U(n)
        steps += 1
    return steps


def rank(word: str):
    value, admin = value_and_H(word)
    a = v2(value)
    return q10(value >> a), a, admin


def moves(word: str):
    for pos in range(len(word) - 1):
        for index, (left, right) in enumerate(RULES):
            if word[pos:pos + 2] == left:
                yield index, word[:pos] + right + word[pos + 2:]


def main() -> None:
    rng = random.Random(20261031)
    edge_count = 0
    schedules = 0
    for length in range(6):
        for interior in itertools.product("abefg", repeat=length):
            word = "c" + "".join(interior) + "d"
            n, admin = value_and_H(word)
            before = rank(word)
            for rule, after in moves(word):
                m, new_admin = value_and_H(after)
                edge_count += 1
                if rule >= 2:
                    check(m == n and new_admin == admin - 1)
                elif rule == 0:
                    check(m == n // 2 and new_admin == admin)
                else:
                    check(m == (3 * n + 1) // 2)
                    check(new_admin == admin + ((n - 1) // 2).bit_length())
                check(rank(after) < before, "literal ordinal failed")

    for _ in range(300):
        word = "c" + "".join(rng.choice("abefg") for _ in range(rng.randrange(1, 25))) + "d"
        initial, H0 = value_and_H(word)
        if (initial >> v2(initial)).bit_count() > 10:
            continue
        bound = H0 + 80 * (initial.bit_length() - 1) + 3239
        for policy in ("left", "right", "random"):
            current, steps = word, 0
            while True:
                n, _ = value_and_H(current)
                if n == 1 or (n >> v2(n)).bit_count() > 10:
                    break
                choices = list(moves(current))
                check(bool(choices), "nonterminal stuck word")
                choice = choices[0] if policy == "left" else choices[-1] if policy == "right" else rng.choice(choices)
                after = choice[1]
                check(rank(after) < rank(current))
                current = after
                steps += 1
                check(steps <= bound, "literal budget exceeded")
            schedules += 1

    separator_cases = 0
    for cap in range(2, 11):
        for _ in range(80):
            upper_ones = rng.randrange(1, cap)
            lower_ones = rng.randrange(1, cap - upper_ones + 1)
            upper = 1 + sum(1 << p for p in rng.sample(range(1, 10001), upper_ones - 1))
            lower = 1 + sum(1 << p for p in rng.sample(range(1, 10001), lower_ones - 1))
            h, z = 0, upper
            while z.bit_count() < cap:
                z *= 3
                h += 1
            D = lower.bit_length() + 2 * h
            original = (upper << D) + lower
            actual, shadow, A = original, lower, 0
            for j in range(1, h + 1):
                a = v2(3 * shadow + 1)
                shadow = U(shadow)  # Explicitly permitted shadow U(1)=1.
                A += a
                actual = U(actual)
                check(A < D)
                check(actual == ((3 ** j * upper) << (D - A)) + shadow)
                check(actual.bit_count() == (3 ** j * upper).bit_count() + shadow.bit_count())
            check(actual.bit_count() > cap)
            separator_cases += 1

    sparse_cases = 0
    max_bits = 0
    for weight in range(1, 9):
        for _ in range(100):
            n = 1 + sum(1 << p for p in rng.sample(range(1, 20001), weight - 1))
            if n == 1:
                continue
            result = compile_descent(n)
            check(result is not None, "sparse coverage failed")
            clock, endpoint = result
            actual = n
            for _ in range(clock):
                actual = T(actual)
            check(actual == endpoint < n and clock <= 552)
            max_bits = max(max_bits, n.bit_length())
            sparse_cases += 1
    accepted = outside = 0
    for _ in range(1000):
        n = rng.getrandbits(700) | 1
        result = compile_descent(n)
        if result is None:
            outside += 1
            continue
        clock, endpoint = result
        actual = n
        for _ in range(clock):
            actual = T(actual)
        check(actual == endpoint < n)
        accepted += 1

    # The strict gap guard cannot be weakened to d >= 2h: n=5, S=2
    # would falsely predict three ones after one odd step, whereas U(5)=1.
    check(U(5) == 1 and (3).bit_count() + 1 == 3)
    # Finite cores alone do not exclude nontrivial cycles for other offsets.
    def minus(n):
        y = 3 * n - 1
        return y // (y & -y)
    check(minus(5) == 7 and minus(7) == 5)
    # Cap exit is not convergence, and the core is not forward invariant.
    core4 = set()
    stack = [(1, 1)]
    while stack:
        n, count = stack.pop()
        core4.add(n)
        if count < 4:
            h, z = 0, n
            while z.bit_count() < 4:
                z *= 3
                h += 1
            stack.extend(((n << d) + 1, count + 1) for d in range(1, 2 * h + 1))
    leaving = next(n for n in sorted(core4) if U(n).bit_count() <= 4 and U(n) not in core4)
    exiting = next(n for n in sorted(core4) if U(n).bit_count() > 4)
    negative_examples = {"gap_equality": 5, "minus_cycle": [5, 7],
                         "core_not_invariant": [leaving, U(leaving)],
                         "cap_exit_not_success": [exiting, U(exiting)]}
    rejected = 0
    for bad in (True, 0, 80, "79", [79], None):
        try:
            same(79, bad)
        except ValueError:
            rejected += 1
        else:
            raise ValueError("mutation accepted")
    try:
        json.loads('{"schema":1,"schema":1}', object_pairs_hook=unique_object)
    except ValueError:
        rejected += 1
    else:
        raise ValueError("duplicate accepted")
    try:
        T(1)
    except ValueError:
        rejected += 1
    else:
        raise ValueError("killed-state violation accepted")
    print(json.dumps({"literal_srs_edges": edge_count, "complete_schedules": schedules,
                      "separated_block_cases": separator_cases,
                      "sparse_lifts": sparse_cases, "largest_lift_bits": max_bits,
                      "dense_lifts": {"accepted": accepted, "outside": outside},
                      "negative_examples": negative_examples,
                      "direct_mutations_rejected": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
