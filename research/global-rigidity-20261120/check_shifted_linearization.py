#!/usr/bin/env python3
"""Exact finite identities for the OPEN shifted-linearization architecture."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import gcd
from pathlib import Path

from check_adic_real_density import require, valuation


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    products = strong_floors = cancellations = excess_t = sources = 0
    for source in range(1, 2001, 2):
        if source % 3 == 0:
            continue
        values, accumulated, gaps = [source], [0], []
        seen = {source}
        for _ in range(100):
            gap = valuation(3 * values[-1] + 1, 2)
            nxt = (3 * values[-1] + 1) // (1 << gap)
            if nxt in seen:
                break
            values.append(nxt)
            accumulated.append(accumulated[-1] + gap)
            gaps.append(gap)
            seen.add(nxt)
        lambdas = [Fraction(1 << a, 3**j) for j, a in enumerate(accumulated)]
        scaled = [lam * n for lam, n in zip(lambdas, values)]
        shifted = [lam * (n + 1) for lam, n in zip(lambdas, values)]
        formal_limit = shifted[-1]
        for j, gap in enumerate(gaps):
            require(
                shifted[j + 1] - shifted[j] == lambdas[j] * ((1 << gap) - 2) / 3,
                "exact shifted increment",
            )
        for j, (n, a, lam, m) in enumerate(zip(values, accumulated, lambdas, shifted)):
            s, t = valuation(n + 1, 2), valuation(n + 1, 3)
            k = min(j, t)
            p_raw, q_raw = (1 << a) * (n + 1), 3**j
            require(gcd(p_raw, q_raw) == 3**k, "raw pair gcd")
            p, q = p_raw // 3**k, q_raw // 3**k
            require(gcd(p, q) == 1, "primitive shifted pair")
            require(valuation(p, 2) == a + s and valuation(q, 2) == 0, "binary valuations")
            require(valuation(p, 3) == t - k and valuation(q, 3) == j - k, "ternary valuations")
            product = abs(formal_limit * q - p) * q * Fraction(1, (1 << (a + s)) * 3 ** (j + t - 2 * k))
            original_product = (formal_limit - scaled[j]) / lam
            require(product == (original_product - 1) / ((1 << s) * 3**t), "shifted product identity")
            require(product == (formal_limit - m) / (lam * (1 << s) * 3**t), "defect product identity")
            require(product >= 0, "formal tail nonnegative")
            if j + s < len(values):
                require(product >= Fraction(1, 3 ** (s + t)), "observed ordinary first-defect floor")
                strong_floors += 1
            require(q * (source + 1) >= (1 << j), "primitive height lower bound")
            for target in (Fraction(0), Fraction(1), Fraction(7, 3)):
                target_product = abs(target * q - p) * q * Fraction(1, (1 << (a + s)) * 3 ** (j + t - 2 * k))
                require(target_product >= abs(target - m) / m, "fixed wrong-target lower bound")
            products += 1
            cancellations += bool(k)
            excess_t += t > j
        sources += 1
    require(excess_t > 0, "t>j normalization cases must be covered")
    report = {
        "status": "PASS",
        "scope": "exact finite identities only; neither open global hypothesis is asserted",
        "tail": "formal eventual valuation-one continuation, not an ordinary infinite orbit",
        "ordinary_odd_unit_sources": sources,
        "source_limit": 2000,
        "maximum_odd_prefix_length": 100,
        "primitive_product_checks": products,
        "observed_first_defect_lower_bounds": strong_floors,
        "nontrivial_ternary_cancellations": cancellations,
        "ternary_valuation_greater_than_j_cases": excess_t,
        "fixed_target_inequality_checks": 3 * products,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
