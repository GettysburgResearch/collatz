#!/usr/bin/env python3
"""Exact control for the unrestricted inverse-clock merger attempt."""

import json
from collections import Counter
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def T(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def odd_word(q):
    result = []
    while q != 1:
        n, a = 3 * q + 1, 0
        while n % 2 == 0:
            n //= 2
            a += 1
        result.append(a)
        q = n
        require(len(result) <= 1000, "unexpected odd-certificate bound")
    return result


def grade(e, word):
    return Counter(([2 * e + 1] if e else []) + [2 * a for a in word])


def compare(left, right):
    for key in sorted(set(left) | set(right), reverse=True):
        if left[key] != right[key]:
            return 1 if left[key] > right[key] else -1
    return 0


def main():
    target, source, q, exponent = 1263, 820, 205, 2
    word = [3, 3, 3, 1, 2, 3, 4]
    require(odd_word(q) == word, "source odd word mismatch")
    G = grade(exponent, word)
    gap_total = 0
    for length, a in enumerate(word, 1):
        gap_total += a
        require(3**length < 2**gap_total, "source prefix fails contraction")
    source_path = [source]
    while source_path[-1] != 1:
        source_path.append(T(source_path[-1]))
    require(len(source_path) - 1 == 21, "source clock mismatch")
    require(max(source_path[1:]) == 410, "source floor mismatch")
    require(max(source_path[1:]) <= (target - 1) // 2, "source floor not below target")
    require(source + 1 < target <= 2 * source + 1, "source interval mismatch")

    # This finite set is closed under ALL integral low-gap inverse parents.
    # Together with the unique last gap four (5 -> 1), induction covers
    # arbitrary lengths of the one-four language, not a depth cutoff.
    one_four = {3, 5, 7, 9, 11, 13, 17, 19, 25, 29, 33, 45, 51, 77, 205, 273}
    for n in one_four:
        require(odd_word(n).count(4) == 1, "listed source has wrong four count")
        require(max(odd_word(n)) <= 4, "listed source has a high gap")
        for a in (1, 2, 3):
            numerator = 2**a * n - 1
            if numerator % 3 == 0:
                parent = numerator // 3
                require(parent > 0 and parent % 2 == 1, "invalid low-gap parent")
                require(parent in one_four, "one-four inverse set is not closed")
    require(odd_word(273) == [2] + word, "273 first-hit word mismatch")
    no_padding_candidates = []
    for n in one_four | {1}:
        for e in range(4):
            order = compare(grade(e, odd_word(n)), G)
            no_padding_candidates.append((2**e * n, order, n, e))
    require(max(S for S, order, _, _ in no_padding_candidates if order <= 0) == 820,
            "at-most grade maximum mismatch")
    require(max(S for S, order, _, _ in no_padding_candidates if order < 0) == 546,
            "strictly-lower grade maximum mismatch")
    require(compare(grade(1, odd_word(273)), G) < 0, "546 grade witness failed")
    # The written proof handles all padding: it only adds grade four and
    # never changes the represented source. In particular the only two
    # candidate exceptions 205/273 at exponent two cannot become cheaper.
    require(compare(grade(2, word + [2]), G) > 0, "205 padding comparison failed")
    require(compare(grade(2, odd_word(273)), G) > 0, "273 grade comparison failed")

    closed = {1, 2}
    hit_clocks = []
    for u in range(1, target):
        n, clock = u, 0
        visited = set()
        while n != 1:
            require(n not in visited, "a smaller source entered a nontrivial cycle")
            visited.add(n)
            closed.add(n)
            n = T(n)
            clock += 1
            require(clock <= 2000, "smaller-source completion bound exceeded")
        hit_clocks.append(clock)
    require(len(closed) == 2008 and max(closed) == 125252, "frozen closed-set fixture changed")
    require(max(hit_clocks) == 115, "smaller-source hit-clock fixture changed")
    require(all(u in closed for u in range(1, target)), "closed set omits a smaller start")
    require(all(T(n) in closed for n in closed), "smaller-source set is not forward closed")

    target_path = [target]
    for _ in range(26):
        target_path.append(T(target_path[-1]))
    require(all(n not in closed for n in target_path[:25]), "unexpected early smaller merger")
    require(target_path[25] == 1622 and T(1081) == 1622, "first merger witness mismatch")
    require(all(n >= target for n in target_path[:26]), "unexpected early descent")
    require(target_path[26] == 811 < target, "first descent mismatch")

    result = {
        "status": "explicit checks passed; target converges; no global proof asserted",
        "target": target,
        "source": source,
        "source_odd_word": word,
        "source_path": source_path,
        "source_grade": dict(sorted(G.items(), reverse=True)),
        "global_grade_bounds": {
            "at_most_G_maximum_source": 820,
            "strictly_below_G_maximum_source": 546,
            "scope": "written all-word argument plus checked finite inverse closure; arbitrary terminal padding retained",
        },
        "one_four_inverse_closed_set": sorted(one_four),
        "smaller_start_count": target - 1,
        "maximum_smaller_hit_clock": max(hit_clocks),
        "smaller_forward_closed_set_size": len(closed),
        "smaller_forward_closed_set": sorted(closed),
        "target_path_through_first_descent": target_path,
        "no_smaller_merger_target_clocks": [0, 24],
        "no_smaller_merger_inverse_clocks": "all natural numbers, by forward closure and induction",
        "first_merger": {"target_clock": 25, "value": 1622, "smaller_start": 1081, "smaller_clock": 1},
        "first_descent": {"target_clock": 26, "value": 811},
    }
    out = Path(__file__).with_name("whole-word-control.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in
                      ("status", "target", "smaller_forward_closed_set_size", "first_merger", "first_descent")}))


if __name__ == "__main__":
    main()
