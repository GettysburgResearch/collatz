#!/usr/bin/env python3
"""Exact controls for ORDINARY_SELECTOR.md; no floating-point proof checks."""

from __future__ import annotations

from fractions import Fraction
import json


class ControlFailure(RuntimeError):
    pass


CHECKS = 0


def require(condition: bool, explanation: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise ControlFailure(explanation)


def odd_step(q: int) -> tuple[int, int]:
    require(q > 0 and q % 2 == 1, "odd_step requires a positive odd source")
    numerator = 3 * q + 1
    gap = (numerator & -numerator).bit_length() - 1
    endpoint = numerator >> gap
    require(gap >= 1 and endpoint % 2 == 1, "literal valuation failure")
    return endpoint, gap


def replay(q: int, word: list[int]) -> list[int]:
    states = [q]
    for expected in word:
        q, gap = odd_step(q)
        require(gap == expected, f"claimed gap {expected} was actually {gap}")
        states.append(q)
    return states


def completed_tail(q: int, budget: int = 20_000) -> tuple[list[int], int]:
    """Finite controls only: fail explicitly if this supplied budget is exhausted."""
    gaps: list[int] = []
    maximum_bits = q.bit_length()
    while q != 1 and len(gaps) < budget:
        q, gap = odd_step(q)
        gaps.append(gap)
        maximum_bits = max(maximum_bits, q.bit_length())
    require(q == 1, "finite control tail did not finish within its stated budget")
    return gaps, maximum_bits


def exact_terminal_scalar(gaps: list[int]) -> Fraction:
    """A completed actual tail has h(1)=1; compare two exact evaluations."""
    result = Fraction(1)
    for gap in reversed(gaps):
        result = (gap + result) / 3
    numerator = 0
    for gap in gaps:
        numerator = 3 * numerator + gap
    direct = Fraction(numerator + 1, 3 ** len(gaps))
    require(result == direct, "reverse scalar recurrence and direct sum differ")
    return result


def control(m: int) -> dict[str, int]:
    require(m >= 1, "construction parameter must be positive")
    a = m + 5
    denominator = 9 ** (m + 1)
    coefficient = 1 << (a + 4)
    residue = (-13 * pow(coefficient, -1, denominator)) % denominator
    require(0 < residue < denominator, "residue must be nonzero")
    t = residue if residue % 2 else residue + denominator
    require(0 < t < 2 * denominator and t % 2 == 1, "odd representative failure")
    require((coefficient * t + 13) % denominator == 0, "source congruence failure")
    u = (coefficient * t + 13) // denominator
    require(u > 0 and u % 2 == 1, "u must be a positive odd integer")
    q = (1 << (3 * m + 1)) * u - 7
    r = (1 << a) * t - 1
    require(0 < q < (1 << (4 * m + 11)), "source size bound failed")
    require(0 < r < (1 << (5 * m + 10)), "endpoint size bound failed")

    word = [2, 1] * m + [1, 4]
    states = replay(q, word)
    require(states[-1] == r, "literal composite endpoint differs from formula")
    for j in range(m + 1):
        expected = 9**j * (1 << (3 * (m - j) + 1)) * u - 7
        require(states[2 * j] == expected, "complete L iterate identity failed")
        if j < m:
            require(expected % 16 == 9, "L source class failed")
    require(states[2 * m] % 64 == 3, "P source class failed")
    slope = Fraction(9 ** (m + 1), 1 << (3 * m + 5))
    require(r == slope * q + 7 * slope - Fraction(29, 16), "full affine map failed")
    if slope > 1:
        require(Fraction(r, q) > slope, "positive affine remainder was lost")

    tail_prefix = replay(r, [1] * (a - 1))
    for k, source in enumerate(tail_prefix):
        require(source == 3**k * (1 << (a - k)) * t - 1, "gap-one prefix formula failed")
    v = 2 * 3 ** (a - 1) * t - 1
    require(tail_prefix[-1] == v, "tail endpoint formula failed")
    require(v < (1 << (2 * a + 4 * m + 4)), "tail endpoint size bound failed")
    require(48 * m + 124 < 3 ** (m + 5), "exponential bound failed")
    lower = Fraction(1, 2)
    upper = lower + Fraction(12 * m + 31, 6 * 3 ** (m + 4))
    bit_upper = lower + (Fraction(v.bit_length() + 3, 3) - lower) / 3 ** (a - 1)
    require(lower < bit_upper <= upper < Fraction(5, 8), "unconditional scalar enclosure failed")

    # These intervals use only an actual finite prefix and the unconditional
    # scalar bounds. No terminating tail is needed for this part of the control.
    intervals = [(lower, upper)]
    for gap in reversed(word):
        lower, upper = (gap + lower) / 3, (gap + upper) / 3
        intervals.append((lower, upper))
    intervals.reverse()
    require(len(intervals) == 2 * m + 3, "state/interval count mismatch")
    high_count = sum(lo >= 1 for lo, _ in intervals)
    low_count = sum(hi <= 1 for _, hi in intervals)
    require(high_count == 1 and low_count == 2 * m + 2, "actual scalar phase pattern failed")
    for j in range(m + 1):
        lo, hi = intervals[2 * j]
        require(Fraction(5, 6) <= lo < hi < Fraction(7, 8), "boundary scalar interval failed")
        if j < m:
            lo, hi = intervals[2 * j + 1]
            require(Fraction(1, 2) < lo < hi < Fraction(5, 8), "L intermediate interval failed")
    lo, hi = intervals[2 * m + 1]
    require(Fraction(3, 2) <= lo < hi < Fraction(37, 24), "P intermediate interval failed")

    # Separate finite evidence: every selected example has a completed ordinary
    # trajectory. This gives exact h values, without being used above.
    tail_gaps, maximum_bits = completed_tail(r)
    b = exact_terminal_scalar(tail_gaps)
    hq = exact_terminal_scalar(word + tail_gaps)
    require(Fraction(1, 2) < b < bit_upper, "exact endpoint scalar escaped enclosure")
    require(hq == Fraction(7, 8) + (b - Fraction(7, 8)) / denominator, "scalar composite failed")
    require(Fraction(1, 4 * denominator) < Fraction(7, 8) - hq < Fraction(3, 8 * denominator),
            "actual denominator-eight approximation bound failed")
    scalar = b
    exact_scalars = [b]
    for gap in reversed(word):
        scalar = (gap + scalar) / 3
        exact_scalars.append(scalar)
    exact_scalars.reverse()
    for scalar, (lo, hi) in zip(exact_scalars, intervals):
        require(lo < scalar < hi, "completed actual scalar escaped prefix enclosure")
    potential_ratio = Fraction(r, q) * hq / b
    require(potential_ratio > Fraction(4, 3) * Fraction(r, q), "q/h expansion bound failed")

    return {
        "m": m,
        "a": a,
        "source_bits": q.bit_length(),
        "endpoint_bits": r.bit_length(),
        "prefix_odd_steps": len(word),
        "high_scalar_states": high_count,
        "low_scalar_states": low_count,
        "endpoint_source_ratio_floor": r // q,
        "potential_ratio_floor": potential_ratio.numerator // potential_ratio.denominator,
        "completed_odd_steps": len(word) + len(tail_gaps),
        "tail_maximum_bits": maximum_bits,
    }


def run_checks() -> dict[str, object]:
    global CHECKS
    CHECKS = 0
    parameters = list(range(1, 17)) + [24, 32, 64, 128]
    cases = [control(m) for m in parameters]
    return {
        "status": "PASS",
        "scope": "selected exact ordinary constructions; no universal termination inference",
        "cases": cases,
        "checks": CHECKS,
    }


def main() -> None:
    print(json.dumps(run_checks(), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
