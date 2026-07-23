#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

A = 4_992_586_555_009
K = 3_149_971_404_836
M = 1_465_129_870_107_858_983
N = 110_340_992_901_879
ETA = Fraction(472_855_261_523, 2_000_000_000_000_000_000_000_000)


def log_interval_unit(y: Fraction, count: int = 140) -> tuple[Fraction, Fraction]:
    assert 1 <= y <= 2
    z = (y - 1) / (y + 1)
    square = z * z
    power = z
    total = Fraction(0)
    for index in range(count):
        total += power / (2 * index + 1)
        power *= square
    low = 2 * total
    high = low + 2 * power / ((2 * count + 1) * (1 - square))
    return low, high


LN2_LOW, LN2_HIGH = log_interval_unit(Fraction(2))


def log_interval(x: Fraction) -> tuple[Fraction, Fraction]:
    assert x > 0
    exponent = x.numerator.bit_length() - x.denominator.bit_length()
    two_power = Fraction(2**exponent) if exponent >= 0 else Fraction(1, 2 ** (-exponent))
    reduced = x / two_power
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    low, high = log_interval_unit(reduced)
    if exponent >= 0:
        return exponent * LN2_LOW + low, exponent * LN2_HIGH + high
    return exponent * LN2_HIGH + low, exponent * LN2_LOW + high


def replay(seed: int) -> tuple[int, int, int, str]:
    value = seed
    steps = 0
    odd = 0
    maximum = seed
    transcript = hashlib.sha256()
    while True:
        transcript.update((str(value) + "\n").encode("ascii"))
        if value == 1:
            return steps, odd, maximum, transcript.hexdigest()
        if value % 2:
            value = (3 * value + 1) // 2
            odd += 1
        else:
            value //= 2
        maximum = max(maximum, value)
        steps += 1


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results/canonical.json")
    frozen = json.loads(path.read_text(encoding="utf-8"))

    ln3_low, ln3_high = log_interval(Fraction(3))
    theta_low = A * LN2_LOW - K * ln3_high
    theta_high = A * LN2_HIGH - K * ln3_low
    assert 0 < theta_low < theta_high < Fraction(1, 2**41)
    assert ETA < Fraction(1, 2**41)
    assert M > 2**60

    ln_m_low, _ln_m_high = log_interval(Fraction(M))
    _ln_theta_low, ln_theta_high = log_interval(theta_high)
    _ln_eta_low, ln_eta_high = log_interval(ETA)
    bound = A * LN2_HIGH + ln_theta_high + ln_eta_high
    sharp = int(bound // ln_m_low + 1)
    assert sharp == 82_733_048_428
    assert (A - 82 + 59) // 60 == 83_209_775_916

    assert N % 16 == 7
    assert N % 16 not in (0, 5, 13)
    orbit = replay(2 * N + 1)
    assert orbit == (
        208,
        101,
        1_885_279_308_409_466,
        "8bc3a42902ca549896d71533c3534a5899bc89ffadd0f217bd50d487cdcf7012",
    )

    assert frozen["height_certificate"]["range_reduced_log_sufficient_M_exponent"] == sharp
    assert frozen["height_certificate"]["coarse_sufficient_M_exponent"] == 83_209_775_916
    assert frozen["height_certificate"]["difference_abs_lt_2_power"] == A - 82
    assert frozen["nstar_refutation"]["N_star_mod_16"] == 7
    assert frozen["nstar_refutation"]["shortcut_steps_to_1"] == orbit[0]
    assert frozen["nstar_refutation"]["trajectory_sha256"] == orbit[3]
    assert frozen["published_x8302_floor_gate"]["floor_mod_16"] == 0
    assert frozen["published_x8302_floor_gate"]["frozen_first_chart_symbol"] == 1
    assert frozen["ladder_budget"]["coarse_bit_deficit"] == (A - 82) - 420

    print("X-8303 independent height and dyadic-gate checks passed")


if __name__ == "__main__":
    main()
