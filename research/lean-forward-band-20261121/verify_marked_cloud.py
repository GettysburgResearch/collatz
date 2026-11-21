#!/usr/bin/env python3
"""Exact finite examples for MARKED_PREDECESSOR_POPULATIONS.md.

The floating/Decimal logarithms only choose a candidate rotation depth. Every
claimed approximation, phase interval, affine identity, section membership,
distinctness, and ordinary clock is subsequently checked with integers.

This demonstrates the finite arithmetic interface. It does not test or prove
the analytic controlled atom floor, its uniform constant, or Collatz.
"""

from __future__ import annotations

import argparse
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def le_power_of_two_ratio(num: int, den: int, exponent: int) -> bool:
    """Return num/den <= 2**exponent, without nonintegral arithmetic."""
    return num <= den << exponent if exponent >= 0 else num << -exponent <= den


def floor_log2_ratio(num: int, den: int) -> int:
    k = num.bit_length() - den.bit_length()
    # Equality belongs to the upper octave, hence the strict correction.
    if (num < den << k) if k >= 0 else (num << -k < den):
        k -= 1
    assert le_power_of_two_ratio(den, num, -k)
    assert not le_power_of_two_ratio(num, den, k - 1)
    assert le_power_of_two_ratio(num, den, k + 1)
    return k


def verify_phase(target: int, s: int, q: int) -> dict[str, int]:
    """Certify 2/q <= frac(log2(target) - (s+1)log2(3)) <= 5/q."""
    den = pow(3, s + 1)
    k = floor_log2_ratio(target, den)
    num_q, den_q = pow(target, q), pow(den, q)
    # v >= 2/q iff 2**(q*k+2) <= target**q / den**q.
    assert le_power_of_two_ratio(den_q, num_q, -q * k - 2)
    assert le_power_of_two_ratio(num_q, den_q, q * k + 5)
    return {"numerator_lower": 2, "numerator_upper": 5,
            "denominator": q, "integer_part": k}


def choose_depth(target: int, p: int, q: int) -> tuple[int, dict[str, int]]:
    # |log2(3)-p/q| <= 1/q**2, proved by an integer power comparison.
    three = pow(3, q * q)
    assert (1 << (p * q - 1)) <= three <= (1 << (p * q + 1))
    with localcontext() as ctx:
        ctx.prec = 90
        alpha = Decimal(3).ln() / Decimal(2).ln()
        theta = Decimal(target).ln() / Decimal(2).ln()
        for s in range(q, 2 * q):
            x = theta - (s + 1) * alpha
            integral = x.to_integral_value(rounding="ROUND_FLOOR")
            v = x - integral
            if Decimal(2) / q <= v <= Decimal(5) / q:
                return s, verify_phase(target, s, q)
    raise AssertionError("The certified rational grid produced no candidate")


def choose_parent(target: int, s: int, beta_bound: int) -> tuple[int, int, int]:
    C = 8 * (1 + 3 * beta_bound)
    e = next(e for e in range(1, 7) if (pow(2, e, 9) * target) % 9 == 4)
    while ((target << e) - 1) // 3 < C * s:
        e += 6
    parent = ((target << e) - 1) // 3
    assert (target << e) == 3 * parent + 1
    assert parent % 2 == 1 and parent % 3 == 1
    assert C * s <= parent <= 65 * C * s
    return e, parent, C


def selected_cloud(parent: int, s: int, beta_bound: int, width: int):
    # These deterministic choices deliberately form a small legal cloud.
    # No inference about the full controlled density is made from this sample.
    cloud: list[tuple[int, int, tuple[int, ...]]] = [(parent, 0, ())]
    three_pow = 1
    for i in range(1, s + 1):
        three_pow *= 3
        children: dict[int, tuple[int, int, tuple[int, ...]]] = {}
        for value, total, word in cloud:
            for exponent in range(1, 9):
                numerator = (value << exponent) - 1
                if numerator % 3:
                    continue
                child = numerator // 3
                if child % 3 == 0:
                    continue
                new_total = total + exponent
                if abs(new_total - 2 * i) > 8:
                    continue
                beta_num = (parent << new_total) - three_pow * child
                if not 0 < beta_num <= beta_bound << new_total:
                    continue
                record = child, new_total, word + (exponent,)
                assert child not in children, "Fixed-depth word collision"
                children[child] = record
        assert children, f"Sample cloud became empty at depth {i}"
        cloud = sorted(children.values(), key=lambda r: (
            abs(r[1] - 2 * i),
            (r[0] ^ (r[0] >> 61) ^ (r[0] >> 127)) % 1000000007,
            r[0],
        ))[:width]
    counts = Counter(total for _, total, _ in cloud)
    total = max(counts, key=lambda a: (counts[a], -abs(a - 2 * s)))
    fixed = [r for r in cloud if r[1] == total]
    assert 19 * s <= 10 * total <= 21 * s
    return total, fixed


def run_case(target: int, p: int, q: int, width: int) -> dict:
    beta_bound = 16
    s, phase = choose_depth(target, p, q)
    e, parent, C = choose_parent(target, s, beta_bound)
    total, cloud = selected_cloud(parent, s, beta_bound, width)
    sources = sorted(n for n, _, _ in cloud)
    assert len(sources) == len(set(sources))
    three_pow = pow(3, s)
    octaves = set()
    betas = []
    section_ratios = []
    word_digest = hashlib.sha256()
    for n, A, word in cloud:
        assert len(word) == s and sum(word) == total == A
        assert n > 0 and n % 2 == 1 and n % 3 != 0
        beta = Fraction((parent << A) - three_pow * n, 1 << A)
        assert 0 < beta <= beta_bound
        betas.append(beta)
        # Reconstruct every inverse step, including its exact ordinary clock.
        value = parent
        for a_i in word:
            assert ((value << a_i) - 1) % 3 == 0
            value = ((value << a_i) - 1) // 3
            assert value > 0 and value % 2 == 1
        assert value == n
        value = n
        for a_i in reversed(word):
            assert 3 * value + 1 > 0
            numerator = 3 * value + 1
            assert numerator % (1 << a_i) == 0
            value = numerator >> a_i
            assert value % 2 == 1
        assert value == parent
        # Independently replay the ordinary map at the promised common clocks.
        value = n
        for _ in range(A):
            value = shortcut(value)
        assert value == parent
        for _ in range(e):
            value = shortcut(value)
        assert value == target
        d = n.bit_length() - 1
        octaves.add(d)
        assert s <= 5 * (d + 1) and d + 1 <= s
        assert (d + 1) * (n - (1 << d)) <= 10 * (1 << d)
        section_ratios.append(Fraction((d + 1) * (n - (1 << d)), 1 << d))
        word_digest.update((str(n) + ":" + ",".join(map(str, word)) + "\n").encode())
    assert len(octaves) == 1
    d = next(iter(octaves))
    assert total + e <= 15 * (d + 1)
    H = Fraction(parent << total, three_pow)
    assert (1 << d) <= H < (1 << (d + 1))
    mass = Fraction(len(sources) * three_pow, 1 << total)
    # Exact normalized mass/count/height identity used after pigeonholing.
    assert Fraction(len(sources), 1) == mass * H / parent
    assert Fraction(len(sources), 1) >= mass * (1 << d) / (65 * C * s)
    return {
        "target": target, "rotation_approximant": {"p": p, "q": q},
        "rotation_phase_certificate": phase,
        "depth": s, "parent": str(parent), "parent_exponent": e,
        "fixed_total": total, "ordinary_common_clock": total + e,
        "distinct_sources": len(sources), "all_sources_are_units": True,
        "binary_octave": d, "section_constant_checked": 10,
        "max_exact_section_ratio": str(max(section_ratios)),
        "beta_min": str(min(betas)), "beta_max": str(max(betas)),
        "normalized_sample_mass": str(mass),
        "minimum_source": str(sources[0]), "maximum_source": str(sources[-1]),
        "word_cloud_sha256": word_digest.hexdigest(),
        "caveat": "Finite legal sample only; no uniform analytic atom-floor claim.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--width", type=int, default=256)
    args = parser.parse_args()
    cases = [run_case(a, 485, 306, args.width) for a in (1, 5, 7)]
    report = {
        "status": "passed", "arithmetic": "exact Python integers and Fraction",
        "claims": [
            "certified irrational-rotation approximant and phase interval",
            "positive odd legal inverse words with bounded real offsets",
            "distinct fixed-total sources in a single actual marked octave",
            "common ordinary shortcut clock to each supplied target",
            "exact normalized sample mass/count/height identity",
        ],
        "not_claimed": ["analytic uniform atom floor", "population asymptotic", "Collatz"],
        "cases": cases,
    }
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    for c in cases:
        print(f"target={c['target']} depth={c['depth']} sources={c['distinct_sources']} "
              f"octave={c['binary_octave']} common_clock={c['ordinary_common_clock']}: passed")


if __name__ == "__main__":
    main()
