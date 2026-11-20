#!/usr/bin/env python3
"""Exact finite checks for the actual-return positive Green functional.

No float arithmetic, resampled parity, or assumed convergence is used.  The
uncomputed ORIGINAL-source tail is included analytically at each fixed horizon.
The written all-time statements live in research/global-closure-20261120/transport.md.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from functools import cache
import hashlib
import json
from math import comb
from pathlib import Path


SCALE = 10**30
TERMS = 32
METRICS = defaultdict(int)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def ceil_div(a, b):
    require(b > 0, "positive denominator required")
    return -((-a) // b)


def valuation(n, p):
    n = abs(n)
    require(n > 0, "valuation of zero")
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent


@cache
def rank(n):
    require(n >= 1, "ordinary positive input required")
    if n == 1:
        return 0
    h = valuation(2 * n + 1, 3)
    modes = (0, 1, 2, h) if h >= 3 else (0, 1, 2)
    candidates = []
    for a in modes:
        z = (3**a - 2**(a + 1)) * n + 3**a - 2**a
        candidates.append(z * z // 3 ** valuation(z, 3))
    result = min(candidates)
    require(n - 1 <= result <= n * n, "rank interface failed")
    return result


@cache
def accel(n):
    if n == 1:
        return 1
    a = 0 if n % 2 == 0 else valuation(n + 1, 2)
    d, c = 3**a - 2**(a + 1), 3**a - 2**a
    z = d * n + c
    k = valuation(z, 2) // (a + 1)
    require(k >= 1, "nonempty A word required")
    top = z * 3 ** (a * k)
    denominator = 2 ** ((a + 1) * k)
    require(top % denominator == 0, "A affine denominator failed")
    zz = top // denominator
    require((zz - c) % d == 0, "A endpoint integrality failed")
    endpoint = (zz - c) // d
    physical = n
    for _ in range(k):
        for letter in range(a + 1):
            odd = letter < a
            require((physical % 2 == 1) == odd, "physical A parity failed")
            physical = (3 * physical + 1) // 2 if odd else physical // 2
            METRICS["physical_shortcut_edges"] += 1
            METRICS["largest_physical_state"] = max(
                METRICS["largest_physical_state"], physical
            )
    require(physical == endpoint, "affine and physical A disagree")
    require(endpoint + 5 <= (n + 5) ** 3, "A height interface failed")
    METRICS["physically_replayed_A_words"] += 1
    return endpoint


@cache
def unsafe(n):
    return n > 1 and 4 * rank(accel(n)) > rank(n)


@cache
def actual_return(n):
    require(unsafe(n), "B input must be unsafe")
    current = accel(n)
    safe_steps = 0
    while current > 1 and not unsafe(current):
        nxt = accel(current)
        require(4 * rank(nxt) <= rank(current), "safe rank drop failed")
        current = nxt
        safe_steps += 1
    if current > 1:
        require(unsafe(current), "B endpoint guard failed")
        require(rank(current) + 6 <= (rank(n) + 6) ** 6,
                "additive psi interface failed")
    METRICS["actual_B_edges"] += 1
    METRICS["safe_A_steps_inside_B"] += safe_steps
    return current


def mul_interval(x, y):
    require(x[0] >= 0 and y[0] >= 0, "positive multiplication required")
    return x[0] * y[0] // SCALE, ceil_div(x[1] * y[1], SCALE)


def atanh_interval(numerator, denominator):
    """Enclose 2 atanh(z), 0 <= z <= 1/3, at fixed integer scale."""
    require(0 <= 3 * numerator <= denominator, "atanh argument outside range")
    z = (SCALE * numerator // denominator,
         ceil_div(SCALE * numerator, denominator))
    square = mul_interval(z, z)
    power = z
    low = high = 0
    for r in range(TERMS):
        low += power[0] // (2 * r + 1)
        high += ceil_div(power[1], 2 * r + 1)
        power = mul_interval(power, square)
    remainder = ceil_div(9 * SCALE, 4 * (2 * TERMS + 1) * 3 ** (2 * TERMS + 1))
    return 2 * low, 2 * high + remainder


LOG_TWO = atanh_interval(1, 3)


def log_rational_interval(a, b=1):
    require(a > 0 and b > 0, "positive logarithm argument required")
    k = a.bit_length() - b.bit_length()
    if (a < (b << k)) if k >= 0 else ((a << (-k)) < b):
        k -= 1
    num, den = (a, b << k) if k >= 0 else (a << (-k), b)
    require(den <= num < 2 * den, "log range reduction failed")
    lo, hi = atanh_interval(num - den, num + den)
    if k >= 0:
        return lo + k * LOG_TWO[0], hi + k * LOG_TWO[1]
    return lo + k * LOG_TWO[1], hi + k * LOG_TWO[0]


@cache
def psi_from_rank(r):
    inner = log_rational_interval(r + 6)
    require(inner[0] > 0, "positive inner logarithm required")
    lower = log_rational_interval(inner[0], SCALE)[0]
    upper = log_rational_interval(inner[1], SCALE)[1]
    result = SCALE + lower, SCALE + upper
    require(result[0] > 0, "positive psi required")
    return result


@cache
def reciprocal_psi(n):
    lo, hi = psi_from_rank(rank(n))
    return SCALE * SCALE // hi, ceil_div(SCALE * SCALE, lo)


def fraction_log_interval(x, terms=48):
    """Independent rational series, used only for bounded cross-checks."""
    require(x > 0, "positive Fraction logarithm input required")
    k = 0
    while x < 1:
        x *= 2
        k -= 1
    while x >= 2:
        x /= 2
        k += 1

    def series(y):
        z = (y - 1) / (y + 1)
        value = Fraction(0)
        for r in range(terms):
            value += 2 * z ** (2 * r + 1) / (2 * r + 1)
        tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
        return value, value + tail

    a, b = series(x)
    c, d = series(Fraction(2))
    return (a + k * c, b + k * d) if k >= 0 else (a + k * d, b + k * c)


def check_logarithms():
    samples = [Fraction(a, b) for a, b in
               [(1, 7), (1, 2), (1, 1), (2, 1), (7, 1), (9, 8), (13, 9),
                (31, 1), (120, 1), (997, 16), (2**127 + 1, 3**41)]]
    for x in samples:
        lo, hi = log_rational_interval(x.numerator, x.denominator)
        ref_lo, ref_hi = fraction_log_interval(x)
        require(Fraction(lo, SCALE) <= ref_lo <= ref_hi <= Fraction(hi, SCALE),
                "independent logarithm interval mismatch")
    for r in [1, 2, 3, 7, 16, 81, 1296, 370881, 2**64 + 1]:
        inner_lo, inner_hi = fraction_log_interval(Fraction(r + 6))
        # Outward rational rounding prevents a gratuitously huge denominator
        # in the independent SECOND logarithm; its error is below 10^-40.
        ref_scale = 10**40
        inner_lo = Fraction(inner_lo.numerator * ref_scale // inner_lo.denominator, ref_scale)
        inner_hi = Fraction(ceil_div(inner_hi.numerator * ref_scale, inner_hi.denominator), ref_scale)
        lower = fraction_log_interval(inner_lo)[0] + 1
        upper = fraction_log_interval(inner_hi)[1] + 1
        actual = psi_from_rank(r)
        require(Fraction(actual[0], SCALE) <= lower <= upper <= Fraction(actual[1], SCALE),
                "independent nested logarithm interval mismatch")
    return {"rational_log_checks": len(samples), "nested_log_checks": 9}


@cache
def interval_bound(width):
    best = width
    for k in range(width.bit_length() + 1):
        modulus = 1 << k
        for h in range(k + 1):
            high = sum(comb(k, q) for q in range(h + 1, k + 1))
            low = sum((3**q * (width + (1 << (k - q))) - 1) // modulus
                      for q in range(h + 1))
            best = min(best, k + ceil_div(width, modulus) * high + low)
    return best


def check_finite_paths(starts, horizon):
    checks = 0
    longest = 0
    all_killed = True
    green_values = {1: Fraction(0)}
    for start in starts:
        path, seen = [], set()
        current = start
        for _ in range(horizon):
            if current == 1 or current in seen:
                break
            seen.add(current)
            path.append(current)
            current = actual_return(current)
        longest = max(longest, len(path))
        all_killed = all_killed and current == 1
        for width in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024):
            anchors = {1, start, max(1, start - width // 2), max(1, max(path) - width + 1)}
            bound = interval_bound(width)
            for anchor in anchors:
                count = sum(anchor <= n < anchor + width for n in path)
                require(count <= bound, "translated interval bound failed")
                require(count**30 <= 10**30 * width**29, "explicit path power bound failed")
                checks += 1
        if current == 1:
            for n in reversed(path):
                nxt = actual_return(n)
                value = Fraction(1, n) + green_values[nxt]
                if n in green_values:
                    require(green_values[n] == value, "merged Green value mismatch")
                green_values[n] = value
    coboundaries = 0
    for n, value in green_values.items():
        if n == 1:
            continue
        require(value <= 300, "bounded reciprocal-height Green estimate failed")
        require(value - green_values[actual_return(n)] == Fraction(1, n),
                "finite Poisson identity failed")
        coboundaries += 1
    return {"source_paths": len(starts), "translated_window_checks": checks,
            "longest_tested_unsafe_path": longest,
            "all_tested_sources_killed_within_horizon": all_killed,
            "exact_reciprocal_height_coboundaries": coboundaries}


def check_control_models():
    # Squaring is nonabsorbing despite strong sparse-path Green bounds.
    current = 2
    reciprocal_sum = Fraction(0)
    squaring_checks = 0
    for _ in range(11):
        reciprocal_sum += Fraction(1, current)
        nxt = current * current
        require(nxt * nxt + 6 <= (current * current + 6) ** 2,
                "squaring additive budget control failed")
        current = nxt
        squaring_checks += 1
    require(reciprocal_sum < 1, "squaring reciprocal Green control failed")

    # Every finite doubling chain terminates; the manuscript chooses unbounded
    # finite lengths L(q)=2^(q^3), proving nonnecessity without iterating them.
    doubling_edges = 0
    for odd in (3, 5, 7):
        for length in (8, 64, 256):
            path = [odd << j for j in range(length)]
            for n in path:
                require(4 * n * n + 6 <= (n * n + 6) ** 2,
                        "doubling additive budget control failed")
                doubling_edges += 1
            for width in (1, 2, 8, 64, 1024):
                for anchor in (1, odd, path[-1] - width + 1):
                    anchor = max(1, anchor)
                    count = sum(anchor <= n < anchor + width for n in path)
                    require(count <= width.bit_length(), "doubling interval control failed")
    for q in (3, 5, 7, 9):
        require(2 ** (q**3) > q * q + 6, "long-chain symbolic margin failed")
    return {"squaring_edges": squaring_checks,
            "nonabsorbing_squaring_reciprocal_sum_below_one": True,
            "finite_doubling_edges": doubling_edges,
            "long_chain_symbolic_margins": 4}


def interval_record(interval):
    lo, hi = interval
    display_scale = 10**12
    lower = lo * display_scale // SCALE
    upper = ceil_div(hi * display_scale, SCALE)

    def fixed(value):
        return f"{value // display_scale}.{value % display_scale:012d}"

    return {"lower_scaled": str(lo), "upper_scaled": str(hi),
            "scale": str(SCALE), "decimal_enclosure": [fixed(lower), fixed(upper)]}


def run(cutoff, horizon):
    require(cutoff >= 2 and horizon >= 1, "invalid finite scope")
    logs = check_logarithms()
    controls = check_control_models()
    starts = [n for n in range(2, cutoff + 1) if unsafe(n)]
    mass = {n: (SCALE // (n * (n + 1)), ceil_div(SCALE, n * (n + 1)))
            for n in starts}
    checkpoints = {1, horizon}
    t = 2
    while t <= horizon:
        checkpoints.add(t)
        t *= 2
    accumulated = (0, 0)
    rows = []
    psi_star = psi_from_rank(1)
    for j in range(horizon):
        energy_low = energy_high = 0
        for n, weight in mass.items():
            low, high = mul_interval(weight, reciprocal_psi(n))
            energy_low += low
            energy_high += high
        accumulated = accumulated[0] + energy_low, accumulated[1] + energy_high
        nsteps = j + 1
        if nsteps in checkpoints:
            tail = ceil_div(nsteps * SCALE * SCALE, (cutoff + 1) * psi_star[0])
            rows.append({"horizon": nsteps, "finite_source_carriers_at_last_observation": len(mass),
                         "finite_source_G": interval_record(accumulated),
                         "omitted_original_source_tail_upper": interval_record((0, tail)),
                         "whole_source_G": interval_record((accumulated[0], accumulated[1] + tail))})
        following = {}
        for n, weight in mass.items():
            endpoint = actual_return(n)
            if endpoint > 1:
                previous = following.get(endpoint, (0, 0))
                following[endpoint] = previous[0] + weight[0], previous[1] + weight[1]
        mass = following
    paths = check_finite_paths(starts, horizon)
    source = Path(__file__).read_bytes()
    return {"status": "PASS", "schema": "global-closure-transport-v1",
            "claims": ["GCT-001", "GCT-002", "GCT-003", "GCT-004"],
            "evidence_scope": "Exact finite actual-return replay; full-source fixed-horizon enclosures via analytic tails. No all-time closing estimate.",
            "source_pins": {
                "main": "ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a",
                "PR152": "2391a9c1e4a7f77233b951d2eb6da92e76652e7c",
                "PR153": "eb04a5d79020cefa0ba46794095b5766c5ff66a4"},
            "checker_sha256": hashlib.sha256(source).hexdigest(),
            "original_source_cutoff": cutoff, "return_horizon": horizon,
            "unsafe_original_sources": len(starts), "psi_star": interval_record(psi_star),
            "integer_log_crosschecks": logs, "controls": controls,
            "finite_path_checks": paths, "actual_replay": dict(sorted(METRICS.items())),
            "functional_enclosures": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cutoff", type=int, default=8192)
    parser.add_argument("--returns", type=int, default=64)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    result = run(args.cutoff, args.returns)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.compare:
        require(json.loads(args.compare.read_text(encoding="utf-8")) == result,
                "frozen report mismatch")
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
