#!/usr/bin/env python3
"""Exact checker for L-8201: sparse-resultant caps for fixed pulse supports.

The checker uses Python's arbitrary-precision integers and the standard library only.
It reconstructs two known negative accelerated Collatz cycles, rotates/repeats them,
selects fixed pulse supports, and verifies:

* the chain-sparse pulse correction;
* every one-variable Sylvester resultant identity;
* the exact 2-adic valuation of each eliminant;
* the resulting uniform pulse-height cap;
* reduction to the two eliminants in PR #51 / L-8001 when support size is two.

No positive cycle or counterexample is asserted.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


NEGATIVE_CYCLES: tuple[tuple[int, ...], ...] = (
    (1, 2),
    (1, 1, 1, 2, 1, 1, 4),
)


def v2(value: int) -> int:
    """Return the exact 2-adic valuation of a nonzero integer."""
    if value == 0:
        raise ValueError("v2(0) is undefined")
    value = abs(value)
    return (value & -value).bit_length() - 1


def prefixes(word: Sequence[int]) -> list[int]:
    out = [0]
    for item in word:
        if item < 1:
            raise ValueError("accelerated valuations must be positive")
        out.append(out[-1] + item)
    return out


def standard_numerator(word: Sequence[int]) -> int:
    pref = prefixes(word)
    length = len(word)
    return sum(3 ** (length - 1 - index) * 2 ** pref[index] for index in range(length))


def rotate(word: Sequence[int], shift: int) -> tuple[int, ...]:
    shift %= len(word)
    return tuple(word[shift:]) + tuple(word[:shift])


def cycle_states(word: Sequence[int]) -> tuple[int, list[int], list[int]]:
    """Return z_0, cyclic states, and prefix valuation totals.

    The input must encode an ordinary negative accelerated cycle exactly.
    """
    pref = prefixes(word)
    denominator = 2 ** pref[-1] - 3 ** len(word)
    numerator = standard_numerator(word)
    if denominator == 0 or numerator % denominator:
        raise ValueError("word does not have an integral affine fixed point")
    z0 = numerator // denominator
    if z0 >= 0 or z0 % 2 == 0:
        raise ValueError("word does not encode a negative odd cycle")

    states = [z0]
    current = z0
    for valuation in word:
        raw = 3 * current + 1
        if v2(raw) != valuation:
            raise ValueError("word fails exact valuation replay")
        current = raw // (2**valuation)
        if current % 2 == 0:
            raise ValueError("accelerated state is not odd")
        states.append(current)
    if current != z0:
        raise ValueError("word does not close")
    return z0, states, pref


@dataclass(frozen=True)
class CompiledSupport:
    word: tuple[int, ...]
    support: tuple[int, ...]
    z0: int
    states: tuple[int, ...]
    pref: tuple[int, ...]
    u: int
    q: int
    weights: tuple[int, ...]
    coefficients: tuple[int, ...]
    lambdas: tuple[int, ...]
    uniform_caps: tuple[int, ...]


def compile_support(word: Sequence[int], support: Sequence[int]) -> CompiledSupport:
    word = tuple(word)
    support = tuple(support)
    if not support or support[0] != 0:
        raise ValueError("the first pulse must be rotated to position zero")
    if tuple(sorted(set(support))) != support:
        raise ValueError("pulse support must be strictly increasing")
    if support[-1] >= len(word):
        raise ValueError("pulse support lies outside the word")

    z0, states, pref = cycle_states(word)
    u = 2 ** pref[-1]
    q = 3 ** len(word)

    # L-9602 positional weights, reconstructed here from the orbit-difference cocycle.
    weights = tuple(
        (-states[position + 1])
        * 3 ** (len(word) - 1 - position)
        * 2 ** pref[position + 1]
        for position in support
    )
    if any(weight <= 0 for weight in weights):
        raise AssertionError("negative cycle weights must be positive")

    coefficients = [-weights[0]]
    coefficients.extend(weights[index - 1] - weights[index] for index in range(1, len(weights)))
    coefficients.append(weights[-1])
    if sum(coefficients) != 0:
        raise AssertionError("chain coefficients must telescope")

    # c_i (1 <= i <= e) has the valuation of the i-th positional weight.
    for index, weight in enumerate(weights, start=1):
        if v2(coefficients[index]) != v2(weight):
            raise AssertionError("coefficient valuation separation failed")

    pulse_count = len(support)
    lambdas: list[int] = []
    caps: list[int] = []
    other_min = 2 ** (pulse_count - 1)
    for variable in range(1, pulse_count + 1):
        lam = (
            u * sum(abs(coefficients[index]) for index in range(variable))
            + q * sum(abs(coefficients[index]) for index in range(variable, pulse_count + 1))
        )
        cap = (other_min * lam + q) // (other_min * u)
        lambdas.append(lam)
        caps.append(cap)

    return CompiledSupport(
        word=word,
        support=support,
        z0=z0,
        states=tuple(states),
        pref=tuple(pref),
        u=u,
        q=q,
        weights=weights,
        coefficients=tuple(coefficients),
        lambdas=tuple(lambdas),
        uniform_caps=tuple(caps),
    )


def prefix_products(values: Sequence[int]) -> list[int]:
    out = [1]
    for value in values:
        out.append(out[-1] * value)
    return out


def pulsed_word(word: Sequence[int], support: Sequence[int], heights: Sequence[int]) -> tuple[int, ...]:
    if len(support) != len(heights):
        raise ValueError("support/height length mismatch")
    out = list(word)
    for position, height in zip(support, heights):
        if height < 1:
            raise ValueError("pulse heights must be positive")
        out[position] += height
    return tuple(out)


def chain_value(coefficients: Sequence[int], x_values: Sequence[int]) -> int:
    products = prefix_products(x_values)
    return sum(coefficient * products[index] for index, coefficient in enumerate(coefficients))


def split_forms(
    coefficients: Sequence[int], x_values: Sequence[int], variable_zero_based: int
) -> tuple[int, int, int, int]:
    """Return A_i, B_i, P_(i-1), S_i in one-based mathematical notation."""
    pulse_count = len(x_values)
    i = variable_zero_based
    products = prefix_products(x_values)
    a_left = sum(coefficients[index] * products[index] for index in range(i + 1))

    b_right = 0
    suffix_product = 1
    for coefficient_index in range(i + 1, pulse_count + 1):
        if coefficient_index > i + 1:
            suffix_product *= x_values[coefficient_index - 1]
        b_right += coefficients[coefficient_index] * suffix_product

    p_before = products[i]
    s_after = math.prod(x_values[i + 1 :])
    return a_left, b_right, p_before, s_after


def eliminant(compiled: CompiledSupport, x_values: Sequence[int], variable_zero_based: int) -> int:
    a_left, b_right, _, s_after = split_forms(
        compiled.coefficients, x_values, variable_zero_based
    )
    return compiled.u * s_after * a_left + compiled.q * b_right


def deterministic_height_vectors(pulse_count: int) -> Iterable[tuple[int, ...]]:
    """A deterministic corpus with exhaustive small and structured large heights."""
    if pulse_count <= 4:
        yield from itertools.product(range(1, 5), repeat=pulse_count)
    else:
        structured = {
            tuple(1 for _ in range(pulse_count)),
            tuple(2 for _ in range(pulse_count)),
            tuple(1 + (index % 4) for index in range(pulse_count)),
            tuple(4 - (index % 4) for index in range(pulse_count)),
            tuple(index + 1 for index in range(pulse_count)),
            tuple(pulse_count - index for index in range(pulse_count)),
        }
        for vector in sorted(structured):
            yield vector
        # A reproducible arithmetic family without importing random.
        for seed in range(32):
            yield tuple(1 + ((seed * (2 * index + 1) + index * index + 3) % 9) for index in range(pulse_count))


def support_corpus(word: Sequence[int], max_support: int = 5) -> Iterable[tuple[int, ...]]:
    upper = min(max_support, len(word))
    positions = range(1, len(word))
    for pulse_count in range(1, upper + 1):
        for remainder in itertools.combinations(positions, pulse_count - 1):
            yield (0,) + remainder


def canonical_words() -> Iterable[tuple[str, tuple[int, ...]]]:
    for primitive_index, primitive in enumerate(NEGATIVE_CYCLES, start=1):
        repetition_limit = 5 if len(primitive) == 2 else 2
        for repetition in range(1, repetition_limit + 1):
            repeated = primitive * repetition
            for shift in range(len(primitive)):
                yield f"cycle{primitive_index}-r{repetition}-rot{shift}", rotate(repeated, shift)


def verify_instance(
    compiled: CompiledSupport, heights: Sequence[int]
) -> tuple[int, int, int, int]:
    x_values = tuple(2**height for height in heights)
    products = prefix_products(x_values)
    pulse_count = len(x_values)

    candidate_word = pulsed_word(compiled.word, compiled.support, heights)
    candidate_pref = prefixes(candidate_word)
    candidate_c = standard_numerator(candidate_word)
    candidate_d = 2 ** candidate_pref[-1] - 3 ** len(candidate_word)

    h_chain = chain_value(compiled.coefficients, x_values)
    if candidate_c - compiled.z0 * candidate_d != h_chain:
        raise AssertionError("chain correction does not match the affine numerator")

    # Direct orbit-difference pulse sum.
    h_direct = sum(
        weight * (x_values[index] - 1) * products[index]
        for index, weight in enumerate(compiled.weights)
    )
    if h_direct != h_chain:
        raise AssertionError("pulse cocycle and chain form disagree")

    divisibility_hit = int(candidate_d > 0 and h_chain % candidate_d == 0)
    resultant_checks = 0
    valuation_checks = 0
    cap_checks = 0

    for i in range(pulse_count):
        a_left, b_right, p_before, s_after = split_forms(compiled.coefficients, x_values, i)
        e_i = compiled.u * s_after * a_left + compiled.q * b_right

        # 2x2 Sylvester determinant for the two linear polynomials in X_i.
        determinant = (
            compiled.u * p_before * s_after * a_left
            - (-compiled.q) * p_before * b_right
        )
        if determinant != p_before * e_i:
            raise AssertionError("Sylvester determinant identity failed")

        if compiled.u * s_after * h_chain - b_right * candidate_d != e_i:
            raise AssertionError("resultantal Bezout identity failed")
        if (h_chain % candidate_d == 0) != (e_i % candidate_d == 0):
            raise AssertionError("divisibility equivalence failed")
        resultant_checks += 1

        expected_valuation = v2(compiled.coefficients[i + 1])
        if v2(e_i) != expected_valuation:
            raise AssertionError("eliminant has the wrong 2-adic valuation")
        valuation_checks += 1

        other_product = math.prod(x_values[:i] + x_values[i + 1 :])
        lambda_i = compiled.lambdas[i]
        if abs(e_i) > lambda_i * other_product:
            raise AssertionError("coefficient-norm eliminant bound failed")

        if divisibility_hit:
            if x_values[i] > compiled.uniform_caps[i]:
                raise AssertionError("a divisor hit exceeds the uniform cap")
            cap_checks += 1

    return resultant_checks, valuation_checks, cap_checks, divisibility_hit


def verify_two_pulse_specialization(compiled: CompiledSupport, heights: Sequence[int]) -> int:
    if len(compiled.support) != 2:
        return 0
    x_value, m_value = (2**heights[0], 2**heights[1])
    gap = compiled.support[1]
    a0 = compiled.word[0]
    common = 2**a0 * 3 ** (len(compiled.word) - gap - 1)
    c0, c1, c2 = compiled.coefficients
    if any(coefficient % common for coefficient in (c0, c1, c2)):
        raise AssertionError("two-pulse common factor is missing")
    alpha = -c0 // common
    gamma = c1 // common
    beta = c2 // common

    k_of_m = compiled.q * (beta * m_value + gamma) - compiled.u * m_value * alpha
    j_of_x = compiled.u * (x_value * gamma - alpha) + beta * compiled.q

    e_first = eliminant(compiled, (x_value, m_value), 0)
    e_second = eliminant(compiled, (x_value, m_value), 1)
    if e_first != common * k_of_m or e_second != common * j_of_x:
        raise AssertionError("two-pulse resultant does not reduce to L-8001 K/J")
    return 2


def build_payload() -> dict[str, object]:
    counters = {
        "negative_cycle_words": 0,
        "fixed_support_packets": 0,
        "pulse_instances": 0,
        "resultant_identities": 0,
        "valuation_certificates": 0,
        "cap_checks_on_divisor_hits": 0,
        "formal_positive_divisor_hits": 0,
        "two_pulse_eliminant_matches": 0,
    }
    transcript = hashlib.sha256()
    samples: list[dict[str, object]] = []
    maximum_cap_bits = 0

    for word_name, word in canonical_words():
        counters["negative_cycle_words"] += 1
        for support in support_corpus(word):
            compiled = compile_support(word, support)
            counters["fixed_support_packets"] += 1
            maximum_cap_bits = max(
                maximum_cap_bits,
                *(cap.bit_length() for cap in compiled.uniform_caps),
            )

            # Freeze a few human-readable support examples.
            if len(samples) < 12 and (
                len(support) in {1, 2, 3, 5} or support == tuple(range(len(support)))
            ):
                samples.append(
                    {
                        "word": word_name,
                        "support": list(support),
                        "weights": [str(value) for value in compiled.weights],
                        "coefficients": [str(value) for value in compiled.coefficients],
                        "uniform_caps": [str(value) for value in compiled.uniform_caps],
                        "coefficient_valuations": [
                            v2(compiled.coefficients[index])
                            for index in range(1, len(compiled.coefficients))
                        ],
                    }
                )

            for heights in deterministic_height_vectors(len(support)):
                resultants, valuations, cap_checks, hit = verify_instance(compiled, heights)
                counters["pulse_instances"] += 1
                counters["resultant_identities"] += resultants
                counters["valuation_certificates"] += valuations
                counters["cap_checks_on_divisor_hits"] += cap_checks
                counters["formal_positive_divisor_hits"] += hit
                counters["two_pulse_eliminant_matches"] += verify_two_pulse_specialization(
                    compiled, heights
                )

                transcript.update(word_name.encode("ascii"))
                transcript.update(b"|")
                transcript.update(",".join(map(str, support)).encode("ascii"))
                transcript.update(b"|")
                transcript.update(",".join(map(str, heights)).encode("ascii"))
                transcript.update(b"\n")

    return {
        "claim": "L-8201",
        "status": "exact finite verification of the declared corpus; theorem remains PROPOSED",
        "scope": {
            "primitive_negative_cycles": [list(word) for word in NEGATIVE_CYCLES],
            "repetitions": {"cycle_1": [1, 5], "cycle_2": [1, 2]},
            "primitive_rotations": True,
            "maximum_support_size": 5,
            "small_height_grid": [1, 4],
            "large_support_structured_vectors": 38,
        },
        "counters": counters,
        "maximum_uniform_cap_bits": maximum_cap_bits,
        "transcript_sha256": transcript.hexdigest(),
        "samples": samples,
    }


def stable_json(payload: dict[str, object]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write-results", type=Path)
    group.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    rendered = stable_json(payload)

    target: Path = args.write_results or args.check_results
    if args.write_results:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8")
        print(f"wrote {target}")
    else:
        existing = target.read_text(encoding="utf-8")
        if existing != rendered:
            raise SystemExit(f"result mismatch: {target}")
        print(f"verified {target}")

    print(json.dumps(payload["counters"], sort_keys=True))
    print(f"transcript_sha256={payload['transcript_sha256']}")


if __name__ == "__main__":
    main()
