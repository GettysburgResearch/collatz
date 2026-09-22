#!/usr/bin/env python3
"""Independent verifier for X-9614.

This implementation does not import run.py.  It reconstructs word cylinders by
iteratively lifting exact source residues, rather than by the closed affine
constant formula used by the generator.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path

LOCAL = {
    "A": {"q": 8, "domain": 7},
    "B": {"q": 16, "domain": 0},
}


def all_words(depth: int):
    return ["".join(bits) for bits in product("AB", repeat=depth)]


def cylinder(word: str) -> tuple[int, int, int, int]:
    """Return source,Q,output mod 9^d,9^d by exact cylinder lifting."""
    source = 0
    q_total = 1
    output_at_source = 0
    p_total = 1

    # Empty word sends source+t to output=t. After a prefix, every input is
    # source+q_total*t and its output is output_at_source+p_total*t.
    for letter in word:
        q_letter = LOCAL[letter]["q"]
        domain = LOCAL[letter]["domain"]
        lift = ((domain - output_at_source) * pow(p_total, -1, q_letter)) % q_letter
        source += q_total * lift
        output_at_source += p_total * lift

        numerator = 9 * output_at_source + (1 if letter == "A" else 0)
        assert numerator % q_letter == 0
        output_at_source = numerator // q_letter

        q_total *= q_letter
        p_total *= 9

    assert 0 <= source < q_total
    output = output_at_source % p_total
    return source, q_total, output, p_total


def egcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def crt_positive(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    g, x, _ = egcd(m, n)
    assert g == 1
    t = ((b - a) * x) % n
    value = a + m * t
    modulus = m * n
    return (value if value else modulus), modulus


def recompute_floor(depth: int):
    words = all_words(depth)
    data = {word: cylinder(word) for word in words}
    digest = hashlib.sha256()
    best = None
    count = 0
    for suffix in words:
        _, _, output, p = data[suffix]
        for prefix in words:
            source, q, _, _ = data[prefix]
            central, modulus = crt_positive(output, p, source, q)
            digest.update(
                f"{depth}|{suffix}|{prefix}|{output}|{p}|{source}|{q}|"
                f"{central}|{modulus}\n".encode()
            )
            candidate = {
                "central": central,
                "suffix": suffix,
                "prefix": prefix,
                "output_residue": output,
                "output_modulus": p,
                "source_residue": source,
                "source_modulus": q,
                "crt_modulus": modulus,
            }
            if best is None or central < best["central"]:
                best = candidate
            count += 1
    return best, count, digest.hexdigest()


def is_contracting(a: int, b: int) -> bool:
    return 9 ** (a + b) < (1 << (3 * a + 4 * b))


def b_min(a: int) -> int:
    b = 1
    while not is_contracting(a, b):
        b += 1
    return b


def exact_margin(a: int, b: int, h: int) -> int:
    q = 1 << (3 * a + 4 * b)
    p = 9 ** (a + b)
    emax = (1 << (4 * b)) * (9**a - (1 << (3 * a)))
    return h * (q - p) - emax


def verify_payload(payload: dict) -> None:
    floors = {row["depth"]: row for row in payload["phase_floors"]}
    assert set(floors) == {5, 8, 10}

    for depth in (5, 8, 10):
        best, count, digest = recompute_floor(depth)
        frozen = floors[depth]
        assert count == frozen["pair_count"] == 4**depth
        assert frozen["word_count_each_side"] == 2**depth
        assert best == frozen["minimum"]
        assert digest == frozen["ordered_pair_digest"]

    assert floors[5]["minimum"] == {
        "central": 26_873_855,
        "suffix": "BAAAA",
        "prefix": "AAAAB",
        "output_residue": 6_560,
        "output_modulus": 59_049,
        "source_residue": 4_095,
        "source_modulus": 65_536,
        "crt_modulus": 3_869_835_264,
    }
    assert floors[8]["minimum"] == {
        "central": 195_221_131_263,
        "suffix": "AABBBBBB",
        "prefix": "AAAABBAB",
        "output_residue": 4_251_528,
        "output_modulus": 43_046_721,
        "source_residue": 68_554_751,
        "source_modulus": 134_217_728,
        "crt_modulus": 5_777_633_090_469_888,
    }
    assert floors[10]["minimum"] == {
        "central": 90_608_969_363_967,
        "suffix": "ABBAAAAABB",
        "prefix": "AAABAAAAAA",
        "output_residue": 1_389_919_581,
        "output_modulus": 3_486_784_401,
        "source_residue": 191_803_903,
        "source_modulus": 2_147_483_648,
        "crt_modulus": 7_487_812_485_248_974_848,
    }

    h10 = floors[10]["minimum"]["central"]
    cert = payload["parameter_certificate"]

    parameter_digest = hashlib.sha256()
    for a in range(14, 244):
        b = b_min(a)
        m = exact_margin(a, b, h10)
        assert m > 0
        parameter_digest.update(f"{a}|{b}|{m}\n".encode())
    assert parameter_digest.hexdigest() == cert["depth10_parameter_digest"]
    assert cert["depth10_parameter_rows"] == 230

    groups = []
    start = 14
    current = b_min(14)
    for a in range(15, 245):
        nxt = b_min(a) if a <= 243 else None
        if a == 244 or nxt != current:
            end = a - 1
            groups.append(
                {
                    "least_contracting_b": current,
                    "a_start": start,
                    "a_end": end,
                    "endpoint_margin": exact_margin(end, current, h10),
                }
            )
            if a <= 243:
                start = a
                current = nxt
    assert len(groups) == cert["depth10_group_endpoint_rows"] == 48
    assert groups[0] == cert["depth10_first_group_endpoint"]
    assert groups[-1] == cert["depth10_last_group_endpoint"]

    group_digest = hashlib.sha256()
    for row in groups:
        group_digest.update(
            f"{row['least_contracting_b']}|{row['a_start']}|{row['a_end']}|"
            f"{row['endpoint_margin']}\n".encode()
        )
    assert group_digest.hexdigest() == cert["depth10_group_digest"]

    failure = cert["first_failure_of_this_depth10_inequality"]
    assert failure["a"] == 244
    assert b_min(244) == failure["least_contracting_b"] == 50
    assert exact_margin(244, 50, h10) == failure["margin"] < 0

    core = dict(payload)
    expected_semantic = core.pop("semantic_sha256")
    actual_semantic = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert actual_semantic == expected_semantic


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.results.read_text())
    verify_payload(payload)
    print("all independent X-9614 two-sided phase checks passed")


if __name__ == "__main__":
    main()
