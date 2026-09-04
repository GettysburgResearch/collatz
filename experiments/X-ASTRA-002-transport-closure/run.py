#!/usr/bin/env python3
"""Exact finite witnesses for T-ASTRA-011 and its Green-history corollary.

No asymptotic inference is made by this program. Infinite even-ray remainders
are enclosed by the proved geometric tail. Only the standard library is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

F = Fraction
PRECISION = 512
SCALE = 1 << PRECISION
CAPS = (1, 4, 8)
HEIGHTS = (16, 32, 64)
HISTORY_DEPTHS = (2, 4, 6)
LAMBDA = F(65, 64)
A_RAY = F(3, 2)
Atom = tuple[int, int, Fraction]


def valuation3(n: int) -> int:
    if n == 0:
        raise ValueError("valuation at zero is excluded")
    n = abs(n)
    r = 0
    while n % 3 == 0:
        n //= 3
        r += 1
    return r


def step(n: int) -> int:
    if n < 1:
        raise ValueError("positive ordinary integer required")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def w0(n: int) -> Fraction:
    if n < 2:
        raise ValueError("killed domain starts at 2")
    return F(3 ** valuation3(n + 1), (n + 1) ** 2)


def affine_word(length: int, code: int) -> tuple[int, int]:
    q = constant = 0
    for i in range(length):
        if (code >> i) & 1:
            constant = 3 * constant + (1 << i)
            q += 1
    return q, constant


def history_atoms(depth: int) -> list[Atom]:
    return [(1 << k, 3 ** q - c, LAMBDA ** k * 3 ** q)
            for k in range(depth + 1)
            for code in range(1 << k)
            for q, c in [affine_word(k, code)]]


def cases() -> list[tuple[str, list[Atom], int]]:
    out = [
        ("base", [(1, 1, F(1))], 0),
        ("displaced_repair", [(1, 1, F(1)), (8, -1, F(1)), (16, -5, F(1))], 0),
        ("mixed_centres", [(1, 1, F(1)), (1, -1, F(2)), (2, 1, F(3, 2)), (5, -7, F(1, 3))], 0),
        ("zero_centre", [(1, 0, F(1))], 0),
    ]
    out += [(f"green_depth_{d}", history_atoms(d), d) for d in HISTORY_DEPTHS]
    return out


def in_ray_set(z: Fraction, atoms: list[Atom]) -> bool:
    for A, B, _ in atoms:
        p = F(-B, A)
        if z == 0:
            if p == 0:
                return True
        else:
            t = p / z
            if t.denominator == 1 and t.numerator > 0:
                m = t.numerator
                if m & (m - 1) == 0:
                    return True
    return False


def choose_centre(atoms: list[Atom], cap: int, depth: int) -> tuple[int, Fraction, Fraction]:
    # The lower atom is the first entry. For Green cases it is the physical w0
    # summand, not an assumption that the unguarded dictionary is physical.
    A, B, _ = atoms[0]
    for j in range(max(cap - 1, depth), 10000):
        r = F(-B, A * (1 << j))
        z = (3 * r + 1) / 2
        if not in_ray_set(z, atoms):
            return j, r, z
    raise RuntimeError("centre search exceeded safety budget; no certificate")


def crt_source(A: int, B: int, j: int, h: int) -> int:
    mod = 3 ** h
    r = (-B * pow(A * (1 << j), -1, mod)) % mod
    return r + ((1 - r) % 2) * mod + 2 * mod


def upper_ray_integer(y: int, atoms: list[Atom], terms: int) -> int:
    # Return U with the entire infinite majorant ray <= U / 2**PRECISION.
    if y < 2 + 2 * max(abs(B) for _, B, _ in atoms):
        raise ValueError("endpoint is not beyond the proved affine tail threshold")
    total = 0
    p2 = p3 = 1
    for _ in range(terms):
        for A, B, c in atoms:
            m = A * p2 * y + B
            num = SCALE * c.numerator * p3 * 3 ** valuation3(m)
            den = c.denominator * p2 * m * m
            total += (num + den - 1) // den
        p2 *= 2
        p3 *= 3
    ctail = sum((F(2) * c / A for A, _, c in atoms), F())
    tail = ctail * F(3, 4) ** terms / (y * F(1, 4))
    total += (SCALE * tail.numerator + tail.denominator - 1) // tail.denominator
    return total


def pair(q: Fraction) -> list[int]:
    return [q.numerator, q.denominator]


def witnesses() -> list[dict[str, Any]]:
    out = []
    for name, atoms, depth in cases():
        A, B, c = atoms[0]
        for cap in CAPS:
            j, r, z = choose_centre(atoms, cap, depth)
            for h in HEIGHTS:
                u = crt_source(A, B, j, h)
                y = step(u)
                assert u % 2 == 1 and 2 * 3**h <= u < 4 * 3**h
                m = A * (1 << j) * u + B
                v = valuation3(m)
                assert v >= h
                terms = 4 * h + 64
                upper = upper_ray_integer(y, atoms, terms)
                lower = A_RAY ** (j - cap + 1) * c * F(3**v, m*m)
                # All ell <= cap reach the same endpoint through real trajectories.
                for ell in range(1, cap + 1):
                    x = (1 << (ell - 1)) * u
                    for t in range(ell):
                        assert x > 1
                        assert x % 2 == int(t == ell - 1)
                        x = step(x)
                    assert x == y
                row = {
                    "case": name, "formal_atoms": len(atoms),
                    "distinct_centres": len({F(-B1, A1) for A1, B1, _ in atoms}),
                    "cap": cap, "h": h, "ray_index": j,
                    "source_centre": pair(r), "endpoint_centre": pair(z),
                    "u": u, "endpoint": y, "source_valuation": v,
                    "ray_terms": terms, "upper_scaled": upper,
                    "common_lower": pair(lower),
                    "certified_common_ratio_floor": (lower.numerator * SCALE) // (lower.denominator * upper),
                }
                if depth:
                    # One actual deeper path, not the unguarded majorant.
                    M = j + 1
                    assert M > depth
                    deeper = LAMBDA ** M * w0((1 << j) * u)
                    row.update({"deeper_history": M,
                                "deeper_ratio_floor": (deeper.numerator * SCALE) // (deeper.denominator * upper)})
                out.append(row)
    return out


def inverse_layers(y: int, depth: int) -> set[int]:
    layer = {y}
    for _ in range(depth):
        new = set()
        for endpoint in layer:
            new.add(2 * endpoint)
            if endpoint % 3 == 2 and endpoint >= 5:
                new.add((2 * endpoint - 1) // 3)
        layer = new
    return layer


def guarded_compile(y: int, k: int) -> tuple[set[int], Fraction]:
    sources = set()
    value = F()
    for code in range(1 << k):
        q, A = affine_word(k, code)
        numerator = (1 << k) * y - A
        if numerator % (3**q):
            continue
        n = numerator // (3**q)
        if n < 2:
            continue
        x = n
        legal = True
        for i in range(k):
            if x < 2 or x % 2 != ((code >> i) & 1):
                legal = False
                break
            x = step(x)
        if not legal or x != y or x < 2:
            continue
        m = (1 << k) * y + 3**q - A
        term = F(3**(q + valuation3(m)), m*m)
        assert term == w0(n)
        assert n not in sources
        sources.add(n)
        value += term
    return sources, value


def compiler_checks() -> dict[str, int]:
    comparisons = sources_count = 0
    for y in range(2, 129):
        for k in range(7):
            direct = inverse_layers(y, k)
            compiled, value = guarded_compile(y, k)
            assert direct == compiled
            assert value == sum((w0(n) for n in direct), F())
            comparisons += 1
            sources_count += len(direct)
    return {"endpoint_depth_comparisons": comparisons,
            "guarded_source_terms": sources_count, "max_endpoint": 128, "max_depth": 6}


def qualitative_checks() -> dict[str, int]:
    # Finite terminating systems test T-ASTRA-009's algebra. Their finite
    # supports do not certify positivity for every positive Collatz source.
    systems = [({n: max(1, n-1) for n in range(2, 25)}, F(1, 2)),
               ({n: n//2 for n in range(2, 25)}, F(2, 3)),
               ({n: 1 + (n*n + 1) % (n-1) for n in range(2, 25)}, F(3, 4))]
    for mapping, rho in systems:
        c: dict[int, Fraction] = {}
        potential: dict[int, Fraction] = {}
        for n in mapping:
            path = []
            x = n
            while x != 1:
                path.append(x)
                x = mapping[x]
                assert len(path) <= len(mapping)
            c[n] = F(1, 2**n) * rho**len(path)
            for k, x in enumerate(path):
                potential[x] = potential.get(x, F()) + rho**(-k) * c[n]
        for y in mapping:
            Lvalue = sum((potential[n] for n in mapping if mapping[n] == y), F())
            assert Lvalue == rho * (potential[y] - c[y])
            assert potential[y] > 0 and Lvalue < rho * potential[y]
        assert sum(potential.values(), F()) <= rho / (2 * (1-rho))
    return {"finite_terminating_systems": len(systems), "states_per_system": 23}


def make_payload() -> dict[str, Any]:
    rows = witnesses()
    assert len(rows) == 63
    assert all(r["certified_common_ratio_floor"] >= 1 for r in rows)
    return {"schema": "X-ASTRA-002/v1", "precision_bits": PRECISION,
            "scope": {"finite_witness_rows": True, "infinite_ray_tail_enclosed": True,
                      "all_parameter_theorem_by_computation": False, "collatz_proved": False,
                      "uniform_green_bound_proved": False},
            "parameters": {"caps": list(CAPS), "heights": list(HEIGHTS),
                           "history_depths": list(HISTORY_DEPTHS),
                           "a": pair(A_RAY), "lambda": pair(LAMBDA)},
            "witnesses": rows, "compiler": compiler_checks(),
            "qualitative_identity": qualitative_checks()}


def canonical_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    payload = make_payload()
    report = {"payload": payload,
              "sha256": hashlib.sha256(canonical_bytes(payload)).hexdigest()}
    if args.check:
        given = json.loads(args.check.read_text())
        if given != report:
            raise SystemExit("FAIL: report differs from full deterministic replay")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, sort_keys=True, separators=(",", ":")) + "\n")
    print("PASS", report["sha256"])
    print("witness_rows", len(payload["witnesses"]), "physical_block_paths",
          sum(r["cap"] for r in payload["witnesses"]))
    print("min_common_ratio_floor", min(r["certified_common_ratio_floor"] for r in payload["witnesses"]))
    print("compiler", payload["compiler"])


if __name__ == "__main__":
    main()
