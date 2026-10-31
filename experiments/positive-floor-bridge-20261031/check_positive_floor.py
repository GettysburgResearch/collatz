#!/usr/bin/env python3
"""Exact bounded checks for the positive-floor bridge.

This tests identities and finite killed models, not the external infinite-state
uniform-floor premise, any infinite limit, or the Collatz conjecture. Checks
remain active with Python -O. Standard library only.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path

OLD = Path(__file__).resolve().parents[1] / "beeping-density-swarm-20261031" / "check_inverse_green.py"
SPEC = importlib.util.spec_from_file_location("recovered_inverse_green", OLD)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Cannot load the pinned inverse-law helper")
old = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(old)


def require(ok: bool, detail: object) -> None:
    if not ok:
        raise RuntimeError(str(detail))


def first_and_dead_profiles() -> dict:
    rows, checks = [], 0
    for t in range(1, 1002, 2):
        if t % 3 == 0:
            first = dead = F(0)
            a0 = None
        else:
            parity = 2 if t % 3 == 1 else 1
            first = F(3, 1 << parity) / (1 - F(1, 4))
            a0 = next(a for a in range(1, 7) if ((1 << a) * t - 1) % 9 == 0)
            dead = F(3, 1 << a0) / (1 - F(1, 64))
        expected = 0 if t % 3 == 0 else 1 if t % 3 == 1 else 2
        require(first == expected, ("exact rho1", t))
        require(dead >= first / 21, ("dead-leaf lower bound", t))
        require(dead <= first, ("dead subset", t))
        checks += 3
        if t < 19:
            rows.append({"t": t, "rho1": str(first), "Ld": str(dead), "a0": a0})
    require(any(F(r["Ld"]) == F(r["rho1"]) / 21 and F(r["rho1"]) > 0 for r in rows),
            "constant 1/21 is attained")
    return {"targets": 501, "checks": checks, "residue_examples": rows,
            "tails": "Infinite geometric exponent tails summed exactly"}


def synchronized_frontiers(laws) -> dict:
    checks = words = 0
    strict = 0
    for t in range(1, 52, 2):
        for n in range(7):
            for depth in range(min(n, 4) + 1):
                leaves = old.frontier(t, threshold=4 * t + 1, D=depth, max_letter=6)
                require(old.prefix_free(w for _, w, _ in leaves), ("prefix-free", t, n, depth))
                lhs = sum((weight * old.density(laws, n - len(word), x)
                           for x, word, weight in leaves), F(0))
                rhs = old.density(laws, n, t)
                require(lhs <= rhs, ("fixed total clock", t, n, depth, lhs, rhs))
                strict += int(lhs < rhs)
                words += len(leaves)
                checks += 1
    # Prefix overlap produces double counting even on the ordinary fixed point.
    overlap = old.density(laws, 2, 1) + F(3, 4) * old.density(laws, 1, 1)
    require(overlap > old.density(laws, 2, 1), "overlap negative control")
    return {"frontiers": checks, "leaf_evaluations": words, "strict_inequalities": strict,
            "max_total_clock": 6, "max_inverse_letter": 6,
            "overlap_control": {"root": 1, "words": [[], [2]], "lhs": str(overlap),
                                "rho2": str(old.density(laws, 2, 1))}}


def finite_operator(f: dict[int, F], bound: int) -> dict[int, F]:
    out = {t: F(0) for t in range(1, bound + 1, 2)}
    for x, value in f.items():
        y, a = old.odd_step(x)
        if y in out:
            out[y] += F(3, 1 << a) * value
    return out


def finite_green(bound: int, z: F) -> dict[int, F]:
    """Sum all paths exactly, including geometric cycle renewal; no time cutoff."""
    out = {t: F(0) for t in range(1, bound + 1, 2)}
    for start in out:
        seen: dict[int, int] = {}
        path, products = [], []
        x, product = start, F(1)
        while x in out and x not in seen:
            seen[x] = len(path)
            path.append(x)
            products.append(product)
            y, a = old.odd_step(x)
            product *= z * F(3, 1 << a)
            x = y
        cycle_start = seen.get(x, len(path))
        multiplier = product / products[cycle_start] if cycle_start < len(path) else F(0)
        require(multiplier < 1, ("finite cycle multiplier", bound, start, z))
        for j, t in enumerate(path):
            out[t] += products[j] if j < cycle_start else products[j] / (1 - multiplier)
    return out


def children(t: int, bound: int):
    a = 1
    while (1 << a) * t - 1 <= 3 * bound:
        numerator = (1 << a) * t - 1
        if numerator % 3 == 0:
            yield numerator // 3, a, F(3, 1 << a)
        a += 1


def model_frontier(t: int, bound: int, depth: int):
    stack = [(t, (), F(1))]
    output = []
    while stack:
        x, word, weight = stack.pop()
        kids = list(children(x, bound))
        stop = (len(word) == depth or not kids or
                (len(word) > 0 and (x + sum(word)) % 5 == 0))
        if stop:
            output.append((x, word, weight))
        else:
            for y, a, factor in kids:
                stack.append((y, word + (a,), weight * factor))
    return output


def finite_model_checks() -> dict:
    records = []
    total = 0
    for bound in (31, 63, 127):
        h = finite_green(bound, F(1))
        lh = finite_operator(h, bound)
        require(all(lh[t] == h[t] - 1 for t in h), ("Green resolvent", bound))
        require(all(v >= 1 for v in h.values()), ("finite-model floor", bound))
        rho = [{t: F(1) for t in h}]
        for q in range(1, 33):
            rho.append(finite_operator(rho[-1], bound))
            for t in h:
                require(rho[q][t] <= 2 * h[t], ("prescribed depth", bound, q, t))
                total += 1
        fcount = leaves_count = 0
        for t in h:
            for depth in range(1, 7):
                leaves = model_frontier(t, bound, depth)
                require(old.prefix_free(word for _, word, _ in leaves), "model prefix-free")
                charge = sum((weight * h[x] for x, _, weight in leaves), F(0))
                mixed = sum((weight * rho[1 + ((x + sum(word)) % 32)][x]
                             for x, word, weight in leaves), F(0))
                require(charge <= h[t], ("optional frontier budget", bound, t, depth))
                require(mixed <= 2 * h[t], ("arbitrary positive leaf clocks", bound, t, depth))
                fcount += 1
                leaves_count += len(leaves)
                total += 2
        tail_checks = 0
        for z in (F(1, 2), F(3, 4), F(7, 8), F(15, 16)):
            az = {t: (1 - z) * value for t, value in finite_green(bound, z).items()}
            laz = finite_operator(az, bound)
            for t in h:
                require(az[t] <= 1 - z + 2 * z * h[t], ("Abel bound", bound, z, t))
                require(laz[t] == az[t] / z - (1-z) / z,
                        ("Abel resolvent", bound, z, t))
                for m in range(9):
                    tail = sum((weight * az[x] for x, a, weight in children(t, bound) if a > m), F(0))
                    htail = sum((weight * h[x] for x, a, weight in children(t, bound) if a > m), F(0))
                    require(tail <= F(3, 1 << m) + 2 * htail,
                            ("uniform inverse-tail bound", bound, z, t, m))
                    tail_checks += 1
                total += 2
        records.append({"height_cutoff": bound, "states": len(h), "frontiers": fcount,
                        "leaf_evaluations": leaves_count, "inverse_tail_checks": tail_checks,
                        "h_at_1": str(h[1]), "h_status": "Exact finite killed Green function, not the infinite canonical trace"})
        total += tail_checks
    return {"models": records, "inequality_and_resolvent_checks": total,
            "rho_depths": 32, "floor_alpha": "1 (finite models only)"}


def zero_clock_control(laws) -> dict:
    require(all(old.density(laws, q, 3) == 0 for q in range(1, len(laws))), "dead root")
    require(old.density(laws, 0, 3) == 1, "zero clock equals one")
    return {"root": 3, "rho0": "1", "positive_depths": "0",
            "normalized_Abel_limit": "0, exactly since a_z(3)=1-z",
            "conclusion": "Cannot remove q(w)>=1 from the uniform-floor theorem"}


def run() -> dict:
    laws = old.exact_laws(6)
    return {"status": "PASS", "schema": 1,
            "scope": "Exact finite identities and finite killed models; no external floor, all-depth limit, or Collatz proof verified",
            "helper_sha256": hashlib.sha256(OLD.read_bytes()).hexdigest(),
            "first_and_dead_profiles": first_and_dead_profiles(),
            "synchronized_frontiers": synchronized_frontiers(laws),
            "finite_models": finite_model_checks(),
            "zero_clock_control": zero_clock_control(laws)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "output": str(args.output),
                      "finite_model_checks": result["finite_models"]["inequality_and_resolvent_checks"]}))


if __name__ == "__main__":
    main()
