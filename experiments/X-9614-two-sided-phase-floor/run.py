#!/usr/bin/env python3
"""Build the exact X-9614 two-sided phase-floor certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path
from typing import Any

LETTERS = {
    "A": (8, 9, 1),   # 8 z' = 9 z + 1
    "B": (16, 9, 0),  # 16 z' = 9 z
}


def words(depth: int):
    return ("".join(bits) for bits in product("AB", repeat=depth))


def compose(word: str) -> tuple[int, int, int]:
    """Return Q,P,e for Q z' = P z + e."""
    q_total = 1
    p_total = 1
    constant = 0
    for letter in word:
        q, p, toll = LETTERS[letter]
        constant = p * constant + q_total * toll
        q_total *= q
        p_total *= p
    return q_total, p_total, constant


def phases(word: str) -> tuple[int, int, int, int]:
    q, p, e = compose(word)
    source = (-e * pow(p, -1, q)) % q
    output = (e * pow(q, -1, p)) % p
    return source, q, output, p


def positive_crt(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    """Least positive x with x=a mod m and x=b mod n; gcd(m,n)=1."""
    lift = ((b - a) * pow(m, -1, n)) % n
    x = a + m * lift
    modulus = m * n
    return (x if x else modulus), modulus


def phase_floor(depth: int) -> dict[str, Any]:
    word_list = list(words(depth))
    outputs = []
    sources = []
    for word in word_list:
        source, q, output, p = phases(word)
        outputs.append((word, output, p))
        sources.append((word, source, q))

    digest = hashlib.sha256()
    minimum = None
    pair_count = 0
    for suffix, output, p in outputs:
        for prefix, source, q in sources:
            central, modulus = positive_crt(output, p, source, q)
            digest.update(
                f"{depth}|{suffix}|{prefix}|{output}|{p}|{source}|{q}|"
                f"{central}|{modulus}\n".encode()
            )
            row = {
                "central": central,
                "suffix": suffix,
                "prefix": prefix,
                "output_residue": output,
                "output_modulus": p,
                "source_residue": source,
                "source_modulus": q,
                "crt_modulus": modulus,
            }
            if minimum is None or central < minimum["central"]:
                minimum = row
            pair_count += 1

    assert minimum is not None
    assert pair_count == 4**depth
    return {
        "depth": depth,
        "word_count_each_side": 2**depth,
        "pair_count": pair_count,
        "minimum": minimum,
        "ordered_pair_digest": digest.hexdigest(),
    }


def contracting(a: int, b: int) -> bool:
    return 9 ** (a + b) < 8**a * 16**b


def least_contracting_b(a: int) -> int:
    b = 1
    while not contracting(a, b):
        b += 1
    return b


def margin(a: int, b: int, phase_floor_value: int) -> int:
    q = 8**a * 16**b
    p = 9 ** (a + b)
    d = q - p
    e_max = 16**b * (9**a - 8**a)
    return phase_floor_value * d - e_max


def parameter_certificate(h10: int) -> dict[str, Any]:
    all_rows = []
    for a in range(14, 244):
        b = least_contracting_b(a)
        m = margin(a, b, h10)
        assert m > 0
        all_rows.append((a, b, m))

    # Compress the finite parameter proof to one endpoint per interval on which
    # the least contracting pulse count is constant. U(a,b) is increasing in
    # a and decreasing in b, so these endpoints are sufficient.
    groups = []
    start = 14
    current_b = least_contracting_b(start)
    for a in range(15, 245):
        next_b = least_contracting_b(a) if a <= 243 else None
        if a == 244 or next_b != current_b:
            end = a - 1
            endpoint_margin = margin(end, current_b, h10)
            assert endpoint_margin > 0
            groups.append(
                {
                    "least_contracting_b": current_b,
                    "a_start": start,
                    "a_end": end,
                    "endpoint_margin": endpoint_margin,
                }
            )
            if a <= 243:
                start = a
                current_b = next_b

    first_failure_a = 244
    first_failure_b = least_contracting_b(first_failure_a)
    first_failure_margin = margin(first_failure_a, first_failure_b, h10)
    assert first_failure_margin < 0

    row_digest = hashlib.sha256()
    for a, b, m in all_rows:
        row_digest.update(f"{a}|{b}|{m}\n".encode())

    group_digest = hashlib.sha256()
    for row in groups:
        group_digest.update(
            f"{row['least_contracting_b']}|{row['a_start']}|{row['a_end']}|"
            f"{row['endpoint_margin']}\n".encode()
        )

    return {
        "depth10_a_start": 14,
        "depth10_a_end": 243,
        "depth10_parameter_rows": len(all_rows),
        "depth10_group_endpoint_rows": len(groups),
        "depth10_parameter_digest": row_digest.hexdigest(),
        "depth10_group_digest": group_digest.hexdigest(),
        "depth10_first_group_endpoint": groups[0],
        "depth10_last_group_endpoint": groups[-1],
        "first_failure_of_this_depth10_inequality": {
            "a": first_failure_a,
            "least_contracting_b": first_failure_b,
            "margin": first_failure_margin,
        },
    }


def semantic_digest(payload: dict[str, Any]) -> str:
    core = dict(payload)
    core.pop("semantic_sha256", None)
    data = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def build() -> dict[str, Any]:
    floors = [phase_floor(5), phase_floor(8), phase_floor(10)]
    h5 = floors[0]["minimum"]["central"]
    h8 = floors[1]["minimum"]["central"]
    h10 = floors[2]["minimum"]["central"]
    assert h5 == 26_873_855
    assert h8 == 195_221_131_263
    assert h10 == 90_608_969_363_967

    payload: dict[str, Any] = {
        "experiment_id": "X-9614",
        "status": "EXACT FINITE CERTIFICATE",
        "interpretation": {
            "proved_by_finite_certificate": [
                "the exact depth-5, depth-8, and depth-10 two-sided phase floors",
                "the exact parameter inequality for every 14<=a<=243 at the least contracting b",
            ],
            "not_proved": [
                "cycle exclusion for a>=244",
                "ordinary extraction for the six-branch divergent chart",
                "a nontrivial positive Collatz cycle or divergent seed",
            ],
        },
        "phase_floors": floors,
        "parameter_certificate": parameter_certificate(h10),
    }
    payload["semantic_sha256"] = semantic_digest(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = build()
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"

    if args.output:
        args.output.write_text(encoded)
    elif not args.check_results:
        print(encoded, end="")

    if args.check_results:
        expected = args.check_results.read_text()
        if encoded != expected:
            raise SystemExit("X-9614 output does not match frozen canonical results")
        print("X-9614 canonical results match")


if __name__ == "__main__":
    main()
