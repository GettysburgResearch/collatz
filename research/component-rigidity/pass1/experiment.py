#!/usr/bin/env python3
"""Exact bounded experiments for the arithmetic component-rigidity packet.

No third-party packages.  This is NOT a Collatz solver or an empirical
convergence-rate study.  Finite colorings retain every boundary component.
All quantitative certificates use integers and fractions, not floating logs.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import random
import sys


def check(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)


def positive_int(n: int) -> None:
    if type(n) is not int or n < 1:
        raise ValueError("expected a positive integer (not a boolean)")


def step(n: int, multiplier: int = 3) -> int:
    positive_int(n)
    if type(multiplier) is not int or multiplier < 3 or multiplier % 2 != 1:
        raise ValueError("multiplier must be an odd integer >= 3")
    return (multiplier * n + 1) // 2 if n % 2 else n // 2


def iterate(n: int, length: int, multiplier: int = 3) -> int:
    if type(length) is not int or length < 0:
        raise ValueError("length must be a nonnegative integer")
    for _ in range(length):
        n = step(n, multiplier)
    return n


def inverse_step(y: int) -> tuple[int, int]:
    """A growing ternary-unit odd predecessor, together with its T-clock."""
    positive_int(y)
    if y < 2 or y % 3 == 0:
        raise ValueError("inverse ladder requires a ternary unit >= 2")
    choices = (2, 4) if y % 3 == 1 else (3, 5)
    for k in choices:
        numerator = (1 << k) * y - 1
        check(numerator % 3 == 0, "inverse branch integrality")
        z = numerator // 3
        if z % 3:
            return z, k
    raise ValueError("no legal inverse branch: mathematical invariant broken")


def component_seed(n: int) -> tuple[int, dict]:
    """A unit >=2 in the ORIGINAL component, with an explicit finite link."""
    positive_int(n)
    if n == 1:
        return 5, {"direction": "seed_to_source", "clock": 4}
    if n % 3:
        return n, {"direction": "source_to_seed", "clock": 0}
    y, clock = n, 0
    while y % 2 == 0:
        y //= 2
        clock += 1
    y = step(y)
    return y, {"direction": "source_to_seed", "clock": clock + 1}


def inverse_ladder(n: int, length: int) -> dict:
    positive_int(n)
    if type(length) is not int or length < 0:
        raise ValueError("length must be nonnegative")
    y, link = component_seed(n)
    nodes, clocks = [y], []
    for _ in range(length):
        y, k = inverse_step(y)
        nodes.append(y)
        clocks.append(k)
    return {"source": n, "seed_link": link, "nodes": nodes, "clocks": clocks}


def verify_ladder(row: dict) -> None:
    """Replay raw parities without calling the inverse-branch generator."""
    source, nodes, clocks = row["source"], row["nodes"], row["clocks"]
    positive_int(source)
    check(len(nodes) == len(clocks) + 1, "ladder inventory")
    for y in nodes:
        positive_int(y)
        check(y >= 2 and y % 3 != 0, "unit node")
    direction = row["seed_link"]["direction"]
    clock = row["seed_link"]["clock"]
    if direction == "source_to_seed":
        check(iterate(source, clock) == nodes[0], "original source link")
    elif direction == "seed_to_source":
        check(iterate(nodes[0], clock) == source, "original inverse link")
    else:
        raise ValueError("unknown source link")
    check(nodes[0] <= 5 * source, "seed height bound")
    for y, z, k in zip(nodes, nodes[1:], clocks):
        check(type(k) is int and k in (2, 3, 4, 5), "clock range")
        check(3 * z + 1 == (1 << k) * y, "inverse identity")
        check(4 * z >= 5 * y and 3 * z <= 32 * y, "growth envelope")
        x = z
        for i in range(k):
            check(x % 2 == (1 if i == 0 else 0), "physical parity word")
            # Independent literal update, not iterate/inverse_step.
            x = (3 * x + 1) // 2 if x % 2 else x // 2
        check(x == y, "physical endpoint")


def mantissa(n: int) -> Fraction:
    positive_int(n)
    return Fraction(n, 1 << (n.bit_length() - 1))


def circular_ratio(nodes: list[int]) -> Fraction:
    """Largest multiplicative gap on R_(>0)/2^Z, exactly."""
    points = sorted(set(mantissa(n) for n in nodes))
    check(bool(points), "empty net")
    gaps = [b / a for a, b in zip(points, points[1:])]
    gaps.append(2 * points[0] / points[-1])
    return max(gaps)


def hit_relative_window(nodes: list[int], x: int, ratio: Fraction) -> dict:
    """Use a finite exact net and only DOUBLING to enter [x, ratio*x]."""
    positive_int(x)
    check(x >= max(nodes), "window below finite-net height")
    check(ratio > 1 and circular_ratio(nodes) < ratio, "insufficient net")
    for j, y in enumerate(nodes):
        t = max(0, x.bit_length() - y.bit_length())
        z = y << t
        if z < x:
            t += 1
            z <<= 1
        if z * ratio.denominator <= x * ratio.numerator:
            return {"index": j, "doublings": t, "root": z, "left": x}
    raise ValueError("net did not hit window")


class DSU:
    def __init__(self, h: int):
        self.parent = list(range(h + 1))
    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parent[max(x, y)] = min(x, y)


def finite_components(h: int, multiplier: int = 3) -> tuple[list[int], list[int]]:
    positive_int(h)
    dsu = DSU(h)
    ports = []
    for n in range(1, h + 1):
        y = step(n, multiplier)
        if y <= h:
            dsu.union(n, y)
        else:
            ports.append(n)
    return [0] + [dsu.find(n) for n in range(1, h + 1)], ports


def finite_invariance(b: list[int]) -> bool:
    h = len(b) - 1
    return all(b[n] == b[step(n)] for n in range(1, h + 1) if step(n) <= h)


def finite_current_laws(b: list[int]) -> bool:
    """All current laws whose entire support lies in 1..H, plus d_1=0."""
    h = len(b) - 1
    if h < 2:
        return True
    d = [0] + [b[n + 1] - b[n] for n in range(1, h)]
    if d[1] != 0:
        return False
    for n in range(1, (h - 2) // 2 + 1):
        if d[n] != d[2*n] + d[2*n+1]:
            return False
    for n in range(0, (h - 5) // 3 + 1):
        if d[2*n+1] + d[2*n+2] != d[3*n+2] + d[3*n+3] + d[3*n+4]:
            return False
    return True


def shell_statistics(b: list[int]) -> list[dict]:
    h = len(b) - 1
    d = [0] + [b[n + 1] - b[n] for n in range(1, h)]
    rows = []
    k = 0
    while (1 << (k + 2)) <= h:
        lo, hi = 1 << k, 1 << (k + 1)
        v = sum(abs(d[n]) for n in range(lo, hi))
        v_next = sum(abs(d[n]) for n in range(2 * lo, 2 * hi))
        births = sum(d[n] == 0 and d[2*n] != 0 for n in range(lo, hi))
        check(v_next == v + 2 * births, "wall-birth conservation")
        rows.append({"k": k, "variation": v, "next_variation": v_next, "births": births})
        k += 1
    return rows


def verify_cycle(cycle: list[int], multiplier: int) -> None:
    check(len(set(cycle)) == len(cycle), "nonprimitive cycle list")
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        check(step(a, multiplier) == b, "incorrect cycle edge")


def run() -> dict:
    digest = hashlib.sha256()
    def retain(obj: object) -> None:
        digest.update(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    summary: dict = {"status": "BOUNDED EXACT CHECKS ONLY", "map": "T(n)=n/2 even; (3n+1)/2 odd"}

    # Exhaust ALL Boolean assignments b(1)=0, not just valid colorings.
    exhaustive, valid_total, by_h = 0, 0, []
    for h in range(1, 19):
        valid = 0
        components, ports = finite_components(h)
        count_components = len(set(components[1:]))
        for bits in itertools.product((0, 1), repeat=h - 1):
            b = [0, 0] + list(bits)
            invariant = finite_invariance(b)
            check(invariant == finite_current_laws(b), "finite converse failure")
            exhaustive += 1
            if invariant:
                valid += 1
                shell_statistics(b)
        check(valid == (1 << (count_components - 1)), "all-boundary component count")
        row = {"height": h, "components": count_components, "ports": len(ports), "valid_colorings": valid}
        by_h.append(row)
        retain(row)
        valid_total += valid
    summary["exhaustive_boolean_assignments"] = exhaustive
    summary["exhaustive_valid_colorings"] = valid_total
    summary["finite_current_equivalence"] = by_h

    # Larger local colorings: every exterior component kept, never wired to 1.
    rng = random.Random(20260925)
    random_rows, nonzero_rows, shell_checks = 0, 0, 0
    profile = []
    for h in (64, 256, 1024, 4096, 16384):
        comps, ports = finite_components(h)
        roots = sorted(set(comps[1:]))
        root1 = comps[1]
        local = []
        for trial in range(32):
            colors = {r: rng.randrange(2) for r in roots}
            colors[root1] = 0
            b = [0] + [colors[comps[n]] for n in range(1, h + 1)]
            check(finite_invariance(b) and finite_current_laws(b), "local coloring invalid")
            stats = shell_statistics(b)
            random_rows += 1
            nonzero_rows += any(b)
            shell_checks += len(stats)
            local.append(stats[-1]["next_variation"] if stats else 0)
            retain({"h": h, "trial": trial, "colors": sorted(colors.items()), "shells": stats})
        profile.append({"height": h, "components": len(roots), "unwired_ports": len(ports),
                        "last_shell_variation_min": min(local), "last_shell_variation_max": max(local)})
    summary["sampled_local_colorings"] = random_rows
    summary["nonzero_sampled_local_colorings"] = nonzero_rows
    summary["sampled_birth_identity_checks"] = shell_checks
    summary["finite_boundary_profile"] = profile

    # Literal integer predecessor certificates for every source in a grid.
    ladders, edges = 0, 0
    for n in range(1, 4097):
        row = inverse_ladder(n, 96)
        verify_ladder(row)
        retain(row)
        ladders += 1
        edges += len(row["clocks"])
    summary["verified_ladders"] = ladders
    summary["literal_inverse_edges"] = edges

    # Finite nets certify ALL sufficiently high windows, not density guesses.
    net_examples, hit_checks = [], 0
    for n in (1, 27, 121, 303, 1311, 2**127 - 1):
        row = inverse_ladder(n, 512)
        verify_ladder(row)
        nodes = row["nodes"]
        gap = circular_ratio(nodes)
        ratio = Fraction(101, 100)
        check(gap < ratio, "512-step exact net needs larger horizon")
        largest = max(nodes)
        roots_checked = []
        for j in range(16):
            x = largest * (17 + j) // 16 + j * j
            hit = hit_relative_window(nodes, x, ratio)
            index, t, z = hit["index"], hit["doublings"], hit["root"]
            check(z == nodes[index] << t, "net lift identity")
            # Every link is already checked; explicitly replay this complete arm.
            check(iterate(z, t + sum(row["clocks"][:index])) == nodes[0], "net endpoint")
            roots_checked.append(hit)
            hit_checks += 1
        item = {"source": n, "nodes": len(nodes), "largest_root_bits": largest.bit_length(),
                "max_circular_ratio": [gap.numerator, gap.denominator],
                "certified_ratio": [101, 100], "threshold": largest,
                "sampled_windows": roots_checked}
        net_examples.append(item)
        retain(item)
    summary["exact_relative_window_nets"] = net_examples
    summary["literal_window_checks"] = hit_checks

    # A negative control for topology/irrationality-alone arguments.
    cycles = [[1, 3, 8, 4, 2], [13, 33, 83, 208, 104, 52, 26], [17, 43, 108, 54, 27, 68, 34]]
    for cycle in cycles:
        verify_cycle(cycle, 5)
    check(all(not (set(a) & set(b)) for i, a in enumerate(cycles) for b in cycles[i+1:]), "cycles intersect")
    comps, _ = finite_components(512, 5)
    check(len({comps[c[0]] for c in cycles}) == 3, "control components collapsed")
    summary["five_x_plus_one_disjoint_cycles"] = cycles
    retain(cycles)

    # Rejection controls. Not a separately authored verifier or formal proof.
    rejected = 0
    bad_ladder = inverse_ladder(27, 12)
    bad_ladder["nodes"][7] += 2
    try:
        verify_ladder(bad_ladder)
    except ValueError:
        rejected += 1
    bad_clock = inverse_ladder(27, 12)
    bad_clock["clocks"][3] += 1
    try:
        verify_ladder(bad_clock)
    except ValueError:
        rejected += 1
    for bad in (True, 0, -3, 6):
        try:
            inverse_step(bad)
        except ValueError:
            rejected += 1
    bad_cycle = [13, 33, 83, 208, 104, 52, 25]
    try:
        verify_cycle(bad_cycle, 5)
    except ValueError:
        rejected += 1
    check(rejected == 7, "negative controls")
    summary["rejected_direct_controls"] = rejected
    summary["semantic_sha256"] = digest.hexdigest()
    summary["scope_limits"] = [
        "Finite colorings are not asserted to extend to infinite colorings.",
        "No global Collatz convergence, natural-density or separator-regularity estimate is proved by these tests.",
        "Equidistribution is a manuscript theorem, not an extrapolation from histograms.",
        "Finite circular-gap nets certify all sufficiently high relative windows for their displayed component by doubling.",
        "No complete repository validator, remote CI, Lean build or independent mathematical review was run.",
        "Verifier diversity inside this file is same-author checking, not peer review."
    ]
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results.json"))
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    compact = {k: result[k] for k in ("exhaustive_boolean_assignments", "exhaustive_valid_colorings", "sampled_local_colorings", "literal_inverse_edges", "literal_window_checks", "rejected_direct_controls", "semantic_sha256")}
    print(json.dumps(compact, indent=2))

if __name__ == "__main__":
    main()
