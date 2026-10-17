#!/usr/bin/env python3
"""Derive the connector-free coordinate and Evertse-admissibility interfaces.

The independent checker in verify.py does not import this module.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path
from typing import Any

SCHEMA = "X-9704/v2"
PR3_HEAD = "f274dfeee3c9c391c48e58d8b57cb9f1759236f8"
PR13_HEAD = "dc7f9667799f169820330e8df356ccb059636b0e"
P = (5, 30, 20, 56)
BETA = (9, 54, 36, 24)
TYPES = range(4)


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0)")
    n = abs(n)
    return (n & -n).bit_length() - 1


def v3(n: int) -> int:
    if n == 0:
        raise ValueError("v3(0)")
    n = abs(n)
    result = 0
    while n % 3 == 0:
        result += 1
        n //= 3
    return result


def scaled_connector(source: int, target: int, t: int, u: int) -> tuple[int, int]:
    h = 1 << (11 * (u + 1))
    n = 3 ** (7 * (t + 1))
    modulus = 64 * h
    x = ((h * P[target] - BETA[source]) * pow(n, -1, modulus)) % modulus
    y = (n * x + BETA[source]) // h
    assert x % 64 == P[source]
    assert y % 64 == P[target]
    assert n * x + BETA[source] == h * y
    return x, y


def local_coordinate_checks() -> int:
    """Check the signed local conjugacy on all stabilized type triples."""
    from math import gcd

    heights = (16, 32, 48)
    count = 0
    for i, j, k in product(TYPES, repeat=3):
        x0, y0 = scaled_connector(i, j, heights[0], heights[1])
        x1, _ = scaled_connector(j, k, heights[1], heights[2])
        c = (y0 - x1) // 64
        assert y0 - x1 == 64 * c
        n0 = 3 ** (7 * (heights[0] + 1))
        h0 = 1 << (11 * (heights[0] + 1))
        h1 = 1 << (11 * (heights[1] + 1))
        h2 = 1 << (11 * (heights[2] + 1))
        rho = (-c * pow(n0, -1, h2)) % h2
        for lift in (-2, -1, 0, 1):
            z0 = rho + h2 * lift
            z1, rem = divmod(n0 * z0 + c, h2)
            assert rem == 0
            zeta0 = x0 + 64 * h1 * z0
            zeta1 = x1 + 64 * h2 * z1
            assert h1 * zeta1 == n0 * zeta0 + BETA[i]
            assert zeta0 % 64 == P[i]
            assert zeta1 % 64 == P[j]

            a0 = h0 * P[i] // 64
            eta0 = (x0 - P[i]) // 64
            physical0 = a0 + h0 * (eta0 + h1 * z0) - 34
            assert 64 * (physical0 + 34) == h0 * zeta0

            a1 = h1 * P[j] // 64
            eta1 = (x1 - P[j]) // 64
            physical1 = a1 + h1 * (eta1 + h2 * z1) - 34
            assert 64 * (physical1 + 34) == h1 * zeta1
            assert BETA[i] % gcd(zeta0, zeta1) == 0

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


def stage_heights(m: int) -> list[int]:
    base = 1 << m
    delta = 1 << (m - 8)
    return [base + j * delta for j in range(257)] + [2 * base + 2 * delta]


def canonical_word() -> list[int]:
    return [((j * j + 3 * j + 1) ^ (j >> 2)) % 4 for j in range(258)]


def exponent_dictionary(m: int, word: list[int]) -> dict[str, Any]:
    if m < 12 or len(word) != 258:
        raise ValueError("need m>=12 and 258 symbols")
    t = stage_heights(m)
    base = 1 << m
    scale = 1 << (m - 9)
    a = 7 * sum(t[j] + 1 for j in range(256))
    e = 11 * sum(t[j] + 1 for j in range(1, 257))
    assert a == (5369 * base) // 2 + 1792
    assert e == (8459 * base) // 2 + 2816
    assert a == 1_374_464 * scale + 1792
    assert e == 2_165_504 * scale + 2816

    rows: list[dict[str, int]] = []
    for j in range(256):
        u = 11 * sum(t[s] + 1 for s in range(1, j + 1))
        v = 7 * sum(t[s] + 1 for s in range(j + 1, 256))
        ub = 11 * j * (j + 513)
        vb = 7 * (255 - j) * (j + 768)
        assert u == ub * scale + 11 * j
        assert v == vb * scale + 7 * (255 - j)
        rows.append(
            {
                "j": j,
                "digit": BETA[word[j]],
                "u": u,
                "v": v,
                "u_base": ub,
                "v_base": vb,
                "u_const": 11 * j,
                "v_const": 7 * (255 - j),
            }
        )
    return {"m": m, "A": a, "E": e, "scale": scale, "rows": rows}


def modular_stage_check(m: int, word: list[int], prime: int) -> dict[str, int]:
    t = stage_heights(m)
    z = (P[word[0]] + 64 * 1_234_567) % prime
    start = z
    p_prod = 1
    h_prod = 1
    offset = 0
    for j in range(256):
        n = pow(3, 7 * (t[j] + 1), prime)
        h = pow(2, 11 * (t[j + 1] + 1), prime)
        z = (n * z + BETA[word[j]]) * pow(h, -1, prime) % prime
        offset = (n * offset + h_prod * BETA[word[j]]) % prime
        p_prod = p_prod * n % prime
        h_prod = h_prod * h % prime
    assert h_prod * z % prime == (p_prod * start + offset) % prime

    closed = 0
    for j in range(256):
        hp = 1
        for r in range(j):
            hp = hp * pow(2, 11 * (t[r + 1] + 1), prime) % prime
        ns = 1
        for r in range(j + 1, 256):
            ns = ns * pow(3, 7 * (t[r] + 1), prime) % prime
        closed = (closed + BETA[word[j]] * hp * ns) % prime
    assert closed == offset
    return {"m": m, "prime": prime, "start": start, "end": z, "offset": offset}


def signed_quotient_audit() -> dict[str, int]:
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
    return {
        "tested": tested,
        "integral": integral,
        "cap_fixed": cap_fixed,
        "cocap_fixed": cocap_fixed,
    }


def evertse_interface_audit() -> dict[str, Any]:
    max_v2_b = max(v2(x) for x in BETA)
    max_v3_b = max(v3(x) for x in BETA)
    gcd_cap = (2**max_v2_b) * (3**max_v3_b)
    assert (max_v2_b, max_v3_b, gcd_cap) == (3, 3, 216)

    endpoint_num = 2166 + 4332
    endpoint_den = 346_819
    assert endpoint_num == 6498
    assert endpoint_num * 50 < endpoint_den

    separation = []
    previous_max = None
    for m in range(12, 21):
        e = (8459 * (1 << m)) // 2 + 2816
        vals = [e + v2(P[k]) - v2(BETA[i]) for i, k in product(TYPES, repeat=2)]
        if previous_max is not None:
            assert min(vals) > previous_max
        previous_max = max(vals)
        separation.append({"m": m, "min": min(vals), "max": max(vals)})

    return {
        "dimension_n": 257,
        "coordinate_count": 258,
        "max_v2_digit": max_v2_b,
        "max_v3_digit": max_v3_b,
        "primitive_gcd_cap": gcd_cap,
        "endpoint_product_ratio": [endpoint_num, endpoint_den],
        "admissibility_exponent": [1, 50],
        "strict_gap": [endpoint_den - 50 * endpoint_num, 50 * endpoint_den],
        "projective_separation": separation,
    }


def payload() -> dict[str, Any]:
    word = canonical_word()
    local_count = local_coordinate_checks()
    dicts = [exponent_dictionary(m, word) for m in (12, 13)]
    normalized = [
        (r["j"], r["digit"], r["u_base"], r["v_base"], r["u_const"], r["v_const"])
        for r in dicts[0]["rows"]
    ]
    normalized2 = [
        (r["j"], r["digit"], r["u_base"], r["v_base"], r["u_const"], r["v_const"])
        for r in dicts[1]["rows"]
    ]
    assert normalized == normalized2
    dictionary_digest = hashlib.sha256(
        json.dumps(normalized, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    result = {
        "schema": SCHEMA,
        "source_heads": {"PR3": PR3_HEAD, "PR13": PR13_HEAD},
        "stable_digits": {"p": list(P), "b": list(BETA)},
        "local_coordinate_cases": local_count,
        "physical_cofactor_cases": local_count,
        "adjacent_gcd_cases": local_count,
        "prime_turnover_cases": local_count,
        "stage_dictionary_rows": len(normalized),
        "dictionary_digest": dictionary_digest,
        "stage_exponents": [
            {"m": d["m"], "A": d["A"], "E": d["E"], "scale": d["scale"]}
            for d in dicts
        ],
        "modular_stage_checks": [
            modular_stage_check(m, word, p)
            for m in (12, 13)
            for p in (1_000_003, 1_000_033)
        ],
        "endpoint_height": {
            "limsup_log2_Z_over_2m": [1083, 41],
            "limsup_log2_Z_over_E": [2166, 346_819],
            "next_endpoint_over_current_E": [4332, 346_819],
            "less_than_one_over_160": True,
            "next_less_than_one_over_80": True,
        },
        "signed_quotient_audit": signed_quotient_audit(),
        "evertse_admissibility": evertse_interface_audit(),
    }
    encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode("utf-8")
    result["payload_digest"] = hashlib.sha256(encoded).hexdigest()
    return result


def write_summary(data: dict[str, Any], path: Path) -> None:
    lines = [
        "X-9704 connector-free power-sum summary",
        f"local coordinate cases: {data['local_coordinate_cases']}",
        f"physical cofactor cases: {data['physical_cofactor_cases']}",
        f"adjacent gcd cases: {data['adjacent_gcd_cases']}",
        f"prime turnover cases: {data['prime_turnover_cases']}",
        f"stable dictionary rows: {data['stage_dictionary_rows']}",
        f"dictionary digest: {data['dictionary_digest']}",
        f"modular stage checks: {len(data['modular_stage_checks'])}",
        "endpoint height ratio: 2166/346819 < 1/160",
        "next endpoint ratio: 4332/346819 < 1/80",
        f"signed quotient integral cases: {data['signed_quotient_audit']['integral']}",
        "primitive gcd cap: 216",
        "endpoint product ratio: 6498/346819 < 1/50",
        f"projective separation rows: {len(data['evertse_admissibility']['projective_separation'])}",
        f"payload digest: {data['payload_digest']}",
        "all derivation checks passed",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--summary", type=Path)
    args = parser.parse_args()
    data = payload()
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    if args.summary:
        args.summary.parent.mkdir(parents=True, exist_ok=True)
        write_summary(data, args.summary)
    print("all derivation checks passed")


if __name__ == "__main__":
    main()
