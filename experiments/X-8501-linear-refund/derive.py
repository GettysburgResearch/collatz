#!/usr/bin/env python3
"""Exact derivation audit for the linear-height quotient-refund packet.

Python standard library only.  All critical arithmetic uses exact integers.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any
from functools import lru_cache

P = (5, 30, 20, 56)
B_TOLL = (9, 54, 36, 24)
STEP = 16
S3 = 3 ** 112
U2 = 1 << 176


def sha_payload(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def n_odd(t: int) -> int:
    return 3 ** (7 * (t + 1))


def m_next(t: int) -> int:
    """Connector modulus from height t to t+16."""
    return 1 << (11 * (t + 17))


def anchors(t: int, i: int, j: int) -> tuple[int, int, int, int]:
    n = n_odd(t)
    m = m_next(t)
    source_cap = (n * P[i] + B_TOLL[i]) // 64
    target_anchor = m * P[j] // 64
    assert n * P[i] + B_TOLL[i] == 64 * source_cap
    return n, m, source_cap, target_anchor


@lru_cache(maxsize=None)
def connector_direct(t: int, i: int, j: int) -> tuple[int, int, int, int]:
    n, m, source_cap, target_anchor = anchors(t, i, j)
    eta = ((target_anchor - source_cap) * pow(n, -1, m)) % m
    theta = (source_cap + n * eta - target_anchor) // m
    assert source_cap + n * eta == target_anchor + m * theta
    assert 0 <= eta < m
    assert 0 <= theta < n
    return eta, theta, n, m


@lru_cache(maxsize=None)
def inverse_data(t: int) -> tuple[int, int, int, int]:
    n = n_odd(t)
    m = m_next(t)
    r = pow(n, -1, m)
    c = (n * r - 1) // m
    assert n * r == 1 + m * c
    assert 0 <= r < m
    assert 0 <= c < n
    return r, c, n, m


def inverse_carry_update(t: int) -> tuple[int, int, int, int]:
    """Return r', c', and the appended base-3^112 digit q."""
    r, c, n, m = inverse_data(t)
    n2 = S3 * n
    m2 = U2 * m

    c_bar = (pow(U2, -1, n) * c) % n
    h = (1 + U2 * m * c_bar) // n
    assert 1 + U2 * m * c_bar == n * h
    q = (-h * pow(U2 * m, -1, S3)) % S3
    c2 = c_bar + n * q
    r2 = (1 + m2 * c2) // n2

    rr, cc, nn, mm = inverse_data(t + STEP)
    assert (r2, c2, n2, m2) == (rr, cc, nn, mm)
    assert 0 <= q < S3
    return r2, c2, q, c_bar


@lru_cache(maxsize=None)
def connector_normal(t: int, i: int, j: int) -> tuple[int, int, int, int, int, int, int]:
    r, c, n, m = inverse_data(t)
    omega_num = P[i] + B_TOLL[i] * r
    assert omega_num % 64 == 0
    omega = omega_num // 64
    delta = (P[j] * r - P[i] * c) % 64
    raw = -omega + (m // 64) * delta
    assert -m < raw < m
    eps = 1 if raw < 0 else 0
    eta = raw + eps * m
    theta_num = n * delta - B_TOLL[i] * c - P[j]
    assert theta_num % 64 == 0
    theta = theta_num // 64 + eps * n

    eta0, theta0, _, _ = connector_direct(t, i, j)
    assert eta == eta0
    assert theta == theta0
    return eta, theta, r, c, delta, eps, omega


def decoder(t: int, i: int, j: int, z: int) -> tuple[int, int] | None:
    eta, theta, n, _ = connector_direct(t, i, j)
    del eta
    _, _, _, _, _, _, omega2 = connector_normal(t + STEP, j, 0)
    m2 = m_next(t + STEP)
    block = m2 // 64
    low = n * z + theta + omega2
    if low % block:
        return None
    top = (low // block) % 64

    candidates = []
    for k in range(4):
        eta2, _, _, _, delta2, eps2, _ = connector_normal(t + STEP, j, k)
        if delta2 == top:
            candidates.append((k, eta2, eps2))
    if len(candidates) != 1:
        return None
    k, eta2, _ = candidates[0]
    numerator = n * z + theta - eta2
    if numerator % m2:
        raise AssertionError("decoder low/top conditions did not imply integrality")
    z2 = numerator // m2
    return k, z2


@lru_cache(maxsize=None)
def canonical_residual(t: int, i: int, j: int, k: int) -> tuple[int, int]:
    _, theta, n, _ = connector_direct(t, i, j)
    eta2, _, _, m2 = connector_direct(t + STEP, j, k)
    y = ((eta2 - theta) * pow(n, -1, m2)) % m2
    cap = (theta + n * y - eta2) // m2
    assert theta + n * y == eta2 + m2 * cap
    assert 0 <= cap < n
    return y, cap


def stage_exponents(width: int, base: int) -> tuple[int, int, int]:
    a = 7 * width * (base + 1) + 56 * width * (width - 1)
    e = 11 * width * (base + 1) + 88 * width * (width + 1)
    e_next = 11 * width * (base + 16 * width + 1) + 88 * width * (width + 1)
    return a, e, e_next


def refund_threshold(width: int) -> int:
    # Need 5*B > 9288*width+9363, with B a nonnegative multiple of 16.
    cutoff = 9288 * width + 9363
    least_integer = cutoff // 5 + 1
    return 16 * ((least_integer + 15) // 16)


def cylinder_depth(t0: int, length: int) -> int:
    return sum(11 * (t0 + 16 * n + 33) for n in range(length))


def build_payload() -> dict[str, Any]:
    # Exact Vaananen--Wallisser endpoint certificates.
    assert (1 << 1287) > 3 ** 812
    assert (1 << 1298) < 3 ** 819
    assert 13573 ** 2 - 13457 * 117 ** 2 == 13456
    assert 118 ** 2 < 13925

    widths = (1, 2, 4, 8, 16, 32, 58, 64, 128, 256)
    refund_rows = []
    for width in widths:
        base = refund_threshold(width)
        a, e, e_next = stage_exponents(width, base)
        margin = 84 * a - 53 * e_next
        assert margin > 0
        if base >= 16:
            a0, _, e0 = stage_exponents(width, base - 16)
            assert 84 * a0 <= 53 * e0
        assert margin == width * (5 * base - 9288 * width - 9363)
        refund_rows.append(
            {
                "width": width,
                "least_multiple_16_base": base,
                "odd_exponent": a,
                "current_binary_exponent": e,
                "next_binary_exponent": e_next,
                "53_scaled_margin": margin,
            }
        )

    carry_rows = []
    connector_cases = 0
    for t in (16, 32, 3744, 3760, 6000):
        r, c, n, m = inverse_data(t)
        r2, c2, q, c_bar = inverse_carry_update(t)
        assert r2.bit_length() <= 11 * (t + 33)
        for i in range(4):
            for j in range(4):
                connector_normal(t, i, j)
                connector_cases += 1
        carry_rows.append(
            {
                "t": t,
                "inverse_bits": r.bit_length(),
                "carry_bits": c.bit_length(),
                "next_carry_bits": c2.bit_length(),
                "appended_ternary_digit_bits": q.bit_length(),
                "reduced_carry_bits": c_bar.bit_length(),
                "modulus_bits": m.bit_length() - 1,
                "odd_multiplier_bits": n.bit_length(),
            }
        )

    decoder_cases = 0
    growth_cases = 0
    decoder_digest = hashlib.sha256()
    for t in (3744, 3760):
        n = n_odd(t)
        m2 = m_next(t + STEP)
        assert 84 * 7 * (t + 1) - 53 * 11 * (t + 33) > 53
        assert n > 2 * m2
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    y, cap = canonical_residual(t, i, j, k)
                    for lift in (0, 1, 2):
                        z = y + m2 * lift
                        if z == 0:
                            continue
                        result = decoder(t, i, j, z)
                        assert result is not None
                        kk, z2 = result
                        assert kk == k
                        assert z2 == cap + n * lift
                        assert z2 >= 2 * z
                        decoder_cases += 1
                        growth_cases += 1
                        for value in (t, i, j, k, lift, z & ((1 << 128) - 1), z2 & ((1 << 128) - 1)):
                            decoder_digest.update(int(value).to_bytes(32, "big", signed=False))

    phase_identity_cases = 0
    for period in range(1, 59):
        for phase in range(period):
            for block in range(6):
                index = period * block + phase
                left = index * (index - 1) // 2
                right = (
                    period * period * block * (block - 1) // 2
                    + block * period * (period + 2 * phase - 1) // 2
                    + phase * (phase - 1) // 2
                )
                assert left == right
                phase_identity_cases += 1
        for a in range(period):
            for bb in range(period):
                if a == bb:
                    continue
                assert (a - bb) % period != 0
                phase_identity_cases += 1

    depth_rows = []
    for length in range(1, 13):
        depth = cylinder_depth(3744, length)
        control = 2 * length
        assert depth == 88 * length * length + (11 * 3744 + 275) * length
        depth_rows.append(
            {
                "length": length,
                "cylinder_bits": depth,
                "directive_bits": control,
                "deficit_bits": depth - control,
            }
        )

    payload: dict[str, Any] = {
        "experiment": "X-8501",
        "status": "EMPIRICAL / EXACT FINITE INTERFACE AUDIT",
        "refund_rows": refund_rows,
        "periodic_cutoff": {
            "last_source_dimension": 58,
            "first_failed_dimension": 59,
            "lower_log_certificate": "2^1287 > 3^812",
            "upper_log_certificate": "2^1298 < 3^819",
            "dimension_58_square_difference": 13456,
            "dimension_59_square_certificate": "118^2 < 13925",
        },
        "carry_rows": carry_rows,
        "connector_normal_form_cases": connector_cases,
        "decoder_cases": decoder_cases,
        "growth_cases": growth_cases,
        "decoder_digest": decoder_digest.hexdigest(),
        "phase_identity_cases": phase_identity_cases,
        "depth_rows": depth_rows,
    }
    payload["payload_digest"] = sha_payload(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()

    payload = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "X-8501 linear quotient-refund derivation",
        f"refund widths: {len(payload['refund_rows'])}",
        "least width-1 refund base: 3744",
        "least width-256 refund base: 477424",
        "periodic source cutoff: 58 (condition first fails at 59)",
        f"inverse-carry rows: {len(payload['carry_rows'])}",
        f"connector normal-form cases: {payload['connector_normal_form_cases']}",
        f"forced decoder cases: {payload['decoder_cases']}",
        f"doubling-growth cases: {payload['growth_cases']}",
        f"decoder digest: {payload['decoder_digest']}",
        f"periodic phase-identity cases: {payload['phase_identity_cases']}",
        f"cylinder-depth rows: {len(payload['depth_rows'])}",
        f"payload digest: {payload['payload_digest']}",
        "all exact derivation checks passed",
    ]
    args.summary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
