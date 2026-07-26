#!/usr/bin/env python3
"""Independent verifier for the X-8260 proof transcript.

This file does not import run.py.  It independently reconstructs logarithm
intervals, continued fractions, analytic margins, largest-gap coverage,
reduced resultants, coordinate caps, every finite tuple, and every physical
replay before comparing the complete object and certificate digests.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

sys.set_int_max_str_digits(0)

NTERMS = 180
C2 = 1 << 32
FORMAT = "X-8260-finite-tuples-v1"

SPECS = (
    {
        "name": "P3",
        "base": (1, 2),
        "A": 3,
        "k": 2,
        "c": 7,
        "cutoff": 200_000_000_000,
        "half": 4,
        "legendre": 10,
        "transition": (4, 5, 6, 7, 8, 9),
        "finite": (2, 3),
        "empty": (1,),
    },
    {
        "name": "P11",
        "base": (1, 1, 1, 2, 1, 1, 4),
        "A": 11,
        "k": 7,
        "c": 91,
        "cutoff": 50_000_000_000,
        "half": 2,
        "legendre": 3,
        "transition": (2,),
        "finite": (1,),
        "empty": (),
    },
)


def rational_digest(value: Fraction) -> str:
    return hashlib.sha256(
        (str(value.numerator) + "/" + str(value.denominator)).encode("ascii")
    ).hexdigest()


def floor_decimal(value: Fraction, places: int = 18) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10**places
    integer = value.numerator * scale // value.denominator
    return (
        f"{sign}{integer // scale}."
        f"{integer % scale:0{places}d}"
    )


def margin_record(value: Fraction, places: int = 18) -> dict[str, object]:
    assert value > 0
    return {
        "decimal_lower": floor_decimal(value, places),
        "fraction_sha256": rational_digest(value),
    }


def series_log_bounds_integer(value: int) -> tuple[Fraction, Fraction]:
    """Independent integer logarithm enclosure via a normalized mantissa."""
    assert value > 0
    if value == 2:
        z = Fraction(1, 3)
        total = Fraction(0)
        term = z
        z_squared = z * z
        for index in range(NTERMS):
            total += 2 * term / (2 * index + 1)
            term *= z_squared
        error = 2 * term / ((2 * NTERMS + 1) * (1 - z_squared))
        return total, total + error
    shift = value.bit_length() - 1
    mantissa = Fraction(value, 1 << shift)
    z = (mantissa - 1) / (mantissa + 1)
    total = Fraction(0)
    term = z
    z_squared = z * z
    for index in range(NTERMS):
        total += 2 * term / (2 * index + 1)
        term *= z_squared
    error = 2 * term / ((2 * NTERMS + 1) * (1 - z_squared))
    l2_lo, l2_hi = series_log_bounds_integer(2)
    return shift * l2_lo + total, shift * l2_hi + total + error


L2 = series_log_bounds_integer(2)
L3 = series_log_bounds_integer(3)


def eta_bounds(A: int, k: int) -> tuple[Fraction, Fraction]:
    lo = (k * L3[0] - A * L2[1]) / L2[1]
    hi = (k * L3[1] - A * L2[0]) / L2[0]
    assert 0 < lo < hi
    return lo, hi


def width_exponent(bounds: tuple[Fraction, Fraction]) -> int:
    width = bounds[1] - bounds[0]
    result = 0
    while width < Fraction(1, 2 ** (result + 1)):
        result += 1
    return result


def cf_expansion(
    bounds: tuple[Fraction, Fraction], limit: int
) -> list[dict[str, object]]:
    original = bounds
    low, high = bounds
    old_p, p = 0, 1
    old_q, q = 1, 0
    output = []
    for index in range(256):
        digit = low.numerator // low.denominator
        assert digit == high.numerator // high.denominator
        new_p = digit * p + old_p
        new_q = digit * q + old_q
        value = Fraction(new_p, new_q)
        if value < original[0]:
            side = "below"
        elif value > original[1]:
            side = "above"
        else:
            raise AssertionError("unresolved convergent")
        output.append(
            {
                "index": index,
                "partial_quotient": digit,
                "p": new_p,
                "q": new_q,
                "side": side,
            }
        )
        if new_q > limit:
            return output
        low, high = 1 / (high - digit), 1 / (low - digit)
        old_p, p = p, new_p
        old_q, q = q, new_q
    raise AssertionError("continued fraction limit not reached")


def exponent_3(k: int, r: int) -> int:
    return (2 * k * r) // 3


def verify_half_range(spec: dict[str, object]) -> dict[str, object]:
    A, k, c = int(spec["A"]), int(spec["k"]), int(spec["c"])
    start = int(spec["half"])
    base = []
    for r in range(start, start + 3):
        difference = 2 ** (A * r) - 2 * c * 3 ** exponent_3(k, r)
        assert difference > 0
        base.append({"r": r, "integer_margin": difference})
    ratio = Fraction(3 ** (2 * k), 2 ** (3 * A))
    assert ratio < 1
    return {
        "first_r": start,
        "residue_modulus": 3,
        "base_rows": base,
        "three_step_ratio": f"{ratio.numerator}/{ratio.denominator}",
    }


def verify_transition(spec: dict[str, object]) -> list[dict[str, object]]:
    A, k, c = int(spec["A"]), int(spec["k"]), int(spec["c"])
    output = []
    for r in spec["transition"]:
        r = int(r)
        lambda_lower = (A * r + 3) * L2[0] - k * r * L3[1]
        lambda_upper = Fraction(2 * c * 3 ** exponent_3(k, r), 2 ** (A * r))
        output.append(
            {
                "r": r,
                "minimum_total_pulse": 3,
                "lambda_lower_minus_upper": margin_record(
                    lambda_lower - lambda_upper
                ),
            }
        )
    return output


def verify_matveev_substitution(spec: dict[str, object]) -> dict[str, object]:
    assert L3[0] > 1
    A, k, c = int(spec["A"]), int(spec["k"]), int(spec["c"])
    cutoff = int(spec["cutoff"])
    rate_low = A * L2[0] - Fraction(2 * k, 3) * L3[1]
    rate_high = A * L2[1] - Fraction(2 * k, 3) * L3[0]
    K_high = C2 * L2[1] * L3[1]
    log_c_high = series_log_bounds_integer(2 * c)[1]
    log_B_high = series_log_bounds_integer(k * cutoff + 1)[1]
    cutoff_margin = (
        cutoff * rate_low - log_c_high - K_high * (1 + log_B_high)
    )
    derivative = rate_low - K_high * Fraction(k, k * cutoff + 1)
    lambda_margin = cutoff * rate_low - log_c_high
    assert rate_low > 0 and rate_high > rate_low
    return {
        "quoted_constant_multiplier": C2,
        "cutoff": cutoff,
        "effective_rate": {
            "lo_sha256": rational_digest(rate_low),
            "hi_sha256": rational_digest(rate_high),
            "lo_decimal": floor_decimal(rate_low),
        },
        "cutoff_margin": margin_record(cutoff_margin, 12),
        "derivative_margin": margin_record(derivative),
        "lambda_lt_one_margin": margin_record(lambda_margin, 12),
    }


def verify_legendre_range(spec: dict[str, object]) -> dict[str, object]:
    A, k, c = int(spec["A"]), int(spec["k"]), int(spec["c"])
    start = int(spec["legendre"])
    rows = []
    for r in range(start, start + 3):
        difference = (
            2 ** (A * r) * L2[0]
            - 4 * c * r * 3 ** exponent_3(k, r)
        )
        rows.append({"r": r, "margin": margin_record(difference, 12)})
    exponential = Fraction(3 ** (2 * k), 2 ** (3 * A))
    bound = Fraction(start + 3, start) * exponential
    assert bound < 1
    return {
        "first_r": start,
        "residue_modulus": 3,
        "base_rows": rows,
        "three_step_ratio_upper": f"{bound.numerator}/{bound.denominator}",
    }


def candidate_rejection(
    spec: dict[str, object], p: int, q: int, next_q: int
) -> dict[str, object]:
    A, k, c = int(spec["A"]), int(spec["k"]), int(spec["c"])
    coefficient = 4 * c * (q + next_q)
    step_exponent = (2 * k * q + 2) // 3
    decay_margin = A * q * L2[0] - step_exponent * L3[1]
    assert decay_margin > 0
    margin = (
        A * q * L2[0]
        - exponent_3(k, q) * L3[1]
        - series_log_bounds_integer(coefficient)[1]
    )
    return {
        "p": p,
        "q": q,
        "q_next": next_q,
        "floor_2kq_over_3": exponent_3(k, q),
        "multiple_step_ceiling_exponent": step_exponent,
        "multiple_step_decay_log_margin": margin_record(decay_margin, 12),
        "all_positive_multiples_rejected": True,
        "log_margin": margin_record(margin, 12),
    }


def one_fifth_record() -> dict[str, object]:
    m = 3
    difference = (
        1
        - Fraction(59049, 65536) ** m
        - Fraction(7 * 3 ** ((20 * m) // 3), 8 ** (5 * m))
    )
    ratio = Fraction(3**7, 8**5)
    assert difference > 0 and ratio < 1
    return {
        "p": 1,
        "q": 5,
        "minimum_multiple_m": 3,
        "reason_for_minimum": "three distinct positive pulses imply t=m>=3",
        "exact_margin_numerator": difference.numerator,
        "exact_margin_denominator": difference.denominator,
        "upper_bound_step_ratio_at_most": (
            f"{ratio.numerator}/{ratio.denominator}"
        ),
        "all_m_at_least_3_rejected": True,
    }


def rebuild_analytic_case(spec: dict[str, object]) -> dict[str, object]:
    bounds = eta_bounds(int(spec["A"]), int(spec["k"]))
    rows = cf_expansion(bounds, int(spec["cutoff"]))
    ordinary = []
    exceptional = []
    for index, row in enumerate(rows[:-1]):
        if row["side"] != "above" or int(row["q"]) >= int(spec["cutoff"]):
            continue
        p, q = int(row["p"]), int(row["q"])
        if spec["name"] == "P3" and (p, q) == (1, 5):
            exceptional.append(one_fifth_record())
        else:
            ordinary.append(
                candidate_rejection(spec, p, q, int(rows[index + 1]["q"]))
            )
    return {
        "name": spec["name"],
        "base": list(spec["base"]),
        "A": spec["A"],
        "k": spec["k"],
        "cmax": spec["c"],
        "support_span_bound": "p3 <= floor(2*k*r/3)",
        "half_bound": verify_half_range(spec),
        "transition_rejections": verify_transition(spec),
        "matveev": verify_matveev_substitution(spec),
        "eta_interval": {
            "lo_sha256": rational_digest(bounds[0]),
            "hi_sha256": rational_digest(bounds[1]),
            "width_lt_2_power": width_exponent(bounds),
        },
        "legendre": verify_legendre_range(spec),
        "continued_fraction_rows": rows,
        "uniform_candidate_rejections": ordinary,
        "exceptional_rows": exceptional,
        "finite_repetitions": list(spec["finite"]),
        "structurally_empty_repetitions": list(spec["empty"]),
    }


def ord2(value: int) -> int:
    assert value
    value = abs(value)
    result = 0
    while value % 2 == 0:
        value //= 2
        result += 1
    return result


def partial_sums(word: tuple[int, ...] | list[int]) -> list[int]:
    result = [0]
    for value in word:
        assert value >= 1
        result.append(result[-1] + value)
    return result


def numerator(word: tuple[int, ...] | list[int]) -> int:
    pref = partial_sums(word)
    n = len(word)
    return sum(3 ** (n - j - 1) * 2 ** pref[j] for j in range(n))


def rotated(word: tuple[int, ...], amount: int) -> tuple[int, ...]:
    amount %= len(word)
    return word[amount:] + word[:amount]


def baseline_orbit(
    word: tuple[int, ...],
) -> tuple[int, list[int], list[int]]:
    pref = partial_sums(word)
    D = 2 ** pref[-1] - 3 ** len(word)
    C = numerator(word)
    assert C % D == 0
    start = C // D
    assert start < 0 and start % 2
    orbit = [start]
    current = start
    for valuation in word:
        raw = 3 * current + 1
        assert ord2(raw) == valuation
        current = raw // 2**valuation
        orbit.append(current)
    assert current == start
    return start, orbit, pref


def replay_positive(word: list[int], start: int) -> bool:
    if start <= 0 or start % 2 == 0:
        return False
    current = start
    for valuation in word:
        raw = 3 * current + 1
        if ord2(raw) != valuation:
            return False
        current = raw // 2**valuation
    return current == start


def canonical_geometry(
    k: int, length: int, initial_rotation: int, support: tuple[int, int, int]
) -> tuple[int, int, int]:
    """Independent largest-gap normalization from cyclic successor pairs."""
    possible = []
    gap_data = []
    for position in support:
        successors = [other for other in support if other > position]
        successor = min(successors) if successors else support[0]
        distance = (successor - position) % length
        gap_data.append((position, successor, distance))
    maximum = max(item[2] for item in gap_data)
    for _, successor, distance in gap_data:
        if distance != maximum:
            continue
        shifted = sorted((entry - successor) % length for entry in support)
        possible.append(
            ((initial_rotation + successor) % k, shifted[1], shifted[2])
        )
    answer = min(possible)
    assert answer[2] <= (2 * length) // 3
    return answer


def geometry_keys(
    spec: dict[str, object], repetition: int
) -> tuple[list[tuple[int, int, int]], dict[str, object]]:
    k = int(spec["k"])
    length = k * repetition
    multiplicity: dict[tuple[int, int, int], int] = {}
    digest = hashlib.sha256()
    count = 0
    for initial in range(k):
        for support in itertools.combinations(range(length), 3):
            key = canonical_geometry(k, length, initial, support)
            multiplicity[key] = multiplicity.get(key, 0) + 1
            count += 1
            digest.update(
                (
                    f"{spec['name']}|{repetition}|{initial}|"
                    f"{','.join(map(str, support))}|"
                    f"{','.join(map(str, key))}\n"
                ).encode("ascii")
            )
    keys = sorted(multiplicity)
    rotations = sorted(set(key[0] for key in keys))
    assert rotations == list(range(k))
    return keys, {
        "family": spec["name"],
        "r": repetition,
        "raw_rotation_support_configurations": count,
        "normalized_packets": len(keys),
        "primitive_rotations": rotations,
        "maximum_p3": max(key[2] for key in keys),
        "floor_2kr_over_3": (2 * length) // 3,
        "normalization_transcript_sha256": digest.hexdigest(),
        "preimage_multiplicities": [
            {
                "rotation": key[0],
                "p2": key[1],
                "p3": key[2],
                "count": multiplicity[key],
            }
            for key in keys
        ],
    }


def compile_finite_packet(
    spec: dict[str, object], repetition: int, key: tuple[int, int, int]
) -> dict[str, object]:
    rotation, p2, p3 = key
    base = tuple(spec["base"])
    word = rotated(base * repetition, rotation)
    support = (0, p2, p3)
    z0, states, pref = baseline_orbit(word)
    length = len(word)
    U, Q = 2 ** pref[-1], 3**length
    common = 2 ** word[0] * 3 ** (length - p3 - 1)
    full_weights = [
        (-states[position + 1])
        * 3 ** (length - position - 1)
        * 2 ** pref[position + 1]
        for position in support
    ]
    assert all(weight % common == 0 for weight in full_weights)
    weights = tuple(weight // common for weight in full_weights)
    assert weights[0] > weights[1] > weights[2] > 0
    coefficients = (
        -weights[0],
        weights[0] - weights[1],
        weights[1] - weights[2],
        weights[2],
    )
    assert sum(coefficients) == 0 and min(coefficients[1:]) > 0
    valuations = [pref[position + 1] - word[0] for position in support]
    assert [ord2(coefficients[index]) for index in range(1, 4)] == valuations
    norms = []
    caps = []
    for i in range(1, 4):
        norm = U * sum(abs(coefficients[j]) for j in range(i))
        norm += Q * sum(abs(coefficients[j]) for j in range(i, 4))
        norms.append(norm)
        caps.append((4 * norm + Q) // (4 * U))
    heights = [cap.bit_length() - 1 for cap in caps]
    assert min(heights) >= 1
    return {
        "family": spec["name"],
        "r": repetition,
        "rotation": rotation,
        "word": word,
        "support": support,
        "z0": z0,
        "states": states,
        "pref": pref,
        "U": U,
        "Q": Q,
        "common": common,
        "weights": weights,
        "coefficients": coefficients,
        "valuations": valuations,
        "norms": norms,
        "caps": caps,
        "heights": heights,
    }


def cumulative_products(values: tuple[int, int, int]) -> list[int]:
    return [1, values[0], values[0] * values[1], math.prod(values)]


def independent_eliminant(
    packet: dict[str, object],
    xs: tuple[int, int, int],
    coordinate: int,
    R: int,
    D: int,
) -> int:
    coeff = packet["coefficients"]
    products = cumulative_products(xs)
    # Form R=A+P_before*X_i*B by direct monomial division.
    A_part = sum(coeff[j] * products[j] for j in range(coordinate + 1))
    B_part = 0
    for j in range(coordinate + 1, 4):
        divisor = products[coordinate + 1]
        B_part += coeff[j] * (products[j] // divisor)
    after = math.prod(xs[coordinate + 1 :])
    E = int(packet["U"]) * after * A_part + int(packet["Q"]) * B_part
    assert int(packet["U"]) * after * R - B_part * D == E
    assert (R % D == 0) == (E % D == 0)
    assert ord2(E) == packet["valuations"][coordinate]
    other = math.prod(xs[:coordinate] + xs[coordinate + 1 :])
    assert abs(E) <= packet["norms"][coordinate] * other
    return E


def public_packet(
    packet: dict[str, object],
    packet_index: int,
    tuple_count: int,
    transcript: str,
    hits: list[dict[str, object]],
) -> dict[str, object]:
    support = packet["support"]
    return {
        "packet_index": packet_index,
        "family": packet["family"],
        "r": packet["r"],
        "primitive_rotation": packet["rotation"],
        "word": list(packet["word"]),
        "support": list(support),
        "cyclic_gaps": [
            support[1],
            support[2] - support[1],
            len(packet["word"]) - support[2],
        ],
        "z0": packet["z0"],
        "U": packet["U"],
        "Q": packet["Q"],
        "coprime_common_factor": packet["common"],
        "reduced_weights": list(packet["weights"]),
        "reduced_coefficients": list(packet["coefficients"]),
        "coefficient_valuations": packet["valuations"],
        "resultant_norms": packet["norms"],
        "coordinate_caps_X": packet["caps"],
        "maximum_pulse_heights": packet["heights"],
        "finite_tuple_count": tuple_count,
        "resultant_identity_count": 3 * tuple_count,
        "tuple_transcript_sha256": transcript,
        "hits": hits,
    }


def scan_and_match_packet(
    packet: dict[str, object],
    packet_index: int,
    certificate_lines: list[bytes],
    line_position: int,
) -> tuple[dict[str, object], list[dict[str, object]], int]:
    digest = hashlib.sha256()
    hits = []
    count = 0
    ranges = [range(1, maximum + 1) for maximum in packet["heights"]]
    for heights in itertools.product(*ranges):
        xs = tuple(2**height for height in heights)
        products = cumulative_products(xs)
        coeff = packet["coefficients"]
        R = sum(coeff[j] * products[j] for j in range(4))
        direct = sum(
            packet["weights"][j] * (xs[j] - 1) * products[j]
            for j in range(3)
        )
        assert R == direct and R > 0
        D = int(packet["U"]) * products[-1] - int(packet["Q"])
        assert D > 0
        assert all(xs[j] <= packet["caps"][j] for j in range(3))
        candidate = list(packet["word"])
        for position, pulse in zip(packet["support"], heights):
            candidate[position] += pulse
        C = numerator(candidate)
        assert C - int(packet["z0"]) * D == int(packet["common"]) * R
        assert math.gcd(D, int(packet["common"])) == 1
        eliminants = [
            independent_eliminant(packet, xs, coordinate, R, D)
            for coordinate in range(3)
        ]
        start = 0
        if R % D == 0:
            assert C % D == 0
            start = C // D
            assert replay_positive(candidate, start)
            hits.append(
                {
                    "packet_index": packet_index,
                    "family": packet["family"],
                    "r": packet["r"],
                    "primitive_rotation": packet["rotation"],
                    "support": list(packet["support"]),
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
            *(value % D for value in eliminants),
            start,
        ]
        expected_line = json.dumps(record, separators=(",", ":")).encode("ascii")
        assert line_position < len(certificate_lines)
        if certificate_lines[line_position] != expected_line:
            raise AssertionError(
                f"tuple certificate mismatch at packet {packet_index}, "
                f"heights {heights}"
            )
        digest.update(expected_line + b"\n")
        line_position += 1
        count += 1
    return (
        public_packet(packet, packet_index, count, digest.hexdigest(), hits),
        hits,
        line_position,
    )


def rebuild_finite(
    raw_certificate: bytes,
) -> tuple[dict[str, object], dict[str, object]]:
    lines = raw_certificate.splitlines()
    assert lines
    header = json.loads(lines[0])
    expected_header_fields = [
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
    ]
    coverage = []
    packets = []
    all_hits = []
    line_position = 1
    packet_index = 0
    for spec in SPECS:
        for repetition in spec["finite"]:
            keys, coverage_row = geometry_keys(spec, int(repetition))
            coverage.append(coverage_row)
            for key in keys:
                packet = compile_finite_packet(spec, int(repetition), key)
                public, hits, line_position = scan_and_match_packet(
                    packet, packet_index, lines, line_position
                )
                packets.append(public)
                all_hits.extend(hits)
                packet_index += 1
    assert line_position == len(lines), "certificate has trailing tuple rows"
    tuple_count = sum(int(packet["finite_tuple_count"]) for packet in packets)
    expected_header = {
        "format": FORMAT,
        "fields": expected_header_fields,
        "packet_count": len(packets),
        "tuple_count": tuple_count,
    }
    assert header == expected_header
    assert len(all_hits) == 1
    assert (
        all_hits[0]["family"] == "P3"
        and all_hits[0]["r"] == 3
        and all_hits[0]["word"] == [2, 2, 2, 2, 2, 2]
        and all_hits[0]["n"] == 1
    )
    totals = {
        "raw_rotation_support_configurations": sum(
            int(row["raw_rotation_support_configurations"]) for row in coverage
        ),
        "normalized_packets": len(packets),
        "finite_tuples": tuple_count,
        "resultant_identities": 3 * tuple_count,
        "divisor_hits": len(all_hits),
        "nontrivial_hits": sum(not bool(hit["trivial"]) for hit in all_hits),
        "trivial_hits": sum(bool(hit["trivial"]) for hit in all_hits),
    }
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
        "coverage": coverage,
        "packets": packets,
        "totals": totals,
        "hits": all_hits,
    }
    return finite, totals


def reconstruct(
    raw_certificate: bytes, compressed_certificate: bytes
) -> dict[str, object]:
    analytic = [rebuild_analytic_case(spec) for spec in SPECS]
    finite, finite_totals = rebuild_finite(raw_certificate)
    core = {"analytic_reduction": analytic, "finite_computation": finite}
    master = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode("utf-8")
        + b"\0"
        + raw_certificate
    ).hexdigest()
    return {
        "experiment_id": "X-8260",
        "claim_id": "T-8260",
        "agent": "gpt56-sol-04",
        "status": (
            "exact proved finite computation; conditional all-repetition "
            "conclusion remains PROPOSED / SOURCE-DEPENDENT"
        ),
        **core,
        "certificate": {
            "path": "results/finite-tuples.jsonl.gz",
            "format": FORMAT,
            "uncompressed_bytes": len(raw_certificate),
            "gzip_bytes": len(compressed_certificate),
            "uncompressed_sha256": hashlib.sha256(raw_certificate).hexdigest(),
            "gzip_sha256": hashlib.sha256(compressed_certificate).hexdigest(),
        },
        "totals": {
            "continued_fraction_rows": sum(
                len(case["continued_fraction_rows"]) for case in analytic
            ),
            "primitive_upper_families_rejected": sum(
                len(case["uniform_candidate_rejections"])
                + len(case["exceptional_rows"])
                for case in analytic
            ),
            "transition_repetitions_rejected": sum(
                len(case["transition_rejections"]) for case in analytic
            ),
            **finite_totals,
        },
        "master_transcript_sha256": master,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    parser.add_argument(
        "--certificate",
        type=Path,
        help="defaults to finite-tuples.jsonl.gz beside the artifact",
    )
    args = parser.parse_args()
    certificate_path = args.certificate or args.artifact.with_name(
        "finite-tuples.jsonl.gz"
    )
    frozen = json.loads(args.artifact.read_text(encoding="utf-8"))
    compressed = certificate_path.read_bytes()
    try:
        raw = gzip.decompress(compressed)
    except (OSError, EOFError) as error:
        raise SystemExit(f"invalid tuple certificate: {error}") from error
    rebuilt = reconstruct(raw, compressed)
    if rebuilt != frozen:
        raise SystemExit("independent reconstruction mismatch")
    print("independent reconstruction matches")
    print(json.dumps(rebuilt["totals"], sort_keys=True))
    print(rebuilt["master_transcript_sha256"])


if __name__ == "__main__":
    main()
