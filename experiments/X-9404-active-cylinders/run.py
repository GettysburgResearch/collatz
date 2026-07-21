#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path
from typing import Any


def params(m: int) -> tuple[int, int, int, int]:
    length = 9 * m + 1
    modulus = 64**length
    multiplier = 81**length
    constant = (modulus + 17) // 81
    return length, modulus, multiplier, constant


def edge(m: int, n: int) -> dict[str, int]:
    _, _, multiplier, _ = params(m)
    next_length, next_modulus, _, next_constant = params(n)
    base = 81 ** (9 * m)
    residue = (
        pow(multiplier, -1, next_modulus) * (next_constant - base)
    ) % next_modulus
    numerator = multiplier * residue + base - next_constant
    assert numerator % next_modulus == 0
    carry = numerator // next_modulus
    return {
        'r': residue,
        'k': carry,
        'M': next_modulus,
        'A': multiplier,
        'bits': 6 * next_length,
    }


def step(x: int, m: int, n: int) -> int | None:
    data = edge(m, n)
    output = data['A'] * x + 81 ** (9 * m)
    numerator = output - params(n)[3]
    if numerator % data['M']:
        return None
    return numerator // data['M']


def replay(x: int, schedule: tuple[int, ...]) -> tuple[bool, list[int]]:
    contexts = [x]
    for m, n in zip(schedule, schedule[1:]):
        nxt = step(x, m, n)
        if nxt is None:
            return False, contexts
        x = nxt
        contexts.append(x)
    return True, contexts


def cylinder(schedule: tuple[int, ...]) -> tuple[int, int, list[int]]:
    residue, modulus = 0, 1
    blocks: list[int] = []
    for i in range(len(schedule) - 2, -1, -1):
        m, n = schedule[i], schedule[i + 1]
        data = edge(m, n)
        quotient_residue = (
            pow(data['A'], -1, modulus) * (residue - data['k'])
        ) % modulus if modulus > 1 else 0
        residue = data['r'] + data['M'] * quotient_residue
        modulus = data['M'] * modulus
        assert 0 <= residue < modulus
        blocks.append(data['bits'])
    blocks.reverse()
    return residue, modulus, blocks


def finite_grid_checks() -> dict[str, Any]:
    schedules: list[tuple[int, ...]] = []
    for edges in range(1, 5):
        schedules.extend(
            tuple(schedule)
            for schedule in product(range(4), repeat=edges + 1)
        )

    cylinder_count = 0
    member_replays = 0
    perturbation_replays = 0
    quotient_pairs = 0
    maximum_bits = 0

    for schedule in schedules:
        residue, modulus, blocks = cylinder(schedule)
        bits = sum(blocks)
        assert modulus == 1 << bits
        maximum_bits = max(maximum_bits, bits)

        for tail in (0, 1, 2, 5):
            ok, _ = replay(residue + modulus * tail, schedule)
            assert ok
            member_replays += 1

        m, n = schedule[0], schedule[1]
        data = edge(m, n)
        for left, right in ((0, 1), (1, 7), (2, 18), (9, 25)):
            x_left = step(data['r'] + data['M'] * left, m, n)
            x_right = step(data['r'] + data['M'] * right, m, n)
            assert x_left == data['A'] * left + data['k']
            assert x_right == data['A'] * right + data['k']
            diff = abs(x_right - x_left)
            source_diff = abs(right - left)
            assert (diff & -diff) == (source_diff & -source_diff)
            quotient_pairs += 1

        if bits <= 700:
            exponents = range(bits)
        else:
            cumulative = 0
            selected = {0, bits - 1}
            for block in blocks:
                selected.update({cumulative, max(0, cumulative + block - 1)})
                cumulative += block
            exponents = sorted(exponent for exponent in selected if exponent < bits)

        for exponent in exponents:
            ok, _ = replay(residue + (1 << exponent), schedule)
            assert not ok
            perturbation_replays += 1

        cylinder_count += 1

    return {
        'schedules': cylinder_count,
        'member_replays': member_replays,
        'perturbation_replays': perturbation_replays,
        'quotient_isometry_pairs': quotient_pairs,
        'maximum_cylinder_bits': maximum_bits,
    }


def fibonacci_bits(length: int) -> tuple[int, ...]:
    word = '0'
    while len(word) < length:
        word = ''.join('01' if symbol == '0' else '0' for symbol in word)
    return tuple(int(symbol) for symbol in word[:length])


def balanced_schedule_checks() -> dict[str, Any]:
    directive = fibonacci_bits(24)
    heights = [1]
    for bit in directive:
        heights.append(heights[-1] + (17 if bit == 0 else 18))

    records: dict[str, Any] = {}
    previous_record_residue = 0
    previous_record_modulus = 1
    nonzero_blocks = 0

    for stages in (1, 2, 3, 4, 6, 8, 12, 16, 20, 24):
        schedule = tuple(heights[:stages + 1])
        residue, modulus, blocks = cylinder(schedule)
        if stages > 1 and previous_record_modulus != 1:
            assert residue % previous_record_modulus == previous_record_residue

        if stages > 1:
            prior_residue, prior_modulus, _ = cylinder(tuple(heights[:stages]))
            assert residue % prior_modulus == prior_residue
            new_block = (residue - prior_residue) // prior_modulus
            assert 0 <= new_block < params(heights[stages])[1]
            if new_block:
                nonzero_blocks += 1

        ok, _ = replay(residue, schedule)
        assert ok
        bits = modulus.bit_length() - 1
        lower = 54 * stages * heights[0] + 459 * stages * (stages + 1) + 6 * stages
        upper = 54 * stages * heights[0] + 486 * stages * (stages + 1) + 6 * stages
        assert lower <= bits <= upper

        records[str(stages)] = {
            'last_height': heights[stages],
            'cylinder_bits': bits,
            'least_representative_bit_length': residue.bit_length(),
            'least_representative_is_zero': residue == 0,
        }
        previous_record_residue = residue
        previous_record_modulus = modulus

    return {
        'directive': 'Fibonacci 0/1 mapped to increments 17/18',
        'prefix_records': records,
        'nonzero_new_blocks_at_recorded_depths': nonzero_blocks,
        'first_24_increments': [17 if bit == 0 else 18 for bit in directive],
    }


def uniqueness_small_checks() -> dict[str, Any]:
    cases: dict[str, Any] = {}
    contexts_scanned = 0
    for m, n in ((0, 0), (0, 1), (1, 0)):
        schedule = (m, n)
        residue, modulus, _ = cylinder(schedule)
        if modulus <= 64:
            good = []
            for context in range(modulus):
                ok, _ = replay(context, schedule)
                if ok:
                    good.append(context)
            assert good == [residue]
            contexts_scanned += modulus
            cases[f'{m}_to_{n}'] = {
                'modulus': modulus,
                'unique_residue': residue,
            }
    return {'cases': cases, 'contexts_scanned': contexts_scanned}


def generate() -> dict[str, Any]:
    return {
        'schema_version': 1,
        'experiment_id': 'X-9404',
        'research_question': (
            'Does active stack steering select exactly one initial residue '
            'cylinder, with odd-affine preservation of unused quotient precision?'
        ),
        'finite_grid': finite_grid_checks(),
        'balanced_schedule': balanced_schedule_checks(),
        'small_exhaustive_uniqueness': uniqueness_small_checks(),
        'interpretation': {
            'proved_by_finite_computation': [
                'the frozen edge residue/carry identities',
                'the frozen finite-cylinder membership and perturbation failures',
                'the frozen balanced-schedule nested cylinders and precision bounds',
            ],
            'not_proved_by_finite_computation': [
                'the universal active cylinder theorem',
                'nonstabilization for every infinite directive',
                'nonexistence of an ordinary M1 witness or Collatz counterexample',
            ],
        },
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + '\n').encode('utf-8')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-results', type=Path)
    parser.add_argument('--check-results', type=Path)
    args = parser.parse_args()

    payload = generate()
    data = canonical_bytes(payload)
    digest = hashlib.sha256(data).hexdigest()

    if args.write_results:
        args.write_results.parent.mkdir(parents=True, exist_ok=True)
        args.write_results.write_bytes(data)
    if args.check_results and args.check_results.read_bytes() != data:
        raise SystemExit('canonical result mismatch')

    print(data.decode('utf-8'), end='')
    print(f'SHA256 {digest}')


if __name__ == '__main__':
    main()
