#!/usr/bin/env python3
"""Proof-producing computation for T-8260.

The author-side program has two logically separate parts:

* an exact finite exhaustive computation, including L-8201-style reduced
  resultants and coordinate caps;
* exact rational certificates for every native step after the quoted
  two-logarithm Matveev bound.

The Matveev statement itself remains an external, source-dependent input.
Only Python integers, Fraction, and the standard library are used.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import itertools
import json
import math
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence

sys.set_int_max_str_digits(0)

EXPERIMENT_ID = "X-8260"
CLAIM_ID = "T-8260"
CERTIFICATE_FORMAT = "X-8260-finite-tuples-v1"
LOG_TERMS = 180
MATVEEV_C2 = 2**32


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if not self.lo < self.hi:
            raise ValueError("invalid interval")


@dataclass(frozen=True)
class Family:
    name: str
    base: tuple[int, ...]
    A: int
    k: int
    cmax: int
    cutoff: int
    half_start: int
    legendre_start: int
    transition: tuple[int, ...]
    finite_repetitions: tuple[int, ...]
    structurally_empty: tuple[int, ...] = ()


FAMILIES = (
    Family(
        name="P3",
        base=(1, 2),
        A=3,
        k=2,
        cmax=7,
        cutoff=200_000_000_000,
        half_start=4,
        legendre_start=10,
        transition=(4, 5, 6, 7, 8, 9),
        finite_repetitions=(2, 3),
        structurally_empty=(1,),
    ),
    Family(
        name="P11",
        base=(1, 1, 1, 2, 1, 1, 4),
        A=11,
        k=7,
        cmax=91,
        cutoff=50_000_000_000,
        half_start=2,
        legendre_start=3,
        transition=(2,),
        finite_repetitions=(1,),
    ),
)


def fraction_sha256(value: Fraction) -> str:
    text = f"{value.numerator}/{value.denominator}".encode("ascii")
    return hashlib.sha256(text).hexdigest()


def decimal_floor(value: Fraction, digits: int = 18) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10**digits
    scaled = value.numerator * scale // value.denominator
    whole, remainder = divmod(scaled, scale)
    return f"{sign}{whole}.{remainder:0{digits}d}"


def positive_margin(value: Fraction, digits: int = 18) -> dict[str, object]:
    if value <= 0:
        raise AssertionError("claimed margin is not positive")
    return {
        "decimal_lower": decimal_floor(value, digits),
        "fraction_sha256": fraction_sha256(value),
    }


def atanh_log_interval(z: Fraction, terms: int = LOG_TERMS) -> Interval:
    """Return an interval for 2*atanh(z) using a geometric tail bound."""
    if not Fraction(0) <= z < 1:
        raise ValueError("atanh series outside [0,1)")
    total = Fraction(0)
    power = z
    square = z * z
    for index in range(terms):
        total += 2 * power / (2 * index + 1)
        power *= square
    tail = 2 * power / ((2 * terms + 1) * (1 - square))
    return Interval(total, total + tail)


def log_interval(value: Fraction, terms: int = LOG_TERMS) -> Interval:
    if value <= 0:
        raise ValueError("logarithm domain")
    log2 = atanh_log_interval(Fraction(1, 3), terms)
    if value == 2:
        return log2
    shift = value.numerator.bit_length() - value.denominator.bit_length()
    mantissa = value / (2**shift) if shift >= 0 else value * 2 ** (-shift)
    while mantissa < 1:
        shift -= 1
        mantissa *= 2
    while mantissa >= 2:
        shift += 1
        mantissa /= 2
    core = atanh_log_interval((mantissa - 1) / (mantissa + 1), terms)
    if shift >= 0:
        return Interval(
            shift * log2.lo + core.lo,
            shift * log2.hi + core.hi,
        )
    return Interval(
        shift * log2.hi + core.lo,
        shift * log2.lo + core.hi,
    )


LOG2 = log_interval(Fraction(2))
LOG3 = log_interval(Fraction(3))


def log_integer(value: int) -> Interval:
    return log_interval(Fraction(value))


def eta_interval(A: int, k: int) -> Interval:
    """Certified interval for eta=log_2(3^k/2^A)."""
    lo = (k * LOG3.lo - A * LOG2.hi) / LOG2.hi
    hi = (k * LOG3.hi - A * LOG2.lo) / LOG2.lo
    if lo <= 0:
        raise AssertionError("eta must be positive")
    return Interval(lo, hi)


def interval_width_power(interval: Interval) -> int:
    """Largest n certified by width(interval)<2^-n."""
    width = interval.hi - interval.lo
    exponent = 0
    while width < Fraction(1, 2 ** (exponent + 1)):
        exponent += 1
    return exponent


def continued_fraction_rows(interval: Interval, stop_q: int) -> list[dict[str, object]]:
    original = interval
    lo, hi = interval.lo, interval.hi
    p_previous, p_current = 0, 1
    q_previous, q_current = 1, 0
    rows: list[dict[str, object]] = []
    for index in range(256):
        digit_lo = lo.numerator // lo.denominator
        digit_hi = hi.numerator // hi.denominator
        if digit_lo != digit_hi:
            raise AssertionError(f"continued fraction unresolved at row {index}")
        digit = digit_lo
        p = digit * p_current + p_previous
        q = digit * q_current + q_previous
        convergent = Fraction(p, q)
        if convergent < original.lo:
            side = "below"
        elif convergent > original.hi:
            side = "above"
        else:
            raise AssertionError("convergent lies in unresolved interval")
        rows.append(
            {
                "index": index,
                "partial_quotient": digit,
                "p": p,
                "q": q,
                "side": side,
            }
        )
        if q > stop_q:
            return rows
        lo, hi = 1 / (hi - digit), 1 / (lo - digit)
        p_previous, p_current = p_current, p
        q_previous, q_current = q_current, q
    raise AssertionError("continued fraction did not pass cutoff")


def decay_exponent(k: int, repetition: int) -> int:
    return (2 * k * repetition) // 3


def half_bound_certificate(spec: Family) -> dict[str, object]:
    """Certify c*3^floor(2kr/3)/2^(Ar)<1/2 for all r in range."""
    base_rows = []
    for repetition in range(spec.half_start, spec.half_start + 3):
        margin = 2 ** (spec.A * repetition) - (
            2 * spec.cmax * 3 ** decay_exponent(spec.k, repetition)
        )
        if margin <= 0:
            raise AssertionError("one-half threshold fails")
        base_rows.append({"r": repetition, "integer_margin": margin})
    step_ratio = Fraction(3 ** (2 * spec.k), 2 ** (3 * spec.A))
    if step_ratio >= 1:
        raise AssertionError("one-half residue sequence does not decrease")
    return {
        "first_r": spec.half_start,
        "residue_modulus": 3,
        "base_rows": base_rows,
        "three_step_ratio": f"{step_ratio.numerator}/{step_ratio.denominator}",
    }


def transition_certificate(spec: Family) -> list[dict[str, object]]:
    """Reject repetitions before Legendre using total pulse height t>=3."""
    rows = []
    for repetition in spec.transition:
        lower = (
            (spec.A * repetition + 3) * LOG2.lo
            - spec.k * repetition * LOG3.hi
        )
        upper = Fraction(
            2 * spec.cmax * 3 ** decay_exponent(spec.k, repetition),
            2 ** (spec.A * repetition),
        )
        margin = lower - upper
        rows.append(
            {
                "r": repetition,
                "minimum_total_pulse": 3,
                "lambda_lower_minus_upper": positive_margin(margin),
            }
        )
    return rows


def matveev_certificate(spec: Family) -> dict[str, object]:
    """Certify the finite cutoff conditional on the quoted Matveev theorem."""
    if LOG3.lo <= 1:
        raise AssertionError("log(3)>1 certificate failed")
    rho = Fraction(2, 3)
    rate_lo = spec.A * LOG2.lo - rho * spec.k * LOG3.hi
    rate_hi = spec.A * LOG2.hi - rho * spec.k * LOG3.lo
    if rate_lo <= 0:
        raise AssertionError("nonpositive exponential decay rate")
    constant_hi = MATVEEV_C2 * LOG2.hi * LOG3.hi
    log_c_hi = log_integer(2 * spec.cmax).hi
    log_B_hi = log_integer(spec.k * spec.cutoff + 1).hi
    margin = (
        spec.cutoff * rate_lo
        - log_c_hi
        - constant_hi * (1 + log_B_hi)
    )
    derivative = rate_lo - constant_hi * Fraction(
        spec.k, spec.k * spec.cutoff + 1
    )
    lambda_lt_one_margin = spec.cutoff * rate_lo - log_c_hi
    if rate_hi <= rate_lo:
        raise AssertionError("rate interval")
    return {
        "quoted_constant_multiplier": MATVEEV_C2,
        "cutoff": spec.cutoff,
        "effective_rate": {
            "lo_sha256": fraction_sha256(rate_lo),
            "hi_sha256": fraction_sha256(rate_hi),
            "lo_decimal": decimal_floor(rate_lo),
        },
        "cutoff_margin": positive_margin(margin, 12),
        "derivative_margin": positive_margin(derivative),
        "lambda_lt_one_margin": positive_margin(lambda_lt_one_margin, 12),
    }


def legendre_certificate(spec: Family) -> dict[str, object]:
    """Certify |t/r-eta|<1/(2r^2) in three residue classes."""
    rows = []
    for repetition in range(spec.legendre_start, spec.legendre_start + 3):
        right = 2 ** (spec.A * repetition) * LOG2.lo
        left = (
            4
            * spec.cmax
            * repetition
            * 3 ** decay_exponent(spec.k, repetition)
        )
        rows.append(
            {
                "r": repetition,
                "margin": positive_margin(right - left, 12),
            }
        )
    exponential_step = Fraction(3 ** (2 * spec.k), 2 ** (3 * spec.A))
    ratio_bound = Fraction(
        spec.legendre_start + 3, spec.legendre_start
    ) * exponential_step
    if ratio_bound >= 1:
        raise AssertionError("Legendre residue sequences do not decrease")
    return {
        "first_r": spec.legendre_start,
        "residue_modulus": 3,
        "base_rows": rows,
        "three_step_ratio_upper": (
            f"{ratio_bound.numerator}/{ratio_bound.denominator}"
        ),
    }


def comparison_certificate(
    spec: Family, p: int, q: int, q_next: int
) -> dict[str, object]:
    right_coefficient = 4 * spec.cmax * (q + q_next)
    step_exponent = (2 * spec.k * q + 2) // 3
    step_decay_margin = (
        spec.A * q * LOG2.lo - step_exponent * LOG3.hi
    )
    if step_decay_margin <= 0:
        raise AssertionError("multiple-family upper bound does not decrease")
    margin = (
        spec.A * q * LOG2.lo
        - decay_exponent(spec.k, q) * LOG3.hi
        - log_integer(right_coefficient).hi
    )
    return {
        "p": p,
        "q": q,
        "q_next": q_next,
        "floor_2kq_over_3": decay_exponent(spec.k, q),
        "multiple_step_ceiling_exponent": step_exponent,
        "multiple_step_decay_log_margin": positive_margin(
            step_decay_margin, 12
        ),
        "all_positive_multiples_rejected": True,
        "log_margin": positive_margin(margin, 12),
    }


def exceptional_one_fifth() -> dict[str, object]:
    """Reject (r,t)=m(5,1); three pulses force m>=3."""
    minimum_m = 3
    left = 1 - Fraction(59049, 65536) ** minimum_m
    right = Fraction(
        7 * 3 ** ((20 * minimum_m) // 3),
        8 ** (5 * minimum_m),
    )
    margin = left - right
    step_ratio = Fraction(3**7, 8**5)
    if step_ratio >= 1:
        raise AssertionError("exceptional upper bound does not decrease")
    if margin <= 0:
        raise AssertionError("exceptional 1/5 row not rejected")
    return {
        "p": 1,
        "q": 5,
        "minimum_multiple_m": minimum_m,
        "reason_for_minimum": "three distinct positive pulses imply t=m>=3",
        "exact_margin_numerator": margin.numerator,
        "exact_margin_denominator": margin.denominator,
        "upper_bound_step_ratio_at_most": (
            f"{step_ratio.numerator}/{step_ratio.denominator}"
        ),
        "all_m_at_least_3_rejected": True,
    }


def analytic_case(spec: Family) -> dict[str, object]:
    eta = eta_interval(spec.A, spec.k)
    rows = continued_fraction_rows(eta, spec.cutoff)
    ordinary = []
    exceptional = []
    for index, row in enumerate(rows[:-1]):
        if row["side"] != "above" or int(row["q"]) >= spec.cutoff:
            continue
        p, q = int(row["p"]), int(row["q"])
        q_next = int(rows[index + 1]["q"])
        if spec.name == "P3" and (p, q) == (1, 5):
            exceptional.append(exceptional_one_fifth())
        else:
            ordinary.append(comparison_certificate(spec, p, q, q_next))
    return {
        "name": spec.name,
        "base": list(spec.base),
        "A": spec.A,
        "k": spec.k,
        "cmax": spec.cmax,
        "support_span_bound": "p3 <= floor(2*k*r/3)",
        "half_bound": half_bound_certificate(spec),
        "transition_rejections": transition_certificate(spec),
        "matveev": matveev_certificate(spec),
        "eta_interval": {
            "lo_sha256": fraction_sha256(eta.lo),
            "hi_sha256": fraction_sha256(eta.hi),
            "width_lt_2_power": interval_width_power(eta),
        },
        "legendre": legendre_certificate(spec),
        "continued_fraction_rows": rows,
        "uniform_candidate_rejections": ordinary,
        "exceptional_rows": exceptional,
        "finite_repetitions": list(spec.finite_repetitions),
        "structurally_empty_repetitions": list(spec.structurally_empty),
    }


def v2(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0)")
    value = abs(value)
    return (value & -value).bit_length() - 1


def prefixes(word: Sequence[int]) -> list[int]:
    out = [0]
    for valuation in word:
        if valuation < 1:
            raise ValueError("accelerated valuations must be positive")
        out.append(out[-1] + valuation)
    return out


def affine_numerator(word: Sequence[int]) -> int:
    pref = prefixes(word)
    length = len(word)
    return sum(
        3 ** (length - 1 - index) * 2 ** pref[index]
        for index in range(length)
    )


def rotate(word: Sequence[int], amount: int) -> tuple[int, ...]:
    amount %= len(word)
    return tuple(word[amount:]) + tuple(word[:amount])


def negative_cycle(
    word: Sequence[int],
) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    pref = prefixes(word)
    denominator = 2 ** pref[-1] - 3 ** len(word)
    numerator = affine_numerator(word)
    if numerator % denominator:
        raise AssertionError("negative baseline is not integral")
    start = numerator // denominator
    if start >= 0 or start % 2 == 0:
        raise AssertionError("baseline is not a negative odd cycle")
    states = [start]
    current = start
    for valuation in word:
        raw = 3 * current + 1
        if v2(raw) != valuation:
            raise AssertionError("baseline valuation mismatch")
        current = raw // 2**valuation
        states.append(current)
    if current != start:
        raise AssertionError("baseline does not close")
    return start, tuple(states), tuple(pref)


def exact_replay(word: Sequence[int], start: int) -> bool:
    if start <= 0 or start % 2 == 0:
        return False
    current = start
    for valuation in word:
        raw = 3 * current + 1
        if v2(raw) != valuation:
            return False
        current = raw // 2**valuation
    return current == start


def normalize_three_support(
    primitive_length: int,
    repeated_length: int,
    initial_rotation: int,
    support: Sequence[int],
) -> tuple[int, int, int]:
    """Rotate a largest cyclic support gap to the end, with a fixed tie rule."""
    chosen = tuple(sorted(support))
    if len(chosen) != 3 or len(set(chosen)) != 3:
        raise ValueError("exactly three distinct support positions required")
    gaps = tuple(
        (chosen[(index + 1) % 3] - chosen[index]) % repeated_length
        for index in range(3)
    )
    largest = max(gaps)
    candidates = []
    for index, gap in enumerate(gaps):
        if gap != largest:
            continue
        new_zero = chosen[(index + 1) % 3]
        translated = sorted(
            (position - new_zero) % repeated_length for position in chosen
        )
        if translated[0] != 0:
            raise AssertionError("normalization failed")
        candidates.append(
            (
                (initial_rotation + new_zero) % primitive_length,
                translated[1],
                translated[2],
            )
        )
    normalized = min(candidates)
    if normalized[2] > (2 * repeated_length) // 3:
        raise AssertionError("largest-gap span bound failed")
    return normalized


def normalized_packet_keys(
    spec: Family, repetition: int
) -> tuple[list[tuple[int, int, int]], dict[str, object]]:
    length = spec.k * repetition
    keys: dict[tuple[int, int, int], int] = {}
    digest = hashlib.sha256()
    raw_count = 0
    for initial_rotation in range(spec.k):
        for support in itertools.combinations(range(length), 3):
            normalized = normalize_three_support(
                spec.k, length, initial_rotation, support
            )
            keys[normalized] = keys.get(normalized, 0) + 1
            raw_count += 1
            digest.update(
                (
                    f"{spec.name}|{repetition}|{initial_rotation}|"
                    f"{','.join(map(str, support))}|"
                    f"{','.join(map(str, normalized))}\n"
                ).encode("ascii")
            )
    ordered = sorted(keys)
    if set(key[0] for key in ordered) != set(range(spec.k)):
        raise AssertionError("not every primitive rotation is represented")
    return ordered, {
        "family": spec.name,
        "r": repetition,
        "raw_rotation_support_configurations": raw_count,
        "normalized_packets": len(ordered),
        "primitive_rotations": sorted(set(key[0] for key in ordered)),
        "maximum_p3": max(key[2] for key in ordered),
        "floor_2kr_over_3": (2 * length) // 3,
        "normalization_transcript_sha256": digest.hexdigest(),
        "preimage_multiplicities": [
            {
                "rotation": key[0],
                "p2": key[1],
                "p3": key[2],
                "count": keys[key],
            }
            for key in ordered
        ],
    }


@dataclass(frozen=True)
class Packet:
    family: str
    repetition: int
    rotation: int
    word: tuple[int, ...]
    support: tuple[int, int, int]
    z0: int
    states: tuple[int, ...]
    pref: tuple[int, ...]
    U: int
    Q: int
    common: int
    weights: tuple[int, int, int]
    coefficients: tuple[int, int, int, int]
    lambdas: tuple[int, int, int]
    caps: tuple[int, int, int]
    max_heights: tuple[int, int, int]


def compile_packet(
    spec: Family,
    repetition: int,
    key: tuple[int, int, int],
) -> Packet:
    rotation, p2, p3 = key
    word = rotate(spec.base * repetition, rotation)
    support = (0, p2, p3)
    z0, states, pref = negative_cycle(word)
    length = len(word)
    U = 2 ** pref[-1]
    Q = 3**length
    common = 2 ** word[0] * 3 ** (length - 1 - p3)
    weights = tuple(
        (-states[position + 1])
        * 3 ** (p3 - position)
        * 2 ** (pref[position + 1] - word[0])
        for position in support
    )
    full_weights = tuple(
        (-states[position + 1])
        * 3 ** (length - 1 - position)
        * 2 ** pref[position + 1]
        for position in support
    )
    if tuple(common * weight for weight in weights) != full_weights:
        raise AssertionError("reduced pulse weights do not reconstruct")
    if not weights[0] > weights[1] > weights[2] > 0:
        raise AssertionError("distributed pulse weights are not decreasing")
    coefficients = (
        -weights[0],
        weights[0] - weights[1],
        weights[1] - weights[2],
        weights[2],
    )
    if sum(coefficients) != 0 or min(coefficients[1:]) <= 0:
        raise AssertionError("reduced chain does not telescope positively")
    expected_valuations = tuple(
        pref[position + 1] - word[0] for position in support
    )
    if tuple(v2(coefficients[index]) for index in range(1, 4)) != (
        expected_valuations
    ):
        raise AssertionError("reduced coefficient valuation failure")
    lambdas = []
    caps = []
    for variable in range(1, 4):
        coefficient_norm = (
            U * sum(abs(coefficients[index]) for index in range(variable))
            + Q
            * sum(abs(coefficients[index]) for index in range(variable, 4))
        )
        cap = (4 * coefficient_norm + Q) // (4 * U)
        lambdas.append(coefficient_norm)
        caps.append(cap)
    max_heights = tuple(cap.bit_length() - 1 for cap in caps)
    if min(max_heights) < 1:
        raise AssertionError("empty coordinate box")
    return Packet(
        family=spec.name,
        repetition=repetition,
        rotation=rotation,
        word=word,
        support=support,
        z0=z0,
        states=states,
        pref=pref,
        U=U,
        Q=Q,
        common=common,
        weights=weights,
        coefficients=coefficients,
        lambdas=tuple(lambdas),
        caps=tuple(caps),
        max_heights=max_heights,
    )


def prefix_products(values: Sequence[int]) -> list[int]:
    out = [1]
    for value in values:
        out.append(out[-1] * value)
    return out


def resultant_data(
    packet: Packet, x_values: Sequence[int], variable: int, R: int, D: int
) -> int:
    products = prefix_products(x_values)
    left = sum(
        packet.coefficients[index] * products[index]
        for index in range(variable + 1)
    )
    right = 0
    suffix = 1
    for coefficient_index in range(variable + 1, 4):
        if coefficient_index > variable + 1:
            suffix *= x_values[coefficient_index - 1]
        right += packet.coefficients[coefficient_index] * suffix
    after = math.prod(x_values[variable + 1 :])
    eliminant = packet.U * after * left + packet.Q * right
    if packet.U * after * R - right * D != eliminant:
        raise AssertionError("reduced Bezout identity failed")
    if (R % D == 0) != (eliminant % D == 0):
        raise AssertionError("resultant divisibility equivalence failed")
    expected = packet.pref[packet.support[variable] + 1] - packet.word[0]
    if v2(eliminant) != expected:
        raise AssertionError("resultant 2-adic valuation failure")
    other_product = math.prod(
        x_values[:variable] + x_values[variable + 1 :]
    )
    if abs(eliminant) > packet.lambdas[variable] * other_product:
        raise AssertionError("resultant coefficient-norm bound failed")
    return eliminant


def packet_json(packet: Packet, index: int) -> dict[str, object]:
    return {
        "packet_index": index,
        "family": packet.family,
        "r": packet.repetition,
        "primitive_rotation": packet.rotation,
        "word": list(packet.word),
        "support": list(packet.support),
        "cyclic_gaps": [
            packet.support[1],
            packet.support[2] - packet.support[1],
            len(packet.word) - packet.support[2],
        ],
        "z0": packet.z0,
        "U": packet.U,
        "Q": packet.Q,
        "coprime_common_factor": packet.common,
        "reduced_weights": list(packet.weights),
        "reduced_coefficients": list(packet.coefficients),
        "coefficient_valuations": [
            v2(packet.coefficients[index]) for index in range(1, 4)
        ],
        "resultant_norms": list(packet.lambdas),
        "coordinate_caps_X": list(packet.caps),
        "maximum_pulse_heights": list(packet.max_heights),
    }


def scan_packet(
    packet: Packet, packet_index: int
) -> tuple[dict[str, object], list[bytes], list[dict[str, object]]]:
    rows: list[bytes] = []
    hits: list[dict[str, object]] = []
    row_digest = hashlib.sha256()
    tuple_count = 0
    for heights in itertools.product(
        *(range(1, maximum + 1) for maximum in packet.max_heights)
    ):
        x_values = tuple(2**height for height in heights)
        products = prefix_products(x_values)
        R = sum(
            packet.coefficients[index] * products[index] for index in range(4)
        )
        direct_R = sum(
            packet.weights[index]
            * (x_values[index] - 1)
            * products[index]
            for index in range(3)
        )
        if R != direct_R or R <= 0:
            raise AssertionError("distributed pulse H formula failed")
        D = packet.U * products[-1] - packet.Q
        if D <= 0:
            raise AssertionError("three-pulse finite denominator not positive")
        candidate = list(packet.word)
        for position, height in zip(packet.support, heights):
            candidate[position] += height
        C = affine_numerator(candidate)
        if C - packet.z0 * D != packet.common * R:
            raise AssertionError("C-zD does not equal the full pulse correction")
        if math.gcd(D, packet.common) != 1:
            raise AssertionError("removed correction factor is not coprime to D")
        eliminants = [
            resultant_data(packet, x_values, variable, R, D)
            for variable in range(3)
        ]
        hit = R % D == 0
        start = 0
        if hit:
            if C % D:
                raise AssertionError("reduced hit does not reconstruct integrality")
            start = C // D
            if not exact_replay(candidate, start):
                raise AssertionError("divisor hit fails physical replay")
            hits.append(
                {
                    "packet_index": packet_index,
                    "family": packet.family,
                    "r": packet.repetition,
                    "primitive_rotation": packet.rotation,
                    "support": list(packet.support),
                    "pulse_heights": list(heights),
                    "word": candidate,
                    "D": D,
                    "R": R,
                    "n": start,
                    "exact_replay": True,
                    "trivial": start == 1,
                }
            )
        record = [
            packet_index,
            *heights,
            D,
            R % D,
            *(eliminant % D for eliminant in eliminants),
            start,
        ]
        encoded = json.dumps(record, separators=(",", ":")).encode("ascii") + b"\n"
        rows.append(encoded)
        row_digest.update(encoded)
        tuple_count += 1
    summary = packet_json(packet, packet_index)
    summary.update(
        {
            "finite_tuple_count": tuple_count,
            "resultant_identity_count": 3 * tuple_count,
            "tuple_transcript_sha256": row_digest.hexdigest(),
            "hits": hits,
        }
    )
    return summary, rows, hits


def build_finite_computation() -> tuple[dict[str, object], bytes]:
    coverage_rows = []
    packets = []
    body_rows: list[bytes] = []
    all_hits: list[dict[str, object]] = []
    packet_index = 0
    for spec in FAMILIES:
        for repetition in spec.finite_repetitions:
            keys, coverage = normalized_packet_keys(spec, repetition)
            coverage_rows.append(coverage)
            for key in keys:
                packet = compile_packet(spec, repetition, key)
                summary, rows, hits = scan_packet(packet, packet_index)
                packets.append(summary)
                body_rows.extend(rows)
                all_hits.extend(hits)
                packet_index += 1
    if len(all_hits) != 1:
        raise AssertionError(f"unexpected hit count: {len(all_hits)}")
    sole = all_hits[0]
    if not (
        sole["family"] == "P3"
        and sole["r"] == 3
        and sole["word"] == [2, 2, 2, 2, 2, 2]
        and sole["n"] == 1
    ):
        raise AssertionError("unexpected finite hit")
    tuple_count = sum(int(packet["finite_tuple_count"]) for packet in packets)
    header = {
        "format": CERTIFICATE_FORMAT,
        "fields": [
            "packet_index",
            "d1",
            "d2",
            "d3",
            "D",
            "R_mod_D",
            "E1_mod_D",
            "E2_mod_D",
            "E3_mod_D",
            "start_if_hit",
        ],
        "packet_count": len(packets),
        "tuple_count": tuple_count,
    }
    raw = (
        json.dumps(header, sort_keys=True, separators=(",", ":")).encode("ascii")
        + b"\n"
        + b"".join(body_rows)
    )
    finite = {
        "scope": {
            "P3_repetitions": [2, 3],
            "P11_repetitions": [1],
            "exactly_three_distinct_positive_pulses": True,
            "arbitrary_heights_closed_by_coordinate_caps": True,
            "normalization": (
                "rotate a largest cyclic support gap to the end; "
                "lexicographic tie rule"
            ),
        },
        "coverage": coverage_rows,
        "packets": packets,
        "totals": {
            "raw_rotation_support_configurations": sum(
                int(row["raw_rotation_support_configurations"])
                for row in coverage_rows
            ),
            "normalized_packets": len(packets),
            "finite_tuples": tuple_count,
            "resultant_identities": 3 * tuple_count,
            "divisor_hits": len(all_hits),
            "nontrivial_hits": sum(not bool(hit["trivial"]) for hit in all_hits),
            "trivial_hits": sum(bool(hit["trivial"]) for hit in all_hits),
        },
        "hits": all_hits,
    }
    return finite, raw


def deterministic_gzip(raw: bytes) -> bytes:
    output = io.BytesIO()
    with gzip.GzipFile(
        filename="", mode="wb", compresslevel=9, fileobj=output, mtime=0
    ) as stream:
        stream.write(raw)
    return output.getvalue()


def build_bundle() -> tuple[dict[str, object], bytes, bytes]:
    analytic = [analytic_case(spec) for spec in FAMILIES]
    finite, raw_certificate = build_finite_computation()
    gzip_certificate = deterministic_gzip(raw_certificate)
    analytic_rows = sum(
        len(case["continued_fraction_rows"]) for case in analytic
    )
    rejected_families = sum(
        len(case["uniform_candidate_rejections"]) + len(case["exceptional_rows"])
        for case in analytic
    )
    core = {"analytic_reduction": analytic, "finite_computation": finite}
    master = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode("utf-8")
        + b"\0"
        + raw_certificate
    ).hexdigest()
    payload = {
        "experiment_id": EXPERIMENT_ID,
        "claim_id": CLAIM_ID,
        "agent": "gpt56-sol-04",
        "status": (
            "exact proved finite computation; conditional all-repetition "
            "conclusion remains PROPOSED / SOURCE-DEPENDENT"
        ),
        **core,
        "certificate": {
            "path": "results/finite-tuples.jsonl.gz",
            "format": CERTIFICATE_FORMAT,
            "uncompressed_bytes": len(raw_certificate),
            "gzip_bytes": len(gzip_certificate),
            "uncompressed_sha256": hashlib.sha256(raw_certificate).hexdigest(),
            "gzip_sha256": hashlib.sha256(gzip_certificate).hexdigest(),
        },
        "totals": {
            "continued_fraction_rows": analytic_rows,
            "primitive_upper_families_rejected": rejected_families,
            "transition_repetitions_rejected": sum(
                len(case["transition_rejections"]) for case in analytic
            ),
            **finite["totals"],
        },
        "master_transcript_sha256": master,
    }
    return payload, raw_certificate, gzip_certificate


def stable_json(payload: dict[str, object]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write-results", type=Path)
    action.add_argument("--check-results", type=Path)
    parser.add_argument(
        "--certificate",
        type=Path,
        help="defaults to finite-tuples.jsonl.gz beside canonical JSON",
    )
    args = parser.parse_args()
    payload, raw_certificate, gzip_certificate = build_bundle()
    target: Path = args.write_results or args.check_results
    certificate = args.certificate or target.with_name("finite-tuples.jsonl.gz")
    if args.write_results:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(stable_json(payload), encoding="utf-8")
        certificate.write_bytes(gzip_certificate)
        print(f"wrote {target}")
        print(f"wrote {certificate}")
    else:
        frozen = json.loads(target.read_text(encoding="utf-8"))
        if frozen != payload:
            raise SystemExit("canonical result mismatch")
        actual_gzip = certificate.read_bytes()
        if hashlib.sha256(actual_gzip).hexdigest() != payload["certificate"][
            "gzip_sha256"
        ]:
            raise SystemExit("compressed certificate digest mismatch")
        try:
            actual_raw = gzip.decompress(actual_gzip)
        except (OSError, EOFError) as error:
            raise SystemExit(f"invalid gzip certificate: {error}") from error
        if actual_raw != raw_certificate:
            raise SystemExit("finite tuple certificate mismatch")
        print("frozen result and finite tuple certificate verified")
    print(json.dumps(payload["totals"], sort_keys=True))
    print(payload["master_transcript_sha256"])


if __name__ == "__main__":
    main()
