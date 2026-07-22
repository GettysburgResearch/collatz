#!/usr/bin/env python3
"""Exact finite checks for the bridge identities in T-0034."""

from __future__ import annotations

from fractions import Fraction


def verify_finite_bridge_identity() -> None:
    binary_radix = 1 << 10
    connector_word = 64 * binary_radix - 8
    residual = 456
    scaled_tail = connector_word + 64 * binary_radix * residual

    residual_scale = Fraction(7, 5)
    homogeneous_scale = 64 * binary_radix * residual_scale
    defect = Fraction(1, 3)
    room = Fraction(scaled_tail, 1) / homogeneous_scale + defect / homogeneous_scale

    assert room * homogeneous_scale - scaled_tail == defect
    assert (
        room * residual_scale - residual
        == Fraction(connector_word, 64 * binary_radix)
        + Fraction(defect, 64 * binary_radix)
    )
    assert 0 < room * residual_scale - residual < 1
    point = room * residual_scale
    assert residual == point.numerator // point.denominator


def verify_residual_scale_exponents() -> None:
    for m in range(12, 25):
        scale = 1 << m
        t1 = scale + (scale >> 8)

        a_m = (5369 * scale) // 2 + 1792 * m
        e_m = (8459 * scale) // 2 + 2816 * m
        head_depth = 11 * (t1 + 1)
        residual_depth = e_m + head_depth + 6

        assert residual_depth == (
            (1085579 * scale) // 256 + 2816 * m + 17
        )

        # The leading logarithmic coefficient is the same exact expression
        # as the full-stage surplus Gamma in T-0024.
        assert 256 * a_m == 687232 * scale + 458752 * m
        assert (
            256 * residual_depth
            == 1085579 * scale + 720896 * m + 4352
        )

        # The connector word always leaves a strict gap below its 64*T box.
        for p in (5, 30, 20, 56):
            maximum_word = p + 64 * (binary_radix_for_depth(head_depth) - 1)
            assert maximum_word <= 64 * binary_radix_for_depth(head_depth) - 8


def binary_radix_for_depth(depth: int) -> int:
    return 1 << depth


def main() -> None:
    verify_finite_bridge_identity()
    print("verified exact finite room-connector bridge identity")

    verify_residual_scale_exponents()
    print("verified residual homogeneous scale and connector gap")

    print("all adelic bridge checks passed")


if __name__ == "__main__":
    main()
