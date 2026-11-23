#!/usr/bin/env python3
"""Exact finite certificates used by the symbolic rational-shadow compiler.

This checker does not enumerate integer starting values. Every check uses
the complete source affine numerator, a rational numerator trace, or the
explicit symbolic descent threshold. Guards remain active under python -O.
"""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def step(n: int) -> int:
    return (3 * n + 1) // 2 if n % 2 else n // 2


def source_affine(word: list[int]) -> tuple[int, int, int]:
    a, b, c = 1, 1, 0
    for gap in word:
        require(type(gap) is int and gap > 0, "positive integer source gap required")
        a, b, c = 3 * a, b * 2**gap, 3 * c + b
    return a, b, c


def rational_prefix(d: int, h: int, clock: int) -> tuple[int, int, str]:
    odds = 0
    parity = []
    for _ in range(clock):
        odd = h % 2
        parity.append(str(odd))
        odds += odd
        h = (3 * h + d) // 2 if odd else h // 2
    return odds, h, "".join(parity)


def verify_one(cert: dict) -> dict:
    word = cert["source_block"]
    require(bool(word), "source block must be nonempty")
    a, b, c = source_affine(word)
    d = b - a
    require(d > 0 and d % 2 == 1, "positive odd fixed-point denominator required")
    require((a, b, c, d) == tuple(cert[k] for k in ("source_a", "source_b", "source_c", "denominator")),
            "source affine data mismatch")
    A, B = cert["target_A"], cert["target_B"]
    require(type(A) is int and A > 0 and type(B) is int and B >= 0, "invalid target affine data")
    h = A * c + d * B
    require(h == cert["shadow_numerator"], "shadow numerator mismatch")
    e = cert["source_repetitions"]
    k = cert["target_clock"]
    require(type(e) is int and e > 0 and type(k) is int and k > 0, "positive clocks required")
    H = sum(word) * e
    require(H == cert["source_horizon"], "source horizon mismatch")
    require(H >= k, "target exceeds supplied source binary horizon")
    require(2**H > c, "source displacement sign is not paid")
    o, end, parity = rational_prefix(d, h, k)
    require(o == cert["target_odd_count"], "rational odd count mismatch")
    require(end == cert["shadow_endpoint"], "rational endpoint mismatch")
    require(parity == cert["target_parity"], "rational parity word mismatch")
    delta = 2**k - 3**o
    require(delta > 0, "rational prefix does not contract")
    margin = delta * A * 2 ** (H - k) + h - end
    require(margin > 0, "positive source displacement does not pay target offset")
    require(margin == cert["minimum_scaled_descent"], "minimum descent margin mismatch")
    exceptional_source = c // d if c % d == 0 else None
    require(exceptional_source == cert["fixed_source_exception"], "source fixed-point exception mismatch")
    if exceptional_source is not None:
        target = A * exceptional_source + B
        endpoint = target
        for _ in range(k):
            endpoint = step(endpoint)
        require(endpoint < target, "fixed source exception has not been separately discharged")
        require(endpoint == cert["exception_target_endpoint"], "fixed-source target endpoint mismatch")
    else:
        require(cert["exception_target_endpoint"] is None, "spurious fixed-source discharge")
    return {"name": cert["name"], "clock": k, "minimum_scaled_descent": margin,
            "scope": "all physical sources with the supplied repeated prefix, all tails"}


def damaged_controls(certificates: list[dict]) -> int:
    mutations = [
        (2, "source_repetitions", 47),
        (2, "target_odd_count", 120),
        (2, "shadow_endpoint", 130),
        (2, "denominator", 15),
        (2, "source_horizon", 188),
        (0, "fixed_source_exception", None),
        (0, "exception_target_endpoint", 11),
    ]
    for index, field, value in mutations:
        damaged = copy.deepcopy(certificates[index])
        damaged[field] = value
        try:
            verify_one(damaged)
        except ValueError:
            continue
        raise ValueError(f"damaged control unexpectedly accepted: {field}")
    return len(mutations)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", type=Path,
                        default=Path(__file__).with_name("rational_shadow_certificates.json"))
    args = parser.parse_args()
    payload = json.loads(args.certificate.read_text())
    require(payload["schema"] == "rational-shadow-descent/v1", "unknown certificate schema")
    results = [verify_one(cert) for cert in payload["certificates"]]
    controls = damaged_controls(payload["certificates"])
    print(json.dumps({"status": "PASS", "certificates": results,
                      "damaged_controls_rejected": controls,
                      "universal_coverage_claimed": False}, indent=2))


if __name__ == "__main__":
    main()
