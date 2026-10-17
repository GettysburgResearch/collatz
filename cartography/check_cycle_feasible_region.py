#!/usr/bin/env python3
"""Exact certificate for the pass-5 cycle length/support bridge.

This uses integer arithmetic only. It does not prove the source theorem that
positive cycles have more than 50,000 odd states; it certifies the arithmetic
consequence of combining that proposed source result with the elementary
least-state product window.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

K_MIN = 50_001


def minimum_support(k: int) -> int:
    """Return the least s with 14**k <= 11**k * 2**s."""
    if k < 1:
        raise ValueError("k must be positive")
    left = pow(14, k)
    base = pow(11, k)
    lo, hi = 0, k
    while lo < hi:
        mid = (lo + hi) // 2
        if left <= base << mid:
            hi = mid
        else:
            lo = mid + 1
    return lo


def int_digest(n: int) -> str:
    width = (n.bit_length() + 7) // 8
    return hashlib.sha256(n.to_bytes(width, "big")).hexdigest()


def build_payload() -> dict[str, object]:
    s = minimum_support(K_MIN)
    lhs = pow(14, K_MIN)
    rhs_below = pow(11, K_MIN) << (s - 1)
    rhs_at = pow(11, K_MIN) << s

    if not rhs_below < lhs <= rhs_at:
        raise AssertionError("support threshold was not certified exactly")

    payload: dict[str, object] = {
        "source_cycle_floor": {
            "status": "conditional on proposed PR45/T-8401",
            "minimum_odd_state_length": K_MIN,
        },
        "elementary_product_window": "2^A * 7^k <= 22^k",
        "defect_total_identity": "A=B+2(k-s), B>=s",
        "derived_exact_inequality": "14^k <= 11^k * 2^s",
        "minimum_support_at_k_50001": s,
        "strict_below_check": rhs_below < lhs,
        "at_threshold_check": lhs <= rhs_at,
        "bit_lengths": {
            "14^50001": lhs.bit_length(),
            "11^50001*2^17396": rhs_below.bit_length(),
            "11^50001*2^17397": rhs_at.bit_length(),
        },
        "integer_sha256": {
            "14^50001": int_digest(lhs),
            "11^50001*2^17396": int_digest(rhs_below),
            "11^50001*2^17397": int_digest(rhs_at),
        },
        "interpretation": (
            "If the proposed no-cycle-through-50000 theorem is correct, every "
            "nontrivial positive accelerated cycle has at least 17397 valuations "
            "different from 2."
        ),
    }
    semantic = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["semantic_sha256"] = hashlib.sha256(semantic.encode()).hexdigest()
    return payload


def main() -> None:
    payload = build_payload()
    output = Path(__file__).with_name("cycle-feasible-region.json")
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if output.exists() and output.read_text() != text:
        raise SystemExit(f"frozen output mismatch: {output}")
    output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
