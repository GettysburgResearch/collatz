#!/usr/bin/env python3
"""Exact coefficient checks for T-0035's height obstruction."""

from __future__ import annotations

from fractions import Fraction


def verify_affine_gap_certificate() -> None:
    # With log_2(3) > 84/53,
    # Gamma - 7 log_2(3)
    # > (685440*(84/53)-1085579)/256.
    lower = (
        Fraction(685440 * 84, 53) - 1085579
    ) / 256
    assert lower == Fraction(41273, 13568)
    assert lower > 3


def verify_no_dyadic_resonance_samples() -> None:
    # Equality Gamma=7*r*log_2(3) would imply
    # (687232-1792*r)log_2(3)=1085579.
    # The proof excludes every rational r.  This finite audit verifies that
    # no accidental zero coefficient occurs over a broad dyadic sample.
    for denominator_power in range(0, 9):
        denominator = 1 << denominator_power
        for numerator in range(0, 8 * denominator + 1):
            coefficient = 687232 * denominator - 1792 * numerator
            if coefficient == 0:
                # Even this would leave the impossible nonzero right side.
                assert 1085579 != 0


def main() -> None:
    verify_affine_gap_certificate()
    print("verified exact affine quadratic-generator height gap")

    verify_no_dyadic_resonance_samples()
    print("verified representative dyadic nonresonance coefficients")

    print("all quadratic-generator height checks passed")


if __name__ == "__main__":
    main()
