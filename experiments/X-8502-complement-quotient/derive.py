#!/usr/bin/env python3
"""Exact derivation checks for the complement-quotient refund coordinate."""
from __future__ import annotations

import argparse
import hashlib
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

P = (5, 30, 20, 56)
TOLL = (9, 54, 36, 24)


def odd(t: int) -> int:
    return 3 ** (7 * (t + 1))


def radix(t: int) -> int:
    return 1 << (11 * (t + 17))


@lru_cache(maxsize=None)
def inverse_pair(t: int) -> tuple[int, int]:
    n, m = odd(t), radix(t)
    r = pow(n, -1, m)
    c = (n * r - 1) // m
    assert n * r == 1 + m * c
    assert 0 < r < m and 0 <= c < n
    return r, c


def origin(t: int, i: int) -> int:
    r, _ = inverse_pair(t)
    return TOLL[i] * (radix(t) - r)


def output(t: int, i: int, k: int) -> int:
    _, c = inverse_pair(t)
    return TOLL[i] * (odd(t) - c) + odd(t) * k


def decode(t: int, i: int, k: int) -> tuple[int, int] | None:
    value = output(t, i, k)
    residue = value % 64
    if residue not in P:
        return None
    j = P.index(residue)
    q = radix(t + 16)
    difference = value - origin(t + 16, j)
    if difference % q:
        return None
    return j, difference // q


def canonical_k(t: int, i: int, j: int) -> tuple[int, int]:
    n = odd(t)
    q = radix(t + 16)
    _, c = inverse_pair(t)
    base = TOLL[i] * (n - c)
    target = origin(t + 16, j)
    residue = ((target - base) * pow(n, -1, q)) % q
    cap = (base + n * residue - target) // q
    assert base + n * residue == target + q * cap
    assert 0 <= residue < q
    return residue, cap


def hash_int(h: "hashlib._Hash", value: int) -> None:
    raw = value.to_bytes(max(1, (value.bit_length() + 7) // 8), "big", signed=False)
    h.update(len(raw).to_bytes(4, "big"))
    h.update(raw)


def payload_digest(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def build_payload() -> dict[str, Any]:
    assert 3 ** 5 < 2 ** 8
    assert 3 ** 106 < 2 ** 170 < 2 ** 175
    assert 2 ** 175 > 3 ** 106

    identity_digest = hashlib.sha256()
    identity_cases = 0
    canonical_cases = 0
    legal_lifts = 0
    growth_cases = 0
    sample_rows: list[dict[str, int]] = []

    for t in (16, 32, 64, 3744, 3760, 4000):
        n, m = odd(t), radix(t)
        r, c = inverse_pair(t)
        del r, c
        for i in range(4):
            for k in (0, 1, 2, 255, 256):
                w = origin(t, i) + m * k
                w_next = output(t, i, k)
                assert m * w_next == n * w + TOLL[i]
                assert w % 64 == P[i]
                assert w > 0 and w_next > 0
                hash_int(identity_digest, t)
                hash_int(identity_digest, i)
                hash_int(identity_digest, k)
                hash_int(identity_digest, w)
                hash_int(identity_digest, w_next)
                identity_cases += 1

        for i in range(4):
            for j in range(4):
                residue, cap = canonical_k(t, i, j)
                assert output(t, i, residue) % 64 == P[j]
                assert decode(t, i, residue) == (j, cap)
                assert cap >= 0
                canonical_cases += 1

                for lift in (0, 1, 2):
                    k = residue + radix(t + 16) * lift
                    result = decode(t, i, k)
                    assert result == (j, cap + n * lift)
                    legal_lifts += 1
                    if t >= 3744 and k >= 256:
                        assert result[1] >= 2 * k
                        growth_cases += 1

                if t in (3744, 3760) and i == j == 0:
                    sample_rows.append(
                        {
                            "t": t,
                            "residue_bits": residue.bit_length(),
                            "cap_bits": cap.bit_length(),
                            "source_origin_bits": origin(t, i).bit_length(),
                            "target_origin_bits": origin(t + 16, j).bit_length(),
                        }
                    )

    type_cells = 0
    for t in (48, 3744):
        n = odd(t)
        _, c = inverse_pair(t)
        for i in range(4):
            cells = []
            for j in range(4):
                target = origin(t + 16, j)
                base = TOLL[i] * (n - c)
                residue = ((target - base) * pow(n, -1, radix(t + 16))) % radix(t + 16)
                cells.append(residue % 64)
                assert output(t, i, residue) % 64 == P[j]
                type_cells += 1
            assert len(set(cells)) == 4

    payload: dict[str, Any] = {
        "experiment": "X-8502",
        "status": "EMPIRICAL / EXACT FINITE INTERFACE AUDIT",
        "identity_cases": identity_cases,
        "identity_digest": identity_digest.hexdigest(),
        "canonical_pair_cases": canonical_cases,
        "legal_lift_cases": legal_lifts,
        "growth_cases": growth_cases,
        "type_cell_cases": type_cells,
        "growth_certificate": {
            "ratio_lower": "N/Q > 9/4 for t>=3744",
            "integer_inequality": "2^175 > 3^106",
            "counter_threshold": 256,
        },
        "sample_rows": sample_rows,
    }
    payload["payload_digest"] = payload_digest(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()

    payload = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n", encoding="utf-8")

    lines = [
        "X-8502 complement-quotient derivation",
        f"exact complement identities: {payload['identity_cases']}",
        f"identity digest: {payload['identity_digest']}",
        f"canonical pair cases: {payload['canonical_pair_cases']}",
        f"legal lift cases: {payload['legal_lift_cases']}",
        f"doubling-growth cases: {payload['growth_cases']}",
        f"unique six-bit type cells: {payload['type_cell_cases']}",
        "growth certificate: N/Q > 9/4, k>=256 => k_next>=2k",
        f"payload digest: {payload['payload_digest']}",
        "all exact complement-quotient checks passed",
    ]
    args.summary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
