#!/usr/bin/env python3
"""Exact conditional R bypasses, with an explicitly bounded optional search.

R(m) means E(27m) => E(9m), for positive odd m.  A certificate joins
9m to 27m by ordinary equivalences and directed y -> 3y moves with
9 | y and 0 < y < 9m.  These directed moves invoke only smaller R.
The default verifies retained infinite cells; it does not claim a cover.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import heapq
import itertools
import json
from math import gcd, lcm
from pathlib import Path
from typing import Callable, Optional


F = Fraction
HERE = Path(__file__).resolve().parent


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def v2(n: int) -> int:
    require(integer(n) and n > 0, "v2 requires a positive integer")
    return (n & -n).bit_length() - 1


@dataclass(frozen=True)
class Witness:
    x: int
    increments: tuple[int, ...]

    def __post_init__(self) -> None:
        require(integer(self.x) and self.x > 0 and self.x % 2 == 1,
                "witness source must be a positive odd integer")
        require(isinstance(self.increments, tuple), "increments must be a tuple")
        n = self.x
        for a in self.increments:
            require(integer(a) and a > 0, "increments must be positive integers")
            require(v2(3 * n + 1) == a, "increment is not the exact odd-step exponent")
            n = (3 * n + 1) // 2**a
        require(n == 1, "witness does not finish at one")

    @property
    def cumulative(self) -> tuple[int, ...]:
        out = [0]
        for a in self.increments:
            out.append(out[-1] + a)
        return tuple(out)

    def pad(self, count: int) -> "Witness":
        require(integer(count) and count >= 0, "invalid padding count")
        return Witness(self.x, self.increments + (2,) * count)


def from_trajectory(x: int, limit: int = 10000) -> Witness:
    """Bounded fixture helper.  The certificate transformer never calls it."""
    require(integer(x) and x > 0 and x % 2 == 1, "invalid fixture source")
    require(integer(limit) and limit >= 0, "invalid fixture limit")
    n, word = x, []
    for _ in range(limit):
        if n == 1:
            return Witness(x, tuple(word))
        a = v2(3 * n + 1)
        word.append(a)
        n = (3 * n + 1) // 2**a
    if n == 1:
        return Witness(x, tuple(word))
    raise ValueError("fixture trajectory exceeded its explicit bound")


def op_form(form: tuple[Fraction, Fraction], op: str, a: int) -> tuple[Fraction, Fraction]:
    A, B = form
    if op == "U":
        return 3 * A / 2**a, (3 * B + 1) / 2**a
    if op == "I":
        return 2**a * A / 3, (2**a * B - 1) / 3
    if op == "J":
        return 4 * A, 4 * B + 1
    if op == "K":
        return A / 4, (B - 1) / 4
    if op == "M":
        return 3 * A, 3 * B
    if op == "V":
        return A / 3, B / 3
    raise ValueError("unknown operation")


def check_form(form: tuple[Fraction, Fraction], u0: int) -> None:
    A, B = form
    require(A.denominator == B.denominator == 1, "nonintegral affine coefficients")
    require(A > 0 and A % 2 == 0 and B % 2 == 1, "affine form is not always odd")
    require(A * u0 + B > 0, "affine form is not always positive")


def check_word(word: object, side: str) -> list[tuple[str, int]]:
    require(isinstance(word, list), "path must be a list")
    out = []
    legal = {"U", "I", "J", "K", "M" if side == "target" else "V"}
    for pair in word:
        require(isinstance(pair, (list, tuple)) and len(pair) == 2, "invalid operation pair")
        op, a = pair
        require(op in legal and integer(a) and a > 0, "invalid path operation")
        require(op in ("U", "I") or a == (3 if op in ("M", "V") else 1),
                "unexpected fixed-operation argument")
        out.append((op, a))
    return out


def verify_cell(cell: dict) -> dict:
    """Check identities and every guard for every integer in the infinite cell."""
    require(isinstance(cell, dict), "certificate must be an object")
    M, r, lower = cell.get("modulus"), cell.get("residue"), cell.get("minimum_m")
    require(integer(M) and M > 0 and M % 2 == 0, "invalid cell modulus")
    require(integer(r) and 0 <= r < M and r % 2 == 1, "invalid cell residue")
    require(integer(lower) and lower >= 1, "invalid cell threshold")
    u0 = max(0, (lower - r + M - 1) // M)
    endpoints, calls, forms = [], [], []
    for side, factor in (("target", 9), ("source", 27)):
        word = check_word(cell.get(side + "_path"), side)
        form = F(factor * M), F(factor * r)
        check_form(form, u0)
        intermediate = [form]
        for op, a in word:
            if op in ("M", "V"):
                y = form if op == "M" else (form[0] / 3, form[1] / 3)
                check_form(y, u0)
                require(y[0] % 9 == y[1] % 9 == 0, "conditional move is not at a multiple of nine")
                dA, dB = 9 * M - y[0], 9 * r - y[1]
                require(dA >= 0 and dA * u0 + dB > 0, "conditional move is not strictly below 9m")
                calls.append({"side": side, "parameter_in_u": [str(y[0] / 9), str(y[1] / 9)]})
            form = op_form(form, op, a)
            # Input and output oddness makes each U exponent exact; it also
            # enforces every inverse division and J inverse domain.
            check_form(form, u0)
            intermediate.append(form)
        endpoints.append(form)
        forms.append(intermediate)
    require(endpoints[0] == endpoints[1], "paths do not have the same affine endpoint")
    if "meeting" in cell:
        proposed = tuple(F(x) for x in cell["meeting"])
        require(len(proposed) == 2, "invalid advertised endpoint")
        require(endpoints[0] == (proposed[0] * M, proposed[0] * r + proposed[1]),
                "advertised endpoint is false")
    return {"id": cell.get("id", "anonymous"), "modulus": M, "residue": r,
            "first_m": M * u0 + r, "conditional_calls": len(calls),
            "calls": calls, "affine_forms_checked": sum(map(len, forms))}


def witness_move(w: Witness, op: str, a: int) -> Witness:
    if op == "U":
        if not w.increments:
            require(w.x == 1 and a == 2, "empty witness cannot follow this forward step")
            return w
        require(w.increments[0] == a, "forward exponent disagrees with supplied witness")
        return Witness((3 * w.x + 1) // 2**a, w.increments[1:])
    if op == "I":
        numerator = 2**a * w.x - 1
        require(numerator % 3 == 0, "nonintegral inverse witness move")
        return Witness(numerator // 3, (a,) + w.increments)
    if op == "J":
        word = w.increments or (2,)
        return Witness(4 * w.x + 1, (word[0] + 2,) + word[1:])
    if op == "K":
        require(w.x % 8 == 5 and w.increments and w.increments[0] >= 3,
                "illegal inverse J witness move")
        return Witness((w.x - 1) // 4, (w.increments[0] - 2,) + w.increments[1:])
    raise ValueError("not an ordinary witness move")


def transform(source: Witness, cell: dict,
              child_solver: Optional[Callable[[Witness], Optional[Witness]]] = None) -> dict:
    """Construct a target witness, or stop at an explicit smaller R obligation.

    A child solver receives a validated witness for 27p and must return one
    for 9p.  No target trajectory search occurs here.  A missing or false
    child never counts as a successful transformation.
    """
    verify_cell(cell)
    require(isinstance(source, Witness), "a validated source witness is required")
    require(source.x % 27 == 0, "source is not 27m")
    m = source.x // 27
    require(m % cell["modulus"] == cell["residue"] and m >= cell["minimum_m"],
            "source is outside the certified cell")
    inverse = {"U": "I", "I": "U", "J": "K", "K": "J", "M": "V"}
    path = check_word(cell["source_path"], "source")
    path += [(inverse[op], a) for op, a in reversed(check_word(cell["target_path"], "target"))]
    current, used = source, 0
    for op, a in path:
        if op == "V":
            require(current.x % 27 == 0, "recursive source is not 27p")
            p = current.x // 27
            require(0 < p < m and p % 2 == 1, "recursive parameter does not strictly decrease")
            if child_solver is None:
                return {"status": "UNRESOLVED", "parameter": m, "child_parameter": p,
                        "child_source": current, "completed_child_calls": used}
            child = child_solver(current)
            if child is None:
                return {"status": "UNRESOLVED", "parameter": m, "child_parameter": p,
                        "child_source": current, "completed_child_calls": used}
            require(isinstance(child, Witness) and child.x == 9 * p, "child solver returned the wrong witness")
            current, used = child, used + 1
        else:
            current = witness_move(current, op, a)
    require(current.x == 9 * m, "reconstruction finished at the wrong target")
    return {"status": "PROVED_FROM_CHILDREN", "witness": current, "child_calls": used}


def ladder_cell(k: int) -> dict:
    """Generate RB-004's cell for any k >= 3, without a bounded-k selector."""
    require(integer(k) and k >= 3, "ladder index must be at least three")
    modulus = 2 ** (2 * k + 4)
    residue = ((1 + 3 * 2 ** (2 * k + 1) * pow(3 ** (k - 3), -1, modulus))
               * pow(27, -1, modulus)) % modulus
    cell = {"id": "RB-ladder-" + str(k), "modulus": modulus, "residue": residue,
            "minimum_m": 1,
            "target_path": [["U", 1]] + [["U", 2]] * (k - 1) + [["K", 1], ["M", 3]],
            "source_path": [["U", 2]] * k + [["U", 1], ["K", 1], ["I", 2]],
            "meeting": [str(F(27 * 3**k, 2 ** (2 * k + 1))),
                        str(F(-3**k, 2 ** (2 * k + 1)))]}
    verify_cell(cell)
    return cell


def verify_ladder_generators() -> dict:
    """Exact affine identities used by the unbounded induction in RB-004."""
    def D(form: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return form[0] / 2, (form[1] + 1) / 2

    variable = F(1), F(0)
    require(op_form(D(variable), "U", 2) == D(op_form(variable, "U", 2)),
            "F2-D commutation failed")
    require(op_form((F(1, 3), F(0)), "U", 1) == D(variable), "initial F1 identity failed")
    source = F(72), F(1)
    target = D(source)
    for op, a in (("U", 2), ("U", 1), ("K", 1), ("I", 2)):
        source = op_form(source, op, a)
    for op, a in (("K", 1), ("M", 3)):
        target = op_form(target, op, a)
    require(source == target == (F(27), F(0)), "ladder terminal identities failed")
    # The parity/positivity guard is the entire p=8u+3 cylinder, not samples.
    terminal = F(72 * 8), F(72 * 3 + 1)
    check_form(terminal, 0)
    for op, a in (("U", 2), ("U", 1), ("K", 1), ("I", 2)):
        terminal = op_form(terminal, op, a)
        check_form(terminal, 0)
    require(terminal == (F(27 * 8), F(27 * 3)), "ladder parameter guard failed")
    return {"generator_identities": "PASS", "all_k_induction": "proved in R_BYPASS.md RB-004"}


def discover(seed: int, budget: int = 2000, inverse_max: int = 8,
             slope_cap: int = 10000) -> Optional[dict]:
    """A bounded search.  Its failures say nothing about unbounded existence."""
    require(integer(seed) and seed > 0 and seed % 2 == 1, "seed must be positive odd")
    require(integer(budget) and budget > 0, "budget must be positive")
    starts = [(F(9), F(0)), (F(27), F(0))]
    seen = [{starts[0]: (None, None)}, {starts[1]: (None, None)}]
    heaps, serial = [[], []], itertools.count()
    for side in (0, 1):
        heapq.heappush(heaps[side], (0, next(serial), starts[side], 0))

    def path(side: int, state: tuple[Fraction, Fraction]) -> list[list]:
        out = []
        while seen[side][state][0] is not None:
            previous, move = seen[side][state]
            out.append(list(move))
            state = previous
        return out[::-1]

    def make_cell(meeting: tuple[Fraction, Fraction]) -> dict:
        words = [path(0, meeting), path(1, meeting)]
        modulus, lower = 2, 1
        for factor, word in zip((9, 27), words):
            form = F(factor), F(0)
            for op, a in word:
                if op in ("M", "V"):
                    yA, yB = form if op == "M" else (form[0] / 3, form[1] / 3)
                    d = lcm(yA.denominator, yB.denominator)
                    modulus = lcm(modulus, 9 * d // gcd(int(yA * d), 9 * d))
                    lower = max(lower, int(yB // (9 - yA)) + 1)
                form = op_form(form, op, a)
                A, B = form
                lower = max(lower, int((-B) // A) + 1)
                d = lcm(A.denominator, B.denominator)
                modulus = lcm(modulus, 2 * d // gcd(int(A * d), 2 * d))
        cell = {"id": "RB-seed-" + str(seed), "modulus": modulus,
                "residue": seed % modulus, "minimum_m": lower,
                "target_path": words[0], "source_path": words[1],
                "meeting": [str(x) for x in meeting]}
        verify_cell(cell)
        return cell

    for turn in range(2 * budget):
        side = turn % 2
        if not heaps[side]:
            continue
        _, _, state, depth = heapq.heappop(heaps[side])
        A, B = state
        value = A * seed + B
        require(value.denominator == 1 and value > 0 and value.numerator % 2 == 1,
                "internal search state is not a positive odd integer")
        n, a = int(value), v2(3 * int(value) + 1)
        edges = [("U", a), ("J", 1)]
        if n > 1 and n % 8 == 5:
            edges.append(("K", 1))
        if n % 3:
            edges += [("I", j) for j in range(1, inverse_max + 1) if (2**j * n - 1) % 3 == 0]
        if side == 0 and n % 9 == 0 and A < 9:
            edges.append(("M", 3))
        if side == 1 and n % 27 == 0 and A / 3 < 9:
            edges.append(("V", 3))
        for op, exponent in edges:
            new = op_form(state, op, exponent)
            C, D = new
            if C <= 0 or C > slope_cap or abs(D) > slope_cap * seed or new in seen[side]:
                continue
            new_value = C * seed + D
            if new_value <= 0 or new_value.denominator != 1 or new_value.numerator % 2 != 1:
                continue
            seen[side][new] = state, (op, exponent)
            if new in seen[1 - side]:
                return make_cell(new)
            score = (depth + 1 + max(0, C.numerator.bit_length() - C.denominator.bit_length() - 5) / 3
                     + (C.denominator.bit_length() + D.denominator.bit_length()) / 40)
            heapq.heappush(heaps[side], (score, next(serial), new, depth + 1))
    return None


def adaptive_search(attempts: int, budget: int, max_modulus: int) -> dict:
    """Partition by exact cells, retaining every unprocessed cell explicitly."""
    require(attempts > 0 and max_modulus >= 2, "invalid adaptive limits")
    queue = [(2, 1)]
    certified, deferred, base_exceptions = [], [], []
    cache = {}
    completed = 0
    while queue and completed < attempts:
        M, r = heapq.heappop(queue)
        if M > max_modulus:
            deferred.append((M, r))
            continue
        if r not in cache:
            cache[r] = discover(r, budget)
        cell = cache[r]
        completed += 1
        if cell is None:
            heapq.heappush(queue, (2 * M, r))
            heapq.heappush(queue, (2 * M, r + M))
            continue
        combined = lcm(M, cell["modulus"])
        chosen = r % combined
        current_M, current_r = M, r
        while current_M < combined:
            ratio = combined // current_M
            factor = 2 if ratio % 2 == 0 else 3
            require(ratio % factor == 0, "unexpected modulus prime")
            next_M = factor * current_M
            desired = chosen % next_M
            for j in range(factor):
                sibling = current_r + j * current_M
                if sibling != desired:
                    heapq.heappush(queue, (next_M, sibling))
            current_M, current_r = next_M, desired
        cell = dict(cell, modulus=combined, residue=chosen,
                    id="RB-cell-" + str(combined) + "-" + str(chosen))
        verify_cell(cell)
        # These excluded individual m are recorded, never silently counted as covered.
        for m in range(chosen, cell["minimum_m"], combined):
            if m > 0:
                base_exceptions.append(m)
        certified.append(cell)
    unresolved = sorted(queue + deferred)
    density = sum((F(2, c["modulus"]) for c in certified), F(0))
    require(density + sum((F(2, M) for M, _ in unresolved), F(0)) == 1,
            "adaptive partition lost or duplicated mass")
    return {"schema": "R-bypass-v1", "status": "PROPOSED", "full_cover": not unresolved and not base_exceptions,
            "search_limits": {"attempts": attempts, "node_pops_per_side": budget,
                              "max_attempted_modulus": max_modulus},
            "processed_cells": completed, "completed_distinct_seed_searches": len(cache), "cells": certified,
            "covered_relative_density": str(density),
            "unresolved_cells": [[M, r] for M, r in unresolved],
            "excluded_base_parameters": sorted(set(base_exceptions))}


def verify_partition(packet: dict) -> dict:
    """Audit the finite exhaustive partition into certified and OPEN cells."""
    cells = packet.get("cells")
    require(isinstance(cells, list), "partition has no certificate list")
    unresolved = packet.get("unresolved_cells")
    require(isinstance(unresolved, list), "partition omits its unresolved cells")
    classes = [(c["modulus"], c["residue"]) for c in cells]
    for item in unresolved:
        require(isinstance(item, list) and len(item) == 2, "invalid unresolved cell")
        M, r = item
        require(integer(M) and M > 0 and M % 2 == 0 and integer(r)
                and 0 <= r < M and r % 2 == 1, "invalid unresolved residue class")
        classes.append((M, r))
    for i, (M, r) in enumerate(classes):
        for N, s in classes[:i]:
            require((r - s) % gcd(M, N) != 0, "partition cells overlap")
    density = sum((F(2, c["modulus"]) for c in cells), F(0))
    require(density == F(packet.get("covered_relative_density", "-1")), "wrong covered density")
    require(sum((F(2, M) for M, _ in classes), F(0)) == 1, "partition is not exhaustive")
    excluded = set()
    for c in cells:
        excluded.update(m for m in range(c["residue"], c["minimum_m"], c["modulus"]) if m > 0)
    require(packet.get("excluded_base_parameters") == sorted(excluded), "wrong finite base exceptions")
    require(packet.get("full_cover") == (not unresolved and not excluded), "wrong cover status")
    return {"certified_cells": len(cells), "unresolved_cells": len(unresolved),
            "covered_relative_density": str(density), "exhaustive_partition": True,
            "excluded_base_parameters": len(excluded)}


def self_test(packet: dict) -> dict:
    cells = packet.get("cells")
    require(isinstance(cells, list) and bool(cells), "packet has no retained certificates")
    summaries = [verify_cell(c) for c in cells]
    partition = verify_partition(packet)
    fixtures = padded = missing = 0
    for cell, summary in zip(cells, summaries):
        for lift in (0, 1):
            m = summary["first_m"] + lift * cell["modulus"]
            source = from_trajectory(27 * m)
            for padding in (0, 2):
                result = transform(source.pad(padding), cell,
                                   lambda w: from_trajectory(w.x // 3).pad(1))
                require(result["status"] == "PROVED_FROM_CHILDREN", "fixture reconstruction failed")
                require(result["witness"].x == 9 * m, "fixture target mismatch")
                fixtures += 1
                padded += bool(padding)
            absent = transform(source, cell)
            if summary["conditional_calls"]:
                require(absent["status"] == "UNRESOLVED", "missing child was treated as success")
                missing += 1
    bad = 0
    import copy
    controls = []
    c = copy.deepcopy(cells[0]); c["meeting"] = ["0", "1"]; controls.append(c)
    c = copy.deepcopy(cells[0]); c["residue"] += 1; controls.append(c)
    c = copy.deepcopy(cells[0]); c["source_path"].append(["J", 1]); controls.append(c)
    c = copy.deepcopy(cells[0]); c["minimum_m"] = 0; controls.append(c)
    controls.append({"modulus": 2, "residue": 1, "minimum_m": 1,
                     "target_path": [["M", 3]], "source_path": []})
    controls.append({"modulus": 2, "residue": 1, "minimum_m": 1,
                     "target_path": [["V", 3]], "source_path": []})
    for c in controls:
        try:
            verify_cell(c)
        except ValueError:
            bad += 1
        else:
            raise ValueError("altered certificate was accepted")
    partition_controls = []
    p = copy.deepcopy(packet); p["unresolved_cells"].pop(); partition_controls.append(p)
    p = copy.deepcopy(packet); p["unresolved_cells"].append(p["unresolved_cells"][0]); partition_controls.append(p)
    p = copy.deepcopy(packet); p["covered_relative_density"] = "1"; partition_controls.append(p)
    for p in partition_controls:
        try:
            verify_partition(p)
        except ValueError:
            bad += 1
        else:
            raise ValueError("altered coverage partition was accepted")
    for source, increments in ((3, (2,)), (1, (0,)), (1, (True,)), (5, (2,)), (True, ())):
        try:
            Witness(source, increments)
        except ValueError:
            bad += 1
        else:
            raise ValueError("malformed witness was accepted")
    conditional = next((c for c, s in zip(cells, summaries) if s["conditional_calls"]), None)
    if conditional is not None:
        m = verify_cell(conditional)["first_m"]
        try:
            transform(from_trajectory(27 * m), conditional, lambda _: Witness(1, ()))
        except ValueError:
            bad += 1
        else:
            raise ValueError("wrong child witness was accepted")
    ladder_schema = verify_ladder_generators()
    ladder_fixtures = 0
    for k in (3, 4, 5, 8):
        cell = ladder_cell(k)
        m = verify_cell(cell)["first_m"]
        source = from_trajectory(27 * m).pad(2)
        p = 3 ** (k - 3) * (27 * m - 1) // 2 ** (2 * k + 1)
        pending = transform(source, cell)
        require(pending["status"] == "UNRESOLVED" and pending["child_parameter"] == p,
                "ladder stopped at the wrong obligation")
        child_source = pending["child_source"]
        require(len(child_source.increments) == len(source.increments) - k
                and sum(child_source.increments) == sum(source.increments) - 2 * k - 1,
                "ladder input witness statistics failed")
        child_target = from_trajectory(9 * p).pad(2)
        result = transform(source, cell, lambda _: child_target)
        target = result["witness"]
        require(len(target.increments) == len(child_target.increments) + k
                and sum(target.increments) == sum(child_target.increments) + 2 * k + 1,
                "ladder output witness statistics failed")
        ladder_fixtures += 1
    return {"status": "PASS", "universal_affine_cells": len(cells),
            "affine_forms_checked": sum(s["affine_forms_checked"] for s in summaries),
            "conditional_calls_in_certificate_words": sum(s["conditional_calls"] for s in summaries),
            "fixture_reconstructions": fixtures, "nonminimal_source_fixture_reconstructions": padded,
            "missing_child_returns_unresolved": missing, "invalid_controls_rejected": bad,
            "partition": partition,
            "unbounded_ladder": ladder_schema, "additional_ladder_fixture_reconstructions": ladder_fixtures,
            "full_R_theorem": "OPEN", "complete_cover": False,
            "evidence_limit": "Exact infinite-cell identities and bounded fixture reconstruction only."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, default=HERE / "r-bypass-certificate.json")
    parser.add_argument("--seed", type=int, help="run one bounded exploratory search instead of replay")
    parser.add_argument("--adaptive", type=int, help="maximum number of adaptive cell searches")
    parser.add_argument("--budget", type=int, default=2000)
    parser.add_argument("--max-modulus", type=int, default=4096)
    args = parser.parse_args()
    require(not (args.seed is not None and args.adaptive is not None), "choose one search mode")
    if args.seed is not None:
        result = discover(args.seed, args.budget)
        print(json.dumps(result or {"status": "UNRESOLVED", "seed": args.seed}, indent=2))
    elif args.adaptive is not None:
        print(json.dumps(adaptive_search(args.adaptive, args.budget, args.max_modulus), indent=2))
    else:
        print(json.dumps(self_test(json.loads(args.certificate.read_text(encoding="utf-8"))), sort_keys=True))


if __name__ == "__main__":
    main()
