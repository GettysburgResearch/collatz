#!/usr/bin/env python3
"""Exact bounded checks for harmonic transport and spectral constructions.

The all-input and infinite-dimensional claims rest on the companion proof.
This program never decides Collatz or an infinite spectral problem.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def step(x: int) -> tuple[int, int]:
    require(x > 0 and x % 2 == 1, "positive odd source required")
    y = 3*x+1
    a = (y & -y).bit_length()-1
    return y >> a, a


def c(x: int) -> F:
    return F(3*x, 3*x+1)


def apply(v: dict[int, F], core: frozenset[int]) -> dict[int, F]:
    out: dict[int, F] = {}
    for x, value in v.items():
        require(x not in core, "vector is outside the killed-space domain")
        y, _ = step(x)
        if y not in core:
            out[y] = out.get(y, F(0))+c(x)*value
    return {x: a for x, a in out.items() if a}


def norm(v: dict[int, F]) -> F:
    return sum(map(abs, v.values()), F(0))


def residual(v: dict[int, F], lam: F, core: frozenset[int]) -> dict[int, F]:
    out = apply(v, core)
    for x, a in v.items():
        out[x] = out.get(x, F(0))-lam*a
    return {x: a for x, a in out.items() if a}


def inverse_ray(seed_exponent: int, length: int) -> list[int]:
    require(seed_exponent >= 4 and seed_exponent % 6 == 4, "seed exponent class")
    x = (2**seed_exponent-1)//3
    require(x % 3 != 0 and step(x)[0] == 1, "unit first predecessor of one")
    ray = [x]
    for _ in range(length-1):
        candidates = []
        for a in range(3, 10):
            numerator = 2**a*x-1
            if numerator % 3:
                continue
            y = numerator//3
            if y % 3 and y > 2*x:
                candidates.append((a, y))
        require(bool(candidates), "no growing unit inverse found")
        a, y = candidates[0]
        require(step(y) == (x, a), "exact inverse valuation")
        ray.append(y)
        x = y
    return ray


def ray_coefficients(ray: list[int], lam: F, sign: int) -> dict[int, F]:
    product = F(1)
    power = F(1)
    out = {}
    for x in ray:
        product *= c(x)
        out[x] = sign*power/product
        power *= lam
    return {x: a for x, a in out.items() if a}


def checks() -> dict:
    require(8*3125**24 < 3456**24, "inherited rho exponent inequality")
    require(F(27, 32) < F(3125, 3456), "high-lane decay is smaller")
    require(F(56, 81) > F(2, 3), "log two lower enclosure")
    require(100*F(56, 81) > F(200, 3), "rational first-hit gap")

    cores = [frozenset(), frozenset({1}), frozenset({1, 3, 5, 7}),
             frozenset({3, 7, 101})]
    transport_cases = 0
    for core in cores:
        for bound in (31, 101, 301):
            v = {x: F((x % 11)+1, x+2)
                 for x in range(1, bound+1, 2) if x not in core}
            out = apply(v, core)
            leakage = F(0)
            for x, a in v.items():
                y, _ = step(x)
                leakage += a if y in core else a/(3*x+1)
            require(norm(v)-norm(out) == leakage, "exact harmonic leakage")
            require(norm(out) < norm(v), "strict loss for nonzero source")
            transport_cases += 1

    circle_cases = 0
    finite_norm_rows = []
    for core in cores:
        for length in (1, 2, 5, 16, 64):
            for odd_b in (103, 1001, 65537):
                ns = [3**j*2**(length+1-j)*odd_b-1 for j in range(length+1)]
                require(min(ns) > max(core, default=0), "all-one segment avoids core")
                require(len(set(ns)) == len(ns), "all-one segment distinct")
                product = F(1)
                for j in range(length):
                    require(step(ns[j]) == (ns[j+1], 1), "all-one valuation")
                    product *= c(ns[j])
                expected = F(ns[0], 1)/(ns[0]+1-F(2, 3)**length)
                require(product == expected, "telescoped power norm")
                require(product >= 1-F(length, 3*ns[0]+1), "power norm lower bound")
                for lam in (F(1), F(-1)):
                    vector = {ns[j]: lam**(-j)/length for j in range(length)}
                    require(norm(vector) == 1, "circle vector normalized")
                    require(norm(residual(vector, lam, core)) <=
                            F(2, length)+F(1, 3*ns[0]+1), "circle residual bound")
                    circle_cases += 1
                if core == frozenset() and odd_b == 65537:
                    finite_norm_rows.append({"length": length,
                                             "source": ns[0],
                                             "power_norm": str(product)})

    rays = [inverse_ray(16+6*j, 14) for j in range(6)]
    require(len(set(x for ray in rays for x in ray)) == 84, "disjoint inverse rays")
    eigenvector_cases = 0
    for core in cores:
        for lam in (F(0), F(1, 2), F(-1, 2), F(3, 4), F(7, 8)):
            for length in (1, 3, 8, 14):
                for r in (0, 2, 4):
                    first, second = rays[r][:length], rays[r+1][:length]
                    vector = ray_coefficients(first, lam, 1)
                    vector.update(ray_coefficients(second, lam, -1))
                    got = residual(vector, lam, core)
                    expected = {}
                    for ray, sign in ((first, 1), (second, -1)):
                        product = F(1)
                        for x in ray:
                            product *= c(x)
                        value = -sign*lam**length/product
                        if value:
                            expected[ray[-1]] = value
                    require(got == expected, "truncated eigenvector boundary residual")
                    require(1 not in got, "root incoming flux cancellation")
                    eigenvector_cases += 1

    first_hit_checks = 0
    minimum_product = F(1)
    max_odd_steps = 0
    for source in range(1, 2048, 2):
        path = []
        value = source
        weight = F(1)
        product = F(1)
        seen = set()
        while value not in seen:
            require(len(path) < 1000, "bounded source replay exceeded clock")
            seen.add(value)
            path.append(value)
            require(weight/F(value) == product/F(source), "first-hit product identity")
            require(product > F(1, 2**100), "first-hit distortion gap")
            first_hit_checks += 1
            minimum_product = min(minimum_product, product)
            next_value, a = step(value)
            weight *= F(3, 2**a)
            product *= c(value)
            value = next_value
        require(value == 1, "unexpected finite-cycle outcome in bounded replay")
        max_odd_steps = max(max_odd_steps, len(path)-1)

    periodic = F(1)
    for q in range(1, 65):
        periodic *= c(1)
        require(periodic == F(3, 4)**q, "periodic harmonic mass")

    return {
        "schema": "harmonic-spectrum-bounded-replay/v1",
        "status": "PASS",
        "scope": "exact finite identities and construction interfaces; no infinite-spectrum computation, reachability oracle, external formal replay, or Collatz proof",
        "transport_cases": transport_cases,
        "circle_residual_cases": circle_cases,
        "interior_eigenvector_truncations": eigenvector_cases,
        "disjoint_inverse_rays": len(rays),
        "inverse_ray_length": len(rays[0]),
        "first_hit_product_checks": first_hit_checks,
        "odd_source_limit": 2047,
        "largest_observed_odd_clock": max_odd_steps,
        "minimum_observed_simple_product": str(minimum_product),
        "periodic_mass_checks": 64,
        "finite_power_norm_examples": finite_norm_rows,
        "open_escape_problem_decided": False,
        "uniform_green_computability_proved": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = checks()
    semantic = hashlib.sha256(json.dumps(report, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    report["semantic_sha256_before_hash_field"] = semantic
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "semantic_sha256": semantic,
                      "transport_cases": report["transport_cases"],
                      "circle_residual_cases": report["circle_residual_cases"],
                      "interior_eigenvector_truncations": report["interior_eigenvector_truncations"],
                      "first_hit_product_checks": report["first_hit_product_checks"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
