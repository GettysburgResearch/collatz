#!/usr/bin/env python3
"""Independent replay for X-9704.

This file does not import derive.py. It reconstructs the stabilized tower
constants from the original recovery congruences and independently rechecks the
connector, exponent, signed-quotient, and Evertse-admissibility gates.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from math import gcd
from pathlib import Path

SPECS = (
    (5, 5, 5, 2),
    (6, 4, 4, 3),
    (7, 3, 5, 2),
    (8, 2, 6, 1),
)
EXPECTED_P = (5, 30, 20, 56)
EXPECTED_B = (9, 54, 36, 24)


def valuation_two(n: int) -> int:
    n = abs(n)
    return (n & -n).bit_length() - 1


def valuation_three(n: int) -> int:
    n = abs(n)
    result = 0
    while n % 3 == 0:
        result += 1
        n //= 3
    return result


def reconstruct_constants(t: int = 16) -> tuple[tuple[int, ...], tuple[int, ...]]:
    ps: list[int] = []
    bs: list[int] = []
    universal_h = 1 << (11 * (t + 1))
    universal_n = 3 ** (7 * (t + 1))
    for k0, r, g0, rec_b in SPECS:
        modulus = 1 << (r + 1)
        g = g0 + 7 * t
        candidates = [
            mu
            for mu in range(1, modulus, 2)
            if (pow(3, g, modulus) * mu + 1) % modulus == 0
        ]
        assert len(candidates) == 1
        mu = candidates[0]
        a = (1 << (k0 + 11 * t)) * mu
        core = (3**g * mu + 1) // modulus
        tower_b = 3**rec_b * core
        ps.append(64 * a // universal_h)
        bs.append(64 * tower_b - universal_n * ps[-1])
    assert tuple(ps) == EXPECTED_P
    assert tuple(bs) == EXPECTED_B
    return tuple(ps), tuple(bs)


def connector(
    ps: tuple[int, ...],
    bs: tuple[int, ...],
    source: int,
    target: int,
    t: int,
    u: int,
) -> tuple[int, int]:
    n = 3 ** (7 * (t + 1))
    h = 1 << (11 * (u + 1))
    modulus = 64 * h
    x = ((h * ps[target] - bs[source]) * pow(n, -1, modulus)) % modulus
    assert x % 64 == ps[source]
    y, rem = divmod(n * x + bs[source], h)
    assert rem == 0 and y % 64 == ps[target]
    return x, y


def independent_local(ps: tuple[int, ...], bs: tuple[int, ...]) -> int:
    heights = (16, 32, 48)
    count = 0
    for i, j, k in product(range(4), repeat=3):
        x0, y0 = connector(ps, bs, i, j, heights[0], heights[1])
        x1, _ = connector(ps, bs, j, k, heights[1], heights[2])
        c = (y0 - x1) // 64
        n = 3 ** (7 * (heights[0] + 1))
        h0 = 1 << (11 * (heights[0] + 1))
        h1 = 1 << (11 * (heights[1] + 1))
        h2 = 1 << (11 * (heights[2] + 1))
        rho = (-c * pow(n, -1, h2)) % h2
        for q in (-2, -1, 0, 2):
            z = rho + h2 * q
            z_next = (n * z + c) // h2
            zeta0 = x0 + 64 * h1 * z
            zeta1 = x1 + 64 * h2 * z_next
            assert h1 * zeta1 == n * zeta0 + bs[i]

            a0 = h0 * ps[i] // 64
            eta0 = (x0 - ps[i]) // 64
            phase0 = a0 + h0 * (eta0 + h1 * z) - 34
            assert 64 * (phase0 + 34) == h0 * zeta0

            a1 = h1 * ps[j] // 64
            eta1 = (x1 - ps[j]) // 64
            phase1 = a1 + h1 * (eta1 + h2 * z_next) - 34
            assert 64 * (phase1 + 34) == h1 * zeta1
            assert bs[i] % gcd(zeta0, zeta1) == 0

            for value in (zeta0, zeta1):
                if value <= 0:
                    continue
                core = value
                while core % 2 == 0:
                    core //= 2
                while core % 3 == 0:
                    core //= 3
                assert core > 1
            count += 1
    return count


def word() -> list[int]:
    return [((j * j + 3 * j + 1) ^ (j >> 2)) % 4 for j in range(258)]


def independent_dictionary(
    m: int, bs: tuple[int, ...]
) -> tuple[list[tuple[int, ...]], int, int, int]:
    base = 1 << m
    delta = 1 << (m - 8)
    t = [base + j * delta for j in range(257)]
    scale = 1 << (m - 9)
    w = word()
    rows: list[tuple[int, ...]] = []
    for j in range(256):
        u = sum(11 * (t[s] + 1) for s in range(1, j + 1))
        v = sum(7 * (t[s] + 1) for s in range(j + 1, 256))
        ub = 11 * j * (j + 513)
        vb = 7 * (255 - j) * (j + 768)
        assert u == ub * scale + 11 * j
        assert v == vb * scale + 7 * (255 - j)
        rows.append((j, bs[w[j]], ub, vb, 11 * j, 7 * (255 - j)))
    a = sum(7 * (t[s] + 1) for s in range(256))
    e = sum(11 * (t[s] + 1) for s in range(1, 257))
    return rows, a, e, scale


def verify_payload(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    ps, bs = reconstruct_constants()
    assert data["stable_digits"] == {"p": list(ps), "b": list(bs)}

    local_cases = independent_local(ps, bs)
    for key in (
        "local_coordinate_cases",
        "physical_cofactor_cases",
        "adjacent_gcd_cases",
        "prime_turnover_cases",
    ):
        assert data[key] == local_cases

    rows12, a12, e12, s12 = independent_dictionary(12, bs)
    rows13, a13, e13, s13 = independent_dictionary(13, bs)
    assert rows12 == rows13
    digest = hashlib.sha256(
        json.dumps(rows12, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    assert digest == data["dictionary_digest"]
    assert data["stage_exponents"] == [
        {"m": 12, "A": a12, "E": e12, "scale": s12},
        {"m": 13, "A": a13, "E": e13, "scale": s13},
    ]

    evertse = data["evertse_admissibility"]
    assert evertse["dimension_n"] == 257
    assert evertse["coordinate_count"] == 258
    assert max(valuation_two(x) for x in bs) == 3
    assert max(valuation_three(x) for x in bs) == 3
    assert evertse["primitive_gcd_cap"] == 216
    assert evertse["endpoint_product_ratio"] == [6498, 346819]
    assert evertse["admissibility_exponent"] == [1, 50]
    assert 6498 * 50 < 346819

    expected = []
    previous_max = None
    for m in range(12, 21):
        e = 8459 * (1 << m) // 2 + 2816
        values = [
            e + valuation_two(ps[k]) - valuation_two(bs[i])
            for i, k in product(range(4), repeat=2)
        ]
        if previous_max is not None:
            assert min(values) > previous_max
        previous_max = max(values)
        expected.append({"m": m, "min": min(values), "max": max(values)})
    assert expected == evertse["projective_separation"]

    tested = integral = cap_fixed = cocap_fixed = 0
    for p_odd in (3, 5, 9, 15):
        for q_next in (64, 128, 256):
            if 4 * p_odd >= q_next:
                continue
            for cap in range(p_odd):
                for corr in range(q_next):
                    for y in range(-24, 25):
                        tested += 1
                        y_next, rem = divmod(cap + p_odd * y - corr, q_next)
                        if rem:
                            continue
                        integral += 1
                        if y >= 0:
                            assert y_next >= 0 and y_next < (y + 1) / 4
                            if y == 0:
                                assert y_next == 0
                                cap_fixed += 1
                        else:
                            k = -y - 1
                            k_next = -y_next - 1
                            assert y_next <= -1
                            assert k_next >= 0 and k_next < (k + 1) / 4
                            if k == 0:
                                assert k_next == 0
                                cocap_fixed += 1
    assert data["signed_quotient_audit"] == {
        "tested": tested,
        "integral": integral,
        "cap_fixed": cap_fixed,
        "cocap_fixed": cocap_fixed,
    }

    ratio = data["endpoint_height"]
    assert ratio["limsup_log2_Z_over_2m"] == [1083, 41]
    assert ratio["limsup_log2_Z_over_E"] == [2166, 346819]
    assert ratio["next_endpoint_over_current_E"] == [4332, 346819]

    clone = dict(data)
    claimed = clone.pop("payload_digest")
    encoded = json.dumps(clone, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    assert hashlib.sha256(encoded).hexdigest() == claimed

    return {
        "reconstructed_types": len(ps),
        "independent_local_cases": local_cases,
        "physical_cofactor_cases": data["physical_cofactor_cases"],
        "adjacent_gcd_cases": data["adjacent_gcd_cases"],
        "prime_turnover_cases": data["prime_turnover_cases"],
        "independent_dictionary_rows": len(rows12),
        "projective_separation_rows": len(expected),
        "signed_quotient_integral_cases": integral,
        "primitive_gcd_cap": 216,
        "payload_digest": claimed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-results", required=True, type=Path)
    args = parser.parse_args()
    report = verify_payload(args.check_results)
    print(json.dumps(report, indent=2, sort_keys=True))
    print("all independent connector-free checks passed")


if __name__ == "__main__":
    main()
