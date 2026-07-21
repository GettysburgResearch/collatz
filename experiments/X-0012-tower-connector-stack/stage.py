#!/usr/bin/env python3
"""Stage-boundary checks for L-0021--L-0023 and O-0009."""

from __future__ import annotations

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys


RUN_PATH = Path(__file__).with_name("run.py")
SPEC = spec_from_file_location("x0012_run", RUN_PATH)
assert SPEC is not None and SPEC.loader is not None
CORE = module_from_spec(SPEC)
sys.modules[SPEC.name] = CORE
SPEC.loader.exec_module(CORE)


def v2_nonzero(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def rational_mod(value: Fraction, bits: int) -> int:
    modulus = 1 << bits
    return (value.numerator * pow(value.denominator, -1, modulus)) % modulus


def two_adic_bits(value: Fraction, length: int) -> tuple[int, ...]:
    p = value.numerator
    q = value.denominator
    assert q & 1
    out = []
    for _ in range(length):
        bit = p & 1
        out.append(bit)
        p = (p - bit * q) // 2
    return tuple(out)


def multiplicative_order(base: int, modulus: int) -> int:
    assert modulus > 1
    value = 1
    for order in range(1, modulus + 1):
        value = value * base % modulus
        if value == 1:
            return order
    raise AssertionError("order not found")


def verify_stage_odometer_frontier_bulk() -> None:
    expected = {
        5: (Fraction(19, 243), 162, "11111001110011001010"),
        6: (Fraction(38, 81), 54, "01011101101011001111"),
        7: (Fraction(76, 243), 162, "00111110011100110010"),
        8: (Fraction(638, 729), 486, "01001010001011001100"),
    }

    for typ in CORE.TYPES:
        base_edge = CORE.tower(typ, 0)
        omega_inf = Fraction(base_edge.c, 3**typ.g0)
        wanted, period, fingerprint = expected[typ.k0]
        assert omega_inf == wanted
        assert multiplicative_order(2, omega_inf.denominator) == period

        bits = two_adic_bits(-omega_inf, 2 * period)
        assert bits[:period] == bits[period:]
        for candidate in range(1, period):
            assert any(
                bits[i] != bits[i % candidate]
                for i in range(2 * period)
            )
        assert "".join(map(str, bits[:20])) == fingerprint

        for m in (12, 13, 14):
            H = m - typ.r - 6
            precision = H + 9
            start = 1 << m
            jump = 1 << (m - 7)
            base_omega = CORE.omega_mod(typ, start, precision)

            for j in range(1, 129):
                current = CORE.omega_mod(
                    typ,
                    start + j * jump,
                    precision,
                )
                difference = (current - base_omega) % (1 << precision)
                assert v2_nonzero(difference) == H + v2_nonzero(j)

            J = m - typ.r + 1
            assert CORE.omega_mod(typ, start, J) == rational_mod(omega_inf, J)

            # L-0023: quadratic moving-bulk recurrence at fixed precision.
            N = 48
            precision_y = m + 3 + N
            modulus_y = 1 << precision_y
            y = pow(
                pow(3, 7 * (1 << m), modulus_y),
                -1,
                modulus_y,
            )
            assert (y - 1) % (1 << (m + 2)) == 0
            u = ((y - 1) >> (m + 2)) % (1 << N)
            assert u & 1

            y_next = pow(
                pow(3, 7 * (1 << (m + 1)), modulus_y),
                -1,
                modulus_y,
            )
            assert (y_next - 1) % (1 << (m + 3)) == 0
            u_next = ((y_next - 1) >> (m + 3)) % (1 << N)
            predicted = (u + (1 << (m + 1)) * u * u) % (1 << N)
            assert u_next == predicted
            assert v2_nonzero((u_next - u) % (1 << N)) == m + 1


def main() -> None:
    verify_stage_odometer_frontier_bulk()
    print("verified stage odometer, periodic frontier, and quadratic bulk")
    print("all stage-boundary checks passed")


if __name__ == "__main__":
    main()
