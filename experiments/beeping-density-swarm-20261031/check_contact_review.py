#!/usr/bin/env python3
"""Independent exact bounded replay of CT-002's all-k proof certificate.

The universal argument is in CONTACT_REVIEW.md. This executable checks the
finite template certificates and symbolic polynomial comparisons on which
that argument rests, plus independently evaluated sample family members.
It does not infer any universal statement from samples.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def step(n: int) -> int:
    return (3 * n + 1) // 2 if n % 2 else n // 2


def valuation(n: int, p: int = 3) -> int:
    require(n != 0, "valuation of zero")
    n = abs(n)
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def g(n: int) -> int:
    return n * n // (3 ** valuation(n))


@lru_cache(maxsize=None)
def gamma(n: int) -> int:
    if n == 1:
        return 0
    best, x = g(n), n
    for j in range(1, n.bit_length()):
        x = step(x)
        if x != n:
            best = min(best, (4 ** j) * g(x - n))
    return best


@lru_cache(maxsize=None)
def phi(n: int) -> int:
    if n == 1:
        return 0
    base = gamma(n)
    best, x, power3, power4 = base, n, 1, 1
    while power3 * (n + 1) ** 2 > power4 * base:
        best = max(best, (gamma(x) + power3 - 1) // power3)
        x = step(x) if x != 1 else 1
        power3 *= 3
        power4 *= 4
    return best


def poly_square(a: F, b: F, scale: F = F(1)) -> tuple[F, F, F]:
    return (scale * b * b, scale * 2 * a * b, scale * a * a)


def poly_sub(a: tuple[F, ...], b: tuple[F, ...]) -> tuple[F, ...]:
    return tuple(x - y for x, y in zip(a, b))


def poly_scale(a: tuple[F, ...], c: F) -> tuple[F, ...]:
    return tuple(c * x for x in a)


def positive_from(poly: tuple[F, ...], n0: int) -> list[str]:
    """Certify nonnegativity on n>=n0 by coefficients in n-n0."""
    a, b, c = poly
    shifted = [a + b * n0 + c * n0 * n0, b + 2 * c * n0, c]
    require(all(v >= 0 for v in shifted), "negative shifted coefficient")
    require(any(v > 0 for v in shifted), "zero comparison polynomial")
    return [str(v) for v in shifted]


def finite_template(b: int, winning: int) -> dict:
    x, q, first, odd_to_first = b, 0, None, None
    rows = []
    for j in range(1, 51):
        q += x % 2
        x = step(x)
        if x == 1 and first is None:
            first, odd_to_first = j, q
        displacement = x - b
        require(displacement != 0, "template repeats its initial state")
        v = valuation(displacement)
        c = F(3 ** q, 2 ** j)
        delta = F(x) - c * b
        require(delta >= 0, "negative affine offset")
        rows.append({"j": j, "x": x, "q": q, "v": v,
                     "c": c, "delta": delta,
                     "leading": F((3 ** q - 2 ** j) ** 2, 3 ** v)})
    finite = [r for r in rows[:23] if r["j"] != winning]
    leading = min(r["leading"] for r in finite)
    margin = min(abs(r["c"] - 1) for r in finite)
    max_delta = max(r["delta"] for r in rows[:23])
    D = max(r["v"] for r in rows[:first + 2])
    expected = {
        115: (23, 10, 3, F(1), F(5, 32), F(97453, 32768)),
        173: (22, 9, 4, F(25, 27), F(1, 4), F(47633, 16384)),
    }[b]
    require((first, odd_to_first, D, leading, margin, max_delta) == expected,
            "template certificate differs from manuscript")
    require(all(r["v"] <= D for r in rows), "tail valuation exceeds D")
    for r in rows[23:]:
        require(r["c"] <= F(1, 2) and 0 <= r["delta"] <= 2,
                "template tail bound fails")
    return {"template": b, "first_one": first, "odd_count": odd_to_first,
            "D": D, "winning_prefix": winning,
            "minimum_other_leading": str(leading),
            "minimum_other_margin": str(margin),
            "maximum_offset_through_23": str(max_delta),
            "base_tail_q": rows[(24 if b == 115 else 23) - 1]["q"]}


def witness_polynomials() -> dict:
    # Write each state on the 115 parity template as a*n+b, exactly.
    states = [(F(1), F(0), 115)]
    for _ in range(12):
        a, b, x = states[-1]
        if x % 2:
            states.append((3 * a / 2, (3 * b + 1) / 2, step(x)))
        else:
            states.append((a / 2, b / 2, step(x)))
    expected = [poly_square(F(1), F(5), F(1, 3)),
                poly_square(F(1), F(1), F(3, 4)),
                poly_square(F(5), F(1), F(1, 16)),
                poly_square(F(5), F(1), F(1, 64)),
                poly_square(F(1), F(13), F(9, 256)),
                poly_square(F(9), F(-11), F(3, 1024))]
    lengths = [3, 1, 3, 3, 3, 2]
    rows = []
    for j, length in enumerate(lengths):
        a0, b0, x0 = states[j]
        a1, b1, x1 = states[j + length]
        a, b = a1 - a0, b1 - b0
        v = valuation(x1 - x0)
        # Perturbing n from 115 by 243*4^k leaves this valuation unchanged.
        shift_v = valuation(a.numerator) + 5
        require(shift_v > v, "witness valuation might cancel")
        actual = poly_square(a, b, F(4 ** length, 3 ** v))
        require(actual == expected[j], "witness polynomial mismatch")
        rows.append({"position": j, "template_state": x0,
                     "prefix_length": length, "displacement_v3": v,
                     "perturbation_v3": shift_v,
                     "polynomial_coefficients": [str(c) for c in actual]})
    comparisons = []
    for j in range(1, 5):
        comparisons.append({"source": "n", "position": j,
                            "shifted_coefficients": positive_from(
                                poly_sub(expected[0], poly_scale(expected[j], F(1, 3 ** j))), 115)})
        comparisons.append({"source": "y", "position": j,
                            "shifted_coefficients": positive_from(
                                poly_sub(expected[1], poly_scale(expected[j + 1], F(1, 3 ** j))), 115)})
    require(F(3, 4) ** 5 < F(1, 3), "universal Phi tail fails")
    return {"witnesses": rows, "envelope_polynomial_comparisons": comparisons}


def cutoff_certificate() -> dict:
    k0, a0 = 12, 4 ** 12
    B = F(3, 2) ** 8 * (F(1, 3) * F(3, 4) ** k0 + F(1, 81 * a0))
    require(B < F(1, 2), "long-prefix height cutoff fails at k=12")
    require(128 <= 243 + F(115, a0) < 256, "n logarithm floor")
    require(256 <= F(729, 2) + F(173, a0) < 512, "y logarithm floor")
    # a=4^k. Positive shifted coefficients prove these for every k>=12.
    n_4L = positive_from((F(-230), F(-486), F(1)), a0)
    y_4L = positive_from((F(-1384), F(-2916), F(1)), a0)
    early = positive_from(poly_sub(poly_square(F(1), F(0), F(3, 4)),
                                    poly_square(F(1), F(5), F(1, 3))), 240)
    require(F(4 ** 24, 16 * 81) > 1, "middle-prefix coefficient")
    return {"minimum_k": k0, "B_at_minimum_k": str(B),
            "exact_log_floors": {"n": "2k+7", "y": "2k+8"},
            "remaining_depths": {"n": 7, "y": 9},
            "n_fourL_minus_2u_shifted": n_4L,
            "y_fourL_minus_2u_scaled_shifted": y_4L,
            "early_candidate_margin_shifted_at_240": early}


def sample_family() -> list[dict]:
    rows = []
    for k in list(range(12, 33)) + [40, 60, 100]:
        n = 243 * 4 ** k + 115
        y = step(n)
        expected_n, expected_y = (n + 5) ** 2 // 3, (y + 1) ** 2 // 3
        require(n % 2 == y % 2 == 1 and n % 3 and y % 3, "family domain")
        require(gamma(n) == phi(n) == expected_n, "n rank formula")
        require(gamma(y) == phi(y) == expected_y, "y rank formula")
        for u, L in [(n, 2 * k), (y, 2 * k - 1)]:
            x = u
            for _ in range(L):
                x = step(x)
            require(x == 3 ** (k + 4) + 2, "common endpoint")
        require(expected_y > expected_n, "expanding contact edge")
        rows.append({"k": k, "n": str(n), "y": str(y),
                     "Gamma_n": str(expected_n), "Gamma_y": str(expected_y)})
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {"schema": "collatz-contact-independent-review/v1",
              "status": "PASS",
              "scope": "finite algebraic certificates and bounded samples; universal proof is in the review",
              "templates": [finite_template(115, 3), finite_template(173, 1)],
              "polynomials": witness_polynomials(),
              "cutoff": cutoff_certificate(),
              "sample_family": sample_family(),
              "full_Collatz_proved": False,
              "formal_proof_assistant_build": False}
    content = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
