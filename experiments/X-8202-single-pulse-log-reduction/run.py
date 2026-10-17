#!/usr/bin/env python3
"""Certified reduction for all-repetition single-pulse exclusions.

This script uses exact rational interval arithmetic to:
* certify continued fractions of log_2(9/8) and log_2(2187/2048);
* verify explicit Matveev cutoffs under the quoted theorem constant C(2)=2^32;
* reduce every possible single-pulse divisibility hit to finitely many convergents;
* reject all convergent candidates by a rigorous denominator-size inequality;
* retain the unique trivial (1,2)->(2,2), n=1 hit.

The Matveev theorem itself is an external theorem dependency. Everything after its
quoted lower bound is checked exactly with Python integers and fractions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

TERMS = 180
sys.set_int_max_str_digits(0)
MATVEEV_C2 = 2**32


@dataclass(frozen=True)
class LogInterval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if not self.lo < self.hi:
            raise ValueError("invalid interval")


def fraction_digest(value: Fraction) -> str:
    return hashlib.sha256(f"{value.numerator}/{value.denominator}".encode()).hexdigest()


def decimal_floor(value: Fraction, digits: int = 18) -> str:
    scale = 10**digits
    sign = "-" if value < 0 else ""
    value = abs(value)
    integer = value.numerator * scale // value.denominator
    whole, frac = divmod(integer, scale)
    return f"{sign}{whole}.{frac:0{digits}d}"


def decimal_ceil(value: Fraction, digits: int = 18) -> str:
    scale = 10**digits
    sign = "-" if value < 0 else ""
    value = abs(value)
    integer = (value.numerator * scale + value.denominator - 1) // value.denominator
    whole, frac = divmod(integer, scale)
    return f"{sign}{whole}.{frac:0{digits}d}"


def interval_summary(interval: LogInterval, digits: int = 30) -> dict[str, object]:
    width = interval.hi - interval.lo
    # Largest n certified by width < 2^-n.
    n = 0
    while width < Fraction(1, 2**(n + 1)):
        n += 1
    return {
        "decimal_lo": decimal_floor(interval.lo, digits),
        "decimal_hi": decimal_ceil(interval.hi, digits),
        "lo_sha256": fraction_digest(interval.lo),
        "hi_sha256": fraction_digest(interval.hi),
        "width_less_than_2_pow_minus": n,
    }


def atanh_series_interval(z: Fraction, terms: int = TERMS) -> LogInterval:
    if not (Fraction(0) <= z < 1):
        raise ValueError("atanh series domain")
    partial = Fraction(0)
    zpow = z
    z2 = z * z
    for j in range(terms):
        partial += 2 * zpow / (2 * j + 1)
        zpow *= z2
    tail = 2 * zpow / ((2 * terms + 1) * (1 - z2))
    return LogInterval(partial, partial + tail)


def atanh_log_interval(x: Fraction, terms: int = TERMS) -> LogInterval:
    """Certified interval for log(x), x>0, after binary range reduction."""
    if x <= 0:
        raise ValueError("log domain")
    if x == 2:
        return atanh_series_interval(Fraction(1, 3), terms)

    # Exact binary range reduction x=2^m*y with 1<=y<2.
    m = x.numerator.bit_length() - x.denominator.bit_length()
    y = x / (2**m) if m >= 0 else x * (2 ** (-m))
    while y < 1:
        m -= 1
        y *= 2
    while y >= 2:
        m += 1
        y /= 2

    z = (y - 1) / (y + 1)
    if not (Fraction(0) <= z <= Fraction(1, 3)):
        raise AssertionError("range reduction failed")
    core = atanh_series_interval(z, terms)
    log2 = atanh_series_interval(Fraction(1, 3), terms)
    if m >= 0:
        return LogInterval(m * log2.lo + core.lo, m * log2.hi + core.hi)
    return LogInterval(m * log2.hi + core.lo, m * log2.lo + core.hi)


LOG2 = atanh_log_interval(Fraction(2))
LOG3 = atanh_log_interval(Fraction(3))


def mul_positive(a: LogInterval, b: LogInterval) -> LogInterval:
    if a.lo <= 0 or b.lo <= 0:
        raise ValueError("positive intervals required")
    return LogInterval(a.lo * b.lo, a.hi * b.hi)


def alpha_interval(A: int, k: int) -> LogInterval:
    # alpha = (k*log(3)-A*log(2))/log(2), positive in both native cases.
    num_lo = k * LOG3.lo - A * LOG2.hi
    num_hi = k * LOG3.hi - A * LOG2.lo
    if num_lo <= 0:
        raise AssertionError("alpha numerator not certified positive")
    return LogInterval(num_lo / LOG2.hi, num_hi / LOG2.lo)


def certified_cf(interval: LogInterval, stop_denominator: int) -> list[dict[str, int | str]]:
    lo, hi = interval.lo, interval.hi
    p_nm2, p_nm1 = 0, 1
    q_nm2, q_nm1 = 1, 0
    out: list[dict[str, int | str]] = []

    for index in range(256):
        a_lo = lo.numerator // lo.denominator
        a_hi = hi.numerator // hi.denominator
        if a_lo != a_hi:
            raise AssertionError(f"continued-fraction interval straddles an integer at {index}")
        a = a_lo
        p = a * p_nm1 + p_nm2
        q = a * q_nm1 + q_nm2
        value = Fraction(p, q)
        if value < interval.lo:
            side = "below"
        elif value > interval.hi:
            side = "above"
        else:
            raise AssertionError("convergent lies inside unresolved alpha interval")
        out.append({"index": index, "partial_quotient": a, "p": p, "q": q, "side": side})
        if q > stop_denominator:
            return out
        lo, hi = 1 / (hi - a), 1 / (lo - a)
        p_nm2, p_nm1 = p_nm1, p
        q_nm2, q_nm1 = q_nm1, q
    raise AssertionError("continued fraction did not reach cutoff")


def log_integer_interval(n: int) -> LogInterval:
    return atanh_log_interval(Fraction(n))


def matveev_cutoff_certificate(A: int, k: int, cmax: int, M: int) -> dict[str, str | bool]:
    """Certify no solution can have r>=M using Matveev's quoted bound.

    A solution gives
      r log(2^A) < log(2*cmax) + K(1+log(k*r+1)),
    K=2^32 log2 log3.
    We certify the reverse inequality at M and positive derivative thereafter.
    """
    # In the cutoff regime, the native upper bound gives Lambda<1<log(3),
    # so B=(Ar+delta)log(2)/log(3)=kr+Lambda/log(3)<kr+1.
    if not (A * M >= (2 * cmax).bit_length() and LOG3.lo > 1):
        raise AssertionError("B<kr+1 was not certified at the cutoff")

    Kint = mul_positive(LOG2, LOG3)
    Kint = LogInterval(MATVEEV_C2 * Kint.lo, MATVEEV_C2 * Kint.hi)
    log_u_lo = A * LOG2.lo
    log_C_hi = log_integer_interval(2 * cmax).hi
    log_B_hi = log_integer_interval(k * M + 1).hi
    lhs_lo = M * log_u_lo
    rhs_hi = log_C_hi + Kint.hi * (1 + log_B_hi)

    # derivative f'(r)=log(u)-K*k/(k*r+1); lower-bound it at M.
    derivative_lo = log_u_lo - Kint.hi * Fraction(k, k * M + 1)
    if not lhs_lo > rhs_hi:
        raise AssertionError("chosen Matveev cutoff is not certified")
    if not derivative_lo > 0:
        raise AssertionError("cutoff function not certified increasing")
    margin = lhs_lo - rhs_hi
    return {
        "cutoff_verified": True,
        "margin_decimal_lower": decimal_floor(margin, 12),
        "margin_sha256": fraction_digest(margin),
        "derivative_decimal_lower": decimal_floor(derivative_lo, 18),
        "derivative_sha256": fraction_digest(derivative_lo),
    }


def exact_small_scan(A: int, k: int, odd_coefficients: Iterable[int], rmax: int) -> list[dict[str, int]]:
    hits: list[dict[str, int]] = []
    qpow = 3**k
    upow = 2**A
    q_r = 1
    u_r = 1
    for r in range(1, rmax + 1):
        q_r *= qpow
        u_r *= upow
        delta = 1
        while u_r * 2**delta <= q_r:
            delta += 1
        # D/2^delta increases with delta, so once the size condition fails for cmax,
        # every later pulse is impossible.
        while True:
            D = u_r * 2**delta - q_r
            possible = False
            for c in odd_coefficients:
                target = c * (2**delta - 1)
                if D <= target:
                    possible = True
                    if target % D == 0:
                        hits.append({"r": r, "delta": delta, "c": c, "D": D, "quotient": target // D})
            if not possible:
                break
            delta += 1
    return hits


def candidate_rejections(
    A: int,
    cmax: int,
    cf: list[dict[str, int | str]],
    cutoff: int,
    minimum_legendre_r: int,
) -> list[dict[str, int | str | bool]]:
    out: list[dict[str, int | str | bool]] = []
    for i, row in enumerate(cf[:-1]):
        q = int(row["q"])
        p = int(row["p"])
        if q >= cutoff or q < minimum_legendre_r or row["side"] != "above":
            continue
        qnext = int(cf[i + 1]["q"])
        # If delta/r reduces to p/q, then (r,delta)=m(q,p). From the
        # standard convergent bound, every m>=1 satisfies
        #   Lambda=m(p-q*alpha)log2 > log2/(q+qnext).
        # The divisibility upper bound is <=2*cmax/U^q, already at m=1.
        # Thus U^q>4*cmax*(q+qnext), using log2>1/2, rejects every multiple.
        rhs = 4 * cmax * (q + qnext)
        size_rejected = (A * q) >= rhs.bit_length()
        if not size_rejected:
            raise AssertionError(
                f"primitive convergent denominator q={q} is too small for the uniform multiple rejection; "
                "move it to the exact small scan"
            )
        out.append(
            {
                "primitive_denominator_q": q,
                "primitive_numerator_p": p,
                "next_denominator": qnext,
                "power_two_exponent_at_m1": A * q,
                "comparison_rhs_at_m1": rhs,
                "all_positive_multiples_rejected": True,
            }
        )
    return out


CASES = (
    {
        "name": "negative-three-cycle",
        "A": 3,
        "k": 2,
        "u": 8,
        "c_values": (5, 7),
        "cmax": 7,
        "cutoff": 50_000_000_000,
        "legendre_r": 3,
        "small_scan": 4,
    },
    {
        "name": "negative-eleven-cycle",
        "A": 11,
        "k": 7,
        "u": 2048,
        "c_values": (17, 25, 37, 41, 55, 61, 91),
        "cmax": 91,
        "cutoff": 12_000_000_000,
        "legendre_r": 1,
        "small_scan": 1,
    },
)


def build_payload() -> dict[str, object]:
    cases = []
    transcript = hashlib.sha256()
    total_convergents = total_candidates = 0

    for spec in CASES:
        A = int(spec["A"])
        k = int(spec["k"])
        cutoff = int(spec["cutoff"])
        alpha = alpha_interval(A, k)
        cf = certified_cf(alpha, cutoff)
        matveev = matveev_cutoff_certificate(A, k, int(spec["cmax"]), cutoff)

        # Certify Legendre's threshold at the first declared r; u^r/r then grows.
        r0 = int(spec["legendre_r"])
        C = 2 * int(spec["cmax"])
        legendre_margin = LOG2.lo * (2 ** (A * r0)) - 2 * C * r0
        if legendre_margin <= 0:
            raise AssertionError("Legendre threshold not certified")

        small_hits = exact_small_scan(A, k, spec["c_values"], int(spec["small_scan"]))
        rejected = candidate_rejections(A, int(spec["cmax"]), cf, cutoff, r0)

        # The only admissible hit is the known trivial negative-three-cycle rotation.
        if spec["name"] == "negative-three-cycle":
            expected = [{"r": 1, "delta": 1, "c": 7, "D": 7, "quotient": 1}]
            if small_hits != expected:
                raise AssertionError(f"unexpected small hits: {small_hits}")
        elif small_hits:
            raise AssertionError(f"unexpected eleven-cycle hit: {small_hits}")

        upper_convergents = [
            {
                "primitive_denominator_q": int(row["q"]),
                "primitive_numerator_p": int(row["p"]),
                "next_q": int(cf[i + 1]["q"]),
            }
            for i, row in enumerate(cf[:-1])
            if row["side"] == "above" and int(row["q"]) < cutoff and int(row["q"]) >= r0
        ]
        if len(upper_convergents) != len(rejected):
            raise AssertionError("not every upper convergent was rejected")

        total_convergents += len(cf)
        total_candidates += len(rejected)
        for row in cf:
            transcript.update(
                f"{spec['name']}|{row['index']}|{row['partial_quotient']}|{row['p']}|{row['q']}|{row['side']}\n".encode()
            )

        cases.append(
            {
                "name": spec["name"],
                "A": A,
                "k": k,
                "odd_coefficients": list(spec["c_values"]),
                "cutoff": cutoff,
                "alpha_interval": interval_summary(alpha),
                "continued_fraction": cf,
                "upper_convergents_below_cutoff": upper_convergents,
                "candidate_rejections": rejected,
                "small_hits": small_hits,
                "matveev_certificate": matveev,
                "legendre_margin_decimal_lower": decimal_floor(legendre_margin, 18),
                "legendre_margin_sha256": fraction_digest(legendre_margin),
            }
        )

    return {
        "claim": "T-8202",
        "status": "SOURCE-DEPENDENT PROPOSED; exact reduction/checker, external Matveev theorem pending independent source reconstruction",
        "matveev_form_used": {
            "n": 2,
            "degree": 1,
            "constant": "2^(6n+20)=2^32",
            "A1": "log(2)",
            "A2": "log(3)",
            "bound": "log|Lambda| >= -2^32*log(2)*log(3)*(1+log B)",
        },
        "log_interval_terms": TERMS,
        "cases": cases,
        "summary": {
            "certified_continued_fraction_rows": total_convergents,
            "upper_convergent_candidates_rejected": total_candidates,
            "nontrivial_divisibility_hits": 0,
            "trivial_hits": 1,
        },
        "transcript_sha256": transcript.hexdigest(),
    }


def stable_json(payload: dict[str, object]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write-results", type=Path)
    group.add_argument("--check-results", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = stable_json(payload)
    target = args.write_results or args.check_results
    assert target is not None
    if args.write_results:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8")
        print(f"wrote {target}")
    else:
        if target.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"result mismatch: {target}")
        print(f"verified {target}")
    print(json.dumps(payload["summary"], sort_keys=True))
    print(f"transcript_sha256={payload['transcript_sha256']}")


if __name__ == "__main__":
    main()
