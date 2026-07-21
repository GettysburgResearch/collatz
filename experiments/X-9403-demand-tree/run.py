#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Any


def v2(n: int) -> int:
    if n == 0:
        raise ValueError('v2(0) undefined')
    n = abs(n)
    return (n & -n).bit_length() - 1


def demand_mod(m: int, j: int) -> int:
    mod = 64**j
    i81 = pow(81, -1, mod)
    return (17 * pow(i81, 9 * m + 2, mod) - i81) % mod


def supply_mod(x: int, m: int, j: int) -> int:
    mod = 64**j
    return (pow(81, 9 * m, mod) * (81 * x + 1)) % mod


def mismatch_mod(x: int, m: int, j: int) -> int:
    return (supply_mod(x, m, j) - demand_mod(m, j)) % (64**j)


def context_mod(m: int, j: int) -> int:
    mod = 64**j
    i81 = pow(81, -1, mod)
    return (
        17 * pow(i81, 18 * m + 3, mod)
        - pow(i81, 9 * m + 2, mod)
        - i81
    ) % mod


def lift_root(x: int, depth: int) -> list[int]:
    if depth < 1:
        raise ValueError('depth must be positive')
    roots = [m for m in range(4) if mismatch_mod(x, m, 1) == 0]
    assert len(roots) == 1
    out = [roots[0]]
    root = roots[0]
    for j in range(1, depth):
        period = 2 ** (6 * j - 4)
        candidates = [root + k * period for k in range(64)]
        roots = [m for m in candidates if mismatch_mod(x, m, j + 1) == 0]
        assert len(roots) == 1
        root = roots[0]
        out.append(root)
    return out


def demand_tree_checks() -> dict[str, Any]:
    full_depths: dict[str, Any] = {}
    total_classes = 0
    total_lift_children = 0
    for j in range(1, 4):
        period = 2 ** (6 * j - 4)
        values = [demand_mod(m, j) for m in range(period)]
        expected = set(range(0, 64**j, 16))
        assert set(values) == expected
        assert len(values) == len(set(values)) == period
        total_classes += period

        valuation_checks = 0
        if period <= 256:
            pairs = combinations(range(period), 2)
        else:
            sample = list(range(0, 512, 7)) + [period - 1 - k for k in range(128)]
            sample = sorted(set(m % period for m in sample))
            pairs = combinations(sample, 2)
        for m, n in pairs:
            diff = (demand_mod(n, j) - demand_mod(m, j)) % (64**j)
            assert diff != 0
            assert v2(diff) == 4 + v2(n - m)
            valuation_checks += 1

        full_depths[str(j)] = {
            'period': period,
            'image_size': len(values),
            'valuation_checks': valuation_checks,
        }

    lift_checks: dict[str, Any] = {}
    for j in (1, 2):
        parent_period = 2 ** (6 * j - 4)
        child_period = parent_period * 64
        parents_checked = 0
        for m0 in range(parent_period):
            parent = demand_mod(m0, j)
            children = [
                demand_mod(m0 + k * parent_period, j + 1) for k in range(64)
            ]
            assert len(set(children)) == 64
            assert {c % (64**j) for c in children} == {parent}
            assert set(children) == {
                parent + digit * (64**j) for digit in range(64)
            }
            parents_checked += 1
            total_lift_children += 64
        lift_checks[f'{j}_to_{j+1}'] = {
            'parents_checked': parents_checked,
            'children_per_parent': 64,
            'child_period': child_period,
        }

    return {
        'depths': full_depths,
        'lift_checks': lift_checks,
        'total_classes': total_classes,
        'total_lift_children': total_lift_children,
    }


def matching_tree_checks() -> dict[str, Any]:
    xs = [15 + 16 * k for k in range(32)]
    depth_checks: dict[str, Any] = {}
    total_pairs = 0
    for j in range(1, 4):
        period = 2 ** (6 * j - 4)
        contexts = [context_mod(m, j) for m in range(period)]
        expected_contexts = set(range(15, 64**j, 16))
        assert set(contexts) == expected_contexts
        assert len(contexts) == len(set(contexts)) == period

        roots_checked = 0
        for x in xs:
            xj = x % (64**j)
            roots = [m for m in range(period) if mismatch_mod(xj, m, j) == 0]
            assert len(roots) == 1
            m = roots[0]
            assert context_mod(m, j) == xj
            roots_checked += 1

        sample = list(range(min(period, 256)))
        valuation_checks = 0
        for m, n in combinations(sample, 2):
            dx = (context_mod(n, j) - context_mod(m, j)) % (64**j)
            assert dx != 0
            assert v2(dx) == 4 + v2(n - m)
            valuation_checks += 1
        total_pairs += valuation_checks
        depth_checks[str(j)] = {
            'period': period,
            'context_image_size': len(contexts),
            'roots_checked': roots_checked,
            'valuation_checks': valuation_checks,
        }

    selected = [15, 31, 47, 63, 79, 95, 111, 127]
    ghost_roots: dict[str, Any] = {}
    for x in selected:
        roots = lift_root(x, 8)
        assert all(roots[j] % (2 ** (6 * j - 4)) == roots[j - 1]
                   for j in range(1, len(roots)))
        ghost_roots[str(x)] = roots

    real_sign_checks = 0
    for m in range(128):
        x_real = (
            Fraction(17, 81 ** (18 * m + 3))
            - Fraction(1, 81 ** (9 * m + 2))
            - Fraction(1, 81)
        )
        assert x_real < 0
        real_sign_checks += 1

    return {
        'depths': depth_checks,
        'ghost_roots': ghost_roots,
        'positive_stage_real_sign_checks': real_sign_checks,
        'total_context_valuation_pairs': total_pairs,
    }


def schedule_novelty_checks() -> dict[str, Any]:
    words_checked = 0
    pair_checks = 0
    depths: dict[str, Any] = {}
    # Exhaust all 17/18 increment words of length 12. The theorem is more
    # general; this is a finite adversarial replay of the active alphabet.
    increment_words = list(product((17, 18), repeat=12))
    for j in (1, 2, 3):
        modulus = 2 ** (6 * j - 4)
        local_pairs = 0
        for increments in increment_words:
            mseq = [0]
            for inc in increments:
                mseq.append(mseq[-1] + inc)
            residues = [demand_mod(m, j) for m in mseq]
            for a, b in combinations(range(len(mseq)), 2):
                if 0 < mseq[b] - mseq[a] < modulus:
                    assert residues[a] != residues[b]
                    local_pairs += 1
            words_checked += 1
        depths[str(j)] = {
            'stage_modulus': modulus,
            'pair_checks': local_pairs,
            'guaranteed_window_for_C18': (modulus - 1) // 18 + 1,
        }
        pair_checks += local_pairs
    return {
        'increment_alphabet': [17, 18],
        'increment_word_length': 12,
        'words_per_depth': len(increment_words),
        'word_depth_runs': words_checked,
        'pair_checks': pair_checks,
        'depths': depths,
    }


def generate() -> dict[str, Any]:
    return {
        'schema_version': 1,
        'experiment_id': 'X-9403',
        'research_question': (
            'Do the exact stack demand and stationary supply-demand matching '
            'maps form scaled 2-adic tree isometries, and what finite residue '
            'novelty follows along 17/18 stage schedules?'
        ),
        'demand_tree': demand_tree_checks(),
        'stationary_matching_tree': matching_tree_checks(),
        'schedule_novelty': schedule_novelty_checks(),
        'interpretation': {
            'proved_by_finite_computation': [
                'the frozen demand permutations and lift tables',
                'the frozen stationary matching roots and inverse contexts',
                'the frozen 17/18 schedule novelty instances',
                'the frozen negative real sign cases',
            ],
            'not_proved_by_finite_computation': [
                'the universal isometry theorems',
                'nonexistence of an actively steered infinite stack tower',
                'nonexistence of an M1 witness or Collatz counterexample',
                'any independence claim between supply and demand streams',
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
    if args.check_results:
        if args.check_results.read_bytes() != data:
            raise SystemExit('canonical result mismatch')
    print(data.decode('utf-8'), end='')
    print(f'SHA256 {digest}')


if __name__ == '__main__':
    main()
