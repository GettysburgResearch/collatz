#!/usr/bin/env python3
"""Exact complete-tree control for GLOBAL_SOURCE_SYNTHESIS.md.

Standard library only. The node limit is an abort guard, never a mathematical
cutoff: every reported closure must have an empty work queue and is independently
checked under every legal inverse gap 1, 2, 3. No assertions are used.
"""

from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
import json
from pathlib import Path
import sys


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def predecessor(n: int, gap: int) -> int | None:
    numerator = (1 << gap) * n - 1
    if numerator % 3:
        return None
    result = numerator // 3
    require(result > 0 and result % 2 == 1, "illegal ordinary inverse")
    return result


def follow_word(n: int, word: list[int]) -> int:
    require(n > 0 and n % 2 == 1, "source is not positive odd")
    for gap in word:
        numerator = 3 * n + 1
        require(numerator % (1 << gap) == 0, "nonintegral forward word")
        n = numerator >> gap
        require(n > 0 and n % 2 == 1, "gap is not the exact valuation")
    return n


def close_three(seeds: dict[int, list[int]], stop: int) -> dict[int, list[int]]:
    """Attach all gaps <=3 to the specified exact suffix words."""
    words = {n: list(word) for n, word in seeds.items()}
    queue = deque(words)
    while queue:
        n = queue.popleft()
        for gap in range(1, 4):
            p = predecessor(n, gap)
            if p is None or p in words:
                continue
            words[p] = [gap] + words[n]
            queue.append(p)
            require(len(words) <= 100_000, "ABORT: closure limit reached")
    # This separate check certifies the complete, unbounded-word closure.
    for n, word in words.items():
        require(follow_word(n, word) == stop, "wrong retained endpoint")
        for gap in range(1, 4):
            p = predecessor(n, gap)
            require(p is None or p in words, "predecessor set is not closed")
    return words


def first_hit_word(n: int) -> list[int]:
    result = []
    seen = set()
    while n != 1:
        require(n not in seen, "unexpected cycle in supplied finite source")
        seen.add(n)
        value = 3 * n + 1
        gap = (value & -value).bit_length() - 1
        result.append(gap)
        n = value >> gap
        require(len(result) <= 10_000, "ABORT: first-hit replay limit")
    return result


def grade(e: int, word: list[int]) -> tuple[int, ...]:
    entries = [2 * a for a in word] + ([2 * e + 1] if e else [])
    require(all(2 <= a <= 8 for a in entries), "grade outside this control")
    counts = Counter(entries)
    return tuple(counts[a] for a in range(8, 1, -1))


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def unit_boundary_check(root: int, cluster: dict[int, list[int]]) -> dict:
    units = {n for n in cluster if n % 3}
    require(root in units and root != 1, "tree root boundary not applicable")
    counts = Counter(n % 9 for n in units)
    require(counts[7] == counts[2] + 1, "unit leaf/branch count failed")
    rhs = (
        sum(3 * n for n in units if n % 9 == 7)
        + sum(n + 1 for n in units if n % 9 == 8)
        - sum(n - 1 for n in units if n % 9 in (1, 4))
        - sum(7 * n - 2 for n in units if n % 9 == 2)
        - sum(5 * n - 1 for n in units if n % 9 == 5)
    )
    require(rhs == 3 * root, "exact height boundary identity failed")
    return {"unit_vertices": len(units), "residue_counts": dict(sorted(counts.items()))}


def lifting_example(length: int) -> dict:
    # Lift the exponent m one ternary digit at a time. The proof in the note
    # establishes existence for every length; these are exact finite checks.
    m, modulus, period = 0, 3, 1
    for _ in range(length + 2):
        modulus *= 3
        target = (113 * pow(80, -1, modulus)) % modulus
        choices = [m + j * period for j in range(3)
                   if pow(4, m + j * period, modulus) == target]
        require(len(choices) == 1, "exponent lift not unique")
        m = choices[0]
        period *= 3
    require(m > 0, "terminal exponent not positive")
    v = (pow(4, m) - 1) // 3
    require(v % 9 == 7, "wrong dead-cell root")
    require((80 * v - 11) % pow(3, length + 2) == 0, "wrong congruence")
    low = predecessor(v, 2)
    require(low is not None and low % 3 == 0, "wrong complete small cluster")
    x = predecessor(v, 4)
    require(x is not None, "gap four is illegal")
    n = predecessor(x, 2)
    require(n is not None, "gap two is illegal")
    for _ in range(length):
        n = predecessor(n, 3)
        require(n is not None, "repeated gap three is illegal")
    word = [3] * length + [2, 4, 2 * m]
    require(follow_word(n, word) == 1, "family is not a complete certificate")
    require(n * pow(3, length + 1) > 16 * pow(8, length) * low,
            "coercivity failure inequality failed")
    return {"length": length, "m": m, "root_bits": v.bit_length(),
            "source_bits": n.bit_length(), "terminal_gap": 2 * m}


def check() -> dict:
    layers: list[dict[int, list[int]]] = [{1: []}]
    for _ in range(2):
        seeds = {}
        for n, word in layers[-1].items():
            p = predecessor(n, 4)
            if p is not None:
                seeds[p] = [4] + word
        layers.append(close_three(seeds, 1))
    require([len(layer) for layer in layers] == [1, 16, 1354], "layer sizes changed")
    all_words = {}
    for k, layer in enumerate(layers):
        require(not (set(all_words) & set(layer)), "different four-layers overlap")
        for n, word in layer.items():
            require(word == first_hit_word(n), "not the literal first-hit word")
            require(max(word, default=0) <= 4 and word.count(4) == k,
                    "wrong gap layer")
        all_words.update(layer)
    require(len(all_words) == 1371, "full source census size changed")

    q = max(all_words)
    word = all_words[q]
    require(q == 184443431956737, "maximum source changed")
    g = grade(3, word)
    candidates = [(pow(2, e) * n, n, e, grade(e, w))
                  for n, w in all_words.items() for e in range(4)]
    strict = max(row for row in candidates if row[3] < g)
    equal = max(row for row in candidates if row[3] == g)
    require(strict[0] == 1106660591740424, "strict-lower source maximum changed")
    require(equal[0] == 1475547455653896, "same-grade source maximum changed")
    require(equal[1:3] == (q, 3), "wrong same-grade maximizer")

    target = pow(2, 51) - 1
    source = 8 * q
    require(2 * strict[0] + 1 < target <= 2 * source + 1,
            "target not in the exact minimum-grade interval")
    require(source + 1 < target and target % 4 == 3, "wrong canonical target cell")
    require(word[-4:] == [1, 2, 3, 4] and len(word) > 4,
            "canonical supplied tail absent")
    running_gap = 0
    for k, gap in enumerate(word, 1):
        running_gap += gap
        require(pow(3, k) < pow(2, running_gap), "literal prefix does not contract")
    source_states = [source]
    while source_states[-1] != 1:
        source_states.append(shortcut(source_states[-1]))
        require(len(source_states) <= 10_000, "ABORT: source replay limit")
    require(max(source_states[1:]) <= (target - 1) // 2, "source floor fails")

    target_states = [target]
    while len(target_states) == 1 or target_states[-1] >= target:
        target_states.append(shortcut(target_states[-1]))
        require(len(target_states) <= 10_000, "ABORT: target descent limit")
    require(len(target_states) - 1 == 138, "target descent time changed")
    require(target_states[-1] == 2089005280842391, "target descent endpoint changed")
    complete_target = list(target_states)
    while complete_target[-1] != 1:
        complete_target.append(shortcut(complete_target[-1]))
        require(len(complete_target) <= 10_000, "ABORT: target convergence limit")
    require(len(complete_target) - 1 == 384, "target convergence clock changed")

    small = close_three({7: []}, 7)
    large = close_three({37: []}, 37)
    require(set(small) == {7, 9}, "small inverse cluster changed")
    require(len(large) == 808 and max(large) == q, "large inverse cluster changed")
    require(all_words[q] == large[q] + [4, 1, 1, 2, 3, 4],
            "literal retained tail at seven is not the specified one")
    require(16 * max(small) + 1 == 145 < target,
            "deleted-prefix replacement unexpectedly captures")
    boundary = unit_boundary_check(37, large)
    unit_boundary_check(7, small)

    encoding = json.dumps([[n, all_words[n]] for n in sorted(all_words)],
                          separators=(",", ":")).encode()
    return {
        "scope": "complete finite grade control and all-length cluster closure; no Collatz proof",
        "four_layer_sizes": [len(layer) for layer in layers],
        "all_first_hit_source_rows_sha256": sha256(encoding).hexdigest(),
        "max_odd_source": q, "source_word": word, "source_odd_steps": len(word),
        "source_odd_clock": sum(word), "source_powered_clock": sum(word) + 3,
        "grade_counts_at_8_through_2": list(g),
        "maximum_strict_lower_source": strict[0],
        "maximum_same_grade_source": equal[0],
        "target": target, "target_first_descent_clock": len(target_states) - 1,
        "target_first_descent_endpoint": target_states[-1],
        "target_first_one_clock": len(complete_target) - 1,
        "source_floor": (target - 1) // 2,
        "actual_positive_time_source_max": max(source_states[1:]),
        "cluster_7": {"vertices": sorted(small), "maximum_powered_source": 72},
        "cluster_37": {"vertices": len(large), "maximum": max(large),
                       "maximum_inverse_depth": max(map(len, large.values())), **boundary},
        "lifting_family_controls": [lifting_example(k) for k in range(1, 5)],
        "badness_hypothesis": False,
        "success": True,
    }


if __name__ == "__main__":
    result = check()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(rendered, encoding="utf-8")
    elif len(sys.argv) != 1:
        raise SystemExit("usage: check_global_source.py [output.json]")
    print(rendered, end="")
