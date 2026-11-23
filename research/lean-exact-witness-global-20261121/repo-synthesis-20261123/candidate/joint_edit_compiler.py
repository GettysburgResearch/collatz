#!/usr/bin/env python3
"""Total exact decision for a prescribed insertion/deletion budget.

Both coordinates are actual positive Collatz trajectories.  A matching
column advances both, and requires equal input parity.  L or R advances
only that coordinate and spends one edit.  The search returns a literal
first-merger certificate, or proves there is none within the supplied
edit budget.  Rejection is not a nonconvergence certificate.
"""

from __future__ import annotations

import argparse
from collections import deque
from functools import lru_cache
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def shortcut(n: int) -> int:
    require(type(n) is int and n > 0, "the state must be a positive integer")
    return (3 * n + 1) // 2 if n & 1 else n // 2


def valuation_two(n: int) -> int:
    require(type(n) is int and n != 0, "valuation requires a nonzero integer")
    n = abs(n)
    return (n & -n).bit_length() - 1


def check_certificate(certificate: dict) -> dict:
    x, y = certificate["start"]
    require(type(x) is int and x > 0 and type(y) is int and y > 0,
            "positive integer sources required")
    word = certificate["alignment"]
    require(type(word) is str, "alignment must be a string")
    left, right, edits = [x], [y], 0
    for column in word:
        require(x != y, "certificate continues after its first merger")
        if column == "=":
            require(x % 2 == y % 2, "a matching column has unequal parities")
            x, y = shortcut(x), shortcut(y)
            left.append(x)
            right.append(y)
        elif column == "L":
            x = shortcut(x)
            left.append(x)
            edits += 1
        elif column == "R":
            y = shortcut(y)
            right.append(y)
            edits += 1
        else:
            raise ValueError("unknown alignment column")
    require(x == y, "the two ordinary endpoints differ")
    require(edits <= certificate["edit_budget"], "edit budget exceeded")
    bit_height = max(certificate["start"]).bit_length()
    bound = bit_height * ((1 << edits) - 1)
    require(len(word) <= bound, "proved alignment-column bound violated")
    return {
        "start": list(certificate["start"]),
        "edit_budget": certificate["edit_budget"],
        "edits": edits,
        "alignment": word,
        "columns": len(word),
        "column_bound": bound,
        "left_clock": len(left) - 1,
        "right_clock": len(right) - 1,
        "endpoint": x,
        "left_path": left,
        "right_path": right,
    }


def compile_merger(x: int, y: int, edit_budget: int) -> dict:
    require(type(x) is int and x > 0 and type(y) is int and y > 0,
            "positive integer sources required")
    require(type(edit_budget) is int and edit_budget >= 0,
            "edit budget must be a nonnegative integer")

    @lru_cache(maxsize=None)
    def seek(a: int, b: int, fuel: int) -> str | None:
        if a == b:
            return ""
        if fuel == 0:
            return None
        # Exactly this many simultaneous inputs have equal parity.
        # Every possible earlier edit location is tried, in both directions.
        common = valuation_two(a - b)
        u, v = a, b
        for k in range(common + 1):
            left = seek(shortcut(u), v, fuel - 1)
            if left is not None:
                return "=" * k + "L" + left
            right = seek(u, shortcut(v), fuel - 1)
            if right is not None:
                return "=" * k + "R" + right
            if k < common:
                require(u % 2 == v % 2, "internal common-run invariant failed")
                u, v = shortcut(u), shortcut(v)
        require(u % 2 != v % 2, "common-run valuation endpoint failed")
        return None

    word = seek(x, y, edit_budget)
    summary = {
        "accepted": word is not None,
        "start": [x, y],
        "edit_budget": edit_budget,
        "clock_bound": max(x, y).bit_length() * ((1 << edit_budget) - 1),
        "scope": "exact bounded-edit ordinary merging; not universal convergence",
    }
    if word is not None:
        summary["certificate"] = check_certificate({
            "start": [x, y], "edit_budget": edit_budget, "alignment": word,
        })
    return summary


def grid_oracle(x: int, y: int, edit_budget: int) -> bool:
    """Independent finite dynamic program, not the recursive compiler.

    It inspects the square allowed by the theorem, without any convergence
    assumption or stopping-time oracle.  The test domain is intentionally
    small; the theorem, not these controls, supplies arbitrary-budget scope.
    """
    bound = max(x, y).bit_length() * ((1 << edit_budget) - 1)
    left, right = [x], [y]
    for _ in range(bound):
        left.append(shortcut(left[-1]))
        right.append(shortcut(right[-1]))
    row = list(range(bound + 1))
    for i in range(bound + 1):
        if i:
            previous = row
            row = [i]
            for j in range(1, bound + 1):
                cost = min(previous[j], row[-1]) + 1
                if left[i - 1] % 2 == right[j - 1] % 2:
                    cost = min(cost, previous[j - 1])
                row.append(cost)
        for j, cost in enumerate(row):
            if cost <= edit_budget and left[i] == right[j]:
                return True
    return False


def path_from_tuple(source: int, exponents: list[int]) -> list[int]:
    require(type(source) is int and source > 0 and source % 2 == 1,
            "tuple source must be positive and odd")
    require(type(exponents) is list and bool(exponents) and exponents[0] == 0,
            "tuple must start at zero")
    require(all(type(a) is int and a >= 0 for a in exponents),
            "nonnegative integer exponents required")
    require(all(a < b for a, b in zip(exponents, exponents[1:])),
            "tuple exponents must strictly increase")
    r = len(exponents) - 1
    lhs = 3 ** r * source + sum(3 ** (r - 1 - j) * 2 ** exponents[j]
                               for j in range(r))
    require(lhs == 2 ** exponents[-1], "complete tuple identity failed")
    result = [source]
    odd_clocks = set(exponents[:-1])
    for k in range(exponents[-1]):
        require((result[-1] % 2 == 1) == (k in odd_clocks),
                "tuple does not replay its exact odd clocks")
        result.append(shortcut(result[-1]))
    require(result[-1] == 1, "tuple endpoint is not one")
    return result


def tuple_from_path(path: list[int]) -> list[int]:
    require(bool(path) and path[0] % 2 == 1 and path[-1] == 1,
            "odd source and endpoint one required")
    exponents = [i for i, n in enumerate(path[:-1]) if n % 2] + [len(path) - 1]
    require(path_from_tuple(path[0], exponents) == path, "emitted tuple replay failed")
    return exponents


def transport_witness(target: int, source: int, source_tuple: list[int],
                      edit_budget: int) -> dict:
    """Consume the whole source tuple and emit a whole target tuple.

    Any terminal-cycle padding in either input or merger is allowed.
    This function terminates even on rejection.  Universal success for
    target=(source+1)//2 is the remaining unproved assertion.
    """
    require(type(target) is int and target > 0 and target % 2 == 1,
            "the target tuple requires a positive odd target")
    source_path = path_from_tuple(source, source_tuple)
    result = compile_merger(target, source, edit_budget)
    result["source_tuple"] = source_tuple
    if not result["accepted"]:
        return result
    certificate = result["certificate"]
    right_clock = certificate["right_clock"]
    output_path = certificate["left_path"][:]
    if right_clock < len(source_path):
        require(output_path[-1] == source_path[right_clock], "source endpoint mismatch")
        output_path.extend(source_path[right_clock + 1:])
    else:
        require(output_path[-1] in (1, 2), "post-witness endpoint left the core cycle")
        if output_path[-1] == 2:
            output_path.append(1)
    # If the target had already arrived, retain the first complete witness.
    output_path = output_path[:output_path.index(1) + 1]
    result["target_tuple"] = tuple_from_path(output_path)
    result["target_path"] = output_path
    result["target_clock_bound"] = 2 * result["clock_bound"] + source_tuple[-1]
    require(len(output_path) - 1 <= result["target_clock_bound"],
            "witness consumer clock bound failed")
    return result


def closed_orbit_minimum(x: int, y: int, left_clock: int, right_clock: int) -> dict:
    """Exact all-clock oracle for supplied finite ordinary core witnesses.

    The two finite state lists are checked to reach one.  Their Cartesian
    product is forward closed after retaining 1 -> 2 -> 1, so a 0/1 shortest
    path calculation covers arbitrary terminal padding, not only a prefix.
    """
    def finite_orbit(n: int, clock: int) -> tuple[set[int], dict[int, int]]:
        states = [n]
        for _ in range(clock):
            states.append(shortcut(states[-1]))
        require(states[-1] == 1, "supplied ordinary clock does not reach one")
        vertices = set(states) | {1, 2}
        edges = {a: shortcut(a) for a in vertices}
        require(set(edges.values()) <= vertices, "orbit graph is not forward closed")
        return vertices, edges

    left, left_next = finite_orbit(x, left_clock)
    right, right_next = finite_orbit(y, right_clock)
    vertices = {(a, b) for a in left for b in right}
    outgoing = {}
    incoming = {v: [] for v in vertices}
    for a, b in sorted(vertices):
        edges = [((left_next[a], b), "L", 1), ((a, right_next[b]), "R", 1)]
        if a % 2 == b % 2:
            edges.append(((left_next[a], right_next[b]), "=", 0))
        outgoing[a, b] = edges
        for endpoint, label, cost in edges:
            incoming[endpoint].append(((a, b), label, cost))
    distances = {v: 0 for v in sorted(vertices) if v[0] == v[1]}
    todo = deque(distances)
    while todo:
        v = todo.popleft()
        for u, _, cost in incoming[v]:
            d = distances[v] + cost
            if d < distances.get(u, len(vertices) + 1):
                distances[u] = d
                (todo.appendleft if cost == 0 else todo.append)(u)
    require(len(distances) == len(vertices), "a core basin pair was not reachable")
    # Check the complete Bellman lower certificate, not just the search result.
    for u, edges in outgoing.items():
        for v, _, cost in edges:
            require(distances[u] <= cost + distances[v], "Bellman lower bound failed")
        if u[0] != u[1]:
            require(any(distances[u] == cost + distances[v] for v, _, cost in edges),
                    "Bellman equality witness missing")
    return {
        "start": [x, y], "closed_pair_states": len(vertices),
        "minimum_edit_budget": distances[x, y],
        "scope": "all clocks including arbitrary core-cycle padding; finite closed ordinary graph",
    }


def self_test() -> dict:
    cases = accepted = 0
    for x in range(1, 17):
        for y in range(1, 17):
            for t in range(4):
                result = compile_merger(x, y, t)
                expected = grid_oracle(x, y, t)
                require(result["accepted"] == expected, "compiler/grid disagreement")
                cases += 1
                accepted += int(result["accepted"])
    common_cases = 0
    for x in range(1, 65):
        for y in range(1, x):
            k = valuation_two(x - y)
            a, b = x, y
            for _ in range(k):
                require(a % 2 == b % 2, "premature parity mismatch")
                a, b = shortcut(a), shortcut(b)
            require(a % 2 != b % 2, "late parity mismatch")
            common_cases += 1
    # These include both edit directions and a delayed insertion.
    fixtures = [compile_merger(3, 2, 4), compile_merger(7, 6, 5),
                compile_merger(45, 19, 2), compile_merger(19, 45, 2)]
    # The two-gap-one repair has a small accelerated edit count, but this
    # compiler counts shortcut letters. Its acceptance is tested, not assumed.
    source_path = [385]
    for _ in range(23):
        source_path.append(shortcut(source_path[-1]))
    source_tuple = tuple_from_path(source_path)
    obstruction = closed_orbit_minimum(193, 385, 76, 23)
    require(obstruction["minimum_edit_budget"] == 39, "all-clock obstruction changed")
    require(not compile_merger(193, 385, 38)["accepted"], "budget 38 unexpectedly succeeds")
    transported = transport_witness(193, 385, source_tuple, 39)
    require(transported["accepted"] and len(transported["target_path"]) == 77,
            "complete source-witness transport failed")
    padded_source = source_tuple + [source_tuple[-1] + 2, source_tuple[-1] + 4]
    padded = transport_witness(193, 385, padded_source, 39)
    require(padded["target_tuple"] == transported["target_tuple"],
            "valid input terminal padding changed the complete target witness")
    damaged = 0
    for certificate in [
        {"start": [1, 2], "edit_budget": 0, "alignment": "="},
        {"start": [3, 2], "edit_budget": 0, "alignment": "L"},
        {"start": [2, 1], "edit_budget": 1, "alignment": "LL"},
        {"start": [3, 2], "edit_budget": 4, "alignment": "LLLLR"},
    ]:
        try:
            check_certificate(certificate)
        except ValueError:
            damaged += 1
        else:
            raise ValueError("damaged certificate accepted")
    return {
        "compiler_grid_cases": cases,
        "accepted": accepted,
        "common_run_cases": common_cases,
        "damaged_certificates_rejected": damaged,
        "fixtures": fixtures,
        "input_clock_budget_obstruction": obstruction,
        "source_tuple": source_tuple,
        "transported_target_tuple": transported["target_tuple"],
        "transported_alignment": transported["certificate"]["alignment"],
        "padded_input_checked": True,
        "scope": "finite independent controls; arbitrary-budget theorem is written and formal",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("x", type=int, nargs="?")
    parser.add_argument("y", type=int, nargs="?")
    parser.add_argument("edit_budget", type=int, nargs="?")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--source-tuple", type=json.loads,
                        help="JSON full exponent tuple for y; emit a tuple for odd x")
    args = parser.parse_args()
    if args.self_test:
        result = self_test()
    else:
        require(None not in (args.x, args.y, args.edit_budget), "supply x y edit_budget")
        result = (transport_witness(args.x, args.y, args.source_tuple, args.edit_budget)
                  if args.source_tuple is not None else
                  compile_merger(args.x, args.y, args.edit_budget))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
